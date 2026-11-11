# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 17: elementary, GitHub and GitLab apps (outliner to gwe).

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import (
    AMBER, AMBER_DEEP, AMBER_LIGHT, BLUE, BLUE_DEEP, BLUE_GREY_DARK, BLUE_GREY_DEEP,
    BLUE_GREY_SOFT, BLUE_SOFT, BROWN, circle, CX, CY, CYAN_DARK, CYAN_DEEP, DEEP_ORANGE,
    DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, g,
    GREY_DARK, GREY_DEEP, GREY_SOFT, HOLE, INDIGO, INDIGO_DEEP, INK, LIGHT_BLUE_DEEP, line,
    ORANGE, ORANGE_DEEP, ORANGE_LIGHT, path, PINK_LIGHT, poly, pt, PURPLE, PURPLE_DEEP,
    PURPLE_SOFT, RED, RED_DEEP, RED_LIGHT, RED_SOFT, rrect, stroke,
)
from glyphs.kit import arc, registry, ring_b, wedge_b

ICONS, SMALL, reg, small = registry()


@reg("com.github.phase1geo.outliner", BLUE_GREY_DEEP)
def outliner():
    bullets = (rrect(15, 14.5, 7, 7, 1.5, INK) + circle(18.5, 30, 3.8, INK) +
               poly([(15.5, 41), (22, 44.5), (15.5, 48)], INK, 1.5))
    lines = "".join(rrect(26.5, y - 1.6, 22, 3.2, 1.6, INK) for y in (18, 30, 44.5))
    return g(bullets + lines, "translate(0 -1.2)")


@reg("com.github.philip-scott.notes-up", BLUE_DEEP)
def notes_up():
    book = rrect(17, 12, 30, 36, 4, INK)
    spine = rrect(22, 12, 2.6, 36, 0, HOLE)
    mark = poly([(35, 12), (42, 12), (42, 25), (38.5, 22), (35, 25)], ORANGE_LIGHT, 1)
    return book + spine + mark


@reg("com.github.thejambi.dayjournal", BLUE_DEEP)
def dayjournal():
    body = rrect(16, 12, 29, 36, 4.5, INK)
    stitch = rrect(19.5, 15.5, 22, 29, 2.5, "none",
                   f' stroke="{HOLE}" stroke-width="2.2" stroke-dasharray="3 2.4"')
    clasp = rrect(38, 25, 11, 9, 3, HOLE) + circle(43.5, 29.5, 2, INK)
    return body + stitch + clasp


@reg("com.github.thejambi.psnotes", BLUE_DEEP)
def psnotes():
    pad = rrect(16, 15, 32, 33, 5, INK)
    rings = "".join(rrect(x - 1.5, 11, 3, 7, 1.5, INK) for x in (22, 28, 34, 40))
    bar = rrect(16, 19.5, 32, 2.2, 0, HOLE)
    p = stroke("M21.5 42V28H25.5A3.8 3.8 0 0 1 25.5 35.6H21.5", HOLE, 3)
    s = stroke("M38.5 29C37.8 28.2 36.8 27.8 35.5 27.8C33.5 27.8 32.2 29 32.2 30.8"
               "C32.2 34.5 38.8 33.5 38.8 37.8C38.8 39.8 37.3 41.2 35.3 41.2"
               "C33.8 41.2 32.6 40.6 31.8 39.6", HOLE, 3)
    dots = circle(28.3, 41, 1.7, HOLE) + circle(42.5, 41, 1.7, HOLE)
    return pad + rings + bar + p + s + dots


@reg("com.lakoliu.Furtherance", BLUE_DEEP)
def furtherance():
    case = rrect(13.5, 14, 37, 32, 5.5, INK)
    screen = rrect(17.5, 18, 29, 16, 3, HOLE)
    three = stroke("M21 22.5H25V30H21M21.5 26.2H25", INK, 2.2)
    two = stroke("M34 22.5H38V26.2H34V30H38", INK, 2.2)
    five = stroke("M44 22.5H40.5V26.2H44V30H40.5", INK, 2.2)
    colon = circle(29.5, 24, 1.2, INK) + circle(29.5, 28.5, 1.2, INK)
    knobs = circle(20.5, 40, 2.2, HOLE) + circle(26.5, 40, 2.2, HOLE)
    return case + screen + three + colon + g(two, "translate(-2.5 0)") + g(five, "translate(-1.8 0)") + knobs


