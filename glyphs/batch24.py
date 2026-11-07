# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 24: double-action-boogaloo to eid-viewer."""
from lm import *
from glyphs.kit import registry, _ring, _star_d

ICONS, SMALL, reg, small = registry()

@reg("double-action-boogaloo", AMBER_DEEP)
def double_action():
    d = stroke("M16 17V43H20.5C27 43 29.5 37 29.5 30C29.5 23 27 17 20.5 17Z", INK, 4.4)
    a = stroke("M34 43L41 17L48 43", INK, 4.4) + line(36.8, 34.5, 45.2, 34.5, INK, 4)
    return d + a

@reg("doublecmd", RED_DEEP)
def doublecmd():
    return (stroke("M14 18H18A9.5 12 0 0 1 18 42H14", INK, 5) +
            stroke("M50 18H46A9.5 12 0 0 0 46 42H50", INK, 5))

@reg("dusk", RED_DEEP)
def dusk():
    w = 3
    d = stroke("M14 23V37H16.3C19.8 37 21 34.2 21 30C21 25.8 19.8 23 16.3 23Z", INK, w)
    u = stroke("M24.5 23V33.3A3.5 3.7 0 0 0 31.5 33.3V23", INK, w)
    s = stroke("M41 24.8C40.2 23.6 39 23 37.6 23C35.6 23 34.4 24.3 34.4 26"
               "C34.4 30 41.2 29.2 41.2 33.6C41.2 35.8 39.6 37 37.5 37C36 37 34.8 36.4 34 35.4", INK, w)
    k = line(44.5, 23, 44.5, 37, INK, w) + stroke("M50 23L44.8 30.2L50 37", INK, w)
    return d + u + s + k

@reg("dying-light", DEEP_ORANGE_DEEP)
def dying_light():
    d = stroke("M18 16V44H21C27.5 44 30 38 30 30C30 22 27.5 16 21 16Z", INK, 5)
    l_ = stroke("M37 16V44H46", INK, 5)
    return d + l_

@reg("echomixer", RED)
def echomixer():
    w = 3
    e = stroke("M19.5 23H14.5V37H19.5", INK, w) + line(14.5, 30, 18.5, 30, INK, w)
    c = stroke("M29 24.5C28 23.5 27 23 25.8 23C23.5 23 22.5 26 22.5 30C22.5 34 23.5 37 25.8 37"
               "C27 37 28 36.5 29 35.5", INK, w)
    h = line(32.5, 23, 32.5, 37, INK, w) + line(38.5, 23, 38.5, 37, INK, w) + line(32.5, 30, 38.5, 30, INK, w)
    o = f'<ellipse cx="45.8" cy="30" rx="4.2" ry="7" fill="none" stroke="{INK}" stroke-width="{w}"/>'
    return e + c + h + o

@reg("eagle", ORANGE_DEEP)
def eagle():
    wing = path("M17 13C22 16 24 21 24 30C24 39 22 44 17 47C15 41 14.5 35 14.5 30"
                "C14.5 25 15 19 17 13Z", ORANGE_SOFT)
    e = stroke("M45 17H33C28 17 26 22 26 30C26 38 28 43 33 43H45", INK, 5) + line(30, 30, 42, 30, INK, 5)
    return wing + e

@reg("edex-ui", BLUE_GREY_DARK)
def edex_ui():
    frame = f'<rect x="16" y="14" width="32" height="32" rx="3" fill="none" stroke="{INK}" stroke-width="3.6"/>'
    e = stroke("M26 31H38.5C38.5 26 35.8 22.5 32 22.5C28 22.5 25.5 26 25.5 31"
               "C25.5 36 28 39 32.5 39C35 39 37 38 38.3 36.5", INK, 4)
    return frame + e

@reg("downline", BLUE)
def downline():
    return stroke("M43 17L22 38", INK, 6) + stroke("M21 23V39H37", INK, 6)

