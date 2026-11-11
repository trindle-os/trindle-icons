# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 58: proton-mail to qpdfview."""
from lm import (
    AMBER, AMBER_DARK, AMBER_DEEP, AMBER_LIGHT, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP,
    BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_LIGHT, BROWN_DEEP, circle, cut, CX, CY,
    CYAN, CYAN_DEEP, CYAN_SOFT, DEEP_ORANGE_DEEP, DEEP_PURPLE, DEEP_PURPLE_DARK,
    DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, g, GREY_DARK, GREY_DEEP, HOLE,
    INDIGO_SOFT, INK, LIGHT_BLUE, LIGHT_BLUE_DEEP, LIGHT_BLUE_LIGHT, line, ORANGE, ORANGE_DARK,
    ORANGE_DEEP, path, PINK_DEEP, PINK_LIGHT, PINK_SOFT, poly, PURPLE_DEEP, PURPLE_SOFT, RED,
    RED_DARK, RED_DEEP, RED_SOFT, rrect, stroke,
)
from glyphs.kit import ellipse_b, registry, _ring

ICONS, SMALL, reg, small = registry()


def L_P(x, y, w, h):
    b = h * 0.58
    r = b / 2
    return f"M{f(x)} {f(y + h)}V{f(y)}H{f(x + w - r)}A{f(r)} {f(r)} 0 0 1 {f(x + w - r)} {f(y + b)}H{f(x)}"


def L_U(x, y, w, h):
    r = w / 2
    return f"M{f(x)} {f(y)}V{f(y + h - r)}A{f(r)} {f(r)} 0 0 0 {f(x + w)} {f(y + h - r)}V{f(y)}"


def L_N(x, y, w, h):
    return f"M{f(x)} {f(y + h)}V{f(y)}L{f(x + w)} {f(y + h)}V{f(y)}"


def L_E(x, y, w, h):
    return f"M{f(x + w)} {f(y)}H{f(x)}V{f(y + h)}H{f(x + w)}M{f(x)} {f(y + h / 2)}H{f(x + w - 1)}"


def L_H(x, y, w, h):
    return f"M{f(x)} {f(y)}V{f(y + h)}M{f(x + w)} {f(y)}V{f(y + h)}M{f(x)} {f(y + h / 2)}H{f(x + w)}"


def L_A(x, y, w, h):
    return (f"M{f(x)} {f(y + h)}L{f(x + w / 2)} {f(y)}L{f(x + w)} {f(y + h)}"
            f"M{f(x + w * .22)} {f(y + h * .64)}H{f(x + w * .78)}")


def L_L(x, y, w, h):
    return f"M{f(x)} {f(y)}V{f(y + h)}H{f(x + w)}"


def L_C(x, y, w, h):
    return (f"M{f(x + w)} {f(y + h * .15)}C{f(x + w * .75)} {f(y)} {f(x)} {f(y - h * .05)} {f(x)} {f(y + h / 2)}"
            f"C{f(x)} {f(y + h * 1.05)} {f(x + w * .75)} {f(y + h)} {f(x + w)} {f(y + h * .85)}")


def L_S(x, y, w, h):
    return (f"M{f(x + w)} {f(y + h * .12)}C{f(x + w * .7)} {f(y - h * .04)} {f(x)} {f(y - h * .04)} {f(x)} {f(y + h * .27)}"
            f"C{f(x)} {f(y + h * .55)} {f(x + w)} {f(y + h * .43)} {f(x + w)} {f(y + h * .73)}"
            f"C{f(x + w)} {f(y + h * 1.04)} {f(x + w * .3)} {f(y + h * 1.04)} {f(x)} {f(y + h * .88)}")


@reg("proton-mail", DEEP_PURPLE)
def proton_mail():
    body = path("M15 18.5C15 15.5 18 14 20.3 15.8L32 25.5L43.7 15.8C46 14 49 15.5 49 18.5V42"
                "A4 4 0 0 1 45 46H19A4 4 0 0 1 15 42Z", INK)
    back = path("M38 20.5L43.7 15.8C46 14 49 15.5 49 18.5V42A4 4 0 0 1 45 46H38Z", DEEP_PURPLE_SOFT)
    return body + back


@reg("proton-pass", DEEP_PURPLE_LIGHT)
def proton_pass():
    gem = g(rrect(18, 16, 28, 28, 8, INK), "rotate(45 32 30)")
    inner = g(rrect(25, 21.5, 13, 13, 4, DEEP_PURPLE_DEEP), "rotate(45 31.5 28)")
    return gem + inner


@reg("proton-vpn-logo", DEEP_PURPLE_DEEP)
def proton_vpn():
    tri = poly([(15, 15.5), (49, 15.5), (33, 46)], INK, 4)
    edge = poly([(41, 20), (49, 15.5), (33, 46), (31.5, 41)], CYAN_SOFT, 2)
    return tri + edge


