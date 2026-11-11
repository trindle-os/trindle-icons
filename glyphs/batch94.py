# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 94: yass to Mingle."""
from lm import (
    AMBER_DARK, AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_GREY_SOFT, BLUE_LIGHT, BROWN, BROWN_DARK, BROWN_DEEP,
    BROWN_LIGHT, BROWN_SOFT, circle, CYAN, CYAN_DARK, CYAN_DEEP, DEEP_ORANGE, DEEP_ORANGE_DARK,
    DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_DARK, DEEP_PURPLE_DEEP,
    DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, GREY, GREY_DARK, GREY_DEEP, HOLE, INDIGO,
    INDIGO_DARK, INDIGO_DEEP, INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE, LIGHT_BLUE_DARK,
    LIGHT_BLUE_DEEP, LIGHT_BLUE_LIGHT, ORANGE_DARK, ORANGE_DEEP, path, PINK, PINK_DARK,
    PINK_DEEP, PINK_LIGHT, PINK_SOFT, poly, pt, PURPLE, PURPLE_DARK, PURPLE_DEEP, PURPLE_LIGHT,
    PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_LIGHT, RED_SOFT, TEAL, TEAL_DARK, TEAL_DEEP,
    TEAL_LIGHT, TEAL_SOFT, YELLOW_DARK,
)
from glyphs.kit import (
    arrowhead, asterisk, cells, dim, ell, ellring, fit, ink_circle, ink_rrect, ink_stroke, petal, registry, ring_c, rot, star4)

ICONS, SMALL, reg, _ = registry()


@reg("io.github.chilledheart.yass", TEAL_DEEP)
def yass():
    out = path("M32 6L54 14V32Q54 48 32 58Q10 48 10 32V14Z", INK)
    return fit(out + ink_stroke("M20 32H40", 5, HOLE) + arrowhead(39, 32, 1, 0, 8, HOLE), 0.669, 31.8, 30.4)


@reg("io.github.chnapy.pkvault", CYAN)
def pkvault():
    out = ink_rrect(8, 8, 48, 44, 6) + ink_rrect(14, 14, 36, 32, 3, HOLE) + ink_rrect(14, 52, 8, 6, 2) + ink_rrect(42, 52, 8, 6, 2)
    out += ring_c(30, 30, 9, 4) + ink_stroke("M30 30L36 24", 3.4) + ink_rrect(46, 26, 4, 10, 2)
    return fit(out, 0.588, 31.9, 31.6)


@reg("io.github.ciromattia.kcc", PURPLE)
def kcc():
    out = ink_rrect(10, 6, 44, 52, 5)
    for x, y, w, h in ((15, 11, 34, 15), (15, 30, 15, 22), (34, 30, 15, 10), (34, 43, 15, 9)):
        out += ink_rrect(x, y, w, h, 2, HOLE)
    return fit(out, 0.572, 31.8, 31.8)


@reg("io.github.cleomenezesjr.Serigy", PINK_LIGHT)
def serigy():
    out = ink_rrect(10, 10, 44, 50, 6) + ink_stroke("M18 30H46", 4, HOLE) + ink_stroke("M18 40H46", 4, HOLE) + ink_stroke("M18 50H34", 4, HOLE)
    out += ink_rrect(22, 4, 20, 12, 4, INK, f' stroke="{HOLE}" stroke-width="2.6"')
    return fit(out, 0.593, 31.9, 35.0)


@reg("io.github.cleomenezesjr.aurea", BLUE)
def aurea():
    out = ink_rrect(5, 15, 55, 34, 4, "none", ' stroke="INK" stroke-width="3.6"')
    out += dim(ink_stroke("M39 15V49", 2.8) + ink_stroke("M39 36H60", 2.8) + ink_stroke("M47 36V49", 2.8), .55)
    out += ink_stroke("M5 49A34 34 0 0 1 39 15A21 21 0 0 1 60 36A13 13 0 0 1 47 49A8 8 0 0 1 39 41", 4.6)
    return fit(out, 0.546, 31.9, 33.3)


@reg("io.github.cmus.cmus", BLUE_GREY)
def cmus():
    out = ink_rrect(6, 10, 52, 46, 7) + ink_stroke("M6 22H58", 3, HOLE)
    out += ell(25, 44, 6.5, 5, HOLE) + ink_rrect(30, 27, 3.8, 17, 1.8, HOLE)
    out += path("M33 27Q46 29 43 39Q41 33 33 34Z", HOLE) + ink_stroke("M42 48H52", 3, HOLE)
    return fit(out, 0.575, 31.8, 32.8)


@reg("io.github.coccinelle.coccinelle", TEAL_SOFT)
def coccinelle():
    out = ink_circle(32, 38, 21) + path("M20 20Q32 6 44 20Z", INK)
    out += ink_stroke("M32 18V58", 3, HOLE) + ink_stroke("M26 12L22 4", 3.2) + ink_stroke("M38 12L42 4", 3.2)
    out += ink_circle(21, 34, 4, HOLE) + ink_circle(43, 34, 4, HOLE) + ink_circle(23, 48, 3.4, HOLE) + ink_circle(41, 48, 3.4, HOLE)
    return fit(out, 0.628, 31.9, 29.7)


@reg("io.github.congard.qnvsm", BLUE_DARK)
def qnvsm():
    out = ink_rrect(4, 14, 56, 34, 5) + ink_rrect(4, 48, 8, 10, 1.5) + ink_rrect(18, 48, 32, 5, 1.5)
    out += ink_circle(24, 31, 13, HOLE) + ink_circle(24, 31, 2.8) + rot(petal(24, 31, 12, 4, 0, INK) + petal(24, 31, 12, 4, 120, INK) + petal(24, 31, 12, 4, 240, INK), 20, 24, 31)
    out += ink_stroke("M44 22H54", 3, HOLE) + ink_stroke("M44 30H54", 3, HOLE) + ink_stroke("M44 38H54", 3, HOLE)
    return fit(out, 0.536, 31.4, 36.7)


@reg("io.github.cortex_command_community.Cortex-Command-Community-Project", RED_DEEP)
def cortex_command_community_project():
    out = path("M10 38Q10 10 32 10Q54 10 54 38Z", INK) + ink_rrect(5, 38, 54, 9, 4.5)
    out += ink_rrect(17, 24, 30, 8, 3, HOLE) + ink_stroke("M32 10V20", 3.4, HOLE) + ink_rrect(14, 50, 36, 6, 3)
    return fit(out, 0.666, 31.9, 37.4)


