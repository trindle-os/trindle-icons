# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 48: net.kirgroup.confy to nos-tv.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER_DARK, AMBER_DEEP, AMBER_SOFT, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_SOFT, BLUE_SOFT, BROWN, BROWN_DEEP, BROWN_LIGHT, BROWN_SOFT,
    circle, CYAN_DEEP, DEEP_PURPLE_DARK, DEEP_PURPLE_DEEP, DEEP_PURPLE_SOFT, f, g, GREY,
    GREY_DARK, GREY_DEEP, GREY_SOFT, HOLE, INDIGO, INDIGO_DARK, INDIGO_DEEP, INDIGO_SOFT, INK,
    LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP, LIGHT_BLUE_SOFT, line, ORANGE_DEEP, path, PINK_DEEP,
    PINK_SOFT, poly, pt, PURPLE, PURPLE_DEEP, RED_DARK, RED_DEEP, RED_LIGHT, RED_SOFT, rrect,
    stroke, TEAL_DEEP, TEAL_SOFT,
)
from glyphs.kit import registry, ring_b

ICONS, SMALL, reg, small = registry()


def _star4(cx, cy, r, fill):
    pts = [pt(cx, cy, r if k % 2 == 0 else r * .35, -90 + 45 * k) for k in range(8)]
    return poly(pts, fill, 1)


@reg("net.kirgroup.confy", LIGHT_BLUE_DEEP)
def confy():
    sheet = path("M22 13H44A3 3 0 0 1 47 16V38L39 47H22A3 3 0 0 1 19 44V16A3 3 0 0 1 22 13Z", INK)
    fold = path("M47 38H42A3 3 0 0 0 39 41V47Z", LIGHT_BLUE_SOFT)
    cells = "".join(rrect(24 + c * 7.5, 18 + r * 7, 5, 4.5, 1, HOLE)
                    for r in range(4) for c in range(3) if not (r == 3 and c == 2))
    bubble = (rrect(13, 21, 18, 12, 3.5, LIGHT_BLUE_DARK)
              + poly([(22, 32), (28, 32), (27, 37)], LIGHT_BLUE_DARK, 1.5))
    return sheet + fold + cells + bubble


@reg("net.kuribo64.melonDS", LIGHT_BLUE_DEEP)
def melonds():
    body = rrect(15.5, 13.5, 33, 33, 8, INK)
    split = line(32, 17, 32, 43, HOLE, 2.4)
    screen = rrect(20.5, 23, 8, 14, 2, HOLE)
    btns = rrect(36, 20, 8, 5, 1.5, HOLE) + rrect(36, 35, 8, 5, 1.5, HOLE)
    return g(body + split + screen + btns, "rotate(-45 32 30)")


@reg("net.meijn.onvifviewer", BLUE_GREY)
def onvifviewer():
    cam = g(rrect(17, 18, 24, 11, 3, INK) + rrect(13.5, 20.5, 5, 6, 1.5, INK),
            "rotate(14 29 23.5)")
    arm = stroke("M37 29L40 36H45", INK, 3.4)
    plate = rrect(44, 29, 6, 15, 2, INK)
    return cam + arm + plate


@reg("net.natesales.Aviator", PINK_DEEP)
def aviator():
    face = rrect(14, 15, 36, 30, 7, INK)
    eyes = circle(24.5, 27.5, 6, HOLE) + circle(39.5, 27.5, 6, HOLE)
    pupils = circle(24.5, 27.5, 3.2, PINK_SOFT) + circle(39.5, 27.5, 3.2, PINK_SOFT)
    mouth = rrect(26.5, 37, 11, 3.5, 1.75, HOLE)
    return face + eyes + pupils + mouth + circle(20, 20, 1.8, HOLE)


