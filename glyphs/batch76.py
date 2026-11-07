# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 76: yuzu-ea to zynaddsubfx."""
from lm import *
from glyphs.kit import ellipse, ering, registry

ICONS, SMALL, reg, small = registry()

@reg("yuzu-ea", GREY_DARK)
def yuzu_ea():
    left = stroke("M29 14.5A11.5 11.5 0 0 0 29 37.5V14.5", AMBER_LIGHT, 4)
    right = stroke("M35 22.5A11.5 11.5 0 0 1 35 45.5V22.5", INK, 4)
    return left + right

@reg("zandronum", BLUE_GREY_DEEP)
def zandronum():
    helmet = path("M15.5 26C15.5 16 22.5 12 32 12C41.5 12 48.5 16 48.5 26V31"
                  "L42.5 47.5H21.5L15.5 31Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    visor = path("M15.5 24.5H48.5V29C44 29 41.5 33 40 43C39 37 36.5 33.5 32 33.5"
                 "C27.5 33.5 25 37 24 43C22.5 33 20 29 15.5 29Z", LIGHT_BLUE_SOFT)
    return helmet + visor

@reg("zdoom", RED_DEEP)
def zdoom():
    z = stroke("M15.5 21.5H28L15.5 38.5H28", INK, 4.6)
    d = stroke("M34.5 21.5V38.5H40A8.5 8.5 0 0 0 40 21.5Z", INK, 4.6)
    return z + d

@reg("zen-bound-2", TEAL_DEEP)
def zen_bound_2():
    bird = poly([(32, 13), (35.5, 20), (48.5, 15), (45, 31), (36, 33.5), (32, 41),
                 (28, 33.5), (19, 31), (15.5, 15), (28.5, 20)], INK, 2.5)
    beak = line(33, 13.5, 39, 13.5, INK, 2.4)
    tail = poly([(26.5, 41), (37.5, 41), (32, 48)], INK, 2.5)
    rope = (line(24.5, 22.5, 39.5, 37, AMBER_DARK, 4) +
            line(39.5, 22.5, 24.5, 37, AMBER_DARK, 4))
    return bird + beak + tail + rope

@reg("zombie-panic-source", DEEP_ORANGE_DEEP)
def zombie_panic():
    out = ""
    for k in range(3):
        a = -90 + 120 * k
        ox, oy = pt(CX, CY + 1, 7.5, a)
        out += circle(ox, oy, 8.8, INK)
    for k in range(3):
        a = -90 + 120 * k
        ix, iy = pt(CX, CY + 1, 10, a)
        out += circle(ix, iy, 6.4, HOLE)
    out += circle(CX, CY + 1, 7, "none", f' stroke="{INK}" stroke-width="2.4"')
    out += circle(CX, CY + 1, 3, HOLE)
    for k in range(3):
        a = -90 + 120 * k
        ex, ey = pt(CX, CY + 1, 11, a)
        out += line(CX, CY + 1, ex, ey, HOLE, 1.6)
    return out

@reg("zsnes", BLUE_GREY_DARK)
def zsnes():
    return (ellipse(32.5, 18.5, 8.5, 7.5, INDIGO_LIGHT, -15) +
            ellipse(44, 29.5, 7.5, 7, RED) +
            ellipse(20, 31.5, 8.5, 6.2, LIGHT_BLUE_SOFT, -10) +
            ellipse(33, 42, 8.5, 6.2, YELLOW, -10))

@reg("zaz", INDIGO_DEEP)
def zaz():
    ball = circle(32, 21.5, 10, INK)
    cradle = stroke("M17 32.5C22 42 42 42 47 32.5", INK, 4)
    base = ellipse(32, 45.5, 8.5, 3, YELLOW)
    return ball + cradle + base