@reg("io.github.ctlcltd.e2se", PINK_DARK)
def e2se():
    bowl = path("M8 28A24 24 0 0 0 56 28Z", INK) + ink_stroke("M32 28L32 8", 3.6) + ink_circle(32, 6, 4.6)
    out = rot(bowl, -35, 32, 34) + ink_rrect(25, 54, 14, 6, 3) + ink_stroke("M50 8Q58 14 54 24", 3.4) + ink_stroke("M42 2Q54 4 60 14", 3.4)
    return fit(out, 0.587, 34.9, 29.4)


@reg("io.github.dagargo.Elektroid", PURPLE_LIGHT)
def elektroid():
    out = ink_stroke("M16 52A22 22 0 1 1 48 52", 6) + ink_rrect(28, 52, 8, 8, 2)
    for k in range(5):
        x, y = pt(32, 36, 13, 200 + 35 * k)
        out += ink_rrect(x - 2.3, y - 4.5, 4.6, 9, 2.3, INK)
    return fit(out, 0.733, 31.9, 36.8)


@reg("io.github.daid.EmptyEpsilon", DEEP_PURPLE_DEEP)
def emptyepsilon():
    out = poly([(32, 4), (40, 24), (58, 42), (58, 52), (42, 46), (38, 58), (26, 58), (22, 46), (6, 52), (6, 42), (24, 24)], INK, 3)
    out += ell(32, 28, 3.6, 8, HOLE) + ink_stroke("M12 46L24 40M52 46L40 40", 2.6, HOLE)
    return fit(out, 0.566, 31.9, 35.0)


@reg("io.github.daniacosta_dev.AuroraMediaPlayer", INDIGO_LIGHT)
def auroramediaplayer():
    out = poly([(10, 10), (10, 54), (42, 32)], INK, 6)
    out += ink_stroke("M48 22A14 14 0 0 1 48 42", 4) + ink_stroke("M56 14A24 24 0 0 1 56 50", 4)
    return fit(out, 0.538, 31.9, 31.9)


@reg("io.github.danst0.passwordgenerator", BLUE_GREY_LIGHT)
def passwordgenerator():
    out = ink_rrect(4, 20, 56, 30, 9) + asterisk(17, 35, 6.5, 3.4, HOLE) + asterisk(32, 35, 6.5, 3.4, HOLE) + asterisk(47, 35, 6.5, 3.4, HOLE)
    return fit(out + star4(50, 11, 9), 0.575, 32.3, 28.3)


@reg("io.github.davidoc26.wallpaper_selector", AMBER_DARK)
def wallpaper_selector():
    out = ink_rrect(16, 6, 44, 34, 5)
    out += ink_rrect(4, 22, 44, 34, 5, INK, f' stroke="{HOLE}" stroke-width="3.6"')
    out += path("M9 50L20 35L28 45L35 39L43 50Z", HOLE) + ink_circle(37, 32, 3.4, HOLE)
    return fit(out, 0.533, 32.8, 30.4)


@reg("io.github.db_mobile.resonance", TEAL_LIGHT)
def resonance():
    out = ink_stroke("M20 6V30Q20 42 32 42Q44 42 44 30V6", 6) + ink_stroke("M32 42V58", 6)
    out += ink_stroke("M10 12Q6 20 10 28", 3.6) + ink_stroke("M54 12Q58 20 54 28", 3.6)
    return fit(out, 0.602, 31.8, 30.3)


@reg("io.github.ddanilov.soundscape", LIGHT_BLUE_DARK)
def soundscape():
    out = path("M2 52Q18 32 34 46Q46 36 62 48V60H2Z", INK)
    out += ink_stroke("M4 22Q12 8 20 22T36 22T52 22", 4.4)
    return fit(out, 0.513, 31.8, 40.0)


@reg("io.github.deaen.awesomecalculator", AMBER_DARK)
def awesomecalculator():
    out = ink_rrect(8, 6, 44, 54, 7) + ink_rrect(14, 12, 32, 12, 2.5, HOLE)
    for r in range(3):
        for c in range(2):
            out += ink_rrect(14 + c * 12, 30 + r * 10, 8, 6.5, 2, HOLE)
    out += ink_rrect(38, 30, 8, 23, 2, HOLE)
    return fit(out + star4(54, 10, 8), 0.515, 33.1, 30.7)


@reg("io.github.denysmb.klaro", PURPLE_DARK)
def klaro():
    out = ink_rrect(4, 7, 15, 15, 4) + circle(11.5, 14.5, 2.8, HOLE)
    out += ink_rrect(5.5, 26.5, 12, 12, 3.5, "none", ' stroke="INK" stroke-width="3.2"')
    out += ink_rrect(5.5, 45.5, 12, 12, 3.5, "none", ' stroke="INK" stroke-width="3.2"')
    return fit(out + ink_stroke("M28 15H60", 5) + ink_stroke("M28 33H60", 5) + ink_stroke("M28 52H48", 5), 0.511, 31.4, 32.4)


@reg("io.github.denysmb.unify", TEAL_DARK)
def unify():
    out = ink_stroke("M12 8V20Q12 32 32 34", 5) + ink_stroke("M52 8V20Q52 32 32 34", 5) + ink_stroke("M32 34V46", 5)
    return fit(out + arrowhead(32, 44, 0, 1, 12), 0.615, 31.8, 26.6)


@reg("io.github.denzilferreira.asteroid_shooter", LIGHT_BLUE_DEEP)
def asteroid_shooter():
    out = poly([(10, 34), (14, 20), (28, 12), (44, 18), (52, 32), (48, 48), (32, 58), (16, 52)], INK, 4)
    out += ink_circle(24, 28, 4.4, HOLE) + ink_circle(38, 42, 5.4, HOLE) + ink_circle(22, 44, 3, HOLE) + ink_circle(40, 26, 2.6, HOLE)
    return fit(out, 0.732, 29.9, 34.8)


@reg("io.github.deterous.redumper-gui", PINK)
def redumper_gui():
    out = ink_circle(30, 30, 24) + ink_circle(30, 30, 6, HOLE) + ring_c(30, 30, 14, 2.4, HOLE) + ink_stroke("M12 24A20 20 0 0 1 20 14", 3.4, HOLE)
    out += ink_circle(50, 50, 12, INK, f' stroke="{HOLE}" stroke-width="3.4"') + ink_stroke("M50 43V54", 3.6, HOLE) + arrowhead(50, 52, 0, 1, 6, HOLE)
    return fit(out, 0.586, 35.1, 35.1)


@reg("io.github.dfandrich.gpscorrelate", INDIGO_LIGHT)
def gpscorrelate():
    out = ink_rrect(4, 16, 42, 36, 5) + path("M9 46L19 32L27 41L33 36L41 46Z", HOLE) + ink_circle(14, 24, 3.4, HOLE)
    pin = "M46 6C38 6 33 12 33 19C33 29 46 42 46 42C46 42 59 29 59 19C59 12 54 6 46 6Z"
    out += path(pin, INK, f' stroke="{HOLE}" stroke-width="3.4" stroke-linejoin="round"') + ink_circle(46, 19, 4.6, HOLE)
    return fit(out, 0.585, 30.0, 30.7)


