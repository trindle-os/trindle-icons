# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 4: OPNplug to aafm."""
import math
from lm import (
    AMBER_DEEP, AMBER_SOFT, BLUE, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_SOFT, BLUE_LIGHT, BROWN, BROWN_DARK, BROWN_DEEP, BROWN_SOFT, circle, CX, CY,
    CYAN_DARK, CYAN_SOFT, DEEP_ORANGE, DEEP_ORANGE_SOFT, DEEP_PURPLE_DARK, DEEP_PURPLE_LIGHT,
    DEEP_PURPLE_SOFT, f, g, GREY_DARK, GREY_DEEP, HOLE, INDIGO, INDIGO_DARK, INDIGO_DEEP,
    INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE_DARK, line, ORANGE_DARK, ORANGE_DEEP,
    ORANGE_LIGHT, path, PINK_DARK, PINK_SOFT, poly, pt, RED_DEEP, RED_LIGHT, rrect, stroke,
    TEAL, TEAL_DEEP, YELLOW_DARK,
)
from glyphs.kit import registry, _ring

ICONS, SMALL, reg, small = registry()


def pixels(rows, x0, y0, u, colour):
    """Pixel art: one rect per horizontal run of X in each row."""
    out = ""
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):
            if row[c] == "X":
                s = c
                while c < len(row) and row[c] == "X":
                    c += 1
                out += rrect(x0 + s * u - .05, y0 + r * u - .05, (c - s) * u + .1, u + .1, 0, colour)
            else:
                c += 1
    return out


@reg("OPNplug", RED_DEEP)
def opnplug():
    o = f'<ellipse cx="19.5" cy="30" rx="4.3" ry="7.2" fill="none" stroke="{INK}" stroke-width="3.6"/>'
    p = stroke("M29 38V22H33A4.3 4.3 0 0 1 33 30.6H29", INK, 3.6)
    n = stroke("M41 38V22L49.5 38V22", INK, 3.6)
    return o + p + n


@reg("Onivim2", DEEP_PURPLE_DARK)
def onivim2():
    ring_ = _ring(30, 32, 14.5, INK, 3)
    disc = circle(30, 32, 8.5, INK)
    bands = rrect(20, 32.3, 20, 2.2, 0, HOLE) + rrect(20, 36.3, 20, 2, 0, HOLE)
    two = circle(44.5, 17, 7.5, HOLE) + stroke("M41.5 14.5C42 11.5 47.5 11.5 47.5 14.5C47.5 17 42 19 41.5 21H47.5", CYAN_SOFT, 2.4)
    return ring_ + disc + bands + two


@reg("OpenAudible", ORANGE_DEEP)
def openaudible():
    chev = stroke("M14 32L32 43L50 32", INK, 4.6)
    arcs = (stroke("M20 31C25 22 39 20 45 29", INK, 3.6) +
            stroke("M25 32.5C28.5 27.5 36 27 39.5 32", INK, 3.4))
    return chev + arcs


@reg("QMPlay2", INDIGO_LIGHT)
def qmplay2():
    outer = poly([(18, 14), (48, 30), (18, 46)], INK, 5)
    inner = poly([(23.5, 22.5), (39, 30), (23.5, 37.5)], INDIGO_SOFT, 2)
    return outer + inner


@reg("QtAV", GREY_DEEP)
def qtav():
    return (circle(CX, CY, 16, INK) +
            poly([(27.5, 21.5), (41, 30), (27.5, 38.5)], HOLE, 3))


@reg("Play", INDIGO_LIGHT)
def play():
    bar = path("M28.5 15.5A3.5 3.5 0 0 1 35.5 15.5L34.3 35.5A2.3 2.3 0 0 1 29.7 35.5Z", INK)
    return bar + circle(32, 43.5, 3.8, INK)


@reg("Zoom", BLUE)
def zoom():
    return (rrect(13.5, 20, 25, 20, 5.5, INK) +
            poly([(41.5, 26.5), (49.5, 21), (49.5, 39), (41.5, 33.5)], INK, 2.5))


