# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 46: mouse-actions to mx-cleanup, Microsoft Office, media players, MX tools.

Same kit and rules as batch01: palette tile, mark in INK, HOLE for
cut-outs, mostly one colour.
"""
from lm import *
from glyphs.kit import _gear_e, registry, _ring

ICONS, SMALL, reg, small = registry()

def _beamed(x1, y1, x2, y2, r, h, colour, w=3):
    """Two note heads joined by a slanted beam; stems rise h from the heads."""
    heads = circle(x1, y1, r, colour) + circle(x2, y2, r, colour)
    s1, s2 = x1 + r - w / 2, x2 + r - w / 2
    stems = line(s1, y1, s1, y1 - h, colour, w, "butt") + line(s2, y2, s2, y2 - h, colour, w, "butt")
    beam = poly([(s1 - w / 2, y1 - h), (s2 + w / 2, y2 - h - 1), (s2 + w / 2, y2 - h + 4),
                 (s1 - w / 2, y1 - h + 5)], colour, 1)
    return heads + stems + beam

def _drive(inner):
    body = rrect(15, 13, 34, 35, 5, INK)
    window = circle(32, 27, 10, HOLE)
    slot = rrect(19, 40.5, 15, 2.8, 1.4, HOLE) + circle(40, 41.9, 1.6, HOLE) + circle(45, 41.9, 1.6, HOLE)
    return body + window + inner + slot

def _ms(letter, back):
    badge = rrect(12, 18, 24, 24, 5, HOLE) + rrect(13, 19, 22, 22, 4, INK)
    return back + badge + letter

def _sheet(shade):
    return rrect(24, 13, 27, 34, 4, shade)

@reg("ms-excel", ORANGE_DARK)
def ms_excel():
    back = _sheet(ORANGE_DEEP)
    back += "".join(line(38, y, 51, y, HOLE, 1.8, "butt") for y in (21.5, 30, 38.5))
    back += line(44, 13, 44, 47, HOLE, 1.8, "butt")
    x = line(20, 25, 28, 35, HOLE, 3.6) + line(28, 25, 20, 35, HOLE, 3.6)
    return _ms(x, back)

@reg("ms-word", BLUE_DARK)
def ms_word():
    back = _sheet(BLUE_LIGHT)
    back += "".join(rrect(38, y, 9, 2.6, 1.3, HOLE) for y in (18.5, 24.5, 30.5, 36.5))
    w = stroke("M17.5 24.5L20.3 35.5L24 27.5L27.7 35.5L30.5 24.5", HOLE, 3)
    return _ms(w, back)

@reg("ms-onenote", PURPLE_DEEP)
def ms_onenote():
    back = _sheet(PURPLE_SOFT)
    back += "".join(line(43, y, 51, y, HOLE, 1.8, "butt") for y in (21.5, 30, 38.5))
    back += line(43, 13, 43, 47, HOLE, 1.8, "butt")
    n = stroke("M19.5 35.5V24.5L28.5 35.5V24.5", HOLE, 3.4)
    return _ms(n, back)

@reg("ms-outlook", BLUE_DEEP)
def ms_outlook():
    back = rrect(24, 14, 27, 32, 4, BLUE_SOFT) + stroke("M36 22L43.5 29L51 22", HOLE, 2.2)
    o = _ring(24, 30, 5, HOLE, 3.4)
    return _ms(o, back)

@reg("ms-powerpoint", RED_DEEP)
def ms_powerpoint():
    back = circle(36, 30, 15, RED_SOFT) + path("M36 15A15 15 0 0 1 51 30H36Z", DEEP_ORANGE_SOFT)
    back += line(36, 13, 36, 30, HOLE, 1.8, "butt") + line(36, 30, 52, 30, HOLE, 1.8, "butt")
    p = stroke("M20.5 35.5V24.5H25.5A3.3 3.3 0 0 1 25.5 31.1H20.5", HOLE, 3.4)
    return _ms(p, back)

@reg("ms-office", PINK)
def ms_office():
    return cut("M17 19.5L37 12L47 15V45L37 48L17 40.5Z" + "M23.5 23V37.5L37 41.5V18.5Z", INK)

@reg("ms-onedrive", BLUE_DEEP)
def ms_onedrive():
    back = path("M20 32C19 24 25 18 32 18C37 18 41 21 42.5 25C44 25 45 25.2 46 25.6"
                "L30 35Z", BLUE_SOFT)
    front = path("M17 42A5.5 5.5 0 0 1 17.5 31C19 27 23 25 27 26.5C29.5 23 33 21.5 37 22.5"
                 "C41 23.5 43.5 26.5 44 30.5A6 6 0 0 1 45 42Z", INK)
    return back + front

@reg("mpv", PURPLE_DARK)
def mpv():
    return (circle(CX, CY, 16.5, PURPLE_LIGHT) + circle(34, 28.5, 12, HOLE) +
            circle(34, 28.5, 8.5, INK) + poly([(31.5, 24), (38.5, 28.5), (31.5, 33)], HOLE, 1.5))

@reg("mpvz", PURPLE)
def mpvz():
    outer = stroke("M18 14.5L46 30L18 45.5Z", INK, 4)
    return outer + poly([(24, 22.5), (37, 30), (24, 37.5)], INK, 2)

@reg("mpz", PURPLE_DEEP)
def mpz():
    d = "M27 14H37V25H48V35H37V46H27V35H16V25H27Z"
    return stroke(d, INK, 3.6)

@reg("mpc-qt", GREY_DARK)
def mpc_qt():
    return (_ring(CX, CY, 15, INK, 3.2) + circle(26.5, 25.5, 2.4, INK) + circle(37.5, 25.5, 2.4, INK)
            + stroke("M24.5 33.5Q32 40.5 39.5 33.5", INK, 3))

@reg("mpd", LIGHT_BLUE_DEEP)
def mpd():
    spk = circle(25, 24, 11, INK) + circle(25, 24, 6.5, HOLE) + circle(25, 24, 3.2, INK)
    mon = (rrect(27, 29, 24, 16, 3, HOLE) + rrect(29, 31, 20, 12, 2, INK) +
           line(39, 43, 39, 47, INK, 3) + line(34, 47.5, 44, 47.5, INK, 2.6))
    return g(spk + mon, "translate(-1 0)")

@reg("mp3splt-gtk", BLUE_GREY_DARK)
def mp3splt():
    disc = circle(CX, CY, 16.5, INK)
    cuts = "".join(line(*pt(CX, CY, 6.8, a), *pt(CX, CY, 17, a), HOLE, 2, "butt") for a in (-90, 30, 150))
    return disc + cuts + circle(CX, CY, 6, AMBER) + circle(CX, CY, 2.3, HOLE)

@reg("mpdevil", RED_DEEP)
def mpdevil():
    band = stroke("M17 34A15 15 0 0 1 47 34", INK, 2.6)
    cups = rrect(13.5, 29, 6, 12, 3, INK) + rrect(44.5, 29, 6, 12, 3, INK)
    horns = (path("M23 26C19 22 18.5 16 20.5 12C22 17 25 20 29 21.5Z", INK) +
             path("M41 26C45 22 45.5 16 43.5 12C42 17 39 20 35 21.5Z", INK))
    head = circle(32, 33, 11.5, INK)
    eyes = circle(28, 31, 3, HOLE) + circle(36, 31, 3, HOLE) + circle(28.5, 31.5, 1.3, INK) + circle(35.5, 31.5, 1.3, INK)
    smile = stroke("M27.5 38Q32 41.5 36.5 38", HOLE, 2.2)
    return band + cups + horns + head + eyes + smile

@reg("mps", LIGHT_BLUE_DEEP)
def mps():
    screen = rrect(13, 14, 38, 32, 5, INK)
    m = stroke("M19 30V20.5L22.5 25L26 20.5V30", HOLE, 2.4)
    p = stroke("M30 30V20.5H33.2A2.6 2.6 0 0 1 33.2 25.7H30", HOLE, 2.4)
    s = stroke("M45 21H40.5A2.3 2.3 0 0 0 40.5 25.5H42.5A2.3 2.3 0 0 1 42.5 30H38", HOLE, 2.4)
    cur = rrect(18.5, 36, 11, 2.8, 1.4, HOLE)
    return screen + m + p + s + cur

@reg("musique", INDIGO_LIGHT)
def musique():
    return _beamed(22, 40, 39, 36.5, 5.2, 24, INK, 3.4)

@reg("musikcube", BLUE_GREY_DARK)
def musikcube():
    chev = stroke("M14.5 20L21 25L14.5 30", INK, 3)
    return chev + _beamed(28, 41, 42, 38, 4.2, 20, YELLOW, 3)

@reg("multimedia-audio-player", DEEP_ORANGE_DEEP)
def audio_player():
    return _ring(CX, CY, 15.5, INK, 3) + _beamed(25.5, 36, 36.5, 34, 3.6, 14, INK, 2.8)

@reg("musicbrainz", DEEP_PURPLE_DEEP)
def musicbrainz():
    left = path("M32 13.5A16.5 16.5 0 0 0 32 46.5Z", DEEP_PURPLE_SOFT)
    right = path("M32 13.5A16.5 16.5 0 0 1 32 46.5Z", ORANGE)
    inner = circle(CX, CY, 12.5, INK)
    return left + right + inner + _beamed(26, 35, 35.5, 33.5, 3, 11.5, HOLE, 2.4)

@reg("museeq", BLUE_DEEP)
def museeq():
    return stroke("M25 17V45M25 17V29A7 7 0 0 0 39 29V17V38", INK, 5)

@reg("museeks", LIGHT_BLUE_DEEP)
def museeks():
    left = poly([(16, 18), (31, 30), (16, 42)], INK, 2.5)
    right = poly([(48, 18), (48, 42), (41, 42), (41, 32), (34, 39), (28.5, 33.5)], LIGHT_BLUE_SOFT, 2.5)
    return right + left

@reg("musescore", INDIGO_DEEP)
def musescore():
    top = stroke("M40.5 20C39 14.5 26 14 25.5 20.5C25 25.5 31.5 26.5 36 26", INK, 4.2)
    mid = line(36, 26, 29, 32, INK, 4.2)
    bot = stroke("M29 32C35 31 41 33.5 40.5 39C40 44.5 29 46 25 41", INK, 4.2)
    return top + mid + bot + circle(41, 20, 3.8, INK) + circle(24.5, 41, 3.8, INK)

@reg("musixmatch", RED_LIGHT)
def musixmatch():
    tie = poly([(16, 18.5), (32, 27), (48, 18.5), (48, 41.5), (32, 33), (16, 41.5)], INK, 3)
    return tie + line(16.5, 19, 47.5, 41, HOLE, 1.4) + line(47.5, 19, 16.5, 41, HOLE, 1.4)

@reg("mouse-actions", ORANGE)
def mouse_actions():
    arc = stroke("M18 15C31 13 43 19 47.5 30C42 28 34 30 27.5 37", INK, 3.4)
    swipe = stroke("M18 15C26.5 22 30 32 30 43", INK, 3.4)
    head = stroke("M25 39.5L30 45L35 39.5", INK, 3.4)
    return arc + swipe + head

@reg("mousepad", BLUE_GREY)
def mousepad():
    sheet = rrect(15, 13, 26, 34, 4, INK)
    lines = "".join(rrect(19, y, w, 2.6, 1.3, HOLE) for y, w in [(20, 16), (26, 16), (32, 10), (38, 12)])
    pencil = g(rrect(-3.5, -15, 7, 24, 1.5, INK) + poly([(-3.5, 9), (3.5, 9), (0, 15)], INK, 1.2)
               + line(-3.5, 6.5, 3.5, 6.5, HOLE, 1.6, "butt"),
               "translate(41 26) rotate(35)")
    outline = g(rrect(-5.5, -17, 11, 34, 3, HOLE), "translate(41 26) rotate(35)")
    return sheet + lines + outline + pencil

@reg("movmetaedit", GREY_DARK)
def movmetaedit():
    disc = circle(28, 30, 12, INK)
    q = stroke("M24.5 26.5A3.5 3.5 0 1 1 29.5 29.5C28.3 30.2 28 31 28 32.5", HOLE, 2.8) + circle(28, 37, 1.8, HOLE)
    moon = stroke("M40 15.5A15 15 0 0 1 40 44.5", INK, 4.4)
    return disc + q + moon

@reg("mozc", DEEP_ORANGE)
def mozc():
    bar = line(19, 20, 40, 18.5, INK, 3.6)
    stem = stroke("M28.5 13.5C28 24 29 35 32.5 44", INK, 3.6)
    loop = stroke("M39 25.5C31 32 24 43 19.5 40C16 37.5 21 29 31.5 27.5"
                  "C41 26 47 29 46.5 35.5C46 41 41 44 36 44.5", INK, 3.6)
    return bar + stem + loop

@reg("mu.codewith.editor", RED_DEEP)
def mu():
    snake = stroke("M26 45V28C26 21.5 30 17.5 36 17.5H45", INK, 8)
    return snake + circle(38, 17.5, 1.8, HOLE)

@reg("mutt", GREY_DARK)
def mutt():
    flap = poly([(14, 28), (32, 15), (50, 28)], GREY_LIGHT, 2)
    paper = rrect(19, 16, 26, 22, 2.5, INK)
    at = (_ring(32, 25.5, 4, HOLE, 2.2) + stroke("M36 25.5V27.5A2 2 0 0 0 40 27.5V25.5"
                                                   "A8 8 0 1 0 36.5 32.2", HOLE, 2.2))
    front = path("M14 29L32 41L50 29V45A3 3 0 0 1 47 48H17A3 3 0 0 1 14 45Z", INK)
    edge = stroke("M14 29L32 41L50 29", HOLE, 2)
    return flap + paper + at + front + edge

@reg("mrboom", BROWN)
def mrboom():
    ball = line(32, 16, 32, 13, INK, 2) + circle(32, 12, 2.6, PINK_SOFT)
    head = rrect(19, 15.5, 26, 19, 9, INK)
    visor = rrect(22.5, 20, 19, 10, 4.5, PINK_SOFT)
    eyes = rrect(27.5, 21.5, 2.8, 6.5, 1.4, INK) + rrect(34.2, 21.5, 2.8, 6.5, 1.4, INK)
    body = rrect(24, 35, 16, 8, 3, INK) + line(24, 38.5, 40, 38.5, HOLE, 1.8, "butt")
    feet = rrect(21, 43.5, 9, 5, 2.5, PINK_SOFT) + rrect(34, 43.5, 9, 5, 2.5, PINK_SOFT)
    return ball + head + visor + eyes + body + feet

@reg("multiwinia", RED_DEEP)
def multiwinia():
    return (line(32, 13, 32, 33, INK, 5) + line(18, 23, 46, 23, INK, 5) +
            line(23, 34, 41, 34, INK, 5) + line(24, 34, 24, 46, INK, 5) + line(40, 34, 40, 46, INK, 5))

@reg("muck", BLUE_DEEP)
def muck():
    ground = rrect(13, 38, 38, 10, 4, LIGHT_BLUE_LIGHT)
    m = stroke("M15 32V22L18.5 26.5L22 22V32", INK, 2.6)
    u = stroke("M25 22V28.5A3.5 3.5 0 0 0 32 28.5V22", INK, 2.6)
    c = stroke("M41.5 23.2A4.8 5 0 1 0 41.5 30.8", INK, 2.6)
    k = stroke("M44.5 22V32M49.5 22L45 27L49.5 32", INK, 2.6)
    return ground + m + u + c + k

@reg("muse-dash", PINK)
def muse_dash():
    m = path("M29 14H36L39 24L42 14H49V45H44L42.5 31L40 45H37L34 31L33.5 45H29Z", INK,
             f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    spikes = poly([(29, 16), (22, 16), (25, 21), (15, 24), (23, 28), (17, 33), (25, 35), (21, 42),
                   (29, 38)], INK, 1.5)
    return spikes + m

@reg("multimc", BROWN_DEEP)
def multimc():
    block = rrect(14, 13, 36, 34, 4, BROWN_LIGHT)
    grass = path("M14 17A4 4 0 0 1 18 13H46A4 4 0 0 1 50 17V21H14Z", LIGHT_BLUE_SOFT)
    for x, h in [(14, 3), (19, 6), (26, 2), (31, 5), (38, 3), (44, 6)]:
        grass += rrect(x, 20, 5, h, 0, LIGHT_BLUE_SOFT)
    inf = stroke("M32 35C28 30 22 30 22 35C22 40 28 40 32 35C36 30 42 30 42 35C42 40 36 40 32 35Z", INK, 3.4)
    return block + grass + inf

@reg("mupen64plus-qt", RED_DEEP)
def mupen64plus():
    m = stroke("M17 44V17L29 30L41 17V28", INK, 6.5)
    badge = circle(41, 39, 10, HOLE) + circle(41, 39, 8, BLUE_LIGHT)
    plus = line(36.5, 39, 45.5, 39, INK, 3.2) + line(41, 34.5, 41, 43.5, INK, 3.2)
    return m + badge + plus

@reg("msfpc", GREY_LIGHT)
def msfpc():
    cow = path("M16 24C16 22 17.5 21 19.5 21H38L43 17.5H47L50 24L48.5 27.5L45.5 27L42.5 30V35.5"
               "L41.5 46H38.8L37.8 37H24.5L23.5 46H20.8L19.8 36.5C17.5 35.5 16 33 16 30Z", INK,
               f' stroke="{INK}" stroke-width="1" stroke-linejoin="round"')
    horn = stroke("M44 18L45.5 13.5", INK, 2.2)
    tail = stroke("M16.5 23.5C14.5 27 14 31 14.5 36", INK, 2.2)
    return cow + horn + tail

@reg("mstdn", BLUE)
def mstdn():
    head = path("M26 13H38C44.6 13 50 18.4 50 25V28C50 34.6 44.6 40 38 40H30.5C29.5 40 29 41 29.8 41.8"
                "C31 42.8 33.5 43 36 43H41V47H33C22 47 15 45 15 36V24C15 17.9 19.9 13 26 13Z", INK)
    return head + circle(24.5, 22.5, 2.4, HOLE)

@reg("mtpaint", RED_DEEP)
def mtpaint():
    out = ""
    for x in (21, 32, 43):
        out += poly([(x - 4, 21), (x, 13), (x + 4, 21)], INK, 1.5)
        out += rrect(x - 4.2, 21, 8.4, 26, 2, INK)
        out += line(x - 4.2, 21.5, x + 4.2, 21.5, HOLE, 1.5, "butt")
        out += line(x, 22.5, x, 45, HOLE, 1.2, "butt")
    return out

@reg("mtvmusic", RED_DEEP)
def mtvmusic():
    m = path("M14 43V14H21.5L27.5 25.5L33.5 14H41V32H34.5V26L27.5 37L20.5 26V43Z", INK)
    badge = circle(42, 39.5, 10, HOLE) + circle(42, 39.5, 8.3, INK)
    tv = (line(36.5, 36, 41, 36, HOLE, 2.2) + line(38.75, 36, 38.75, 43.5, HOLE, 2.2) +
          stroke("M42.5 36L44.7 43.5L47 36", HOLE, 2.2))
    return m + badge + tv

@reg("mullvad-browser", INDIGO_DARK)
def mullvad_browser():
    return path("M16 45V15H24L32 29L40 15H48V45H41.5V27L34.5 39H29.5L22.5 27V45Z", AMBER,
                ' stroke="#FFC006" stroke-width="1.5" stroke-linejoin="round"')

@reg("mullvad-vpn", INDIGO_DARK)
def mullvad_vpn():
    body = path("M15 45C15 33 21 25.5 31 25C39 24.5 45 28.5 48 33C49.2 35 48.3 37.5 46 37.5H41"
                "C39 40.5 38 43 38 45Z", BROWN_SOFT)
    helmet = path("M20 29C20 20 26 14.5 33 14.5C40 14.5 45 19.5 45 26.5L20 30Z", AMBER,
                  ' stroke="#FFC006" stroke-width="1.5" stroke-linejoin="round"')
    lamp = rrect(41, 20, 6, 5, 2, INK)
    eye = circle(37, 31, 1.8, INDIGO_DARK)
    nose = circle(47.3, 34.5, 2, BROWN_DARK)
    return body + helmet + lamp + eye + nose

@reg("multimedia-photo-viewer", LIGHT_BLUE_DEEP)
def photo_viewer():
    card = rrect(13, 14, 38, 32, 5, INK)
    sun = circle(23, 22, 3.8, HOLE)
    cloud = circle(38, 23, 3.4, HOLE) + circle(42.5, 21.5, 4, HOLE) + rrect(35, 22.5, 12, 4.5, 2.25, HOLE)
    hills = path("M16.5 42.5L26 31L33 38.5L38 33.5L47.5 42.5Z", HOLE,
                 f' stroke="{HOLE}" stroke-width="1.8" stroke-linejoin="round"')
    return card + sun + cloud + hills

@reg("multimedia-photo-manager", PINK_LIGHT)
def photo_manager():
    card = rrect(13, 14, 32, 26, 4, INK)
    sun = circle(36, 21.5, 3.6, HOLE)
    hills = path("M16 36.5L24 27L30 33L34 29L42 36.5Z", HOLE,
                 f' stroke="{HOLE}" stroke-width="1.5" stroke-linejoin="round"')
    badge = circle(42, 39, 10, HOLE) + circle(42, 39, 8.2, INK)
    cam = rrect(36.5, 35.5, 11, 8, 2, HOLE) + rrect(39.5, 34, 5, 3, 1, HOLE) + circle(42, 39.5, 2.2, INK)
    return card + sun + hills + badge + cam

@reg("multimedia-video-player", PURPLE)
def video_player():
    play = poly([(25, 13.5), (41, 25), (25, 36.5)], INK, 3.5)
    track = line(15, 44, 49, 44, PURPLE_SOFT, 3.4)
    done = line(15, 44, 36, 44, INK, 3.4)
    return play + track + done + circle(36, 44, 4, INK)

@reg("mumble", BLUE_DEEP)
def mumble():
    band = stroke("M19 36V26A13 13 0 0 1 45 26V36", INK, 4)
    mic = stroke("M28.5 14V22A3.5 3.5 0 0 0 35.5 22V14", INK, 4)
    cups = path("M12.5 41A7.5 7.5 0 0 1 20 33.5H24V48H20A7.5 7.5 0 0 1 12.5 41Z", INK)
    cups += path("M51.5 41A7.5 7.5 0 0 0 44 33.5H40V48H44A7.5 7.5 0 0 0 51.5 41Z", INK)
    boom = rrect(28, 42.5, 10, 5.5, 2.75, INK)
    return band + mic + cups + boom

@reg("muon", AMBER_DEEP)
def muon():
    m = stroke("M17 45V16L32 31L47 16V45", INK, 5.5)
    arrow = line(32, 21, 32, 40, AMBER_DARK, 3.6) + stroke("M26.5 35L32 41L37.5 35", AMBER_DARK, 3.6)
    return m + arrow

@reg("mx-alerts", AMBER_DEEP)
def mx_alerts():
    bulb = path("M32 12A11.5 11.5 0 0 1 39.5 32.2C38 33.7 37.5 35 37.5 36.5H26.5C26.5 35 26 33.7 24.5 32.2"
                "A11.5 11.5 0 0 1 32 12Z", INK)
    base = rrect(26.5, 38, 11, 3.2, 1.6, INK) + rrect(27.5, 42.2, 9, 3.2, 1.6, INK) + rrect(30, 46.2, 4, 2.4, 1.2, INK)
    return bulb + base

@reg("mx-boot-options", ORANGE_DEEP)
def mx_boot_options():
    return _drive(_gear_e(32, 27, 5.2, INK, HOLE))

@reg("mx-bootrepair", RED_DEEP)
def mx_bootrepair():
    return _drive(line(26, 27, 38, 27, INK, 4.4) + line(32, 21, 32, 33, INK, 4.4))

@reg("mx-cleanup", DEEP_PURPLE_LIGHT)
def mx_cleanup():
    handle = line(47, 12, 35, 29, INK, 3.4)
    head = path("M31 26.5L39.5 32.5C38 38 35 44 31 47.5C25 47.5 18.5 45.5 14.5 41.5C21 40 27 34 31 26.5Z", INK)
    band = line(30.5, 28.5, 38.5, 34.2, HOLE, 2)
    bristles = line(28, 38, 24, 44.5, HOLE, 1.6) + line(33, 39, 30, 46, HOLE, 1.6)
    return handle + head + band + bristles

@small("mps")
def mps_s():
    screen = rrect(13, 14, 38, 32, 5, INK)
    m = stroke("M19 33V20L25 27L31 20V33", HOLE, 4)
    return screen + m + rrect(35, 29.5, 10, 4, 2, HOLE)

@small("muck")
def muck_s():
    ground = rrect(13, 38, 38, 10, 4, LIGHT_BLUE_LIGHT)
    return ground + stroke("M20 33V16L32 26L44 16V33", INK, 5)

@small("ms-excel")
def ms_excel_s():
    return _sheet(LIGHT_BLUE) + rrect(12, 17, 26, 26, 5, HOLE) + rrect(13, 18, 24, 24, 4, INK) + \
        line(20, 24, 30, 36, HOLE, 4.4) + line(30, 24, 20, 36, HOLE, 4.4)

@small("ms-word")
def ms_word_s():
    return _sheet(BLUE_LIGHT) + rrect(12, 17, 26, 26, 5, HOLE) + rrect(13, 18, 24, 24, 4, INK) + \
        stroke("M17.5 24L20.5 36L25 28L29.5 36L32.5 24", HOLE, 3.6)

@small("ms-onenote")
def ms_onenote_s():
    return _sheet(PURPLE_SOFT) + rrect(12, 17, 26, 26, 5, HOLE) + rrect(13, 18, 24, 24, 4, INK) + \
        stroke("M19.5 36V24L30.5 36V24", HOLE, 4.2)

@small("ms-outlook")
def ms_outlook_s():
    return rrect(24, 14, 27, 32, 4, BLUE_SOFT) + rrect(12, 17, 26, 26, 5, HOLE) + \
        rrect(13, 18, 24, 24, 4, INK) + _ring(25, 30, 5.5, HOLE, 4.2)

@small("ms-powerpoint")
def ms_powerpoint_s():
    return circle(36, 30, 15, RED_SOFT) + rrect(12, 17, 26, 26, 5, HOLE) + \
        rrect(13, 18, 24, 24, 4, INK) + stroke("M21 36V24H26A3.8 3.8 0 0 1 26 31.6H21", HOLE, 4.2)

@small("mtvmusic")
def mtvmusic_s():
    m = path("M14 43V14H21.5L27.5 25.5L33.5 14H41V32H34.5V26L27.5 37L20.5 26V43Z", INK)
    return m + circle(42, 39.5, 10, HOLE) + circle(42, 39.5, 8.3, INK)

@small("mutt")
def mutt_s():
    paper = rrect(19, 12, 26, 22, 2.5, INK) + circle(32, 21.5, 5, HOLE) + circle(32, 21.5, 2, INK)
    front = path("M14 29L32 41L50 29V45A3 3 0 0 1 47 48H17A3 3 0 0 1 14 45Z", INK)
    return paper + front + stroke("M14 29L32 41L50 29", HOLE, 3)

@small("mx-boot-options")
def mx_boot_options_s():
    body = rrect(15, 13, 34, 35, 5, INK) + circle(32, 28, 11, HOLE)
    return body + circle(32, 28, 5.5, INK) + rrect(19, 40.5, 26, 3.5, 1.75, HOLE)

@small("mx-bootrepair")
def mx_bootrepair_s():
    body = rrect(15, 13, 34, 35, 5, INK) + circle(32, 28, 11, HOLE)
    return body + line(25, 28, 39, 28, INK, 5) + line(32, 21, 32, 35, INK, 5)

@small("mrboom")
def mrboom_s():
    head = rrect(18, 13, 28, 21, 10, INK) + rrect(22, 18, 20, 11, 5, PINK_SOFT)
    return head + rrect(23, 35, 18, 8, 3, INK) + rrect(20, 42, 10, 6, 3, PINK_SOFT) + rrect(34, 42, 10, 6, 3, PINK_SOFT)

@small("mozc")
def mozc_s():
    return (line(19, 20, 40, 18.5, INK, 4.4) + stroke("M28.5 13C28 24 29 35 32.5 45", INK, 4.4) +
            stroke("M40 25C31 32 24 44 19 40.5C15.5 37.5 21 28.5 32 27C42 26 47.5 30 47 36C46.5 41.5 41 44.5 36 45", INK, 4.4))

@small("movmetaedit")
def movmetaedit_s():
    return circle(27, 30, 13, INK) + circle(27, 30, 4.5, HOLE) + stroke("M40 15A15 15 0 0 1 40 45", INK, 5)

@small("mpdevil")
def mpdevil_s():
    horns = (path("M22 27C18 22 17.5 15 20 11C22 16 25 19.5 29.5 21Z", INK) +
             path("M42 27C46 22 46.5 15 44 11C42 16 39 19.5 34.5 21Z", INK))
    return horns + circle(32, 32, 14, INK) + circle(27, 30, 3.5, HOLE) + circle(37, 30, 3.5, HOLE)

@small("mpv")
def mpv_s():
    return circle(CX, CY, 16.5, PURPLE_LIGHT) + circle(CX, CY, 11.5, INK) + \
        poly([(28.5, 23.5), (38, 30), (28.5, 36.5)], HOLE, 2)

@small("musicbrainz")
def musicbrainz_s():
    left = path("M32 13A17 17 0 0 0 32 47Z", DEEP_PURPLE_SOFT)
    right = path("M32 13A17 17 0 0 1 32 47Z", ORANGE)
    return left + right + circle(CX, CY, 12, INK) + circle(29, 34, 4, HOLE) + line(32, 34, 32, 22, HOLE, 3.4, "butt")

@small("multimedia-audio-player")
def audio_player_s():
    return _ring(CX, CY, 15.5, INK, 3.6) + circle(28, 36, 4.5, INK) + line(31.5, 36, 31.5, 21, INK, 3.4, "butt") + \
        stroke("M31.5 22L38 25", INK, 3.4)

@small("multimedia-photo-manager")
def photo_manager_s():
    card = rrect(13, 14, 32, 26, 4, INK)
    hills = path("M16 36L24 26L32 36Z", HOLE, ' stroke="HOLE" stroke-width="2" stroke-linejoin="round"')
    return card + hills + circle(42, 39, 10.5, HOLE) + circle(42, 39, 8.5, INK) + circle(42, 39.5, 3.2, HOLE)

@small("musixmatch")
def musixmatch_s():
    return poly([(15, 17.5), (32, 27), (49, 17.5), (49, 42.5), (32, 33), (15, 42.5)], INK, 3)

@small("multimc")
def multimc_s():
    block = rrect(13, 13, 38, 35, 4, BROWN_LIGHT)
    grass = path("M13 17A4 4 0 0 1 17 13H47A4 4 0 0 1 51 17V24H13Z", LIGHT_BLUE_SOFT)
    inf = stroke("M32 36C28 30 20 30 20 36C20 42 28 42 32 36C36 30 44 30 44 36C44 42 36 42 32 36Z", INK, 4)
    return block + grass + inf

@small("mousepad")
def mousepad_s():
    sheet = rrect(14, 12, 28, 36, 4, INK)
    lines = rrect(18, 20, 18, 4, 2, HOLE) + rrect(18, 28, 12, 4, 2, HOLE) + rrect(18, 36, 14, 4, 2, HOLE)
    pencil = g(rrect(-4, -15, 8, 24, 2, INK) + poly([(-4, 9), (4, 9), (0, 15)], INK, 1.2),
               "translate(42 27) rotate(35)")
    outline = g(rrect(-6.5, -17.5, 13, 35, 3.5, HOLE), "translate(42 27) rotate(35)")
    return sheet + lines + outline + pencil

@small("mpd")
def mpd_s():
    spk = circle(24, 23, 11, INK) + circle(24, 23, 4.5, HOLE)
    mon = rrect(26, 28, 26, 18, 3.5, HOLE) + rrect(28, 30, 22, 14, 2.5, INK)
    return g(spk + mon, "translate(-1 0)")
