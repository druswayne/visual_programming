/**
 * Главная логика приложения PyBlocks.
 */

let workspace = null;
let suppressCodePreview = false;

const pyblocksTheme = window.pyblocksTheme;

function refreshWorkspaceLayout() {
  if (typeof TopicsUI !== "undefined" && typeof TopicsUI.updateWorkspaceLayout === "function") {
    TopicsUI.updateWorkspaceLayout();
    return;
  }
  if (!workspace || typeof Blockly === "undefined") return;
  Blockly.svgResize(workspace);
  if (typeof ScratchToolbox !== "undefined") ScratchToolbox.onResize();
}

function scheduleWorkspaceLayoutRefresh() {
  refreshWorkspaceLayout();
  requestAnimationFrame(refreshWorkspaceLayout);
  setTimeout(refreshWorkspaceLayout, 50);
}

function initBlockly() {
  const names =
    Blockly.blockRendering && typeof Blockly.blockRendering.getRendererNames === "function"
      ? Blockly.blockRendering.getRendererNames()
      : [];
  const renderer = names.includes("compact")
    ? "compact"
    : names.includes("thrasos")
      ? "thrasos"
      : "geras";

  workspace = Blockly.inject("blocklyShell", {
    toolbox: PYBLOCKS_TOOLBOX,
    grid: {
      spacing: 16,
      length: 2,
      colour: "#2a2d32",
      snap: true,
    },
    zoom: {
      controls: true,
      wheel: true,
      startScale: 0.79,
      maxScale: 1.6,
      minScale: 0.3,
      pinch: true,
    },
    move: {
      scrollbars: { horizontal: true, vertical: true },
      drag: true,
      wheel: true,
    },
    trashcan: true,
    renderer: renderer,
    theme: pyblocksTheme,
    sounds: false,
  });

  if (typeof BlockCodeSync !== "undefined") {
    BlockCodeSync.init(workspace);
  }

  workspace.addChangeListener(updateCodePreview);

  ScratchToolbox.init(workspace);
  StepDebugger.init(workspace);
  ProgramFrame.setup(workspace);
  initPanelResize();

  requestAnimationFrame(function () {
    Blockly.svgResize(workspace);
    ScratchToolbox.hideNativeToolbox();
    ScratchToolbox.syncFlyoutLayout();
    if (typeof TopicsUI !== "undefined") TopicsUI.updateWorkspaceLayout();
  });

  const shell = document.getElementById("blocklyShell");
  const resizeObserver = new ResizeObserver(function () {
    Blockly.svgResize(workspace);
    ScratchToolbox.onResize();
  });
  if (shell) resizeObserver.observe(shell);

  window.addEventListener("resize", function () {
    Blockly.svgResize(workspace);
    ScratchToolbox.onResize();
  });

  updateCodePreview();
}

function initPanelResize() {
  const handle = document.getElementById("panelResizeHandle");
  const shell = document.getElementById("blocklyShell");
  if (!handle || !shell) return;

  const minPalette = 154;
  const maxPalette = 396;
  let dragging = false;

  handle.addEventListener("mousedown", function (e) {
    dragging = true;
    handle.classList.add("is-active");
    document.body.style.cursor = "col-resize";
    document.body.style.userSelect = "none";
    e.preventDefault();
  });

  document.addEventListener("mousemove", function (e) {
    if (!dragging) return;
    const area = document.getElementById("editorArea");
    const rect = area.getBoundingClientRect();
    const catWidth =
      parseInt(getComputedStyle(shell).getPropertyValue("--cat-width"), 10) || 84;
    const paletteWidth = Math.min(maxPalette, Math.max(minPalette, e.clientX - rect.left - catWidth));
    shell.style.setProperty("--palette-width", paletteWidth + "px");
    Blockly.svgResize(workspace);
    ScratchToolbox.onResize();
    if (typeof TopicsUI !== "undefined") TopicsUI.updateWorkspaceLayout();
  });

  document.addEventListener("mouseup", function () {
    if (!dragging) return;
    dragging = false;
    handle.classList.remove("is-active");
    document.body.style.cursor = "";
    document.body.style.userSelect = "";
  });
}

