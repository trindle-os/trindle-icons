# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 57: preferences-* system icons and pr* apps."""
from lm import *
from glyphs.kit import _gear_j, registry, _star_f

ICONS, SMALL, reg, small = registry()

def _mirror(content):
    return g(content, "translate(64 0) scale(-1 1)")

@reg("preferences-desktop-gaming", ORANGE_DEEP)
def gaming():
    body = path("M20 18H44C48 18 50 21 50.5 25L51 37C51.3 41 48 43 45.5 41L41 37H23L18.5 41"
                "C16 43 12.7 41 13 37L13.5 25C14 21 16 18 20 18Z", INK)
    pad = rrect(18.5, 26, 10, 3.4, 1.7, HOLE) + rrect(21.8, 22.7, 3.4, 10, 1.7, HOLE)
    btn = "".join(circle(x, y, 2.1, HOLE) for x, y in [(40, 23.8), (44, 27.7), (40, 31.6), (36, 27.7)])
    return body + pad + btn

@reg("preferences-desktop-icons", BLUE_DEEP)
def desk_icons():
    return "".join(rrect(x, y, 10.5, 10.5, 2.5, INK)
                   for x, y in [(20.5, 12.5), (33, 12.5), (20.5, 25), (33, 25), (20.5, 37.5)])

def _keyboard(accent=None):
    out = rrect(13, 18, 38, 24, 4.5, INK)
    for i, x in enumerate([19, 25.5, 32, 38.5, 45]):
        out += circle(x, 23.5, 2, accent if accent and i == 4 else HOLE)
    for i, x in enumerate([22.2, 28.7, 35.2, 41.7]):
        out += circle(x, 29.5, 2, accent if accent and i == 2 else HOLE)
    return out + rrect(21, 34, 22, 3.6, 1.8, HOLE)

@reg("preferences-desktop-keyboard", GREY_DARK)
def keyboard():
    return _keyboard()

@reg("preferences-desktop-keyboard-shortcuts", GREY_DARK)
def keyboard_shortcuts():
    return _keyboard(DEEP_ORANGE_LIGHT)

@reg("preferences-desktop-locale", BLUE)
def locale():
    back = rrect(28, 20, 22, 27, 4, BLUE_DARK)
    wen = (line(33, 28, 45, 28, INK, 2.4) + line(39, 23.8, 39, 28, INK, 2.4) +
           stroke("M35.5 30.5C37.5 35.5 41 39 45 41", INK, 2.4) +
           stroke("M42.5 30.5C40.5 35.5 37 39 33 41", INK, 2.4))
    front = rrect(14, 13, 22, 27, 4, INK)
    a = stroke("M19.5 35L25 19L30.5 35", HOLE, 3.2) + line(21.6, 29.5, 28.4, 29.5, HOLE, 2.8)
    return back + wen + front + a

@reg("preferences-desktop-navigation", BLUE_GREY_DEEP)
def navigation():
    ring = f'<circle cx="32" cy="30" r="15.5" fill="none" stroke="{INK}" stroke-width="3.2"/>'
    north = poly([(40.5, 21.5), (34.6, 32.6), (29.4, 27.4)], RED_LIGHT, 1.5)
    south = poly([(23.5, 38.5), (34.6, 32.6), (29.4, 27.4)], INK, 1.5)
    return ring + north + south + circle(32, 30, 1.6, HOLE)

