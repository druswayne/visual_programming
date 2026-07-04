/**
 * Генератор Python-кода из блоков Blockly + режим пошаговой отладки.
 */

let debugMarkersEnabled = false;

function getPythonGenerator() {
  if (typeof python !== "undefined" && python.pythonGenerator) {
    return python.pythonGenerator;
  }
  if (typeof Blockly !== "undefined" && Blockly.Python) {
    return Blockly.Python;
  }
  return null;
}

function sanitizeUnicodeName(name) {
  let safe = String(name).trim().replace(/\s+/g, "_");
  safe = safe.replace(/[^\p{L}\p{N}_]/gu, "_");
  safe = safe.replace(/_+/g, "_").replace(/^_|_$/g, "");
  if (!safe) return null;
  if (/^\d/.test(safe)) {
    safe = "my_" + safe;
  }
  if (/^[\p{L}_][\p{L}\p{N}_]*$/u.test(safe)) {
    return safe;
  }
  return null;
}

function patchBlocklyNamesUnicode() {
  if (typeof Blockly === "undefined" || !Blockly.Names) return;
  const proto = Blockly.Names.prototype;
  if (proto._pyblocksUnicodePatched) return;

  const original = proto.safeName;
  proto.safeName = function (name) {
    const safe = sanitizeUnicodeName(name);
    if (safe) return safe;
    return original.call(this, typeof name === "string" ? name : String(name ?? ""));
  };
  proto._pyblocksUnicodePatched = true;
}

function patchUnicodeVariableNames(gen) {
  if (!gen || gen._unicodePatched) return;

  const originalInit = gen.init.bind(gen);
  gen.init = function (workspace) {
    originalInit(workspace);
    if (this.definitions_) {
      delete this.definitions_.variables;
    }
    patchNameDBSafeName(this.nameDB_);
    applyDebugMarkers(this);
  };

  const originalGetVariableName = gen.getVariableName.bind(gen);
  gen.getVariableName = function (idOrName) {
    const nameDB = this.nameDB_;
    if (nameDB && nameDB.variableMap_) {
      const varModel = nameDB.variableMap_.getVariableById(idOrName);
      if (varModel) {
        const safe = sanitizeUnicodeName(varModel.name);
        if (safe) return safe;
      }
    }
    return originalGetVariableName(idOrName);
  };

  gen._unicodePatched = true;
}

function patchNameDBSafeName(nameDB) {
  if (!nameDB || nameDB._unicodeSafeNamePatched) return;

  const original =
    typeof nameDB.safeName === "function"
      ? nameDB.safeName.bind(nameDB)
      : typeof nameDB.safeName_ === "function"
        ? nameDB.safeName_.bind(nameDB)
        : null;

  if (!original) return;

  const patched = function (name) {
    const safe = sanitizeUnicodeName(name);
    if (safe) return safe;
    const raw = typeof name === "string" ? name : String(name ?? "");
    return original(raw);
  };

  if (typeof nameDB.safeName === "function") {
    nameDB.safeName = patched;
  } else {
    nameDB.safeName_ = patched;
  }

  nameDB._unicodeSafeNamePatched = true;
}

function applyDebugMarkers(gen) {
  if (!debugMarkersEnabled) {
    gen.STATEMENT_PREFIX = null;
    return;
  }

  if (!gen._originalInjectId) {
    gen._originalInjectId = gen.injectId.bind(gen);
    gen.injectId = function (template, block) {
      if (typeof template === "string" && template.indexOf("# @block:") === 0) {
        return "# @block:" + block.id + "\n";
      }
      return gen._originalInjectId(template, block);
    };
  }

  gen.STATEMENT_PREFIX = "# @block:%1\n";
}

