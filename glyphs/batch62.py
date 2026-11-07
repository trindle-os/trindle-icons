# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 62: runescape to serviio."""
from lm import *
from glyphs.kit import gear, registry, _ring

ICONS, SMALL, reg, small = registry()

SHIELD = "M32 12.5L47 17.5V29C47 38 40.5 44.5 32 48C23.5 44.5 17 38 17 29V17.5Z"

def _shield():
    return path(SHIELD, INK, f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')

def _engine(colour, w=3):
    return stroke("M17 27V37M17 32H21M21 27H25L27 24H36L38 27H42V29.5H45L47.5 27V39L45 36.5H42V39"
                  "H29L26 36H21V27Z", colour, w) + stroke("M28 24V20M24 20H32", colour, w)

@reg("runescape", BLUE_DARK)
def runescape():
    stem = path("M24 16H30V40L27 46L24 40Z", INK, f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    guard = rrect(19, 20, 16, 3.6, 1.8, INK)
    bowl = stroke("M30 17H35A6.5 6.5 0 0 1 35 30H30", INK, 4.4)
    leg = stroke("M33 30L45 44", INK, 4.4)
    return stem + guard + bowl + leg

@reg("rust", RED_DEEP)
def rust():
    bucket = poly([(28, 12.5), (40, 12.5), (38.5, 20), (29.5, 20)], INK, 1.5)
    post = rrect(31, 20, 6, 27, 1.5, INK)
    flag = poly([(16, 23), (28.5, 21.5), (28.5, 30), (16, 29)], INK, 1.5)
    dots = "".join(rrect(x, y, 3.2, 3.2, .6, INK) for x, y in [(39, 22.5), (42, 25.5)])
    blade = g(rrect(40, 29, 7, 16, 2, INK), "rotate(-38 43.5 37)")
    return bucket + post + flag + dots + blade

@reg("rustdesk", BLUE)
def rustdesk():
    return (stroke("M26 18A13.5 13.5 0 0 0 26 42", INK, 5.8) +
            stroke("M38 18A13.5 13.5 0 0 1 38 42", INK, 5.8))

@reg("rustrover", PINK_LIGHT)
def rustrover():
    r1 = stroke("M20.5 32V19H24.5A3.2 3.2 0 0 1 24.5 25.4H20.5M24.5 25.4L28 32", HOLE, 3.2)
    r2 = stroke("M31.5 32V19H35.5A3.2 3.2 0 0 1 35.5 25.4H31.5M35.5 25.4L39 32", HOLE, 3.2)
    return rrect(15, 13, 34, 34, 3, INK) + r1 + r2 + rrect(20.5, 38.5, 12, 3.2, 1.6, HOLE)

@reg("rvgl", BLUE_GREY_DEEP)
def rvgl():
    body = gear(CX, CY, 17, 14, 14, INK, .5, 1.5)
    bolt = poly([(35, 18), (25, 32), (31.5, 32), (29, 42), (39, 27.5), (32.5, 27.5)], ORANGE, 1.5)
    return body + circle(CX, CY, 10.5, HOLE) + bolt

@reg("rygel", RED)
def rygel():
    arms = (stroke("M30 30C27 25 25 21 22 18", INK, 3) + stroke("M32 28C33 22 33 17 33 14", INK, 3) +
            stroke("M34 31C39 30 43 29 47 30", INK, 3) + stroke("M31 33C31 38 29 42 26 45", INK, 3))
    blobs = (circle(20.5, 16.5, 4, INK) + circle(33, 13.5, 3, INK) + circle(46, 30, 3, INK) +
             circle(25.5, 45, 3, INK) + circle(32, 31, 6.5, INK))
    return arms + blobs

@reg("ryujinx", INDIGO)
def ryujinx():
    left = path("M26 14H23A8 8 0 0 0 15 22V38A8 8 0 0 0 23 46H26Z", BLUE_LIGHT)
    right = path("M38 14H41A8 8 0 0 1 49 22V38A8 8 0 0 1 41 46H38Z", RED_LIGHT)
    hash_ = (line(30, 22.5, 28, 37.5, INK, 2.6) + line(36, 22.5, 34, 37.5, INK, 2.6) +
             line(26, 27, 38.5, 27, INK, 2.6) + line(25.5, 33, 38, 33, INK, 2.6))
    return left + right + hash_

@reg("sabnzbdplus", ORANGE_DEEP)
def sabnzbdplus():
    return poly([(25, 12), (39, 12), (39, 26), (48, 26), (32, 46), (16, 26), (25, 26)], INK, 3)

@reg("safeeyes", BLUE_GREY)
def safeeyes():
    face = _ring(CX, CY, 14.5, INK, 4)
    wedge = path("M32 30L38 18.5A13 13 0 0 1 43.5 24Z", BLUE_SOFT)
    dots = "".join(circle(x, y, 2.2, INK) for x, y in [(32, 21.5), (40.5, 30), (32, 38.5), (23.5, 30)])
    return face + wedge + dots

@reg("sage-notebook", DEEP_PURPLE_LIGHT)
def sage_notebook():
    outer = [pt(CX, CY, 16, -90 + 60 * k) for k in range(6)]
    inner = [(27, 25), (38, 23), (35, 36)]
    lines = ""
    for i in range(6):
        a, b = outer[i], outer[(i + 1) % 6]
        lines += line(a[0], a[1], b[0], b[1], INK, 2.2)
    for i, j in [(0, 0), (1, 1), (5, 0), (2, 2), (3, 2), (4, 2), (4, 0), (1, 2)]:
        a, b = outer[i], inner[j]
        lines += line(a[0], a[1], b[0], b[1], INK, 2.2)
    for i in range(3):
        a, b = inner[i], inner[(i + 1) % 3]
        lines += line(a[0], a[1], b[0], b[1], INK, 2.2)
    nodes = "".join(circle(x, y, 2.6, INK) for x, y in outer + inner)
    return lines + nodes

def _petals(cx, cy, r, w, fill, rot=-90):
    out = ""
    for k in range(5):
        a = rot + 72 * k
        out += g(path(f"M{f(cx)} {f(cy)}C{f(cx - w)} {f(cy - r * .45)} {f(cx - w)} {f(cy - r)} {f(cx - w * .35)} {f(cy - r)}"
                      f"L{f(cx)} {f(cy - r * .82)}L{f(cx + w * .35)} {f(cy - r)}"
                      f"C{f(cx + w)} {f(cy - r)} {f(cx + w)} {f(cy - r * .45)} {f(cx)} {f(cy)}Z", fill),
                 f"rotate({a + 90} {f(cx)} {f(cy)})")
    return out

@reg("sakura-dungeon", DEEP_ORANGE_LIGHT)
def sakura_dungeon():
    blade = poly([(14, 13), (18.5, 13.5), (35, 30), (31, 34), (14.5, 17.5)], INK, 2)
    guard = line(29, 36, 37, 28, INK, 3.6)
    grip = line(35, 32, 45, 42, DEEP_ORANGE_DARK, 3.4) + circle(46, 43, 2.4, DEEP_ORANGE_DARK)
    flower = _petals(42, 21, 9, 6, INK) + circle(42, 21, 2, HOLE)
    return blade + guard + grip + flower

@reg("sakura-spirit", PINK)
def sakura_spirit():
    return _petals(CX, 30.5, 17, 9.5, INK) + circle(CX, 30.5, 3, HOLE)

@reg("sanctum-2", BLUE_DEEP)
def sanctum_2():
    arcs = stroke("M32 13A17 17 0 0 1 49 30", INK, 3) + stroke("M28 46.5A17 17 0 0 1 15 26", INK, 3)
    disc_ = circle(CX, CY, 11.5, INK)
    two = stroke("M27.5 26A4.6 4.6 0 0 1 36.5 26.5C36.5 30 27.5 33 27.5 36.5H37", HOLE, 3.2)
    return arcs + disc_ + two

@reg("satisfactory", ORANGE_DEEP)
def satisfactory():
    s = path("M21 13H43V21H31V26H43V47H21V39H33V34H21Z", INK,
             f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return s

@reg("sauerbraten", BROWN_DEEP)
def sauerbraten():
    hexa = [pt(CX, CY, 17, -90 + 60 * k) for k in range(6)]
    shell = stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexa) + "Z", INK, 3)
    top = poly([(32, 21.5), (39.5, 25.5), (32, 29.5), (24.5, 25.5)], DEEP_ORANGE_SOFT, 1.5)
    lf = poly([(24.5, 25.5), (32, 29.5), (32, 38), (24.5, 34)], DEEP_ORANGE, 1.5)
    rt = poly([(39.5, 25.5), (32, 29.5), (32, 38), (39.5, 34)], DEEP_ORANGE_DEEP, 1.5)
    return shell + top + lf + rt

@reg("sayonara", BLUE_GREY_DARK)
def sayonara():
    out = ""
    for y, c in [(18, INK), (30, INK), (42, ORANGE)]:
        out += circle(19.5, y, 4, c) + rrect(27, y - 4, 22, 8, 4, c)
    return out

@reg("sc_ide", GREY_DARK)
def sc_ide():
    return _ring(CX, CY, 14.5, INK, 3.2) + _ring(CX, CY, 8.5, INK, 3.2) + circle(CX, CY, 3.5, INK)

@reg("scania-truck-driving-simulator", INDIGO_DEEP)
def scania():
    rim = _ring(CX, CY, 14, AMBER, 4.4)
    spokes = "".join(line(*pt(CX, CY, 4, 22.5 * (2 * k + 1)), *pt(CX, CY, 12, 22.5 * (2 * k + 1)), INK, 2.4)
                     for k in range(8))
    return rim + spokes + circle(CX, CY, 4, INK)

@reg("scans2pdf", BLUE_GREY_DEEP)
def scans2pdf():
    sheet = rrect(19, 16, 26, 31, 3, INK)
    cuts = (line(19, 34, 34, 19, HOLE, 2.4) + line(22, 44, 44, 22, HOLE, 2.4) +
            line(34, 44.5, 44, 34.5, HOLE, 2.4))
    bar = rrect(14, 16, 36, 5, 2.5, BLUE_LIGHT)
    return sheet + cuts + bar

@reg("scantailor", BROWN_LIGHT)
def scantailor():
    s = stroke("M27.5 20.5H21.5A3.8 3.8 0 0 0 21.5 28.2H24.5A3.8 3.8 0 0 1 24.5 36H18", RED, 4)
    dash = "".join(rrect(31.5, y, 2.4, 3.5, 1.2, INK) for y in (14, 20, 26, 32, 38, 44))
    t = stroke("M37.5 27H46M41.75 27V37", INK, 3.6)
    return s + dash + t

@reg("scenarist", BLUE_GREY)
def scenarist():
    body = g(rrect(17, 15, 30, 30, 5, INK) + rrect(21, 19.5, 22, 10, 1.5, HOLE) +
             rrect(21, 30.5, 22, 10, 1.5, HOLE), "rotate(45 32 30)")
    return body

@reg("schism", BROWN_LIGHT)
def schism():
    frame = rrect(15, 14, 34, 32, 3, INK)
    head = rrect(18, 17, 10, 3, 1, HOLE) + rrect(36, 17, 10, 3, 1, HOLE)
    cols = "".join(rrect(x, 23, 7, 20, 1, LIGHT_BLUE_DARK) for x in (18.5, 28.5, 38.5))
    ticks = "".join(rrect(x, y, 7, 1.4, 0, LIGHT_BLUE_LIGHT) for x in (18.5, 28.5, 38.5) for y in (27, 32, 37))
    return frame + head + cols + ticks

@reg("scid", AMBER_DARK)
def scid():
    checks = "".join(rrect(15 + c * 8.5, 13 + r * 8.5, 8.5, 8.5, 0, AMBER_DEEP)
                     for r in range(4) for c in range(4) if (r + c) % 2 == 0)
    board = f'<g>{checks}</g>'
    s = stroke("M41 22H26.5A4 4 0 0 0 26.5 30H37.5A4 4 0 0 1 37.5 38H23", INK, 5.5)
    return board + s

@reg("scidavis", BLUE_DEEP)
def scidavis():
    curve = stroke("M14 40C22 38 26 32 32 30C38 28 42 22 50 20", INK, 2.6)
    beam = stroke("M25 16H39M32 16V44M25 44H39", INK, 3.8)
    return curve + beam + circle(CX, 30, 4.5, DEEP_ORANGE_LIGHT)

@reg("scilab", RED_DEEP)
def scilab():
    return circle(CX, CY, 16.5, INK) + stroke(
        "M40.5 20C37 17.5 30.5 18 27 21.5C24 25 29 29 32 31C35 33 39 37 36 40C33 43 26.5 42 23.5 39.5",
        HOLE, 6)

@reg("scinotes", RED)
def scinotes():
    sheet = rrect(18, 12, 28, 36, 3, INK)
    lines = "".join(rrect(22, y, w, 2.6, 1.3, HOLE)
                    for y, w in [(17, 20), (22, 16), (27, 20), (32, 16), (37, 20), (42, 13)])
    return sheet + lines

@reg("scout-app", ORANGE_DEEP)
def scout_app():
    head = path("M22 22C22 16 26 14 32 14C38 14 42 16 42 22C43 30 42 36 38 42"
                "C36 45 34 46 32 46C30 46 28 45 26 42C22 36 21 30 22 22Z", INK)
    ears = (path("M22 17C18 15 14 17 14 21C14 25 17 28 20 30Z", BROWN_DEEP) +
            path("M42 17C46 15 50 17 50 21C50 25 47 28 44 30Z", BROWN_DEEP))
    face = circle(27.5, 27, 2.6, BLACK) + circle(36.5, 27, 2.6, BLACK)
    nose = path("M29 35H35C35 37.5 33.5 38.5 32 38.5C30.5 38.5 29 37.5 29 35Z", BLACK)
    return ears + head + face + nose

@reg("scratch", ORANGE_DEEP)
def scratch():
    head = path("M17 42C13 36 14 28 17 24L15 13L24.5 19C29 17.5 35 17.5 39.5 19L49 13L47 24"
                "C50 28 51 36 47 42C43 46.5 21 46.5 17 42Z", INK,
                f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    eyes = circle(26, 29, 3.4, HOLE) + circle(38, 29, 3.4, HOLE)
    mouth = stroke("M24 37C29 40.5 35 40.5 40 37", HOLE, 2.6)
    return head + eyes + mouth

@reg("screencloud", BLUE_DEEP)
def screencloud():
    cloud = path("M19 43A8 8 0 0 1 17.5 27.5A10 10 0 0 1 30 18A11 11 0 0 1 47 26A8.5 8.5 0 0 1 45 43Z", INK)
    return cloud + circle(32, 32, 7.5, HOLE) + circle(32, 32, 4.5, INK)

@reg("scribus", BLUE)
def scribus():
    return path("M45 13C41 15 32 18 26 26C21 33 20 40 19 47L21.5 47C23 41 26 36 30 33"
                "C27 36 25.5 40 25 44C35 41 42 32 45 13Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')

@reg("scsi", GREY_DARK)
def scsi():
    frame = g(f'<rect x="19" y="17" width="26" height="26" rx="6" fill="none" stroke="{INK}" stroke-width="4.4"/>',
              "rotate(45 32 30)")
    mark = stroke("M32 22L24 30L32 38", INK, 3.6) + line(30, 30, 40.5, 30, INK, 3.6)
    return frame + mark

@reg("scummvm", BROWN_SOFT)
def scummvm():
    return stroke("M42.5 18C38 14 29 14.5 26 18.5C22 24 30 27.5 34 29.5C39 32 42 36 38.5 40.5"
                  "C35 45 26 45 21 41", INK, 7)

@reg("sdl_instead", BLUE_DEEP)
def sdl_instead():
    book = rrect(18, 12, 28, 36, 3, INK) + rrect(18, 12, 4.5, 36, 2, BLUE_SOFT)
    ribbon = poly([(38, 12), (43, 12), (43, 21), (40.5, 19), (38, 21)], RED)
    gears = (gear(31, 31, 7, 5, 8, HOLE, .5, 1) + circle(31, 31, 2.2, INK) +
             gear(38.5, 40, 5, 3.6, 7, HOLE, .5, 1) + circle(38.5, 40, 1.6, INK))
    return book + ribbon + gears

@reg("sdrangel", BLUE_GREY_DEEP)
def sdrangel():
    halo = f'<ellipse cx="38" cy="16" rx="7" ry="2.3" fill="none" stroke="{INK}" stroke-width="2.2"/>'
    wing = path("M15 26C21 23 27 25 29 29C28 34 23 38 18 38C21 35 21 30 15 26Z", BLUE_SOFT)
    s = stroke("M44 24C41 21 34 21 33 24.5C32 28 44 29 43.5 34C43 39 35 40.5 31.5 37", INK, 4.2)
    return halo + wing + s

@reg("seafile", ORANGE_DEEP)
def seafile():
    cloud = path("M17 40A7 7 0 0 1 17.5 26A9 9 0 0 1 32 21A10 10 0 0 1 47 30A5.5 5.5 0 0 1 46 40Z", INK)
    swirl = stroke("M24 34C24 29 29 27 32 30C35 33 38 32 38.5 29", HOLE, 3)
    return cloud + swirl

@reg("seahorse", ORANGE_DARK)
def seahorse():
    card = rrect(14, 22, 36, 22, 3, ORANGE_DARK)
    stars = "".join(circle(x, 38, 1.7, INK) for x in (33, 38, 43))
    key = (circle(26, 20, 7.5, INK) + circle(26, 18, 2.5, HOLE) +
           rrect(23.5, 25, 5, 22, 1.5, INK) + rrect(27, 38, 4.5, 3, 1, INK))
    return card + stars + key

@reg("seamonkey", INDIGO_DEEP)
def seamonkey():
    waves = stroke("M14 40C19 36 24 44 30 40C36 36 41 44 50 39", BLUE_SOFT, 3.2)
    bird = path("M24 42C22 34 24 25 30 20C34 16.5 38 14 44 13C42 16 40 17 40.5 20"
                "C41 26 37 33 31 38C29 40 27 41.5 24 42Z", INK)
    return waves + bird + circle(38, 18.5, 1.4, HOLE)

@reg("searchmonkey", BROWN)
def searchmonkey():
    head = circle(17, 28, 5, INK) + circle(47, 28, 5, INK) + circle(CX, 30, 15, INK)
    face = path("M22 30C22 23 26 20 32 22C38 20 42 23 42 30C42 38 38 43 32 43C26 43 22 38 22 30Z", BROWN_SOFT)
    lens = _ring(35.5, 28, 5.5, INK, 3) + line(39.5, 32, 45, 38, INK, 3.4)
    eye = circle(26.5, 28, 2.2, INK)
    mouth = stroke("M26.5 37C30 39.5 34 39.5 37 37", INK, 2.4)
    return head + face + eye + lens + mouth

@reg("securecrt", BLUE_GREY_DARK)
def securecrt():
    dollar = stroke("M26 17.5H20.5A3.2 3.2 0 0 0 20.5 24H23.5A3.2 3.2 0 0 1 23.5 30.5H17.5", INK, 3) + \
        line(22, 14.5, 22, 33.5, INK, 2.6)
    under = rrect(29, 29, 11, 3.6, 1.8, INK)
    badge = circle(40, 39, 10, PURPLE_LIGHT)
    rss = (circle(36.5, 42.5, 1.9, INK) + stroke("M35.5 37A6 6 0 0 1 42 43.5", INK, 2.4) +
           stroke("M35.5 32.5A10.5 10.5 0 0 1 46.5 43.5", INK, 2.4))
    return dollar + under + badge + rss

@reg("security-high", INDIGO_SOFT)
def security_high():
    return _shield() + circle(32, 27, 4.2, HOLE) + stroke("M32 30V38", HOLE, 3.8)

@reg("security-low", RED)
def security_low():
    return _shield() + rrect(29.8, 19, 4.4, 14, 2.2, HOLE) + circle(32, 38.5, 2.6, HOLE)

@reg("security-medium", ORANGE_DEEP)
def security_medium():
    return _shield() + rrect(29.8, 19, 4.4, 14, 2.2, HOLE) + circle(32, 38.5, 2.6, HOLE)

@reg("selene", BROWN_LIGHT)
def selene():
    return stroke("M43 18H26A6 6 0 0 0 26 30H38A6 6 0 0 1 38 42H21", INK, 7)

@reg("selinux", BLUE_GREY_DARK)
def selinux():
    return _engine(ORANGE_LIGHT)

@reg("semaphor", INDIGO_DARK)
def semaphor():
    return (poly([(32, 12), (40, 21), (24, 21)], INK, 2) +
            poly([(24, 21), (40, 21), (32, 30)], BLUE_LIGHT, 2) +
            poly([(32, 30), (40, 39), (24, 39)], BLUE_LIGHT, 2) +
            poly([(24, 39), (40, 39), (32, 48)], INK, 2))

@reg("sengi", LIGHT_BLUE_DEEP)
def sengi():
    body = path("M34 14C24 13 16 21 16 31C16 41 25 47 34 46C40 45.5 45 42 47 37"
                "C43 40 38 41 34 40C27 38.5 23 33 24 27C25 21.5 30 18 36 18Z", INK)
    head = path("M34 14L40 11L39 15L46 15L41 19C43 22 42 25 39 26C37 24 36 21 36 18Z", INK)
    return body + head + circle(39.5, 19, 1.3, HOLE)

@reg("sentinel", INDIGO_DARK)
def sentinel():
    shield = path("M17 13H47V29C47 38 40 44.5 32 48C24 44.5 17 38 17 29Z", INK,
                  f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    band = line(20, 17, 44, 38, HOLE, 3.6)
    return shield + band

@reg("sepolicy", BLUE_GREY_DARK)
def sepolicy():
    badge = circle(41, 39, 9.5, BLUE)
    cog = gear(41, 39, 6.5, 4.6, 8, INK, .5, 1) + circle(41, 39, 2, BLUE)
    return g(_engine(ORANGE_LIGHT), "translate(-3 -4)") + badge + cog

@reg("servez", BLUE_DEEP)
def servez():
    mask = path("M32 12C41 12 46 19 46 28C46 38 40 47 32 47C24 47 18 38 18 28C18 19 23 12 32 12Z", INK)
    eyes = (poly([(21.5, 24), (29.5, 29), (27, 32), (22.5, 30)], HOLE, 1.5) +
            poly([(42.5, 24), (34.5, 29), (37, 32), (41.5, 30)], HOLE, 1.5))
    return mask + eyes + line(32, 13, 32, 46, HOLE, 2)

@reg("serviio", ORANGE_DEEP)
def serviio():
    return (stroke("M20 27A12.5 12.5 0 0 1 42 22", INK, 4.4) +
            poly([(45.5, 16), (46.5, 26.5), (36.5, 24)], INK, 2) +
            stroke("M44 33A12.5 12.5 0 0 1 22 38", INK, 4.4) +
            poly([(18.5, 44), (17.5, 33.5), (27.5, 36)], INK, 2))

@small("sage-notebook")
def sage_notebook_s():
    outer = [pt(CX, CY, 15, -90 + 60 * k) for k in range(6)]
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in outer) + "Z"
    return (stroke(d, INK, 2.6) + stroke("M32 15L32 30L19 37.5M32 30L45 37.5", INK, 2.6) +
            "".join(circle(x, y, 3, INK) for x, y in outer + [(32, 30)]))

@small("scid")
def scid_s():
    return stroke("M42 21H26A4.5 4.5 0 0 0 26 30H38A4.5 4.5 0 0 1 38 39H22", INK, 6)

@small("schism")
def schism_s():
    return rrect(15, 14, 34, 32, 3, INK) + "".join(rrect(x, 19, 7, 23, 1, INDIGO) for x in (18.5, 28.5, 38.5))

@small("securecrt")
def securecrt_s():
    dollar = stroke("M28 16H20.5A4.2 4.2 0 0 0 20.5 24.5H24A4.2 4.2 0 0 1 24 33H16", INK, 4.4)
    return dollar + circle(40, 38, 11, PURPLE_LIGHT) + circle(40, 38, 4, INK)

@small("sdl_instead")
def sdl_instead_s():
    book = rrect(18, 12, 28, 36, 3, INK)
    return book + gear(32, 31, 9, 6.5, 8, HOLE, .5, 1) + circle(32, 31, 3, INK)

@small("scantailor")
def scantailor_s():
    s = stroke("M28 19H21.5A4.5 4.5 0 0 0 21.5 28H24.5A4.5 4.5 0 0 1 24.5 37H17", RED, 5)
    return s + rrect(31.2, 13, 3, 34, 1.5, INK) + stroke("M37.5 26H47M42.25 26V38", INK, 4)

@small("sepolicy")
def sepolicy_s():
    eng = stroke("M17 26H27L29 22H35L37 26H44V38H17Z", ORANGE_LIGHT, 4.4)
    return eng + circle(43, 40, 9, BLUE) + circle(43, 40, 3.5, INK)

def _engine_s():
    return stroke("M16 25H27L29 21H35L37 25H44L48 22V40L44 37V41H16Z", ORANGE_LIGHT, 4.4)

@small("selinux")
def selinux_s():
    return _engine_s()

@small("rustrover")
def rustrover_s():
    r = stroke("M25 34V19H31A4 4 0 0 1 31 27H25M31 27L37 34", HOLE, 4.6)
    return rrect(14, 12, 36, 36, 3, INK) + r + rrect(20, 39, 14, 3.6, 1.8, HOLE)

@small("ryujinx")
def ryujinx_s():
    left = path("M28 13H23A8 8 0 0 0 15 21V39A8 8 0 0 0 23 47H28Z", BLUE_LIGHT)
    right = path("M36 13H41A8 8 0 0 1 49 21V39A8 8 0 0 1 41 47H36Z", RED_LIGHT)
    return left + right

@small("safeeyes")
def safeeyes_s():
    return _ring(CX, CY, 14, INK, 4.4) + path("M32 30V17A13 13 0 0 1 45 30Z", BLUE_SOFT)

@small("sanctum-2")
def sanctum_2_s():
    return circle(CX, CY, 16, INK) + stroke("M26 25A6 6 0 0 1 38 25.5C38 30 26 33 26 37.5H38.5", HOLE, 4.4)

@small("scania-truck-driving-simulator")
def scania_s():
    spokes = "".join(line(*pt(CX, CY, 4, 45 * k + 22.5), *pt(CX, CY, 12, 45 * k + 22.5), INK, 3)
                     for k in (0, 2, 4, 6))
    return _ring(CX, CY, 13.5, AMBER, 5.5) + spokes + circle(CX, CY, 4.5, INK)

@small("scidavis")
def scidavis_s():
    return stroke("M24 15H40M32 15V45M24 45H40", INK, 5) + circle(CX, 30, 6, DEEP_ORANGE_LIGHT)
