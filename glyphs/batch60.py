# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 60: radicle-upstream to resharper."""
import math
from lm import (
    AMBER, AMBER_DEEP, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_LIGHT, BLUE_SOFT, BROWN_DARK, BROWN_LIGHT, circle,
    cpath, cut, CX, CY, CYAN_DEEP, DEEP_ORANGE, DEEP_ORANGE_DEEP, DEEP_PURPLE_DEEP,
    DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, g, GREY, GREY_DARK, HOLE, INDIGO, INDIGO_DEEP,
    INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP,
    LIGHT_BLUE_LIGHT, line, ORANGE, ORANGE_DEEP, path, PINK_DEEP, PINK_SOFT, poly, pt, PURPLE,
    RED, RED_DARK, RED_DEEP, RED_SOFT, rrect, stroke, TEAL_DEEP, TEAL_LIGHT, YELLOW,
    YELLOW_DARK, YELLOW_SOFT,
)
from glyphs.kit import arc, arrowhead_c, ell_b, registry, ring_b

ICONS, SMALL, reg, small = registry()


@reg("radicle-upstream", INDIGO_LIGHT)
def radicle_upstream():
    stem = stroke("M32 47V29", INK, 4.4)
    left = path("M31 31C23 31 16 25.5 16 15.5C24 15.5 31 21 31 31Z", INK)
    right = path("M33 28C33 20 39 13.5 48 13.5C48 22 42 28 33 28Z", INK)
    return stem + left + right


@reg("radiotray", BLUE_GREY_DEEP)
def radiotray():
    body = rrect(13.5, 16, 37, 29, 5, INK)
    spk = circle(25, 30.5, 7.5, HOLE) + circle(25, 30.5, 3, INK)
    lines = "".join(rrect(35, y, 10.5, 2.6, 1.3, HOLE) for y in (21, 26, 31))
    knobs = circle(37.3, 38.5, 2, HOLE) + circle(43.2, 38.5, 2, HOLE)
    return body + spk + lines + knobs


@reg("radiotunes", BLUE)
def radiotunes():
    stem = stroke("M28.5 15L25.5 39", INK, 5)
    head = g(ell_b(21.5, 40.5, 6, 4.6, INK), "rotate(-20 21.5 40.5)")
    bowl = stroke("M28.5 15H37C41.5 15 44 18 43.3 22C42.5 26.5 38.5 28.5 34 28.5H27", INK, 5)
    leg = stroke("M34 28.5L40 44", INK, 5)
    return stem + head + bowl + leg


@reg("rakarrack", ORANGE_DEEP)
def rakarrack():
    neck = line(31, 31, 44, 17, INK, 4)
    head = g(rrect(41.5, 10.5, 7, 10, 2.5, INK), "rotate(45 45 15.5)")
    body = circle(24.5, 38.5, 10, INK) + circle(31, 31.5, 7.5, INK)
    hole = circle(27, 35.5, 3, HOLE)
    bridge = g(rrect(18.5, 39.5, 8, 3, 1.5, HOLE), "rotate(-45 22.5 41)")
    return neck + head + body + hole + bridge


@reg("rambox", CYAN_DEEP)
def rambox():
    outer = stroke("M16.5 42C19 42 20.5 40.5 20.5 38V26A11.5 11.5 0 0 1 43.5 26V38"
                   "C43.5 40.5 45 42 47.5 42", INK, 3.8)
    inner = stroke("M26.5 40V27A5.5 5.5 0 0 1 37.5 27V40", INK, 3.8)
    mid = stroke("M32 33V44", INK, 3.8)
    return outer + inner + mid


@reg("rancher-desktop", BLUE_DEEP)
def rancher_desktop():
    brackets = stroke("M15 20H19.5V27", INK, 3.6) + stroke("M49 20H44.5V27", INK, 3.6)
    screen = stroke("M23 36V25.5A3 3 0 0 1 26 22.5H38A3 3 0 0 1 41 25.5V36", INK, 3.6)
    base = line(17, 40.5, 47, 40.5, INK, 3.8)
    return brackets + screen + base


def _sd(x, y, fill, contacts):
    card = path(f"M{x} {y + 2.5}A2.5 2.5 0 0 1 {x + 2.5} {y}H{x + 13}L{x + 18} {y + 5}"
                f"V{y + 22.5}A2.5 2.5 0 0 1 {x + 15.5} {y + 25}H{x + 2.5}A2.5 2.5 0 0 1 {x} {y + 22.5}Z", fill)
    pins = "".join(rrect(x + 2.5 + 3 * k, y + 2.5, 1.8, 5, .6, contacts) for k in range(4))
    return card + pins


@reg("rapid-photo-downloader", RED_DEEP)
def rapid_photo():
    back = _sd(29, 12, RED_SOFT, HOLE)
    front = _sd(16, 22, INK, HOLE) + rrect(19.5, 33, 11, 9, 1.5, HOLE)
    return back + front