function registerCustomGenerators() {
  const gen = getPythonGenerator();
  if (!gen || gen._pyblocksCustomRegistered) return;

  patchBlocklyNamesUnicode();
  patchUnicodeVariableNames(gen);
  const Order = (typeof python !== "undefined" && python.Order) || gen;

  gen.forBlock["py_ifelse"] = function (block, generator) {
    const condition = generator.valueToCode(block, "IF0", Order.NONE) || "False";
    const branch = generator.statementToCode(block, "DO0");
    const elseBranch = generator.statementToCode(block, "ELSE");
    let code = "if " + condition + ":\n" + branch;
    if (elseBranch) code += "else:\n" + elseBranch;
    return code;
  };

  gen.forBlock["py_if"] = function (block, generator) {
    let code = "";
    let i = 0;
    while (block.getInput("IF" + i)) {
      const condition = generator.valueToCode(block, "IF" + i, Order.NONE) || "False";
      const branch = generator.statementToCode(block, "DO" + i);
      code += (i === 0 ? "if " : "elif ") + condition + ":\n" + branch;
      i++;
    }
    if (block.getInput("ELSE")) {
      const elseBranch = generator.statementToCode(block, "ELSE");
      if (elseBranch) code += "else:\n" + elseBranch;
    }
    return code;
  };

  gen.forBlock["py_for"] = function (block, generator) {
    const variable = generator.getVariableName(block.getFieldValue("VAR"));
    const seq = generator.valueToCode(block, "SEQ", Order.NONE) || "[]";
    const branch = generator.statementToCode(block, "DO");
    return "for " + variable + " in " + seq + ":\n" + branch;
  };

  gen.forBlock["py_break"] = function () {
    return "break\n";
  };

  gen.forBlock["py_continue"] = function () {
    return "continue\n";
  };

  gen.forBlock["variables_set"] = function (block, generator) {
    const varName = generator.getVariableName(block.getFieldValue("VAR"));
    const value = generator.valueToCode(block, "VALUE", Order.NONE) || "0";
    return varName + " = " + value + "\n";
  };

  gen.forBlock["py_while"] = function (block, generator) {
    const cond = generator.valueToCode(block, "COND", Order.NONE) || "False";
    const branch = generator.statementToCode(block, "DO");
    return "while " + cond + ":\n" + branch;
  };

  gen.forBlock["py_comment"] = function (block) {
    const text = String(block.getFieldValue("TEXT") || "").replace(/\n/g, "\n# ");
    return "# " + text + "\n";
  };

  gen.forBlock["py_pass"] = function () {
    return "pass\n";
  };

  gen.forBlock["py_len"] = function (block, generator) {
    const obj = generator.valueToCode(block, "OBJ", Order.NONE) || "''";
    return ["len(" + obj + ")", Order.FUNCTION_CALL];
  };

  gen.forBlock["py_none"] = function () {
    return ["None", Order.ATOMIC];
  };

  gen.forBlock["py_import_math"] = function () {
    return "import math\n";
  };

  gen.forBlock["py_import_random"] = function () {
    return "import random\n";
  };

  gen.forBlock["py_convert"] = function (block, generator) {
    const value = generator.valueToCode(block, "VALUE", Order.NONE) || "0";
    const target = block.getFieldValue("TO");
    const fnMap = { STR: "str", INT: "int", FLOAT: "float", LIST: "list" };
    return [fnMap[target] + "(" + value + ")", Order.FUNCTION_CALL];
  };

  gen.forBlock["py_type_check"] = function (block, generator) {
    const value = generator.valueToCode(block, "VALUE", Order.NONE) || "None";
    const typeMap = { INT: "int", STR: "str", LIST: "list", FLOAT: "float", BOOL: "bool" };
    const pyType = typeMap[block.getFieldValue("TYPE")] || "int";
    return ["isinstance(" + value + ", " + pyType + ")", Order.RELATIONAL];
  };

  gen.forBlock["py_in"] = function (block, generator) {
    const needle = generator.valueToCode(block, "NEEDLE", Order.NONE) || "None";
    const haystack = generator.valueToCode(block, "HAYSTACK", Order.NONE) || "[]";
    return [needle + " in " + haystack, Order.RELATIONAL];
  };

  gen.forBlock["py_range"] = function (block, generator) {
    const fromVal = generator.valueToCode(block, "FROM", Order.NONE) || "0";
    const toVal = generator.valueToCode(block, "TO", Order.NONE) || "0";
    const byVal = generator.valueToCode(block, "BY", Order.NONE) || "1";
    return ["range(" + fromVal + ", " + toVal + ", " + byVal + ")", Order.FUNCTION_CALL];
  };

  gen.forBlock["py_paren"] = function (block, generator) {
    const expr = generator.valueToCode(block, "EXPR", Order.NONE) || "0";
    return ["(" + expr + ")", Order.ATOMIC];
  };

  function mathBinaryCode(block, generator, pyOp, orderKey) {
    const order = Order[orderKey];
    const parts = [];
    let i = 0;
    while (block.getInput("ARG" + i)) {
      const code = generator.valueToCode(block, "ARG" + i, order);
      if (code) parts.push(code);
      i++;
    }
    if (!parts.length) {
      const legacyA = generator.valueToCode(block, "A", order);
      const legacyB = generator.valueToCode(block, "B", order);
      if (legacyA || legacyB) {
        return [(legacyA || "0") + " " + pyOp + " " + (legacyB || "0"), order];
      }
      parts.push("0");
    }
    return [parts.join(" " + pyOp + " "), order];
  }

  gen.forBlock["py_add"] = function (block, generator) {
    return mathBinaryCode(block, generator, "+", "ADDITIVE");
  };

  gen.forBlock["py_sub"] = function (block, generator) {
    return mathBinaryCode(block, generator, "-", "ADDITIVE");
  };

  gen.forBlock["py_mul"] = function (block, generator) {
    return mathBinaryCode(block, generator, "*", "MULTIPLICATIVE");
  };

  gen.forBlock["py_div"] = function (block, generator) {
    return mathBinaryCode(block, generator, "/", "MULTIPLICATIVE");
  };

  gen.forBlock["py_floordiv"] = function (block, generator) {
    return mathBinaryCode(block, generator, "//", "MULTIPLICATIVE");
  };

  gen.forBlock["py_pow"] = function (block, generator) {
    return mathBinaryCode(block, generator, "**", "EXPONENTIATION");
  };

  gen.forBlock["py_mod"] = function (block, generator) {
    return mathBinaryCode(block, generator, "%", "MULTIPLICATIVE");
  };

  function naryMathCode(block, generator, op, order) {
    const parts = [];
    let i = 0;
    while (block.getInput("ADD" + i)) {
      const code = generator.valueToCode(block, "ADD" + i, order);
      if (code) parts.push(code);
      i++;
    }
    if (!parts.length) parts.push("0");
    return [parts.join(" " + op + " "), order];
  }

  gen.forBlock["py_sum"] = function (block, generator) {
    return naryMathCode(block, generator, "+", Order.ADDITIVE);
  };

  gen.forBlock["py_product"] = function (block, generator) {
    return naryMathCode(block, generator, "*", Order.MULTIPLICATIVE);
  };

  gen.forBlock["py_str_method"] = function (block, generator) {
    const obj = generator.valueToCode(block, "OBJ", Order.NONE) || "''";
    const arg = generator.valueToCode(block, "ARG", Order.NONE) || "''";
    const method = block.getFieldValue("METHOD");
    let expr;
    switch (method) {
      case "UPPER":
        expr = obj + ".upper()";
        break;
      case "LOWER":
        expr = obj + ".lower()";
        break;
      case "STRIP":
        expr = obj + ".strip()";
        break;
      case "CAP":
        expr = obj + ".capitalize()";
        break;
      case "TITLE":
        expr = obj + ".title()";
        break;
      case "SPLIT":
        expr = obj + ".split(" + arg + ")";
        break;
      case "REPLACE":
        expr = obj + ".replace(" + arg + ", '')";
        break;
      case "COUNT":
        expr = obj + ".count(" + arg + ")";
        break;
      case "STARTSWITH":
        expr = obj + ".startswith(" + arg + ")";
        break;
      case "ENDSWITH":
        expr = obj + ".endswith(" + arg + ")";
        break;
      case "ISDIGIT":
        expr = obj + ".isdigit()";
        break;
      case "ISALPHA":
        expr = obj + ".isalpha()";
        break;
      default:
        expr = obj;
    }
    const boolMethods = ["STARTSWITH", "ENDSWITH", "ISDIGIT", "ISALPHA"];
    const order = boolMethods.indexOf(method) >= 0 ? Order.RELATIONAL : Order.FUNCTION_CALL;
    return [expr, order];
  };

  gen.forBlock["py_list_method"] = function (block, generator) {
    const obj = generator.valueToCode(block, "OBJ", Order.NONE) || "[]";
    const arg = generator.valueToCode(block, "ARG", Order.NONE) || "0";
    const method = block.getFieldValue("METHOD");
    switch (method) {
      case "APPEND":
        return obj + ".append(" + arg + ")\n";
      case "INSERT":
        return obj + ".insert(0, " + arg + ")\n";
      case "REMOVE":
        return obj + ".remove(" + arg + ")\n";
      case "CLEAR":
        return obj + ".clear()\n";
      default:
        return "pass\n";
    }
  };

  gen.forBlock["py_list_expr"] = function (block, generator) {
    const obj = generator.valueToCode(block, "OBJ", Order.NONE) || "[]";
    const arg = generator.valueToCode(block, "ARG", Order.NONE) || "0";
    const method = block.getFieldValue("METHOD");
    let expr;
    switch (method) {
      case "POP":
        expr = obj + ".pop()";
        break;
      case "COUNT":
        expr = obj + ".count(" + arg + ")";
        break;
      case "INDEX":
        expr = obj + ".index(" + arg + ")";
        break;
      case "SORTED":
        expr = "sorted(" + obj + ")";
        break;
      case "REVERSED":
        expr = "list(reversed(" + obj + "))";
        break;
      default:
        expr = obj;
    }
    return [expr, Order.FUNCTION_CALL];
  };

  gen.forBlock["py_input"] = function (block, generator) {
    const prompt = String(block.getFieldValue("PROMPT") || "");
    const quoted = generator.quote_(prompt);
    return ["input(" + quoted + ")", Order.FUNCTION_CALL];
  };

  gen.forBlock["py_start"] = function () {
    return "";
  };

  gen.forBlock["py_end"] = function () {
    return "";
  };

  registerPyMethodGenerators(gen, Order);

  gen.INDENT = "    ";
  gen._pyblocksCustomRegistered = true;
}

