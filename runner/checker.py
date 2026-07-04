"""Проверка решений задач PyBlocks по тестам."""

import re

from i18n import _

from runner.sandbox import run_python_code

_INPUT_PROMPT_RE = re.compile(
    r"input\s*\(\s*(['\"])((?:\\.|(?!\1)[^\\])*?)\1\s*\)"
)


def _unescape_python_string(text: str) -> str:
    return (
        text.replace("\\n", "\n")
        .replace("\\t", "\t")
        .replace("\\'", "'")
        .replace('\\"', '"')
        .replace("\\\\", "\\")
    )


def extract_input_prompts(code: str) -> list[str]:
    prompts = []
    for match in _INPUT_PROMPT_RE.finditer(code):
        prompts.append(_unescape_python_string(match.group(2)))
    return prompts


def strip_input_prompts(code: str, output: str) -> str:
    """Убирает подсказки input('...') из stdout — в тестах их быть не должно."""
    if not output:
        return output
    result = output
    for prompt in sorted(extract_input_prompts(code), key=len, reverse=True):
        if prompt:
            result = result.replace(prompt, "")
    return result


def normalize_output(text: str) -> str:
    if not text:
        return ""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def check_solution(code: str, tests: list) -> dict:
    """Запускает код на каждом тесте и сравнивает stdout с ожидаемым результатом."""
    if not tests:
        return {"success": False, "passed": 0, "total": 0, "message": _("check.no_tests")}

    details = []
    passed = 0

    for index, test in enumerate(tests):
        stdin_text = test.get("stdin", "")
        expected = normalize_output(test.get("expected_output", ""))
        result = run_python_code(code, stdin_text=stdin_text)

        if result.get("overloaded"):
            return {
                "success": False,
                "passed": passed,
                "total": len(tests),
                "message": result.get("error", _("api.server_busy")),
                "overloaded": True,
                "details": details,
            }

        item = {"index": index + 1, "passed": False}

        if not result["success"]:
            item["message"] = result.get("error") or _("check.exec_error")
            if test.get("stdin"):
                item["hint"] = _("check.input_hint")
            details.append(item)
            continue

        actual = normalize_output(strip_input_prompts(code, result.get("output", "")))
        if actual == expected:
            item["passed"] = True
            passed += 1
        else:
            item["message"] = _("check.wrong_result")
            if test.get("stdin"):
                item["hint"] = _("check.stdin_hint", stdin=test["stdin"].strip())
            item["expected"] = expected
            item["actual"] = actual
        details.append(item)

    total = len(tests)
    success = passed == total
    if success:
        message = _("check.success", passed=passed, total=total)
    elif passed == 0:
        message = _("check.fail_all")
    else:
        message = _("check.partial", passed=passed, total=total)

    return {
        "success": success,
        "passed": passed,
        "total": total,
        "message": message,
        "details": details,
    }
