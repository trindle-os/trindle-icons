# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 36: io.github.lainsce.Emulsion to jami.

Same hand as batch01: chunky rounded marks in INK, HOLE for cut-outs,
any second shade a palette step.
"""
from lm import *
from glyphs.kit import arc, gear, registry, ring_b

ICONS, SMALL, reg, small = registry()

def _sheet(x0, y0, x1, y1, ear, fill):
    """Page with its bottom-right corner folded under."""
    return path(f"M{x0 + 3} {y0}H{x1 - 3}A3 3 0 0 1 {x1} {y0 + 3}V{y1 - ear}"
                f"L{x1 - ear} {y1}H{x0 + 3}A3 3 0 0 1 {x0} {y1 - 3}V{y0 + 3}"
                f"A3 3 0 0 1 {x0 + 3} {y0}Z", fill)

@reg("io.github.lainsce.Emulsion", GREY_DARK)
def emulsion():
    out = ""
    for y, k in [(19, 38), (30, 24), (41, 30)]:
        out += line(16, y, 48, y, GREY_LIGHT, 4.4) + circle(k, y, 5.5, INK)
    return out

@reg("io.github.lainsce.Khronos", PURPLE_LIGHT)
def khronos():
    face = ring_b(CX, CY, 15, INK, 3.6)
    hands = stroke("M32 21V30H40", INK, 3.4)
    return face + hands + circle(CX, CY, 2.8, INK)

@reg("io.github.lainsce.Notejot", AMBER_LIGHT)
def notejot():
    sheet = _sheet(15, 13, 45, 47, 9, INK)
    lines = "".join(rrect(20, y, w, 2.6, 1.3, HOLE) for y, w in [(20, 14), (26, 10), (32, 17)])
    pencil = (line(47.5, 16.5, 32, 32, HOLE, 9.5) + line(47.5, 16.5, 34, 30, INK, 5.2)
              + poly([(35.8, 32.2), (31.8, 28.2), (29.5, 34.5)], INK, 1.2))
    return sheet + lines + pencil

@reg("io.github.lainsce.Quilter", BLUE_DEEP)
def quilter():
    sheet = rrect(17, 12, 30, 36, 4, INK)
    lines = "".join(rrect(22, y, w, 2.6, 1.3, HOLE) for y, w in
                    [(19, 20), (24.5, 20), (30, 14), (35.5, 20), (41, 12)])
    cursor = line(40, 28.5, 40, 39, BLUE_LIGHT, 2.6)
    return sheet + lines + cursor

@reg("io.github.leonardschardijn.Chirurgien", BLUE_GREY)
def chirurgien():
    out = ""
    for a in [-78, -62, -46, -30, -14]:
        hx, hy = pt(17, 46, 22, a)
        bx, by = pt(17, 46, 33, a)
        mx, my = pt(hx, hy, 4, a)
        out += line(17, 46, hx, hy, INK, 2.4) + line(hx, hy, bx, by, INK, 2.4) + line(mx, my, bx, by, INK, 4.2)
    return out

@reg("io.github.mightycreak.Diffuse", AMBER_DARK)
def diffuse():
    lanes = line(14, 21, 38, 21, AMBER, 4.4) + line(26, 39, 50, 39, AMBER, 4.4)
    top = circle(40, 21, 8.5, INK) + stroke("M44.5 21H36M39.5 17.2L35.7 21L39.5 24.8", HOLE, 2.6)
    bot = circle(24, 39, 8.5, INK) + stroke("M19.5 39H28M24.5 35.2L28.3 39L24.5 42.8", HOLE, 2.6)
    return lanes + top + bot

@reg("io.github.mki1967.mki3dgame", RED)
def mki3dgame():
    gem = poly([(28, 13), (40, 16), (47, 28), (43, 42), (29, 47), (17, 38), (19, 22)], INK, 2.5)
    face = poly([(30, 28), (47, 28), (43, 42), (29, 47)], RED_SOFT, 2.5)
    return gem + face

@reg("io.github.mpobaschnig.Vaults", GREY_DARK)
def vaults():
    box = rrect(14, 12, 36, 36, 5, INK)
    door = rrect(19, 16, 27, 28, 3, HOLE)
    hinges = rrect(12.5, 19, 4, 6, 1.5, INK) + rrect(12.5, 35, 4, 6, 1.5, INK)
    x = (line(25, 22, 40, 38, INK, 3) + line(40, 22, 25, 38, INK, 3)
         + circle(32.5, 30, 5, INK) + circle(32.5, 30, 2.2, HOLE))
    return box + hinges + door + x

@reg("io.github.nokse22.minitext", BLUE_GREY_LIGHT)
def minitext():
    card = rrect(13, 16, 38, 28, 5, INK)
    rows = (rrect(18, 22, 16, 3, 1.5, HOLE) + circle(44, 23.5, 2.8, HOLE)
            + rrect(18, 29, 11, 3, 1.5, HOLE) + rrect(32, 29, 14, 3, 1.5, HOLE)
            + rrect(18, 36, 7, 3, 1.5, HOLE) + rrect(28, 36, 18, 3, 1.5, HOLE))
    return card + rows

@reg("io.github.parnassius.SysDVR-Qt", RED)
def sysdvr():
    body = rrect(13, 16, 38, 28, 10, INK)
    seams = line(22, 16, 22, 44, HOLE, 2.2) + line(42, 16, 42, 44, HOLE, 2.2)
    sticks = circle(17.5, 23, 2.2, HOLE) + circle(46.5, 36, 2.2, HOLE)
    cast = (circle(26.5, 37.5, 2.2, HOLE) + stroke(arc(26, 38, 6, -90, 0), HOLE, 2.4)
            + stroke(arc(26, 38, 11, -90, 0), HOLE, 2.4))
    return body + seams + sticks + cast

@reg("io.github.purplehorrorrus.Meridius", BLUE_GREY_DARK)
def meridius():
    heads = (f'<ellipse cx="22" cy="41.5" rx="5.8" ry="4.5" fill="{INK}" transform="rotate(-20 22 41.5)"/>'
             f'<ellipse cx="40" cy="37.5" rx="5.8" ry="4.5" fill="{INK}" transform="rotate(-20 40 37.5)"/>')
    stems = line(26.5, 41, 26.5, 19, INK, 3.4) + line(44.5, 37, 44.5, 15, INK, 3.4)
    beam = poly([(26.5, 17), (46.2, 12.5), (46.2, 19), (26.5, 23.5)], INK, 1.6)
    return heads + stems + beam

@reg("io.github.quodlibet.ExFalso", BLUE_DEEP)
def exfalso():
    blade = path("M32 30C27 25 25 19 27 13C32 14 38 17 38.5 22C38.8 25 36 28 32 30Z", INK)
    blades = "".join(g(blade, f"rotate({90 * k} 32 30)") for k in range(4))
    return blades + circle(CX, CY, 2.6, HOLE)

@reg("io.github.realmazharhussain.GdmSettings", BLUE_GREY_DEEP)
def gdmsettings():
    panel = rrect(14, 12, 30, 34, 5, INK)
    user = circle(29, 23, 5, HOLE) + path("M20.5 36C20.5 31 24 29 29 29C34 29 37.5 31 37.5 36Z", HOLE)
    field = rrect(20, 39, 12, 2.6, 1.3, HOLE)
    badge = circle(42, 39, 10, HOLE) + gear(42, 39, 8, 6, 8, BLUE_SOFT, .55, 1.5) + circle(42, 39, 2.6, HOLE)
    return panel + user + field + badge

@reg("io.github.seadve.Kooha", PINK)
def kooha():
    corners = stroke("M14 20V15H19M45 15H50V20M50 40V45H45M19 45H14V40", INK, 3.2)
    cam = poly([(19, 24), (26, 30), (19, 36)], INK, 2.5) + rrect(27, 21, 19, 18, 3.5, INK)
    return corners + cam + circle(36.5, 30, 4.4, HOLE) + circle(36.5, 30, 2, INK)

@reg("io.github.seadve.Mousai", PURPLE)
def mousai():
    heads = ring_b(23, 38, 4.8, INK, 3.4) + ring_b(40, 38, 4.8, INK, 3.4)
    stems = line(27.8, 38, 27.8, 17, INK, 3.4) + line(44.8, 38, 44.8, 17, INK, 3.4)
    beam = rrect(26.1, 14.5, 20.4, 5, 1.5, INK)
    return heads + stems + beam

@reg("io.github.swanux.hbud", TEAL_DARK)
def hbud():
    outer = ring_b(CX, CY, 16, TEAL_SOFT, 3.2)
    return outer + circle(29, 27, 6.2, INK) + stroke(arc(CX, CY, 10, 10, 105), INK, 3.4)

@reg("io.github.tfuxu.Halftone", ORANGE_DEEP)
def halftone():
    frame = rrect(14, 12, 36, 36, 5, INK) + rrect(18, 16, 28, 28, 2, HOLE)
    top = rrect(18, 16, 28, 9, 2, INK)
    dots = ""
    for r, (y, rad) in enumerate([(28, 1.7), (33, 1.35), (38, 1.0), (42, 0.7)]):
        for c in range(6):
            x = 20.5 + c * 4.6 + (2.3 if r % 2 else 0)
            if x < 45:
                dots += circle(x, y, rad + 0.6, INK)
    return frame + top + dots

@reg("io.github.trytonvanmeer.DungeonJournal", RED_DEEP)
def dungeonjournal():
    book = rrect(17, 12, 30, 36, 4, INK)
    spine = line(22.5, 12.5, 22.5, 47.5, HOLE, 2.2)
    ribbon = path("M36 12H42V26L39 23.5L36 26Z", RED_DARK)
    return book + spine + ribbon

@reg("io.github.vegad.vnotes", BLUE_GREY)
def vnotes():
    sheet = _sheet(16, 12, 48, 48, 8, INK)
    holes = "".join(circle(20.5 + k * 4.6, 16.5, 1.4, HOLE) for k in range(7))
    v = stroke("M24.5 23L32 40L39.5 23", HOLE, 3.8)
    return sheet + holes + v

@reg("io.github.vinegarhq.Vinegar", BROWN)
def vinegar():
    bowl = path("M20 13H44C45 24 40 32 32 32C24 32 19 24 20 13Z", INK)
    liquid = path("M21.2 20H42.8C42 26.5 38 29.5 32 29.5C26 29.5 22 26.5 21.2 20Z", BROWN_DARK)
    stem = line(32, 31, 32, 43, INK, 3.4) + rrect(23, 43, 18, 4, 2, INK)
    return bowl + liquid + stem

@reg("io.gitlab.caveman250.headlines", BLUE)
def headlines():
    face = path("M15 31H49A17 15 0 0 1 15 31Z", INK)
    eyes = circle(25.5, 37.5, 2.6, HOLE) + circle(38.5, 37.5, 2.6, HOLE)
    hat = poly([(20, 13), (44, 13), (39.5, 28), (24.5, 28)], INK, 3)
    band = rrect(26, 20, 12, 3, 1.5, HOLE)
    return face + eyes + hat + band

@reg("io.gitlab.hamadmarri.gamma", BLUE_GREY_DARK)
def gamma():
    gam = stroke("M16 45V17H25", ORANGE_LIGHT, 5)
    pills = (rrect(30, 15, 11, 5, 2.5, INK) + circle(46, 17.5, 2.5, RED_LIGHT)
             + rrect(30, 23.5, 12, 5, 2.5, AMBER_SOFT) + rrect(30, 32, 19, 5, 2.5, INK)
             + rrect(30, 40.5, 13, 5, 2.5, AMBER_SOFT))
    return gam + pills

@reg("io.gitlab.idevecore.Pomodoro", RED)
def pomodoro():
    body = circle(32, 32, 16, INK)
    leaves = path("M19 22C21 15 26 12.5 32 12.5C38 12.5 43 15 45 22L40 19L36 23L32 19L28 23L24 19Z", DEEP_PURPLE_LIGHT,
                  ' stroke="#825DBA" stroke-width="1.5" stroke-linejoin="round"')
    eye = path("M23 32C26 29 31 28.5 34 30.5C31 33 26 33.5 23 32Z", HOLE) + circle(29.5, 31, 1.6, INK)
    swirl = stroke(arc(32, 32, 10, -25, 55), HOLE, 2.6)
    return body + leaves + eye + swirl

@reg("io.gitlab.leesonwai.Sums", ORANGE_DEEP)
def sums():
    left = rrect(14, 13, 18, 34, 4, INK)
    right = rrect(33, 13, 17, 34, 4, ORANGE_SOFT)
    split = line(14.5, 30, 31.5, 30, HOLE, 1.8)
    minus = line(19, 21.5, 27, 21.5, HOLE, 3.2)
    plus = line(19, 38.5, 27, 38.5, HOLE, 3.2) + line(23, 34.5, 23, 42.5, HOLE, 3.2)
    eq = line(37, 33.5, 46, 33.5, ORANGE_DEEP, 3.2) + line(37, 39.5, 46, 39.5, ORANGE_DEEP, 3.2)
    return left + right + split + minus + plus + eq

@reg("io.missioncenter.MissionCenter", BLUE_GREY_DARK)
def missioncenter():
    side = "".join(rrect(13, y, 9, 10, 2, INK) for y in [13, 25, 37])
    main = rrect(25, 13, 26, 34, 4, INK)
    pulse = stroke("M28.5 31H33L36 23.5L40 38L43 29H47.5", HOLE, 2.8)
    return side + main + pulse

@reg("io.posidon.Paper", TEAL)
def paper():
    sheet = _sheet(16, 12, 48, 48, 9, INK)
    band = path("M19 12H45A3 3 0 0 1 48 15V19H16V15A3 3 0 0 1 19 12Z", TEAL_DARK)
    lines = "".join(rrect(21, y, w, 2.6, 1.3, HOLE) for y, w in [(25, 22), (30.5, 16)])
    bullets = "".join(circle(22.3, y + 1.3, 1.4, HOLE) + rrect(26, y, 12, 2.6, 1.3, HOLE)
                      for y in [36, 41.5])
    return sheet + band + lines + bullets

@reg("io.sam.Boards", BROWN_LIGHT)
def boards():
    board = rrect(14, 15, 36, 32, 5, INK)
    clip = rrect(26, 11, 12, 7, 2.5, INK) + circle(32, 13.2, 1.6, HOLE)
    cols = (rrect(18.5, 21, 7.5, 21, 2, HOLE) + rrect(28.3, 21, 7.5, 11, 2, HOLE)
            + rrect(38, 21, 7.5, 16, 2, HOLE))
    return board + clip + cols

@reg("io.seamly.seamly2d", DEEP_PURPLE_DEEP)
def seamly2d():
    return stroke("M40 18C37 14 27 13.5 25 18.5C22.5 25 40 27 40 36.5C40 43 28 45 23.5 40.5",
                  INK, 4.6, ' stroke-dasharray="2.5 6"')

@reg("iortcw", RED_DARK)
def iortcw():
    bar = poly([(13, 15), (51, 15), (47, 20.5), (17, 20.5)], INK, 2)
    posts = rrect(21, 20, 4.5, 10, 1, INK) + rrect(38.5, 20, 4.5, 10, 1, INK)
    w = stroke("M20 25L26 45L32 32L38 45L44 25", INK, 4.6)
    return bar + posts + w

@reg("ipscan", GREY_DEEP)
def ipscan():
    ball = circle(CX, CY, 12.5, GREY_DARK)
    bar = rrect(13, 27.5, 38, 5, 2.5, GREY_SOFT)
    bolt = poly([(39, 12), (24, 32), (32, 32), (26, 48), (42, 27), (34, 27)], INK, 2)
    return ball + bar + bolt

@reg("ipython", BLUE_GREY_DARK)
def ipython():
    blue = BLUE_LIGHT
    left = stroke("M19 19H15V41H19", blue, 3.6)
    right = stroke("M40 19H44V41H40", blue, 3.6)
    y = stroke("M22.5 22L29.5 33.5M36.5 22L27 43", INK, 3.8)
    colon = circle(49, 25, 2, blue) + circle(49, 35, 2, blue)
    return left + right + y + colon

@reg("ir.imansalmani.IPlan", BLUE)
def iplan():
    return rrect(16, 14, 32, 32, 8, "none", f' stroke="{INK}" stroke-width="5.5"') + stroke("M32 22V38M24 30H40", INK, 5)

@reg("irc-chat", LIGHT_BLUE_DEEP)
def irc_chat():
    back = rrect(27, 11, 22, 21, 3, LIGHT_BLUE_SOFT)
    front = path("M18 19H38A3 3 0 0 1 41 22V44A3 3 0 0 1 38 47H21A3 3 0 0 1 18 44V25L13 21Z", INK,
                 f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    hsh = (line(26, 25, 24, 41, HOLE, 2.6) + line(34, 25, 32, 41, HOLE, 2.6)
           + line(21.5, 29.5, 37.5, 29.5, HOLE, 2.6) + line(21, 36.5, 37, 36.5, HOLE, 2.6))
    return back + front + hsh

@reg("irccloud-desktop", BLUE_DEEP)
def irccloud():
    cloud = path("M21 41C16 41 13 37.5 13 33.5C13 29.5 16 26.5 20 26.5C20.5 20 25.5 15.5 32 15.5"
                 "C38 15.5 42.5 19.5 43.5 25C47.5 25.5 51 29 51 33C51 37.5 47.5 41 43 41H27"
                 "L21 46Z", INK)
    return cloud

@reg("iridium-browser", BLUE_DEEP)
def iridium():
    globe = ring_b(34, 30, 15, INK, 3.4)
    swoosh = (stroke("M33 22C39 20 44 21 47 24", INK, 2.8) + stroke("M34 30H48.5", INK, 2.8)
              + stroke("M33 38C39 40 44 39 47 36", INK, 2.8) + circle(45.5, 20, 3.4, BLUE_SOFT))
    shield = path("M14 19L26 14.5L38 19V29C38 37 32.5 42.5 26 46C19.5 42.5 14 37 14 29Z", INK,
                  f' stroke="{HOLE}" stroke-width="3" stroke-linejoin="round"')
    hole = circle(26, 27, 3, HOLE) + poly([(24.5, 28.5), (27.5, 28.5), (28.3, 36), (23.7, 36)], HOLE, 1)
    return globe + swoosh + shield + hole

@reg("iron_product_logo", BLUE)
def iron():
    disc_ = circle(CX, CY + 1, 15.5, INK)
    blade = path("M12.5 30.5C22 21 36 18 42 22C46 25 48.5 32 51.5 38.5"
                 "C44 29 34 28 25 33C21 35 17.5 39 15 43C14 38 16 34 12.5 30.5Z", BLUE_DARK)
    return disc_ + blade

@reg("ishiiruka", PINK)
def ishiiruka():
    body = path("M13.5 32C18 24 27 19.5 36 20C43 20.5 48 25 50 32C51 36 50.5 40 49 43"
                "C47.5 37 44 31.5 37 29C31 27 24.5 28.5 19.5 32.5C18 33.5 15.5 33.5 13.5 32Z", INK)
    fin = poly([(29, 21), (34, 14.5), (38, 21)], INK, 2)
    waves = (stroke("M20 38.5C27 33 36 33.5 41 38", INK, 2.6)
             + stroke("M25 43.5C30 40.5 35 40.5 38 43", INK, 2.6))
    return body + fin + waves + circle(20, 29.5, 1.3, HOLE)

@reg("isomaster", GREY_DEEP)
def isomaster():
    cd = cut(cpath(30, 28, 15.5) + cpath(30, 28, 4.2), INK) + circle(30, 28, 7.5, GREY_SOFT) + circle(30, 28, 4.2, HOLE)
    badge = circle(42, 40, 9.5, HOLE) + circle(42, 40, 8, BLUE_DEEP)
    pen = line(38.5, 43.5, 45.5, 36.5, INK, 3.2) + poly([(36.2, 45.8), (37, 42), (40, 45)], INK, 0.8)
    return cd + badge + pen

@reg("it.mijorus.gearlever", GREY_DARK)
def gearlever():
    cog = gear(32, 35, 15, 11.5, 9, INK, .5, 2) + circle(32, 35, 5, HOLE)
    arrow_d = "M27 11H37V25H43L32 37L21 25H27Z"
    arrow = (path(arrow_d, HOLE, f' stroke="{HOLE}" stroke-width="6" stroke-linejoin="round"')
             + path(arrow_d, GREY_SOFT, ' stroke="#C0BFC0" stroke-width="2" stroke-linejoin="round"'))
    return cog + arrow

@reg("it.mijorus.smile", AMBER_LIGHT)
def smile():
    eyes = (circle(25, 22, 4.5, INK) + circle(39, 22, 4.5, INK)
            + circle(25.8, 22.5, 2, HOLE) + circle(39.8, 22.5, 2, HOLE))
    mouth = path("M16 31H48C48 40 41 46 32 46C23 46 16 40 16 31Z", INK)
    tongue = path("M24 42.5C27 39.5 37 39.5 40 42.5C37.5 44 35 44.5 32 44.5C29 44.5 26.5 44 24 42.5Z", RED)
    return eyes + mouth + tongue

@reg("itch", RED_LIGHT)
def itch():
    pad = path("M21 16C26 16 28 20 28 20H36C36 20 38 16 43 16C49 16 51 27 51 35C51 42 48 45 44.5 45"
               "C41 45 39.5 41 38 38H26C24.5 41 23 45 19.5 45C16 45 13 42 13 35C13 27 15 16 21 16Z", INK)
    arrow = path("M29.5 22H34.5V28H38.5L32 34L25.5 28H29.5Z", HOLE,
                 f' stroke="{HOLE}" stroke-width="1.5" stroke-linejoin="round"')
    return pad + arrow

@reg("itmages", BLUE)
def itmages():
    i = rrect(15, 14, 7, 32, 1.5, INK)
    t = rrect(25, 14, 24, 7, 1.5, INK) + rrect(33.5, 14, 7, 32, 1.5, INK)
    return i + t

@reg("iwgtk", BLUE_GREY)
def iwgtk():
    dot = circle(CX, 27, 3.6, INK)
    mast = poly([(30, 29), (34, 29), (35.5, 46), (28.5, 46)], INK, 1.5)
    arcs = (stroke(arc(CX, 27, 8, 140, 220), INK, 3.2) + stroke(arc(CX, 27, 8, -40, 40), INK, 3.2)
            + stroke(arc(CX, 27, 14.5, 135, 225), INK, 3.2) + stroke(arc(CX, 27, 14.5, -45, 45), INK, 3.2))
    return dot + mast + arcs

@reg("jabref", INDIGO_DEEP)
def jabref():
    j = stroke("M25 15V35C25 42 20 44.5 15.5 41.5", INK, 5)
    r = stroke("M31.5 44V15H38C43.5 15 46 18 46 22.5C46 27 43 29.5 38 29.5H33L48 45", INK, 5)
    return j + r

@reg("jack_mixer", GREY_DARK)
def jack_mixer():
    out = ""
    for x, k in [(21, 23), (32, 36), (43, 25)]:
        out += line(x, 14, x, 46, GREY_LIGHT, 3) + rrect(x - 6, k - 3.2, 12, 6.4, 2.5, INK)
    return out

@reg("jackpatch", GREY_DEEP)
def jackpatch():
    j = stroke("M25 15V35C25 42 20 44.5 15 41.5", INK, 5.5)
    p = stroke("M31.5 45V15H39C44.5 15 47.5 18.5 47.5 23C47.5 27.5 44.5 31 39 31H32", INK, 5.5)
    return j + p

@reg("jadx", DEEP_PURPLE_DEEP)
def jadx():
    j = stroke("M22 13V24C22 28 19 29.5 16 27.5", INK, 3.2)
    a = stroke("M26 29L32 13L38 29M28.2 23.5H35.8", INK, 3.2)
    d = stroke("M17 33H22C27 33 29 36.5 29 40C29 43.5 27 47 22 47H17Z", AMBER_SOFT, 3.2)
    x = stroke("M34 33L46 47M46 33L34 47", TEAL_SOFT, 3.2)
    return j + a + d + x

@reg("jamendo", PURPLE_DARK)
def jamendo():
    return circle(CX, CY, 16, INK) + poly([(28, 22), (40.5, 30), (28, 38)], HOLE, 3)

@reg("jamesdsp", DEEP_PURPLE_LIGHT)
def jamesdsp():
    frame = rrect(15, 14, 34, 32, 6, "none", f' stroke="{INK}" stroke-width="3.4"')
    out = frame
    for x, k in [(24, 25), (32, 37), (40, 29)]:
        out += line(x, 20, x, 40, INK, 3.2) + circle(x, k, 4.4, INK)
    return out

@reg("jami", LIGHT_BLUE_DEEP)
def jami():
    ring_ = f'<ellipse cx="32" cy="31" rx="18" ry="6.5" fill="none" stroke="{INK}" stroke-width="4.6"/>'
    d1 = line(20, 14, 44, 46, HOLE, 8.5, "butt") + line(20, 14, 44, 46, INK, 4.8)
    d2 = line(44, 14, 20, 46, HOLE, 8.5, "butt") + line(44, 14, 20, 46, INK, 4.8)
    fd = "M41 36.63A18 6.5 0 0 1 23 36.63"
    front = (f'<path d="{fd}" fill="none" stroke="{HOLE}" stroke-width="8.5"/>'
             f'<path d="{fd}" fill="none" stroke="{INK}" stroke-width="4.6"/>')
    return ring_ + d1 + d2 + front

@small("io.github.leonardschardijn.Chirurgien")
def chirurgien_s():
    out = ""
    for a in [-75, -48, -21]:
        hx, hy = pt(17, 46, 19, a)
        bx, by = pt(17, 46, 33, a)
        out += line(17, 46, hx, hy, INK, 3) + line(hx, hy, bx, by, INK, 5.5)
    return out

@small("io.github.tfuxu.Halftone")
def halftone_s():
    frame = rrect(13, 11, 38, 38, 5, INK) + rrect(18, 16, 28, 28, 2, HOLE)
    top = rrect(18, 16, 28, 12, 2, INK)
    dots = "".join(circle(x, 35, 2.6, INK) for x in [23, 32, 41])
    return frame + top + dots

@small("io.posidon.Paper")
def paper_s():
    sheet = _sheet(15, 11, 49, 49, 10, INK)
    band = path("M18 11H46A3 3 0 0 1 49 14V20H15V14A3 3 0 0 1 18 11Z", TEAL_DARK)
    lines = "".join(rrect(20, y, w, 4, 2, HOLE) for y, w in [(26, 24), (34, 16)])
    return sheet + band + lines

@small("jadx")
def jadx_s():
    return stroke("M24 13V32C24 38 20 40 15 37.5", INK, 5) + stroke("M29 47L38.5 14L48 47M32.5 36H44.5", INK, 5)

@small("io.gitlab.hamadmarri.gamma")
def gamma_s():
    return (stroke("M16 45V16H26", ORANGE_LIGHT, 6) + rrect(31, 15, 18, 7, 3.5, INK)
            + rrect(31, 26.5, 14, 7, 3.5, AMBER_SOFT) + rrect(31, 38, 18, 7, 3.5, INK))

@small("io.github.nokse22.minitext")
def minitext_s():
    return (rrect(12, 15, 40, 30, 5, INK) + rrect(17, 22, 22, 4.5, 2.25, HOLE)
            + rrect(17, 33, 30, 4.5, 2.25, HOLE))

@small("iridium-browser")
def iridium_s():
    globe = ring_b(34, 30, 15, INK, 3.6)
    shield = path("M13 18L26 13L39 18V29C39 37.5 33 43 26 47C19 43 13 37.5 13 29Z", INK,
                  f' stroke="{HOLE}" stroke-width="3" stroke-linejoin="round"')
    return globe + shield + circle(26, 28, 3.6, HOLE)

@small("io.github.lainsce.Emulsion")
def emulsion_s():
    out = ""
    for y, k in [(18, 38), (30, 24), (42, 32)]:
        out += line(15, y, 49, y, GREY_LIGHT, 4) + circle(k, y, 6, INK)
    return out

@small("io.github.mightycreak.Diffuse")
def diffuse_s():
    top = circle(38, 20, 10, INK) + stroke("M43 20H33M37.5 15.5L33 20L37.5 24.5", HOLE, 3.4)
    bot = circle(26, 40, 10, INK) + stroke("M21 40H31M26.5 35.5L31 40L26.5 44.5", HOLE, 3.4)
    return top + bot

@small("io.github.mpobaschnig.Vaults")
def vaults_s():
    return (rrect(13, 11, 38, 38, 5, INK) + rrect(18.5, 16.5, 27, 27, 3, HOLE)
            + line(24, 22, 40, 38, INK, 4) + line(40, 22, 24, 38, INK, 4))

@small("io.github.parnassius.SysDVR-Qt")
def sysdvr_s():
    body = rrect(12, 15, 40, 30, 10, INK)
    cast = (circle(24, 38, 3, HOLE) + stroke(arc(23, 39, 8, -90, 0), HOLE, 3.4)
            + stroke(arc(23, 39, 15, -90, 0), HOLE, 3.4))
    return body + cast

@small("io.github.realmazharhussain.GdmSettings")
def gdmsettings_s():
    panel = rrect(13, 11, 32, 36, 5, INK)
    user = circle(29, 22, 6, HOLE) + path("M19 38C19 32 23 30 29 30C35 30 39 32 39 38Z", HOLE)
    return panel + user

@small("io.github.seadve.Kooha")
def kooha_s():
    corners = stroke("M13 21V14H20M44 14H51V21M51 39V46H44M20 46H13V39", INK, 3.6)
    return corners + poly([(18, 23), (26, 30), (18, 37)], INK, 2.5) + rrect(27, 20, 20, 20, 4, INK)

@small("io.github.seadve.Mousai")
def mousai_s():
    heads = circle(22, 39, 6, INK) + circle(40, 39, 6, INK)
    stems = line(27, 39, 27, 17, INK, 4) + line(45, 39, 45, 17, INK, 4)
    return heads + stems + rrect(25, 13.5, 22, 6.5, 2, INK)

@small("io.github.swanux.hbud")
def hbud_s():
    return ring_b(CX, CY, 16, TEAL_SOFT, 3.6) + circle(28.5, 26.5, 7, INK) + stroke(arc(CX, CY, 10.5, 15, 100), INK, 4)

@small("io.gitlab.caveman250.headlines")
def headlines_s():
    return (path("M14 31H50A18 16 0 0 1 14 31Z", INK) + circle(25, 38, 3.2, HOLE) + circle(39, 38, 3.2, HOLE)
            + poly([(19, 12), (45, 12), (40, 28), (24, 28)], INK, 3))

@small("io.gitlab.idevecore.Pomodoro")
def pomodoro_s():
    body = circle(32, 32, 16, INK)
    leaves = path("M19 22C21 15 26 12 32 12C38 12 43 15 45 22L38 19L32 24L26 19Z", CYAN_DEEP,
                  ' stroke="#0096A9" stroke-width="2" stroke-linejoin="round"')
    return body + leaves + stroke(arc(32, 32, 9.5, -20, 60), HOLE, 3.6)

@small("io.gitlab.leesonwai.Sums")
def sums_s():
    left = rrect(13, 12, 19, 36, 4, INK)
    right = rrect(34, 12, 17, 36, 4, ORANGE_SOFT)
    plus = line(17.5, 30, 27.5, 30, HOLE, 4) + line(22.5, 25, 22.5, 35, HOLE, 4)
    eq = line(38, 26.5, 47, 26.5, ORANGE_DEEP, 4) + line(38, 33.5, 47, 33.5, ORANGE_DEEP, 4)
    return left + right + plus + eq

@small("ipython")
def ipython_s():
    blue = BLUE_LIGHT
    return (stroke("M19 17H14V43H19", blue, 4.4) + stroke("M45 17H50V43H45", blue, 4.4)
            + stroke("M23 22L32 36M41 22L29 45", INK, 4.8))

@small("irc-chat")
def irc_chat_s():
    front = path("M17 15H43A3 3 0 0 1 46 18V44A3 3 0 0 1 43 47H20A3 3 0 0 1 17 44V22L12 17Z", INK,
                 f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    hsh = (line(28, 20, 26, 42, HOLE, 3.6) + line(37, 20, 35, 42, HOLE, 3.6)
           + line(22, 27, 41, 27, HOLE, 3.6) + line(21.5, 35, 40.5, 35, HOLE, 3.6))
    return front + hsh

@small("isomaster")
def isomaster_s():
    cd = cut(cpath(30, 28, 16) + cpath(30, 28, 5), INK)
    badge = circle(42, 40, 10.5, HOLE) + circle(42, 40, 8.5, BLUE_DEEP)
    return cd + badge + line(38.5, 43.5, 45.5, 36.5, INK, 4)

@small("it.mijorus.gearlever")
def gearlever_s():
    cog = gear(32, 36, 15, 11, 8, INK, .5, 2) + circle(32, 36, 5, HOLE)
    arrow_d = "M26.5 10H37.5V24H44L32 37L20 24H26.5Z"
    return cog + path(arrow_d, HOLE, f' stroke="{HOLE}" stroke-width="5" stroke-linejoin="round"') + path(
        arrow_d, GREY_SOFT, ' stroke="#C0BFC0" stroke-width="2" stroke-linejoin="round"')

@small("itch")
def itch_s():
    pad = path("M21 15C26 15 28 19 28 19H36C36 19 38 15 43 15C49 15 52 27 52 35C52 42 49 46 45 46"
               "C41 46 39.5 42 38 39H26C24.5 42 23 46 19 46C15 46 12 42 12 35C12 27 15 15 21 15Z", INK)
    return pad + poly([(24.5, 25), (39.5, 25), (32, 34)], HOLE, 2.5)

@small("iwgtk")
def iwgtk_s():
    dot = circle(CX, 27, 4.2, INK)
    mast = poly([(29.5, 30), (34.5, 30), (36, 47), (28, 47)], INK, 1.5)
    arcs = stroke(arc(CX, 27, 10, 135, 225), INK, 4.2) + stroke(arc(CX, 27, 10, -45, 45), INK, 4.2)
    return dot + mast + arcs

@small("jamesdsp")
def jamesdsp_s():
    out = rrect(13, 12, 38, 36, 6, "none", f' stroke="{INK}" stroke-width="3.6"')
    for x, k in [(23, 25), (32, 36), (41, 28)]:
        out += line(x, 19, x, 41, INK, 3) + circle(x, k, 5, INK)
    return out

@small("jami")
def jami_s():
    x = line(20, 14, 44, 46, INK, 6) + line(44, 14, 20, 46, INK, 6)
    band = f'<ellipse cx="32" cy="31" rx="18" ry="7" fill="none" stroke="{INK}" stroke-width="5"/>'
    return x + band

@small("jabref")
def jabref_s():
    j = stroke("M24 14V35C24 42 19 45 14 42", INK, 6)
    r = stroke("M31 45V14H38.5C44 14 47 17.5 47 22.5C47 27.5 44 30.5 38.5 30.5H33L49 46", INK, 6)
    return j + r
