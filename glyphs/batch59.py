# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 59: qphotorec to radeon-profile."""
from lm import (
    AMBER, AMBER_DARK, AMBER_LIGHT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_GREY_SOFT, BLUE_LIGHT, BLUE_SOFT, BROWN_LIGHT,
    BROWN_SOFT, circle, cut, CYAN_DEEP, DEEP_PURPLE_DARK, DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT,
    DEEP_PURPLE_SOFT, f, g, GREY_DARK, GREY_DEEP, GREY_SOFT, HOLE, INDIGO, INDIGO_DARK,
    INDIGO_DEEP, INDIGO_SOFT, INK, LIGHT_BLUE, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP,
    LIGHT_BLUE_LIGHT, LIGHT_BLUE_SOFT, line, ORANGE_DEEP, path, PINK, PINK_SOFT, poly, pt,
    PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_LIGHT, rrect, stroke, TEAL_DEEP, TEAL_LIGHT,
    TEAL_SOFT,
)
from glyphs.kit import arc, badge, ell_b, ering_b, gear_i, registry, ring_b, shrink

ICONS, SMALL, reg, small = registry()


def _qt_badge():
    return poly([(20.5, 16), (49, 16), (49, 38.5), (43.5, 44), (15, 44), (15, 21.5)], INK, 3)


def _qt_letters(col, w=3.4):
    q = ering_b(24.5, 30, 5.2, 7.5, col, w) + line(27, 35, 30.5, 39.5, col, w)
    t = (stroke("M38.5 21V33.5C38.5 36.5 40 37.5 43.5 37", col, w) +
         line(34.5, 25.5, 43, 25.5, col, w))
    return q + t


@reg("qt", BROWN_SOFT)
def qt():
    return _qt_badge() + _qt_letters(HOLE)


@reg("qtassistant", AMBER_DARK)
def qtassistant():
    return _qt_badge() + stroke("M25 39.5L32 20.5L39 39.5", HOLE, 3.8) + line(27.8, 33, 36.2, 33, HOLE, 3.4)


@reg("qtconfig", GREY_DEEP)
def qtconfig():
    return gear_i(32, 30, 14.5, INK, None, 8) + shrink(_qt_letters(HOLE, 3.6), .78, 32.5, 30)


@reg("qtcreator", INDIGO)
def qtcreator():
    q = ering_b(24.5, 30, 5.6, 8, HOLE, 3.4) + line(27, 35.5, 30.5, 40, HOLE, 3.4)
    c = stroke("M44 23.5C42.8 21.8 41.3 21 39.5 21C36 21 34 25 34 30C34 35 36 39 39.5 39"
               "C41.3 39 42.8 38.2 44 36.5", HOLE, 3.4)
    return _qt_badge() + q + c


@reg("qtdbusviewer", DEEP_PURPLE_LIGHT)
def qtdbusviewer():
    d = stroke("M19 21.5V38.5H21.5C25.5 38.5 28 35 28 30C28 25 25.5 21.5 21.5 21.5Z", HOLE, 3.4)
    v = stroke("M33 21.5L38.5 38.5L44 21.5", HOLE, 3.4)
    return _qt_badge() + d + v


@reg("qtdesigner", LIGHT_BLUE_DEEP)
def qtdesigner():
    return _qt_badge() + stroke("M27 20.5V39.5H30C35 39.5 38 35.5 38 30C38 24.5 35 20.5 30 20.5Z", HOLE, 3.8)


@reg("qtlinguist", BLUE_GREY_LIGHT)
def qtlinguist():
    return _qt_badge() + stroke("M28 20.5V39.5H37.5", HOLE, 3.8)


def _qr():
    def finder(x, y):
        return (cut(f"M{x} {y}h11v11h-11Z" + f"M{x + 2.6} {y + 2.6}v5.8h5.8v-5.8Z", INK)
                + rrect(x + 3.9, y + 3.9, 3.2, 3.2, 0.6, INK))
    out = finder(15, 12.5) + finder(38, 12.5) + finder(15, 36.5)
    blocks = [(29, 12.5), (29, 19), (15, 28), (22, 28), (29, 28), (37, 28), (44, 28),
              (29, 37), (37, 35.5), (44, 42), (37, 43), (29, 43.5)]
    return out + "".join(rrect(x, y, 5, 5, 0.8, INK) for x, y in blocks)


