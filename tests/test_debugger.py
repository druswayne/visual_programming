"""Тесты пошаговой трассировки с памятью."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runner.debugger import debug_python_code


def test_debug_includes_stack_and_heap():
    code = (
        "# @block:a\n"
        "items = [1, 2, 3]\n"
        "# @block:b\n"
        "x = items[0]\n"
        "# @block:c\n"
        "print(x)\n"
    )
    result = debug_python_code(code)
    assert result["success"], result.get("error")
    steps = result["steps"]
    assert len(steps) >= 2

    last = steps[-1]
    assert "stack" in last
    assert "heap" in last
    assert isinstance(last["stack"], list)
    assert last["stack"]
    assert last["stack"][-1]["name"] == "программа"


def test_debug_tracks_variable_changes():
    code = (
        "# @block:a\n"
        "n = 1\n"
        "# @block:b\n"
        "n = 2\n"
        "# @block:c\n"
        "print(n)\n"
    )
    result = debug_python_code(code)
    assert result["success"], result.get("error")

    changed_steps = [s for s in result["steps"] if "n" in (s.get("changed") or [])]
    assert changed_steps, "ожидалось изменение переменной n"


def test_debug_heap_for_dict():
    code = (
        "# @block:a\n"
        "data = {'a': 1, 'b': 2}\n"
        "# @block:b\n"
        "print(len(data))\n"
    )
    result = debug_python_code(code)
    assert result["success"], result.get("error")

    with_heap = [s for s in result["steps"] if s.get("heap")]
    assert with_heap
    heap = with_heap[-1]["heap"]
    assert any(entry.get("kind") == "dict" for entry in heap.values())


def test_debug_function_stack():
    code = (
        "# @block:a\n"
        "def add(a, b):\n"
        "    return a + b\n"
        "# @block:b\n"
        "result = add(2, 3)\n"
        "# @block:c\n"
        "print(result)\n"
    )
    result = debug_python_code(code)
    assert result["success"], result.get("error")

    depths = [len(s.get("stack") or []) for s in result["steps"]]
    assert max(depths) >= 2, "ожидался вызов функции в стеке"
