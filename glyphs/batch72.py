# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 72: vitomu to webcamoid."""
from lm import (
    AMBER_DARK, AMBER_DEEP, AMBER_LIGHT, AMBER_SOFT, BLUE, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_LIGHT, BROWN_LIGHT, circle, cut, CX, CY, CYAN_DARK, DEEP_ORANGE,
    DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_DEEP, DEEP_PURPLE_SOFT, f, g, GREY_DARK,
    GREY_SOFT, HOLE, INDIGO, INK, LIGHT_BLUE, LIGHT_BLUE_DEEP, line, ORANGE_DEEP, ORANGE_LIGHT,
    ORANGE_SOFT, path, PINK, poly, pt, PURPLE, PURPLE_DEEP, PURPLE_SOFT, RED, RED_LIGHT, rrect,
    stroke, TEAL, TEAL_DEEP, TEAL_SOFT, YELLOW_LIGHT, YELLOW_SOFT,
)
from glyphs.kit import arc, arrowhead_e, ell_b, registry
from glyphs.kit import shared_vivaldi

ICONS, SMALL, reg, small = registry()


def hexagon(cx, cy, r, rot=0):
    return [pt(cx, cy, r, rot + 60 * k) for k in range(6)]


def hexd(cx, cy, r, rot=0):
    return "M" + "L".join(f"{f(x)} {f(y)}" for x, y in hexagon(cx, cy, r, rot)) + "Z"


def cloud(fill):
    return (circle(26, 32, 7, fill) + circle(34.5, 27.5, 9, fill) + circle(42, 34, 6, fill) +
            rrect(19, 32, 29, 8, 4, fill))


@reg("vitomu", PINK)
def vitomu():
    a = stroke(arc(CX, CY, 14, 195, 315), INK, 4.4) + arrowhead_e(*pt(CX, CY, 14, 335), 70, INK, 4.4)
    b = stroke(arc(CX, CY, 14, 15, 135), INK, 4.4) + arrowhead_e(*pt(CX, CY, 14, 155), 250, INK, 4.4)
    return a + b + poly([(28.5, 23.5), (38.5, 30), (28.5, 36.5)], INK, 2.5)


@reg("vmd", GREY_DARK)
def vmd():
    v = stroke("M14 22L19 38L24 22", RED_LIGHT, 4)
    m = stroke("M27.5 38V22L32.5 31L37.5 22V38", AMBER_DEEP, 4)
    d = stroke("M41.5 22V38H43A7 8 0 0 0 43 22Z", BLUE_LIGHT, 4)
    return v + m + d


@reg("vmpk", GREY_DARK)
def vmpk():
    keys = rrect(14, 13, 36, 34, 3.5, INK)
    seps = "".join(line(x, 13, x, 47, HOLE, 1.8, "butt") for x in (21.2, 28.4, 35.6, 42.8))
    blacks = "".join(rrect(x - 2.5, 13, 5, 19, 1.2, HOLE) for x in (21.2, 28.4, 42.8))
    return keys + seps + blacks


@reg("vocal", PURPLE)
def vocal():
    mic = rrect(25, 12, 14, 22, 7, INK)
    cup = stroke("M18.5 28A13.5 13.5 0 0 0 45.5 28", INK, 3.6)
    return mic + cup + line(32, 41.5, 32, 46.5, INK, 3.6) + line(25, 47, 39, 47, INK, 3.6)


@reg("vokoscreenNG", DEEP_PURPLE)
@reg("vokoscreen", BLUE)
def vokoscreen():
    return _voko()


def _voko():
    body = rrect(13, 13, 38, 27, 4, INK) + rrect(16.5, 16.5, 31, 20, 2, HOLE)
    reel = circle(32, 26.5, 7.5, INK) + "".join(
        circle(*pt(32, 26.5, 4.3, -90 + 72 * k), 1.7, HOLE) for k in range(5))
    stand = line(32, 40, 32, 45, INK, 3.6) + line(24, 46.5, 40, 46.5, INK, 3.6)
    return body + reel + stand


