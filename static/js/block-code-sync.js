/**
 * Синхронная подсветка блок ↔ Python-код.
 * При выборе/перетаскивании блока подсвечивается соответствующий фрагмент кода.
 */
const BlockCodeSync = {
  workspace: null,
  plainCode: "",
  mappings: {},
  frozenCode: "",
  frozenMappings: {},
  lastStableCode: "",
  lastStableMappings: {},
  activeBlockId: null,
  activeBlockIds: [],
  highlightSlot: null,
  isDragging: false,
  enabled: true,

  init(workspace) {
    this.workspace = workspace;
    workspace.addChangeListener(this.onWorkspaceChange.bind(this));
  },

  isBlocked() {
    if (typeof StepDebugger !== "undefined" && (StepDebugger.sessionActive || StepDebugger.loading)) {
      return true;
    }
    if (typeof CodeEditor !== "undefined" && CodeEditor.isEditMode()) {
      return true;
    }
    if (typeof suppressCodePreview !== "undefined" && suppressCodePreview) {
      return true;
    }
    return false;
  },

  cloneMappings(source) {
    const out = {};
    Object.keys(source || {}).forEach(function (id) {
      out[id] = JSON.parse(JSON.stringify(source[id]));
    });
    return out;
  },

  /** Блоки, которые «захватываются» вместе с выбранным (цепочка next + тела вложенных веток). */
  collectCapturedBlockIds(block) {
    if (!block) return [];
    const ids = [];
    const seen = new Set();

    function visitChain(start) {
      let current = start;
      while (current && !seen.has(current.id)) {
        seen.add(current.id);
        ids.push(current.id);

        current.inputList.forEach(function (input) {
          if (input.type === Blockly.NEXT_STATEMENT) {
            visitChain(current.getInputTargetBlock(input.name));
          }
        });

        current = current.getNextBlock();
      }
    }

    visitChain(block);
    return ids;
  },

  resolveBlock(blockId, workspaceId) {
    if (!blockId || !this.workspace) return null;
    if (workspaceId && workspaceId !== this.workspace.id) {
      const flyout = this.workspace.getToolbox && this.workspace.getToolbox();
      const fo = flyout && flyout.getFlyout ? flyout.getFlyout() : null;
      const fw = fo && fo.getWorkspace ? fo.getWorkspace() : null;
      if (fw && fw.id === workspaceId) {
        return fw.getBlockById(blockId);
      }
    }
    return this.workspace.getBlockById(blockId);
  },

  setActiveBlocks(primaryBlockId, workspaceId) {
    this.activeBlockId = primaryBlockId || null;
    if (!primaryBlockId) {
      this.activeBlockIds = [];
      return;
    }
    const block = this.resolveBlock(primaryBlockId, workspaceId || this.workspace.id);
    this.activeBlockIds = block ? this.collectCapturedBlockIds(block) : [primaryBlockId];
  },

  rebuild() {
    if (this.isDragging) return;

    const prevCode = this.plainCode;
    const prevMappings = this.cloneMappings(this.mappings);

    if (!this.workspace || typeof generatePythonCodeWithMapping !== "function") {
      this.lastStableCode = prevCode;
      this.lastStableMappings = prevMappings;
      this.plainCode =
        typeof generatePythonCode === "function"
          ? generatePythonCode(this.workspace)
          : "";
      this.mappings = {};
      this.frozenCode = this.plainCode;
      this.frozenMappings = this.cloneMappings(this.mappings);
      return;
    }

    const result = generatePythonCodeWithMapping(this.workspace);
    this.lastStableCode = prevCode;
    this.lastStableMappings = prevMappings;
    this.plainCode = result.code || "";
    this.mappings = result.mappings || {};

    const activeStillMapped =
      !this.activeBlockId ||
      this.activeBlockIds.some(function (id) {
        return !!this.mappings[id];
      }, this);

    if (activeStillMapped) {
      this.frozenCode = this.plainCode;
      this.frozenMappings = this.cloneMappings(this.mappings);
    }
  },

  beginDrag(blockId, workspaceId) {
    this.isDragging = true;
    this.highlightSlot = null;
    this.setActiveBlocks(blockId, workspaceId);

    if (this.mappings[blockId]) {
      this.frozenCode = this.plainCode;
      this.frozenMappings = this.cloneMappings(this.mappings);
    } else if (this.lastStableMappings[blockId]) {
      this.frozenCode = this.lastStableCode;
      this.frozenMappings = this.cloneMappings(this.lastStableMappings);
    }

    this.render();
  },

  endDrag() {
    this.isDragging = false;
    this.rebuild();
    this.render();
  },

  onWorkspaceChange(event) {
    if (!this.enabled || this.isBlocked()) return;

    const type = event.type;

    if (type === Blockly.Events.BLOCK_DRAG) {
      if (event.isStart) {
        this.beginDrag(event.blockId, event.workspaceId);
      } else {
        this.endDrag();
      }
      return;
    }

    if (this.isDragging) {
      return;
    }

    if (type === Blockly.Events.BLOCK_MOVE) {
      if (event.newInputName === "COND" || event.newInputName === "IF0" || event.newInputName === "VALUE") {
        this.highlightSlot = event.newInputName;
        this.setActiveBlocks(event.newParentId || event.blockId);
      }
      this.rebuild();
      this.render();
      return;
    }

    if (type === Blockly.Events.SELECTED) {
      this.highlightSlot = null;
      this.setActiveBlocks(event.newElementId || null);
      this.rebuild();
      this.render();
      return;
    }

    const rebuildTypes = [
      Blockly.Events.BLOCK_MOVE,
      Blockly.Events.BLOCK_CHANGE,
      Blockly.Events.BLOCK_CREATE,
      Blockly.Events.BLOCK_DELETE,
      Blockly.Events.CHANGE,
      Blockly.Events.FINISHED_LOADING,
    ];

    if (rebuildTypes.indexOf(type) >= 0) {
      this.rebuild();
      this.render();
    }
  },

  getMappingForBlock(blockId) {
    if (!blockId) return null;
    const source = this.isDragging ? this.frozenMappings : this.mappings;
    if (source[blockId]) return source[blockId];

    const block = this.resolveBlock(blockId);
    if (block && typeof block.getSurroundParent === "function") {
      let parent = block.getSurroundParent();
      while (parent) {
        if (source[parent.id]) return source[parent.id];
        parent = parent.getSurroundParent();
      }
    }
    return null;
  },

  getHighlightRangesForBlock(blockId) {
    const ranges = [];
    if (!blockId) return ranges;

    const isPrimary = blockId === this.activeBlockId;
    const mapping = this.getMappingForBlock(blockId);
    if (!mapping) return ranges;

    if (mapping.kind === "expression" && mapping.start != null) {
      ranges.push({
        line: mapping.line,
        start: mapping.start,
        end: mapping.end,
        kind: "expression",
      });
      return ranges;
    }

    if (mapping.statement) {
      ranges.push({
        line: mapping.line,
        start: mapping.statement.start,
        end: mapping.statement.end,
        kind: "expression",
      });
      return ranges;
    }

    if (isPrimary && this.highlightSlot && mapping.slots && mapping.slots[this.highlightSlot]) {
      const s = mapping.slots[this.highlightSlot];
      ranges.push({
        line: mapping.line,
        start: s.start,
        end: s.end,
        kind: "expression",
      });
      return ranges;
    }

    if (mapping.keyword) {
      ranges.push({
        line: mapping.line,
        start: mapping.keyword.start,
        end: mapping.keyword.end,
        kind: "keyword",
      });
      return ranges;
    }

    const slotKeys = Object.keys(mapping.slots || {});
    if (slotKeys.length === 1) {
      const s = mapping.slots[slotKeys[0]];
      ranges.push({
        line: mapping.line,
        start: s.start,
        end: s.end,
        kind: "expression",
      });
    }

    return ranges;
  },

  getAllHighlightRanges() {
    const merged = [];
    const seen = new Set();

    this.activeBlockIds.forEach(function (blockId) {
      this.getHighlightRangesForBlock(blockId).forEach(function (range) {
        const key = range.line + ":" + range.start + "-" + range.end;
        if (seen.has(key)) return;
        seen.add(key);
        merged.push(range);
      });
    }, this);

    merged.sort(function (a, b) {
      return a.line - b.line || a.start - b.start;
    });

    return merged;
  },

  render() {
    const nodes = typeof getCodePreviewNodes === "function" ? getCodePreviewNodes() : null;
    if (!nodes) return;

    const codeSource = this.isDragging ? this.frozenCode : this.plainCode;
    const displayCode = codeSource.trim() || "# Соберите программу из блоков";
    const ranges = this.getAllHighlightRanges();

    if (typeof PythonHighlighter !== "undefined" && ranges.length) {
      nodes.codeEl.innerHTML = PythonHighlighter.highlightWithRanges(displayCode, ranges);
      this.scrollToFirstRange(ranges);
    } else if (typeof PythonHighlighter !== "undefined") {
      nodes.codeEl.innerHTML = PythonHighlighter.highlight(displayCode);
    } else {
      nodes.codeEl.textContent = displayCode;
    }
  },

  scrollToFirstRange(ranges) {
    if (!ranges.length) return;
    const nodes = typeof getCodePreviewNodes === "function" ? getCodePreviewNodes() : null;
    if (!nodes) return;
    const mark = nodes.codeEl.querySelector(".py-sync-hl");
    if (mark) {
      mark.scrollIntoView({ block: "nearest", behavior: "smooth" });
    }
  },

  clearSelection() {
    this.activeBlockId = null;
    this.activeBlockIds = [];
    this.highlightSlot = null;
    this.isDragging = false;
    this.render();
  },
};
