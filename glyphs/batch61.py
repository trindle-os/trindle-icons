# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 61: resharpercpp to rubymine.

Same rules as batch01: tile from the palette step nearest the brand
colour, mark in INK, HOLE for cut-throughs, any second shade another
palette step.
"""
from lm import *
from glyphs.kit import arc_c, arrowhead_d, _jb, pie_c, registry, ring_b, _star

ICONS, SMALL, reg, small = registry()

def hexagon(cx, cy, r, colour):
    return poly([pt(cx, cy, r, 60 * k) for k in range(6)], colour, 1.4)

JB_R = "M20.5 29.5V19.5H24.5A2.6 2.6 0 0 1 24.5 24.7H20.5M24.2 24.7L27.5 29.5"
BIG_R = "M24 45V15H33A7.5 7.5 0 0 1 33 30H24M32 30L41 45"

@reg("resharpercpp", PURPLE_DEEP)
def resharpercpp():
    plus = "".join(line(x - 2.8, 24.5, x + 2.8, 24.5, HOLE, 2.6) + line(x, 21.7, x, 27.3, HOLE, 2.6)
                   for x in (34, 42))
    return _jb(stroke(JB_R, HOLE, 3) + plus)

@reg("rider", PINK)
def rider():
    return _jb(stroke(JB_R, HOLE, 3) + stroke("M32 19.5V29.5H34.5A5 5 0 0 0 34.5 19.5Z", HOLE, 3))

@reg("rubymine", RED_DEEP)
def rubymine():
    return _jb(stroke(JB_R, HOLE, 3) + stroke("M31.5 29.5V19.5L36 25.5L40.5 19.5V29.5", HOLE, 3))

@reg("residualvm", ORANGE_DEEP)
def residualvm():
    return stroke(BIG_R, INK, 7.5)

@reg("revolt-desktop", RED)
def revolt_desktop():
    r = stroke("M24.5 45V16H33A7.5 7.5 0 0 1 33 31H24.5M32 31L41 45", INK, 6.5)
    flag = poly([(17.5, 12.8), (27.7, 12.8), (27.7, 20)], INK, 1)
    return r + flag

@reg("rise-to-ruins", GREY_DEEP)
def rise_to_ruins():
    return g(stroke(BIG_R, BROWN_DARK, 7), "translate(2.5 2)") + stroke(BIG_R, INK, 7)

@reg("rrootage", GREY_DARK)
def rrootage():
    r = stroke("M18 45V32M18 35.5A5.5 5.5 0 0 1 24.5 31.5", INK, 4.6)
    R = stroke("M29 45V16H37A7 7 0 0 1 37 30H29M36 30L44 45", INK, 5.4)
    return g(r + R, "translate(1 0)")

@reg("riot-web", BLUE)
def riot_web():
    stem = line(23, 18, 23, 44, INK, 6.4)
    bowl = stroke("M23 16.5H34A8.5 8.5 0 0 1 34 33.5H28", INK, 6.4)
    leg = line(32, 34, 41, 44, BLUE_DARK, 6.4)
    return stem + bowl + leg + circle(23, 16.5, 5, BLUE_DARK)

@reg("rlogo_icon", BLUE_DEEP)
def rlogo_icon():
    rg = cut("M32 13a17 11.5 0 1 0 0.01 0Z" + "M33 18.5a11 6.5 0 1 0 0.01 0Z", BLUE_SOFT)
    r = "M28 46V24H39A5.5 5.5 0 0 1 39 35H28M36 35L43 46"
    return rg + stroke(r, HOLE, 9) + stroke(r, INK, 5.2)

@reg("rstudio", BLUE_LIGHT)
def rstudio():
    r = stroke("M23.5 18.5H33.5A6.2 6.2 0 0 1 33.5 31H27.5M27.5 18.5V41.5M23.5 41.5H31.5"
               "M33 31L37.5 41.5H41", HOLE, 3.8)
    return circle(CX, CY, 16.5, INK) + r

def _rtt():
    doc = rrect(15, 12, 28, 33, 5, INK)
    p = ring_b(29.5, 24, 5.5, HOLE, 3.6) + line(24, 24, 24, 38, HOLE, 3.6)
    badge = circle(40.5, 39.5, 10.5, HOLE) + circle(40.5, 39.5, 8.3, INK)
    spin = arc_c(40.5, 39.5, 4.3, -60, 210, HOLE, 2.4) + arrowhead_d(40.5, 39.5, 4.3, 210, HOLE, 2.6)
    return doc + p + badge + spin

@reg("rtt-rlinux", INDIGO_DEEP)
def rtt_rlinux():
    return _rtt()

@reg("rtt-rstudio", CYAN_DEEP)
def rtt_rstudio():
    return _rtt()

@reg("resolve", BLUE_GREY_DARK)
def resolve():
    petal = path("M32 30L26.3 22.5A7 7 0 1 1 37.7 22.5Z", INK)
    return g("".join(g(petal, f"rotate({a} 32 32)") for a in (0, 120, 240)), "translate(0 2.5)")

@reg("responder", LIGHT_BLUE_DEEP)
def responder():
    sq = rrect(15, 13, 34, 34, 5, INK)
    a = stroke("M44 16C33 20 24 28 15.5 35", HOLE, 3.4)
    b = stroke("M36 22C41 28 43.5 37 44 46.5", HOLE, 3.4)
    return sq + a + b

@reg("restic", BLUE_GREY_DEEP)
def restic():
    def brolly(cx, rot):
        top = path(f"M{cx - 8} 20.5A8 7 0 0 1 {cx + 8} 20.5Z", INK)
        return g(top + line(cx, 20, cx, 27.5, INK, 2.2), f"rotate({rot} {cx} 24)")
    body = path("M22 47V36A10 10 0 0 1 42 36V47Z", INK)
    ears = circle(24, 29, 3, INK) + circle(40, 29, 3, INK)
    eyes = circle(28, 35.5, 2.6, HOLE) + circle(36, 35.5, 2.6, HOLE)
    teeth = rrect(30.3, 39.5, 3.4, 3, 1, HOLE)
    return brolly(19.5, -18) + brolly(44.5, 18) + body + ears + eyes + teeth

@reg("retext", BLUE_GREY)
def retext():
    page = rrect(18, 12, 28, 36, 4, INK)
    rings = "".join(circle(22.5, y, 1.5, HOLE) for y in (17, 22.5, 28, 33.5, 39, 44))
    r = stroke("M29.5 41V19.5H35.5A5.2 5.2 0 0 1 35.5 30H29.5M35 30L40.5 41", HOLE, 3.4)
    return page + rings + r

@reg("retropie", RED_DEEP)
def retropie():
    dome = path("M16 46C16 38 23 34 32 34C41 34 48 38 48 46Z", INK)
    stick = line(32, 35, 32, 20, INK, 3.6)
    ball = circle(32, 18, 6.3, INK)
    dots = circle(23.5, 41.5, 2.2, HOLE) + circle(40.5, 41.5, 2.2, HOLE)
    return dome + stick + ball + dots

@reg("retroshare", BLUE_DARK)
def retroshare():
    a, b, c = (19, 24), (44, 18), (37, 42)
    lines = line(*a, *b, INK, 3) + line(*b, *c, INK, 3) + line(*c, *a, INK, 3)
    return lines + circle(*a, 6, INK) + circle(*b, 6, INK) + circle(*c, 6, INK)

@reg("revolt", BLUE_GREY_DEEP)
def revolt():
    holes = "".join(circle(*pt(CX, CY, 11.3, a), 2.9, HOLE) for a in range(-60, 241, 33))
    stop = line(*pt(CX, CY, 9, 290), *pt(CX, CY, 16, 290), HOLE, 2.4)
    return circle(CX, CY, 16.5, INK) + holes + circle(CX, CY, 5, HOLE) + stop

@reg("rhythmbox", GREY_DEEP)
def rhythmbox():
    cab = rrect(17, 12, 30, 36, 5, INK)
    cone = circle(32, 33, 10.5, AMBER) + circle(32, 33, 4.5, HOLE)
    return cab + cone + circle(22, 17, 1.9, HOLE) + circle(42, 17, 1.9, HOLE)

@reg("ricochet-game", BLUE_GREY_DEEP)
def ricochet():
    out = ""
    for a0 in (200, 20):
        out += arc_c(CX, CY, 15, a0, a0 + 130, INK, 3.6) + arrowhead_d(CX, CY, 15, a0 + 130, INK, 3.6)
    for a0 in (110, 290):
        out += arc_c(CX, CY, 8.5, a0, a0 + 120, BLUE_GREY_SOFT, 3.4) + arrowhead_d(CX, CY, 8.5, a0 + 120, BLUE_GREY_SOFT, 3.2)
    return out

@reg("rigs-of-rods", BLUE_DEEP)
def rigs_of_rods():
    cab = path("M14 38V25A4 4 0 0 1 18 21H24A3 3 0 0 1 27 24V38Z", INK)
    win = rrect(17, 24, 7, 6, 1.5, HOLE)
    bed = rrect(27, 32, 23, 6, 1.5, INK)
    wheels = "".join(circle(x, 39.5, 5.2, HOLE) + circle(x, 39.5, 3.8, INK) for x in (20, 35, 45))
    return g(cab + win + bed + wheels, "translate(0 -1)")

@reg("rimworld", GREY_DEEP)
def rimworld():
    st = poly(_star(CX, CY, 10, 4.6), INK, 2)
    tips = "".join(circle(*pt(CX, CY, 10.5, -90 + 72 * k), 2, INK) for k in range(5))
    return ring_b(CX, CY, 15.3, INK, 3.2) + st + tips

@reg("ristretto", ORANGE_DEEP)
def ristretto():
    cup = path("M18 26H40V32A9 9 0 0 1 31 41H27A9 9 0 0 1 18 32Z", INK)
    handle = ring_b(41, 30.5, 4.3, INK, 3)
    saucer = rrect(14.5, 43, 31, 3.8, 1.9, INK)
    steam = (stroke("M25 21C23 19 27 17 25 14", INK, 2.4) +
             stroke("M32 21C30 19 34 17 32 14", INK, 2.4))
    return g(cup + handle + saucer + steam, "translate(2.5 0)")

@reg("rivals-of-aether", DEEP_PURPLE_DEEP)
def rivals():
    ae = stroke("M14 45L31 15H47M31 15L25.5 45H44M21.5 33.5H42", INK, 4.4)
    return g(ae, "translate(0.5 0)")

@reg("rkward", BLUE_DEEP)
def rkward():
    rg = cut("M28 25a14 9.5 0 1 0 0.01 0Z" + "M28.5 30a8 4.5 0 1 0 0.01 0Z", INK)
    k = line(38, 13, 38, 44, INDIGO_DARK, 5.5) + stroke("M47 22L39.5 31L47.5 44", INDIGO_DARK, 5.5)
    return g(rg + k, "translate(-1.5 0)")

@reg("rmg", CYAN_DEEP)
def rmg():
    m = stroke("M18 42V18L31 31L44 18V30", INK, 6)
    badge = circle(41.5, 39, 9.3, HOLE) + circle(41.5, 39, 7.3, INK)
    plus = line(37.8, 39, 45.2, 39, HOLE, 2.6) + line(41.5, 35.3, 41.5, 42.7, HOLE, 2.6)
    return m + badge + plus

@reg("rnote", BLUE_GREY_DARK)
def rnote():
    book = rrect(18, 12, 28, 36, 4, INK) + line(23, 12, 23, 48, HOLE, 1.8)
    sq = stroke("M38 17.5C31 17 29.5 22 34 24.5C39 27 38.5 32.5 32 33.5"
                "C26.5 34.5 27 40.5 33.5 40.5C36.5 40.5 37.5 43 35 44", HOLE, 3)
    return book + sq

@reg("roam-research", GREY_DARK)
def roam():
    wheel = circle(CX, CY, 16.5, INK) + circle(CX, CY, 12.3, HOLE)
    spokes = (line(20, 30, 44, 30, INK, 2.6) + line(32, 18, 32, 42, INK, 2.6) +
              line(23.5, 38.5, 40.5, 21.5, INK, 2.6))
    base = path("M20.5 36.5H43.5A12.3 12.3 0 0 1 20.5 36.5Z", INK)
    return wheel + spokes + base + circle(CX, CY, 3.2, INK)

@reg("robo3t", INDIGO_LIGHT)
def robo3t():
    body = path("M32 11C39.5 17 42 26 40.5 37H23.5C22 26 24.5 17 32 11Z", INK)
    port = circle(32, 26, 5.3, HOLE) + circle(32, 26, 2.6, INK)
    fins = (path("M23.5 30L17 37V45L24 40Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"') +
            path("M40.5 30L47 37V45L40 40Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"'))
    nozzle = rrect(27.5, 38.5, 9, 6.5, 2, INK)
    return body + port + fins + nozzle

@reg("robocraft", GREY_DARK)
def robocraft():
    out = ""
    for k in range(6):
        x, y = pt(CX, CY, 10.6, -30 + 60 * k)
        out += hexagon(x, y, 5.4, ORANGE if k == 0 else INK)
    return out

@reg("roccat", LIGHT_BLUE_DEEP)
def roccat():
    head = path("M13.5 32.5L19 27C21 20 27 15.5 35 14.5L45 12L41.5 17C46 19.5 49 24 50 29.5"
                "L43.5 29L48.5 34L41.5 34.5L45 41C39.5 39 34.5 38.5 30.5 41L28.5 46.5"
                "L25 40.5L20.5 43L21.5 37.5L15.5 36.5Z", INK)
    eye = path("M21.5 27.5L28.5 25.5L26.5 28.5Z", HOLE, f' stroke="{HOLE}" stroke-width="1.2" stroke-linejoin="round"')
    mouth = stroke("M20 35L27.5 34.5L30 38", HOLE, 2)
    return head + eye + mouth

@reg("rochard", AMBER_DARK)
def rochard():
    outline = stroke("M20 46V32A20 20 0 0 1 40 12H44V24H40A8 8 0 0 0 32 32V46Z", INK, 3)
    mid = stroke("M26 46V32A14 14 0 0 1 40 18H44", INK, 3)
    return outline + mid

@reg("rocket-league", BLUE_DEEP)
def rocket_league():
    shield = path("M15 17C23 12 41 12 49 17C48.5 32 42 42 32 47C22 42 15.5 32 15 17Z", INK)
    inner = path("M21 19.5C28 17 36 17 43.5 19.5C43 30 38.5 37.5 32 41.5C25.5 37.5 21.5 30 21 19.5Z", HOLE)
    swoosh = stroke("M24.5 27C30 26 37 28 41 32", INK, 2.8)
    ball = circle(18.5, 17, 6.8, HOLE) + circle(18.5, 17, 4.8, INK)
    return shield + inner + swoosh + ball

@reg("rocketchat", RED)
def rocketchat():
    bubble = path("M32 16C42 16 49.5 21.5 49.5 29C49.5 36.5 42 42 32 42C29.5 42 27 41.6 25 41"
                  "L16 46L19 38C16 35.5 14.5 32.5 14.5 29C14.5 21.5 22 16 32 16Z", INK)
    dots = "".join(circle(x, 29, 2.9, HOLE) for x in (24, 32, 40))
    return bubble + dots

@reg("rockradio", RED_DEEP)
def rockradio():
    index = rrect(21, 11, 6.4, 24, 3.2, INK)
    pinky = rrect(37.6, 14, 6.4, 20, 3.2, INK)
    palm = rrect(20, 27, 25, 20, 8, INK)
    thumb = g(rrect(13, 30, 14, 6.4, 3.2, INK), "rotate(-35 20 33)")
    folds = line(28.5, 31, 36, 31, HOLE, 2) + line(21, 38.5, 30, 35.5, HOLE, 2)
    return index + pinky + palm + thumb + folds

@reg("rocksndiamonds", BLUE_DEEP)
def rocksndiamonds():
    outer = [(32, 12), (46.5, 20.5), (47, 37.5), (32, 47.5), (17, 37.5), (17.5, 20.5)]
    gem = poly(outer, INK, 2.5)
    face = [(32, 22), (40.5, 35), (23.5, 35)]
    facets = stroke("M32 22L40.5 35H23.5Z", HOLE, 1.9)
    spokes = "".join(line(*a, *b, HOLE, 1.9) for a, b in
                     [((32, 12), face[0]), ((47, 37.5), face[1]), ((17, 37.5), face[2])])
    return gem + facets + spokes

@reg("rocs", BLUE)
def rocs():
    teeth = "".join(g(rrect(29, 11.5, 6, 8, 1.5, INK), f"rotate({45 * k} 32 30)") for k in range(8))
    gear = teeth + circle(CX, CY, 14, INK) + circle(CX, CY, 9.5, HOLE)
    graph = "".join(line(CX, CY, *pt(CX, CY, 6, 60 * k - 90), INK, 1.8) +
                    circle(*pt(CX, CY, 6.3, 60 * k - 90), 1.7, INK) for k in range(6))
    return gear + graph + circle(CX, CY, 2.5, INK)

@reg("rog-control-center", RED_DARK)
def rog():
    top = path("M13 26.5L25.5 29C33 21.5 42 18 51 17C47.5 20.5 46 25.5 45.5 30"
               "C42 36.5 35.5 40 28.5 41.5C27.5 37 25 33.5 20 31.5Z", INK)
    eye = path("M29.5 37.5C34 34.5 38.5 30.5 42.5 25.5C42 31.5 37.5 35.5 30.5 38.5Z", HOLE)
    prong = poly([(13.5, 33.5), (21, 34), (25.5, 39)], INK, 1.6)
    return top + eye + prong

@reg("rogue-legacy", RED_DARK)
def rogue_legacy():
    helm = path("M19 46V31A13 13 0 0 1 45 31V46Z", INK)
    slot = rrect(23, 31, 18, 5, 1.5, HOLE) + rrect(29.5, 31, 5, 15.5, 1.5, HOLE)
    plume = path("M30 18.5C26 12.5 18 11 13 14.5C19 14.5 22 17 23.5 21.5Z", RED_SOFT,
                 ' stroke="#F7847C" stroke-width="1.5" stroke-linejoin="round"')
    return helm + slot + plume

@reg("rolled-out", DEEP_PURPLE_SOFT)
def rolled_out():
    ball = circle(CX, CY, 16.5, INK)
    mouse = circle(32, 33, 7.5, HOLE) + circle(25, 24.5, 4.5, HOLE) + circle(39, 24.5, 4.5, HOLE)
    return ball + mouse + circle(32, 37.5, 1.8, INK)

@reg("rosegarden", PINK_DEEP)
def rosegarden():
    petals = "".join(circle(*pt(CX, CY + 1, 8.3, -90 + 72 * k), 7.2, INK,
                            f' stroke="{HOLE}" stroke-width="1.6"') for k in range(5))
    return petals + circle(CX, CY + 1, 5.5, PINK_SOFT)

@reg("rpcs3", DEEP_PURPLE)
def rpcs3():
    bars = "".join(rrect(x, y, 46 - x, 7, 3.5, INK) for x, y in [(18, 14.5), (24, 26.5), (18, 38.5)])
    return bars + path("M36 14.5H42A4 4 0 0 1 46 18.5V41.5A4 4 0 0 1 42 45.5H36Z", INK)

@reg("rpg-maker-mv", INDIGO_DEEP)
def rpg_maker():
    castle = path("M17 40V14H20V17H22.5V14H25.5V20H28.5V17H31V20H33V17H35.5V20H38.5V14H41.5V17H44V14H47V40Z", INK)
    gate = path("M28 40V31A4 4 0 0 1 36 31V40Z", HOLE)
    grass = rrect(14.5, 38.5, 35, 9, 2.5, GREY_LIGHT)
    return castle + gate + grass

@reg("rquickshare", BLUE)
def rquickshare():
    out = ""
    for a0 in (200, 20):
        out += arc_c(CX, CY, 14.5, a0, a0 + 125, INK, 3.6) + arrowhead_d(CX, CY, 14.5, a0 + 125, INK, 3.8)
    arrow = line(23.5, 30, 38, 30, INK, 3.4) + stroke("M34 25L39.5 30L34 35", INK, 3.4)
    return out + arrow

@reg("rs.ruffle.Ruffle", INDIGO_DEEP)
def ruffle():
    return path("M19 47L21.5 25Q22 21 26 21H29L29.5 17.5Q30 14 34 14H44.5Q48.5 14 48 18"
                "L46.8 29H39.3L40.2 21H33.5L31.5 22.5L28.3 47Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')

@reg("rsibreak", DEEP_PURPLE)
def rsibreak():
    return (ring_b(CX, CY + 1, 15, INK, 3.4) + pie_c(CX, CY + 1, 11, 0, 270, INK) +
            line(32, 31, 32, 11.5, INK, 3.6) + circle(CX, CY + 1, 3, HOLE))

@reg("rssguard", DEEP_ORANGE_DEEP)
def rssguard():
    shield = path("M17 13H47V29C47 38 40 44 32 48C24 44 17 38 17 29Z", INK,
                  f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    rss = (circle(25.5, 35.5, 2.9, HOLE) + stroke("M24.5 27A8.5 8.5 0 0 1 34 36.5", HOLE, 3.2) +
           stroke("M24.5 20A15.5 15.5 0 0 1 41 36.5", HOLE, 3.2))
    return shield + rss

@reg("rto-proxy", AMBER_DEEP)
def rto_proxy():
    return circle(CX, CY, 16.5, INK) + poly(_star(CX, CY + 1, 10.5, 4.6), HOLE, 2.2)

@reg("ru.linux_gaming.PortProtonQt", CYAN)
def portproton():
    pad = path("M19 20H45A5 5 0 0 1 50 25L49 40A5 5 0 0 1 41 43L37.5 38.5H26.5L23 43A5 5 0 0 1 15 40L14 25"
               "A5 5 0 0 1 19 20Z", INK)
    dpad = line(20.5, 29.5, 28.5, 29.5, HOLE, 3) + line(24.5, 25.5, 24.5, 33.5, HOLE, 3)
    btns = "".join(circle(x, y, 1.9, HOLE) for x, y in [(39.5, 25.5), (39.5, 33.5), (35.5, 29.5), (43.5, 29.5)])
    return g(pad + dpad + btns, "translate(0 -1)")

def _jb_s(second):
    r = stroke("M19.5 30.5V17.5H25A3.4 3.4 0 0 1 25 24.3H19.5M24.5 24.3L28.5 30.5", HOLE, 3)
    return rrect(14, 12, 36, 36, 4, INK) + r + second + rrect(19, 39, 14, 4, 2, HOLE)

@small("resharpercpp")
def resharpercpp_s():
    return _jb_s(line(33, 24, 43, 24, HOLE, 3.2) + line(38, 19, 38, 29, HOLE, 3.2))

@small("rider")
def rider_s():
    return _jb_s(stroke("M32.5 17.5V30.5H35.5A6.5 6.5 0 0 0 35.5 17.5Z", HOLE, 3))

@small("rubymine")
def rubymine_s():
    return _jb_s(stroke("M32 30.5V17.5L38 25L44 17.5V30.5", HOLE, 3))

@small("rstudio")
def rstudio_s():
    r = stroke("M26 42V18H33.5A6.5 6.5 0 0 1 33.5 31H26M33 31L39.5 42", HOLE, 4)
    return circle(CX, CY, 17, INK) + r

def _rtt_s():
    doc = rrect(14, 11, 30, 34, 5, INK) + ring_b(29.5, 23.5, 6, HOLE, 3.8) + line(23.5, 23.5, 23.5, 38, HOLE, 3.8)
    badge = circle(41, 40, 10.5, HOLE) + circle(41, 40, 8.5, INK)
    return doc + badge + circle(41, 40, 3.5, HOLE)

@small("rtt-rlinux")
def rtt_rlinux_s():
    return _rtt_s()

@small("rtt-rstudio")
def rtt_rstudio_s():
    return _rtt_s()

@small("roam-research")
def roam_s():
    return (circle(CX, CY, 17, INK) + circle(CX, CY, 11.5, HOLE) + line(20, 30, 44, 30, INK, 3)
            + line(32, 18, 32, 42, INK, 3) + circle(CX, CY, 4, INK))

@small("rocs")
def rocs_s():
    teeth = "".join(g(rrect(28.5, 10.5, 7, 8, 1.5, INK), f"rotate({45 * k} 32 30)") for k in range(8))
    return teeth + circle(CX, CY, 14.5, INK) + circle(CX, CY, 8, HOLE) + circle(CX, CY, 4, INK)

@small("restic")
def restic_s():
    canopy = path("M15 24A17 11 0 0 1 49 24Z", INK)
    body = path("M21 48V37A11 11 0 0 1 43 37V48Z", INK)
    return canopy + body + circle(27.5, 37, 3.2, HOLE) + circle(36.5, 37, 3.2, HOLE)

@small("retext")
def retext_s():
    page = rrect(17, 11, 30, 38, 4, INK)
    r = stroke("M26.5 42V18.5H34A6 6 0 0 1 34 30.5H26.5M33.5 30.5L39.5 42", HOLE, 4)
    return page + r

@small("responder")
def responder_s():
    return (rrect(14, 12, 36, 36, 5, INK) + stroke("M45 15C33 20 24 28 14 35", HOLE, 4) +
            stroke("M36 22C42 28 44 37 45 47", HOLE, 4))

@small("rog-control-center")
def rog_s():
    top = path("M12 26L25.5 29C33 21 42 17.5 52 16C48 20 46.5 25.5 46 30"
               "C42 37 35.5 40.5 28 42C27 37.5 25 33.5 19.5 31.5Z", INK)
    return top + path("M30 38C35 35 39 31 43 26C42.5 32 38 36 31 39Z", HOLE)

@small("ricochet-game")
def ricochet_s():
    out = ""
    for a0 in (200, 20):
        out += arc_c(CX, CY, 14, a0, a0 + 120, INK, 4) + arrowhead_d(CX, CY, 14, a0 + 120, INK, 4.5)
    return out + circle(CX, CY, 5, BLUE_GREY_SOFT)

@small("rigs-of-rods")
def rigs_s():
    cab = path("M12 38V24A4 4 0 0 1 16 20H23A4 4 0 0 1 27 24V38Z", INK)
    bed = rrect(27, 30, 25, 8, 2, INK)
    wheels = "".join(circle(x, 40, 5.5, HOLE) + circle(x, 40, 4, INK) for x in (19.5, 42))
    return cab + rrect(16, 23.5, 7.5, 6.5, 1.5, HOLE) + bed + wheels

@small("rrootage")
def rrootage_s():
    return (stroke("M17 45V31M17 35A6 6 0 0 1 24 30.5", INK, 5) +
            stroke("M30 45V16H38A7 7 0 0 1 38 30H30M37 30L45 45", INK, 5.4))

@small("rosegarden")
def rosegarden_s():
    petals = "".join(circle(*pt(CX, CY + 1, 8.5, -90 + 72 * k), 7.5, INK) for k in range(5))
    return petals + circle(CX, CY + 1, 5, PINK_SOFT)

@small("rocksndiamonds")
def rocksndiamonds_s():
    outer = [(32, 11), (47.5, 20), (48, 38), (32, 48.5), (16, 38), (16.5, 20)]
    return poly(outer, INK, 2.5) + poly([(32, 22.5), (40, 35), (24, 35)], HOLE, 2)

@small("rnote")
def rnote_s():
    return rrect(17, 11, 30, 38, 4, INK) + stroke(
        "M38 17C30 17 29 22.5 34 25C39 27.5 38.5 33 31.5 34C26 35 27 41 34 41", HOLE, 4)

@small("rsibreak")
def rsibreak_s():
    return ring_b(CX, CY + 1, 15, INK, 4) + pie_c(CX, CY + 1, 10.5, 0, 270, INK) + line(32, 31, 32, 11, INK, 4)

@small("rimworld")
def rimworld_s():
    return ring_b(CX, CY, 15.5, INK, 3.6) + poly(_star(CX, CY + 0.5, 10.5, 4.8), INK, 2.4)

@small("revolt")
def revolt_s():
    holes = "".join(circle(*pt(CX, CY, 11, a), 3.2, HOLE) for a in range(-60, 241, 50))
    return circle(CX, CY, 17, INK) + holes + circle(CX, CY, 4.5, HOLE)

@small("rhythmbox")
def rhythmbox_s():
    return rrect(16, 11, 32, 38, 5, INK) + circle(32, 32, 11, AMBER) + circle(32, 32, 4.5, HOLE)

@small("ru.linux_gaming.PortProtonQt")
def portproton_s():
    pad = path("M19 19H45A5 5 0 0 1 50 24L49 40A5 5 0 0 1 41 43L37.5 38H26.5L23 43A5 5 0 0 1 15 40L14 24"
               "A5 5 0 0 1 19 19Z", INK)
    dpad = line(20, 28.5, 29, 28.5, HOLE, 3.4) + line(24.5, 24, 24.5, 33, HOLE, 3.4)
    return pad + dpad + circle(40.5, 25.5, 2.5, HOLE) + circle(40.5, 32, 2.5, HOLE)

@small("rolled-out")
def rolled_out_s():
    return (circle(CX, CY, 17, INK) + circle(32, 33, 8, HOLE) + circle(24.5, 24, 5, HOLE)
            + circle(39.5, 24, 5, HOLE))

@small("rochard")
def rochard_s():
    return (stroke("M20 46V32A20 20 0 0 1 40 12H45V25H40A7 7 0 0 0 33 32V46Z", INK, 3.4)
            + path("M20 46V32A20 20 0 0 1 40 12H45V17H40A15 15 0 0 0 25 32V46Z", INK))

@small("rquickshare")
def rquickshare_s():
    out = ""
    for a0 in (200, 20):
        out += arc_c(CX, CY, 14, a0, a0 + 120, INK, 4) + arrowhead_d(CX, CY, 14, a0 + 120, INK, 4.5)
    return out + line(24, 30, 38, 30, INK, 4) + stroke("M33.5 24.5L39.5 30L33.5 35.5", INK, 4)