@reg("webamp-desktop", TEAL)
def webamp():
    bolt = poly([(42, 12), (20, 30), (30.5, 32), (22, 48), (44, 28), (33.5, 26)], AMBER_SOFT, 2.4)
    return bolt


@reg("webcamoid", BLUE_GREY)
def webcamoid():
    base = path("M15 48C18 42 25 39.5 32 39.5C39 39.5 46 42 49 48Z", INK)
    head = circle(32, 25, 14, INK) + circle(32, 25, 8, HOLE) + circle(32, 25, 4.2, INK)
    return base + head


@reg("vuze", BLUE_DEEP)
def vuze():
    body = path("M30 11C35 9.5 42 10.5 44 14C45.5 17 41 20 38 23C36 26 38 30 38 34"
                "C38 41 33 46 27 46C21 46 17 42 18 36C19 31 22 29 22 24C22 18 25 12.5 30 11Z", INK)
    fore = stroke("M36.5 28L43 31.5L48 29.5", INK, 3.4)
    hind = stroke("M34 41.5L42 44.5L48.5 43", INK, 3.6)
    toes = circle(48.5, 29.3, 2.1, INK) + circle(49, 42.8, 2.2, INK)
    return body + fore + hind + toes


@reg("vivaldi-snapshot", GREY_DARK)
@reg("vivaldi-beta", RED)
def vivaldi_beta():
    return _vivaldi()


def _vivaldi():
    return shared_vivaldi()


@reg("waterfox", LIGHT_BLUE_DEEP)
def waterfox():
    w = stroke("M15.5 22L23.5 42L32 27L40.5 42L48.5 22", INK, 6.5)
    drops = (path("M30 12C32.5 15.5 34 17.5 34 19.5A4 4 0 0 1 26 19.5C26 17.5 27.5 15.5 30 12Z", INK) +
             circle(39, 14.5, 2.6, INK))
    return w + drops


@reg("wavebox", LIGHT_BLUE)
def wavebox():
    left = poly([(15, 14), (30, 14), (30, 22), (26, 25), (30, 28), (30, 32), (26, 35), (30, 38),
                 (30, 46), (15, 46), (15, 36), (20, 30), (15, 24)], INK, 2)
    right = poly([(49, 14), (34, 14), (34, 22), (38, 25), (34, 28), (34, 32), (38, 35), (34, 38),
                  (34, 46), (49, 46), (49, 36), (44, 30), (49, 24)], INK, 2)
    return left + right


@reg("web-lounge", BLUE_GREY_DARK)
def web_lounge():
    a = stroke(hexd(24, 30, 10.5, 30), INK, 3.4)
    b = stroke(hexd(40, 30, 10.5, 30), ORANGE_LIGHT, 3.4)
    dots = circle(22, 31, 1.9, INK) + circle(27, 31, 1.9, INK)
    dots2 = circle(38, 29, 1.9, INK) + circle(43, 29, 1.9, INK)
    return a + b + dots + dots2


@reg("webapp-manager", BLUE_GREY_DARK)
def webapp_manager():
    c = g(cloud(INK), "translate(32 30) scale(1.05) translate(-33 -30)")
    bars = "".join(rrect(15 + 9 * k, 44, 7.4, 3.5, 1.75, c) for k, c in
                   enumerate([RED_LIGHT, ORANGE_DEEP, BLUE_LIGHT, AMBER_LIGHT]))
    return g(c, "translate(0 -3)") + bars


@reg("webby", PURPLE_DEEP)
def webby():
    return stroke("M15 16L22.5 44L32 22L41.5 44L49 16", INK, 6.5)


@reg("weather", LIGHT_BLUE_DEEP)
def weather():
    sun = circle(37, 23, 7, AMBER_SOFT) + "".join(
        line(*pt(37, 23, 10, a), *pt(37, 23, 12.5, a), AMBER_SOFT, 2.8) for a in range(-180, 60, 45))
    return sun + _weather_cloud()


def _weather_cloud():
    halo = (circle(23, 37, 9.2, HOLE) + circle(31.5, 32.5, 11.2, HOLE) + circle(39, 39, 8.2, HOLE))
    body = (circle(23, 37, 7, INK) + circle(31.5, 32.5, 9, INK) + circle(39, 39, 6, INK) +
            rrect(16, 37, 29, 8, 4, INK))
    return halo + body