@reg("preferences-desktop-notification-bell", AMBER_DEEP)
def bell():
    dome = path("M32 14.5C25.5 14.5 22 19.5 22 25.5V33L17.5 38.5H46.5L42 33V25.5"
                "C42 19.5 38.5 14.5 32 14.5Z", INK,
                f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    return dome + circle(32, 13, 2.8, INK) + path("M27 42A5 5 0 0 0 37 42Z", INK)

@reg("preferences-desktop-online-accounts", TEAL)
def online_accounts():
    inner = f'<circle cx="32" cy="30" r="5.5" fill="none" stroke="{INK}" stroke-width="4.2"/>'
    outer = stroke("M37.5 24.5V32C37.5 35 39.5 36.5 42 36.5C45 36.5 47 34 47 30"
                   "A15 15 0 1 0 39.5 43", INK, 4.2)
    return inner + outer

@reg("preferences-desktop-peripherals", GREY_DARK)
def peripherals():
    return (rrect(21, 12, 22, 36, 11, INK) + rrect(30, 16.5, 4, 8, 2, HOLE) +
            line(21.5, 28, 42.5, 28, HOLE, 2.2, "butt"))

@reg("preferences-desktop-personal", BLUE)
def personal():
    return circle(32, 21, 7.5, INK) + path(
        "M17 45C17 37 23.5 32 32 32C40.5 32 47 37 47 45Z", INK,
        f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')

@reg("preferences-desktop-remote-desktop", BLUE_DEEP)
def remote_desktop():
    screen = rrect(13, 13, 32, 23, 3.5, INK) + rrect(21, 38, 16, 3.6, 1.8, INK)
    badge = circle(42, 38, 10.5, HOLE) + circle(42, 38, 8.5, TEAL_LIGHT)
    arrows = stroke("M40 34.5L36.8 38L40 41.5", INK, 2.4) + stroke("M44 34.5L47.2 38L44 41.5", INK, 2.4)
    return screen + badge + arrows

@reg("preferences-desktop-screensaver", DEEP_PURPLE)
def screensaver():
    moon = path("M29.27 20.13A12 12 0 1 0 42.87 33.73A10 10 0 0 1 29.27 20.13Z", INK)
    return moon + _star_f(41, 18.5, 6, INK) + _star_f(47.5, 28.5, 3.6, INK)

@reg("preferences-desktop-theme", BLUE_DEEP)
def desk_theme():
    frame = rrect(13, 14, 38, 32, 4.5, INK) + rrect(24, 18, 23.5, 24.5, 2.5, HOLE)
    side = "".join(rrect(16.8, y, 4.4, 4.4, 1.2, HOLE) for y in [18.5, 24.5, 30.5, 36.5])
    return frame + side + rrect(28, 25, 15.5, 10, 2.5, INK)

@reg("preferences-desktop-theme-windowdecorations", GREY_DARK)
def window_decorations():
    win = rrect(13, 14, 38, 32, 4.5, INK) + line(13, 23.5, 51, 23.5, HOLE, 2.4, "butt")
    return win + "".join(circle(x, 18.8, 2, HOLE) for x in [19, 25, 31])

@reg("preferences-desktop-thunderbolt", BLUE_DEEP)
def thunderbolt():
    bolt = poly([(40, 11), (22, 31), (31, 31), (28.3, 40.2), (23.5, 38.5), (25, 49),
                 (33.5, 42.5), (30.2, 41.2), (43, 26), (34, 26)], INK, 1.8)
    return g(bolt, "translate(33.5 30) scale(1.12) translate(-32.5 -30)")

@reg("preferences-desktop-user-password", BLUE_GREY_DEEP)
def user_password():
    shackle = stroke("M24.5 28V22A7.5 7.5 0 0 1 39.5 22V28", INK, 4.2)
    body = rrect(18, 27, 28, 21, 4.5, INK)
    hole = circle(32, 35.5, 3, HOLE) + rrect(30.7, 35.5, 2.6, 7, 1.3, HOLE)
    return shackle + body + hole

@reg("preferences-desktop-wallpaper", LIGHT_BLUE_DEEP)
def wallpaper():
    sheet = path("M17 13H47A2.5 2.5 0 0 1 49.5 15.5V36.5L39.5 46.5H17A2.5 2.5 0 0 1 14.5 44V15.5"
                 "A2.5 2.5 0 0 1 17 13Z", INK)
    fold = path("M49.5 36.5H42A2.5 2.5 0 0 0 39.5 39V46.5Z", LIGHT_BLUE_SOFT)
    sun = circle(24.5, 22.5, 4, HOLE)
    hills = stroke("M19 39L26 32.5L31.5 37L38 30.5L44.5 36", HOLE, 3.2)
    return sheet + fold + sun + hills

@reg("preferences-management-service", DEEP_ORANGE)
def management_service():
    return stroke("M25 15.5V42.5H39", INK, 7)

@reg("preferences-plugin", BLUE_DEEP)
def plugin():
    d = ("M16 19H25.25A4.8 4.8 0 1 1 32.75 19H42V28.25A4.8 4.8 0 1 1 42 35.75V45"
         "H32.8A3.8 3.8 0 0 0 25.2 45H16V35.8A3.8 3.8 0 0 0 16 28.2Z")
    return g(path(d, INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"'),
             "translate(-1 2)")

@reg("preferences-system-bluetooth", INDIGO_DEEP)
def bluetooth():
    return stroke("M24 22.5L40 37L32 44.5V15.5L40 23L24 37.5", INK, 3.8)

@reg("preferences-system-brightness-lock", BLUE_GREY_DEEP)
def brightness_lock():
    sq = rrect(18.5, 16.5, 27, 27, 4, INK)
    star = sq + g(sq, "rotate(45 32 30)")
    return star + circle(32, 30, 9.5, HOLE) + path("M32 23A7 7 0 0 0 32 37Z", INK)

@reg("preferences-system-login", ORANGE_DEEP)
def login():
    body = path("M32 11C37 15 39.5 21 39.5 29V38H24.5V29C24.5 21 27 15 32 11Z", INK)
    fins = (poly([(24.5, 30), (18.5, 37.5), (18.5, 42), (24.5, 39)], INK, 1.5) +
            poly([(39.5, 30), (45.5, 37.5), (45.5, 42), (39.5, 39)], INK, 1.5))
    flame = poly([(28.5, 41), (35.5, 41), (32, 48)], INK, 1.5)
    rocket = body + fins + flame + circle(32, 24.5, 3.5, HOLE)
    return g(rocket, "rotate(45 32 30)")

@reg("preferences-system-network", GREY_DEEP)
def network():
    port = poly([(21.5, 20), (42.5, 20), (42.5, 35.5), (37.5, 35.5), (37.5, 40), (26.5, 40),
                 (26.5, 35.5), (21.5, 35.5)], HOLE, 1.5)
    pins = "".join(rrect(x, 19.5, 2.6, 5, .8, INK) for x in [24.7, 29, 33.3, 37.6])
    return rrect(14.5, 13, 35, 34, 5, INK) + port + pins

@reg("preferences-system-network-connection", DEEP_PURPLE)
def network_connection():
    top = line(18, 23, 44, 23, INK, 4.2) + stroke("M38 17L44.5 23L38 29", INK, 4.2)
    bot = line(46, 37, 20, 37, INK, 4.2) + stroke("M26 31L19.5 37L26 43", INK, 4.2)
    return top + bot

@reg("preferences-system-network-proxy", INDIGO)
def network_proxy():
    globe = circle(32, 23.5, 11.5, INK)
    grid = (stroke("M32 12.5A5 11 0 0 0 32 34.5A5 11 0 0 0 32 12.5", HOLE, 2.2) +
            line(21, 23.5, 43, 23.5, HOLE, 2.2, "butt"))
    stand = rrect(30, 34, 4, 7, 0, INK) + rrect(16, 42, 32, 4, 2, INK) + rrect(27, 39.5, 10, 9, 2.5, INK)
    return globe + grid + stand

@reg("preferences-system-network-share-windows", BLUE)
def share_windows():
    sq = "".join(rrect(x, y, 16, 16, 3.5, INK) for x, y in [(15, 13), (33, 13), (15, 31), (33, 31)])
    arrow = (stroke("M42 21H24V30H40V39H22", HOLE, 3.2) + stroke("M38 17L42 21L38 25", HOLE, 3.2) +
             stroke("M26 35L22 39L26 43", HOLE, 3.2))
    return sq + arrow

def _bubble():
    body = rrect(19, 19, 31, 24, 4.5, INK) + poly([(31, 42), (38, 42), (34.5, 47)], INK, 1.5)
    badge = circle(22, 18, 9.5, HOLE) + circle(22, 18, 7.8, BLUE)
    mark = line(22, 14, 22, 18.5, INK, 2.6) + circle(22, 22.3, 1.5, INK)
    return body + badge + mark

@reg("preferences-system-notifications", GREY_DARK)
def notifications():
    return _bubble()

@reg("preferences-system-notifications-rtl", GREY_DARK)
def notifications_rtl():
    return _mirror(_bubble())

@reg("preferences-system-parental-controls", ORANGE_LIGHT)
def parental():
    adult = (circle(25, 16.5, 4, INK) + rrect(20, 22, 10, 14, 3.5, INK) +
             rrect(20.8, 32, 3.8, 14.5, 1.9, INK) + rrect(25.4, 32, 3.8, 14.5, 1.9, INK))
    child = (circle(39.5, 27, 3.2, INK) + rrect(35.5, 31.5, 8, 9.5, 2.8, INK) +
             rrect(36, 38, 3.2, 8.5, 1.6, INK) + rrect(40, 38, 3.2, 8.5, 1.6, INK))
    return adult + child + line(29, 27.5, 35.5, 33.5, INK, 2.6)

@reg("preferences-system-power", AMBER_DEEP)
def power():
    return poly([(35.5, 12), (20, 33), (31, 33), (28, 48), (44, 26), (33, 26)], INK, 2.2)

@reg("preferences-system-privacy", BLUE_GREY_DEEP)
def privacy():
    drop = path("M32 18.5L37.6 25.3A8.7 8.7 0 1 1 26.4 25.3Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return circle(32, 30, 16, BLUE_GREY_LIGHT) + drop

@reg("preferences-system-search", BLUE_DEEP)
def search():
    return (f'<circle cx="29" cy="27" r="9.5" fill="none" stroke="{INK}" stroke-width="4.6"/>'
            + line(36, 34, 45, 43, INK, 6))

@reg("preferences-system-services", DEEP_PURPLE_LIGHT)
def services():
    gear = _gear_j(32, 30, 17, 13.2, 8, INK) + circle(32, 30, 9.5, HOLE)
    tools = (line(27, 25, 37, 35, INK, 3) + line(37, 25, 27, 35, INK, 3) +
             circle(26.5, 24.5, 2.8, INK) + circle(37.5, 24.5, 2.3, INK))
    return gear + tools

@reg("preferences-system-splash", DEEP_PURPLE)
def splash():
    return "".join(circle(*pt(32, 30, 12, -90 + 45 * i), 1.8 + .25 * i, INK) for i in range(8))

@reg("preferences-system-time", ORANGE_DEEP)
def time():
    hands = stroke("M32 30L38.5 19.5", HOLE, 3.2) + stroke("M32 30L21.5 35.5", HOLE, 3.2)
    return (circle(32, 30, 16.5, INK) + hands + line(32, 30, 39.5, 38, RED, 2.2) +
            circle(32, 30, 2.4, HOLE))

@reg("preferences-system-windows", GREY_DEEP)
def sys_windows():
    back = rrect(22, 13, 28, 23, 3.5, INK) + line(22, 19, 50, 19, HOLE, 2.2, "butt")
    front = (rrect(14, 24, 28, 23, 3.5, INK, f' stroke="{HOLE}" stroke-width="2.5"') +
             line(15.3, 30, 40.7, 30, HOLE, 2.2, "butt"))
    return back + front

@reg("preferences-system-windows-move", BLUE_DEEP)
def windows_move():
    return (rrect(13, 14, 17.5, 13, 3, INK) + rrect(33.5, 14, 17.5, 13, 3, INK) +
            rrect(23.25, 32, 17.5, 13, 3, INK))

@reg("preferences-ubuntu-panel", PINK_DARK)
def ubuntu_panel():
    frame = rrect(13, 14, 38, 32, 4.5, INK) + rrect(24, 18, 23.5, 24.5, 2.5, HOLE)
    return frame + "".join(rrect(16.8, y, 4.4, 4.4, 1.2, HOLE) for y in [18.5, 24.5, 30.5, 36.5])

@reg("preferences-web-browser-cookies", ORANGE_DEEP)
def cookies():
    cookie = path("M39.59 15.9A16 16 0 1 0 46.61 23.46A6.5 6.5 0 0 1 39.59 15.9Z", INK)
    chips = "".join(circle(x, y, r, HOLE) for x, y, r in
                    [(25, 24, 2.8), (35, 33.5, 2.8), (24, 37, 2.4), (37.5, 23.5, 2.2), (30, 41, 1.9)])
    return cookie + chips

@reg("premid", INDIGO_LIGHT)
def premid():
    card = rrect(13, 17, 38, 26, 5, INK)
    play = poly([(20, 24), (20, 36), (29, 30)], HOLE, 1.8)
    lines = rrect(33, 23.5, 12, 3, 1.5, HOLE) + rrect(33, 28.5, 12, 3, 1.5, HOLE) + rrect(33, 33.5, 8, 3, 1.5, HOLE)
    return card + play + lines

@reg("prepros", CYAN_DEEP)
def prepros():
    gear = circle(32, 30, 12.5, INK) + "".join(circle(*pt(32, 30, 13.5, -90 + 60 * i), 4.5, INK) for i in range(6))
    p = (f'<circle cx="34" cy="29" r="4.8" fill="none" stroke="{HOLE}" stroke-width="3.8"/>'
         + line(29.2, 25, 29.2, 40, HOLE, 3.8))
    return gear + p

@reg("prey", RED_DEEP)
def prey():
    body = poly([(32, 12), (35, 22), (35, 36), (32, 47), (29, 36), (29, 22)], INK, 1.5)
    wing = poly([(29.5, 24), (22, 17), (13.5, 12), (15.5, 20), (13, 21), (17.5, 27),
                 (15, 28.5), (21, 33), (19.5, 35.5), (29, 36)], INK, 1.5)
    cut_ = stroke("M28.5 26L21.5 22", HOLE, 2) + stroke("M28.5 31L22 29.5", HOLE, 2)
    half = wing + cut_
    return body + half + _mirror(half)

@reg("prison-architect", ORANGE_DEEP)
def prison_architect():
    suit = path("M14 48C14 37 21 31 32 31C43 31 50 37 50 48Z", INK)
    stripe = rrect(30.2, 35, 3.6, 13, 0, HOLE)
    head = circle(32, 21, 8.5, INK) + path("M23.7 19A8.5 8.5 0 0 1 40.3 19Z", ORANGE_DARK)
    return suit + stripe + head

@reg("pritunl_client_electron", BLUE_GREY_DARK)
def pritunl():
    return (f'<circle cx="32.5" cy="27.5" r="7" fill="none" stroke="{INK}" stroke-width="6"/>'
            + line(25.5, 22, 25.5, 45, INK, 6))

def _m():
    return stroke("M19 44L24 16L32 36L40 16L45 44", INK, 6)

@reg("projectM", BLUE_DEEP)
def projectm():
    return _m()

@reg("prjm16-transparent", BLUE_DEEP)
def prjm16():
    burst = poly([pt(32, 31, 18.5 if i % 2 == 0 else 11, -90 + 22.5 * i) for i in range(16)], INDIGO_DARK, 1)
    return burst + _m()

@reg("project-zomboid", RED_DARK)
def project_zomboid():
    head = circle(32, 15.5, 4.5, INK)
    body = stroke("M32 21.5L31 32", INK, 7)
    arms = stroke("M33 22.5L39 27L41 31.5", INK, 3.6) + stroke("M29.5 23L26 32", INK, 3.6)
    legs = stroke("M30 33L26.5 40L24.5 47", INK, 4.4) + stroke("M32 33L36 39.5L37.5 47", INK, 4.4)
    return head + body + arms + legs

@reg("projecteur", GREY_DEEP)
def projecteur():
    cone = path("M28 17H36L46 40A14 4.5 0 0 1 18 40Z", INK)
    rim = stroke("M18 40A14 4.5 0 0 1 46 40", HOLE, 2.2)
    rays = line(30.5, 20, 26, 35.5, HOLE, 2) + line(33.5, 20, 38, 35.5, HOLE, 2)
    head = g(rrect(25.5, 11, 13, 6.5, 2.5, INK), "rotate(-8 32 14)")
    return cone + rim + rays + head

@reg("pronterface", RED_DEEP)
def pronterface():
    colon = circle(18.5, 24, 3, INK) + circle(18.5, 36, 3, INK)
    dash = line(24.5, 30, 29, 30, INK, 3.8)
    p = (f'<circle cx="40.5" cy="30" r="5.5" fill="none" stroke="{INK}" stroke-width="4"/>'
         + line(35, 24.5, 35, 45, INK, 4))
    return colon + dash + p

@reg("protege", DEEP_ORANGE_DEEP)
def protege():
    swoosh = stroke("M31 19C41 12.5 49 10.5 49 14.5C49 24 45 38 39.5 47", DEEP_ORANGE_SOFT, 5)
    drop = stroke("M15 30C21 24 30 20 37.5 20A10 10 0 0 1 37.5 40C30 40 21 36 15 30Z", INK, 5)
    return swoosh + drop

def _keyboard_s(accent=None):
    out = rrect(12, 17, 40, 26, 5, INK)
    for i, x in enumerate([20, 28, 36, 44]):
        out += rrect(x - 2.5, 21.5, 5, 5, 1.5, accent if accent and i == 3 else HOLE)
    return out + rrect(19.5, 32, 25, 5, 2.5, HOLE)

@small("preferences-desktop-keyboard")
def keyboard_s():
    return _keyboard_s()

@small("preferences-desktop-keyboard-shortcuts")
def keyboard_shortcuts_s():
    return _keyboard_s(DEEP_ORANGE_LIGHT)

@small("preferences-desktop-locale")
def locale_s():
    return (rrect(28, 20, 22, 27, 4, BLUE_DARK) + rrect(14, 13, 24, 29, 4.5, INK) +
            stroke("M19.5 37L26 19.5L32.5 37", HOLE, 4) + line(22.3, 31, 29.7, 31, HOLE, 3.6))

@small("preferences-desktop-navigation")
def navigation_s():
    ring = f'<circle cx="32" cy="30" r="15.5" fill="none" stroke="{INK}" stroke-width="3.4"/>'
    north = poly([(41, 21), (35.5, 33.5), (28.5, 26.5)], RED_LIGHT, 1.5)
    south = poly([(23, 39), (35.5, 33.5), (28.5, 26.5)], INK, 1.5)
    return ring + north + south

@small("preferences-desktop-online-accounts")
def online_accounts_s():
    inner = f'<circle cx="31" cy="30" r="5.5" fill="none" stroke="{INK}" stroke-width="4.4"/>'
    outer = stroke("M37.5 24V33C37.5 36 40 37 42.5 37C45.5 37 47.5 34 47.5 30"
                   "A15.5 15.5 0 1 0 39.5 43.5", INK, 3.6)
    return inner + outer

@small("preferences-desktop-remote-desktop")
def remote_desktop_s():
    screen = rrect(12, 13, 34, 25, 4, INK) + rrect(20, 40, 18, 4, 2, INK)
    return screen + circle(42, 38, 11, HOLE) + circle(42, 38, 9, TEAL_LIGHT)

@small("preferences-desktop-theme")
def desk_theme_s():
    frame = rrect(13, 14, 38, 32, 4.5, INK) + rrect(25, 18, 22.5, 24.5, 2.5, HOLE)
    return frame + rrect(29, 25, 14.5, 10, 2.5, INK)

@small("preferences-desktop-wallpaper")
def wallpaper_s():
    sheet = rrect(14, 13, 36, 34, 4, INK)
    return sheet + circle(24, 22.5, 4.5, HOLE) + path("M14 42L25 31L32 37L39 30L50 40V43H14Z", HOLE)

@small("preferences-system-network")
def network_s():
    port = poly([(20.5, 20), (43.5, 20), (43.5, 35), (38, 35), (38, 40), (26, 40),
                 (26, 35), (20.5, 35)], HOLE, 2)
    return rrect(14, 13, 36, 34, 5, INK) + port

@small("preferences-system-network-proxy")
def network_proxy_s():
    globe = circle(32, 23, 12, INK) + line(20, 23, 44, 23, HOLE, 3, "butt")
    return globe + rrect(29.5, 34, 5, 8, 0, INK) + rrect(14, 41, 36, 5, 2.5, INK)

@small("preferences-system-network-share-windows")
def share_windows_s():
    top = line(17, 22, 44, 22, INK, 5) + stroke("M38 15.5L45 22L38 28.5", INK, 5)
    bot = line(47, 38, 20, 38, INK, 5) + stroke("M26 31.5L19 38L26 44.5", INK, 5)
    return top + bot

def _bubble_s():
    body = rrect(18, 18, 33, 25, 5, INK) + poly([(31, 42), (39, 42), (35, 47.5)], INK, 1.5)
    return body + circle(21, 18, 10.5, HOLE) + circle(21, 18, 8.5, BLUE) + line(21, 14, 21, 20, INK, 3.4)

@small("preferences-system-notifications")
def notifications_s():
    return _bubble_s()

@small("preferences-system-notifications-rtl")
def notifications_rtl_s():
    return _mirror(_bubble_s())

@small("preferences-system-parental-controls")
def parental_s():
    adult = circle(24.5, 16, 5, INK) + rrect(18.5, 23, 12, 24, 4, INK)
    child = circle(40, 27.5, 4, INK) + rrect(35, 33.5, 10, 13.5, 3.5, INK)
    return adult + child

@small("preferences-system-privacy")
def privacy_s():
    drop = path("M32 16L38.5 24A9.8 9.8 0 1 1 25.5 24Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    return circle(32, 30, 17, BLUE_GREY_LIGHT) + drop

@small("preferences-system-services")
def services_s():
    return _gear_j(32, 30, 17.5, 13.5, 8, INK) + circle(32, 30, 6.5, HOLE)

@small("preferences-system-splash")
def splash_s():
    return "".join(circle(*pt(32, 30, 12.5, -90 + 60 * i), 2.6 + .45 * i, INK) for i in range(6))

@small("preferences-system-time")
def time_s():
    return (circle(32, 30, 17, INK) + stroke("M32 30L38 19", HOLE, 4.2) +
            stroke("M32 30L22 35", HOLE, 4.2))

@small("preferences-web-browser-cookies")
def cookies_s():
    cookie = path("M39.59 15.9A16 16 0 1 0 46.61 23.46A6.5 6.5 0 0 1 39.59 15.9Z", INK)
    return cookie + circle(25, 25, 3.8, HOLE) + circle(36, 34, 3.8, HOLE) + circle(24.5, 38, 3, HOLE)

@small("premid")
def premid_s():
    card = rrect(12, 16, 40, 28, 5.5, INK)
    play = poly([(19, 23), (19, 37), (29, 30)], HOLE, 2)
    return card + play + rrect(33, 23.5, 13, 4.5, 2.25, HOLE) + rrect(33, 32, 13, 4.5, 2.25, HOLE)

@small("prepros")
def prepros_s():
    gear = circle(32, 30, 13, INK) + "".join(circle(*pt(32, 30, 13.5, -90 + 60 * i), 4.8, INK) for i in range(6))
    p = (f'<circle cx="34.5" cy="29" r="5" fill="none" stroke="{HOLE}" stroke-width="4.6"/>'
         + line(29, 24, 29, 40, HOLE, 4.6))
    return gear + p

@small("prey")
def prey_s():
    body = poly([(32, 12), (35.5, 22), (35.5, 36), (32, 47), (28.5, 36), (28.5, 22)], INK, 1.5)
    wing = poly([(29.5, 24), (13, 11.5), (14, 27), (29, 37)], INK, 2)
    return body + wing + _mirror(wing)

@small("projecteur")
def projecteur_s():
    cone = path("M27 17H37L47 40A15 5 0 0 1 17 40Z", INK)
    return cone + rrect(24.5, 10, 15, 7, 3, INK) + stroke("M17.5 40A14.5 4.5 0 0 1 46.5 40", HOLE, 3)

@small("prjm16-transparent")
def prjm16_s():
    burst = poly([pt(32, 31, 19 if i % 2 == 0 else 12.5, -90 + 30 * i) for i in range(12)], INDIGO_DARK, 1)
    return burst + _m()
