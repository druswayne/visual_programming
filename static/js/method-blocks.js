/**

 * Стандартные методы строк и списков — отдельные блоки для каждого метода Python.

 */

function methodLabel(def) {

  const key = def.i18nKey || "method." + def.type.replace(/^py_(str|list)_/, "$1.").replace(/_/g, ".");

  return t(key, def.label);

}



function methodArgLabel(arg) {

  if (!arg.label && !arg.i18nKey) return "";

  return t(arg.i18nKey, arg.label || "");

}



const PY_STR_METHOD_DEFS = [

  { type: "py_str_upper", label: "верхний регистр", py: "upper()", bool: false },

  { type: "py_str_lower", label: "нижний регистр", py: "lower()", bool: false },

  { type: "py_str_strip", label: "обрезать пробелы", py: "strip()", bool: false },

  { type: "py_str_lstrip", label: "обрезать слева", py: "lstrip()", bool: false },

  { type: "py_str_rstrip", label: "обрезать справа", py: "rstrip()", bool: false },

  { type: "py_str_capitalize", label: "с заглавной буквы", py: "capitalize()", bool: false },

  { type: "py_str_title", label: "заголовок", py: "title()", bool: false },

  { type: "py_str_swapcase", label: "сменить регистр", py: "swapcase()", bool: false },

  { type: "py_str_isdigit", label: "только цифры?", py: "isdigit()", bool: true },

  { type: "py_str_isalpha", label: "только буквы?", py: "isalpha()", bool: true },

  { type: "py_str_isalnum", label: "буквы и цифры?", py: "isalnum()", bool: true },

  { type: "py_str_isspace", label: "только пробелы?", py: "isspace()", bool: true },

  { type: "py_str_islower", label: "в нижнем регистре?", py: "islower()", bool: true },

  { type: "py_str_isupper", label: "в верхнем регистре?", py: "isupper()", bool: true },

  {

    type: "py_str_split",

    label: "разделить",

    py: "split",

    args: [{ name: "SEP", check: "String", label: "по", i18nKey: "method.arg.by" }],

    optionalArg: "SEP",

  },

  {

    type: "py_str_find",

    label: "найти",

    py: "find",

    args: [{ name: "SUB", check: "String", label: "" }],

  },

  {

    type: "py_str_count",

    label: "сколько раз",

    py: "count",

    args: [{ name: "SUB", check: "String", label: "" }],

  },

  {

    type: "py_str_startswith",

    label: "начинается с",

    py: "startswith",

    args: [{ name: "PREFIX", check: "String", label: "" }],

    bool: true,

  },

  {

    type: "py_str_endswith",

    label: "заканчивается на",

    py: "endswith",

    args: [{ name: "SUFFIX", check: "String", label: "" }],

    bool: true,

  },

  {

    type: "py_str_replace",

    label: "заменить",

    py: "replace",

    args: [

      { name: "OLD", check: "String", label: "" },

      { name: "NEW", check: "String", label: "на", i18nKey: "method.arg.to" },

    ],

  },

  {

    type: "py_str_join",

    label: "соединить",

    py: "join",

    join: true,

    args: [{ name: "LIST", check: "Array", label: "" }],

  },

];



const PY_LIST_STMT_DEFS = [

  {

    type: "py_list_append",

    label: "добавить",

    py: "append",

    args: [{ name: "VALUE", label: "" }],

  },

  {

    type: "py_list_extend",

    label: "расширить",

    py: "extend",

    args: [{ name: "SEQ", label: "" }],

  },

  {

    type: "py_list_insert",

    label: "вставить",

    py: "insert",

    args: [

      { name: "INDEX", check: "Number", label: "на место", i18nKey: "method.arg.at" },

      { name: "VALUE", label: "" },

    ],

  },

  {

    type: "py_list_remove",

    label: "удалить",

    py: "remove",

    args: [{ name: "VALUE", label: "" }],

  },

  { type: "py_list_clear", label: "очистить", py: "clear()" },

  { type: "py_list_sort", label: "отсортировать", py: "sort()" },

  { type: "py_list_reverse", label: "развернуть", py: "reverse()" },

];



const PY_LIST_EXPR_DEFS = [

  {

    type: "py_list_pop",

    label: "извлечь",

    py: "pop",

    args: [{ name: "INDEX", check: "Number", label: "с позиции", i18nKey: "method.arg.from_index" }],

    optionalArg: "INDEX",

  },

  {

    type: "py_list_count",

    label: "сколько раз",

    py: "count",

    args: [{ name: "VALUE", label: "" }],

  },

  {

    type: "py_list_index",

    label: "номер элемента",

    py: "index",

    args: [{ name: "VALUE", label: "" }],

  },

  { type: "py_list_copy", label: "копия", py: "copy()" },

  { type: "py_list_sorted", label: "отсортированная копия", py: "sorted" },

  { type: "py_list_reversed", label: "развёрнутая копия", py: "reversed" },

];