@reg("downloader-arrow", BLUE_GREY_LIGHT)
def downloader_arrow():
    return poly([(26, 13), (38, 13), (38, 27), (47, 27), (32, 45), (17, 27), (26, 27)], INK, 3)

@reg("dse", LIGHT_BLUE_DEEP)
def dse():
    return line(32, 13, 32, 35, INK, 5.5) + poly([(21, 32), (43, 32), (32, 46)], INK, 3)

@reg("dupeguru", DEEP_ORANGE_DEEP)
def dupeguru():
    down = poly([(19, 13), (27, 13), (27, 30), (32, 30), (23, 41), (14, 30), (19, 30)], INK, 2.5)
    up = poly([(37, 47), (45, 47), (45, 30), (50, 30), (41, 19), (32, 30), (37, 30)], DEEP_ORANGE_SOFT, 2.5)
    return up + down

@reg("dragon-ball-online-global", ORANGE_DEEP)
def dbo():
    ball = circle(CX, CY, 16.5, INK)
    stars = "".join(_star_d(x, y, 6.2, 2.7, RED) for x, y in
                    [(26, 23.5), (38, 23.5), (26, 36.5), (38, 36.5)])
    return ball + stars

@reg("dragon-ball-xenoverse", ORANGE_DEEP)
def dbx():
    stars = "".join(_star_d(x, y, 5.2, 2.2, INK) for x, y in [(19, 17.5), (32, 15.5), (45, 17.5)])
    xv = (line(18, 27, 29, 44, INK, 4.4) + line(29, 27, 18, 44, INK, 4.4) +
          stroke("M35 27L40.5 44L46 27", INK, 4.4))
    return stars + xv

@reg("dragonframe4", BLUE_GREY)
def dragonframe():
    half = [(32, 15), (27, 11), (27.5, 18), (21, 13), (23, 21), (16, 20), (22, 27),
            (19, 31), (25, 33), (27, 42), (32, 49)]
    pts = half + [(64 - x, y) for x, y in reversed(half[1:-1])]
    head = poly(pts, BLUE_GREY_DARK, 2)
    eyes = (poly([(24, 27), (29.5, 29.5), (26, 31)], BLUE_GREY_SOFT, 1) +
            poly([(40, 27), (34.5, 29.5), (38, 31)], BLUE_GREY_SOFT, 1))
    return head + eyes

@reg("dragonplayer", DEEP_PURPLE_DARK)
def dragonplayer():
    head = path("M14 27C17 22 22 19 28 18L38 11L35 19C41 20 46 24 48 30"
                "C44 27 40 26 36 27C38 30 38 34 36 37C33 33 28 31 23 31L16 32Z", INK)
    eye = circle(29, 23.5, 1.8, HOLE)
    waves = (stroke("M16 38C21 34 26 34 30 38C34 42 40 42 48 36", TEAL_SOFT, 4) +
             stroke("M20 45C24 42.5 28 42.5 31.5 45C35 47.5 40 47.5 44 45", TEAL_SOFT, 3.4))
    return head + eye + waves

@reg("draw.io", ORANGE_DEEP)
def drawio():
    lines = stroke("M32 22L21 36M32 22L43 36", INK, 2.8)
    return (lines + rrect(25, 12, 14, 11, 3, INK) +
            rrect(14, 35, 14, 11, 3, INK) + rrect(36, 35, 14, 11, 3, INK))

@reg("driconf", BLUE_DEEP)
def driconf():
    lines = stroke("M21 20L42 25M21 20L28 41M42 25L28 41", INK, 2.8)
    return (lines + rrect(14, 14, 15, 11, 3, INK) +
            rrect(36, 19, 14, 11, 3, INK) + rrect(21, 36, 13, 10, 3, INK))

