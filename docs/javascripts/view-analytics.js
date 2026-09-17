/** Add anonymous GA4 page counts to each rendered documentation page. */

(() => {
  "use strict";

  const ELEMENT_ID = "view-analytics";
  const scriptUrl = document.currentScript?.src;
  const analyticsUrl = scriptUrl
    ? new URL("../assets/data/view-analytics.json", scriptUrl)
    : new URL("assets/data/view-analytics.json", document.baseURI);

  let analyticsPromise;

  function normalizePagePath(pathname) {
    let path = pathname.replace(/\/index\.html$/, "/");
    const finalSegment = path.split("/").at(-1);

    if (!path.endsWith("/") && !finalSegment?.includes(".")) {
      path += "/";
    }

    return path;
  }

  async function loadAnalytics() {
    if (!analyticsPromise) {
      analyticsPromise = fetch(analyticsUrl, { cache: "no-store" }).then(
        (response) => {
          if (!response.ok) {
            throw new Error(`Analytics request failed: ${response.status}`);
          }
          return response.json();
        },
      );
    }

    return analyticsPromise;
  }

  function getPageMetrics(analytics, pagePath) {
    return (
      analytics.pages?.[pagePath] ?? {
        unique_visitors: 0,
        page_views: 0,
      }
    );
  }

  function createAnalyticsElement(analytics, metrics) {
    const section = document.createElement("section");
    section.id = ELEMENT_ID;
    section.className = "view-analytics";
    section.setAttribute("aria-label", "Page activity for this academic block");

    const rule = document.createElement("hr");
    const summary = document.createElement("p");
    const label = document.createElement("strong");
    const period = document.createElement("small");

    label.textContent = "Page activity this academic block";
    summary.append(label, document.createElement("br"));
    summary.append(
      `${metrics.unique_visitors} unique visitors · `,
      `${metrics.page_views} page views · `,
      `approximately ${analytics.estimated_students} viewers`,
    );

    period.textContent =
      `Period: ${analytics.period_start} through ${analytics.period_end}.`;

    section.append(rule, summary, period);
    return section;
  }

  async function renderViewAnalytics() {
    const pagePath = normalizePagePath(window.location.pathname);

    try {
      const analytics = await loadAnalytics();

      if (pagePath !== normalizePagePath(window.location.pathname)) {
        return;
      }

      const content =
        document.querySelector(".md-content__inner") ??
        document.querySelector("article") ??
        document.querySelector("main");

      if (!content) {
        return;
      }

      document.getElementById(ELEMENT_ID)?.remove();
      const metrics = getPageMetrics(analytics, pagePath);
      content.append(createAnalyticsElement(analytics, metrics));
    } catch (error) {
      console.warn("Page analytics are temporarily unavailable.", error);
    }
  }

  const navigation = globalThis.document$;
  if (navigation && typeof navigation.subscribe === "function") {
    navigation.subscribe(() => {
      void renderViewAnalytics();
    });
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      void renderViewAnalytics();
    });
  } else {
    void renderViewAnalytics();
  }
})();