@reg("qtqr", RED_DARK)
@reg("qreator", RED_DEEP)
def qreator():
    return _qr()


@reg("qphotorec", BLUE_GREY_DARK)
def qphotorec():
    cols = [AMBER_LIGHT, BLUE_LIGHT, DEEP_PURPLE_SOFT, RED_LIGHT]
    quads = "".join(path(arc(32, 30, 16.5, -90 + 90 * k, 90 * k) + "L32 30Z", c) for k, c in enumerate(cols))
    seams = "".join(line(*pt(32, 30, 8, a), *pt(32, 30, 17, a), HOLE, 2, "butt") for a in (-90, 0, 90, 180))
    lens = circle(32, 30, 9, HOLE) + circle(34.2, 27.8, 2.6, INK) + circle(29.8, 32.2, 1.6, INK)
    return quads + seams + lens


@reg("qprompt", BLUE_GREY_DEEP)
def qprompt():
    wedge = poly([(14.5, 20), (40, 20), (31, 41)], INK, 3)
    pill = rrect(38, 26.5, 12, 7, 3.5, LIGHT_BLUE_LIGHT)
    return wedge + pill


@reg("qqmusic", AMBER_DARK)
def qqmusic():
    head = ell_b(26, 40.5, 6.8, 5.6, INK)
    stem = line(31.5, 40, 31.5, 15, INK, 4)
    flag = stroke("M31.5 15C35 15.5 38.5 17.5 40.5 20.5C42.5 24 42 28 39 31.5", INK, 4)
    return head + stem + flag


@reg("qsampler", DEEP_PURPLE_DARK)
def qsampler():
    orbit = stroke(arc(32, 30, 16, 200, 330), DEEP_PURPLE_SOFT, 2.4)
    s = stroke("M42 20.5C37 16.5 23 17 22.5 23.5C22 30 42 28 42 35.5C42 42.5 28.5 43.5 21 39", INK, 5.4)
    return orbit + s


@reg("qsynth", ORANGE_DEEP)
def qsynth():
    return path("M32 11.5C37 20 44 27.5 44 35A12 12 0 0 1 20 35C20 27.5 27 20 32 11.5Z", INK)


@reg("qtemu", BLUE_DEEP)
def qtemu():
    tower = rrect(35, 13, 14, 30, 2.5, BLUE_GREY_SOFT) + rrect(38, 17, 8, 3, 1, BLUE_GREY) + circle(42, 37.5, 1.6, BLUE_GREY)
    frame = rrect(13.5, 20, 29, 21, 3, INK) + rrect(17, 23.5, 22, 14, 1.5, HOLE)
    stand = rrect(19, 43.5, 18, 4, 2, INK)
    return tower + frame + stand


@reg("qtfm", LIGHT_BLUE_DEEP)
def qtfm():
    quads = "".join(rrect(x, y, 16.5, 16.5, 3, INK) for x in (14.5, 33) for y in (12, 30.5))
    lid = path("M21 23.5A2 2 0 0 1 23 21.5H28L30.5 24H41A2 2 0 0 1 43 26V38A2 2 0 0 1 41 40H23"
               "A2 2 0 0 1 21 38Z", INK, f' stroke="{HOLE}" stroke-width="2.6" stroke-linejoin="round"')
    return quads + lid


@reg("qtikz", GREY_DEEP)
def qtikz():
    page = rrect(16, 12, 25, 33, 3.5, INK)
    curve = stroke("M20.5 36C24 26 29 22 36.5 20.5", HOLE, 2.4) + circle(20.5, 36, 2.4, HOLE) + circle(36.5, 20.5, 2.4, HOLE)
    pen = (badge(42, 40, BLUE_GREY_DARK, 9) +
           g(rrect(40.5, 32.5, 3.6, 11, 1, INK) + poly([(40.5, 44.5), (44.1, 44.5), (42.3, 48)], INK, 1),
             "rotate(45 42.3 40)"))
    return page + curve + pen


