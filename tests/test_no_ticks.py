# SPDX-License-Identifier: MIT
"""Fails if any built icon, or any symbolic drawing, contains a tick (check mark).

The rule: an open, straight-line path or polyline of exactly three points where
the first stroke runs down and to the right, the second runs up and to the right,
both lean 25 to 60 degrees from horizontal, and the second is 1.25 to 3.5 times
as long as the first. Built symbolic files are outlined, so the symbolic drawings
are checked from their source instead.
"""
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

TOK = re.compile(r"([MmLlHhVvZzCcSsQqTtAa])|(-?\d*\.?\d+(?:e-?\d+)?)")
NARGS = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7}

def subpaths(d):
    """Yield (points, closed, straight) for every subpath of a path string."""
    toks = [(m.group(1), m.group(2)) for m in TOK.finditer(d)]
    i, cmd, x, y, sx, sy = 0, None, 0.0, 0.0, 0.0, 0.0
    pts, closed, straight = [], False, True
    out = []

    def flush():
        if pts:
            out.append((pts[:], closed, straight))

    while i < len(toks):
        c, v = toks[i]
        if c:
            cmd = c
            i += 1
            if c in "Zz":
                closed = True
                x, y = sx, sy
                flush()
                pts.clear()
                closed, straight = False, True
                continue
        up = cmd.upper()
        rel = cmd.islower()
        k = NARGS[up]
        args = [float(t[1]) for t in toks[i:i + k]]
        i += k
        if len(args) < k:
            break
        if up == "M":
            flush()
            pts.clear()
            straight = True
            x, y = (x + args[0], y + args[1]) if rel else (args[0], args[1])
            sx, sy = x, y
            pts.append((x, y))
            cmd = "l" if rel else "L"
        elif up == "L":
            x, y = (x + args[0], y + args[1]) if rel else (args[0], args[1])
            pts.append((x, y))
        elif up == "H":
            x = x + args[0] if rel else args[0]
            pts.append((x, y))
        elif up == "V":
            y = y + args[0] if rel else args[0]
            pts.append((x, y))
        else:
            straight = False
            x, y = (x + args[-2], y + args[-1]) if rel else (args[-2], args[-1])
            pts.append((x, y))
    flush()
    return out

def is_tick(pts):
    """Three points: a short stroke down and right, then a longer one up and right."""
    if len(pts) != 3:
        return False
    (x0, y0), (x1, y1), (x2, y2) = pts
    d1, d2 = (x1 - x0, y1 - y0), (x2 - x1, y2 - y1)
    if not (d1[0] > 0 and d1[1] > 0 and d2[0] > 0 and d2[1] < 0):
        return False
    l1, l2 = math.hypot(*d1), math.hypot(*d2)
    if l1 < 1.2 or l2 < 1.25 * l1 or l2 > 3.5 * l1:
        return False
    a1 = math.degrees(math.atan2(d1[1], d1[0]))
    a2 = math.degrees(math.atan2(-d2[1], d2[0]))
    return 25 <= a1 <= 60 and 25 <= a2 <= 60

def ticks_in_svg(text):
    """Return a list of tick point triples found in one SVG's text."""
    found = []
    for d in re.findall(r'<path[^>]*?\sd="([^"]+)"', text):
        for pts, closed, straight in subpaths(d):
            if straight and not closed and is_tick(pts):
                found.append(pts)
    for pts in re.findall(r'<polyline[^>]*?\spoints="([^"]+)"', text):
        nums = [float(v) for v in re.findall(r"-?\d*\.?\d+", pts)]
        p = list(zip(nums[::2], nums[1::2]))
        if is_tick(p):
            found.append(p)
    return found

def own_svgs(*themes):
    """Yield built SVGs without following the symlinks into Papirus's own folders."""
    for theme in themes:
        for d, _, names in os.walk(os.path.join(ROOT, theme)):
            for n in names:
                p = os.path.join(d, n)
                if n.endswith(".svg") and not os.path.islink(p):
                    yield p

def main():
    files, bad = 0, []
    for path in own_svgs("Trindle-Circle"):
        files += 1
        with open(path, encoding="utf-8") as fh:
            if ticks_in_svg(fh.read()):
                bad.append(os.path.relpath(path, ROOT))
    assert files, "no built SVGs found: run build.py first"
    from symbolic.set1 import SYM
    for name, (_, fn) in SYM.items():
        if ticks_in_svg(fn()):
            bad.append("symbolic drawing " + name)
    assert not bad, f"{len(bad)} icons with a tick, first: {bad[:5]}"
    print(f"ok: {files} SVGs and {len(SYM)} symbolic drawings, no ticks")

if __name__ == "__main__":
    main()
