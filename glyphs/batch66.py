# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 66: subtitlecomposer to system-software-update."""
import math
from lm import *
from glyphs.kit import _arc_c, _hex, registry

ICONS, SMALL, reg, small = registry()

def _head(cx, cy, r, a, size, fill, cw=True):
    """Arrowhead sitting on a circle at angle a, pointing along the motion."""
    ex, ey = pt(cx, cy, r, a)
    t = math.radians(a + (90 if cw else -90))
    rad = math.radians(a)
    tip = (ex + size * math.cos(t), ey + size * math.sin(t))
    b1 = (ex + size * .95 * math.cos(rad), ey + size * .95 * math.sin(rad))
    b2 = (ex - size * .95 * math.cos(rad), ey - size * .95 * math.sin(rad))
    return poly([b1, tip, b2], fill, 1.6)

def _pixels(rows, x0, y0, s, fill):
    out = ""
    for j, row in enumerate(rows):
        for i, c in enumerate(row):
            if c == "X":
                out += (f'<rect x="{f(x0 + i * s - .15)}" y="{f(y0 + j * s - .15)}" '
                        f'width="{f(s + .3)}" height="{f(s + .3)}" fill="{fill}"/>')
    return out

def _sub_screen():
    return rrect(14, 16, 36, 28, 5, INK)

@reg("subtitlecomposer", ORANGE_DEEP)
def subtitlecomposer():
    s = stroke("M26 25.3C25 24.3 23.8 23.8 22.5 23.8C20.3 23.8 19 25 19 26.8"
               "C19 30.8 26.3 29.5 26.3 34C26.3 36 24.8 37.5 22.5 37.5C21 37.5 19.5 37 18.5 36", HOLE, 2.8)
    u = stroke("M29.5 28V34C29.5 36.3 31 37.5 32.8 37.5C34.6 37.5 36 36.3 36 34M36 28V37.5", HOLE, 2.8)
    b = (stroke("M39.8 23V37.5", HOLE, 2.8) +
         f'<circle cx="42.6" cy="34" r="3.3" fill="none" stroke="{HOLE}" stroke-width="2.8"/>')
    return _sub_screen() + s + u + b

@reg("subtitleeditor", TEAL_DEEP)
def subtitleeditor():
    bubble = rrect(14, 13, 32, 25, 5, INK) + poly([(19, 35), (28, 35), (19, 43.5)], INK, 2.5)
    lines = "".join(rrect(19.5, y, w, 2.8, 1.4, HOLE) for y, w in [(19, 21), (24.5, 21), (30, 13)])
    badge = circle(41.5, 38, 9.5, PURPLE, f' stroke="{HOLE}" stroke-width="2"')
    pencil = line(37.5, 42, 44.5, 35, INK, 3.4) + poly([(35.5, 44), (36.2, 40.6), (38.9, 43.3)], INK, 1)
    return bubble + lines + badge + pencil

@reg("sunflower", AMBER_DEEP)
def sunflower():
    pts = [pt(CX, CY, 17.5 if k % 2 == 0 else 14, -90 + 11.25 * k) for k in range(32)]
    return poly(pts, INK, 1.5) + circle(CX, CY, 11, BROWN_DEEP)

SUNVOX = [".XX.XX.",
          ".X...X.",
          "XX.X.XX",
          ".X...X.",
          ".XX.XX.",
          "..X.X..",
          "XXXXXXX"]

@reg("sunvox", GREY_SOFT)
def sunvox():
    return _pixels(SUNVOX, 13.8, 11.8, 5.2, INK)

@reg("super-hexagon", RED_DEEP)
def super_hexagon():
    outer = _hex(CX, CY, 15.5, -90)
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in outer[1:] + outer[:1])
    ring = f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>'
    inner = poly(_hex(CX, CY, 5.5, -60), INK, 2)
    cursor = poly([(32, 18.5), (35, 22.5), (29, 22.5)], INK, 1.2)
    return ring + inner + cursor