@reg("io.github.dgsasha.Remembrance", BROWN_SOFT)
def remembrance():
    out = path("M32 2Q39 8 32 13Q25 8 32 2Z", INK) + ink_rrect(29.5, 13, 5, 11, 2) + ink_rrect(16, 23, 32, 14, 4) + ink_rrect(8, 35, 48, 22, 5)
    out += ink_stroke("M8 44Q16 38 24 44T40 44T56 44", 3, HOLE)
    return fit(out, 0.585, 32.0, 33.4)


@reg("io.github.dida_code.OpstaKultura", ORANGE_DEEP)
def opstakultura():
    out = path("M10 8H54Q58 8 58 12V40Q58 44 54 44H34L22 56V44H10Q6 44 6 40V12Q6 8 10 8Z", INK)
    out += ink_stroke("M24 20Q24 14 32 14Q40 14 40 21Q40 26 32 29V32", 4.4, HOLE) + ink_circle(32, 38, 2.8, HOLE)
    return fit(out, 0.597, 32.0, 26.6)


@reg("io.github.didley.CamOverlay", GREY_DARK)
def camoverlay():
    out = ink_rrect(4, 8, 52, 36, 6, "none", ' stroke="INK" stroke-width="4.4"') + ink_stroke("M18 54H42", 4.4) + ink_stroke("M30 44V54", 4.4)
    out += ink_circle(47, 38, 13, INK, f' stroke="{HOLE}" stroke-width="3.4"') + ink_circle(47, 38, 6, HOLE) + ink_circle(47, 38, 2.8)
    return fit(out, 0.575, 29.8, 26.8)


@reg("io.github.diegoivan.GaticTacToe", INDIGO_DARK)
def gatictactoe():
    out = ink_stroke("M22 6V58", 4.4) + ink_stroke("M42 6V58", 4.4) + ink_stroke("M6 22H58", 4.4) + ink_stroke("M6 42H58", 4.4)
    out += ink_stroke("M9 9L17 17", 4) + ink_stroke("M17 9L9 17", 4) + ring_c(32, 32, 5.6, 3.6) + ink_stroke("M47 47L55 55", 4) + ink_stroke("M55 47L47 55", 4)
    return fit(out, 0.532, 31.8, 31.8)


@reg("io.github.diegoivan.pdf_metadata_editor", DEEP_ORANGE_LIGHT)
def pdf_metadata_editor():
    out = path("M12 4H38L52 18V56Q52 60 48 60H16Q12 60 12 56Z", INK) + poly([(38, 4), (38, 18), (52, 18)], INK) + path("M38 6V14Q38 18 42 18H50Z", HOLE)
    out += ink_stroke("M20 28H44", 3.6, HOLE) + ink_stroke("M20 36H36", 3.6, HOLE) + path("M20 43H34L40 49L34 55H20Z", HOLE)
    return fit(out, 0.545, 31.2, 31.5)


@reg("io.github.diegopvlk.Dosage", PURPLE_LIGHT)
def dosage():
    cap = ink_rrect(4, 18, 28, 22, 11) + dim(ink_rrect(28, 18, 28, 22, 11), .5) + ink_stroke("M30 18V40", 2.6, HOLE)
    out = rot(cap, -38, 30, 29) + ink_circle(46, 48, 9) + ink_stroke("M39 48H53", 2.8, HOLE)
    return fit(out, 0.672, 33.9, 34.1)


@reg("io.github.diegopvlk.Tomatillo", BLUE_LIGHT)
def tomatillo():
    out = ink_circle(32, 38, 21) + ink_stroke("M32 38V26", 4, HOLE) + ink_stroke("M32 38L40 43", 4, HOLE)
    out += ink_rrect(29.5, 4, 5, 10, 2.5) + path("M32 14Q20 12 12 22Q24 24 32 20Q40 24 52 22Q44 12 32 14Z", INK, f' stroke="{HOLE}" stroke-width="2.6" stroke-linejoin="round"')
    return fit(out, 0.67, 31.9, 31.5)


@reg("io.github.dimtpap.coppwr", INDIGO_SOFT)
def coppwr():
    out = ink_rrect(4, 6, 24, 17, 4) + ink_rrect(36, 41, 24, 17, 4) + ink_stroke("M9 14.5H23", 3.2, HOLE) + ink_stroke("M41 49.5H55", 3.2, HOLE)
    out += ink_stroke("M28 14.5C46 14.5 18 49.5 36 49.5", 4.4) + ink_circle(28, 14.5, 4.6, HOLE, f' stroke="{INK}" stroke-width="2.8"') + ink_circle(36, 49.5, 4.6, HOLE, f' stroke="{INK}" stroke-width="2.8"')
    return fit(out, 0.501, 31.7, 31.9)


@reg("io.github.dlippok.photometric-viewer", AMBER_DEEP)
def photometric_viewer():
    out = ink_rrect(18, 4, 28, 10, 4) + dim(poly([(22, 17), (42, 17), (60, 52), (4, 52)], INK, 3), .45)
    out += ink_stroke("M4 52Q32 36 60 52", 4.4) + ink_stroke("M32 20V44", 3.4, HOLE) + ink_stroke("M26 25L22 40M38 25L42 40", 3, HOLE)
    return fit(out, 0.536, 31.8, 36.3)


@reg("io.github.dman95.SASM", BROWN_DARK)
def sasm():
    out = ink_rrect(14, 14, 36, 36, 5, INK)
    for k in range(4):
        o = 19.5 + k * 8.7
        out += ink_rrect(o, 5, 4.6, 9, 2.3) + ink_rrect(o, 50, 4.6, 9, 2.3) + ink_rrect(5, o, 9, 4.6, 2.3) + ink_rrect(50, o, 9, 4.6, 2.3)
    out += ink_rrect(21, 21, 22, 22, 3, HOLE) + ink_stroke("M26 27L32 32L26 37", 3.2) + ink_stroke("M34 38H39", 3.2)
    return fit(out, 0.579, 32.0, 31.9)


@reg("io.github.doukutsu_rs.doukutsu-rs", RED_DARK)
def doukutsu_rs():
    out = path("M4 56V40Q4 10 32 8Q60 10 60 40V56Z", INK) + path("M18 56V42Q18 28 32 28Q46 28 46 42V56Z", HOLE)
    out += star4(32, 44, 7)
    return fit(out, 0.574, 31.8, 40.0)