@reg("vmware-netcfg", BLUE_DEEP)
def vmware_netcfg():
    box = rrect(22, 12.5, 20, 18, 3, INK) + rrect(27, 17.5, 10, 8, 1.5, HOLE)
    net = line(32, 30, 32, 40, INK, 3.4) + line(18, 40, 46, 40, INK, 3.4)
    nodes = "".join(circle(x, 40, 4.6, INK) for x in (17.5, 32, 46.5))
    return box + net + nodes


@reg("vmware-player", BLUE_DEEP)
def vmware_player():
    out = ""
    for rot in (0, 90, 180, 270):
        arm = (stroke("M29 27L19 17", INK, 4.2) + stroke("M16 26V16H26", INK, 4.6))
        out += g(arm, f"rotate({rot} 32 30)")
    return out


@reg("vmware-view", ORANGE_DEEP)
def vmware_view():
    screen = rrect(13, 13, 38, 26, 4, INK) + rrect(16.5, 16.5, 31, 19, 2, HOLE)
    tree = (rrect(28.5, 19, 7, 5, 1, INK) + line(32, 24, 32, 27, INK, 1.8, "butt") +
            line(23, 27, 41, 27, INK, 1.8, "butt") +
            "".join(line(x, 27, x, 29, INK, 1.8, "butt") + rrect(x - 3.5, 28.5, 7, 5, 1, INK)
                    for x in (23, 32, 41)))
    stand = line(32, 39, 32, 45, INK, 3.6) + line(24, 46.5, 40, 46.5, INK, 3.6)
    return screen + tree + stand


@reg("vmware-vmrc", BLUE_DEEP)
def vmware_vmrc():
    sq = rrect(36, 12, 13, 13, 2.5, INK)
    shaft = stroke("M17 46L37 26", INK, 5)
    head = stroke("M24 25H37V38", INK, 5)
    return sq + shaft + head


@reg("vmware-workstation", BLUE_DEEP)
def vmware_workstation():
    back = cut("M27 11.5H46A3.5 3.5 0 0 1 49.5 15V34A3.5 3.5 0 0 1 46 37.5H27A3.5 3.5 0 0 1 23.5 34"
               "V15A3.5 3.5 0 0 1 27 11.5Z M29 17V32H44V17Z", INK)
    front = cut("M18 22.5H37A3.5 3.5 0 0 1 40.5 26V45A3.5 3.5 0 0 1 37 48.5H18A3.5 3.5 0 0 1 14.5 45"
                "V26A3.5 3.5 0 0 1 18 22.5Z M20 28V43H35V28Z", INK)
    gap = stroke("M23.5 26H29V32", HOLE, 1.6)
    return back + gap + front


@reg("vncviewer", BLUE)
def vncviewer():
    v = stroke("M15.5 15L22.5 45L29.5 15", INK, 3.6)
    n = stroke("M34.5 29V20.5A5 5 0 0 1 44.5 20.5V29", INK, 3.6)
    cx0, cy0 = pt(39.5, 39, 5.5, -40)
    cx1, cy1 = pt(39.5, 39, 5.5, 40)
    c = stroke(f"M{f(cx0)} {f(cy0)}A5.5 5.5 0 1 0 {f(cx1)} {f(cy1)}", INK, 3.6)
    return v + n + c


def _vscode(shade):
    x = line(40.5, 17, 18, 37, INK, 5.5) + line(40.5, 43, 18, 23, shade, 5.5)
    bar = path("M38 12.5L46 16.5A2.5 2.5 0 0 1 47.5 18.8V41.2A2.5 2.5 0 0 1 46 43.5L38 47.5Z", INK)
    return x + bar


@reg("vscode-exploration", ORANGE_DEEP)
def vscode_exploration():
    return _vscode(ORANGE_SOFT)


@reg("vscode-insiders", TEAL_DEEP)
def vscode_insiders():
    return _vscode(TEAL_SOFT)