@reg("rapidsvn", GREY_DARK)
def rapidsvn():
    face = circle(CX, CY, 16.5, INK)
    patch = path("M16.5 25C18 18.5 23 14.5 29.5 13.8C26.5 18 26 23 28 28"
                 "C24 30 18.5 29.5 16.5 25Z", HOLE)
    strap = stroke("M27 19.5L47 23", HOLE, 2.4)
    eye = circle(40, 28, 2.6, HOLE)
    mouth = path("M27.5 37C31.5 34.5 37 35 40 38.5C37 42.5 31 43.5 27.5 40.5Z", HOLE)
    return face + patch + strap + eye + mouth


@reg("rare", CYAN_DEEP)
def rare():
    loops = ring_b(23, 30, 8.8, INK, 5) + ring_b(41, 30, 8.8, INK, 5)
    plus = line(19.5, 30, 26.5, 30, INK, 2.8) + line(23, 26.5, 23, 33.5, INK, 2.8)
    minus = line(37.5, 30, 44.5, 30, INK, 2.8) + line(41, 26.5, 41, 33.5, INK, 2.8)
    return loops + plus + minus


@reg("raven-reader", TEAL_LIGHT)
def raven_reader():
    bird = path("M15 25C18 20.5 22.5 19 27 19.5C31 15 39 15 43.5 20.5"
                "C48 26.5 46.5 36 49.5 46C43 42.5 36.5 41 32.5 36.5"
                "C29 32.5 29 28.5 26.5 26.5C23 25 19 25 15 25Z", INK)
    return bird + circle(34, 23, 2, HOLE)


@reg("rawtherapee", BLUE_GREY_DARK)
def rawtherapee():
    cols = [RED, ORANGE, YELLOW, GREY, LIGHT_BLUE, PURPLE]
    out = ""
    for k, c in enumerate(cols):
        a0 = -90 + 60 * k
        out += (f'<path d="{arc(CX, CY, 12, a0, a0 + 60)}" fill="none" stroke="{c}" '
                f'stroke-width="9"/>')
    return out


@reg("razercommander", LIGHT_BLUE_DEEP)
def razercommander():
    mid = stroke("M32 46C28 40.5 36 36 32 30C28 24 36 19.5 32 14", INK, 3.6)
    left = stroke("M28.5 44C21.5 40.5 26 34.5 21 30.5C17 27.5 20.5 21.5 17 17", INK, 3.6)
    right = stroke("M35.5 44C42.5 40.5 38 34.5 43 30.5C47 27.5 43.5 21.5 47 17", INK, 3.6)
    heads = circle(32, 14, 3, INK) + circle(17, 17, 3, INK) + circle(47, 17, 3, INK)
    return mid + left + right + heads


@reg("rclone-browser", BLUE_DEEP)
def rclone_browser():
    out = ""
    for k, c in enumerate([INK, BLUE_SOFT, INK]):
        a = -90 + 120 * k
        cx, cy = pt(CX, 31, 7, a)
        out += stroke(arc(cx, cy, 7.5, a - 120 + 360, a + 120 + 360), c, 5)
    return out


def _cloud(fill):
    return path("M20 45C15 45 12.5 41.5 12.5 37.5C12.5 33.5 15.5 30.5 19 30.5"
                "C19 22.5 24.5 15 32 15C39.5 15 45 21 45 29.5C49 30 51.5 33.5 51.5 37.5"
                "C51.5 41.5 48.5 45 44 45Z", fill)


@reg("rclonetray", BLUE_DARK)
def rclonetray():
    r = stroke("M27 41V23H33.5C37 23 39 25 39 28C39 31 37 33 33.5 33H27M33 33L39 41", HOLE, 4)
    return _cloud(INK) + r


def _slab(y, top, side, gap):
    shape = poly([(15, y), (32, y - 7.5), (49, y), (49, y + 4.5), (32, y + 12), (15, y + 4.5)], side, 2)
    face = poly([(15, y), (32, y - 7.5), (49, y), (32, y + 7.5)], top, 2)
    return (poly([(15, y), (32, y - 7.5), (49, y), (49, y + 4.5), (32, y + 12), (15, y + 4.5)], gap, 5)
            + shape + face)


@reg("rdm", RED_DEEP)
def rdm():
    out = _slab(35, INK, INK, HOLE) + _slab(28, INK, INK, HOLE) + _slab(21, INK, INK, HOLE)
    star = poly([pt(36, 19.5, 3.4 if k % 2 == 0 else 1.5, -90 + 36 * k) for k in range(10)], HOLE, .8)
    blob = g(ell_b(25.5, 21.5, 4, 2.2, HOLE), "rotate(-8 25.5 21.5)")
    return out + star + blob


@reg("re.fossplant.songrec", LIGHT_BLUE_DEEP)
def songrec():
    disc = cut(cpath(28.5, 32, 14.5) + cpath(28.5, 32, 3.5), INK)
    groove = ring_b(28.5, 32, 8.5, HOLE, 1.6)
    note = (line(42, 15, 42, 36, HOLE, 7) + ell_b(37.5, 37.5, 5.5, 4.4, HOLE)
            + stroke("M42 15C43 19.5 48 20 48 25", HOLE, 7)
            + line(42, 15, 42, 36, INK, 3) + g(ell_b(37.5, 37.5, 4.6, 3.6, INK), "rotate(-20 37.5 37.5)")
            + stroke("M42 15C43 19.5 48 20 48 25", INK, 3))
    return disc + groove + note


