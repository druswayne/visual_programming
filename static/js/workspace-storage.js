/**
 * Сохранение и загрузка Blockly-рабочей области.
 */
const WorkspaceStorage = {
  serialize(workspace) {
    if (!workspace || typeof Blockly === "undefined") return "";

    try {
      if (Blockly.Xml && Blockly.Xml.workspaceToDom && Blockly.Xml.domToText) {
        return Blockly.Xml.domToText(Blockly.Xml.workspaceToDom(workspace));
      }
      if (Blockly.utils && Blockly.utils.xml && Blockly.utils.xml.workspaceToDom) {
        const dom = Blockly.utils.xml.workspaceToDom(workspace);
        return Blockly.utils.xml.domToText(dom);
      }
    } catch (err) {
      console.error("WorkspaceStorage.serialize:", err);
    }
    return "";
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

  domToWorkspace(xmlDom, workspace) {
    if (Blockly.Xml && Blockly.Xml.domToWorkspace) {
      return Blockly.Xml.domToWorkspace(xmlDom, workspace);
    }
    if (Blockly.serialization && Blockly.serialization.blocks && Blockly.serialization.blocks.append) {
      return Blockly.serialization.blocks.append(xmlDom, workspace);
    }
    throw new Error("Blockly workspace loader unavailable");
  },

  load(workspace, xmlString, options) {
    if (!workspace || !xmlString || typeof Blockly === "undefined") return false;

    const skipOrphans = options && options.skipIntegrateOrphans;

    try {
      workspace.clear();
      const xmlDom = this.textToDom(xmlString);
      this.domToWorkspace(xmlDom, workspace);
      if (typeof ProgramFrame !== "undefined") {
        ProgramFrame.ensure(workspace);
        ProgramFrame.decorateFrameBlocks(workspace);
        ProgramFrame.updateDetachedStyles(workspace);
        ProgramFrame.bindWorkspaceListener(workspace);
        if (!skipOrphans) {
          ProgramFrame.integrateOrphans(workspace);
        }
        const start = ProgramFrame.findStart(workspace);
        const end = ProgramFrame.findEnd(workspace);
        if (end && start && !ProgramFrame.isEndInChain(end, start)) {
          ProgramFrame.parkEnd(end);
        }
      }
      if (!options || options.focus !== false) {
        WorkspaceStorage.focusContent(workspace);
      }
      return true;
    } catch (err) {
      console.error("WorkspaceStorage.load:", err);
      workspace.clear();
      if (typeof ProgramFrame !== "undefined") {
        ProgramFrame.setup(workspace);
      }
      return false;
    }
  },

  focusContent(workspace) {
    if (!workspace) return;

    const start =
      typeof ProgramFrame !== "undefined" ? ProgramFrame.findStart(workspace) : null;
    const topBlocks = workspace.getTopBlocks(true);
    const block = start || (topBlocks.length ? topBlocks[0] : null);
    if (!block) return;

    const center = function () {
      if (typeof workspace.scroll === "function") {
        workspace.scroll(0, 0);
      }
      if (typeof workspace.centerOnBlock === "function") {
        workspace.centerOnBlock(block.id);
      }
      if (typeof scheduleWorkspaceLayoutRefresh === "function") {
        scheduleWorkspaceLayoutRefresh();
      } else if (typeof Blockly !== "undefined") {
        Blockly.svgResize(workspace);
        if (typeof ScratchToolbox !== "undefined") ScratchToolbox.onResize();
      } else if (typeof workspace.resize === "function") {
        workspace.resize();
      }
    };

    if (typeof requestAnimationFrame === "function") {
      requestAnimationFrame(center);
    } else {
      setTimeout(center, 0);
    }
  },
};

function serializeWorkspace(workspace) {
  return WorkspaceStorage.serialize(workspace);
}

function loadWorkspaceXml(workspace, xmlString) {
  return WorkspaceStorage.load(workspace, xmlString);
}
