/**
 * Кастомные блоки PyBlocks — максимально близко к Python.
 */
function pbMsg(key, fallback) {
  const messages = window.PYBLOCKS_BLOCK_MSG || {};
  return messages[key] || fallback;
}

function pbOpt(key, fallback, value) {
  return [pbMsg(key, fallback), value];
}

function getPyblocksCustomBlocks() {
  return [
  {
    type: "py_start",
    message0: pbMsg("start", "▶  НАЧАЛО ПРОГРАММЫ"),
    nextStatement: null,
    style: "program_start_blocks",
    hat: "cap",
    tooltip: pbMsg("tooltip.start", "Подключайте блоки программы ниже"),
  },
  {
    type: "py_end",
    message0: pbMsg("end", "■  КОНЕЦ ПРОГРАММЫ"),
    previousStatement: null,
    style: "program_end_blocks",
    tooltip: pbMsg("tooltip.end", "Конец программы. Отсоедините и отложите в сторону, чтобы вставить блоки в конец цепочки"),
  },
  {
    type: "py_ifelse",
    message0: pbMsg("ifelse", "если %1"),
    args0: [{ type: "input_value", name: "IF0", check: "Boolean" }],
    message1: "%1",
    args1: [{ type: "input_statement", name: "DO0" }],
    message2: pbMsg("ifelse_else", "иначе %1"),
    args2: [{ type: "input_statement", name: "ELSE" }],
    previousStatement: null,
    nextStatement: null,
    style: "logic_blocks",
    tooltip: pbMsg("tooltip.ifelse", "Если условие истинно — выполняется верхняя ветка, иначе — нижняя"),
  },
  {
    type: "py_for",
    message0: pbMsg("for", "для %1 в %2"),
    args0: [
      { type: "field_variable", name: "VAR", variable: pbMsg("for_var_default", "элемент") },
      { type: "input_value", name: "SEQ" },
    ],
    message1: "%1",
    args1: [{ type: "input_statement", name: "DO" }],
    inputsInline: true,
    previousStatement: null,
    nextStatement: null,
    style: "loop_blocks",
    tooltip: pbMsg("tooltip.for", "Цикл for — перебор элементов (список, строка, range(...) и т.д.)"),
  },
  {
    type: "py_while",
    message0: pbMsg("while", "пока %1"),
    args0: [{ type: "input_value", name: "COND", check: "Boolean" }],
    message1: "%1",
    args1: [{ type: "input_statement", name: "DO" }],
    previousStatement: null,
    nextStatement: null,
    style: "loop_blocks",
    tooltip: pbMsg("tooltip.while", "Цикл while — пока условие истинно"),
  },
  {
    type: "py_break",
    message0: pbMsg("break", "прервать цикл"),
    previousStatement: null,
    style: "loop_blocks",
    tooltip: pbMsg("tooltip.break", "break — выйти из цикла"),
  },
  {
    type: "py_continue",
    message0: pbMsg("continue", "следующий шаг цикла"),
    previousStatement: null,
    style: "loop_blocks",
    tooltip: pbMsg("tooltip.continue", "continue — перейти к следующей итерации"),
  },
  {
    type: "py_comment",
    message0: "# %1",
    args0: [{ type: "field_input", name: "TEXT", text: pbMsg("comment_default", "заметка") }],
    previousStatement: null,
    nextStatement: null,
    style: "text_blocks",
    tooltip: pbMsg("tooltip.comment", "Комментарий"),
  },
  {
    type: "py_input",
    message0: pbMsg("input", "ввод(%1)"),
    args0: [{ type: "field_input", name: "PROMPT", text: pbMsg("input_default", "Введите:") }],
    output: "String",
    style: "text_blocks",
    tooltip: pbMsg("tooltip.input", "Ввод текста с клавиатуры (всегда строка)"),
  },
  {
    type: "py_pass",
    message0: pbMsg("pass", "ничего"),
    previousStatement: null,
    nextStatement: null,
    style: "logic_blocks",
    tooltip: pbMsg("tooltip.pass", "Пустая команда (pass)"),
  },
  {
    type: "py_len",
    message0: pbMsg("len", "длина(%1)"),
    args0: [{ type: "input_value", name: "OBJ" }],
    output: "Number",
    style: "math_blocks",
    tooltip: pbMsg("tooltip.len", "Длина строки или списка"),
  },
  {
    type: "py_none",
    message0: pbMsg("none", "пусто"),
    output: null,
    style: "logic_blocks",
    tooltip: pbMsg("tooltip.none", "Пустое значение (None)"),
  },
  {
    type: "py_import_math",
    message0: pbMsg("import_math", "подключить math"),
    previousStatement: null,
    nextStatement: null,
    style: "text_blocks",
    tooltip: pbMsg("tooltip.import_math", "Подключить модуль math"),
  },
  {
    type: "py_import_random",
    message0: pbMsg("import_random", "подключить random"),
    previousStatement: null,
    nextStatement: null,
    style: "text_blocks",
    tooltip: pbMsg("tooltip.import_random", "Подключить модуль random"),
  },
  {
    type: "py_convert",
    message0: pbMsg("convert", "преобразовать %1 в %2"),
    args0: [
      { type: "input_value", name: "VALUE" },
      {
        type: "field_dropdown",
        name: "TO",
        options: [
          pbOpt("convert.str", "строку", "STR"),
          pbOpt("convert.int", "целое", "INT"),
          pbOpt("convert.float", "дробное", "FLOAT"),
          pbOpt("convert.list", "список", "LIST"),
        ],
      },
    ],
    inputsInline: true,
    output: null,
    style: "math_blocks",
    tooltip: pbMsg("tooltip.convert", "Преобразование типа: str, int, float, list"),
  },
  {
    type: "py_type_check",
    message0: pbMsg("type_check", "%1 — это %2?"),
    args0: [
      { type: "input_value", name: "VALUE" },
      {
        type: "field_dropdown",
        name: "TYPE",
        options: [
          pbOpt("type.int", "целое", "INT"),
          pbOpt("type.str", "строка", "STR"),
          pbOpt("type.list", "список", "LIST"),
          pbOpt("type.float", "дробное", "FLOAT"),
          pbOpt("type.bool", "логическое", "BOOL"),
        ],
      },
    ],
    inputsInline: true,
    output: "Boolean",
    style: "logic_blocks",
    tooltip: pbMsg("tooltip.type_check", "Проверка типа значения"),
  },
  {
    type: "py_str_method",
    message0: pbMsg("str_method", "строка %1 → %2 %3"),
    args0: [
      { type: "input_value", name: "OBJ", check: "String" },
      {
        type: "field_dropdown",
        name: "METHOD",
        options: [
          pbOpt("str.upper", "верхний регистр", "UPPER"),
          pbOpt("str.lower", "нижний регистр", "LOWER"),
          pbOpt("str.strip", "обрезать пробелы", "STRIP"),
          pbOpt("str.cap", "с заглавной буквы", "CAP"),
          pbOpt("str.title", "заголовок", "TITLE"),
          pbOpt("str.split", "разделить", "SPLIT"),
          pbOpt("str.replace", "заменить", "REPLACE"),
          pbOpt("str.count", "сколько раз", "COUNT"),
          pbOpt("str.startswith", "начинается с", "STARTSWITH"),
          pbOpt("str.endswith", "заканчивается на", "ENDSWITH"),
          pbOpt("str.isdigit", "это цифры", "ISDIGIT"),
          pbOpt("str.isalpha", "это буквы", "ISALPHA"),
        ],
      },
      { type: "input_value", name: "ARG", check: "String" },
    ],
    inputsInline: true,
    output: null,
    style: "text_blocks",
    tooltip: pbMsg("tooltip.str_method", "Метод строки"),
  },
  {
    type: "py_list_method",
    message0: pbMsg("list_method", "список %1 → %2 %3"),
    args0: [
      { type: "input_value", name: "OBJ", check: "Array" },
      {
        type: "field_dropdown",
        name: "METHOD",
        options: [
          pbOpt("list.append", "добавить", "APPEND"),
          pbOpt("list.insert", "вставить", "INSERT"),
          pbOpt("list.remove", "удалить", "REMOVE"),
          pbOpt("list.clear", "очистить", "CLEAR"),
        ],
      },
      { type: "input_value", name: "ARG" },
    ],
    inputsInline: true,
    previousStatement: null,
    nextStatement: null,
    style: "list_blocks",
    tooltip: pbMsg("tooltip.list_method", "Метод списка (изменяет список)"),
  },
  {
    type: "py_list_expr",
    message0: pbMsg("list_expr", "список %1 → %2 %3"),
    args0: [
      { type: "input_value", name: "OBJ", check: "Array" },
      {
        type: "field_dropdown",
        name: "METHOD",
        options: [
          pbOpt("list.pop", "извлечь", "POP"),
          pbOpt("list.count", "сколько раз", "COUNT"),
          pbOpt("list.index", "номер элемента", "INDEX"),
          pbOpt("list.sorted", "отсортировать", "SORTED"),
          pbOpt("list.reversed", "развернуть", "REVERSED"),
        ],
      },
      { type: "input_value", name: "ARG" },
    ],
    inputsInline: true,
    output: null,
    style: "list_blocks",
    tooltip: pbMsg("tooltip.list_expr", "Метод списка (возвращает значение)"),
  },
  {
    type: "py_in",
    message0: pbMsg("in", "%1 в %2"),
    args0: [
      { type: "input_value", name: "NEEDLE" },
      { type: "input_value", name: "HAYSTACK" },
    ],
    inputsInline: true,
    output: "Boolean",
    style: "logic_blocks",
    tooltip: pbMsg("tooltip.in", "Проверка вхождения элемента"),
  },
  {
    type: "py_paren",
    message0: "( %1 )",
    args0: [{ type: "input_value", name: "EXPR", check: "Number" }],
    inputsInline: true,
    output: "Number",
    style: "math_blocks",
    tooltip: pbMsg("tooltip.paren", "Скобки — меняют порядок вычислений"),
  },
  {
    type: "py_range",
    message0: pbMsg("range", "диапазон(%1, %2, %3)"),
    args0: [
      { type: "input_value", name: "FROM", check: "Number" },
      { type: "input_value", name: "TO", check: "Number" },
      { type: "input_value", name: "BY", check: "Number" },
    ],
    inputsInline: true,
    output: null,
    style: "math_blocks",
    tooltip: pbMsg("tooltip.range", "Диапазон чисел range(...)"),
  },
  ];
}