@reg("re.sonny.Commit", BLUE_GREY_DEEP)
def commit():
    diamond = g(rrect(17.5, 15.5, 29, 29, 6, INK), "rotate(45 32 30)")
    graph = line(27, 18, 27, 42, HOLE, 2.6)
    dots = circle(27, 21.5, 3, HOLE) + circle(27, 30, 3, HOLE) + circle(27, 38.5, 3, HOLE)
    pencil = (line(44, 16, 34, 31, HOLE, 8) + line(44, 16, 34, 31, INK, 4)
              + poly([(32.3, 29.8), (35.7, 32.2), (31.5, 35)], INK, 1))
    return diamond + graph + dots + pencil


@reg("re.sonny.Junction", AMBER)
def junction():
    sign = stroke("M32 13L48.5 44H15.5Z", INK, 3.4)
    road = line(33.5, 43, 33.5, 23, INK, 3) + arrowhead_c(33.5, 20.5, -90, INK, 3.4)
    branch = stroke("M33.5 34H27", INK, 3) + arrowhead_c(24.5, 34, 180, INK, 3.4)
    return sign + road + branch


@reg("re.sonny.OhMySVG", ORANGE_DEEP)
def ohmysvg():
    sq = rrect(14, 14, 25, 25, 4, INK)
    petals = "".join(g(ell_b(26.5, 21.5, 2.2, 4, HOLE), f"rotate({45 * k} 26.5 26.5)") for k in range(8))
    clamp = (stroke("M44 13V44H20", INK, 3.4) + line(20, 44, 20, 48, INK, 3)
             + line(40, 44, 40, 48, INK, 3) + line(44, 16, 49.5, 16, INK, 3))
    return sq + petals + circle(26.5, 26.5, 2.2, INK) + clamp


@reg("re.sonny.Tangram", DEEP_PURPLE_DEEP)
def tangram():
    u, x0, y0 = 8, 16, 14
    pieces = [[(0, 0), (4, 0), (2, 2)], [(0, 0), (2, 2), (0, 4)], [(4, 0), (4, 2), (3, 1)],
              [(2, 2), (3, 1), (4, 2), (3, 3)], [(4, 2), (4, 4), (2, 4)],
              [(0, 4), (1, 3), (3, 3), (2, 4)], [(1, 3), (2, 2), (3, 3)]]
    fills = [INK, PINK_SOFT, INK, AMBER_SOFT, INK, INK, AMBER]
    return "".join(poly([(x0 + u * a, y0 + u * b) for a, b in p], c)
                   + path("M" + "L".join(f"{f(x0 + u * a)} {f(y0 + u * b)}" for a, b in p) + "Z",
                          "none", f' stroke="{HOLE}" stroke-width="1.8" stroke-linejoin="round"')
                   for p, c in zip(pieces, fills))


@reg("reactotron", DEEP_ORANGE_DEEP)
def reactotron():
    petals = g(ell_b(32, 30, 7, 18, INK), "rotate(35 32 30)") + g(ell_b(32, 30, 7, 18, INK), "rotate(-35 32 30)")
    hexa = poly([pt(CX, CY, 9.5, 30 + 60 * k) for k in range(6)], HOLE, 1.5)
    hexb = poly([pt(CX, CY, 7.2, 30 + 60 * k) for k in range(6)], INK, 1.5)
    return petals + hexa + hexb + circle(CX, CY, 3, HOLE)


@reg("realtimesync", RED_DEEP)
def realtimesync():
    a = stroke(arc(CX, CY, 13, 200, 320), INK, 4.6) + arrowhead_c(*pt(CX, CY, 13, 335), 65, INK, 4.4)
    b = stroke(arc(CX, CY, 13, 20, 140), INK, 4.6) + arrowhead_c(*pt(CX, CY, 13, 155), 245, INK, 4.4)
    return a + b