@reg("superkaramba", BLUE_GREY_DEEP)
def superkaramba():
    frame = cut("M18 15H46A4 4 0 0 1 50 19V41A4 4 0 0 1 46 45H18A4 4 0 0 1 14 41V19A4 4 0 0 1 18 15Z"
                "M20.5 19.5H43.5A2 2 0 0 1 45.5 21.5V38.5A2 2 0 0 1 43.5 40.5H20.5A2 2 0 0 1 18.5 38.5V21.5A2 2 0 0 1 20.5 19.5Z", INK)
    return frame + rrect(36.5, 22.5, 6, 15, 2, INK)

@reg("supermeatboy", RED_DEEP)
def supermeatboy():
    body = path("M19 14H45A4 4 0 0 1 49 18V40A4 4 0 0 1 45 44H39V48H33V44H31V48H25V44H19"
                "A4 4 0 0 1 15 40V18A4 4 0 0 1 19 14Z", INK)
    eyes = circle(24.5, 25, 2.8, HOLE) + circle(40, 25, 2.8, HOLE)
    grin = path("M20.5 31H43.5C43 36.5 38 39.5 32 39.5C26 39.5 21 36.5 20.5 31Z", HOLE)
    aid = g(rrect(34, 17.5, 11, 3.6, 1.8, HOLE), "rotate(35 39.5 19.3)")
    return body + eyes + grin + aid

@reg("superpaper", GREY_DARK)
def superpaper():
    banner = path("M15 15Q32 21.5 49 15V45Q32 38.5 15 45Z", INK)
    hills = poly([(19.5, 37.5), (26, 29), (30, 33.5), (35.5, 26), (44.5, 37.5)], HOLE, 2)
    return banner + hills

@reg("superproductivity", BLUE_DEEP)
def superproductivity():
    return poly([(15, 30.5), (29, 37.5), (47.5, 14), (31, 46)], INK, 2.5)

@reg("supertux", LIGHT_BLUE_SOFT)
def supertux():
    body = path("M32 12C24 12 20.5 18 20.5 25C20.5 29 18 32 16.5 36C15 40.5 18 46 24 46.5H40"
                "C46 46 49 40.5 47.5 36C46 32 43.5 29 43.5 25C43.5 18 40 12 32 12Z", INK)
    belly = path("M32 26C26.5 26 23.5 31 23.5 36.5C23.5 41.5 27 44 32 44C37 44 40.5 41.5 40.5 36.5"
                 "C40.5 31 37.5 26 32 26Z", WHITE)
    eyes = (circle(27.5, 20.5, 3.4, WHITE) + circle(36.5, 20.5, 3.4, WHITE) +
            circle(28.3, 21, 1.6, INK) + circle(35.7, 21, 1.6, INK))
    beak = poly([(28.5, 26), (35.5, 26), (32, 30.5)], DEEP_ORANGE, 1.5)
    return body + belly + eyes + beak

@reg("supertuxkart", RED_DEEP)
def supertuxkart():
    head = path("M32 12C25 12 21.5 17 21.5 23V32H42.5V23C42.5 17 39 12 32 12Z", BLUE_GREY_DARK)
    face = circle(28, 22, 3.2, INK) + circle(36, 22, 3.2, INK) + circle(28.6, 22.4, 1.4, BLUE_GREY_DARK) + \
        circle(35.4, 22.4, 1.4, BLUE_GREY_DARK)
    beak = poly([(28.5, 26.5), (35.5, 26.5), (32, 30.5)], AMBER, 1.5)
    kart = path("M15 36C15 32 18 30.5 22 30.5H42C46 30.5 49 32 49 36V38C49 40 47.5 41 45.5 41H18.5"
                "C16.5 41 15 40 15 38Z", INK)
    wheels = rrect(15, 41, 9, 6.5, 2.5, INK) + rrect(40, 41, 9, 6.5, 2.5, INK)
    slot = rrect(27, 34, 10, 3, 1.5, HOLE)
    return head + face + beak + kart + wheels + slot