def _proton_lock():
    shackle = stroke("M24.5 26V21.5A7.5 7.5 0 0 1 39.5 21.5V26", INK, 4)
    body = rrect(17, 24.5, 30, 22, 4.5, INK)
    flap = stroke("M21.5 29.5L32 37.5L42.5 29.5", HOLE, 2.8)
    return shackle + body + flap


@reg("protonmail-desktop", GREY_DARK)
@reg("protonmail-bridge", DEEP_PURPLE_LIGHT)
def protonmail_bridge():
    return _proton_lock()


@reg("protonmail-import-export-app", DEEP_PURPLE)
def protonmail_ie():
    lock = g(_proton_lock(), "translate(-3.5 -2)")
    badge = circle(42.5, 40.5, 9.5, DEEP_PURPLE_DARK)
    arrows = (line(39.5, 45, 39.5, 36.5, INK, 2.4) + stroke("M37 39L39.5 36.3L42 39", INK, 2.4) +
              line(45.5, 36, 45.5, 44.5, INK, 2.4) + stroke("M43 42L45.5 44.7L48 42", INK, 2.4))
    return lock + circle(42.5, 40.5, 11.2, HOLE) + badge + arrows


@reg("protonplus", PURPLE_DEEP)
def protonplus():
    p = stroke("M22 45L27 15H36A7 7 0 0 1 36 29H25", INK, 5.5)
    plus = line(41, 36, 41, 46, PINK_SOFT, 3.4) + line(36, 41, 46, 41, PINK_SOFT, 3.4)
    return p + plus


def _psi():
    arms = stroke("M18.5 17C18.5 30 22.5 35.5 32 35.5C41.5 35.5 45.5 30 45.5 17", INK, 5)
    stem = line(32, 13, 32, 47, INK, 5)
    return arms + stem


@reg("psi", BLUE_DEEP)
def psi():
    return _psi()


@reg("psi-plus", BLUE_DEEP)
def psi_plus():
    badge = circle(42.5, 40.5, 11, HOLE) + circle(42.5, 40.5, 9, RED)
    plus = line(42.5, 36, 42.5, 45, INK, 3) + line(38, 40.5, 47, 40.5, INK, 3)
    return g(_psi(), "translate(-3 -1)") + badge + plus


@reg("pspp", RED_DEEP)
def pspp():
    pie = path("M31 14.5A15.5 15.5 0 1 0 45.3 36L31 30Z", INK)
    wedge = path("M34.5 12.5A15.5 15.5 0 0 1 48.3 33L34.5 27Z", RED_SOFT)
    return pie + wedge


@reg("puddletag", PINK_LIGHT)
def puddletag():
    cloud = path("M21 42A7.5 7.5 0 0 1 19.5 27.2A11 11 0 0 1 40.5 23A9.5 9.5 0 1 1 43 42Z", INK)
    note = (stroke("M30 37V23.5L38 22V35", HOLE, 2.4) +
            circle(28, 37, 2.8, HOLE) + circle(36, 35, 2.8, HOLE))
    return cloud + note


@reg("pulsar", PURPLE_DEEP)
def pulsar():
    orbits = ellipse_b(32, 30, 16, 8.5, INK, 2.4, -25) + ellipse_b(32, 30, 16, 8.5, INK, 2.4, 65)
    core = _ring(32, 30, 5, INK, 2.4) + circle(32, 30, 2.2, INK)
    needle = line(16.5, 45.5, 47.5, 14.5, PURPLE_DEEP, 5) + line(16.5, 45.5, 47.5, 14.5, INK, 2.4)
    return orbits + needle + circle(32, 30, 7.5, HOLE) + core


@reg("pulse-sms", BLUE_DEEP)
def pulse_sms():
    bubble = path("M19 15H45A3 3 0 0 1 48 18V38A3 3 0 0 1 45 41H25L17 47V18A3 3 0 0 1 19 15Z", INK)
    lines = "".join(rrect(x, y, 43 - x, 3, 1.5, HOLE) for x, y in
                    [(22, 20.5), (26, 26), (29.5, 31.5)])
    return bubble + lines


@reg("pulseUi", BLUE_GREY_DEEP)
def pulse_ui():
    top = stroke("M34.5 25.5L40 20L33.5 13.5L27.5 19.5V29.5L38.5 40.5", CYAN, 4.4)
    bottom = stroke("M21.5 38L28 44.5H34", INK, 4.4)
    return top + bottom


@reg("pulseeffects", LIGHT_BLUE)
def pulseeffects():
    out = ""
    for x, k in [(21, 23), (32, 36), (43, 25)]:
        out += line(x, 14, x, 46, INK, 3.2) + circle(x, k, 5, INK)
    return out


