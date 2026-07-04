"""Blockly XML для примеров в теоретических материалах."""

XMLNS = 'xmlns="https://developers.google.com/blockly/xml"'


def xml(*parts: str) -> str:
    return f"<xml {XMLNS}>{''.join(parts)}</xml>"


def num(value: int | str) -> str:
    return f'<block type="math_number"><field name="NUM">{value}</field></block>'


def var_get(var_id: str, name: str) -> str:
    return f'<block type="variables_get"><field name="VAR" id="{var_id}">{name}</field></block>'


def bin_op(op_type: str, left: str, right: str) -> str:
    return (
        f'<block type="{op_type}">'
        f'<mutation items="2"></mutation>'
        f'<value name="ARG0">{left}</value>'
        f'<value name="ARG1">{right}</value>'
        f"</block>"
    )


PY_END = '<block type="py_end"></block>'


def attach_py_end(block_xml: str) -> str:
    """Добавляет «Конец программы» в конец цепочки statement-блоков."""
    stripped = block_xml.strip()
    if not stripped:
        return PY_END

    chain_tail = "</block></next></block>"
    chain_idx = stripped.rfind(chain_tail)
    if chain_idx >= 0:
        insert_at = chain_idx
    else:
        insert_at = stripped.rfind("</block>")
        if insert_at < 0:
            return block_xml

    return stripped[:insert_at] + f"<next>{PY_END}</next>" + stripped[insert_at:]


def program(*parts: str) -> str:
    """Оборачивает цепочку блоков в «Начало» и «Конец программы»."""
    variables = ""
    chunks: list[str] = []
    for part in parts:
        if part.strip().startswith("<variables"):
            variables = part
        else:
            chunks.append(part)
    body = attach_py_end("".join(chunks).strip())
    return xml(
        variables,
        '<block type="py_start" x="20" y="20">',
        "<next>",
        body,
        "</next>",
        "</block>",
    )


# --- Ввод и вывод ---
IO_HELLO = program(
    '<block type="text_print" x="20" y="20">',
    '<value name="TEXT"><block type="text"><field name="TEXT">Привет, мир!</field></block></value>',
    "</block>",
)

HELLO_WORLD = program(
    '<block type="text_print" x="20" y="20">',
    '<value name="TEXT"><block type="text"><field name="TEXT">Hello, world!</field></block></value>',
    "</block>",
)

IO_WELCOME = program(
    '<block type="text_print" x="20" y="20">',
    '<value name="TEXT"><block type="text"><field name="TEXT">Добро пожаловать!</field></block></value>',
    "</block>",
)

IO_VARIABLE = program(
    "<variables><variable id=\"v_name\">имя</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_name">имя</field>',
    '<value name="VALUE"><block type="text"><field name="TEXT">Аня</field></block></value>',
    "<next>",
    '<block type="text_print">',
    '<value name="TEXT"><block type="variables_get"><field name="VAR" id="v_name">имя</field></block></value>',
    "</block>",
    "</next>",
    "</block>",
)

IO_GREETING = program(
    "<variables><variable id=\"v_name\">имя</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_name">имя</field>',
    '<value name="VALUE"><block type="py_input"><field name="PROMPT">Как тебя зовут?</field></block></value>',
    "<next>",
    '<block type="text_print">',
    '<value name="TEXT">',
    '<block type="text_join">',
    '<mutation items="2"></mutation>',
    '<value name="ADD0"><block type="text"><field name="TEXT">Привет, </field></block></value>',
    '<value name="ADD1"><block type="variables_get"><field name="VAR" id="v_name">имя</field></block></value>',
    "</block>",
    "</value>",
    "</block>",
    "</next>",
    "</block>",
)

# Демо на главной странице: задать имя + вывести приветствие
LANDING_DEMO = program(
    "<variables><variable id=\"v_ld_name\">имя</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_ld_name">имя</field>',
    '<value name="VALUE"><block type="text"><field name="TEXT">Аня</field></block></value>',
    "<next>",
    '<block type="text_print">',
    '<value name="TEXT">',
    '<block type="text_join">',
    '<mutation items="2"></mutation>',
    '<value name="ADD0"><block type="text"><field name="TEXT">Привет, </field></block></value>',
    '<value name="ADD1"><block type="variables_get"><field name="VAR" id="v_ld_name">имя</field></block></value>',
    "</block>",
    "</value>",
    "</block>",
    "</next>",
    "</block>",
)