@reg("surfshark", CYAN_DEEP)
def surfshark():
    fin = path("M24.5 13H44A3.5 3.5 0 0 1 47.4 17L43.6 44A3.5 3.5 0 0 1 40 47H20.5"
               "A3.5 3.5 0 0 1 17 43L20.9 16A3.5 3.5 0 0 1 24.5 13Z", INK)
    s = stroke("M40 20.5C37 18 30.5 18.5 30.5 23.5C30.5 28 36.5 29.5 35.5 34.5C34.5 39.5 28.5 40.5 24 38.5", HOLE, 3.6)
    return fin + s

@reg("surviving-mars", DEEP_ORANGE_LIGHT)
def surviving_mars():
    dome = path("M17.8 41.5A16.5 16.5 0 1 1 46.2 41.5C40.5 39.5 34 33.5 32 19.5"
                "C30 33.5 23.5 39.5 17.8 41.5Z", INK)
    return dome

@reg("sven-co-op", INDIGO)
def sven_co_op():
    ring = f'<circle cx="32" cy="30" r="15.5" fill="none" stroke="{INK}" stroke-width="3.2"/>'
    lam = stroke("M24.5 19.5H28.5L39.5 41", INK, 3.6) + stroke("M32.5 28.5L24.5 41", INK, 3.6)
    return ring + lam

@reg("svgcleaner", BLUE_DEEP)
def svgcleaner():
    blade = line(20, 20.5, 41, 11.5, INK, 5.5)
    handle = line(31, 16.5, 47, 36, INK, 3.4)
    s = stroke("M20.5 35.2C19.9 34.4 19 34 18 34C16.6 34 15.5 34.8 15.5 36C15.5 38.8 20.8 38 20.8 41"
               "C20.8 42.5 19.6 43.5 18 43.5C16.8 43.5 15.8 43 15 42.2", INK, 2.4)
    v = stroke("M23.5 34L27 43.5L30.5 34", INK, 2.4)
    gg = stroke("M39.5 35C38.8 34.3 37.8 34 36.8 34C34.5 34 33 36 33 38.8C33 41.5 34.5 43.5 36.8 43.5"
                "C38.5 43.5 39.8 42.5 39.8 40.5V39H37", INK, 2.4)
    return blade + handle + s + v + gg

@reg("svp-manager4", DEEP_ORANGE)
def svp_manager4():
    arcs = "".join(stroke(_arc_c(CX, CY, 15, a, a + 100), INK, 4.2) for a in (-80, 40, 160))
    play = poly([(27.5, 21.5), (40.5, 30), (27.5, 38.5)], INK, 3)
    return arcs + play

@reg("sw4stm32", LIGHT_BLUE)
def sw4stm32():
    upper = path("M26 33C21 25 23.5 15.5 31.5 14.5C36.5 14 41.5 15 47.5 12C48.5 21 44.5 30 33.5 33Z", INK)
    lower = path("M26 33C27 39 30 45.5 36.5 45.5C41.5 45.5 43.5 40.5 41 36.5C38.5 33.5 33 32.5 26 33Z", INK)
    body = g(rrect(15, 30.5, 13, 5, 2.5, INK), "rotate(-35 21.5 33)")
    return upper + lower + line(28, 33.5, 34, 32.8, HOLE, 1.8) + body

@reg("swatchbooker", PINK_LIGHT)
def swatchbooker():
    out = ""
    for a in (-90, -62, -34):
        out += g(rrect(18.5, 15, 9, 31, 4.5, INK, f' stroke="{HOLE}" stroke-width="1.8"'),
                 f"rotate({a + 90} 23 41.5)")
    base = rrect(14.5, 37, 35, 9, 4.5, INK, f' stroke="{HOLE}" stroke-width="1.8"')
    return out + base + circle(19.5, 41.5, 2, HOLE)

@reg("sweeper", BLUE_GREY_DEEP)
def sweeper():
    out = ""
    for k in range(3):
        a = -70 + 120 * k
        out += stroke(_arc_c(CX, CY, 13, a, a + 62), INK, 4.4)
        out += _head(CX, CY, 13, a + 62, 5.5, INK)
    return out

