# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 81: apps Papirus lacks (ollama to parabolic)."""
from lm import *
from glyphs.kit import ellipse, ering_c, registry

ICONS, SMALL, reg, small = registry()

LLAMA = ("M18 49V36.5C18 31.5 19.5 28.5 22 26.5V16.5C22 11.5 27 11.5 27 16.5V24"
         "C30 23 34 23 37 24V16.5C37 11.5 42 11.5 42 16.5V26.5C44.5 28.5 46 31.5 46 36.5V49")

def _llama(detail=True):
    head = stroke(LLAMA, INK, 3.2)
    eyes = circle(25.5, 34, 2.1, INK) + circle(38.5, 34, 2.1, INK)
    snout = ering_c(32, 41, 5.6, 4, INK, 2.4)
    nose = ellipse(32, 40.2, 1.6, 1.1, INK) if detail else ""
    return head + eyes + snout + nose

@reg("ollama", GREY_SOFT)
def ollama():
    return _llama()

@small("ollama")
def ollama_small():
    return _llama(False)

@reg("anytype", BLUE_GREY_DARK)
def anytype():
    bar = rrect(15, 12.5, 19, 8, 3, INK)
    dot = circle(24.5, 38.5, 9.5, INK)
    post = rrect(38.5, 22.5, 9.5, 26, 3.5, INK)
    return bar + dot + post

def _tri_spiral(levels, widths):
    pts = [(32, 11.5), (50.5, 45), (13.5, 45)]
    out = ""
    for k in range(levels):
        d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z"
        out += stroke(d, INK, widths[k])
        t = .3
        pts = [(pts[i][0] + (pts[(i + 1) % 3][0] - pts[i][0]) * t,
                pts[i][1] + (pts[(i + 1) % 3][1] - pts[i][1]) * t) for i in range(3)]
    return out

@reg("affine", BLUE_DEEP)
def affine():
    return _tri_spiral(4, [3.4, 2.6, 2.3, 2.2])

@small("affine")
def affine_small():
    return _tri_spiral(2, [3.6, 3])

@reg("appflowy", BLUE_GREY_DARK)
def appflowy():
    return (ellipse(23.5, 21, 11.5, 7, DEEP_PURPLE_LIGHT, -45) +
            ellipse(40.5, 21, 11.5, 7, LIGHT_BLUE_LIGHT, 45) +
            ellipse(23.5, 39, 11.5, 7, PINK_LIGHT, 45) +
            ellipse(40.5, 39, 11.5, 7, AMBER, -45))

def _penpot(pencils=3):
    out = ""
    xs = [23, 32, 41] if pencils == 3 else [26, 38]
    w = 6.5 if pencils == 3 else 9
    for cx in xs:
        out += poly([(cx - w / 2, 31), (cx - w / 2, 18.5), (cx, 12.5),
                     (cx + w / 2, 18.5), (cx + w / 2, 31)], INK, 1.2)
    box = [(15, 27), (32, 33), (49, 27), (49, 43), (32, 49), (15, 43)]
    out += poly(box, HOLE, 4.5) + poly(box, INK, 1.8)
    out += line(32, 34, 32, 48, HOLE, 1.8)
    return out

@reg("penpot", TEAL_DARK)
def penpot():
    return _penpot()

@small("penpot")
def penpot_small():
    out = ""
    for cx in (22.5, 32, 41.5):
        out += poly([(cx - 3, 30), (cx - 3, 17), (cx, 11), (cx + 3, 17), (cx + 3, 30)], INK, 1)
    box = [(14.5, 30), (32, 36), (49.5, 30), (49.5, 44), (32, 50), (14.5, 44)]
    out += poly(box, HOLE, 5) + poly(box, INK, 1.5)
    return out

def _qpw(w, r):
    wires = (stroke("M16 18H20C27 18 26 30 32 30C38 30 37 42 44 42H48", INK, w) +
             stroke("M16 42H20C27 42 26 30 32 30C38 30 37 18 44 18H48", INK, w) +
             line(16, 30, 48, 30, INK, w))
    nodes = ""
    for x in (16, 48):
        for y in (18, 30, 42):
            nodes += circle(x, y, r, INK) + circle(x, y, r * .42, HOLE)
    return wires + nodes

@reg("qpwgraph", BLUE_GREY_DEEP)
def qpwgraph():
    return _qpw(3, 4)

@small("qpwgraph")
def qpwgraph_small():
    return (stroke("M17 20C28 20 36 40 47 40", INK, 3.6) +
            stroke("M17 40C28 40 36 20 47 20", INK, 3.6) +
            circle(17, 20, 4.5, INK) + circle(17, 40, 4.5, INK) +
            circle(47, 20, 4.5, INK) + circle(47, 40, 4.5, INK))

@reg("grayjay", BLUE_GREY_DARK)
def grayjay():
    tri = poly([(13.5, 21), (50.5, 21), (32, 48)], LIGHT_BLUE_LIGHT, 3)
    body = ellipse(33, 28, 12, 7.8, INK, -48)
    head = circle(40.5, 16.5, 5, INK)
    beak = poly([(44, 14), (49.5, 14.5), (45, 18.5)], INK, 1)
    tail = poly([(26, 32), (14, 44), (20, 44.5), (31.5, 37)], INK, 1.5)
    return tri + body + head + beak + tail

def _dish(cols, rows):
    out = rrect(30, 38, 4, 11, 2, INK)
    out += path("M14 16Q32 21.5 50 16V37Q32 42.5 14 37Z", INK,
                f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    step = 34 / (2 * cols + 1)
    xs = [15 + step * (k + .5) for k in range(cols)] + \
         [49 - step * (k + .5) for k in range(cols)]
    h = 16 / rows - 2
    for x in xs:
        dy = 2.7 * (1 - ((x - 32) / 18) ** 2)
        for r in range(rows):
            y = 19.5 + dy + r * (h + 2.2)
            out += rrect(x - 1.4, y, 2.8, h, 1.4, HOLE)
    out += circle(32, 12.5, 3, INK) + line(32, 13, 32, 36, HOLE, 2.2)
    return out

@reg("parabolic", RED_DEEP)
def parabolic():
    return _dish(3, 2)

@small("parabolic")
def parabolic_small():
    out = rrect(29.5, 38, 5, 11, 2.5, INK)
    out += path("M14 16Q32 21.5 50 16V37Q32 42.5 14 37Z", INK,
                f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    for x in (20.5, 43.5):
        dy = 2.7 * (1 - ((x - 32) / 18) ** 2)
        out += rrect(x - 2, 20.5 + dy, 4, 14, 2, HOLE)
    out += circle(32, 12.5, 3.5, INK) + line(32, 13, 32, 36, HOLE, 3)
    return out
