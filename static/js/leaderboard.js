/** Переключение фильтров рейтинга без сброса прокрутки. */
(function () {
  "use strict";

  const PAGE = ".leaderboard-page";
  let inflight = 0;

  function boardUrl(url) {
    const parsed = new URL(url, window.location.origin);
    parsed.hash = "";
    return parsed.pathname + parsed.search;
  }

  function samePath(url) {
    try {
      return new URL(url, window.location.origin).pathname === window.location.pathname;
    } catch (err) {
      return false;
    }
  }

  async function load(url, push) {
    const current = document.querySelector(PAGE);
    if (!current) return;
    const requestId = ++inflight;
    current.classList.add("is-loading");
    const y = window.scrollY;
    try {
      const response = await fetch(url, {
        headers: { "X-Requested-With": "fetch", Accept: "text/html" },
      });
      if (!response.ok) throw new Error("status");
      const html = await response.text();
      if (requestId !== inflight) return;
      const doc = new DOMParser().parseFromString(html, "text/html");
      const incoming = doc.querySelector(PAGE);
      if (!incoming) throw new Error("board");
      current.replaceWith(incoming);
      if (push) history.pushState({ pyblocksLeaderboard: true }, "", boardUrl(url));
      const title = doc.querySelector("title");
      if (title) document.title = title.textContent;
      window.scrollTo(0, y);
    } catch (err) {
      window.location.assign(url);
    }
  }

  document.addEventListener("click", function (event) {
    const link = event.target.closest("a.lb-tab");
    if (!link || !document.querySelector(PAGE)) return;
    if (event.defaultPrevented || event.button !== 0) return;
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    if (link.target === "_blank") return;
    if (!samePath(link.href)) return;
    event.preventDefault();
    if (boardUrl(link.href) === boardUrl(window.location.href)) return;
    load(link.href, true);
  });

  window.addEventListener("popstate", function () {
    if (!document.querySelector(PAGE)) return;
    load(window.location.href, false);
  });
})();
