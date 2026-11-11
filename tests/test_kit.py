# SPDX-License-Identifier: GPL-3.0-or-later
"""Checks that the glyph batches share glyphs/kit.py and hold no helper copies."""
import ast
import glob
import importlib
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

FILES = sorted(glob.glob(os.path.join(ROOT, "glyphs", "batch*.py")))
KIT = ast.parse(open(os.path.join(ROOT, "glyphs", "kit.py")).read())
KIT_NAMES = {n.name for n in KIT.body if isinstance(n, ast.FunctionDef)}
for n in KIT.body:
    if isinstance(n, ast.Assign):
        KIT_NAMES |= {t.id for t in n.targets if isinstance(t, ast.Name)}


def shape(fn):
    """Arguments and body without the name or docstring, so a renamed copy compares equal."""
    body = fn.body[1:] if isinstance(fn.body[0], ast.Expr) and isinstance(getattr(fn.body[0], "value", None), ast.Constant) else fn.body
    return ast.dump(fn.args), tuple(ast.dump(x) for x in body)


KIT_SHAPES = {shape(n): n.name for n in KIT.body if isinstance(n, ast.FunctionDef)}


def modules():
    return [importlib.import_module("glyphs." + os.path.basename(p)[:-3]) for p in FILES]


def test_no_helper_copies():
    assert FILES
    for path in FILES:
        tree = ast.parse(open(path).read())
        for n in tree.body:
            names = []
            if isinstance(n, ast.FunctionDef) and not n.decorator_list:
                names = [n.name]
            elif isinstance(n, ast.Assign):
                names = [t.id for t in n.targets if isinstance(t, ast.Name)]
            for name in names:
                assert name not in ("reg", "small"), f"{path} defines {name}"
                assert name not in KIT_NAMES, f"{path} redefines kit helper {name}"
            if isinstance(n, ast.FunctionDef) and not n.decorator_list:
                assert shape(n) not in KIT_SHAPES, f"{path} copies kit helper {KIT_SHAPES[shape(n)]} as {n.name}"


def test_icon_names_unique():
    seen = {}
    for mod in modules():
        for name in mod.ICONS:
            assert name not in seen, f"{name} is in {seen[name]} and {mod.__name__}"
            seen[name] = mod.__name__
    assert seen


if __name__ == "__main__":
    for fn in (test_no_helper_copies, test_icon_names_unique):
        fn()
        print("ok", fn.__name__)