def _coral():
    return (stroke("M32 47V18", INK, 4.4) +
            stroke("M32 39C24 39 19.5 34 19.5 25V19", INK, 4.4) +
            stroke("M32 39C40 39 44.5 34 44.5 25V19", INK, 4.4) +
            stroke("M19.8 30L14 25", INK, 3.6) + stroke("M44.2 30L50 25", INK, 3.6) +
            stroke("M32 30L25.5 24.5", INK, 3.4) + stroke("M32 27L38.5 21.5", INK, 3.4))


@reg("vscodium-insiders", ORANGE_DEEP)
@reg("vscodium", BLUE)
def vscodium():
    return _coral()


@reg("vstudio", BLUE_LIGHT)
def vstudio():
    body = path("M32 11C38.5 15.5 40.5 24 39.5 35H24.5C23.5 24 25.5 15.5 32 11Z", INK)
    fins = (poly([(24.5, 27), (18, 38), (24.5, 38)], INK, 2) +
            poly([(39.5, 27), (46, 38), (39.5, 38)], INK, 2))
    window = circle(32, 23, 3.4, HOLE)
    flame = poly([(27.5, 38.5), (36.5, 38.5), (32, 48)], AMBER_SOFT, 2)
    return g(body + fins + window + flame, "rotate(45 32 30)")


@reg("vnote", TEAL_DEEP)
def vnote():
    fold = poly([(39, 12.5), (50, 12.5), (50, 23.5)], TEAL_SOFT, 1.5)
    return stroke("M17 14.5L30.5 45L47.5 15.5", INK, 6.5) + fold


VYM_HEAD = path('M24 48V42H20.5A2 2 0 0 1 18.5 40V35.5L15.5 33L18.5 27.5C18.5 18 24.5 12 33 12C42 12 48.5 18.5 48.5 27C48.5 33 46 37 42.5 39.5V48Z', INK)


@reg("vym", INDIGO)
def vym():
    head = VYM_HEAD
    target = circle(34, 26, 7, HOLE) + circle(34, 26, 4.4, INK) + circle(34, 26, 2, HOLE)
    return head + target


@reg("vivado_logo", GREY_DARK)
def vivado():
    top = poly([(18.3, 4.5), (37, 17), (39.5, 37), (21, 24)], YELLOW_SOFT, 1.5)
    left = poly([(21, 24), (4, 41), (4, 59.5), (21, 45)], GREY_SOFT, 1.5)
    right = poly([(39.5, 37), (60, 46), (41, 54), (21, 45)], YELLOW_LIGHT, 1.5)
    tri = poly([(21, 24), (39.5, 37), (21, 45)], INK, 1.5)
    return g(top + left + right + tri, "translate(32 30) scale(.68) translate(-32 -32)")


@reg("void-wizard", PURPLE_DEEP)
def void_wizard():
    a = stroke(arc(CX, CY, 13.5, -70, 150), INK, 5.5)
    b = stroke(arc(CX, CY, 13.5, 180, 260), PURPLE_SOFT, 5.5)
    return a + b + circle(CX, CY, 5, INK)


@reg("vorta", BLUE_GREY_DEEP)
def vorta():
    top = poly([(20, 16.5), (44, 16.5), (49.5, 28), (14.5, 28)], INK, 2.5)
    box = rrect(13.5, 30, 37, 14, 3.5, INK)
    dots = circle(37, 37, 2.6, DEEP_ORANGE_LIGHT) + circle(43.5, 37, 2.6, ORANGE_LIGHT)
    return top + box + dots


@reg("vprerex", AMBER_DEEP)
def vprerex():
    frame = f'<rect x="16" y="19" width="32" height="22" rx="3.5" fill="none" stroke="{INK}" stroke-width="3.6"/>'
    a1 = stroke("M19 11.5L27.5 23.5", HOLE, 8) + stroke("M19 11.5L27.5 23.5", INK, 3.4) + \
        arrowhead_e(29, 25.5, 55, INK, 4.4)
    a2 = stroke("M35 35L43 46", HOLE, 8) + stroke("M35 35L43 46", INK, 3.4) + \
        arrowhead_e(44.5, 48, 55, INK, 4.4)
    return frame + a1 + a2