function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function getCodePreviewNodes() {
  const preview = document.getElementById("codePreview");
  if (!preview) return null;
  let codeEl = preview.querySelector("code");
  if (!codeEl) {
    preview.textContent = "";
    codeEl = document.createElement("code");
    preview.appendChild(codeEl);
  }
  return { preview: preview, codeEl: codeEl };
}

function setCodePreviewPlain(text) {
  const nodes = getCodePreviewNodes();
  if (!nodes) return;
  if (typeof PythonHighlighter !== "undefined") {
    nodes.codeEl.innerHTML = PythonHighlighter.highlight(text);
  } else {
    nodes.codeEl.textContent = text;
  }
}

function setCodePreviewHighlight(lines, activeLineNo) {
  const nodes = getCodePreviewNodes();
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

  nodes.codeEl.innerHTML = html || "# Соберите программу из блоков";

  const active = nodes.codeEl.querySelector(".code-line--active");
  if (active) active.scrollIntoView({ block: "nearest" });
}

function setCodePreviewSuppressed(value) {
  suppressCodePreview = !!value;
}

function updateCodePreview() {
  if (!workspace) return;
  if (suppressCodePreview) return;
  if (typeof CodeEditor !== "undefined" && CodeEditor.isEditMode()) return;
  if (StepDebugger.sessionActive || StepDebugger.loading) return;

  if (typeof BlockCodeSync !== "undefined" && BlockCodeSync.enabled) {
    if (BlockCodeSync.isDragging) {
      BlockCodeSync.render();
      return;
    }
    BlockCodeSync.rebuild();
    BlockCodeSync.render();
    return;
  }

  const code = generatePythonCode(workspace);
  setCodePreviewPlain(code.trim() || "# Соберите программу из блоков");
}

function setStatus(state, text) {
  const badge = document.getElementById("statusBadge");
  badge.className = "badge badge--" + state;
  badge.textContent = text;
}

function setOutput(text, isError) {
  const inDebug =
    typeof StepDebugger !== "undefined" && StepDebugger.isPanelVisible();
  const output = document.getElementById(
    inDebug ? "debugOutputConsole" : "outputConsole"
  );
  if (!output) return;
  output.textContent = text;
  output.className =
    "output-console" +
    (inDebug ? " debug-output-console" : "") +
    (isError ? " output-console--error" : " output-console--success");
}

async function runCode() {
  StepDebugger.stop();
  const code = getActivePythonCode();
  if (!code.trim()) {
    setStatus("error", "Ошибка");
    setOutput("Добавьте хотя бы один блок в рабочую область.", true);
    return;
  }

  const stdinText = await InputHelper.collectStdin(code);
  if (stdinText === null) {
    setStatus("idle", "Готов");
    setOutput("Ввод отменён.", false);
    return;
  }

  setStatus("running", "Выполняется…");
  setOutput("Выполнение программы…", false);

  try {
    const response = await fetch("/api/run", {
      method: "POST",
      headers: getJsonHeaders(),
      body: JSON.stringify({ code: code, stdin: stdinText }),
    });
    const data = await response.json();
    const limitMsg = getApiErrorMessage(data, response);
    if (limitMsg) {
      setStatus("error", "Подождите");
      setOutput(limitMsg, true);
      return;
    }

    if (data.success) {
      setStatus("success", "Готово");
      setOutput(data.output || "(программа выполнена без вывода)", false);
    } else {
      setStatus("error", "Ошибка");
      setOutput([data.error, data.output].filter(Boolean).join("\n\n"), true);
    }
  } catch (err) {
    setStatus("error", "Ошибка");
    setOutput("Не удалось связаться с сервером: " + err.message, true);
  }
}

