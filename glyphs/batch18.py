# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 18: com.lettier.movie-monad to crawl."""
from lm import (
    AMBER, AMBER_DARK, AMBER_DEEP, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY,
    BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_GREY_SOFT, BLUE_LIGHT, BLUE_SOFT,
    circle, cut, CX, CY, CYAN_DEEP, CYAN_LIGHT, CYAN_SOFT, DEEP_ORANGE, DEEP_ORANGE_DEEP,
    DEEP_ORANGE_SOFT, DEEP_PURPLE, DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, g, GREY_DARK,
    GREY_DEEP, GREY_LIGHT, HOLE, INDIGO, INDIGO_LIGHT, INK, line, ORANGE, ORANGE_DEEP,
    ORANGE_LIGHT, ORANGE_SOFT, path, PINK_DARK, PINK_DEEP, PINK_SOFT, poly, PURPLE,
    PURPLE_LIGHT, PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_LIGHT, rrect, stroke, TEAL, YELLOW,
)
from glyphs.kit import arc_e, registry, ring_b, star_b

ICONS, SMALL, reg, small = registry()


@reg("com.lettier.movie-monad", DEEP_PURPLE)
def movie_monad():
    bars = rrect(13.5, 23, 11, 5, 2, INK) + rrect(13.5, 32, 11, 5, 2, INK)
    chev = (stroke("M38 20.5L29 30L38 39.5", INK, 5) +
            stroke("M48 20.5L39 30L48 39.5", PINK_SOFT, 5))
    return bars + chev


@reg("com.mitchellh.ghostty", INDIGO)
def ghostty():
    ghost = path("M16 28C16 18.5 23 12 32 12C41 12 48 18.5 48 28V45"
                 "C48 47.5 45.5 48.5 43.5 46.8L40.5 44.3L36.2 47.5C34.8 48.5 33.4 48.5 32 47.5"
                 "L27.8 44.3L23.5 47.5C22 48.5 20.5 48.5 19 47.3L16 44.8Z", INK)
    prompt = stroke("M22.5 23.5L27.5 27.5L22.5 31.5", HOLE, 3.2) + line(31.5, 27.5, 40.5, 27.5, HOLE, 3.2)
    return ghost + prompt


@reg("com.moddb.TotalChaos", RED_DARK)
def totalchaos():
    t = path("M16 13H48L49 23H46.5C45.5 18.5 43.5 17 39.5 17H35.5V41.5C35.5 43.5 36.5 44.5 40 44.8V47.5"
             "H24V44.8C27.5 44.5 28.5 43.5 28.5 41.5V17H24.5C20.5 17 18.5 18.5 17.5 23H15Z", INK)
    return t


@reg("com.naps2.Naps2", BLUE_DEEP)
def naps2():
    page = rrect(20, 12, 24, 36, 3, INK)
    beam = rrect(13, 27.5, 38, 5, 2.5, ORANGE_SOFT, f' stroke="{HOLE}" stroke-width="1.6"')
    return page + beam


def _person(x, y, s, fill, edge=None):
    extra = f' stroke="{edge}" stroke-width="1.8"' if edge else ""
    head = circle(x, y, 4.2 * s, fill, extra)
    body = path(f"M{f(x - 6 * s)} {f(y + 8.5 * s)}A{f(3 * s)} {f(3 * s)} 0 0 1 {f(x - 3 * s)} {f(y + 5.5 * s)}"
                f"H{f(x + 3 * s)}A{f(3 * s)} {f(3 * s)} 0 0 1 {f(x + 6 * s)} {f(y + 8.5 * s)}"
                f"V{f(y + 19 * s)}H{f(x + 3.2 * s)}V{f(y + 29 * s)}H{f(x - 3.2 * s)}V{f(y + 19 * s)}"
                f"H{f(x - 6 * s)}Z", fill,
                (extra + ' stroke-linejoin="round"') if edge else "")
    return body + head


@reg("com.neatdecisions.Detwinner", CYAN_DEEP)
def detwinner():
    back = g(_person(0, 0, 1, CYAN_LIGHT), "translate(24.5 13) scale(1.15 1.05)")
    front = g(_person(0, 0, 1, INK, HOLE), "translate(38.5 16.5) scale(1.15 1.05)")
    return back + front


