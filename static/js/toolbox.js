/**
 * Панель блоков — структура близкая к Python.
 */
const SH = {
  n: (v) => ({ shadow: { type: "math_number", fields: { NUM: v } } }),
  t: (v) => ({ shadow: { type: "text", fields: { TEXT: v } } }),
  b: (v) => ({ shadow: { type: "logic_boolean", fields: { BOOL: v ? "TRUE" : "FALSE" } } }),
};

function toolboxCat(key, fallback, colour, contents) {
  const entry = {
    kind: "category",
    name: t("toolbox." + key, fallback),
    catKey: key,
    colour: colour,
  };
  if (contents === "VARIABLE") {
    entry.custom = "VARIABLE";
  } else if (contents === "PROCEDURE") {
    entry.custom = "PROCEDURE";
  } else {
    entry.contents = contents;
  }
  return entry;
}

const PYBLOCKS_TOOLBOX = {
  kind: "categoryToolbox",
  contents: [
    toolboxCat("basics", "Основы", "210", [
      { kind: "block", type: "text_print" },
      { kind: "block", type: "py_input" },
      { kind: "block", type: "py_comment" },
      { kind: "block", type: "py_pass" },
      { kind: "block", type: "py_import_math" },
      { kind: "block", type: "py_import_random" },
      { kind: "block", type: "variables_set" },
      { kind: "block", type: "variables_get" },
      { kind: "block", type: "text" },
      { kind: "block", type: "math_number" },
      { kind: "block", type: "py_none" },
    ]),
    toolboxCat("variables", "Переменные", "330", "VARIABLE"),
    toolboxCat("math", "Математика", "230", [
      { kind: "block", type: "py_paren" },
      { kind: "block", type: "py_add" },
      { kind: "block", type: "py_sub" },
      { kind: "block", type: "py_mul" },
      { kind: "block", type: "py_div" },
      { kind: "block", type: "py_floordiv" },
      { kind: "block", type: "py_pow" },
      { kind: "block", type: "py_mod" },
      { kind: "block", type: "math_single" },
      { kind: "block", type: "math_constrain" },
      { kind: "block", type: "math_random_int" },
      { kind: "block", type: "math_on_list" },
      { kind: "block", type: "py_range", inputs: { FROM: SH.n(0), TO: SH.n(10), BY: SH.n(1) } },
      { kind: "block", type: "py_len" },
    ]),
    toolboxCat("text", "Текст", "160", [{ kind: "block", type: "text" }, { kind: "block", type: "text_join" }, { kind: "block", type: "py_len" }].concat(
      PY_STR_TOOLBOX_BLOCKS.map(function (type) {
        return pyMethodToolboxEntry(type);
      })
    )),
    toolboxCat("logic", "Логика", "210", [
      { kind: "block", type: "logic_compare" },
      { kind: "block", type: "logic_operation" },
      { kind: "block", type: "logic_negate" },
      { kind: "block", type: "logic_boolean" },
      { kind: "block", type: "logic_null" },
      { kind: "block", type: "py_in" },
      { kind: "block", type: "py_type_check" },
    ]),
    toolboxCat("conditions", "Условия", "210", [
      { kind: "block", type: "py_if" },
      { kind: "block", type: "py_ifelse", inputs: { IF0: SH.b(true) } },
      {
        kind: "block",
        type: "py_if",
        extraState: { elseIfCount: 1, hasElse: true },
      },
    ]),
    toolboxCat("loops", "Циклы", "120", [
      { kind: "block", type: "py_for" },
      { kind: "block", type: "py_while", inputs: { COND: SH.b(true) } },
      { kind: "block", type: "py_break" },
      { kind: "block", type: "py_continue" },
    ]),
    toolboxCat("lists", "Списки", "260", [{ kind: "block", type: "lists_create_empty" }, { kind: "block", type: "lists_create_with" }, { kind: "block", type: "lists_repeat" }, { kind: "block", type: "py_len" }, { kind: "block", type: "py_in" }]
      .concat(
        PY_LIST_STMT_TOOLBOX_BLOCKS.map(function (type) {
          if (type === "py_list_insert") {
            return pyMethodToolboxEntry(type, { INDEX: SH.n(0), VALUE: SH.n(1) });
          }
          if (type === "py_list_append" || type === "py_list_remove") {
            return pyMethodToolboxEntry(type, { VALUE: SH.n(1) });
          }
          return pyMethodToolboxEntry(type);
        })
      )
      .concat(
        PY_LIST_EXPR_TOOLBOX_BLOCKS.map(function (type) {
          if (type === "py_list_pop") {
            return pyMethodToolboxEntry(type);
          }
          if (type === "py_list_count" || type === "py_list_index") {
            return pyMethodToolboxEntry(type, { VALUE: SH.n(1) });
          }
          return pyMethodToolboxEntry(type);
        })
      )),
    toolboxCat("functions", "Функции", "290", "PROCEDURE"),
    toolboxCat("types", "Типы", "20", [
      { kind: "block", type: "py_convert" },
      { kind: "block", type: "py_type_check" },
      { kind: "block", type: "py_len" },
    ]),
  ],
};