@reg("net.pioneerspacesim.Pioneer", INDIGO_DARK)
def pioneer():
    ring = ring_b(32, 30, 16, INK, 2.6)
    ship = path("M32 16C37 22 38.5 31 36.5 42H27.5C25.5 31 27 22 32 16Z", INK)
    fins = (poly([(27.5, 33), (22.5, 43), (28, 42)], INK, 1.5) +
            poly([(36.5, 33), (41.5, 43), (36, 42)], INK, 1.5))
    window = circle(32, 27, 2.6, HOLE)
    return ring + ship + fins + window + _star4(41.5, 20, 4.2, INK)


@reg("net.retrodeck.retrodeck", DEEP_PURPLE_DEEP)
def retrodeck():
    r = stroke("M18 42V19H25.5A6.2 6.2 0 0 1 25.5 31.4H18M25 31.4L31 42", INK, 4.6)
    arc = stroke("M33 15.5A14.5 14.5 0 0 1 33 44.5", DEEP_PURPLE_SOFT, 5)
    return r + arc


@reg("net.runelite.RuneLite", GREY_DEEP)
def runelite():
    blade = poly([(22, 20), (26, 20), (26, 42), (24, 46.5), (22, 42)], INK, 1.5)
    guard = rrect(17, 18, 14, 3.6, 1.8, INK) + circle(24, 14.5, 2.6, INK)
    bowl = stroke("M27.5 19.5H34A6.5 6.5 0 0 1 34 32.5H27.5M33 32.5L45 46", INK, 4.2)
    return blade + guard + bowl


@reg("net.sapples.LiveCaptions", BLUE_GREY_DEEP)
def livecaptions():
    screen = rrect(13.5, 16, 37, 28, 5, INK)
    bars = (rrect(19, 25, 15, 4, 2, HOLE) + rrect(36.5, 25, 8.5, 4, 2, HOLE) +
            rrect(19, 32, 8, 4, 2, HOLE) + rrect(29.5, 32, 15.5, 4, 2, HOLE))
    return screen + bars


@reg("net.sf.VICE", INDIGO_DEEP)
def vice():
    c = ('<path d="M36 19A12 12 0 1 0 36 41" fill="none" stroke="INK" '
         'stroke-width="7.5" stroke-linecap="butt"/>')
    top = poly([(37.5, 22.5), (49.5, 22.5), (45.5, 29), (37.5, 29)], INK, 1)
    bot = poly([(37.5, 31), (45.5, 31), (49.5, 37.5), (37.5, 37.5)], RED_LIGHT, 1)
    return g(c + top + bot, "translate(-1.5 0)")


@reg("net.sourceforge.Fillets", BLUE_GREY_DARK)
def fillets():
    ring = ring_b(32, 30, 16, INK, 3.4)
    fish = path("M23.5 30C27 24 37 23.5 43 30C37 36.5 27 36 23.5 30Z", INK)
    tail = poly([(25.5, 30), (19, 24.5), (19, 35.5)], INK, 2)
    return ring + fish + tail + circle(37.5, 29, 1.8, HOLE)


@reg("net.sourceforge.Teo", INDIGO)
def teo():
    top = stroke("M17 25V19.5L32 12.5L47 19.5V25", INK, 4.4)
    bot = stroke("M17 35V40.5L32 47.5L47 40.5V35", INDIGO_SOFT, 4.4)
    hexa = poly([pt(32, 30, 8.5, -90 + 60 * k) for k in range(6)], INK, 2)
    return top + bot + hexa


@reg("netbeans", BLUE_DARK)
def netbeans():
    outer = poly([pt(32, 30, 17, -90 + 60 * k) for k in range(6)], INK, 3)
    inner = poly([pt(32, 30.5, 9.5, -90 + 60 * k) for k in range(6)], BLUE_SOFT, 2)
    y = (line(32, 30.5, 32, 40, HOLE, 2.2) + line(32, 30.5, 23.8, 25.8, HOLE, 2.2) +
         line(32, 30.5, 40.2, 25.8, HOLE, 2.2))
    return outer + inner + y


