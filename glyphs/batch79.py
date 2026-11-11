# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 79: Flathub apps that Papirus lacks, drawn to look like each app."""
import math
from lm import (
    AMBER, AMBER_DARK, AMBER_DEEP, AMBER_LIGHT, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BROWN, BROWN_LIGHT, circle, cpath, cut, CX, CY, CYAN_DARK, CYAN_DEEP,
    DEEP_ORANGE_DARK, DEEP_PURPLE, DEEP_PURPLE_DARK, DEEP_PURPLE_LIGHT, f, g, GREY, GREY_DEEP,
    HOLE, INDIGO, INDIGO_LIGHT, INK, LIGHT_BLUE, LIGHT_BLUE_DARK, line, ORANGE_DEEP,
    ORANGE_LIGHT, path, PINK_DARK, poly, pt, PURPLE_SOFT, RED, RED_DEEP, rrect, stroke, TEAL,
)
from glyphs.kit import arc_b, ellipse, registry, ring_e

ICONS, SMALL, reg, small = registry()


@reg("com.adamcake.Bolt", BLUE_GREY_DARK)
def bolt():
    main = poly([(35, 11), (19.5, 33), (29.5, 33), (24, 49.5), (46, 24), (35.5, 24),
                 (43.5, 11)], AMBER_LIGHT, 2)
    echo = line(28.5, 12, 15.5, 30.5, AMBER_LIGHT, 2.6)
    return main + echo


@reg("org.gnome.gitlab.wwarner.Solitaire", AMBER_DARK)
def solitaire():
    sep = f' stroke="{HOLE}" stroke-width="2"'
    back = g(rrect(13.5, 15, 22, 30, 3.5, INK, sep), "rotate(-14 25 30)")
    spade = (path("M36 22.5C33.5 26.5 30 28 30 31.5C30 34 33 35 36 32.8"
                  "C39 35 42 34 42 31.5C42 28 38.5 26.5 36 22.5Z", HOLE) +
             poly([(36, 31), (33.8, 37), (38.2, 37)], HOLE, 1))
    front = g(rrect(24, 14.5, 24, 32, 3.5, INK, sep) + spade, "rotate(8 36 30.5)")
    return back + front


@reg("at.vintagestory.VintageStory", BLUE_DEEP)
def vintage_story():
    crown = "".join(circle(x, y, r, INK) for x, y, r in
                    [(22.5, 21, 4.5), (28, 16, 5.5), (36, 13.5, 5), (42.5, 18, 5),
                     (37.5, 22, 5), (30, 22.5, 4.5), (45, 24, 3.5)])
    trunk = path("M29 41C30.5 36 30 31 33.5 24.5L36 25.5C34 31 35 36 36.5 41Z", INK)
    boughs = stroke("M31.5 29L25.5 23.5M34.5 26.5L42 21.5", INK, 2.4)
    isle = path("M14.5 39.5H49.5C47 43 42.5 44 38.5 45L32 49.5L25.5 45"
                "C21.5 44 17 43 14.5 39.5Z", INK)
    return crown + trunk + boughs + isle


@reg("io.gdevelop.ide", DEEP_PURPLE)
def gdevelop():
    outer = stroke("M46.5 17H24a8.5 8.5 0 0 0-8.5 8.5v9a8.5 8.5 0 0 0 8.5 8.5H38"
                   "a8.5 8.5 0 0 0 8.5-8.5V30H33", INK, 4.2)
    inner = stroke("M46.5 24.5H25.5a2.5 2.5 0 0 0-2.5 2.5v6.5a2.5 2.5 0 0 0 2.5 2.5H38",
                   INK, 4.2)
    return outer + inner


@reg("org.zdoom.UZDoom", CYAN_DARK)
def uzdoom():
    shield = poly([(15, 12), (27, 12), (32, 18.5), (37, 12), (49, 12), (49, 34),
                   (32, 48), (15, 34)], INK, 2.5)
    u = stroke("M25 21.5V31Q25 37.5 32 37.5Q39 37.5 39 31V21.5", HOLE, 4.2)
    return shield + u


