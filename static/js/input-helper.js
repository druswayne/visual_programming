/**
 * Сбор ввода для input() — как в Python, каждое значение это str.
 * Учитывает циклы for ... in range(N) с известным числом повторений.
 */
const InputHelper = {
  /** Имена переменных Python, в т.ч. кириллица (элемент, числа, …). */
  _IDENT: "[\\p{L}_][\\p{L}\\p{N}_]*",
  _IDENT_RE: null,
  _FOR_RANGE_RE: null,
  _FOR_LIST_RE: null,
  _FOR_EACH_RE: null,
  _ASSIGN_NUMBER_RE: null,
  _ASSIGN_INPUT_RE: null,

  _initRegexes() {
    if (this._FOR_RANGE_RE) return;
    const id = this._IDENT;
    const u = "u";
    this._IDENT_RE = new RegExp("^" + id + "$", u);
    this._FOR_RANGE_RE = new RegExp(
      "^for\\s+" + id + "\\s+in\\s+range\\s*\\(\\s*([^)]+)\\s*\\)\\s*:",
      u
    );
    this._FOR_LIST_RE = new RegExp(
      "^for\\s+" + id + "\\s+in\\s+(\\[[^\\]]*\\])\\s*:",
      u
    );
    this._FOR_EACH_RE = new RegExp("^for\\s+" + id + "\\s+in\\s+(" + id + ")\\s*:", u);
    this._ASSIGN_NUMBER_RE = new RegExp("^(" + id + ")\\s*=\\s*(-?\\d+)\\s*$", u);
    this._ASSIGN_INPUT_RE = new RegExp(
      "^(" + id + ")\\s*=\\s*(?:(?:int|float)\\s*\\(\\s*)?input\\s*\\(",
      u
    );
  },

  parseInputCalls(code, knownVars) {
    return this.analyzeInputs(code, knownVars || {});
  },

  analyzeInputs(code, knownVars) {
    this._initRegexes();
    const lines = this.normalizeLines(code);
    let prompts = this.processBlock(lines, 0, 0, knownVars);
    if (!prompts.length && /input\s*\(/.test(code)) {
      prompts = this.fallbackInputPrompts(code, knownVars);
    }
    return prompts;
  },

  fallbackInputPrompts(code, knownVars) {
    const flat = code.replace(/\s+/g, " ");
    let prompts = this.extractInputsFromLine(flat);
    const rangeMatch = code.match(/range\s*\(\s*([^)]+)\s*\)/);
    if (rangeMatch) {
      const iterations = this.resolveRangeIterations(rangeMatch[1], knownVars);
      if (iterations > 1 && prompts.length) {
        const base = prompts.slice();
        prompts = [];
        for (let n = 0; n < iterations; n++) {
          prompts.push.apply(prompts, base);
        }
      }
    }
    return prompts;
  },

  normalizeLines(code) {
    return code.replace(/\r\n/g, "\n").split("\n");
  },

  getIndent(line) {
    const match = line.match(/^(\s*)/);
    return match ? match[1].length : 0;
  },

  detectIndentStep(lines, lineIndex) {
    const base = this.getIndent(lines[lineIndex]);
    for (let i = lineIndex + 1; i < lines.length; i++) {
      const trimmed = lines[i].trim();
      if (!trimmed || trimmed.startsWith("#")) continue;
      const indent = this.getIndent(lines[i]);
      if (indent > base) return indent - base;
      break;
    }
    return 4;
  },

  findBlockEnd(lines, startIdx, parentIndent) {
    let i = startIdx;
    while (i < lines.length) {
      const trimmed = lines[i].trim();
      if (!trimmed || trimmed.startsWith("#")) {
        i++;
        continue;
      }
      if (this.getIndent(lines[i]) <= parentIndent) break;
      i++;
    }
    return i;
  },

  resolveRangeIterations(expr, knownVars) {
    const text = expr.trim();

    let match = text.match(/^(-?\d+)$/);
    if (match) {
      return Math.max(0, parseInt(match[1], 10));
    }

    if (knownVars[text] !== undefined && typeof knownVars[text] === "number") {
      return Math.max(0, knownVars[text]);
    }

    match = text.match(/^(-?\d+)\s*,\s*(-?\d+)(?:\s*,\s*(-?\d+))?$/);
    if (match) {
      const start = parseInt(match[1], 10);
      const end = parseInt(match[2], 10);
      const step = match[3] ? parseInt(match[3], 10) : 1;
      if (!step) return 0;
      if (step > 0) {
        return start < end ? Math.ceil((end - start) / step) : 0;
      }
      return start > end ? Math.ceil((start - end) / -step) : 0;
    }

    return null;
  },

  isDeferredRangeExpr(expr, knownVars) {
    this._initRegexes();
    const text = expr.trim();
    if (/^-?\d+(?:\s*,\s*-?\d+){1,2}$/.test(text)) return false;
    if (this._IDENT_RE.test(text) && knownVars[text] === undefined) return true;
    return false;
  },

  countListLiteralItems(listLiteral) {
    const inner = listLiteral.slice(1, -1).trim();
    if (!inner) return 0;
    return inner.split(",").filter(function (part) {
      return part.trim().length > 0;
    }).length;
  },

  processBlock(lines, startIdx, blockIndent, knownVars) {
    this._initRegexes();
    const prompts = [];
    let i = startIdx;

    while (i < lines.length) {
      const line = lines[i];
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith("#")) {
        i++;
        continue;
      }

      const indent = this.getIndent(line);
      if (indent < blockIndent) break;
      if (indent > blockIndent) {
        i++;
        continue;
      }

      const forRange = trimmed.match(this._FOR_RANGE_RE);
      if (forRange) {
        const rangeExpr = forRange[1];
        const iterations = this.resolveRangeIterations(rangeExpr, knownVars);
        const bodyIndent = blockIndent + this.detectIndentStep(lines, i);
        const bodyEnd = this.findBlockEnd(lines, i + 1, blockIndent);
        const bodyPrompts = this.processBlock(lines, i + 1, bodyIndent, knownVars);

        if (iterations !== null) {
          for (let n = 0; n < iterations; n++) {
            prompts.push.apply(prompts, bodyPrompts);
          }
        } else if (!this.isDeferredRangeExpr(rangeExpr, knownVars)) {
          prompts.push.apply(prompts, bodyPrompts);
        }

        i = bodyEnd;
        continue;
      }

      const forList = trimmed.match(this._FOR_LIST_RE);
      if (forList) {
        const iterations = this.countListLiteralItems(forList[1]);
        const bodyIndent = blockIndent + this.detectIndentStep(lines, i);
        const bodyEnd = this.findBlockEnd(lines, i + 1, blockIndent);
        const bodyPrompts = this.processBlock(lines, i + 1, bodyIndent, knownVars);

        for (let n = 0; n < iterations; n++) {
          prompts.push.apply(prompts, bodyPrompts);
        }

        i = bodyEnd;
        continue;
      }

      const forEach = trimmed.match(this._FOR_EACH_RE);
      if (forEach && !forRange && !forList) {
        const bodyIndent = blockIndent + this.detectIndentStep(lines, i);
        const bodyEnd = this.findBlockEnd(lines, i + 1, blockIndent);
        const bodyPrompts = this.processBlock(lines, i + 1, bodyIndent, knownVars);
        prompts.push.apply(prompts, bodyPrompts);
        i = bodyEnd;
        continue;
      }

      const whileLoop = trimmed.match(/^while\s+/);
      if (whileLoop) {
        const bodyIndent = blockIndent + this.detectIndentStep(lines, i);
        const bodyEnd = this.findBlockEnd(lines, i + 1, blockIndent);
        const bodyPrompts = this.processBlock(lines, i + 1, bodyIndent, knownVars);
        prompts.push.apply(prompts, bodyPrompts);
        i = bodyEnd;
        continue;
      }

      const assignNumber = trimmed.match(this._ASSIGN_NUMBER_RE);
      if (assignNumber) {
        knownVars[assignNumber[1]] = parseInt(assignNumber[2], 10);
        i++;
        continue;
      }

      prompts.push.apply(prompts, this.extractInputsFromLine(trimmed));
      i++;
    }

    return prompts;
  },

  deriveKnownVars(code, values) {
    this._initRegexes();
    const knownVars = {};
    const lines = this.normalizeLines(code);
    let valueIndex = 0;

    const consumeInputs = function (line) {
      const count = InputHelper.countInputsInLine(line);
      const consumed = values.slice(valueIndex, valueIndex + count);
      valueIndex += count;
      return consumed;
    };

    const walk = function (startIdx, blockIndent) {
      let i = startIdx;
      while (i < lines.length) {
        const line = lines[i];
        const trimmed = line.trim();
        if (!trimmed || trimmed.startsWith("#")) {
          i++;
          continue;
        }

        const indent = InputHelper.getIndent(line);
        if (indent < blockIndent) break;
        if (indent > blockIndent) {
          i++;
          continue;
        }

        const forRange = trimmed.match(InputHelper._FOR_RANGE_RE);
        if (forRange) {
          const rangeExpr = forRange[1];
          const iterations = InputHelper.resolveRangeIterations(rangeExpr, knownVars);
          const bodyIndent = blockIndent + InputHelper.detectIndentStep(lines, i);
          const bodyEnd = InputHelper.findBlockEnd(lines, i + 1, blockIndent);
          const count =
            iterations !== null
              ? iterations
              : InputHelper.isDeferredRangeExpr(rangeExpr, knownVars)
                ? 0
                : 1;
          for (let n = 0; n < count; n++) {
            walk(i + 1, bodyIndent);
          }
          i = bodyEnd;
          continue;
        }

        const forList = trimmed.match(InputHelper._FOR_LIST_RE);
        if (forList) {
          const iterations = InputHelper.countListLiteralItems(forList[1]);
          const bodyIndent = blockIndent + InputHelper.detectIndentStep(lines, i);
          const bodyEnd = InputHelper.findBlockEnd(lines, i + 1, blockIndent);
          for (let n = 0; n < iterations; n++) {
            walk(i + 1, bodyIndent);
          }
          i = bodyEnd;
          continue;
        }

        const forEach = trimmed.match(InputHelper._FOR_EACH_RE);
        if (forEach && !forRange && !forList) {
          const bodyIndent = blockIndent + InputHelper.detectIndentStep(lines, i);
          const bodyEnd = InputHelper.findBlockEnd(lines, i + 1, blockIndent);
          walk(i + 1, bodyIndent);
          i = bodyEnd;
          continue;
        }

        const whileLoop = trimmed.match(/^while\s+/);
        if (whileLoop) {
          const bodyIndent = blockIndent + InputHelper.detectIndentStep(lines, i);
          const bodyEnd = InputHelper.findBlockEnd(lines, i + 1, blockIndent);
          walk(i + 1, bodyIndent);
          i = bodyEnd;
          continue;
        }

        const assignNumber = trimmed.match(InputHelper._ASSIGN_NUMBER_RE);
        if (assignNumber) {
          knownVars[assignNumber[1]] = parseInt(assignNumber[2], 10);
          i++;
          continue;
        }

        const assignFromInput = trimmed.match(InputHelper._ASSIGN_INPUT_RE);
        if (assignFromInput) {
          const consumed = consumeInputs(trimmed);
          if (consumed.length) {
            const parsed = parseInt(consumed[0], 10);
            if (!isNaN(parsed)) knownVars[assignFromInput[1]] = parsed;
          }
          i++;
          continue;
        }

        consumeInputs(trimmed);
        i++;
      }
    };

    walk(0, 0);
    return knownVars;
  },

  extractInputsFromLine(line) {
    const prompts = [];
    const quotedRe = /input\s*\(\s*(['"])((?:\\.|(?!\1)[^\\])*?)\1\s*\)/g;
    let quotedIndex = 0;
    const masked = line.replace(quotedRe, function (_match, _quote, text) {
      prompts.push(InputHelper.unescapePythonString(text));
      quotedIndex++;
      return "__PY_INPUT_QUOTED_" + quotedIndex + "__";
    });

    const bareMatches = masked.match(/input\s*\(\s*\)/g);
    if (bareMatches) {
      for (let i = 0; i < bareMatches.length; i++) {
        prompts.push(t("input.default_prompt", "Введите значение:"));
      }
    }

    return prompts;
  },

  countInputsInLine(line) {
    return this.extractInputsFromLine(line).length;
  },

  unescapePythonString(text) {
    return text
      .replace(/\\n/g, "\n")
      .replace(/\\t/g, "\t")
      .replace(/\\'/g, "'")
      .replace(/\\"/g, '"')
      .replace(/\\\\/g, "\\");
  },

  buildStdin(values) {
    if (!values.length) return "";
    return values.join("\n") + "\n";
  },

  async collectStdin(code) {
    const collected = [];

    for (let pass = 0; pass < 6; pass++) {
      const knownVars = this.deriveKnownVars(code, collected);
      const prompts = this.parseInputCalls(code, knownVars);
      if (!prompts.length) {
        return this.buildStdin(collected);
      }
      if (prompts.length <= collected.length) {
        return this.buildStdin(collected);
      }

      const batch = prompts.slice(collected.length);
      const values = await this.promptValues(batch);
      if (values === null) return null;
      collected.push.apply(collected, values);
    }

    return this.buildStdin(collected);
  },

  promptValues(prompts) {
    if (!prompts.length) {
      return Promise.resolve([]);
    }
    if (prompts.length === 1) {
      return this.showModal(prompts);
    }
    return this.promptSequential(prompts);
  },

  async promptSequential(prompts) {
    const values = [];
    for (let i = 0; i < prompts.length; i++) {
      const batch = await this.showModal([prompts[i]], {
        index: i + 1,
        total: prompts.length,
      });
      if (batch === null) return null;
      values.push(batch[0]);
    }
    return values;
  },

  showModal(prompts, options) {
    const opts = options || {};
    const modal = document.getElementById("inputModal");
    const form = document.getElementById("inputModalForm");
    const btnCancel = document.getElementById("inputModalCancel");
    const btnOk = document.getElementById("inputModalOk");
    const hint = document.getElementById("inputModalHint");
    if (!modal || !form) {
      return Promise.resolve(
        prompts.map(function () {
          return window.prompt(t("input.prompt_fallback", "Ввод:"), "") || "";
        })
      );
    }

    if (hint) {
      if (opts.total > 1 && opts.index) {
        hint.textContent = t("input.step_of", "Шаг {index} из {total}", {
          index: opts.index,
          total: opts.total,
        });
        hint.hidden = false;
      } else {
        hint.hidden = true;
        hint.textContent = "";
      }
    }

    if (btnOk) {
      btnOk.textContent =
        opts.total > 1 && opts.index < opts.total ? t("input.next") : t("input.submit");
    }

    form.innerHTML = "";
    prompts.forEach(function (prompt, index) {
      const label = document.createElement("label");
      label.className = "input-modal__field";
      label.textContent = prompt;

      const input = document.createElement("input");
      input.type = "text";
      input.className = "input-modal__input";
      input.name = "input_" + index;
      input.autocomplete = "off";
      if (index === 0) input.autofocus = true;

      label.appendChild(input);
      form.appendChild(label);
    });

    modal.hidden = false;

    return new Promise(function (resolve) {
      function cleanup() {
        modal.hidden = true;
        form.removeEventListener("submit", onSubmit);
        if (btnCancel) btnCancel.removeEventListener("click", onCancel);
        if (btnOk) btnOk.textContent = t("input.submit");
        if (hint) hint.hidden = true;
      }

      function onCancel() {
        cleanup();
        resolve(null);
      }

      function onSubmit(event) {
        event.preventDefault();
        const inputs = form.querySelectorAll(".input-modal__input");
        const values = Array.from(inputs).map(function (el) {
          return el.value;
        });
        cleanup();
        resolve(values);
      }

      form.addEventListener("submit", onSubmit);
      if (btnCancel) btnCancel.addEventListener("click", onCancel);

      const first = form.querySelector(".input-modal__input");
      if (first) first.focus();
    });
  },
};