const STR_METHODS_WITH_ARG = ["SPLIT", "REPLACE", "COUNT", "STARTSWITH", "ENDSWITH"];
const LIST_METHODS_WITH_ARG = ["APPEND", "INSERT", "REMOVE"];
const LIST_EXPR_WITH_ARG = ["COUNT", "INDEX"];

function isBlockTypeRegistered(type) {
  if (Blockly.Blocks[type]) return true;
  if (Blockly.registry && typeof Blockly.registry.hasItem === "function") {
    return Blockly.registry.hasItem(Blockly.registry.Type.BLOCK, type);
  }
  return false;
}

function registerMethodBlockHelpers() {
  function updateMethodArgVisibility(block, methodsWithArg) {
    const method = block.getFieldValue("METHOD");
    const argInput = block.getInput("ARG");
    if (!argInput) return;
    const needsArg = methodsWithArg.indexOf(method) >= 0;
    argInput.setVisible(needsArg);
  }

  Blockly.Blocks["py_str_method"] = {
    init: function () {
      this.jsonInit(getPyblocksCustomBlocks().find(function (b) {
        return b.type === "py_str_method";
      }));
      updateMethodArgVisibility(this, STR_METHODS_WITH_ARG);
      this.setOnChange(function (event) {
        if (event.type === Blockly.Events.BLOCK_CHANGE && event.name === "METHOD") {
          updateMethodArgVisibility(this, STR_METHODS_WITH_ARG);
        }
      });
    },
  };

  Blockly.Blocks["py_list_method"] = {
    init: function () {
      this.jsonInit(getPyblocksCustomBlocks().find(function (b) {
        return b.type === "py_list_method";
      }));
      updateMethodArgVisibility(this, LIST_METHODS_WITH_ARG);
      this.setOnChange(function (event) {
        if (event.type === Blockly.Events.BLOCK_CHANGE && event.name === "METHOD") {
          updateMethodArgVisibility(this, LIST_METHODS_WITH_ARG);
          if (this.getFieldValue("METHOD") === "CLEAR") {
            this.getInput("ARG").setVisible(false);
          }
        }
      });
    },
  };

  Blockly.Blocks["py_list_expr"] = {
    init: function () {
      this.jsonInit(getPyblocksCustomBlocks().find(function (b) {
        return b.type === "py_list_expr";
      }));
      updateMethodArgVisibility(this, LIST_EXPR_WITH_ARG);
      this.setOnChange(function (event) {
        if (event.type === Blockly.Events.BLOCK_CHANGE && event.name === "METHOD") {
          updateMethodArgVisibility(this, LIST_EXPR_WITH_ARG);
        }
      });
    },
  };
}