@reg("pulseview", GREY_DARK)
def pulseview():
    wires = "".join(line(x, 12.5, x, 25, INK, 2.8) for x in (18.5, 23.9, 29.3, 34.7, 40.1, 45.5))
    box = rrect(14, 26, 36, 20, 4, INK)
    wave = stroke("M18.5 40.5H22.5V32H28V40.5H33.5V32H39V40.5H45.5", HOLE, 2.4)
    return wires + box + wave


PUMPA_BODY = path('M32 20.5C36 17.5 45 17.5 48 25C51 33 47.5 44 39 45.5C36 46 34 45 32 44C30 45 28 46 25 45.5C16.5 44 13 33 16 25C19 17.5 28 17.5 32 20.5Z', INK)


@reg("pumpa", ORANGE_DEEP)
def pumpa():
    body = (PUMPA_BODY)
    grooves = stroke("M26.5 22.5C23 29 23 37 26.5 43", HOLE, 2.2) + stroke("M37.5 22.5C41 29 41 37 37.5 43", HOLE, 2.2)
    stem = stroke("M32 21.5C31.5 16.5 33 13 37.5 12", BROWN_DEEP, 3.6)
    return body + grooves + stem


@reg("punes", ORANGE_DARK)
def punes():
    top = stroke(L_P(21.5, 14, 9, 13) + L_U(34, 14, 9, 13), INK, 3.4)
    bot = stroke(L_N(15, 33, 8.5, 13) + L_E(28, 33, 8, 13) + L_S(40.5, 33, 8.5, 13), INK, 3.4)
    return top + bot


@reg("pureref", GREY_DEEP)
def pureref():
    frame = path("M17 17A3 3 0 0 1 20 14H33A13 13 0 0 1 33 40H24V44A3 3 0 0 1 21 47H20"
                 "A3 3 0 0 1 17 44Z", INK)
    tail = line(36.5, 35, 46, 45.5, INK, 6)
    return frame + circle(33, 27, 6.2, HOLE) + tail


@reg("pushbullet-indicator", ORANGE_DARK)
def pushbullet():
    return (circle(CX, CY, 16.5, INK) + rrect(21.5, 22, 4, 16, 1.2, HOLE) +
            path("M29 22H35A8 8 0 0 1 35 38H29Z", HOLE))


@reg("putty", BLUE_DEEP)
def putty():
    back = rrect(27, 12, 22, 18, 2.5, INK) + rrect(30, 15, 16, 12, 1, HOLE)
    front = rrect(13.5, 24, 26, 21, 2.5, HOLE) + rrect(15, 25.5, 23, 18, 2.5, INK)
    screen = rrect(18, 28.5, 17, 12, 1, AMBER_SOFT)
    bolt = poly([(38, 32.5), (44, 33.5), (41, 37), (46.5, 41), (38.5, 38.5), (41, 35.5)], AMBER_SOFT, 1)
    return back + front + screen + bolt


def _pc():
    box = rrect(16, 14, 32, 32, 2.5, INK)
    p = stroke("M21 32V20.5H25.5A3 3 0 0 1 25.5 26.5H21", HOLE, 3)
    c = stroke("M38.5 21.5C37.5 20.6 36.5 20.3 35.2 20.3C32.6 20.3 31 22.6 31 26.2"
               "C31 29.8 32.6 32.2 35.2 32.2C36.5 32.2 37.5 31.8 38.5 30.9", HOLE, 3)
    bar = rrect(21, 38, 12, 3.2, 0.6, HOLE)
    return box + p + c + bar


def _pc_s():
    box = rrect(15, 13, 34, 34, 3, INK)
    p = stroke("M21.5 34V21H26A3.8 3.8 0 0 1 26 28.5H21.5", HOLE, 4)
    c = stroke("M40 22.5C39 21.4 37.8 21 36.5 21C33.5 21 31.8 23.8 31.8 27.5"
               "C31.8 31.2 33.5 34 36.5 34C37.8 34 39 33.6 40 32.5", HOLE, 4)
    return box + p + c + rrect(20, 38.5, 13, 4, 1, HOLE)


@reg("pycharm-community", CYAN_DEEP)
@reg("pycharm", PURPLE_SOFT)
def pycharm():
    return _pc()


@reg("pyhoca_x2go-logo-ubuntu", RED_DARK)
def x2go():
    thick = poly([(24, 13), (32, 13), (46, 47), (38, 47)], INK, 1.5)
    thin = line(43, 14.5, 23, 45.5, INK, 3)
    serifs = (line(21.5, 13.5, 34, 13.5, INK, 2.4) + line(38.5, 14, 47, 14, INK, 2.4) +
              line(18.5, 46, 28, 46, INK, 2.4) + line(36, 46.5, 48, 46.5, INK, 2.4))
    speed = "".join(line(14, y, 14 + w, y, INK, 2.2) for y, w in [(22, 11), (28, 13), (34, 10)])
    return thick + thin + serifs + speed