@reg("qtodotxt", GREY_DARK)
def qtodotxt():
    q = ring_b(30.5, 28.5, 12.5, INK, 4.6) + line(39, 37, 46, 44, INK, 5)
    tick = stroke("M24 25H37M24 32H33", GREY_SOFT, 4.4)
    return q + tick


@reg("qtpass-icon", BLUE_DEEP)
def qtpass():
    shackle = stroke("M25 25V20.5A7 7 0 0 1 39 20.5V25", INK, 3.6)
    heart = path("M32 47C25 42 15.5 35.5 15.5 28A7.5 7.5 0 0 1 32 24.5A7.5 7.5 0 0 1 48.5 28"
                 "C48.5 35.5 39 42 32 47Z", INK)
    hole = circle(32, 31.5, 3, HOLE) + poly([(30.8, 32), (33.2, 32), (34, 39), (30, 39)], HOLE, 1)
    return shackle + heart + hole


@reg("qtractor", BLUE_GREY_DARK)
def qtractor():
    disc = ring_b(28.5, 30, 13, INK, 3.6) + circle(28.5, 30, 5.5, RED_LIGHT) + circle(28.5, 30, 2, INK)
    horn = poly([(31, 36.5), (46, 14), (48.5, 40)], AMBER, 2.5)
    bell = circle(45.5, 40.5, 4.2, AMBER) + circle(45.5, 40.5, 1.8, HOLE)
    return disc + horn + bell


@reg("qtscrcpy", TEAL_DEEP)
def qtscrcpy():
    head = path("M16.5 36A15.5 15.5 0 0 1 47.5 36Z", INK)
    ant = line(22, 17, 25.5, 23, INK, 2.8) + line(42, 17, 38.5, 23, INK, 2.8)
    eyes = circle(25, 30.5, 2.2, HOLE) + circle(39, 30.5, 2.2, HOLE)
    base = rrect(14.5, 38.5, 35, 4, 2, INK) + rrect(25, 44, 14, 3.6, 1.8, TEAL_SOFT)
    return head + ant + eyes + base


@reg("qtwebflix", BLUE_GREY_DARK)
def qtwebflix():
    ears = circle(26, 13.5, 2.6, INK) + circle(38, 13.5, 2.6, INK) + line(26, 13.5, 29, 18, INK, 2.2) + line(38, 13.5, 35, 18, INK, 2.2)
    tv = rrect(13.5, 17.5, 37, 29, 7, INK) + rrect(18, 22, 28, 20, 4.5, HOLE)
    w = stroke("M22 26L26 38L32 28.5L38 38L42 26", TEAL_LIGHT, 3.4)
    return ears + tv + w


@reg("quadrapassel", RED)
def quadrapassel():
    return "".join(rrect(x, y, 10, 10, 2.5, INK) for x, y in
                   [(21, 12.5), (21, 24.5), (21, 36.5), (33, 36.5)])


def _quake(nails=1):
    ringp = stroke(arc(32, 25, 13, 300, 240), INK, 4.2)
    inner = stroke(arc(32, 21, 6, 330, 210), INK, 2.6)
    out = ringp + inner
    xs = [32] if nails == 1 else [28.5, 35.5]
    for x in xs:
        out += poly([(x - 3.5, 32), (x + 3.5, 32), (x + 1.4, 35.5), (x, 48.5), (x - 1.4, 35.5)], INK, 1.2)
    if nails == 1:
        out += rrect(26.5, 30.5, 11, 3, 1.5, INK)
    else:
        out += rrect(24.5, 30.5, 15, 3, 1.5, INK)
    return out


@reg("quake", ORANGE_DEEP)
def quake():
    return _quake(1)


@reg("quake2", INDIGO_SOFT)
def quake2():
    return _quake(2)


@reg("quake4", LIGHT_BLUE_DARK)
def quake4():
    return circle(32, 30, 17, INK) + g(_quake(1).replace('"INK"', '"HOLE"'), "translate(32 30) scale(.8) translate(-32 -30)")