function registerProgramFrameBlocks() {
  const startJson = getPyblocksCustomBlocks().find(function (b) {
    return b.type === "py_start";
  });
  const endJson = getPyblocksCustomBlocks().find(function (b) {
    return b.type === "py_end";
  });

  if (!Blockly.Blocks["py_start"] || !Blockly.Blocks["py_start"].init) {
    Blockly.Blocks["py_start"] = {
      init: function () {
        this.jsonInit(startJson);
        this.setDeletable(false);
        this.setMovable(true);
        if (typeof this.setStyle === "function") {
          this.setStyle("program_start_blocks");
        }
        this.setOnChange(function (event) {
          if (
            event.type === Blockly.Events.BLOCK_CREATE ||
            event.type === Blockly.Events.BLOCK_MOVE ||
            event.type === Blockly.Events.BLOCK_CHANGE
          ) {
            if (typeof ProgramFrame !== "undefined") {
              ProgramFrame.decorateBlock(this);
            }
          }
        });
      },
    };
  }

  if (!Blockly.Blocks["py_end"] || !Blockly.Blocks["py_end"].init) {
    Blockly.Blocks["py_end"] = {
      init: function () {
        this.jsonInit(endJson);
        this.setDeletable(false);
        this.setMovable(true);
        if (typeof this.setStyle === "function") {
          this.setStyle("program_end_blocks");
        }
        this.setOnChange(function (event) {
          if (
            event.type === Blockly.Events.BLOCK_CREATE ||
            event.type === Blockly.Events.BLOCK_MOVE ||
            event.type === Blockly.Events.BLOCK_CHANGE
          ) {
            if (typeof ProgramFrame !== "undefined") {
              ProgramFrame.decorateBlock(this);
            }
          }
        });
      },
    };
  }
}