@reg("pymol", BLUE_GREY_DEEP)
def pymol():
    atoms = [(19.5, 16.5), (46, 19), (17.5, 43), (44.5, 43)]
    bonds = "".join(line(31.5, 30, x, y, INK, 2.6) for x, y in atoms)
    return (bonds + circle(31.5, 30, 7.5, INK) + circle(31.5, 30, 4.2, HOLE) +
            "".join(circle(x, y, 4.2, AMBER_LIGHT) for x, y in atoms))


@reg("pynocchio", INDIGO_SOFT)
def pynocchio():
    bubble = path("M32 13A16 15 0 1 1 22.5 42.2L15.5 46L17.8 38.5A16 15 0 0 1 32 13Z", INK)
    x = line(26, 22.5, 38, 34.5, HOLE, 4.4) + line(38, 22.5, 26, 34.5, HOLE, 4.4)
    return bubble + x


@reg("pyrenamer", BLUE_DEEP)
def pyrenamer():
    a_tile = rrect(14, 25, 22, 22, 3.5, INK)
    a = stroke(L_A(19.5, 30.5, 11, 12), HOLE, 3)
    b_tile = rrect(26.5, 11.5, 25, 25, 4.5, HOLE) + rrect(28, 13, 22, 22, 3.5, AMBER_LIGHT)
    b = stroke("M34.5 30V18H39.5A3 3 0 0 1 39.5 24H34.5H40A3 3 0 0 1 40 30Z", BLUE_DARK, 3)
    return a_tile + a + b_tile + b


def _snake():
    return path("M27 13H35C38 13 40 15 40 18V26.5C40 29 38 31 35.5 31H27.5C24.5 31 22 33.5 22 36.5"
                "V40H18.5C15 40 13 36.5 13 31.5C13 26.5 15 23.5 18.5 23.5H32V21.5H22V18"
                "C22 15 23.5 13 27 13Z", INK)


@reg("python", BLUE_DEEP)
def python():
    top = _snake() + circle(26, 17, 1.7, HOLE)
    bot = g(_snake().replace(f'"{INK}"', f'"{AMBER_SOFT}"'), "rotate(180 32 30)") + circle(38, 43, 1.7, HOLE)
    return top + bot


@reg("python-faraday", RED_DEEP)
def faraday():
    return poly([(25, 13), (48, 13), (46, 20.5), (33, 20.5), (31.8, 26), (42.5, 26),
                 (40.5, 33), (30, 33), (27, 47), (17, 47)], INK, 2.5)


@reg("pyzologo", BLUE_DEEP)
def pyzologo():
    left = rrect(14, 13, 16, 34, 3, INK) + "".join(
        rrect(17.5, y, 9, 2.6, 1.3, HOLE) for y in (19, 25, 31, 37))
    top = rrect(33, 13, 17, 15, 3, INK) + stroke("M37 17.5L40 20.5L37 23.5M42.5 17.5L45.5 20.5L42.5 23.5", HOLE, 2.2)
    bot = rrect(33, 31, 7.5, 16, 2.5, INK) + rrect(42.5, 31, 7.5, 16, 2.5, INK)
    return left + top + bot


@reg("q4oslogo", BLUE)
def q4os():
    disc = circle(CX, CY, 16.5, INK)
    cuts = (line(14, 30, 50, 30, HOLE, 3.4) + line(32, 12, 32, 48, HOLE, 3.4) +
            path("M30 28H50V50H30Z", HOLE) + circle(CX, CY, 5.5, HOLE))
    sq = g(rrect(35.5, 33.5, 10, 10, 2, INK), "rotate(45 40.5 38.5)")
    return disc + cuts + circle(CX, CY, 3, INK) + sq


@reg("q4wine", AMBER_DARK)
def q4wine():
    glass = path("M24 13H40C40.7 21 38.5 28.5 32 30C25.5 28.5 23.3 21 24 13Z", INK)
    wine_ = path("M24.2 16.5H39.8C39.5 22 37 27.5 32 28.5C27 27.5 24.5 22 24.2 16.5Z", AMBER)
    stem = line(32, 30, 32, 43, INK, 3) + line(25.5, 44.5, 38.5, 44.5, INK, 3.4)
    return g(glass + wine_ + stem, "rotate(-14 32 30)")


