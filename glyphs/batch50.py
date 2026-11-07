# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 50: oolite to org.eu.encom.spectral.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
import math
from lm import *
from glyphs.kit import arc_b, arrowhead_b, crescent_e, _gear_h, registry, ring_b

ICONS, SMALL, reg, small = registry()

@reg("oolite", DEEP_PURPLE_DEEP)
def oolite():
    wings = (poly([(14, 13), (30, 26), (30, 32), (14, 20)], INK, 2) +
             poly([(50, 13), (34, 26), (34, 32), (50, 20)], INK, 2))
    band = rrect(18, 30, 28, 5, 2.5, DEEP_PURPLE_SOFT)
    tail = poly([(28, 33), (36, 33), (34, 41), (32, 48), (30, 41)], INK, 2)
    head = circle(32, 25, 6, HOLE) + circle(32, 25, 4.2, INK)
    return wings + band + tail + head

@reg("openage", GREY_DARK)
def openage():
    tower = path("M19 12H25V17H29V12H35V17H39V12H45V30C45 37 41.5 41.5 38.5 44L43 48H21"
                 "L25.5 44C22.5 41.5 19 37 19 30Z", INK,
                 f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    shield = path("M24.5 23Q32 20.5 39.5 23V30C39.5 35 36 38.5 32 41C28 38.5 24.5 35 24.5 30Z", HOLE)
    return tower + shield

@reg("openarena", INDIGO_DEEP)
def openarena():
    halo = f'<ellipse cx="32" cy="29" rx="15.5" ry="10" fill="none" stroke="{INK}" stroke-width="4"/>'
    a = stroke("M22.5 44L32 18.5L41.5 44", HOLE, 8.5) + stroke("M22.5 44L32 18.5L41.5 44", INK, 4.2)
    gem = poly([(32, 34), (35, 38.5), (32, 43), (29, 38.5)], INK, 1.5)
    return halo + a + gem

@reg("openclonk", RED)
def openclonk():
    shield = path("M17 15H47V28C47 37.5 40.5 43.5 32 47.5C23.5 43.5 17 37.5 17 28Z", INK,
                  f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    rifle = line(17, 17, 45, 45, RED_DARK, 3.2) + line(40, 40, 46, 46, RED_DARK, 5)
    shovel = line(20, 44, 40, 22, RED_DARK, 3.2)
    blade = g(rrect(38, 11, 9, 12, 3, RED_DARK), "rotate(42 42.5 17)")
    return shield + rifle + shovel + blade

@reg("openmw", BROWN_DARK)
def openmw():
    moon = crescent_e((31, 30), 17, (36.5, 29.5), 15.5, INK)
    star = ""
    for k in range(6):
        a = -90 + 60 * k
        tx, ty = pt(37, 30, 10.5, a)
        c1 = pt(37, 30, 6.5, a + 40)
        c2 = pt(37, 30, 3.5, a - 25)
        star += path(f"M37 30Q{f(c1[0])} {f(c1[1])} {f(tx)} {f(ty)}Q{f(c2[0])} {f(c2[1])} 37 30Z", INK,
                     f' stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"')
    return moon + star + circle(37, 30, 2.4, INK)

@reg("openmw-cs", BROWN_DARK)
def openmw_cs():
    return crescent_e((31, 30), 17, (36.5, 29.5), 15.5, INK) + _gear_h(37.5, 30, 7.4, 8, INK)

@reg("openra-cnc", GREY_DARK)
def openra_cnc():
    rim = ring_b(32, 30, 15.5, INK, 3.6)
    c = arc_b(32, 30, 9, 45, 315, RED_LIGHT, 4.2)
    cross = rrect(29, 25, 6, 10, 1.5, INK) + rrect(27, 27, 10, 6, 1.5, INK)
    return rim + c + g(cross, "translate(3 0)")

@reg("openra-d2k", DEEP_ORANGE_DEEP)
def openra_d2k():
    far = circle(19, 16.5, 5, DEEP_ORANGE_SOFT)
    planet = circle(31, 30, 15, HOLE) + circle(31, 30, 13.5, INK)
    spots = (path("M22 24C25 21 29 22 28 26C27 29 23 29 22 27Z", HOLE) +
             path("M31 34C34 32 37 34 35 37C33 39 30 38 31 34Z", HOLE) +
             circle(35, 22.5, 2.2, HOLE))
    moon = circle(42, 39, 7.5, HOLE) + circle(42, 39, 5.8, INK) + circle(43.5, 40, 1.8, HOLE)
    return far + planet + spots + moon

@reg("openra-ra", RED_DEEP)
def openra_ra():
    pts = [pt(32, 31, 18 if k % 2 == 0 else 8.2, -90 + 36 * k) for k in range(10)]
    star = poly(pts, INK, 3)
    sickle = stroke("M28.5 26.5A6.2 6.2 0 1 0 36.5 34", HOLE, 2.3) + line(29, 36, 26.5, 38.5, HOLE, 2.6)
    hammer = line(28, 35, 35.5, 27.5, HOLE, 2.3) + line(33, 25, 38, 30, HOLE, 3)
    return star + sickle + hammer

@reg("openrct2", BLUE_DEEP)
def openrct2():
    flag = line(32, 12, 32, 19, INK, 2.2) + poly([(32, 11.5), (38.5, 13.8), (32, 16.2)], INK, 1.5)
    dome = path("M26.5 23.5A5.5 5.5 0 0 1 37.5 23.5Z", INK)
    tower = poly([(27.5, 24.5), (36.5, 24.5), (41.5, 47), (22.5, 47)], INK, 2.5)
    stripes = line(30.2, 27.5, 28.8, 45, HOLE, 2.2) + line(33.8, 27.5, 35.2, 45, HOLE, 2.2)
    return flag + dome + tower + stripes

@reg("openspades", DEEP_PURPLE_DEEP)
def openspades():
    head = rrect(16, 14, 32, 32, 5, INK)
    hair = path("M16 26V19A5 5 0 0 1 21 14H43A5 5 0 0 1 48 19V26Z", DEEP_PURPLE_SOFT)
    eyes = rrect(22, 26, 6, 7, 1, HOLE) + rrect(36, 26, 6, 7, 1, HOLE)
    return head + hair + eyes

@reg("openttd", ORANGE_DEEP)
def openttd():
    diamond = g(rrect(19, 17, 26, 26, 5, INK), "rotate(45 32 30)")
    s = stroke("M36.5 23.8C35.5 22.6 34 22 32 22C29.3 22 27.5 23.4 27.5 25.6"
               "C27.5 30.3 36.5 29 36.5 34.2C36.5 36.5 34.6 38 32 38C29.8 38 28 37.2 27 36", HOLE, 3.2)
    return diamond + s + line(32, 18.5, 32, 41.5, HOLE, 2.4)

@reg("opentyrian", BLUE_GREY_DARK)
def opentyrian():
    hull = path("M28.5 15H35.5L38 25L35.5 40L32 46L28.5 40L26 25Z", INK)
    wings = (poly([(26, 21), (17, 13.5), (15.5, 20), (25, 29)], INK, 2) +
             poly([(38, 21), (47, 13.5), (48.5, 20), (39, 29)], INK, 2))
    claws = (stroke("M26.5 31C20.5 32 17 37 18.5 45", INK, 3.4) +
             stroke("M37.5 31C43.5 32 47 37 45.5 45", INK, 3.4))
    core = circle(32, 26, 2.8, ORANGE) + rrect(30, 32, 4, 6, 1.2, HOLE)
    return wings + claws + hull + core

@reg("openxcom", TEAL_DEEP)
def openxcom():
    x = line(17, 15, 47, 45, TEAL_SOFT, 6) + line(47, 15, 17, 45, TEAL_SOFT, 6)
    head = path("M32 17C40 17 44 22 44 28C44 35 37 41 32 43C27 41 20 35 20 28C20 22 24 17 32 17Z", INK,
                f' stroke="{HOLE}" stroke-width="2.4"')
    eyes = (poly([(23.5, 27), (29.5, 29.5), (28.5, 33), (24.5, 31)], HOLE, 1.5) +
            poly([(40.5, 27), (34.5, 29.5), (35.5, 33), (39.5, 31)], HOLE, 1.5))
    return x + head + eyes

@reg("org.es_de.emulationstation-de", RED_DEEP)
def es_de():
    e = stroke("M29 18H18.5V42H29M18.5 30H27", INK, 5)
    s = stroke("M46 21C44.5 19 42.5 18 40 18C36.6 18 34.3 20 34.3 23.4"
               "C34.3 29.6 46.5 28 46.5 35C46.5 39.3 43.6 42 39.6 42C37 42 34.8 41 33.3 39", INK, 5)
    return e + s

def _opera():
    return cut("M32 13a14 17 0 1 0 0.01 0Z" + "M32 18.5a6.5 11.5 0 1 0 0.01 0Z", INK)

@reg("opera-beta", RED_DEEP)
def opera_beta():
    return _opera()

@reg("opera-developer", GREY_DEEP)
def opera_developer():
    return _opera()

@reg("openoffice4-main", BLUE_DEEP)
def oo_main():
    def gull(s, dx, dy):
        d = ("M13 40C20 33 28 33 33 38.5C38 31.5 46 29 51 31C44 33 38.5 37 34.5 43.5"
             "C29.5 38.5 21 37.5 13 40Z")
        return g(path(d, INK), f"translate({dx} {dy}) scale({s})")
    return gull(1, 0, 1) + gull(.62, 17, 2)

@reg("openoffice4-base", PINK)
def oo_base():
    body = path("M20.5 19A11.5 4.8 0 0 1 43.5 19V41A11.5 4.8 0 0 1 20.5 41Z", INK)
    seams = (stroke("M20.5 19A11.5 4.8 0 0 0 43.5 19", HOLE, 2.2) +
             stroke("M20.5 27A11.5 4.8 0 0 0 43.5 27", HOLE, 2.2) +
             stroke("M20.5 35A11.5 4.8 0 0 0 43.5 35", HOLE, 2.2))
    return body + seams

@reg("openoffice4-calc", DEEP_PURPLE_SOFT)
def oo_calc():
    cells = "".join(rrect(19.5 + c * 8.8, 18.5 + r * 6.4, 6.6, 4.2, .8, HOLE)
                    for r in range(4) for c in range(3))
    return rrect(16.5, 15.5, 31, 31, 3.5, INK) + cells

@reg("openoffice4-draw", AMBER)
def oo_draw():
    return stroke("M15 40C19 40 22 37 24 33C26 29 24.5 25 22 26C19.5 27 21 33 26 35"
                  "C31 37 33 31 32 27C31 23 34 20 37 22C40 24 36 30 39.5 32"
                  "C43 34 46 29 49 27", INK, 3.6)

@reg("openoffice4-impress", DEEP_ORANGE)
def oo_impress():
    pie = path("M24 18.5A8.5 8.5 0 1 0 32.5 27H24Z", INK)
    slice_ = path("M26 16.5A8.5 8.5 0 0 1 34.5 25H26Z", INK)
    lines = (rrect(37, 19, 11, 3.6, 1.8, INK) + rrect(37, 26, 11, 3.6, 1.8, INK) +
             rrect(16, 39, 32, 3.6, 1.8, INK))
    return g(pie + slice_, "translate(-1 0)") + lines

@reg("openoffice4-math", GREY_DEEP)
def oo_math():
    root = stroke("M16 31L19.5 29L24.5 41L29.5 18H35", INK, 3.6)
    x = line(35, 27, 46, 40, INK, 3.6) + line(46, 27, 35, 40, INK, 3.6)
    return root + x

@reg("openoffice4-writer", INDIGO)
def oo_writer():
    return "".join(rrect(17, y, w, 3.8, 1.9, INK) for y, w in
                   [(16, 30), (22.5, 30), (29, 30), (35.5, 30), (42, 19)])

@reg("openbazaar2", BLUE_DEEP)
def openbazaar2():
    roof = poly([(32, 12), (47, 25), (17, 25)], INK, 3)
    shop = rrect(19, 28.5, 26, 19, 2.5, INK)
    door = poly([(32, 31.5), (39.5, 47.5), (24.5, 47.5)], HOLE, 1.5)
    return roof + shop + door

@reg("openblok", CYAN)
def openblok():
    return rrect(15, 13, 34, 34, 6, INK) + rrect(21, 19, 22, 22, 3, CYAN_DEEP)

@reg("openboard", DEEP_ORANGE)
def openboard():
    bubble = rrect(14.5, 16, 33, 22, 4, INK) + poly([(19.5, 35), (28.5, 35), (19.5, 45)], INK, 2)
    pen = line(31, 31, 47, 12.5, DEEP_ORANGE_DARK, 3.4)
    return bubble + pen

@reg("openboardview", INDIGO_DEEP)
def openboardview():
    top = (circle(20.5, 17, 2.4, INK) + circle(27, 17, 2.4, INK) + circle(33.5, 17, 2.4, INK) +
           ring_b(43, 17, 3.3, INK, 2.4))
    mid = circle(20, 30, 4.2, INK) + stroke("M24 30H30L34 34H40", INK, 2.6) + circle(44, 34, 4.2, INK)
    low = ring_b(21.5, 43, 3.3, INK, 2.4) + line(25, 43, 47, 43, INK, 2.6)
    return top + mid + low

@reg("openbox", BLUE_DEEP)
def openbox():
    win = rrect(14, 14, 36, 32, 4, INK)
    bar = path("M14 22V18A4 4 0 0 1 18 14H46A4 4 0 0 1 50 18V22Z", BLUE_SOFT)
    foot = path("M14 40V42A4 4 0 0 0 18 46H46A4 4 0 0 0 50 42V40Z", BLUE_SOFT)
    return win + bar + foot

@reg("openbve", GREY_DARK)
def openbve():
    b = line(22, 13, 22, 33, INK, 5) + ring_b(31.5, 34, 9.5, INK, 5)
    return b + circle(34.5, 35, 2.8, ORANGE)

@reg("opencomic", RED)
def opencomic():
    panels = (rrect(17, 15, 5, 17, 1.5, INK) + rrect(24, 15, 5, 17, 1.5, INK) +
              rrect(31, 15, 16, 11, 2, INK) + rrect(31, 28, 16, 4, 1.5, INK) +
              rrect(17, 34, 30, 4, 1.5, INK) + rrect(17, 40, 22, 4, 1.5, INK))
    return g(panels, "rotate(-10 32 30)")

@reg("opengl", LIGHT_BLUE_DEEP)
def opengl():
    outer = '<ellipse cx="32" cy="30" rx="17" ry="11" fill="INK"/>'
    inner = '<ellipse cx="35.8" cy="30" rx="12.8" ry="6.2" fill="HOLE"/>'
    return outer + inner

@reg("openhardwaremonitor", BLUE_GREY_DEEP)
def openhardwaremonitor():
    chip = rrect(15, 16, 26, 26, 4, INK)
    dots = circle(46.5, 15, 2, INK) + circle(46.5, 20.5, 2, INK) + circle(46.5, 26, 2, INK)
    lines = rrect(31, 45.5, 17, 2.6, 1.3, AMBER)
    corner = poly([(15.5, 38.5), (15.5, 47), (24, 47)], AMBER, 1.5)
    return chip + dots + lines + corner

@reg("openlp", BLUE_DARK)
def openlp():
    disc_ = circle(CX, CY, 16.5, INK)
    ax, ay = 46, 33
    rays = ""
    for a0, a1 in [(191, 204), (177, 186), (164.5, 171)]:
        pts = [(ax, ay)]
        for a in (a0, a1):
            dx, dy = math.cos(math.radians(a)), math.sin(math.radians(a))

            bx, by = ax - CX, ay - CY
            b = bx * dx + by * dy
            t = -b + math.sqrt(b * b - (bx * bx + by * by - 16.5 ** 2)) - 3
            pts.append((ax + t * dx, ay + t * dy))
        rays += poly(pts, HOLE)
    return disc_ + rays

@reg("openrgb", BLUE_GREY_DARK)
def openrgb():
    cols = [RED, ORANGE, YELLOW, DEEP_PURPLE_SOFT, LIGHT_BLUE, PURPLE]
    out = ""
    for k, c in enumerate(cols):
        a0 = -90 + 60 * k + 3
        out += arc_b(32, 27, 12.5, a0, a0 + 54, c, 6)
    mouse = rrect(27.5, 33, 9, 14, 4, INK)
    return out + circle(32, 27, 4.5, INK) + mouse

@reg("openscad", AMBER_DEEP)
def openscad():
    stub1 = g(rrect(11, 26, 12, 10, 3, INK), "rotate(25 20 31)")
    stub2 = g(rrect(40, 13, 10, 12, 3, INK), "rotate(35 45 19)")
    sphere = circle(32, 31, 13.5, HOLE) + circle(32, 31, 12, INK)
    holes = ('<ellipse cx="29" cy="25" rx="4.5" ry="3" fill="HOLE"/>'
             '<ellipse cx="37" cy="36" rx="3.6" ry="4.4" fill="HOLE"/>')
    return stub1 + stub2 + sphere + holes

@reg("openshot", BLUE_DARK)
def openshot():
    disc_ = circle(CX, CY, 16.5, INK)
    band = rrect(15.3, 24.5, 33.4, 11, 0, HOLE)
    holes = "".join(rrect(19 + 5.5 * k, 26.3, 3, 2.4, .5, INK) + rrect(19 + 5.5 * k, 31.3, 3, 2.4, .5, INK)
                    for k in range(5))
    return disc_ + band + holes

@reg("opensnitch-ui", RED)
def opensnitch():
    cloud = stroke("M22 42H42.5A7 7 0 0 0 43.5 28A10.5 10.5 0 0 0 23.5 25A8.5 8.5 0 0 0 22 42Z", INK, 3.4)
    arrows = (line(26, 31, 37, 31, INK, 2.6) + arrowhead_b(37.5, 31, 0, 3.6, INK) +
              line(38, 37, 27, 37, INK, 2.6) + arrowhead_b(26.5, 37, 180, 3.6, INK))
    return cloud + arrows

@reg("openvpn", ORANGE_DEEP)
def openvpn():
    rim = stroke("M25.5 40.3A13 13 0 1 1 38.5 40.3", INK, 6)
    key = circle(32, 27, 5, INK) + poly([(29.5, 29), (34.5, 29), (36, 45), (28, 45)], INK, 2)
    return rim + key

@reg("ophcrack", ORANGE_DARK)
def ophcrack():
    o = rrect(15.5, 21.5, 13, 17, 6.5, "none", f' stroke="{INK}" stroke-width="4.4"')
    s = stroke("M47 23.5C45.6 22 43.8 21.5 41.5 21.5C38.4 21.5 36.3 23 36.3 25.5"
               "C36.3 30.5 47.5 29 47.5 34.4C47.5 37 45.2 38.5 41.8 38.5C39.2 38.5 37.2 37.6 35.8 36.2", INK, 4.4)
    return o + s

def _bank(note_colour):
    chip = rrect(13.5, 11.5, 37, 37, 6, "none",
                 f' stroke="{INK}" stroke-width="2.4" stroke-dasharray="2.4 2.4"')
    disc_ = circle(32, 30, 12.5, INK)
    note = (circle(27.5, 35.5, 2.9, note_colour) + circle(37, 33.5, 2.9, note_colour) +
            rrect(28.3, 23, 2.2, 13, .6, note_colour) + rrect(37.8, 21, 2.2, 13, .6, note_colour) +
            poly([(28.3, 23), (40, 20.6), (40, 24), (28.3, 26.4)], note_colour))
    return chip + disc_ + note

@reg("opl3_bank_editor", RED_DEEP)
def opl3():
    return _bank(HOLE)

@reg("opn2_bank_editor", BLUE_DEEP)
def opn2():
    return _bank(HOLE)

@reg("org.codeberg.som.Tracks", LIGHT_BLUE_DARK)
def tracks():
    out = ""
    for c in range(7):
        for r in range(7):
            d = abs(r - 3)
            if c == 0 and d == 3:
                continue
            arrow = (1 <= c <= 2 and d <= 1) or (3 <= c <= 5 and d <= 5 - c)
            out += circle(17 + 5 * c, 15 + 5 * r, 2.1, INK if arrow else LIGHT_BLUE)
    return out

@reg("org.coolercontrol.CoolerControl", DEEP_PURPLE_DEEP)
def coolercontrol():
    fork = lambda x: stroke(f"M{x - 3.8} 14V18.5A3.8 3.8 0 0 0 {x + 3.8} 18.5V14", INK, 3) + line(x, 22.5, x, 45, INK, 3.4)
    mid = line(32, 14, 32, 33, INK, 3.4) + ring_b(32, 39.5, 4.2, INK, 3)
    return fork(21) + mid + fork(43)

@reg("org.coolero.Coolero", BLUE)
def coolero():
    top = arc_b(32, 30, 15, 200, 320, INK, 2.8) + arrowhead_b(*pt(32, 30, 15, 322), 50, 4, INK)
    bot = arc_b(32, 30, 15, 20, 140, INK, 2.8) + arrowhead_b(*pt(32, 30, 15, 142), 230, 4, INK)
    side = ring_b(17, 30, 2.8, INK, 2.4) + ring_b(47, 30, 2.8, INK, 2.4)
    core = ring_b(32, 30, 6, INK, 2.8) + circle(32, 30, 2.4, INK)
    return top + bot + side + core

@reg("org.cubocore.CoreRenamer", CYAN_DEEP)
def corerenamer():
    out = ""
    v = [pt(32, 32, 17, -90 + 120 * k) for k in range(3)]
    for k in range(3):
        (x0, y0), (x1, y1) = v[k], v[(k + 1) % 3]
        sx, sy = x0 + .18 * (x1 - x0), y0 + .18 * (y1 - y0)
        ex, ey = x0 + .6 * (x1 - x0), y0 + .6 * (y1 - y0)
        deg = math.degrees(math.atan2(y1 - y0, x1 - x0))
        out += line(sx, sy, ex, ey, INK, 5.5) + arrowhead_b(ex, ey, deg, 7, INK)
    return out

@reg("org.cvfosammmm.Setzer", BLUE_GREY_LIGHT)
def setzer():
    page = rrect(21, 12, 26, 36, 3, INK)
    text = rrect(25, 16.5, 18, 2.6, 1.3, HOLE) + rrect(31, 41, 12, 2.6, 1.3, HOLE)
    bird = path("M14 13C20 17 24 22 26 27C30 26 35 26 39 27L43.5 25L48.5 27.5L43 29.5"
                "C41.5 33.5 37.5 36.5 32 37.5L26 43L25.5 37.5C20.5 34 16 25 14 13Z", BLUE_GREY_DARK,
                f' stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"')
    return page + text + bird

@reg("org.emilien.Password", GREY_DARK)
def password():
    head = ring_b(21.5, 30, 6, INK, 4.4)
    shaft = line(27.5, 30, 47, 30, INK, 4.4)
    teeth = line(41, 30, 41, 36.5, INK, 3.6) + line(46, 30, 46, 35, INK, 3.6)
    return head + shaft + teeth

@reg("org.emilien.SpaceLaunch", BLUE_DEEP)
def spacelaunch():
    body = path("M32 11C38 15.5 40 23 38.5 36H25.5C24 23 26 15.5 32 11Z", INK)
    fins = poly([(25.5, 29), (20, 38), (26, 37)], INK, 2) + poly([(38.5, 29), (44, 38), (38, 37)], INK, 2)
    window = circle(32, 23, 3.2, HOLE)
    flame = poly([(28.5, 39), (35.5, 39), (32, 47)], INK, 1.5)
    return g(body + fins + window + flame, "rotate(40 32 30)")

@reg("org.eu.encom.spectral", TEAL_LIGHT)
def spectral():
    s = stroke("M39.5 21.5C36.5 18.5 29.5 18.3 26.5 22.3C24 25.8 27 29.3 32 30.3"
               "C37 31.3 40.5 34.5 37.8 38.3C35 42.3 28 42 24.8 39", HOLE, 4.6)
    return circle(CX, CY, 16.5, INK) + s

def _bank_s():
    disc_ = circle(32, 30, 16, INK)
    note = (circle(26.5, 37, 3.8, HOLE) + circle(38, 34.5, 3.8, HOLE) +
            rrect(27.3, 21, 3.2, 16, .8, HOLE) + rrect(38.8, 18.5, 3.2, 16, .8, HOLE) +
            poly([(27.3, 21), (42, 18), (42, 22.5), (27.3, 25.5)], HOLE))
    return disc_ + note

@small("opl3_bank_editor")
def opl3_s():
    return _bank_s()

@small("opn2_bank_editor")
def opn2_s():
    return _bank_s()

@small("openboardview")
def openboardview_s():
    return (circle(21, 18, 3.5, INK) + circle(30, 18, 3.5, INK) + ring_b(42, 18, 4, INK, 3) +
            circle(20, 31, 5, INK) + stroke("M24 31H43", INK, 3.4) +
            ring_b(21.5, 43, 4, INK, 3) + line(26, 43, 46, 43, INK, 3.4))

@small("openoffice4-calc")
def oo_calc_s():
    cells = "".join(rrect(20 + c * 12.5, 19.5 + r * 11.5, 9.5, 8.5, 1.5, HOLE)
                    for r in range(2) for c in range(2))
    return rrect(16.5, 15.5, 31, 31, 3.5, INK) + cells

@small("openoffice4-base")
def oo_base_s():
    body = path("M19.5 19A12.5 5 0 0 1 44.5 19V41A12.5 5 0 0 1 19.5 41Z", INK)
    return body + stroke("M19.5 19A12.5 5 0 0 0 44.5 19", HOLE, 2.6) + stroke("M19.5 30A12.5 5 0 0 0 44.5 30", HOLE, 2.6)

@small("openoffice4-writer")
def oo_writer_s():
    return "".join(rrect(17, y, w, 5, 2.5, INK) for y, w in [(17, 30), (26, 30), (35, 30), (44, 18)])

@small("opencomic")
def opencomic_s():
    panels = (rrect(16, 14, 7, 18, 2, INK) + rrect(26, 14, 21, 18, 2, INK) + rrect(16, 36, 31, 8, 2, INK))
    return g(panels, "rotate(-10 32 30)")

@small("openshot")
def openshot_s():
    disc_ = circle(CX, CY, 16.5, INK)
    band = rrect(15.3, 23.5, 33.4, 13, 0, HOLE)
    holes = "".join(rrect(19 + 9 * k, 27.5, 5, 5, 1, INK) for k in range(3))
    return disc_ + band + holes

@small("oolite")
def oolite_s():
    wings = (poly([(14, 13), (30, 26), (30, 33), (14, 21)], INK, 2) +
             poly([(50, 13), (34, 26), (34, 33), (50, 21)], INK, 2))
    tail = poly([(27, 32), (37, 32), (32, 48)], INK, 2.5)
    return wings + tail + circle(32, 25, 6.5, HOLE) + circle(32, 25, 5, INK)

@small("org.codeberg.som.Tracks")
def tracks_s():
    out = ""
    for c in range(5):
        for r in range(5):
            d = abs(r - 2)
            arrow = (c <= 1 and d == 0) or (2 <= c <= 4 and d <= 4 - c)
            out += circle(18 + 7 * c, 16 + 7 * r, 2.8, INK if arrow else ORANGE_DEEP)
    return out

@small("openarena")
def openarena_s():
    halo = f'<ellipse cx="32" cy="29" rx="16" ry="10.5" fill="none" stroke="{INK}" stroke-width="3.4"/>'
    return halo + stroke("M22 45L32 17L42 45", HOLE, 9) + stroke("M22 45L32 17L42 45", INK, 4.4)

@small("openlp")
def openlp_s():
    return (circle(CX, CY, 16.5, INK) + poly([(47, 33), (17, 20), (15.5, 29)], HOLE) +
            poly([(47, 33), (16.5, 35), (20, 42)], HOLE))

@small("openoffice4-draw")
def oo_draw_s():
    return stroke("M15 38C21 38 22 24 28 24C34 24 30 37 36 37C42 37 42 25 49 23", INK, 4)

@small("openoffice4-main")
def oo_main_s():
    return g(path("M13 40C20 33 28 33 33 38.5C38 31.5 46 29 51 31C44 33 38.5 37 34.5 43.5"
                  "C29.5 38.5 21 37.5 13 40Z", INK), "translate(32 31) scale(1.1 1.7) translate(-32 -37)")

@small("openra-cnc")
def openra_cnc_s():
    return ring_b(32, 30, 15, INK, 3.6) + arc_b(32, 30, 7.5, 45, 315, RED_LIGHT, 4.4)

@small("openra-d2k")
def openra_d2k_s():
    planet = circle(30, 29, 15, INK) + circle(24.5, 25, 3.5, HOLE)
    return planet + circle(42, 40, 8.5, HOLE) + circle(42, 40, 6.5, INK)

@small("openra-ra")
def openra_ra_s():
    pts = [pt(32, 31, 18.5 if k % 2 == 0 else 8.5, -90 + 36 * k) for k in range(10)]
    return poly(pts, INK, 3)

@small("openrgb")
def openrgb_s():
    cols = [RED, ORANGE, YELLOW, ORANGE_DEEP, LIGHT_BLUE, PURPLE]
    out = "".join(arc_b(32, 30, 12.5, -90 + 60 * k, -30 + 60 * k, c, 7) for k, c in enumerate(cols))
    return out + circle(32, 30, 5, INK)

@small("openscad")
def openscad_s():
    stub = g(rrect(10, 25, 14, 12, 3.5, INK), "rotate(25 20 31)")
    sphere = circle(33, 30, 15, HOLE) + circle(33, 30, 13.5, INK)
    return stub + sphere + '<ellipse cx="31" cy="24" rx="5.5" ry="3.8" fill="HOLE"/>'

@small("openttd")
def openttd_s():
    diamond = g(rrect(18, 16, 28, 28, 5, INK), "rotate(45 32 30)")
    return diamond + stroke("M37 23.5C35.5 21.5 29 20.8 27.8 24.6C26.3 30 37.5 29 36.6 35"
                            "C36 39.2 29.5 39 27 36.5", HOLE, 3.4)

@small("opentyrian")
def opentyrian_s():
    hull = path("M28 14H36L39 25L36 40L32 47L28 40L25 25Z", INK)
    wings = (poly([(26, 21), (16, 13), (14.5, 21), (25, 30)], INK, 2) +
             poly([(38, 21), (48, 13), (49.5, 21), (39, 30)], INK, 2))
    return wings + hull + circle(32, 26, 3.4, ORANGE)

@small("openxcom")
def openxcom_s():
    x = line(16, 14, 48, 46, TEAL_SOFT, 6.5) + line(48, 14, 16, 46, TEAL_SOFT, 6.5)
    head = path("M32 16C41 16 45 21.5 45 28C45 35.5 37.5 41.5 32 44C26.5 41.5 19 35.5 19 28"
                "C19 21.5 23 16 32 16Z", INK)
    eyes = (poly([(22.5, 26.5), (30, 29.5), (28.5, 34), (23.5, 31)], HOLE, 1.5) +
            poly([(41.5, 26.5), (34, 29.5), (35.5, 34), (40.5, 31)], HOLE, 1.5))
    return x + head + eyes

@small("org.coolercontrol.CoolerControl")
def coolercontrol_s():
    fork = lambda x: stroke(f"M{x - 4.5} 13V18A4.5 4.5 0 0 0 {x + 4.5} 18V13", INK, 3.2) + line(x, 23, x, 46, INK, 3.6)
    return fork(19) + line(32, 13, 32, 46, INK, 3.6) + fork(45)

@small("org.coolero.Coolero")
def coolero_s():
    top = arc_b(32, 30, 15, 205, 315, INK, 3) + arrowhead_b(*pt(32, 30, 15, 320), 50, 5, INK)
    bot = arc_b(32, 30, 15, 25, 135, INK, 3) + arrowhead_b(*pt(32, 30, 15, 140), 230, 5, INK)
    return top + bot + circle(32, 30, 6, INK)

@small("org.cubocore.CoreRenamer")
def corerenamer_s():
    out = ""
    v = [pt(32, 32, 17.5, -90 + 120 * k) for k in range(3)]
    for k in range(3):
        (x0, y0), (x1, y1) = v[k], v[(k + 1) % 3]
        sx, sy = x0 + .2 * (x1 - x0), y0 + .2 * (y1 - y0)
        ex, ey = x0 + .55 * (x1 - x0), y0 + .55 * (y1 - y0)
        deg = math.degrees(math.atan2(y1 - y0, x1 - x0))
        out += line(sx, sy, ex, ey, INK, 5.5) + arrowhead_b(ex, ey, deg, 8, INK)
    return out

@small("org.cvfosammmm.Setzer")
def setzer_s():
    page = rrect(21, 12, 26, 36, 3, INK)
    bird = path("M13 12C19 17 23 22 25 27C30 26 35 26 39 27L44 25L49.5 28L43.5 30"
                "C42 34.5 38 37.5 32 38.5L25.5 44L25 38.5C20 35 15 25 13 12Z", BLUE_GREY_DARK)
    return page + bird

@small("org.eu.encom.spectral")
def spectral_s():
    return circle(CX, CY, 17, INK) + stroke("M39.5 21C35 17.5 26 18.5 26 24C26 30 38 28.5 38 35.5"
                                           "C38 41.5 29 42 24.5 38.5", HOLE, 4.4)

@small("org.es_de.emulationstation-de")
def es_de_s():
    e = stroke("M29 18H18.5V42H29M18.5 30H27", INK, 4)
    s_ = stroke("M46 21C44.5 19 42.5 18 40 18C36.6 18 34.3 20 34.3 23.4"
                "C34.3 29.6 46.5 28 46.5 35C46.5 39.3 43.6 42 39.6 42C37 42 34.8 41 33.3 39", INK, 4)
    return e + s_

@small("openvpn")
def openvpn_s():
    rim = stroke("M24.5 41A14 14 0 1 1 39.5 41", INK, 4.6)
    return rim + circle(32, 27, 5.5, INK) + poly([(29, 29), (35, 29), (36.5, 46), (27.5, 46)], INK, 2)

@small("openclonk")
def openclonk_s():
    shield = path("M17 15H47V28C47 37.5 40.5 43.5 32 47.5C23.5 43.5 17 37.5 17 28Z", INK,
                  f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return shield + line(22, 20, 42, 40, RED_DARK, 4) + line(42, 20, 22, 40, RED_DARK, 4)
