# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 75: xine to yuzu.

Each tile takes the palette step nearest the app's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import *
from glyphs.kit import badge_f, registry, _ring

ICONS, SMALL, reg, small = registry()

def play(cx, cy, s, colour, rounding=2.5):
    return poly([(cx - s * .45, cy - s * .55), (cx - s * .45, cy + s * .55),
                 (cx + s * .6, cy)], colour, rounding)

@reg("xine", INDIGO_LIGHT)
def xine():
    tri = poly([(24, 14.5), (24, 35.5), (42.5, 25)], INK, 3.5)
    bar = rrect(15, 42, 34, 3.6, 1.8, INK) + circle(37, 43.8, 4.4, INK) + circle(37, 43.8, 1.8, HOLE)
    return tri + bar

@reg("xiphos", RED_DARK)
def xiphos():
    book = rrect(16, 12, 32, 36, 4, INK) + line(21, 13, 21, 47, HOLE, 2.2)
    cross = rrect(31, 17, 5.5, 26, 1.5, HOLE) + rrect(24.5, 23, 18.5, 5.5, 1.5, HOLE)
    return book + cross

@reg("xmind", RED_DEEP)
def xmind():
    return (stroke("M16 20C24 18 28 24 32 30C36 36 40 42 48 40", INK, 6)
            + stroke("M16 40C24 42 28 36 32 30C36 24 40 18 48 20", INK, 6))

@reg("xmlcopyeditor", BROWN_LIGHT)
def xmlcopyeditor():
    sq = rrect(15, 13, 34, 34, 5, INK)
    pent = [pt(32, 31, 7.5, -90 + 72 * k) for k in range(5)]
    corners = [(32, 13), (49, 22), (44, 47), (20, 47), (15, 22)]
    cuts = "".join(line(p[0], p[1], c[0], c[1], HOLE, 2.2) for p, c in zip(pent, corners))
    return sq + cuts + poly(pent, HOLE, 3) + poly(pent, INK, 0)

@reg("xmoto", AMBER_DEEP)
def xmoto():
    helmet = path("M15.5 33C15.5 21 23.5 13.5 34 13.5C43.5 13.5 49 21 49 30.5"
                  "C49 39 44 45.5 36 46.5H24C19 46.5 15.5 42 15.5 37Z", INK)
    visor = path("M15.5 27H33C35.5 27 37 28.5 37 31V33C37 35.5 35.5 37 33 37H15.5Z", AMBER_DARK)
    return helmet + visor + circle(40, 21, 2, AMBER_DARK)

