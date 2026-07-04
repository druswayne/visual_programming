/**
 * «Машина времени» — визуализация переменных.
 */
const MemoryViz = {
  varsEl: null,
  outputWrap: null,

  init() {
    this.varsEl = document.getElementById("debugMemoryVars");
    this.outputWrap = document.getElementById("debugOutputWrap");
  },

  clear() {
    if (this.varsEl) {
      this.varsEl.innerHTML = '<p class="memory-viz__empty">Коробочки переменных появятся на каждом шаге</p>';
    }
    if (this.outputWrap) {
      this.outputWrap.classList.remove("debug-output--active");
    }
  },

  render(step, prevStep) {
    if (!step) return;

    const stack = step.stack || this._stackFromLegacy(step);
    const heap = step.heap || {};
    const changed = new Set(step.changed || []);
    const prevStack = prevStep ? prevStep.stack || this._stackFromLegacy(prevStep) : [];

    this._highlightOutput(step, prevStep);
    this.renderVariableBoxes(stack, heap, changed, prevStack);
  },

  _highlightOutput(step, prevStep) {
    if (!this.outputWrap) return;
    const out = step.output || "";
    const prevOut = prevStep ? prevStep.output || "" : "";
    if (out !== prevOut && out.length > prevOut.length) {
      this.outputWrap.classList.add("debug-output--active");
    } else {
      this.outputWrap.classList.remove("debug-output--active");
    }
  },

  _stackFromLegacy(step) {
    const vars = step.vars || {};
    const cells = {};
    Object.keys(vars).forEach(function (name) {
      cells[name] = MemoryViz._legacyToCell(vars[name]);
    });
    return [{ name: "программа", line: step.line || 1, vars: cells }];
  },

  _legacyToCell(value) {
    if (value === null) return { kind: "value", type: "NoneType", value: null };
    if (typeof value === "boolean") return { kind: "value", type: "bool", value: value };
    if (typeof value === "number") {
      return { kind: "value", type: Number.isInteger(value) ? "int" : "float", value: value };
    }
    if (typeof value === "string") return { kind: "value", type: "str", value: value };
    if (Array.isArray(value)) {
      return {
        kind: "list",
        length: value.length,
        items: value.map(MemoryViz._legacyToCell),
        truncated: false,
      };
    }
    if (typeof value === "object") {
      return {
        kind: "dict",
        length: Object.keys(value).length,
        entries: Object.keys(value).map(function (key) {
          return { key: MemoryViz._legacyToCell(key), value: MemoryViz._legacyToCell(value[key]) };
        }),
        truncated: false,
      };
    }
    return { kind: "value", type: "object", value: String(value) };
  },

  _topFrame(stack) {
    return stack.length ? stack[stack.length - 1] : null;
  },

  _prevVarCell(prevStack, name) {
    const frame = this._topFrame(prevStack);
    return frame && frame.vars ? frame.vars[name] : null;
  },

  _sharedRefs(vars) {
    const byId = {};
    Object.keys(vars || {}).forEach(function (name) {
      const cell = vars[name];
      if (cell && cell.kind === "ref") {
        if (!byId[cell.id]) byId[cell.id] = [];
        byId[cell.id].push(name);
      }
    });
    return byId;
  },

  _typeLabel(cell) {
    if (!cell) return "?";
    if (cell.kind === "ref") return cell.type || "объект";
    if (cell.kind === "list") return "list";
    if (cell.kind === "dict") return "dict";
    if (cell.kind === "tuple") return "tuple";
    if (cell.kind === "set") return "set";
    return cell.type || "значение";
  },

  renderVariableBoxes(stack, heap, changed, prevStack) {
    if (!this.varsEl) return;

    const top = this._topFrame(stack);
    if (!top || !Object.keys(top.vars || {}).length) {
      this.varsEl.innerHTML = '<p class="memory-viz__empty">Нет переменных</p>';
      return;
    }

    const shared = this._sharedRefs(top.vars);
    const names = Object.keys(top.vars).sort();

    this.varsEl.innerHTML = names
      .map(function (name) {
        const cell = top.vars[name];
        const isChanged = changed.has(name);
        const isNew = !MemoryViz._prevVarCell(prevStack, name);
        const prevCell = MemoryViz._prevVarCell(prevStack, name);
        const type = MemoryViz._typeLabel(cell);
        const display = MemoryViz.formatCell(cell, heap);
        const prevText = prevCell && isChanged ? MemoryViz.formatPlain(prevCell, heap) : "";

        let classes = "memory-var";
        if (cell.kind === "ref") classes += " memory-var--ref";
        if (isChanged) classes += " memory-var--changed";
        if (isNew) classes += " memory-var--new";

        let sharedHint = "";
        if (cell.kind === "ref" && shared[cell.id] && shared[cell.id].length > 1) {
          sharedHint =
            '<span class="memory-var__shared" title="Общая ссылка">⇄ ' +
            MemoryViz.escape(shared[cell.id].join(", ")) +
            "</span>";
        }

        return (
          '<div class="' +
          classes +
          '" data-var="' +
          MemoryViz.escape(name) +
          '">' +
          '<div class="memory-var__head">' +
          '<span class="memory-var__name">' +
          MemoryViz.escape(name) +
          "</span>" +
          '<span class="memory-var__type">' +
          MemoryViz.escape(type) +
          "</span>" +
          "</div>" +
          '<div class="memory-var__value">' +
          display +
          "</div>" +
          (prevText && isChanged
            ? '<span class="memory-var__delta">было ' +
              MemoryViz.escape(prevText) +
              " → стало " +
              MemoryViz.escape(MemoryViz.formatPlain(cell, heap)) +
              "</span>"
            : "") +
          sharedHint +
          (isChanged ? '<span class="memory-var__badge">изменено</span>' : "") +
          (isNew ? '<span class="memory-var__badge memory-var__badge--new">новая</span>' : "") +
          "</div>"
        );
      })
      .join("");
  },

  _resolveCell(cell, heap) {
    if (cell && cell.kind === "ref" && heap[cell.id]) {
      return heap[cell.id];
    }
    return cell;
  },

  formatPlain(cell, heap) {
    const resolved = MemoryViz._resolveCell(cell, heap);
    if (!resolved) return "?";
    if (resolved.kind === "list" || resolved.kind === "dict" || resolved.kind === "tuple") {
      return MemoryViz.collectionPreview(resolved);
    }
    return MemoryViz.primitiveText(resolved);
  },

  formatCell(cell, heap) {
    if (!cell) return '<span class="memory-cell">?</span>';

    const resolved = MemoryViz._resolveCell(cell, heap);
    if (
      resolved &&
      (resolved.kind === "list" ||
        resolved.kind === "tuple" ||
        resolved.kind === "dict" ||
        resolved.kind === "set")
    ) {
      return MemoryViz.renderCollection(resolved, heap);
    }

    return (
      '<span class="memory-cell memory-cell--primitive">' +
      MemoryViz.escape(MemoryViz.primitiveText(resolved || cell)) +
      "</span>"
    );
  },

  renderCollection(entry, heap) {
    if (!entry) return "";

    if (entry.kind === "list" || entry.kind === "tuple" || entry.kind === "set") {
      const items = entry.items || [];
      if (!items.length) {
        return '<span class="memory-cell memory-cell--inline">[]</span>';
      }
      return (
        '<ul class="memory-coll__list">' +
        items
          .map(function (item, index) {
            return (
              '<li class="memory-coll__item">' +
              '<span class="memory-coll__index">[' +
              index +
              "]</span>" +
              '<span class="memory-coll__arrow" aria-hidden="true">→</span>' +
              MemoryViz.formatCell(item, heap) +
              "</li>"
            );
          })
          .join("") +
        (entry.truncated ? '<li class="memory-coll__item memory-coll__item--more">…</li>' : "") +
        "</ul>"
      );
    }

    if (entry.kind === "dict") {
      const entries = entry.entries || [];
      if (!entries.length) {
        return '<span class="memory-cell memory-cell--inline">{}</span>';
      }
      return (
        '<ul class="memory-coll__dict">' +
        entries
          .map(function (pair) {
            return (
              '<li class="memory-coll__dict-row">' +
              '<span class="memory-coll__key">' +
              MemoryViz.formatCell(pair.key, heap) +
              "</span>" +
              '<span class="memory-coll__arrow" aria-hidden="true">→</span>' +
              '<span class="memory-coll__val">' +
              MemoryViz.formatCell(pair.value, heap) +
              "</span>" +
              "</li>"
            );
          })
          .join("") +
        (entry.truncated ? '<li class="memory-coll__dict-row memory-coll__item--more">…</li>' : "") +
        "</ul>"
      );
    }

    return (
      '<span class="memory-cell memory-cell--primitive">' +
      MemoryViz.escape(MemoryViz.primitiveText(entry)) +
      "</span>"
    );
  },

  collectionPreview(entry) {
    if (!entry) return "?";
    if (entry.kind === "list" || entry.kind === "tuple" || entry.kind === "set") {
      const items = (entry.items || [])
        .slice(0, 6)
        .map(function (item) {
          if (item.kind === "value") return MemoryViz.primitiveText(item);
          return "…";
        })
        .join(", ");
      const suffix = entry.length > 6 || entry.truncated ? ", …" : "";
      const bracket = entry.kind === "tuple" ? ["(", ")"] : ["[", "]"];
      return bracket[0] + items + suffix + bracket[1];
    }
    if (entry.kind === "dict") {
      return "{… " + entry.length + " пар}";
    }
    return MemoryViz.primitiveText(entry);
  },

  primitiveText(cell) {
    if (!cell || cell.value === undefined) return String(cell && cell.type ? cell.type : "?");
    if (cell.type === "str") return JSON.stringify(cell.value);
    if (cell.type === "NoneType") return "None";
    return String(cell.value);
  },

  escape(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  },
};