@reg("vroid-studio", AMBER_DEEP)
def vroid():
    hexa = poly(hexagon(CX, CY, 17.5, 0), INK, 3)
    v = stroke("M22.5 23L31 37.5L41.5 21.5", HOLE, 5.5)
    return hexa + v


@reg("wallch", AMBER_DEEP)
def wallch():
    x0, y0 = pt(CX, 31, 12.5, -40)
    x1, y1 = pt(CX, 31, 12.5, 40)
    body = stroke(f"M{f(x0)} {f(y0)}A12.5 12.5 0 1 0 {f(x1)} {f(y1)}", INK, 6)
    head = poly([(x0 - 3, y0 - 4.5), (x0 + 4, y0 - 5), (x0 + 12, y0 - 1.5), (x0 + 2, y0 + 3.5)], INK, 3)
    tail = poly([(x1 - 3, y1 + 1.5), (x1 + 5, y1 - 7.5), (x1 + 2.5, y1 + 2.5)], INK, 1.5)
    legs = (stroke("M24.5 24L29 25.5L29.5 29.5", INK, 2.8) + stroke("M24.5 38.5L29 37L29.5 33", INK, 2.8))
    return body + head + tail + legs


@reg("wallpapoz", PURPLE_DEEP)
def wallpapoz():
    hexa = poly(hexagon(CX, CY, 17.5, 30), INK, 3)
    w = stroke("M22.5 23L26.5 38L32 28L37.5 38L41.5 23", HOLE, 4.4)
    return hexa + w


@reg("warpinator", DEEP_PURPLE_DEEP)
def warpinator():
    out = ""
    for a, r, nr in [(-45, 16, 3.4), (-140, 11, 2.8), (180, 15, 3.2), (125, 13.5, 3), (55, 13, 3)]:
        x, y = pt(33, 30, r, a)
        out += line(33, 30, x, y, INK, 2.6) + circle(x, y, nr, INK)
    return out + circle(33, 30, 7, INK) + circle(33, 30, 3.5, HOLE)


@reg("warsow", DEEP_ORANGE)
def warsow():
    shape = (rrect(22, 13, 29, 6, 0.5, INK) + rrect(22, 13, 6, 15, 0.5, INK) +
             cut("M22 23H43V38H22Z M28 27.5V33.5H37V27.5Z", INK) +
             rrect(37, 33, 6, 14, 0.5, INK) + rrect(13, 41, 30, 6, 0.5, INK))
    return g(shape, "translate(32 30) skewX(-14) translate(-32 -30)")


@reg("war-thunder", INDIGO)
def war_thunder():
    turret = path("M21 26C21 20.5 25 18 30 18C35 18 38 20.5 38 26Z", INK)
    barrel = line(36, 22.5, 50, 22.5, INK, 3)
    hull = poly([(14, 27.5), (48, 27.5), (45, 33), (17, 33)], INK, 2)
    track = rrect(14, 34.5, 36, 11, 5.5, INK)
    wheels = "".join(circle(x, 40, 3, HOLE) for x in (20.5, 28, 35.5, 43))
    return turret + barrel + hull + track + wheels


@reg("warzone2100", BLUE_GREY_DEEP)
def warzone():
    top = rrect(18, 13, 28, 16, 3, INK) + "".join(
        rrect(21 + 6 * c, 16 + 6 * r, 4, 4, 1, HOLE) for r in range(2) for c in range(4))
    hull = rrect(17, 31, 30, 10, 2, INK)
    tracks = rrect(12, 31, 8, 16, 2, INK) + rrect(44, 31, 8, 16, 2, INK)
    lines = "".join(line(12, y, 20, y, HOLE, 1.6, "butt") + line(44, y, 52, y, HOLE, 1.6, "butt")
                    for y in (36, 41))
    return top + hull + tracks + lines


@reg("wassabee", BLUE_DEEP)
def wassabee():
    shield = "M15 16C22 12.5 42 12.5 49 16C49.5 31 42 42 32 48C22 42 14.5 31 15 16Z"
    outer = stroke(shield, INK, 3.4)
    inner = stroke("M21 21.5C21 32 25.5 38 28 41M43 21.5C43 32 38.5 38 36 41", INK, 3.2)
    spike = poly([(32, 27), (35, 42), (32, 46), (29, 42)], INK, 1.5)
    bar = stroke("M20.5 20C27 18 37 18 43.5 20", ORANGE_LIGHT, 3.4) + line(32, 19, 32, 24, ORANGE_LIGHT, 3)
    return outer + inner + spike + bar