# Компактное превью для шага «Соединяйте блоки» на главной
STEP_CONNECT_DEMO = program(
    "<variables><variable id=\"v_sc_name\">имя</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_sc_name">имя</field>',
    '<value name="VALUE"><block type="text"><field name="TEXT">Аня</field></block></value>',
    "<next>",
    '<block type="text_print" x="20" y="20">',
    '<value name="TEXT"><block type="text"><field name="TEXT">Привет!</field></block></value>',
    "</block>",
    "</next>",
    "</block>",
)

# --- Числа ---
NUMS_ADD = program(
    '<block type="text_print" x="20" y="20">',
    f'<value name="TEXT">{bin_op("py_add", num(7), num(5))}</value>',
    "</block>",
)

NUMS_PERIMETER = program(
    "<variables><variable id=\"v_p\">периметр</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_p">периметр</field>',
    f'<value name="VALUE">{bin_op("py_mul", num(2), bin_op("py_add", num(7), num(3)))}</value>',
    "<next>",
    '<block type="text_print">',
    f'<value name="TEXT">{var_get("v_p", "периметр")}</value>',
    "</block>",
    "</next>",
    "</block>",
)

NUMS_INPUT_SUM = program(
    "<variables><variable id=\"v_a\">a</variable><variable id=\"v_b\">b</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_a">a</field>',
    '<value name="VALUE"><block type="py_convert">',
    '<value name="VALUE"><block type="py_input"><field name="PROMPT">Первое число</field></block></value>',
    '<field name="TO">INT</field>',
    "</block></value>",
    "<next>",
    '<block type="variables_set">',
    '<field name="VAR" id="v_b">b</field>',
    '<value name="VALUE"><block type="py_convert">',
    '<value name="VALUE"><block type="py_input"><field name="PROMPT">Второе число</field></block></value>',
    '<field name="TO">INT</field>',
    "</block></value>",
    "<next>",
    '<block type="text_print">',
    f'<value name="TEXT">{bin_op("py_add", var_get("v_a", "a"), var_get("v_b", "b"))}</value>',
    "</block>",
    "</next>",
    "</block>",
    "</block>",
)

# --- Условия и логика ---
COND_COMPARE_DEMO = program(
    '<block type="py_ifelse" x="20" y="20">',
    '<value name="IF0"><block type="logic_compare">',
    '<field name="OP">GTE</field>',
    f'<value name="A">{num(15)}</value>',
    f'<value name="B">{num(10)}</value>',
    "</block></value>",
    '<statement name="DO0"><block type="text_print">',
    '<value name="TEXT"><block type="text"><field name="TEXT">истина</field></block></value>',
    "</block></statement>",
    '<statement name="ELSE"><block type="text_print">',
    '<value name="TEXT"><block type="text"><field name="TEXT">ложь</field></block></value>',
    "</block></statement>",
    "</block>",
)

COND_LOGIC_AND = program(
    '<block type="py_ifelse" x="20" y="20">',
    '<value name="IF0"><block type="logic_operation">',
    '<field name="OP">AND</field>',
    '<value name="A"><block type="logic_compare">',
    '<field name="OP">GT</field>',
    f'<value name="A">{num(15)}</value>',
    f'<value name="B">{num(10)}</value>',
    "</block></value>",
    '<value name="B"><block type="logic_compare">',
    '<field name="OP">EQ</field>',
    f'<value name="A">{num(4)}</value>',
    f'<value name="B">{num(2)}</value>',
    "</block></value>",
    "</block></value>",
    '<statement name="DO0"><block type="text_print">',
    '<value name="TEXT"><block type="text"><field name="TEXT">да</field></block></value>',
    "</block></statement>",
    '<statement name="ELSE"><block type="text_print">',
    '<value name="TEXT"><block type="text"><field name="TEXT">нет</field></block></value>',
    "</block></statement>",
    "</block>",
)

