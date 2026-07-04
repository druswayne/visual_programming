"""Разбор Python-кода в промежуточное представление для Blockly-блоков PyBlocks."""

from __future__ import annotations

import ast
from typing import Any

from i18n import _
from runner.program_to_xml import program_to_xml

BINOP_MAP = {
    ast.Add: "+",
    ast.Sub: "-",
    ast.Mult: "*",
    ast.Div: "/",
    ast.FloorDiv: "//",
    ast.Mod: "%",
    ast.Pow: "**",
}

COMPARE_MAP = {
    ast.Eq: "EQ",
    ast.NotEq: "NEQ",
    ast.Lt: "LT",
    ast.LtE: "LTE",
    ast.Gt: "GT",
    ast.GtE: "GTE",
}

BOOL_OP_MAP = {
    ast.And: "AND",
    ast.Or: "OR",
}

MATH_SINGLE_MAP = {
    "sqrt": "ROOT",
    "fabs": "ABS",
    "abs": "ABS",
    "log": "LN",
    "log10": "LOG10",
    "exp": "EXP",
    "sin": "SIN",
    "cos": "COS",
    "tan": "TAN",
}

STR_METHOD_BLOCKS = {
    "upper": "py_str_upper",
    "lower": "py_str_lower",
    "strip": "py_str_strip",
    "lstrip": "py_str_lstrip",
    "rstrip": "py_str_rstrip",
    "capitalize": "py_str_capitalize",
    "title": "py_str_title",
    "swapcase": "py_str_swapcase",
    "isdigit": "py_str_isdigit",
    "isalpha": "py_str_isalpha",
    "isalnum": "py_str_isalnum",
    "isspace": "py_str_isspace",
    "islower": "py_str_islower",
    "isupper": "py_str_isupper",
    "split": "py_str_split",
    "find": "py_str_find",
    "count": "py_str_count",
    "startswith": "py_str_startswith",
    "endswith": "py_str_endswith",
    "replace": "py_str_replace",
    "join": "py_str_join",
}

LIST_STMT_BLOCKS = {
    "append": "py_list_append",
    "extend": "py_list_extend",
    "insert": "py_list_insert",
    "remove": "py_list_remove",
    "clear": "py_list_clear",
    "sort": "py_list_sort",
    "reverse": "py_list_reverse",
}

LIST_EXPR_BLOCKS = {
    "pop": "py_list_pop",
    "count": "py_list_count",
    "index": "py_list_index",
    "copy": "py_list_copy",
}

TYPE_CHECK_MAP = {
    "int": "INT",
    "str": "STR",
    "list": "LIST",
    "float": "FLOAT",
    "bool": "BOOL",
}

CONVERT_MAP = {
    "str": "STR",
    "int": "INT",
    "float": "FLOAT",
    "list": "LIST",
}


class PythonToBlocksError(Exception):
    def __init__(self, message: str, line: int | None = None):
        super().__init__(message)
        self.line = line