function registerMathBinaryBlocks() {
  const ops = [
    {
      type: "py_add",
      symbol: "+",
      py: "+",
      order: "ADDITIVE",
      tooltip: pbMsg("tooltip.math.add", "Сложение. Вставьте другой блок в гнездо слева или справа, например: (2 + 3) + 5."),
      extendable: true,
    },
    {
      type: "py_sub",
      symbol: "−",
      py: "-",
      order: "ADDITIVE",
      tooltip: pbMsg("tooltip.math.sub", "Вычитание. Вставьте блок «+» в левое или правое гнездо, например: 5 − (2 + 3)."),
      extendable: true,
    },
    {
      type: "py_mul",
      symbol: "×",
      py: "*",
      order: "MULTIPLICATIVE",
      tooltip: pbMsg("tooltip.math.mul", "Умножение"),
      extendable: true,
    },
    {
      type: "py_div",
      symbol: "÷",
      py: "/",
      order: "MULTIPLICATIVE",
      tooltip: pbMsg("tooltip.math.div", "Деление"),
      extendable: true,
    },
    {
      type: "py_floordiv",
      symbol: "//",
      py: "//",
      order: "MULTIPLICATIVE",
      tooltip: pbMsg("tooltip.math.floordiv", "Целочисленное деление"),
      extendable: true,
    },
    {
      type: "py_pow",
      symbol: "**",
      py: "**",
      order: "EXPONENTIATION",
      tooltip: pbMsg("tooltip.math.pow", "Степень"),
      extendable: false,
    },
    {
      type: "py_mod",
      symbol: "%",
      py: "%",
      order: "MULTIPLICATIVE",
      tooltip: pbMsg("tooltip.math.mod", "Остаток от деления"),
      extendable: true,
    },
  ];

  ops.forEach(function (def) {
    Blockly.Blocks[def.type] = {
      init: function () {
        this.setStyle("math_blocks");
        this.setOutput(true, "Number");
        this.opSymbol_ = def.symbol;
        this.opDef_ = def;
        this.count_ = 2;
        const hint = def.extendable ? pbMsg("tooltip.math.extend_hint", " ПКМ — добавить операнд справа.") : "";
        this.setTooltip(def.tooltip + hint);
        this.updateInputs_();
      },
      updateInputs_: function () {
        if (this.getInput("OP")) this.removeInput("OP");
        let i = 0;
        while (this.getInput("ARG" + i)) {
          this.removeInput("ARG" + i);
          i++;
        }
        while (this.getInput("A")) this.removeInput("A");
        while (this.getInput("B")) this.removeInput("B");

        for (let j = 0; j < this.count_; j++) {
          if (j === 1) {
            this.appendDummyInput("OP").appendField(this.opSymbol_);
          }
          const inp = this.appendValueInput("ARG" + j).setCheck(null);
          if (j >= 2) inp.appendField(this.opSymbol_);
        }
        this.setInputsInline(true);
      },
      customContextMenu: function (menuOptions) {
        if (!this.opDef_.extendable) return;
        const block = this;
        menuOptions.push({
          text: pbMsg("menu.add_right", "добавить справа"),
          enabled: block.count_ < 8,
          callback: function () {
            block.count_++;
            block.updateInputs_();
          },
        });
        if (block.count_ > 2) {
          menuOptions.push({
            text: pbMsg("menu.remove_right", "убрать справа"),
            callback: function () {
              block.count_--;
              block.updateInputs_();
            },
          });
        }
      },
      mutationToDom: function () {
        const container =
          Blockly.utils && Blockly.utils.xml
            ? Blockly.utils.xml.createElement("mutation")
            : document.createElement("mutation");
        container.setAttribute("items", this.count_);
        return container;
      },
      domToMutation: function (xmlElement) {
        this.count_ = Math.max(2, parseInt(xmlElement.getAttribute("items"), 10) || 2);
        if (!this.opDef_.extendable) this.count_ = 2;
        this.updateInputs_();
      },
      saveExtraState: function () {
        return { items: this.count_ };
      },
      loadExtraState: function (state) {
        this.count_ = Math.max(2, state.items || 2);
        if (!this.opDef_.extendable) this.count_ = 2;
        this.updateInputs_();
      },
    };
  });
}

