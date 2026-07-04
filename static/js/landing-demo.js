/**
 * Демо на главной: настоящие Blockly-блоки + анимация кода и результата.
 */
(function () {
  function initHeroScrollDown() {
    const btn = document.getElementById("heroScrollDown");
    const target = document.getElementById("how-it-works");
    if (!btn || !target) return;

    const desktopMq = window.matchMedia("(min-width: 1024px)");

    function scrollToContent() {
      const heading = target.querySelector(".section-title") || target;
      const topGap = 40;
      const scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop ||
        0;
      const y = heading.getBoundingClientRect().top + scrollTop - topGap;
      window.scrollTo({ top: Math.max(0, y), behavior: "smooth" });
    }

    btn.addEventListener("click", scrollToContent);

    function syncVisibility() {
      if (!desktopMq.matches) {
        btn.classList.add("is-hidden");
        return;
      }
      const hero = document.querySelector(".hero--landing");
      if (!hero) return;
      const heroBottom = hero.getBoundingClientRect().bottom;
      const hide = heroBottom < window.innerHeight * 0.55;
      btn.classList.toggle("is-hidden", hide);
    }

    window.addEventListener("scroll", syncVisibility, { passive: true });
    if (typeof desktopMq.addEventListener === "function") {
      desktopMq.addEventListener("change", syncVisibility);
    } else if (typeof desktopMq.addListener === "function") {
      desktopMq.addListener(syncVisibility);
    }
    syncVisibility();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initHeroScrollDown);
  } else {
    initHeroScrollDown();
  }

  if (typeof Blockly === "undefined") return;

  const pyblocksTheme = Blockly.Theme.defineTheme("pyblocks", {
    base: Blockly.Themes.Classic,
    fontStyle: {
      family: "Segoe UI, system-ui, sans-serif",
      weight: "600",
      size: 11,
    },
    blockStyles: {
      program_start_blocks: {
        colourPrimary: "#22c55e",
        colourSecondary: "#16a34a",
        colourTertiary: "#14532d",
        hat: "cap",
      },
      program_end_blocks: {
        colourPrimary: "#f97316",
        colourSecondary: "#ea580c",
        colourTertiary: "#9a3412",
      },
    },
    componentStyles: {
      workspaceBackgroundColour: "#111827",
    },
  });

  window.pyblocksTheme = pyblocksTheme;

  function mountHeroPreview() {
    if (typeof GuidePreview === "undefined") return;

    const main = document.getElementById("landingBlocksPreview");
    if (main && window.LANDING_DEMO_XML) {
      GuidePreview.mount(main, window.LANDING_DEMO_XML);

      if (typeof ResizeObserver !== "undefined") {
        const observer = new ResizeObserver(function () {
          GuidePreview.resizeContainer(main);
        });
        observer.observe(main);
        const col = main.closest(".landing-demo__col--blocks");
        if (col) observer.observe(col);
      }

      window.addEventListener("load", function () {
        GuidePreview.resizeContainer(main);
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mountHeroPreview);
  } else {
    mountHeroPreview();
  }

  const demo = document.getElementById("landingDemo");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (demo) {
    if (reducedMotion) {
      demo.classList.add("is-static");
    } else {
      demo.classList.add("is-animating");
      restartDemoLoop(demo);
    }
  }

  function restartDemoLoop(el) {
    const cycleMs = 12000;
    const badge = el.querySelector(".demo-output-badge");

    function runCycle() {
      el.classList.remove("is-animating");
      if (badge) badge.textContent = "Выполняется…";
      void el.offsetWidth;
      el.classList.add("is-animating");
      window.setTimeout(function () {
        if (badge) badge.textContent = "Готово";
      }, 7600);
    }

    runCycle();
    window.setInterval(runCycle, cycleMs);
  }

  const reveals = document.querySelectorAll(".reveal");
  if (!reveals.length) return;

  if (reducedMotion || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) {
      el.classList.add("is-visible");
    });
    return;
  }

  const observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
  );

  reveals.forEach(function (el) {
    observer.observe(el);
  });
})();