@reg("eeschema", PURPLE_SOFT)
def eeschema():
    wires = stroke("M27 14V46M27 30H47M27 36L17 44", INK, 2.8)
    dots = "".join(circle(x, y, 3.6, YELLOW_LIGHT) for x, y in [(27, 14), (27, 30), (47, 30), (27, 46), (17, 44)])
    return wires + dots

@reg("drawpile", CYAN_DEEP)
def drawpile():
    globe = circle(32, 30, 15, INK)
    land = (path("M22 22C25 20 28 21 28 24C28 27 24 27 24 30C24 33 21 33 19.5 30C19 26 20 23.5 22 22Z", CYAN_SOFT) +
            path("M37 33C40 31.5 43 33 42.5 36C42 39 38.5 41 36 40C34.5 38 34.8 34.5 37 33Z", CYAN_SOFT))
    pencil = line(15, 44, 45, 17, BLUE_GREY_DARK, 5.5) + poly([(45, 17), (50, 12), (48.3, 19.2)], BLUE_GREY_DARK, 1.5)
    return globe + land + pencil

@reg("drill-search-gtk", GREY_DEEP)
def drill():
    chuck = rrect(20, 12, 24, 7, 2, INK)
    bit = poly([(22, 21), (42, 21), (32, 48)], INK, 2)
    cuts = (line(24, 24.5, 40, 29, HOLE, 2.2) + line(26.5, 31, 37.8, 34.5, HOLE, 2.2) +
            line(29, 37.5, 35.5, 39.5, HOLE, 2.2))
    return chuck + bit + cuts

@reg("droidcam", GREY_DEEP)
def droidcam():
    dome = path("M20 23A12 10.5 0 0 1 44 23Z", INK)
    ants = line(23.5, 13, 26, 16.5, INK, 2.2) + line(40.5, 13, 38, 16.5, INK, 2.2)
    eyes = circle(27, 19.5, 1.5, HOLE) + circle(37, 19.5, 1.5, HOLE)
    body = rrect(20, 25, 24, 20, 4, INK)
    arms = rrect(14, 25, 4.5, 14, 2.25, INK) + rrect(45.5, 25, 4.5, 14, 2.25, INK)
    lens = circle(32, 34.5, 7, HOLE) + circle(32, 34.5, 4.5, INK) + circle(32, 34.5, 2, HOLE)
    return dome + ants + eyes + body + arms + lens

@reg("drweb-gui", PURPLE_SOFT)
def drweb():
    base = circle(CX, CY, 16.5, INK)
    body = f'<ellipse cx="32" cy="33" rx="5.5" ry="7.5" fill="{HOLE}"/>' + circle(32, 23.5, 3.8, HOLE)
    legs = ""
    for s in (1, -1):
        for d in ["M27 28L21 23L19 19", "M26.5 32L19 31", "M27 36L21 38L19 42", "M28.5 39.5L25 44"]:
            legs += g(stroke(d, HOLE, 2.2), f"translate(64 0) scale(-1 1)") if s < 0 else stroke(d, HOLE, 2.2)
    return base + legs + body

@reg("ds9", LIGHT_BLUE_DEEP)
def ds9():
    pts = [pt(CX, CY, 16.5 if k % 2 == 0 else 10, -90 + 15 * k) for k in range(24)]
    return poly(pts, AMBER_SOFT, 1) + circle(CX, CY, 9.5, AMBER)

@reg("dsda-doom", BLUE_GREY)
def dsda():
    goose = path("M19 14C22 13 24.5 15 24.5 18C24.5 22 22 25 23 29C25 31 30 29.5 36 28"
                 "L47 18C48.5 24 47 30 44 33C45.5 36 44 40 40 42C34 44.5 25 43 21 39"
                 "C17 35 17 28 18 23C18 21 17 20 15.5 20.5L13 20C14 17 16 14.5 19 14Z", INK)
    beak = poly([(13, 19.5), (18, 18), (18, 21.5)], ORANGE, 1.5)
    feet = stroke("M27 42.5L25 48M34 43.5L35 48", ORANGE, 2.6)
    eye = circle(20.5, 17.5, 1.3, HOLE)
    return feet + goose + beak + eye