@reg("com.github.rickybas.date-countdown", BLUE_DEEP)
def date_countdown():
    return circle(CX, CY, 11.5, INK) + stroke(arc(CX, CY, 16.5, -90, 190), INK, 3.6)


@reg("com.github.sgpthomas.hourglass", BLUE_DEEP)
def hourglass():
    caps = rrect(17, 11.5, 30, 4.5, 2.25, INK) + rrect(17, 44, 30, 4.5, 2.25, INK)
    glass = path("M20.5 16H43.5C43.5 23 38 27 34.5 30C38 33 43.5 37 43.5 44H20.5"
                 "C20.5 37 26 33 29.5 30C26 27 20.5 23 20.5 16Z", INK)
    sand = (path("M25 20H39C38 23.5 35 25.5 32 27.5C29 25.5 26 23.5 25 20Z", AMBER_LIGHT) +
            path("M32 35C28 36.5 25.5 38.5 24.5 41H39.5C38.5 38.5 36 36.5 32 35Z", AMBER_LIGHT))
    return caps + glass + sand


@reg("com.github.subhadeepjasu.pebbles", BLUE_DEEP)
def pebbles():
    tiles = "".join(rrect(x, y, 15.5, 15.5, 3.5, INK) for x in (15, 33.5) for y in (13, 31.5))
    check = stroke("M19 17.5L26 24.5M26 17.5L19 24.5", HOLE, 2.8)
    minus = stroke("M37 20.75H45.5", HOLE, 2.8)
    plus = stroke("M18.5 39.25H27M22.75 35V43.5", HOLE, 2.8)
    eq = stroke("M37 36.8H45.5M37 41.7H45.5", HOLE, 2.8)
    return tiles + check + minus + plus + eq


@reg("com.github.zelikos.rannum", DEEP_PURPLE)
def rannum():
    die = rrect(15, 13, 34, 34, 7, INK)
    pips = circle(22.5, 39.5, 3.6, HOLE) + circle(32, 30, 3.6, HOLE) + circle(41.5, 20.5, 3.6, HOLE)
    return die + pips


@reg("com.github.stsdc.monitor", BLUE_GREY_DARK)
def monitor():
    return stroke("M13.5 31H23L27 31L31 17L35.5 43.5L39.5 31H50.5", INK, 3.8)


@reg("com.gitlab.miridyan.Mt", BLUE_GREY_DARK)
def mt():
    s = stroke("M29 20.5C28 19 26.3 18.3 24.3 18.3C21.3 18.3 19.3 20 19.3 22.5"
               "C19.3 28 29.3 26.5 29.3 32.5C29.3 35.2 27 37 24 37"
               "C21.8 37 20 36.2 18.8 34.5", INK, 3.4)
    bar = stroke("M24.2 14.5V41", INK, 3)
    under = stroke("M34.5 41H46", INK, 3.8)
    return s + bar + under


@reg("com.github.plugarut.pwned-checker", BLUE_GREY_DEEP)
def pwned_checker():
    tick = stroke("M17.5 17V23.5", INK, 3.6)
    dot = circle(24.5, 30, 2.6, INK)
    semi = circle(24.5, 38.5, 2.6, INK) + stroke("M26 39L24 44.5", INK, 2.8)
    dashes = stroke("M31.5 36.5H38.5M42.5 36.5H48.5", INK, 3.6)
    return g(tick + dot + semi + dashes, "translate(0 -1.5)")


@reg("com.github.philip-scott.spice-up", BLUE)
def spice_up():
    bar = rrect(13.5, 13, 37, 5.5, 2.5, INK)
    board = rrect(16.5, 19.5, 31, 27, 4, INK)
    play = poly([(28.5, 26), (38.5, 33), (28.5, 40)], HOLE, 2.5)
    return bar + board + play


@reg("com.github.philip-scott.wallpaperize", PURPLE)
def wallpaperize():
    frame = rrect(14, 15, 36, 30, 5, INK)
    sun = path("M18 45V37A8 8 0 0 1 26 45Z", HOLE)
    trunk = stroke("M37 42C36.5 35 37 29 38.5 24", HOLE, 2.6)
    fronds = (stroke("M38.5 24C35 21 31 21.5 29 24", HOLE, 2.6) +
              stroke("M38.5 24C39.5 20.5 42.5 19 45.5 19.5", HOLE, 2.6) +
              stroke("M38.5 24C42.5 23.5 45 25.5 45.8 28.5", HOLE, 2.6) +
              stroke("M38.5 24C37.5 20.5 35 18.5 32 18.5", HOLE, 2.6))
    return frame + sun + trunk + fronds


