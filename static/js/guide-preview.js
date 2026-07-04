/**
 * Read-only Blockly-превью для модального окна «Подробнее».
 * Без внутренней прокрутки — блоки показываются целиком, скролл только у модалки.
 */
const GuidePreview = {
  workspaces: [],
  CONTENT_PADDING: 12,

  getRenderer() {
    const names =
      Blockly.blockRendering && typeof Blockly.blockRendering.getRendererNames === "function"
        ? Blockly.blockRendering.getRendererNames()
        : [];
    if (names.includes("compact")) return "compact";
    if (names.includes("thrasos")) return "thrasos";
    return "geras";
  },

  getTheme() {
    if (typeof pyblocksTheme !== "undefined") return pyblocksTheme;
    return Blockly.Themes && Blockly.Themes.Classic ? Blockly.Themes.Classic : undefined;
  },

  isCompactMode(container) {
    return !!(container && container.getAttribute("data-preview-mode") === "compact");
  },

  disposeAll() {
    this.workspaces.forEach(function (ws) {
      try {
        const injectionDiv = ws.getInjectionDiv && ws.getInjectionDiv();
        const container = injectionDiv && injectionDiv.parentElement;
        if (container) {
          container.dataset.guideMounted = "0";
          container._guideWorkspace = null;
        }
        ws.dispose();
      } catch (e) {
        /* ignore */
      }
    });
    this.workspaces = [];
  },

  textToDom(xmlString) {
    if (typeof Blockly.utils !== "undefined" && Blockly.utils.xml) {
      return Blockly.utils.xml.textToDom(xmlString);
    }
    if (Blockly.Xml && Blockly.Xml.textToDom) {
      return Blockly.Xml.textToDom(xmlString);
    }
    throw new Error("Blockly XML parser unavailable");
  },

  domToWorkspace(xmlDom, ws) {
    if (Blockly.Xml && Blockly.Xml.domToWorkspace) {
      return Blockly.Xml.domToWorkspace(xmlDom, ws);
    }
    if (Blockly.serialization && Blockly.serialization.blocks && Blockly.serialization.blocks.append) {
      return Blockly.serialization.blocks.append(xmlDom, ws);
    }
    throw new Error("Blockly workspace loader unavailable");
  },

  isMounted(container) {
    return !!(container && container.dataset.guideMounted === "1");
  },

  ensureBlocksRendered(ws) {
    ws.getAllBlocks(false).forEach(function (block) {
      if (!block.rendered && typeof block.render === "function") {
        if (typeof block.initSvg === "function" && !block.getSvgRoot()) {
          block.initSvg();
        }
        block.render();
      }
    });
  },

  getContentBounds(ws) {
    const blocks = ws.getAllBlocks(false);
    if (!blocks.length) {
      return { width: 120, height: 80, minX: 0, minY: 0 };
    }

    this.ensureBlocksRendered(ws);

    let minX = Infinity;
    let minY = Infinity;
    let maxX = -Infinity;
    let maxY = -Infinity;

    blocks.forEach(function (block) {
      const hw = block.getHeightWidth();
      const xy = block.getRelativeToSurfaceXY();
      minX = Math.min(minX, xy.x);
      minY = Math.min(minY, xy.y);
      maxX = Math.max(maxX, xy.x + hw.width);
      maxY = Math.max(maxY, xy.y + hw.height);
    });

    if (!Number.isFinite(minX) || !Number.isFinite(minY)) {
      return { width: 120, height: 80, minX: 0, minY: 0 };
    }

    const pad = this.CONTENT_PADDING;
    return {
      minX: minX,
      minY: minY,
      width: Math.max(120, Math.ceil(maxX - minX + pad * 2)),
      height: Math.max(80, Math.ceil(maxY - minY + pad * 2)),
    };
  },

  getInjectOptions(container) {
    const compact = this.isCompactMode(container);
    return {
      readOnly: true,
      scrollbars: false,
      sounds: false,
      renderer: this.getRenderer(),
      theme: this.getTheme(),
      zoom: {
        controls: false,
        wheel: false,
        pinch: false,
        startScale: compact ? 1 : 0.82,
        maxScale: 1,
        minScale: 0.35,
      },
      move: {
        scrollbars: false,
        drag: false,
        wheel: false,
      },
    };
  },

  isLandingMode(container) {
    return !!(container && container.classList.contains("landing-blocks-preview"));
  },

  getContainerLimits(container) {
    const visual = container.closest(".step-card__visual");
    const landingCol = container.closest(".landing-demo__col--blocks");
    const maxW = container.clientWidth || container.offsetWidth || 240;
    let maxH = 150;
    if (visual) {
      maxH = Math.max(130, visual.clientHeight - 8);
    } else if (landingCol) {
      maxH = Math.max(120, landingCol.clientHeight - 24);
    }
    return {
      maxW: Math.max(120, maxW),
      maxH: maxH,
    };
  },

  layoutBlocks(ws) {
    const start =
      typeof ProgramFrame !== "undefined" && ProgramFrame.findStart
        ? ProgramFrame.findStart(ws)
        : ws.getTopBlocks(true)[0];
    if (!start) return;

    const xy = start.getRelativeToSurfaceXY();
    start.moveBy(this.CONTENT_PADDING - xy.x, this.CONTENT_PADDING - xy.y);
  },

  mount(container, xmlString) {
    if (!container || !xmlString || typeof Blockly === "undefined") return null;
    if (this.isMounted(container)) {
      this.resizeContainer(container);
      return container._guideWorkspace || null;
    }

    container.innerHTML = "";
    container.dataset.guideMounted = "1";
    container.classList.add("guide-preview--mounted");

    const host = document.createElement("div");
    host.className = "guide-preview__host";
    container.appendChild(host);

    let ws;
    try {
      ws = Blockly.inject(host, this.getInjectOptions(container));
    } catch (err) {
      console.error("GuidePreview.inject:", err);
      container.dataset.guideMounted = "0";
      container.classList.remove("guide-preview--mounted");
      container.innerHTML = '<p class="guide-preview__error">Не удалось создать превью блоков</p>';
      return null;
    }

    try {
      const xmlDom = this.textToDom(xmlString);
      this.domToWorkspace(xmlDom, ws);
      if (typeof ProgramFrame !== "undefined") {
        ProgramFrame.setup(ws);
        ProgramFrame.decorateFrameBlocks(ws);
      }
      this.layoutBlocks(ws);
      container._guideWorkspace = ws;
      this.workspaces.push(ws);
      this.resizeContainer(container);
      return ws;
    } catch (err) {
      console.error("GuidePreview.mount:", err);
      try {
        ws.dispose();
      } catch (disposeErr) {
        /* ignore */
      }
      container.dataset.guideMounted = "0";
      container.classList.remove("guide-preview--mounted");
      container.innerHTML =
        '<p class="guide-preview__error">Не удалось показать блоки: ' +
        String(err.message || err) +
        "</p>";
      return null;
    }
  },

  applyContainerSize(container, bounds, ws) {
    const host = container.querySelector(".guide-preview__host");
    if (!host || !ws) return;

    if (this.isCompactMode(container) || this.isLandingMode(container)) {
      this.applyCompactSize(container, host, bounds, ws);
      return;
    }

    host.style.width = "100%";
    host.style.height = bounds.height + "px";
    host.style.transform = "none";
    container.style.width = "100%";
    container.style.height = bounds.height + "px";
    container.style.minHeight = bounds.height + "px";
    container.style.maxHeight = "none";
  },

  applyCompactSize(container, host, bounds, ws) {
    const limits = this.getContainerLimits(container);
    const isLanding = this.isLandingMode(container);
    let fitScale = Math.min(1, limits.maxW / bounds.width, limits.maxH / bounds.height);
    if (isLanding) {
      fitScale = Math.min(fitScale, 0.84);
    }
    const scale = Math.max(0.42, fitScale);
    const visualH = Math.max(isLanding ? 110 : 100, Math.ceil(bounds.height * scale));

    host.style.width = bounds.width + "px";
    host.style.height = bounds.height + "px";
    host.style.transform = "none";

    container.style.width = "100%";
    container.style.height = visualH + "px";
    container.style.minHeight = visualH + "px";
    container.style.maxHeight = visualH + "px";

    if (typeof ws.setScale === "function") {
      ws.setScale(scale);
    }
  },

  resizeContainer(container) {
    const ws = container._guideWorkspace;
    if (!ws) return;

    const run = function () {
      try {
        if (
          (GuidePreview.isCompactMode(container) || GuidePreview.isLandingMode(container)) &&
          container.clientWidth < 20
        ) {
          return;
        }

        GuidePreview.ensureBlocksRendered(ws);
        const bounds = GuidePreview.getContentBounds(ws);
        GuidePreview.applyContainerSize(container, bounds, ws);
        Blockly.svgResize(ws);

        if (typeof ws.scroll === "function") {
          ws.scroll(0, 0);
        }
      } catch (err) {
        console.error("GuidePreview.resizeContainer:", err);
      }
    };

    requestAnimationFrame(function () {
      requestAnimationFrame(run);
    });
  },

  resizeAll() {
    document.querySelectorAll(".guide-preview[data-guide-mounted=\"1\"]").forEach(function (container) {
      GuidePreview.resizeContainer(container);
    });
  },
};
