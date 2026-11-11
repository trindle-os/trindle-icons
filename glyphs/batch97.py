# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 97: Randovania to RecentFilter."""
from lm import (
    AMBER, AMBER_DARK, AMBER_DEEP, AMBER_LIGHT, AMBER_SOFT, BLUE, BLUE_DARK, BLUE_DEEP,
    BLUE_GREY, BLUE_GREY_DARK, BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_GREY_SOFT, BLUE_LIGHT,
    BLUE_SOFT, BROWN, BROWN_DARK, BROWN_DEEP, BROWN_LIGHT, BROWN_SOFT, circle, CYAN, CYAN_DARK,
    CYAN_DEEP, CYAN_LIGHT, CYAN_SOFT, DEEP_ORANGE, DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP,
    DEEP_ORANGE_LIGHT, DEEP_ORANGE_SOFT, DEEP_PURPLE, DEEP_PURPLE_DARK, DEEP_PURPLE_DEEP,
    DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, GREY, GREY_DARK, GREY_DEEP, GREY_LIGHT, GREY_SOFT,
    HOLE, INDIGO, INDIGO_DARK, INDIGO_DEEP, INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE,
    LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP, LIGHT_BLUE_LIGHT, LIGHT_BLUE_SOFT, ORANGE, ORANGE_DARK,
    ORANGE_DEEP, ORANGE_LIGHT, ORANGE_SOFT, path, PINK, PINK_DARK, PINK_DEEP, PINK_LIGHT,
    PINK_SOFT, poly, pt, PURPLE, PURPLE_DARK, PURPLE_DEEP, PURPLE_LIGHT, PURPLE_SOFT, RED,
    RED_DARK, RED_DEEP, RED_LIGHT, RED_SOFT, TEAL, TEAL_DARK, TEAL_DEEP, TEAL_LIGHT, TEAL_SOFT,
    YELLOW, YELLOW_DARK, YELLOW_DEEP, YELLOW_LIGHT, YELLOW_SOFT,
)
from glyphs.kit import (
    arrowhead, asterisk, cells, crescent, dim, ell, ellring, fit, hexring, hs, hx, ink_circle, ink_rrect, ink_stroke, registry, ring_c, rot, spiral, star4, star5)

ICONS, SMALL, reg, _ = registry()


@reg("io.github.randovania.Randovania", PURPLE_SOFT)
def randovania():
    out = ink_circle(32, 32, 15) + rot(ellring(32, 32, 27, 8, 8, HOLE), -22, 32, 32) + rot(ellring(32, 32, 27, 8, 4), -22, 32, 32)
    return fit(out + star4(52, 10, 7), 0.540, 32.0, 25.6)


@reg("io.github.rdybka.vht", ORANGE_DARK)
def vht():
    out = ""
    for x in (6, 26, 46):
        out += dim(ink_rrect(x, 6, 12, 52, 4), .45)
    out += ink_rrect(6, 12, 12, 9, 3) + ink_rrect(26, 30, 12, 9, 3) + ink_rrect(46, 18, 12, 9, 3) + ink_rrect(46, 42, 12, 9, 3) + ink_rrect(6, 40, 12, 9, 3)
    return fit(out, 0.525, 32.0, 32.0)


@reg("io.github.redddfoxxyy.pomolin", BROWN_LIGHT)
def pomolin():
    crown = "M" + "L".join("%s %s" % (f(a), f(b)) for a, b in [pt(32, 20, 13 if k % 2 == 0 else 5.5, -90 + 36 * k) for k in range(10)]) + "Z"
    out = ink_circle(32, 38, 21) + path(crown, INK, hs(2.8)) + ink_stroke("M32 14V5", 4.4)
    return fit(out, 0.657, 32.0, 30.9)


@reg("io.github.redddfoxxyy.samaya", INDIGO_DARK)
def samaya():
    out = path("M16 8H48L32 30Z", INK, ' stroke="INK" stroke-width="3" stroke-linejoin="round"') + path("M32 34L48 56H16Z", INK, ' stroke="INK" stroke-width="3" stroke-linejoin="round"')
    out += ink_rrect(10, 3, 44, 6, 3) + ink_rrect(10, 55, 44, 6, 3) + poly([(24, 52), (40, 52), (32, 42)], HOLE, 1.5)
    return fit(out, 0.520, 32.0, 32.0)


@reg("io.github.retgal.Dayon", YELLOW)
def dayon():
    out = ink_rrect(6, 10, 52, 36, 6) + ink_rrect(11, 15, 42, 26, 2, HOLE)
    out += poly([(25, 19), (25, 36), (30, 32), (34, 40), (38, 38), (34, 30), (41, 30)], INK, 1.6)
    return fit(out + ink_stroke("M32 46V54", 4.4) + ink_stroke("M21 56H43", 4.4), 0.557, 32.0, 34.1)


@reg("io.github.retux_game.retux", BLUE_GREY_SOFT)
def retux():
    out = ell(32, 34, 17, 22) + ell(32, 40, 10, 14, HOLE) + ell(16, 38, 4.5, 12) + ell(48, 38, 4.5, 12)
    out += ink_circle(25, 22, 2.8, HOLE) + ink_circle(39, 22, 2.8, HOLE) + poly([(28, 27), (36, 27), (32, 33)], INK, 1.6)
    return fit(out + ell(23, 57, 7, 3.4) + ell(41, 57, 7, 3.4), 0.682, 32.0, 36.2)


