/**
 * Простая подсветка Python для панели кода (без внешних зависимостей).
 */
const PythonHighlighter = {
  KEYWORDS: new Set([
    "and",
    "as",
    "break",
    "continue",
    "elif",
    "else",
    "False",
    "for",
    "if",
    "import",
    "in",
    "None",
    "not",
    "or",
    "pass",
    "return",
    "True",
    "while",
    "from",
    "def",
    "class",
  ]),

  BUILTINS: new Set([
    "abs",
    "bool",
    "dict",
    "enumerate",
    "float",
    "input",
    "int",
    "len",
    "list",
    "max",
    "min",
    "print",
    "range",
    "round",
    "set",
    "sorted",
    "str",
    "sum",
    "tuple",
    "type",
    "zip",
  ]),

  escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  },

  findStringEnd(line, start) {
    const quote = line[start];
    let i = start + 1;
    while (i < line.length) {
      if (line[i] === "\\") {
        i += 2;
        continue;
      }
      if (line[i] === quote) {
        return i + 1;
      }
      i++;
    }
    return line.length;
  },

  highlightLine(line) {
    let result = "";
    let i = 0;

    while (i < line.length) {
      const ch = line[i];

      if (ch === "#") {
        result += '<span class="py-hl-comment">' + this.escapeHtml(line.slice(i)) + "</span>";
        break;
      }

      if (ch === "'" || ch === '"') {
        const end = this.findStringEnd(line, i);
        result += '<span class="py-hl-string">' + this.escapeHtml(line.slice(i, end)) + "</span>";
        i = end;
        continue;
      }

      if (/[0-9]/.test(ch)) {
        let j = i + 1;
        while (j < line.length && /[0-9._]/.test(line[j])) j++;
        result += '<span class="py-hl-number">' + this.escapeHtml(line.slice(i, j)) + "</span>";
        i = j;
        continue;
      }

      if (/[A-Za-z_\u0400-\u04FF]/.test(ch)) {
        let j = i + 1;
        while (j < line.length && /[\w\u0400-\u04FF]/.test(line[j])) j++;
        const word = line.slice(i, j);
        let cls = "py-hl-name";
        if (this.KEYWORDS.has(word)) cls = "py-hl-keyword";
        else if (this.BUILTINS.has(word)) cls = "py-hl-builtin";
        result += '<span class="' + cls + '">' + this.escapeHtml(word) + "</span>";
        i = j;
        continue;
      }

      if ("+-*/%=<>!:.".includes(ch)) {
        let j = i + 1;
        while (j < line.length && "<>=!".includes(line[j])) j++;
        result += '<span class="py-hl-op">' + this.escapeHtml(line.slice(i, j)) + "</span>";
        i = j;
        continue;
      }

      result += this.escapeHtml(ch);
      i++;
    }

    return result;
  },

  highlight(code) {
    const text = String(code);
    if (!text) return "";
    const lines = text.split("\n");
    const html = lines.map((line) => this.highlightLine(line)).join("\n");
    return text.endsWith("\n") ? html + "\n" : html;
  },

  highlightSegment(text) {
    if (!text) return "";
    return this.highlightLine(text);
  },

  /**
   * Подсветка с диапазонами синхронизации блок↔код.
   * @param {string} code
   * @param {Array<{line: number, start: number, end: number, kind?: string}>} ranges
   */
  highlightWithRanges(code, ranges) {
    const text = String(code);
    if (!text) return "";
    const lines = text.split("\n");
    const byLine = {};
    (ranges || []).forEach(function (r) {
      if (r.line < 0 || r.line >= lines.length) return;
      if (!byLine[r.line]) byLine[r.line] = [];
      byLine[r.line].push(r);
    });

    const html = lines
      .map(function (line, lineIdx) {
        const lineRanges = byLine[lineIdx];
        if (!lineRanges || !lineRanges.length) {
          return PythonHighlighter.highlightLine(line);
        }
        const sorted = lineRanges.slice().sort(function (a, b) {
          return a.start - b.start;
        });
        let result = "";
        let pos = 0;
        sorted.forEach(function (range) {
          const start = Math.max(0, Math.min(range.start, line.length));
          const end = Math.max(start, Math.min(range.end, line.length));
          if (start > pos) {
            result += PythonHighlighter.highlightSegment(line.slice(pos, start));
          }
          const cls =
            range.kind === "keyword"
              ? "py-sync-hl py-sync-hl--keyword"
              : range.kind === "drag"
                ? "py-sync-hl py-sync-hl--drag"
                : "py-sync-hl";
          result +=
            '<span class="' +
            cls +
            '">' +
            PythonHighlighter.highlightSegment(line.slice(start, end)) +
            "</span>";
          pos = end;
        });
        if (pos < line.length) {
          result += PythonHighlighter.highlightSegment(line.slice(pos));
        }
        return result;
      })
      .join("\n");

    return text.endsWith("\n") ? html + "\n" : html;
  },
};