class PythonToBlocksConverter:
    def __init__(self) -> None:
        self.variables: set[str] = set()

    def convert(self, code: str) -> dict[str, Any]:
        code = code.strip()
        if not code:
            raise PythonToBlocksError(_("runner.ptb.empty_code"))

        try:
            tree = ast.parse(code)
        except SyntaxError as exc:
            line = exc.lineno or 1
            raise PythonToBlocksError(_("runner.ptb.syntax_error", msg=exc.msg), line) from exc

        chain: list[dict[str, Any]] = []
        for node in tree.body:
            chain.extend(self._stmt(node))

        return {
            "variables": sorted(self.variables),
            "chain": chain,
        }

    def _err(self, key: str, node: ast.AST, **kwargs) -> PythonToBlocksError:
        line = getattr(node, "lineno", None)
        return PythonToBlocksError(_(key, **kwargs), line)

    def _stmt(self, node: ast.AST) -> list[dict[str, Any]]:
        if isinstance(node, ast.Expr):
            value = node.value
            if isinstance(value, ast.Call) and self._is_print_call(value):
                return [{"type": "text_print", "inputs": {"TEXT": self._expr(value.args[0] if value.args else self._empty_str())}}]
            if isinstance(value, ast.Call):
                inner = self._call_expr(value)
                if inner.get("statement"):
                    return [inner["block"]]
            raise self._err("runner.ptb.expr_to_block", node)

        if isinstance(node, ast.Assign):
            if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
                raise self._err("runner.ptb.simple_assign", node)
            name = node.targets[0].id
            self.variables.add(name)
            return [
                {
                    "type": "variables_set",
                    "fields": {"VAR": name},
                    "inputs": {"VALUE": self._expr(node.value)},
                }
            ]

        if isinstance(node, ast.If):
            return [self._if_block(node)]

        if isinstance(node, ast.For):
            if not isinstance(node.target, ast.Name):
                raise self._err("runner.ptb.for_single_var", node)
            self.variables.add(node.target.id)
            return [
                {
                    "type": "py_for",
                    "fields": {"VAR": node.target.id},
                    "inputs": {"SEQ": self._expr(node.iter)},
                    "statements": {"DO": self._stmt_list(node.body)},
                }
            ]

        if isinstance(node, ast.While):
            return [
                {
                    "type": "py_while",
                    "inputs": {"COND": self._expr(node.test)},
                    "statements": {"DO": self._stmt_list(node.body)},
                }
            ]

        if isinstance(node, ast.Break):
            return [{"type": "py_break"}]

        if isinstance(node, ast.Continue):
            return [{"type": "py_continue"}]

        if isinstance(node, ast.Pass):
            return [{"type": "py_pass"}]

        if isinstance(node, ast.Import):
            blocks = []
            for alias in node.names:
                if alias.name in ("math", "random"):
                    blocks.append({"type": f"py_import_{alias.name}"})
                else:
                    raise self._err("runner.ptb.import_not_supported", node, name=alias.name)
            return blocks

        if isinstance(node, ast.ImportFrom):
            raise self._err("runner.ptb.import_from", node)

        raise self._err("runner.ptb.stmt_not_supported", node, name=type(node).__name__)

    def _stmt_list(self, nodes: list[ast.AST]) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for node in nodes:
            result.extend(self._stmt(node))
        return result

    def _if_block(self, node: ast.If) -> dict[str, Any]:
        branches = [{"cond": self._expr(node.test), "body": self._stmt_list(node.body)}]
        current = node
        else_body: list[dict[str, Any]] = []

        while current.orelse and len(current.orelse) == 1 and isinstance(current.orelse[0], ast.If):
            current = current.orelse[0]
            branches.append({"cond": self._expr(current.test), "body": self._stmt_list(current.body)})

        if current.orelse:
            else_body = self._stmt_list(current.orelse)

        if len(branches) == 1 and else_body:
            return {
                "type": "py_ifelse",
                "inputs": {"IF0": branches[0]["cond"]},
                "statements": {"DO0": branches[0]["body"], "ELSE": else_body},
            }

        block: dict[str, Any] = {
            "type": "py_if",
            "mutation": {"elseif": max(0, len(branches) - 1), "else": 1 if else_body else 0},
            "inputs": {},
            "statements": {},
        }
        for index, branch in enumerate(branches):
            block["inputs"][f"IF{index}"] = branch["cond"]
            block["statements"][f"DO{index}"] = branch["body"]
        if else_body:
            block["statements"]["ELSE"] = else_body
        return block

    def _empty_str(self) -> dict[str, Any]:
        return {"type": "text", "fields": {"TEXT": ""}}

    def _is_print_call(self, node: ast.Call) -> bool:
        return isinstance(node.func, ast.Name) and node.func.id == "print"

    def _expr(self, node: ast.AST) -> dict[str, Any]:
        if isinstance(node, ast.Constant):
            if node.value is None:
                return {"type": "py_none"}
            if isinstance(node.value, bool):
                return {"type": "logic_boolean", "fields": {"BOOL": "TRUE" if node.value else "FALSE"}}
            if isinstance(node.value, (int, float)):
                return {"type": "math_number", "fields": {"NUM": node.value}}
            if isinstance(node.value, str):
                return {"type": "text", "fields": {"TEXT": node.value}}
            raise self._err("runner.ptb.literal_not_supported", node, name=type(node.value).__name__)

        if isinstance(node, ast.Name):
            if node.id == "None":
                return {"type": "py_none"}
            if node.id in ("True", "False"):
                return {"type": "logic_boolean", "fields": {"BOOL": "TRUE" if node.id == "True" else "FALSE"}}
            self.variables.add(node.id)
            return {"type": "variables_get", "fields": {"VAR": node.id}}

        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            return {"type": "logic_negate", "inputs": {"BOOL": self._expr(node.operand)}}

        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            inner = self._expr(node.operand)
            return {
                "type": "py_mul",
                "mutation": {"items": 2},
                "inputs": {
                    "ARG0": {"type": "math_number", "fields": {"NUM": -1}},
                    "ARG1": inner,
                },
            }

        if isinstance(node, ast.BinOp):
            return self._binop(node)

        if isinstance(node, ast.BoolOp):
            op = BOOL_OP_MAP.get(type(node.op))
            if not op or len(node.values) < 2:
                raise self._err("runner.ptb.bool_op", node)
            result = self._expr(node.values[0])
            for value in node.values[1:]:
                result = {
                    "type": "logic_operation",
                    "fields": {"OP": op},
                    "inputs": {"A": result, "B": self._expr(value)},
                }
            return result

        if isinstance(node, ast.Compare):
            if len(node.ops) != 1 or len(node.comparators) != 1:
                raise self._err("runner.ptb.multi_compare", node)
            if isinstance(node.ops[0], ast.In):
                return {
                    "type": "py_in",
                    "inputs": {
                        "NEEDLE": self._expr(node.left),
                        "HAYSTACK": self._expr(node.comparators[0]),
                    },
                }
            if isinstance(node.ops[0], ast.NotIn):
                return {
                    "type": "logic_negate",
                    "inputs": {
                        "BOOL": {
                            "type": "py_in",
                            "inputs": {
                                "NEEDLE": self._expr(node.left),
                                "HAYSTACK": self._expr(node.comparators[0]),
                            },
                        }
                    },
                }
            op = COMPARE_MAP.get(type(node.ops[0]))
            if not op:
                raise self._err("runner.ptb.compare_not_supported", node)
            return {
                "type": "logic_compare",
                "fields": {"OP": op},
                "inputs": {"A": self._expr(node.left), "B": self._expr(node.comparators[0])},
            }

        if isinstance(node, ast.Call):
            return self._call_expr(node)["block"]

        if isinstance(node, ast.List):
            if not node.elts:
                return {"type": "lists_create_empty"}
            return {
                "type": "lists_create_with",
                "mutation": {"items": len(node.elts)},
                "inputs": {f"ADD{i}": self._expr(elt) for i, elt in enumerate(node.elts)},
            }

        if isinstance(node, ast.JoinedStr):
            parts = []
            for value in node.values:
                if isinstance(value, ast.Constant) and isinstance(value.value, str):
                    parts.append(self._expr(value))
                elif isinstance(value, ast.FormattedValue):
                    parts.append(self._expr(value.value))
                else:
                    raise self._err("runner.ptb.fstring_simple", node)
            return self._text_join(parts)

        raise self._err("runner.ptb.expr_not_supported", node, name=type(node).__name__)

    def _binop(self, node: ast.BinOp) -> dict[str, Any]:
        op = BINOP_MAP.get(type(node.op))
        if not op:
            raise self._err("runner.ptb.operator_not_supported", node)

        flat = self._flatten_binop(node, type(node.op))
        block_type = {
            "+": "py_add",
            "-": "py_sub",
            "*": "py_mul",
            "/": "py_div",
            "//": "py_floordiv",
            "%": "py_mod",
            "**": "py_pow",
        }[op]

        if op in ("+", "*") and len(flat) > 2:
            nary_type = "py_sum" if op == "+" else "py_product"
            return {
                "type": nary_type,
                "mutation": {"items": len(flat)},
                "inputs": {f"ADD{i}": self._expr(value) for i, value in enumerate(flat)},
            }

        if len(flat) == 2:
            return {
                "type": block_type,
                "mutation": {"items": 2},
                "inputs": {"ARG0": self._expr(flat[0]), "ARG1": self._expr(flat[1])},
            }

        result = self._expr(flat[0])
        for value in flat[1:]:
            result = {
                "type": block_type,
                "mutation": {"items": 2},
                "inputs": {"ARG0": result, "ARG1": self._expr(value)},
            }
        return result

    def _flatten_binop(self, node: ast.BinOp, op_type: type) -> list[ast.AST]:
        values: list[ast.AST] = []
        current: ast.AST = node
        while isinstance(current, ast.BinOp) and type(current.op) is op_type:
            values.insert(0, current.right)
            current = current.left
        values.insert(0, current)
        return values

    def _text_join(self, parts: list[dict[str, Any]]) -> dict[str, Any]:
        if len(parts) == 1:
            return parts[0]
        return {
            "type": "text_join",
            "mutation": {"items": len(parts)},
            "inputs": {f"ADD{i}": part for i, part in enumerate(parts)},
        }

    def _call_expr(self, node: ast.Call) -> dict[str, Any]:
        if isinstance(node.func, ast.Name):
            name = node.func.id
            if name == "print":
                raise self._err("runner.ptb.print_as_stmt", node)
            if name == "len":
                if len(node.args) != 1:
                    raise self._err("runner.ptb.len_one_arg", node)
                return {"block": {"type": "py_len", "inputs": {"OBJ": self._expr(node.args[0])}}}
            if name == "input":
                prompt = ""
                if node.args:
                    arg = self._expr(node.args[0])
                    if arg.get("type") == "text":
                        prompt = arg.get("fields", {}).get("TEXT", "")
                return {"block": {"type": "py_input", "fields": {"PROMPT": prompt}}}
            if name == "range":
                return {"block": self._range_block(node)}
            if name in CONVERT_MAP:
                if len(node.args) != 1:
                    raise self._err("runner.ptb.func_one_arg", node, name=name)
                return {
                    "block": {
                        "type": "py_convert",
                        "fields": {"TO": CONVERT_MAP[name]},
                        "inputs": {"VALUE": self._expr(node.args[0])},
                    }
                }
            if name == "isinstance":
                if len(node.args) != 2:
                    raise self._err("runner.ptb.isinstance_two_args", node)
                py_type = self._type_name(node.args[1])
                type_key = TYPE_CHECK_MAP.get(py_type)
                if not type_key:
                    raise self._err("runner.ptb.type_check_not_supported", node, type=py_type)
                return {
                    "block": {
                        "type": "py_type_check",
                        "fields": {"TYPE": type_key},
                        "inputs": {"VALUE": self._expr(node.args[0])},
                    }
                }
            if name == "sorted":
                if len(node.args) != 1:
                    raise self._err("runner.ptb.sorted_one_arg", node)
                return {
                    "block": {
                        "type": "py_list_sorted",
                        "inputs": {"OBJ": self._expr(node.args[0])},
                    }
                }
            if name == "list" and len(node.args) == 1:
                inner = node.args[0]
                if isinstance(inner, ast.Call) and isinstance(inner.func, ast.Name) and inner.func.id == "reversed" and len(inner.args) == 1:
                    return {
                        "block": {
                            "type": "py_list_reversed",
                            "inputs": {"OBJ": self._expr(inner.args[0])},
                        }
                    }
                return {
                    "block": {
                        "type": "py_convert",
                        "fields": {"TO": "LIST"},
                        "inputs": {"VALUE": self._expr(node.args[0])},
                    }
                }

        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            if node.func.value.id == "math" and node.func.attr in MATH_SINGLE_MAP:
                if len(node.args) != 1:
                    raise self._err("runner.ptb.math_one_arg", node, name=node.func.attr)
                return {
                    "block": {
                        "type": "math_single",
                        "fields": {"OP": MATH_SINGLE_MAP[node.func.attr]},
                        "inputs": {"NUM": self._expr(node.args[0])},
                    }
                }
            if node.func.value.id == "random" and node.func.attr == "randint":
                if len(node.args) != 2:
                    raise self._err("runner.ptb.randint_two_args", node)
                return {
                    "block": {
                        "type": "math_random_int",
                        "inputs": {
                            "FROM": self._expr(node.args[0]),
                            "TO": self._expr(node.args[1]),
                        },
                    }
                }

        if isinstance(node.func, ast.Attribute):
            return self._method_call(node)

        raise self._err("runner.ptb.call_not_supported", node)

    def _method_call(self, node: ast.Call) -> dict[str, Any]:
        method = node.func.attr
        obj = self._expr(node.func.value)

        if method in STR_METHOD_BLOCKS:
            block_type = STR_METHOD_BLOCKS[method]
            spec: dict[str, Any] = {"type": block_type, "inputs": {"OBJ": obj}}
            if method == "join":
                if len(node.args) != 1:
                    raise self._err("runner.ptb.join_one_arg", node)
                spec["inputs"]["LIST"] = self._expr(node.args[0])
            elif method == "replace":
                if len(node.args) != 2:
                    raise self._err("runner.ptb.replace_two_args", node)
                spec["inputs"]["OLD"] = self._expr(node.args[0])
                spec["inputs"]["NEW"] = self._expr(node.args[1])
            elif method == "split":
                if node.args:
                    spec["inputs"]["SEP"] = self._expr(node.args[0])
            elif method in ("find", "count", "startswith", "endswith"):
                if len(node.args) != 1:
                    raise self._err("runner.ptb.method_one_arg", node, method=method)
                arg_name = {"find": "SUB", "count": "SUB", "startswith": "PREFIX", "endswith": "SUFFIX"}[method]
                spec["inputs"][arg_name] = self._expr(node.args[0])
            return {"block": spec, "statement": False}

        if method in LIST_STMT_BLOCKS:
            block_type = LIST_STMT_BLOCKS[method]
            spec = {"type": block_type, "inputs": {"OBJ": obj}}
            if method == "insert":
                if len(node.args) != 2:
                    raise self._err("runner.ptb.insert_two_args", node)
                spec["inputs"]["INDEX"] = self._expr(node.args[0])
                spec["inputs"]["VALUE"] = self._expr(node.args[1])
            elif method in ("append", "extend", "remove"):
                if len(node.args) != 1:
                    raise self._err("runner.ptb.method_one_arg", node, method=method)
                arg_name = "VALUE" if method in ("append", "remove") else "SEQ"
                spec["inputs"][arg_name] = self._expr(node.args[0])
            return {"block": spec, "statement": True}

        if method in LIST_EXPR_BLOCKS:
            block_type = LIST_EXPR_BLOCKS[method]
            spec = {"type": block_type, "inputs": {"OBJ": obj}}
            if method == "pop":
                if node.args:
                    spec["inputs"]["INDEX"] = self._expr(node.args[0])
            elif method in ("count", "index"):
                if len(node.args) != 1:
                    raise self._err("runner.ptb.method_one_arg", node, method=method)
                spec["inputs"]["VALUE"] = self._expr(node.args[0])
            return {"block": spec, "statement": False}

        raise self._err("runner.ptb.method_not_supported", node, method=method)

    def _range_block(self, node: ast.Call) -> dict[str, Any]:
        args = node.args
        if len(args) == 1:
            return {
                "type": "py_range",
                "inputs": {
                    "FROM": {"type": "math_number", "fields": {"NUM": 0}},
                    "TO": self._expr(args[0]),
                    "BY": {"type": "math_number", "fields": {"NUM": 1}},
                },
            }
        if len(args) == 2:
            return {
                "type": "py_range",
                "inputs": {
                    "FROM": self._expr(args[0]),
                    "TO": self._expr(args[1]),
                    "BY": {"type": "math_number", "fields": {"NUM": 1}},
                },
            }
        if len(args) == 3:
            return {
                "type": "py_range",
                "inputs": {
                    "FROM": self._expr(args[0]),
                    "TO": self._expr(args[1]),
                    "BY": self._expr(args[2]),
                },
            }
        raise self._err("runner.ptb.range_args", node)

    def _type_name(self, node: ast.AST) -> str:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        raise self._err("runner.ptb.isinstance_type_name", node)


def python_to_blocks(code: str) -> dict[str, Any]:
    converter = PythonToBlocksConverter()
    program = converter.convert(code)
    return {
        "success": True,
        "program": program,
        "xml": program_to_xml(program),
    }


def python_to_blocks_safe(code: str) -> dict[str, Any]:
    try:
        return python_to_blocks(code)
    except PythonToBlocksError as exc:
        payload: dict[str, Any] = {"success": False, "error": str(exc)}
        if exc.line:
            payload["line"] = exc.line
        return payload