function registerPyMethodGenerators(gen, Order) {
  if (typeof PY_STR_METHOD_DEFS === "undefined") return;

  PY_STR_METHOD_DEFS.forEach(function (def) {
    gen.forBlock[def.type] = function (block, generator) {
      const obj = generator.valueToCode(block, "OBJ", Order.NONE) || "''";

      if (def.join) {
        const list = generator.valueToCode(block, "LIST", Order.NONE) || "[]";
        return [obj + ".join(" + list + ")", Order.FUNCTION_CALL];
      }

      if (!def.args || !def.args.length) {
        const expr = obj + "." + def.py;
        const order = def.bool ? Order.RELATIONAL : Order.FUNCTION_CALL;
        return [expr, order];
      }

      const argCodes = def.args.map(function (arg) {
        return generator.valueToCode(block, arg.name, Order.NONE);
      });

      let expr;
      if (def.py === "split" && hasOptionalArg(block, "SEP")) {
        expr = obj + ".split()";
      } else if (def.py === "replace") {
        const oldVal = argCodes[0] || "''";
        const newVal = argCodes[1] || "''";
        expr = obj + ".replace(" + oldVal + ", " + newVal + ")";
      } else {
        const parts = argCodes.map(function (code, i) {
          return code || (def.args[i].check === "String" ? "''" : "0");
        });
        expr = obj + "." + def.py + "(" + parts.join(", ") + ")";
      }

      const order = def.bool ? Order.RELATIONAL : Order.FUNCTION_CALL;
      return [expr, order];
    };
  });

  PY_LIST_STMT_DEFS.forEach(function (def) {
    gen.forBlock[def.type] = function (block, generator) {
      const obj = generator.valueToCode(block, "OBJ", Order.NONE) || "[]";

      if (!def.args || !def.args.length) {
        return obj + "." + def.py + "\n";
      }

      if (def.py === "insert") {
        const index = generator.valueToCode(block, "INDEX", Order.NONE) || "0";
        const value = generator.valueToCode(block, "VALUE", Order.NONE) || "None";
        return obj + ".insert(" + index + ", " + value + ")\n";
      }

      const argName = def.args[0].name;
      const arg = generator.valueToCode(block, argName, Order.NONE) || "None";
      return obj + "." + def.py + "(" + arg + ")\n";
    };
  });

  PY_LIST_EXPR_DEFS.forEach(function (def) {
    gen.forBlock[def.type] = function (block, generator) {
      const obj = generator.valueToCode(block, "OBJ", Order.NONE) || "[]";

      if (def.py === "sorted") {
        return ["sorted(" + obj + ")", Order.FUNCTION_CALL];
      }
      if (def.py === "reversed") {
        return ["list(reversed(" + obj + "))", Order.FUNCTION_CALL];
      }

      if (!def.args || !def.args.length) {
        return [obj + "." + def.py, Order.FUNCTION_CALL];
      }

      if (def.py === "pop" && hasOptionalArg(block, "INDEX")) {
        return [obj + ".pop()", Order.FUNCTION_CALL];
      }

      const argName = def.args[0].name;
      const arg = generator.valueToCode(block, argName, Order.NONE) || "None";
      return [obj + "." + def.py + "(" + arg + ")", Order.FUNCTION_CALL];
    };
  });
}

