"""Тесты проверки решений."""

from runner.checker import check_solution, extract_input_prompts, strip_input_prompts


def test_extract_input_prompts_default_block():
    code = "x = input('Введите:')\nprint(x)"
    assert extract_input_prompts(code) == ["Введите:"]


def test_strip_input_prompts_removes_from_stdout():
    code = "print(input('Введите:'))"
    output = "Введите:кот\n"
    assert strip_input_prompts(code, output) == "кот\n"


def test_check_solution_ignores_default_input_prompt():
    code = "x = input('Введите:')\nprint(x)"
    tests = [{"stdin": "кот\n", "expected_output": "кот"}]
    result = check_solution(code, tests)
    assert result["success"] is True


def test_check_solution_multiple_inputs():
    code = "print(input('Введите:'))\nprint(input('Введите:'))"
    tests = [{"stdin": "Оля\nсиний\n", "expected_output": "Оля\nсиний"}]
    result = check_solution(code, tests)
    assert result["success"] is True
