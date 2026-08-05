/**
 * Сохранение и загрузка программ в режиме песочницы.
 */
const SandboxSavesUI = {
  currentId: null,
  currentTitle: "",
  saves: [],
  limit: 20,
  busy: false,
  pendingDeleteId: null,
  pendingDeleteTitle: "",

  init() {
    this.bar = document.getElementById("sandboxSavesBar");
    this.titleEl = document.getElementById("sandboxSaveTitle");
    this.btnSave = document.getElementById("btnSandboxSave");
    this.btnOpen = document.getElementById("btnSandboxOpen");
    this.modal = document.getElementById("sandboxSavesModal");
    this.modalTitle = document.getElementById("sandboxSavesModalTitle");
    this.modalClose = document.getElementById("sandboxSavesModalClose");
    this.form = document.getElementById("sandboxSaveForm");
    this.nameInput = document.getElementById("sandboxSaveNameInput");
    this.btnSaveConfirm = document.getElementById("btnSandboxSaveConfirm");
    this.btnSaveAsNew = document.getElementById("btnSandboxSaveAsNew");
    this.listEl = document.getElementById("sandboxSavesList");
    this.emptyEl = document.getElementById("sandboxSavesEmpty");
    this.countEl = document.getElementById("sandboxSavesCount");
    this.mainView = document.getElementById("sandboxSavesMainView");
    this.deleteView = document.getElementById("sandboxSavesDeleteView");
    this.deleteText = document.getElementById("sandboxSavesDeleteText");
    this.btnDeleteCancel = document.getElementById("btnSandboxDeleteCancel");
    this.btnDeleteConfirm = document.getElementById("btnSandboxDeleteConfirm");
    this._defaultModalTitle = this.modalTitle ? this.modalTitle.textContent : "";

    if (!this.bar) return;

    if (this.btnSave) {
      this.btnSave.addEventListener("click", () => this.openModal("save"));
    }
    if (this.btnOpen) {
      this.btnOpen.addEventListener("click", () => this.openModal("list"));
    }
    if (this.modalClose) {
      this.modalClose.addEventListener("click", () => this.closeModal());
    }
    if (this.modal) {
      this.modal.addEventListener("click", (event) => {
        if (event.target === this.modal) this.closeModal();
      });
    }
    if (this.form) {
      this.form.addEventListener("submit", (event) => {
        event.preventDefault();
        this.saveCurrent({ asNew: false });
      });
    }
    if (this.btnSaveAsNew) {
      this.btnSaveAsNew.addEventListener("click", () => this.saveCurrent({ asNew: true }));
    }
    if (this.listEl) {
      this.listEl.addEventListener("click", (event) => this.onListClick(event));
    }
    if (this.btnDeleteCancel) {
      this.btnDeleteCancel.addEventListener("click", () => this.hideDeleteConfirm());
    }
    if (this.btnDeleteConfirm) {
      this.btnDeleteConfirm.addEventListener("click", () => this.confirmDelete());
    }

    document.addEventListener("keydown", (event) => {
      if (event.key !== "Escape" || !this.modal || this.modal.hidden) return;
      if (this.pendingDeleteId) {
        this.hideDeleteConfirm();
        return;
      }
      this.closeModal();
    });

    this.setVisible(false);
  },

  setVisible(visible) {
    if (!this.bar) return;
    this.bar.hidden = !visible;
    if (!visible) {
      this.closeModal();
    }
  },

  clearCurrent() {
    this.currentId = null;
    this.currentTitle = "";
    this.updateTitleBadge();
  },

  setCurrent(save) {
    if (!save) {
      this.clearCurrent();
      return;
    }
    this.currentId = save.id;
    this.currentTitle = save.title || "";
    this.updateTitleBadge();
  },

  updateTitleBadge() {
    if (!this.titleEl) return;
    if (this.currentTitle) {
      this.titleEl.textContent = this.currentTitle;
      this.titleEl.hidden = false;
      this.titleEl.title = this.currentTitle;
    } else {
      this.titleEl.textContent = "";
      this.titleEl.hidden = true;
      this.titleEl.title = "";
    }
  },

  syncSaveAsNewButton() {
    if (!this.btnSaveAsNew) return;
    this.btnSaveAsNew.hidden = !this.currentId;
  },

  async openModal(focus) {
    if (!this.modal) return;
    this.hideDeleteConfirm();
    this.modal.hidden = false;
    document.body.style.overflow = "hidden";
    if (this.nameInput) {
      this.nameInput.value = this.currentTitle || "";
    }
    this.syncSaveAsNewButton();
    await this.refreshList();
    if (focus === "save" && this.nameInput) {
      this.nameInput.focus();
      this.nameInput.select();
    }
  },

  closeModal() {
    if (!this.modal || this.modal.hidden) return;
    this.hideDeleteConfirm();
    this.modal.hidden = true;
    document.body.style.overflow = "";
  },

  showDeleteConfirm(saveId, title) {
    this.pendingDeleteId = saveId;
    this.pendingDeleteTitle = title;
    if (this.deleteText) {
      this.deleteText.textContent = t("sandbox.delete_confirm", "Удалить сохранение «{title}»?", {
        title: title,
      });
    }
    if (this.modalTitle) {
      this.modalTitle.textContent = t("sandbox.delete_confirm_title", "Удаление сохранения");
    }
    if (this.mainView) this.mainView.hidden = true;
    if (this.deleteView) this.deleteView.hidden = false;
    if (this.btnDeleteConfirm) this.btnDeleteConfirm.focus();
  },

  hideDeleteConfirm() {
    this.pendingDeleteId = null;
    this.pendingDeleteTitle = "";
    if (this.mainView) this.mainView.hidden = false;
    if (this.deleteView) this.deleteView.hidden = true;
    if (this.modalTitle && this._defaultModalTitle) {
      this.modalTitle.textContent = this._defaultModalTitle;
    }
  },

  escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  },

  formatDate(iso) {
    if (!iso) return "";
    try {
      const date = new Date(iso);
      if (Number.isNaN(date.getTime())) return "";
      return date.toLocaleString(undefined, {
        day: "2-digit",
        month: "short",
        hour: "2-digit",
        minute: "2-digit",
      });
    } catch (err) {
      return "";
    }
  },

  async refreshList() {
    if (!this.listEl) return;
    this.listEl.innerHTML = '<p class="sandbox-saves-empty">' + t("sandbox.loading") + "</p>";
    if (this.emptyEl) this.emptyEl.hidden = true;

    try {
      const response = await fetch("/api/sandbox/saves");
      const data = await response.json();
      if (!response.ok || !data.success) {
        throw new Error(data.error || t("sandbox.load_error"));
      }
      this.saves = data.saves || [];
      this.limit = data.limit || 20;
      this.renderList();
    } catch (err) {
      console.error("SandboxSavesUI.refreshList:", err);
      this.listEl.innerHTML =
        '<p class="sandbox-saves-empty sandbox-saves-empty--error">' +
        this.escapeHtml(err.message || t("sandbox.load_error")) +
        "</p>";
      if (this.countEl) this.countEl.textContent = "";
    }
  },

  renderList() {
    if (!this.listEl) return;

    if (this.countEl) {
      this.countEl.textContent = t("sandbox.count", "{count} / {limit}", {
        count: this.saves.length,
        limit: this.limit,
      });
    }

    if (!this.saves.length) {
      this.listEl.innerHTML = "";
      if (this.emptyEl) this.emptyEl.hidden = false;
      return;
    }

    if (this.emptyEl) this.emptyEl.hidden = true;

    const self = this;
    this.listEl.innerHTML = this.saves
      .map(function (save) {
        const active = self.currentId === save.id ? " is-active" : "";
        const updated = self.formatDate(save.updated_at);
        return (
          '<article class="sandbox-saves-item' +
          active +
          '" data-save-id="' +
          save.id +
          '">' +
          '<div class="sandbox-saves-item__info">' +
          '<strong class="sandbox-saves-item__title">' +
          self.escapeHtml(save.title) +
          "</strong>" +
          (updated
            ? '<span class="sandbox-saves-item__meta">' + self.escapeHtml(updated) + "</span>"
            : "") +
          "</div>" +
          '<div class="sandbox-saves-item__actions">' +
          '<button type="button" class="btn btn--small btn--primary" data-action="open">' +
          t("sandbox.open") +
          "</button>" +
          '<button type="button" class="btn btn--small btn--ghost" data-action="delete">' +
          t("sandbox.delete") +
          "</button>" +
          "</div>" +
          "</article>"
        );
      })
      .join("");
  },

  getWorkspacePayload() {
    if (typeof workspace === "undefined" || !workspace) {
      return { error: t("sandbox.no_workspace") };
    }
    if (typeof CodeEditor !== "undefined" && CodeEditor.isEditMode()) {
      return { error: t("sandbox.sync_code_first") };
    }
    const blocksXml =
      typeof serializeWorkspace === "function" ? serializeWorkspace(workspace) : "";
    if (!blocksXml || !blocksXml.trim()) {
      return { error: t("sandbox.empty_workspace") };
    }
    const code =
      typeof generatePythonCode === "function" ? generatePythonCode(workspace) : "";
    return { blocksXml: blocksXml, code: code };
  },

  async saveCurrent(options) {
    if (this.busy) return;
    const asNew = options && options.asNew;
    const title = this.nameInput ? this.nameInput.value.trim() : "";
    if (!title) {
      setStatus("error", t("status.error"));
      setOutput(t("sandbox.title_required"), true);
      if (this.nameInput) this.nameInput.focus();
      return;
    }

    const payload = this.getWorkspacePayload();
    if (payload.error) {
      setStatus("error", t("status.error"));
      setOutput(payload.error, true);
      return;
    }

    const updateExisting = !asNew && this.currentId;
    this.busy = true;
    if (this.btnSaveConfirm) this.btnSaveConfirm.disabled = true;
    if (this.btnSaveAsNew) this.btnSaveAsNew.disabled = true;

    try {
      const url = updateExisting
        ? "/api/sandbox/saves/" + encodeURIComponent(this.currentId)
        : "/api/sandbox/saves";
      const response = await fetch(url, {
        method: updateExisting ? "PUT" : "POST",
        headers: getJsonHeaders(),
        body: JSON.stringify({
          title: title,
          blocks_xml: payload.blocksXml,
          code: payload.code,
        }),
      });
      const data = await response.json();
      if (!response.ok || !data.success) {
        throw new Error(data.error || t("sandbox.save_error"));
      }

      this.setCurrent(data.save);
      this.syncSaveAsNewButton();
      await this.refreshList();
      setStatus("success", t("status.success"));
      setOutput(
        updateExisting ? t("sandbox.updated", "Сохранение «{title}» обновлено.", { title: data.save.title }) : t("sandbox.saved", "Сохранение «{title}» создано.", { title: data.save.title }),
        false
      );
    } catch (err) {
      console.error("SandboxSavesUI.saveCurrent:", err);
      setStatus("error", t("status.error"));
      setOutput(err.message || t("sandbox.save_error"), true);
    } finally {
      this.busy = false;
      if (this.btnSaveConfirm) this.btnSaveConfirm.disabled = false;
      if (this.btnSaveAsNew) this.btnSaveAsNew.disabled = false;
    }
  },

  async onListClick(event) {
    const button = event.target.closest("button[data-action]");
    if (!button || this.busy) return;
    const item = button.closest("[data-save-id]");
    if (!item) return;
    const saveId = parseInt(item.getAttribute("data-save-id"), 10);
    if (!saveId) return;

    const action = button.getAttribute("data-action");
    if (action === "open") {
      await this.loadSave(saveId);
    } else if (action === "delete") {
      const save = this.saves.find(function (s) {
        return s.id === saveId;
      });
      const title = save ? save.title : "#" + saveId;
      this.showDeleteConfirm(saveId, title);
    }
  },

  async loadSave(saveId) {
    if (this.busy) return;
    this.busy = true;
    try {
      const response = await fetch("/api/sandbox/saves/" + encodeURIComponent(saveId));
      const data = await response.json();
      if (!response.ok || !data.success || !data.save) {
        throw new Error(data.error || t("sandbox.load_error"));
      }

      if (typeof StepDebugger !== "undefined") StepDebugger.stop();
      if (typeof CodeEditor !== "undefined") CodeEditor.leaveEditMode();

      const loaded =
        typeof loadWorkspaceXml === "function"
          ? loadWorkspaceXml(workspace, data.save.blocks_xml)
          : false;
      if (!loaded) {
        throw new Error(t("sandbox.load_workspace_error"));
      }

      this.setCurrent(data.save);
      if (this.nameInput) this.nameInput.value = data.save.title || "";
      this.syncSaveAsNewButton();

      if (typeof updateCodePreview === "function") updateCodePreview();
      if (typeof scheduleWorkspaceLayoutRefresh === "function") {
        scheduleWorkspaceLayoutRefresh();
      }

      this.closeModal();
      setStatus("idle", t("status.ready"));
      setOutput(
        t("sandbox.loaded", "Загружено сохранение «{title}».", { title: data.save.title }),
        false
      );
    } catch (err) {
      console.error("SandboxSavesUI.loadSave:", err);
      setStatus("error", t("status.error"));
      setOutput(err.message || t("sandbox.load_error"), true);
    } finally {
      this.busy = false;
    }
  },

  async confirmDelete() {
    if (this.busy || !this.pendingDeleteId) return;
    const saveId = this.pendingDeleteId;
    const title = this.pendingDeleteTitle || "#" + saveId;

    this.busy = true;
    if (this.btnDeleteConfirm) this.btnDeleteConfirm.disabled = true;
    if (this.btnDeleteCancel) this.btnDeleteCancel.disabled = true;

    try {
      const response = await fetch("/api/sandbox/saves/" + encodeURIComponent(saveId), {
        method: "DELETE",
        headers: getJsonHeaders(),
      });
      const data = await response.json();
      if (!response.ok || !data.success) {
        throw new Error(data.error || t("sandbox.delete_error"));
      }

      if (this.currentId === saveId) {
        this.clearCurrent();
        if (this.nameInput) this.nameInput.value = "";
        this.syncSaveAsNewButton();
      }
      this.hideDeleteConfirm();
      await this.refreshList();
      setStatus("success", t("status.success"));
      setOutput(t("sandbox.deleted", "Сохранение «{title}» удалено.", { title: title }), false);
    } catch (err) {
      console.error("SandboxSavesUI.confirmDelete:", err);
      setStatus("error", t("status.error"));
      setOutput(err.message || t("sandbox.delete_error"), true);
    } finally {
      this.busy = false;
      if (this.btnDeleteConfirm) this.btnDeleteConfirm.disabled = false;
      if (this.btnDeleteCancel) this.btnDeleteCancel.disabled = false;
    }
  },
};