@reg("zanshin", BLUE_GREY_DARK)
def zanshin():
    frame = cut("M20 13H44A5 5 0 0 1 49 18V42A5 5 0 0 1 44 47H20A5 5 0 0 1 15 42V18A5 5 0 0 1 20 13Z"
                "M22 18H42A2 2 0 0 1 44 20V40A2 2 0 0 1 42 42H22A2 2 0 0 1 20 40V20A2 2 0 0 1 22 18Z", INK)
    ring = cut(cpath(32, 30, 8.5) + cpath(32, 30, 5.5), CYAN)
    return frame + ring + circle(32, 30, 2.8, INK)

@reg("zaproxy", BLUE_DEEP)
def zaproxy():
    return poly([(17, 12.5), (37, 12.5), (30.5, 21), (41, 21.5), (35, 29.5),
                 (48.5, 47.5), (25.5, 32.5), (32, 31.5), (21.5, 24), (28, 22.5)], INK, 2)

@reg("zart", DEEP_PURPLE_DEEP)
def zart():
    brim = ellipse(27, 35.5, 13, 4.5, INK, -12)
    crown = path("M17 34L19 17.5C25 14.5 31 14.5 35 17.5L37.5 31Z", INK,
                 f' stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"')
    band = path("M17.8 28C23 26 30 25.5 36.2 26.5L36.8 29.5C30 28.5 23.5 29 17.4 31Z", HOLE)
    star = poly([pt(41, 15, 5.5 if k % 2 == 0 else 2.2, -90 + 45 * k) for k in range(8)], INK, 1)
    cam = rrect(36, 34, 13, 13, 3.5, PURPLE_SOFT) + circle(42.5, 39.5, 3, INK) + circle(42.5, 39.5, 1.3, PURPLE_SOFT)
    return brim + crown + band + star + cam

@reg("zbstudio", DEEP_ORANGE_DEEP)
def zbstudio():
    arms = line(15, 18, 15, 38, INK, 2.8) + line(49, 18, 49, 38, INK, 2.8)
    head = rrect(25, 11.5, 14, 14, 3, INK) + cut(cpath(32, 18.5, 4.2) + cpath(32, 18.5, 1.8), HOLE)
    body = path("M22 27H42A6 6 0 0 1 48 33V40C43 44 37 46 32 46C27 46 21 44 16 40V33A6 6 0 0 1 22 27Z", INK)
    shoulders = rrect(14, 31, 36, 6, 3, INK)
    eyes = circle(25.5, 36, 3.6, HOLE) + circle(38.5, 36, 3.6, HOLE)
    return arms + head + shoulders + body + eyes

@reg("zeal", DEEP_ORANGE_DEEP)
def zeal():
    book = rrect(16.5, 12, 31, 36, 4, INK)
    spine = line(23.5, 12, 23.5, 48, HOLE, 2.4, "butt")
    z = stroke("M28.5 20.5H41.5L28.5 39.5H41.5", HOLE, 4.2)
    return book + spine + z

@reg("zed", BLUE_GREY_DEEP)
def zed():
    outer = stroke("M15.5 23V14.5H42", INK, 3.4) + stroke("M48.5 37V45.5H22", INK, 3.4)
    mid = stroke("M21 19.5H43L21 40.5H43", INK, 3.4)
    inner = stroke("M29.5 30H35", INK, 3.4)
    return outer + mid + inner

@reg("zegrapher", CYAN_DEEP)
def zegrapher():
    w = 3.2
    wings = (ering(23.5, 21.5, 8.5, 5.5, INK, w, 40) + ering(40.5, 21.5, 8.5, 5.5, INK, w, -40) +
             ering(25.5, 38.5, 6.5, 4.2, INK, w, -45) + ering(38.5, 38.5, 6.5, 4.2, INK, w, 45))
    body = rrect(29.8, 22, 4.4, 17, 2.2, INK)
    return wings + body

@reg("zen-browser", DEEP_ORANGE_LIGHT)
def zen_browser():
    return (cut(cpath(CX, CY, 16.5) + cpath(CX, CY, 13), INK) +
            cut(cpath(CX, CY, 10) + cpath(CX, CY, 6.5), INK) + circle(CX, CY, 3.5, INK))