def _netease():
    return stroke("M37.5 14.5C27 14 18 21 18 31C18 39.5 24.5 45.5 32 45.5"
                  "C39.5 45.5 46 40 46 32.5C46 26.5 41.5 22.5 36 22.5"
                  "C30.5 22.5 26.5 26.5 26.5 31.5C26.5 35 29 37.5 32.5 37.5"
                  "C36 37.5 38.5 34.5 37.5 30.5L35.5 21.5C35 18.5 37 16.5 40.5 17", INK, 4.4)


@reg("netease-cloud-music-gtk", AMBER_DEEP)
@reg("netease-cloud-music", RED_DEEP)
def netease():
    return _netease()


@reg("netflix", RED_DEEP)
def netflix():
    stems = (path("M21 13H28V46.5L21 47.5Z", RED_SOFT) +
             path("M36 13H43V47.5L36 46.5Z", RED_SOFT))
    diag = path("M21 13H28L43 47.5H36Z", INK)
    return stems + diag


@reg("nethack", TEAL_DEEP)
def nethack():
    shield = path("M17.5 16L32 12.5L46.5 16V29C46.5 38 40 44.5 32 48C24 44.5 17.5 38 17.5 29Z", INK,
                  f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    half = path("M32 16.5L42.5 19V29C42.5 35.5 38 40.5 32 43.5Z", TEAL_SOFT)
    return shield + half


@reg("netsniff-ng", RED_DEEP)
def netsniff():
    horns = (path("M20 25C15 22 14 16 16.5 11.5C17.5 16 20 18.5 24.5 19.5Z", INK) +
             path("M44 25C49 22 50 16 47.5 11.5C46.5 16 44 18.5 39.5 19.5Z", INK))
    head = path("M19 22C19 19 21 18 24 18H40C43 18 45 19 45 22V44C45 46 44 47 42 47H22"
                "C20 47 19 46 19 44Z", INK)
    eyes = (poly([(22.5, 28), (29.5, 31), (28, 35), (23, 34)], HOLE, 1.5) +
            poly([(41.5, 28), (34.5, 31), (36, 35), (41, 34)], HOLE, 1.5))
    return horns + head + eyes


@reg("netsurf", LIGHT_BLUE_DEEP)
def netsurf():
    globe = circle(32, 30, 16.5, INK)
    pts = [pt(37.5, 23, 7 if k % 2 == 0 else 3, -90 + 22.5 * k) for k in range(16)]
    star = poly(pts, HOLE, 1)
    swoosh = stroke("M16 23C24 27 32 34 38.5 47", HOLE, 2.6)
    return globe + star + swoosh


@reg("network_local", CYAN_DEEP)
def network_local():
    box = rrect(22, 12, 20, 18, 4, INK) + rrect(27, 17, 10, 8, 1.5, HOLE)
    tree = line(32, 30, 32, 39, INK, 3.2) + line(19, 39, 45, 39, INK, 3.2)
    nodes = "".join(circle(x, 42, 4.5, INK) for x in (19, 32, 45))
    return box + tree + nodes


def _quarters(r, light, dark):
    return (circle(32, 30, r, light) +
            path(f"M32 30V{f(30 - r)}A{f(r)} {f(r)} 0 0 1 {f(32 + r)} 30Z", dark) +
            path(f"M32 30V{f(30 + r)}A{f(r)} {f(r)} 0 0 1 {f(32 - r)} 30Z", dark))


@reg("neverball", GREY)
def neverball():
    return _quarters(16.5, INK, GREY_DARK)


@reg("neverputt", RED_DEEP)
def neverputt():
    ball = _quarters(15.5, INK, RED_SOFT)
    shaft = line(23, 13, 29, 38, RED_DARK, 3.6)
    head = rrect(22, 37, 20, 6.5, 3.25, RED_DARK)
    return ball + shaft + head


@reg("newbreeze", CYAN_DEEP)
def newbreeze():
    folder = path("M15 18A3 3 0 0 1 18 15H26L30 19H46A3 3 0 0 1 49 22V43A3 3 0 0 1 46 46H18"
                  "A3 3 0 0 1 15 43Z", INK)
    return folder + rrect(20, 31, 24, 11, 2, HOLE) + rrect(24.5, 35, 15, 3.5, 1.5, INK)


@reg("nexuiz", GREY_DARK)
def nexuiz():
    return (stroke("M18 24H42.5C42.5 35 40.5 42 33.5 46", INK, 5) +
            stroke("M30.5 14C30.5 30 27 40 18.5 46.5", INK, 5))


@reg("nfoview", BLUE_DEEP)
def nfoview():
    return (rrect(28.5, 12, 7, 7, 2.5, INK) + stroke("M25 25H33V43", INK, 6) +
            rrect(23, 40, 18, 5.5, 2.5, INK))


@reg("nheko", BLUE_DARK)
def nheko():
    blue = poly([(22.5, 20), (27.5, 20), (19.5, 40), (14.5, 40)], BLUE_SOFT, 1)
    seven = poly([(30.5, 20), (35.5, 20), (27.5, 40), (22.5, 40)], INK, 1)
    n = path("M38.5 20H47C49.5 20 50.5 22 49.5 24.5L43.5 40H38.5L44 25H41.5L35.5 40H30.5Z", INK)
    return g(blue + seven + n, "translate(32 30) scale(1.3) translate(-32 -30)")


@reg("nicotine-plus", ORANGE_DEEP)
def nicotine():
    n = stroke("M18 45V17H25A6.5 6.5 0 0 1 31.5 23.5V45", INK, 6)
    plus = line(36, 36.5, 49, 36.5, INK, 5.5) + line(42.5, 30, 42.5, 43, INK, 5.5)
    return n + plus


@reg("night-in-the-woods", DEEP_PURPLE_DARK)
def nitw():
    head = path("M16 22L14 11L24 17C29 15.5 35 15.5 40 17L50 11L48 22C51 27 50 34 46 39"
                "C42 44 37 46 32 46C27 46 22 44 18 39C14 34 13 27 16 22Z", INK)
    eyes = (path("M19.5 29C22 25.5 27 25.5 29.5 29.5C27 33 22 33 19.5 29Z", AMBER_SOFT) +
            path("M44.5 29C42 25.5 37 25.5 34.5 29.5C37 33 42 33 44.5 29Z", AMBER_SOFT))
    pupils = circle(26, 29.5, 2.4, HOLE) + circle(38, 29.5, 2.4, HOLE)
    nose = poly([(30, 36), (34, 36), (32, 38.5)], HOLE, 1.5)
    return head + eyes + pupils + nose


@reg("nighthawk", BLUE_DEEP)
def nighthawk():
    orb = circle(32, 25, 13, INK) + ring_b(32, 25, 7.5, HOLE, 2.4)
    wings = path("M14 31L26 36.5L32 31L38 36.5L50 31L39 43L32 49L25 43Z", BLUE_DARK,
                 f' stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"')
    return orb + wings


@reg("nightsky", INDIGO_DARK)
def nightsky():
    return circle(32, 30, 16, INDIGO_DEEP) + ring_b(32, 30, 15, INK, 3.2) + circle(25, 22.5, 3.6, INK)


@reg("nihilumbra", PURPLE)
def nihilumbra():
    arms = ""
    for k in range(5):
        a = -60 + 72 * k
        x1, y1 = pt(32, 30, 9, a)
        x2, y2 = pt(32, 30, 18.5, a + 20)
        x3, y3 = pt(32, 30, 12.5, a + 58)
        arms += stroke(f"M{f(x1)} {f(y1)}Q{f(x2)} {f(y2)} {f(x3)} {f(y3)}", INK, 3.2)
    body = circle(32, 30, 9, INK)
    eyes = circle(28, 30, 3, HOLE) + circle(36, 30, 3, HOLE)
    return arms + body + eyes


@reg("nikto", BLUE_GREY)
def nikto():
    head = path("M32 12C42.5 12 48 19.5 47 28C46 36 39 44.5 32 48C25 44.5 18 36 17 28"
                "C16 19.5 21.5 12 32 12Z", INK)
    eyes = (path("M20 28C24 27 29.5 29 30 33C26 34.5 21.5 32.5 20 28Z", HOLE) +
            path("M44 28C40 27 34.5 29 34 33C38 34.5 42.5 32.5 44 28Z", HOLE))
    return head + eyes


@reg("nip2", BLUE_DEEP)
def nip2():
    frame = rrect(14.5, 14, 35, 32, 4, INK) + rrect(18.5, 18, 27, 24, 2, HOLE)
    back = path("M18.5 30C24 26 28 32 33 29.5C38 27 41 28.5 45.5 27.5V42H18.5Z", BLUE_SOFT)
    front = path("M18.5 36C24 33 29 37.5 34 35C38 33 41.5 34.5 45.5 33.5V42H18.5Z", INK)
    return frame + back + front


@reg("nishang", INDIGO_DARK)
def nishang():
    c = stroke("M24.5 23.5C23.5 22 22 21.5 20.5 21.5C17.5 21.5 15.5 24.5 15.5 29"
               "C15.5 33.5 17.5 36.5 20.5 36.5C22 36.5 23.5 36 24.5 34.5", INK, 3.6)
    colon = circle(29, 25, 2, INK) + circle(29, 34.5, 2, INK)
    return c + colon + line(34, 21.5, 40, 36.5, INK, 3.6) + line(43.5, 36.5, 49, 36.5, INK, 3.6)


@reg("nitrogen", BLUE_DEEP)
def nitrogen():
    rings = "".join(g(f'<ellipse cx="32" cy="30" rx="16.5" ry="8.5" fill="none" stroke="{INK}" '
                      'stroke-width="2.8"/>', f"rotate({a} 32 30)") for a in (45, -45))
    return rings + circle(32, 30, 8, INK) + circle(32, 30, 4, BLUE_SOFT)


@reg("nitroshare", GREY_DARK)
def nitroshare():
    shape = poly([(20, 21), (36, 11.5), (36, 18), (44, 18), (44, 39), (28, 48.5), (28, 42), (20, 42)], INK, 3)
    n = stroke("M26.5 36.5V23.5L37.5 36.5V23.5", HOLE, 3.6)
    return shape + n


@reg("nixnote2", ORANGE_DEEP)
def nixnote2():
    rhino = path("M15.5 44C14 35 16 25 22 19.5L23.5 13L27.5 17C31.5 15.5 35.5 16.5 38.5 19.5"
                 "C40.5 21.5 42 24 43 26.5L45.5 15.5C49 21 50 27.5 48.5 33L50.5 35.5"
                 "C49.5 40.5 45.5 43.5 40 44.5L36 46H17Z", INK)
    return rhino + circle(34.5, 26.5, 2, HOLE) + circle(45.5, 38, 1.4, HOLE)


@reg("nl.g4d.Girens", AMBER_DARK)
def girens():
    back = rrect(21, 13, 22, 24, 8, INK)
    arms = rrect(14.5, 25, 8, 17, 3.5, INK) + rrect(41.5, 25, 8, 17, 3.5, INK)
    seat = rrect(20, 33, 24, 11, 2.5, AMBER_SOFT)
    legs = rrect(21, 43, 4, 4, 1.5, INK) + rrect(39, 43, 4, 4, 1.5, INK)
    tufts = "".join(line(x - 1.4, y - 1.4, x + 1.4, y + 1.4, HOLE, 1.6) +
                    line(x + 1.4, y - 1.4, x - 1.4, y + 1.4, HOLE, 1.6)
                    for x, y in [(32, 19), (27, 25), (37, 25)])
    return back + arms + seat + legs + tufts


@reg("nmap", PURPLE_DEEP)
def nmap():
    globe = circle(32, 30, 16, INK)
    land = (path("M22 20C26 18 30 19 30 23C30 27 25 26 24 30C23 34 26 36 25 40"
                 "C20 37 17 31 18 26C18.5 23 20 21 22 20Z", HOLE) +
            path("M36 17C41 18 45 22 46 27C43 28 42 25 38 25C35 25 34 22 36 17Z", HOLE) +
            path("M35 32C39 31 42 33 41 37C40 40 37 42 34 43C33 39 32 35 35 32Z", HOLE))
    return globe + land


@reg("nnn", BLUE_GREY_DARK)
def nnn():
    knight = path("M18 47C18 39 22 34 26 30L20 32C16.5 33 14 30 15.5 27L25 17L25.5 11.5"
                  "L30 15C41 15.5 48 24 48 35V47Z", INK)
    eye = circle(26, 22, 1.8, HOLE)
    n = stroke("M33 47V38A4.5 4.5 0 0 1 42 38V47", HOLE, 3.6)
    return knight + eye + n


@reg("no-mans-sky", RED_DARK)
def no_mans_sky():
    gem = poly([(32, 11.5), (45, 29), (32, 48.5), (19, 29)], INK, 2)
    facet = poly([(32, 11.5), (45, 29), (32, 48.5)], RED_SOFT, 2)
    return gem + facet + circle(34, 28.5, 5.2, HOLE)


@reg("node-red-icon", RED_DARK)
def node_red():
    wires = (stroke("M22 30C32 30 30 20 41 20", INK, 3.2) +
             stroke("M22 30C32 30 30 40 41 40", INK, 3.2))
    nodes = (rrect(13, 24, 11, 12, 3, INK) + rrect(40, 14.5, 11, 11, 3, INK) +
             rrect(40, 34.5, 11, 11, 3, INK))
    return wires + nodes


@reg("noisetorch", LIGHT_BLUE_DARK)
def noisetorch():
    stand = line(26, 16, 26, 43, INK, 4) + rrect(19.5, 13, 13, 6, 2.5, INK) + line(19, 46, 33, 46, INK, 4)
    head = rrect(33, 12, 16, 17, 7, LIGHT_BLUE_SOFT)
    dots = "".join(circle(37.5 + c * 3.5, 16.5 + r * 4, 1.2, LIGHT_BLUE_DARK)
                   for r in range(3) for c in range(3))
    return stand + head + dots


@reg("noiz2sa", BLUE_GREY_DEEP)
def noiz2sa():
    diag = poly([(20.5, 14), (28, 14), (43.5, 46), (36, 46)], BLUE_GREY_SOFT, 2)
    stems = rrect(16, 13, 9, 34, 4.5, INK) + rrect(39, 13, 9, 34, 4.5, INK)
    return diag + stems


@reg("nomacs", BLUE_DEEP)
def nomacs():
    glass = poly([(18, 14), (46, 14), (32, 30)], INK, 3)
    stem = line(32, 29, 32, 43, INK, 3.4) + rrect(24, 42, 16, 4, 2, INK)
    corners = "".join(stroke(d, BLUE_SOFT, 2.6) for d in
                      ["M14 18V13H19", "M50 18V13H45", "M14 42V47H19", "M50 42V47H45"])
    return corners + glass + stem


@reg("nootka", BROWN_LIGHT)
def nootka():
    staff = "".join(line(14, y, 50, y, GREY_SOFT, 2) for y in (19, 25, 31, 37, 43))
    clef = stroke("M31 48C33.5 48 34.5 46 34 43.5L29.5 15C29 11.5 32 10.5 33 13"
                  "C35 17 32 22 28 26C23.5 30.5 22.5 34.5 25.5 37.5C28.5 40.5 35 39.5 36 35"
                  "C37 30.5 32.5 28.5 29.5 30.5C27.5 32 28 34.5 30 35.5", INK, 3.2)
    return staff + clef


@reg("normcap", PINK_DEEP)
def normcap():
    rect = rrect(15, 15, 28, 22, 2, "none",
                 f' stroke="{INK}" stroke-width="2.4" stroke-dasharray="4 3"')
    wand = line(29, 26, 47, 45, INK, 4.2)
    return rect + wand + _star4(22, 21, 5.5, INK) + _star4(37, 19, 4, INK)


@reg("northgard", BROWN)
def northgard():
    rim = ring_b(32, 30, 15.5, INK, 3.6)
    face = circle(32, 30, 13.7, BROWN_SOFT)
    planks = line(24, 18, 24, 42, BROWN, 2) + line(40, 18, 40, 42, BROWN, 2)
    boss = circle(32, 30, 8, INK) + stroke("M28.5 34V26L35.5 34V26", HOLE, 2.4)
    return face + planks + rim + boss


@reg("nos-tv", INDIGO)
def nos_tv():
    tv = rrect(14, 15, 29, 21, 3.5, INK) + rrect(17.5, 18.5, 22, 14, 1.5, HOLE)
    stand = line(28.5, 36, 28.5, 42, INK, 3.2) + line(22, 43, 35, 43, INK, 3.2)
    phone = (rrect(36, 22, 14, 25, 3.5, HOLE) + rrect(38, 24, 10, 21, 2.5, INK) +
             rrect(40, 26.5, 6, 14, 1, HOLE))
    return tv + stand + phone


@small("net.kirgroup.confy")
def confy_s():
    sheet = rrect(19, 13, 28, 34, 4, INK)
    cells = "".join(rrect(29 + c * 8, 20 + r * 9, 6, 6, 1.5, HOLE) for r in range(3) for c in range(2))
    bubble = rrect(13, 20, 18, 13, 4, LIGHT_BLUE_DARK) + poly([(20, 32), (27, 32), (25, 38)], LIGHT_BLUE_DARK, 1.5)
    return sheet + cells + bubble


@small("northgard")
def northgard_s():
    return ring_b(32, 30, 15, INK, 4.5) + circle(32, 30, 8, INK)


@small("nishang")
def nishang_s():
    c = stroke("M28 22C26.5 20 25 19.5 23 19.5C19 19.5 16.5 23.5 16.5 29.5"
               "C16.5 35.5 19 39.5 23 39.5C25 39.5 26.5 39 28 37", INK, 4.4)
    return c + line(35, 20, 42, 39, INK, 4.4)


@small("nip2")
def nip2_s():
    frame = rrect(14.5, 14, 35, 32, 4, INK) + rrect(19, 18.5, 26, 23, 2, HOLE)
    return frame + path("M19 33C25 29 29 36 34 33C38 31 41.5 32 45 31V41.5H19Z", INK)


@small("nomacs")
def nomacs_s():
    return (poly([(16, 13), (48, 13), (32, 31)], INK, 3) + line(32, 29, 32, 43, INK, 4) +
            rrect(23, 42, 18, 5, 2.5, INK))


@small("normcap")
def normcap_s():
    rect = rrect(14, 14, 30, 24, 3, "none", f' stroke="{INK}" stroke-width="3.2"')
    return rect + line(30, 28, 47, 45, INK, 6) + _star4(22, 22, 6, INK)


@small("nl.g4d.Girens")
def girens_s():
    back = rrect(21, 13, 22, 24, 8, INK)
    arms = rrect(14, 25, 9, 18, 3.5, INK) + rrect(41, 25, 9, 18, 3.5, INK)
    return back + arms + rrect(20, 33, 24, 11, 2.5, AMBER_SOFT)


@small("nitroshare")
def nitroshare_s():
    shape = poly([(19, 21), (36, 11), (36, 17), (45, 17), (45, 39), (28, 49), (28, 43), (19, 43)], INK, 3)
    return shape + stroke("M26 37V23L38 37V23", HOLE, 4.2)


@small("net.meijn.onvifviewer")
def onvifviewer_s():
    cam = g(rrect(14, 16, 28, 14, 4, INK), "rotate(14 28 23)")
    return cam + stroke("M38 30V39H44", INK, 4) + rrect(43, 28, 7, 17, 2.5, INK)


@small("net.natesales.Aviator")
def aviator_s():
    return (rrect(13, 14, 38, 32, 7, INK) + circle(24, 28, 6.5, PINK_SOFT) +
            circle(40, 28, 6.5, PINK_SOFT))


@small("net.sf.VICE")
def vice_s():
    c = ('<path d="M35 18A12.5 12.5 0 1 0 35 42" fill="none" stroke="INK" '
         'stroke-width="9" stroke-linecap="butt"/>')
    return (c + poly([(37, 20), (50, 20), (46, 28.5), (37, 28.5)], INK, 1) +
            poly([(37, 31.5), (46, 31.5), (50, 40), (37, 40)], RED_LIGHT, 1))


@small("net.sourceforge.Fillets")
def fillets_s():
    fish = path("M20 30C25 21 38 20.5 47 30C38 39.5 25 39 20 30Z", INK)
    return fish + poly([(23, 30), (14, 22), (14, 38)], INK, 2) + circle(39, 28.5, 2.6, HOLE)


@small("netbeans")
def netbeans_s():
    outer = poly([pt(32, 30, 18, -90 + 60 * k) for k in range(6)], INK, 3)
    return outer + poly([pt(32, 30.5, 10, -90 + 60 * k) for k in range(6)], BLUE_SOFT, 2)


@small("netsurf")
def netsurf_s():
    pts = [pt(36, 24, 9 if k % 2 == 0 else 4, -90 + 30 * k) for k in range(12)]
    return circle(32, 30, 17, INK) + poly(pts, HOLE, 1)


@small("nitrogen")
def nitrogen_s():
    rings = "".join(g(f'<ellipse cx="32" cy="30" rx="17" ry="8" fill="none" stroke="{INK}" '
                      'stroke-width="3"/>', f"rotate({a} 32 30)") for a in (45, -45))
    return rings + circle(32, 30, 7, INK)


@small("nihilumbra")
def nihilumbra_s():
    arms = "".join(line(32, 30, *pt(32, 30, 17, -60 + 72 * k), INK, 5) for k in range(5))
    return arms + circle(32, 30, 11, INK) + circle(27.5, 30, 3.5, HOLE) + circle(36.5, 30, 3.5, HOLE)


@small("nmap")
def nmap_s():
    return (circle(32, 30, 17, INK) +
            path("M20 19C26 17 30 20 29 25C28 30 23 30 23 36C19 33 16 28 17 24C17.5 22 18.5 20 20 19Z", HOLE) +
            path("M36 33C41 31 45 33 43 38C41 42 37 44 34 45C33 40 32 36 36 33Z", HOLE))


@small("nootka")
def nootka_s2():
    staff = "".join(line(14, y, 50, y, BROWN_DEEP, 2.4) for y in (22, 30, 38))
    clef = stroke("M31 48L28.5 15C28 11.5 32 11 33 13.5C34.5 18 31 22 27.5 26"
                  "C23 30.5 23 35 26.5 37.5C30 40 35.5 38.5 36 34C36.5 30 31.5 29 29.5 31.5", INK, 4)
    return staff + clef


@small("nos-tv")
def nos_tv_s():
    tv = rrect(13, 14, 30, 23, 4, INK) + rrect(17, 18, 22, 15, 1.5, HOLE)
    return tv + line(28, 37, 28, 43, INK, 4) + rrect(36, 21, 15, 27, 4, HOLE) + rrect(38, 23, 11, 23, 3, INK)
