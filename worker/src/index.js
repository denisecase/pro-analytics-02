/**
 * Welcome to Cloudflare Workers! This is your first worker.
 *
 * - Run "npm run dev" in your terminal to start a development server
 * - Open a browser tab at http://localhost:8787/ to see your worker in action
 * - Run "npm run deploy" to publish your worker
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */

// ============================================================
// worker/src/index.js
// ============================================================
// Assistant proxy for the "Pro Analytics 02" guide.
//
// WHAT: ai-assistant.js POSTs { question, context } here; the worker asks
//       Gemini and returns { answer }.
// WHY:  A public static site cannot hold an API key; anything shipped to
//       the browser is scraped. The key lives here as a secret. The system
//       instruction and guardrails also live here.
//
// Expects (see wrangler.toml):
//   secret GEMINI_API_KEY       AI Studio key (free, no credit card)
//   var    GEMINI_MODEL         free-tier Flash model id
//   var    ALLOWED_ORIGINS      comma-separated CORS/403 allowlist
//   var    MAX_QUESTION_CHARS   cap on the question (default 1000)
//   var    MAX_CONTEXT_CHARS    cap on the context (default 20000)
//   var    DAILY_CALLS_PER_IP   per-IP daily cap (default 50)
//   kv     RATE                 optional; without it the per-IP cap is skipped
//
// Request:  POST { "question": "...", "context": "..." }
// Response: 200 { "answer": "..." }  |  4xx/5xx { "error": "..." }
// ============================================================

const SYSTEM_INSTRUCTION = `You are the assistant for the "Pro Analytics 02" Professional Python guide.
Answer the question using ONLY the provided documentation context.
If the context does not cover it,
say so plainly and point to https://denisecase.github.io/pro-analytics-02/ .
Be concise and practical. Ask their operating system. Note we use uv, ruff, and ty.
Assume the reader may be new to Python and the terminal.`;

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const cors = corsHeaders(origin, env);

    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    if (request.method !== "POST") return json({ error: "POST only" }, 405, cors);
    if (!originAllowed(origin, env)) return json({ error: "origin not allowed" }, 403, cors);

    let body;
    try {
      body = await request.json();
    } catch {
      return json({ error: "invalid JSON" }, 400, cors);
    }

    const question = String(body.question || "").trim();
    const context = String(body.context || "").trim();
    if (!question) return json({ error: "question is required" }, 400, cors);

    // Length caps protect the free-tier token budget from a public endpoint.
    const maxQ = parseInt(env.MAX_QUESTION_CHARS || "1000", 10);
    const maxC = parseInt(env.MAX_CONTEXT_CHARS || "20000", 10);
    if (question.length > maxQ) return json({ error: "question too long" }, 413, cors);
    const clippedContext = context.slice(0, maxC);

    // Optional per-IP daily cap (needs the RATE KV binding).
    if (env.RATE) {
      const cap = parseInt(env.DAILY_CALLS_PER_IP || "50", 10);
      const ip = request.headers.get("CF-Connecting-IP") || "anon";
      const key = `rl:${ip}:${todayUTC()}`;
      const used = parseInt((await env.RATE.get(key)) || "0", 10);
      if (used >= cap) return json({ error: "daily limit reached" }, 429, cors);
      await env.RATE.put(key, String(used + 1), { expirationTtl: 172800 }); // ~2 days
    }

    const model = env.GEMINI_MODEL || "gemini-3.6-flash";
    const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`;
    const payload = {
      systemInstruction: { parts: [{ text: SYSTEM_INSTRUCTION }] },
      contents: [
        {
          role: "user",
          parts: [
            {
              text: `Context from the documentation:\n${clippedContext || "(none provided)"}\n\nQuestion: ${question}`,
            },
          ],
        },
      ],
      generationConfig: { temperature: 0.2, maxOutputTokens: 800 },
    };

    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-goog-api-key": env.GEMINI_API_KEY,
        },
        body: JSON.stringify(payload),
      });
      if (!res.ok) {
        const detail = await res.text();
        console.error("Gemini request failed:", res.status, detail);

        return json(
          {
            error: "model request failed",
            status: res.status,
          },
          502,
          cors
        );
      }
      const data = await res.json();
      const answer =
        (data.candidates?.[0]?.content?.parts || []).map((p) => p.text || "").join("").trim();
      if (!answer) return json({ error: "empty response", detail: data.promptFeedback ?? null }, 502, cors);
      return json({ answer }, 200, cors);
    } catch (err) {
      return json({ error: "upstream failure", detail: String(err) }, 502, cors);
    }
  },
};

// ------------------------------------------------------------
// Helpers
// ------------------------------------------------------------

function allowedOrigins(env) {
  return (env.ALLOWED_ORIGINS || "")
    .split(",")
    .map((s) => s.trim())
    .filter(Boolean);
}

function originAllowed(origin, env) {
  const list = allowedOrigins(env);
  return list.length === 0 || list.includes(origin);
}

function corsHeaders(origin, env) {
  const allow = originAllowed(origin, env) ? origin || "*" : allowedOrigins(env)[0] || "*";
  return {
    "Access-Control-Allow-Origin": allow,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    Vary: "Origin",
  };
}

function json(obj, status, cors) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { ...cors, "Content-Type": "application/json" },
  });
}

function todayUTC() {
  return new Date().toISOString().slice(0, 10);
}