@reg("recipes", BROWN_LIGHT)
def recipes():
    blade = path("M24 13C31 15.5 34.5 22 33.5 32H23Z", INK,
                 f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    handle = rrect(23, 32, 8, 15, 3, BROWN_DARK) + circle(27, 36.5, 1.3, INK) + circle(27, 42.5, 1.3, INK)
    tomato = circle(40, 38, 8.5, RED) + poly([(35.5, 30.5), (40, 32.5), (44.5, 30.5), (40, 28)], BLUE_GREY_LIGHT, 1.5)
    return blade + handle + tomato


@reg("recoll", INDIGO_SOFT)
def recoll():
    out = ""
    for r in range(4):
        for c in range(4):
            if (r + c) % 2 == 0:
                col = INDIGO_LIGHT if (r, c) == (2, 0) else INK
                out += rrect(15 + 8.5 * c, 13 + 8.5 * r, 8.5, 8.5, 1, col)
    return out


@reg("recstudio", YELLOW_DARK)
def recstudio():
    board = rrect(15, 12, 27, 34, 4, INK)
    bits = ""
    for r, row in enumerate(["101", "010", "110"]):
        for c, b in enumerate(row):
            x, y = 20.5 + 6.5 * c, 18 + 7.5 * r
            bits += (rrect(x - 1.1, y - 2.8, 2.2, 5.6, 1.1, HOLE) if b == "1"
                     else ell_b(x, y, 2.2, 2.8, "none", f' stroke="{HOLE}" stroke-width="1.6"'))
    badge = circle(41.5, 40, 10, HOLE) + circle(41.5, 40, 8.5, YELLOW_SOFT)
    c = stroke(arc(41.5, 40, 4, 45, 315), YELLOW_DARK, 3)
    return board + bits + badge + c


@reg("reddit", DEEP_ORANGE)
def reddit():
    ears = circle(18, 28, 4, INK) + circle(46, 28, 4, INK)
    ant = stroke("M32 24L34.5 15L41.5 16.5", INK, 2.4) + circle(43.5, 16.5, 3.2, INK)
    head = ell_b(32, 34, 15, 10.5, INK, f' stroke="{HOLE}" stroke-width="1.6"')
    eyes = circle(26.5, 32.5, 2.8, HOLE) + circle(37.5, 32.5, 2.8, HOLE)
    smile = stroke("M26 38.5Q32 42 38 38.5", HOLE, 2.2)
    return ears + ant + head + eyes + smile


@reg("redeclipse", RED_DEEP)
def redeclipse():
    rays = poly([pt(28.5, 26.5, 16 if k % 2 == 0 else 11.5, -90 + 15 * k) for k in range(24)], INK, 1)
    moon = circle(35, 33.5, 14, HOLE) + circle(35, 33.5, 12.3, BLUE_GREY_DARK)
    return rays + moon


@reg("redirection", RED_DARK)
def redirection():
    frame = rrect(15, 13, 34, 28, 4.5, INK) + rrect(19.5, 17.5, 25, 19, 2, HOLE)
    eyes = rrect(25.5, 22.5, 4, 8, 1, INK) + rrect(34.5, 22.5, 4, 8, 1, INK)
    stand = rrect(25, 43.5, 14, 3.6, 1.8, INK)
    return frame + eyes + stand


@reg("redisinsight", RED_DARK)
def redisinsight():
    return (_slab(36, RED_SOFT, INK, HOLE) + _slab(28, RED_SOFT, INK, HOLE)
            + _slab(20, RED_SOFT, INK, HOLE))


@reg("reditr", BLUE_DARK)
def reditr():
    rot = "rotate(-20 32 30)"
    back = g(stroke("M13 30A19 6 0 0 1 51 30", INK, 2.8), rot)
    planet = circle(CX, CY, 11.5, INK)
    front = g(stroke("M13 30A19 6 0 0 0 51 30", HOLE, 6.5) + stroke("M13 30A19 6 0 0 0 51 30", INK, 2.8), rot)
    return back + planet + front


@reg("rednotebook", RED_DEEP)
def rednotebook():
    book = rrect(17, 12, 30, 36, 4, INK)
    spine = line(23, 12, 23, 48, HOLE, 2.2)
    mark = poly([(36, 12), (42, 12), (42, 27), (39, 24), (36, 27)], HOLE, 1)
    return book + spine + mark


@reg("redream", BLUE_DEEP)
def redream():
    a = path("M18 34C16 24 23 15 33 14.5L32 11L41 17.5L33 24L33.5 20C27 20.5 22.5 26 24 34Z", INK,
             f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    b = g(path("M18 34C16 24 23 15 33 14.5L32 11L41 17.5L33 24L33.5 20C27 20.5 22.5 26 24 34Z", BLUE_SOFT,
               f' stroke="{BLUE_SOFT}" stroke-width="2" stroke-linejoin="round"'), "rotate(180 32 30)")
    return a + b


@reg("redriver2", RED_DEEP)
def redriver2():
    w = 3.4
    txt = (stroke("M19 27V15H25C28 15 29.5 16.5 29.5 18.5C29.5 20.5 28 22 25 22H19M24.5 22L29.5 27", INK, w)
           + stroke("M44 15H33.5V27H44M33.5 21H42", INK, w)
           + stroke("M19 32V44H23.5C27.5 44 30 41.5 30 38C30 34.5 27.5 32 23.5 32Z", INK, w)
           + stroke("M33.5 35C33.5 33 35.5 32 38.5 32C41.5 32 43.5 33.3 43.5 35.5C43.5 38 40.5 40 33.5 44H44.5", INK, w))
    return g(txt, "translate(32 30) skewX(-10) translate(-32 -30)")


@reg("redshift", RED_DEEP)
def redshift():
    bulb = path("M32 11A12.5 12.5 0 0 1 44.5 23.5C44.5 30 38.5 33 37.5 38H26.5"
                "C25.5 33 19.5 30 19.5 23.5A12.5 12.5 0 0 1 32 11Z", INK)
    base = rrect(26, 40, 12, 3, 1.5, INK) + rrect(27, 44.5, 10, 3, 1.5, INK)
    return bulb + base


@reg("referencer", TEAL_DEEP)
def referencer():
    book = rrect(17, 12, 30, 36, 4, INK) + line(22.5, 12, 22.5, 48, HOLE, 2.2)
    globe = (ring_b(35, 30, 8, HOLE, 2.4) + ell_b(35, 30, 3.4, 8, "none", f' stroke="{HOLE}" stroke-width="2"')
             + line(27, 30, 43, 30, HOLE, 2))
    return book + globe


@reg("regedit", CYAN_DEEP)
def regedit():
    cells = "".join(rrect(14 + 9 * c, 12 + 9 * r, 7.5, 7.5, 1.5, INK)
                    for r in range(3) for c in range(3) if (r, c) != (2, 2))
    badge = circle(40, 39, 10.5, HOLE) + circle(40, 39, 9, LIGHT_BLUE_DARK)
    win = "".join(rrect(x, y, 4.3, 4.3, .8, INK) for x in (35.4, 40.3) for y in (34.4, 39.3))
    return cells + badge + win


@reg("regexxer", BROWN_LIGHT)
def regexxer():
    folder = path("M14 18A3 3 0 0 1 17 15H26L29.5 19H47A3 3 0 0 1 50 22V43A3 3 0 0 1 47 46H17"
                  "A3 3 0 0 1 14 43Z", INK)
    lens = ring_b(30, 29.5, 6.5, HOLE, 3.2) + line(34.8, 34.3, 40, 39.5, HOLE, 3.6)
    return folder + lens


@reg("reicast", INDIGO)
def reicast():
    pts = []
    for i in range(0, 81):
        t = i / 80 * 4 * math.pi
        r = 2.5 + 12 * t / (4 * math.pi)
        pts.append(pt(32, 30, r, math.degrees(t) + 90))
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts)
    return stroke(d, INK, 4)


@reg("reigns", BLUE_GREY_DARK)
def reigns():
    crown = poly([(21, 25), (21, 16), (26.5, 21), (32, 15), (37.5, 21), (43, 16), (43, 25)], AMBER, 2)
    jewels = circle(21, 14.5, 2.4, AMBER) + circle(32, 13, 2.4, AMBER) + circle(43, 14.5, 2.4, AMBER)
    body = path("M21 27H43V42L32 48L21 42Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    eyes = rrect(25.5, 31, 3, 5.5, 1, HOLE) + rrect(35.5, 31, 3, 5.5, 1, HOLE)
    return crown + jewels + body + eyes


@reg("remarkable", LIGHT_BLUE_DEEP)
def remarkable():
    r = stroke("M26 43V17H34.5C39.5 17 42 20 42 23.5C42 27.5 39 30 34.5 30H26M33 30L42.5 43", INK, 5)
    return ring_b(CX, CY, 17, INK, 2.2) + g(r, "translate(-1 0)")


@reg("rememberthemilk", BLUE_DEEP)
def rememberthemilk():
    ears = g(ell_b(17.5, 24, 5, 2.8, INK), "rotate(-20 17.5 24)") + g(ell_b(46.5, 24, 5, 2.8, INK), "rotate(20 46.5 24)")
    tuft = circle(26.5, 16.5, 4.2, INK) + circle(32, 14.5, 4.2, INK) + circle(37.5, 16.5, 4.2, INK)
    head = rrect(21, 16, 22, 32, 10, INK)
    eyes = circle(27, 27, 2.2, HOLE) + circle(37, 27, 2.2, HOLE)
    muzzle = stroke("M22.5 35.5H41.5", HOLE, 2) + circle(28, 41, 1.9, HOLE) + circle(36, 41, 1.9, HOLE)
    return ears + tuft + head + eyes + muzzle


@reg("remmina", BLUE_DEEP)
def remmina():
    rim = stroke(arc(CX, CY, 16.5, 200, 340), INK, 3) + stroke(arc(CX, CY, 16.5, 20, 160), LIGHT_BLUE_LIGHT, 3)
    a = stroke("M21 20L28.5 25.5L21 31", INK, 4.4)
    b = stroke("M43 29L35.5 34.5L43 40", BLUE_SOFT, 4.4)
    return rim + a + b


@reg("remnote", INDIGO)
def remnote():
    rays = "".join(line(32, 32, *pt(32, 32, 15, a), INK, 6) for a in (180, -135, -90, -45, 0))
    base = poly([(24, 45), (32, 36), (40, 45)], DEEP_PURPLE_SOFT, 2)
    return rays + base


@reg("renderdoc", DEEP_PURPLE_LIGHT)
def renderdoc():
    head = ring_b(32, 23, 7, INK, 4.4)
    shoulders = stroke("M15 44C20 36 26 34 32 34C38 34 44 36 49 44", INK, 4.4)
    return head + shoulders


@reg("renoise", DEEP_ORANGE_DEEP)
def renoise():
    tag = g(rrect(18, 15, 28, 31, 4, INK), "rotate(-25 32 30.5)")
    r = stroke("M27.5 40V21H34C37.5 21 39.5 23 39.5 26C39.5 29 37.5 31 34 31H27.5M33.5 31L39.5 40", HOLE, 4.4)
    return tag + g(r, "rotate(-25 32 30.5) translate(-1 0)")


def _renpy_face(hat):
    face = circle(32, 34, 11.5, INK)
    hair = path("M19.5 38C18 27 23 20 32 20C41 20 46 27 44.5 38C43 33 41.5 30 40 29"
                "C37 31 30 31 26 28C24.5 31 22 34 19.5 38Z", RED_SOFT)
    eyes = ell_b(27.5, 36, 2, 2.6, INDIGO_DEEP) + ell_b(36.5, 36, 2, 2.6, INDIGO_DEEP)
    out = face + hair + eyes
    if hat:
        out += ell_b(32, 22.5, 18, 4, AMBER_SOFT) + path("M24 22.5C24 16.5 27.5 13 32 13C36.5 13 40 16.5 40 22.5Z", AMBER_SOFT)
        out += stroke("M24.5 21.5H39.5", AMBER_DEEP, 2.2)
    return out


@reg("renpy", LIGHT_BLUE_LIGHT)
def renpy():
    return _renpy_face(True)


@reg("renpy-demo", BLUE_LIGHT)
def renpy_demo():
    return _renpy_face(False)


@reg("repl.it", BLUE_GREY_DARK)
def replit():
    blades = "".join(g(stroke("M32 14.5C41 14.5 47.5 21.5 47.5 30C43 24.5 37 22.5 32 24", INK, 4.4),
                       f"rotate({120 * k} 32 30)") for k in range(3))
    return blades + circle(CX, CY, 4.5, INK)


@reg("rescuetime", BLUE_GREY)
def rescuetime():
    cross = rrect(24.5, 12.5, 15, 36, 4, INK) + rrect(14, 23, 36, 15, 4, INK)
    hands = line(32, 30.5, 32, 17, HOLE, 2.6) + line(32, 30.5, 45, 30.5, HOLE, 2.6)
    return cross + hands + circle(32, 30.5, 5.5, RED)


@reg("resharper", PINK_DEEP)
def resharper():
    sq = rrect(15, 13, 34, 34, 4, INK)
    r = stroke("M20.5 33V19H25.5C28.5 19 30 20.7 30 23C30 25.3 28.5 27 25.5 27H20.5M25 27L30 33", HOLE, 2.8)
    h = (line(35, 22, 44, 22, HOLE, 2.4) + line(35, 28.5, 44, 28.5, HOLE, 2.4)
         + line(37.5, 19, 36.5, 32, HOLE, 2.4) + line(42.5, 19, 41.5, 32, HOLE, 2.4))
    bar = rrect(20.5, 38.5, 13, 3.2, 1.6, HOLE)
    return sq + r + h + bar


@small("radiotray")
def radiotray_s():
    return (rrect(13, 16, 38, 29, 5, INK) + circle(24.5, 30.5, 7.5, HOLE)
            + rrect(35, 21, 11, 4, 2, HOLE) + rrect(35, 29, 11, 4, 2, HOLE) + rrect(35, 37, 11, 4, 2, HOLE))


@small("rakarrack")
def rakarrack_s():
    return (line(30, 32, 45, 16, INK, 5) + circle(24, 39, 10.5, INK) + circle(31, 32, 8, INK)
            + circle(27, 35.5, 3.5, HOLE))


@small("rambox")
def rambox_s():
    return (stroke("M19 43V26A13 13 0 0 1 45 26V43", INK, 5)
            + stroke("M28 43V28A4 4 0 0 1 36 28V43", INK, 5))


@small("rancher-desktop")
def rancher_desktop_s():
    return (stroke("M22 36V24H42V36", INK, 5) + line(16, 41.5, 48, 41.5, INK, 5)
            + stroke("M14 18H19V24", INK, 4.4) + stroke("M50 18H45V24", INK, 4.4))


@small("rapid-photo-downloader")
def rapid_photo_s():
    back = path("M30 11H44L50 17V36H30Z", RED_SOFT, f' stroke="{RED_SOFT}" stroke-width="3" stroke-linejoin="round"')
    front = path("M15 21H29L35 27V47H15Z", INK, f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return back + front + rrect(18, 33, 13, 10, 2, HOLE)


@small("rapidsvn")
def rapidsvn_s():
    return (circle(CX, CY, 17, INK) + path("M15.5 26C17 18 23 13.5 30.5 13C27 18 27 24 29 29C23.5 31 17.5 30 15.5 26Z", HOLE)
            + circle(40.5, 27, 3.2, HOLE) + path("M27 37C31.5 34.5 37.5 35 41 39C37 44 30 44.5 27 41Z", HOLE))


@small("rare")
def rare_s():
    return ring_b(23, 30, 8.8, INK, 6) + ring_b(41, 30, 8.8, INK, 6)


@small("rclonetray")
def rclonetray_s():
    return _cloud(INK) + stroke("M28 41V24H33.5C37 24 39 26 39 29C39 32 37 34 33.5 34H28M34 34L39.5 41", HOLE, 5)


@small("rdm")
def rdm_s():
    return (_slab(36, INK, INK, HOLE) + _slab(22, INK, INK, HOLE)
            + poly([pt(33, 21.5, 4.5 if k % 2 == 0 else 2, -90 + 36 * k) for k in range(10)], HOLE, 1))


@small("re.fossplant.songrec")
def songrec_s():
    disc = cut(cpath(28, 32, 15) + cpath(28, 32, 4.5), INK)
    note = (line(43, 13, 43, 36, HOLE, 9) + ell_b(38, 38, 7, 6, HOLE)
            + line(43, 13, 43, 36, INK, 4) + ell_b(38, 38, 5, 4, INK))
    return disc + note


@small("re.sonny.Commit")
def commit_s():
    return (g(rrect(17, 15, 30, 30, 6, INK), "rotate(45 32 30)") + line(28, 17, 28, 43, HOLE, 3.5)
            + circle(28, 22, 4, HOLE) + circle(28, 38, 4, HOLE))


@small("re.sonny.Junction")
def junction_s():
    return (path("M32 12L50 45H14Z", INK, f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
            + line(33, 42, 33, 26, HOLE, 4) + arrowhead_c(33, 22, -90, HOLE, 4) + line(33, 35, 26, 35, HOLE, 4))


@small("re.sonny.OhMySVG")
def ohmysvg_s():
    return (rrect(13, 13, 27, 27, 4, INK) + circle(26.5, 26.5, 6, HOLE) + circle(26.5, 26.5, 2.5, INK)
            + stroke("M45 12V45H19", INK, 5))


@small("re.sonny.Tangram")
def tangram_s():
    return (poly([(16, 14), (48, 14), (32, 30)], INK) + poly([(16, 14), (32, 30), (16, 46)], PINK_SOFT)
            + poly([(48, 30), (48, 46), (32, 46)], INK) + stroke("M16 14L32 30M32 30L16 46M48 14L32 30", HOLE, 2.5)
            + poly([(32, 30), (40, 22), (48, 30), (40, 38)], AMBER_SOFT))


@small("reactotron")
def reactotron_s():
    petals = g(ell_b(32, 30, 7.5, 18, INK), "rotate(35 32 30)") + g(ell_b(32, 30, 7.5, 18, INK), "rotate(-35 32 30)")
    return petals + circle(CX, CY, 9, HOLE) + circle(CX, CY, 6.5, INK)


@small("recipes")
def recipes_s():
    blade = path("M22 12C31 15 35 22 34 33H22Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return blade + rrect(22, 33, 9, 14, 3, BROWN_DARK) + circle(41, 38, 9.5, RED)


@small("recoll")
def recoll_s():
    return "".join(rrect(15 + 11 * c, 13 + 11 * r, 11, 11, 1.5, INDIGO_LIGHT if (r, c) == (2, 0) else INK)
                   for r in range(3) for c in range(3) if (r + c) % 2 == 0)


@small("recstudio")
def recstudio_s():
    board = rrect(14, 12, 28, 34, 4, INK) + rrect(19, 17, 3.5, 9, 1.7, HOLE) + ring_b(29, 21.5, 3.2, HOLE, 3)
    return board + circle(41.5, 40, 11, HOLE) + circle(41.5, 40, 9.5, YELLOW_SOFT) + stroke(arc(41.5, 40, 4.2, 45, 315), YELLOW_DARK, 3.6)


@small("reddit")
def reddit_s():
    ant = circle(42, 16, 4, INK) + stroke("M32 24L34 16L40 16", INK, 3)
    head = ell_b(32, 34, 16, 11.5, INK) + circle(17, 27, 4.5, INK) + circle(47, 27, 4.5, INK)
    return ant + head + circle(26, 32.5, 3.5, HOLE) + circle(38, 32.5, 3.5, HOLE)


@small("redeclipse")
def redeclipse_s():
    rays = poly([pt(28, 26, 17 if k % 2 == 0 else 12, -90 + 20 * k) for k in range(18)], INK, 1)
    return rays + circle(36, 34, 14.5, HOLE) + circle(36, 34, 12.5, BLUE_GREY_DARK)


@small("redirection")
def redirection_s():
    return (rrect(14, 12, 36, 30, 5, INK) + rrect(19.5, 17.5, 25, 19, 2, HOLE)
            + rrect(25, 22, 5, 10, 1, INK) + rrect(34, 22, 5, 10, 1, INK) + rrect(24, 44, 16, 4, 2, INK))


@small("redisinsight")
def redisinsight_s():
    return _slab(36, RED_SOFT, INK, HOLE) + _slab(22, RED_SOFT, INK, HOLE)


@small("reditr")
def reditr_s():
    rot = "rotate(-20 32 30)"
    return (circle(CX, CY, 12, INK)
            + g(stroke("M12 30A20 6.5 0 0 0 52 30", HOLE, 8) + stroke("M12 30A20 6.5 0 0 0 52 30", INK, 4), rot))


@small("rednotebook")
def rednotebook_s():
    return (rrect(16, 11, 32, 38, 4, INK) + line(23, 11, 23, 49, HOLE, 3.5)
            + poly([(34, 11), (42, 11), (42, 29), (38, 25), (34, 29)], HOLE, 1))


@small("redriver2")
def redriver2_s():
    txt = (stroke("M17 43V17H26C30.5 17 32.5 19.5 32.5 23C32.5 26.5 30.5 29 26 29H17M25.5 29L32.5 43", INK, 5)
           + stroke("M36 22C36 18.5 38.5 17 42 17C45.5 17 48 19 48 22.5C48 26.5 44 30 36 43H49", INK, 5))
    return g(txt, "translate(32 30) skewX(-10) translate(-32 -30)")


@small("referencer")
def referencer_s():
    return (rrect(16, 11, 32, 38, 4, INK) + line(22.5, 11, 22.5, 49, HOLE, 3)
            + ring_b(35.5, 30, 8.5, HOLE, 3.4) + line(27, 30, 44, 30, HOLE, 3))


@small("regedit")
def regedit_s():
    cells = "".join(rrect(13 + 12 * c, 11 + 12 * r, 10, 10, 2, INK)
                    for r in range(2) for c in range(2))
    badge = circle(41, 40, 11.5, HOLE) + circle(41, 40, 10, LIGHT_BLUE_DARK)
    win = "".join(rrect(x, y, 5.5, 5.5, 1, INK) for x in (35, 41.5) for y in (34, 40.5))
    return cells + badge + win


@small("regexxer")
def regexxer_s():
    folder = path("M13 18A3 3 0 0 1 16 15H26L29.5 19H48A3 3 0 0 1 51 22V43A3 3 0 0 1 48 46H16"
                  "A3 3 0 0 1 13 43Z", INK)
    return folder + ring_b(30, 29.5, 7, HOLE, 4.4) + line(35, 34.5, 41, 40.5, HOLE, 5)


@small("reicast")
def reicast_s():
    pts = []
    for i in range(0, 61):
        t = i / 60 * 3.2 * math.pi
        r = 3 + 12.5 * t / (3.2 * math.pi)
        pts.append(pt(32, 30, r, math.degrees(t) + 90))
    return stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts), INK, 5.5)


@small("reigns")
def reigns_s():
    crown = poly([(20, 26), (20, 14), (26, 20), (32, 13), (38, 20), (44, 14), (44, 26)], AMBER, 2)
    body = path("M20 28H44V42L32 48L20 42Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return crown + body + rrect(25, 32, 4, 7, 1, HOLE) + rrect(35, 32, 4, 7, 1, HOLE)


@small("remarkable")
def remarkable_s():
    return stroke("M24 45V15H34C40 15 43 18.5 43 23C43 27.5 40 31 34 31H24M33 31L43.5 45", INK, 6.5)


@small("rememberthemilk")
def rememberthemilk_s():
    ears = g(ell_b(16.5, 23, 5.5, 3.5, INK), "rotate(-20 16.5 23)") + g(ell_b(47.5, 23, 5.5, 3.5, INK), "rotate(20 47.5 23)")
    head = rrect(20, 14, 24, 34, 11, INK)
    return ears + head + circle(26.5, 26, 3, HOLE) + circle(37.5, 26, 3, HOLE) + rrect(24, 37, 16, 3.2, 1.6, HOLE)


@small("remmina")
def remmina_s():
    return (stroke("M18 18L28 25L18 32", INK, 6) + stroke("M46 28L36 35L46 42", BLUE_SOFT, 6))


@small("remnote")
def remnote_s():
    rays = "".join(line(32, 33, *pt(32, 33, 15, a), INK, 7.5) for a in (180, -135, -90, -45, 0))
    return rays + poly([(23, 46), (32, 37), (41, 46)], DEEP_PURPLE_SOFT, 2)


@small("renoise")
def renoise_s():
    tag = g(rrect(17, 14, 30, 33, 5, INK), "rotate(-25 32 30.5)")
    r = stroke("M27 41V20H34C38 20 40 22.5 40 26C40 29.5 38 32 34 32H27M33.5 32L40 41", HOLE, 5.5)
    return tag + g(r, "rotate(-25 32 30.5) translate(-1 0)")


def _renpy_small(hat):
    out = circle(32, 34, 13, INK) + path("M18.5 36C17 26 23 19 32 19C41 19 47 26 45.5 36C42 31 38 29 32 29C26 29 22 31 18.5 36Z", RED_SOFT)
    out += ell_b(27, 37, 2.6, 3.4, INDIGO_DEEP) + ell_b(37, 37, 2.6, 3.4, INDIGO_DEEP)
    if hat:
        out += ell_b(32, 21, 19, 4.5, AMBER_SOFT) + path("M23.5 21C23.5 15 27.5 11 32 11C36.5 11 40.5 15 40.5 21Z", AMBER_SOFT)
    return out


@small("renpy")
def renpy_s():
    return _renpy_small(True)


@small("renpy-demo")
def renpy_demo_s():
    return _renpy_small(False)


@small("repl.it")
def replit_s():
    blades = "".join(g(stroke("M32 13C41.5 13 48.5 20.5 48.5 30C43.5 24.5 37.5 22.5 32 24", INK, 6),
                       f"rotate({120 * k} 32 30)") for k in range(3))
    return blades


@small("rescuetime")
def rescuetime_s():
    cross = rrect(24, 11, 16, 38, 4, INK) + rrect(13, 22.5, 38, 16, 4, INK)
    return cross + line(32, 30.5, 32, 16, HOLE, 3.5) + circle(32, 30.5, 7, RED)


@small("resharper")
def resharper_s():
    sq = rrect(13, 11, 38, 38, 5, INK)
    r = stroke("M20 37V17H27C31 17 33 19.5 33 22.5C33 25.5 31 28 27 28H20M26.5 28L33 37", HOLE, 4.4)
    h = line(37, 22, 46, 22, HOLE, 3.4) + line(37, 30, 46, 30, HOLE, 3.4) + line(40, 17, 40, 36, HOLE, 3.4) + line(44, 17, 44, 36, HOLE, 3.4)
    return sq + r + h
