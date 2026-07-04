"""Тесты разбора Python → блоки."""

from runner.python_to_blocks import python_to_blocks, python_to_blocks_safe


def test_print_chain():
    result = python_to_blocks("print('')\nprint('')")
    chain = result["program"]["chain"]
    assert len(chain) == 2
    assert chain[0]["type"] == "text_print"
    assert chain[1]["type"] == "text_print"
    assert "<block type=\"text_print\">" in result["xml"]
    assert result["xml"].count("text_print") == 2


def test_assign_and_print():
    code = "x = 5\nprint(x)"
    result = python_to_blocks(code)
    assert "x" in result["program"]["variables"]
    chain = result["program"]["chain"]
    assert chain[0]["type"] == "variables_set"
    assert chain[1]["type"] == "text_print"


def test_if_else():
    code = "if x > 0:\n    print('да')\nelse:\n    print('нет')"
    result = python_to_blocks(code)
    assert result["program"]["chain"][0]["type"] == "py_ifelse"


def test_for_loop():
    code = "for i in range(3):\n    print(i)"
    result = python_to_blocks(code)
    block = result["program"]["chain"][0]
    assert block["type"] == "py_for"
    assert block["fields"]["VAR"] == "i"


def test_if_body_has_single_program_end():
    code = "if 2 > 1:\n    print(1)"
    result = python_to_blocks(code)
    assert result["program"]["chain"][0]["type"] == "py_if"
    assert result["xml"].count('type="py_end"') == 1
    statement = result["xml"].split("<statement", 1)[1].split("</statement>", 1)[0]
    assert "py_end" not in statement


def test_for_body_has_single_program_end():
    code = "for i in range(3):\n    print(i)"
    result = python_to_blocks(code)
    assert result["xml"].count('type="py_end"') == 1


def test_unsupported_syntax():
    result = python_to_blocks_safe("def foo():\n    pass")
    assert result["success"] is False
    assert "не поддерживается" in result["error"]
