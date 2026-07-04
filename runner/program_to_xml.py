"""Сборка Blockly XML из JSON-программы (для импорта Python → блоки)."""

from __future__ import annotations

import html
import re
from typing import Any

XMLNS = 'xmlns="https://developers.google.com/blockly/xml"'


def _esc(text: str) -> str:
    return html.escape(str(text), quote=True)


def _var_id(name: str) -> str:
    safe = re.sub(r"[^\w\u0400-\u04FF]+", "_", name.strip(), flags=re.UNICODE)
    safe = safe.strip("_") or "var"
    return f"v_{safe}"


def _render_block(
    spec: dict[str, Any],
    indent: str,
    next_chain: list[dict[str, Any]] | None,
    *,
    with_end: bool = False,
) -> str:
    block_type = spec.get("type", "")
    lines = [f'{indent}<block type="{_esc(block_type)}">']

    mutation = spec.get("mutation")
    if mutation:
        attrs = " ".join(f'{key}="{_esc(value)}"' for key, value in mutation.items())
        lines.append(f"{indent}  <mutation {attrs}></mutation>")

    fields = spec.get("fields") or {}
    for name, value in fields.items():
        if name == "VAR":
            var_name = str(value)
            lines.append(
                f'{indent}  <field name="VAR" id="{_esc(_var_id(var_name))}">{_esc(var_name)}</field>'
            )
        else:
            lines.append(f'{indent}  <field name="{_esc(name)}">{_esc(value)}</field>')

    inputs = spec.get("inputs") or {}
    for input_name, child in inputs.items():
        lines.append(f'{indent}  <value name="{_esc(input_name)}">')
        lines.append(_render_value_block(child, indent + "    "))
        lines.append(f"{indent}  </value>")

    statements = spec.get("statements") or {}
    for input_name, chain in statements.items():
        if not chain:
            continue
        lines.append(f'{indent}  <statement name="{_esc(input_name)}">')
        lines.append(_render_statement_chain(chain, indent + "    "))
        lines.append(f"{indent}  </statement>")

    if next_chain is not None:
        lines.append(f"{indent}  <next>")
        if next_chain:
            lines.append(_render_statement_chain(next_chain, indent + "    ", with_end=with_end))
        elif with_end:
            lines.append(f'{indent}    <block type="py_end"></block>')
        lines.append(f"{indent}  </next>")

    lines.append(f"{indent}</block>")
    return "\n".join(lines)


def _render_value_block(spec: dict[str, Any], indent: str) -> str:
    block_type = spec.get("type", "")
    lines = [f'{indent}<block type="{_esc(block_type)}">']

    mutation = spec.get("mutation")
    if mutation:
        attrs = " ".join(f'{key}="{_esc(value)}"' for key, value in mutation.items())
        lines.append(f"{indent}  <mutation {attrs}></mutation>")

    fields = spec.get("fields") or {}
    for name, value in fields.items():
        if name == "VAR":
            var_name = str(value)
            lines.append(
                f'{indent}  <field name="VAR" id="{_esc(_var_id(var_name))}">{_esc(var_name)}</field>'
            )
        else:
            lines.append(f'{indent}  <field name="{_esc(name)}">{_esc(value)}</field>')

    inputs = spec.get("inputs") or {}
    for input_name, child in inputs.items():
        lines.append(f'{indent}  <value name="{_esc(input_name)}">')
        lines.append(_render_value_block(child, indent + "    "))
        lines.append(f"{indent}  </value>")

    lines.append(f"{indent}</block>")
    return "\n".join(lines)


def _render_statement_chain(
    chain: list[dict[str, Any]], indent: str, *, with_end: bool = False
) -> str:
    if not chain:
        return f'{indent}<block type="py_end"></block>' if with_end else ""

    first, *rest = chain
    if rest:
        next_chain: list[dict[str, Any]] | None = rest
    elif with_end:
        next_chain = []
    else:
        next_chain = None

    return _render_block(first, indent, next_chain, with_end=with_end)


def program_to_xml(program: dict[str, Any], *, x: int = 48, y: int = 48) -> str:
    variables = program.get("variables") or []
    chain = program.get("chain") or []

    var_lines: list[str] = []
    if variables:
        var_lines.append("  <variables>")
        for name in variables:
            var_lines.append(f'    <variable id="{_esc(_var_id(name))}">{_esc(name)}</variable>')
        var_lines.append("  </variables>")

    body = (
        _render_statement_chain(chain, "      ", with_end=True)
        if chain
        else '      <block type="py_end"></block>'
    )
    start_block = (
        f'  <block type="py_start" x="{x}" y="{y}">\n'
        f"    <next>\n"
        f"{body}\n"
        f"    </next>\n"
        f"  </block>"
    )

    chunks = var_lines + [start_block]
    return f"<xml {XMLNS}>\n" + "\n".join(chunks) + "\n</xml>"