@reg("sweethome3d", BLUE_DEEP)
def sweethome3d():
    hexa = poly(_hex(CX, CY, 17.5, -90), INK, 3)
    c, s = 9, 5.2
    top = poly([(32, 30 - c), (32 + c * .87, 30 - c / 2), (32, 30), (32 - c * .87, 30 - c / 2)], RED_SOFT, 1.5)
    left = poly([(32 - c * .87, 30 - c / 2), (32, 30), (32, 30 + c), (32 - c * .87, 30 + c / 2)], RED, 1.5)
    right = poly([(32 + c * .87, 30 - c / 2), (32, 30), (32, 30 + c), (32 + c * .87, 30 + c / 2)], RED_DEEP, 1.5)
    return hexa + top + left + right

@reg("sweethome3d-furniture-editor", BROWN)
def sh3d_furniture():
    hutch = rrect(17, 13, 30, 12, 2, INK)
    cells = "".join(rrect(x, 15.5, 7.2, 3, .8, HOLE) + rrect(x, 20, 7.2, 3, .8, HOLE) for x in (19.5, 28.4, 37.3))
    top = rrect(13.5, 25.5, 37, 4.5, 2.2, INK)
    left = rrect(16, 30, 11, 17, 1.5, INK)
    right = rrect(37, 30, 11, 17, 1.5, INK)
    back = rrect(27, 30, 10, 13, 0, BROWN_DEEP)
    seams = "".join(line(17, y, 26, y, HOLE, 1.6, "butt") + line(38, y, 47, y, HOLE, 1.6, "butt")
                    for y in (35.7, 41.3))
    return hutch + cells + top + back + left + right + seams

@reg("sweethome3d-textures-editor", BROWN_LIGHT)
def sh3d_textures():
    outer = cut("M18 14H46A4 4 0 0 1 50 18V42A4 4 0 0 1 46 46H18A4 4 0 0 1 14 42V18A4 4 0 0 1 18 14Z"
                "M21 18.5H43A2 2 0 0 1 45 20.5V39.5A2 2 0 0 1 43 41.5H21A2 2 0 0 1 19 39.5V20.5A2 2 0 0 1 21 18.5Z", INK)
    inner = rrect(22.5, 21.5, 19, 17, 2.5, BROWN_DEEP)
    tile = rrect(27, 25, 10, 10, 1.5, INK)
    return outer + inner + tile

@reg("swell-foop", BLUE_DEEP)
def swell_foop():
    star = poly([pt(23, 21, 7.8 if k % 2 == 0 else 3.4, -90 + 36 * k) for k in range(10)], INK, 1.8)
    return (star + circle(41, 21, 7, INK) + circle(23, 39, 7, INK) +
            rrect(34.5, 32.5, 13, 13, 2.5, INK))

SXIV = [".XX.X.X.X.X.X",
        "X...X.X...X.X",
        ".X...X..X.X.X",
        "..X.X.X.X.X.X",
        "XX..X.X.X..X."]

@reg("sxiv", BLUE_GREY_DARK)
def sxiv():
    letters = _pixels(SXIV, 13.5, 14, 2.85, INK)
    hills = path("M14 45V40C20 34 27 33 33 37C38 40 43 36 50 33V45Z", GREY)
    return letters + hills

@reg("synapse", TEAL)
def synapse():
    ring = f'<circle cx="32" cy="30" r="13" fill="none" stroke="{INK}" stroke-width="3.4"/>'
    ticks = line(32, 12, 32, 17, INK, 3.4) + line(32, 43, 32, 48, INK, 3.4)
    s = stroke("M37 24.5C36 23.3 34.3 22.5 32.2 22.5C29.3 22.5 27.3 24 27.3 26.2C27.3 31.2 37 28.5 37 33.6"
               "C37 36 34.8 37.5 31.8 37.5C29.5 37.5 27.8 36.6 26.8 35.3", INK, 3.2)
    return ring + ticks + s

@reg("synaptic", PINK_LIGHT)
def synaptic():
    arcs = stroke(_arc_c(CX, CY, 14, -40, 120), INK, 4.6) + stroke(_arc_c(CX, CY, 14, 140, 300), INK, 4.6)
    arrow = line(32, 18.5, 32, 35, INK, 4.4) + poly([(24.5, 30.5), (39.5, 30.5), (32, 40.5)], INK, 2.5)
    return arcs + arrow