COND_IF_ELSE_AGE = program(
    "<variables><variable id=\"v_age\">возраст</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_age">возраст</field>',
    '<value name="VALUE"><block type="math_number"><field name="NUM">15</field></block></value>',
    "<next>",
    '<block type="py_ifelse">',
    '<value name="IF0"><block type="logic_compare">',
    '<field name="OP">GTE</field>',
    '<value name="A"><block type="variables_get"><field name="VAR" id="v_age">возраст</field></block></value>',
    '<value name="B"><block type="math_number"><field name="NUM">18</field></block></value>',
    "</block></value>",
    '<statement name="DO0"><block type="text_print">',
    '<value name="TEXT"><block type="text"><field name="TEXT">можно</field></block></value>',
    "</block></statement>",
    '<statement name="ELSE"><block type="text_print">',
    '<value name="TEXT"><block type="text"><field name="TEXT">нельзя</field></block></value>',
    "</block></statement>",
    "</block>",
    "</next>",
    "</block>",
)

COND_EVEN = program(
    "<variables><variable id=\"v_n\">n</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_n">n</field>',
    '<value name="VALUE"><block type="math_number"><field name="NUM">8</field></block></value>',
    "<next>",
    '<block type="py_ifelse">',
    '<value name="IF0"><block type="logic_compare">',
    '<field name="OP">EQ</field>',
    f'<value name="A">{bin_op("py_mod", var_get("v_n", "n"), num(2))}</value>',
    f'<value name="B">{num(0)}</value>',
    "</block></value>",
    '<statement name="DO0"><block type="text_print">',
    '<value name="TEXT"><block type="text"><field name="TEXT">чётное</field></block></value>',
    "</block></statement>",
    '<statement name="ELSE"><block type="text_print">',
    '<value name="TEXT"><block type="text"><field name="TEXT">нечётное</field></block></value>',
    "</block></statement>",
    "</block>",
    "</next>",
    "</block>",
)

COND_WEATHER = program(
    "<variables><variable id=\"v_t\">тепло</variable><variable id=\"v_d\">дождь</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_t">тепло</field>',
    '<value name="VALUE"><block type="logic_boolean"><field name="BOOL">TRUE</field></block></value>',
    "<next>",
    '<block type="variables_set">',
    '<field name="VAR" id="v_d">дождь</field>',
    '<value name="VALUE"><block type="logic_boolean"><field name="BOOL">FALSE</field></block></value>',
    "<next>",
    '<block type="py_ifelse">',
    '<value name="IF0"><block type="logic_operation">',
    '<field name="OP">AND</field>',
    '<value name="A"><block type="variables_get"><field name="VAR" id="v_t">тепло</field></block></value>',
    '<value name="B"><block type="logic_negate">',
    '<value name="BOOL"><block type="variables_get"><field name="VAR" id="v_d">дождь</field></block></value>',
    "</block></value>",
    "</block></value>",
    '<statement name="DO0"><block type="text_print">',
    '<value name="TEXT"><block type="text"><field name="TEXT">идём гулять!</field></block></value>',
    "</block></statement>",
    '<statement name="ELSE"><block type="text_print">',
    '<value name="TEXT"><block type="text"><field name="TEXT">остаёмся дома</field></block></value>',
    "</block></statement>",
    "</block>",
    "</next>",
    "</block>",
    "</block>",
)

# --- Цикл while ---
WHILE_COUNTER = program(
    "<variables><variable id=\"v_i\">i</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_i">i</field>',
    '<value name="VALUE"><block type="math_number"><field name="NUM">1</field></block></value>',
    "<next>",
    '<block type="py_while">',
    '<value name="COND"><block type="logic_compare">',
    '<field name="OP">LTE</field>',
    '<value name="A"><block type="variables_get"><field name="VAR" id="v_i">i</field></block></value>',
    '<value name="B"><block type="math_number"><field name="NUM">3</field></block></value>',
    "</block></value>",
    '<statement name="DO">',
    '<block type="text_print">',
    '<value name="TEXT"><block type="variables_get"><field name="VAR" id="v_i">i</field></block></value>',
    "<next>",
    '<block type="variables_set">',
    '<field name="VAR" id="v_i">i</field>',
    f'<value name="VALUE">{bin_op("py_add", var_get("v_i", "i"), num(1))}</value>',
    "</block>",
    "</next>",
    "</block>",
    "</statement>",
    "</block>",
    "</next>",
    "</block>",
)

