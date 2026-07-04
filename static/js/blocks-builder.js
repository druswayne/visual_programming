/**
 * Загрузка Blockly-программы из XML (импорт Python → блоки).
 */
const BlocksBuilder = {
  cleanupStrayBlocks(workspace) {
    const start = ProgramFrame.findStart(workspace);
    if (!start) return;
    const connectedIds = ProgramFrame.collectProgramBlockIds(start);
    workspace.getAllBlocks(false).forEach(function (block) {
      if (connectedIds.has(block.id)) return;
      if (block.type === "py_start" || block.type === "py_end") return;
      if (block.outputConnection) return;
      if (block.getParent && block.getParent()) return;
      block.dispose(false);
    });
  },

  applyProgram(workspace, program, xml) {
    if (!workspace) return false;
    if (!xml || typeof xml !== "string" || !xml.trim()) {
      throw new Error(t("builder.no_xml"));
    }

    if (typeof setCodePreviewSuppressed === "function") {
      setCodePreviewSuppressed(true);
    }

    const wasEnabled = Blockly.Events.isEnabled();
    Blockly.Events.disable();
    Blockly.Events.setGroup(true);
    try {
      const loaded = WorkspaceStorage.load(workspace, xml, { skipIntegrateOrphans: true });
      if (!loaded) {
        throw new Error(t("builder.load_failed"));
      }
      if (typeof ProgramFrame !== "undefined") {
        ProgramFrame.consolidateEndBlocks(workspace);
        ProgramFrame.decorateFrameBlocks(workspace);
        ProgramFrame.updateDetachedStyles(workspace);
        BlocksBuilder.cleanupStrayBlocks(workspace);
      }
    } catch (err) {
      console.error("BlocksBuilder.applyProgram:", err);
      throw err;
    } finally {
      Blockly.Events.setGroup(false);
      if (wasEnabled) Blockly.Events.enable();
      if (typeof setCodePreviewSuppressed === "function") {
        setCodePreviewSuppressed(false);
      }
    }

    workspace.render();
    if (typeof Blockly !== "undefined" && typeof Blockly.svgResize === "function") {
      Blockly.svgResize(workspace);
    }
    return true;
  },
};