@reg("io.github.dp0sk.Crosspipe", DEEP_ORANGE_DEEP)
def crosspipe():
    out = ink_stroke("M8 14C30 14 34 50 56 50", 6)
    out += ink_stroke("M8 50C30 50 34 14 56 14", 11, HOLE) + ink_stroke("M8 50C30 50 34 14 56 14", 6)
    out += ink_circle(8, 14, 5.4) + ink_circle(56, 50, 5.4) + ink_circle(8, 50, 5.4) + ink_circle(56, 14, 5.4)
    return fit(out, 0.518, 32.0, 31.9)


@reg("io.github.dprietob.queue", LIGHT_BLUE)
def queue():
    out = poly([(6, 6), (6, 24), (21, 15)], INK, 4) + ink_stroke("M30 15H58", 5) + ink_stroke("M8 34H58", 5) + ink_stroke("M8 50H44", 5)
    return fit(out, 0.546, 29.2, 27.2)


@reg("io.github.dragonGR.Dropzone", BROWN_DEEP)
def dropzone():
    out = ink_rrect(6, 6, 52, 52, 10, "none", ' stroke="INK" stroke-width="4.4" stroke-dasharray="8 7" stroke-linecap="round"')
    return fit(out + ink_stroke("M32 18V36", 5) + arrowhead(32, 33, 0, 1, 12), 0.53, 31.6, 31.9)


@reg("io.github.dtsudo.ChessCompStompWithHacks", PINK_SOFT)
def chesscompstompwithhacks():
    out = path("M14 6H23V14H28V6H36V14H41V6H50V26L43 32V46L50 52V58H14V52L21 46V32L14 26Z", INK)
    out += ink_stroke("M24 22H40", 2.6, HOLE) + ink_stroke("M26 52H38", 2.6, HOLE)
    return fit(out, 0.583, 31.8, 32.0)


@reg("io.github.dtsudo.SymbiosisChess", DEEP_PURPLE_LIGHT)
def symbiosischess():
    out = ell(32, 24, 11, 15) + ink_circle(32, 7, 4.2) + ink_stroke("M27 15L38 27", 3.6, HOLE) + ink_rrect(18, 38, 28, 6, 3) + path("M22 44H42L48 58H16Z", INK)
    return fit(out, 0.617, 31.9, 32.6)


@reg("io.github.dtsudo.TuxPlanetSpeedrunAnyPercent", PURPLE_SOFT)
def tuxplanetspeedrunanypercent():
    out = ink_circle(32, 34, 17) + rot(ellring(32, 34, 28, 8, 8, HOLE) + ellring(32, 34, 28, 8, 4), -20, 32, 34)
    return fit(out + star4(10, 10, 6), 0.593, 29.3, 27.1)


@reg("io.github.dubstar_04.design", BLUE_GREY_SOFT)
def design():
    out = poly([(8, 8), (8, 56), (56, 56)], INK, 4) + poly([(18, 30), (18, 46), (34, 46)], HOLE, 2)
    out += ink_stroke("M8 18H13", 2.6, HOLE) + ink_stroke("M8 26H13", 2.6, HOLE) + ink_stroke("M8 34H13", 2.6, HOLE) + ink_stroke("M8 42H13", 2.6, HOLE)
    return fit(out, 0.511, 31.9, 31.9)


@reg("io.github.dweymouth.supersonic", PINK_DEEP)
def supersonic():
    out = ell(20, 46, 11, 8.5) + ink_rrect(27, 8, 5.4, 38, 2.4) + path("M32 8Q50 12 48 28Q44 18 32 20Z", INK)
    out += ink_stroke("M42 40A8 8 0 0 1 42 54", 3.6) + ink_stroke("M50 34A16 16 0 0 1 50 60", 3.6)
    return fit(out, 0.629, 36.0, 36.3)


@reg("io.github.dxx_rebirth.dxx-rebirth", YELLOW_DARK)
def dxx_rebirth():
    out = ink_rrect(4, 4, 56, 56, 6, "none", ' stroke="INK" stroke-width="4"') + ink_rrect(21, 21, 22, 22, 3, "none", ' stroke="INK" stroke-width="4"')
    for a, b, c, d in ((4, 4, 21, 21), (60, 4, 43, 21), (4, 60, 21, 43), (60, 60, 43, 43)):
        out += ink_stroke(f"M{a} {b}L{c} {d}", 3.6)
    return fit(out, 0.443, 31.8, 31.8)


@reg("io.github.dyegoaurelio.simple-wireplumber-gui", BLUE)
def simple_wireplumber_gui():
    out = ""
    for x, y in ((14, 18), (32, 38), (50, 26)):
        out += ink_stroke(f"M{x} 6V58", 4.4) + ink_rrect(x - 8, y - 5, 16, 10, 3.5, INK, f' stroke="{HOLE}" stroke-width="2.6"')
    return fit(out, 0.543, 31.8, 32.0)


@reg("io.github.dynobo.sphereview", GREY_DEEP)
def sphereview():
    out = ring_c(32, 28, 22, 4.4) + ellring(32, 28, 9, 22, 3.4) + ink_stroke("M10 28H54", 3.4) + ink_stroke("M14 16H50", 3) + ink_stroke("M14 40H50", 3)
    out += ink_stroke("M10 54Q32 62 54 54", 4) + arrowhead(54, 54, 1, -0.2, 7)
    return fit(out, 0.563, 34.5, 35.7)


@reg("io.github.ebonjaeger.bluejay", ORANGE_DEEP)
def bluejay():
    out = rot(ell(30, 38, 21, 13), -20, 30, 38) + ink_circle(46, 22, 10) + poly([(42, 14), (40, 2), (53, 11)], INK, 2)
    out += poly([(54, 19), (63, 24), (54, 28)], INK, 2) + poly([(14, 38), (0, 56), (9, 58), (22, 46)], INK, 2)
    out += ink_stroke("M22 38Q32 30 42 38", 3.4, HOLE) + ink_circle(48, 21, 2.2, HOLE)
    return fit(out, 0.501, 29.4, 35.9)


@reg("io.github.ecotubehq.player", PURPLE_DEEP)
def player():
    out = path("M10 54C8 24 24 8 56 8C58 38 42 56 10 54Z", INK) + poly([(26, 22), (26, 42), (42, 32)], HOLE, 3) + ink_stroke("M10 54L3 61", 3.6)
    return fit(out, 0.479, 28.6, 35.1)


@reg("io.github.efogdev.mpris-timer", YELLOW_DARK)
def mpris_timer():
    out = ink_circle(32, 36, 22) + path("M32 36V16A20 20 0 0 1 52 36Z", HOLE) + ink_rrect(26, 4, 12, 6, 2.5) + ink_rrect(29.5, 9, 5, 7, 1)
    out += rot(ink_rrect(49, 11, 8, 5, 2), 45, 53, 13)
    return fit(out, 0.663, 34.5, 30.8)