WHILE_SUM = program(
    "<variables><variable id=\"v_i\">i</variable><variable id=\"v_s\">сумма</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_s">сумма</field>',
    '<value name="VALUE"><block type="math_number"><field name="NUM">0</field></block></value>',
    "<next>",
    '<block type="variables_set">',
    '<field name="VAR" id="v_i">i</field>',
    '<value name="VALUE"><block type="math_number"><field name="NUM">1</field></block></value>',
    "<next>",
    '<block type="py_while">',
    '<value name="COND"><block type="logic_compare">',
    '<field name="OP">LTE</field>',
    '<value name="A"><block type="variables_get"><field name="VAR" id="v_i">i</field></block></value>',
    '<value name="B"><block type="math_number"><field name="NUM">5</field></block></value>',
    "</block></value>",
    '<statement name="DO">',
    '<block type="variables_set">',
    '<field name="VAR" id="v_s">сумма</field>',
    f'<value name="VALUE">{bin_op("py_add", var_get("v_s", "сумма"), var_get("v_i", "i"))}</value>',
    "<next>",
    '<block type="variables_set">',
    '<field name="VAR" id="v_i">i</field>',
    f'<value name="VALUE">{bin_op("py_add", var_get("v_i", "i"), num(1))}</value>',
    "</block>",
    "</next>",
    "</block>",
    "</statement>",
    "</block>",
    "<next>",
    '<block type="text_print">',
    '<value name="TEXT"><block type="variables_get"><field name="VAR" id="v_s">сумма</field></block></value>',
    "</block>",
    "</next>",
    "</block>",
    "</block>",
)

# --- Цикл for ---
FOR_RANGE = program(
    '<block type="py_for" x="20" y="20">',
    '<field name="VAR" id="v_i">i</field>',
    '<value name="SEQ"><block type="py_range">',
    '<value name="FROM"><block type="math_number"><field name="NUM">1</field></block></value>',
    '<value name="TO"><block type="math_number"><field name="NUM">5</field></block></value>',
    '<value name="BY"><block type="math_number"><field name="NUM">1</field></block></value>',
    "</block></value>",
    '<statement name="DO"><block type="text_print">',
    '<value name="TEXT"><block type="variables_get"><field name="VAR" id="v_i">i</field></block></value>',
    "</block></statement>",
    "</block>",
)

FOR_SUM = program(
    "<variables><variable id=\"v_i\">i</variable><variable id=\"v_s\">сумма</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_s">сумма</field>',
    '<value name="VALUE"><block type="math_number"><field name="NUM">0</field></block></value>',
    "<next>",
    '<block type="py_for">',
    '<field name="VAR" id="v_i">i</field>',
    '<value name="SEQ"><block type="py_range">',
    '<value name="FROM"><block type="math_number"><field name="NUM">1</field></block></value>',
    '<value name="TO"><block type="math_number"><field name="NUM">5</field></block></value>',
    '<value name="BY"><block type="math_number"><field name="NUM">1</field></block></value>',
    "</block></value>",
    '<statement name="DO"><block type="variables_set">',
    '<field name="VAR" id="v_s">сумма</field>',
    f'<value name="VALUE">{bin_op("py_add", var_get("v_s", "сумма"), var_get("v_i", "i"))}</value>',
    "</block></statement>",
    "</block>",
    "<next>",
    '<block type="text_print">',
    '<value name="TEXT"><block type="variables_get"><field name="VAR" id="v_s">сумма</field></block></value>',
    "</block>",
    "</next>",
    "</block>",
)

