# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 68: the-stanley-parable to tokodon.

Same rules as batch01: tile is the palette step nearest the brand colour,
the mark is INK, HOLE is the tile showing through, extra shades come
from the palette.
"""
from lm import *
from glyphs.kit import gear_k, registry, _ring

ICONS, SMALL, reg, small = registry()

@reg("the-stanley-parable", GREY_DARK)
def stanley():
    jacket = path("M24 14L32 20L40 14C45 16 49 19 50 23L48 48H16L14 23C15 19 19 16 24 14Z", INK)
    shirt = poly([(25.5, 15.5), (38.5, 15.5), (32, 37)], HOLE, 2)
    tie = poly([(30, 19), (34, 19), (35, 31), (32, 35), (29, 31)], RED, 1.5)
    return jacket + shirt + tie

@reg("the-swapper", DEEP_PURPLE_DEEP)
def swapper():
    helmet = path("M15 32C15 20 22.5 13 32 13C41.5 13 49 20 49 32V38C49 43 45.5 46 41 46H23"
                  "C18.5 46 15 43 15 38Z", INK)
    visor = rrect(18.5, 27, 27, 11, 5.5, HOLE)
    return helmet + visor + rrect(38, 27, 3.5, 11, 0, INK)

@reg("the-talos-principle", AMBER_DEEP)
def talos():
    return (_ring(32, 30, 14.5, INK, 4.4) + line(24.5, 24, 24.5, 36, INK, 4) +
            line(39.5, 24, 39.5, 36, INK, 4) + line(24.5, 28.5, 39.5, 28.5, INK, 4.4))

def _wolf(eye):
    head = poly([(16, 11), (25, 19), (39, 19), (48, 11), (47, 22), (52, 27), (44.5, 30.5),
                 (41, 38), (37.5, 48), (26.5, 48), (23, 38), (19.5, 30.5), (12, 27), (17, 22)], INK, 2.2)
    eyes = (poly([(22, 25), (29.5, 27.5), (27, 30)], eye, 1.5) +
            poly([(42, 25), (34.5, 27.5), (37, 30)], eye, 1.5))
    mouth = poly([(27.5, 36), (36.5, 36), (35, 45.5), (29, 45.5)], HOLE, 2)
    fangs = poly([(28, 35.5), (30.5, 35.5), (29.2, 40)], INK, .8) + poly([(33.5, 35.5), (36, 35.5), (34.8, 40)], INK, .8)
    return head + eyes + mouth + fangs

@reg("the-witcher", RED_DEEP)
def witcher():
    return _wolf(ORANGE)

@reg("the-witcher-2", AMBER_DARK)
def witcher2():
    return _wolf(ORANGE)

@reg("the-witcher-3", BLUE_GREY)
def witcher3():
    return _wolf(RED)

@reg("thedarkmod", BROWN_DEEP)
def thedarkmod():
    return gear_k(32, 30, 15, INK, HOLE, 16, 11.5) + gear_k(32, 30, 6.5, INK, HOLE, 8, 2.6)

@reg("thextech", BLUE_DEEP)
def thextech():
    cap = path("M14 30C14 19.5 22 13 32 13C42 13 50 19.5 50 30A2.5 2.5 0 0 1 47.5 32.5H16.5A2.5 2.5 0 0 1 14 30Z", INK)
    x = line(26.5, 17.5, 37.5, 28.5, HOLE, 4) + line(37.5, 17.5, 26.5, 28.5, HOLE, 4)
    stem = rrect(22.5, 35, 19, 13, 5, INK)
    eyes = rrect(27, 37.5, 3, 6, 1.5, HOLE) + rrect(34, 37.5, 3, 6, 1.5, HOLE)
    return cap + x + stem + eyes

@reg("thimbleweed-park", TEAL_DARK)
def thimbleweed():
    trees = (poly([(19, 14), (24.5, 30), (13.5, 30)], INK, 2) + poly([(19, 21), (25.5, 40), (12.5, 40)], INK, 2) +
             poly([(28, 22), (32, 34), (24, 34)], INK, 2) + poly([(28, 27), (33, 42), (23, 42)], INK, 2))
    sign = rrect(34, 21, 17, 12, 2.5, INK) + rrect(37, 24, 11, 6, 1.5, HOLE)
    post = rrect(40.5, 33, 3.5, 12, 1, INK)
    return trees + sign + post + rrect(13, 44, 38, 3.5, 1.75, INK)

def _tag(fill):
    pts = [(0, 0), (9, -9.5), (25, -9.5), (25, 9.5), (9, 9.5)]
    return poly(pts, fill, 3)

@reg("thingy", RED)
def thingy():
    back = g(stroke("M9 -9.5H25V9.5H9L0 0Z", INK, 3), "translate(21.5 13) rotate(45)")
    front = g(_tag(INK) + circle(8, 0, 2.6, HOLE), "translate(15.5 15.5) rotate(45)")
    halo = g(stroke("M9 -9.5H25V9.5H9L0 0Z", HOLE, 3), "translate(15.5 15.5) rotate(45)")
    return back + halo + front

@reg("thinkorswim", BLUE_DARK)
def thinkorswim():
    out = ""
    for k in range(14):
        a = k * 360 / 14 + 8
        r = 17 if k % 2 == 0 else 11.5
        tip = pt(32, 30, 3.5, a)
        b1 = pt(32, 30, r, a - 7)
        b2 = pt(32, 30, r, a + 7)
        out += poly([tip, b1, b2], INK, 1)
    return out

@reg("thomas-was-alone", TEAL_DARK)
def thomas():
    return (rrect(13, 42, 38, 5, 2.5, INK) + rrect(28, 24, 8, 18, 1, RED_LIGHT) +
            poly([(28, 14.5), (36, 14.5), (32, 19.5)], INK, 1.5))

def _th(w=5):
    return (line(16.5, 17, 32.5, 17, INK, w) + line(24.5, 17, 24.5, 43, INK, w) +
            stroke("M38 15V43M38 31C38 27 40.5 25 43 25C45.5 25 48 27 48 31V43", INK, w))

@reg("thonny", GREY_DARK)
def thonny():
    return _th()

@reg("thorium", BLUE)
def thorium():
    return _th(5.5)

@reg("thorium-browser", BLUE_LIGHT)
def thorium_browser():
    return circle(32, 30, 16.5, INK) + circle(32, 30, 10, HOLE) + circle(32, 30, 7, BLUE_DARK)

@reg("tic80", BLUE)
def tic80():
    face = rrect(15, 14, 30, 30, 7, INK)
    eyes = rrect(22, 20, 4, 9, 2, HOLE) + rrect(34, 20, 4, 9, 2, HOLE)
    smile = stroke("M22 35.5H38", HOLE, 3.4)
    plug = stroke("M45 29H48.5V39", INK, 3.4)
    return face + eyes + smile + plug

def _tidal():
    return "".join(g(rrect(cx - 3.9, cy - 3.9, 7.8, 7.8, 1, INK), f"rotate(45 {cx} {cy})")
                   for cx, cy in [(21, 25), (32, 25), (43, 25), (32, 36)])

@reg("tidal", GREY_SOFT)
def tidal():
    return _tidal()

@reg("tidal-hifi", BLUE_GREY_DARK)
def tidal_hifi():
    return _tidal()

@reg("tigervnc", ORANGE_DEEP)
def tigervnc():
    stripes = (stroke("M15 21C22 14 32 13 44 16", INK, 3.6) +
               stroke("M20 44C28 46.5 38 45 46 38", INK, 3.6))
    eye = path("M14 30C20 22 44 22 50 30C44 38 20 38 14 30Z", INK)
    iris = circle(32, 30, 6, CYAN_DARK) + f'<ellipse cx="32" cy="30" rx="1.7" ry="4.6" fill="{BLACK}"/>'
    return stripes + eye + iris

@reg("tiktok", BLUE_GREY_DARK)
def tiktok():
    return (stroke("M34 14V35.5A7 7 0 1 1 27 28.5", INK, 5) +
            stroke("M34 14.5C34.5 19.5 38.5 23 44 23", INK, 5))

@reg("tiled", INDIGO_LIGHT)
def tiled():
    cells = [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)]
    return "".join(rrect(18 + c * 10, 15 + r * 10, 8.5, 8.5, 2, INK) for c, r in cells)

@reg("tilem", BLUE_GREY_DEEP)
def tilem():
    body = rrect(18, 11, 28, 38, 6, INK)
    screen = rrect(21.5, 14.5, 21, 15, 3, BLUE_GREY_SOFT)
    keys = "".join(rrect(22 + c * 7, 33 + r * 6, 5.5, 4, 1.5, HOLE) for r in range(2) for c in range(3))
    return body + screen + keys

@reg("tilesetter", GREY_DARK)
def tilesetter():
    c = stroke("M28.5 17H18V25.5L21 30L18 34.5V43H28.5", INK, 5)
    t = line(33, 17, 47, 17, INK, 5) + line(42, 17, 42, 43, INK, 5)
    return c + t

@reg("tilix", BLUE_GREY_DARK)
def tilix():
    out = ""
    for x in (14, 33):
        out += rrect(x, 16, 17, 28, 3, INK)
        out += stroke(f"M{x + 3.5} 23L{x + 7.5} 27L{x + 3.5} 31", HOLE, 2.6)
        out += line(x + 9.5, 31, x + 13, 31, HOLE, 2.6)
    return out

@reg("tilp", BLUE_GREY)
def tilp():
    calc = rrect(19, 11, 26, 38, 6, INK) + rrect(22.5, 14.5, 19, 12, 3, BLUE_GREY_SOFT)
    keys = "".join(rrect(23 + c * 6.5, 30 + r * 5.5, 4.5, 3.5, 1.5, HOLE) for r in range(3) for c in range(3))
    return g(calc + keys, "rotate(25 32 30)")

@reg("timekpr", RED_DEEP)
def timekpr():
    shackle = stroke("M23 26V20A9 9 0 0 1 41 20V26", INK, 4.4)
    body = rrect(15.5, 25, 33, 23, 5, INK)
    clock = circle(32, 36.5, 7.5, HOLE) + stroke("M32 32V36.5L35.5 38.5", INK, 2.4)
    return shackle + body + clock

@reg("timeshift", RED)
def timeshift():
    return (stroke("M18 24C16.5 17.5 24 18.5 30 18.5C36 18.5 41 15.5 46 14", INK, 4.2) +
            stroke("M35 18.5C26 27 38 33 28 42", INK, 4.8) +
            stroke("M18 44C24 39 33 45.5 40 41.5C43 40 45 38 46 35.5", INK, 4.2))

@reg("timestripe", BLUE_GREY_DARK)
def timestripe():
    return (poly([(16, 18), (28, 13.5), (28, 46.5), (16, 42)], INK, 1.5) +
            poly([(32, 19.5), (37.5, 18), (37.5, 42), (32, 40.5)], INK, 1.5) +
            poly([(41, 22), (45, 21), (45, 39), (41, 38)], INK, 1.5) +
            poly([(48, 25), (49.5, 24.8), (49.5, 35.2), (48, 35)], INK, 1.5))

@reg("timidity", GREY_DARK)
def timidity():
    ti = (line(19, 14.5, 31, 14.5, INK, 3.6) + line(25, 14.5, 25, 23, INK, 3.6) +
          circle(38, 14.5, 2.2, INK) + line(38, 19, 38, 23, INK, 3.6))
    keys = rrect(15, 27, 34, 20, 3, INK)
    black = "".join(rrect(x, 27, 3.4, 11, 1, HOLE) for x in (21, 27.5, 34, 40.5))
    return ti + keys + black

@reg("tinder", PINK_LIGHT)
def tinder():
    return path("M27 13C28 20 22 23 20 29C17 37 22 47 32.5 47C42 47 47 40 46 32"
                "C45.5 27 43 23.5 40 21.5C40 25 38.5 27.5 36.5 28.5C37.5 21 33 15 27 13Z", INK)

@reg("tipp10", ORANGE_DEEP)
def tipp10():
    top = "".join(rrect(14.5 + k * 6, 14, 5, 5, 1.2, INK) for k in range(6))
    stem = "".join(rrect(29.5, 20 + k * 6, 5, 5, 1.2, INK) for k in range(4))
    return top + stem

@reg("tixati", BLUE_GREY_DARK)
def tixati():
    x = line(18, 18, 46, 46, INK, 3.6) + line(46, 18, 18, 46, INK, 3.6)
    t = line(16, 14, 48, 14, INK, 4) + line(32, 14, 32, 46, INK, 4)
    return x + t

@reg("tizen-studio-certificatemanager", LIGHT_BLUE_DEEP)
def tizen_cert():
    pts = [pt(32, 25, 12 if k % 2 == 0 else 10, -90 + 15 * k) for k in range(24)]
    rosette = poly(pts, INK, 1.5) + circle(32, 25, 6.5, HOLE) + circle(32, 25, 4, INK)
    tails = poly([(25, 33), (31, 35), (29, 47), (26, 44), (22, 45)], INK, 1.5) + \
        poly([(39, 33), (33, 35), (35, 47), (38, 44), (42, 45)], INK, 1.5)
    return tails + rosette

@reg("tizen-studio-dynamicanalyzer", BLUE_DEEP)
def tizen_dyn():
    lens = _ring(29, 27, 12, INK, 4.2)
    handle = line(38, 36, 46.5, 44.5, INK, 5.5)
    pulse = stroke("M20 28H24.5L27 22L31 33L33.5 27H38", INK, 2.6)
    return lens + handle + pulse

@reg("tizen-studio-em", LIGHT_BLUE)
def tizen_em():
    out = ""
    for k in range(3):
        y = 16 + k * 10
        out += f'<rect x="16" y="{y}" width="7" height="7" rx="1.5" fill="none" stroke="{INK}" stroke-width="2.6"/>'
        out += line(28, y + 3.5, 47, y + 3.5, INK, 3.4)
    return out

@reg("tizen-studio-ide", BLUE)
def tizen_ide():
    petal = path("M33 25.5C33.5 20 37 15.5 42 13.5C43 19 40 24.5 35 27Z", INK)
    return "".join(g(petal, f"rotate({45 * k} 32 30)") for k in range(8))

@reg("tlauncher", LIGHT_BLUE)
def tlauncher():
    return (line(15.5, 20, 31.5, 20, INK, 6) + line(23.5, 20, 23.5, 42, INK, 6) +
            stroke("M38 18V40H48.5", INK, 6))

@reg("tlpui", BLUE_GREY_DARK)
def tlpui():
    screen = rrect(14, 13, 36, 26, 3, INK)
    bars = rrect(18, 18, 4, 16, 1, HOLE) + rrect(42, 18, 4, 16, 1, HOLE)
    bolt = poly([(35, 15.5), (26, 27.5), (31.5, 27.5), (28.5, 36.5), (38, 24.5), (32.5, 24.5)], HOLE, 1.2)
    return screen + bars + bolt + rrect(14, 42.5, 36, 4, 2, INK)

@reg("tmm", ORANGE_DEEP)
def tmm():
    return _ring(32, 30, 15, INK, 4.6) + stroke("M32 19.5C30 27 27.5 35 31 38C34 40.5 37.5 37.5 39 34", INK, 4.2)

@reg("to-the-moon", DEEP_PURPLE_DEEP)
def to_the_moon():
    craters = (path("M24 20C27 19 29 22 27.5 24.5C26 27 22 26 21.5 23.5Z", DEEP_PURPLE_SOFT) +
               path("M35 30C39 28 43 31 42 35C41 38.5 36 39 34 36Z", DEEP_PURPLE_SOFT) +
               circle(27, 37, 2.8, DEEP_PURPLE_SOFT) + circle(38, 20.5, 2, DEEP_PURPLE_SOFT))
    return circle(32, 30, 16, INK) + craters

@reg("toby-the-secret-mine", BLUE_GREY_LIGHT)
def toby():
    body = path("M24 16C21 13 23 11 25.5 11.5C24.5 14 25 16 28 17H34C37 14.5 40 13 43.5 13.5"
                "C41 15 39.5 17 40.5 19C44 28 43 39 39 45C35.5 49 25 49 21.5 44"
                "C17 37 18 23 24 16Z", INK)
    eyes = circle(28, 38.5, 2.2, HOLE) + circle(36, 39.5, 2.2, HOLE)
    return body + eyes

@reg("todoist", RED)
def todoist():
    return "".join(stroke(f"M{15 + 3 * k} {20 + 10 * k}H{45 + 3 * k}", INK, 5) for k in range(3))

@reg("toggldesktop", PURPLE_SOFT)
def toggl():
    return (circle(32, 30, 16.5, INK) + stroke("M26 24.5A8.5 8.5 0 1 0 38 24.5", HOLE, 3.8) +
            line(32, 20, 32, 29, HOLE, 3.8))

@reg("toki-tori", AMBER_DEEP)
def toki_tori():
    body = path("M32 12C41 12 47 22 47 33C47 42 40 48 32 48C24 48 17 42 17 33C17 22 23 12 32 12Z", INK)
    eyes = (circle(27.5, 25, 5, HOLE) + circle(36.5, 25, 5, HOLE) +
            circle(28.5, 26.5, 2.4, INK) + circle(35.5, 26.5, 2.4, INK))
    beak = path("M27 32H37C37 36 35 38 32 38C29 38 27 36 27 32Z", AMBER_DARK)
    return body + eyes + beak

@reg("tokodon", LIGHT_BLUE)
def tokodon():
    head = rrect(16, 14, 32, 14, 5, INK)
    trunk = stroke("M32 25V40C32 44 36 45.5 40 42.5", INK, 8)
    eyes = circle(24, 20.5, 2.2, HOLE) + circle(40, 20.5, 2.2, HOLE)
    tusks = stroke("M24 29C23 33 19.5 35 15.5 34", INK, 2.8) + stroke("M40 29C41 33 44.5 35 48.5 34", INK, 2.8)
    return head + trunk + eyes + tusks

@reg("theia", BLUE_GREY_DARK)
def theia():
    head = circle(40, 30, 9.5, INK) + rrect(35.5, 28, 9, 4, 2, HOLE)
    trails = (line(18, 20.5, 31, 20.5, INK, 3.4) + line(22, 25.5, 29, 25.5, INK, 3.4) +
              line(14, 30.5, 28, 30.5, INK, 3.4) + line(20, 35.5, 29, 35.5, INK, 3.4) +
              line(25, 40.5, 32, 40.5, INK, 3.4))
    return trails + head

@reg("thermal-monitor", GREY_DARK)
def thermal_monitor():
    pins = "".join(line(x, 13, x, 47, INK, 2.4) for x in (22.5, 28.5, 35.5, 41.5)) + \
        "".join(line(15, y, 49, y, INK, 2.4) for y in (21, 27, 33, 39))
    chip = rrect(18, 16, 28, 28, 4, INK)
    therm = rrect(28.5, 19.5, 7, 17, 3.5, HOLE) + circle(32, 36, 5.5, HOLE)
    red = line(32, 25, 32, 34, RED, 2.6) + circle(32, 36, 3.2, RED)
    return pins + chip + therm + red

@reg("thunar", BLUE_GREY)
def thunar():
    head = rrect(13, 13, 38, 16, 4, INK)
    knot = stroke("M24 21C24 17 29 17 32 21C35 25 40 25 40 21C40 17 35 17 32 21C29 25 24 25 24 21Z", HOLE, 2.4)
    handle = rrect(28.5, 28, 7, 20, 2, INK)
    band = rrect(27, 31, 10, 4.5, 1.5, RED)
    return head + knot + handle + band

@reg("thunderbird-beta", BLUE_DARK)
def thunderbird_beta():
    bird = circle(33, 31, 16, INK)
    beak = poly([(13.5, 23), (20, 19.5), (20, 26)], INK, 2.5)
    crest = path("M24 15.5C27 11.5 33 10.5 38 12.5C33 12.5 29.5 14 27.5 17Z", INK)
    eye = circle(23.5, 21.5, 1.8, HOLE)
    env = rrect(20, 26, 20, 14, 3, HOLE) + stroke("M21.5 28L30 34L38.5 28", INK, 2)
    badge = circle(44, 42, 8.5, HOLE) + circle(44, 42, 6.5, INK)
    beta = stroke("M42.2 47V39.5C42.2 37.5 46.3 37.5 46.3 39.6C46.3 41 44.3 41.4 43.5 41.4"
                  "C46.8 41.4 47 45.2 44.2 45.2C43.3 45.2 42.5 44.7 42.2 44.2", HOLE, 1.8)
    return bird + beak + crest + eye + env + badge + beta

@small("thunderbird-beta")
def thunderbird_beta_s():
    bird = circle(33, 31, 16, INK) + poly([(13.5, 23), (20, 19.5), (20, 26)], INK, 2.5)
    env = rrect(20, 25, 22, 16, 3.5, HOLE) + stroke("M22 27.5L31 34L40 27.5", INK, 3)
    return bird + env + circle(45, 43, 7.5, HOLE) + circle(45, 43, 5, BLUE_SOFT)

@small("thedarkmod")
def thedarkmod_s():
    return gear_k(32, 30, 15, INK, HOLE, 10, 9.5) + circle(32, 30, 5, INK)

@small("thinkorswim")
def thinkorswim_s():
    out = ""
    for k in range(8):
        a = k * 45 + 8
        r = 17 if k % 2 == 0 else 12
        out += poly([pt(32, 30, 3, a), pt(32, 30, r, a - 11), pt(32, 30, r, a + 11)], INK, 1)
    return out

@small("timidity")
def timidity_s():
    keys = rrect(14, 18, 36, 26, 4, INK)
    return keys + "".join(rrect(x, 18, 5, 14, 1.2, HOLE) for x in (22, 29.5, 37))

@small("tizen-studio-certificatemanager")
def tizen_cert_s():
    tails = poly([(25, 33), (31, 35), (29, 47), (22, 45)], INK, 2) + poly([(39, 33), (33, 35), (35, 47), (42, 45)], INK, 2)
    return tails + circle(32, 25, 12, INK) + circle(32, 25, 5, HOLE)

@small("tilem")
def tilem_s():
    return (rrect(18, 11, 28, 38, 6, INK) + rrect(21.5, 14.5, 21, 16, 3, HOLE) +
            rrect(22, 35, 20, 4, 2, HOLE) + rrect(22, 41, 20, 4, 2, HOLE))

@small("tilp")
def tilp_s():
    return g(rrect(19, 11, 26, 38, 6, INK) + rrect(22.5, 14.5, 19, 14, 3, HOLE) +
             rrect(23, 34, 18, 4, 2, HOLE), "rotate(25 32 30)")

@small("tizen-studio-ide")
def tizen_ide_s():
    petal = path("M33 25C33.5 19 37 14.5 43 12.5C44 19.5 40 25 35 28Z", INK)
    return "".join(g(petal, f"rotate({60 * k} 32 30)") for k in range(6))

@small("tixati")
def tixati_s():
    return line(19, 19, 45, 45, INK, 4.5) + line(45, 19, 19, 45, INK, 4.5) + line(15, 14, 49, 14, INK, 5) + line(32, 14, 32, 46, INK, 5)

@small("theia")
def theia_s():
    return (line(16, 23, 29, 23, INK, 4.5) + line(14, 30, 28, 30, INK, 4.5) + line(18, 37, 29, 37, INK, 4.5) +
            circle(40, 30, 10, INK) + rrect(35, 28, 10, 4.5, 2.2, HOLE))

@small("thermal-monitor")
def thermal_monitor_s():
    return rrect(15, 13, 34, 34, 5, INK) + rrect(28, 17, 8, 18, 4, HOLE) + circle(32, 36, 6.5, HOLE) + circle(32, 36, 4, RED)

@small("thimbleweed-park")
def thimbleweed_s():
    return (poly([(21, 13), (29, 41), (13, 41)], INK, 2.5) +
            rrect(32, 20, 19, 14, 3, INK) + rrect(40, 34, 4, 12, 1, INK) + rrect(12, 43, 40, 4, 2, INK))

@small("tidal-hifi")
def tidal_hifi_s():
    return "".join(g(rrect(cx - 4.6, cy - 4.6, 9.2, 9.2, 1, INK), f"rotate(45 {cx} {cy})")
                   for cx, cy in [(19.5, 25), (32, 25), (44.5, 25), (32, 37.5)])

SMALL["tidal"] = tidal_hifi_s

@small("tilix")
def tilix_s():
    out = ""
    for x in (13, 33):
        out += rrect(x, 15, 18, 30, 3.5, INK) + stroke(f"M{x + 4} 24L{x + 9} 30L{x + 4} 36", HOLE, 3.4)
    return out

@small("timestripe")
def timestripe_s():
    return (poly([(15, 17), (29, 13), (29, 47), (15, 43)], INK, 2) +
            poly([(34, 19), (41, 18), (41, 42), (34, 41)], INK, 2) +
            poly([(46, 22), (50, 21.5), (50, 38.5), (46, 38)], INK, 2))

@small("todoist")
def todoist_s():
    return "".join(stroke(f"M{15 + 3 * k} {22 + 11 * k}H{45 + 3 * k}", INK, 5.6) for k in range(2))

@small("tlpui")
def tlpui_s():
    bolt = poly([(36, 14.5), (25, 29), (31.5, 29), (28, 39.5), (40, 24.5), (33, 24.5)], HOLE, 1.5)
    return rrect(13, 12, 38, 29, 4, INK) + bolt + rrect(13, 43.5, 38, 4.5, 2.2, INK)

@small("toki-tori")
def toki_tori_s():
    body = path("M32 12C41 12 47 22 47 33C47 42 40 48 32 48C24 48 17 42 17 33C17 22 23 12 32 12Z", INK)
    return body + circle(26.5, 26, 5, HOLE) + circle(37.5, 26, 5, HOLE) + path("M26 34H38C38 38 35.5 40 32 40C28.5 40 26 38 26 34Z", AMBER_DARK)

@small("to-the-moon")
def to_the_moon_s():
    return circle(32, 30, 16, INK) + circle(26, 23, 4, DEEP_PURPLE_SOFT) + circle(38.5, 34, 5, DEEP_PURPLE_SOFT)

@small("tokodon")
def tokodon_s():
    return (rrect(15, 13, 34, 15, 5, INK) + stroke("M32 25V40C32 44 36 45.5 40 42.5", INK, 9) +
            circle(24, 20.5, 2.8, HOLE) + circle(40, 20.5, 2.8, HOLE))

@small("thextech")
def thextech_s():
    cap = path("M14 30C14 19.5 22 13 32 13C42 13 50 19.5 50 30A2.5 2.5 0 0 1 47.5 32.5H16.5A2.5 2.5 0 0 1 14 30Z", INK)
    return cap + line(27, 18, 37, 28, HOLE, 5) + line(37, 18, 27, 28, HOLE, 5) + rrect(22, 35, 20, 13, 5, INK)