@reg("io.github.CyberTimon.RapidRAW", BLUE_GREY_DARK)
def rapidraw():
    out = circle(CX, CY, 16, INK)
    for k in range(6):
        a = -60 + 60 * k
        x0, y0 = pt(CX, CY, 8.5, a)
        dx, dy = math.cos(math.radians(a + 90)), math.sin(math.radians(a + 90))
        out += line(x0, y0, x0 + 14.5 * dx, y0 + 14.5 * dy, HOLE, 2.2)
    out += circle(CX, CY, 9, HOLE)
    r = stroke("M29 35.5V24.5H33.3a3.2 3.2 0 0 1 0 6.4H29M33 31L36 35.5", INK, 2.6)
    return out + r


@reg("com.markopejic.downloader", CYAN_DARK)
def marko_downloader():
    return ring_e(CX, CY, 16, INK, 3.2) + poly([(28, 22), (28, 38), (40.5, 30)], INK, 3.5)


@reg("page.codeberg.M23Snezhok.Vinyl", BROWN)
def vinyl():
    record = circle(38, 30, 13, INK) + ring_e(38, 30, 8.5, HOLE, 1.5) + circle(38, 30, 2, HOLE)
    sleeve = rrect(13, 16, 28, 28, 3.5, INK, f' stroke="{HOLE}" stroke-width="2"')
    bars = "".join(line(19 + 4 * k, 22.5, 19 + 4 * k, 37.5, HOLE, 2.4) for k in range(5))
    return record + sleeve + bars


@reg("io.github.amit9838.mousam", LIGHT_BLUE)
def mousam():
    sun = circle(37, 22, 8, AMBER_LIGHT)
    rays = "".join(line(*pt(37, 22, 11, a), *pt(37, 22, 13.5, a), AMBER_LIGHT, 2.4)
                   for a in (-150, -110, -70, -30, 10))
    cloud = (circle(24, 34, 7, INK) + circle(33, 30.5, 9, INK) + circle(42, 35.5, 6.5, INK) +
             rrect(17, 34, 31.5, 8, 4, INK))
    return sun + rays + cloud


@reg("jp.nonbili.noutube", BLUE_DEEP)
def noutube():
    head = (circle(23.5, 19.5, 2.6, INK) + circle(44.5, 19.5, 2.6, INK) +
            ellipse(34, 24.5, 12, 8.5, INK))
    face = (circle(29.5, 22, 1.7, HOLE) + circle(38.5, 22, 1.7, HOLE) +
            poly([(32, 26), (36, 26), (34, 28.2)], HOLE, 1.2))
    badge = rrect(14.5, 30, 22, 17, 5, RED, f' stroke="{HOLE}" stroke-width="2"')
    play = poly([(22.5, 34.5), (22.5, 42.5), (29.5, 38.5)], INK, 1.5)
    return head + face + badge + play


@reg("com.warlordsoftwares.media-downloader", RED)
def warlord_downloader():
    return rrect(14.5, 18.5, 35, 24, 5.5, INK) + poly([(28, 24), (28, 37), (38.5, 30.5)], HOLE, 2)


@reg("page.codeberg.impromptux.ytdl-gui", RED)
def ytdl_gui():
    shaft = line(32, 13, 32, 28, INK, 7, "butt")
    head = poly([(20, 26), (44, 26), (32, 39)], INK, 3)
    bar = line(20, 45, 44, 45, INK, 3.6)
    return shaft + head + bar


@reg("com.warlordsoftwares.wallpaper-app-4kwall", BROWN_LIGHT)
def fourkwall():
    four = stroke("M25 13.5L16 28H30M25.5 21V33", INK, 4.2)
    k = stroke("M35.5 13.5V33M46.5 13.5L37 23.2L46.5 33", INK, 4.2)
    fields = (stroke("M15 41Q30 33.5 49 38.5", INK, 3) +
              stroke("M19 47Q32 40.5 46.5 44.5", INK, 3))
    return four + k + fields


@reg("io.github.chidiwilliams.Buzz", RED_DEEP)
def buzz():
    return ring_e(CX, CY, 15, INK, 4.5) + circle(CX, CY, 8.5, INK)


@reg("com.indomitusgroup.indipdf", BLUE_DEEP)
def indipdf():
    page = poly([(17, 12), (35, 12), (43, 20), (43, 48), (17, 48)], INK, 3)
    fold = poly([(35, 12), (35, 20), (43, 20)], HOLE, 1.5)
    sig = stroke("M21.5 42L25 38L27 41L30.5 38.5H34", HOLE, 2.2)
    pen = (line(49, 15, 38.5, 25.5, ORANGE_LIGHT, 5.5) +
           poly([(40.5, 27.5), (36.5, 23.5), (31.5, 33)], ORANGE_LIGHT, 2))
    return page + fold + sig + pen


