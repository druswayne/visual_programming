/**
 * Темы, задачи и режим песочницы.
 */
const TopicsUI = {
  mode: "sandbox",
  topicId: "",
  taskId: "",
  topics: [],
  tasks: [],
  taskCollapsed: false,

  init() {
    this.modeSelect = document.getElementById("modeSelect");
    this.modeSwitch = document.getElementById("modeSwitch");
    this.topicSelect = document.getElementById("topicSelect");
    this.taskSelect = document.getElementById("taskSelect");
    this.taskPickersRow = document.getElementById("taskPickersRow");
    this.taskPanel = document.getElementById("taskPanel");
    this.taskTitle = document.getElementById("taskTitle");
    this.taskCondition = document.getElementById("taskCondition");
    this.taskHint = document.getElementById("taskHint");
    this.taskMeta = document.getElementById("taskMeta");
    this.workspaceChrome = document.getElementById("workspaceChrome");
    this.blocklyShell = document.getElementById("blocklyShell");
    this.btnCheck = document.getElementById("btnCheckTask");
    this.btnPrev = document.getElementById("btnTaskPrev");
    this.btnNext = document.getElementById("btnTaskNext");
    this.btnTaskCollapse = document.getElementById("btnTaskCollapse");
    this.taskBannerBody = document.getElementById("taskBannerBody");
    this.btnTopicMore = document.getElementById("btnTopicMore");
    this.topicGuideModal = document.getElementById("topicGuideModal");
    this.topicGuideTitle = document.getElementById("topicGuideTitle");
    this.topicGuideBody = document.getElementById("topicGuideBody");
    this.topicGuideClose = document.getElementById("topicGuideClose");
    this.topicGuideOk = document.getElementById("topicGuideOk");
    this.guideCache = {};
    this._guideXmlMap = {};
    this._guidePreviewSeq = 0;
    this.authenticated = document.body.dataset.authenticated === "1";

    this.initTopicGuideModal();
    this.initTaskCollapse();
    this.initModeSwitch();
    this.initCustomSelects();

    if (this.btnCheck) {
      this.btnCheck.addEventListener("click", () => this.checkSolution());
    }
    if (this.btnPrev) {
      this.btnPrev.addEventListener("click", () => this.navigateTask(-1));
    }
    if (this.btnNext) {
      this.btnNext.addEventListener("click", () => this.navigateTask(1));
    }
    if (this.modeSelect) {
      this.modeSelect.addEventListener("change", () => this.onModeChange());
    }
    if (this.topicSelect) {
      this.topicSelect.addEventListener("change", () => this.onTopicChange());
    }
    if (this.taskSelect) {
      this.taskSelect.addEventListener("change", () => this.onTaskChange());
    }

    this.syncPickerPlaceholders();
    this.setupWorkspaceLayoutObserver();

    const hasDemo = new URLSearchParams(window.location.search).has("demo");

    if (!this.authenticated) {
      this.mode = "sandbox";
      this.applyMode();
      if (hasDemo) {
        this.applySandboxDemo();
      }
      return;
    }

    this.loadTopics().then(function () {
      TopicsUI.applyUrlParams();
      if (hasDemo) {
        TopicsUI.applySandboxDemo();
      }
    });
    this.applyMode();
  },

  initCustomSelects() {
    if (typeof CustomSelect === "undefined") return;
    CustomSelect.enhance(this.topicSelect);
    CustomSelect.enhance(this.taskSelect);
  },

  refreshSelect(select) {
    if (typeof CustomSelect !== "undefined" && select) {
      CustomSelect.refresh(select);
    }
  },

  setSelectDisabled(select, disabled) {
    if (!select) return;
    select.disabled = disabled;
    if (typeof CustomSelect !== "undefined") {
      CustomSelect.setDisabled(select, disabled);
    }
  },

  async applySandboxDemo() {
    const params = new URLSearchParams(window.location.search);
    const demoId = params.get("demo");
    if (!demoId || typeof workspace === "undefined" || !workspace) return;

    try {
      const response = await fetch("/api/sandbox-demo/" + encodeURIComponent(demoId));
      const data = await response.json();
      if (!data.success || !data.xml) return;

      if (typeof loadWorkspaceXml === "function") {
        loadWorkspaceXml(workspace, data.xml);
      } else if (typeof WorkspaceStorage !== "undefined") {
        WorkspaceStorage.load(workspace, data.xml);
      }

      if (typeof updateCodePreview === "function") {
        updateCodePreview();
      }
      if (typeof centerWorkspaceOnBlocks === "function") {
        centerWorkspaceOnBlocks();
      }
    } catch (err) {
      console.error("applySandboxDemo:", err);
    }
  },

  async applyUrlParams() {
    const params = new URLSearchParams(window.location.search);
    const topic = params.get("topic");
    const task = params.get("task");
    if (!topic) return;

    if (this.modeSelect) {
      this.modeSelect.value = "topic";
      this.mode = "topic";
    }
    this.applyMode();

    const topicOption = this.topicSelect && this.topicSelect.querySelector('option[value="' + topic + '"]');
    if (!topicOption || topicOption.disabled) {
      const meta = this.getTopicById(topic);
      if (meta && !meta.unlocked) {
        this.showTopicLockedMessage(meta);
      }
      return;
    }

    this.topicSelect.value = topic;
    await this.onTopicChange();

    if (task) {
      const taskOption = this.taskSelect && this.taskSelect.querySelector('option[value="' + task + '"]');
      if (taskOption) {
        this.taskSelect.value = task;
        this.onTaskChange();
      }
    }
  },

  initTaskCollapse() {
    if (!this.btnTaskCollapse) return;
    this.btnTaskCollapse.addEventListener("click", () => this.toggleTaskCollapse());
    this.setTaskCollapsed(this.taskCollapsed);
  },

  toggleTaskCollapse() {
    this.setTaskCollapsed(!this.taskCollapsed);
  },

  setTaskCollapsed(collapsed) {
    this.taskCollapsed = collapsed;
    if (this.taskPanel) {
      this.taskPanel.classList.toggle("is-collapsed", collapsed);
    }
    if (this.btnTaskCollapse) {
      this.btnTaskCollapse.textContent = collapsed ? "▼" : "▲";
      this.btnTaskCollapse.title = collapsed ? "Развернуть условие" : "Свернуть условие";
      this.btnTaskCollapse.setAttribute("aria-expanded", collapsed ? "false" : "true");
    }
    requestAnimationFrame(() => this.updateWorkspaceLayout());
  },

  initTopicGuideModal() {
    if (this.btnTopicMore) {
      this.btnTopicMore.addEventListener("click", () => this.openTopicGuide());
    }
    if (this.topicGuideClose) {
      this.topicGuideClose.addEventListener("click", () => this.closeTopicGuide());
    }
    if (this.topicGuideOk) {
      this.topicGuideOk.addEventListener("click", () => this.closeTopicGuide());
    }
    if (this.topicGuideModal) {
      this.topicGuideModal.addEventListener("click", (event) => {
        if (event.target === this.topicGuideModal) {
          this.closeTopicGuide();
        }
      });
    }
    if (this.topicGuideBody) {
      this.topicGuideBody.addEventListener("click", (event) => {
        const btn = event.target.closest(".guide-solution-toggle");
        if (!btn) return;
        this.toggleGuideSolution(btn);
      });
    }
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && this.topicGuideModal && !this.topicGuideModal.hidden) {
        this.closeTopicGuide();
      }
    });
  },

  shouldShowTopicMore() {
    return this.mode === "topic" && !!this.topicId && !this.taskId;
  },

  initModeSwitch() {
    if (!this.modeSwitch || !this.modeSelect) return;

    const buttons = this.modeSwitch.querySelectorAll(".mode-switch__btn");
    const self = this;

    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        const mode = btn.getAttribute("data-mode");
        if (!mode || self.mode === mode) return;
        self.modeSelect.value = mode;
        self.onModeChange();
      });
    });

    this.syncModeSwitch();
  },

  syncModeSwitch() {
    if (!this.modeSwitch) return;
    const active = this.mode;
    this.modeSwitch.querySelectorAll(".mode-switch__btn").forEach(function (btn) {
      btn.classList.toggle("is-active", btn.getAttribute("data-mode") === active);
    });
  },

  updateTopicIntroFooter() {
    const show = this.shouldShowTopicMore();
    if (this.btnTopicMore) {
      this.btnTopicMore.hidden = !show;
    }
  },

  updateTaskChrome() {
    const isTopic = this.mode === "topic";
    const hasTask = isTopic && !!this.taskId;

    if (this.taskPickersRow) this.taskPickersRow.hidden = !isTopic;
    if (this.taskPanel) this.taskPanel.hidden = !hasTask;

    const showNav = hasTask;
    if (this.btnCheck) this.btnCheck.hidden = !showNav;
    if (this.btnPrev) this.btnPrev.hidden = !showNav;
    if (this.btnNext) this.btnNext.hidden = !showNav;

    this.updateTopicIntroFooter();
    this.syncModeSwitch();
    this.syncPickerPlaceholders();
    requestAnimationFrame(() => this.updateWorkspaceLayout());
  },

  escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  },

  renderGuideText(text) {
    const escaped = this.escapeHtml(text);
    return escaped.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
  },

  registerGuideXml(xml) {
    const id = "gp-" + ++this._guidePreviewSeq;
    this._guideXmlMap[id] = xml;
    return id;
  },

  renderGuidePreview(xml) {
    if (!xml) return "";
    const id = this.registerGuideXml(xml);
    return '<div class="guide-preview" data-preview-id="' + id + '"></div>';
  },

  renderGuideExample(example, index) {
    let html = '<div class="topic-guide__example topic-guide__example--task">';
    html += '<div class="topic-guide__example-label">Задача ' + (index + 1) + "</div>";
    html += '<div class="topic-guide__text topic-guide__task-text">' + this.renderGuideText(example.task) + "</div>";
    if (example.result) {
      html += '<div class="topic-guide__result">';
      html += '<div class="topic-guide__result-label">Ожидаемый результат</div>';
      html += '<div class="topic-guide__result-text">' + this.escapeHtml(example.result) + "</div>";
      html += "</div>";
    }
    if (example.solution_xml) {
      const solutionId = this.registerGuideXml(example.solution_xml);
      html +=
        '<button type="button" class="btn btn--ghost guide-solution-toggle" ' +
        'data-solution-id="' +
        solutionId +
        '" aria-expanded="false">Показать решение</button>';
      html += '<div class="guide-solution" hidden data-solution-for="' + solutionId + '">';
      html += '<div class="topic-guide__example-label">Решение из блоков</div>';
      html += '<div class="guide-preview" data-preview-id="' + solutionId + '"></div>';
      html += "</div>";
    }
    html += "</div>";
    return html;
  },

  renderGuideContent(guide) {
    this._guideXmlMap = {};
    this._guidePreviewSeq = 0;

    let html = "";
    if (guide.intro) {
      html += '<p class="topic-guide__intro">' + this.renderGuideText(guide.intro) + "</p>";
    }
    (guide.sections || []).forEach(function (section) {
      html += '<article class="topic-guide__section">';
      if (section.title) {
        html += '<h4 class="topic-guide__section-title">' + TopicsUI.escapeHtml(section.title) + "</h4>";
      }
      if (section.text) {
        html += '<div class="topic-guide__text">' + TopicsUI.renderGuideText(section.text) + "</div>";
      }
      if (section.demo_xml) {
        html += '<div class="topic-guide__example">';
        html += '<div class="topic-guide__example-label">Пример из блоков</div>';
        html += TopicsUI.renderGuidePreview(section.demo_xml);
        html += "</div>";
      }
      if (section.examples && section.examples.length) {
        section.examples.forEach(function (example, index) {
          html += TopicsUI.renderGuideExample(example, index);
        });
      }
      if (section.tip) {
        html += '<div class="topic-guide__tip">' + TopicsUI.renderGuideText(section.tip) + "</div>";
      }
      html += "</article>";
    });
    return html;
  },

  mountGuidePreviews() {
    if (typeof GuidePreview === "undefined" || !this.topicGuideBody) return;

    const hosts = this.topicGuideBody.querySelectorAll(".guide-preview[data-preview-id]");
    hosts.forEach(function (host) {
      if (GuidePreview.isMounted(host)) return;

      const previewId = host.getAttribute("data-preview-id");
      const solutionPanel = host.closest(".guide-solution");
      if (solutionPanel && solutionPanel.hidden) return;

      const xml = TopicsUI._guideXmlMap[previewId];
      if (xml) GuidePreview.mount(host, xml);
    });
  },

  mountGuideSolution(solutionId, panel) {
    if (!panel || typeof GuidePreview === "undefined") return;

    const host = panel.querySelector('.guide-preview[data-preview-id="' + solutionId + '"]');
    if (!host) return;

    const xml = this._guideXmlMap[solutionId];
    if (!xml) {
      host.innerHTML = '<p class="guide-preview__error">XML решения не найден</p>';
      return;
    }

    const mount = function () {
      GuidePreview.mount(host, xml);
    };

    requestAnimationFrame(function () {
      requestAnimationFrame(mount);
    });
  },

  toggleGuideSolution(button) {
    const solutionId = button.getAttribute("data-solution-id");
    const panel = this.topicGuideBody.querySelector('[data-solution-for="' + solutionId + '"]');
    if (!panel) return;

    const wasHidden = panel.hidden;
    panel.hidden = !wasHidden;
    button.setAttribute("aria-expanded", wasHidden ? "true" : "false");
    button.textContent = wasHidden ? "Скрыть решение" : "Показать решение";

    if (wasHidden) {
      this.mountGuideSolution(solutionId, panel);
    }
  },

  async openTopicGuide() {
    if (!this.shouldShowTopicMore() || !this.topicGuideModal) return;

    if (typeof GuidePreview !== "undefined") {
      GuidePreview.disposeAll();
    }

    const topic = this.topics.find(function (t) {
      return t.id === TopicsUI.topicId;
    });
    if (this.topicGuideTitle) {
      this.topicGuideTitle.textContent = topic ? topic.title : "О теме";
    }
    if (this.topicGuideBody) {
      this.topicGuideBody.innerHTML = '<p class="topic-guide__text">Загрузка…</p>';
    }

    this.topicGuideModal.hidden = false;
    document.body.style.overflow = "hidden";

    try {
      let guide = this.guideCache[this.topicId];
      if (!guide) {
        const response = await fetch("/api/topics/" + encodeURIComponent(this.topicId) + "/guide");
        if (!response.ok) throw new Error("Не удалось загрузить материалы");
        const data = await response.json();
        guide = data.guide;
        this.guideCache[this.topicId] = guide;
      }
      if (this.topicGuideBody && guide) {
        this.topicGuideBody.innerHTML = this.renderGuideContent(guide);
        requestAnimationFrame(() => {
          this.mountGuidePreviews();
          if (typeof GuidePreview !== "undefined") {
            GuidePreview.resizeAll();
          }
        });
      }
    } catch (err) {
      if (this.topicGuideBody) {
        this.topicGuideBody.innerHTML =
          '<p class="topic-guide__text">Не удалось загрузить материалы: ' + this.escapeHtml(err.message) + "</p>";
      }
    }
  },

  closeTopicGuide() {
    if (!this.topicGuideModal) return;
    if (typeof GuidePreview !== "undefined") {
      GuidePreview.disposeAll();
    }
    this._guideXmlMap = {};
    this.topicGuideModal.hidden = true;
    document.body.style.overflow = "";
  },

  syncPickerPlaceholders() {
    this.refreshSelect(this.topicSelect);
    this.refreshSelect(this.taskSelect);
  },

  setupWorkspaceLayoutObserver() {
    if (typeof ResizeObserver === "undefined") return;
    this._layoutObserver = new ResizeObserver(() => this.updateWorkspaceLayout());
    if (this.taskPanel) this._layoutObserver.observe(this.taskPanel);
    if (this.blocklyShell) this._layoutObserver.observe(this.blocklyShell);
  },

  updateWorkspaceLayout() {
    const shell = this.blocklyShell;
    if (!shell) return;

    let offset = 0;
    if (this.taskPanel && !this.taskPanel.hidden) {
      offset = this.taskPanel.offsetHeight;
    }
    shell.style.setProperty("--workspace-top-offset", offset + "px");

    if (typeof Blockly !== "undefined" && workspace) {
      requestAnimationFrame(function () {
        Blockly.svgResize(workspace);
        if (typeof ScratchToolbox !== "undefined") ScratchToolbox.onResize();
      });
    }
  },

  setCondition(text) {
    if (this.taskCondition) this.taskCondition.textContent = text || "";
    requestAnimationFrame(() => this.updateWorkspaceLayout());
  },

  setHint(text) {
    if (!this.taskHint) return;
    if (text) {
      this.taskHint.textContent = "Подсказка: " + text;
      this.taskHint.hidden = false;
    } else {
      this.taskHint.textContent = "";
      this.taskHint.hidden = true;
    }
    requestAnimationFrame(() => this.updateWorkspaceLayout());
  },

  async loadTopics() {
    try {
      const response = await fetch("/api/topics");
      const data = await response.json();
      this.topics = data.topics || [];
      this.topicSelect.innerHTML = '<option value="">Выберите тему</option>';
      this.topics.forEach(function (topic) {
        const option = document.createElement("option");
        option.value = topic.id;
        let label = topic.title;
        if (!topic.unlocked) {
          option.disabled = true;
          label += " 🔒";
          if (topic.unlock_hint) {
            option.title = topic.unlock_hint;
          }
        } else if (topic.total_tasks) {
          label += " (" + topic.completed_count + "/" + topic.total_tasks + ")";
        }
        option.textContent = label;
        TopicsUI.topicSelect.appendChild(option);
      });
      TopicsUI.refreshSelect(TopicsUI.topicSelect);
    } catch (err) {
      console.error("loadTopics:", err);
    }
  },

  getTopicById(topicId) {
    return this.topics.find(function (t) {
      return t.id === topicId;
    });
  },

  isTopicUnlocked(topicId) {
    const topic = this.getTopicById(topicId);
    return !topic || topic.unlocked !== false;
  },

  showTopicLockedMessage(topic) {
    this.topicId = "";
    if (this.topicSelect) this.topicSelect.value = "";
    this.showTopicIntro();
    const hint = (topic && topic.unlock_hint) || "Сначала пройдите половину задач предыдущей темы.";
    setStatus("error", "Тема закрыта");
    setOutput(hint, true);
  },

  onModeChange() {
    if (!this.authenticated) {
      this.mode = "sandbox";
      this.applyMode();
      return;
    }
    this.mode = this.modeSelect.value;
    this.applyMode();
  },

  applyMode() {
    const isTopic = this.mode === "topic";

    if (this.modeSelect && this.modeSelect.value !== this.mode) {
      this.modeSelect.value = this.mode;
    }

    this.updateTaskChrome();

    if (!isTopic) {
      this.topicId = "";
      this.taskId = "";
      if (this.topicSelect) this.topicSelect.value = "";
      if (this.taskSelect) {
        this.taskSelect.innerHTML = '<option value="">Выберите задачу</option>';
        this.setSelectDisabled(this.taskSelect, true);
      }
      this.closeTopicGuide();
      return;
    }

    if (this.topicSelect) this.setSelectDisabled(this.topicSelect, false);
    this.topicId = this.topicSelect ? this.topicSelect.value || "" : "";
    if (this.topicId) {
      this.onTopicChange();
    } else {
      this.showTopicIntro();
    }
  },

  showTopicIntro() {
    this.taskId = "";
    if (this.taskSelect) this.taskSelect.value = "";

    if (this.taskTitle) this.taskTitle.textContent = "Задача";
    this.setCondition("");
    this.setHint("");
    if (this.taskMeta) this.taskMeta.textContent = "";
    if (this.btnPrev) this.btnPrev.disabled = true;
    if (this.btnNext) this.btnNext.disabled = true;

    this.updateTaskChrome();
  },

  async onTopicChange() {
    this.topicId = this.topicSelect.value;
    this.taskId = "";
    this.taskSelect.innerHTML = '<option value="">Выберите задачу</option>';
    this.setSelectDisabled(this.taskSelect, !this.topicId);

    if (!this.topicId) {
      this.showTopicIntro();
      return;
    }

    const topicMeta = this.getTopicById(this.topicId);
    if (topicMeta && !topicMeta.unlocked) {
      this.showTopicLockedMessage(topicMeta);
      return;
    }

    StepDebugger.stop();
    if (typeof CodeEditor !== "undefined") CodeEditor.leaveEditMode();
    workspace.clear();
    ProgramFrame.setup(workspace);
    updateCodePreview();
    setStatus("idle", "Готов");
    setOutput("Тема выбрана. Откройте задачу и соберите решение.", false);

    try {
      const response = await fetch("/api/topics/" + encodeURIComponent(this.topicId) + "/tasks");
      const data = await response.json();
      if (response.status === 403 && data.locked) {
        this.showTopicLockedMessage(data);
        return;
      }
      if (!response.ok) {
        throw new Error(data.error || "Не удалось загрузить задачи");
      }
      this.tasks = data.tasks || [];
      this.tasks.forEach(function (task, index) {
        const option = document.createElement("option");
        option.value = task.id;
        option.textContent = index + 1 + ". " + task.title;
        TopicsUI.taskSelect.appendChild(option);
      });
      this.refreshSelect(this.taskSelect);
      this.showTopicIntro();
    } catch (err) {
      setOutput("Не удалось загрузить задачи: " + err.message, true);
    }
  },

  onTaskChange() {
    const self = this;
    this.taskId = this.taskSelect.value;
    if (!this.taskId) {
      this.showTopicIntro();
      return;
    }

    StepDebugger.stop();
    if (typeof CodeEditor !== "undefined") CodeEditor.leaveEditMode();
    workspace.clear();
    ProgramFrame.setup(workspace);

    const task = this.tasks.find(function (t) {
      return t.id === self.taskId;
    });

    this.loadSavedSolution().then(function (loaded) {
      if (!loaded && task && task.starter_xml) {
        loadWorkspaceXml(workspace, task.starter_xml);
        setStatus("idle", "Готов");
        setOutput(
          "Загружена программа с ошибкой. Исправьте блоки и нажмите «Проверить».",
          false
        );
      } else if (loaded) {
        setStatus("idle", "Готов");
        setOutput("Загружено сохранённое решение из блоков. Можно изменить и проверить снова.", false);
      } else {
        setStatus("idle", "Готов");
        setOutput("Задача загружена. Соберите решение и нажмите «Проверить».", false);
      }
      updateCodePreview();
      if (typeof scheduleWorkspaceLayoutRefresh === "function") {
        scheduleWorkspaceLayoutRefresh();
      }
    });

    if (!task) return;

    const index = this.tasks.indexOf(task);
    if (this.taskTitle) this.taskTitle.textContent = task.title;
    this.setCondition(task.condition);
    this.setHint(task.hint || "");
    if (this.taskMeta) {
      this.taskMeta.textContent = "Задача " + (index + 1) + " из " + this.tasks.length;
    }
    this.updateTaskChrome();
    this.updateNavButtons();
  },

  async loadSavedSolution() {
    if (!this.topicId || !this.taskId) return false;

    try {
      const response = await fetch(
        "/api/progress/" +
          encodeURIComponent(this.topicId) +
          "/" +
          encodeURIComponent(this.taskId)
      );
      if (!response.ok) return false;

      const data = await response.json();
      if (!data.solution_xml) return false;

      return loadWorkspaceXml(workspace, data.solution_xml);
    } catch (err) {
      console.error("loadSavedSolution:", err);
      return false;
    }
  },

  navigateTask(delta) {
    if (!this.tasks.length || !this.taskId) return;
    const index = this.tasks.findIndex(function (t) {
      return t.id === TopicsUI.taskId;
    });
    const next = index + delta;
    if (next < 0 || next >= this.tasks.length) return;
    this.taskSelect.value = this.tasks[next].id;
    this.refreshSelect(this.taskSelect);
    this.onTaskChange();
  },

  updateNavButtons() {
    if (!this.btnPrev || !this.btnNext) return;
    const index = this.tasks.findIndex(function (t) {
      return t.id === TopicsUI.taskId;
    });
    this.btnPrev.disabled = index <= 0;
    this.btnNext.disabled = index < 0 || index >= this.tasks.length - 1;
  },

  async checkSolution() {
    if (this.mode !== "topic" || !this.topicId || !this.taskId) return;

    if (typeof CodeEditor !== "undefined" && CodeEditor.isEditMode()) {
      setStatus("error", "Ошибка");
      setOutput("Перед проверкой нажмите «Собрать», чтобы синхронизировать код с рабочей областью.", true);
      return;
    }

    const code = generatePythonCode(workspace);
    const blocksXml = typeof serializeWorkspace === "function" ? serializeWorkspace(workspace) : "";
    if (!code.trim()) {
      setStatus("error", "Ошибка");
      setOutput("Сначала соберите программу из блоков.", true);
      return;
    }

    setStatus("running", "Проверка…");
    setOutput("Проверяем решение…", false);

    try {
      const response = await fetch("/api/check", {
        method: "POST",
        headers: getJsonHeaders(),
        body: JSON.stringify({
          code: code,
          topic_id: this.topicId,
          task_id: this.taskId,
          blocks_xml: blocksXml,
        }),
      });
      const result = await response.json();
      const limitMsg = getApiErrorMessage(result, response);
      if (limitMsg) {
        setStatus("error", "Подождите");
        setOutput(limitMsg, true);
        return;
      }

      if (result.success) {
        setStatus("success", "Верно!");
        let msg = result.message;
        if (result.progress) {
          msg += "\n\nПопыток: " + result.progress.attempts_count;
          if (result.progress.completed) {
            msg += " · Прогресс сохранён";
          }
        }
        setOutput(msg, false);
        await this.loadTopics();
        if (this.topicSelect && this.topicId) {
          this.topicSelect.value = this.topicId;
          this.refreshSelect(this.topicSelect);
        }
      } else {
        if (result.locked) {
          setStatus("error", "Тема закрыта");
          setOutput(result.message || "Тема ещё не открыта", true);
          await this.loadTopics();
          return;
        }
        setStatus("error", "Неверно");
        let text = result.message || "Решение не прошло проверку";
        if (result.details && result.details.length) {
          const failed = result.details.find(function (d) {
            return !d.passed;
          });
          if (failed && failed.actual !== undefined) {
            text += "\n\nОжидалось:\n" + failed.expected + "\n\nПолучено:\n" + failed.actual;
          } else if (failed && failed.message) {
            text += "\n\n" + failed.message;
          }
        }
        setOutput(text, true);
      }
    } catch (err) {
      setStatus("error", "Ошибка");
      setOutput("Ошибка проверки: " + err.message, true);
    }
  },
};