@reg("duckduckgo", DEEP_ORANGE_DEEP)
def duckduckgo():
    ring = _ring(CX, CY, 15.2, INK, 2.6)
    duck = path("M24 20C26 16.5 31 15 35 17C39 19 40 23 39 27C38 30 37 32 38 36"
                "C38.5 40 37 44 33.5 44.8C30 45.5 26.5 44 25 40.5C23.5 36.5 25 33 23.5 29"
                "C22 26 22.5 22.5 24 20Z", INK)
    eye = circle(33, 22.5, 1.9, BLUE_GREY_DARK)
    beak = path("M36 26.5C39.5 25.5 43 26.5 43.5 28C43 29.5 39.5 30.2 36.5 29.5Z", AMBER)
    bow = poly([(29, 35), (33, 37), (29, 39)], AMBER_DEEP, 1.2) + poly([(37, 35), (33, 37), (37, 39)], AMBER_DEEP, 1.2)
    return ring + duck + eye + beak + bow

@reg("duckstation", ORANGE_DEEP)
def duckstation():
    head = rrect(28, 12, 13, 13, 1.5, INK)
    beak = rrect(40, 18, 8, 5, 1.5, RED)
    body = rrect(18, 25, 23, 14, 1.5, INK)
    tail = rrect(14, 21, 7, 7, 1.5, INK)
    wing = rrect(22, 29, 11, 6, 1, ORANGE_SOFT)
    legs = rrect(24, 39, 4, 7, 1, RED) + rrect(33, 39, 4, 7, 1, RED)
    eye = rrect(35, 16, 3, 3, .5, HOLE)
    return legs + tail + body + head + beak + wing + eye

@reg("dukto", CYAN_DEEP)
def dukto():
    pipe = rrect(20, 23, 24, 25, 1.5, INK) + rrect(15, 12, 34, 11, 2.5, INK)
    return pipe + line(20, 23, 44, 23, HOLE, 2)

@reg("duolingo", PURPLE_SOFT)
def duolingo():
    body = path("M17 17L22 19C25 17.5 28.5 16.8 32 16.8C35.5 16.8 39 17.5 42 19L47 17"
                "C47.8 21 48 26 48 31C48 40 41 46 32 46C23 46 16 40 16 31C16 26 16.2 21 17 17Z", INK)
    eyes = (circle(25.5, 29, 6, HOLE) + circle(38.5, 29, 6, HOLE) +
            circle(26.5, 30, 3, INK) + circle(37.5, 30, 3, INK))
    beak = poly([(29.5, 35.5), (34.5, 35.5), (32, 39.5)], AMBER, 2)
    return body + eyes + beak

@reg("duplicati", BLUE_DEEP)
def duplicati():
    big = rrect(24, 13, 26, 21, 4, INK) + rrect(27.5, 16.5, 19, 14, 2, BLUE_DARK)
    small_ = rrect(12, 28, 22, 18, 4, HOLE) + rrect(14, 30, 18, 14, 3, INK) + rrect(17, 33, 12, 8, 1.5, BLUE_LIGHT)
    return big + small_

@reg("duskplayer", PINK_DEEP)
def duskplayer():
    band = stroke("M18 37V31A14 14 0 0 1 46 31V37", INK, 5)
    cups = rrect(13.5, 31, 9, 15, 4, INK) + rrect(41.5, 31, 9, 15, 4, INK)
    pads = rrect(17, 33.5, 5, 10, 2.5, PINK_SOFT) + rrect(42, 33.5, 5, 10, 2.5, PINK_SOFT)
    return band + cups + pads

