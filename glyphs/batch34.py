# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 34: horizon-chase-turbo to igdm."""
import math
from lm import (
    AMBER, AMBER_DARK, AMBER_LIGHT, BLUE, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    circle, cut, CX, CY, CYAN_DEEP, CYAN_SOFT, DEEP_ORANGE, DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP,
    DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_DARK, DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT, f, g,
    GREY_DARK, GREY_DEEP, GREY_LIGHT, HOLE, INDIGO, INDIGO_DARK, INDIGO_DEEP, INDIGO_SOFT, INK,
    LIGHT_BLUE, LIGHT_BLUE_DEEP, LIGHT_BLUE_SOFT, line, ORANGE_DARK, ORANGE_DEEP, path, PINK,
    poly, pt, PURPLE, PURPLE_SOFT, RED_DEEP, RED_LIGHT, rrect, stroke, TEAL, TEAL_LIGHT,
)
from glyphs.kit import arc_f, ell_d, registry, _ring, sector_b

ICONS, SMALL, reg, small = registry()


def pl(pts):
    return "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts)


@reg("horizon-chase-turbo", BLUE_GREY_DARK)
def horizon_chase():
    h = (stroke("M24 14L19 36", INK, 5.5) + stroke("M44 14L39 36", INK, 5.5)
         + stroke("M19.5 25H43", RED_LIGHT, 4.5))
    swoosh = stroke("M16 44C25 39.5 37 38.5 48 41", AMBER, 4)
    return h + swoosh


@reg("horizon-client", CYAN_DEEP)
def horizon_client():
    cloud = path("M20 44C15 44 13 40 13.3 37C13.7 33.5 16.5 31 20 31.2"
                 "C20.5 25 25.5 21 31.5 21C37.5 21 42 25 43 30.5"
                 "C47.5 31 50.5 34.5 50.5 38C50.5 41.5 48 44 44 44Z", CYAN_SOFT)
    sun = circle(35, 25, 10.5, INK, f' stroke="{HOLE}" stroke-width="2"')
    return cloud + sun


@reg("hotspot", DEEP_ORANGE_DEEP)
def hotspot():
    flame = path("M33 10C27 17 24.5 22 25.5 27C22 25 21 22 22 18.5C17 23.5 15.5 30 16 36"
                 "C17 43.5 23.5 48.5 32 48.5C41 48.5 48 42 48 34C48 25.5 41 20 36.5 16.5"
                 "C36.5 20.5 38 24 37 27.5C35 22.5 32.5 17 33 10Z", INK)
    return flame + circle(31, 37.5, 8, AMBER_LIGHT)


@reg("houdini", DEEP_ORANGE)
def houdini():
    pts = []
    for i in range(0, 121):
        t = i / 120
        a = math.radians(-90 + t * 2.3 * 360)
        r = 2.2 + t * 14.2
        pts.append((32 + r * math.cos(a), 30.5 + r * math.sin(a)))
    return stroke(pl(pts), INK, 4.2)


@reg("hp-logo", LIGHT_BLUE_DEEP)
def hp_logo():
    letters = (stroke("M25 17V40", HOLE, 4) + stroke("M25 31C25 25 33 25 33 31V40", HOLE, 4)
               + stroke("M37.5 26V45", HOLE, 4) + _ring(41.5, 31.5, 4.3, HOLE, 4))
    return circle(CX, CY, 16.5, INK) + g(letters, "translate(32 30) skewX(-18) translate(-32 -30)")


@reg("htop", BLUE_GREY_DARK)
def htop():
    out = ""
    rows = [(18, [LIGHT_BLUE_SOFT] * 3 + [RED_LIGHT] * 2),
            (30, [LIGHT_BLUE_SOFT] * 4),
            (42, [LIGHT_BLUE_SOFT] * 2 + [AMBER])]
    for y, bars in rows:
        out += stroke(f"M17.5 {y - 4}H15.5V{y + 4}H17.5", INK, 2.4)
        out += stroke(f"M46.5 {y - 4}H48.5V{y + 4}H46.5", INK, 2.4)
        for k, c in enumerate(bars):
            out += rrect(20.5 + k * 4.8, y - 4, 3, 8, 1, c)
    return out