@reg("io.github.seinedkoda.kisel", PINK_DARK)
def kisel():
    jug = path("M17.5 18H36C38.5 24 40 29 40 35C40 43.5 35 48 28 48C21 48 16 43.5 16 35"
               "C16 29 17 24 17.5 18Z", INK)
    rim = poly([(14.5, 13), (37.5, 13), (37.5, 18.5), (17.5, 18.5)], INK, 2)
    handle = stroke("M37 17.5C44 16.5 46.5 22 42 29", INK, 3)
    sep = f' stroke="{HOLE}" stroke-width="1.6"'
    berries = "".join(circle(x, y, 5, RED, sep) for x, y in
                      [(37.5, 32), (45, 35), (39.5, 41.5)])
    leaf = ellipse(43.5, 26, 4.5, 2.2, GREY, -25)
    return jug + rim + handle + leaf + berries


@reg("io.github.flattool.Ignition", RED_DEEP)
def ignition():
    frame = rrect(14, 12, 36, 36, 7, "none",
                  f' stroke="{INK}" stroke-width="3.4"')
    button = circle(CX, CY, 11.5, INK)
    rocket = (path("M32 20.5C35.8 23.5 36.3 29.5 35 34.5H29C27.7 29.5 28.2 23.5 32 20.5Z", HOLE) +
              poly([(29, 30), (25.8, 35.5), (29, 34.5)], HOLE, 1) +
              poly([(35, 30), (38.2, 35.5), (35, 34.5)], HOLE, 1) +
              poly([(30.5, 35.5), (33.5, 35.5), (32, 38.5)], HOLE, 1))
    return frame + button + g(rocket, "rotate(45 32 30)")


@reg("io.github.alper_han.crossmacro", BLUE_GREY_DEEP)
def crossmacro():
    body = rrect(20.5, 11.5, 23, 37, 11.5, INK)
    split = line(32, 11.5, 32, 19.5, HOLE, 1.6, "butt")
    wheel = rrect(30.2, 17.5, 3.6, 7.5, 1.8, HOLE)
    return body + split + wheel


@reg("org.cubocore.CoreKeyboard", GREY_DEEP)
def corekeyboard():
    cap = rrect(13.5, 12, 37, 37, 7, INK)
    top = rrect(17.5, 15, 29, 28, 5, HOLE)
    a_big = stroke("M20.5 37.5L26.5 20.5L32.5 37.5M23 31.5H30", INK, 2.8)
    a_small = ring_e(38.3, 32.8, 4, INK, 2.6) + line(42.3, 27.5, 42.3, 37.5, INK, 2.6)
    return cap + top + a_big + a_small


@reg("net.codelogistics.clicker", TEAL)
def clicker():
    c, r, end = (29, 30), 14, -75
    loop = arc_b(*c, r, 55, 360 + end, INK, 4.2)
    ex, ey = pt(*c, r, end)
    t = math.radians(end + 90)
    tx, ty = math.cos(t), math.sin(t)
    head = poly([(ex + 7 * tx, ey + 7 * ty), (ex - 5.5 * ty, ey + 5.5 * tx),
                 (ex + 5.5 * ty, ey - 5.5 * tx)], INK, 2)
    dots = "".join(line(*pt(*c, 5.5, a), *pt(*c, 8, a), AMBER_LIGHT, 3.2)
                   for a in (135, 185, 235, 285))
    pts = [(35, 29), (35, 45.5), (39, 41.7), (42, 48), (45.2, 46.5), (42.3, 40.3), (47.5, 40)]
    return loop + head + dots + poly(pts, HOLE, 4.5) + poly(pts, INK, 1)


@reg("io.github.prateekmedia.appimagepool", BLUE_DEEP)
def appimagepool():
    shaft = line(32, 12, 32, 28, INK, 5)
    head = poly([(23, 26), (41, 26), (32, 36.5)], INK, 2.5)
    ripples = (stroke("M16.5 36A15.5 7 0 0 0 47.5 36", INK, 3) +
               stroke("M23.5 38A8.5 3.5 0 0 0 40.5 38", INK, 3))
    return shaft + head + ripples