@reg("dust3d", GREY_DARK)
def dust3d():
    head = path("M14 26C17 21.5 23 19 29 19.5C35 20 39 18 44 17C47 23 49 32 49 42"
                "C45 38 41 34.5 37 32.5C32 33.5 26 33 21 31.5C17.5 30.5 14.5 28.5 14 26Z", INK)
    return head + circle(24, 24.5, 1.6, HOLE)

@reg("dvanalyzer", ORANGE_DEEP)
def dvanalyzer():
    dot = circle(30.5, 17, 5, INK)
    p = _ring(34, 33, 6.3, INK, 4.2) + line(27.7, 33, 27.7, 46, INK, 4.2)
    return dot + p

@reg("dvdisaster", BLUE_GREY)
def dvdisaster():
    disc = cut(cpath(29, 28, 15) + cpath(29, 28, 3), INK) + _ring(29, 28, 6, BLUE_GREY_SOFT, 3)
    badge = circle(42.5, 39.5, 8.5, INDIGO)
    bang = line(42.5, 35, 42.5, 40.5, INK, 3) + circle(42.5, 44.3, 1.6, INK)
    return disc + circle(42.5, 39.5, 10.5, HOLE) + badge + bang

@reg("eBook-speaker", PURPLE_DEEP)
def ebook_speaker():
    sheet = rrect(20, 15, 27, 34, 3, INK)
    lines = "".join(rrect(30, y, 13, 2.6, 1.3, HOLE) for y in (22, 27.5)) + \
        "".join(rrect(24, y, 19, 2.6, 1.3, HOLE) for y in (33, 38.5))
    bubble = rrect(13, 11, 17, 14, 3.5, HOLE) + rrect(14.5, 12.5, 14, 11, 2.5, PURPLE_SOFT)
    spk = poly([(17.5, 16), (19.5, 16), (22.5, 13.8), (22.5, 21.2), (19.5, 19), (17.5, 19)], INK, 1)
    wave = stroke("M25 15.5C26 16.5 26 18.5 25 19.5", INK, 1.8)
    return sheet + lines + bubble + spk + wave

@reg("ease", DEEP_ORANGE)
def ease():
    sheet = rrect(18, 13, 28, 34, 4, INK)
    pie = path("M27 20A6 6 0 1 0 33 26H27Z", HOLE)
    bars = rrect(34.5, 20, 7.5, 2.8, 1.4, HOLE) + rrect(34.5, 25.5, 7.5, 2.8, 1.4, HOLE) + rrect(22, 35, 20, 2.8, 1.4, HOLE)
    return sheet + pie + bars

@reg("easy-ebook-viewer", BLUE_DEEP)
def easy_ebook():
    book = path("M32 21C27 17 21 16 14.5 17V42C21 41 27 42 32 46C37 42 43 41 49.5 42V17"
                "C43 16 37 17 32 21Z", INK)
    spine = line(32, 22.5, 32, 43, HOLE, 2.4)
    head = circle(32, 14, 4.2, BLUE_SOFT)
    return book + spine + head

@reg("easyeda", BLUE)
def easyeda():
    cloud = path("M20.5 42C16 42 13 38.5 13 34.5C13 30.5 16 27.5 20 27.5C20.5 21 25.5 16.5 32 16.5"
                 "C37.5 16.5 42 20 43.5 25C48 25.5 51 29 51 33.5C51 38 47.5 42 43 42Z", INK)
    trace = stroke("M29.5 35H40V28", HOLE, 3.2) + circle(26, 35, 4, HOLE) + circle(26, 35, 1.8, INK)
    return cloud + trace

@reg("easymp3gain", GREY_DEEP)
def easymp3gain():
    note = (circle(20.5, 39, 5, INK) + line(24.3, 39, 24.3, 18, INK, 3.4) +
            stroke("M24.3 18L43 13V22", INK, 3.4))
    badge = circle(40, 37, 11, HOLE) + circle(40, 37, 9, GREY_SOFT)
    bars = "".join(rrect(33.5 + 3.6 * k, 41 - h, 2.4, h, 1.2, GREY_DARK)
                   for k, h in enumerate([3, 5, 7.5, 10]))
    return note + badge + bars