@reg("syncplay", PINK_LIGHT)
def syncplay():
    feathers = (stroke("M22 40C27 26 36 17 48 14", INK, 3.4) +
                stroke("M29 43C34 34 41 28 49 26", INK, 3.4) +
                stroke("M19 33C22 23 28 16 36 12.5", INK, 3.4))
    ring = circle(26, 36, 10.5, INK) + circle(26, 36, 7.5, HOLE)
    play = poly([(23.5, 31.5), (31, 36), (23.5, 40.5)], INK, 1.5)
    return feathers + ring + play

@reg("syncthing-gtk", LIGHT_BLUE_DEEP)
def syncthing_gtk():
    ring = f'<circle cx="32" cy="30" r="14.5" fill="none" stroke="{INK}" stroke-width="3"/>'
    a, b, c, m = pt(CX, CY, 14.5, 192), pt(CX, CY, 14.5, -48), pt(CX, CY, 14.5, 62), (35, 30.5)
    links = (line(*a, *m, INK, 2.6) + line(*m, *b, INK, 2.6) + line(*m, *c, INK, 2.6))
    nodes = "".join(circle(x, y, 3.6, INK) for x, y in (a, b, c, m))
    return ring + links + nodes

@reg("synergy", BLUE_GREY_DEEP)
def synergy():
    arcs = "".join(stroke(_arc_c(CX, CY, 14.5, a + 8, a + 82), INK, 5) for a in (-90, 0, 90, 180))
    return arcs + circle(CX, CY, 8.5, INK)

@reg("synergy-mod", BLUE_LIGHT)
def synergy_mod():
    arcs = "".join(stroke(_arc_c(CX, CY, 14.5, a + 12, a + 78), INK, 4.4) for a in (-90, 0, 90, 180))
    hub = f'<circle cx="32" cy="30" r="6" fill="none" stroke="{INK}" stroke-width="3.6"/>'
    spokes = (line(32, 15.5, 32, 24, INK, 3.6) + line(32, 36, 32, 44.5, INK, 3.6) +
              line(17.5, 30, 26, 30, INK, 3.6) + line(38, 30, 46.5, 30, INK, 3.6))
    return arcs + hub + spokes

@reg("synfig_icon", BLUE_DEEP)
def synfig():
    arch = path("M32 11C40 19.5 47.5 31 47.5 47H16.5C16.5 31 24 19.5 32 11Z", INK)
    rays = "".join(line(32, 47, *pt(32, 47, 30, a), HOLE, 2.2, "butt") for a in (-150, -126, -102, -78, -54, -30))
    return arch + rays

@reg("synology-assistant", BLUE_DEEP)
def synology_assistant():
    ring = f'<circle cx="30.5" cy="28.5" r="12" fill="none" stroke="{INK}" stroke-width="4"/>'
    plus = line(30.5, 22.5, 30.5, 34.5, INK, 4) + line(24.5, 28.5, 36.5, 28.5, INK, 4)
    return ring + plus + circle(44, 42, 3.4, INK)

def _cloud():
    return (circle(23.5, 33, 8, INK) + circle(33.5, 26.5, 11, INK) + circle(42, 34, 7, INK) +
            rrect(15.5, 33, 33.5, 10, 5, INK))

@reg("synology-cloud-station-backup", BLUE)
def syn_cloud_backup():
    ring = f'<circle cx="32.5" cy="32.5" r="7" fill="none" stroke="{HOLE}" stroke-width="2.4"/>'
    arrow = line(32.5, 30, 32.5, 36.5, HOLE, 2.4) + poly([(29.3, 31.3), (35.7, 31.3), (32.5, 27.5)], HOLE, 1.2)
    return _cloud() + ring + arrow

@reg("synology-cloud-station-drive", BLUE)
def syn_cloud_drive():
    a = (stroke(_arc_c(32.5, 32.5, 6, 200, 320), HOLE, 2.6) + _head(32.5, 32.5, 6, 320, 3, HOLE) +
         stroke(_arc_c(32.5, 32.5, 6, 20, 140), HOLE, 2.6) + _head(32.5, 32.5, 6, 140, 3, HOLE))
    return _cloud() + a