@reg("me.iepure.devtoolbox", BLUE_DEEP)
def devtoolbox():
    handle = stroke("M25 20V16.5a2.5 2.5 0 0 1 2.5-2.5h9a2.5 2.5 0 0 1 2.5 2.5V20", INK, 3)
    box = rrect(13.5, 19.5, 37, 27, 4.5, INK)
    lid = line(13.5, 26.5, 50.5, 26.5, HOLE, 2, "butt")
    code = (stroke("M25.5 33L21.5 37L25.5 41", HOLE, 2.6) +
            stroke("M38.5 33L42.5 37L38.5 41", HOLE, 2.6) +
            line(34, 31.5, 30, 42.5, HOLE, 2.6))
    return handle + box + lid + code


@reg("dev.skynomads.Seabird", BLUE_DEEP)
def seabird():
    head = path("M20 47V26.5C20 18.5 25.5 13 32 13C38.5 13 44 18.5 44 26.5V47Z", INK)
    beak = poly([(27.5, 28), (36.5, 28), (32, 38)], AMBER, 2)
    eyes = circle(26, 24, 1.9, HOLE) + circle(38, 24, 1.9, HOLE)
    return head + beak + eyes


@reg("io.github.hakandundar34coding.system-monitoring-center", BLUE_DEEP)
def sysmon():
    lens = ring_e(29, 27, 13.5, INK, 3.6)
    handle = line(38.8, 36.8, 47.5, 45.5, INK, 5.5)
    pulse = stroke("M18.5 29.5H22.5L25 22L29 35L32.5 24.5L35 29.5H39", INK, 2.6)
    return lens + handle + pulse


@reg("io.github.nozwock.Packet", BLUE_GREY)
def packet():
    pillars = rrect(13, 12.5, 7.5, 35, 3.75, INK) + rrect(43.5, 12.5, 7.5, 35, 3.75, INK)
    studs = circle(16.75, 30, 1.6, HOLE) + circle(47.25, 30, 1.6, HOLE)
    panel = rrect(22.5, 16.5, 19, 27, 2, INK)
    bits = (line(26, 22, 26, 26, HOLE, 2.2) + ring_e(32, 24, 2, HOLE, 1.8) + line(38, 22, 38, 26, HOLE, 2.2) +
            ring_e(26, 36, 2, HOLE, 1.8) + line(32, 34, 32, 38, HOLE, 2.2) + ring_e(38, 36, 2, HOLE, 1.8))
    return pillars + studs + panel + bits


@reg("io.github.debasish_patra_1987.linuxthemestore", CYAN_DEEP)
def themestore():
    p1 = pt(32, 30, 12, -25)
    p2 = pt(32, 30, 12, -85)
    d = (f"M{f(p2[0])} {f(p2[1])}A12 12 0 1 0 {f(p1[0])} {f(p1[1])}"
         f"A7 7 0 0 1 {f(p2[0])} {f(p2[1])}Z")
    halo = ring_e(CX, CY, 16.5, INK, 2.4)
    dots = "".join(circle(x, y, 2, HOLE) for x, y in
                   [(26, 29), (30.5, 24.5), (36.5, 27.5), (28.5, 34.5)])
    return halo + path(d, INK) + dots


@reg("io.github.mfat.sshpilot", BLUE_GREY_DEEP)
def sshpilot():
    sq = (rrect(16, 14, 14.5, 14.5, 2.5, INK) + rrect(33.5, 14, 14.5, 14.5, 2.5, INK) +
          rrect(16, 31.5, 14.5, 14.5, 2.5, INK) + rrect(33.5, 31.5, 14.5, 14.5, 2.5, INK))
    dollar = (stroke("M26 18.5H21.5a2.2 2.2 0 0 0 0 4.4h2.8a2.2 2.2 0 0 1 0 4.4H19.2", HOLE, 2) +
              line(23.2, 16.5, 23.2, 26.5, HOLE, 2))
    note = rrect(37, 17.5, 7.5, 7.5, 1.2, HOLE)
    prompt = stroke("M19.5 34.5L25.5 38.75L19.5 43", HOLE, 2.4)
    hash_ = stroke("M38.5 35V43M43 35V43M36.5 37.2H45M36.5 40.8H45", HOLE, 1.9)
    return sq + dollar + note + prompt + hash_


@reg("top.akizip.akizip", BLUE_DEEP)
def akizip():
    win = rrect(13.5, 15, 37, 30, 3.5, INK)
    bar = line(13.5, 20.5, 50.5, 20.5, HOLE, 1.8, "butt")
    zip_ = line(22, 23, 22, 36, HOLE, 2.6, "butt", ' stroke-dasharray="1.6 1.4"')
    pull = rrect(19.5, 35, 5, 7, 1.8, AMBER)
    return win + bar + zip_ + pull