@reg("easystroke", INDIGO)
def easystroke():
    loops = "".join(g(f'<ellipse cx="32" cy="23" rx="7" ry="10" fill="none" stroke="{INK}" stroke-width="3.2"/>',
                      f"rotate({120 * k} 32 31)") for k in range(3))
    return loops

@reg("easytag", BLUE_LIGHT)
def easytag():
    tag = poly([(32, 11), (43, 20), (43, 47), (21, 47), (21, 20)], INK, 3)
    hole = circle(32, 19.5, 2.6, HOLE)
    e = stroke("M26.8 35H37.2C37.2 31.2 35.2 28.5 32 28.5C28.7 28.5 26.8 31.3 26.8 35"
               "C26.8 38.8 28.9 41.5 32.3 41.5C34.4 41.5 36 40.7 37 39.4", HOLE, 3.2)
    return g(tag + hole + e, "rotate(-35 32 30) translate(32 30) scale(.92) translate(-32 -30)")

@reg("echonest", BLUE_GREY_DARK)
def echonest():
    c = stroke("M45 23.5A15 15 0 1 0 45 36.5", INK, 5.5)
    inner = stroke("M25.5 30A6.5 6.5 0 0 1 38.5 30", LIGHT_BLUE_LIGHT, 4)
    return c + inner

@reg("eclipse", DEEP_PURPLE_DARK)
def eclipse():
    moon = cut(cpath(31, 30, 17) + cpath(34, 30, 15), ORANGE)
    disc = circle(34, 30, 13.5, DEEP_PURPLE_LIGHT)
    bands = "".join(rrect(20.5, y, 27, 2.8, 1.4, INK) for y in (23, 28.6, 34.2))
    return moon + disc + bands

@reg("eclipse-cdt", DEEP_PURPLE_DARK)
def eclipse_cdt():
    moon = cut(cpath(25, 30, 13) + cpath(27.5, 30, 11.2), ORANGE)
    c = stroke("M32.5 25A7 7 0 1 0 32.5 35", INK, 3.8)
    plus = "".join(line(x - 3.2, 30, x + 3.2, 30, INK, 2.6) + line(x, 26.8, x, 33.2, INK, 2.6) for x in (39.5, 47.5))
    return moon + c + plus

@reg("eco", BLUE_DEEP)
def eco():
    globe = circle(CX, CY, 16.5, CYAN)
    sea = path("M18 22H22V18H30V14.6A16.5 16.5 0 0 0 16.2 25.5V26H18Z", HOLE) + \
        rrect(33, 20, 6, 4, 0, HOLE) + rrect(24, 30, 5, 5, 0, HOLE) + rrect(38, 37, 7, 4, 0, HOLE)
    return globe + sea + circle(33.5, 17.5, 2.2, INK)

@reg("edb-debugger", BLUE_DARK)
def edb():
    arcs = (stroke("M15 44C19 29 31 20 48 16", INK, 3.4) +
            stroke("M20 44C24 33 33 26 47 23.5", INK, 3.2) +
            stroke("M25 44C28.5 37.5 35 32.5 45 31", INK, 3))
    return arcs

@reg("edge-game", DEEP_PURPLE)
def edge_game():
    hexa = poly([pt(CX, CY, 17, -90 + 60 * k) for k in range(6)], INK, 3)
    top = poly([(32, 20), (41, 25), (32, 30), (23, 25)], PINK_SOFT, 1.5)
    left = poly([(23, 25), (32, 30), (32, 41), (23, 36)], PINK_LIGHT, 1.5)
    right = poly([(41, 25), (32, 30), (32, 41), (41, 36)], PINK_DEEP, 1.5)
    return hexa + top + left + right