# --- Строки ---
STR_UPPER = program(
    "<variables><variable id=\"v_s\">слово</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_s">слово</field>',
    '<value name="VALUE"><block type="text"><field name="TEXT">python</field></block></value>',
    "<next>",
    '<block type="text_print">',
    '<value name="TEXT"><block type="py_str_upper">',
    '<value name="OBJ"><block type="variables_get"><field name="VAR" id="v_s">слово</field></block></value>',
    "</block></value>",
    "</block>",
    "</next>",
    "</block>",
)

STR_JOIN = program(
    '<block type="text_print" x="20" y="20">',
    '<value name="TEXT">',
    '<block type="text_join">',
    '<mutation items="2"></mutation>',
    '<value name="ADD0"><block type="text"><field name="TEXT">Привет</field></block></value>',
    '<value name="ADD1"><block type="text"><field name="TEXT">, мир!</field></block></value>',
    "</block>",
    "</value>",
    "</block>",
)

STR_INPUT_UPPER = program(
    "<variables><variable id=\"v_s\">s</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_s">s</field>',
    '<value name="VALUE"><block type="py_input"><field name="PROMPT">Введите слово</field></block></value>',
    "<next>",
    '<block type="text_print">',
    '<value name="TEXT"><block type="py_str_upper">',
    '<value name="OBJ"><block type="variables_get"><field name="VAR" id="v_s">s</field></block></value>',
    "</block></value>",
    "</block>",
    "</next>",
    "</block>",
)

# --- Списки ---
LIST_CREATE = program(
    "<variables><variable id=\"v_f\">фрукты</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_f">фрукты</field>',
    '<value name="VALUE"><block type="lists_create_with">',
    '<mutation items="3"></mutation>',
    '<value name="ADD0"><block type="text"><field name="TEXT">яблоко</field></block></value>',
    '<value name="ADD1"><block type="text"><field name="TEXT">банан</field></block></value>',
    '<value name="ADD2"><block type="text"><field name="TEXT">груша</field></block></value>',
    "</block></value>",
    "<next>",
    '<block type="text_print">',
    '<value name="TEXT"><block type="lists_getIndex">',
    '<mutation statement="false" at="true"></mutation>',
    '<field name="MODE">GET</field>',
    '<field name="WHERE">FROM_START</field>',
    '<value name="VALUE"><block type="variables_get"><field name="VAR" id="v_f">фрукты</field></block></value>',
    '<value name="AT"><block type="math_number"><field name="NUM">1</field></block></value>',
    "</block></value>",
    "</block>",
    "</next>",
    "</block>",
)

LIST_SUM = program(
    "<variables><variable id=\"v_n\">числа</variable><variable id=\"v_x\">x</variable><variable id=\"v_s\">сумма</variable></variables>",
    '<block type="variables_set" x="20" y="20">',
    '<field name="VAR" id="v_n">числа</field>',
    '<value name="VALUE"><block type="lists_create_with">',
    '<mutation items="3"></mutation>',
    '<value name="ADD0"><block type="math_number"><field name="NUM">10</field></block></value>',
    '<value name="ADD1"><block type="math_number"><field name="NUM">20</field></block></value>',
    '<value name="ADD2"><block type="math_number"><field name="NUM">30</field></block></value>',
    "</block></value>",
    "<next>",
    '<block type="variables_set">',
    '<field name="VAR" id="v_s">сумма</field>',
    '<value name="VALUE"><block type="math_number"><field name="NUM">0</field></block></value>',
    "<next>",
    '<block type="py_for">',
    '<field name="VAR" id="v_x">x</field>',
    '<value name="SEQ"><block type="variables_get"><field name="VAR" id="v_n">числа</field></block></value>',
    '<statement name="DO"><block type="variables_set">',
    '<field name="VAR" id="v_s">сумма</field>',
    f'<value name="VALUE">{bin_op("py_add", var_get("v_s", "сумма"), var_get("v_x", "x"))}</value>',
    "</block></statement>",
    "</block>",
    "<next>",
    '<block type="text_print">',
    '<value name="TEXT"><block type="variables_get"><field name="VAR" id="v_s">сумма</field></block></value>',
    "</block>",
    "</next>",
    "</block>",
    "</block>",
)