@reg("com.github.rafostar.Clapper", INDIGO)
def clapper():
    top = g(rrect(15, 15, 34, 7, 2, INK) +
            "".join(poly([(x, 15), (x + 4, 15), (x + 1, 22), (x - 3, 22)], HOLE) for x in (21, 30, 39)),
            "rotate(-12 15 22)")
    body = rrect(15, 24.5, 34, 22, 3.5, INK)
    play = poly([(28.5, 29.5), (37.5, 35.5), (28.5, 41.5)], HOLE, 2.2)
    return top + body + play


@reg("com.github.robertsanseries.karim", RED)
def karim():
    tri = poly([(18, 13), (48, 30), (18, 47)], INK, 6)
    arrow = stroke("M27.5 20.5V36M21.5 31L27.5 37L33.5 31", HOLE, 4)
    return tri + arrow


@reg("com.github.unrud.VideoDownloader", DEEP_ORANGE_DEEP)
def video_downloader():
    film = rrect(14, 13, 36, 34, 4, INK)
    holes = "".join(rrect(x, y, 3.2, 3, .8, HOLE) for x in (16, 44.8) for y in (16.5, 23, 29.5, 36, 42.5))
    arrow = stroke("M32 19V38M25 31.5L32 38.5L39 31.5", HOLE, 4)
    return film + holes + arrow


@reg("com.github.weclaw1.ImageRoll", ORANGE_DEEP)
def image_roll():
    strip = rrect(13, 19, 18, 20, 2.5, INK)
    sprockets = "".join(rrect(x, 21, 2.6, 3, .6, HOLE) for x in (15.5, 20, 24.5))
    can = rrect(27, 16, 22, 32, 4, INK) + rrect(34, 11.5, 8, 5.5, 1.5, INK)
    crop = stroke("M33 24H43V36M31 28H33V38H45", HOLE, 2.6)
    return strip + sprockets + can + rrect(27, 16, 2.4, 32, 0, HOLE) + crop


@reg("com.github.torikulhabib.mindi", DEEP_ORANGE)
def mindi():
    spiral = (stroke(arc(29, 31, 15, 140, 400), INK, 3) +
              stroke(arc(29, 31, 9.5, 100, 380), INK, 3) +
              circle(29, 31, 3.8, INK))
    arrowhead = poly([(15, 25.5), (14, 16), (22.5, 20)], INK, 1.5)
    note = (circle(38, 42, 5, INK) + stroke("M42.3 42V14", INK, 3) +
            stroke("M42.3 14.5C44.5 18.5 49 19.5 48 26.5", INK, 3))
    notecut = circle(38, 42, 7, HOLE) + circle(42.3, 28, 3.2, HOLE)
    return spiral + arrowhead + notecut + note


@reg("com.github.torikulhabib.nino", DEEP_PURPLE_LIGHT)
def nino():
    down = stroke("M21 13V33M14.5 27L21 34L27.5 27", INK, 4.2)
    up = stroke("M36 35V13M29.5 19L36 12.5L42.5 19", INK, 4.2)
    globe = (circle(40.5, 38.5, 9.5, HOLE) + circle(40.5, 38.5, 7.8, INK) +
             ring_b(40.5, 38.5, 3.2, HOLE, 2, '') + stroke("M33 38.5H48", HOLE, 1.8))
    return down + up + globe


@reg("com.github.sixpounder.GameOfLife", INDIGO_DEEP)
def game_of_life():
    return "".join(rrect(x, y, 15, 15, 3, c) for x, y, c in
                   [(15, 13, INK), (34, 13, PURPLE_SOFT), (15, 32, INK), (34, 32, INK)])


@reg("com.inventwithpython.flippy", BLUE_DEEP)
def flippy():
    dark = {(2, 1), (0, 2), (1, 2)}
    return "".join(ring_b(20 + 12 * c, 18 + 12 * r, 3.8, INK, 2.4) if (c, r) in dark
                   else circle(20 + 12 * c, 18 + 12 * r, 5, INK)
                   for r in range(3) for c in range(3))


