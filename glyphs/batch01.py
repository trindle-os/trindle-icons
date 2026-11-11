# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 1: the first fifty brand glyphs."""
from lm import (
    AMBER_DARK, AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_SOFT, BLUE_LIGHT, BLUE_SOFT, BROWN, BROWN_DARK, BROWN_DEEP,
    BROWN_LIGHT, BROWN_SOFT, circle, cpath, cut, CX, CY, CYAN_DARK, CYAN_DEEP, CYAN_SOFT,
    DEEP_ORANGE, DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_ORANGE_SOFT,
    DEEP_PURPLE, DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT, g, GREY_DARK, GREY_DEEP, HOLE, INDIGO,
    INDIGO_DARK, INDIGO_DEEP, INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE, LIGHT_BLUE_DARK,
    LIGHT_BLUE_DEEP, LIGHT_BLUE_LIGHT, LIGHT_BLUE_SOFT, line, ORANGE, ORANGE_DEEP, path,
    PINK_DEEP, poly, pt, PURPLE_DARK, PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_LIGHT, RED_SOFT,
    rrect, stroke, TEAL, TEAL_DEEP,
)
from glyphs.kit import (
    _chrome, _doc, EDGE_OUTER, FIREFOX_BODY, GIMP_HEAD, registry, WHATSAPP_PHONE, WHATSAPP_RING,
)
from glyphs.kit import shared_brave, shared_discord, shared_gimp_s, shared_lo_writer, shared_steam, shared_vivaldi

ICONS, SMALL, reg, small = registry()


@reg("firefox", DEEP_ORANGE)
def firefox():
    globe = circle(32.8, 26.8, 11.2, DEEP_PURPLE)
    body = FIREFOX_BODY
    ear = poly([(18.5, 17.5), (19.5, 9.5), (25.5, 14.5)], INK, 2.5)
    tail = path("M37 13.5C42 13.8 46 17 47 21.5C44 18.5 40.5 17.5 36.5 18.5"
                "C35 16.5 35.5 14.5 37 13.5Z", INK)
    return globe + body + ear + tail


@reg("brave", DEEP_ORANGE_DEEP)
def brave():
    return shared_brave()


@reg("chromium-browser", BLUE_DEEP)
@reg("google-chrome", LIGHT_BLUE_DEEP)
def chrome():
    return _chrome()


@reg("vivaldi", RED_DEEP)
def vivaldi():
    return shared_vivaldi()


@reg("opera", RED)
def opera():
    return cut("M32 13a14 17 0 1 0 0.01 0Z" + "M32 18.5a6.5 11.5 0 1 0 0.01 0Z", INK)


@reg("microsoft-edge", CYAN_DEEP)
def edge():
    outer = EDGE_OUTER
    inner = path("M35 47C41 47 46 44.5 48 40.5C45 43 41 44 37 43.5"
                 "C31 42.5 28 39 28.5 35C27 40 29.5 45.5 35 47Z", CYAN_SOFT)
    return outer + inner


@reg("tor", DEEP_PURPLE)
def tor():
    rings = cut(cpath(CX, CY, 16) + cpath(CX, CY, 13.5), INK)
    half = cut("M32 13.5A16.5 16.5 0 0 1 32 46.5Z", INK)
    lines = (stroke("M32 18.5A11.5 11.5 0 0 1 32 41.5", HOLE, 2) +
             stroke("M32 23.5A6.5 6.5 0 0 1 32 36.5", HOLE, 2))
    return rings + half + lines


@reg("thunderbird", BLUE_DARK)
def thunderbird():
    bird = circle(33, 31, 16, INK)
    beak = poly([(13.5, 23), (20, 19.5), (20, 26)], INK, 2.5)
    crest = path("M24 15.5C27 11.5 33 10.5 38 12.5C33 12.5 29.5 14 27.5 17Z", INK)
    eye = circle(23.5, 21.5, 1.8, HOLE)
    env = rrect(22, 27, 22, 15, 3, HOLE)
    flap = stroke("M23.5 29L33 35.5L42.5 29", INK, 2)
    return bird + beak + crest + eye + env + flap


@reg("discord", INDIGO_LIGHT)
def discord():
    return shared_discord()


@reg("telegram", LIGHT_BLUE)
def telegram():
    plane = poly([(15, 29), (47, 16.5), (41.5, 44), (32, 36.5), (27, 41), (26.5, 34)], INK, 2.5)
    fold = poly([(26.5, 34), (41, 22.5), (32, 36.5)], LIGHT_BLUE_DEEP, 1)
    return plane + fold


