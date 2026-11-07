# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 44: mate-panel-separator .. miktex-console."""
from lm import *
from glyphs.kit import crescent_d, ell_c, registry, _ring, star_f

ICONS, SMALL, reg, small = registry()

@reg("mate-panel-separator", BLUE_DEEP)
def mate_panel_separator():
    bar = rrect(28.5, 12, 7, 36, 3.5, INK)
    left = stroke("M24 30H14M18.5 25.5L14 30L18.5 34.5", INK, 3.4)
    right = stroke("M40 30H50M45.5 25.5L50 30L45.5 34.5", INK, 3.4)
    return bar + left + right

@reg("mc", BLUE_DARK)
def mc():
    frame = rrect(13, 14, 38, 32, 4, INK)
    panes = rrect(16, 17, 14.5, 26, 2, HOLE) + rrect(33.5, 17, 14.5, 26, 2, HOLE)
    rows = ""
    for x in (18.5, 36):
        for y, w in [(20.5, 9.5), (25.5, 7), (30.5, 9.5), (35.5, 5.5)]:
            rows += rrect(x, y, w, 2.4, 1.2, INK)
    return frame + panes + rows

@reg("menulibre", BLUE_GREY)
def menulibre():
    bubble = path("M19 12H45A4 4 0 0 1 49 16V40A4 4 0 0 1 45 44H36L32 49L28 44H19"
                  "A4 4 0 0 1 15 40V16A4 4 0 0 1 19 12Z", INK)
    rows = ""
    for y in (18.5, 26.5, 34.5):
        rows += rrect(20, y, 5, 5, 1.2, HOLE) + rrect(28, y + 0.5, 16, 4, 2, HOLE)
    return bubble + rows

@reg("media-downloader", CYAN_DEEP)
def media_downloader():
    screen = rrect(14, 13, 36, 26, 4, INK)
    arrow = stroke("M32 17.5V30M26.5 25L32 30.5L37.5 25", HOLE, 4)
    stand = rrect(29.5, 39, 5, 5, 0, INK) + rrect(22, 43.5, 20, 4, 2, INK)
    return screen + arrow + stand + rrect(18, 34, 28, 1.8, 0.9, HOLE)