def _q3(side, mid):
    horns = (path("M28.5 40C19.5 40 13.5 33.5 14 22.5C16.5 30 21.5 34 28.5 34.5Z", side) +
             path("M35.5 40C44.5 40 50.5 33.5 50 22.5C47.5 30 42.5 34 35.5 34.5Z", side))
    prongs = (poly([(25, 20), (26.6, 33), (25, 44), (23.4, 33)], side, 1) +
              poly([(39, 20), (40.6, 33), (39, 44), (37.4, 33)], side, 1))
    spike = poly([(32, 11.5), (34.8, 30), (32, 49), (29.2, 30)], mid, 1)
    return horns + prongs + spike


@reg("quake3", RED_DEEP)
def quake3():
    return _q3(INK, INK)


@reg("quake3-team-arena", INDIGO_DEEP)
def quake3_ta():
    return _q3(INK, PURPLE_SOFT)


@reg("quanta", BLUE_DEEP)
def quanta():
    lens = circle(29.5, 27.5, 13, INK)
    land = (path("M22 21C25 18 30 18 32 20C30 23 33 26 30 28C27 30 25 26 22 27Z", HOLE) +
            path("M33 31C36 29 40 31 39.5 34C37 37 33 38 30 36.5C32 35 31 32 33 31Z", HOLE))
    handle = line(39, 37, 47, 45, INK, 5.2)
    return lens + land + handle


@reg("quassel", LIGHT_BLUE_DEEP)
def quassel():
    return circle(30.5, 29, 15.5, INK) + circle(37.5, 34, 7.5, HOLE)


@reg("quaternion", BLUE)
def quaternion():
    bubble = circle(31, 29, 16, INK) + rrect(31, 29, 17.5, 17.5, 3, INK)
    a1 = stroke(arc(31, 29, 9, 200, 330), HOLE, 3) + poly([pt(31, 29, 9, 345), pt(31, 29, 12.5, 322), pt(31, 29, 5.5, 322)], HOLE, 1)
    a2 = stroke(arc(31, 29, 9, 20, 150), HOLE, 3) + poly([pt(31, 29, 9, 165), pt(31, 29, 12.5, 142), pt(31, 29, 5.5, 142)], HOLE, 1)
    return bubble + a1 + a2


@reg("qubic", BLUE_GREY)
def qubic():
    q = ring_b(22.5, 29, 6.5, INK, 4.6) + line(25.5, 33, 30, 39.5, INK, 4.6)
    b = stroke("M36 18.5V40H41C45 40 47 38 47 35C47 32 45 30 41 30H36M36 18.5H40.5C43.5 18.5 45.5 20.5 45.5 24"
               "C45.5 27.5 43.5 30 40.5 30", INK, 4.4)
    return q + b


@reg("quickaccess", CYAN_DEEP)
def quickaccess():
    q = ring_b(30.5, 28.5, 14, INK, 4.2) + line(39.5, 38, 47, 45.5, INK, 5)
    a = ring_b(30, 30, 4.8, INK, 3.2) + line(34.8, 25, 34.8, 35.5, INK, 3.2)
    return q + a


@reg("quickgui_512", PINK)
def quickgui():
    lines = "".join(rrect(x, y, w, 3, 1.5, INK) for x, y, w in
                    [(14, 21, 12), (16, 27, 11), (14, 33, 13), (17, 39, 9)])
    neck = stroke("M35 48C35 40 33 34 34.5 25", INK, 6)
    head = ell_b(37, 20.5, 6, 5, INK) + poly([(41, 18), (49, 22), (41, 24)], INK, 1.5)
    eye = circle(37.5, 19.5, 1.3, HOLE)
    return lines + neck + head + eye


@reg("quickhash", CYAN_DEEP)
def quickhash():
    return (line(27.5, 15, 24.5, 45, INK, 4.4) + line(39.5, 15, 36.5, 45, INK, 4.4) +
            line(17, 24.5, 47, 24.5, INK, 4.4) + line(16, 35.5, 46, 35.5, INK, 4.4))