@reg("signal-desktop", INDIGO)
def signal():
    ring = (f'<circle cx="{CX}" cy="{CY}" r="16" fill="none" stroke="{INK}" '
            'stroke-width="2.2" stroke-dasharray="3.6 2.2"/>')
    bubble = path("M32 18A12 12 0 1 1 26 40.4L20.5 42L22 36.3A12 12 0 0 1 32 18Z", INK)
    return ring + bubble


@reg("slack", PURPLE_DARK)
def slack():
    one = rrect(23.75, 13.5, 5.5, 16.5, 2.75, INK) + rrect(17.5, 24.5, 5.5, 5.5, 2.75, INK)
    return "".join(g(one, f"rotate({90 * k} 32 30)") for k in range(4))


@reg("skype", LIGHT_BLUE_LIGHT)
def skype():
    body = circle(22, 20, 7.5, INK) + circle(42, 40, 7.5, INK) + circle(CX, CY, 14.5, INK)
    s = stroke("M38 23.5C36.5 21.5 34.5 21 32 21C28.5 21 26 22.8 26 25.5"
               "C26 31 38.5 28.5 38.5 34.5C38.5 37.2 35.5 39 32 39"
               "C29 39 27 38 25.5 36", HOLE, 3.6)
    return body + s


@reg("element-desktop", TEAL)
def element():
    return "".join(g(stroke("M22.5 25A10.5 10.5 0 0 1 38 17.5", INK, 4.4),
                     f"rotate({90 * k} 32 30)") for k in range(4))


@reg("whatsapp", LIGHT_BLUE)
def whatsapp():
    ring = (WHATSAPP_RING)
    phone = WHATSAPP_PHONE
    return ring + phone


@reg("libreoffice-writer", BLUE_DEEP)
def lo_writer():
    return shared_lo_writer()


@reg("libreoffice-calc", BLUE)
def lo_calc():
    cells = "".join(rrect(22 + c * 6.6, 23 + r * 5.6, 5, 4, 1, HOLE)
                    for r in range(4) for c in range(3))
    return _doc(cells, BLUE_SOFT)


@reg("libreoffice-impress", DEEP_ORANGE_DARK)
def lo_impress():
    screen = rrect(21.5, 23, 20, 14, 2, HOLE)
    chart = stroke("M25 33.5L29.5 29L33 31.5L38 26.5", INK, 2.2)
    return _doc(screen + chart + rrect(21.5, 40, 12, 2.6, 1.3, HOLE), DEEP_ORANGE_SOFT)


@reg("notion", BLUE_GREY_DEEP)
def notion():
    return rrect(16, 13, 32, 34, 6, INK) + stroke("M24.5 39V21L39.5 39V21", HOLE, 4.2)


@reg("joplin", LIGHT_BLUE_DARK)
def joplin():
    return stroke("M36 16V32C36 39 32.5 43 27.5 43C23.5 43 21 40.5 20.5 36.5", INK, 5.5)


@reg("obsidian", DEEP_PURPLE_LIGHT)
def obsidian():
    gem = poly([(27, 12), (39, 17.5), (44, 33), (37, 47), (24, 43), (20, 31)], INK, 3)
    ridge = poly([(31, 29), (39, 17.5), (44, 33), (37, 47)], PURPLE_SOFT, 3)
    return gem + ridge


@reg("zotero", PINK_DEEP)
def zotero():
    return stroke("M20 17H44L20 43H44", INK, 5.5)


@reg("anki", INDIGO_SOFT)
def anki():
    back = g(rrect(19, 14, 24, 32, 5, INDIGO), "rotate(-10 31 30)")
    front = g(rrect(22, 14, 24, 32, 5, INK), "rotate(8 34 30)")
    pts = [pt(34, 30.5, 8.5 if k % 2 == 0 else 3.8, -90 + 36 * k) for k in range(10)]
    return back + front + poly(pts, HOLE, 2.2)