@reg("wargus", AMBER_DARK)
def wargus():
    w = stroke("M17 16L24 45L32 25L40 45L47 16", AMBER_SOFT, 5.2)
    serifs = line(13, 15.5, 22, 15.5, AMBER_SOFT, 3.6) + line(42, 15.5, 51, 15.5, AMBER_SOFT, 3.6)
    return w + serifs


@reg("warmux", BLUE_GREY_DEEP)
def warmux():
    fuse = stroke("M40 20L45 13", INK, 3.2) + circle(46.5, 11.5, 2.4, ORANGE_LIGHT)
    cap = g(rrect(-4.5, -3, 9, 6, 1.5, INK), "translate(38.5 22) rotate(-35)")
    bomb = circle(30, 32, 15, INK)
    face = (ell_b(24.5, 29, 3.2, 4, HOLE) + ell_b(35, 29, 3.2, 4, HOLE) +
            rrect(26, 38, 3, 4.5, 1.4, HOLE) + rrect(31, 38, 3, 4.5, 1.4, HOLE))
    return fuse + cap + bomb + face


@reg("warframe", CYAN_DARK)
def warframe():
    arches = (stroke("M14.5 41C19.5 36 23 27 32 14C41 27 44.5 36 49.5 41", INK, 3.4) +
              stroke("M21 43C24.5 38 27 32 32 25C37 32 39.5 38 43 43", INK, 3.2) +
              stroke("M27 45C28.5 41.5 30 38.5 32 35.5C34 38.5 35.5 41.5 37 45", INK, 3))
    return arches


@reg("waveform11", BLUE_GREY_DARK)
def waveform():
    body = (stroke("M24.5 21L32 28.5L39.5 21", INK, 5) + stroke("M24.5 39L32 31.5L39.5 39", INK, 5) +
            stroke(arc(CX, CY, 13.5, 135, 225), INK, 5) + stroke(arc(CX, CY, 13.5, -45, 45), INK, 5))
    tris = poly([(27, 13.5), (37, 13.5), (32, 19)], DEEP_PURPLE_SOFT, 1.5) + \
        poly([(27, 46.5), (37, 46.5), (32, 41)], DEEP_PURPLE_SOFT, 1.5)
    return body + tris


@reg("waydroid", BROWN_LIGHT)
def waydroid():
    dome = path("M15.5 30A16.5 16.5 0 0 1 48.5 30Z", INK)
    ant = line(22, 17, 18.5, 12, INK, 2.8) + line(42, 17, 45.5, 12, INK, 2.8)
    low = path("M15.5 32.5H48.5A16.5 16.5 0 0 1 15.5 32.5Z", ORANGE_LIGHT)
    w = stroke("M24 35L28 43.5L32 37L36 43.5L40 35", INK, 2.8)
    eyes = circle(25.5, 24.5, 1.9, HOLE) + circle(38.5, 24.5, 1.9, HOLE)
    return dome + ant + eyes + low + w


@reg("wayland", AMBER_DEEP)
def wayland():
    return (stroke("M17 16L23.5 44L32 24L39 44L47 13", INK, 5) +
            line(47, 13, 48.5, 10.5, INK, 2.6) + line(17, 16, 15.5, 13, INK, 2.6))


@reg("vk", BLUE)
def vk():
    return _vk(0)


@reg("vkaudiosaver", BLUE_GREY_DEEP)
def vkaudiosaver():
    arrow = stroke("M31 36V45.5M26.5 41L31 45.5L35.5 41", INK, 3.4)
    return _vk(-7) + arrow


def _vk(dy):
    v = stroke(f"M14 {20 + dy}L21 {38 + dy}L28 {20 + dy}", INK, 4.6)
    k = stroke(f"M34 {20 + dy}V{38 + dy}M47 {20 + dy}L37 {29 + dy}L48 {38 + dy}", INK, 4.6)
    return v + k