@reg("io.github.eiskaltdcpp.eiskaltdcpp", LIGHT_BLUE_LIGHT)
def eiskaltdcpp():
    out = ""
    for a in (90, 150, 210):
        x1, y1 = pt(32, 32, 26, a)
        x2, y2 = pt(32, 32, 26, a + 180)
        out += ink_stroke(f"M{f(x1)} {f(y1)}L{f(x2)} {f(y2)}", 4.4)
    for a in range(0, 360, 60):
        x, y = pt(32, 32, 17, a)
        for d in (-50, 50):
            x2, y2 = pt(x, y, 8, a + d)
            out += ink_stroke(f"M{f(x)} {f(y)}L{f(x2)} {f(y2)}", 3.4)
    return fit(out, 0.649, 31.8, 31.9)


@reg("io.github.elahpeca.Eigen", INDIGO)
def eigen():
    out = ink_stroke("M17 8H8V56H17", 4.6) + ink_stroke("M47 8H56V56H47", 4.6)
    for x, y in ((20, 16), (33, 16), (20, 35), (33, 35)):
        out += ink_rrect(x, y, 11, 13, 2.5)
    return fit(out, 0.506, 31.8, 32.0)


@reg("io.github.electronstudio.WeylusCommunityEdition", DEEP_ORANGE_DARK)
def weyluscommunityedition():
    out = ink_rrect(4, 14, 50, 38, 6) + ink_rrect(9, 19, 40, 28, 2, HOLE) + ink_stroke("M14 40Q22 26 30 36T44 30", 3.4)
    pen = "M43 8H51L52 40L47 49L42 40Z"
    out += rot(path(pen, INK, f' stroke="{HOLE}" stroke-width="3" stroke-linejoin="round"'), 28, 47, 30)
    return fit(out, 0.568, 31.9, 31.2)


@reg("io.github.ellie_commons.sequeler", YELLOW_DARK)
def sequeler():
    out = path("M10 14V46Q10 56 32 56Q54 56 54 46V14Z", INK) + ell(32, 14, 22, 8)
    out += ink_stroke("M10 26Q32 36 54 26", 3, HOLE) + ink_stroke("M10 38Q32 48 54 38", 3, HOLE)
    return fit(out, 0.644, 31.8, 30.7)


@reg("io.github.eminfedar.vaktisalah-gtk-rs", RED_SOFT)
def vaktisalah_gtk_rs():
    out = path("M38 4A27 27 0 1 0 56 48A21 21 0 1 1 38 4Z", INK)
    return fit(out + star4(50, 18, 9), 0.675, 35.0, 30.7)


@reg("io.github.enginkirmaci.lumux", BROWN_LIGHT)
def lumux():
    out = ink_circle(32, 26, 16) + path("M21 36Q25 44 25 48H39Q39 44 43 36Z", INK) + ink_rrect(24, 50, 16, 5, 2.5) + ink_rrect(27, 56, 10, 4, 2)
    out += ink_stroke("M26 30L29 21L34 30L37 21", 2.8, HOLE)
    for a in (-90, -140, -40, 180, 0):
        x1, y1 = pt(32, 26, 22, a)
        x2, y2 = pt(32, 26, 28, a)
        out += ink_stroke(f"M{f(x1)} {f(y1)}L{f(x2)} {f(y2)}", 3.4)
    return fit(out, 0.577, 32.0, 28.1)


@reg("io.github.epasveer.seer", CYAN_DEEP)
def seer():
    out = path("M3 32Q32 4 61 32Q32 60 3 32Z", INK) + ink_circle(32, 32, 12, HOLE) + ink_circle(32, 32, 6) + ink_circle(36, 28, 2.2, HOLE)
    return fit(out, 0.635, 31.8, 31.9)


@reg("io.github.eqonomize.eqonomize", DEEP_PURPLE)
def eqonomize():
    out = path("M28 38L50 38A22 22 0 1 1 28 16Z", INK) + path("M33 33V11A22 22 0 0 1 55 33Z", INK)
    return fit(out, 0.717, 30.3, 35.4)


@reg("io.github.erenseymen.android-tv-remote", RED_LIGHT)
def android_tv_remote():
    out = ink_rrect(18, 2, 28, 60, 9) + ring_c(32, 22, 8, 3.6, HOLE) + ink_circle(32, 22, 3, HOLE)
    out += ink_circle(24, 41, 3.4, HOLE) + ink_circle(40, 41, 3.4, HOLE) + ink_rrect(23, 48, 18, 4, 2, HOLE) + ink_rrect(23, 55, 18, 3, 1.5, HOLE)
    return fit(out, 0.598, 31.9, 31.8)


@reg("io.github.erkin.ponysay", ORANGE_DARK)
def ponysay():
    out = ell(32, 27, 28, 21) + poly([(16, 42), (10, 58), (32, 46)], INK, 3) + poly([(32, 7), (22, 40), (42, 40)], HOLE, 2)
    out += ink_stroke("M26 30L38 25", 2.6) + ink_stroke("M24.5 36L39.5 31", 2.6) + ink_stroke("M29 21L35 19", 2.4)
    return fit(out, 0.576, 31.8, 36.7)


@reg("io.github.essentialist_app.essentialist", BLUE_GREY_SOFT)
def essentialist():
    out = path("M6 8H58L38 32V50L26 58V32Z", INK) + star4(32, 19, 7, HOLE)
    return fit(out, 0.578, 31.9, 26.5)


@reg("io.github.everestapi.Olympus", BLUE_DEEP)
def olympus():
    out = poly([(2, 56), (24, 18), (34, 32), (42, 22), (62, 56)], INK, 3) + poly([(17, 28), (24, 18), (31, 28), (27, 27), (24, 31), (21, 27)], HOLE, 1.5)
    out += ink_stroke("M42 22V6", 3.2) + poly([(42, 6), (54, 10), (42, 15)], INK, 1.5)
    return fit(out, 0.505, 31.8, 38.0)


@reg("io.github.fabiangreffrath.Doom", DEEP_PURPLE_DARK)
def doom():
    out = ring_c(32, 30, 25, 4)
    pts = [pt(32, 30, 21, -90 + 144 * k) for k in range(5)]
    out += ink_stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z", 4)
    return fit(out, 0.677, 31.8, 29.9)