@reg("io.github.hkdb.Aerion", DEEP_PURPLE_LIGHT)
def aerion():
    env = rrect(22.5, 17.5, 27, 22, 4, "none", f' stroke="{INK}" stroke-width="3.4"')
    flap = stroke("M24.5 21L36 29.5L47.5 21", INK, 3.4)
    speed = (line(15.5, 21, 18, 21, INK, 3.4) + line(13, 28.5, 18, 28.5, INK, 3.4) +
             line(15.5, 36, 18, 36, INK, 3.4))
    return env + flap + speed


@reg("com.tomjwatson.Emote", AMBER_DEEP)
def emote():
    sun = circle(CX, CY, 16, INK)
    bands = (stroke("M16.5 31.5Q32 21.5 47.5 31.5", HOLE, 2.2) +
             stroke("M19 40Q32 31 45 40", HOLE, 2.2))
    return sun + bands


@reg("io.github.totoshko88.RustConn", DEEP_ORANGE_DARK)
def rustconn():
    teeth = "".join(g(rrect(29.25, 12, 5.5, 6, 1.2, INK), f"rotate({36 * k} 32 30)") for k in range(10))
    gear = cut(cpath(CX, CY, 15) + cpath(CX, CY, 11), INK)
    twig = stroke("M24 37Q28 31 33.5 28", INK, 2.4)
    leaf = path("M27 32C23 30.5 22.5 26 24.5 22.5C28 24 29.5 28 27 32Z", INK)
    berries = "".join(circle(x, y, 3, INK) for x, y in [(36, 24.5), (40, 30), (34.5, 31.5)])
    return teeth + gear + twig + leaf + berries


@reg("com.github.jkotra.eovpn", ORANGE_DEEP)
def eovpn():
    ring_ = arc_b(CX, 28, 14, 125, 55, INK, 5.5)
    hole = circle(CX, 26, 5, INK) + poly([(29.5, 28), (34.5, 28), (36, 44), (28, 44)], INK, 2)
    return ring_ + hole


@reg("app.comaps.comaps", LIGHT_BLUE_DARK)
def comaps():
    c = arc_b(CX, CY, 14.5, 60, 300, INK, 5)
    side = arc_b(CX, CY, 14.5, -32, 32, INK, 5)
    nav = poly([(24.5, 24), (39, 28.5), (33, 31), (30.5, 37)], INK, 2.5)
    return c + side + nav


@reg("com.github.marhkb.Pods", BLUE_GREY_DEEP)
def pods():
    box = rrect(16.5, 11.5, 31, 37, 3.5, INK)
    lid = line(16.5, 18.5, 47.5, 18.5, HOLE, 2, "butt")
    shutter = "".join(line(20, y, 44, y, HOLE, 1.8, "butt") for y in (22.5, 26, 29.5))
    shelf = line(20, 33.5, 44, 33.5, HOLE, 1.8, "butt")
    crates = rrect(20, 36.5, 11, 9, 1.5, HOLE) + rrect(33, 36.5, 11, 9, 1.5, HOLE)
    return box + lid + shutter + shelf + crates


@reg("app.fluxer.Fluxer", INDIGO)
def fluxer():
    w1 = stroke("M15.5 25.5C20.5 19 26 19 32 25.5S43.5 32 48.5 25.5", INK, 4.6)
    w2 = stroke("M15.5 35.5C20.5 29 26 29 32 35.5S43.5 42 48.5 35.5", INK, 4.6)
    return w1 + w2


@reg("io.github.shonebinu.Brief", INDIGO_LIGHT)
def brief():
    tl = stroke("M15 14H25M20 14V27.5M28.5 14V27.5H36.5", INK, 3.6)
    semi = circle(42, 17, 2, INK) + line(42, 23.5, 40.5, 28, INK, 3)
    d = stroke("M17 33V46.5H20.5a6.75 6.75 0 0 0 0-13.5Z", INK, 3.6)
    r = stroke("M32 46.5V33H37a4 4 0 0 1 0 8H32M37 41L41.5 46.5", INK, 3.6)
    return tl + semi + d + r