@reg("com.rafaelmardojai.Blanket", BLUE_DEEP)
def blanket():
    cloth = rrect(15, 12, 34, 30, 4, INK)
    checks = "".join(rrect(19 + c * 6.5, 15.5 + r * 6.5, 6.5, 6.5, 0.6, BLUE_SOFT)
                     for r in range(4) for c in range(4) if (r + c) % 2 == 0)
    fringe = "".join(line(x, 42, x, 47.5, INK, 2.6) for x in (18.5, 24, 29.5, 35, 40.5, 46))
    return cloth + checks + fringe


@reg("com.rafaelmardojai.SharePreview", DEEP_PURPLE_LIGHT)
def sharepreview():
    card = rrect(13.5, 22, 33, 25, 3.5, INK)
    lines = rrect(17.5, 37, 18, 2.6, 1.3, HOLE) + rrect(17.5, 41.5, 12, 2.6, 1.3, HOLE)
    handle = line(41, 28, 48.5, 35.5, INK, 5, extra="")
    lens = (circle(35, 21.5, 11, HOLE) + circle(35, 21.5, 9.5, INK) + circle(35, 21.5, 6.5, PINK_DEEP))
    return card + lines + line(41, 28, 48.5, 35.5, HOLE, 8) + handle + lens


@reg("com.rafaelmardojai.WebfontKitGenerator", ORANGE_DEEP)
def webfontkit():
    lid = rrect(14, 20, 36, 7, 2.5, INK)
    box = rrect(16.5, 26, 31, 21, 3, INK)
    ribbon = rrect(29.5, 20, 5, 27, 0, RED_DEEP)
    bow = (path("M32 20C27 12 19.5 13 21 17.5C22 20 27 20 32 20Z", RED_DEEP) +
           path("M32 20C37 12 44.5 13 43 17.5C42 20 37 20 32 20Z", RED_DEEP))
    a1 = stroke("M19.5 43.5L23 32.5L26.5 43.5M21 39.5H25", HOLE, 2.6)
    a2 = ring_b(40.5, 39.5, 3.2, HOLE, 2.6) + line(43.7, 36, 43.7, 43.5, HOLE, 2.6)
    return lid + box + ribbon + bow + a1 + a2


@reg("com.raggesilver.BlackBox", BLUE_GREY_DARK)
def blackbox():
    s = stroke("M29 19C28 17.3 26.3 16.5 24 16.5C20.8 16.5 18.5 18.2 18.5 20.8"
               "C18.5 26.5 29.5 23.5 29.5 29.5C29.5 32.2 27 34 23.8 34C21 34 19 33 18 31", INK, 3.6)
    bar = line(24, 12.5, 24, 38, INK, 3)
    cursor = rrect(33, 37, 15, 5, 2.5, INK)
    return s + bar + cursor


@reg("com.ranfdev.Geopard", GREY_DARK)
def geopard():
    moon = circle(CX, CY, 17, INK)
    craters = (circle(26, 23, 4.5, GREY_LIGHT) + circle(37.5, 21, 3, GREY_LIGHT) +
               circle(38, 34, 5.5, GREY_LIGHT) + circle(24.5, 37, 3, GREY_LIGHT) +
               circle(44, 26.5, 1.8, GREY_LIGHT))
    return moon + craters


@reg("com.rtosta.zapzap", INDIGO_LIGHT)
def zapzap():
    bubble = path("M32 13A17 17 0 1 1 22.5 44.2L14.5 46.5L17 38.5A17 17 0 0 1 32 13Z", INK)
    z = path("M22 20.5H41.5L31 32.5H42V39.5H21.5L32 27.5H22Z", HOLE,
             f' stroke="{HOLE}" stroke-width="1.5" stroke-linejoin="round"')
    return bubble + z


@reg("com.scoutshonour.Digital", INDIGO)
def digital():
    d = cut("M14 16H29L33 20V40L29 44H14V39.5H16.5V20.5H14Z" "M22 21V39H27.5V21Z", INK)
    i = rrect(38, 16, 6.5, 6, 1, INK) + path("M36 25.5H44.5V39.5H48V44H36V39.5H38.5V30H36Z", INK)
    return d + i