@reg("synology-drive", BLUE_DARK)
def synology_drive():
    chev = stroke("M17 17.5L26 30L17 42.5", CYAN_SOFT, 5.5)
    d = stroke("M28.5 17.5H38L46.5 30L38 42.5H28.5", INK, 5.5)
    return chev + d

@reg("synology-note-station", BLUE)
def syn_note():
    card = rrect(14, 14, 27, 33, 4, INK)
    band = rrect(14, 30, 27, 8, 0, BLUE_DARK) + rrect(18, 32.3, 10, 3.2, 1.6, INK)
    lines = rrect(18, 20, 16, 3, 1.5, HOLE) + rrect(18, 25, 11, 3, 1.5, HOLE)
    pencil = (line(47.5, 16, 37, 38, HOLE, 8) + line(47.5, 16, 37, 38, INK, 4.6) +
              poly([(34.8, 36.8), (39.2, 38.9), (35.5, 43.5)], INK, 1.2))
    return card + band + lines + pencil

@reg("syspeek", GREY_DARK)
def syspeek():
    return rrect(18, 13, 28, 34, 3.5, INK) + rrect(21.5, 33, 21, 10, 1.5, HOLE)

@reg("systach", CYAN_DARK)
def systach():
    dots = "".join(circle(*pt(CX, CY, 14.5, a), 2.1, INK) for a in range(135, 406, 30))
    needle = line(32, 30, *pt(CX, CY, 11, -125), INK, 3)
    return dots + needle + circle(CX, CY, 4, INK)

@reg("system-config-samba", BLUE_LIGHT)
def samba():
    up = line(25, 20, 25, 44, INK, 4.6) + poly([(18, 23.5), (32, 23.5), (25, 14.5)], INK, 2.5)
    dn = line(39, 16, 39, 40, INK, 4.6) + poly([(32, 36.5), (46, 36.5), (39, 45.5)], INK, 2.5)
    return up + dn

@reg("system-error", RED_DEEP)
def system_error():
    return rrect(28.5, 12, 7, 23, 3.5, INK) + circle(32, 43.5, 4, INK)

@reg("system-file-manager", BLUE_GREY)
def system_file_manager():
    sheets = rrect(18, 13, 28, 10, 2.5, BLUE_GREY_SOFT) + rrect(16, 18, 32, 10, 2.5, GREY_SOFT)
    drawer = rrect(13.5, 23, 37, 24, 4, INK)
    return sheets + drawer + rrect(26, 29, 12, 3.6, 1.8, HOLE)

@reg("system-help", RED_DEEP)
def system_help():
    ring = cut(cpath(CX, CY, 16.5) + cpath(CX, CY, 7.5), INK)
    bands = "".join(stroke(_arc_c(CX, CY, 12, a - 20, a + 20), HOLE, 9) for a in (-90, 0, 90, 180))
    bands = bands.replace('stroke-linecap="round"', 'stroke-linecap="butt"')
    return ring + bands

@reg("system-keyboard-mx", BLUE)
def keyboard_mx():
    board = rrect(12.5, 17, 39, 26, 4, INK)
    keys = "".join(circle(18.5 + 5.4 * i, 23, 1.9, HOLE) for i in range(6))
    keys += "".join(circle(21.2 + 5.4 * i, 29, 1.9, HOLE) for i in range(5))
    return board + keys + rrect(21, 34.5, 22, 3.6, 1.8, HOLE)

@reg("system-lock-screen", DEEP_ORANGE)
def lock_screen():
    shackle = stroke("M23.5 28V22A8.5 8.5 0 0 1 40.5 22V28", INK, 4.6)
    body = rrect(16.5, 26, 31, 21, 4, INK)
    return shackle + body + circle(32, 34.5, 3, HOLE) + rrect(30.6, 34.5, 2.8, 7, 1.4, HOLE)

