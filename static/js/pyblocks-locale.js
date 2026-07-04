/**
 * Русские названия блоков в стиле псевдокода (поверх Blockly ru.js).
 */
(function applyPyBlocksLocale() {
  if (typeof Blockly === "undefined") return;

  Object.assign(Blockly.Msg, {
    TEXT_PRINT_TITLE: "вывести %1",
    VARIABLES_SET: "задать %1 = %2",
    VARIABLES_GET_TOOLTIP: "Значение переменной.",
    VARIABLES_SET_TOOLTIP: "Задать переменной новое значение.",

    CONTROLS_IF_MSG_IF: "если",
    CONTROLS_IF_MSG_ELSEIF: "иначе если",
    CONTROLS_IF_MSG_ELSE: "иначе",
    CONTROLS_REPEAT_INPUT_DO: "выполнить",
    CONTROLS_REPEAT_TITLE: "повторить %1 раз",
    CONTROLS_FOREACH_TITLE: "для каждого %1 из списка %2",

    CONTROLS_FLOW_STATEMENTS_OPERATOR_BREAK: "прервать цикл",
    CONTROLS_FLOW_STATEMENTS_OPERATOR_CONTINUE: "следующий шаг цикла",

    LOGIC_BOOLEAN_TRUE: "истина",
    LOGIC_BOOLEAN_FALSE: "ложь",
    LOGIC_NULL: "пусто",
    LOGIC_NEGATE_TITLE: "не %1",
    LOGIC_OPERATION_AND: "и",
    LOGIC_OPERATION_OR: "или",

    MATH_ARITHMETIC_TOOLTIP_ADD: "Сложить два числа.",
    MATH_ARITHMETIC_TOOLTIP_MINUS: "Вычесть второе число из первого.",
    MATH_ARITHMETIC_TOOLTIP_MULTIPLY: "Умножить два числа.",
    MATH_ARITHMETIC_TOOLTIP_DIVIDE: "Разделить первое число на второе.",
    MATH_MODULO_TITLE: "остаток %1 ÷ %2",
    MATH_CONSTRAIN_TITLE: "ограничить %1 от %2 до %3",
    MATH_RANDOM_INT_TITLE: "случайное число от %1 до %2",
    MATH_SINGLE_OP_ROOT: "корень",
    MATH_SINGLE_OP_ABSOLUTE: "модуль",

    TEXT_JOIN_TITLE_CREATEWITH: "соединить текст из",
    TEXT_LENGTH_TITLE: "длина %1",
    TEXT_CHARAT_TITLE: "в тексте %1 %2",
    TEXT_INDEXOF_TITLE: "в тексте %1 %2 %3",
    TEXT_ISEMPTY_TITLE: "%1 пустой",
    TEXT_TRIM_OPERATOR_BOTH: "обрезать пробелы",
    TEXT_TRIM_OPERATOR_LEFT: "обрезать слева",
    TEXT_TRIM_OPERATOR_RIGHT: "обрезать справа",
    TEXT_CHANGECASE_OPERATOR_UPPERCASE: "в верхний регистр",
    TEXT_CHANGECASE_OPERATOR_LOWERCASE: "в нижний регистр",
    TEXT_CHANGECASE_OPERATOR_TITLECASE: "каждое слово с заглавной",

    LISTS_CREATE_EMPTY_TITLE: "пустой список",
    LISTS_CREATE_WITH_INPUT_WITH: "список из",
    LISTS_CREATE_WITH_TOOLTIP:
      "Создать список с элементами. ПКМ — добавить или убрать элемент.",
    LISTS_LENGTH_TITLE: "длина списка %1",
    LISTS_ISEMPTY_TITLE: "список %1 пуст",
    LISTS_INDEX_OF_TITLE: "в списке %1 %2 %3",
    LISTS_INDEX_OF_OPERATOR_FIRST: "найти первое",
    LISTS_INDEX_OF_OPERATOR_LAST: "найти последнее",
    LISTS_GET_INDEX_GET: "взять",
    LISTS_GET_INDEX_REMOVE: "удалить",
    LISTS_GET_INDEX_GET_REMOVE: "взять и удалить",
    LISTS_SET_INDEX_INSERT: "вставить в",
    LISTS_SET_INDEX_SET: "задать",
    LISTS_SORT_TITLE: "отсортировать %1 %2 %3",
    LISTS_SPLIT_LIST_FROM_TEXT: "список из текста",
    LISTS_SPLIT_TEXT_FROM_LIST: "текст из списка",
    LISTS_REPEAT_TITLE: "список из %1 повторить %2 раз",

    PROCEDURES_DEFNORETURN_TITLE: "функция",
    PROCEDURES_DEFNORETURN_PROCEDURE: "моя_функция",
    PROCEDURES_DEFNORETURN_COMMENT: "описание функции…",
    PROCEDURES_DEFRETURN_RETURN: "вернуть",

    INPUT_LABEL_VARIABLES_SET: "значение",
    INPUT_LABEL_LISTS_CREATE_WITH_ITEM: "элемент %1",
    INPUT_LABEL_TEXT_JOIN_ITEM: "фрагмент %1",
    INPUT_LABEL_MATH_CONSTRAIN_VALUE: "число",
    INPUT_LABEL_MATH_DIVIDEND: "делимое",
    INPUT_LABEL_MATH_DIVISOR: "делитель",
    INPUT_LABEL_MATH_CHANGE_BY: "на сколько",
  });
})();