@reg("com.scoutshonour.dtipbijays", BLUE_GREY)
def dtipbijays():
    cells = rrect(15, 13, 10, 10, 2.2, BLUE_LIGHT)
    for r in range(1, 3):
        for c in range(3):
            cells += rrect(15 + c * 12, 13 + r * 12, 10, 10, 2.2, INK)
    return cells


@reg("com.shatteredpixel.shatteredpixeldungeon", AMBER_DARK)
def shatteredpixel():
    chest = rrect(15, 22, 34, 25, 3, INK)
    straps = (path("M19 11.5V47H24V11.5L21.5 14Z", AMBER) +
              path("M40 11.5V47H45V11.5L42.5 14Z", AMBER))
    lock = rrect(25.5, 25, 13, 13, 2.5, AMBER) + path("M30.2 28H33.8V31.5H32.8V35H31.2V31.5H30.2Z", HOLE,
                                                          f' stroke="{HOLE}" stroke-width="1" stroke-linejoin="round"')
    return chest + straps + lock


@reg("com.steamgriddb.SGDBoop", BLUE_DARK)
def sgdboop():
    return circle(30, 32, 16, INK) + circle(34, 28, 13, BLUE_LIGHT)


@reg("com.system76.Popsicle", TEAL)
def popsicle():
    body = path("M21 22A11 11 0 0 1 43 22V38H21Z", INK)
    slots = rrect(26, 20, 4, 14, 2, HOLE) + rrect(34, 20, 4, 14, 2, HOLE)
    plug = rrect(24, 38, 16, 11, 1.5, BLUE_GREY_SOFT) + rrect(27, 42, 3.5, 3, 0.5, HOLE) + rrect(33.5, 42, 3.5, 3, 0.5, HOLE)
    return body + slots + plug


@reg("com.szibele.e-juice-calc", BLUE_GREY_DEEP)
def ejuice():
    cap = rrect(29, 11, 6, 7, 1.5, INK)
    neck = rrect(25, 17, 14, 6, 1.5, INK)
    bottle = rrect(18, 22, 28, 27, 4, INK)
    label = rrect(18, 29, 28, 9, 0, DEEP_ORANGE_DEEP)
    band = rrect(23, 25, 18, 3.2, 1, HOLE)
    return cap + neck + bottle + label + band


@reg("com.ticktick.TickTick", BLUE)
def ticktick():
    ringp = stroke(arc_e(CX, 31, 15, -40, 250), INK, 5)
    tick = stroke("M25 26.5H39M25 35.5H34", AMBER_SOFT, 5)
    return ringp + tick


@reg("com.ulduzsoft.Birdtray", BLUE_DARK)
def birdtray():
    bird = circle(31, 30, 15.5, INK)
    beak = poly([(13, 22), (19.5, 18.5), (19.5, 25)], INK, 2.5)
    crest = path("M22.5 15C25.5 11 31.5 10 36.5 12C31.5 12 28 13.5 26 16.5Z", INK)
    eye = circle(22, 21, 1.8, HOLE)
    env = rrect(20.5, 26, 20, 14, 3, HOLE) + stroke("M22 28L30.5 34L39 28", INK, 2)
    badge = circle(42, 40, 9, HOLE) + circle(42, 40, 7.5, RED)
    bell = path("M38.5 42.5C39.5 41.5 39.3 39.5 39.5 38.2C39.8 36.2 40.8 35.2 42 35.2"
                "C43.2 35.2 44.2 36.2 44.5 38.2C44.7 39.5 44.5 41.5 45.5 42.5Z", INK,
                f' stroke="{INK}" stroke-width="1" stroke-linejoin="round"') + circle(42, 44, 1.3, INK)
    return bird + beak + crest + eye + env + badge + bell


@reg("com.usebottles.bottles", RED_DEEP)
def bottles():
    left = rrect(14, 22, 11, 25, 3, INK) + rrect(17, 16, 5, 7, 1, INK)
    mid = rrect(26.5, 18, 11, 29, 3, INK) + rrect(29.5, 11.5, 5, 8, 1, INK)
    right = rrect(39, 25, 11, 22, 3, INK) + rrect(42, 19.5, 5, 6.5, 1, INK)
    gaps = line(25.75, 20, 25.75, 48, HOLE, 1.5, "butt") + line(38.25, 20, 38.25, 48, HOLE, 1.5, "butt")
    drop = path("M32 28C33.8 31 35 32.5 35 34.2A3 3 0 0 1 29 34.2C29 32.5 30.2 31 32 28Z", HOLE)
    return left + right + mid + gaps + drop