@reg("qalculate", PINK_DEEP)
def qalculate():
    block = rrect(14.5, 13, 18, 34, 3.5, INK) + line(14.5, 30, 32.5, 30, HOLE, 1.8)
    x = stroke("M19.5 18.5L27.5 25.5M27.5 18.5L19.5 25.5", HOLE, 2.6)
    om = stroke("M19 42.5H21.8V40.8C19.8 39.7 19 38 19 36.5A4.5 4.5 0 0 1 28 36.5"
                "C28 38 27.2 39.7 25.2 40.8V42.5H28", HOLE, 2.2)
    eq = rrect(37, 24, 12, 3.8, 1.9, INK) + rrect(37, 32.5, 12, 3.8, 1.9, INK)
    return block + x + om + eq


@reg("qasmixer", GREY_DEEP)
def qasmixer():
    out = ""
    for x, k in [(20.5, 22), (32, 34), (43.5, 26)]:
        out += line(x, 14, x, 46, INK, 3.2) + rrect(x - 5, k - 3.5, 10, 7, 2, INK) + line(x - 2.5, k, x + 2.5, k, HOLE, 1.6)
    return out


@reg("qbrowser", BLUE_GREY_DEEP)
def qbrowser():
    globe = circle(CX, CY, 16.5, INK)
    land = (path("M20 19C23 16 28 15 31 16.5C30.5 19 27.5 20 28 23C28.5 26 25 27.5 23 26.5"
                 "C21 25.5 21.5 23 19.5 22.5C18.5 21.5 18.8 20.2 20 19Z", HOLE) +
            path("M36 22C39.5 20.5 44 22.5 45.5 26C47 29.5 46 34 43.5 37C41.5 39 38.5 38 37.5 35.5"
                 "C36.5 33 38.5 31 36.5 29C34.5 27 33.5 23.5 36 22Z", HOLE) +
            path("M24 33C26.5 31.5 30 33 30.5 36C31 39.5 29 43 26.5 43.5C24.5 42 22 38 22.5 35.5Z", HOLE))
    return globe + land


@reg("qcalcfilehash", BLUE_DARK)
def qcalcfilehash():
    w, h, gap = 6.6, 11, 2.6
    xs = [15 + i * (w + gap) for i in range(4)]
    top = L_H(xs[0], 15, w, h) + L_A(xs[1], 15, w, h) + L_S(xs[2], 15, w, h) + L_H(xs[3], 15, w, h)
    bot = L_C(xs[0], 34, w, h) + L_A(xs[1], 34, w, h) + L_L(xs[2], 34, w, h) + L_C(xs[3], 34, w, h)
    return stroke(top + bot, INK, 2.4)


@reg("qchdman", GREY_DEEP)
def qchdman():
    card = rrect(15, 12, 27, 33, 3.5, INK)
    chip = path("M20 30V23A7 7 0 0 1 34 23V30H30V23.5A3 3 0 0 0 24 23.5V30Z", HOLE)
    disc = circle(40.5, 38.5, 12, HOLE) + circle(40.5, 38.5, 10, LIGHT_BLUE_LIGHT)
    return card + chip + disc + circle(40.5, 38.5, 5, INK) + circle(40.5, 38.5, 2.2, LIGHT_BLUE_LIGHT)


@reg("qctools", GREY_DARK)
def qctools():
    frame = rrect(14, 16, 36, 24, 3.5, INK)
    reel = circle(25, 28, 7.5, HOLE) + circle(25, 28, 5.5, INK) + circle(25, 28, 2, HOLE)
    c = stroke("M44.5 23.5C43.3 22.4 41.8 22 40.5 22C37 22 35 24.5 35 28C35 31.5 37 34 40.5 34"
               "C41.8 34 43.3 33.6 44.5 32.5", HOLE, 3)
    tape = stroke("M20.5 34C18 38 17 42 19 46", INK, 2.6)
    return frame + reel + c + tape


@reg("qdirstat", BLUE_GREY)
def qdirstat():
    bars = (rrect(15, 13, 18, 7.5, 2, INK) + rrect(24, 26, 21, 7.5, 2, INK) +
            rrect(33, 39, 16, 7.5, 2, INK))
    links = stroke("M19 21V29.5H22.5M27.5 34V42.5H31", INK, 2.4)
    return bars + links


@reg("qelectrotech", BLUE_GREY_DEEP)
def qelectrotech():
    wire = stroke("M24.5 19H15V43H28.5M35.5 43H49V19H39.5", INK, 2.6)
    lamp = _ring(32, 19, 7, INK, 2.6) + stroke("M27 14L37 24M37 14L27 24", INK, 2.4)
    bat = line(29.5, 37, 29.5, 49, INK, 2.6) + line(34.5, 39.5, 34.5, 46.5, INK, 2.6)
    return wire + lamp + bat