@reg("mediaget", LIGHT_BLUE_DEEP)
def mediaget():
    a0, a1 = pt(CX, CY, 14, -60), pt(CX, CY, 14, -120)
    arc = stroke(f"M{f(a0[0])} {f(a0[1])}A14 14 0 1 1 {f(a1[0])} {f(a1[1])}", INK, 4)
    arrow = path("M28 17H36V27H41.5L32 38L22.5 27H28Z", INK,
                 f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return arc + arrow

@reg("mediawriter", BLUE_DEEP)
def mediawriter():
    bubble = path("M32 11A15 15 0 1 1 32 41H17V26A15 15 0 0 1 32 11Z", INK)
    f_ = stroke("M29 36V24.5C29 21 31 19 34 19C35.5 19 36.5 19.5 37.5 20.5M25.5 27.5H35", HOLE, 3.4)
    plug = rrect(20, 41, 14, 8, 2, INK) + rrect(22.5, 44, 3, 2.4, 0.6, HOLE) + rrect(28.5, 44, 3, 2.4, 0.6, HOLE)
    return g(bubble + f_, "translate(1.5 0)") + g(plug, "translate(-0.5 0)")

@reg("microscope", ORANGE_DEEP)
def microscope():
    base = rrect(17, 42, 30, 5.5, 2.75, INK)
    arm = stroke("M26 42C19 38 18 30 22 25", INK, 4)
    tube = g(rrect(28, 10, 10, 24, 3.5, INK), "rotate(-30 33 22)")
    eye = circle(26.5, 18.5, 4.5, HOLE) + circle(26.5, 18.5, 2.2, INK)
    stage = rrect(33, 37, 12, 3.4, 1.7, INK)
    return base + arm + tube + eye + stage

@reg("metronome", BLUE_DEEP)
def metronome():
    body = poly([(24, 12), (40, 12), (48, 47), (16, 47)], INK, 3)
    notch = poly([(28.5, 12.5), (35.5, 12.5), (32, 17)], HOLE, 1)
    arm = line(29, 39, 41, 19, HOLE, 3.6)
    bob = circle(29, 39, 5, HOLE) + circle(29, 39, 2.4, INK)
    return body + notch + arm + bob

@reg("meterbridge", GREY_DARK)
def meterbridge():
    face = path("M14 38A18 18 0 0 1 50 38Z", INK,
                f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    scale = stroke("M20.5 31A13 13 0 0 1 38.5 23.5", HOLE, 2.6) + stroke("M41 25.5A13 13 0 0 1 43.5 31", RED, 2.6)
    needle = line(32, 37, 25.5, 24.5, HOLE, 3.2) + circle(32, 38, 4.5, HOLE)
    return face + scale + needle

@reg("mgba", BLUE_GREY)
def mgba():
    body = rrect(18, 11, 28, 38, 5, INK)
    screen = rrect(22, 15, 20, 14, 2, HOLE)
    dpad = rrect(21.5, 36.2, 9, 3.2, 1, HOLE) + rrect(24.4, 33.3, 3.2, 9, 1, HOLE)
    btns = "".join(circle(x, y, 1.9, HOLE) for x, y in [(36.5, 35), (41, 35), (36.5, 40), (41, 40)])
    return body + screen + dpad + btns

@reg("material-maker", LIGHT_BLUE_DEEP)
def material_maker():
    edge = _ring(CX, CY, 15.5, INK, 2.6)
    blob = path("M21 20.5C21 17.5 26 17.5 26 20.5V29C26 30.5 28 30.5 28.5 29C29.5 25.5 34.5 25.5 35.5 29"
                "C36 30.5 38 30.5 38 29V21C38 18 43 18 43 21V33C43 39.5 38 43 32 43"
                "C26 43 21 39.5 21 33Z", INK)
    return edge + blob

@reg("mathematica", RED_DEEP)
def mathematica():
    outer = poly(star_f(CX, 30.5, 10, 18.5, 12.5), INK, 2)
    inner = poly(star_f(CX, 31, 7, 11.5, 5.5), HOLE, 0.8)
    return outer + inner

@reg("matlab", DEEP_ORANGE_LIGHT)
def matlab():
    peak = path("M20.5 36L29 28.5L38 12.5C41.5 20 45.5 33 49.5 42.5C47 41 45 41 43 43.5"
                "C39.5 38.5 36 37.5 31.5 41Z", INK)
    wing = path("M14 35.5L23 30L27.5 32L21.5 38Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return peak + wing

@reg("mattermost", BLUE_DEEP)
def mattermost():
    a0, a1 = pt(CX, CY, 13.5, -62), pt(CX, CY, 13.5, -108)
    arc = stroke(f"M{f(a0[0])} {f(a0[1])}A13.5 13.5 0 1 1 {f(a1[0])} {f(a1[1])}", INK, 5.5)
    needle = circle(31.5, 31, 5, INK) + poly([(35.5, 15.5), (36.4, 31.6), (26.8, 29.5)], INK, 1.5)
    return arc + needle

@reg("maxima", INDIGO_DEEP)
def maxima():
    legs = line(21.5, 17.5, 20, 42, INK, 2.8) + line(42.5, 17.5, 44, 42, INK, 4.2)
    diag = line(22, 18, 32, 41, INK, 4.6) + line(32, 41, 42.5, 18, INK, 2.6)
    serifs = (line(15.5, 42, 24.5, 42, INK, 2.6) + line(39.5, 42, 48.5, 42, INK, 2.6) +
              line(16.5, 17.5, 22, 17.5, INK, 2.6) + line(42, 17.5, 47.5, 17.5, INK, 2.6))
    return legs + diag + serifs

@reg("maxthon-browser", LIGHT_BLUE_DEEP)
def maxthon():
    frame = path("M18 15H46A2 2 0 0 1 48 17V45H39V26H25V45H16V17A2 2 0 0 1 18 15Z", INK)
    return frame + rrect(28, 30, 8, 8, 0.8, INK)

@reg("maya", CYAN_DEEP)
def maya():
    left = poly([(15, 13), (22, 13), (22, 47), (15, 44)], CYAN_SOFT, 1.5)
    diag = poly([(15, 13), (22.5, 13), (35, 37), (31, 45)], INK, 1.5)
    right = poly([(42, 13), (49, 13), (49, 47), (42, 44)], INK, 1.5)
    rdiag = poly([(35, 37), (42, 13), (49, 13), (38, 42)], CYAN_SOFT, 1.5)
    return left + diag + rdiag + right

@reg("mcomix", BROWN_LIGHT)
def mcomix():
    ears = circle(17, 28, 6.5, INK) + circle(47, 28, 6.5, INK) + circle(17, 28, 3.2, HOLE) + circle(47, 28, 3.2, HOLE)
    head = circle(CX, 30, 15, INK)
    eyes = circle(26.5, 27, 2.8, HOLE) + circle(37.5, 27, 2.8, HOLE)
    smile = stroke("M25.5 35.5C29 39 35 39 38.5 35.5", HOLE, 2.8)
    return ears + head + eyes + smile

@reg("mcpelauncher-ui-qt", BLUE_GREY_DEEP)
def mcpelauncher():
    top = poly([(32, 12), (48, 20.5), (32, 29), (16, 20.5)], ORANGE, 1.5)
    left = poly([(16, 20.5), (32, 29), (32, 48), (16, 39.5)], GREY_LIGHT, 1.5)
    right = poly([(48, 20.5), (32, 29), (32, 48), (48, 39.5)], GREY_DEEP, 1.5)
    grass = (poly([(16, 20.5), (32, 29), (32, 34), (28, 32), (27, 35), (23, 30), (20, 32), (16, 26)], ORANGE_DEEP) +
             poly([(48, 20.5), (32, 29), (32, 34), (36, 31), (38, 34), (41, 29), (44, 30), (48, 26)], ORANGE_DARK))
    return top + left + right + grass

@reg("me.dusansimic.DynamicWallpaper", DEEP_PURPLE_LIGHT)
def dynamic_wallpaper():
    frame = rrect(13, 15, 38, 30, 4, INK)
    night = path("M36 18.5H45A2.5 2.5 0 0 1 47.5 21V39A2.5 2.5 0 0 1 45 41.5H28Z", HOLE)
    sun = circle(24, 28, 3.6, HOLE) + "".join(
        line(*pt(24, 28, 5.8, a), *pt(24, 28, 7.6, a), HOLE, 1.9) for a in range(0, 360, 45))
    moon = path(crescent_d(40, 30, 5.5, 43, 27, 4.5), INK)
    return frame + night + sun + moon

@reg("mediaconch", RED_DEEP)
def mediaconch():
    fans = (stroke("M20 31C22 22 32 17 43 19", INK, 4.2) +
            stroke("M24.5 34C26 27.5 33 24 41 25", INK, 4.2) +
            stroke("M29 37C30 33 35 30.5 40 31", INK, 4.2))
    fin = path("M44 17C48 25 49 33 50 41C47 39 45 38 43 39C44 32 44 24 41 19Z", INK)
    badge = circle(21, 40, 7.5, INK)
    q = stroke("M18.3 38C18.3 36 19.5 35 21 35C22.6 35 23.8 36 23.8 37.5C23.8 39.5 21 39.5 21 41.5", HOLE, 2.3)
    return fans + fin + badge + q + circle(21, 44.2, 1.3, HOLE)

@reg("mednafen", INDIGO_SOFT)
def mednafen():
    ant = stroke("M26 26C24 20 22 17 18 16M38 26C40 20 42 17 46 16", INK, 2.4)
    balls = circle(17.5, 15.5, 3.5, INK) + circle(46.5, 15.5, 3.5, INK)
    head = ell_c(CX, 34, 16, 12, INK)
    eyes = ell_c(24.5, 31, 5.5, 4, HOLE) + ell_c(39.5, 31, 5.5, 4, HOLE)
    mouth = path("M29.5 38.5H34.5V40A2.5 2.5 0 0 1 29.5 40Z", HOLE)
    return ant + balls + head + eyes + mouth

@reg("mednaffe", INDIGO_LIGHT)
def mednaffe():
    m = stroke("M21 43V17L32 33L43 17V43", INK, 6.5)
    serifs = rrect(15, 40, 12, 5, 2.5, INK) + rrect(37, 40, 12, 5, 2.5, INK) + rrect(15, 14.5, 8, 5, 2.5, INK) + rrect(41, 14.5, 8, 5, 2.5, INK)
    return m + serifs

@reg("mega", RED)
def mega():
    return circle(CX, CY, 17, INK) + stroke("M23 38.5V21.5L32 30.5L41 21.5V38.5", HOLE, 5)

@reg("megabasterd", RED_DEEP)
def megabasterd():
    spade = path("M32 11C39 19.5 49 24.5 49 33C49 38 45.5 41 41.5 41C38 41 35 39.5 33 37"
                 "L36.5 45.5H27.5L31 37C29 39.5 26 41 22.5 41C18.5 41 15 38 15 33C15 24.5 25 19.5 32 11Z", INK,
                 f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    m = stroke("M25.5 34.5V24.5L32 30.5L38.5 24.5V34.5", HOLE, 3.8)
    return spade + m

@reg("megaglest", ORANGE_DEEP)
def megaglest():
    humps = ell_c(24, 28, 9.5, 15, INK) + ell_c(40, 28, 9.5, 15, INK)
    holes = ell_c(24, 28, 4.5, 9, HOLE) + ell_c(40, 28, 4.5, 9, HOLE)
    base = stroke("M15 45.5C22 41.5 42 41.5 49 45.5", INK, 5.5)
    return humps + holes + stroke("M15 45.5C22 41.5 42 41.5 49 45.5", HOLE, 9) + base

@reg("megazeux", INDIGO_DEEP)
def megazeux():
    face = path("M20 13H44V16H47V42H44V46H20V42H17V16H20Z", INK)
    eyes = rrect(24, 20, 4, 7, 0, HOLE) + rrect(36, 20, 4, 7, 0, HOLE)
    mouth = path("M22 31H42V35H34.5V39H29.5V35H22Z", HOLE)
    return face + eyes + mouth

@reg("meld", BLUE_DEEP)
def meld():
    arm = stroke("M16.5 38C15 26 22 16 33 16C41 16 46.5 21 46.5 27.5C46.5 33 42.5 36.5 38 36.5"
                 "C34.5 36.5 32 34 32 31", INK, 5.5)
    return arm + g(arm.replace(f'"{INK}"', '"#FEAA2E"'), "rotate(180 32 30)")

@reg("mellowplayer", INDIGO)
def mellowplayer():
    cloud = "".join(circle(x, y, r, INK) for x, y, r in
                    [(22, 22, 7.5), (22, 38, 7.5), (35, 18.5, 7), (35, 41.5, 7), (43, 30, 8)])
    play = poly([(24, 16), (46, 30), (24, 44)], AMBER, 3)
    return cloud + play

@reg("melvor-idle", RED_DARK)
def melvor():
    return (poly([(14.5, 16), (23.5, 16), (32, 26), (32, 38), (24, 28), (24, 44), (14.5, 44)], INK, 2) +
            poly([(49.5, 16), (40.5, 16), (32, 26), (32, 38), (40, 28), (40, 44), (49.5, 44)], RED_SOFT, 2))

@reg("memento", BLUE_DEEP)
def memento():
    return path(crescent_d(31, 32, 16.5, 40.5, 22, 13), INK)

@reg("mendeley-desktop", RED_DEEP)
def mendeley():
    top = stroke("M20.5 21C26 20.5 27.5 27.5 32 27.5C36.5 27.5 38 20.5 43.5 21", INK, 7)
    lobes = circle(20.5, 20.5, 5.5, INK) + circle(43.5, 20.5, 5.5, INK)
    low = stroke("M23 38C22 31.5 27 28.5 32 28.5C37 28.5 42 31.5 41 38", INK, 7)
    feet = circle(22.5, 39, 6, INK) + circle(41.5, 39, 6, INK)
    return top + lobes + low + feet + circle(32, 23.5, 2.2, HOLE)

@reg("meow", CYAN_DEEP)
def meow():
    head = path("M17 16L25 22.5C29.5 21.5 34.5 21.5 39 22.5L47 16L47.5 29C48.5 38 41.5 43 32 43"
                "C22.5 43 15.5 38 16.5 29Z", INK,
                f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    eyes = circle(25.5, 32, 2.6, HOLE) + circle(38.5, 32, 2.6, HOLE)
    wh = (stroke("M17 36.5L11.5 35M17.5 39.5L12.5 41", INK, 2.2) +
          stroke("M47 36.5L52.5 35M46.5 39.5L51.5 41", INK, 2.2))
    return head + eyes + wh

@reg("mesen", BLUE_GREY_DEEP)
def mesen():
    top = stroke("M15.5 24C25 15 39 15 48.5 24", BLUE_SOFT, 4.2)
    low = stroke("M15.5 36.5C25 44.5 39 44.5 48.5 36.5", INK, 4.2)
    ball = circle(CX, 30, 9, INK) + line(34, 26, 36.5, 28.5, HOLE, 3)
    return top + low + ball

@reg("meshlab", GREY_DEEP)
def meshlab():
    eye = path("M13.5 31C20 22 28 19 35 19.5C42 20 47.5 24 50.5 30C45 38 38 41.5 31 41.5C24 41.5 18 38 13.5 31Z", INK)
    iris = circle(33, 30.5, 8, AMBER_DEEP) + circle(33, 30.5, 3.6, BLACK) + circle(35.5, 28, 1.5, INK)
    lash = stroke("M26 20L24 15M31.5 19L31 13.5M37 19.5L38.5 14.5M42.5 21.5L45.5 17", INK, 2.2)
    return eye + iris + lash

@reg("mess", ORANGE_DEEP)
def mess():
    return poly([(13, 44), (33, 17), (33, 33), (51, 13), (51, 33), (42, 44), (42, 31), (27, 44)], INK, 2)

@reg("metasploit", LIGHT_BLUE_DARK)
def metasploit():
    shield = path("M16 14.5C21 13 26.5 12 32 12C37.5 12 43 13 48 14.5V30C48 39 41 45 32 48.5"
                  "C23 45 16 39 16 30Z", INK)
    m = stroke("M23.5 38V20L32 29.5L40.5 20V38M32 29.5V40", HOLE, 4.2)
    return shield + m

@reg("methane", PURPLE_DEEP)
def methane():
    head = path("M18 17C21 13 26 14 27 16C30.3 15.3 33.7 15.3 37 16C38 14 43 13 46 17C49 21 48 26 46 29"
                "C46 37 40 41 32 41C24 41 18 37 18 29C16 26 15 21 18 17Z", INK)
    eyes = circle(27, 25, 2.6, HOLE) + circle(37, 25, 2.6, HOLE)
    ball = circle(35, 38, 11.5, HOLE) + circle(35, 38, 9, PURPLE_SOFT)
    dots = "".join(circle(x, y, 1.9, INK) for x, y in
                   [(35, 38), (35, 32.5), (35, 43.5), (29.5, 38), (40.5, 38)])
    return head + eyes + ball + dots

def _metro():
    m = poly([(15, 12), (24, 12), (32, 25), (40, 12), (49, 12), (49, 38), (41, 38), (41, 26),
              (32, 36), (23, 26), (23, 38), (15, 38)], INK, 2)
    scuff = circle(20, 33, 1, HOLE) + circle(44.5, 18, 0.9, HOLE) + rrect(17.5, 23, 2.4, 1.4, 0.4, HOLE)
    return m + scuff + rrect(15, 42, 34, 5.5, 2, INK)

@reg("metro-2033-redux", RED_DEEP)
def metro_2033():
    return _metro()

@reg("metro-last-light-redux", AMBER_DEEP)
def metro_last_light():
    return _metro()

@reg("mhwaveedit", CYAN_DEEP)
def mhwaveedit():
    mh = stroke("M15 27V14L21.5 21L28 14V27M34 14V27M47 14V27M34 20.5H47", INK, 3.2)
    we = stroke("M15 33L18 46L21.5 38L25 46L28 33M47 33H35V46H47M35 39.5H45", DEEP_ORANGE_SOFT, 3.2)
    return mh + we

@reg("micro", INDIGO)
def micro():
    mu = stroke("M25.5 17V31.5C25.5 36 28 38.5 31.5 38.5C35.5 38.5 38.5 35 38.5 30.5V17"
                "M38.5 30.5V35C38.5 38 40 39 42.5 38M25.5 31.5L23.5 46", INK, 4.2)
    return mu

@reg("microsoft", BLUE_GREY_DEEP)
def microsoft():
    return (rrect(15, 13, 16, 16, 1.5, RED_LIGHT) + rrect(33, 13, 16, 16, 1.5, LIGHT_BLUE_SOFT) +
            rrect(15, 31, 16, 16, 1.5, LIGHT_BLUE_LIGHT) + rrect(33, 31, 16, 16, 1.5, AMBER))

@reg("microsoft-365", BLUE_DEEP)
def microsoft_365():
    hexo = [pt(CX, 30, 17.5, -90 + 60 * k) for k in range(6)]
    outer = poly(hexo, INK, 6)
    lower = poly([hexo[1], hexo[2], hexo[3], (CX, 30)], DEEP_PURPLE_SOFT, 6)
    hole = poly([pt(CX, 31, 6, -90 + 60 * k) for k in range(6)], HOLE, 3.5)
    return outer + lower + hole

def _edge():
    outer = path("M16 31C16 20 23 13.5 32.5 13.5C42 13.5 48.5 20 48.5 27.5"
                 "C48.5 33 44 36 38.5 36C33 36 30.5 33.5 30.5 31C30.5 29 32 28 33 27.5"
                 "C28 27 23 31 23 37C23 43 29 47 35 47C28 49 16 44 16 31Z", INK)
    inner = path("M35 47C41 47 46 44.5 48 40.5C45 43 41 44 37 43.5"
                 "C31 42.5 28 39 28.5 35C27 40 29.5 45.5 35 47Z", CYAN_SOFT)
    return g(outer + inner, "translate(13 11) scale(.84) translate(-13 -11)")

def _badge(letter):
    return rrect(35, 36, 16, 13, 3.5, CYAN_SOFT, f' stroke="{HOLE}" stroke-width="2"') + letter

@reg("microsoft-edge-beta", LIGHT_BLUE_DEEP)
def edge_beta():
    b = stroke("M40 39V46H44A2 2 0 0 0 44 42.5H40M40 39H43.5A1.75 1.75 0 0 1 43.5 42.5", BLACK, 2.2)
    return _edge() + _badge(b)

@reg("microsoft-edge-dev", TEAL_DEEP)
def edge_dev():
    d = stroke("M40 39V46H42.5C44.8 46 46 44.5 46 42.5C46 40.5 44.8 39 42.5 39Z", BLACK, 2.2)
    return _edge() + _badge(d).replace(CYAN_SOFT, CYAN_SOFT)

@reg("midori", ORANGE_DEEP)
def midori():
    disc_ = circle(CX, CY, 16.5, INK)
    lower = path("M43.7 18.3A16.5 16.5 0 0 1 20.3 41.7Z", ORANGE_SOFT)
    needle = poly([(19, 43), (44.5, 17), (36, 32)], HOLE, 1.5) + poly([(44.5, 17), (36, 32), (31, 29.5)], RED, 1.5)
    return disc_ + lower + needle

@reg("midterm", AMBER_DARK)
def midterm():
    left = poly([(18, 15), (31, 27.5), (31, 36), (24.5, 29.5), (24.5, 45), (18, 41)], INK, 1.5)
    right = poly([(46, 15), (33, 27.5), (33, 36), (39.5, 29.5), (39.5, 45), (46, 41)], INK, 1.5)
    return left + right

@reg("mihomo-party", BLUE_DEEP)
def mihomo_party():
    m = poly([(17, 14), (32, 25), (47, 14), (47, 35), (41, 35), (41, 26), (32, 32), (23, 26), (23, 35), (17, 35)], INK, 2)
    nose = poly([(29.5, 38), (34.5, 38), (32, 41)], INK, 1.5)
    wh = stroke("M14 39.5L24 38.5M15 44.5L24 42.5M50 39.5L40 38.5M49 44.5L40 42.5", ORANGE_SOFT, 2.4)
    return m + nose + wh

@reg("miktex-console", INDIGO)
def miktex():
    handle = line(16.5, 31, 33, 20, INK, 5.5)
    head = path(crescent_d(38, 17, 7.5, 43, 13, 4.2), INK)
    tex = stroke("M18 35H27M22.5 35V47M30.5 37.5H36.5M30.5 37.5V48H36.5M30.5 42.7H35.5M39.5 35L47.5 47M47.5 35L39.5 47", INK, 2.8)
    return handle + head + circle(20, 28.7, 1.5, HOLE) + tex

@small("mc")
def mc_s():
    frame = rrect(13, 14, 38, 32, 4, INK)
    panes = rrect(17, 18, 13, 24, 2, HOLE) + rrect(34, 18, 13, 24, 2, HOLE)
    rows = "".join(rrect(x, y, 8, 3.5, 1.5, INK) for x in (19.5, 36.5) for y in (22, 30))
    return frame + panes + rows

@small("menulibre")
def menulibre_s():
    bubble = path("M19 12H45A4 4 0 0 1 49 16V40A4 4 0 0 1 45 44H36L32 49L28 44H19"
                  "A4 4 0 0 1 15 40V16A4 4 0 0 1 19 12Z", INK)
    rows = "".join(rrect(20, y, 24, 6, 3, HOLE) for y in (18, 31))
    return bubble + rows

@small("mhwaveedit")
def mhwaveedit_s():
    return (stroke("M17 27V14L32 24L47 14V27", INK, 4.5) +
            stroke("M17 33L22 46L32 37L42 46L47 33", DEEP_ORANGE_SOFT, 4.5))

@small("miktex-console")
def miktex_s():
    handle = line(16, 33, 33, 21, INK, 6)
    head = path(crescent_d(38, 17, 8.5, 43.5, 12.5, 4.8), INK)
    return handle + head + stroke("M33 35H47M40 35V48", INK, 4.5)

@small("microsoft-edge-beta")
def edge_beta_s():
    return _edge() + rrect(34, 35, 17, 14, 4, CYAN_SOFT, f' stroke="{HOLE}" stroke-width="2"')

@small("microsoft-edge-dev")
def edge_dev_s():
    return _edge() + rrect(34, 35, 17, 14, 4, BLUE_SOFT, f' stroke="{HOLE}" stroke-width="2"')

@small("meshlab")
def meshlab_s():
    eye = path("M12.5 31C20 21 28 18.5 35 19C42 19.5 48 24 51.5 30C45 39 38 42.5 31 42.5C24 42.5 18 39 12.5 31Z", INK)
    return eye + circle(33, 30.5, 8.5, BLUE_LIGHT) + circle(33, 30.5, 4, BLACK)

@small("me.dusansimic.DynamicWallpaper")
def dynamic_wallpaper_s():
    frame = rrect(12, 14, 40, 32, 4, INK)
    night = path("M36 18H46A2 2 0 0 1 48 20V40A2 2 0 0 1 46 42H28Z", HOLE)
    return frame + night + circle(23.5, 28, 5.5, HOLE) + path(crescent_d(40, 30, 6.5, 43.5, 26.5, 5), INK)

@small("metro-2033-redux")
def metro_2033_s():
    return poly([(15, 12), (24, 12), (32, 25), (40, 12), (49, 12), (49, 38), (41, 38), (41, 26),
                 (32, 36), (23, 26), (23, 38), (15, 38)], INK, 2) + rrect(15, 42, 34, 6, 2, INK)

SMALL["metro-last-light-redux"] = metro_2033_s

@small("mathematica")
def mathematica_s():
    return poly(star_f(CX, 30.5, 8, 19.5, 11.5), INK, 2) + circle(CX, 31, 3.5, HOLE)

@small("material-maker")
def material_maker_s():
    return g(material_maker().split("/>", 1)[1], "translate(32 30) scale(1.2) translate(-32 -30)")

@small("mediaconch")
def mediaconch_s():
    fans = (stroke("M17 36C19 24 30 17 43 18", INK, 5.5) +
            stroke("M25.5 39C27 31 33 27 41 27.5", INK, 5.5))
    fin = path("M44 16C48 25 49.5 34 50.5 43C47.5 41 45 40 43 41C44 33 44 24 41 18Z", INK)
    return fans + fin

@small("megabasterd")
def megabasterd_s():
    spade = path("M32 10C40 19 50 24.5 50 33.5C50 38.5 46 41.5 42 41.5C38.5 41.5 35 40 33 37.5"
                 "L37 46.5H27L31 37.5C29 40 25.5 41.5 22 41.5C18 41.5 14 38.5 14 33.5C14 24.5 24 19 32 10Z", INK)
    return spade + stroke("M23.5 34.5V24.5L32 31L40.5 24.5V34.5", HOLE, 4)

@small("meterbridge")
def meterbridge_s():
    face = path("M13 39A19 19 0 0 1 51 39Z", INK,
                f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return face + line(32, 37, 24, 23.5, HOLE, 4.5) + circle(32, 38.5, 5.5, HOLE)

@small("methane")
def methane_s():
    head = path("M18 17C21 13 26 14 27 16C30.3 15.3 33.7 15.3 37 16C38 14 43 13 46 17C49 21 48 26 46 29"
                "C46 37 40 41 32 41C24 41 18 37 18 29C16 26 15 21 18 17Z", INK)
    eyes = circle(26.5, 25, 3.2, HOLE) + circle(37.5, 25, 3.2, HOLE)
    return head + eyes + circle(36, 39, 11, HOLE) + circle(36, 39, 8, PURPLE_SOFT)

@small("mcomix")
def mcomix_s():
    ears = circle(16.5, 28, 6.5, INK) + circle(47.5, 28, 6.5, INK)
    head = circle(CX, 30, 15.5, INK)
    eyes = circle(26, 27, 3.4, HOLE) + circle(38, 27, 3.4, HOLE)
    return ears + head + eyes + stroke("M25 36C29 40.5 35 40.5 39 36", HOLE, 3.4)

@small("mediaget")
def mediaget_s():
    a0, a1 = pt(CX, CY, 15, -55), pt(CX, CY, 15, -125)
    arc = stroke(f"M{f(a0[0])} {f(a0[1])}A15 15 0 1 1 {f(a1[0])} {f(a1[1])}", INK, 4.5)
    return arc + path("M27.5 15H36.5V26H42.5L32 38.5L21.5 26H27.5Z", INK,
                      f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