@reg("quimup", LIGHT_BLUE_DARK)
def quimup():
    return poly([(40, 13), (20.5, 32), (31, 32), (24, 47.5), (45, 27), (34, 27)], INK, 2.5)


@reg("quiterss", DEEP_PURPLE_SOFT)
def quiterss():
    rss = (circle(19.5, 42.5, 3.6, INK) + stroke("M16.5 29A14 14 0 0 1 33 45.5", INK, 4.2) +
           stroke("M16.5 19A24 24 0 0 1 43 45.5", INK, 4.2))
    star = badge(42, 18, AMBER, 7.5) + poly([pt(42, 18.4, 5 if k % 2 == 0 else 2.2, -90 + 36 * k) for k in range(10)], INK, 1)
    return rss + star


@reg("quodlibet", BLUE_DEEP)
def quodlibet():
    head = ell_b(28.5, 18.5, 4.8, 4, INK, ' transform="rotate(-20 28.5 18.5)"')
    stem = line(32, 18, 32, 46, INK, 3.4)
    flag = stroke("M32 26C38 30 41 36 37 44", INK, 3.4)
    return head + stem + flag


@reg("qupzilla", LIGHT_BLUE_DEEP)
def qupzilla():
    disc = circle(32, 30, 16.5, INK)
    wave = path("M15.5 36C21 25 33 20.5 48.5 25C39 24.5 31 27.5 27 36Z", HOLE)
    low = path("M16.5 40C24 36 36 35 47 37C44 42 39 45.5 32 46.5C24 46.5 19.5 43.5 16.5 40Z", LIGHT_BLUE_SOFT)
    return disc + wave + low


@reg("qutebrowser", BLUE_DARK)
def qutebrowser():
    disc = circle(32, 30, 16.5, INK)
    q = ring_b(25, 26, 5, HOLE, 3.2) + line(30, 21, 30, 43, HOLE, 3.2)
    b = ring_b(39, 34, 5, HOLE, 3.2) + line(34, 17, 34, 39, HOLE, 3.2)
    return disc + q + b


@reg("qutim", LIGHT_BLUE_DEEP)
def qutim():
    face = path("M30 17C24 17 20 21.5 20 27C20 29 19 31 17 33.5L20.5 34.5C20.5 37 20 39 21 41"
                "C22 43 25 43 27 42.5L28 47H40L39 40C43 37 45 32.5 44 27C43 21 37.5 17 30 17Z", INK)
    flames = (path("M30 17C31 12 34 10 38 9.5C36 12 36 14 37 16Z", INK) +
              path("M36 17.5C38 13.5 42 12 46 12.5C43 14.5 42 16.5 42.5 19.5Z", INK) +
              path("M41 22C44 19.5 47.5 19.5 50 21C47 22 45.5 24 45 27Z", INK))
    eye = circle(27, 27.5, 1.6, HOLE)
    return face + flames + eye


@reg("qv2ray", DEEP_PURPLE_DEEP)
def qv2ray():
    def swoosh(dy, col):
        return path(f"M15 {26 + dy}C22 {17 + dy} 36 {16 + dy} 49 {21 + dy}"
                    f"C38 {20.5 + dy} 30 {24 + dy} 25 {33 + dy}C22 {29 + dy} 19 {27 + dy} 15 {26 + dy}Z", col)
    return swoosh(-4, PINK_SOFT) + swoosh(3.5, INK) + swoosh(11, BLUE_SOFT)


@reg("qv4l2", GREY_DEEP)
def qv4l2():
    cam = circle(29.5, 27.5, 15, INK) + circle(29.5, 27.5, 10.5, BLUE_GREY_DARK) + circle(29.5, 27.5, 7, RED_DEEP) + circle(27.5, 25.5, 2.2, INK)
    return cam + badge(42.5, 40.5, INDIGO_SOFT, 8) + gear_i(42.5, 40.5, 4.6, INK, INDIGO_SOFT, 8, 1.9)