@reg("io.github.fabrialberio.pinapp", BROWN)
def pinapp():
    out = ink_rrect(4, 8, 22, 22, 6) + ink_rrect(4, 34, 22, 22, 6) + ink_rrect(30, 34, 22, 22, 6)
    out += rot(path("M38 4H50L48 16L54 24H34L40 16Z", INK) + ink_stroke("M44 24V36", 3.4), 32, 44, 22)
    return fit(out, 0.532, 32.0, 31.6)


@reg("io.github.falldaemon.engplayer", BLUE_GREY_DARK)
def engplayer():
    out = ink_rrect(4, 8, 56, 38, 12) + poly([(16, 44), (12, 59), (30, 46)], INK, 3) + poly([(27, 18), (27, 36), (42, 27)], HOLE, 3)
    return fit(out, 0.553, 31.6, 34.0)


@reg("io.github.faridjaff.StickyNotesCanvas", GREY)
def stickynotescanvas():
    back = dim(rot(ink_rrect(24, 4, 34, 34, 3), 10, 41, 21), .5)
    out = back + path("M8 18H46V46L34 58H8Z", INK) + poly([(34, 58), (34, 46), (46, 46)], HOLE, 0.5)
    out += ink_stroke("M14 28H38", 3.4, HOLE) + ink_stroke("M14 37H32", 3.4, HOLE)
    return fit(out, 0.511, 33.7, 32.5)


@reg("io.github.fastrizwaan.WebkitWord", RED)
def webkitword():
    out = path("M24 6A15 15 0 0 0 24 36H28V58H34V12H40V58H46V6Z", INK)
    return fit(out, 0.631, 32.6, 31.9)


@reg("io.github.ferraridamiano.ConverterNOW", DEEP_ORANGE)
def converternow():
    out = ink_stroke("M6 20H48", 5) + arrowhead(48, 20, 1, 0, 10) + ink_stroke("M58 44H16", 5) + arrowhead(16, 44, -1, 0, 10)
    return fit(out, 0.589, 31.8, 31.8)


@reg("io.github.fezlight.mine4ease", TEAL)
def mine4ease():
    out = poly([(32, 4), (58, 18), (32, 32), (6, 18)], INK, 2) + dim(poly([(6, 22), (30, 35), (30, 62), (6, 48)], INK, 2), .62) + dim(poly([(34, 35), (58, 22), (58, 48), (34, 62)], INK, 2), .38)
    out += ink_stroke("M20 11L44 25", 2.6, HOLE) + ink_stroke("M44 11L20 25", 2.6, HOLE)
    return fit(out, 0.591, 32.0, 32.8)


@reg("io.github.fidele007.akkhara", CYAN_DARK)
def akkhara():
    out = ink_rrect(4, 6, 56, 52, 12) + ink_stroke("M20 42C12 24 30 14 38 24C46 34 28 42 26 30", 4.6, HOLE) + ink_stroke("M48 16V40Q48 46 53 46", 4.6, HOLE)
    return fit(out, 0.55, 31.7, 31.9)


@reg("io.github.finefindus.Hieroglyphic", DEEP_PURPLE_SOFT)
def hieroglyphic():
    out = ink_stroke("M48 10H16L34 32L16 54H50", 6.4) + ink_stroke("M48 10V17", 5) + ink_stroke("M50 54V47", 5)
    return fit(out, 0.591, 32.8, 31.8)


@reg("io.github.fizzyizzy05.binary", INDIGO_DEEP)
def binary():
    out = ellring(18, 32, 11, 19, 5.4) + ink_stroke("M40 22L50 12V52", 5.6) + ink_stroke("M40 52H60", 5.6)
    return fit(out, 0.559, 35.6, 34.6)


@reg("io.github.fjrevoredo.mini-diarium", BLUE_GREY_DEEP)
def mini_diarium():
    out = ink_rrect(10, 4, 44, 56, 5) + ink_stroke("M26 4V60", 2.4, HOLE) + ink_stroke("M33 24H47", 3.4, HOLE) + ink_stroke("M33 33H44", 3.4, HOLE) + ink_stroke("M33 42H47", 3.4, HOLE)
    out += path("M40 4V24L45 19L50 24V4Z", INK, f' stroke="{HOLE}" stroke-width="2.4" stroke-linejoin="round"')
    return fit(out, 0.545, 31.9, 32.0)


@reg("io.github.fkinoshita.Telegraph", TEAL_LIGHT)
def telegraph():
    out = ink_rrect(4, 50, 56, 9, 3) + ink_rrect(27, 40, 10, 12, 2) + ink_rrect(46, 44, 9, 8, 2)
    out += rot(ink_rrect(6, 33, 52, 7, 3.5), -9, 32, 38) + ink_circle(13, 24, 8) + ink_rrect(11, 26, 4, 10, 1)
    return fit(out, 0.561, 31.9, 39.7)


@reg("io.github.fm_elpac.pmim_ibus", AMBER_DEEP)
def pmim_ibus():
    out = ink_rrect(4, 8, 56, 24, 7) + ink_rrect(8, 12, 17, 16, 3.5, HOLE) + ink_stroke("M12 20H21", 3) + ink_stroke("M16.5 15.5V24.5", 3)
    out += ink_stroke("M32 20H42", 3.4, HOLE) + ink_stroke("M48 20H53", 3.4, HOLE) + poly([(18, 34), (32, 34), (25, 43)], INK, 1.5)
    out += ink_rrect(16, 47, 32, 12, 5)
    return fit(out, 0.569, 31.8, 29.1)


@reg("io.github.foldynl.QLog", PURPLE)
def qlog():
    out = ink_stroke("M32 18L15 60", 4.4) + ink_stroke("M32 18L49 60", 4.4) + ink_stroke("M23 40H41", 3.4) + ink_stroke("M27 29H37", 3.4) + ink_stroke("M19 50H45", 3.4)
    out += ink_circle(32, 16, 5) + ink_stroke("M19 7Q14 16 19 25", 3.4) + ink_stroke("M45 7Q50 16 45 25", 3.4) + ink_stroke("M11 2Q3 16 11 30", 3.2) + ink_stroke("M53 2Q61 16 53 30", 3.2)
    return fit(out, 0.501, 31.9, 30.0)


@reg("io.github.forkgram.tdesktop", BLUE_LIGHT)
def tdesktop():
    out = dim(ink_rrect(20, 4, 40, 28, 8), .5)
    out += ink_rrect(4, 22, 44, 28, 8, INK, f' stroke="{HOLE}" stroke-width="3.4"') + poly([(10, 48), (8, 60), (22, 50)], INK, 3)
    out += ink_stroke("M13 32H37", 3.4, HOLE) + ink_stroke("M13 40H29", 3.4, HOLE)
    return fit(out, 0.493, 31.9, 33.6)