@reg("qemu", DEEP_ORANGE_DEEP)
def qemu():
    q = circle(CX, 29.5, 16.5, INK) + poly([(40, 40), (49, 47), (41, 47.5), (35, 43)], INK, 2)
    bird = path("M21.5 45C20.5 36 22 24 30 19.5C34.5 17 39 18 41 21.5L48 25L40.5 26.5"
                "C38.5 28 37 31 34.5 34C32 37 30.5 41 30.5 45.5Z", HOLE)
    return q + bird + circle(35.5, 22.8, 1.7, INK)


@reg("qgis", INDIGO_SOFT)
def qgis():
    q = _ring(29.5, 27.5, 12, INK, 5.5)
    tail = line(33, 31, 46, 44, HOLE, 10) + line(34, 32, 46, 44, INK, 6)
    tip = line(34, 32, 38, 36, AMBER_LIGHT, 6)
    return q + tail + tip


@reg("qgo", BLUE)
def qgo():
    return (circle(23.5, 21.5, 7.5, INK) + circle(40.5, 21.5, 7.5, BLUE_DARK) +
            circle(23.5, 38.5, 7.5, BLUE_DARK) + circle(40.5, 38.5, 7.5, INK))


@reg("qimgv", BLUE_GREY_DARK)
def qimgv():
    q = cut("M16 18H38V45H31V35H16Z" "M22.5 23.5V29.5H31V23.5Z", INK)
    i = rrect(42, 18, 6.5, 27, 0.8, INK)
    return q + i


@reg("qjackctl", BLUE_GREY)
def qjackctl():
    tip = path("M30 18.5C30 14 31 12 32 12C33 12 34 14 34 18.5Z", INK)
    rings = rrect(29.5, 19.5, 5, 3, 0.5, INK) + rrect(29.5, 23.5, 5, 4, 0.5, INK) + rrect(29, 28.5, 6, 3, 0.5, INK)
    body = rrect(25, 32, 14, 16, 3, INK)
    return tip + rings + body


@reg("qmc2-arcade", RED_DEEP)
def qmc2():
    top = rrect(14, 12, 36, 8, 2.5, INK)
    bot = rrect(14, 40, 36, 8, 2.5, INK)
    cab = rrect(17, 20, 30, 20, 0, RED_SOFT)
    screen = rrect(25, 22.5, 19, 13, 2.5, RED_DARK)
    m = poly([(28, 33), (33, 27), (34, 30), (37.5, 27), (37.5, 33), (35.5, 33), (35.5, 31), (33.5, 33)], INK, 1)
    stick = line(20.5, 35, 20.5, 29.5, RED_DARK, 2) + circle(20.5, 29, 2, RED_DARK)
    return top + bot + cab + screen + m + stick


@reg("qmmp", GREY_DARK)
def qmmp():
    upper = (path("M30 22C24 16 16 14.5 13.5 17C12 21 16 29 29 31Z", INK) +
             path("M34 22C40 16 48 14.5 50.5 17C52 21 48 29 35 31Z", INK))
    lower = (path("M29 32.5C22 33 18 37 19 42.5C21 45 26 43 29.5 38Z", INK) +
             path("M35 32.5C42 33 46 37 45 42.5C43 45 38 43 34.5 38Z", INK))
    ant = stroke("M31 18.5L27.5 12M33 18.5L36.5 12", INK, 2.2)
    return upper + lower + line(32, 20, 32, 45, HOLE, 6.4) + line(32, 20, 32, 45, INK, 3.8) + ant


@reg("qnapi", ORANGE)
def qnapi():
    return _ring(31, 28.5, 12.5, INK, 5.5) + line(35.5, 33.5, 45, 46, INK, 5.5)


@reg("qomp", BLUE_DEEP)
def qomp():
    disc = circle(CX, CY, 16.5, INK) + circle(CX, CY, 13.5, BLUE_LIGHT)
    note = (stroke("M29 36.5V23L39 21V34.5", BLUE_DARK, 2.8) +
            circle(26.5, 36.5, 3, BLUE_DARK) + circle(36.5, 34.5, 3, BLUE_DARK))
    return disc + note


@reg("qpdfview", LIGHT_BLUE_DEEP)
def qpdfview():
    page = rrect(15, 12, 28, 35, 3.5, INK)
    badge = circle(41, 39.5, 12.2, HOLE)
    eye = path("M31.5 39.5C34 35 37.5 33.5 41 33.5C44.5 33.5 48 35 50.5 39.5"
               "C48 44 44.5 45.5 41 45.5C37.5 45.5 34 44 31.5 39.5Z", INK)
    return page + badge + eye + circle(41, 39.5, 3.2, HOLE)


SMALL["pycharm"] = _pc_s
SMALL["pycharm-community"] = _pc_s


@small("punes")
def punes_s():
    return stroke(L_P(17, 17, 12, 22) + L_U(35, 17, 12, 22), INK, 5)