@reg("edu.stanford.Almond", ORANGE_DEEP)
def almond():
    nut = path("M32 12C38.5 12 44.5 24 44.5 34C44.5 42 39.5 47 32 47C24.5 47 19.5 42 19.5 34"
               "C19.5 24 25.5 12 32 12Z", INK)
    face = (stroke("M25.5 33.5Q27.5 31.5 29.5 33.5", HOLE, 2.2) +
            stroke("M34.5 33.5Q36.5 31.5 38.5 33.5", HOLE, 2.2) +
            stroke("M29 38.5Q32 41 35 38.5", HOLE, 2.2))
    return nut + face

@reg("eekboard", BLUE_GREY_DARK)
def eekboard():
    board = rrect(13, 17, 38, 27, 4.5, INK)
    keys = "".join(rrect(17 + 6.2 * c, 21 + 6 * r, 4.4, 4, 1, HOLE) for r in range(2) for c in range(5))
    return board + keys + rrect(22, 34.5, 20, 4.5, 1.5, HOLE)

@reg("eiciel", LIGHT_BLUE_DEEP)
def eiciel():
    head = circle(32, 18, 6.5, INK)
    body = path("M32 26C38 26 41 31 42.5 37L45 47H19L21.5 37C23 31 26 26 32 26Z", INK)
    e = stroke("M27.5 38.5H36.5C36.5 35.2 34.8 33 32 33C29.2 33 27.5 35.4 27.5 38.5"
               "C27.5 41.8 29.3 44 32.2 44C34 44 35.3 43.3 36.2 42.2", HOLE, 2.8)
    return head + body + e

@reg("eid-viewer", BLUE_GREY)
def eid_viewer():
    card = rrect(13, 17, 38, 27, 4, INK)
    person = circle(43, 26, 3.5, BLUE_GREY_SOFT) + path("M36.5 38C36.5 33 39.5 31 43 31C46.5 31 49 33 49 38Z", BLUE_GREY_SOFT)
    glass = _ring(26, 28.5, 6, HOLE, 3.2) + line(30.5, 33, 35, 37.5, HOLE, 3.6)
    return card + person + glass

@small("dusk")
def dusk_s():
    return stroke("M20 16V44H24C33 44 36 38 36 30C36 22 33 16 24 16Z", INK, 5.5)

@small("echomixer")
def echomixer_s():
    return stroke("M42 17H24V43H42", INK, 5.5) + line(24, 30, 38, 30, INK, 5.5)

@small("drweb-gui")
def drweb_s():
    base = circle(CX, CY, 16.5, INK)
    legs = "".join(stroke(d, HOLE, 3) + g(stroke(d, HOLE, 3), "translate(64 0) scale(-1 1)")
                   for d in ["M27 28L20 21", "M27 38L20 43"])
    return base + legs + f'<ellipse cx="32" cy="32" rx="6.5" ry="9" fill="{HOLE}"/>' + circle(32, 22, 4, HOLE)

@small("eBook-speaker")
def ebook_speaker_s():
    sheet = rrect(20, 15, 27, 34, 3, INK)
    lines = "".join(rrect(24, y, 19, 4, 2, HOLE) for y in (30, 38))
    bubble = rrect(12, 10, 19, 16, 4, HOLE) + rrect(14, 12, 15, 12, 3, PURPLE_SOFT)
    spk = poly([(17, 15.5), (20, 15.5), (24, 13), (24, 23), (20, 20.5), (17, 20.5)], INK, 1)
    return sheet + lines + bubble + spk

@small("easymp3gain")
def easymp3gain_s():
    note = circle(20.5, 39, 6, INK) + line(25, 39, 25, 16, INK, 4) + stroke("M25 16L43 12V21", INK, 4)
    return note + circle(40, 37, 11.5, HOLE) + circle(40, 37, 9.5, LIGHT_BLUE_SOFT)

