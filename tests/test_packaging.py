# SPDX-License-Identifier: GPL-3.0-or-later
"""Packaging checks. Run: python3 tests/test_packaging.py"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(*p):
    with open(os.path.join(ROOT, *p)) as f:
        return f.read()


reqs = read("requirements.txt").lower()
for mod in ("cairosvg", "pillow", "picosvg"):
    assert re.search(rf"^{mod}==\d", reqs, re.M), f"{mod} is not pinned in requirements.txt"

used = set()
for folder, _, names in os.walk(ROOT):
    top = os.path.relpath(folder, ROOT).split(os.sep)[0]
    if top in ("venv", "Papirus", ".git", ".publish", "Trindle-Circle", "dist", "scratch"):
        continue
    for name in names:
        if name.endswith(".py"):
            used |= set(re.findall(r"^\s*(?:import|from)\s+(\w+)", read(os.path.relpath(os.path.join(folder, name), ROOT)), re.M))
for imp, pkg in (("cairosvg", "cairosvg"), ("PIL", "pillow"), ("picosvg", "picosvg")):
    assert imp in used, f"nothing imports {imp}: drop {pkg} from requirements.txt"
    assert pkg in reqs, f"the code imports {imp} but {pkg} is not in requirements.txt"

assert "Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/" in read("tools", "apt", "build.sh")
assert "License: MIT" in read("tools", "apt", "build.sh")
assert re.search(r"Papirus.*GPL-3\.0", read("README.md")), "README needs a Papirus credit line"
assert not os.path.exists(os.path.join(ROOT, "tools-sheet.py")), "tools-sheet.py must not be at the root"
assert os.path.exists(os.path.join(ROOT, "tools", "sheet.py"))
assert re.fullmatch(r"\d+\.\d+\.\d+", read("VERSION").strip())
print("ok")
