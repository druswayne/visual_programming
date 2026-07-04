/**
 * Пошаговая отладка: подсветка блоков, строк кода и переменных.
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
  outputPanelEl: null,
  statusBadgeSlot: null,
  outputStatusSlot: null,

  init(workspace) {
    this.workspace = workspace;
    this.panelEl = document.getElementById("debugPanel");
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
    return Boolean(this.panelEl && !this.panelEl.hidden);
  },

  showPanel() {
    if (this.outputPanelEl) {
      this.outputPanelEl.hidden = true;
    }
    if (this.panelEl) {
      this.panelEl.hidden = false;
    }

    const sidebar = document.querySelector(".sidebar");
    if (sidebar) sidebar.classList.add("sidebar--debug");

    const codePanel = document.getElementById("codePanel");
    if (codePanel) codePanel.classList.add("panel--code--debug");

    const badge = document.getElementById("statusBadge");
    if (badge && this.statusBadgeSlot) {
      this.statusBadgeSlot.appendChild(badge);
    }

    const mainOut = document.getElementById("outputConsole");
    const debugOut = document.getElementById("debugOutputConsole");
    if (mainOut && debugOut) {
      debugOut.textContent = mainOut.textContent;
      debugOut.className = mainOut.className + " debug-output-console";
    }

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

    if (this.panelEl) {
      this.panelEl.hidden = true;
    }
    if (this.outputPanelEl) {
      this.outputPanelEl.hidden = false;
    }

    const sidebar = document.querySelector(".sidebar");
    if (sidebar) sidebar.classList.remove("sidebar--debug");

    const codePanel = document.getElementById("codePanel");
    if (codePanel) codePanel.classList.remove("panel--code--debug");

    const badge = document.getElementById("statusBadge");
    if (badge && this.outputStatusSlot) {
      this.outputStatusSlot.appendChild(badge);
    }

    const btnStart = document.getElementById("btnDebugStart");
    if (btnStart) btnStart.classList.remove("btn--active");
  },

  bindControls() {
    const btnStart = document.getElementById("btnDebugStart");
    const btnStep = document.getElementById("btnDebugStep");
    const btnStop = document.getElementById("btnDebugStop");
    const btnPrev = document.getElementById("btnDebugPrev");
    const btnPlay = document.getElementById("btnDebugPlay");
    const timeline = document.getElementById("debugTimeline");
    const speed = document.getElementById("debugPlaySpeed");

    if (btnStart) btnStart.addEventListener("click", () => this.start());
    if (btnStep) btnStep.addEventListener("click", () => this.stepForward());
    if (btnStop) btnStop.addEventListener("click", () => this.stop());
    if (btnPrev) btnPrev.addEventListener("click", () => this.stepBack());
    if (btnPlay) btnPlay.addEventListener("click", () => this.toggleAutoplay());
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
    btnPlay.textContent = this.playing ? "⏸ Пауза" : "▶ Авто";
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
    if (!timeline) return;
    const max = Math.max(0, this.steps.length - 1);
    timeline.disabled = !this.sessionActive;
    timeline.max = String(max);
    timeline.value = String(this.stepIndex < 0 ? 0 : this.stepIndex);
  },

  async start() {
    if (!this.workspace || this.loading) return;

    if (typeof CodeEditor !== "undefined" && CodeEditor.isEditMode()) {
      setStatus("error", "Ошибка");
      setOutput("Для пошаговой отладки нажмите «Собрать» или закройте редактор.", true);
      return;
    }

    if (this.sessionActive) {
      this.stop();
    }

    const data = generatePythonDebugData(this.workspace);
    if (!data.code.trim()) {
      setStatus("error", "Ошибка");
      setOutput("Добавьте блоки для пошагового выполнения.", true);
      return;
    }

    this.loading = true;
    this.displayLines = data.displayLines;
    this.debugLineToDisplay = data.debugLineToDisplay;
    this.lineBlockMap = data.lineBlockMap;
    this.showPanel();
    this.setControls();
    this.showCleanPreview();
    setStatus("running", "Отладка");
    setOutput("Сбор шагов выполнения…", false);

    const stdinText = await InputHelper.collectStdin(data.code);
    if (stdinText === null) {
      this.loading = false;
      this.hidePanel();
      this.setControls();
      setStatus("idle", "Готов");
      setOutput("Ввод отменён.", false);
      return;
    }

    try {
      const response = await fetch("/api/debug", {
        method: "POST",
        headers: getJsonHeaders(),
        body: JSON.stringify({ code: data.code, stdin: stdinText }),
      });
      const result = await response.json();
      const limitMsg = getApiErrorMessage(result, response);
      if (limitMsg) {
        setStatus("error", "Подождите");
        setOutput(limitMsg, true);
        this.loading = false;
        this.hidePanel();
        this.setControls();
        return;
      }

      if (!result.success && (!result.steps || !result.steps.length)) {
        setStatus("error", "Ошибка");
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
        setOutput("Ошибка: " + result.error, true);
      }

      this.renderStep();
      setStatus("running", "Шаг 1/" + this.steps.length);
    } catch (err) {
      setStatus("error", "Ошибка");
      setOutput("Ошибка отладки: " + err.message, true);
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
    setStatus("idle", "Готов");
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

  renderStep() {
    const step = this.steps[this.stepIndex];
    if (!step) return;

    const counter = document.getElementById("debugStepCounter");
    if (counter) {
      counter.textContent = "Шаг " + (this.stepIndex + 1) + " / " + this.steps.length;
    }

    this.highlightLine(step.line);
    this.highlightBlock(step.block_id);
    const prevStep = this.stepIndex > 0 ? this.steps[this.stepIndex - 1] : null;
    if (typeof MemoryViz !== "undefined") {
      MemoryViz.render(step, prevStep);
    } else {
      this.renderVariables(step.vars || {});
    }
    setOutput(step.output || "(нет вывода)", false);
    setStatus("running", "Шаг " + (this.stepIndex + 1));
    this.updateTimeline();
  },

  showCleanPreview() {
    const text = this.displayLines.join("\n").trim();
    setCodePreviewPlain(text || "# Соберите программу из блоков");
  },

  highlightLine(lineNo) {
    const displayLineNo = this.debugLineToDisplay[lineNo];
    if (!displayLineNo) return;
    setCodePreviewHighlight(this.displayLines, displayLineNo);
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
        svg.classList.remove("py-debug-highlight");
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
      panel.innerHTML = '<p class="debug-vars__empty">Нет переменных</p>';
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