@small("vmpk")
def vmpk_s():
    keys = rrect(14, 13, 36, 34, 3.5, INK)
    blacks = "".join(rrect(x - 3, 13, 6, 20, 1.2, HOLE) for x in (23, 32, 41))
    return keys + blacks


@small("vokoscreenNG")
@small("vokoscreen")
def vokoscreen_s():
    return _voko_s()


def _voko_s():
    body = rrect(13, 13, 38, 27, 4, INK) + rrect(17, 17, 30, 19, 2, HOLE)
    return body + circle(32, 26.5, 6.5, INK) + circle(32, 26.5, 2.4, HOLE) + \
        line(32, 40, 32, 45, INK, 3.6) + line(24, 46.5, 40, 46.5, INK, 3.6)


@small("vmware-view")
def vmware_view_s():
    screen = rrect(13, 13, 38, 26, 4, INK) + rrect(17, 17, 30, 18, 2, HOLE)
    tree = (rrect(28, 19.5, 8, 5, 1, INK) + line(32, 24, 32, 28, INK, 2.4, "butt") +
            rrect(20, 27.5, 8, 5, 1, INK) + rrect(36, 27.5, 8, 5, 1, INK) +
            line(24, 27.5, 40, 27.5, INK, 2.4, "butt"))
    return screen + tree + line(32, 39, 32, 45, INK, 3.6) + line(24, 46.5, 40, 46.5, INK, 3.6)


@small("warzone2100")
def warzone_s():
    top = rrect(18, 13, 28, 16, 3, INK) + "".join(
        rrect(22 + 11 * c, 17, 8, 8, 1.5, HOLE) for c in range(2))
    return top + rrect(12, 31, 40, 16, 3, INK) + line(12, 39, 52, 39, HOLE, 2.4, "butt")


@small("web-lounge")
def web_lounge_s():
    return stroke(hexd(24, 30, 10.5, 30), INK, 4) + stroke(hexd(40, 30, 10.5, 30), ORANGE_LIGHT, 4)


@small("vncviewer")
def vncviewer_s():
    v = stroke("M15.5 15L22.5 45L29.5 15", INK, 4)
    return v + stroke("M35 45V33A5 5 0 0 1 45 33V45", INK, 4)


@small("vkaudiosaver")
def vkaudiosaver_s():
    return _vk(0)


@small("vmd")
def vmd_s():
    return stroke("M14 18L21 42L28 18", RED_LIGHT, 5) + stroke("M34 42V18L41 31L48 18V42", AMBER_DEEP, 5)


@small("vmware-player")
def vmware_player_s():
    tri = poly([(15, 13), (27, 13), (15, 25)], INK, 3)
    return "".join(g(tri, f"rotate({r} 32 30)") for r in (0, 90, 180, 270))


@small("vmware-workstation")
def vmware_workstation_s():
    back = f'<rect x="27" y="14" width="20" height="20" rx="3" fill="none" stroke="{INK}" stroke-width="5"/>'
    front = f'<rect x="17" y="26" width="20" height="20" rx="3" fill="none" stroke="{INK}" stroke-width="5"/>'
    return back + front


@small("vprerex")
def vprerex_s():
    frame = f'<rect x="15" y="20" width="34" height="23" rx="4" fill="none" stroke="{INK}" stroke-width="4"/>'
    return frame + stroke("M22 12L31 25", INK, 4) + arrowhead_e(33, 28, 55, INK, 5.5)


@small("vym")
def vym_s():
    head = VYM_HEAD
    return head + circle(34, 26, 7.5, HOLE) + circle(34, 26, 3.6, INK)


@small("wassabee")
def wassabee_s():
    shield = "M15 16C22 12.5 42 12.5 49 16C49.5 31 42 42 32 48C22 42 14.5 31 15 16Z"
    return (stroke(shield, INK, 4) + poly([(32, 24), (36, 41), (32, 45), (28, 41)], INK, 2) +
            stroke("M21 20.5C27 18.5 37 18.5 43 20.5", ORANGE_LIGHT, 4))