function registerMathNaryBlocks() {
  function defineNaryBlock(type, opSymbol, addLabel, removeLabel, tooltip) {
    if (Blockly.Blocks[type] && Blockly.Blocks[type].init) return;

    Blockly.Blocks[type] = {
      init: function () {
        this.setStyle("math_blocks");
        this.setOutput(true, "Number");
        this.setTooltip(tooltip);
        this.setInputsInline(true);
        this.count_ = 2;
        this.opSymbol_ = opSymbol;
        this.updateInputs_();
      },
      updateInputs_: function () {
        let i = 0;
        while (this.getInput("ADD" + i)) i++;
        while (i > this.count_) {
          i--;
          this.removeInput("ADD" + i);
        }
        for (let j = 0; j < this.count_; j++) {
          if (!this.getInput("ADD" + j)) {
            const inp = this.appendValueInput("ADD" + j).setCheck("Number");
            if (j > 0) inp.appendField(this.opSymbol_);
          }
        }
      },
      customContextMenu: function (menuOptions) {
        const block = this;
        menuOptions.push({
          text: addLabel,
          enabled: block.count_ < 8,
          callback: function () {
            block.count_++;
            block.updateInputs_();
          },
        });
        if (block.count_ > 2) {
          menuOptions.push({
            text: removeLabel,
            callback: function () {
              block.count_--;
              block.updateInputs_();
            },
          });
        }
      },
      mutationToDom: function () {
        const container =
          Blockly.utils && Blockly.utils.xml
            ? Blockly.utils.xml.createElement("mutation")
            : document.createElement("mutation");
        container.setAttribute("items", this.count_);
        return container;
      },
      domToMutation: function (xmlElement) {
        this.count_ = Math.max(2, parseInt(xmlElement.getAttribute("items"), 10) || 2);
        this.updateInputs_();
      },
    };
  }

  defineNaryBlock(
    "py_sum",
    "+",
    pbMsg("menu.sum.add", "добавить слагаемое"),
    pbMsg("menu.sum.remove", "убрать слагаемое"),
    pbMsg("tooltip.sum", "Сложение нескольких чисел. ПКМ — добавить или убрать слагаемое.")
  );
  defineNaryBlock(
    "py_product",
    "×",
    pbMsg("menu.product.add", "добавить множитель"),
    pbMsg("menu.product.remove", "убрать множитель"),
    pbMsg("tooltip.product", "Умножение нескольких чисел. ПКМ — добавить или убрать множитель.")
  );
}