@reg("vlc", DEEP_ORANGE_LIGHT)
def vlc():
    cone = path("M29.5 13H34.5L43 42H21Z", INK, f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    bands = (path("M26.3 24H37.7L39.8 31H24.2Z", HOLE) +
             path("M23.5 35H40.5L41.6 39H22.4Z", HOLE))
    return cone + bands + rrect(15, 41, 34, 7, 3.5, INK)


@reg("gimp", BROWN_LIGHT)
def gimp():
    head = GIMP_HEAD
    eyes = (circle(26.5, 25, 5, HOLE) + circle(37.5, 25, 5, HOLE) +
            circle(28, 26, 2.2, INK) + circle(39, 26, 2.2, INK))
    brush = line(34, 38, 48, 29, BROWN_DARK, 3) + path(
        "M46.5 30L50.5 27.5L52 30.5L48.5 32Z", BROWN_DARK,
        f' stroke="{BROWN_DARK}" stroke-width="1.5" stroke-linejoin="round"')
    return head + eyes + brush


@reg("inkscape", BLUE_GREY_DARK)
def inkscape():
    mount = path("M32 12C33.5 12 34.5 12.8 35.5 14.3L48 33C49.5 35.5 48 38 45 38H19"
                 "C16 38 14.5 35.5 16 33L28.5 14.3C29.5 12.8 30.5 12 32 12Z", INK)
    snow = path("M28.3 17.5L32 12.8L35.7 17.5L37.7 20.8C36 21.5 35 23 34 25C33.3 23.5 32.6 23 31.8 23"
                "C31 23 30.3 24 29.8 27C29 23.5 28 21.5 26.3 21Z", BLUE_GREY_SOFT)
    drips = rrect(21, 40, 14, 3.6, 1.8, INK) + rrect(27, 45, 12, 3.6, 1.8, INK) + circle(41, 41.8, 1.8, INK)
    return mount + snow + drips


@reg("blender", ORANGE_DEEP)
def blender():
    arms = (path("M31 25L14 25.5A2.5 2.5 0 0 0 12.5 30L25 39Z", INK) +
            path("M33 21.5L25 15A2.3 2.3 0 0 0 21.5 17.5L27 26Z", INK))
    ring = circle(36, 32, 12, INK) + circle(36, 32, 7.5, HOLE) + circle(36, 32, 4.5, INK)
    return arms + ring


@reg("audacity", INDIGO_DEEP)
def audacity():
    band = stroke("M17.5 36V30A14.5 14.5 0 0 1 46.5 30V36", INK, 4)
    cups = rrect(13.5, 30, 8, 14, 3.5, INK) + rrect(42.5, 30, 8, 14, 3.5, INK)
    wave = stroke("M24.5 37L27 31L29.5 42L32 25L34.5 40L37 30L39.5 37", DEEP_ORANGE_SOFT, 2.6)
    return band + cups + wave


@reg("obs", GREY_DARK)
def obs():
    blobs = ""
    for k in range(3):
        a = -90 + 120 * k
        x, y = pt(CX, CY, 7.2, a)
        ix, iy = pt(x, y, 2.3, a + 150)
        blobs += circle(x, y, 5.6, HOLE) + circle(ix, iy, 3.2, INK)
    return circle(CX, CY, 16.5, INK) + blobs


@reg("sublime-text", AMBER_DARK)
def sublime():
    return (poly([(21, 21.5), (43, 15.5), (43, 22), (21, 28)], INK, 1.5) +
            poly([(21, 28), (43, 34), (43, 40.5), (21, 34.5)], INK, 1.5) +
            poly([(21, 40), (43, 34), (43, 40.5), (21, 46.5)], INK, 1.5))


@reg("vscode", LIGHT_BLUE_DEEP)
def vscode():
    x = line(40.5, 17, 18, 37, INK, 5.5) + line(40.5, 43, 18, 23, LIGHT_BLUE_SOFT, 5.5)
    bar = path("M38 12.5L46 16.5A2.5 2.5 0 0 1 47.5 18.8V41.2A2.5 2.5 0 0 1 46 43.5L38 47.5Z", INK)
    return x + bar


@reg("utilities-terminal", BLUE_GREY)
def terminal():
    return stroke("M18 20L28 29.5L18 39", INK, 5) + rrect(31, 36.5, 16, 5, 2.5, INK)


@reg("git", RED_LIGHT)
def git():
    diamond = g(rrect(17.5, 15.5, 29, 29, 6, INK), "rotate(45 32 30)")
    tree = (line(26, 24, 38.5, 36.5, HOLE, 2.8) + line(32.2, 30.2, 32.2, 38, HOLE, 2.8) +
            circle(26, 24, 3, HOLE) + circle(32.2, 38.5, 3, HOLE) + circle(38.5, 36.5, 3, HOLE))
    return diamond + tree


@reg("vim", AMBER_DARK)
def vim():
    diamond = g(rrect(18, 16, 28, 28, 5, AMBER_DEEP), "rotate(45 32 30)")
    v = path("M20 16H29V19H27.5V35L38 19H36.5V16H44L44.5 17.5L30 43H27L24 39V19H20Z", INK,
             f' stroke="{HOLE}" stroke-width="1.6" stroke-linejoin="round"')
    return diamond + v


@reg("emacs", DEEP_PURPLE_DEEP)
def emacs():
    return stroke("M41 17C33 16.5 22 18.5 22.5 21.5C23 24.5 39 23.5 38.5 28.5"
                  "C38 33 23.5 31 23.5 36.5C23.5 41.5 34 43 42 42.5", INK, 4.4)


@reg("virtualbox", INDIGO_DARK)
def virtualbox():
    top = poly([(32, 12.5), (47, 20.5), (32, 28.5), (17, 20.5)], INK, 2.5)
    left = poly([(17, 20.5), (32, 28.5), (32, 47), (17, 39)], INDIGO_SOFT, 2.5)
    right = poly([(47, 20.5), (32, 28.5), (32, 47), (47, 39)], INDIGO, 2.5)
    return top + left + right + stroke("M20.5 27L24.5 37.5L28.5 29.5", INK, 2.4)


@reg("filezilla", RED)
def filezilla():
    return (path("M19 18H29L28 22H23.5L22.6 26H27L26 30H21.7L19.5 42H15Z", INK) +
            path("M31 18H48L47 22L37 38H45.5L44.5 42H28.5L29.5 38L39.5 22H30Z", INK))


@reg("qbittorrent", BLUE_LIGHT)
def qbittorrent():
    q = (f'<circle cx="23.5" cy="32" r="5.2" fill="none" stroke="{INK}" stroke-width="3.6"/>'
         + line(28.7, 27, 28.7, 44, INK, 3.6))
    b = (f'<circle cx="40.5" cy="32" r="5.2" fill="none" stroke="{INK}" stroke-width="3.6"/>'
         + line(35.3, 16, 35.3, 37, INK, 3.6))
    return q + b


@reg("keepassxc", TEAL_DEEP)
def keepassxc():
    return (f'<circle cx="32" cy="21.5" r="6.5" fill="none" stroke="{INK}" stroke-width="4"/>'
            + line(32, 28, 32, 45, INK, 4) + line(32, 37, 37.5, 37, INK, 3.6)
            + line(32, 43, 36, 43, INK, 3.6))


@reg("bitwarden", BLUE_DARK)
def bitwarden():
    shield = path("M17 14H47V29C47 38 40 44.5 32 48C24 44.5 17 38 17 29Z", INK,
                  f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return shield + path("M32 17.5H42.5V29C42.5 35.5 37.5 40.5 32 43.5Z", HOLE)


@reg("nextcloud", BLUE)
def nextcloud():
    return "".join(f'<circle cx="{x}" cy="30" r="{r}" fill="none" stroke="{INK}" stroke-width="3.6"/>'
                   for x, r in [(19.5, 4.5), (32, 7), (44.5, 4.5)])


@reg("dropbox", BLUE_DEEP)
def dropbox():
    box = "".join(poly([(cx, cy - 5), (cx + 7, cy), (cx, cy + 5), (cx - 7, cy)], INK, 2)
                  for cx, cy in [(25, 20), (39, 20), (25, 31), (39, 31)])
    return box + poly([(32, 37.5), (39, 42.5), (32, 47), (25, 42.5)], INK, 2)


@reg("steam", INDIGO_DARK)
def steam():
    return shared_steam()


@reg("minecraft", BROWN_DEEP)
def minecraft():
    out = rrect(16, 14, 32, 32, 4, BROWN_SOFT)
    out += path("M16 18A4 4 0 0 1 20 14H44A4 4 0 0 1 48 18V24H16Z", ORANGE)
    for x, h in [(16, 4), (22, 7), (28, 3), (34, 6), (40, 4), (44, 7)]:
        out += rrect(x, 23, 4, h, 0, ORANGE)
    for x, y in [(21, 33), (33, 30), (39, 39), (26, 41)]:
        out += rrect(x, y, 4, 4, 0.8, BROWN)
    return out


@reg("retroarch", GREY_DEEP)
def retroarch():
    inv = path("M22 17H26V21H38V17H42V23H46V29H50V39H45V33H42V39H38V35H26V39H22V33H19V39H14V29H18V23H22Z", INK)
    return inv + rrect(26, 25, 4, 4, 0.5, HOLE) + rrect(34, 25, 4, 4, 0.5, HOLE)


@reg("lutris", AMBER_DEEP)
def lutris():
    ball = circle(34, 37, 11, INK)
    body = stroke("M20 26C24 20 34 19 40 21.5C44 23 46.5 25.5 47.5 28", BROWN_DEEP, 7)
    head = circle(19.5, 25, 5.2, BROWN_DEEP) + circle(17, 20.5, 1.9, BROWN_DEEP) + circle(17.2, 24.3, 1.3, INK)
    return ball + body + head


@reg("kodi", CYAN_DARK)
def kodi():
    return "".join(g(rrect(cx - 5.8, cy - 5.8, 11.6, 11.6, 2.5, c), f"rotate(45 {cx} {cy})")
                   for (cx, cy), c in [((32, 17.5), INK), ((19.5, 30), INK),
                                       ((44.5, 30), INK), ((32, 42.5), CYAN_SOFT)])


@reg("wine", RED_DARK)
def wine():
    glass = path("M24 13H40C40.7 21 38.5 28.5 32 30C25.5 28.5 23.3 21 24 13Z", INK)
    wine_ = path("M24.5 18.5H39.5C39.3 23.5 37 28 32 28.8C27 28 24.7 23.5 24.5 18.5Z", RED_SOFT)
    stem = line(32, 30, 32, 43, INK, 3) + line(25.5, 44.5, 38.5, 44.5, INK, 3.4)
    return glass + wine_ + stem


@reg("spotify-client", BLUE_LIGHT)
def spotify():
    bars = (stroke("M20.5 24.5C27.5 22 36.5 22.5 43.5 26", HOLE, 3.4) +
            stroke("M22 30.5C28 28.8 35 29.2 41 32.3", HOLE, 3) +
            stroke("M23.5 36C28.5 34.8 34 35.2 38.5 37.6", HOLE, 2.6))
    return circle(CX, CY, 16.5, INK) + bars


@small("libreoffice-writer")
def lo_writer_s():
    lines = "".join(rrect(21, y, w, 4, 2, HOLE) for y, w in [(24, 21), (32, 21), (40, 13)])
    return _doc(lines, BLUE_SOFT)


@small("libreoffice-calc")
def lo_calc_s():
    cells = "".join(rrect(21.5 + c * 11, 23 + r * 11, 9, 8.5, 1.5, HOLE)
                    for r in range(2) for c in range(2))
    return _doc(cells, BLUE_SOFT)


@small("libreoffice-impress")
def lo_impress_s():
    return _doc(rrect(21, 24, 21, 16, 2.5, HOLE) +
                stroke("M25 36L30 30.5L33.5 33L38.5 27.5", INK, 3), DEEP_ORANGE_SOFT)


@small("thunderbird")
def thunderbird_s():
    bird = circle(33, 31, 16, INK) + poly([(13.5, 23), (20, 19.5), (20, 26)], INK, 2.5)
    return bird + rrect(21, 26, 24, 17, 3.5, HOLE) + stroke("M23 28.5L33 36L43 28.5", INK, 3)


@small("gimp")
def gimp_s():
    return shared_gimp_s()


@small("audacity")
def audacity_s():
    band = stroke("M17.5 36V30A14.5 14.5 0 0 1 46.5 30V36", INK, 4)
    cups = rrect(12.5, 29, 10, 16, 4, INK) + rrect(41.5, 29, 10, 16, 4, INK)
    return band + cups + stroke("M26 37L29 29L32 40L35 29L38 37", DEEP_ORANGE_SOFT, 3.2)


@small("signal-desktop")
def signal_s():
    ring = (f'<circle cx="{CX}" cy="{CY}" r="16" fill="none" stroke="{INK}" '
            'stroke-width="2.4" stroke-dasharray="6 3.2"/>')
    return ring + path("M32 17A13 13 0 1 1 25.5 41.2L19.5 43L21.2 36.8A13 13 0 0 1 32 17Z", INK)


@small("minecraft")
def minecraft_s():
    out = rrect(15, 13, 34, 34, 4, BROWN_SOFT)
    out += path("M15 17A4 4 0 0 1 19 13H45A4 4 0 0 1 49 17V26H15Z", BLUE_SOFT)
    out += rrect(21, 26, 6, 5, 0, BLUE_SOFT) + rrect(37, 26, 6, 6, 0, BLUE_SOFT)
    return out


@small("inkscape")
def inkscape_s():
    mount = path("M32 11C33.5 11 34.5 11.8 35.5 13.3L49 34C50.5 36.5 49 39 46 39H18"
                 "C15 39 13.5 36.5 15 34L28.5 13.3C29.5 11.8 30.5 11 32 11Z", INK)
    snow = path("M27.5 18L32 12L36.5 18L38.5 22L34 25L32 23L30 25L25.5 22Z", BLUE_GREY_SOFT)
    return mount + snow + rrect(22, 42, 20, 5, 2.5, INK)
