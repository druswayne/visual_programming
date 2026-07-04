"""Build data/translations/en_tasks.py from translation data modules."""

from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from data.registry import TASKS_BY_TOPIC  # noqa: E402
from scripts.en_tasks_data_conditions import CONDITIONS, CONDITIONS_FIX  # noqa: E402
from scripts.en_tasks_data_io import IO, IO_FIX  # noqa: E402
from scripts.en_tasks_data_loops import FOR, FOR_FIX, WHILE, WHILE_FIX  # noqa: E402
from scripts.en_tasks_data_numbers import NUMBERS, NUMBERS_FIX  # noqa: E402
from scripts.en_tasks_data_strings_lists import (  # noqa: E402
    LISTS,
    LISTS_FIX,
    STRINGS,
    STRINGS_FIX,
)

OUT = ROOT / "data" / "translations" / "en_tasks.py"


def _merge(*parts: dict[str, dict]) -> dict[str, dict]:
    merged: dict[str, dict] = {}
    for part in parts:
        for key, value in part.items():
            if key in merged:
                raise KeyError(f"duplicate task id: {key}")
            merged[key] = value
    return merged


def _format_value(value, indent: int) -> str:
    if isinstance(value, str):
        if "\n" in value or len(value) > 72:
            return repr(value)
        return repr(value)
    if isinstance(value, list):
        if not value:
            return "[]"
        lines = ["["]
        for item in value:
            lines.append(f"{' ' * (indent + 4)}{_format_entry(item, indent + 4)},")
        lines.append(f"{' ' * indent}]")
        return "\n".join(lines)
    if isinstance(value, dict):
        return _format_entry(value, indent)
    return repr(value)


def _format_entry(entry: dict, indent: int) -> str:
    lines = ["{"]
    for key in ("title", "condition", "hint", "tests"):
        if key not in entry:
            continue
        val = entry[key]
        if isinstance(val, str) and "\n" not in val and len(val) <= 72:
            lines.append(f"{' ' * (indent + 4)}{key!r}: {val!r},")
        elif key == "tests":
            lines.append(f"{' ' * (indent + 4)}tests: {_format_value(val, indent + 4)},")
        else:
            lines.append(f"{' ' * (indent + 4)}{key!r}: (")
            for part in val.split("\n") if isinstance(val, str) else [str(val)]:
                lines.append(f"{' ' * (indent + 8)}{part!r}")
            lines.append(f"{' ' * (indent + 4)}),")
    lines.append(f"{' ' * indent}}}")
    return "\n".join(lines)


def _render_tasks_en(tasks: dict[str, dict]) -> str:
    lines = [
        '"""English translations for PyBlocks tasks."""',
        "",
        "from __future__ import annotations",
        "",
        "TASKS_EN: dict[str, dict] = {",
    ]
    for task_id in sorted(tasks.keys(), key=_sort_key):
        entry = tasks[task_id]
        lines.append(f'    "{task_id}": {{')
        for key in ("title", "condition", "hint", "tests"):
            if key not in entry:
                continue
            val = entry[key]
            if key == "tests":
                import pprint

                formatted = pprint.pformat(val, width=100, sort_dicts=False)
                lines.append(f"        'tests': {formatted},")
            elif isinstance(val, str) and ("\n" in val or len(val) > 70):
                lines.append(f"        {key!r}: (")
                # wrap long strings as concatenated literals
                lines.append(f"            {val!r}")
                lines.append("        ),")
            else:
                lines.append(f"        {key!r}: {val!r},")
        lines.append("    },")
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def _sort_key(task_id: str) -> tuple:
    """Sort io-01 before io-fix-01, keep numeric order."""
    if "-fix-" in task_id:
        prefix, num = task_id.split("-fix-")
        return (prefix, 1, int(num))
    prefix, num = task_id.rsplit("-", 1)
    return (prefix, 0, int(num))


def main() -> None:
    tasks_en = _merge(
        IO,
        IO_FIX,
        NUMBERS,
        NUMBERS_FIX,
        CONDITIONS,
        CONDITIONS_FIX,
        WHILE,
        WHILE_FIX,
        FOR,
        FOR_FIX,
        STRINGS,
        STRINGS_FIX,
        LISTS,
        LISTS_FIX,
    )

    # Validate against registry
    expected: set[str] = set()
    for topic_tasks in TASKS_BY_TOPIC.values():
        for task in topic_tasks:
            expected.add(task["id"])

    missing = expected - set(tasks_en)
    extra = set(tasks_en) - expected
    if missing:
        raise SystemExit(f"Missing translations ({len(missing)}): {sorted(missing)[:10]}...")
    if extra:
        raise SystemExit(f"Extra translations ({len(extra)}): {sorted(extra)[:10]}...")

    # Validate structure
    for task_id, entry in tasks_en.items():
        for field in ("title", "condition", "tests"):
            if field not in entry:
                raise SystemExit(f"{task_id}: missing {field}")
        if not isinstance(entry["tests"], list) or not entry["tests"]:
            raise SystemExit(f"{task_id}: tests must be non-empty list")

    content = _render_tasks_en(tasks_en)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding="utf-8")

    # Syntax check
    ast.parse(content)

    print(f"Wrote {OUT}")
    print(f"Total tasks translated: {len(tasks_en)}")


if __name__ == "__main__":
    main()