function clearWorkspace() {
  StepDebugger.stop();
  if (typeof CodeEditor !== "undefined") CodeEditor.leaveEditMode();
  workspace.clear();
  ProgramFrame.setup(workspace);
  updateCodePreview();
  setStatus("idle", "Готов");
  setOutput("Рабочая область очищена.", false);
}

function copyCode() {
  const code = getActivePythonCode();
  const btn = document.getElementById("btnCopy");
  const label = btn ? btn.querySelector(".btn-label") : null;
  const original = label ? label.textContent : btn ? btn.textContent : "Копировать";
  navigator.clipboard.writeText(code).then(function () {
    if (label) label.textContent = "Скопировано!";
    else if (btn) btn.textContent = "Скопировано!";
    setTimeout(function () {
      if (label) label.textContent = original;
      else if (btn) btn.textContent = original;
    }, 1500);
  });
}

function getEditorViewportWidth() {
  if (window.visualViewport && window.visualViewport.width > 0) {
    return window.visualViewport.width;
  }
  return document.documentElement.clientWidth;
}

function initEditorResponsive() {
  const toggle = document.getElementById("btnBlocksToggle");
  const backdrop = document.getElementById("blocksPanelBackdrop");
  const layout = document.querySelector(".layout");
  const shell = document.getElementById("blocklyShell");
  if (!layout) return;

  let raf = 0;

  function refreshWorkspace() {
    refreshWorkspaceLayout();
  }

  function setBlocksOpen(open) {
    document.body.classList.toggle("blocks-panel-open", open);
    if (toggle) {
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    }
    if (backdrop) {
      backdrop.hidden = !open;
      backdrop.setAttribute("aria-hidden", open ? "false" : "true");
    }
    refreshWorkspace();
  }

  function updateLayoutMode() {
    const viewportWidth = getEditorViewportWidth();
    const shellWidth = shell ? shell.clientWidth : viewportWidth;
    const narrow = viewportWidth < 1100;
    const compact = viewportWidth < 880;
    const tiny = shellWidth < 620 || viewportWidth < 640;

    document.body.classList.toggle("editor-narrow", narrow);
    document.body.classList.toggle("editor-compact", compact);
    document.body.classList.toggle("editor-tiny", tiny);

    if (toggle) {
      toggle.hidden = !tiny;
    }
    if (!tiny && document.body.classList.contains("blocks-panel-open")) {
      setBlocksOpen(false);
    } else {
      refreshWorkspace();
    }
  }

  function scheduleUpdate() {
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(updateLayoutMode);
  }

  if (toggle) {
    toggle.addEventListener("click", function () {
      setBlocksOpen(!document.body.classList.contains("blocks-panel-open"));
    });
  }

  if (backdrop) {
    backdrop.addEventListener("click", function () {
      setBlocksOpen(false);
    });
  }

  if (window.visualViewport) {
    window.visualViewport.addEventListener("resize", scheduleUpdate);
  }
  window.addEventListener("resize", scheduleUpdate);

  if (typeof ResizeObserver !== "undefined") {
    const observer = new ResizeObserver(scheduleUpdate);
    observer.observe(layout);
    if (shell) observer.observe(shell);
  }

  scheduleUpdate();
}

function centerWorkspaceOnBlocks() {
  const topBlocks = workspace.getTopBlocks(true);
  if (!topBlocks.length) return;
  if (typeof workspace.centerOnBlock === "function") {
    workspace.centerOnBlock(topBlocks[0].id);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  initBlockly();
  initEditorResponsive();
  TopicsUI.init();
  CodeEditor.init();
  document.getElementById("btnRun").addEventListener("click", runCode);
  document.getElementById("btnClear").addEventListener("click", clearWorkspace);
  document.getElementById("btnCopy").addEventListener("click", copyCode);
});