@reg("httrack", DEEP_PURPLE_LIGHT)
def httrack():
    globe = (circle(29, 27, 14, INK) + _ring(29, 27, 6, HOLE, 2.4) + line(15.5, 27, 42.5, 27, HOLE, 2.4)
             + path("M29 13.5C24.5 18 24.5 36 29 40.5C33.5 36 33.5 18 29 13.5Z", "none",
                    f' stroke="{HOLE}" stroke-width="2.4"'))
    badge = circle(41.5, 39.5, 10, HOLE) + circle(41.5, 39.5, 8, DEEP_PURPLE_DARK)
    arrow = stroke("M41.5 34V43.5M37.5 39.8L41.5 43.8L45.5 39.8", INK, 2.6) + line(37, 46, 46, 46, INK, 2.2)
    return g(globe, "translate(-1 0)") + badge + arrow


@reg("hub", INDIGO)
def hub():
    sq = rrect(15.5, 13.5, 33, 33, 3, INK)
    h = stroke("M21 19V32M28 19V32M21 25.5H28", HOLE, 3.4)
    b = stroke("M33 19V32H38.5C43 32 43 25.5 38.5 25.5H33M33 19H37.5C41 19 41 25.5 37.5 25.5", HOLE, 3.4)
    return sq + h + b + rrect(20, 37.5, 13, 3.5, 1.2, HOLE)


