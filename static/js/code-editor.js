/**
 * Режим редактирования Python-кода и импорт в Blockly.
 */
const CodeEditor = {
  editMode: false,
  applying: false,
  indent: "    ",

  init() {
    this.preview = document.getElementById("codePreview");
    this.wrap = document.getElementById("codeEditorWrap");
    this.editor = document.getElementById("codeEditor");
    this.highlightPre = document.getElementById("codeEditorHighlight");
    this.highlightCode =
      this.highlightPre && this.highlightPre.querySelector
        ? this.highlightPre.querySelector("code")
        : null;
    this.btnEdit = document.getElementById("btnCodeEdit");
    this.btnApply = document.getElementById("btnCodeApply");
    this.btnHelp = document.getElementById("btnCodeHelp");
    this.panelTitle = document.getElementById("codePanelTitle");
    this.codePanel = document.getElementById("codePanel");
    this.helpModal = document.getElementById("codeEditorHelpModal");
    this.helpClose = document.getElementById("codeEditorHelpClose");
    this.helpOk = document.getElementById("codeEditorHelpOk");

    if (!this.preview || !this.editor || !this.wrap) return;

    if (this.btnHelp) {
      this.btnHelp.addEventListener("click", () => this.openHelp());
    }
    if (this.helpClose) {
      this.helpClose.addEventListener("click", () => this.closeHelp());
    }
    if (this.helpOk) {
      this.helpOk.addEventListener("click", () => this.closeHelp());
    }
    if (this.helpModal) {
      this.helpModal.addEventListener("click", (event) => {
        if (event.target === this.helpModal) this.closeHelp();
      });
    }
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && this.helpModal && !this.helpModal.hidden) {
        this.closeHelp();
      }
    });

    if (this.btnEdit) {
      this.btnEdit.addEventListener("click", () => this.toggleEditMode());
    }
    if (this.btnApply) {
      this.btnApply.addEventListener("click", () => this.applyToBlocks());
    }

    this.editor.addEventListener("input", () => this.syncHighlight());
    this.editor.addEventListener("scroll", () => this.syncScroll());
    this.editor.addEventListener("keydown", (event) => this.onKeyDown(event));
  },

  isEditMode() {
    return this.editMode;
  },

  openHelp() {
    if (!this.helpModal) return;
    this.helpModal.hidden = false;
    if (this.helpOk) this.helpOk.focus();
  },

  closeHelp() {
    if (!this.helpModal) return;
    this.helpModal.hidden = true;
  },

  setEditModeUI(isEdit) {
    if (this.panelTitle) this.panelTitle.hidden = isEdit;
    if (this.codePanel) this.codePanel.classList.toggle("panel--code-editing", isEdit);
    if (this.btnApply) this.btnApply.hidden = !isEdit;
    if (this.btnEdit) {
      this.btnEdit.textContent = isEdit ? t("editor.close") : t("editor.open");
      this.btnEdit.title = isEdit ? t("editor.close_title") : t("editor.open_title");
    }
  },

  syncHighlight() {
    if (!this.highlightCode || typeof PythonHighlighter === "undefined") return;
    this.highlightCode.innerHTML = PythonHighlighter.highlight(this.editor.value);
    this.syncScroll();
  },

  syncScroll() {
    if (!this.highlightPre || !this.editor) return;
    this.highlightPre.scrollTop = this.editor.scrollTop;
    this.highlightPre.scrollLeft = this.editor.scrollLeft;
  },

  getLineIndent(line) {
    const match = line.match(/^\s*/);
    return match ? match[0] : "";
  },

  getCurrentLineInfo() {
    const value = this.editor.value;
    const pos = this.editor.selectionStart;
    const lineStart = value.lastIndexOf("\n", pos - 1) + 1;
    const nextBreak = value.indexOf("\n", pos);
    const lineEnd = nextBreak === -1 ? value.length : nextBreak;
    return {
      value: value,
      pos: pos,
      lineStart: lineStart,
      lineEnd: lineEnd,
      line: value.slice(lineStart, lineEnd),
    };
  },

  insertText(text, selectStart, selectEnd) {
    const ta = this.editor;
    const start = ta.selectionStart;
    const end = ta.selectionEnd;
    const before = ta.value.slice(0, start);
    const after = ta.value.slice(end);
    ta.value = before + text + after;
    const cursorStart = typeof selectStart === "number" ? selectStart : start + text.length;
    const cursorEnd = typeof selectEnd === "number" ? selectEnd : cursorStart;
    ta.setSelectionRange(cursorStart, cursorEnd);
    this.syncHighlight();
  },

  indentSelection() {
    const ta = this.editor;
    const start = ta.selectionStart;
    const end = ta.selectionEnd;
    const value = ta.value;

    if (start !== end) {
      const blockStart = value.lastIndexOf("\n", start - 1) + 1;
      let blockEnd = end;
      if (end > start && value[end - 1] === "\n") {
        blockEnd = end - 1;
      }
      const block = value.slice(blockStart, blockEnd);
      const indented = block
        .split("\n")
        .map((line) => this.indent + line)
        .join("\n");
      ta.value = value.slice(0, blockStart) + indented + value.slice(blockEnd);
      ta.setSelectionRange(start + this.indent.length, end + (indented.length - block.length));
      this.syncHighlight();
      return;
    }

    this.insertText(this.indent);
  },

  unindentSelection() {
    const ta = this.editor;
    const start = ta.selectionStart;
    const end = ta.selectionEnd;
    const value = ta.value;
    const blockStart = value.lastIndexOf("\n", start - 1) + 1;
    let blockEnd = end;
    if (end > start && value[end - 1] === "\n") {
      blockEnd = end - 1;
    }
    const block = value.slice(blockStart, blockEnd);
    let removed = 0;
    const lines = block.split("\n");
    const unindented = lines
      .map(function (line, index) {
        if (line.startsWith(CodeEditor.indent)) {
          removed += CodeEditor.indent.length;
          return line.slice(CodeEditor.indent.length);
        }
        if (line.startsWith("\t")) {
          removed += 1;
          return line.slice(1);
        }
        if (index === 0 && line.startsWith(" ")) {
          const spaces = line.match(/^ +/);
          if (spaces) {
            const cut = Math.min(spaces[0].length, 4);
            removed += cut;
            return line.slice(cut);
          }
        }
        return line;
      })
      .join("\n");

    ta.value = value.slice(0, blockStart) + unindented + value.slice(blockEnd);
    const nextStart = Math.max(blockStart, start - (start === blockStart ? Math.min(this.indent.length, removed) : 0));
    ta.setSelectionRange(nextStart, Math.max(nextStart, end - removed));
    this.syncHighlight();
  },

  onKeyDown(event) {
    const ta = this.editor;

    if (event.key === "Tab") {
      event.preventDefault();
      if (event.shiftKey) this.unindentSelection();
      else this.indentSelection();
      return;
    }

    if (event.key === "Enter") {
      event.preventDefault();
      const info = this.getCurrentLineInfo();
      const indent = this.getLineIndent(info.line);
      let extra = "";
      if (info.line.trimEnd().endsWith(":")) {
        extra = this.indent;
      }
      const insert = "\n" + indent + extra;
      const nextPos = info.pos + insert.length;
      this.insertText(insert, nextPos, nextPos);
      return;
    }

    if (event.key === "Backspace") {
      const start = ta.selectionStart;
      const end = ta.selectionEnd;
      if (start !== end) return;

      const lineStart = ta.value.lastIndexOf("\n", start - 1) + 1;
      const before = ta.value.slice(lineStart, start);
      if (before === this.indent || before === "\t") {
        event.preventDefault();
        const deleteStart = start - before.length;
        ta.value = ta.value.slice(0, deleteStart) + ta.value.slice(start);
        ta.setSelectionRange(deleteStart, deleteStart);
        this.syncHighlight();
      }
    }
  },

  getCode() {
    if (this.editMode && this.editor) {
      return this.editor.value;
    }
    if (typeof workspace !== "undefined" && workspace) {
      return generatePythonCode(workspace);
    }
    return "";
  },

  toggleEditMode(force) {
    const next = typeof force === "boolean" ? force : !this.editMode;
    if (next === this.editMode) return;

    this.editMode = next;
    this.setEditModeUI(next);

    if (next) {
      const code = typeof workspace !== "undefined" && workspace ? generatePythonCode(workspace) : "";
      this.editor.value = code.trim() || "";
      this.preview.hidden = true;
      this.wrap.hidden = false;
      this.syncHighlight();
      this.editor.focus();
    } else {
      this.wrap.hidden = true;
      this.preview.hidden = false;
      if (typeof updateCodePreview === "function") {
        updateCodePreview();
      }
    }
  },

  leaveEditMode() {
    if (this.editMode) this.toggleEditMode(false);
  },

  async applyToBlocks() {
    if (!this.editMode || this.applying) return;
    if (typeof workspace === "undefined" || !workspace) return;

    const code = this.editor.value.trim();
    if (!code) {
      setOutput(t("editor.enter_code"), true);
      return;
    }

    this.applying = true;
    if (this.btnApply) {
      this.btnApply.disabled = true;
      this.btnApply.textContent = t("editor.building");
    }

    try {
      const response = await fetch("/api/python-to-blocks", {
        method: "POST",
        headers: getJsonHeaders(),
        body: JSON.stringify({ code: code }),
      });
      const data = await response.json();
      const limitMsg = getApiErrorMessage(data, response);
      if (limitMsg) {
        setOutput(limitMsg, true);
        return;
      }

      if (!data.success || !data.xml) {
        const line = data.line ? t("editor.line_suffix", " (строка {line})", { line: data.line }) : "";
        setOutput((data.error || t("editor.parse_error")) + line, true);
        return;
      }

      StepDebugger.stop();
      BlocksBuilder.applyProgram(workspace, data.program, data.xml);
      this.toggleEditMode(false);
      setStatus("idle", t("status.ready"));
      setOutput(t("editor.blocks_built"), false);
      centerWorkspaceOnBlocks();
    } catch (err) {
      setOutput(t("editor.build_error", "Ошибка сборки блоков: {message}", { message: err.message }), true);
    } finally {
      this.applying = false;
      if (this.btnApply) {
        this.btnApply.disabled = false;
        this.btnApply.textContent = t("editor.build");
      }
    }
  },
};

function getActivePythonCode() {
  return CodeEditor.getCode();
}