@reg("system-log-out", BROWN_SOFT)
def log_out():
    arc = stroke(_arc_c(CX, CY, 14, 40, 320), INK, 5)
    arrow = line(29, 30, 42, 30, INK, 5) + poly([(40, 22.5), (49, 30), (40, 37.5)], INK, 2.5)
    return arc + arrow

@reg("system-reboot", ORANGE_DEEP)
def reboot():
    out = ""
    for a in (-160, 20):
        out += stroke(_arc_c(CX, CY, 13.5, a, a + 120), INK, 4.8) + _head(CX, CY, 13.5, a + 120, 6.5, INK)
    return out

@reg("system-save-session", PINK_DEEP)
def save_session():
    disk = path("M18 13H41L49 21V43A4 4 0 0 1 45 47H18A4 4 0 0 1 14 43V17A4 4 0 0 1 18 13Z", INK)
    shutter = rrect(21, 13, 17, 10, 1.5, HOLE) + rrect(31.5, 15, 4, 6, 1, INK)
    label = rrect(20, 30, 24, 17, 2, HOLE) + rrect(34, 36, 4, 11, 0, INK)
    return disk + shutter + label

@reg("system-shutdown", RED)
def shutdown():
    return stroke(_arc_c(CX, 31.5, 14, -55, 235), INK, 5) + line(32, 13, 32, 29, INK, 5)

@reg("system-software-install", BLUE_GREY_DEEP)
def software_install():
    squares = rrect(14, 12, 16, 16, 3.5, INK) + rrect(34, 12, 16, 16, 3.5, INK) + rrect(14, 32, 16, 16, 3.5, INK)
    arrow = line(42, 31.5, 42, 42, INK, 4.4) + poly([(35.5, 39.5), (48.5, 39.5), (42, 47)], INK, 2)
    return squares + arrow

@reg("system-software-update", AMBER_DEEP)
def software_update():
    out = ""
    for a in (-155, 25):
        out += stroke(_arc_c(CX, CY, 15, a, a + 125), INK, 4.2) + _head(CX, CY, 15, a + 125, 5.5, INK)
    return out + rrect(22, 26.5, 20, 7, 3.5, INK) + rrect(25, 28.7, 10, 2.6, 1.3, HOLE)

@small("subtitlecomposer")
def subtitlecomposer_s():
    s = stroke("M38 22.5C36.5 21 34.5 20.5 32.5 20.5C28.8 20.5 26.5 22.3 26.5 25"
               "C26.5 31 38 29 38 35C38 37.8 35.5 39.8 31.8 39.8C29.3 39.8 27.2 39 25.8 37.5", HOLE, 4.2)
    return _sub_screen() + s

@small("subtitleeditor")
def subtitleeditor_s():
    bubble = rrect(14, 13, 32, 25, 5, INK) + poly([(19, 35), (28, 35), (19, 43.5)], INK, 2.5)
    lines = rrect(19, 19, 22, 4, 2, HOLE) + rrect(19, 27, 14, 4, 2, HOLE)
    return bubble + lines + circle(42, 39, 9.5, PURPLE, f' stroke="{HOLE}" stroke-width="2"')

@small("sxiv")
def sxiv_s():
    rows = [".XX.X.X",
            "X...X.X",
            ".X...X.",
            "..X.X.X",
            "XX..X.X"]
    return _pixels(rows, 16, 14, 4.6, INK) + path("M14 46V41C20 36 27 35 33 38.5C38 41 43 37 50 34.5V46Z", INDIGO_SOFT)

@small("svgcleaner")
def svgcleaner_s():
    return (line(17, 25, 41, 14, INK, 7) + line(29, 19.5, 46, 44, INK, 4.4) +
            stroke("M25 33.5C24 32.5 22.8 32 21.5 32C19.5 32 18 33.2 18 35C18 39 25.5 38 25.5 42.3"
                   "C25.5 44.3 23.8 45.8 21.5 45.8C19.8 45.8 18.5 45 17.5 44", INK, 3.6))