function registerPyIfBlock() {
  if (Blockly.Blocks["py_if"] && Blockly.Blocks["py_if"].init) return;

  Blockly.Blocks["py_if"] = {
    init: function () {
      this.setStyle("logic_blocks");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setTooltip(pbMsg("tooltip.if", "Условие: если / иначе если / иначе. ПКМ — добавить или убрать ветки."));
      this.elseIfCount_ = 0;
      this.elseCount_ = 0;
      this.appendValueInput("IF0").setCheck("Boolean").appendField(pbMsg("if.if", "если"));
      this.appendStatementInput("DO0");
    },
    updateShape_: function () {
      for (let i = 1; i <= this.elseIfCount_; i++) {
        if (!this.getInput("IF" + i)) {
          this.appendValueInput("IF" + i).setCheck("Boolean").appendField(pbMsg("if.elif", "иначе если"));
          this.appendStatementInput("DO" + i);
        }
      }
      let i = this.elseIfCount_ + 1;
      while (this.getInput("IF" + i)) {
        this.removeInput("IF" + i);
        this.removeInput("DO" + i);
        i++;
      }
      if (this.elseCount_ && !this.getInput("ELSE")) {
        this.appendStatementInput("ELSE").appendField(pbMsg("if.else", "иначе"));
      } else if (!this.elseCount_ && this.getInput("ELSE")) {
        this.removeInput("ELSE");
      }
    },
    customContextMenu: function (menuOptions) {
      const block = this;
      menuOptions.push({
        text: pbMsg("menu.if.add_elif", "добавить иначе если"),
        enabled: block.elseIfCount_ < 5,
        callback: function () {
          block.elseIfCount_++;
          block.updateShape_();
        },
      });
      if (block.elseIfCount_ > 0) {
        menuOptions.push({
          text: pbMsg("menu.if.remove_elif", "убрать иначе если"),
          callback: function () {
            block.elseIfCount_--;
            block.updateShape_();
          },
        });
      }
      if (!block.elseCount_) {
        menuOptions.push({
          text: pbMsg("menu.if.add_else", "добавить иначе"),
          callback: function () {
            block.elseCount_ = 1;
            block.updateShape_();
          },
        });
      } else {
        menuOptions.push({
          text: pbMsg("menu.if.remove_else", "убрать иначе"),
          callback: function () {
            block.elseCount_ = 0;
            block.updateShape_();
          },
        });
      }
    },
    mutationToDom: function () {
      const container =
        Blockly.utils && Blockly.utils.xml
          ? Blockly.utils.xml.createElement("mutation")
          : document.createElement("mutation");
      container.setAttribute("elseif", this.elseIfCount_);
      container.setAttribute("else", this.elseCount_);
      return container;
    },
    domToMutation: function (xmlElement) {
      this.elseIfCount_ = parseInt(xmlElement.getAttribute("elseif"), 10) || 0;
      this.elseCount_ = parseInt(xmlElement.getAttribute("else"), 10) || 0;
      this.updateShape_();
    },
    saveExtraState: function () {
      return {
        elseIfCount: this.elseIfCount_,
        hasElse: !!this.elseCount_,
      };
    },
    loadExtraState: function (state) {
      this.elseIfCount_ = state.elseIfCount || 0;
      this.elseCount_ = state.hasElse ? 1 : 0;
      this.updateShape_();
    },
  };
}