@reg("StartWine", BLUE_DEEP)
def startwine():
    arc = stroke("M24 18.5A13.5 13.5 0 1 0 40 18.5", INK, 3.6)
    bar = line(32, 12, 32, 22, INK, 3.6)
    water = path("M23 32C26 30 29 34 32 32C35 30 38 34 41 32A9 9 0 0 1 23 32Z", INK)
    return arc + bar + water


@reg("RenameMyTVSeries", ORANGE_DEEP)
def renamemytv():
    tv = rrect(13, 14, 38, 31, 5, INK)
    screen = rrect(16.5, 17.5, 25, 24, 7, HOLE)
    knobs = circle(46, 21.5, 2.2, HOLE) + circle(46, 28, 2.2, HOLE) + rrect(43.5, 34.5, 5, 2, 1, HOLE) + rrect(43.5, 38, 5, 2, 1, HOLE)
    pencil = line(25, 34.5, 33.5, 26, INK, 3.4) + poly([(22.5, 37), (23.3, 33.8), (25.7, 36.2)], INK, 1)
    return tv + screen + knobs + pencil


def _slicer(dark):
    base = circle(CX, CY, 16.5, INK)
    s = math.sqrt(.5)

    def half(cx, cy, r, colour):
        x1, y1 = cx + r * s, cy - r * s
        x2, y2 = cx - r * s, cy + r * s
        return path(f"M{f(x1)} {f(y1)}A{f(r)} {f(r)} 0 0 0 {f(x2)} {f(y2)}Z", colour)
    return base + half(30.3, 28.3, 11.5, dark) + half(33.7, 31.7, 11.5, HOLE)


@reg("PrusaSlicer", DEEP_ORANGE)
def prusaslicer():
    return _slicer(BROWN_DARK)


@reg("SuperSlicer", BLUE)
def superslicer():
    return _slicer(INDIGO_DARK)


@reg("PosteRazor", GREY_DEEP)
def posterazor():
    blade = rrect(13, 19, 38, 22, 3, INK)
    slot = circle(32, 30, 5.2, HOLE) + rrect(19.5, 28.2, 25, 3.6, 1.8, HOLE)
    notches = (poly([(11, 26.5), (16, 30), (11, 33.5)], HOLE, 1.5) +
               poly([(53, 26.5), (48, 30), (53, 33.5)], HOLE, 1.5))
    return blade + slot + notches