@small("sweethome3d-furniture-editor")
def sh3d_furniture_s():
    hutch = rrect(17, 13, 30, 11, 2, INK) + rrect(20, 16.5, 24, 4, 1, HOLE)
    top = rrect(13.5, 25.5, 37, 5, 2.5, INK)
    return hutch + top + rrect(16, 30, 12, 17, 1.5, INK) + rrect(36, 30, 12, 17, 1.5, INK)

@small("synfig_icon")
def synfig_s():
    arch = path("M32 11C40 19.5 47.5 31 47.5 47H16.5C16.5 31 24 19.5 32 11Z", INK)
    rays = "".join(line(32, 47, *pt(32, 47, 30, a), HOLE, 3, "butt") for a in (-135, -90, -45))
    return arch + rays

@small("syncthing-gtk")
def syncthing_s():
    ring = f'<circle cx="32" cy="30" r="14.5" fill="none" stroke="{INK}" stroke-width="3.6"/>'
    a, b, m = pt(CX, CY, 14.5, 192), pt(CX, CY, 14.5, -48), (35, 32)
    return ring + line(*a, *m, INK, 3.4) + line(*m, *b, INK, 3.4) + "".join(
        circle(x, y, 4.6, INK) for x, y in (a, b, m))

@small("systach")
def systach_s():
    dots = "".join(circle(*pt(CX, CY, 14.5, a), 2.8, INK) for a in range(135, 406, 45))
    return dots + line(32, 30, *pt(CX, CY, 11, -125), INK, 3.6) + circle(CX, CY, 4.5, INK)

@small("system-keyboard-mx")
def keyboard_mx_s():
    board = rrect(12, 16, 40, 28, 4.5, INK)
    keys = "".join(rrect(17 + 8 * i, 21, 5, 5, 1.2, HOLE) for i in range(4))
    return board + keys + rrect(21, 33, 22, 5, 2.5, HOLE)

@small("synology-note-station")
def syn_note_s():
    card = rrect(14, 14, 27, 33, 4, INK) + rrect(14, 30, 27, 8, 0, BLUE_DARK)
    pencil = line(47.5, 16, 37, 38, HOLE, 9) + line(47.5, 16, 37, 38, INK, 5.5)
    return card + rrect(18, 20, 16, 4, 2, HOLE) + pencil

@small("supermeatboy")
def supermeatboy_s():
    body = path("M19 14H45A4 4 0 0 1 49 18V40A4 4 0 0 1 45 44H39V48H33V44H31V48H25V44H19"
                "A4 4 0 0 1 15 40V18A4 4 0 0 1 19 14Z", INK)
    return (body + circle(24.5, 24.5, 3.4, HOLE) + circle(40, 24.5, 3.4, HOLE) +
            path("M20.5 31H43.5C43 36.5 38 39.5 32 39.5C26 39.5 21 36.5 20.5 31Z", HOLE))

@small("supertuxkart")
def supertuxkart_s():
    head = path("M32 12C25 12 21.5 17 21.5 23V32H42.5V23C42.5 17 39 12 32 12Z", BLUE_GREY_DARK)
    face = circle(28, 22, 3.6, INK) + circle(36, 22, 3.6, INK)
    kart = path("M15 36C15 32 18 30.5 22 30.5H42C46 30.5 49 32 49 36V41C49 43 47.5 44 45.5 44H18.5"
                "C16.5 44 15 43 15 41Z", INK)
    return head + face + kart + rrect(15, 42, 10, 6, 2.5, INK) + rrect(39, 42, 10, 6, 2.5, INK)

@small("system-help")
def system_help_s():
    ring = cut(cpath(CX, CY, 17) + cpath(CX, CY, 7), INK)
    bands = "".join(stroke(_arc_c(CX, CY, 12, a - 12, a + 12), HOLE, 6.8) for a in (-90, 0, 90, 180))
    return ring + bands.replace('stroke-linecap="round"', 'stroke-linecap="butt"')

@small("sweeper")
def sweeper_s():
    out = ""
    for k in range(3):
        a = -70 + 120 * k
        out += stroke(_arc_c(CX, CY, 12.5, a, a + 55), INK, 4) + _head(CX, CY, 12.5, a + 55, 6.5, INK)
    return out