@reg("io.github.fragglet.sdl_sopwith", BROWN_SOFT)
def sdl_sopwith():
    out = ell(32, 34, 22, 8) + poly([(12, 32), (3, 18), (10, 18), (19, 29)], INK, 2) + ink_rrect(14, 11, 34, 6.5, 3.2) + ink_rrect(12, 46, 34, 6.5, 3.2)
    out += ink_stroke("M21 17L21 46", 3.4) + ink_stroke("M41 17L41 46", 3.4) + ink_rrect(53, 22, 4.4, 24, 2.2) + ink_circle(30, 59, 4.4) + ink_stroke("M25 50L29 56", 3.2)
    out += ell(34, 31, 5.5, 3.4, HOLE)
    return fit(out, 0.597, 28.8, 32.5)


@reg("io.github.fralonra.PpdEditor", LIGHT_BLUE_DEEP)
def ppdeditor():
    out = ink_rrect(4, 24, 56, 26, 6) + ink_rrect(16, 6, 32, 20, 3, INK, f' stroke="{HOLE}" stroke-width="2.6"')
    out += ink_circle(51, 33, 2.6, HOLE) + ink_rrect(14, 42, 36, 18, 3, INK, f' stroke="{HOLE}" stroke-width="2.6"') + ink_stroke("M20 49H44", 2.8, HOLE) + ink_stroke("M20 55H34", 2.8, HOLE)
    out += ink_stroke("M22 12H42", 2.8, HOLE)
    return fit(out, 0.611, 32.0, 34.1)


@reg("io.github.fralonra.WgShadertoy", PURPLE_LIGHT)
def wgshadertoy():
    out = ink_stroke("M32 14L52 48H12Z", 4) + ink_stroke("M2 42L22 36", 3.4) + ink_stroke("M40 34L62 24", 3.2) + ink_stroke("M43 40L62 40", 3.2) + ink_stroke("M43 46L58 56", 3.2)
    return fit(out + star4(46, 8, 6), 0.533, 33.5, 33.8)


@reg("io.github.friesi23.mhabit", BLUE_DARK)
def mhabit():
    out = dim(ring_c(32, 30, 22, 5), .35) + ink_stroke("M32 8A22 22 0 1 1 10 30", 5) + circle(32, 30, 5.5, INK)
    return fit(out, 0.746, 31.9, 29.8)


@reg("io.github.gaheldev.Millisecond", PINK)
def millisecond():
    out = ink_rrect(10, 4, 44, 6, 3) + ink_rrect(10, 54, 44, 6, 3) + path("M16 10H48Q48 26 36 32Q48 38 48 54H16Q16 38 28 32Q16 26 16 10Z", INK)
    out += poly([(23, 15), (41, 15), (32, 24)], HOLE, 1.5) + poly([(32, 43), (22, 51), (42, 51)], HOLE, 1.5) + ink_stroke("M32 25V43", 1.8, HOLE)
    return fit(out, 0.533, 31.8, 31.8)


@reg("io.github.gamingdoom.Datcord", CYAN_DARK)
def datcord():
    out = ink_stroke("M10 36V30Q10 8 32 8Q54 8 54 30V36", 5) + ink_rrect(5, 32, 12, 20, 5) + ink_rrect(47, 32, 12, 20, 5)
    out += ink_stroke("M53 50Q52 58 38 58", 3.6) + ink_rrect(30, 54, 10, 8, 4)
    return fit(out, 0.612, 31.8, 34.9)


