# Set Up the Guide Assistant

> Enable an **Ask the agent** button on documentation pages.

The browser sends a question and the current page text to a Cloudflare
Worker.
The Worker calls Google Gemini and returns an answer.

The Gemini API key is stored as a Cloudflare secret.

## Task 1. Create or Use Existing Google Cloud Project

Use the `github-pages-analytics` project created during Google Analytics
setup.
Or follow the instructions there to create a new cloud project.

The two integrations use different credentials:

- **Google Analytics:** GitHub Actions authenticates through Workload
  Identity Federation using the `ga4-reader` service account.
- **Gemini assistant:** The Cloudflare Worker authenticates using a
  Gemini API key stored in its `GEMINI_API_KEY` secret.

Keep the existing Google Analytics configuration unchanged.

## Task 2. Import the Existing Project into Google AI Studio

1. Open [Google AI Studio](https://aistudio.google.com/).
2. Sign in with the Google account that owns `github-pages-analytics`.
3. Accept the terms if prompted.
4. Optional / not needed: In the left panel, open **Dashboard**, **Projects**.
5. If `github-pages-analytics` already appears, continue to the next section.
6. Otherwise, click **Import projects**.
7. Search for `github-pages-analytics`.
8. Select the project and click **Import**.

## Task 3. Create the Gemini API Key

1. Open the [AI Studio API Keys page](https://aistudio.google.com/apikey).
2. Click **Create API key**.
3. Select `github-pages-analytics` as the project.
4. If asked for a key name, enter one. I used `pro-analytics-02-worker`.
5. Finish creating the key.
6. Copy the generated API key to your clipboard.

Store this API key in Cloudflare as `GEMINI_API_KEY` during the Worker setup.
The API key is a secret.
Do not put it in GitHub repository variables or source files.

## Task 4. Set Up the Assistant in Cloudflare

Complete these steps in the Cloudflare website.
Existing Cloudflare domains and DNS settings do not change.

Cloudflare hosts only the assistant Worker,
using a Cloudflare-provided `workers.dev` address.

### 1. Open Workers & Pages

1. Sign in to [Cloudflare](https://dash.cloudflare.com/).
2. Select the Cloudflare account that will own the assistant.
3. Stay at the account level. Do not select a domain.
4. In the sidebar, open **Build** / **Compute** / **Workers & Pages**.

### 2. Create the Worker

1. Click **Create application**.
2. Select **Start with Hello World!**.
3. Enter this Worker name (or similar for your site):

   ```text
   pro-analytics-02-assistant.denisecase.workers.dev
   ```

4. Click **Deploy**.
5. Open the newly created Worker.

If Cloudflare asks you to choose an account subdomain for `workers.dev`,
choose an available name.
If your account already has one, use it.

My Worker address has this form:

```text
https://pro-analytics-02-assistant.denisecase.workers.dev/
```

### 3. Add the Configuration Variables

In Cloudflare / your account / Workers & Pages / pro-analytics-02-assistant (or your worker):

1. Within `pro-analytics-02-assistant`, open **Settings** in the top menu.
2. Find **Runtime variables and secrets**.
3. Click **Add variable**.
4. Enter the variable name and value from the table below (without back tics).
5. Use **Add variable** to add the remaining rows, or save and repeat.
6. Click **Deploy** to apply the changes.

| Type | Variable Key         | Value                                                                      |
| ---- | -------------------- | -------------------------------------------------------------------------- |
| Text | `GEMINI_MODEL`       | `gemini-2.5-flash`                                                         |
| Text | `ALLOWED_ORIGINS`    | `https://denisecase.github.io,http://localhost:8000,http://127.0.0.1:8000` |
| Text | `MAX_QUESTION_CHARS` | `1000`                                                                     |
| Text | `MAX_CONTEXT_CHARS`  | `20000`                                                                    |
| Text | `DAILY_CALLS_PER_IP` | `50`                                                                       |

Enter values without surrounding quotation or tic marks.

`ALLOWED_ORIGINS` identifies the websites allowed by the Worker's browser-origin check.
Do not append `/pro-analytics-02/` to that origin.

### 4. Store the Gemini API Key

Have the Gemini API key from Google AI Studio ready.

1. Remain in the Worker's **Settings / Runtime variables**.
2. Click **Add**.
3. Click the **Secret** box.
4. For **Variable key**, enter: `GEMINI_API_KEY`
5. For **Value**, paste the Gemini API key.
6. Click **Add 1 variable and Deploy**.

Confirm that `GEMINI_API_KEY` appears as a secret.
Cloudflare hides its saved value.

This dashboard step stores the secret used by `env.GEMINI_API_KEY`.

### 5. Replace the Example Code

1. Open the Worker's **Overview** tab.
2. Click **Edit code** in the upper right.
3. Select the JavaScript entry file containing the Hello World example.
4. Replace its contents with the complete contents of your repository's
   `worker/src/index.js`.
5. Paste only JavaScript. Do not paste `wrangler.toml` into the editor.
6. Click **Deploy**.

The dashboard does not read the local `wrangler.toml`.
The variables entered above provide the corresponding settings.

### 6. Enable the Optional Daily Request Counter

The current Worker uses a KV namespace to store request counts.
Without this binding, it skips the daily counter.

Create the storage:

1. Return to the Cloudflare account-level sidebar.
2. Open **Build** / **Storage & Databases / Workers KV**.
3. Click **Create a KV namespace**.
4. Enter the namespace name: pro-analytics-02-assistant-rate
5. Click **Create**.

Connect the storage to the Worker:

1. Return to **Build** / **Compute** / **Workers & Pages**.
2. Open `pro-analytics-02-assistant`.
3. Select the **Bindings** tab.
4. Click **Add binding**.
5. Select **KV namespace**, then **Add binding**.
6. For **Variable name**, enter exactly:

   ```text
   RATE
   ```

7. From the namespace dropdown, select
   `pro-analytics-02-assistant-rate`.
8. Click **Add binding** to apply it.

The binding name must be `RATE` because the Worker uses `env.RATE`.

No initial keys or values need to be entered.
The Worker creates them when requests arrive.

This counter is approximate and shared by people using the same public
IP address.

### 7. Copy the Worker Endpoint

1. Back on the **Workers & Pages** for pro-analytics-02-assistant.
2. Go to the **Overview** tab.
3. Find its `workers.dev` address.
4. Confirm that the address is enabled.
5. Copy the full address, including `https://`.

Use the production address in this form:

```text
https://pro-analytics-02-assistant.denisecase.workers.dev
```

Do not add a custom domain or route for GitHub Pages.

### 8. Verify That the Worker Is Running

Open the copied Worker URL in a browser tab.

With your assistant code deployed, the expected response is:

```json
{ "error": "POST only" }
```

This is expected because opening a URL sends a GET request,
while the assistant accepts POST requests.

If you see `Hello World!`, the example code is still deployed.
Repeat the code replacement step.

This check confirms that the Worker is reachable.
The complete Gemini request is tested after connecting the documentation.

### 9. Connect the Documentation on Your Machine

This step takes place in VS Code.

1. Open `docs/javascripts/ai-assistant.js`.
2. Find `WORKER_URL`.
3. Replace the address with the exact URL copied from Cloudflare.
4. Save the file.
5. Commit and push the change.
6. Wait for the documentation deployment to finish.
7. Open a documentation page.
8. Click **Ask the agent** and submit a question about that page.
9. Confirm that an answer appears.

## Local Deployment with Wrangler

The dashboard steps above deploy the Worker without requiring Node.js
on your machine.

To run locally, install the current Node.js LTS release, which includes npm.
In VS Code, open a PowerShell terminal at the repository root.

Check the installation:

```powershell
node --version
npm --version
```

Before using Wrangler for later deployments, ensure that
`worker/wrangler.toml` contains the same variables and the actual KV
namespace ID.
Wrangler deployments use that file to configure the Worker.

Change to the Worker directory and sign in:

```powershell
Set-Location worker
npx wrangler@latest login
```

Complete the Cloudflare sign-in in the browser.
Run the remaining Wrangler commands from the worker directory.

In wrangler.toml, set the model:

```toml
GEMINI_MODEL = "gemini-2.5-flash"
```

Set the allowed browser origins:

```toml
ALLOWED_ORIGINS = "https://denisecase.github.io,http://localhost:8000,http://127.0.0.1:8000"
```

An origin includes the scheme, hostname, and port when applicable.
It does not include the repository path or a trailing slash.

The browser calls the Worker URL.
The Worker constructs the Google Gemini API URL internally.

Create the KV namespace:

```powershell
npx wrangler@latest kv namespace create RATE
```

Copy its returned ID into wrangler.toml:

```toml
[[kv_namespaces]]
binding = "RATE"
id = "REPLACE_WITH_RETURNED_ID"
```

The Worker uses DAILY_CALLS_PER_IP as an approximate daily request limit.
People sharing a public IP address share this allowance. Concurrent
requests may exceed the counter because KV updates are not atomic.
Without the RATE binding, the Worker skips this counter.

Deploy the Worker:

```powershell
npx wrangler@latest deploy
```

If prompted, register a workers.dev subdomain.
Copy the HTTPS Worker URL printed by Wrangler.
Store the Gemini API key:

```powershell
npx wrangler@latest secret put GEMINI_API_KEY
```

Paste the key at the secret prompt.
The endpoint is ready for testing after the secret has been stored.

In docs/javascripts/ai-assistant.js, replace WORKER_URL with the exact
Worker URL printed during deployment.

In zensical.toml, add this entry to the existing extra_javascript array
under [project]:

```toml
"javascripts/ai-assistant.js",
```

Preserve the existing JavaScript entries.
Deploy the documentation using the existing documentation workflow.

Open a published documentation page and refresh it.
Select **Ask the agent**.
Ask a question answered on that page.
Confirm that an answer appears.
Navigate to another documentation page and repeat.
Each question is independent. The assistant receives the current page
text, up to the configured context limit, without previous questions
or answers.

### Troubleshooting

- No button: confirm that the JavaScript entry is present and the
  documentation deployment succeeded.
- Endpoint not configured: replace denisecase in WORKER_URL.
- Origin not allowed: add the exact browser origin to ALLOWED_ORIGINS
  and redeploy the Worker.
- Model request failed: confirm the API key, model availability, and
  quota in Google AI Studio.
- Daily limit reached: wait until the next UTC day or adjust
  DAILY_CALLS_PER_IP and redeploy.
- Network error: confirm the Worker URL and inspect the browser
  Network panel for CORS or connection errors.

Opening the Worker URL directly in a browser returns POST only.
This is expected: the assistant sends POST requests.

After changing Worker code or wrangler.toml, redeploy from worker:

```powershell
npx wrangler@latest deploy
```

Documentation deployment and Worker deployment are separate operations.

## Scope

This implementation answers questions using the current page.
It does not search the whole guide or store questions and answers.
CORS restricts browser access but does not authenticate callers.
System instructions guide responses but do not prevent all misuse.

## References

- [Gemini API keys](https://aistudio.google.com/apikey)
- [Gemini model availability](https://ai.google.dev/gemini-api/docs/models)
- [Gemini pricing and free tiers](https://ai.google.dev/gemini-api/docs/pricing)
- [Wrangler commands](https://developers.cloudflare.com/workers/wrangler/commands/)