@small("eekboard")
def eekboard_s():
    board = rrect(12, 16, 40, 29, 5, INK)
    keys = "".join(rrect(17 + 11 * c, 21, 8, 6, 1.5, HOLE) for c in range(3))
    return board + keys + rrect(21, 33, 22, 6, 2, HOLE)

@small("eid-viewer")
def eid_viewer_s():
    return rrect(12, 16, 40, 29, 5, INK) + _ring(28, 29, 7, HOLE, 4) + line(33, 34, 38, 39, HOLE, 4.5)

@small("dragon-ball-online-global")
def dbo_s():
    return circle(CX, CY, 17, INK) + _star_d(CX, CY, 10, 4.5, RED)

@small("dragon-ball-xenoverse")
def dbx_s():
    return (line(15, 16, 29, 44, INK, 6) + line(29, 16, 15, 44, INK, 6) +
            stroke("M35 16L42 44L49 16", INK, 6))

@small("droidcam")
def droidcam_s():
    dome = path("M19 22A13 11 0 0 1 45 22Z", INK)
    body = rrect(19, 24, 26, 22, 4, INK)
    return dome + body + circle(32, 35, 7, HOLE) + circle(32, 35, 3.5, INK)

@small("drill-search-gtk")
def drill_s():
    return (rrect(19, 11, 26, 8, 2, INK) + poly([(21, 21), (43, 21), (32, 49)], INK, 2) +
            line(24.5, 26, 39.5, 31, HOLE, 3.2))

@small("duckduckgo")
def duckduckgo_s():
    return (circle(CX, CY, 16.5, INK) + circle(29, 26, 8, HOLE) + circle(31, 24, 2.2, INK) +
            path("M34 30C39 28.5 44 29.5 44 31.5C43 33.5 38.5 34 34.5 33Z", AMBER))

@small("eclipse")
def eclipse_s():
    moon = cut(cpath(31, 30, 17.5) + cpath(34.5, 30, 15), ORANGE)
    disc = circle(34.5, 30, 14, DEEP_PURPLE_LIGHT)
    return moon + disc + rrect(20.5, 23, 28, 4, 2, INK) + rrect(20.5, 32.5, 28, 4, 2, INK)

@small("eclipse-cdt")
def eclipse_cdt_s():
    moon = cut(cpath(27, 30, 16) + cpath(30, 30, 13.5), ORANGE)
    return moon + stroke("M37 23A9 9 0 1 0 37 37", INK, 5)

@small("easytag")
def easytag_s():
    tag = poly([(32, 11), (43, 20), (43, 47), (21, 47), (21, 20)], INK, 3)
    e = stroke("M26 35H38C38 30.5 35.7 27.5 32 27.5C28.3 27.5 26 30.5 26 35"
               "C26 39.5 28.5 42.5 32.3 42.5C34.7 42.5 36.5 41.5 37.6 40", HOLE, 4)
    return g(tag + e, "rotate(-35 32 30)")

@small("dvdisaster")
def dvdisaster_s():
    disc = cut(cpath(29, 28, 16) + cpath(29, 28, 4), INK)
    return disc + circle(43, 41, 10, HOLE) + circle(43, 41, 8.5, INDIGO) + line(43, 37, 43, 45, INK, 4)

@small("edb-debugger")
def edb_s():
    return stroke("M15 45C19 29 31 20 48 15", INK, 4.4) + stroke("M24 45C28 35.5 35 30 47 27", INK, 4.4)

@small("dragonplayer")
def dragonplayer_s():
    head = path("M14 27C17 22 22 19 28 18L38 11L35 19C41 20 46 24 48 30"
                "C44 27 40 26 36 27C38 30 38 34 36 37C33 33 28 31 23 31L16 32Z", INK)
    return head + stroke("M16 41C21 36.5 26 36.5 30 41C34 45.5 40 45.5 48 39", TEAL_SOFT, 5)