@reg("qvge", BLUE_GREY_DEEP)
def qvge():
    nodes = [(26, 15.5), (40, 15.5), (29.5, 29.5), (16.5, 30), (40, 43), (22.5, 43)]
    edges = [(0, 2), (1, 4), (4, 2), (4, 5), (2, 3)]
    out = "".join(line(*nodes[a], *nodes[b], INK, 2.4) for a, b in edges)
    cols = [BLUE_LIGHT, AMBER_LIGHT, PURPLE_SOFT, TEAL_LIGHT, RED_LIGHT, INK]
    out += "".join(circle(x, y, 4.3, HOLE) + circle(x, y, 3.3, c) for (x, y), c in zip(nodes, cols))
    return out


@reg("qvidcap", BROWN_LIGHT)
def qvidcap():
    frame = rrect(14, 14, 36, 29, 4, INK) + rrect(17.5, 17.5, 29, 22, 2.5, HOLE) + rrect(20, 20, 24, 17, 2, INK)
    legs = rrect(18.5, 44.5, 7, 2.8, 1.4, INK) + rrect(38.5, 44.5, 7, 2.8, 1.4, INK)
    return frame + legs


@reg("qview", BLUE_GREY_DARK)
def qview():
    mount = poly([(15, 41), (26, 25), (33, 34), (38, 28), (49, 41)], INK, 3)
    return mount + circle(40, 19, 3.8, INK)


@reg("qwinff", BLUE)
def qwinff():
    a1 = stroke(arc(29, 27, 11, 200, 320), INK, 3.6) + poly([pt(29, 27, 11, 340), pt(29, 27, 15.5, 314), pt(29, 27, 6.5, 314)], INK, 1)
    a2 = stroke(arc(29, 27, 11, 20, 140), INK, 3.6) + poly([pt(29, 27, 11, 160), pt(29, 27, 15.5, 134), pt(29, 27, 6.5, 134)], INK, 1)
    cam = badge(42, 40.5, RED, 8.5) + rrect(36.5, 37, 8, 7, 1.5, INK) + poly([(44.5, 40.5), (48, 38), (48, 43)], INK, 1)
    return a1 + a2 + cam


def _racket(cx=32, cy=30, r=16.5, w=4.4):
    disc = circle(cx, cy, r, RED)
    a0, a1 = 237, 25
    p0, p1 = pt(cx, cy, r, a0), pt(cx, cy, r, a1)
    blue = path(f"M{f(p0[0])} {f(p0[1])}A{f(r)} {f(r)} 0 0 1 {f(p1[0])} {f(p1[1])}"
                f"L{f(cx - r * .02)} {f(cy - r * .02)}Z", INDIGO)
    k = r / 16.5
    lam = (line(cx - 7 * k, cy - 14.5 * k, cx + 8 * k, cy + 15.5 * k, INK, w, "butt") +
           line(cx + 0.5 * k, cy + 0.5 * k, cx - 8.5 * k, cy + 15 * k, INK, w, "butt"))
    return disc + blue + lam


@reg("racket-logo", INDIGO_DARK)
def racket_logo():
    return _racket()


@reg("racket-slideshow", BLUE_GREY)
def racket_slideshow():
    screen = rrect(13, 13, 38, 28, 3, INK) + rrect(16.5, 16.5, 31, 21, 1.5, HOLE)
    stand = rrect(27, 41, 10, 4, 1, INK) + rrect(21, 44.5, 22, 3.6, 1.8, INK)
    return screen + stand + _racket(32, 27, 9, 2.6)


@reg("radeon-profile", RED_DEEP)
def radeon_profile():
    outer = poly([(16.5, 13), (49, 13), (49, 45.5), (40.5, 37), (40.5, 21.5), (25, 21.5)], INK, 1.5)
    inner = poly([(16, 38), (25, 29), (33.5, 29), (33.5, 37.5), (24.5, 46.5), (16, 46.5)], INK, 1.5)
    amd = shrink(outer + inner, .82, 29.5, 27.5)
    return amd + badge(43, 41, DEEP_PURPLE_LIGHT, 8) + gear_i(43, 41, 4.6, INK, DEEP_PURPLE_LIGHT, 8, 1.9)