@small("qcalcfilehash")
def qcalcfilehash_s():
    return stroke(L_H(15, 17, 13, 24) + L_C(35, 17, 13, 24), INK, 5)


@small("pulsar")
def pulsar_s():
    orbits = ellipse_b(32, 30, 16, 8, INK, 3.2, -25) + ellipse_b(32, 30, 16, 8, INK, 3.2, 65)
    return orbits + circle(32, 30, 7, HOLE) + circle(32, 30, 4.5, INK)


@small("qalculate")
def qalculate_s():
    block = rrect(14, 13, 19, 34, 4, INK)
    x = stroke("M18.5 23L28.5 33M28.5 23L18.5 33", HOLE, 3.6)
    eq = rrect(37, 22.5, 12, 5, 2.5, INK) + rrect(37, 32.5, 12, 5, 2.5, INK)
    return block + x + eq


@small("pyzologo")
def pyzologo_s():
    return (rrect(14, 13, 16, 34, 3, INK) + rrect(33, 13, 17, 15, 3, INK) +
            rrect(33, 31, 7.5, 16, 2.5, INK) + rrect(42.5, 31, 7.5, 16, 2.5, INK) +
            rrect(17.5, 20, 9, 3.5, 1.7, HOLE) + rrect(17.5, 28, 9, 3.5, 1.7, HOLE))


@small("qelectrotech")
def qelectrotech_s():
    wire = stroke("M24 19H15V43H28.5M35.5 43H49V19H40", INK, 3.2)
    lamp = _ring(32, 19, 7.5, INK, 3.4)
    bat = line(29.5, 36, 29.5, 50, INK, 3.4) + line(35, 39, 35, 47, INK, 3.4)
    return wire + lamp + bat


@small("pyhoca_x2go-logo-ubuntu")
def x2go_s():
    return (poly([(22, 13), (31, 13), (46, 47), (37, 47)], INK, 2) +
            line(43, 14, 22, 46, INK, 4.4))


@small("qctools")
def qctools_s():
    frame = rrect(13, 15, 38, 27, 4, INK)
    reel = circle(24.5, 28.5, 7.5, HOLE) + circle(24.5, 28.5, 4, INK)
    c = stroke("M45 23.5C43.8 22.4 42.3 22 41 22C37.5 22 35.5 24.8 35.5 28.5C35.5 32.2 37.5 35 41 35"
               "C42.3 35 43.8 34.6 45 33.5", HOLE, 4)
    return frame + reel + c


@small("pymol")
def pymol_s():
    atoms = [(19, 16), (46, 18.5), (17, 43.5), (45, 43.5)]
    return ("".join(line(31.5, 30, x, y, INK, 3.4) for x, y in atoms) + circle(31.5, 30, 8, INK) +
            "".join(circle(x, y, 5, AMBER_LIGHT) for x, y in atoms))


def _proton_lock_s():
    shackle = stroke("M24 26V21.5A8 8 0 0 1 40 21.5V26", INK, 5)
    return shackle + rrect(15.5, 24, 33, 24, 5, INK) + stroke("M21 30L32 38.5L43 30", HOLE, 4)


SMALL["protonmail-bridge"] = _proton_lock_s
SMALL["protonmail-desktop"] = _proton_lock_s


@small("protonmail-import-export-app")
def protonmail_ie_s():
    return (g(_proton_lock_s(), "translate(-3 -3)") + circle(43, 41, 11.5, HOLE) +
            circle(43, 41, 9.5, DEEP_PURPLE_DARK) + stroke("M39 37L43 33.5L47 37M43 34V48", INK, 3))


@small("psi-plus")
def psi_plus_s():
    return (g(_psi(), "translate(-3 -1)") + circle(43, 41, 12, HOLE) + circle(43, 41, 10, RED) +
            line(43, 35.5, 43, 46.5, INK, 3.6) + line(37.5, 41, 48.5, 41, INK, 3.6))


@small("pulse-sms")
def pulse_sms_s():
    bubble = path("M19 14H45A3 3 0 0 1 48 17V38A3 3 0 0 1 45 41H25L16 48V17A3 3 0 0 1 19 14Z", INK)
    return bubble + rrect(22, 20.5, 21, 4.5, 2.2, HOLE) + rrect(29, 30, 14, 4.5, 2.2, HOLE)


@small("puddletag")
def puddletag_s():
    cloud = path("M21 43A8 8 0 0 1 19.5 27A11.5 11.5 0 0 1 41 22.5A10 10 0 1 1 43 43Z", INK)
    return cloud + stroke("M33 38V24L39 23.5", HOLE, 3.4) + circle(29.5, 38, 4, HOLE)