@reg("commix", RED_DEEP)
def commix():
    plunger = rrect(24, 11, 16, 3.6, 1.8, INK) + line(32, 13, 32, 19, INK, 3.2)
    body = rrect(22, 18.5, 20, 21, 3, INK)
    needle = poly([(28, 39), (36, 39), (32, 49)], INK, 2)
    mark = stroke("M27.5 34.5L32 30L36.5 34.5", HOLE, 2.8) + line(33.5, 22.5, 33.5, 25.5, HOLE, 2.6)
    return plunger + body + needle + mark


@reg("company-of-heroes-2", RED_DEEP)
def coh2():
    s = star_b(CX, 31.5, 18.5, 8.5, INK, 4)
    two = stroke("M28 27.5C28 25 29.8 23.5 32.2 23.5C34.6 23.5 36.3 25 36.3 27.2"
                 "C36.3 30.5 28.2 34 28 38.2H36.5", HOLE, 3)
    return s + two


@reg("compiz", BLUE_DEEP)
def compiz():
    arrow = poly([(19, 12), (19, 42), (26, 35.5), (31, 47.5), (37, 45), (32, 33.5), (42, 33)], INK, 3)
    return g(arrow, "translate(1.5 0)")


@reg("compton", CYAN_DEEP)
def compton():
    teeth = "".join(g(rrect(28.5, 11.5, 7, 9, 2, INK), f"rotate({45 * k} 32 30)") for k in range(8))
    body = circle(CX, CY, 14.5, INK)
    c = stroke(arc_e(CX, CY, 7.8, 45, 315), HOLE, 4.6)
    return teeth + body + c


@reg("computerjanitor", AMBER_DEEP)
def computerjanitor():
    handle = line(46.5, 12.5, 34, 29, RED_DARK, 3.6)
    band = g(rrect(28.5, 26, 10, 6, 1.5, RED_DARK), "rotate(37 33.5 29)")
    head = path("M28 28L39 36.5C37 43 30 48.5 15 49C15.5 41.5 19.5 32.5 28 28Z", INK)
    bristles = (stroke("M24 46.5L33 38", HOLE, 2.2) + stroke("M19 47L28.5 35", HOLE, 2.2))
    return handle + head + bristles + band


@reg("comsol", BLUE_DEEP)
def comsol():
    diamond = g(rrect(17, 15, 30, 30, 8, INK), "rotate(45 32 30)")
    cyl = rrect(20, 24.5, 26, 11, 5.5, HOLE)
    stripes = "".join(rrect(x, 24.5, 3, 11, 0, BLUE_SOFT) for x in (29, 35, 41))
    cap = circle(22, 30, 5.5, ORANGE) + circle(22, 30, 2.4, INK)
    return diamond + cyl + stripes + cap


@reg("confclerk", CYAN_DEEP)
def confclerk():
    cal = rrect(14, 15, 36, 33, 4, INK)
    head = path("M18 15H46A4 4 0 0 1 50 19V23H14V19A4 4 0 0 1 18 15Z", CYAN_SOFT)
    rings = circle(21, 18.5, 1.8, INK) + circle(43, 18.5, 1.8, INK)
    cells = "".join(rrect(18 + c * 7.3, 26.5 + r * 6.8, 5.5, 5, 1, HOLE)
                    for r in range(3) for c in range(4))
    return cal + head + rings + cells


@reg("conky", DEEP_PURPLE)
def conky():
    frame = stroke("M46 22.5V19.5C46 16.5 44 14.5 41 14.5H20C17 14.5 15 16.5 15 19.5V35"
                   "C15 38 17 40 20 40H41C44 40 46 38 46 35V32", INK, 4)
    bars = "".join(rrect(x, 36.5 - h, 2.6, h, 0.6, PURPLE_SOFT)
                   for x, h in [(20, 6), (23.5, 10), (27, 7), (30.5, 14), (34, 9), (37.5, 12)])
    stand = stroke("M22 48C24 44 27.5 42 32 42C36.5 42 40 44 42 48", INK, 3.6) + line(32, 40, 32, 43, INK, 3.6)
    return frame + bars + stand