@small("qphotorec")
def qphotorec_s():
    cols = [AMBER_LIGHT, BLUE_LIGHT, LIGHT_BLUE_LIGHT, RED_LIGHT]
    quads = "".join(path(arc(32, 30, 17, -90 + 90 * k, 90 * k) + "L32 30Z", c) for k, c in enumerate(cols))
    return quads + circle(32, 30, 8.5, HOLE) + circle(33.5, 28.5, 3, INK)


@small("qt")
def qt_s():
    q = ering_b(24, 30, 6, 8, HOLE, 2.3) + line(27, 36, 30.5, 40.5, HOLE, 2.3)
    t = stroke("M38.5 20V33.5C38.5 36.5 40 38 44 37.5", HOLE, 2.3) + line(34, 25, 44, 25, HOLE, 2.3)
    return _qt_badge() + q + t


@small("qtconfig")
def qtconfig_s():
    return (gear_i(32, 30, 14.5, INK, None, 8) + ering_b(31, 29, 6, 7.5, HOLE, 3) +
            line(33.5, 34, 37, 38.5, HOLE, 3))


@small("qtcreator")
def qtcreator_s():
    q = ering_b(24, 30, 6, 8.5, HOLE, 2.3) + line(27, 36, 30.5, 40.5, HOLE, 2.3)
    c = stroke("M45 23C43.8 21.3 42 20.5 40 20.5C36.3 20.5 34 24.5 34 30C34 35.5 36.3 39.5 40 39.5"
               "C42 39.5 43.8 38.7 45 37", HOLE, 2.3)
    return _qt_badge() + q + c


@small("qtdbusviewer")
def qtdbusviewer_s():
    d = stroke("M18.5 21V39H21C25.8 39 28.5 35.5 28.5 30C28.5 24.5 25.8 21 21 21Z", HOLE, 2.3)
    v = stroke("M32.5 21L38.5 39L44.5 21", HOLE, 2.3)
    return _qt_badge() + d + v


def _qr_s():
    def finder(x, y):
        return (cut(f"M{x} {y}h14v14h-14Z" + f"M{x + 3} {y + 3}v8h8v-8Z", INK)
                + rrect(x + 5, y + 5, 4, 4, 0.6, INK))
    out = finder(14, 12) + finder(36, 12) + finder(14, 34)
    return out + rrect(36, 34, 6, 6, 1, INK) + rrect(44, 42, 6, 6, 1, INK)


@small("qtqr")
@small("qreator")
def qreator_s():
    return _qr_s()


@small("qtikz")
def qtikz_s():
    page = rrect(15, 11, 27, 35, 4, INK)
    curve = stroke("M20.5 37C24 26 29 21.5 37 19.5", HOLE, 3)
    return page + curve + badge(42.5, 40.5, BLUE_GREY_DARK, 8.5) + line(38.5, 44.5, 46.5, 36.5, INK, 3.4)


@small("qtractor")
def qtractor_s():
    disc = ring_b(27, 30, 13, INK, 3.6) + circle(27, 30, 6, RED_LIGHT)
    horn = poly([(29, 38), (46, 12), (49, 42)], AMBER, 3)
    return disc + horn


@small("qtwebflix")
def qtwebflix_s():
    tv = rrect(13, 15, 38, 32, 7, INK) + rrect(17.5, 19.5, 29, 23, 4.5, HOLE)
    w = stroke("M21.5 24L26 38L32 28L38 38L42.5 24", INK, 3.4)
    return tv + w


def _q3_s(side, mid):
    horns = (path("M29 41C19 41 13 34 13.5 21.5C16.5 30 22 34 29 34.5Z", side) +
             path("M35 41C45 41 51 34 50.5 21.5C47.5 30 42 34 35 34.5Z", side))
    return horns + poly([(32, 11), (35.5, 30), (32, 49), (28.5, 30)], mid, 1.5)


@small("quake3")
def quake3_s():
    return _q3_s(INK, INK)


@small("quake3-team-arena")
def quake3_ta_s():
    return _q3_s(INK, PURPLE_SOFT)


