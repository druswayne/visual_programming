/**
 * Мини-песочница Blockly на главной странице.
 */
(function () {
  if (typeof Blockly === "undefined") return;

  const container = document.getElementById("landingSandboxWorkspace");
  const codeEl = document.getElementById("landingSandboxCode");
  const outputEl = document.getElementById("landingSandboxOutput");
  const runBtn = document.getElementById("landingSandboxRun");
  if (!container || !codeEl) return;

  const miniToolbox = {
    kind: "flyoutToolbox",
    contents: [
      { kind: "block", type: "text_print" },
      { kind: "block", type: "text" },
    ],
  };

  const theme =
    window.pyblocksTheme ||
    Blockly.Theme.defineTheme("pyblocks", {
      base: Blockly.Themes.Classic,
      componentStyles: { workspaceBackgroundColour: "#111827" },
    });

  const names =
    Blockly.blockRendering && typeof Blockly.blockRendering.getRendererNames === "function"
      ? Blockly.blockRendering.getRendererNames()
      : [];
  const renderer = names.includes("compact") ? "compact" : "geras";

  let workspace = null;

  const EXPECTED_TEXT = "Hello, world!";

  function getJsonHeaders() {
    const headers = { "Content-Type": "application/json" };
    const meta = document.querySelector('meta[name="csrf-token"]');
    if (meta && meta.content) headers["X-CSRFToken"] = meta.content;
    return headers;
  }

  function setOutput(text, mode) {
    if (!outputEl) return;
    outputEl.textContent = text;
    const suffix = mode ? " landing-sandbox__output--" + mode : "";
    outputEl.className = "landing-sandbox__output" + suffix;
  }

  function getProgramChainBlocks() {
    if (typeof ProgramFrame === "undefined") return [];
    const start = ProgramFrame.findStart(workspace);
    if (!start) return [];

    const blocks = [];
    let cur = start.getNextBlock();
    while (cur && cur.type !== "py_end") {
      blocks.push(cur);
      cur = cur.getNextBlock();
    }
    return blocks;
  }

  function getPrintBlockText(printBlock) {
    const textBlock = printBlock.getInputTargetBlock("TEXT");
    if (!textBlock || textBlock.type !== "text") return null;
    return textBlock.getFieldValue("TEXT");
  }

  function analyzeBlocks() {
    const allPrints = workspace
      .getAllBlocks(false)
      .filter(function (b) {
        return b.type === "text_print";
      });
    const chainPrints = getProgramChainBlocks().filter(function (b) {
      return b.type === "text_print";
    });

    if (!allPrints.length) {
      return {
        ok: false,
        hint:
          "Перетащите блок «вывести» из панели слева между «Начало программы» и «Конец программы».",
      };
    }

    if (!chainPrints.length) {
      return {
        ok: false,
        hint:
          "Блок «вывести» есть, но не подключён к программе. Вставьте его между «Начало» и «Конец программы».",
      };
    }

    if (chainPrints.length > 1) {
      return {
        ok: false,
        hint: "Достаточно одного блока «вывести». Оставьте только один в цепочке.",
      };
    }

    if (allPrints.length > chainPrints.length) {
      return {
        ok: false,
        hint:
          "Есть лишний блок «вывести» вне программы. Удалите его или подключите только один к цепочке.",
      };
    }

    const printBlock = chainPrints[0];
    const text = getPrintBlockText(printBlock);

    if (text === null) {
      return {
        ok: false,
        hint:
          "В блок «вывести» нужно вставить текст. Перетащите блок «» внутрь «вывести» и напишите Hello, world!",
      };
    }

    if (!text.trim()) {
      return {
        ok: false,
        hint: "Текст пустой. В блоке с кавычками напишите: Hello, world!",
      };
    }

    if (text.trim() !== EXPECTED_TEXT) {
      return {
        ok: false,
        hint:
          "Сейчас выводится «" +
          text.trim() +
          "». Нужно вывести именно: Hello, world!",
      };
    }

    return { ok: true };
  }

  function updateCode() {
    if (!workspace) return;
    try {
      const code =
        typeof generatePythonCode === "function"
          ? generatePythonCode(workspace)
          : Blockly.Python.workspaceToCode(workspace);
      codeEl.textContent = code.trim() || "# соберите программу из блоков";
    } catch (err) {
      console.error("landing-sandbox updateCode:", err);
      codeEl.textContent = "# ошибка генерации кода";
    }
  }

  async function runCode() {
    if (!workspace) return;

    const check = analyzeBlocks();
    if (!check.ok) {
      setOutput(check.hint, "hint");
      return;
    }

    const code =
      typeof generatePythonCode === "function"
        ? generatePythonCode(workspace)
        : Blockly.Python.workspaceToCode(workspace);

    if (runBtn) {
      runBtn.disabled = true;
      runBtn.textContent = "Выполняется…";
    }
    setOutput("Выполнение программы…", "running");

    try {
      const response = await fetch("/api/run", {
        method: "POST",
        headers: getJsonHeaders(),
        body: JSON.stringify({ code: code, stdin: "" }),
      });
      const data = await response.json();

      if (data.success) {
        const out = (data.output || "").trim();
        if (out === EXPECTED_TEXT) {
          setOutput(out + "\n\n✓ Отлично! Задача решена.", "success");
        } else if (!out) {
          setOutput(
            "Программа выполнилась, но ничего не вывела. Проверьте, что в блок «вывести» вставлен текст Hello, world!",
            "hint"
          );
        } else {
          setOutput(
            "Программа вывела: " + out + "\n\nНужно вывести: Hello, world!",
            "hint"
          );
        }
      } else {
        setOutput([data.error, data.output].filter(Boolean).join("\n\n"), "error");
      }
    } catch (err) {
      setOutput("Не удалось связаться с сервером: " + err.message, "error");
    } finally {
      if (runBtn) {
        runBtn.disabled = false;
        runBtn.textContent = "▶ Запустить";
      }
    }
  }

  function init() {
    workspace = Blockly.inject(container, {
      toolbox: miniToolbox,
      readOnly: false,
      scrollbars: true,
      zoom: { controls: false, wheel: true, startScale: 0.85, maxScale: 1.2, minScale: 0.5 },
      move: { scrollbars: true, drag: true, wheel: true },
      trashcan: true,
      renderer: renderer,
      theme: theme,
      sounds: false,
      grid: { spacing: 16, length: 2, colour: "#2a2d32", snap: true },
    });

    if (typeof ProgramFrame !== "undefined") {
      ProgramFrame.setup(workspace);
    }

    workspace.addChangeListener(function (event) {
      if (
        event.type === Blockly.Events.UI ||
        (event.type === Blockly.Events.BLOCK_MOVE && event.isUiEvent)
      ) {
        return;
      }
      updateCode();
    });

    if (runBtn) {
      runBtn.addEventListener("click", runCode);
    }

    updateCode();

    window.addEventListener("resize", function () {
      if (workspace) Blockly.svgResize(workspace);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
