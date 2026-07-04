/**
 * English block labels (on top of Blockly en.js).
 */
(function applyPyBlocksLocaleEn() {
  if (typeof Blockly === "undefined") return;

  Object.assign(Blockly.Msg, {
    TEXT_PRINT_TITLE: "print %1",
    VARIABLES_SET: "set %1 = %2",
    VARIABLES_DEFAULT_NAME: "item",
    VARIABLES_GET_TOOLTIP: "Value of the variable.",
    VARIABLES_SET_TOOLTIP: "Set the variable to a new value.",

    CONTROLS_IF_MSG_IF: "if",
    CONTROLS_IF_MSG_ELSEIF: "else if",
    CONTROLS_IF_MSG_ELSE: "else",
    CONTROLS_REPEAT_INPUT_DO: "do",
    CONTROLS_REPEAT_TITLE: "repeat %1 times",
    CONTROLS_FOREACH_TITLE: "for each %1 in list %2",

    CONTROLS_FLOW_STATEMENTS_OPERATOR_BREAK: "break",
    CONTROLS_FLOW_STATEMENTS_OPERATOR_CONTINUE: "continue",

    LOGIC_BOOLEAN_TRUE: "true",
    LOGIC_BOOLEAN_FALSE: "false",
    LOGIC_NULL: "null",
    LOGIC_NEGATE_TITLE: "not %1",
    LOGIC_OPERATION_AND: "and",
    LOGIC_OPERATION_OR: "or",

    MATH_ARITHMETIC_TOOLTIP_ADD: "Add two numbers.",
    MATH_ARITHMETIC_TOOLTIP_MINUS: "Subtract the second number from the first.",
    MATH_ARITHMETIC_TOOLTIP_MULTIPLY: "Multiply two numbers.",
    MATH_ARITHMETIC_TOOLTIP_DIVIDE: "Divide the first number by the second.",
    MATH_MODULO_TITLE: "remainder of %1 ÷ %2",
    MATH_CONSTRAIN_TITLE: "constrain %1 between %2 and %3",
    MATH_RANDOM_INT_TITLE: "random integer from %1 to %2",
    MATH_SINGLE_OP_ROOT: "square root",
    MATH_SINGLE_OP_ABSOLUTE: "absolute",

    TEXT_JOIN_TITLE_CREATEWITH: "join text from",
    TEXT_LENGTH_TITLE: "length of %1",
    TEXT_CHARAT_TITLE: "in text %1 %2",
    TEXT_INDEXOF_TITLE: "in text %1 %2 %3",
    TEXT_ISEMPTY_TITLE: "%1 is empty",
    TEXT_TRIM_OPERATOR_BOTH: "trim spaces",
    TEXT_TRIM_OPERATOR_LEFT: "trim left",
    TEXT_TRIM_OPERATOR_RIGHT: "trim right",
    TEXT_CHANGECASE_OPERATOR_UPPERCASE: "to UPPER CASE",
    TEXT_CHANGECASE_OPERATOR_LOWERCASE: "to lower case",
    TEXT_CHANGECASE_OPERATOR_TITLECASE: "to Title Case",

    LISTS_CREATE_EMPTY_TITLE: "create empty list",
    LISTS_CREATE_WITH_INPUT_WITH: "create list with",
    LISTS_CREATE_WITH_CONTAINER_TITLE_ADD: "list",
    LISTS_CREATE_WITH_TOOLTIP: "Create a list with items. Right-click — add or remove an item.",
    LISTS_LENGTH_TITLE: "length of %1",
    LISTS_ISEMPTY_TITLE: "list %1 is empty",
    LISTS_INDEX_OF_TITLE: "in list %1 %2 %3",
    LISTS_INDEX_OF_OPERATOR_FIRST: "find first",
    LISTS_INDEX_OF_OPERATOR_LAST: "find last",
    LISTS_GET_INDEX_GET: "get",
    LISTS_GET_INDEX_REMOVE: "remove",
    LISTS_GET_INDEX_GET_REMOVE: "get and remove",
    LISTS_SET_INDEX_INSERT: "insert at",
    LISTS_SET_INDEX_SET: "set",
    LISTS_SORT_TITLE: "sort %1 %2 %3",
    LISTS_SPLIT_LIST_FROM_TEXT: "list from text",
    LISTS_SPLIT_TEXT_FROM_LIST: "text from list",
    LISTS_REPEAT_TITLE: "create list with %1 repeated %2 times",

    PROCEDURES_DEFNORETURN_TITLE: "function",
    PROCEDURES_DEFNORETURN_PROCEDURE: "my_function",
    PROCEDURES_DEFNORETURN_COMMENT: "Describe this function…",
    PROCEDURES_DEFRETURN_RETURN: "return",

    INPUT_LABEL_VARIABLES_SET: "value",
    INPUT_LABEL_LISTS_CREATE_WITH_ITEM: "item %1",
    INPUT_LABEL_TEXT_JOIN_ITEM: "part %1",
    INPUT_LABEL_MATH_CONSTRAIN_VALUE: "number",
    INPUT_LABEL_MATH_DIVIDEND: "dividend",
    INPUT_LABEL_MATH_DIVISOR: "divisor",
    INPUT_LABEL_MATH_CHANGE_BY: "by",
  });
})();