registerCustomGenerators();

function cleanGeneratedCode(code) {
  return code
    .replace(/\n{3,}/g, "\n\n")
    .replace(/[ \t]+\n/g, "\n")
    .trim();
}

/** Код одного statement-блока без scrub_ (Blockly иначе дублирует следующие блоки в цепочке). */
function generateSingleBlockCode(gen, block) {
  if (!block || (typeof block.isEnabled === "function" && !block.isEnabled())) return "";

  const handler = gen.forBlock[block.type];
  if (typeof handler !== "function") return "";

  let code = handler(block, gen);
  if (Array.isArray(code)) {
    code = code[0];
  }
  if (typeof code !== "string" || !code) {
    return "";
  }

  if (gen.STATEMENT_PREFIX && !block.suppressPrefixSuffix) {
    code = gen.injectId(gen.STATEMENT_PREFIX, block) + code;
  }
  if (gen.STATEMENT_SUFFIX && !block.suppressPrefixSuffix) {
    code += gen.injectId(gen.STATEMENT_SUFFIX, block);
  }
  return code;
}

function generateFromProgramFrame(gen, workspace) {
  const startBlock = workspace.getTopBlocks(true).find(function (b) {
    return b.type === "py_start";
  });

  if (!startBlock) {
    return gen.workspaceToCode(workspace);
  }

  let code = "";
  let block = startBlock.getNextBlock();

  while (block) {
    if (block.type === "py_end") break;
    const blockCode = generateSingleBlockCode(gen, block);
    if (blockCode) {
      code += blockCode;
    }
    block = block.getNextBlock();
  }

  return cleanGeneratedCode(gen.finish(code));
}

