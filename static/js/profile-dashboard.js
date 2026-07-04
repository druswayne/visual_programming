/**
 * Достижения в личном кабинете: фильтры и видимость групп.
 */
(function initAchievementsPanel() {
  const panel = document.querySelector("[data-achievements-panel]");
  if (!panel) return;

  const filters = panel.querySelectorAll("[data-ach-filter]");
  const cards = panel.querySelectorAll(".achievement-card");
  const groups = panel.querySelectorAll("[data-ach-group]");
  const emptyMsg = panel.querySelector("[data-achievements-empty]");

  const applyFilter = function (filterId) {
    let visibleCount = 0;

    cards.forEach(function (card) {
      const state = card.getAttribute("data-ach-filter-state");
      let show = filterId === "all";
      if (filterId === "unlocked") show = state === "unlocked";
      if (filterId === "progress") show = state === "progress";
      if (filterId === "locked") show = state === "locked";
      card.hidden = !show;
      if (show) visibleCount += 1;
    });

    groups.forEach(function (group) {
      const visibleInGroup = group.querySelectorAll(".achievement-card:not([hidden])");
      group.hidden = visibleInGroup.length === 0;
    });

    if (emptyMsg) {
      emptyMsg.hidden = visibleCount > 0;
    }
  };

  filters.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const filterId = btn.getAttribute("data-ach-filter");
      filters.forEach(function (b) {
        const active = b === btn;
        b.classList.toggle("is-active", active);
        b.setAttribute("aria-selected", active ? "true" : "false");
      });
      applyFilter(filterId);
    });
  });

  applyFilter("all");
})();