@reg("xyz.ketok.Speedtest", DEEP_PURPLE_DARK)
def speedtest():
    dial = arc_b(CX, 31, 16, 135, 45, INK, 3)
    ticks = "".join(line(*pt(CX, 31, 10, a), *pt(CX, 31, 12, a), INK, 2.2)
                    for a in (150, 195, 240, 285, 330))
    needle = line(CX, 31, *pt(CX, 31, 12.5, 30), PURPLE_SOFT, 3.6)
    hub = circle(CX, 31, 3.6, INK)
    return dial + ticks + needle + hub


@reg("io.appflowy.AppFlowy", DEEP_PURPLE)
def appflowy():
    return (ellipse(23.5, 20, 9, 5.5, INK, 50) + ellipse(41, 20.5, 9, 5.5, INK, 40) +
            ellipse(22.5, 39.5, 9, 5.5, INK, 40) + ellipse(40.5, 40, 9, 5.5, INK, -40))


@small("io.github.CyberTimon.RapidRAW")
def rapidraw_s():
    out = circle(CX, CY, 16, INK)
    for k in range(6):
        a = -60 + 60 * k
        x0, y0 = pt(CX, CY, 7.5, a)
        dx, dy = math.cos(math.radians(a + 90)), math.sin(math.radians(a + 90))
        out += line(x0, y0, x0 + 14 * dx, y0 + 14 * dy, HOLE, 2.6)
    return out + circle(CX, CY, 7.5, HOLE)


@small("io.github.nozwock.Packet")
def packet_s():
    pillars = rrect(13, 12.5, 8, 35, 4, INK) + rrect(43, 12.5, 8, 35, 4, INK)
    panel = rrect(23.5, 17, 17, 26, 2, INK)
    bits = line(28, 23, 36, 23, HOLE, 3) + line(28, 30, 36, 30, HOLE, 3) + line(28, 37, 36, 37, HOLE, 3)
    return pillars + panel + bits


@small("io.github.totoshko88.RustConn")
def rustconn_s():
    teeth = "".join(g(rrect(28.5, 12, 7, 6, 1.5, INK), f"rotate({45 * k} 32 30)") for k in range(8))
    gear = cut(cpath(CX, CY, 15) + cpath(CX, CY, 10), INK)
    berries = circle(28.5, 28, 3.2, INK) + circle(35.5, 28, 3.2, INK) + circle(32, 34, 3.2, INK)
    return teeth + gear + berries


@small("com.github.marhkb.Pods")
def pods_s():
    box = rrect(16.5, 11.5, 31, 37, 3.5, INK)
    shutter = line(20, 21, 44, 21, HOLE, 2.6, "butt") + line(20, 27, 44, 27, HOLE, 2.6, "butt")
    crates = rrect(20, 34, 11, 11, 1.5, HOLE) + rrect(33, 34, 11, 11, 1.5, HOLE)
    return box + shutter + crates


@small("io.github.shonebinu.Brief")
def brief_s():
    return stroke("M14 17H28M21 17V43M35 17V43H49", INK, 5)


@small("io.github.mfat.sshpilot")
def sshpilot_s():
    sq = (rrect(14, 12, 17, 17, 3, INK) + rrect(33, 12, 17, 17, 3, INK) +
          rrect(14, 31, 17, 17, 3, INK) + rrect(33, 31, 17, 17, 3, INK))
    return (sq + stroke("M18.5 34L25.5 39.5L18.5 45", HOLE, 3.2) +
            stroke("M38.5 34.5V44.5M44.5 34.5V44.5M36 37.5H47M36 41.5H47", HOLE, 2.4))


@small("xyz.ketok.Speedtest")
def speedtest_s():
    dial = arc_b(CX, 31, 16, 135, 45, INK, 3.4)
    needle = line(CX, 31, *pt(CX, 31, 12.5, 30), PURPLE_SOFT, 4.4)
    return dial + needle + circle(CX, 31, 4.2, INK)


@small("io.github.debasish_patra_1987.linuxthemestore")
def themestore_s():
    p1 = pt(32, 30, 16, -25)
    p2 = pt(32, 30, 16, -85)
    d = (f"M{f(p2[0])} {f(p2[1])}A16 16 0 1 0 {f(p1[0])} {f(p1[1])}"
         f"A9 9 0 0 1 {f(p2[0])} {f(p2[1])}Z")
    return path(d, INK) + circle(25.5, 29, 3, HOLE) + circle(33.5, 26, 3, HOLE) + circle(29, 36, 3, HOLE)


