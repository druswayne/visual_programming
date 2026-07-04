/**
 * Панель категорий блоков — инженерный стиль (Blueprint / Blender).
 * Blockly монтируется в #blocklyShell; flyout позиционирует Blockly (не переносим DOM).
 */
const ScratchToolbox = {
  activeIndex: 0,

  categoryStyle: {
    basics: { color: "#4A6278", icon: "▷" },
    variables: { color: "#4A5A82", icon: "x" },
    math: { color: "#4A6B52", icon: "+" },
    text: { color: "#5A5278", icon: "T" },
    logic: { color: "#4A6878", icon: "&" },
    conditions: { color: "#8B7340", icon: "?" },
    loops: { color: "#8B7340", icon: "↻" },
    lists: { color: "#6B5278", icon: "[]" },
    functions: { color: "#7A5260", icon: "f" },
    types: { color: "#3A6B6B", icon: "τ" },
  },

  init(workspace) {
    this.workspace = workspace;
    this.toolbox = workspace.getToolbox();
    if (!this.toolbox) return;

    this.shell = document.getElementById("blocklyShell");
    this.categoriesEl = document.getElementById("scratchCategories");
    this.paletteTitleEl = document.getElementById("scratchPaletteTitle");
    if (!this.categoriesEl) return;

    this.buildCategoryRail();
    this.setupPersistentFlyout();
    this.patchFlyoutFixedWidth();
    this.patchToolboxRefresh();
    this.setupVariableChangeGuard();
    this.hideNativeToolbox();
    this.setupFlyoutDragRefresh();
    this.selectCategory(0);
  },

  setupPersistentFlyout() {
    const flyout = this.toolbox.getFlyout && this.toolbox.getFlyout();
    if (!flyout) return;

    if (typeof flyout.setAutoClose === "function") {
      flyout.setAutoClose(false);
    } else {
      flyout.autoClose = false;
    }

    if (typeof flyout.setRecycleBlocks === "function") {
      flyout.setRecycleBlocks(true);
    }
  },

  /**
   * Blockly по умолчанию подстраивает ширину flyout под содержимое и сдвигает
   * рабочую область (translate). У нас ширина задаётся CSS (--palette-width).
   */
  patchFlyoutFixedWidth() {
    const flyout = this.toolbox.getFlyout && this.toolbox.getFlyout();
    if (!flyout || flyout._pyblocksFixedWidthPatched) return;

    const self = this;
    flyout._pyblocksFixedWidthPatched = true;

    flyout.reflowInternal_ = function () {
      const fixedWidth = self.getPaletteWidth();
      this.workspace_.scale = this.getFlyoutScale();

      if (this.getWidth() === fixedWidth) return;

      if (this.RTL) {
        for (const item of this.getContents()) {
          const rect = item.getElement().getBoundingRectangle();
          const targetLeft =
            fixedWidth / this.workspace_.scale - rect.getWidth() - this.MARGIN - this.tabWidth_;
          item.getElement().moveBy(targetLeft - rect.left, 0);
        }
      }

      this.width_ = fixedWidth;
      this.position();
      if (this.targetWorkspace) {
        this.targetWorkspace.resizeContents();
        this.targetWorkspace.recordDragTargets();
      }
      self.applyFixedFlyoutWidth(fixedWidth);
    };
  },

  patchToolboxRefresh() {
    if (!this.toolbox || this.toolbox._pyblocksRefreshPatched) return;

    const self = this;
    const originalRefresh = this.toolbox.refreshSelection.bind(this.toolbox);
    this.toolbox._pyblocksRefreshPatched = true;

    this.toolbox.refreshSelection = function () {
      originalRefresh();
      self.applyFixedFlyoutWidth(self.getPaletteWidth());
    };
  },

  setupVariableChangeGuard() {
    const varEvents = new Set([
      Blockly.Events.VAR_CREATE,
      Blockly.Events.VAR_DELETE,
      Blockly.Events.VAR_RENAME,
      Blockly.Events.VAR_TYPE_CHANGE,
    ]);

    this.workspace.addChangeListener((event) => {
      if (!varEvents.has(event.type)) return;
      if (event.workspaceId !== this.workspace.id) return;

      const width = this.getPaletteWidth();
      this.applyFixedFlyoutWidth(width);
      requestAnimationFrame(() => {
        this.applyFixedFlyoutWidth(width);
      });
    });
  },

  isInteractionBlocked() {
    const ws = this.workspace;
    if (!ws) return false;
    if (typeof ws.isDragging === "function" && ws.isDragging()) return true;
    if (ws.currentGesture_) return true;
    return false;
  },

  setupFlyoutDragRefresh() {
    const flyout = this.toolbox.getFlyout && this.toolbox.getFlyout();
    const flyoutWorkspace =
      flyout && flyout.getWorkspace ? flyout.getWorkspace() : flyout && flyout.workspace_;

    this.flyoutWorkspaceId = flyoutWorkspace && flyoutWorkspace.id;

    this.workspace.addChangeListener((event) => {
      if (this._flyoutRefreshing) return;

      const isFlyoutDelete =
        this.flyoutWorkspaceId &&
        event.type === Blockly.Events.BLOCK_DELETE &&
        event.workspaceId === this.flyoutWorkspaceId;

      const isDragEnd =
        event.type === Blockly.Events.BLOCK_DRAG &&
        event.isStart === false &&
        (event.workspaceId === this.workspace.id ||
          event.workspaceId === this.flyoutWorkspaceId);

      if (isFlyoutDelete || isDragEnd) {
        this.debouncedRefreshActiveCategory();
      }
    });
  },

  debouncedRefreshActiveCategory() {
    clearTimeout(this._refreshTimer);
    this._refreshTimer = setTimeout(() => {
      if (this.isInteractionBlocked()) {
        this.debouncedRefreshActiveCategory();
        return;
      }
      this.refreshActiveCategory();
    }, 120);
  },

  refreshActiveCategory() {
    if (this.activeIndex < 0 || this._flyoutRefreshing) return;
    if (this.isInteractionBlocked()) {
      this.debouncedRefreshActiveCategory();
      return;
    }

    this._flyoutRefreshing = true;

    const flyout = this.toolbox.getFlyout && this.toolbox.getFlyout();
    const flyoutWorkspace = flyout && flyout.getWorkspace ? flyout.getWorkspace() : null;
    const needsRefill =
      flyoutWorkspace &&
      flyoutWorkspace.getAllBlocks(false).length === 0 &&
      this.toolbox.getToolboxItems &&
      this.toolbox.getToolboxItems()[this.activeIndex];

    if (needsRefill) {
      this.toolbox.selectItemByPosition(this.activeIndex);
    } else {
      this.syncFlyoutLayout();
    }

    requestAnimationFrame(() => {
      this.hideNativeToolbox();
      this.applyFixedFlyoutWidth(this.getPaletteWidth());
      this._flyoutRefreshing = false;
    });
  },

  hideNativeToolbox() {
    document
      .querySelectorAll(".blocklyTreeRoot, .blocklyToolboxCategory, .blocklyToolboxCategoryGroup, .blocklyTreeRow")
      .forEach(function (el) {
        el.style.display = "none";
      });
  },

  getPaletteWidth() {
    if (!this.shell) return 242;
    const raw = getComputedStyle(this.shell).getPropertyValue("--palette-width").trim();
    const n = parseInt(raw, 10);
    return Number.isFinite(n) ? n : 242;
  },

  getStyle(cat) {
    return (
      this.categoryStyle[cat.catKey] || {
        color: this.hueToColor(cat.colour || "210"),
        icon: cat.name.charAt(0),
      }
    );
  },

  hueToColor(hue) {
    return "hsl(" + hue + ", 65%, 52%)";
  },

  buildCategoryRail() {
    this.categoriesEl.innerHTML = "";
    (PYBLOCKS_TOOLBOX.contents || []).forEach((cat, index) => {
      const style = this.getStyle(cat);
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "scratch-cat";
      btn.dataset.index = String(index);
      btn.title = cat.name;
      btn.style.setProperty("--cat-color", style.color);
      btn.innerHTML =
        '<span class="scratch-cat__icon">' + style.icon + "</span>" +
        '<span class="scratch-cat__label">' + cat.name + "</span>";
      btn.addEventListener("click", () => this.selectCategory(index));
      this.categoriesEl.appendChild(btn);
    });
  },

  selectCategory(index) {
    const categories = PYBLOCKS_TOOLBOX.contents || [];
    if (index < 0 || index >= categories.length) return;

    this.activeIndex = index;
    const cat = categories[index];
    const style = this.getStyle(cat);

    this.categoriesEl.querySelectorAll(".scratch-cat").forEach((btn, i) => {
      btn.classList.toggle("is-active", i === index);
    });

    if (this.paletteTitleEl) {
      this.paletteTitleEl.textContent = cat.name;
      this.paletteTitleEl.style.borderColor = style.color;
      this.paletteTitleEl.style.color = style.color;
    }

    if (this.shell) {
      this.shell.style.setProperty("--active-cat-color", style.color);
    }

    this.toolbox.selectItemByPosition(index);
    this.scheduleFlyoutSync();
  },

  scheduleFlyoutSync() {
    const run = () => {
      if (this.isInteractionBlocked()) return;
      this.hideNativeToolbox();
      this.syncFlyoutLayout();
    };

    run();
    requestAnimationFrame(run);
    setTimeout(run, 50);
    setTimeout(run, 300);
  },

  syncFlyoutLayout() {
    if (this.isInteractionBlocked()) return;

    const width = this.getPaletteWidth();
    this.applyFixedFlyoutWidth(width);

    requestAnimationFrame(() => {
      if (this.isInteractionBlocked()) return;
      this.applyFixedFlyoutWidth(width);
      if (this.workspace && typeof Blockly !== "undefined") {
        Blockly.svgResize(this.workspace);
      }
    });
  },

  applyFixedFlyoutWidth(width) {
    if (this.isInteractionBlocked()) return;

    const flyout = this.toolbox.getFlyout && this.toolbox.getFlyout();
    const svg = this.shell && this.shell.querySelector(".blocklyFlyout");
    if (!flyout || !svg) return;

    flyout.visible = true;
    flyout.containerVisible = true;
    flyout.width_ = width;

    const shellHeight = this.shell ? this.shell.getBoundingClientRect().height : 0;
    const titleHeight =
      parseInt(
        getComputedStyle(this.shell || document.documentElement).getPropertyValue("--palette-title-height"),
        10
      ) || 38;
    const height = Math.max(flyout.height_ || 0, shellHeight - titleHeight, svg.getBoundingClientRect().height, 400);
    const corner = flyout.CORNER_RADIUS || 8;

    flyout.height_ = height;

    if (typeof flyout.setBackgroundPath === "function") {
      flyout.setBackgroundPath(width - corner, height);
    }

    svg.setAttribute("width", String(width));
    svg.setAttribute("height", String(height));
    svg.style.width = width + "px";
    svg.style.height = height + "px";
    svg.style.display = "block";
    svg.style.visibility = "visible";
    svg.classList.remove("blocklyHidden");

    if (typeof flyout.position === "function") {
      flyout.position();
    }
  },

  onResize() {
    this.syncFlyoutLayout();
  },
};
