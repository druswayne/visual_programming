/**
 * Кастомные выпадающие списки поверх нативного <select>.
 */
const CustomSelect = {
  _map: new WeakMap(),
  _open: null,

  enhance(select) {
    if (!select || select.dataset.cselectEnhanced) return null;
    select.dataset.cselectEnhanced = "1";
    select.classList.add("visually-hidden");
    select.tabIndex = -1;

    const wrap = document.createElement("div");
    wrap.className = "cselect";
    select.parentNode.insertBefore(wrap, select);
    wrap.appendChild(select);

    const trigger = document.createElement("button");
    trigger.type = "button";
    trigger.className = "cselect__trigger";

    const listId = (select.id || "cselect") + "-list";
    trigger.setAttribute("aria-haspopup", "listbox");
    trigger.setAttribute("aria-expanded", "false");
    trigger.setAttribute("aria-controls", listId);
    if (select.getAttribute("aria-label")) {
      trigger.setAttribute("aria-label", select.getAttribute("aria-label"));
    }

    const valueEl = document.createElement("span");
    valueEl.className = "cselect__value";
    const chevron = document.createElement("span");
    chevron.className = "cselect__chevron";
    chevron.setAttribute("aria-hidden", "true");
    trigger.append(valueEl, chevron);

    const menu = document.createElement("ul");
    menu.className = "cselect__menu";
    menu.id = listId;
    menu.setAttribute("role", "listbox");
    menu.hidden = true;

    wrap.insertBefore(trigger, select);
    wrap.insertBefore(menu, select);

    wrap.addEventListener("mousedown", function (e) {
      e.stopPropagation();
    });

    const inst = {
      select: select,
      wrap: wrap,
      trigger: trigger,
      valueEl: valueEl,
      menu: menu,
      highlight: -1,
    };
    this._map.set(select, inst);

    trigger.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      if (select.disabled) return;
      if (CustomSelect._open === inst) CustomSelect.close();
      else CustomSelect.open(inst);
    });

    trigger.addEventListener("keydown", function (e) {
      if (select.disabled) return;
      if (e.key === "ArrowDown" || e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        if (CustomSelect._open !== inst) CustomSelect.open(inst);
        else CustomSelect.moveHighlight(inst, 1);
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        if (CustomSelect._open !== inst) CustomSelect.open(inst);
        else CustomSelect.moveHighlight(inst, -1);
      } else if (e.key === "Escape") {
        CustomSelect.close();
      }
    });

    menu.addEventListener("click", function (e) {
      e.stopPropagation();
      const item = e.target.closest(".cselect__option");
      if (!item || item.classList.contains("is-disabled")) return;
      CustomSelect.choose(inst, item.dataset.value);
    });

    this.refresh(select);
    return inst;
  },

  refresh(select) {
    const inst = this._map.get(select);
    if (!inst) return;

    const menu = inst.menu;
    menu.innerHTML = "";
    const options = Array.from(select.options);

    options.forEach(function (opt) {
      const li = document.createElement("li");
      li.className = "cselect__option";
      li.dataset.value = opt.value;
      li.setAttribute("role", "option");
      li.textContent = opt.textContent;
      if (!opt.value) li.classList.add("is-placeholder");
      if (opt.disabled) li.classList.add("is-disabled");
      if (opt.value === select.value) {
        li.classList.add("is-selected");
        li.setAttribute("aria-selected", "true");
      } else {
        li.setAttribute("aria-selected", "false");
      }
      menu.appendChild(li);
    });

    this.syncDisplay(inst);
    inst.wrap.classList.toggle("is-disabled", select.disabled);
    inst.trigger.disabled = !!select.disabled;
  },

  syncDisplay(inst) {
    const select = inst.select;
    const opt = select.options[select.selectedIndex];
    const text = opt ? opt.textContent : "";
    const empty = !select.value;

    inst.valueEl.textContent = text;
    inst.valueEl.classList.toggle("is-placeholder", empty);
    inst.wrap.classList.toggle("has-value", !empty);
    inst.trigger.title = empty ? "" : text;
  },

  setDisabled(select, disabled) {
    select.disabled = disabled;
    const inst = this._map.get(select);
    if (!inst) return;
    inst.wrap.classList.toggle("is-disabled", disabled);
    inst.trigger.disabled = !!disabled;
    if (disabled) this.close(inst);
    this.syncDisplay(inst);
  },

  positionMenu(inst) {
    const menu = inst.menu;
    const rect = inst.trigger.getBoundingClientRect();
    const margin = 12;
    const gap = 6;

    menu.classList.add("cselect__menu--fixed");
    menu.style.top = rect.bottom + gap + "px";
    menu.style.minWidth = Math.max(rect.width, 160) + "px";

    const menuWidth = menu.offsetWidth || Math.max(rect.width, 200);
    let left = rect.left;

    if (left + menuWidth > window.innerWidth - margin) {
      left = rect.right - menuWidth;
    }
    left = Math.max(margin, Math.min(left, window.innerWidth - margin - menuWidth));
    menu.style.left = left + "px";
  },

  resetMenuPosition(inst) {
    inst.menu.classList.remove("cselect__menu--fixed");
    inst.menu.style.top = "";
    inst.menu.style.left = "";
    inst.menu.style.minWidth = "";
  },

  open(inst) {
    this.close();
    this._open = inst;
    inst.menu.hidden = false;
    inst.wrap.classList.add("is-open");
    inst.trigger.setAttribute("aria-expanded", "true");
    inst.highlight = this.getSelectedIndex(inst);
    this.applyHighlight(inst);
    this.positionMenu(inst);
  },

  close(inst) {
    const target = inst || this._open;
    if (!target) return;
    target.menu.hidden = true;
    target.wrap.classList.remove("is-open");
    target.trigger.setAttribute("aria-expanded", "false");
    target.highlight = -1;
    this.resetMenuPosition(target);
    if (this._open === target) this._open = null;
  },

  choose(inst, value) {
    inst.select.value = value;
    this.close(inst);
    this.refresh(inst.select);
    inst.select.dispatchEvent(new Event("change", { bubbles: true }));
  },

  getSelectedIndex(inst) {
    const items = inst.menu.querySelectorAll(".cselect__option:not(.is-disabled)");
    for (let i = 0; i < items.length; i++) {
      if (items[i].dataset.value === inst.select.value) return i;
    }
    return 0;
  },

  moveHighlight(inst, delta) {
    const items = inst.menu.querySelectorAll(".cselect__option:not(.is-disabled)");
    if (!items.length) return;
    let next = inst.highlight + delta;
    if (next < 0) next = items.length - 1;
    if (next >= items.length) next = 0;
    inst.highlight = next;
    this.applyHighlight(inst);
    items[next].scrollIntoView({ block: "nearest" });
  },

  applyHighlight(inst) {
    const selectable = inst.menu.querySelectorAll(".cselect__option:not(.is-disabled)");
    inst.menu.querySelectorAll(".cselect__option").forEach(function (li) {
      li.classList.remove("is-highlighted");
    });
    if (inst.highlight >= 0 && selectable[inst.highlight]) {
      selectable[inst.highlight].classList.add("is-highlighted");
    }
  },
};

document.addEventListener("click", function () {
  CustomSelect.close();
});

document.addEventListener("keydown", function (e) {
  if (e.key !== "Escape") return;
  CustomSelect.close();
});

window.addEventListener("resize", function () {
  if (CustomSelect._open) {
    CustomSelect.positionMenu(CustomSelect._open);
  }
});

document.addEventListener("keydown", function (e) {
  const inst = CustomSelect._open;
  if (!inst) return;
  if (e.key === "ArrowDown") {
    e.preventDefault();
    CustomSelect.moveHighlight(inst, 1);
  } else if (e.key === "ArrowUp") {
    e.preventDefault();
    CustomSelect.moveHighlight(inst, -1);
  } else if (e.key === "Enter") {
    e.preventDefault();
    const items = inst.menu.querySelectorAll(".cselect__option:not(.is-disabled)");
    const item = items[inst.highlight];
    if (item) CustomSelect.choose(inst, item.dataset.value);
  }
});