@small("app.comaps.comaps")
def comaps_s():
    return (arc_b(CX, CY, 15, 65, 295, INK, 5.5) +
            poly([(22.5, 23), (41, 28.5), (33.5, 31.5), (30.5, 39)], INK, 3))


@small("org.cubocore.CoreKeyboard")
def corekeyboard_s():
    cap = rrect(13.5, 12, 37, 37, 7, INK) + rrect(18, 15.5, 28, 27, 5, HOLE)
    return cap + stroke("M23.5 38L32 19.5L40.5 38M26.5 32H37.5", INK, 3.4)


@small("page.codeberg.M23Snezhok.Vinyl")
def vinyl_s():
    record = circle(38, 30, 13, INK)
    sleeve = rrect(13, 16, 28, 28, 3.5, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    bars = "".join(line(20 + 7 * k, 22.5, 20 + 7 * k, 37.5, HOLE, 3.2) for k in range(3))
    return record + sleeve + bars


@small("org.gnome.gitlab.wwarner.Solitaire")
def solitaire_s():
    card = rrect(19, 12, 26, 36, 4, INK)
    spade = (path("M32 19.5C28.5 25 24 27 24 31C24 34.5 28 35.5 32 32.5"
                  "C36 35.5 40 34.5 40 31C40 27 35.5 25 32 19.5Z", HOLE) +
             poly([(32, 31), (29, 39), (35, 39)], HOLE, 1))
    return card + spade


@small("com.warlordsoftwares.wallpaper-app-4kwall")
def fourkwall_s():
    return (stroke("M25 16L15.5 32H30M25.5 24V38", INK, 4.6) +
            stroke("M36 16V38M48 16L38 27L48 38", INK, 4.6))


@small("jp.nonbili.noutube")
def noutube_s():
    head = (circle(22.5, 17, 3, INK) + circle(45.5, 17, 3, INK) + ellipse(34, 22.5, 13, 9.5, INK))
    badge = rrect(13, 29, 26, 20, 5.5, RED, f' stroke="{HOLE}" stroke-width="2.4"')
    return head + badge + poly([(22.5, 34), (22.5, 44), (31, 39)], INK, 1.5)


@small("me.iepure.devtoolbox")
def devtoolbox_s():
    handle = stroke("M25 20V15.5h14V20", INK, 3.4)
    box = rrect(13.5, 19.5, 37, 28, 4.5, INK)
    code = stroke("M27 29L21.5 34L27 39", HOLE, 3.2) + stroke("M37 29L42.5 34L37 39", HOLE, 3.2)
    return handle + box + code


@small("io.github.hakandundar34coding.system-monitoring-center")
def sysmon_s():
    return (ring_e(29, 27, 13.5, INK, 3.6) + line(38.8, 36.8, 47.5, 45.5, INK, 6) +
            stroke("M19 30H23L26.5 21L31 34L34.5 26H38.5", INK, 3))


@small("com.indomitusgroup.indipdf")
def indipdf_s():
    page = poly([(16, 12), (35, 12), (43, 20), (43, 48), (16, 48)], INK, 3)
    pen = (line(49, 15, 38.5, 25.5, ORANGE_LIGHT, 6.5) +
           poly([(41, 28), (36, 23), (30, 35)], ORANGE_LIGHT, 2.5))
    return page + pen


@small("io.github.flattool.Ignition")
def ignition_s():
    return (rrect(13.5, 11.5, 37, 37, 7.5, "none", f' stroke="{INK}" stroke-width="3.6"') +
            circle(CX, CY, 11.5, INK))


@small("net.codelogistics.clicker")
def clicker_s():
    c, r, end = (29, 30), 14, -75
    loop = arc_b(*c, r, 55, 360 + end, INK, 4.6)
    ex, ey = pt(*c, r, end)
    t = math.radians(end + 90)
    tx, ty = math.cos(t), math.sin(t)
    head = poly([(ex + 7.5 * tx, ey + 7.5 * ty), (ex - 6 * ty, ey + 6 * tx),
                 (ex + 6 * ty, ey - 6 * tx)], INK, 2)
    pts = [(33, 26), (33, 45.5), (38, 41), (41.5, 48), (45, 46.5), (41.8, 39.5), (48, 39)]
    return loop + head + poly(pts, HOLE, 5) + poly(pts, INK, 1)