def _cm():
    c = path("M13 14H28V21H24.5V18.5H20V41.5H24.5V39H28V46H13V41.5H15.5V18.5H13Z", INK,
             f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    m = path("M31 14H37L42 24.5L47 14H51V46H46V25L42 33.5L37 25V46H31Z", INK,
             f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return c + m


@reg("conky-manager", RED_DEEP)
def conky_manager():
    return _cm()


@reg("conky-manager2", RED_DEEP)
def conky_manager2():
    badge = circle(42.5, 39.5, 10.5, HOLE) + circle(42.5, 39.5, 9, ORANGE_DEEP)
    two = stroke("M38.8 36.8C38.8 34.6 40.4 33.3 42.5 33.3C44.6 33.3 46.1 34.6 46.1 36.4"
                 "C46.1 39.2 39 42 38.8 45.5H46.3", INK, 2.6)
    return _cm() + badge + two


@reg("connectagram", BLUE_GREY)
def connectagram():
    return stroke(arc_e(CX, CY, 12.5, 40, 320), INK, 7)


@reg("construo", CYAN_DEEP)
def construo():
    nodes = [(41, 13.5), (29, 15.5), (19, 23.5), (27, 25), (17, 34), (26, 36),
             (30, 44.5), (44, 44), (40, 34)]
    edges = [(0, 1), (1, 2), (1, 3), (0, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5),
             (4, 6), (5, 6), (5, 8), (6, 7), (7, 8), (6, 8)]
    lines = "".join(line(*nodes[a], *nodes[b], INK, 2.4) for a, b in edges)
    dots = "".join(circle(x, y, 3.3, RED_LIGHT) for x, y in nodes)
    return lines + dots


@reg("contact-editor", ORANGE_DEEP)
def contact_editor():
    head = circle(29, 22, 6.5, INK)
    body = path("M16 43C16 35 21.5 31.5 29 31.5C36.5 31.5 42 35 42 43Z", INK)
    badge = circle(41.5, 40, 9.5, HOLE) + circle(41.5, 40, 8, PURPLE)
    pencil = g(rrect(40, 33.5, 3.5, 11, 1, INK) + poly([(40, 44.5), (43.5, 44.5), (41.75, 47)], INK, 0.8),
               "rotate(45 41.5 40)")
    return head + body + badge + pencil


@reg("converseen", BLUE)
def converseen():
    top = stroke(arc_e(CX, 31, 13, 160, 300), INK, 4.6)
    tip1 = poly([(35, 12.5), (44, 17.5), (36, 23.5)], INK, 2)
    bot = stroke(arc_e(CX, 31, 13, 340, 480), INK, 4.6)
    tip2 = poly([(29, 49.5), (20, 44.5), (28, 38.5)], INK, 2)
    return top + tip1 + bot + tip2


@reg("convertall-icon", PURPLE)
def convertall():
    post = line(32, 15, 32, 45, INK, 3.4) + rrect(24, 44, 16, 3.6, 1.8, INK)
    beam = line(17, 19, 47, 15, INK, 3.2) + circle(32, 17, 3, INK)
    strings = (stroke("M17 19L13.5 31M17 19L20.5 31", INK, 1.8) +
               stroke("M47 15L43.5 27M47 15L50.5 27", INK, 1.8))
    pans = path("M12 31H22A5 5 0 0 1 12 31Z", INK) + path("M42 27H52A5 5 0 0 1 42 27Z", INK)
    return post + strings + beam + pans


@reg("cool-retro-term", BLUE_GREY_DARK)
def cool_retro_term():
    amber = AMBER
    c = stroke("M22 16H15.5V27H22", amber, 3.4)
    r = stroke("M25.5 27V16H31.5V21.5H25.5M29 21.5L32 27", amber, 3.4)
    t = stroke("M35.5 16H47M41.25 16V27", amber, 3.4)
    cursor = rrect(14, 32, 7, 12, 1, amber)
    return c + r + t + cursor


@reg("copyq", DEEP_PURPLE_SOFT)
def copyq():
    blades = (poly([(26, 29), (29.5, 27), (40, 48), (34, 46)], INK, 2) +
              poly([(38, 29), (34.5, 27), (24, 48), (30, 46)], INK, 2))
    rings = ring_b(22, 21, 6.5, INK, 4.2) + ring_b(42, 21, 6.5, INK, 4.2)
    pivot = circle(32, 34, 2, HOLE)
    return blades + rings + pivot


@reg("corebird", BLUE_DEEP)
def corebird():
    cap = path("M19 22A14 12 0 0 1 45 22Z", PINK_SOFT)
    head = path("M16.5 30A15.5 15.5 0 0 0 47.5 30C47.5 25 45.5 22 42.5 20.5H21.5C18.5 22 16.5 25 16.5 30Z", INK)
    eyes = circle(26, 28, 2.4, HOLE) + circle(38, 28, 2.4, HOLE)
    beak = poly([(32, 30), (37, 35.5), (32, 41), (27, 35.5)], AMBER, 2)
    return cap + head + eyes + beak


@reg("corectrl", BLUE_GREY_DARK)
def corectrl():
    pins = "".join(rrect(x, 12, 2.4, 4, 0.6, INK) + rrect(x, 44, 2.4, 4, 0.6, INK)
                   for x in (20, 25, 30, 35, 40))
    pins += "".join(rrect(12, y, 4, 2.4, 0.6, INK) + rrect(48, y, 4, 2.4, 0.6, INK)
                    for y in (19, 24, 29, 34, 39))
    chip = rrect(16, 16, 32, 28, 3.5, INK)
    s1 = line(26, 20, 26, 40, DEEP_ORANGE_DEEP, 3) + rrect(22, 30, 8, 4, 1.5, DEEP_ORANGE_DEEP)
    s2 = stroke("M42 21.5H36.5V27H42M42 33H36.5V38.5H42", ORANGE, 3)
    return pins + chip + s1 + s2


@reg("corelvector", PINK_DEEP)
def corelvector():
    disc = circle(CX, CY, 17, INK)
    swoosh = path("M39 14.5C33 22 30.5 33 33 47C38 47 42 45 45 42C42 34 41 24 43 16.3Z", HOLE)
    sliver = path("M36 14C28 18 21.5 24.5 16.5 32L16 29C20 21 27 16 36 14Z", HOLE)
    return disc + swoosh + sliver


@reg("cosmigo-pro-motion-icon", GREY_DARK)
def cosmigo():
    body = circle(CX, CY, 17, INK)
    segs = ""
    for k, c in enumerate([RED, AMBER, GREY_LIGHT, BLUE]):
        segs += stroke(arc_e(CX, CY, 11, -90 + 90 * k + 4, -90 + 90 * (k + 1) - 4), c, 4)
    lens = circle(CX, CY, 7.5, BLUE_GREY_DARK) + circle(29, 27, 2.2, INK)
    return body + segs + lens


@reg("coypu", RED_LIGHT)
def coypu():
    rat = path("M13 40C15 37 19 36.5 21 34.5C22 29 27 23.5 34 22.5C35 20 37 19.5 38.5 20.5"
               "C40.5 20.5 42 21.5 43 23C46 24 48.5 26.5 50 29C50.5 30.5 49.5 31.5 48 31.5"
               "C46 31.5 44 32 43 33.5C42.5 36.5 41 38.5 39.5 39.5L41.5 43.5H37.5L35.5 40.5"
               "C32.5 41 29 41 26.5 40.5L25 43.5H21L22.5 39.5C20 39.5 17 40.5 13 42.5Z", INK,
               f' stroke="{INK}" stroke-width="1" stroke-linejoin="round"')
    eye = circle(44, 26.5, 1.4, HOLE)
    return rat + eye


@reg("cozy", DEEP_ORANGE)
def cozy():
    page = rrect(17, 12, 30, 37, 3, DEEP_ORANGE_SOFT)
    band = stroke("M22 36V30A10 10 0 0 1 42 30V36", INK, 3.4)
    cups = rrect(19, 32, 6.5, 11, 2.5, INK) + rrect(38.5, 32, 6.5, 11, 2.5, INK)
    return page + band + cups


@reg("cozydrive", BLUE)
def cozydrive():
    cloud = path("M20 43C15.5 43 13 39.5 13 36C13 32 16 29 20 29C20 22 25.5 17 32 17"
                 "C38.5 17 43.5 21.5 44.5 27.5C48.5 28 51 31.5 51 35.5C51 39.5 48 43 44 43Z", INK)
    smile = stroke("M28 33.5C30.5 36 33.5 36 36 33.5", HOLE, 2.6)
    return cloud + smile


@reg("cpod", YELLOW)
def cpod():
    return (stroke(arc_e(CX, CY, 16, 40, 320), INK, 3.6) +
            stroke(arc_e(CX, CY, 10.5, 40, 320), INK, 3.6) +
            stroke(arc_e(CX, CY, 5, 40, 320), INK, 3.6))


@reg("cpu-x", GREY_DEEP)
def cpu_x():
    chip = cut("M17 13H47A4 4 0 0 1 51 17V43A4 4 0 0 1 47 47H17A4 4 0 0 1 13 43V17A4 4 0 0 1 17 13Z"
               "M13 25A3 3 0 0 0 13 31ZM51 25A3 3 0 0 1 51 31Z", INK)
    screen = rrect(19, 18.5, 26, 23, 3, HOLE)
    bars = rrect(23, 24, 12, 3, 1.5, INK) + rrect(23, 30, 6, 3, 1.5, INK) + rrect(31, 30, 9, 3, 1.5, INK)
    return chip + screen + bars


@reg("crab-game", BLUE_LIGHT)
def crab_game():
    body = path("M14 49C15 41.5 19 38 22.5 36.5C19.5 33.5 18.5 29 18.5 25C18.5 16.5 24.5 11 32 11"
                "C39.5 11 45.5 16.5 45.5 25C45.5 29 44.5 33.5 41.5 36.5C45 38 49 41.5 50 49Z", PINK_DEEP)
    mask = path("M24.5 25C24.5 20 27.5 17 32 17C36.5 17 39.5 20 39.5 25C39.5 31 36 35.5 32 35.5"
                "C28 35.5 24.5 31 24.5 25Z", BLUE_GREY_DARK)
    sign = ring_b(32, 24, 3.4, INK, 2.4)
    zip_ = line(32, 38, 32, 49, PINK_DARK, 2.4, "butt")
    return body + mask + sign + zip_


@reg("crack-attack", BLUE_GREY_DEEP)
def crack_attack():
    cols = [[INK, ORANGE, PURPLE_LIGHT], [PURPLE_LIGHT, INK, INK], [BLUE_GREY_LIGHT, ORANGE, BLUE_GREY_LIGHT]]
    return "".join(rrect(14 + c * 12.5, 12 + r * 12.5, 11, 11, 2, cols[r][c])
                   for r in range(3) for c in range(3))


@reg("crashplan", BLUE)
def crashplan():
    house = poly([(32, 12), (50, 28.5), (45.5, 28.5), (45.5, 47), (18.5, 47), (18.5, 28.5), (14, 28.5)], INK, 2)
    dots = "".join(circle(25.5 + c * 6.5, 31 + r * 5.5, 2, HOLE) for r in range(3) for c in range(3))
    return house + dots


@reg("crawl", BLUE_GREY_DARK)
def crawl():
    fire = path("M18 49C15 44 18 40 20 38C20.5 41 22 42 23 42C22.5 39 24 36 27 35C27 38.5 29.5 40 32 40"
                "C34.5 40 37 38.5 37 35C40 36 41.5 39 41 42C42 42 43.5 41 44 38C46 40 49 44 46 49Z", ORANGE)
    pot = path("M14 21H50C50 32 45 39 32 39C19 39 14 32 14 21Z", INK)
    rim = rrect(12, 18, 40, 5, 2.5, INK)
    ladle = stroke("M28 18V13.5C28 11.5 30 11 32 11.5L38 13", ORANGE_LIGHT, 3.6)
    return fire + ladle + rim + pot


@small("com.rafaelmardojai.WebfontKitGenerator")
def webfontkit_s():
    lid = rrect(13, 20, 38, 8, 3, INK)
    box = rrect(16, 27, 32, 21, 3, INK)
    ribbon = rrect(28.5, 20, 7, 28, 0, RED_DEEP)
    bow = (path("M32 20C27 11 18.5 12.5 20.5 17.5C21.5 20 27 20 32 20Z", RED_DEEP) +
           path("M32 20C37 11 45.5 12.5 43.5 17.5C42.5 20 37 20 32 20Z", RED_DEEP))
    return lid + box + ribbon + bow


@small("com.ulduzsoft.Birdtray")
def birdtray_s():
    bird = circle(31, 30, 15.5, INK) + poly([(13, 22), (19.5, 18.5), (19.5, 25)], INK, 2.5)
    env = rrect(20, 25, 20, 14, 3, HOLE)
    badge = circle(43, 41, 9, HOLE) + circle(43, 41, 7.5, RED)
    return bird + env + badge


@small("com.scoutshonour.Digital")
def digital_s():
    d = cut("M13 15H29L34 20V40L29 45H13Z" "M20.5 22V38H27V22Z", INK)
    i = rrect(38, 15, 8, 7, 1, INK) + rrect(38, 25, 8, 20, 1, INK)
    return d + i


@small("corectrl")
def corectrl_s():
    chip = rrect(14, 14, 36, 32, 4, INK)
    s1 = line(25, 19, 25, 41, DEEP_ORANGE_DEEP, 4) + rrect(20, 28, 10, 5, 2, DEEP_ORANGE_DEEP)
    s2 = stroke("M44 20H37V27.5H44M44 32.5H37V40H44", ORANGE, 4)
    return chip + s1 + s2


@small("construo")
def construo_s():
    nodes = [(40, 14), (22, 19), (17, 31), (24, 42), (41, 44)]
    lines = "".join(line(*nodes[k], *nodes[k + 1], INK, 3.4) for k in range(4))
    return lines + "".join(circle(x, y, 4.5, RED_LIGHT) for x, y in nodes)


@small("cool-retro-term")
def crt_s():
    amber = AMBER
    return (stroke("M26 16H15.5V29H26", amber, 4.4) + stroke("M31 29V16H40V22.5H31M36 22.5L40 29", amber, 4.4)
            + rrect(14, 34, 9, 12, 1, amber))


@small("confclerk")
def confclerk_s():
    cal = rrect(14, 14, 36, 34, 4, INK)
    head = path("M18 14H46A4 4 0 0 1 50 18V24H14V18A4 4 0 0 1 18 14Z", CYAN_SOFT)
    cells = "".join(rrect(19 + c * 10, 28 + r * 9, 7, 6, 1.2, HOLE) for r in range(2) for c in range(3))
    return cal + head + cells


@small("com.rafaelmardojai.Blanket")
def blanket_s():
    cloth = rrect(15, 12, 34, 30, 4, INK)
    checks = "".join(rrect(19 + c * 9, 16 + r * 9, 8, 8, 1, BLUE_SOFT)
                     for r in range(3) for c in range(3) if (r + c) % 2 == 0)
    fringe = "".join(line(x, 42, x, 48, INK, 3.2) for x in (19, 27, 35, 43))
    return cloth + checks + fringe


@small("cpod")
def cpod_s():
    return (stroke(arc_e(CX, CY, 15.5, 40, 320), INK, 4.6) +
            stroke(arc_e(CX, CY, 7, 40, 320), INK, 4.6))


def _cm_s():
    c = path("M13 14H27V20H21V40H27V46H13Z", INK)
    m = path("M31 14H37L41.5 24L46 14H51V46H45.5V27L41.5 35L37.5 27V46H31Z", INK)
    return c + m


@small("conky-manager")
def conky_manager_s():
    return _cm_s()


@small("conky-manager2")
def conky_manager2_s():
    return _cm_s() + circle(43, 40, 10.5, HOLE) + circle(43, 40, 9, ORANGE_DEEP)


@small("crashplan")
def crashplan_s():
    house = poly([(32, 11), (51, 28), (46, 28), (46, 48), (18, 48), (18, 28), (13, 28)], INK, 2)
    dots = "".join(circle(25 + c * 7, 31 + r * 6.5, 2.6, HOLE) for r in range(3) for c in range(3))
    return house + dots
