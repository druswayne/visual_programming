/**
 * Рамка программы: блоки «Начало» и «Конец».
 * В Python-код попадает только цепочка между ними.
 */
const ProgramFrame = {
  findStart(workspace) {
    return workspace.getAllBlocks(false).find(function (b) {
      return b.type === "py_start";
    });
  },

  isEndInChain(end, start) {
    if (!end || !start) return false;
    let cur = start.getNextBlock();
    while (cur) {
      if (cur === end) return true;
      cur = cur.getNextBlock();
    }
    return false;
  },

  isEndParked(end, workspace) {
    if (!end) return false;
    if (end._pyEndParked) return true;
    const start = this.findStart(workspace);
    return !!start && !this.isEndInChain(end, start);
  },

  parkEnd(end) {
    if (!end || end._pyEndParked) return;
    end._pyEndParked = true;
    if (end.previousConnection) {
      end._pyEndPrevCheck = end.previousConnection.getCheck();
      end.previousConnection.setCheck("__py_end_parked__");
    }
    this.decorateBlock(end);
  },

  unparkEnd(end) {
    if (!end) return;
    end._pyEndParked = false;
    if (end.previousConnection) {
      const check =
        end._pyEndPrevCheck !== undefined ? end._pyEndPrevCheck : null;
      end.previousConnection.setCheck(check);
    }
    this.decorateBlock(end);
  },

  shouldAutoConnectEnd(workspace, end) {
    if (!end || end._pyEndParked) return false;
    const start = this.findStart(workspace);
    if (!start) return true;
    return this.isEndInChain(end, start);
  },

  findEnd(workspace) {
    const ends = workspace.getAllBlocks(false).filter(function (b) {
      return b.type === "py_end";
    });
    if (!ends.length) return null;

    const start = this.findStart(workspace);
    if (start) {
      let cur = start.getNextBlock();
      while (cur) {
        if (cur.type === "py_end") return cur;
        cur = cur.getNextBlock();
      }
    }

    return ends[0];
  },

  consolidateEndBlocks(workspace) {
    const ends = workspace.getAllBlocks(false).filter(function (b) {
      return b.type === "py_end";
    });
    if (ends.length <= 1) return;

    const start = this.findStart(workspace);
    let canonicalEnd = null;

    if (start) {
      let cur = start.getNextBlock();
      while (cur) {
        if (cur.type === "py_end") {
          canonicalEnd = cur;
          break;
        }
        cur = cur.getNextBlock();
      }
    }

    if (!canonicalEnd) {
      canonicalEnd = ends[0];
    }

    ends
      .filter(function (end) {
        return end !== canonicalEnd;
      })
      .forEach(function (end) {
      const prev = end.getPreviousBlock();
      if (prev && prev.nextConnection && prev.nextConnection.targetBlock() === end) {
        prev.nextConnection.disconnect();
      }
      if (typeof end.isDisposed !== "function" || !end.isDisposed()) {
        end.dispose(false);
      }
    });
  },

  createBlock(workspace, type, x, y) {
    const block = workspace.newBlock(type);
    block.initSvg();
    block.render();
    block.moveBy(x, y);
    this.decorateBlock(block);
    return block;
  },

  decorateBlock(block) {
    if (!block || typeof block.getSvgRoot !== "function") return;
    const svg = block.getSvgRoot();
    if (!svg) return;
    svg.classList.remove("py-frame-start", "py-frame-end", "py-frame-end-parked");
    if (block.type === "py_start") svg.classList.add("py-frame-start");
    if (block.type === "py_end") {
      svg.classList.add("py-frame-end");
      if (block._pyEndParked) svg.classList.add("py-frame-end-parked");
    }
  },

  decorateFrameBlocks(workspace) {
    const start = this.findStart(workspace);
    const end = this.findEnd(workspace);
    if (start) this.decorateBlock(start);
    if (end) this.decorateBlock(end);
  },

  getChainTail(block) {
    let tail = block;
    while (tail.getNextBlock()) {
      tail = tail.getNextBlock();
    }
    return tail;
  },

  collectProgramBlockIds(start) {
    const connected = new Set();
    if (!start) return connected;

    const visit = function (block) {
      if (!block || connected.has(block.id)) return;
      connected.add(block.id);

      const stackNext = block.getNextBlock();
      if (stackNext) visit(stackNext);

      if (!block.inputList) return;
      block.inputList.forEach(function (input) {
        if (!input.connection) return;
        const child = input.connection.targetBlock();
        if (child) visit(child);
      });
    };

    visit(start);
    return connected;
  },

  updateDetachedStyles(workspace) {
    if (!workspace || workspace.isFlyout) return;

    const start = this.findStart(workspace);
    const connected = this.collectProgramBlockIds(start);

    workspace.getAllBlocks(false).forEach(function (block) {
      const svg = typeof block.getSvgRoot === "function" ? block.getSvgRoot() : null;
      if (!svg) return;
      svg.classList.toggle("py-block-detached", !connected.has(block.id));
    });
  },

  bindWorkspaceListener(workspace) {
    if (!workspace || workspace._pyFrameBound) return;
    workspace._pyFrameBound = true;

    let pendingStyles = false;
    const scheduleUpdate = function () {
      if (pendingStyles) return;
      pendingStyles = true;
      requestAnimationFrame(function () {
        pendingStyles = false;
        ProgramFrame.updateDetachedStyles(workspace);
      });
    };

    let pendingConsolidate = false;
    const scheduleConsolidate = function () {
      if (pendingConsolidate) return;
      pendingConsolidate = true;
      requestAnimationFrame(function () {
        pendingConsolidate = false;
        if (typeof workspace.isDragging === "function" && workspace.isDragging()) {
          scheduleConsolidate();
          return;
        }
        ProgramFrame.consolidateEndBlocks(workspace);
      });
    };

    workspace.addChangeListener(function (event) {
      if (!event || event.isUiEvent) return;

      const block = event.blockId ? workspace.getBlockById(event.blockId) : null;
      const start = ProgramFrame.findStart(workspace);

      if (event.type === Blockly.Events.BLOCK_DRAG && block && block.type === "py_end") {
        if (event.isStart) {
          if (block._pyEndParked) {
            ProgramFrame.unparkEnd(block);
          }
        } else if (!ProgramFrame.isEndInChain(block, start)) {
          ProgramFrame.parkEnd(block);
        } else {
          ProgramFrame.unparkEnd(block);
        }
      }

      if (
        event.type === Blockly.Events.BLOCK_MOVE &&
        block &&
        block.type === "py_end"
      ) {
        if (!ProgramFrame.isEndInChain(block, start)) {
          ProgramFrame.parkEnd(block);
        } else {
          ProgramFrame.unparkEnd(block);
        }
        scheduleConsolidate();
      } else if (event.type === Blockly.Events.BLOCK_CREATE && block && block.type === "py_end") {
        scheduleConsolidate();
      }

      scheduleUpdate();
    });
  },

  ensure(workspace) {
    this.consolidateEndBlocks(workspace);

    let start = this.findStart(workspace);
    let end = this.findEnd(workspace);

    if (!start) {
      start = this.createBlock(workspace, "py_start", 48, 48);
    }
    if (!end) {
      end = this.createBlock(workspace, "py_end", 48, 160);
    }

    if (!start.getNextBlock()) {
      if (
        start.nextConnection &&
        end.previousConnection &&
        !end.previousConnection.isConnected() &&
        this.shouldAutoConnectEnd(workspace, end)
      ) {
        start.nextConnection.connect(end.previousConnection);
      }
    }

    return { start: start, end: end };
  },

  integrateOrphans(workspace) {
    const start = this.findStart(workspace);
    const end = this.findEnd(workspace);
    if (!start || !end) return;

    const connectedIds = this.collectProgramBlockIds(start);

    const orphans = workspace
      .getTopBlocks(true)
      .filter(function (block) {
        if (connectedIds.has(block.id)) return false;
        if (block.type === "py_start" || block.type === "py_end") return false;
        if (block.outputConnection) return false;
        if (!block.previousConnection) return false;
        return !block.previousConnection.isConnected();
      })
      .sort(function (a, b) {
        return a.getRelativeToSurfaceXY().y - b.getRelativeToSurfaceXY().y;
      });

    if (!orphans.length) return;

    if (start.getNextBlock() === end) {
      start.nextConnection.disconnect(end);
    }

    let tail = start;
    while (tail.getNextBlock() && tail.getNextBlock().type !== "py_end") {
      tail = tail.getNextBlock();
    }

    if (tail.getNextBlock() === end) {
      tail.nextConnection.disconnect(end);
    }

    orphans.forEach(function (orphan) {
      if (!tail.nextConnection || tail.nextConnection.isConnected()) return;
      if (!orphan.previousConnection || orphan.previousConnection.isConnected()) return;
      tail.nextConnection.connect(orphan.previousConnection);
      tail = ProgramFrame.getChainTail(orphan);
    });

    if (
      this.shouldAutoConnectEnd(workspace, end) &&
      end.previousConnection &&
      !end.previousConnection.isConnected() &&
      tail.nextConnection &&
      !tail.nextConnection.isConnected()
    ) {
      tail.nextConnection.connect(end.previousConnection);
    }
  },

  setup(workspace) {
    if (!workspace) return;
    this.ensure(workspace);
    this.integrateOrphans(workspace);
    const start = this.findStart(workspace);
    const end = this.findEnd(workspace);
    if (end && start && !this.isEndInChain(end, start)) {
      this.parkEnd(end);
    }
    this.updateDetachedStyles(workspace);
    this.bindWorkspaceListener(workspace);
    requestAnimationFrame(function () {
      ProgramFrame.decorateFrameBlocks(workspace);
      ProgramFrame.updateDetachedStyles(workspace);
    });
  },
};