@reg("PyCrust", AMBER_DEEP)
def pycrust():
    top = path("M14 28L41 15C45.5 13 50 16 50 20.5V28Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    block = rrect(13, 31, 38, 15, 3, INK)
    jam = rrect(13, 36.5, 38, 4, 0, PINK_DARK)
    return top + block + jam


@reg("QOwnNotes", INDIGO_DEEP)
def qownnotes():
    page = path("M18 13H43A3.5 3.5 0 0 1 46.5 16.5V43.5A3.5 3.5 0 0 1 43 47H26L15 36V16A3 3 0 0 1 18 13Z", INK)
    fold = path("M15 36H23A3 3 0 0 1 26 39V47Z", INDIGO_SOFT)
    cloud = stroke("M25 32.5H39A4.5 4.5 0 0 0 39 23.5A7 7 0 0 0 26.5 23.8A4.4 4.4 0 0 0 25 32.5Z", HOLE, 2.8)
    return page + fold + cloud


@reg("SymbolEditor", BLUE_GREY)
def symboleditor():
    sq = rrect(16, 14, 12.5, 12.5, 2, "none", f' stroke="{INK}" stroke-width="3.2"')
    ci = circle(41.5, 20.2, 7.3, INK)
    plus = line(22.2, 34, 22.2, 46, INK, 4) + line(16.2, 40, 28.2, 40, INK, 4)
    tri = poly([(41.5, 33.5), (48, 46), (35, 46)], INK, 2.5)
    return sq + ci + plus + tri


@reg("SysMonTask", BLUE_DEEP)
def sysmontask():
    mon = rrect(13, 13, 38, 27, 4, INK) + rrect(16.5, 16.5, 31, 20, 2, HOLE)
    pulse = stroke("M18.5 28H24L28 21L33 34L37 26.5H45.5", INK, 2.6)
    stand = rrect(29, 39, 6, 6, 0, INK) + rrect(22, 44, 20, 4, 2, INK)
    return mon + pulse + stand


@reg("Worker", BLUE_GREY)
def worker():
    win = rrect(14, 13, 36, 34, 4, INK)
    panes = rrect(17.5, 19.5, 13.5, 16, 1.5, HOLE) + rrect(33, 19.5, 13.5, 16, 1.5, HOLE)
    bars = (rrect(17.5, 38.5, 13.5, 2.6, 1.3, HOLE) + rrect(33, 38.5, 13.5, 2.6, 1.3, HOLE) +
            rrect(17.5, 42.3, 8, 2.6, 1.3, HOLE) + rrect(33, 42.3, 8, 2.6, 1.3, HOLE))
    return win + panes + bars


@reg("Xfwm4CompositeEditor", TEAL_DEEP)
def xfwm4ce():
    teeth = "".join(g(rrect(28.5, 12.5, 7, 8, 2, INK), f"rotate({45 * k} 32 30)") for k in range(8))
    return teeth + circle(CX, CY, 13, INK) + circle(CX, CY, 5.5, HOLE)


@reg("XRCed", INDIGO)
def xrced():
    x = line(15, 14, 22.5, 25, INK, 3) + line(22.5, 14, 15, 25, INK, 3)
    r = stroke("M27 25V14H30.5A3 3 0 0 1 30.5 20H27M30.5 20L34 25", INK, 3)
    c = stroke("M48.5 15.5A5.5 5.5 0 1 0 48.5 23.5", INK, 3)
    e = stroke("M20.5 38H31.5A5.5 5.5 0 1 0 29.5 42.5", INK, 3)
    d = _ring(39.5, 38, 5.5, INK, 3) + line(45, 29, 45, 44, INK, 3)
    return x + r + c + e + d


@reg("TeXworks", INDIGO)
def texworks():
    t = path("M15 13H43V21H40.5L39 17.5H32V42H36V46H22V42H26V17.5H19L17.5 21H15Z", INK,
             f' stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"')
    badge = circle(43, 40, 9.5, INDIGO_DARK, f' stroke="{HOLE}" stroke-width="2"')
    pencil = line(39.5, 43.5, 46.5, 36.5, INK, 3.2)
    return t + badge + pencil


@reg("TeXmacs", BLUE_GREY_DEEP)
def texmacs():
    return stroke("M45 15H20V45H45M45 15L33 30L45 45", INK, 4.6)


@reg("TeighaViewer", RED_DEEP)
def teighaviewer():
    return (_ring(35, 34, 11.5, INK, 3.2) + _ring(23, 25.5, 7.8, INK, 3.2) +
            _ring(31.5, 19.5, 7.8, INK, 3.2))


@reg("Temps", TEAL)
def temps():
    sun = circle(25, 22.5, 7, AMBER_SOFT)
    cloud = (circle(27.5, 33, 6.5, INK) + circle(36, 29.5, 8.5, INK) +
             circle(43.5, 35, 5.5, INK) + rrect(20, 33, 29, 8.5, 4.25, INK))
    return sun + cloud


@reg("ToneLib-GFX", BROWN_DEEP)
def tonelib_gfx():
    head = rrect(15, 12.5, 34, 10, 3, INK)
    knobs = "".join(circle(x, 17.5, 1.9, HOLE) for x in (32, 38, 44)) + rrect(19, 15.5, 5, 4, 1, HOLE)
    cab = rrect(15, 25, 34, 22.5, 3, INK)
    spk = circle(32, 36.2, 8, HOLE) + circle(32, 36.2, 3.4, INK)
    return head + knobs + cab + spk


@reg("ToneLib-Jam", RED_DEEP)
def tonelib_jam():
    neck = line(29, 35, 44.5, 17.5, INK, 3.4)
    head = g(rrect(43, 11, 5, 9, 2, INK), "rotate(41 45.5 15.5)")
    body = path("M26 29C23.5 29.5 22 31.5 20.5 33C17 33 14.5 36 15 40C15.5 44.5 19.5 47.5 24 47"
                "C27 46.5 28.5 44 29.5 41.5C31.5 41 34 40.5 35 38.5C35.5 37 34.5 36 33 36"
                "C31.5 35 31 33.5 31.5 31.5C32 29.5 30 28.5 28 30Z", INK)
    pick = line(21.5, 38, 25, 42, HOLE, 2.2) + circle(27.5, 37, 1.6, HOLE)
    return neck + head + body + pick


@reg("ToneLib-Zoom", BLUE_GREY_DEEP)
def tonelib_zoom():
    body = rrect(17, 11.5, 30, 38, 4.5, INK)
    disp = rrect(21, 15.5, 22, 9, 1.8, HOLE)
    digits = stroke("M25.5 17.5V20.5H28.5M28 17.5V22.5", INK, 1.6) + stroke("M33.5 18H37V20H33.5V22.5H37", INK, 1.6)
    knob = circle(32, 33.5, 6.8, HOLE) + line(32, 33.5, 35.5, 30, INK, 2.2)
    dots = "".join(circle(x, 44.5, 1.9, HOLE) for x in (25, 32, 39))
    return body + disp + digits + knob + dots


@reg("VCVRack", BLUE_GREY_DARK)
def vcvrack():
    a, b = pt(32, 30, 11, -42), pt(32, 30, 11, 42)
    c = stroke(f"M{f(a[0])} {f(a[1])}A11 11 0 1 0 {f(b[0])} {f(b[1])}", INK, 8)
    return c + circle(32, 30, 4.2, INK)


@reg("Ri-li", ORANGE_DARK)
def rili():
    d = "M19.5 30V20.5H43.5V47"
    return stroke(d, INK, 9.5) + stroke(d, HOLE, 2.6)


@reg("Ripcord_Icon", BLUE_GREY_DEEP)
def ripcord():
    def frame(cy, colour):
        outer = f"M32 {f(cy - 10)}L50 {f(cy)}L32 {f(cy + 10)}L14 {f(cy)}Z"
        inner = f"M32 {f(cy - 4.6)}L40.3 {f(cy)}L32 {f(cy + 4.6)}L23.7 {f(cy)}Z"
        return path(outer + inner, colour, f' fill-rule="evenodd" stroke="{colour}" stroke-width="1.5" stroke-linejoin="round"')
    return frame(37, BLUE_GREY_SOFT) + frame(31.5, DEEP_ORANGE_SOFT) + frame(24, INK)


@reg("Sci48M", CYAN_DARK)
def sci48m():
    disc = circle(CX, CY, 16.5, INK)
    waves = ""
    for dx in (-9, -1, 7):
        x = 32 + dx
        waves += stroke(f"M{f(x - 2)} 15.5C{f(x + 5)} 21 {f(x - 4)} 27 {f(x + 2)} 32"
                        f"C{f(x + 7)} 36 {f(x)} 41 {f(x + 5)} 44.5", HOLE, 3)
    return disc + waves


@reg("SheepShaver", PINK_SOFT)
def sheepshaver():
    petals = "".join(circle(*pt(32, 30, 11, 22.5 + 45 * k), 6.5, INK) for k in range(8))
    apple = path("M32 26C29 24 23.5 24.5 23.5 30.5C23.5 35.5 27 40 29.5 40C30.8 40 31 39.3 32 39.3"
                 "C33 39.3 33.2 40 34.5 40C37 40 40.5 35.5 40.5 30.5C40.5 24.5 35 24 32 26Z", HOLE)
    leaf = path("M32 24.5C32 21.5 34 19.5 36.5 19.5C36.5 22 34.5 24 32 24.5Z", HOLE)
    return petals + circle(CX, CY, 12, INK) + apple + leaf


@reg("Sparrow", BROWN)
def sparrow():
    body = path("M44 19C40 16.5 35 18 33 22L16 43C22 43 28 41 33 37C39 33 43 28 44 23Z", INK)
    head = circle(41, 21, 6.2, INK) + poly([(46.5, 19), (51, 21), (46.5, 23)], INK, 1.5)
    wing = path("M34 25C30 20 25 17 18 16C21 21 25 27 30 30Z", BROWN_SOFT)
    eye = circle(42.5, 20, 1.6, HOLE)
    return wing + body + head + eye


@reg("SpiderOakONE", BLUE_DEEP)
def spideroak():
    shield = path("M17 13H47V35L32 47.5L17 35Z", INK,
                  f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return shield + poly([(32, 16.5), (40.5, 25), (32, 33.5), (23.5, 25)], HOLE, 2)


@reg("VVVVVV", LIGHT_BLUE_DARK)
def vvvvvv():
    rows = [".XXXXXXX.",
            "XXXXXXXXX",
            "X..XXX..X",
            "X..XXX..X",
            "XXXXXXXXX",
            "X.XXXXX.X",
            "XX.....XX",
            ".XXXXXXX.",
            "..XXXXX.."]
    return pixels(rows, 16.25, 13.5, 3.5, INK)


@reg("Weasis", BLUE_DEEP)
def weasis():
    return stroke("M19.5 14L32 45.5L44.5 14", INK, 5) + poly([(25, 26), (39, 26), (32, 44)], INK, 2)


@reg("WickrMe", GREY_DARK)
def wickrme():
    return line(18, 41, 33, 22, INK, 6) + line(31, 41, 46, 22, INK, 6)


@reg("YACReader", AMBER_DEEP)
def yacreader():
    return path("M32 12.5C42 12.5 49.5 18.5 49.5 27C49.5 35.5 42 41 32 41C30 41 28 40.8 26.5 40.3"
                "C24 43.5 21 46 17.5 47C19.5 44.5 20.5 41.5 20.5 38.5C16.5 35.5 14.5 31.5 14.5 27"
                "C14.5 18.5 22 12.5 32 12.5Z", INK)


@reg("YACReaderLibrary", AMBER_DEEP)
def yacreaderlib():
    book = rrect(17, 12, 30, 36, 3.5, INK)
    spine = rrect(22, 12, 2.6, 36, 0, HOLE)
    mark = poly([(35, 12), (42, 12), (42, 26), (38.5, 22.5), (35, 26)], HOLE, 1)
    return book + spine + mark


@reg("ZeroNet", DEEP_PURPLE_LIGHT)
def zeronet():
    return stroke("M17.5 31V21.5L32 13L46.5 21.5L17.5 38.5L32 47L46.5 38.5V29", INK, 5)


@reg("OpenLieroX", BLUE_GREY_DARK)
def openlierox():
    hat = (rrect(14, 21, 36, 4, 2, INK) +
           path("M21 21.5L22.5 14C23 12 24.5 11.5 26.5 12.5C29.5 14 34.5 14 37.5 12.5"
                "C39.5 11.5 41 12 41.5 14L43 21.5Z", INK))
    band = rrect(21.5, 18, 21, 2.2, 0, HOLE)
    face = poly([(20, 27.5), (44, 27.5), (32, 47.5)], INK, 3)
    eyes = (circle(27.5, 32, 3.6, HOLE) + circle(36.5, 32, 3.6, HOLE) +
            circle(28.2, 32.6, 1.6, INK) + circle(35.8, 32.6, 1.6, INK))
    return hat + band + face + eyes


@reg("PCSX2", INDIGO)
def pcsx2():
    diamond = g(rrect(16.5, 14.5, 31, 31, 6.5, "none", f' stroke="{INK}" stroke-width="3.2"'), "rotate(45 32 30)")
    marks = g(stroke("M23.5 22.5H30V29.5H23.5V37H30", INK, 3.4) +
              stroke("M40.5 22.5H34V29.5H40.5V37H34", INK, 3.4), "rotate(45 32 30)")
    return diamond + marks


@reg("a-boy-and-his-blob", INDIGO_DEEP)
def boyblob():
    blob = path("M14 45.5C14 38 16.5 31 20.5 25C24 18 28 13.5 34 13.5C42 13.5 46.5 19.5 47 27"
                "C47.5 34 50 39.5 50 45.5Z", INK)
    face = circle(35.5, 23.5, 2.3, HOLE) + circle(42.5, 23.5, 2.3, HOLE)
    mouth = f'<ellipse cx="39" cy="31" rx="4.6" ry="3" fill="{HOLE}"/>'
    return blob + face + mouth


@reg("a-dance-of-fire-and-ice", DEEP_PURPLE_DARK)
def adofai():
    red, blue = RED_LIGHT, BLUE_LIGHT
    trail_r = path("M22 16.5C31 13 41 13.5 48 18.5C41 17.5 33 19 27.5 24Z", red)
    trail_b = path("M42 43.5C33 47 23 46.5 16 41.5C23 42.5 31 41 36.5 36Z", blue)
    return trail_r + circle(23, 23, 6.8, red) + trail_b + circle(41, 37, 6.8, blue)


@reg("a-short-hike", DEEP_PURPLE_SOFT)
def ashorthike():
    bird = INDIGO_DEEP
    body = path("M24 25C20 30 19 38 22 43C25 47.5 33 47.5 36 43C38.5 39 37 33 34 29Z", bird)
    head = circle(32, 22.5, 9.5, bird)
    beak = poly([(40.5, 20), (48.5, 23), (40.5, 26)], ORANGE_LIGHT, 2)
    eye = circle(35, 20.5, 3.4, INK) + circle(35.8, 20.8, 1.6, INDIGO_DARK)
    return body + head + beak + eye


@reg("a-story-about-my-uncle", BLUE_GREY_DARK)
def storyuncle():
    return (stroke("M32 11.5V19.5L22 29.5L32 39.5V48.5", INK, 3.4) +
            stroke("M32 19.5L39 26.5L34.5 31", INK, 3.4) +
            stroke("M32 39.5L40.5 31L43.5 34", INK, 3.4))


@reg("a7800", BLUE_GREY_DARK)
def a7800():
    left = path("M23 12H28.5V26C28.5 36 25 43 20.5 47.5H14C19 41.5 23 34.5 23 24Z", RED_LIGHT)
    mid = rrect(29.5, 12, 5, 35.5, 0, BROWN_SOFT)
    right = path("M41 12H35.5V26C35.5 36 39 43 43.5 47.5H50C45 41.5 41 34.5 41 24Z", BLUE_LIGHT)
    return left + mid + right


@reg("a7xpg", DEEP_PURPLE_LIGHT)
def a7xpg():
    crown = poly([(15, 25), (24, 34), (32, 13), (40, 34), (49, 25), (44, 44), (20, 44)], INK, 3)
    return crown + stroke("M22 42L32 34L42 42", HOLE, 2.6)


@reg("aaaaxy", YELLOW_DARK)
def aaaaxy():
    frame = rrect(19, 13, 26, 34, 2, INK) + rrect(15, 17, 34, 26, 2, INK) + rrect(17, 15, 30, 30, 2, INK)
    arrow = pixels(["..X..", ".XXX.", "XXXXX", "..X..", "..X..", "..X.."], 23.25, 19.5, 3.5, HOLE)
    return frame + arrow


@reg("aafm", BLUE_LIGHT)
def aafm():
    head = path("M18.5 25A13.5 13.5 0 0 1 45.5 25Z", INK)
    ants = line(22.5, 13.5, 25, 17, INK, 2.4) + line(41.5, 13.5, 39, 17, INK, 2.4)
    eyes = circle(26.5, 20.5, 1.8, HOLE) + circle(37.5, 20.5, 1.8, HOLE)
    body = rrect(18.5, 27.5, 27, 20, 3.5, INK)
    folder = path("M24 33.5A1.5 1.5 0 0 1 25.5 32H29.5L31 34H38.5A1.5 1.5 0 0 1 40 35.5V41.5"
                  "A1.5 1.5 0 0 1 38.5 43H25.5A1.5 1.5 0 0 1 24 41.5Z", HOLE)
    return head + ants + eyes + body + folder


@small("OPNplug")
def opnplug_s():
    o = f'<ellipse cx="18.5" cy="30" rx="4.6" ry="8" fill="none" stroke="{INK}" stroke-width="2.6"/>'
    return (o + stroke("M28 38.5V21.5H32.5A4.5 4.5 0 0 1 32.5 30.5H28", INK, 2.6) +
            stroke("M40.5 38.5V21.5L49.5 38.5V21.5", INK, 2.6))


@small("Onivim2")
def onivim2_s():
    return (_ring(32, 30, 15, INK, 3.2) + circle(32, 30, 8.5, INK) +
            rrect(22, 31.5, 20, 3, 0, HOLE))


@small("OpenLieroX")
def openlierox_s():
    hat = rrect(13, 20, 38, 5, 2.5, INK) + rrect(21, 11.5, 22, 10, 4, INK)
    face = poly([(19, 28), (45, 28), (32, 48)], INK, 3)
    return hat + face + circle(27, 33, 4, HOLE) + circle(37, 33, 4, HOLE)


@small("PCSX2")
def pcsx2_s():
    diamond = g(rrect(16.5, 14.5, 31, 31, 6.5, "none", f' stroke="{INK}" stroke-width="3"'), "rotate(45 32 30)")
    return diamond + g(stroke("M25 22.5H38.5V30H25.5V37.5H39", INK, 3.4), "rotate(45 32 30)")


@small("PosteRazor")
def posterazor_s():
    return rrect(12, 18, 40, 24, 4, INK) + circle(32, 30, 6.5, HOLE) + rrect(18, 27.5, 28, 5, 2.5, HOLE)


@small("QOwnNotes")
def qownnotes_s():
    page = path("M18 12H44A3.5 3.5 0 0 1 47.5 15.5V44.5A3.5 3.5 0 0 1 44 48H27L14.5 35.5V15.5A3.5 3.5 0 0 1 18 12Z", INK)
    cloud = stroke("M23.5 35H40A5.5 5.5 0 0 0 40 24A8 8 0 0 0 25.5 24A5.5 5.5 0 0 0 23.5 35Z", HOLE, 3)
    return page + cloud


@small("RenameMyTVSeries")
def renamemytv_s():
    tv = rrect(12, 13, 40, 33, 5, INK) + rrect(15.5, 16.5, 27, 26, 7, HOLE)
    return (tv + circle(47, 22, 2.5, HOLE) + circle(47, 30, 2.5, HOLE) +
            line(22, 36, 34, 24, INK, 4.2))


@small("Ripcord_Icon")
def ripcord_s():
    def frame(cy, colour):
        return path(f"M32 {f(cy - 11)}L51 {f(cy)}L32 {f(cy + 11)}L13 {f(cy)}Z"
                    f"M32 {f(cy - 4.5)}L40 {f(cy)}L32 {f(cy + 4.5)}L24 {f(cy)}Z", colour,
                    f' fill-rule="evenodd" stroke="{colour}" stroke-width="1.5" stroke-linejoin="round"')
    return frame(36, DEEP_ORANGE_SOFT) + frame(26, INK)


@small("Sci48M")
def sci48m_s():
    waves = "".join(stroke(f"M{f(x - 2)} 15C{f(x + 6)} 21 {f(x - 5)} 28 {f(x + 2)} 33C{f(x + 7)} 37 {f(x)} 41 {f(x + 4)} 45", HOLE, 3.2)
                    for x in (27, 37))
    return circle(CX, CY, 17, INK) + waves


@small("SheepShaver")
def sheepshaver_s():
    petals = "".join(circle(*pt(32, 30, 11, 22.5 + 45 * k), 7, INK) for k in range(8))
    apple = path("M32 25C28.5 23 22.5 23.5 22.5 30.5C22.5 36 26.5 41 29.5 41C31 41 31 40.3 32 40.3"
                 "C33 40.3 33 41 34.5 41C37.5 41 41.5 36 41.5 30.5C41.5 23.5 35.5 23 32 25Z", HOLE)
    return petals + circle(CX, CY, 12, INK) + apple


@small("SymbolEditor")
def symboleditor_s():
    sq = rrect(15.5, 13.5, 12, 12, 2, "none", f' stroke="{INK}" stroke-width="3"')
    plus = line(21.5, 34, 21.5, 46, INK, 3.4) + line(15.5, 40, 27.5, 40, INK, 3.4)
    return sq + circle(42, 19.5, 6.5, INK) + plus + poly([(42, 34.5), (48, 45.5), (36, 45.5)], INK, 2)


@small("SysMonTask")
def sysmontask_s():
    mon = rrect(12, 12, 40, 29, 4, INK) + rrect(15.5, 15.5, 33, 22, 2, HOLE)
    pulse = stroke("M19 28H25L29.5 21L34 34L38 27H45", INK, 3)
    return mon + pulse + rrect(21, 43, 22, 5, 2.5, INK)


@small("TeXworks")
def texworks_s():
    return path("M14 12H46V22H42L40.5 18.5H35V42H39V47H25V42H29V18.5H23.5L22 22H18Z", INK,
                f' stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"')


@small("TeighaViewer")
def teighaviewer_s():
    return _ring(35.5, 34.5, 11.5, INK, 2.6) + _ring(23, 24, 8.5, INK, 2.6)


@small("ToneLib-GFX")
def tonelib_gfx_s():
    return (rrect(14, 11.5, 36, 10, 3, INK) + rrect(19, 15, 26, 3.2, 1.6, HOLE) +
            rrect(14, 24.5, 36, 24, 3.5, INK) + circle(32, 36.5, 8, HOLE))


@small("ToneLib-Jam")
def tonelib_jam_s():
    neck = line(29, 35, 45, 16.5, INK, 4.2)
    body = circle(22.5, 40, 8.5, INK) + circle(28.5, 34, 5.5, INK)
    return neck + body + circle(23, 40, 2.4, HOLE)


@small("ToneLib-Zoom")
def tonelib_zoom_s():
    return (rrect(16, 11, 32, 39, 5, INK) + rrect(20.5, 15, 23, 9.5, 2, HOLE) +
            circle(32, 36, 7.5, HOLE))


@small("Worker")
def worker_s():
    return (rrect(13, 12, 38, 36, 4.5, INK) + rrect(17, 19, 13.5, 24, 2, HOLE) +
            rrect(33.5, 19, 13.5, 24, 2, HOLE))


@small("XRCed")
def xrced_s():
    e = stroke("M14.5 30H29.5A7.5 7.5 0 1 0 27 36", INK, 3.8)
    d = _ring(40.5, 30, 7.5, INK, 3.8) + line(48, 12, 48, 38, INK, 3.8)
    return e + d


@small("aafm")
def aafm_s():
    head = path("M17.5 25A14.5 14.5 0 0 1 46.5 25Z", INK)
    body = rrect(17.5, 28, 29, 20, 4, INK)
    folder = path("M23 33A1.5 1.5 0 0 1 24.5 31.5H29.5L31.5 34H39.5A1.5 1.5 0 0 1 41 35.5V42"
                  "A1.5 1.5 0 0 1 39.5 43.5H24.5A1.5 1.5 0 0 1 23 42Z", HOLE)
    return head + body + folder