@reg("io.github.rfrench3.scopebuddy-gui", LIGHT_BLUE_DEEP)
def scopebuddy_gui():
    out = ring_c(32, 32, 16, 4.4) + ink_circle(32, 32, 3.6)
    for a in (0, 90, 180, 270):
        x0, y0 = pt(32, 32, 10, a)
        x1, y1 = pt(32, 32, 26, a)
        out += ink_stroke(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", 4)
    return fit(out, 0.657, 32.0, 32.0)


@reg("io.github.riftr.intelpy", AMBER_LIGHT)
def intelpy():
    out = ink_circle(32, 26, 18) + ink_rrect(24, 40, 16, 7, 2.5) + ink_rrect(26, 49, 12, 6, 3)
    return fit(out + ink_stroke("M25 24L32 33L39 24", 3.6, HOLE) + ink_stroke("M32 33V42", 3.6, HOLE), 0.779, 32.0, 31.5)


@reg("io.github.riyaniii.Kaori", PINK_DARK)
def kaori():
    out = path("M10 54Q8 12 54 10Q56 54 10 54Z", INK) + ink_stroke("M14 50L44 20", 3.6, HOLE) + ink_stroke("M28 36L28 26", 3, HOLE) + ink_stroke("M36 28L46 28", 3, HOLE)
    return fit(out, 0.598, 32.0, 32.0)


@reg("io.github.rizukirr.apic", TEAL)
def apic():
    out = ink_stroke("M24 8Q16 8 16 16V25Q16 32 9 32Q16 32 16 39V48Q16 56 24 56", 4.8)
    out += ink_stroke("M40 8Q48 8 48 16V25Q48 32 55 32Q48 32 48 39V48Q48 56 40 56", 4.8)
    return fit(out + ink_circle(32, 32, 4.2), 0.638, 32.0, 32.0)


@reg("io.github.rocket.editor", DEEP_ORANGE_SOFT)
def editor():
    out = ink_rrect(6, 6, 38, 52, 6) + ink_stroke("M13 18H37", 3.4, HOLE) + ink_stroke("M13 27H37", 3.4, HOLE) + ink_stroke("M13 36H28", 3.4, HOLE)
    pencil = ink_rrect(44, 26, 10, 28, 2, INK, hs(3)) + path("M44 54L49 62L54 54Z", INK, hs(3))
    return fit(out + rot(pencil, 28, 49, 44), 0.494, 34.4, 33.8)


@reg("io.github.ronniedroid.concessio", DEEP_PURPLE_DEEP)
def concessio():
    out = ink_circle(18, 32, 13) + ink_circle(18, 32, 5, HOLE) + ink_rrect(28, 29, 32, 7, 3.5) + ink_rrect(46, 35, 6, 11, 2) + ink_rrect(55, 35, 6, 8, 2)
    return fit(out, 0.632, 33.0, 32.5)


@reg("io.github.roseblume.rosary", LIGHT_BLUE_SOFT)
def rosary():
    out = ink_stroke("M6 6Q6 40 32 40Q58 40 58 6", 4.4) + ink_circle(32, 46, 4.6) + ink_stroke("M32 50V63", 4.6) + ink_stroke("M25 56H39", 4.6)
    return fit(out, 0.451, 32.0, 34.6)


@reg("io.github.rsevero.mapiah", GREY_DARK)
def mapiah():
    out = ink_stroke("M8 34Q6 12 30 9Q56 6 57 30Q58 54 32 56Q10 58 8 34Z", 3.6)
    out += ink_stroke("M19 33Q19 21 31 21Q45 21 45 32Q45 45 32 45Q19 45 19 33Z", 3.6) + ink_circle(32, 33, 3.6)
    return fit(out, 0.658, 32.5, 32.4)


@reg("io.github.rsvzz.csven", BLUE)
def csven():
    out = ink_rrect(6, 8, 52, 48, 7) + ink_stroke("M6 24H58", 3, HOLE) + ink_stroke("M26 24V56", 3, HOLE) + ink_stroke("M42 24V56", 3, HOLE)
    out += ink_rrect(12, 13, 14, 6, 3, HOLE) + ink_stroke("M30 38L33 46", 3, HOLE)
    return fit(out, 0.555, 32.0, 32.8)


@reg("io.github.rsvzz.iconvwadw", YELLOW_SOFT)
def iconvwadw():
    out = ink_stroke("M8 22H44", 5) + arrowhead(44, 22, 1, 0, 11) + ink_stroke("M56 42H20", 5) + arrowhead(20, 42, -1, 0, 11)
    return fit(out, 0.641, 32.0, 32.0)


@reg("io.github.saeugetier.photobooth", RED_DEEP)
def photobooth():
    out = ink_rrect(14, 3, 36, 58, 6) + ink_rrect(20, 9, 24, 12, 2, HOLE) + ink_rrect(20, 26, 24, 12, 2, HOLE) + ink_rrect(20, 43, 24, 12, 2, HOLE)
    return fit(out + ink_circle(32, 32, 3.8), 0.575, 32.0, 32.0)


@reg("io.github.sameboy.SameBoy", CYAN_LIGHT)
def sameboy():
    out = ink_rrect(10, 4, 44, 56, 7) + ink_rrect(16, 10, 32, 24, 3, HOLE)
    out += ink_stroke("M22 41V51", 3.4, HOLE) + ink_stroke("M17 46H27", 3.4, HOLE) + ink_circle(38, 49, 3.4, HOLE) + ink_circle(46, 43, 3.4, HOLE)
    return fit(out, 0.557, 32.0, 32.0)


@reg("io.github.santiagocezar.maniatic-launcher", ORANGE_DARK)
def maniatic_launcher():
    out = path("M32 3Q48 14 45 38H19Q16 14 32 3Z", INK) + ink_circle(32, 22, 5.4, HOLE)
    out += poly([(19, 28), (8, 46), (19, 42)], INK, 2) + poly([(45, 28), (56, 46), (45, 42)], INK, 2) + poly([(26, 44), (38, 44), (32, 60)], INK, 2)
    return fit(out, 0.634, 32.0, 32.0)


@reg("io.github.savantsavior.lettersfall", PURPLE_DEEP)
def lettersfall():
    tile = ink_rrect(14, 18, 34, 34, 7) + ink_stroke("M23 43L31 25L39 43", 4, HOLE) + ink_stroke("M26 38H36", 3.2, HOLE)
    out = rot(tile, 12, 31, 35) + ink_stroke("M52 12V22", 3.6) + ink_stroke("M44 6V14", 3.6) + ink_stroke("M58 26V34", 3.6)
    return fit(out, 0.646, 36.0, 29.0)


@reg("io.github.savantsavior.t-crisis4", BLUE_LIGHT)
def t_crisis4():
    out = cells([(1, 0), (0, 1), (1, 1), (2, 1)], 13, 15, 6, 6) + dim(cells([(0, 2), (1, 2), (2, 2)], 13, 15, 6, 6), .5)
    return fit(out, 0.634, 27.5, 27.5)


@reg("io.github.savantsavior.t-story", BROWN_DARK)
def t_story():
    out = path("M30 14Q18 7 4 11V50Q18 46 30 53Z", INK) + path("M34 14Q46 7 60 11V50Q46 46 34 53Z", INK)
    out += ink_stroke("M10 22Q17 21 24 24", 2.8, HOLE) + ink_stroke("M10 31Q17 30 24 33", 2.8, HOLE) + ink_stroke("M54 22Q47 21 40 24", 2.8, HOLE) + ink_stroke("M54 31Q47 30 40 33", 2.8, HOLE)
    return fit(out, 0.532, 32.0, 31.2)


@reg("io.github.schwarzen.colormydesktop", INDIGO)
def colormydesktop():
    out = path("M32 5C14 5 5 19 7 33C9 48 21 59 34 57C43 56 40 48 45 46C52 44 59 44 59 33C59 17 49 5 32 5Z", INK)
    out += ink_circle(19, 29, 4.6, HOLE) + ink_circle(30, 17, 4.6, HOLE) + ink_circle(44, 20, 4.6, HOLE) + ink_circle(28, 43, 4.6, HOLE)
    return fit(out, 0.672, 32.9, 31.1)


@reg("io.github.seadve.Breathing", YELLOW_SOFT)
def breathing():
    out = ink_circle(32, 32, 8) + ring_c(32, 32, 17, 3.6) + dim(ring_c(32, 32, 26, 3.2), .55)
    return fit(out, 0.662, 32.0, 32.0)


@reg("io.github.seadve.Delineate", BLUE_GREY_DEEP)
def delineate():
    out = ink_rrect(20, 4, 24, 15, 4) + ink_rrect(4, 44, 24, 15, 4) + ink_rrect(36, 44, 24, 15, 4)
    out += ink_stroke("M32 19V32H16V44", 3.8) + ink_stroke("M32 32H48V44", 3.8)
    return fit(out, 0.491, 32.0, 31.5)


@reg("io.github.searchandrescue2.sar2", LIGHT_BLUE_LIGHT)
def sar2():
    out = ell(28, 36, 19, 12) + ink_stroke("M42 33H60", 5) + ink_stroke("M60 26V38", 4) + ink_stroke("M6 16H50", 4.6) + ink_stroke("M28 16V24", 4)
    out += ink_stroke("M10 54H46", 3.8) + ink_stroke("M20 46V54", 3.4) + ink_stroke("M38 46V54", 3.4) + ell(21, 35, 6, 5, HOLE)
    return fit(out, 0.520, 33.0, 34.8)


@reg("io.github.seja_arctic_fox.vidcom", AMBER_DARK)
def vidcom():
    body = ink_rrect(6, 24, 52, 34, 5) + poly([(26, 34), (26, 50), (40, 42)], HOLE, 1.8)
    bar = ink_rrect(6, 8, 52, 13, 3) + poly([(16, 8), (24, 8), (18, 21), (10, 21)], HOLE) + poly([(32, 8), (40, 8), (34, 21), (26, 21)], HOLE) + poly([(48, 8), (56, 8), (50, 21), (42, 21)], HOLE)
    return fit(body + rot(bar, -9, 6, 21), 0.497, 31.1, 29.1)


@reg("io.github.sepehr_rs.Sudoku", PINK)
def sudoku():
    out = ink_rrect(6, 6, 52, 52, 8) + ink_stroke("M23 6V58", 2.8, HOLE) + ink_stroke("M41 6V58", 2.8, HOLE) + ink_stroke("M6 23H58", 2.8, HOLE) + ink_stroke("M6 41H58", 2.8, HOLE)
    out += ink_rrect(10, 10, 9, 9, 1.6, HOLE) + ink_rrect(27, 27, 10, 10, 1.6, HOLE) + ink_rrect(45, 45, 9, 9, 1.6, HOLE)
    return fit(out, 0.548, 32.0, 32.0)


@reg("io.github.sgsaenger.vipster", TEAL_SOFT)
def vipster():
    out = ink_stroke("M32 22L14 46", 5) + ink_stroke("M32 22L50 46", 5) + ink_circle(32, 22, 13) + ink_circle(14, 46, 8) + ink_circle(50, 46, 8)
    return fit(out + ink_circle(28, 18, 3.4, HOLE), 0.592, 32.0, 31.5)


@reg("io.github.sharkwouter.oceanpop", DEEP_ORANGE_DEEP)
def oceanpop():
    out = ring_c(26, 36, 20, 4.6) + ink_stroke("M14 32Q15 25 22 22", 3.6) + ring_c(49, 16, 9, 3.8) + ring_c(52, 48, 5.5, 3.4)
    return fit(out, 0.536, 31.8, 31.8)


@reg("io.github.shmmodbus.shm-modbus", DEEP_PURPLE_LIGHT)
def shm_modbus():
    out = ink_stroke("M4 32H60", 5) + ink_rrect(6, 6, 18, 15, 3.4) + ink_rrect(40, 6, 18, 15, 3.4) + ink_rrect(23, 43, 18, 15, 3.4)
    out += ink_stroke("M15 21V32", 4.4) + ink_stroke("M49 21V32", 4.4) + ink_stroke("M32 32V43", 4.4)
    return fit(out, 0.520, 32.0, 32.0)


@reg("io.github.shonebinu.Exchange", LIGHT_BLUE_DARK)
def exchange():
    out = ink_stroke("M18 56V18", 5.4) + arrowhead(18, 20, 0, -1, 13) + ink_stroke("M46 8V46", 5.4) + arrowhead(46, 44, 0, 1, 13)
    return fit(out, 0.604, 32.0, 32.0)


@reg("io.github.shonebinu.Glyph", GREY)
def glyph():
    out = ink_stroke("M8 52H24V46Q9 40 9 27Q9 8 32 8Q55 8 55 27Q55 40 40 46V52H56", 5.4)
    return fit(out, 0.524, 32.0, 30.0)


@reg("io.github.shonubot.Spruce", BLUE_SOFT)
def spruce():
    out = ""
    for d in ("M32 3L47 22H17Z", "M32 15L51 38H13Z", "M32 28L56 54H8Z"):
        out += path(d, INK, ' stroke="INK" stroke-width="3" stroke-linejoin="round"')
    out += ink_rrect(27, 52, 10, 9, 2)
    return fit(out, 0.533, 32.0, 31.2)


@reg("io.github.shundhammer.qdirstat", YELLOW_DEEP)
def qdirstat():
    out = ink_rrect(4, 6, 31, 30, 4) + dim(ink_rrect(39, 6, 21, 17, 4), .65) + ink_rrect(39, 27, 21, 9, 3) + ink_rrect(4, 40, 20, 18, 4) + dim(ink_rrect(28, 40, 32, 18, 4), .65)
    return fit(out, 0.500, 32.0, 32.0)


@reg("io.github.sigmasd.VirtAudio", RED_LIGHT)
def virtaudio():
    out = poly([(6, 24), (17, 24), (31, 10), (31, 54), (17, 40), (6, 40)], INK, 3)
    return fit(out + ink_stroke("M41 23Q49 32 41 41", 4.2) + ink_stroke("M48 14Q62 32 48 50", 4.2), 0.664, 30.9, 32.0)


@reg("io.github.sigmasd.pingmonitor", CYAN_DARK)
def pingmonitor():
    out = ink_stroke("M8 6V56H58", 4) + ink_stroke("M15 42L25 30L34 38L50 14", 4.8) + ink_circle(50, 14, 4.8)
    return fit(out, 0.491, 33.0, 31.0)


@reg("io.github.sigmasd.recordapps", ORANGE)
def recordapps():
    out = ink_rrect(4, 8, 56, 48, 8) + ink_circle(13, 16, 2.4, HOLE) + ink_circle(21, 16, 2.4, HOLE) + ink_rrect(9, 24, 46, 26, 3, HOLE)
    return fit(out + ink_circle(32, 37, 8), 0.544, 32.0, 32.0)


@reg("io.github.sigmasd.share", PURPLE_LIGHT)
def share():
    out = ink_stroke("M18 32L45 17", 4.4) + ink_stroke("M18 32L45 47", 4.4) + ink_circle(47, 14, 9) + ink_circle(16, 32, 9) + ink_circle(47, 50, 9)
    return fit(out, 0.562, 31.5, 32.0)


@reg("io.github.sigmasd.stimulator", ORANGE_DARK)
def stimulator():
    out = poly([(38, 3), (12, 35), (28, 35), (24, 61), (52, 27), (35, 27)], INK, 2.6)
    return fit(out, 0.590, 32.0, 32.0)


@reg("io.github.signus_game.signus", BROWN)
def signus():
    out = poly([(32, 3), (40, 28), (40, 46), (32, 40), (24, 46), (24, 28)], INK, 2) + poly([(24, 30), (6, 52), (24, 46)], INK, 2) + poly([(40, 30), (58, 52), (40, 46)], INK, 2)
    return fit(out + ell(32, 24, 3.2, 7, HOLE) + poly([(28, 49), (36, 49), (32, 61)], INK, 2), 0.548, 32.0, 32.0)


@reg("io.github.sil_car.SqueezeVid", INDIGO_SOFT)
def squeezevid():
    out = ink_rrect(20, 14, 24, 36, 5) + ink_rrect(25, 19, 14, 26, 2, HOLE) + poly([(29, 26), (29, 38), (37, 32)], INK, 1.2)
    out += ink_stroke("M2 32H8", 4.6) + arrowhead(8, 32, 1, 0, 9) + ink_stroke("M62 32H56", 4.6) + arrowhead(56, 32, -1, 0, 9)
    return fit(out, 0.566, 32.0, 32.0)


@reg("io.github.simoonas.marca", YELLOW_DARK)
def marca():
    out = path("M14 4H50V60L32 46L14 60Z", INK) + star5(32, 24, 9.5, HOLE)
    return fit(out, 0.553, 32.0, 32.0)


@reg("io.github.sithlord48.blackchocobo", BLUE_GREY_LIGHT)
def blackchocobo():
    out = ell(27, 38, 19, 13) + ink_stroke("M38 32L44 18", 9) + ink_circle(46, 14, 9) + poly([(53, 11), (62, 16), (53, 19)], INK, 1.6)
    out += ink_circle(48, 12, 2.2, HOLE) + ink_stroke("M22 50V59", 3.8) + ink_stroke("M33 50V59", 3.8) + ink_stroke("M17 59H27", 3.8) + ink_stroke("M28 59H38", 3.8)
    return fit(out + poly([(10, 34), (2, 24), (14, 28)], INK, 2) + ink_stroke("M43 6L40 1", 3.4), 0.537, 31.9, 30.1)


@reg("io.github.sitraorg.sitra", LIGHT_BLUE_DARK)
def sitra():
    out = hexring(32, 32, 25, 5.2) + ink_circle(32, 32, 8.5) + ink_stroke("M32 7V16", 4.2)
    return fit(out, 0.662, 32.0, 32.0)


@reg("io.github.smallbasic.SmallBASIC", AMBER)
def smallbasic():
    out = ink_rrect(4, 8, 56, 48, 8) + ink_stroke("M15 22L27 32L15 42", 4.6, HOLE) + ink_stroke("M33 44H49", 4.6, HOLE)
    return fit(out, 0.544, 32.0, 32.0)


@reg("io.github.smcameron.space-nerds-in-space", PINK_SOFT)
def space_nerds_in_space():
    out = path("M19 30Q19 10 32 10Q45 10 45 30Z", INK) + ell(32, 34, 28, 9) + dim(poly([(21, 44), (43, 44), (53, 61), (11, 61)], INK, 1.6), .55)
    return fit(out + ink_stroke("M8 34H56", 2.6, HOLE), 0.550, 32.0, 35.9)


@reg("io.github.smolblackcat.Progress", TEAL_DEEP)
def progress():
    x0, y0 = pt(32, 32, 22, -90)
    x1, y1 = pt(32, 32, 22, 150)
    out = dim(ring_c(32, 32, 22, 7.5), .4) + ink_stroke(f"M{f(x0)} {f(y0)}A22 22 0 1 1 {f(x1)} {f(y1)}", 7.5)
    return fit(out, 0.709, 32.0, 32.0)


@reg("io.github.snesrev.Zelda3", DEEP_ORANGE_LIGHT)
def zelda3():
    blade = poly([(32, 2), (38, 10), (38, 38), (26, 38), (26, 10)], INK, 2) + ink_rrect(12, 38, 40, 7, 3.5) + ink_rrect(28, 45, 8, 11, 2) + ink_circle(32, 59, 3.8)
    return fit(rot(blade, 38, 32, 32), 0.574, 30.6, 32.2)


@reg("io.github.sniper1720.khushu", DEEP_PURPLE_DARK)
def khushu():
    return fit(crescent(26, 32, 24) + star4(47, 22, 9), 0.642, 29.1, 32.0)


@reg("io.github.sockeye_d.godl", GREY_LIGHT)
def godl():
    out = ink_stroke("M32 6V34", 6.4) + arrowhead(32, 32, 0, 1, 15) + ink_stroke("M8 40V54H56V40", 5.4)
    return fit(out, 0.503, 32.0, 29.8)


@reg("io.github.sofusa.qobine", GREY_SOFT)
def qobine():
    out = ink_stroke("M11 40V32Q11 8 32 8Q53 8 53 32V40", 5.6) + ink_rrect(5, 36, 14, 22, 6) + ink_rrect(45, 36, 14, 22, 6)
    return fit(out, 0.525, 32.0, 31.5)


@reg("io.github.srb2.rphys", BLUE_DEEP)
def rphys():
    out = ink_circle(34, 36, 17) + ink_stroke("M24 31Q27 24 34 23", 3.6, HOLE) + ink_stroke("M4 61H60", 4.4) + ink_stroke("M6 14Q8 8 15 6", 3.4) + ink_stroke("M2 24Q3 20 8 18", 3.2)
    return fit(out, 0.444, 31.2, 33.8)


@reg("io.github.srpvpn.pulse", YELLOW_LIGHT)
def pulse():
    out = ink_stroke("M2 34H17L24 18L33 50L40 26L45 34H62", 5.4)
    return fit(out, 0.565, 32.0, 34.0)


@reg("io.github.sss_says_snek.diurnals", RED_DARK)
def diurnals():
    out = ink_circle(32, 32, 12)
    for k in range(8):
        x0, y0 = pt(32, 32, 19, 45 * k)
        x1, y1 = pt(32, 32, 27, 45 * k)
        out += ink_stroke(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", 4.4)
    return fit(out, 0.627, 32.0, 32.0)


@reg("io.github.stephanecouturier.Katalog", CYAN)
def katalog():
    out = ink_rrect(8, 4, 48, 56, 7) + ink_stroke("M8 32H56", 3, HOLE) + ink_rrect(24, 14, 16, 7, 3.5, HOLE) + ink_rrect(24, 43, 16, 7, 3.5, HOLE)
    return fit(out, 0.538, 32.0, 32.0)


@reg("io.github.strikerx3.ymir", ORANGE_SOFT)
def ymir():
    return fit(asterisk(32, 32, 26, 5) + ink_circle(32, 32, 4.6, HOLE), 0.642, 32.0, 32.0)


@reg("io.github.subhra74.Muon", PURPLE_DARK)
def muon():
    out = ink_stroke("M14 8V58", 6) + ink_stroke("M14 36Q14 50 28 50Q42 50 46 34V8", 6) + ink_stroke("M46 34Q47 48 58 50", 6)
    return fit(out, 0.504, 36.0, 33.0)


@reg("io.github.subsoundorg.Subsound", GREY)
def subsound():
    out = ell(16, 48, 9, 7) + ell(46, 42, 9, 7) + ink_stroke("M23 46V14", 4.4) + ink_stroke("M53 40V8", 4.4) + poly([(21, 12), (55, 5), (55, 15), (21, 22)], INK, 1.6)
    return fit(out, 0.530, 31.5, 29.6)


@reg("io.github.suchnsuch.Tangent", BROWN_SOFT)
def tangent():
    out = ring_c(32, 40, 17, 5) + ink_stroke("M2 21H62", 5) + ink_circle(32, 22, 4.4)
    return fit(out, 0.492, 32.0, 38.5)


@reg("io.github.sugarycandybar.Carabiner", INDIGO_DEEP)
def carabiner():
    out = ink_stroke("M22 8H38Q54 8 54 24V40Q54 56 38 56H26Q10 56 10 40V32", 6.4) + ink_stroke("M10 24V14Q10 10 16 10", 6.4)
    return fit(rot(out, 28, 32, 32), 0.574, 32.0, 31.2)


@reg("io.github.sugarycandybar.Crucible", YELLOW_LIGHT)
def crucible():
    out = path("M8 28H56Q56 53 32 53Q8 53 8 28Z", INK) + ink_rrect(5, 23, 54, 7, 3.5) + ink_stroke("M24 60H40", 4.4)
    return fit(out + ink_stroke("M22 15Q17 9 23 3", 3.8) + ink_stroke("M36 15Q31 9 37 3", 3.8) + ink_stroke("M49 14Q45 9 49 5", 3.4), 0.555, 32.0, 31.6)


@reg("io.github.sugarycandybar.Hosty", BLUE_GREY_DARK)
def hosty():
    out = poly([(32, 5), (60, 30), (4, 30)], INK, 3) + ink_rrect(11, 29, 42, 29, 3) + ink_rrect(26, 39, 12, 19, 2, HOLE) + ink_rrect(44, 10, 8, 14, 1.5)
    return fit(out, 0.556, 32.0, 30.8)


@reg("io.github.swordpuffin.hunt", LIGHT_BLUE)
def hunt():
    out = ink_rrect(5, 22, 21, 36, 9) + ink_rrect(38, 22, 21, 36, 9) + ink_rrect(22, 28, 20, 9, 4) + ink_rrect(8, 10, 15, 14, 3) + ink_rrect(41, 10, 15, 14, 3)
    return fit(out + ink_circle(15.5, 46, 5.6, HOLE) + ink_circle(48.5, 46, 5.6, HOLE), 0.560, 32.0, 34.0)


@reg("io.github.swordpuffin.rewaita", AMBER_SOFT)
def rewaita():
    out = ink_rrect(6, 6, 42, 18, 6) + ink_stroke("M48 15H57V33H33V42", 4.6) + ink_rrect(28, 42, 10, 17, 4)
    return fit(out, 0.523, 32.8, 32.5)


@reg("io.github.swordpuffin.splices", PINK_DEEP)
def splices():
    a = "M16 5C16 22 48 22 48 36S16 50 16 60"
    b = "M48 5C48 22 16 22 16 36S48 50 48 60"
    return fit(ink_stroke(a, 5.4) + ink_stroke(b, 11, HOLE) + ink_stroke(b, 5.4), 0.492, 32.0, 32.5)


@reg("io.github.swordpuffin.wardrobe", TEAL_LIGHT)
def wardrobe():
    out = ink_stroke("M32 24Q42 22 42 14Q42 6 33 6Q26 6 26 11", 4.6) + ink_stroke("M32 24L6 46Q3 52 10 52H54Q61 52 58 46Z", 4.8) + ink_stroke("M16 56H48", 4)
    return fit(out, 0.520, 31.9, 30.8)


@reg("io.github.sxyazi.yazi", DEEP_ORANGE_DARK)
def yazi():
    out = ink_rrect(4, 8, 56, 48, 7) + ink_stroke("M21 12V52", 2.8, HOLE) + ink_stroke("M40 12V52", 2.8, HOLE)
    for y in (20, 30, 40):
        out += ink_stroke(f"M9 {y}H16", 3.2, HOLE) + ink_stroke(f"M26 {y}H34", 3.2, HOLE)
    return fit(out + ink_rrect(45, 17, 10, 14, 2, HOLE), 0.538, 32.0, 32.0)


@reg("io.github.taboulet.BiggerTask", DEEP_PURPLE)
def biggertask():
    out = ink_rrect(4, 26, 24, 24, 6) + circle(16, 38, 3.6, HOLE) + ink_rrect(24, 6, 38, 38, 9, INK, hs(3.2)) + ink_stroke("M43 16V34M34 25H52", 5.4, HOLE)
    return fit(out, 0.525, 33.9, 27.1)


@reg("io.github.tanaybhomia.DeepDive", CYAN_SOFT)
def deepdive():
    out = ink_stroke("M4 14Q12 6 20 14T36 14T52 14T60 12", 4.4) + ink_stroke("M32 26V44", 5.6) + arrowhead(32, 42, 0, 1, 14) + dim(ring_c(15, 40, 5, 3.2), .6) + dim(ring_c(50, 46, 4, 3), .6)
    return fit(out, 0.502, 32.0, 32.2)


@reg("io.github.tanaybhomia.Whisp", GREY_DEEP)
def whisp():
    out = spiral(32, 28, 3, 18, 2, 0, 5.2) + ink_stroke("M50 28Q52 44 38 54", 5.2)
    return fit(out, 0.769, 34.0, 33.0)


@reg("io.github.tangsangsimida.easykiconverter", BLUE_LIGHT)
def easykiconverter():
    out = ink_rrect(14, 14, 36, 36, 6) + ink_rrect(22, 22, 20, 20, 3, HOLE) + ink_circle(32, 32, 4)
    for k in range(3):
        v = 22 + 10 * k
        out += ink_stroke(f"M{v} 3V12", 3.6) + ink_stroke(f"M{v} 52V61", 3.6) + ink_stroke(f"M3 {v}H12", 3.6) + ink_stroke(f"M52 {v}H61", 3.6)
    return fit(out, 0.564, 31.9, 32.0)


@reg("io.github.tapscodes.MuseAmp", YELLOW_DARK)
def museamp():
    x0, y0 = pt(32, 36, 27, 135)
    x1, y1 = pt(32, 36, 27, 45)
    out = ink_circle(32, 36, 19) + ink_stroke("M32 36V22", 4.4, HOLE) + ink_stroke(f"M{f(x0)} {f(y0)}A27 27 0 1 1 {f(x1)} {f(y1)}", 3.8)
    return fit(out, 0.582, 32.0, 32.0)


@reg("io.github.tareksander.StoryReader", RED)
def storyreader():
    out = ink_rrect(14, 8, 36, 48, 3) + ink_stroke("M21 20H43", 3, HOLE) + ink_stroke("M21 29H43", 3, HOLE) + ink_stroke("M21 38H35", 3, HOLE) + ink_rrect(7, 4, 50, 10, 5) + ink_rrect(7, 50, 50, 10, 5)
    return fit(out, 0.518, 32.0, 32.0)


@reg("io.github.teacond.Morse", CYAN_SOFT)
def morse():
    out = ink_rrect(6, 50, 52, 9, 3.4) + ink_rrect(28, 42, 10, 10, 2) + ink_stroke("M54 38L16 30", 5.4) + ink_circle(13, 26, 8.4) + ink_stroke("M46 40V50", 4)
    return fit(out, 0.570, 31.2, 38.2)


@reg("io.github.tfuxu.floodit", ORANGE_DEEP)
def floodit():
    out = path("M12 26L18 58H46L52 26Z", INK) + ell(32, 26, 20, 6) + ell(32, 26, 13, 3, HOLE) + ink_stroke("M12 26Q32 -2 52 26", 3.6)
    return fit(out, 0.671, 31.9, 34.0)


@reg("io.github.theforceengine.tfe", PURPLE)
def tfe():
    out = ink_circle(32, 32, 19)
    for k in range(8):
        out += rot(ink_rrect(27.5, 4, 9, 13, 2.4), 45 * k, 32, 32)
    return fit(out + ink_circle(32, 32, 8, HOLE), 0.653, 32.0, 32.0)


@reg("io.github.thiefmd.themegenerator", BLUE_SOFT)
def themegenerator():
    out = rot(ink_rrect(25, 6, 15, 46, 5, INK, hs(2.6)), -34, 32, 58) + rot(ink_rrect(25, 6, 15, 46, 5, INK, hs(2.6)), 34, 32, 58) + rot(ink_rrect(25, 6, 15, 46, 5, INK, hs(2.6)), 0, 32, 58)
    return fit(out + ink_circle(32.5, 44, 3.4, HOLE), 0.502, 32.4, 30.8)


@reg("io.github.timcharper.EmojiClu", BROWN_DEEP)
def emojiclu():
    out = ink_circle(32, 32, 26) + ink_circle(23, 26, 3.8, HOLE) + ink_circle(41, 26, 3.8, HOLE) + ink_stroke("M19 38Q32 51 45 38", 4, HOLE)
    return fit(out, 0.701, 32.0, 32.0)


@reg("io.github.tntwise.REAL-Video-Enhancer", INDIGO_LIGHT)
def real_video_enhancer():
    out = poly([(8, 10), (8, 54), (40, 32)], INK, 4) + star4(49, 17, 11) + star4(53, 47, 7)
    return fit(out, 0.512, 33.1, 30.9)


@reg("io.github.toCase.Birchflow", YELLOW_DARK)
def birchflow():
    out = ink_rrect(22, 4, 17, 56, 3) + ink_stroke("M39 24L54 12", 4.4) + ink_stroke("M22 38L8 28", 4.4) + ink_stroke("M26 14H33", 3, HOLE) + ink_stroke("M28 30H36", 3, HOLE) + ink_stroke("M25 47H32", 3, HOLE)
    return fit(out + ink_stroke("M54 12V5", 4.4) + ink_stroke("M8 28V21", 4.4), 0.495, 31.0, 31.4)


@reg("io.github.tobagin.Draughts", BLUE_GREY)
def draughts():
    st = ' stroke="HOLE" stroke-width="2.8"'
    out = f'<ellipse cx="32" cy="44" rx="23" ry="13" fill="INK"{st}/><ellipse cx="32" cy="34" rx="23" ry="13" fill="INK"{st}/>' + ellring(32, 34, 13, 7, 2.8, HOLE)
    return fit(out, 0.727, 32.0, 39.0)


@reg("io.github.tobagin.Ntfyr", LIGHT_BLUE_SOFT)
def ntfyr():
    out = path("M32 4Q36 4 36 9Q50 13 50 31V39L58 49H6L14 39V31Q14 13 28 9Q28 4 32 4Z", INK) + ink_circle(32, 57, 5.4)
    return fit(out, 0.619, 32.0, 33.2)


@reg("io.github.tobagin.digger", AMBER_DEEP)
def digger():
    out = path("M20 26H44Q46 48 32 58Q18 48 20 26Z", INK) + ink_stroke("M32 26V10", 5) + ink_stroke("M22 8H42", 5.4)
    return fit(rot(out, -32, 32, 32), 0.607, 28.0, 28.8)


@reg("io.github.tobagin.keysmith", PINK_LIGHT)
def keysmith():
    out = path("M32 3L55 11V30Q55 48 32 61Q9 48 9 30V11Z", INK) + ink_circle(32, 27, 6.4, HOLE) + poly([(28.5, 31), (35.5, 31), (38, 44), (26, 44)], HOLE, 1.4)
    return fit(out, 0.591, 32.0, 32.0)


@reg("io.github.tobagin.scramble", TEAL_DARK)
def scramble():
    out = hx(32, 32, 27, -90, INK, 3)
    for a in (30, 150, 270):
        x, y = pt(32, 32, 27, a)
        out += ink_stroke(f"M32 32L{f(x)} {f(y)}", 3, HOLE)
    return fit(out, 0.642, 32.0, 32.0)


@reg("io.github.tobagin.sonar", DEEP_ORANGE)
def sonar():
    x1, y1 = pt(32, 32, 25, -30)
    out = ring_c(32, 32, 25, 3.6) + dim(ring_c(32, 32, 12, 3), .6) + path(f"M32 32L32 7A25 25 0 0 1 {f(x1)} {f(y1)}Z", INK) + ink_circle(46, 44, 3.6)
    return fit(out, 0.680, 32.0, 32.0)


@reg("io.github.tobagin.tempo", DEEP_PURPLE_SOFT)
def tempo():
    out = path("M23 6H41L53 56H11Z", INK) + ink_rrect(7, 56, 50, 6, 3) + ink_stroke("M32 50L42 16", 3.6, HOLE) + ink_rrect(34, 24, 12, 7, 2, HOLE)
    return fit(out, 0.509, 32.0, 34.0)


@reg("io.github.tom94.tev", CYAN_DEEP)
def tev():
    out = ink_rrect(4, 8, 56, 48, 8) + ink_rrect(10, 14, 44, 36, 3, HOLE) + ink_circle(32, 32, 12) + path("M32 20A12 12 0 0 0 32 44Z", HOLE)
    return fit(out, 0.544, 32.0, 32.0)


@reg("io.github.tomluchowski.OpenDungeonsPlus", GREY_LIGHT)
def opendungeonsplus():
    out = ink_rrect(7, 16, 17, 44, 2) + ink_rrect(40, 16, 17, 44, 2) + ink_rrect(18, 28, 28, 32, 2)
    for x in (7, 17.5, 40, 50.5):
        out += ink_rrect(x, 8, 6.5, 10, 1)
    return fit(out + path("M26 60V47Q26 39 32 39Q38 39 38 47V60Z", HOLE), 0.515, 32.0, 34.0)


@reg("io.github.torrent_file_editor.Torrent-file-editor", BLUE_DARK)
def torrent_file_editor():
    out = ink_stroke("M14 14V36Q14 52 32 52Q50 52 50 36V14", 12) + ink_rrect(8, 4, 12, 12, 2, HOLE) + ink_rrect(44, 4, 12, 12, 2, HOLE)
    return fit(out, 0.519, 32.0, 31.0)


@reg("io.github.trackballs.Trackballs", YELLOW)
def trackballs():
    out = poly([(4, 50), (60, 38), (60, 46), (4, 60)], INK, 2.4) + ink_circle(36, 27, 14) + ink_stroke("M28 24Q30 18 37 17", 3.4, HOLE)
    return fit(out, 0.494, 32.0, 37.1)


@reg("io.github.trevorsandy.LPub3D", RED_SOFT)
def lpub3d():
    out = ink_rrect(5, 28, 54, 28, 5) + ink_rrect(13, 17, 14, 12, 3) + ink_rrect(37, 17, 14, 12, 3) + ink_stroke("M11 39H53", 3, HOLE)
    return fit(out, 0.589, 32.0, 36.5)


@reg("io.github.trigg.discover_overlay", CYAN_DEEP)
def discover_overlay():
    out = f'<rect x="4" y="6" width="40" height="32" rx="6" fill="none" stroke="INK" stroke-width="4.4"/>'
    out += path("M24 26H54Q60 26 60 32V46Q60 52 54 52H42L33 61V52H24Q18 52 18 46V32Q18 26 24 26Z", INK, hs(3.4)) + ink_stroke("M26 36H52", 3, HOLE) + ink_stroke("M26 44H42", 3, HOLE)
    return fit(out, 0.477, 31.8, 33.2)


@reg("io.github.trufae.Parla", ORANGE_LIGHT)
def parla():
    out = ink_rrect(22, 3, 20, 34, 10) + ink_stroke("M13 28Q13 48 32 48Q51 48 51 28", 4.6) + ink_stroke("M32 48V58", 4.6) + ink_stroke("M21 59H43", 4.6)
    return fit(out, 0.591, 32.0, 32.2)


@reg("io.github.tsmetana.mpk3-settings", PURPLE_SOFT)
def mpk3_settings():
    out = ink_rrect(3, 10, 58, 44, 7) + ink_circle(14, 20, 4.4, HOLE) + ink_circle(27, 20, 4.4, HOLE)
    for x in (37, 48):
        for y in (15, 26):
            out += ink_rrect(x, y, 9, 8, 2, HOLE)
    out += ink_rrect(8, 38, 48, 11, 2, HOLE) + ink_stroke("M20 38V49", 2.2) + ink_stroke("M32 38V49", 2.2) + ink_stroke("M44 38V49", 2.2)
    return fit(out, 0.544, 32.0, 32.0)


@reg("io.github.tuner_labs.tuner", AMBER_DARK)
def tuner():
    out = ink_stroke("M22 5V28Q22 40 32 40Q42 40 42 28V5", 5.6) + ink_stroke("M32 40V59", 5.6) + ink_stroke("M11 14Q7 20 11 26", 3.6) + ink_stroke("M53 14Q57 20 53 26", 3.6)
    return fit(out, 0.581, 32.0, 32.0)


@reg("io.github.twanvl.MagicSetEditor2", BROWN_LIGHT)
def magicseteditor2():
    out = ink_rrect(12, 4, 40, 56, 7) + ink_rrect(17, 9, 30, 46, 3, HOLE) + star5(32, 32, 13) + ink_circle(22, 15, 2.4)
    return fit(out, 0.577, 32.0, 32.0)


@reg("io.github.unicornyrainbow.secrets", INDIGO_DARK)
def secrets():
    out = ink_rrect(5, 5, 54, 51, 8) + ink_rrect(11, 11, 42, 39, 4, HOLE) + ring_c(32, 30, 10, 4) + ink_circle(32, 30, 3.2) + ink_rrect(12, 56, 8, 5, 2) + ink_rrect(44, 56, 8, 5, 2)
    for a in (0, 90, 180, 270):
        x, y = pt(32, 30, 14.5, a)
        out += ink_circle(x, y, 1.6)
    return fit(out, 0.515, 32.0, 33.0)


@reg("io.github.unrud.RecentFilter", YELLOW)
def recentfilter():
    out = path("M5 8H59L39 33V54L27 47V33Z", INK, ' stroke="INK" stroke-width="3" stroke-linejoin="round"')
    out += ink_circle(47, 46, 14, INK, hs(3.2)) + ink_stroke("M47 38V46L53 50", 3.4, HOLE)
    return fit(out, 0.462, 33.1, 34.1)