@reg("zenbooru", CYAN_DEEP)
def zenbooru():
    brow = stroke("M14.5 17.5Q32 10 49.5 16", INK, 4)
    eye = path("M16 23C24 19.5 40 19 48 22.5V38C40 45 24 45 16 38Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    iris = circle(33, 31.5, 8, CYAN_LIGHT) + circle(33, 31.5, 4.5, CYAN_DARK)
    return brow + eye + iris

@reg("zenkit", PINK_LIGHT)
def zenkit():
    w = 2.8
    outline = stroke("M32 12.5L46.5 30L32 47.5L17.5 30Z", INK, w)
    mid = line(17.5, 30, 46.5, 30, INK, w)
    facets = stroke("M32 12.5L27 30L32 47.5L37 30Z", INK, w)
    return outline + mid + facets

@reg("zerotier-gui", ORANGE)
def zerotier():
    return (line(16, 14.5, 48, 14.5, INK, 3.4) + line(32, 14.5, 32, 47, INK, 3.4) +
            circle(32, 32, 11, "none", f' stroke="{INK}" stroke-width="3.4"'))

@reg("zettlr", TEAL_LIGHT)
def zettlr():
    return stroke("M25 13.5H38.5C29 19 22.5 26 22.5 33C22.5 38.5 27 40 32 40.5"
                  "C37 41 38.5 44 35.5 47.5", INK, 4.6)

@reg("zevdocs", AMBER_DARK)
def zevdocs():
    lip = rrect(24.5, 11.5, 15, 4, 2, INK)
    flask = path("M28 15V24.5L17.5 42.5C16.3 44.8 17.5 47.5 20.5 47.5H43.5"
                 "C46.5 47.5 47.7 44.8 46.5 42.5L36 24.5V15Z", INK)
    leaves = (path("M20.5 42C23 35.5 29 33.5 33.5 36.5C30 41.5 25 43.5 20.5 42Z", HOLE) +
              path("M30.5 37.5C33 31 39 29 43.5 32C40 37 35 39 30.5 37.5Z", HOLE))
    return lip + flask + leaves

@reg("ziggurat", ORANGE_DEEP)
def ziggurat():
    return path("M22 12.5H47.5C41 20 34.5 27.5 28 35.5C33 34 38 33 43 32.5"
                "C34 37.5 25.5 42 16.5 48C22 38 29 28.5 36.5 19.5H20.5Z", INK,
                f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')

@reg("zim", INDIGO)
def zim():
    globe = circle(31, 31, 16.5, INDIGO_DARK)
    feather = path("M31 30C35 21 42 14.5 50.5 12C48.5 21 42 28 34 32Z", GREY)
    nib = path("M34.5 27.5L28 25.5C24.5 30 21 36 17 45.5C25 40 31 36.5 36 33.5Z", INK,
               f' stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"')
    slit = line(20.5, 42.5, 27.5, 34, INDIGO_DARK, 1.8) + circle(28.5, 32.5, 2.3, INDIGO_DARK)
    return globe + feather + nib + slit

@reg("zint", BLUE_GREY_DEEP)
def zint():
    top = path("M16 13H48V24A5 5 0 0 1 43 29H37.5V23H43V19H16Z", INK)
    bot = path("M48 47H16V36A5 5 0 0 1 21 31H26.5V37H21V41H48Z", INK)
    return top + bot + circle(32, 30, 3.8, INK)

@reg("zmninja", GREY_DARK)
def zmninja():
    head = circle(CX, CY, 16.5, INK)
    band = g(rrect(14, 22.5, 36, 11, 1, HOLE), "rotate(-6 32 28)")
    eyes = (poly([(21, 26), (29, 28.5), (27.5, 31), (22, 29.5)], INK, 1.2) +
            poly([(43, 24.5), (35, 27.5), (36.5, 30), (42, 28)], INK, 1.2))
    mouth = line(26, 40, 38, 38.5, HOLE, 2.4)
    return head + band + eyes + mouth

@reg("zoho-mail-desktop", BLUE_DEEP)
def zoho_mail():
    house = stroke("M16.5 26L32 13.5L47.5 26V44A3 3 0 0 1 44.5 47H19.5A3 3 0 0 1 16.5 44Z", INK, 3.6)
    top = stroke("M24.5 34V29H39.5V34", ORANGE_LIGHT, 3.6)
    bot = stroke("M24.5 34V39.5H39.5V34", INK, 3.6)
    return house + top + bot

@reg("zrythm", RED)
def zrythm():
    frame = cut("M15.5 13.5H48.5V46.5H15.5Z" "M20.5 18.5V41.5H43.5V18.5Z", INK)
    z = stroke("M24.5 23H39.5L24.5 37H39.5", INK, 4)
    return frame + z

@reg("zulip", INDIGO_LIGHT)
def zulip():
    return circle(CX, CY, 16.5, INK) + stroke("M24.5 21.5H39.5L24.5 38.5H39.5", HOLE, 4.6)

@reg("zuluCrypt", RED_DEEP)
def zulucrypt():
    z = stroke("M15.5 24H27L15.5 38H27", INK, 4)
    c = stroke("M46.5 25.5A8.5 8.5 0 1 0 46.5 36.5", INK, 4)
    return z + c

@reg("zuluMount", RED_DEEP)
def zulumount():
    z = stroke("M14.5 24H25L14.5 38H25", INK, 4)
    m = stroke("M31 38V23.5L39.5 32L48 23.5V38", INK, 4)
    return z + m

@reg("zumaudio", GREY_DARK)
def zumaudio():
    return stroke("M22 16.5H42.5L22.5 43.5H43", INK, 6.5)

@reg("zynaddsubfx", BLUE_GREY_DARK)
def zynaddsubfx():
    outline = poly([(15, 13.5), (49, 16.5), (37.5, 30), (49, 46.5), (15, 44.5), (26.5, 30)], INK, 3)
    blue = poly([(20, 17), (44.5, 19.5), (37.5, 27.5)], LIGHT_BLUE, 1.5)
    green = poly([(26.5, 32.5), (44.5, 43.5), (20, 41.5)], TEAL_LIGHT, 1.5)
    return outline + blue + green

@small("zanshin")
def zanshin_s():
    frame = cut("M20 13H44A5 5 0 0 1 49 18V42A5 5 0 0 1 44 47H20A5 5 0 0 1 15 42V18A5 5 0 0 1 20 13Z"
                "M23 19H41V41H23Z", INK)
    return frame + circle(32, 30, 6, CYAN)

@small("zart")
def zart_s():
    brim = ellipse(29, 38, 16, 5, INK, -10)
    crown = path("M18 37L20.5 16C27 13 33 13 38 16L41 34Z", INK,
                 f' stroke="{INK}" stroke-width="3" stroke-linejoin="round"')
    return brim + crown + path("M18.8 28C25 25.5 33 25 39.7 26.5L40.4 31C33 29.5 25.5 30 18.2 33Z", HOLE)

@small("zbstudio")
def zbstudio_s():
    head = rrect(24.5, 11, 15, 13, 3, INK) + circle(32, 17.5, 3.6, HOLE)
    body = rrect(15, 27, 34, 20, 7, INK)
    eyes = circle(25, 37, 4.2, HOLE) + circle(39, 37, 4.2, HOLE)
    return head + body + eyes

@small("zeal")
def zeal_s():
    return rrect(16, 12, 32, 36, 4, INK) + stroke("M24 20.5H40L24 39.5H40", HOLE, 5)

@small("zed")
def zed_s():
    return (stroke("M15.5 24V14.5H40", INK, 4.5) + stroke("M48.5 36V45.5H24", INK, 4.5) +
            stroke("M23 21.5H41L23 38.5H41", INK, 4.5))

@small("zegrapher")
def zegrapher_s():
    wings = (ellipse(23, 21, 8.5, 6, INK, 40) + ellipse(41, 21, 8.5, 6, INK, -40) +
             ellipse(25, 39, 7, 5, INK, -45) + ellipse(39, 39, 7, 5, INK, 45))
    return wings + line(32, 22, 32, 40, HOLE, 2.4)

@small("zen-bound-2")
def zen_bound_2_s():
    bird = poly([(32, 14), (48.5, 15), (44, 32), (32, 46), (20, 32), (15.5, 15)], INK, 3)
    rope = (line(24, 21.5, 40, 37.5, AMBER_DARK, 4.5) + line(40, 21.5, 24, 37.5, AMBER_DARK, 4.5))
    return bird + rope

@small("zen-browser")
def zen_browser_s():
    return cut(cpath(CX, CY, 16.5) + cpath(CX, CY, 12), INK) + circle(CX, CY, 6.5, INK)

@small("zenkit")
def zenkit_s():
    return (stroke("M32 12.5L46.5 30L32 47.5L17.5 30Z", INK, 3.4) +
            line(17.5, 30, 46.5, 30, INK, 3.4))

@small("zerotier-gui")
def zerotier_s():
    return (line(15.5, 14, 48.5, 14, INK, 4) + line(32, 14, 32, 48, INK, 4) +
            circle(32, 32, 11.5, "none", f' stroke="{INK}" stroke-width="3.6"'))

@small("zevdocs")
def zevdocs_s():
    flask = path("M27 12V24.5L16.5 42.5C15.3 44.8 16.5 47.5 19.5 47.5H44.5"
                 "C47.5 47.5 48.7 44.8 47.5 42.5L37 24.5V12Z", INK)
    return flask + path("M21 43C24 35 32 32 40 36C34 43 27 45 21 43Z", HOLE)

@small("zim")
def zim_s():
    globe = circle(31, 31, 16.5, INDIGO_DARK)
    feather = path("M30 31C34 21 42 14.5 51 12C49 22 42 29 33 33Z", LIGHT_BLUE_LIGHT)
    nib = path("M35 27L27.5 24.5C24 30 20.5 36 16.5 46C25 40.5 31 37 37 33.5Z", INK)
    return globe + feather + nib

@small("zmninja")
def zmninja_s():
    head = circle(CX, CY, 16.5, INK)
    band = g(rrect(14, 22, 36, 12, 1, HOLE), "rotate(-6 32 28)")
    eyes = circle(25, 28.5, 2.8, INK) + circle(39, 27, 2.8, INK)
    return head + band + eyes

@small("zombie-panic-source")
def zombie_panic_s():
    out = ""
    for k in range(3):
        a = -90 + 120 * k
        out += circle(*pt(CX, CY + 1, 8, a), 9, INK)
    for k in range(3):
        a = -90 + 120 * k
        out += circle(*pt(CX, CY + 1, 11, a), 5.8, HOLE)
    return out + circle(CX, CY + 1, 3.5, HOLE)

@small("zrythm")
def zrythm_s():
    frame = cut("M15 13H49V47H15Z" "M21 19V41H43V19Z", INK)
    return frame + stroke("M26 25H38L26 35H38", INK, 4.5)

@small("zuluCrypt")
def zulucrypt_s():
    return stroke("M14.5 23H27L14.5 38H27", INK, 5) + stroke("M47.5 25A9 9 0 1 0 47.5 37", INK, 5)

@small("zuluMount")
def zulumount_s():
    return stroke("M13.5 23H24.5L13.5 38H24.5", INK, 5) + stroke("M30 38V23.5L39.5 32.5L49 23.5V38", INK, 5)

@small("zynaddsubfx")
def zynaddsubfx_s():
    blue = poly([(15, 14), (49, 17), (36, 30)], LIGHT_BLUE, 3)
    green = poly([(28, 30), (49, 46), (15, 44)], TEAL_SOFT, 3)
    return blue + green