@small("quanta")
def quanta_s():
    return circle(29.5, 27.5, 13.5, INK) + circle(27.5, 25.5, 5, HOLE) + line(39, 37, 47, 45, INK, 5)


@small("qubic")
def qubic_s():
    q = ring_b(22, 29, 6.5, INK, 3.6) + line(25.5, 33.5, 29.5, 39.5, INK, 3.6)
    b = stroke("M36 18V40H41C45 40 47.5 38 47.5 35C47.5 32 45 30 41 30H36M36 18H40.5C43.5 18 46 20 46 24"
               "C46 27.5 43.5 30 40.5 30", INK, 3.4)
    return q + b


@small("quickaccess")
def quickaccess_s():
    return (ring_b(30, 28.5, 14, INK, 3.6) + line(39.5, 38, 47, 45.5, INK, 4.4) +
            circle(30, 28.5, 4.5, INK))


@small("qutebrowser")
def qutebrowser_s():
    disc = circle(32, 30, 17, INK)
    q = ring_b(25, 25.5, 5, HOLE, 2.8) + line(30, 20, 30, 45, HOLE, 3)
    b = ring_b(39, 34.5, 5, HOLE, 2.8) + line(34, 15, 34, 40, HOLE, 3)
    return disc + q + b


@small("qv2ray")
def qv2ray_s():
    def swoosh(dy, col):
        return path(f"M15 {26 + dy}C22 {17 + dy} 36 {16 + dy} 49 {21 + dy}"
                    f"C38 {21 + dy} 30 {24 + dy} 26 {31 + dy}C22 {28 + dy} 19 {27 + dy} 15 {26 + dy}Z", col)
    return swoosh(-6, PINK_SOFT) + swoosh(3, INK) + swoosh(12, BLUE_SOFT)


@small("qv4l2")
def qv4l2_s():
    cam = circle(29.5, 27.5, 16, INK) + circle(29.5, 27.5, 10.5, BLUE_GREY_DARK) + circle(29.5, 27.5, 6.5, RED_DEEP)
    return cam + badge(43, 41, LIGHT_BLUE, 7.5)


@small("qvge")
def qvge_s():
    nodes = [(24, 16), (40, 16), (32, 31), (22, 44), (41, 44)]
    edges = [(0, 2), (1, 4), (4, 2), (4, 3)]
    out = "".join(line(*nodes[a], *nodes[b], INK, 2.4) for a, b in edges)
    cols = [BLUE_LIGHT, AMBER_LIGHT, PURPLE_SOFT, INK, RED_LIGHT]
    return out + "".join(circle(x, y, 5.5, HOLE) + circle(x, y, 4.3, c) for (x, y), c in zip(nodes, cols))


@small("qwinff")
def qwinff_s():
    a1 = stroke(arc(29, 27, 11, 200, 320), INK, 3.4) + poly([pt(29, 27, 11, 342), pt(29, 27, 16.5, 312), pt(29, 27, 5.5, 312)], INK, 1)
    a2 = stroke(arc(29, 27, 11, 20, 140), INK, 3.4) + poly([pt(29, 27, 11, 162), pt(29, 27, 16.5, 132), pt(29, 27, 5.5, 132)], INK, 1)
    return a1 + a2 + badge(43, 41, RED, 8) + rrect(38.5, 38, 9, 6, 1.5, INK)


@small("racket-slideshow")
def racket_slideshow_s():
    screen = rrect(12, 11, 40, 31, 3, INK) + rrect(15, 14, 34, 25, 1.5, HOLE)
    stand = rrect(20, 44, 24, 4, 2, INK)
    return screen + stand + _racket(32, 26.5, 12, 3)


@small("radeon-profile")
def radeon_profile_s():
    outer = poly([(16.5, 13), (49, 13), (49, 45.5), (40.5, 37), (40.5, 21.5), (25, 21.5)], INK, 1.5)
    inner = poly([(16, 38), (25, 29), (33.5, 29), (33.5, 37.5), (24.5, 46.5), (16, 46.5)], INK, 1.5)
    return outer + inner