function registerListsCreateWithBlock() {
  const original = Blockly.Blocks["lists_create_with"];
  if (!original || !original.init || original._pyblocksExtended) return;

  const originalInit = original.init;
  const MAX_LIST_ITEMS = 20;

  Blockly.Blocks["lists_create_with"] = Object.assign({}, original, {
    _pyblocksExtended: true,
    init: function () {
      originalInit.call(this);
      this.setTooltip(pbMsg("tooltip.lists_create", "Создать список с элементами. ПКМ — добавить или убрать элемент."));
    },
    customContextMenu: function (menuOptions) {
      const block = this;
      menuOptions.push({
        text: pbMsg("menu.list.add_item", "добавить элемент"),
        enabled: block.itemCount_ < MAX_LIST_ITEMS,
        callback: function () {
          block.itemCount_++;
          block.updateShape_();
        },
      });
      if (block.itemCount_ > 1) {
        menuOptions.push({
          text: pbMsg("menu.list.remove_item", "убрать элемент"),
          callback: function () {
            block.itemCount_--;
            block.updateShape_();
          },
        });
      }
    },
  });
}

function registerCustomBlocks() {
  if (typeof registerPyMethodBlocks === "function") {
    registerPyMethodBlocks();
  }

  const skipTypes = [
    "py_str_method",
    "py_list_method",
    "py_list_expr",
    "py_start",
    "py_end",
    "py_sum",
    "py_product",
    "py_add",
    "py_sub",
    "py_mul",
    "py_div",
    "py_floordiv",
    "py_pow",
    "py_mod",
  ];
  const toRegister = getPyblocksCustomBlocks().filter(function (json) {
    return skipTypes.indexOf(json.type) < 0 && !isBlockTypeRegistered(json.type);
  });

  if (toRegister.length) {
    if (Blockly.common && Blockly.common.defineBlocks) {
      Blockly.common.defineBlocks(Blockly.common.createBlockDefinitionsFromJsonArray(toRegister));
    } else {
      toRegister.forEach(function (json) {
        Blockly.Blocks[json.type] = {
          init: function () {
            this.jsonInit(json);
          },
        };
      });
    }
  }

  registerMethodBlockHelpers();
  registerMathBinaryBlocks();
  registerMathNaryBlocks();
  registerPyIfBlock();
  registerListsCreateWithBlock();
  registerProgramFrameBlocks();
}

registerCustomBlocks();
