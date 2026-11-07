# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 7: apifox to ark.

Same rules as batch01: palette tile nearest the brand colour, mark in
INK, HOLE for the tile showing through, any second shade another step
from the palette.
"""
import math
from lm import *
from glyphs.kit import _gear, registry

ICONS, SMALL, reg, small = registry()

@reg("apifox", RED_LIGHT)
def apifox():

    body = circle(32, 31, 16.5, INK)
    head = circle(32, 20, 8, HOLE)
    teeth = poly([(36, 30), (48.5, 26), (43, 31), (48, 33.5), (41.5, 36.5),
                  (44, 40), (37, 36)], HOLE, 1.2)
    return body + head + teeth

@reg("apk-editor-studio", CYAN_DEEP)
def apk_editor_studio():
    sheet = path("M19 13H45A3 3 0 0 1 48 16V38L38 48H19A3 3 0 0 1 16 45V16A3 3 0 0 1 19 13Z", INK)
    fold = path("M48 38H41A3 3 0 0 0 38 41V48Z", CYAN_SOFT)
    cells = "".join(rrect(20 + c * 7.5, 17 + r * 7.5, 5, 5, 1.2, HOLE)
                    for r in range(4) for c in range(4) if not (r == 3 and c == 3))
    return sheet + fold + cells

@reg("apk-icon-editor", AMBER)
def apk_icon_editor():
    return "".join(rrect(15 + c * 9, 13 + r * 9, 7, 7, 1.8, INK)
                   for r in range(4) for c in range(4))

@reg("apktool", INDIGO_SOFT)
def apktool():
    top = path("M17 13H48L42.5 20.5L48 28H17A2 2 0 0 1 15 26V15A2 2 0 0 1 17 13Z", INK)
    bars = rrect(21, 16, 3, 9, 1.5, HOLE) + rrect(29, 16, 3, 9, 1.5, HOLE)
    low = path("M15 31H40V43H48V48H24V36H15Z", BLUE_DARK,
               ' stroke="#155C95" stroke-width="2" stroke-linejoin="round"')
    lbars = rrect(27.5, 36, 3, 8, 1.5, INK) + rrect(34, 36, 3, 8, 1.5, INK)
    return top + bars + low + lbars

@reg("apollo-studio", BLUE_GREY_DARK)
def apollo_studio():
    legs = (line(21, 39, 32, 16.5, INK, 4.6) + line(36.5, 25.5, 46, 44, INK, 4.6) +
            line(17, 44, 40.5, 44, INK, 4.6))
    bell = path("M32 28C29 28 28.5 31 28.5 33.5L26.5 37H37.5L35.5 33.5C35.5 31 35 28 32 28Z", INK,
                f' stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"')
    return legs + bell

@reg("app-outlet", DEEP_PURPLE)
def app_outlet():
    bag = path("M18 16H46L48 42A5 5 0 0 1 43 47H21A5 5 0 0 1 16 42Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    handle = stroke("M25 21V24A7 7 0 0 0 39 24V21", HOLE, 3.2)
    return bag + handle + circle(25, 21, 2, HOLE) + circle(39, 21, 2, HOLE)

@reg("app.bluebubbles.BlueBubbles", BLUE)
def bluebubbles():
    bubble = path("M32 13A17 16 0 1 1 22.5 42.5L15 46L17.5 38.5A17 16 0 0 1 32 13Z", INK)
    dots = "".join(circle(x, 29, 2.8, HOLE) for x in (24.5, 32, 39.5))
    return bubble + dots

@reg("app.devsuite.Manuals", RED)
def manuals():
    book = rrect(14, 14, 36, 32, 4, INK)
    spine = line(29, 17, 29, 43, HOLE, 2.4)
    brace = stroke("M24 20C21 20 21.5 22.5 21.5 25C21.5 28 20.5 30 19 30"
                   "C20.5 30 21.5 32 21.5 35C21.5 37.5 21 40 24 40", HOLE, 2.6)
    lines = "".join(rrect(33, y, 13, 2.6, 1.3, HOLE) for y in (20, 25.5, 31, 36.5))
    return book + spine + brace + lines

@reg("app.drey.EarTag", AMBER_DEEP)
def eartag():
    tag = path("M27 13H37A4 4 0 0 1 41 17V21L47 26V43A4 4 0 0 1 43 47H21A4 4 0 0 1 17 43V26L23 21V17"
               "A4 4 0 0 1 27 13Z", INK, f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    hole = circle(32, 19.5, 3, HOLE)
    note = (circle(26.5, 40, 3.2, HOLE) + circle(37.5, 38, 3.2, HOLE) +
            poly([(28, 40), (28, 30), (39, 28), (39, 38), (36.8, 38), (36.8, 31.5),
                  (30.2, 32.7), (30.2, 40)], HOLE, 0.8))
    return tag + hole + note

@reg("app.drey.PaperPlane", LIGHT_BLUE_DEEP)
def paperplane():
    dart = poly([(27, 12), (39, 46), (27, 40), (15, 46)], INK, 2.5)
    fold = poly([(27, 12), (39, 46), (27, 40)], LIGHT_BLUE_SOFT, 2.5)
    lines = "".join(rrect(49 - w, y, w, 3, 1.5, INK) for y, w in [(14, 12), (20, 10), (26, 8), (32, 6)])
    return dart + fold + lines

@reg("app.drey.Warp", PURPLE)
def warp():
    pts = []
    for i in range(0, 461):
        t = i / 460
        a = math.radians(-90 + t * 720 * 1.08)
        r = 2.5 + 14 * t
        pts.append((32 + r * math.cos(a), 30 + r * math.sin(a)))
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts[::4])
    return stroke(d, INK, 3.6)

@reg("app.organicmaps.desktop", INDIGO_LIGHT)
def organicmaps():
    pin = path("M32 12A13.5 13.5 0 0 1 45.5 25.5C45.5 34 38 40 32 47C26 40 18.5 34 18.5 25.5"
               "A13.5 13.5 0 0 1 32 12Z", INK)
    leaf = path("M24 30C25 22 32 18.5 40.5 19.5C39.5 27.5 33 31 24 30Z", HOLE)
    vein = stroke("M27 28L35 23.5", INK, 1.6)
    orbit = g(f'<ellipse cx="32" cy="26" rx="19" ry="6" fill="none" stroke="{INK}" stroke-width="2.6"/>',
              "rotate(-22 32 26)")
    return orbit + pin + leaf + vein

@reg("app.riftshare.RiftShare", CYAN_DEEP)
def riftshare():
    band = path("M20 21C27 25 37 25 44 21V39C37 35 27 35 20 39Z", CYAN_SOFT)
    portals = ""
    for x in (19, 45):
        portals += (f'<ellipse cx="{x}" cy="30" rx="5.5" ry="15" fill="{INK}"/>'
                    f'<ellipse cx="{x}" cy="30" rx="2.3" ry="9" fill="{HOLE}"/>')
    return band + portals

@reg("appcode", BLUE_DEEP)
def appcode():
    sq = rrect(15, 13, 34, 34, 3, INK)
    a = stroke("M19.5 32L24.5 18.5L29.5 32M21.5 27.5H27.5", HOLE, 3)
    c = stroke("M44 21C43 19 41.5 18.5 39.5 18.5C36 18.5 34 21 34 25.2C34 29.5 36 32 39.5 32"
               "C41.5 32 43 31.3 44 29.5", HOLE, 3)
    bar = rrect(19.5, 38.5, 12, 3.4, 1, HOLE)
    return sq + a + c + bar

@reg("appimagekit-diffuse", BLUE_GREY_LIGHT)
def appimagekit_diffuse():
    d = path("M29 16H36C44 16 48.5 21.5 48.5 30C48.5 38.5 44 44 36 44H29Z", INK,
             f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    lines = (rrect(17, 21, 10, 4, 2, INK) + rrect(14, 28, 13, 4, 2, INK) + rrect(17, 35, 10, 4, 2, INK))
    return d + path("M36 24.5C39.5 24.5 41 26.5 41 30C41 33.5 39.5 35.5 36 35.5Z", HOLE) + lines

@reg("apple-music", RED)
def apple_music():
    beam = poly([(27, 18), (43, 14.5), (43, 19.5), (27, 23)], INK, 2)
    stems = line(27.5, 19, 27.5, 39, INK, 3.2) + line(42.5, 16, 42.5, 36, INK, 3.2)
    heads = (f'<ellipse cx="23.5" cy="40" rx="5.5" ry="4.5" fill="{INK}"/>'
             f'<ellipse cx="38.5" cy="37" rx="5.5" ry="4.5" fill="{INK}"/>')
    return beam + stems + heads

@reg("applets-screenshooter", TEAL)
def screenshooter():
    out = circle(CX, CY, 16.5, INK) + circle(CX, CY, 12.5, HOLE) + circle(CX, CY, 10.5, INK)
    for k in range(6):
        a = -90 + 60 * k
        x0, y0 = pt(CX, CY, 5, a)
        x1, y1 = x0 + 11 * math.cos(math.radians(a + 90)), y0 + 11 * math.sin(math.radians(a + 90))
        out += line(x0, y0, x1, y1, HOLE, 2.2)
    return out + circle(CX, CY, 3.5, HOLE)

@reg("application-community", RED)
def community():
    return path("M32 46C23 39.5 15 33 15 23.5C15 17.5 19.5 13.5 24.5 13.5C28 13.5 30.5 15.5 32 18"
                "C33.5 15.5 36 13.5 39.5 13.5C44.5 13.5 49 17.5 49 23.5C49 33 41 39.5 32 46Z", INK)

@reg("application-default-icon", BLUE_GREY_DEEP)
def default_icon():
    return _gear(CX, CY, 17, 12.5, 8, INK) + circle(CX, CY, 6, HOLE)

@reg("application-x-renderdoc-capture", BLUE_GREY_LIGHT)
def renderdoc():
    ring = f'<circle cx="32" cy="22.5" r="6.5" fill="none" stroke="{INK}" stroke-width="3.8"/>'
    arc = stroke("M15 42C19.5 35.5 25.5 32.5 32 32.5C38.5 32.5 44.5 35.5 49 42", INK, 4)
    return ring + arc

@reg("applications-accessories", TEAL_DEEP)
def accessories():
    square = cut("M15 13L15 47H49Z" + "M20 25L20 42H37Z", TEAL_SOFT)
    legs = line(29.5, 26, 22, 46, INK, 3.2) + line(34.5, 26, 42, 46, INK, 3.2)
    head = rrect(26.5, 17, 11, 12, 3, INK) + rrect(30, 12.5, 4, 5, 1, INK) + circle(32, 23, 2.3, HOLE)
    return square + legs + head

@reg("applications-all", BLUE_GREY_DEEP)
def apps_all():
    return (rrect(15, 13, 15, 15, 4, INK) + rrect(34, 13, 15, 15, 4, BLUE_GREY_DARK) +
            rrect(15, 32, 15, 15, 4, BLUE_GREY_DARK) + rrect(34, 32, 15, 15, 4, INK))

@reg("applications-development", BROWN)
def apps_development():
    handle = line(29, 27, 45.5, 45, INK, 4.2)
    head = path("M17 22L27.5 12.5C31 11.5 35 12.5 38 15L36 17L39.5 20.5L32 28L28.5 24.5L22.5 30Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return handle + head

@reg("applications-development-translation", BLUE_DEEP)
def apps_translation():
    a = stroke("M36 30L42 13.5L48 30M38 24.5H46", INK, 3.4)
    kana = (stroke("M15 29H30", BLUE_SOFT, 3) + stroke("M21 24C21 33 22 40 25 46", BLUE_SOFT, 3) +
            stroke("M30 32C23 31 16.5 36 18 41.5C19.5 46 27 43 30.5 37C32.5 33.5 39 33.5 39.5 39"
                   "C40 44 35 47 31 46.5", BLUE_SOFT, 3))
    return kana + a

@reg("applications-development-web", LIGHT_BLUE_DEEP)
def apps_web():
    globe = (f'<circle cx="30" cy="28" r="14.5" fill="none" stroke="{INK}" stroke-width="3.2"/>'
             f'<ellipse cx="30" cy="28" rx="6" ry="14.5" fill="none" stroke="{INK}" stroke-width="2.6"/>'
             + line(16, 28, 44, 28, INK, 2.6))
    badge = circle(42, 40, 10, HOLE) + _gear(42, 40, 8.5, 6.2, 7, INK) + circle(42, 40, 2.8, HOLE)
    return globe + badge

@reg("applications-education", BLUE_GREY)
def apps_education():
    base = path("M21 29V37C21 40.5 26 43 32 43C38 43 43 40.5 43 37V29L32 34Z", INK)
    board = poly([(32, 15), (50, 24), (32, 33), (14, 24)], INK, 2.5)
    rim = poly([(32, 30.5), (46.5, 23.5), (32, 16.5), (17.5, 23.5)], INK, 0)
    tassel = stroke("M32 24L18 28V38", ORANGE_LIGHT, 2.4) + rrect(16, 36.5, 4, 8, 1.5, ORANGE_LIGHT)
    return base + board + rim + tassel

@reg("applications-education-mathematics", BLUE_GREY_DEEP)
def apps_maths():
    root = stroke("M14 31L18 29L23.5 42L30 17.5H49", INK, 3.6)
    x = line(34, 25, 45, 40, INK, 3.6) + line(45, 25, 34, 40, INK, 3.6)
    return root + x

@reg("applications-electronics", BROWN_LIGHT)
def apps_electronics():
    cap = (line(24, 12, 24, 25, INK, 3) + line(24, 35, 24, 48, INK, 3) +
           rrect(16, 24, 16, 3.6, 1.5, INK) + rrect(16, 32.4, 16, 3.6, 1.5, INK))
    res = line(40, 12, 40, 48, INK, 3) + rrect(35, 20, 10, 20, 2.5, INK)
    return cap + res

@reg("applications-engineering", BLUE_GREY)
def apps_engineering():
    base = rrect(15, 43, 20, 5, 2.5, INK) + rrect(19, 36, 12, 9, 2, INK)
    arm = stroke("M25 32L27.5 20.5L42 16", INK, 5)
    joints = circle(25, 32, 6, INK) + circle(25, 32, 2.5, HOLE) + circle(27.5, 20.5, 3.4, HOLE)
    claw = stroke("M43.5 21.5L49 21L48 26M44 12.5L49 13L50 17.5", INK, 3)
    return arm + base + joints + claw + circle(42, 16, 4.5, INK)

@reg("applications-haskell", DEEP_PURPLE_DEEP)
def apps_haskell():
    left = poly([(14, 14), (21, 14), (29, 30), (21, 46), (14, 46), (22, 30)], DEEP_PURPLE_SOFT, 1.4)
    lam = poly([(24, 14), (31, 14), (49, 46), (42, 46), (36.3, 36), (30.5, 46), (23.5, 46), (32.8, 29.8)],
               INK, 1.4)
    eq = (poly([(38.5, 23), (50, 23), (50, 28), (41.3, 28)], INK, 1.4) +
          poly([(43, 31), (50, 31), (50, 36), (45.8, 36)], INK, 1.4))
    return left + lam + eq

@reg("applications-interfacedesign", BLUE_GREY)
def apps_interface():
    win = rrect(14, 13, 36, 34, 5, INK)
    bar = rrect(14, 13, 36, 6, 3, BLUE_GREY_SOFT)
    bits = circle(21.5, 26, 2.8, HOLE) + rrect(27.5, 23.2, 5.6, 5.6, 1.2, HOLE)
    track = line(21, 38, 43, 38, HOLE, 3.4)
    knob = circle(37, 38, 5, HOLE) + circle(37, 38, 2.8, INK)
    return win + bar + bits + track + knob

@reg("applications-multimedia", PURPLE)
def apps_multimedia():
    film = rrect(13, 14, 30, 24, 4, INK)
    holes = "".join(rrect(15.5, y, 3, 3, 0.8, HOLE) for y in (17, 24.5, 32))
    play = poly([(27, 20.5), (36.5, 26), (27, 31.5)], HOLE, 2)
    note_o = (stroke("M36 44V29L48 27V41", HOLE, 7) + circle(33.5, 44, 5.5, HOLE) +
              circle(45.5, 41, 5.5, HOLE))
    note = (stroke("M36 44V29L48 27V41", INK, 3) + circle(33.5, 44, 3.6, INK) +
            circle(45.5, 41, 3.6, INK))
    return film + holes + play + note_o + note

@reg("applications-office", BROWN_LIGHT)
def apps_office():
    handle = stroke("M26 19V15.5A2 2 0 0 1 28 13.5H36A2 2 0 0 1 38 15.5V19", INK, 3.4)
    body = rrect(14, 19, 36, 27, 5, INK)
    seam = line(15, 32, 49, 32, HOLE, 2)
    clasp = rrect(28, 29, 8, 6, 2, HOLE) + rrect(30, 31, 4, 2, 1, INK)
    return handle + body + seam + clasp

@reg("applications-other", BLUE_GREY_DEEP)
def apps_other():
    return "".join(circle(x, CY, 4.6, INK) for x in (19.5, 32, 44.5))

@reg("applications-science", TEAL_LIGHT)
def apps_science():
    orbits = "".join(g(f'<ellipse cx="32" cy="30" rx="17" ry="6.5" fill="none" stroke="{INK}" '
                       'stroke-width="2.6"/>', f"rotate({a} 32 30)") for a in (0, 60, 120))
    return orbits + circle(CX, CY, 4.5, INK)

@reg("applications-utilities", RED_DEEP)
def apps_utilities():
    handle = stroke("M25 20V16A2.5 2.5 0 0 1 27.5 13.5H36.5A2.5 2.5 0 0 1 39 16V20", INK, 3.4)
    lid = rrect(13, 19, 38, 9, 3, INK)
    body = rrect(15, 29.5, 34, 16.5, 3, INK)
    latches = rrect(19, 25, 6, 7, 1.5, HOLE) + rrect(39, 25, 6, 7, 1.5, HOLE)
    return handle + lid + body + latches

@reg("applixware", BLUE_GREY_DEEP)
def applixware():
    d = "M19.5 43.5L32 16L44.5 43.5M25 36H39"
    return stroke(d, INK, 9.5) + stroke(d, HOLE, 3.4)

@reg("aptana", RED_DEEP)
def aptana():
    return _gear(CX, CY, 17, 13, 10, INK, 0.55) + circle(CX, CY, 6, HOLE)

@reg("aqemu", BLUE_DEEP)
def aqemu():
    ring = f'<circle cx="30.5" cy="28.5" r="14" fill="none" stroke="{INK}" stroke-width="3.6"/>'
    tail = line(39.5, 38, 47, 46, INK, 4.2)
    a = stroke("M24 37L30.5 20L37 37M26.3 31H34.7", INK, 3)
    return ring + tail + a

@reg("aqualung", BLUE)
def aqualung():
    band = stroke("M17 33V29A15 15 0 0 1 47 29V33", BLUE_GREY_SOFT, 3.4)
    cups = rrect(12.5, 29, 7, 13, 3, BLUE_GREY_SOFT) + rrect(44.5, 29, 7, 13, 3, BLUE_GREY_SOFT)
    drop = path("M32 11C35 17 43 25 43 34A11 11 0 0 1 21 34C21 25 29 17 32 11Z", INK)
    visor = rrect(21, 31, 22, 4.5, 2, BLUE_DARK)
    return band + cups + drop + visor

@reg("ar.xjuan.Cambalache", DEEP_PURPLE_SOFT)
def cambalache():
    return cut("M15 13L15 47H49Z" + "M20.5 27L20.5 41.5H35Z", INK)

@reg("aranym", INDIGO_DEEP)
def aranym():

    rows = ["110111",
            "101101",
            "111011",
            "110111",
            "101101",
            "011011"]
    out = rrect(14, 12, 36, 36, 5, INDIGO_SOFT)
    for r, row in enumerate(rows):
        for c, v in enumerate(row):
            if v == "1":
                out += rrect(15 + c * 5.8, 13 + r * 5.8, 5, 5, 0.8, INK)
    return out

@reg("archipelago", BLUE_GREY_DEEP)
def archipelago():
    peaks = stroke("M13.5 43L24.5 19L33 37.5M28.5 43L39.5 19L50.5 43", INK, 3.6)
    ground = line(13.5, 43, 50.5, 43, INK, 3.6)
    snow = stroke("M20 29L23 31.5L26.5 28.5M35 29L38 31.5L41.5 28.5", INK, 2.6)
    return peaks + ground + snow

@reg("arcolinux-hello", BLUE_LIGHT)
def arcolinux():
    return path("M32 12L49 46H38C35 40 31.5 36.5 26 36.5C29 38 31 41.5 32 46H15Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')

@reg("ardour", RED_DARK)
def ardour():
    tri = poly([(32, 12), (49, 46), (15, 46)], INK, 2.5)
    bars = "".join(rrect(x - 1.2, 46.5 - h, 2.4, h, 1, HOLE)
                   for x, h in [(23, 5), (27.5, 9), (32, 14), (36.5, 10), (41, 6)])
    return tri + bars

@reg("arduino", CYAN_DEEP)
def arduino():
    inf = stroke("M32 30C29 25 26 21.5 22 21.5A8.5 8.5 0 0 0 22 38.5C26 38.5 29 35 32 30"
                 "C35 25 38 21.5 42 21.5A8.5 8.5 0 0 1 42 38.5C38 38.5 35 35 32 30Z", INK, 4.4)
    minus = line(18.5, 30, 25.5, 30, INK, 2.8)
    plus = line(38.5, 30, 45.5, 30, INK, 2.8) + line(42, 26.5, 42, 33.5, INK, 2.8)
    return inf + minus + plus

@reg("ares", AMBER_DEEP)
def ares():
    return path("M36.8 14.2A16.5 16.5 0 1 0 46.4 36.6A13 13 0 1 1 36.8 14.2Z", INK)

@reg("argouml", GREY_DEEP)
def argouml():
    hull = path("M13 33H51L43 45H21Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    sail = poly([(32, 12), (42, 31), (22, 31)], INK, 2)
    fold = poly([(32, 12), (32, 31), (22, 31)], GREY_SOFT, 2)
    crease = line(22, 38.5, 42, 38.5, HOLE, 2.2)
    return sail + fold + hull + crease

@reg("arianna", ORANGE_DEEP)
def arianna():
    book = rrect(17, 12, 30, 36, 3.5, INK)
    spine = rrect(17, 12, 7, 36, 3.5, ORANGE_SOFT)
    mark = path("M35 12H42V28L38.5 25L35 28Z", HOLE)
    return book + spine + mark

@reg("ark", ORANGE_DEEP)
def ark():
    teeth = "".join(rrect(29 if k % 2 == 0 else 32, 11 + k * 3.5, 3, 2.6, 0.8, INK) for k in range(6))
    pull = rrect(26.5, 31, 11, 16, 5.5, INK) + circle(32, 40.5, 2.8, HOLE)
    neck = rrect(29.5, 31.5 - 4, 5, 5, 1.5, INK)
    return teeth + neck + pull

@small("apk-editor-studio")
def apk_editor_studio_s():
    sheet = path("M19 13H45A3 3 0 0 1 48 16V38L38 48H19A3 3 0 0 1 16 45V16A3 3 0 0 1 19 13Z", INK)
    cells = "".join(rrect(21 + c * 11, 18 + r * 11, 7.5, 7.5, 1.5, HOLE)
                    for r in range(2) for c in range(2))
    return sheet + cells

@small("apk-icon-editor")
def apk_icon_editor_s():
    return "".join(rrect(14.5 + c * 12.5, 12.5 + r * 12.5, 10, 10, 2.5, INK)
                   for r in range(3) for c in range(3))

@small("app.devsuite.Manuals")
def manuals_s():
    book = rrect(14, 14, 36, 32, 4, INK)
    brace = stroke("M25 19C21 19 22 23 22 26C22 28.5 20.5 30 19 30"
                   "C20.5 30 22 31.5 22 34C22 37 21 41 25 41", HOLE, 3.4)
    lines = "".join(rrect(31, y, 15, 4, 2, HOLE) for y in (20, 28, 36))
    return book + brace + lines

@small("app.drey.EarTag")
def eartag_s():
    tag = path("M27 13H37A4 4 0 0 1 41 17V21L47 26V43A4 4 0 0 1 43 47H21A4 4 0 0 1 17 43V26L23 21V17"
               "A4 4 0 0 1 27 13Z", INK, f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    note = circle(29, 39.5, 4.5, HOLE) + rrect(31, 27, 3.8, 13, 1.5, HOLE) + rrect(31, 27, 8, 4, 1.5, HOLE)
    return tag + circle(32, 19.5, 3.2, HOLE) + note

@small("applications-development-web")
def apps_web_s():
    globe = (f'<circle cx="30" cy="28" r="14.5" fill="none" stroke="{INK}" stroke-width="3.2"/>'
             + line(16, 28, 44, 28, INK, 2.8))
    badge = circle(42, 40, 10.5, HOLE) + _gear(42, 40, 9, 6.6, 6, INK) + circle(42, 40, 3, HOLE)
    return globe + badge

@small("aranym")
def aranym_s():
    rows = ["101", "110", "011"]
    out = rrect(14, 12, 36, 36, 5, INDIGO_SOFT)
    for r, row in enumerate(rows):
        for c, v in enumerate(row):
            if v == "1":
                out += rrect(15 + c * 11.7, 13 + r * 11.7, 10.4, 10.4, 1.5, INK)
    return out

@small("ardour")
def ardour_s():
    tri = poly([(32, 12), (49, 46), (15, 46)], INK, 2.5)
    bars = "".join(rrect(x - 2, 46.5 - h, 4, h, 1.5, HOLE) for x, h in [(25, 7), (32, 14), (39, 8)])
    return tri + bars

@small("ark")
def ark_s():
    teeth = "".join(rrect(27.5 if k % 2 == 0 else 32, 11 + k * 5, 4.5, 4, 1, INK) for k in range(4))
    pull = rrect(25.5, 30, 13, 17, 6, INK) + circle(32, 40.5, 3.2, HOLE)
    return teeth + pull

@small("apifox")
def apifox_s():
    return (circle(32, 31, 16.5, INK) + circle(32, 19, 8.5, HOLE) +
            poly([(36, 29), (49, 26), (43, 33), (46, 40), (37, 36)], HOLE, 1.2))

@small("apollo-studio")
def apollo_studio_s():
    return (line(20.5, 39, 32, 16, INK, 5.5) + line(36.5, 25, 46, 44, INK, 5.5) +
            line(17, 44.5, 40, 44.5, INK, 5.5))

@small("app.drey.Warp")
def warp_s():
    pts = []
    for i in range(0, 241):
        t = i / 240
        a = math.radians(-90 + t * 540)
        r = 3 + 13.5 * t
        pts.append((32 + r * math.cos(a), 30 + r * math.sin(a)))
    return stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts[::4]), INK, 4)

@small("app.organicmaps.desktop")
def organicmaps_s():
    pin = path("M32 12A14 14 0 0 1 46 26C46 34.5 38.5 40.5 32 47.5C25.5 40.5 18 34.5 18 26"
               "A14 14 0 0 1 32 12Z", INK)
    return pin + path("M23.5 31C24.5 22 32 18 41.5 19C40.5 28 33 32 23.5 31Z", HOLE)

@small("app.riftshare.RiftShare")
def riftshare_s():
    band = rrect(19, 24, 26, 12, 0, CYAN_SOFT)
    return band + "".join(f'<ellipse cx="{x}" cy="30" rx="6.5" ry="16" fill="{INK}"/>' for x in (18, 46))

@small("appcode")
def appcode_s():
    sq = rrect(14, 12, 36, 36, 3, INK)
    a = stroke("M19 33L24.5 18L30 33", HOLE, 3.2)
    c = stroke("M45 21C44 18.5 42 18 40 18C36 18 34 21 34 25.5C34 30 36 33 40 33C42 33 44 32.5 45 30", HOLE, 3.2)
    return sq + a + c + rrect(19, 39, 13, 4.5, 1, HOLE)

@small("applications-accessories")
def accessories_s():
    legs = line(29, 26, 20, 47, INK, 3.4) + line(35, 26, 44, 47, INK, 3.4)
    return legs + rrect(25, 14, 14, 15, 4, INK) + circle(32, 22, 3, HOLE)

@small("applications-haskell")
def apps_haskell_s():
    left = poly([(13, 14), (21, 14), (29, 30), (21, 46), (13, 46), (21, 30)], DEEP_PURPLE_SOFT, 1.4)
    lam = poly([(25, 14), (33, 14), (51, 46), (43, 46), (37.5, 36.5), (32, 46), (24, 46), (33.5, 29.5)],
               INK, 1.4)
    return left + lam

@small("applications-science")
def apps_science_s():
    orbits = "".join(g(f'<ellipse cx="32" cy="30" rx="17" ry="6.5" fill="none" stroke="{INK}" '
                       'stroke-width="2.4"/>', f"rotate({a} 32 30)") for a in (-45, 45))
    return orbits + circle(CX, CY, 5, INK)

@small("arduino")
def arduino_s():
    return "".join(f'<circle cx="{x}" cy="30" r="8.3" fill="none" stroke="{INK}" stroke-width="4"/>'
                   for x in (22, 42))

@small("applications-multimedia")
def apps_multimedia_s():
    film = rrect(13, 13, 28, 23, 4, INK) + poly([(23, 18.5), (33, 24.5), (23, 30.5)], HOLE, 2)
    outline = stroke("M46 43V24H51", HOLE, 8) + circle(41.5, 43, 6.5, HOLE)
    note = stroke("M46 43V24H50", INK, 3.4) + circle(41.5, 43, 4.5, INK)
    return film + outline + note

@small("applications-development-translation")
def apps_translation_s():
    a = stroke("M35 32L42 12.5L49 32M37.5 26H46.5", INK, 3.6)
    kana = (stroke("M14 30H29", BLUE_SOFT, 3.4) + stroke("M20.5 25V46", BLUE_SOFT, 3.4) +
            stroke("M31 36C25 34 16 38 17.5 43C19 47 28 45 31 39", BLUE_SOFT, 3.4))
    return kana + a

@small("applets-screenshooter")
def screenshooter_s():
    out = circle(CX, CY, 16.5, INK)
    for k in range(6):
        a = -90 + 60 * k
        x0, y0 = pt(CX, CY, 6.5, a)
        x1, y1 = x0 + 9 * math.cos(math.radians(a + 90)), y0 + 9 * math.sin(math.radians(a + 90))
        out += line(x0, y0, x1, y1, HOLE, 2.3)
    return out

@small("app.bluebubbles.BlueBubbles")
def bluebubbles_s():
    bubble = path("M32 13A17 16 0 1 1 22.5 42.5L15 46L17.5 38.5A17 16 0 0 1 32 13Z", INK)
    return bubble + "".join(circle(x, 29, 3, HOLE) for x in (22.5, 32, 41.5))

@small("applications-engineering")
def apps_engineering_s():
    base = rrect(14, 42, 22, 6, 3, INK)
    arm = stroke("M25 38L27 21L44 17", INK, 6)
    return base + arm + circle(25, 34, 6.5, INK) + stroke("M44 17L49 22", INK, 4.5)