@small("pumpa")
def pumpa_s():
    body = PUMPA_BODY
    return body + stroke("M32 21.5C31.5 16.5 33 13 37.5 12", BROWN_DEEP, 4.4)


@small("pulseview")
def pulseview_s():
    wires = "".join(line(x, 12, x, 25, INK, 3.4) for x in (19, 26, 33, 40, 45))
    return wires + rrect(13, 26, 38, 21, 4, INK) + stroke("M18 41H23V32H30V41H36V32H41V41H46", HOLE, 3.2)


@small("pynocchio")
def pynocchio_s():
    bubble = path("M32 12A17 16 0 1 1 22 43L14.5 47L17 39A17 16 0 0 1 32 12Z", INK)
    return bubble + line(25.5, 22, 38.5, 35, HOLE, 5.5) + line(38.5, 22, 25.5, 35, HOLE, 5.5)


@small("pyrenamer")
def pyrenamer_s():
    return (rrect(13, 24, 24, 24, 4, INK) + rrect(26, 10.5, 27, 27, 5, HOLE) +
            rrect(28, 12.5, 23, 23, 4, AMBER_LIGHT) +
            stroke("M35 30.5V17.5H40A3.2 3.2 0 0 1 40 24H35H40.5A3.2 3.2 0 0 1 40.5 30.5Z", BLUE_DARK, 3.6))


@small("python")
def python_s():
    top = _snake()
    bot = g(_snake().replace(f'"{INK}"', f'"{AMBER_SOFT}"'), "rotate(180 32 30)")
    return g(top + bot, "translate(32 30) scale(1.05) translate(-32 -30)")


@small("qbrowser")
def qbrowser_s():
    land = (path("M18 21C21 15 28 14 31 16C31 20 27 21 27 25C24 28 20 26 17 25Z", HOLE) +
            path("M37 21C42 21 47 25 47 31C46 36 43 39 40 38C38 34 40 31 36 28C34 25 34 22 37 21Z", HOLE))
    return circle(CX, CY, 17, INK) + land


@small("qchdman")
def qchdman_s():
    return (rrect(14, 11, 27, 33, 4, INK) + circle(40.5, 38.5, 13, HOLE) +
            circle(40.5, 38.5, 11, AMBER_DEEP) + circle(40.5, 38.5, 4.5, INK))


@small("qdirstat")
def qdirstat_s():
    return (rrect(14, 12, 20, 9, 2.5, INK) + rrect(23, 25.5, 22, 9, 2.5, INK) +
            rrect(32, 39, 18, 9, 2.5, INK))


@small("qmc2-arcade")
def qmc2_s():
    return (rrect(13, 11, 38, 9, 3, INK) + rrect(13, 40, 38, 9, 3, INK) +
            rrect(17, 20, 30, 20, 0, RED_SOFT) + rrect(22, 23, 20, 14, 2.5, RED_DARK))


@small("qmmp")
def qmmp_s():
    wings = (path("M30 22C24 15 15 13.5 12.5 16.5C11 21 15 30 30 32Z", INK) +
             path("M34 22C40 15 49 13.5 51.5 16.5C53 21 49 30 34 32Z", INK) +
             path("M30 33C22 33 17 37 18 43C21 46 27 43 30 38Z", INK) +
             path("M34 33C42 33 47 37 46 43C43 46 37 43 34 38Z", INK))
    return wings + line(32, 18, 32, 46, HOLE, 7) + line(32, 18, 32, 46, INK, 4)


@small("qomp")
def qomp_s():
    return (circle(CX, CY, 17, INK) + circle(CX, CY, 13.5, AMBER_DEEP) +
            stroke("M31 37V22.5L38 21.5", BLUE_DARK, 3.6) + circle(27.5, 37, 4.2, BLUE_DARK))


@small("qpdfview")
def qpdfview_s():
    page = rrect(13, 11, 29, 36, 4, INK)
    eye = path("M29 40C32 34.5 36.5 32.5 41 32.5C45.5 32.5 50 34.5 53 40"
               "C50 45.5 45.5 47.5 41 47.5C36.5 47.5 32 45.5 29 40Z", INK)
    return page + circle(41, 40, 13.5, HOLE) + eye + circle(41, 40, 4, HOLE)


@small("pureref")
def pureref_s():
    frame = path("M16 16A3 3 0 0 1 19 13H33A14 14 0 0 1 33 41H24V45A3 3 0 0 1 21 48H19"
                 "A3 3 0 0 1 16 45Z", INK)
    return frame + circle(33, 27, 6, HOLE) + line(37, 36, 47, 46.5, INK, 7)


@small("pulseUi")
def pulse_ui_s():
    return (stroke("M35 26L41 20L33.5 12.5L26.5 19.5V29.5L39 42", AMBER, 5.5) +
            stroke("M20.5 38L27.5 45H35", INK, 5.5))