def _hubstaff():
    segs = "".join(path(sector_b(CX, CY, 11.6, 17.5, a0, a1), INK,
                        f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
                   for a0, a1 in [(-83, 23), (37, 143), (157, 263)])
    return segs + circle(CX, 47.8, 3, HOLE) + circle(CX, CY, 9.2, INK)


for _n, _t in [("hubstaff", BLUE_DEEP), ("hubstaff-color", BLUE), ("hubstaff-black", BLUE_GREY_DARK),
               ("hubstaff-gray", GREY_DEEP), ("hubstaff-green", CYAN_DEEP), ("hubstaff-red", RED_DEEP)]:
    reg(_n, _t)(_hubstaff)


@reg("hulu", CYAN_DEEP)
def hulu():
    w = stroke("M15.5 21V38M15.5 29.5C15.5 24.5 23 24.5 23 29.5V38"
               "M27.5 25V32.5C27.5 38.5 35 38.5 35 32.5V25V38"
               "M39.5 21V38"
               "M43.5 25V32.5C43.5 38.5 51 38.5 51 32.5V25V38", INK, 4)
    return g(w, "translate(32 30) scale(.93) translate(-33.25 -29.5)")


@reg("hw-probe", BLUE_DEEP)
def hw_probe():
    head = circle(30, 31, 14.5, INDIGO_DARK)
    face = ell_d(33, 37.5, 9.5, 7.2, INK)
    eye = circle(36, 25.5, 3, INK) + circle(36.8, 25.8, 1.4, INDIGO_DARK)
    beak = poly([(40.5, 25.5), (50, 23.5), (42, 30)], AMBER, 1.5)
    return g(head + face + eye + beak, "translate(32 30) scale(1.08) translate(-32 -30.5)")


@reg("hwinfo", BLUE)
def hwinfo():
    return circle(32, 16.5, 4, INK) + rrect(28, 23.5, 8, 22, 4, INK)


@reg("hwloc", TEAL)
def hwloc():
    card = rrect(17, 15, 30, 30, 5, INK)
    cells = "".join(rrect(21 + c * 5.5, 19 + r * 5.5, 4.2, 4.2, 1, HOLE) for r in range(2) for c in range(2))
    big = rrect(31.5, 29.5, 11, 11, 2, HOLE)
    return g(card + cells + big, "rotate(-35 32 30)")


@reg("hydrogen", INDIGO_DEEP)
def hydrogen():
    h = stroke("M18.5 14V35M28.5 14V35M18.5 24.5H28.5", INK, 4.4)
    two = stroke("M34 19C34 13 45 13 45 19.5C45 25.5 34 28.5 34 35H45.5", INK, 4.4)
    dots = "".join(circle(19 + k * 6.5, 43.5, 2.3, INK) for k in range(5))
    return h + two + dots


@reg("hyper", PINK)
def hyper():
    box = rrect(14.5, 12.5, 35, 35, 8, INK)
    bolt = poly([(26, 18), (19.5, 29.5), (24.5, 29.5), (21, 39.5), (30.5, 26.5), (25.5, 26.5), (30, 18)], HOLE, 1.2)
    return box + bolt + rrect(31.5, 33, 11, 3.8, 1.9, HOLE)


@reg("hyperspace", DEEP_PURPLE_DEEP)
def hyperspace():
    head = rrect(19, 14.5, 29, 29, 13, INK)
    ear = rrect(13.5, 20.5, 12.5, 19, 6, INK, f' stroke="{HOLE}" stroke-width="2.2"')
    trunk = stroke("M42 31C43 38.5 46.5 40.5 49.5 36", INK, 5)
    eye = stroke("M33.5 25C34.8 23.3 37.2 23.3 38.5 25", HOLE, 2)
    tusk = ell_d(36.5, 42.5, 4.5, 2.6, INK) + ell_d(36.5, 42.5, 4.5, 2.6, "none").replace(
        'fill="none"', f'fill="none" stroke="{HOLE}" stroke-width="1.8"')
    return head + trunk + ear + eye + tusk


@reg("hypnospace-outlaw", DEEP_PURPLE)
def hypnospace():
    oct_ = poly([(26, 11.5), (38, 11.5), (44, 16.5), (44, 23.5), (38, 28.5),
                 (26, 28.5), (20, 23.5), (20, 16.5)], INK, 2)
    inner = poly([(28, 15.5), (36, 15.5), (39.5, 18.5), (39.5, 21.5), (36, 24.5),
                  (28, 24.5), (24.5, 21.5), (24.5, 18.5)], HOLE, 1)
    pill = rrect(28, 18.3, 8, 3.4, 1.7, INK)
    wings = poly([(14.5, 17.5), (19, 17.5), (19, 22)], INK, 1.5) + poly([(49.5, 17.5), (45, 17.5), (45, 22)], INK, 1.5)
    tri = poly([(16.5, 32), (47.5, 32), (32, 48)], INK, 2.5)
    band = line(22, 36.5, 42, 36.5, HOLE, 2.2)
    return oct_ + inner + pill + wings + tri + band


@reg("hypnotix", LIGHT_BLUE)
def hypnotix():
    base = circle(CX, CY, 16.5, INK)
    blades = "".join(g(stroke("M32 19.5C38 20 42 23 43.5 27.5L47.5 25.5", HOLE, 2.2), f"rotate({60 * k} 32 30)")
                     for k in range(6))
    hub = circle(CX, CY, 9.5, HOLE) + circle(CX, CY, 7.8, INK)
    play = poly([(29.5, 26), (36.5, 30), (29.5, 34)], HOLE, 1.8)
    return base + blades + hub + play


@reg("i-nex", ORANGE_DARK)
def i_nex():
    return (rrect(16, 13, 32, 34, 5, INK) + circle(32, 20.5, 3, HOLE)
            + rrect(29, 26, 6, 15.5, 2, HOLE))


@reg("i2pd", ORANGE_DEEP)
def i2pd():
    shield = path("M17 15C23 15 28 13.5 32 11C36 13.5 41 15 47 15V28C47 37.5 40.5 44.5 32 48"
                  "C23.5 44.5 17 37.5 17 28Z", INK)
    left = path("M32 15.8C29 17.5 25.5 18.5 21.5 18.8V28C21.5 35.2 26 40.5 32 43.4Z", HOLE)
    return shield + left


@reg("iaito-o", GREY_DARK)
def iaito():
    return (stroke(arc_f(CX, CY, 13.5, 205, 520), INK, 5.5)
            + stroke(arc_f(CX, CY, 8.5, 230, 470), INK, 2.2))


@reg("ib-tws", RED_DEEP)
def ib_tws():
    wedge = poly([(19, 46), (38, 12), (33.5, 37), (43, 46)], INK, 2)
    return wedge + circle(43, 29, 4, INK)


@reg("ibus", BLUE_DEEP)
def ibus():
    return (circle(33, 16, 4, INK) + stroke("M26 25.5H33.5V43.5M26 43.5H40.5", INK, 5))


@reg("ibus-anthy", BLUE)
def ibus_anthy():
    return stroke("M18.5 20.5L45 18.5M31 12.5L26.5 33"
                  "M26.5 33C33 27.5 45 27.5 45 36C45 42.5 38.5 46 29.5 46", INK, 4.4)


@reg("ibus-bopomofo", BLUE)
def ibus_bopomofo():
    return stroke("M27 13L20 25H43.5C44 34 40.5 42 30.5 46", INK, 4.8)


@reg("ibus-keyboard", BLUE)
def ibus_keyboard():
    kb = rrect(12.5, 17, 39, 26, 5, INK)
    keys = "".join(circle(19 + c * 6.5, 24.5, 2.1, HOLE) for c in range(5))
    keys += "".join(circle(22.25 + c * 6.5, 30.5, 2.1, HOLE) for c in range(4))
    return kb + keys + rrect(21, 35, 22, 3.5, 1.75, HOLE)


@reg("ibus-pinyin", BLUE)
def ibus_pinyin():
    left = stroke("M15.5 22.5H27M21.5 13.5V43.5C21.5 45.5 20.2 46.2 18 45.5M15.5 37.5L27.5 31.5", INK, 3.4)
    right = stroke("M33.5 14L36 18.5M45.5 13.5L43 18.5M31 23H49M30.5 32.5H49.5"
                   "M36.5 23V35C36.5 40 34.5 43.5 30.5 46.5M43.5 23V46.5", INK, 3.4)
    return left + right


@reg("ibus-setup-hangul", BLUE_DEEP)
def ibus_hangul():
    base = circle(CX, CY, 16.5, INK)
    cuts = "".join(g(stroke("M32 30A8.25 8.25 0 0 1 32 13.5", HOLE, 2.6), f"rotate({120 * k} 32 30)")
                   for k in range(3))
    return base + cuts


@reg("ibus-typing-booster", BLUE_GREY_DEEP)
def ibus_booster():
    body = path("M32 11C38.5 16 40.5 24.5 39.5 37H24.5C23.5 24.5 25.5 16 32 11Z", INK)
    nose = path("M32 11C35 13.3 37 16.3 38.2 20H25.8C27 16.3 29 13.3 32 11Z", RED_LIGHT)
    win = circle(32, 26.5, 3.4, HOLE)
    fins = poly([(24.8, 29), (18.5, 37), (18.5, 42), (25, 37)], INK, 2) + \
        poly([(39.2, 29), (45.5, 37), (45.5, 42), (39, 37)], INK, 2)
    flame = poly([(27.5, 39.5), (36.5, 39.5), (32, 48)], DEEP_ORANGE_LIGHT, 2)
    return g(body + nose + win + fins + flame, "translate(32 30) rotate(40) scale(.92) translate(-32 -30)")


@reg("icarus", INDIGO_SOFT)
def icarus():
    return stroke("M17 14.5L21.5 18.5M15 26H24.5L15.5 40.5"
                  "M32 12.5V43.5C32 46 30.5 46.5 27.5 45"
                  "M45 19L36.5 27.5M36.5 26C39 34.5 43.5 39.5 49.5 43", INK, 4)


TOP_O, LEFT_O, RIGHT_O = (17, 20.5), (17, 20.5), (32, 29)


def _face(o, u, v):
    def m(a, b):
        return (o[0] + u[0] * a + v[0] * b, o[1] + u[1] * a + v[1] * b)
    return m


def _cube(top, left, right):
    return (poly([(32, 12), (47, 20.5), (32, 29), (17, 20.5)], top, 2.5)
            + poly([(17, 20.5), (32, 29), (32, 47), (17, 38.5)], left, 2.5)
            + poly([(47, 20.5), (32, 29), (32, 47), (47, 38.5)], right, 2.5))


def _letter(m, pts):
    return pl([m(a, b) for a, b in pts])


def _circ(cx, cy, r, a0, a1, n=24):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


@reg("ice", LIGHT_BLUE_DEEP)
def ice():
    cube = _cube(INK, LIGHT_BLUE_SOFT, INK)
    top = _face((32, 12), (-15, 8.5), (15, 8.5))
    i_dot = circle(*top(0.28, 0.28), 2, HOLE)
    i_stem = stroke(_letter(top, [(0.45, 0.45), (0.72, 0.72)]), HOLE, 2.8)
    lf = _face((17, 20.5), (15, 8.5), (0, 18))
    c = stroke(_letter(lf, _circ(0.5, 0.52, 0.27, 40, 320)), INK, 2.8)
    rf = _face((32, 29), (15, -8.5), (0, 18))
    e = stroke(_letter(rf, [(0.25, 0.52), (0.75, 0.52)] + _circ(0.5, 0.52, 0.26, 0, -300)), LIGHT_BLUE_DEEP, 2.8)
    return cube + i_dot + i_stem + c + e


@reg("ice-store", BLUE_DEEP)
def ice_store():
    cube = _cube(INK, TEAL_LIGHT, TEAL)
    top = _face((32, 12), (-15, 8.5), (15, 8.5))
    a = stroke(_letter(top, [(0.25, 0.25), (0.68, 0.68)]), HOLE, 2.8)
    head = stroke(_letter(top, [(0.25, 0.62), (0.25, 0.25), (0.62, 0.25)]), HOLE, 2.8)
    lf = _face((17, 20.5), (15, 8.5), (0, 18))
    rf = _face((32, 29), (15, -8.5), (0, 18))
    downs = ""
    for m in (lf, rf):
        downs += stroke(_letter(m, [(0.5, 0.2), (0.5, 0.72)]), INK, 2.8)
        downs += poly([m(0.25, 0.5), m(0.5, 0.78), m(0.75, 0.5)], INK, 1.6)
    return cube + a + head + downs


@reg("icecat", BLUE_DEEP)
def icecat():
    globe = circle(32, 31.5, 12.5, INDIGO_DARK)
    body = stroke("M40 16C33 12.5 22 14.5 18 23.5C14 33 19 45 30 47.5C38 49 45 45 47.5 39", INK, 6)
    head = ell_d(42, 19.5, 6.5, 5.2, INK, 25)
    ears = poly([(38, 15.5), (39.5, 10), (43, 14)], INK, 2) + poly([(44, 14.5), (48.5, 11), (48, 17)], INK, 2)
    paw = stroke("M20 27C24 29 27 33 27.5 38", INK, 4)
    return globe + body + head + ears + paw


@reg("icedove", PURPLE_SOFT)
def icedove():
    globe = circle(CX, CY, 16.5, PURPLE)
    wing_r = path("M33 37C35.5 28.5 37.5 20 37 11C42.5 14 46 19 47 25C48 31 44 36 38 38Z", INK)
    wing_l = path("M26 35C22 32.5 17.5 31.5 13.5 33C15.5 37 20 39.5 25.5 39.5Z", INK)
    body = path("M24.5 33C22.5 39.5 25 46.5 32 47C39.5 47.5 44.5 42 43 36.5C39 38 36 36.5 34 33.5Z", INK)
    head = circle(29.5, 31, 5, INK)
    eye = circle(28.5, 30, 1.2, PURPLE)
    return globe + wing_r + wing_l + body + head + eye


@reg("iceweasel", BLUE)
def iceweasel():
    globe = circle(30, 33, 13, INDIGO_DARK)
    body = stroke("M20.5 33V24C20.5 18 28 15 36 17", INK, 5.5)
    head = circle(42.5, 19.5, 6.5, INK) + circle(38.5, 13.8, 2.4, INK) + circle(47.5, 14.5, 2.4, INK)
    eye = circle(42.5, 20.5, 1.3, INDIGO_DARK)
    tail = stroke("M22 42C29 47.5 41 47 46.5 40", INK, 4.5)
    return globe + body + head + eye + tail


@reg("icloud", BLUE)
def icloud():
    return path("M20 42C14.5 42 12.5 37.5 13 34.5C13.5 30.5 17 28 20.5 28.5"
                "C21 21.5 26.5 17 32.5 17C38.5 17 43 21 44 26.5C48.5 27 51 31 51 34.5"
                "C51 38.5 48 42 44 42Z", INK)


@reg("icloud-photos", RED_LIGHT)
def icloud_photos():
    return "".join(g(rrect(28.2, 13.5, 7.6, 14, 3.8, INK, f' stroke="{HOLE}" stroke-width="1.2"'),
                     f"rotate({45 * k} 32 30)") for k in range(8))


@reg("icon-requests", GREY_DARK)
def icon_requests():
    c = stroke(arc_f(30.5, 31, 11, 40, 320), INK, 7.5)
    return c + poly([(39.5, 11), (48.5, 16.5), (39.5, 22)], LIGHT_BLUE, 2.5)


@reg("icon_gentoo_small", AMBER_DARK)
def gentoo():
    g_ = cut("M29 12.5C35.5 11.5 38 16 37 21.5C36 27 31 29.5 27.5 31.5C25 33 25.5 36 28 39"
             "C30 41.5 31 44.5 28 46.5C22.5 45.5 16.5 39.5 16 31C15.5 22 21 13.5 29 12.5Z"
             "M30 17C32.5 17 33 19.5 32 22C31 24.5 28 26 26 25.5C24.5 25 24.7 22.5 26 20.5"
             "C27 18.5 28.5 17 30 17Z", INK)
    moon = path("M39 13.5C45 17 48.5 23 48 31C47.5 38.5 43 44.5 36.5 47.5"
                "C40 41 41.5 35 41.5 29C41.5 23 40.5 18 39 13.5Z", INK)
    return g_ + moon


@reg("iconoclasts", DEEP_ORANGE_DARK)
def iconoclasts():
    head = circle(32, 17, 9, INK) + rrect(29, 6, 6, 12, 1.2, HOLE)
    handle = rrect(28.5, 21, 7, 27, 3.5, INK)
    return g(head + handle, "translate(32 30) rotate(45) scale(.95) translate(-32 -28)")


@reg("icq", GREY_DEEP)
def icq():
    petals = "".join(ell_d(*pt(CX, CY, 10, -90 + k * 360 / 7), 5.2, 6.8, INK if k else RED_LIGHT,
                         -90 + k * 360 / 7 + 90) for k in range(7))
    return petals + circle(CX, CY, 4, HOLE)


@reg("idevice", BLUE_GREY)
def idevice():
    tab = rrect(15, 11, 27, 37, 4.5, INK) + rrect(18.5, 14.5, 20, 27, 1.5, HOLE) + circle(28.5, 44.5, 1.5, HOLE)
    badge = circle(42.5, 40, 10, HOLE) + circle(42.5, 40, 8.5, DEEP_ORANGE_LIGHT)
    apple = (path("M42.5 38.7C44.3 37.5 47.3 38 47.3 41.5C47.3 45 45 47 43.7 47C43.1 47 42.9 46.7 42.5 46.7"
                  "C42.1 46.7 41.9 47 41.3 47C40 47 37.7 45 37.7 41.5C37.7 38 40.7 37.5 42.5 38.7Z", INK)
             + path("M42.7 38.1C42.7 36.3 43.7 35.3 45.3 35.1C45.3 36.8 44.3 37.9 42.7 38.1Z", INK))
    return tab + badge + g(apple, "translate(0 -.8)")


@reg("idjc", BLUE_GREY_DARK)
def idjc():
    disc = circle(CX, CY, 16.5, INK)
    bolt = poly([(45, 9.5), (34.5, 26.5), (39.5, 26.5), (19, 50.5), (29.5, 33), (24.5, 33), (35, 9.5)], AMBER, 1.5)
    hub = circle(CX, CY, 7, HOLE) + circle(CX, CY, 5.3, INK) + circle(CX, CY, 2.2, HOLE)
    return disc + bolt + hub


@reg("ieee1394", GREY_DARK)
def ieee1394():
    bars = (g(rrect(17.5, 15.5, 7, 3.4, 1, INK), "rotate(45 21 17.2)")
            + g(rrect(21.5, 11.5, 7, 3.4, 1, INK), "rotate(45 25 13.2)"))
    diamond = g(rrect(37, 12, 8, 8, 1.2, INK), "rotate(45 41 16)")
    ring_ = _ring(32, 27, 5.2, INK, 3.4)
    base = rrect(27, 36, 10, 3.6, 1, INK) + rrect(27, 42, 10, 3.6, 1, INK)
    return bars + diamond + ring_ + base


@reg("igdm", GREY_DEEP)
def igdm():
    return _ring(31, 31.5, 10.5, INK, 5.5) + circle(45, 16.5, 3.4, INK)


@small("houdini")
def houdini_s():
    pts = []
    for i in range(0, 81):
        t = i / 80
        a = math.radians(-90 + t * 1.6 * 360)
        r = 3 + t * 13.5
        pts.append((32 + r * math.cos(a), 30.5 + r * math.sin(a)))
    return stroke(pl(pts), INK, 4.6)


@small("hp-logo")
def hp_logo_s():
    letters = (stroke("M24.5 16V41M24.5 31C24.5 24.5 32.5 24.5 32.5 31V41", HOLE, 4.4)
               + stroke("M37.5 25V46", HOLE, 4.4) + _ring(41.5, 31.5, 4.4, HOLE, 4.4))
    return circle(CX, CY, 17.5, INK) + g(letters, "translate(32 30) skewX(-18) translate(-32 -30)")


@small("htop")
def htop_s():
    out = ""
    for y, bars in [(22, [GREY_LIGHT, GREY_LIGHT, RED_LIGHT]), (38, [GREY_LIGHT, GREY_LIGHT, AMBER])]:
        out += stroke(f"M18 {y - 5}H15V{y + 5}H18", INK, 2.6)
        out += stroke(f"M46 {y - 5}H49V{y + 5}H46", INK, 2.6)
        for k, c in enumerate(bars):
            out += rrect(21 + k * 7.9, y - 5, 5, 10, 1.2, c)
    return out


@small("httrack")
def httrack_s():
    globe = (circle(28, 26, 14.5, INK) + path("M28 12.5C22.5 17 22.5 35 28 39.5C33.5 35 33.5 17 28 12.5Z",
             "none", f' stroke="{HOLE}" stroke-width="2.4"'))
    badge = circle(41.5, 39.5, 11, HOLE) + circle(41.5, 39.5, 9, DEEP_PURPLE_DARK)
    return globe + badge + stroke("M41.5 33.5V44M36.5 39.5L41.5 44.5L46.5 39.5", INK, 3)


@small("hub")
def hub_s():
    sq = rrect(13.5, 12, 37, 37, 3.5, INK)
    h = stroke("M19.5 18V33M27.5 18V33M19.5 25.5H27.5", HOLE, 3.6)
    b = stroke("M34 18V33H38.5C44 33 44 25.5 38.5 25.5H34M34 18H38C42 18 42 25.5 38 25.5", HOLE, 3.6)
    return sq + h + b + rrect(19, 38.5, 13, 4, 1.5, HOLE)


def _hubstaff_s():
    segs = "".join(path(sector_b(CX, CY, 12.8, 18, a0, a1), INK)
                   for a0, a1 in [(-80, 20), (40, 140), (160, 260)])
    return segs + circle(CX, CY, 9, INK)


for _n in ["hubstaff", "hubstaff-color", "hubstaff-black", "hubstaff-gray", "hubstaff-green", "hubstaff-red"]:
    small(_n)(_hubstaff_s)


@small("hulu")
def hulu_s():
    return stroke("M22 13V45M22 30C22 21 40 21 40 30V45", INK, 6.5)


@small("hw-probe")
def hw_probe_s():
    head = circle(30.5, 30.5, 16, INDIGO_DARK)
    face = ell_d(33, 38, 11, 7.5, INK)
    eye = circle(37, 25, 3.6, INK)
    beak = poly([(42, 24.5), (50.5, 23), (43, 30)], AMBER, 2)
    return head + face + eye + beak


@small("hwloc")
def hwloc_s():
    card = rrect(16, 14, 32, 32, 5, INK)
    return g(card + rrect(20.5, 18.5, 8, 8, 1.5, HOLE) + rrect(31, 29, 12.5, 12.5, 2, HOLE), "rotate(-35 32 30)")


@small("hydrogen")
def hydrogen_s():
    return (stroke("M17.5 16V44M28.5 16V44M17.5 30H28.5", INK, 5)
            + stroke("M34.5 22C34.5 14 46.5 14 46.5 22C46.5 30 34.5 34 34.5 44H47", INK, 5))


@small("hypnospace-outlaw")
def hypnospace_s():
    oct_ = poly([(25.5, 11), (38.5, 11), (45, 16.5), (45, 23.5), (38.5, 29),
                 (25.5, 29), (19, 23.5), (19, 16.5)], INK, 2)
    return oct_ + rrect(26, 17.5, 12, 5, 2.5, HOLE) + poly([(16, 33), (48, 33), (32, 48.5)], INK, 2.5)


@small("hypnotix")
def hypnotix_s():
    base = circle(CX, CY, 17.5, INK)
    blades = "".join(g(stroke("M32 18.5C39 19 43.5 23 45 28.5L50 26", HOLE, 2.4), f"rotate({90 * k} 32 30)")
                     for k in range(4))
    return base + blades + circle(CX, CY, 9.5, HOLE) + circle(CX, CY, 7.5, INK) + \
        poly([(29.5, 26), (36.5, 30), (29.5, 34)], HOLE, 2)


@small("iaito-o")
def iaito_s():
    return stroke(arc_f(CX, CY, 13, 205, 520), INK, 7)


@small("ibus-keyboard")
def ibus_keyboard_s():
    kb = rrect(11, 15.5, 42, 29, 5.5, INK)
    keys = "".join(rrect(16.5 + c * 11, 21, 8, 6, 1.5, HOLE) for c in range(3))
    return kb + keys + rrect(19, 33, 26, 5, 2, HOLE)


@small("ibus-pinyin")
def ibus_pinyin_s():
    left = stroke("M14.5 22H27M21 12.5V45.5M14.5 38.5L27.5 32", INK, 3.6)
    right = stroke("M31.5 22.5H50M30.5 33.5H50.5M37 22.5V35C37 40 35 44 31 47M44.5 22.5V47", INK, 3.6)
    return left + right


@small("ibus-typing-booster")
def ibus_booster_s():
    body = path("M32 10C39 15.5 41.5 24.5 40.5 37.5H23.5C22.5 24.5 25 15.5 32 10Z", INK)
    nose = path("M32 10C35.3 12.5 37.6 16 39 20H25C26.4 16 28.7 12.5 32 10Z", RED_LIGHT)
    fins = poly([(24, 29), (17, 38), (17, 43), (24, 38)], INK, 2) + poly([(40, 29), (47, 38), (47, 43), (40, 38)], INK, 2)
    flame = poly([(27, 40), (37, 40), (32, 49)], DEEP_ORANGE_LIGHT, 2)
    return g(body + nose + fins + flame, "translate(32 30) rotate(40) scale(.92) translate(-32 -30)")


@small("ice")
def ice_s():
    top = _face((32, 12), (-15, 8.5), (15, 8.5))
    return (_cube(INK, LIGHT_BLUE_SOFT, INK) + circle(*top(0.25, 0.25), 2.4, HOLE)
            + stroke(_letter(top, [(0.47, 0.47), (0.74, 0.74)]), HOLE, 3.2))


@small("ice-store")
def ice_store_s():
    top = _face((32, 12), (-15, 8.5), (15, 8.5))
    return (_cube(INK, TEAL_LIGHT, TEAL)
            + stroke(_letter(top, [(0.28, 0.28), (0.7, 0.7)]), HOLE, 3.2)
            + stroke(_letter(top, [(0.28, 0.66), (0.28, 0.28), (0.66, 0.28)]), HOLE, 3.2))


@small("icecat")
def icecat_s():
    globe = circle(31.5, 32, 13, INDIGO_DARK)
    body = stroke("M40 15.5C33 12 21 14 17 23.5C13 33 18.5 45.5 30 48C38 49.5 45 45.5 48 39", INK, 5)
    head = ell_d(42, 19.5, 7, 5.8, INK, 25)
    ears = poly([(37.5, 15.5), (39, 9.5), (43, 14)], INK, 2) + poly([(44, 14.5), (49, 10.5), (48.5, 17.5)], INK, 2)
    return globe + body + head + ears


@small("icedove")
def icedove_s():
    globe = circle(CX, CY, 17.5, GREY_DARK)
    wing_r = path("M32 37C35 28 37.5 19 37 10C43 13 47 19 48 25.5C49 32 44.5 37 38 39Z", INK)
    body = path("M22.5 32.5C20 40 23 47.5 31.5 48C40 48.5 45.5 42.5 44 36.5C39.5 38 35.5 36.5 33.5 33Z", INK)
    return globe + wing_r + body + circle(28, 30, 6, INK)


@small("icq")
def icq_s():
    petals = "".join(ell_d(*pt(CX, CY, 11.5, -90 + k * 360 / 7), 4.6, 6.2, INK if k else RED_LIGHT,
                         -90 + k * 360 / 7 + 90) for k in range(7))
    return petals + circle(CX, CY, 5, HOLE)


@small("idevice")
def idevice_s():
    tab = rrect(13, 10, 28, 38, 5, INK) + rrect(17, 14, 20, 28, 1.5, HOLE)
    badge = circle(42, 39.5, 12, HOLE) + circle(42, 39.5, 10, DEEP_ORANGE_LIGHT)
    apple = (path("M42 37.5C44.4 36 48.3 36.7 48.3 41.2C48.3 45.7 45.3 48.2 43.6 48.2C42.8 48.2 42.5 47.8 42 47.8"
                  "C41.5 47.8 41.2 48.2 40.4 48.2C38.7 48.2 35.7 45.7 35.7 41.2C35.7 36.7 39.6 36 42 37.5Z", INK)
             + path("M42.3 36.8C42.3 34.5 43.6 33.2 45.6 33C45.6 35.2 44.3 36.6 42.3 36.8Z", INK))
    return tab + badge + g(apple, "translate(0 -1.5)")


@small("idjc")
def idjc_s():
    disc = circle(CX, CY, 17.5, INK)
    bolt = poly([(46, 8.5), (35, 26), (40.5, 26), (18, 51.5), (29, 34), (23.5, 34), (34.5, 8.5)], AMBER, 1.5)
    return disc + bolt + circle(CX, CY, 7.5, HOLE) + circle(CX, CY, 4.5, INK)


@small("ieee1394")
def ieee1394_s():
    bar = g(rrect(16, 14.5, 10, 4.4, 1.2, INK), "rotate(45 21 16.7)")
    diamond = g(rrect(36.5, 11, 9.5, 9.5, 1.5, INK), "rotate(45 41.25 15.75)")
    return bar + diamond + _ring(32, 28.5, 5.5, INK, 4) + rrect(25.5, 39, 13, 5, 1.2, INK)