def _xn_eye(inner):
    out = ""
    for a in (-150, -120, -90, -60, -30):
        x1, y1 = pt(32, 32, 11, a)
        x2, y2 = pt(32, 32, 17.5, a)
        out += line(x1, y1, x2, y2, INK, 4)
    out += path("M13.5 32Q21 23 32 20.5Q43 23 50.5 32Q43 41 32 43.5Q21 41 13.5 32Z", INK,
                f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return out + circle(32, 32, 12, INK) + inner

@reg("xnconvert", DEEP_ORANGE)
def xnconvert():
    return _xn_eye(circle(32, 32, 8.5, HOLE) + stroke("M35.5 28.5A5 5 0 1 0 35.5 35.5", INK, 3))

@reg("xnview", ORANGE_DEEP)
def xnview():
    return _xn_eye(circle(32, 32, 8.5, HOLE) + circle(32, 32, 5, ORANGE_DARK))

@reg("xneur", DEEP_ORANGE_DEEP)
def xneur():
    return (poly([(16, 15), (24, 15), (32, 30), (24, 45), (16, 45), (24, 30)], INK, 2.5)
            + poly([(48, 15), (40, 15), (32, 30), (40, 45), (48, 45), (40, 30)], INK, 2.5))

@reg("xnoise", PURPLE_LIGHT)
def xnoise():
    return (stroke("M17 15C29 15 35 45 47 45", INK, 3.2)
            + stroke("M17 45C29 45 35 15 47 15", INK, 3.2))

@reg("xnretro", GREY_DARK)
def xnretro():
    donut = cut(cpath(31, 31, 15.5) + cpath(31, 31, 6.2), INK)
    blades = "".join(g(stroke("M31 24.8C36 21 41 21 45.5 24.5", HOLE, 2.2), f"rotate({120 * k} 31 31)")
                     for k in range(3))
    return donut + blades + circle(46, 15, 3, INK)

@reg("xnsketch", DEEP_ORANGE_LIGHT)
def xnsketch():
    disc_ = circle(29, 33, 13.5, INK) + circle(29, 33, 5.5, DEEP_ORANGE_DARK)
    swirl = stroke("M20 37A10 10 0 0 0 38 35", HOLE, 2.2)
    pencil = (line(33, 29, 45.5, 16.5, HOLE, 9) + line(33.5, 28.5, 45.5, 16.5, DEEP_ORANGE_DARK, 5.5)
              + poly([(30, 32.5), (32.5, 26), (37, 30.5)], DEEP_ORANGE_DARK, 1.5))
    return disc_ + swirl + pencil

@reg("xonotic", RED_DEEP)
def xonotic():
    arc = stroke("M22 45A16.5 16.5 0 1 1 42.5 45", INK, 3)
    head = path("M17.5 32.5L21.5 25C24 21.5 28 19.5 33 19L40 13L39.5 19L46 16.5L43.5 22L48.5 22.5"
                "L44 27.5C44.5 33 42 38 38.5 41L35.5 46.5L32.5 40C30 38 28.5 35.5 28.5 32.5"
                "C26.5 31.5 24.5 31.5 22.5 33L21 36Z", INK)
    return arc + head + circle(29.5, 24.5, 1.8, HOLE)

@reg("xonsh", GREY_DEEP)
def xonsh():
    shell = path("M28.5 11.5L33 17.5C40.5 19.5 47 26 47 34C47 40.5 43 45 38 47"
                 "L36 42.5C34 46 30 48.5 26.5 48C22 41 20 32 21.5 24C22.5 19 25 15 28.5 11.5Z", INK)
    spire = stroke("M25.5 18.5L32 20M23 24.5L35 24", HOLE, 2.2)
    lip = stroke("M37 29C41 32.5 42 38.5 38.5 43", HOLE, 2.4)
    return shell + spire + lip

@reg("xorg", BLUE_GREY_DEEP)
def xorg():
    return line(18, 16, 46, 44, INK, 8.5) + line(46, 16, 18, 44, INK, 8.5)

@reg("xournal", BLUE_GREY_DEEP)
def xournal():
    sheet = rrect(14, 12, 30, 36, 3.5, INK)
    lines = "".join(line(19, y, 38, y, HOLE, 2.2) for y in (18, 23))
    x = stroke("M20 30.5C22.5 29.5 24 31 25 35C26 39.5 27.5 42 31 40.5", HOLE, 2.6) + \
        stroke("M30 31C27 32 24.5 37 21 41", HOLE, 2.6)
    pencil = (line(36, 38, 49, 16, HOLE, 8.5) + line(36.5, 37, 49, 16, INK, 5)
              + poly([(34, 42.5), (34.5, 36), (38.8, 38.5)], INK, 1.5))
    return sheet + lines + x + pencil

@reg("xt7-player-mpv", BLUE_GREY_DARK)
def xt7():
    return circle(CX, CY, 16.5, INK) + _ring(CX, CY, 13, HOLE, 2.4) + play(33, 30, 14, HOLE)

@reg("yad", BLUE_GREY)
def yad():
    flask = path("M28 17H36V24C42 26 46 30.5 46 36.5C46 43 40 48 32 48C24 48 18 43 18 36.5"
                 "C18 30.5 22 26 28 24Z", INK)
    liquid = path("M21.5 35H42.5C42.5 41 38 44.5 32 44.5C26 44.5 21.5 41 21.5 35Z", ORANGE)
    return flask + liquid + rrect(24.5, 12, 15, 4, 2, INK)

@reg("yahoo-mail", DEEP_PURPLE)
def yahoo_mail():
    env = rrect(15, 12, 34, 22, 3.5, INK) + stroke("M18 15.5L32 25L46 15.5", HOLE, 2.6)
    y = stroke("M22 38L26 43M30 38L26 43V48", INK, 3)
    y2 = stroke("M35.5 38V44.5", INK, 3) + circle(35.5, 48, 1.6, INK)
    return env + y + y2

@reg("yakuake", BLUE_GREY_DARK)
def yakuake():
    bar = rrect(13, 12, 38, 5, 2.5, INK)
    win = rrect(18, 20, 28, 28, 3.5, INK)
    prompt = stroke("M22.5 27L28 32L22.5 37", HOLE, 3) + rrect(30, 38.5, 11, 3.4, 1.7, HOLE)
    return bar + win + prompt

@reg("yakyak", AMBER_DEEP)
def yakyak():
    bubble = path("M32 13.5A16 16 0 0 0 32 45.5C35 45.5 37 45 39.5 44L47 48L45 40"
                  "A16 16 0 0 0 32 13.5Z", INK)
    y = stroke("M25 21.5L32 30L39 21.5M32 30V39", HOLE, 4.5)
    return bubble + y

@reg("yandex-browser-beta", RED)
def yandex_browser():
    return circle(CX, CY, 16.5, INK) + stroke("M24.5 20L32 31L39.5 20M32 31V42", HOLE, 5)

@reg("yandex-disk", BLUE)
def yandex_disk():
    brim = g(f'<ellipse cx="32" cy="34" rx="18.5" ry="7.5" fill="{INK}"/>', "rotate(-12 32 34)")
    under = g(f'<ellipse cx="34" cy="37" rx="8" ry="3" fill="{HOLE}"/>', "rotate(-12 34 37)")
    dome = g(path("M22.5 31C22.5 22 26.5 16 32 16C37.5 16 41.5 22 41.5 31Z", INK,
                  f' stroke="{HOLE}" stroke-width="2.6" stroke-linejoin="round"'), "rotate(-12 32 34)")
    return g(brim + under + dome, "translate(0 -1)")

@reg("yandex-music", AMBER_DEEP)
def yandex_music():
    lens = [16, 7, 13, 6, 17, 7, 11, 6, 15, 7, 12, 6, 16, 7, 10, 6, 14, 7, 12, 6]
    pts = [pt(CX, CY, lens[k] * 1.15 if k % 2 == 0 else 6.5, -90 + 18 * k) for k in range(20)]
    return poly(pts, INK, 1.8)

@reg("yaourtgui", BLUE_DEEP)
def yaourtgui():
    return stroke("M20 16L32 30L44 16M32 30V45", INK, 6.5)

@reg("yaradio-yamusic", AMBER)
def yaradio():
    return (_ring(CX, CY, 15.5, INK, 2.4) + circle(32, 35, 10.5, RED_DEEP)
            + circle(32, 39.5, 5.5, HOLE))

@reg("yarock", RED_DEEP)
def yarock():
    return circle(CX, CY, 16.5, INK) + circle(CX, CY, 13, HOLE) + play(33.5, 30, 14.5, INK)

@reg("yast", TEAL)
def yast():
    body = path("M24 24C28.5 20.5 38 20.5 43 24.5C46 27 47 31 46 35L45 44H41.5L40.5 37.5H29.5"
                "L28.5 44H25L24.5 35.5C22 33.5 18.5 33.5 14.5 36L13.5 34.5C16.5 30 20 27 24 24Z", INK)
    ear = poly([(23.5, 24.5), (21.5, 15.5), (28, 22)], INK, 2)
    tail = stroke("M45 27.5C48.5 30.5 50 35 49.5 40", INK, 2.6)
    return body + ear + tail + circle(22.5, 28, 1.5, HOLE)

@reg("yast-hwinfo", BLUE_GREY)
def yast_hwinfo():
    chip = rrect(23, 21, 18, 18, 3.5, INK)
    pins = "".join(circle(x, y, 2, INK) for x in (16, 24, 32, 40, 48) for y in (14.5, 45.5))
    pins += "".join(circle(x, y, 2, INK) for x in (16, 48) for y in (22.25, 30, 37.75))
    return chip + rrect(28, 26, 8, 8, 1.5, HOLE) + pins

@reg("yast-snapper", LIGHT_BLUE)
def yast_snapper():
    a = stroke("M17.5 31A14.5 14.5 0 0 1 42 20", INK, 4.2) + poly([(38, 15), (47.5, 17), (43, 25.5)], INK, 2)
    b = stroke("M46.5 29A14.5 14.5 0 0 1 22 40", INK, 4.2) + poly([(26, 45), (16.5, 43), (21, 34.5)], INK, 2)
    return a + b

@reg("yast-sound", GREY_DARK)
def yast_sound():
    box = rrect(17, 12, 30, 36, 4, INK)
    return (box + circle(32, 34, 9.5, HOLE) + circle(32, 34, 6.5, INK)
            + circle(32, 34, 2.8, HOLE) + circle(32, 19.5, 2.8, HOLE))

def _vm_window():
    win = rrect(13, 13, 34, 28, 3.5, INK)
    bar = "".join(circle(x, 17.2, 1.3, HOLE) for x in (35, 39, 43))
    pane = rrect(22, 22.5, 21, 7, 1.5, HOLE)
    side = "".join(rrect(16.5, y, 3, 3, .8, HOLE) for y in (23, 28.5, 34))
    return win + line(13, 20.8, 47, 20.8, HOLE, 1.2) + bar + pane + side

@reg("yast-vm-install", BLUE)
def yast_vm_install():
    arrow = stroke("M43 34V45M38.5 41L43 45.5L47.5 41", INK, 2.8)
    return _vm_window() + badge_f(arrow, BLUE_DARK, 43, 40, 9)

@reg("yast-vm-migrate", BLUE_DEEP)
def yast_vm_migrate():
    arrow = stroke("M37.5 40H48.5M44.5 35.5L49 40L44.5 44.5", INK, 2.8)
    return _vm_window() + badge_f(arrow, BLUE_DARK, 43, 40, 9)

@reg("yast-vpn", BLUE_GREY_DEEP)
def yast_vpn():
    shackle = stroke("M25.5 25V20.5A6.5 6.5 0 0 1 38.5 20.5V25", INK, 3.6)
    body = rrect(20, 24, 24, 16, 3, INK) + circle(32, 30.5, 2.4, HOLE) + line(32, 31, 32, 35, HOLE, 2.4)
    net = line(32, 40, 32, 45, INK, 3) + line(15, 46, 49, 46, INK, 3.4)
    return shackle + body + net

@reg("yed", DEEP_PURPLE_DEEP)
def yed():
    c = stroke("M38.5 20.5C35.5 17 30 16.5 26 18.5C24 21.5 20.5 22.5 19 27"
               "C18 31 20 34 20.5 37C22 41 26 43.5 30 41.5C34 40 38.5 42.5 42 40", INK, 5.5)
    return c + circle(42.5, 25, 3.4, INK)

@reg("ymuse", LIGHT_BLUE_DEEP)
def ymuse():
    glass = poly([(14, 20), (38, 20), (26, 33)], INK, 2.5)
    stem = line(26, 33, 26, 44, INK, 3) + rrect(19, 43.5, 14, 3.4, 1.7, INK)
    lime = circle(41, 19.5, 9.5, HOLE) + circle(41, 19.5, 7.5, INK) + play(41.8, 19.5, 7, HOLE, 1.5)
    return glass + stem + lime

@reg("yokadi", CYAN_DEEP)
def yokadi():
    y = stroke("M16.5 17V23.5C16.5 25.5 17.5 26.5 19.5 26.5H24.5M24.5 17V32C24.5 34 23.5 35 21.5 35H16.5", INK, 3.4)
    check = stroke("M30.5 24L34 31L39 16H45", INK, 3.4)
    under = rrect(29.5, 36.5, 16, 3.4, 1.7, INK)
    return g(y + check + under, "translate(1 4)")

@reg("yoshimi", PINK_LIGHT)
def yoshimi():
    ant = line(22, 18, 18.5, 12, INK, 2.6) + line(42, 18, 45.5, 12, INK, 2.6)
    head = rrect(15, 17, 34, 30, 5, INK)
    eyes = (circle(25, 26.5, 5, HOLE) + circle(39, 26.5, 5, HOLE)
            + circle(25, 26.5, 2.2, INK) + circle(39, 26.5, 2.2, INK))
    mouth = rrect(21, 35, 22, 7.5, 1.5, HOLE) + "".join(line(x, 35, x, 42.5, INK, 2.2) for x in (26.5, 32, 37.5))
    return ant + head + eyes + mouth

@reg("youdao-dict", LIGHT_BLUE_DEEP)
def youdao():
    box = stroke("M31 14.5H43C45.5 14.5 47 16.5 46 19L41.5 41.5C41 44 39 45.5 36.5 45.5H21"
                 "C18.5 45.5 17 43.5 17 41V35", INK, 3.6)
    lens = _ring(27, 24.5, 7.5, INK, 3.8) + line(32.5, 30, 37, 35, INK, 4.2)
    return box + lens

@reg("your-freedom", RED)
def your_freedom():
    box = rrect(15, 31, 34, 17, 2.5, INK)
    blocks = (g(rrect(16, 18, 8, 8, 1.5, RED_DARK), "rotate(-20 20 22)")
              + g(rrect(25, 11, 14, 7, 1.5, RED_DARK), "rotate(12 32 14.5)")
              + g(rrect(39.5, 16, 7, 13, 1.5, RED_DARK), "rotate(12 43 22.5)"))
    return blocks + box

@reg("youtrack", DEEP_PURPLE)
def youtrack():
    sq = rrect(14, 12, 36, 36, 4, INK)
    y = stroke("M20 18.5L24.5 25L29 18.5M24.5 25V31.5", HOLE, 3.2)
    t = stroke("M33 18.5H44M38.5 18.5V31.5", HOLE, 3.2)
    return sq + y + t + rrect(20, 38, 13, 3.4, 1.7, HOLE)

@reg("youtube", RED)
def youtube():
    return rrect(13, 17, 38, 27, 8, INK) + play(33, 30.5, 13, HOLE, 2)

@reg("youtube-dl", RED_DEEP)
def youtube_dl():
    yt = rrect(12, 15, 34, 24, 7, INK) + play(30, 27, 11.5, HOLE, 2)
    arrow = stroke("M43 34.5V45M38.5 41L43 45.5L47.5 41", INK, 2.8)
    return yt + badge_f(arrow, RED_DARK, 43, 40, 9)

@reg("youtube-music", RED)
def youtube_music():
    return _ring(CX, CY, 14, INK, 3.4) + play(33.5, 30, 12, INK, 2)

@reg("youtube-music-desktop-app", RED_DEEP)
def ytmdesktop():
    return circle(CX, CY, 16.5, INK) + play(34, 30, 15, HOLE, 2.5)

def _yubi(sym):
    y = stroke("M18 16L26.5 29M38 15L25 44", INK, 6)
    return y + badge_f(sym, AMBER_DARK, 42, 40, 9)

@reg("yubikey-neo-manager", BLUE_GREY_LIGHT)
def yubikey_neo():
    return _yubi(stroke("M38.5 44.5V35.5L45.5 44.5V35.5", INK, 2.6))

@reg("yubikey-personalization-gui", BLUE_GREY_LIGHT)
def yubikey_pers():
    teeth = "".join(g(rrect(40.6, 33.5, 2.8, 4, .8, INK), f"rotate({45 * k} 42 40)") for k in range(8))
    return _yubi(teeth + _ring(42, 40, 3.6, INK, 2.6))

@reg("yubikey-piv-manager", CYAN_DEEP)
def yubikey_piv():
    return _yubi(stroke("M39 45V35.5H43A3 3 0 0 1 43 41.5H39", INK, 2.6))

@reg("yubioath", AMBER_DARK)
def yubioath():
    key = _ring(39, 40, 2.8, INK, 2.4) + stroke("M41.8 40H47.5M45.5 40V42.5", INK, 2.2)
    return _yubi(key)

@reg("yuna", INDIGO_DARK)
def yuna():
    return (stroke("M21 13C21 27 25 33 32 35.5C39 33 43 27 43 13", INK, 4.6)
            + line(32, 35.5, 32, 47, INK, 4.6))

@reg("yuzu", RED)
def yuzu():
    left = stroke("M29 13V47M29 13H27.5A10.5 10.5 0 0 0 17 23.5V36.5A10.5 10.5 0 0 0 26 46.9", INK, 3.6)
    right = stroke("M35 47V13M35 47H36.5A10.5 10.5 0 0 0 47 36.5V23.5A10.5 10.5 0 0 0 38 13.1", INK, 3.6)
    return left + right

@small("xiphos")
def xiphos_s():
    return (rrect(16, 12, 32, 36, 4, INK) + rrect(29, 16, 7, 28, 2, HOLE)
            + rrect(22.5, 22.5, 20, 7, 2, HOLE))

@small("xmlcopyeditor")
def xmlcopyeditor_s():
    pent = [pt(32, 31, 8.5, -90 + 72 * k) for k in range(5)]
    return rrect(15, 13, 34, 34, 5, INK) + poly(pent, HOLE, 3.5)

@small("xnconvert")
def xnconvert_s():
    return _xn_eye(circle(32, 32, 9, HOLE) + stroke("M36 28A5.5 5.5 0 1 0 36 36", INK, 3.4))

@small("xnview")
def xnview_s():
    return _xn_eye(circle(32, 32, 9, HOLE))

@small("xnretro")
def xnretro_s():
    return cut(cpath(31, 31, 16) + cpath(31, 31, 7), INK) + circle(47, 14.5, 3.4, INK)

@small("xnsketch")
def xnsketch_s():
    return (circle(28, 34, 13.5, INK) + circle(28, 34, 6, HOLE)
            + line(33, 29, 46, 16, HOLE, 10) + line(33, 29, 46, 16, DEEP_ORANGE_DARK, 6.5))

@small("xonotic")
def xonotic_s():
    head = path("M15.5 33L20.5 24C23.5 19.5 28 17.5 33 17L41 11L40.5 17.5L48 15L45 21.5L50 22.5"
                "L45 28C45.5 34 43 39.5 39 43L35.5 48.5L32.5 41C29.5 39 28.5 36 28.5 33"
                "C26 32 23.5 32 21.5 34L19.5 38Z", INK)
    return head + circle(29, 24, 2.2, HOLE)

@small("xonsh")
def xonsh_s():
    shell = path("M28.5 11.5L33 17.5C40.5 19.5 47 26 47 34C47 40.5 43 45 38 47"
                 "L36 42.5C34 46 30 48.5 26.5 48C22 41 20 32 21.5 24C22.5 19 25 15 28.5 11.5Z", INK)
    return shell + stroke("M37 29C41 32.5 42 38.5 38.5 43", HOLE, 3)

@small("xournal")
def xournal_s():
    sheet = rrect(14, 12, 30, 36, 3.5, INK)
    x = line(20, 27, 31, 41, HOLE, 3.4) + line(31, 27, 20, 41, HOLE, 3.4)
    pencil = line(37, 37, 49, 16, HOLE, 10) + line(37, 37, 49, 16, INK, 6)
    return sheet + x + pencil

@small("xt7-player-mpv")
def xt7_s():
    return circle(CX, CY, 17, INK) + play(33.5, 30, 17, HOLE)

@small("yahoo-mail")
def yahoo_mail_s():
    return rrect(13, 16, 38, 28, 4, INK) + stroke("M17 20.5L32 31L47 20.5", HOLE, 3.6)

@small("yakuake")
def yakuake_s():
    return (rrect(12, 11, 40, 6, 3, INK) + rrect(17, 21, 30, 27, 4, INK)
            + stroke("M22.5 28L29 34L22.5 40", HOLE, 3.8))

@small("yandex-disk")
def yandex_disk_s():
    brim = g(f'<ellipse cx="32" cy="35" rx="19" ry="7.5" fill="{INK}"/>', "rotate(-12 32 35)")
    dome = g(path("M22 32C22 22 26.5 15 32 15C37.5 15 42 22 42 32Z", INK,
                  f' stroke="{HOLE}" stroke-width="3" stroke-linejoin="round"'), "rotate(-12 32 35)")
    return brim + dome

@small("yandex-music")
def yandex_music_s():
    pts = [pt(CX, CY, 17.5 if k % 2 == 0 else 7, -90 + 30 * k) for k in range(12)]
    return poly(pts, INK, 2)

@small("yaradio-yamusic")
def yaradio_s():
    return circle(32, 32, 13.5, RED_DEEP) + circle(32, 37.5, 7, HOLE)

@small("yarock")
def yarock_s():
    return circle(CX, CY, 17, INK) + play(33.5, 30, 17, HOLE)

@small("yast")
def yast_s():
    body = path("M24 24C28.5 20.5 38 20.5 43 24.5C46 27 47 31 46 35L45 45H40.5L40 38H30"
                "L29 45H24.5L24 36C21.5 34 18 34 14 36.5L13 34C16 29.5 19.5 26.5 24 24Z", INK)
    return body + poly([(23.5, 24.5), (21, 15), (29, 22)], INK, 2.5)

@small("yast-hwinfo")
def yast_hwinfo_s():
    pins = "".join(rrect(x - 2, y - 2.5, 4, 5, 1, INK) for x in (22, 32, 42) for y in (14, 46))
    pins += "".join(rrect(x - 2.5, y - 2, 5, 4, 1, INK) for x in (14, 50) for y in (22, 30, 38))
    return rrect(19, 17, 26, 26, 4, INK) + rrect(27, 25, 10, 10, 2, HOLE) + pins

@small("yast-sound")
def yast_sound_s():
    return rrect(16, 11, 32, 38, 4, INK) + circle(32, 33, 10, HOLE) + circle(32, 33, 5, INK)

def _vm_window_s():
    return (rrect(12, 13, 36, 28, 4, INK) + line(12, 21, 48, 21, HOLE, 2.4)
            + rrect(17, 25.5, 22, 7, 2, HOLE))

@small("yast-vm-install")
def yast_vm_install_s():
    return _vm_window_s() + badge_f(stroke("M42 34V45.5M37 40.5L42 45.5L47 40.5", INK, 3.4),
                                  BLUE_DARK, 42, 40, 10)

@small("yast-vm-migrate")
def yast_vm_migrate_s():
    return _vm_window_s() + badge_f(stroke("M36 40H47.5M42.5 35L47.5 40L42.5 45", INK, 3.4),
                                  BLUE_DARK, 42, 40, 10)

@small("yast-vpn")
def yast_vpn_s():
    return (stroke("M25 25V20A7 7 0 0 1 39 20V25", INK, 4.2) + rrect(19, 24, 26, 17, 3, INK)
            + circle(32, 32, 3, HOLE) + line(32, 41, 32, 45, INK, 3.6) + line(14, 46.5, 50, 46.5, INK, 4))

@small("ymuse")
def ymuse_s():
    glass = poly([(13, 19), (39, 19), (26, 33)], INK, 3)
    stem = line(26, 33, 26, 44, INK, 4) + rrect(18, 43, 16, 4.5, 2.2, INK)
    return glass + stem + circle(42, 18.5, 11, HOLE) + circle(42, 18.5, 8.5, INK)

@small("yokadi")
def yokadi_s():
    y = stroke("M16 16V24C16 26 17 27 19 27H25M25 16V34C25 36 24 37 22 37H16", INK, 4.4)
    check = stroke("M31 26L35.5 35L41 16H47", INK, 4.4)
    return g(y + check, "translate(0 4)")

@small("yoshimi")
def yoshimi_s():
    head = rrect(14, 16, 36, 31, 5, INK)
    eyes = circle(24.5, 26.5, 5.5, HOLE) + circle(39.5, 26.5, 5.5, HOLE)
    return head + eyes + rrect(21, 36, 22, 6, 2, HOLE)

@small("youdao-dict")
def youdao_s():
    box = stroke("M31 14H43C46 14 47.5 16.5 46.5 19L42 42C41.5 44.5 39.5 46 37 46H20"
                 "C17.5 46 16 44 16 41V35", INK, 4.4)
    return box + _ring(27, 24.5, 7.5, INK, 4.6) + line(32.5, 30, 37.5, 35.5, INK, 5)

@small("your-freedom")
def your_freedom_s():
    blocks = (g(rrect(15, 17, 10, 9, 2, RED_DARK), "rotate(-20 20 21.5)")
              + g(rrect(33, 12, 13, 13, 2, RED_DARK), "rotate(12 39.5 18.5)"))
    return blocks + rrect(14, 30, 36, 18, 3, INK)

@small("youtrack")
def youtrack_s():
    sq = rrect(13, 12, 38, 36, 4, INK)
    return (sq + stroke("M19 19L24.5 27L30 19M24.5 27V40", HOLE, 4.2)
            + stroke("M34 19H46M40 19V40", HOLE, 4.2))

@small("youtube-dl")
def youtube_dl_s():
    yt = rrect(11, 14, 36, 26, 7, INK) + play(29, 27, 12.5, HOLE, 2)
    return yt + badge_f(stroke("M43 34V45.5M38 40.5L43 45.5L48 40.5", INK, 3.4), RED_DARK, 43, 40, 10)

@small("youtube-music")
def youtube_music_s():
    return _ring(CX, CY, 14.5, INK, 4.2) + play(33.5, 30, 14, INK, 2)

def _yubi_s(sym):
    return stroke("M17 15L26 29M38 14L24.5 45", INK, 7) + badge_f(sym, DEEP_PURPLE_LIGHT, 42, 39.5, 10.5)

@small("yubikey-neo-manager")
def yubikey_neo_s():
    return _yubi_s(stroke("M38 45V34L46 45V34", INK, 3))

@small("yubikey-personalization-gui")
def yubikey_pers_s():
    return _yubi_s(_ring(42, 39.5, 4.2, INK, 3.4))

@small("yubikey-piv-manager")
def yubikey_piv_s():
    return _yubi_s(stroke("M38.5 45.5V34H43A3.5 3.5 0 0 1 43 41H38.5", INK, 3))

@small("yubioath")
def yubioath_s():
    return _yubi_s(_ring(38.5, 39.5, 3.2, INK, 3) + line(42, 39.5, 47.5, 39.5, INK, 3))

@small("yuzu")
def yuzu_s():
    left = stroke("M29 13V47M29 13H27A10 10 0 0 0 17 23V37A10 10 0 0 0 25.5 46.9", INK, 4.4)
    right = stroke("M35 47V13M35 47H37A10 10 0 0 0 47 37V23A10 10 0 0 0 38.5 13.1", INK, 4.4)
    return left + right