function generatePythonCode(workspace, withDebugMarkers) {
  const gen = getPythonGenerator();
  if (!gen) return "# Ошибка: генератор Python не загружен";

  const prev = debugMarkersEnabled;
  debugMarkersEnabled = !!withDebugMarkers;

  try {
    patchBlocklyNamesUnicode();
    patchUnicodeVariableNames(gen);
    gen.init(workspace);
    const code = generateFromProgramFrame(gen, workspace);
    return cleanGeneratedCode(code);
  } catch (err) {
    console.error("generatePythonCode:", err);
    return "# Ошибка генерации: " + err.message;
  } finally {
    debugMarkersEnabled = prev;
  }
}

function parseDebugMarkers(debugLines) {
  const lineBlockMap = {};
  const debugLineToDisplay = {};
  const rawDisplay = [];
  let pendingBlock = null;

  debugLines.forEach(function (line, index) {
    const debugLineNo = index + 1;
    const stripped = line.trim();

    if (stripped.indexOf("# @block:") === 0) {
      pendingBlock = stripped.slice(9).trim().replace(/^['"]|['"]$/g, "");
      return;
    }

    rawDisplay.push({ debugLineNo: debugLineNo, line: line });

    if (pendingBlock && stripped && stripped.indexOf("#") !== 0) {
      lineBlockMap[debugLineNo] = pendingBlock;
      pendingBlock = null;
    }
  });

  while (rawDisplay.length && rawDisplay[0].line.trim() === "") {
    rawDisplay.shift();
  }
  while (rawDisplay.length && rawDisplay[rawDisplay.length - 1].line.trim() === "") {
    rawDisplay.pop();
  }

  const displayLines = rawDisplay.map(function (entry) {
    return entry.line;
  });

  rawDisplay.forEach(function (entry, index) {
    debugLineToDisplay[entry.debugLineNo] = index + 1;
  });

  return { debugLineToDisplay: debugLineToDisplay, lineBlockMap: lineBlockMap, displayLines: displayLines };
}

function generatePythonDebugData(workspace) {
  const debugCode = generatePythonCode(workspace, true);
  const debugLines = debugCode.split("\n");
  const cleanCode = generatePythonCode(workspace, false);
  const mapping = parseDebugMarkers(debugLines);

  return {
    code: debugCode,
    lines: debugLines,
    displayLines: mapping.displayLines.length ? mapping.displayLines : cleanCode.trim().split("\n"),
    cleanCode: cleanCode,
    debugLineToDisplay: mapping.debugLineToDisplay,
    lineBlockMap: mapping.lineBlockMap,
  };
}

function formatValueForDisplay(value) {
  if (value === null || value === undefined) return "None";
  if (typeof value === "string") return JSON.stringify(value);
  if (typeof value === "object") return JSON.stringify(value);
  return String(value);
}

/** Ключевые слова Python для statement-блоков */
const PYBLOCKS_STATEMENT_KEYWORDS = {
  py_while: "while",
  py_for: "for",
  py_if: "if",
  py_ifelse: "if",
  py_break: "break",
  py_continue: "continue",
  py_pass: "pass",
  py_import_math: "import",
  py_import_random: "import",
  text_print: "print",
  variables_set: null,
  controls_if: "if",
  controls_repeat_ext: "for",
};

/** Ключевое слово по типу блока (для подсветки при перетаскивании из палитры) */
const PYBLOCKS_TYPE_KEYWORD = {
  py_while: "while",
  py_for: "for",
  py_if: "if",
  py_ifelse: "if",
  py_break: "break",
  py_continue: "continue",
  py_pass: "pass",
  py_import_math: "import",
  py_import_random: "import",
  text_print: "print",
  controls_if: "if",
  controls_repeat_ext: "for",
  controls_whileUntil: "while",
};

function extractValueCode(gen, block) {
  if (!block || !gen) return "";
  try {
    const handler = gen.forBlock[block.type];
    if (typeof handler === "function") {
      let code = handler(block, gen);
      if (Array.isArray(code)) code = code[0];
      if (typeof code === "string") return code;
    }
    if (typeof gen.blockToCode === "function") {
      let code = gen.blockToCode(block);
      if (Array.isArray(code)) code = code[0];
      if (typeof code === "string") return code;
    }
  } catch (e) {
    /* ignore */
  }
  return "";
}

function findLineFromIndex(lines, snippet, fromLine) {
  if (!snippet) return -1;
  const trimmed = snippet.trim();
  for (let i = Math.max(0, fromLine); i < lines.length; i++) {
    if (lines[i].trim() === trimmed) {
      return i;
    }
  }
  return -1;
}

function mapValueBlockTree(gen, block, parentExpr, line, baseCol, mappings) {
  if (!block) return;
  const ownCode = extractValueCode(gen, block);
  if (!ownCode) return;

  let start = baseCol;
  const pos = parentExpr.indexOf(ownCode);
  if (pos >= 0) start = baseCol + pos;
  const end = start + ownCode.length;

  mappings[block.id] = {
    blockId: block.id,
    blockType: block.type,
    line: line,
    start: start,
    end: end,
    kind: "expression",
  };

  block.inputList.forEach(function (input) {
    if (input.type !== Blockly.INPUT_VALUE) return;
    const child = block.getInputTargetBlock(input.name);
    if (child) {
      mapValueBlockTree(gen, child, ownCode, line, start, mappings);
    }
  });
}

function analyzeStatementMapping(gen, block, firstLine, lineIdx, mappings) {
  const kw = PYBLOCKS_STATEMENT_KEYWORDS[block.type];
  const entry = {
    blockId: block.id,
    blockType: block.type,
    line: lineIdx,
    keyword: null,
    slots: {},
  };

  if (kw) {
    const kwPos = firstLine.indexOf(kw);
    if (kwPos >= 0) {
      entry.keyword = { start: kwPos, end: kwPos + kw.length };
    }
  }

  const Order = (typeof python !== "undefined" && python.Order) || gen;

  if (block.type === "py_while") {
    const cond = gen.valueToCode(block, "COND", Order.NONE) || "False";
    const condStart = firstLine.indexOf(cond);
    if (condStart >= 0) {
      entry.slots.COND = { start: condStart, end: condStart + cond.length };
      const condBlock = block.getInputTargetBlock("COND");
      if (condBlock) {
        mapValueBlockTree(gen, condBlock, cond, lineIdx, condStart, mappings);
      }
    }
  } else if (block.type === "py_for") {
    const seq = gen.valueToCode(block, "SEQ", Order.NONE) || "[]";
    const seqStart = firstLine.lastIndexOf(seq);
    if (seqStart >= 0) {
      entry.slots.SEQ = { start: seqStart, end: seqStart + seq.length };
      const seqBlock = block.getInputTargetBlock("SEQ");
      if (seqBlock) {
        mapValueBlockTree(gen, seqBlock, seq, lineIdx, seqStart, mappings);
      }
    }
    const varName = gen.getVariableName(block.getFieldValue("VAR"));
    const varPos = firstLine.indexOf(varName);
    if (varPos >= 0) {
      entry.slots.VAR = { start: varPos, end: varPos + varName.length };
    }
  } else if (block.type === "py_if" || block.type === "py_ifelse" || block.type === "controls_if") {
    const cond = gen.valueToCode(block, "IF0", Order.NONE) || "False";
    const condStart = firstLine.indexOf(cond);
    if (condStart >= 0) {
      entry.slots.IF0 = { start: condStart, end: condStart + cond.length };
      const condBlock = block.getInputTargetBlock("IF0");
      if (condBlock) {
        mapValueBlockTree(gen, condBlock, cond, lineIdx, condStart, mappings);
      }
    }
  } else if (block.type === "variables_set") {
    const value = gen.valueToCode(block, "VALUE", Order.NONE) || "0";
    entry.statement = { start: 0, end: firstLine.length };
    const valStart = firstLine.indexOf(value);
    if (valStart >= 0) {
      entry.slots.VALUE = { start: valStart, end: valStart + value.length };
      const valBlock = block.getInputTargetBlock("VALUE");
      if (valBlock && !(typeof valBlock.isShadow === "function" && valBlock.isShadow())) {
        mapValueBlockTree(gen, valBlock, value, lineIdx, valStart, mappings);
      }
    }
  } else if (block.type === "py_comment") {
    entry.statement = { start: 0, end: firstLine.length };
  } else if (block.type === "text_print") {
    const msg = gen.valueToCode(block, "TEXT", Order.NONE);
    if (msg) {
      const msgStart = firstLine.indexOf(msg);
      if (msgStart >= 0) {
        entry.slots.TEXT = { start: msgStart, end: msgStart + msg.length };
        const msgBlock = block.getInputTargetBlock("TEXT");
        if (msgBlock) {
          mapValueBlockTree(gen, msgBlock, msg, lineIdx, msgStart, mappings);
        }
      }
    }
  }

  block.inputList.forEach(function (input) {
    if (input.type !== Blockly.INPUT_VALUE) return;
    if (entry.slots[input.name]) return;
    const child = block.getInputTargetBlock(input.name);
    if (!child) return;
    const expr = gen.valueToCode(block, input.name, Order.NONE);
    if (!expr) return;
    const pos = firstLine.indexOf(expr);
    if (pos >= 0) {
      entry.slots[input.name] = { start: pos, end: pos + expr.length };
      mapValueBlockTree(gen, child, expr, lineIdx, pos, mappings);
    }
  });

  if (!entry.keyword && !entry.statement && !Object.keys(entry.slots).length && firstLine.trim()) {
    entry.statement = { start: 0, end: firstLine.length };
  }

  mappings[block.id] = entry;
}

function walkStatementChain(gen, block, lineCursor, mappings) {
  while (block) {
    if (block.type === "py_end") break;
    if (typeof block.isEnabled === "function" && !block.isEnabled()) {
      block = block.getNextBlock();
      continue;
    }

    const blockCode = generateSingleBlockCode(gen, block);
    if (blockCode) {
      const blockLines = blockCode.replace(/\n$/, "").split("\n");
      const firstLine = blockLines[0] || "";
      analyzeStatementMapping(gen, block, firstLine, lineCursor, mappings);
      let innerLine = lineCursor + 1;
      block.inputList.forEach(function (input) {
        if (input.type !== Blockly.NEXT_STATEMENT) return;
        const child = block.getInputTargetBlock(input.name);
        if (child) {
          innerLine = walkStatementChain(gen, child, innerLine, mappings);
        }
      });
      lineCursor += blockLines.length;
    }

    block = block.getNextBlock();
  }
  return lineCursor;
}

function generatePythonCodeWithMapping(workspace) {
  const gen = getPythonGenerator();
  if (!gen) {
    return { code: "# Ошибка: генератор Python не загружен", mappings: {} };
  }

  const prev = debugMarkersEnabled;
  debugMarkersEnabled = false;

  try {
    patchBlocklyNamesUnicode();
    patchUnicodeVariableNames(gen);
    gen.init(workspace);
    const code = generateFromProgramFrame(gen, workspace);
    const cleanCode = cleanGeneratedCode(code);
    const mappings = {};

    const startBlock = workspace.getTopBlocks(true).find(function (b) {
      return b.type === "py_start";
    });

    if (startBlock) {
      walkStatementChain(gen, startBlock.getNextBlock(), 0, mappings);
    } else {
      workspace.getTopBlocks(true).forEach(function (top) {
        walkStatementChain(gen, top, 0, mappings);
      });
    }

    return { code: cleanCode, mappings: mappings };
  } catch (err) {
    console.error("generatePythonCodeWithMapping:", err);
    return { code: "# Ошибка генерации: " + err.message, mappings: {} };
  } finally {
    debugMarkersEnabled = prev;
  }
}