function buildStrMethodJson(def) {

  const label = methodLabel(def);



  if (def.join) {

    return {

      type: def.type,

      message0: t("method.str.join_message", "разделитель %1 → соединить %2"),

      args0: [

        { type: "input_value", name: "OBJ", check: "String" },

        { type: "input_value", name: def.args[0].name, check: def.args[0].check },

      ],

      inputsInline: true,

      output: null,

      style: "text_blocks",

      tooltip: t("method.str.join_tooltip", "str.join() — соединить элементы списка"),

    };

  }



  const args0 = [{ type: "input_value", name: "OBJ", check: "String" }];

  let message = t("method.str.template", "строка %1 → {label}", { label: label });



  if (def.args && def.args.length) {

    def.args.forEach(function (arg, i) {

      const placeholder = "%" + (i + 2);

      const argLabel = methodArgLabel(arg);

      if (argLabel) {

        message += " " + argLabel + " " + placeholder;

      } else {

        message += " " + placeholder;

      }

      args0.push({

        type: "input_value",

        name: arg.name,

        check: arg.check || null,

      });

    });

  }



  return {

    type: def.type,

    message0: message,

    args0: args0,

    inputsInline: true,

    output: def.bool ? "Boolean" : null,

    style: "text_blocks",

    tooltip: t("method.str.tooltip", "Метод строки: {label}", { label: label }),

  };

}



function buildListStmtJson(def) {

  const label = methodLabel(def);

  const args0 = [{ type: "input_value", name: "OBJ", check: "Array" }];

  let message = t("method.list.template", "список %1 → {label}", { label: label });



  if (def.args && def.args.length) {

    def.args.forEach(function (arg, i) {

      const placeholder = "%" + (i + 2);

      const argLabel = methodArgLabel(arg);

      if (argLabel) {

        message += " " + argLabel + " " + placeholder;

      } else {

        message += " " + placeholder;

      }

      args0.push({

        type: "input_value",

        name: arg.name,

        check: arg.check || null,

      });

    });

  }



  return {

    type: def.type,

    message0: message,

    args0: args0,

    inputsInline: true,

    previousStatement: null,

    nextStatement: null,

    style: "list_blocks",

    tooltip: t("method.list.tooltip", "Метод списка: {label}", { label: label }),

  };

}



function buildListExprJson(def) {

  const label = methodLabel(def);

  const args0 = [{ type: "input_value", name: "OBJ", check: "Array" }];

  let message = t("method.list.template", "список %1 → {label}", { label: label });



  if (def.args && def.args.length) {

    def.args.forEach(function (arg, i) {

      const placeholder = "%" + (i + 2);

      const argLabel = methodArgLabel(arg);

      if (argLabel) {

        message += " " + argLabel + " " + placeholder;

      } else {

        message += " " + placeholder;

      }

      args0.push({

        type: "input_value",

        name: arg.name,

        check: arg.check || null,

      });

    });

  }



  return {

    type: def.type,

    message0: message,

    args0: args0,

    inputsInline: true,

    output: null,

    style: "list_blocks",

    tooltip: t("method.list.tooltip", "Метод списка: {label}", { label: label }),

  };

}



function getPyMethodBlockJsonArray() {

  const blocks = [];

  PY_STR_METHOD_DEFS.forEach(function (def) {

    blocks.push(buildStrMethodJson(def));

  });

  PY_LIST_STMT_DEFS.forEach(function (def) {

    blocks.push(buildListStmtJson(def));

  });

  PY_LIST_EXPR_DEFS.forEach(function (def) {

    blocks.push(buildListExprJson(def));

  });

  return blocks;

}



function hasOptionalArg(block, inputName) {

  const target = block.getInputTargetBlock(inputName);

  if (!target) return true;

  if (typeof target.isShadow === "function" && target.isShadow()) return true;

  return false;

}



function registerPyMethodBlocks() {

  if (typeof Blockly === "undefined") return;



  const jsonArray = getPyMethodBlockJsonArray();

  const toRegister = jsonArray.filter(function (json) {

    if (Blockly.Blocks[json.type] && Blockly.Blocks[json.type].init) return false;

    if (Blockly.registry && typeof Blockly.registry.hasItem === "function") {

      return !Blockly.registry.hasItem(Blockly.registry.Type.BLOCK, json.type);

    }

    return !Blockly.Blocks[json.type];

  });



  if (!toRegister.length) return;



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



const PY_STR_TOOLBOX_BLOCKS = [

  "py_str_upper",

  "py_str_lower",

  "py_str_strip",

  "py_str_lstrip",

  "py_str_rstrip",

  "py_str_capitalize",

  "py_str_title",

  "py_str_swapcase",

  "py_str_split",

  "py_str_replace",

  "py_str_find",

  "py_str_count",

  "py_str_startswith",

  "py_str_endswith",

  "py_str_join",

  "py_str_isdigit",

  "py_str_isalpha",

  "py_str_isalnum",

  "py_str_isspace",

  "py_str_islower",

  "py_str_isupper",

];



const PY_LIST_STMT_TOOLBOX_BLOCKS = [

  "py_list_append",

  "py_list_extend",

  "py_list_insert",

  "py_list_remove",

  "py_list_clear",

  "py_list_sort",

  "py_list_reverse",

];



const PY_LIST_EXPR_TOOLBOX_BLOCKS = [

  "py_list_pop",

  "py_list_count",

  "py_list_index",

  "py_list_copy",

  "py_list_sorted",

  "py_list_reversed",

];



function pyMethodToolboxEntry(type, inputs) {

  const entry = { kind: "block", type: type };

  if (inputs) entry.inputs = inputs;

  return entry;

}