@reg("com.github.plugarut.wingpanel-monitor", GREY_DARK)
def wingpanel_monitor():
    fan = circle(32, 23, 11.5, INK)
    blades = "".join(g(path("M32 23C31 18.5 32.5 15 36 14.5C37 17.5 35.5 21 32 23Z", HOLE),
                       f"rotate({90 * k} 32 23)") for k in range(4))
    hub = circle(32, 23, 2.4, INK)
    bars = "".join(rrect(x, 49 - h, 5.2, h, 1.2, INK) for x, h in
                   [(18, 6), (25.2, 9), (32.4, 5), (39.6, 10)])
    return fan + blades + hub + bars


@reg("com.github.qarmin.czkawka", PURPLE_DEEP)
def czkawka():
    back = path("M15 17H31V44H15Z", PURPLE_SOFT,
                f' stroke="{PURPLE_SOFT}" stroke-width="3" stroke-linejoin="round"')
    front = path("M29 12H41L49 20V44H29Z", INK,
                 f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    fold = path("M41 12V20H49Z", HOLE)
    lines = "".join(rrect(32, y, 13, 2.4, 1.2, HOLE) for y in (24, 29, 34))
    blines = "".join(rrect(18, y, 9, 2.4, 1.2, PURPLE_DEEP) for y in (22, 27, 32, 37))
    return back + blines + front + fold + lines


@reg("com.github.rkoesters.xkcd-gtk", GREY_DARK)
def xkcd():
    disc_ = circle(CX, CY, 16.5, INK)
    brim = stroke("M14 38L50 26", HOLE, 2.6)
    hat = poly([(22, 31), (36, 26.5), (34.8, 21.5), (21, 26)], HOLE, 1.5)
    return disc_ + brim + hat


@reg("com.github.ronnydo.wammer", RED_DEEP)
def wammer():
    waves = (stroke(arc(32, 28, 7, 135, 225), INK, 3.2) + stroke(arc(32, 28, 7, -45, 45), INK, 3.2) +
             stroke(arc(32, 28, 13, 135, 225), INK, 3.2) + stroke(arc(32, 28, 13, -45, 45), INK, 3.2))
    return waves + circle(32, 28, 4, INK) + stroke("M32 30V47", INK, 3.6)


@reg("com.github.ryonakano.konbucase", AMBER_DEEP)
def konbucase():
    big_a = stroke("M14.5 33L22 13.5L29.5 33M17.3 26H26.7", INK, 3.8)
    small_a = (ring_b(40.5, 40.5, 4.8, INK, 3.2) + stroke("M45.3 34.5V47", INK, 3.2))
    arr1 = stroke("M36 15.5C41 15 44 18 43.5 22.5", INK, 2.6) + poly([(40.5, 21.5), (46.5, 21.5), (43.5, 26)], INK, 1)
    arr2 = stroke("M28 44.5C23 45 20 42 20.5 37.5", INK, 2.6) + poly([(17.5, 38.5), (23.5, 38.5), (20.5, 34)], INK, 1)
    return big_a + small_a + arr1 + arr2


@reg("com.github.ryonakano.louper", GREY_DEEP)
def louper():
    bar = rrect(12.5, 24, 39, 12, 4, GREY_SOFT)
    lens = circle(CX, CY, 15, INK)
    wen = (stroke("M32 19.5V21.5M24 24.5H40", HOLE, 2.6) +
           stroke("M27 25.5C29 32 33 37 40 40.5M37 25.5C35 32 31 37 24 40.5", HOLE, 2.6))
    return bar + lens + wen


@reg("com.github.sdv43.whaler", BLUE_DEEP)
def whaler():
    body = path("M14 30C14 26 17 24.5 20.5 26C23 23 30 20.5 37 21.5C45 22.5 50 29 50 35.5"
                "C50 41.5 45.5 45 39 45H25C18 45 14 38 14 30Z", INK)
    tail = path("M20.5 26C16.5 21 16 16 16.8 12.8C19 15.2 21.5 16.8 24 17"
                "C25.5 15 28 13.8 31.5 13.8C29.5 16.2 26.8 18.5 23.5 21.5Z", INK)
    eye = circle(41, 32.5, 1.9, HOLE)
    mouth = stroke("M33 39.5C37 40.5 41 40.5 45 39", HOLE, 2.2)
    return body + tail + eye + mouth


@reg("com.github.spheras.desktopfolder", BLUE_DEEP)
def desktopfolder():
    screen = rrect(13, 13, 38, 27, 4, INK)
    panels = (rrect(17, 17, 11, 19, 2.5, HOLE) + rrect(31, 17, 16, 8.5, 2.5, HOLE) +
              rrect(31, 27.5, 16, 8.5, 2.5, HOLE))
    stand = rrect(25, 41.5, 14, 6, 2, INK)
    return screen + panels + stand


@reg("com.github.subhadeepjasu.enigma", BROWN)
def enigma():
    return (stroke("M42 14.5H28.5L21 30L28.5 45.5H42", INK, 5.5) +
            stroke("M21 30H37.5", INK, 5.5))


@reg("com.github.taiko2k.avvie", DEEP_PURPLE)
def avvie():
    sq = rrect(18.5, 16.5, 27, 27, 3, INK)
    corners = (stroke("M40.5 12.5H49.5V21.5", INK, 3.2) + stroke("M23.5 47.5H14.5V38.5", INK, 3.2))
    return sq + corners


@reg("com.github.tchx84.Flatseal", BLUE_GREY_DEEP)
def flatseal():
    roll = circle(30, 28, 15, INK)
    core = circle(30, 28, 6.8, BLUE_GREY_SOFT) + circle(30, 28, 4.6, HOLE)
    tape = poly([(35, 42), (50, 42), (48, 45.5), (50, 49), (30, 49), (30, 42.5)], INK, 1.5)
    return tape + roll + core


@reg("com.github.themix_project.Oomox", BLUE_GREY_DARK)
def oomox():
    cols = [RED, PURPLE, BLUE, DEEP_PURPLE_SOFT, AMBER, ORANGE]
    wheel = "".join(path(wedge_b(CX, CY, 11.5, 17.5, -150 + 60 * k, -90 + 60 * k), c)
                    for k, c in enumerate(cols))
    blob = path("M21.5 29C21.5 23 26 19.5 32 19.5H40.5V29C40.5 35 36.5 40 30.5 40"
                "C25 40 21.5 35 21.5 29Z", INK)
    return wheel + blob + circle(35, 25, 2.4, BLUE)


@reg("com.github.tkashkin.boiler", ORANGE_DEEP)
def boiler():
    jug = path("M20 15H38L37 19.5C37.5 24 39 28 39 33V44A3 3 0 0 1 36 47H21A3 3 0 0 1 18 44V33"
               "C18 28 19.5 24 20 19.5C18 18.5 17.5 16 20 15Z", INK)
    handle = stroke("M38.5 21.5H43.5A2.5 2.5 0 0 1 46 24V34.5A2.5 2.5 0 0 1 43.5 37H39", INK, 3.6)
    return jug + handle


@reg("com.github.tkashkin.gamehub", DEEP_PURPLE_LIGHT)
def gamehub():
    pad = path("M22 19H42C47 19 50 23 50.5 29L51.2 38C51.5 42 47.5 44 44.5 41L39.5 36H24.5"
               "L19.5 41C16.5 44 12.5 42 12.8 38L13.5 29C14 23 17 19 22 19Z", INK)
    dpad = stroke("M19.5 28H26.5M23 24.5V31.5", HOLE, 2.6)
    btns = "".join(circle(x, y, 1.9, HOLE) for x, y in [(41, 24.5), (41, 31.5), (37.5, 28), (44.5, 28)])
    return pad + dpad + btns + circle(32, 25, 2.2, HOLE)


@reg("com.github.treagod.spectator", ORANGE_DEEP)
def spectator():
    return (path("M13.5 30C13.5 23 22 18 32 18C42 18 50.5 23 50.5 30C50.5 37 42 42 32 42"
                 "C22 42 13.5 37 13.5 30Z" + "M20 30C20 34 25.5 36.5 32 36.5C38.5 36.5 44 34 44 30"
                 "C44 26 38.5 23.5 32 23.5C25.5 23.5 20 26 20 30Z", INK, ' fill-rule="evenodd"') +
            path("M25.5 30C25.5 28 28.5 26.8 32 26.8C35.5 26.8 38.5 28 38.5 30"
                 "C38.5 32 35.5 33.2 32 33.2C28.5 33.2 25.5 32 25.5 30Z", INK))


@reg("com.github.unrud.RemoteTouchpad", GREY_DARK)
def remote_touchpad():
    dev = rrect(12.5, 15, 39, 30, 5, INK)
    pad = rrect(17.5, 18.5, 27, 23, 3, HOLE)
    btns = rrect(20, 34.5, 10, 5, 1.5, INK) + rrect(32, 34.5, 10, 5, 1.5, INK)
    side = rrect(47, 24, 2, 12, 1, HOLE)
    return dev + pad + btns + side


@reg("com.github.zocker_160.SyncThingy", LIGHT_BLUE_DEEP)
def syncthingy():
    c = (CX, CY)
    nodes = [pt(32, 30, 14.5, a) for a in (-40, 170, 60)]
    hub = (29.5, 31.5)
    out = ring_b(32, 30, 14.5, INK, 3)
    out += "".join(line(hub[0], hub[1], x, y, INK, 2.6) for x, y in nodes)
    out += "".join(circle(x, y, 3.6, INK) for x, y in nodes)
    return out + circle(*hub, 4, INK)


@reg("com.gitlab.bitseater.meteo", DEEP_PURPLE_LIGHT)
def meteo():
    body = stroke("M32 15V35", INK, 10) + circle(32, 39, 8.5, INK)
    merc = stroke("M32 20.5V36", BLUE_SOFT, 3.4) + circle(32, 39, 4.8, BLUE_SOFT)
    return body + merc


@reg("com.gitlab.cunidev.Gestures", LIGHT_BLUE_DEEP)
def gestures():
    screen = rrect(13.5, 13, 37, 22, 3.5, INK)
    arrow = (stroke("M26 29L38 19", HOLE, 3) + stroke("M32 19H38V25", HOLE, 3) +
             stroke("M26 23V29H32", HOLE, 3))
    btns = rrect(13.5, 38, 17.5, 9, 2.5, INK) + rrect(33, 38, 17.5, 9, 2.5, INK)
    return screen + arrow + btns


@reg("com.gitlab.newsflash", ORANGE_DEEP)
def newsflash():
    return poly([(35.5, 12), (22, 33), (31, 33), (27, 48), (42, 26), (33, 26), (37.5, 12)], INK, 2.5)


@reg("com.gitlab.nvlgit.Balss", BLUE_DEEP)
def balss():
    book = rrect(16, 12, 32, 36, 4, INK)
    spine = rrect(21, 12, 2.6, 36, 0, HOLE)
    play = poly([(29.5, 21.5), (41, 30), (29.5, 38.5)], HOLE, 2.5)
    return book + spine + play


@reg("com.gluonhq.SceneBuilder", DEEP_ORANGE_LIGHT)
def scene_builder():
    hand = (stroke("M17 20L29 30", INK, 5.2) + stroke("M22 15L32 27", INK, 5.2) +
            stroke("M29.5 13.5L36.5 25.5", INK, 5.2) + stroke("M37.5 15L41.5 25", INK, 5.2) +
            stroke("M19 37L25 39", INK, 5.2) +
            path("M26 27C30 22.5 38 22 42.5 25.5C47.5 29.5 48 37 44 42C40 47 32 47.5 27.5 44"
                 "C23.5 41 22 36 23.5 32Z", INK))
    return g(hand, "translate(-1 1)")


@reg("com.hunterwittenborn.Celeste", BLUE_DEEP)
def celeste():
    cloud = path("M20 44A8 8 0 0 1 18.5 28.2A10 10 0 0 1 31 20.5A11 11 0 0 1 48.2 30.5"
                 "A7 7 0 0 1 45 44Z", INK)
    arrows = (stroke(arc(32.5, 34.5, 6.5, 200, 330), HOLE, 2.8) +
              stroke(arc(32.5, 34.5, 6.5, 20, 150), HOLE, 2.8) +
              poly([(38, 26), (39.5, 32.5), (33.5, 31)], HOLE, 1) +
              poly([(27, 43), (25.5, 36.5), (31.5, 38)], HOLE, 1))
    return g(cloud + arrows, "translate(0 -2.5)")


@reg("com.jonathankang.Weibird", BLUE_DEEP)
def weibird():
    body = poly([(32, 12), (48, 45), (16, 45)], INK, 8)
    eyes = (circle(27.5, 30, 4.2, HOLE) + circle(36.5, 30, 4.2, HOLE) +
            circle(28.3, 30.5, 1.8, INK) + circle(35.7, 30.5, 1.8, INK))
    beak = poly([(28, 37.5), (36, 37.5), (32, 45)], AMBER, 1.5)
    return body + eyes + beak


@reg("com.katawa_shoujo.KatawaShoujo", PINK_LIGHT)
def katawa_shoujo():
    heart = path("M32 47C24 40 14 33 14 23.5C14 17.5 18.5 13 24 13C27.5 13 30.5 15 32 18"
                 "C33.5 15 36.5 13 40 13C45.5 13 50 17.5 50 23.5C50 33 40 40 32 47Z", INK)
    plaster = g(rrect(32, 29.5, 17, 7, 3.5, RED_SOFT) + rrect(38, 29.5, 5, 7, 0, RED_LIGHT),
                "rotate(-40 40.5 33)")
    return heart + plaster


@reg("com.krillbite.ThePlan", CYAN_DARK)
def the_plan():
    stem = rrect(18.5, 13, 7, 36, 2, INK)
    bowl = path("M22 13H33A12 12 0 0 1 33 37H22Z", INK)
    fig = (circle(34.5, 20.5, 2.4, HOLE) + stroke("M34.5 23.5V29.5M30.5 25.5L38.5 25.5M34.5 29.5L31.5 33.5M34.5 29.5L37.5 33.5", HOLE, 2.2))
    return stem + bowl + fig


def _gwe_eye(w):
    outer = arc(32, 39.2, 20.2, -152.9, -27.1) + arc(32, 20.8, 20.2, 27.1, 152.9)
    inner = arc(32, 37.83, 14.33, -146.9, -33.1) + arc(32, 22.17, 14.33, 33.1, 146.9)
    r_outer = arc(32, 39.2, 20.2, -90, -27.1) + arc(32, 20.8, 20.2, 27.1, 90)
    r_inner = arc(32, 37.83, 14.33, -90, -33.1) + arc(32, 22.17, 14.33, 33.1, 90)
    return (stroke(outer + inner, INK, w) + circle(27, 30, 3.8, INK) +
            rrect(32, 13, 18, 34, 3, INK) +
            stroke(r_outer + r_inner, HOLE, w))


@reg("com.leinardi.gwe", CYAN_DEEP)
def gwe():
    return _gwe_eye(3)


@reg("com.github.rajkumaar23.badgie", AMBER_DEEP)
def badgie():
    ribbons = (poly([(25, 33), (21, 47), (26, 44.5), (29, 48), (31, 35)], INK, 1.5) +
               poly([(39, 33), (43, 47), (38, 44.5), (35, 48), (33, 35)], INK, 1.5))
    pts = [pt(32, 25, 14 if k % 2 == 0 else 12.3, -90 + 15 * k) for k in range(24)]
    rosette = poly(pts, INK, 1.5)
    return ribbons + rosette + circle(32, 25, 9.5, HOLE) + circle(32, 25, 7.2, INK)


@small("com.lakoliu.Furtherance")
def furtherance_s():
    case = rrect(13, 14, 38, 32, 5.5, INK)
    screen = rrect(17, 18, 30, 17, 3, HOLE)
    colon = circle(32, 23.5, 2, INK) + circle(32, 29.5, 2, INK)
    return case + screen + colon + circle(21, 40.5, 2.5, HOLE)


@small("com.github.thejambi.psnotes")
def psnotes_s():
    pad = rrect(16, 15, 32, 33, 5, INK)
    rings = "".join(rrect(x - 2, 10.5, 4, 8, 2, INK) for x in (23, 32, 41))
    p = stroke("M24 42V26H29A4.5 4.5 0 0 1 29 35H24", HOLE, 4)
    dot = circle(38, 41, 2.8, HOLE)
    return pad + rings + p + dot


@small("com.github.thejambi.dayjournal")
def dayjournal_s():
    return rrect(16, 12, 29, 36, 4.5, INK) + rrect(37, 24.5, 12, 10, 3, HOLE) + circle(43, 29.5, 2.4, INK)


@small("com.github.plugarut.wingpanel-monitor")
def wingpanel_monitor_s():
    fan = circle(32, 22, 11, INK)
    blades = "".join(g(path("M32 22L35 12.5C38 14 39.5 17 39 20Z", HOLE), f"rotate({90 * k} 32 22)")
                     for k in range(4))
    bars = "".join(rrect(x, 48 - h, 7, h, 1.5, INK) for x, h in [(17, 7), (28.5, 10), (40, 5)])
    return fan + blades + bars


@small("com.github.ryonakano.louper")
def louper_s():
    bar = rrect(12, 24, 40, 12, 4, GREY_SOFT)
    lens = circle(CX, CY, 15, INK)
    wen = stroke("M24 23H40M27 24C29 32 33 37 40 41M37 24C35 32 31 37 24 41", HOLE, 3.2)
    return bar + lens + wen


@small("com.github.ryonakano.konbucase")
def konbucase_s():
    big_a = stroke("M13.5 34L22 13L30.5 34M17 27H27", INK, 4.4)
    small_a = ring_b(40.5, 40, 5, INK, 3.6) + stroke("M45.5 34V47", INK, 3.6)
    return big_a + small_a


@small("com.github.torikulhabib.nino")
def nino_s():
    down = stroke("M21 13V33M14.5 27L21 34L27.5 27", INK, 4.6)
    up = stroke("M36 35V13M29.5 19L36 12.5L42.5 19", INK, 4.6)
    return down + up + circle(40.5, 38.5, 10, HOLE) + circle(40.5, 38.5, 8, INK)


@small("com.github.torikulhabib.mindi")
def mindi_s():
    spiral = stroke(arc(29, 31, 14, 140, 400), INK, 4) + circle(29, 31, 5, INK)
    note = circle(38, 42, 5.5, INK) + stroke("M42.5 42V14C45 18 49 19.5 48 26", INK, 3.6)
    return spiral + circle(38, 42, 7.5, HOLE) + circle(42.5, 28, 3.6, HOLE) + note


@small("com.leinardi.gwe")
def gwe_s():
    return _gwe_eye(3.4)


@small("com.github.qarmin.czkawka")
def czkawka_s():
    back = rrect(13.5, 16, 19, 30, 3, PURPLE_SOFT)
    front = rrect(27.5, 12, 23, 34, 3, INK)
    lines = "".join(rrect(31, y, 16, 3.5, 1.75, HOLE) for y in (19, 26, 33))
    return back + front + lines


@small("com.github.rajkumaar23.badgie")
def badgie_s():
    ribbons = (poly([(24, 32), (20, 47), (31, 36)], INK, 3) + poly([(40, 32), (44, 47), (33, 36)], INK, 3))
    return ribbons + circle(32, 25, 13, INK) + ring_b(32, 25, 7.5, HOLE, 3)


@small("com.github.ronnydo.wammer")
def wammer_s():
    waves = (stroke(arc(32, 27, 9, 135, 225), INK, 4) + stroke(arc(32, 27, 9, -45, 45), INK, 4) +
             stroke(arc(32, 27, 16, 140, 220), INK, 4) + stroke(arc(32, 27, 16, -40, 40), INK, 4))
    return waves + circle(32, 27, 4.5, INK) + stroke("M32 30V47", INK, 4)


@small("com.github.subhadeepjasu.pebbles")
def pebbles_s():
    tiles = "".join(rrect(x, y, 16, 16, 3.5, INK) for x in (15, 33) for y in (12.5, 31.5))
    plus = stroke("M18.5 39.5H27.5M23 35V44", HOLE, 3.6)
    eq = stroke("M36.5 36.8H45.5M36.5 42.2H45.5", HOLE, 3.4)
    minus = stroke("M36.5 20.5H45.5", HOLE, 3.6)
    return tiles + plus + eq + minus


@small("com.inventwithpython.flippy")
def flippy_s():
    return (circle(23, 21, 7, INK) + circle(41, 39, 7, INK) +
            ring_b(41, 21, 5.5, INK, 3) + ring_b(23, 39, 5.5, INK, 3))


@small("com.github.philip-scott.wallpaperize")
def wallpaperize_s():
    frame = rrect(13, 14, 38, 32, 5, INK)
    sun = path("M17 46V36A10 10 0 0 1 27 46Z", HOLE)
    palm = (stroke("M38 43V25", HOLE, 3.4) + stroke("M29 25C32 20 44 20 47 25", HOLE, 3.4))
    return frame + sun + palm


@small("com.jonathankang.Weibird")
def weibird_s():
    body = poly([(32, 11), (48.5, 45), (15.5, 45)], INK, 8)
    eyes = circle(27, 31, 4.6, HOLE) + circle(37, 31, 4.6, HOLE)
    return body + eyes + poly([(28, 39), (36, 39), (32, 45)], AMBER, 2)


@small("com.gitlab.cunidev.Gestures")
def gestures_s():
    screen = rrect(13, 12, 38, 24, 3.5, INK)
    arrow = stroke("M25 30L39 18M31 18H39V26", HOLE, 3.6)
    btns = rrect(13, 39, 18, 9, 2.5, INK) + rrect(33, 39, 18, 9, 2.5, INK)
    return screen + arrow + btns