@reg("io.github.garrett_webb.terminalpolyominos", DEEP_PURPLE_DEEP)
def terminalpolyominos():
    out = cells([(0, 0), (0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (3, 0), (2, 1)])
    out += dim(cells([(3, 1), (3, 2), (2, 2)]), .5)
    return fit(out, 0.562, 30.8, 25.8)


@reg("io.github.gen2brain.cbconvert", GREY_DARK)
def cbconvert():
    out = ink_rrect(24, 18, 16, 22, 3) + ink_stroke("M29 25H35", 2.6, HOLE) + ink_stroke("M29 31H35", 2.6, HOLE)
    out += ink_stroke("M10 28A24 24 0 0 1 46 10", 4.6) + arrowhead(46, 10, 0.95, 0.35, 8)
    out += ink_stroke("M54 34A24 24 0 0 1 18 52", 4.6) + arrowhead(18, 52, -0.95, -0.35, 8)
    return fit(out, 0.556, 31.8, 31.0)


@reg("io.github.georgewoodall82.jsymphonic", YELLOW_DARK)
def jsymphonic():
    out = ink_rrect(14, 2, 36, 60, 8) + ink_rrect(20, 8, 24, 16, 3, HOLE) + ring_c(32, 44, 10, 3.6, HOLE) + ink_circle(32, 44, 3.4, HOLE)
    return fit(out, 0.57, 31.8, 31.8)


@reg("io.github.gerryferdinandus.bittorrent-tracker-editor", BLUE_GREY)
def bittorrent_tracker_editor():
    out = ink_stroke("M14 14V34Q14 52 32 52Q50 52 50 34V14", 10, INK) + ink_rrect(9, 4, 10, 12, 2) + ink_rrect(45, 4, 10, 12, 2)
    out += ink_rrect(9, 16, 10, 3, 0, HOLE) + ink_rrect(45, 16, 10, 3, 0, HOLE)
    return fit(out, 0.591, 31.8, 25.9)


@reg("io.github.getnf.embellish", BROWN_DARK)
def embellish():
    out = ink_stroke("M12 56L30 8L48 56", 6.4) + ink_stroke("M19 40H41", 5)
    return fit(out + star4(52, 14, 10), 0.532, 33.1, 32.7)


@reg("io.github.gimletlove.imagecompare", GREY_DEEP)
def imagecompare():
    out = ink_rrect(4, 10, 56, 44, 8, "none", ' stroke="INK" stroke-width="4"') + path("M12 10H32V54H12Q4 54 4 46V18Q4 10 12 10Z", INK)
    out += path("M9 46L18 34L25 42L31 37V46Z", HOLE) + ink_stroke("M32 4V60", 3.6)
    out += ink_circle(32, 32, 8, INK, f' stroke="{HOLE}" stroke-width="3"') + ink_stroke("M30 29L27 32L30 35", 2.2, HOLE) + ink_stroke("M34 29L37 32L34 35", 2.2, HOLE)
    return fit(out, 0.532, 31.7, 31.9)


@reg("io.github.glaumar.QRookie", PINK_LIGHT)
def qrookie():
    out = ""
    for x, y in ((4, 4), (38, 4), (4, 38)):
        out += ink_rrect(x + 2, y + 2, 18, 18, 3.5, "none", ' stroke="INK" stroke-width="4"') + ink_rrect(x + 8.5, y + 8.5, 7, 7, 1.5)
    out += ink_rrect(38, 38, 9, 9, 2) + ink_rrect(51, 51, 9, 9, 2) + ink_rrect(51, 38, 9, 9, 2, INK) + ink_rrect(38, 51, 9, 9, 2)
    return fit(out, 0.482, 32.5, 32.5)


@reg("io.github.glitterware.Passy", TEAL_SOFT)
def passy():
    out = ink_circle(18, 20, 14) + ink_circle(18, 20, 6, HOLE) + ink_stroke("M28 30L56 58", 7) + ink_stroke("M48 50L55 43", 5.6) + ink_stroke("M40 42L46 36", 5.6)
    return fit(out, 0.515, 33.3, 35.3)


@reg("io.github.go_musicfox.go-musicfox", DEEP_ORANGE_LIGHT)
def go_musicfox():
    out = path("M4 6L20 18H44L60 6V32Q60 52 32 60Q4 52 4 32Z", INK)
    out += poly([(13, 30), (26, 34), (18, 40)], HOLE, 1.5) + poly([(51, 30), (38, 34), (46, 40)], HOLE, 1.5) + poly([(28, 47), (36, 47), (32, 53)], HOLE, 1.5)
    out += poly([(12, 12), (17, 17), (11, 22)], HOLE, 1) + poly([(52, 12), (47, 17), (53, 22)], HOLE, 1)
    return fit(out, 0.539, 31.9, 25.7)


@reg("io.github.grangerhub.Tremulous", INDIGO)
def tremulous():
    out = path("M32 4Q58 4 58 28Q58 44 40 56Q32 62 24 56Q6 44 6 28Q6 4 32 4Z", INK)
    out += poly([(10, 22), (27, 31), (22, 38), (10, 31)], HOLE, 2) + poly([(54, 22), (37, 31), (42, 38), (54, 31)], HOLE, 2) + ink_stroke("M26 50H38", 3, HOLE)
    return fit(out, 0.648, 31.9, 30.5)


@reg("io.github.greykaizen.tur", CYAN)
def tur():
    out = ink_stroke("M16 8H48", 4.6) + ink_stroke("M16 22L32 36L48 22", 5.4) + ink_stroke("M16 38L32 52L48 38", 5.4)
    return fit(out, 0.671, 31.9, 27.1)


@reg("io.github.gutopardini.wayshot", RED_DEEP)
def wayshot():
    out = ""
    for sx, sy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        x, y = (6 if sx > 0 else 58), (6 if sy > 0 else 58)
        out += ink_stroke(f"M{x} {y + 14 * sy}V{y}H{x + 14 * sx}", 4.4)
    out += ink_circle(32, 32, 12) + ring_c(32, 32, 5.5, 2.8, HOLE)
    return fit(out, 0.472, 32.0, 32.0)


@reg("io.github.h8moss.progressive", DEEP_ORANGE_DARK)
def progressive():
    out = ink_rrect(4, 24, 56, 22, 11, "none", ' stroke="INK" stroke-width="4.4"') + ink_rrect(11, 31, 30, 8, 4)
    out += poly([(38, 8), (50, 8), (44, 17)], INK, 2)
    return fit(out, 0.6, 31.9, 31.2)


@reg("io.github.hafmed.Basic-Numerical-Methods-qml", TEAL_DARK)
def basic_numerical_methods_qml():
    out = ink_stroke("M8 6V56H58", 3.8) + ink_stroke("M12 50C24 48 34 38 40 26C44 18 50 14 58 12", 4.2) + ink_stroke("M24 43L52 13", 3)
    out += ink_circle(40, 26, 4.8, INK, f' stroke="{HOLE}" stroke-width="2.4"')
    return fit(out, 0.492, 32.8, 30.8)


@reg("io.github.hafmed.Hydraulics-Channel-GVF", CYAN_DEEP)
def hydraulics_channel_gvf():
    out = ink_stroke("M5 12L15 52H49L59 12", 5.4) + path("M10 32Q19 26 26 32T42 32T55 32L49 48H15Z", INK)
    return fit(out, 0.55, 31.9, 26.3)


@reg("io.github.hafmed.TP-Labo-Hyd", DEEP_PURPLE)
def tp_labo_hyd():
    out = ink_stroke("M22 5H42", 4.6) + ink_stroke("M25 5V24L8 52Q5 59 12 59H52Q59 59 56 52L39 24V5", 4.6) + path("M17 40H47L55 53Q58 59 51 59H13Q6 59 9 53Z", INK)
    out += ink_circle(32, 30, 2.6) + ink_circle(36, 21, 2)
    return fit(out, 0.528, 32.0, 35.8)


@reg("io.github.hafmed.Thakir-Prayer-Times", RED_LIGHT)
def thakir_prayer_times():
    out = path("M17 34Q17 14 32 12Q47 14 47 34Z", INK) + ink_stroke("M32 12V3", 3.2) + ink_rrect(14, 34, 36, 24, 0)
    out += ink_rrect(2, 22, 9, 36, 3) + poly([(2, 22), (6.5, 10), (11, 22)], INK, 2) + ink_rrect(53, 22, 9, 36, 3) + poly([(53, 22), (57.5, 10), (62, 22)], INK, 2)
    out += path("M26 58V47Q26 41 32 41Q38 41 38 47V58Z", HOLE)
    return fit(out, 0.501, 31.9, 34.8)


@reg("io.github.hafmed.Water-Hammer-Simulation", DEEP_ORANGE_DEEP)
def water_hammer_simulation():
    out = ink_rrect(2, 38, 44, 13, 3) + ink_stroke("M3 24H12L17 10L24 32L29 18L33 24H38", 3.8)
    out += ink_rrect(42, 33, 18, 23, 3, INK, f' stroke="{HOLE}" stroke-width="2.6"') + ink_rrect(49, 22, 4, 11, 1.5) + ink_rrect(43, 16, 16, 6, 3)
    return fit(out, 0.564, 31.3, 35.4)


@reg("io.github.halfmexican.Mingle", BLUE_GREY_SOFT)
def mingle():
    out = ink_circle(24, 34, 19) + ink_circle(42, 30, 19, INK, f' stroke="{HOLE}" stroke-width="3.4"')
    out += ink_stroke("M13 28V33", 3.4, HOLE) + ink_stroke("M21 28V33", 3.4, HOLE) + ink_stroke("M12 42Q17 48 22 42", 3.4, HOLE)
    out += ink_stroke("M36 22V27", 3.4, HOLE) + ink_stroke("M47 22V27", 3.4, HOLE) + ink_stroke("M35 36Q41.5 43 48 36", 3.4, HOLE)
    return fit(out, 0.67, 32.1, 32.1)
