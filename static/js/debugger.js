/**
 * Пошаговая отладка: модалка «Машина времени», подсветка блоков и строк.
 */
const StepDebugger = {
  steps: [],
  stepIndex: -1,
  displayLines: [],
  debugLineToDisplay: {},
  lineBlockMap: {},
  activeBlockId: null,
  highlightedBlock: null,
  sessionActive: false,
  loading: false,
  playing: false,
  playTimer: null,
  panelEl: null,
  modalEl: null,
  outputPanelEl: null,
  statusBadgeSlot: null,
  outputStatusSlot: null,
  lastRenderedIndex: -1,

  init(workspace) {
    this.workspace = workspace;
    this.panelEl = document.getElementById("debugPanel");
    this.modalEl = document.getElementById("timeMachineModal");
    this.outputPanelEl = document.getElementById("outputPanel");
    this.statusBadgeSlot = document.getElementById("debugStatusSlot");
    this.outputStatusSlot = document.getElementById("outputStatusSlot");
    if (typeof MemoryViz !== "undefined") {
      MemoryViz.init();
      MemoryViz.clear();
    }
    this.hidePanel();
    this.bindControls();
  },

  isPanelVisible() {
    return Boolean(this.modalEl && !this.modalEl.hidden);
  },

  showPanel() {
    if (!this.modalEl) return;

    const mainOut = document.getElementById("outputConsole");
    const debugOut = document.getElementById("debugOutputConsole");
    if (mainOut && debugOut) {
      debugOut.textContent = mainOut.textContent;
      debugOut.className = mainOut.className + " debug-output-console";
    }

    this.modalEl.hidden = false;
    this.modalEl.classList.remove("tm-modal--closing");
    // Force reflow so open animation restarts.
    void this.modalEl.offsetWidth;
    this.modalEl.classList.add("tm-modal--open");

    document.body.classList.add("tm-modal-open");

    const codePanel = document.getElementById("codePanel");
    if (codePanel) codePanel.classList.add("panel--code--debug");

    const btnStart = document.getElementById("btnDebugStart");
    if (btnStart) btnStart.classList.add("btn--active");
  },

  hidePanel() {
    const debugOut = document.getElementById("debugOutputConsole");
    const mainOut = document.getElementById("outputConsole");
    if (debugOut && mainOut && debugOut.textContent) {
      mainOut.textContent = debugOut.textContent;
      mainOut.className = debugOut.className.replace(/\s*debug-output-console\s*/g, " ").trim();
    }

    if (this.modalEl) {
      this.modalEl.classList.remove("tm-modal--open");
      this.modalEl.hidden = true;
    }

    document.body.classList.remove("tm-modal-open");

    const codePanel = document.getElementById("codePanel");
    if (codePanel) codePanel.classList.remove("panel--code--debug");

    const btnStart = document.getElementById("btnDebugStart");
    if (btnStart) btnStart.classList.remove("btn--active");
  },

  bindControls() {
    const btnStart = document.getElementById("btnDebugStart");
    const btnStep = document.getElementById("btnDebugStep");
    const btnStop = document.getElementById("btnDebugStop");
    const btnPrev = document.getElementById("btnDebugPrev");
    const btnPlay = document.getElementById("btnDebugPlay");
    const btnClose = document.getElementById("timeMachineClose");
    const timeline = document.getElementById("debugTimeline");
    const speed = document.getElementById("debugPlaySpeed");

    if (btnStart) btnStart.addEventListener("click", () => this.start());
    if (btnStep) btnStep.addEventListener("click", () => this.stepForward());
    if (btnStop) btnStop.addEventListener("click", () => this.stop());
    if (btnPrev) btnPrev.addEventListener("click", () => this.stepBack());
    if (btnPlay) btnPlay.addEventListener("click", () => this.toggleAutoplay());
    if (btnClose) btnClose.addEventListener("click", () => this.stop());
    if (this.modalEl) {
      this.modalEl.addEventListener("click", (event) => {
        if (event.target === this.modalEl) this.stop();
      });
    }
    if (timeline) {
      timeline.addEventListener("input", () => this.seekTimeline(Number(timeline.value)));
    }
    if (speed) {
      speed.addEventListener("change", () => {
        if (this.playing) {
          this.stopAutoplay();
          this.startAutoplay();
        }
      });
    }

    document.addEventListener("keydown", (event) => this.onKeyDown(event));
  },

  onKeyDown(event) {
    if (!this.isPanelVisible()) return;
    if (event.key === "Escape") {
      event.preventDefault();
      this.stop();
      return;
    }

    if (!this.sessionActive || this.loading) return;
    const tag = (event.target && event.target.tagName) || "";
    if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;

    if (event.key === "F5") {
      event.preventDefault();
      this.stepForward();
    } else if (event.key === "ArrowRight") {
      event.preventDefault();
      this.stepForward();
    } else if (event.key === "ArrowLeft") {
      event.preventDefault();
      this.stepBack();
    } else if (event.key === " ") {
      event.preventDefault();
      this.toggleAutoplay();
    }
  },

  getPlayDelay() {
    const speed = document.getElementById("debugPlaySpeed");
    return speed ? Number(speed.value) || 700 : 700;
  },

  toggleAutoplay() {
    if (!this.sessionActive) return;
    if (this.playing) {
      this.stopAutoplay();
    } else {
      this.startAutoplay();
    }
  },

  startAutoplay() {
    if (!this.sessionActive || this.stepIndex >= this.steps.length - 1) return;
    this.playing = true;
    this.updatePlayButton();
    const tick = () => {
      if (!this.playing || !this.sessionActive) return;
      if (this.stepIndex < this.steps.length - 1) {
        this.stepIndex++;
        this.renderStep();
        this.playTimer = window.setTimeout(tick, this.getPlayDelay());
      } else {
        this.stopAutoplay();
      }
    };
    this.playTimer = window.setTimeout(tick, this.getPlayDelay());
  },

  stopAutoplay() {
    this.playing = false;
    if (this.playTimer) {
      window.clearTimeout(this.playTimer);
      this.playTimer = null;
    }
    this.updatePlayButton();
  },

  updatePlayButton() {
    const btnPlay = document.getElementById("btnDebugPlay");
    if (!btnPlay) return;
    btnPlay.textContent = this.playing ? t("debugger.pause") : t("debugger.autoplay");
    btnPlay.classList.toggle("btn--active", this.playing);
  },

  seekTimeline(index) {
    if (!this.sessionActive || !this.steps.length) return;
    const next = Math.max(0, Math.min(this.steps.length - 1, index));
    if (next === this.stepIndex) return;
    this.stepIndex = next;
    this.renderStep();
  },

  updateTimeline() {
    const timeline = document.getElementById("debugTimeline");
    const fill = document.getElementById("debugTimelineFill");
    if (!timeline) return;
    const max = Math.max(0, this.steps.length - 1);
    timeline.disabled = !this.sessionActive;
    timeline.max = String(max);
    timeline.value = String(this.stepIndex < 0 ? 0 : this.stepIndex);
    if (fill) {
      const pct = max > 0 ? (Math.max(0, this.stepIndex) / max) * 100 : 0;
      fill.style.width = pct + "%";
    }
  },

  async start() {
    if (!this.workspace || this.loading) return;
    if (typeof GameUI !== "undefined" && GameUI.active) return;

    if (typeof CodeEditor !== "undefined" && CodeEditor.isEditMode()) {
      setStatus("error", t("status.error"));
      setOutput(t("debugger.edit_mode_hint"), true);
      return;
    }

    if (this.sessionActive) {
      this.stop();
    }

    const data = generatePythonDebugData(this.workspace);
    if (!data.code.trim()) {
      setStatus("error", t("status.error"));
      setOutput(t("debugger.no_code"), true);
      return;
    }

    this.loading = true;
    this.displayLines = data.displayLines;
    this.debugLineToDisplay = data.debugLineToDisplay;
    this.lineBlockMap = data.lineBlockMap;
    this.lastRenderedIndex = -1;
    this.setControls();
    setStatus("running", t("debugger.status"));
    setOutput(t("debugger.collecting_steps"), false);

    const stdinText = await InputHelper.collectStdin(data.code);
    if (stdinText === null) {
      this.loading = false;
      this.setControls();
      setStatus("idle", t("status.ready"));
      setOutput(t("run.input_cancelled"), false);
      return;
    }

    this.showPanel();
    this.showCleanPreview();
    setOutput(t("debugger.collecting_steps"), false);

    try {
      const response = await fetch("/api/debug", {
        method: "POST",
        headers: getJsonHeaders(),
        body: JSON.stringify({ code: data.code, stdin: stdinText }),
      });
      const result = await response.json();
      const limitMsg = getApiErrorMessage(result, response);
      if (limitMsg) {
        setStatus("error", t("status.wait"));
        setOutput(limitMsg, true);
        this.loading = false;
        this.hidePanel();
        this.setControls();
        return;
      }

      if (!result.success && (!result.steps || !result.steps.length)) {
        setStatus("error", t("status.error"));
        setOutput([result.error, result.output].filter(Boolean).join("\n\n"), true);
        this.loading = false;
        this.hidePanel();
        this.setControls();
        updateCodePreview();
        return;
      }

      this.loading = false;
      this.sessionActive = true;
      this.steps = result.steps || [];
      this.stepIndex = 0;
      this.setControls();

      if (result.error) {
        setOutput(t("debugger.error_prefix", "Ошибка: {message}", { message: result.error }), true);
      }

      this.renderStep();
      setStatus(
        "running",
        t("debugger.step_of", "Шаг {current} из {total}", { current: 1, total: this.steps.length })
      );
    } catch (err) {
      setStatus("error", t("status.error"));
      setOutput(t("debugger.debug_error", "Ошибка отладки: {message}", { message: err.message }), true);
      this.loading = false;
      this.sessionActive = false;
      this.hidePanel();
      this.setControls();
      updateCodePreview();
    }
  },

  stop() {
    this.stopAutoplay();
    this.loading = false;
    this.sessionActive = false;
    this.steps = [];
    this.stepIndex = -1;
    this.lastRenderedIndex = -1;
    this.displayLines = [];
    this.debugLineToDisplay = {};
    this.clearBlockHighlight();
    this.renderVariables({});
    if (typeof MemoryViz !== "undefined") {
      MemoryViz.clear();
    }
    this.hidePanel();
    this.setControls();
    updateCodePreview();
    setStatus("idle", t("status.ready"));
  },

  setControls() {
    const stepping = this.sessionActive;
    const busy = this.loading;

    const btnStep = document.getElementById("btnDebugStep");
    const btnStop = document.getElementById("btnDebugStop");
    const btnPrev = document.getElementById("btnDebugPrev");
    const btnPlay = document.getElementById("btnDebugPlay");
    const btnStart = document.getElementById("btnDebugStart");
    const btnRun = document.getElementById("btnRun");
    const speed = document.getElementById("debugPlaySpeed");

    if (btnStep) btnStep.disabled = !stepping;
    if (btnStop) btnStop.disabled = !stepping && !busy;
    if (btnPrev) btnPrev.disabled = !stepping;
    if (btnPlay) btnPlay.disabled = !stepping;
    if (speed) speed.disabled = !stepping;
    if (btnStart) btnStart.disabled = busy;
    if (btnRun) btnRun.disabled = busy;

    this.updateTimeline();
    this.updatePlayButton();

    const counter = document.getElementById("debugStepCounter");
    if (counter) counter.textContent = stepping ? "" : "—";
  },

  stepForward() {
    if (!this.sessionActive || !this.steps.length) return;
    if (this.stepIndex < this.steps.length - 1) {
      this.stepIndex++;
      this.renderStep();
    } else {
      this.stopAutoplay();
    }
  },

  stepBack() {
    if (!this.sessionActive || !this.steps.length) return;
    if (this.stepIndex > 0) {
      this.stopAutoplay();
      this.stepIndex--;
      this.renderStep();
    }
  },

  pulseStage(direction) {
    const stage = this.panelEl;
    if (!stage) return;
    stage.classList.remove("tm-modal__stage--forward", "tm-modal__stage--back");
    void stage.offsetWidth;
    stage.classList.add(direction === "back" ? "tm-modal__stage--back" : "tm-modal__stage--forward");
  },

  renderStep() {
    const step = this.steps[this.stepIndex];
    if (!step) return;

    const direction = this.stepIndex < this.lastRenderedIndex ? "back" : "forward";
    if (this.lastRenderedIndex !== this.stepIndex) {
      this.pulseStage(direction);
    }
    this.lastRenderedIndex = this.stepIndex;

    const counter = document.getElementById("debugStepCounter");
    if (counter) {
      counter.textContent = t("debugger.step_of", "Шаг {current} из {total}", {
        current: this.stepIndex + 1,
        total: this.steps.length,
      });
      counter.classList.remove("tm-modal__step-badge--pulse");
      void counter.offsetWidth;
      counter.classList.add("tm-modal__step-badge--pulse");
    }

    this.highlightLine(step.line);
    this.highlightBlock(step.block_id);
    const prevStep = this.stepIndex > 0 ? this.steps[this.stepIndex - 1] : null;
    if (typeof MemoryViz !== "undefined") {
      MemoryViz.render(step, prevStep);
    } else {
      this.renderVariables(step.vars || {});
    }
    setOutput(step.output || t("debugger.no_output"), false);
    setStatus(
      "running",
      t("debugger.step_short", "Шаг {current}", { current: this.stepIndex + 1 })
    );
    this.updateTimeline();
  },

  getDebugCodeNodes() {
    const preview = document.getElementById("debugCodePreview");
    if (!preview) return null;
    let codeEl = preview.querySelector("code");
    if (!codeEl) {
      preview.textContent = "";
      codeEl = document.createElement("code");
      preview.appendChild(codeEl);
    }
    return { preview: preview, codeEl: codeEl };
  },

  showCleanPreview() {
    const text = this.displayLines.join("\n").trim();
    const plain = text || t("code.placeholder");
    setCodePreviewPlain(plain);

    const nodes = this.getDebugCodeNodes();
    if (!nodes) return;
    if (typeof PythonHighlighter !== "undefined") {
      nodes.codeEl.innerHTML = PythonHighlighter.highlight(plain);
    } else {
      nodes.codeEl.textContent = plain;
    }
  },

  highlightLine(lineNo) {
    const displayLineNo = this.debugLineToDisplay[lineNo];
    if (!displayLineNo) return;
    setCodePreviewHighlight(this.displayLines, displayLineNo);
    this.highlightDebugCode(this.displayLines, displayLineNo);
  },

  highlightDebugCode(lines, activeLineNo) {
    const nodes = this.getDebugCodeNodes();
    if (!nodes) return;

    const normalized = lines.slice();
    while (normalized.length && normalized[0].trim() === "") {
      normalized.shift();
      activeLineNo--;
    }
    while (normalized.length && normalized[normalized.length - 1].trim() === "") {
      normalized.pop();
    }
    if (activeLineNo < 1) activeLineNo = 1;
    if (activeLineNo > normalized.length) activeLineNo = normalized.length;

    const html = normalized
      .map(function (line, index) {
        const highlighted =
          typeof PythonHighlighter !== "undefined"
            ? PythonHighlighter.highlightLine(line)
            : escapeHtml(line);
        if (index + 1 === activeLineNo) {
          return '<mark class="code-line--active">' + highlighted + "</mark>";
        }
        return highlighted;
      })
      .join("\n");

    nodes.codeEl.innerHTML = html || t("code.placeholder");

    const active = nodes.codeEl.querySelector(".code-line--active");
    if (active) {
      active.classList.add("code-line--enter");
      active.scrollIntoView({ block: "nearest", behavior: "smooth" });
    }
  },

  highlightBlock(blockId) {
    this.clearBlockHighlight();
    if (!blockId || !this.workspace) return;

    const block = this.workspace.getBlockById(blockId);
    if (!block) return;

    this.activeBlockId = blockId;
    this.highlightedBlock = block;

    const svg = typeof block.getSvgRoot === "function" ? block.getSvgRoot() : null;
    if (svg) {
      svg.classList.add("py-debug-highlight");
      svg.classList.remove("py-debug-highlight--pulse");
      void svg.offsetWidth;
      svg.classList.add("py-debug-highlight--pulse");
    }

    this.scrollBlockIntoView(block);
  },

  scrollBlockIntoView(block) {
    if (!block || !this.workspace) return;

    const metrics = this.workspace.getMetrics();
    const xy = block.getRelativeToSurfaceXY();
    const hw = block.getHeightWidth ? block.getHeightWidth().width : 120;
    const hh = block.getHeightWidth ? block.getHeightWidth().height : 40;

    const viewLeft = metrics.viewLeft + 40;
    const viewRight = metrics.viewLeft + metrics.viewWidth - 40;
    const viewTop = metrics.viewTop + 40;
    const viewBottom = metrics.viewTop + metrics.viewHeight - 40;

    const offScreen =
      xy.x < viewLeft ||
      xy.x + hw > viewRight ||
      xy.y < viewTop ||
      xy.y + hh > viewBottom;

    if (offScreen && typeof this.workspace.centerOnBlock === "function") {
      this.workspace.centerOnBlock(block.id);
    }
  },

  clearBlockHighlight() {
    if (this.highlightedBlock) {
      const svg =
        typeof this.highlightedBlock.getSvgRoot === "function"
          ? this.highlightedBlock.getSvgRoot()
          : null;
      if (svg) {
        svg.classList.remove("py-debug-highlight", "py-debug-highlight--pulse");
      }
    }

    this.activeBlockId = null;
    this.highlightedBlock = null;
  },

  renderVariables(vars) {
    const panel = document.getElementById("debugVars");
    if (!panel) return;

    const names = Object.keys(vars || {}).sort();
    if (!names.length) {
      panel.innerHTML = '<p class="debug-vars__empty">' + t("debugger.no_vars") + "</p>";
      return;
    }

    panel.innerHTML = names
      .map(function (name) {
        const val = formatValueForDisplay(vars[name]);
        return (
          '<div class="debug-var">' +
          '<span class="debug-var__name">' + name + "</span>" +
          '<span class="debug-var__value">' + val + "</span>" +
          "</div>"
        );
      })
      .join("");
  },
};
