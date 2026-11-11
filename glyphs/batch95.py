# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 95: Coulomb to jottr."""
from lm import (
    AMBER_DARK, AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_GREY_SOFT, BLUE_LIGHT, BROWN, BROWN_DARK, BROWN_DEEP,
    BROWN_LIGHT, BROWN_SOFT, CYAN, CYAN_DARK, DEEP_ORANGE, DEEP_ORANGE_DARK, DEEP_ORANGE_DEEP,
    DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_DARK, DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT,
    DEEP_PURPLE_SOFT, f, GREY_DARK, GREY_DEEP, HOLE, INDIGO, INDIGO_DARK, INDIGO_DEEP,
    INDIGO_LIGHT, INDIGO_SOFT, INK, LIGHT_BLUE, LIGHT_BLUE_DARK, LIGHT_BLUE_DEEP,
    LIGHT_BLUE_LIGHT, line, ORANGE_DARK, ORANGE_DEEP, path, PINK, PINK_DARK, PINK_DEEP,
    PINK_LIGHT, PINK_SOFT, poly, pt, PURPLE, PURPLE_DARK, PURPLE_DEEP, PURPLE_LIGHT,
    PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_LIGHT, RED_SOFT, stroke, TEAL, TEAL_DARK,
    TEAL_DEEP, TEAL_LIGHT, TEAL_SOFT, YELLOW_DARK,
)
from glyphs.kit import (
    arc_arrow, arrowhead, crescent, dim, ell, fit, hexring, hx, ink_circle, ink_rrect, ink_stroke, registry, ring_c, rot, spiral, star4, star5)

ICONS, SMALL, reg, _ = registry()


@reg("io.github.hamza_algohary.Coulomb", DEEP_PURPLE_SOFT)
def coulomb():
    out = ink_circle(21, 40, 15) + ink_stroke("M21 33V47", 3.6, HOLE) + ink_stroke("M14 40H28", 3.6, HOLE)
    out += ink_circle(47, 17, 9) + ink_stroke("M43 17H51", 3.4, HOLE)
    out += dim(ink_stroke("M33 30L40 24", 3.4), .65)
    return fit(out, 0.630, 32.1, 30.7)


@reg("io.github.heathcliff26.go-minesweeper", LIGHT_BLUE_DEEP)
def go_minesweeper():
    out = ink_circle(32, 32, 14)
    for k in range(8):
        a, b = pt(32, 32, 12, 45 * k), pt(32, 32, 25, 45 * k)
        out += ink_stroke(f"M{f(a[0])} {f(a[1])}L{f(b[0])} {f(b[1])}", 5)
    return fit(out + ink_circle(27, 27, 3.4, HOLE), 0.672, 32.1, 32.1)


@reg("io.github.hedge_dev.hedgemodmanager", GREY_DEEP)
def hedgemodmanager():
    out = ell(30, 40, 22, 15)
    out += poly([(8, 38), (5, 22), (14, 27), (15, 11), (23, 21), (29, 7), (34, 20), (42, 11), (43, 26), (51, 22), (46, 34)], INK, 2)
    out += poly([(44, 32), (60, 41), (52, 50), (42, 48)], INK, 2.4)
    out += ink_circle(59, 41, 2.8, HOLE) + ink_circle(46, 38, 2.4, HOLE)
    return fit(out + ink_rrect(14, 52, 9, 6, 2.5) + ink_rrect(36, 52, 9, 6, 2.5), 0.608, 32.6, 32.3)


@reg("io.github.heidefinnischen.cuneo", BLUE_DEEP)
def cuneo():
    out = ink_rrect(5, 8, 54, 48, 9)
    out += poly([(13, 22), (24, 16), (24, 28)], HOLE, 1.2) + ink_stroke("M24 22H34", 3.4, HOLE)
    out += poly([(13, 38), (24, 32), (24, 44)], HOLE, 1.2) + ink_stroke("M24 38H40", 3.4, HOLE)
    out += poly([(48, 38), (42, 26), (54, 26)], HOLE, 1.2) + ink_stroke("M48 26V16", 3.4, HOLE)
    return fit(out, 0.573, 31.9, 32.1)


@reg("io.github.helpseeker.Gyre", YELLOW_DARK)
def gyre():
    return fit(spiral(32, 32, 2, 25, 2.4, -90, 5.6) + ink_circle(32, 32, 3.6), 0.726, 34.8, 33.0)


@reg("io.github.hepfnepf.blutfest", RED_SOFT)
def blutfest():
    out = path("M32 5C42 20 52 30 52 41A20 20 0 0 1 12 41C12 30 22 20 32 5Z", INK)
    return fit(out + ink_stroke("M22 42Q22 51 30 54", 3.6, HOLE), 0.662, 32.0, 33.1)


@reg("io.github.herve4m.Hexkudo", CYAN)
def hexkudo():
    out = hx(19.5, 22, 13) + hexring(45, 22, 11.5, 3.6) + hx(32.2, 44.5, 13)
    return fit(out + ink_circle(32.2, 44.5, 4, HOLE) + ink_stroke("M14 22H25", 3.2, HOLE), 0.643, 31.6, 29.8)


@reg("io.github.herve4m.Length", ORANGE_DEEP)
def length():
    out = ink_rrect(4, 14, 56, 22, 4)
    for k, x in enumerate(range(12, 56, 8)):
        out += line(x, 14, x, 22 + (6 if k % 2 == 0 else 2), HOLE, 2.8, "butt")
    out += ink_stroke("M10 50H54", 3.4) + arrowhead(6, 50, -1, 0, 6) + arrowhead(58, 50, 1, 0, 6)
    return fit(out, 0.531, 31.9, 37.6)


@reg("io.github.hihebark.QuranReader", PURPLE_LIGHT)
def quranreader():
    out = path("M32 14C24 8 14 8 6 12V42C14 38 24 38 32 44Z", INK) + path("M32 14C40 8 50 8 58 12V42C50 38 40 38 32 44Z", INK)
    out += ink_stroke("M14 58L32 46L50 58", 4.4) + crescent(19, 25, 7, HOLE) + ink_stroke("M38 22H50", 2.8, HOLE) + ink_stroke("M38 29H50", 2.8, HOLE)
    return fit(out, 0.559, 32.1, 32.7)


@reg("io.github.hoisasa.SharksEmpire-English", AMBER_DARK)
def sharksempire_english():
    out = path("M14 42Q30 40 28 6Q44 26 52 42Z", INK)
    out += ink_stroke("M4 52Q10 46 16 52T28 52T40 52T52 52T60 52", 4.2)
    return fit(out, 0.563, 31.9, 38.8)


@reg("io.github.horsicq.detect-it-easy", BROWN_SOFT)
def detect_it_easy():
    out = ring_c(26, 26, 18, 5) + ink_stroke("M40 40L57 57", 7.2) + ink_stroke("M17 22H35M17 30H29", 4.6)
    return fit(out, 0.544, 35.6, 35.6)


@reg("io.github.hrkfdn.ncspot", INDIGO)
def ncspot():
    out = rot(ell(20, 46, 10, 7.4), -20, 20, 46) + ink_rrect(26.6, 10, 4.8, 34, 2.4)
    out += path("M31 10Q47 12 47 28Q42 20 31 21Z", INK) + ink_rrect(46, 42, 10, 15, 1.8)
    return fit(out, 0.666, 35.3, 36.9)


@reg("io.github.hrniels.Eventix", YELLOW_DARK)
def eventix():
    out = path("M6 14H58V27A6 6 0 0 0 58 39V52H6V39A6 6 0 0 0 6 27Z", INK)
    out += star5(24, 33, 9, HOLE) + stroke("M42 21V45", HOLE, 2.8, ' stroke-dasharray="3.5 4.5"')
    return fit(out, 0.578, 31.8, 32.8)


@reg("io.github.huderlem.porymap", BLUE_GREY_LIGHT)
def porymap():
    out = poly([(4, 14), (22, 8), (42, 14), (60, 8), (60, 50), (42, 56), (22, 50), (4, 56)], INK, 2)
    out += dim(line(22, 9, 22, 50, HOLE, 2.6, "butt") + line(42, 14, 42, 56, HOLE, 2.6, "butt"), .9)
    out += path("M32 46L24.5 34A9 9 0 1 1 39.5 34Z", HOLE, ' stroke="INK" stroke-width="2.4"') + ink_circle(32, 29, 3.2)
    return fit(out, 0.488, 32.2, 31.8)


@reg("io.github.hugomg.xjump-sdl", LIGHT_BLUE_LIGHT)
def xjump_sdl():
    out = ink_rrect(4, 50, 26, 6, 3) + ink_rrect(34, 32, 26, 6, 3) + ink_rrect(8, 14, 22, 6, 3)
    out += ink_circle(14, 41, 5.4) + dim(ink_stroke("M21 34Q30 22 44 24", 3.2), .7) + arrowhead(46, 24.5, 1, .15, 5)
    return fit(out, 0.609, 29.5, 37.1)


@reg("io.github.hurricangame.hurrican", AMBER_DEEP)
def hurrican():
    arm = path("M32 32C30 18 40 6 56 10C45 13 42 22 41 34Z", INK)
    return fit(rot(arm, 0, 32, 32) + rot(arm, 120, 32, 32) + rot(arm, 240, 32, 32) + ink_circle(32, 32, 4.4, HOLE), 0.574, 32.1, 32.0)


@reg("io.github.hvdwofl.jExifToolGUI", PINK)
def jexiftoolgui():
    out = poly([(6, 16), (36, 16), (58, 32), (36, 48), (6, 48)], INK, 3)
    return fit(out + ink_circle(14, 32, 3.4, HOLE) + ring_c(35, 32, 8, 3, HOLE) + ink_circle(35, 32, 2.6, HOLE), 0.619, 29.3, 32.0)


@reg("io.github.hydrusnetwork.hydrus", TEAL_DARK)
def hydrus():
    out = dim(rot(ink_rrect(8, 12, 34, 40, 5), -16, 25, 32), .4) + dim(rot(ink_rrect(22, 12, 34, 40, 5), 16, 39, 32), .6)
    out += ink_rrect(15, 12, 34, 42, 5, INK, f' stroke="{HOLE}" stroke-width="2.6"')
    out += poly([(20, 46), (30, 32), (36, 40), (40, 36), (45, 46)], HOLE, 1.6) + ink_circle(39, 24, 3.6, HOLE)
    return fit(out, 0.631, 32.0, 29.9)


@reg("io.github.hypengw.Qcm", DEEP_ORANGE_LIGHT)
def qcm():
    out = ink_circle(26, 34, 22) + ring_c(26, 34, 14, 2.4, HOLE) + ink_circle(26, 34, 6, HOLE) + ink_circle(26, 34, 2.2)
    return fit(out + ink_stroke("M54 8V30L48 44", 4.4) + ink_circle(54, 9, 4.6), 0.577, 33.5, 27.1)


@reg("io.github.iSlammedMyKindle.godotGem", DEEP_PURPLE_DARK)
def godotgem():
    out = poly([(14, 8), (50, 8), (60, 24), (32, 58), (4, 24)], INK, 3.4)
    out += ink_stroke("M6 24H58", 2.8, HOLE) + ink_stroke("M22 24L32 8L42 24", 2.8, HOLE) + ink_stroke("M22 24L32 54L42 24", 2.8, HOLE)
    return fit(out, 0.614, 31.9, 29.3)


@reg("io.github.idescriptor.iDescriptor", CYAN_DARK)
def idescriptor():
    out = ink_rrect(15, 4, 34, 56, 8) + ink_rrect(20, 12, 24, 38, 2.5, HOLE) + ink_rrect(27, 6.6, 10, 2.8, 1.4, HOLE)
    out += ink_circle(32, 23, 2.8) + ink_rrect(30, 29, 4, 13, 2) + ink_stroke("M28 55H36", 3, HOLE)
    return fit(out, 0.618, 31.8, 31.8)


@reg("io.github.idevecore.Valuta", GREY_DEEP)
def valuta():
    out = ink_circle(25, 36, 21) + ink_stroke("M33 28C28 21 17 25 20 31C23 36 33 34 31 41C29 47 18 47 16 42", 4.2, HOLE) + ink_stroke("M25.5 20V52", 3, HOLE)
    out += ink_circle(47, 19, 11, INK, f' stroke="{HOLE}" stroke-width="3.6"') + ring_c(47, 19, 5, 2.6, HOLE)
    return fit(out, 0.600, 32.9, 29.9)


@reg("io.github.igaldino.CoyoteTM", BLUE)
def coyotetm():
    out = poly([(8, 6), (22, 18), (42, 18), (56, 6), (54, 32), (38, 56), (32, 58), (26, 56), (10, 32)], INK, 3.4)
    out += poly([(16, 28), (28, 31), (25, 35)], HOLE, 1.2) + poly([(48, 28), (36, 31), (39, 35)], HOLE, 1.2)
    return fit(out + ink_circle(32, 52, 3.6, HOLE), 0.560, 31.8, 26.4)


@reg("io.github.igorlogius.scr2ppm", YELLOW_DARK)
def scr2ppm():
    out = ink_rrect(5, 9, 54, 42, 6, "none", ' stroke="INK" stroke-width="4"')
    for x in range(3):
        for y in range(3):
            out += dim(ink_rrect(19 + x * 9, 17 + y * 9, 7, 7, 1.4), round(1 - .2 * (x + y), 2))
    return fit(out + ink_rrect(22, 54, 20, 4, 2), 0.547, 31.8, 29.8)


@reg("io.github.iionel.Visu", RED_DARK)
def visu():
    lens = [8, 15, 10, 17, 6, 13, 16, 9, 14, 17, 7, 11, 16, 10]
    out = ""
    for k, L in enumerate(lens):
        a, b = pt(32, 32, 11, 360 / 14 * k - 90), pt(32, 32, 11 + L, 360 / 14 * k - 90)
        out += ink_stroke(f"M{f(a[0])} {f(a[1])}L{f(b[0])} {f(b[1])}", 3.8)
    return fit(out + ink_circle(32, 32, 5), 0.625, 32.3, 32.9)


@reg("io.github.ilius.pyglossary", CYAN)
def pyglossary():
    out = ink_rrect(6, 4, 42, 54, 5) + ink_stroke("M15 4V58", 3, HOLE)
    out += ink_stroke("M22 46L32 20L42 46", 4.6, HOLE) + ink_stroke("M26 37H38", 3.4, HOLE)
    return fit(out + ink_stroke("M52 14V50", 4.4) + dim(ink_stroke("M58 22V42", 4), .6), 0.557, 28.9, 30.8)


@reg("io.github.input_leap.input-leap", ORANGE_DARK)
def input_leap():
    out = ink_rrect(4, 30, 22, 17, 3) + ink_rrect(38, 30, 22, 17, 3) + ink_rrect(10, 50, 10, 4, 2) + ink_rrect(44, 50, 10, 4, 2)
    out += poly([(10, 6), (10, 22), (14, 18), (18, 25), (21, 23.5), (17, 16.5), (22, 15.5)], INK, 1.2)
    return fit(out + stroke("M27 14H44", INK, 3.6, ' stroke-dasharray="3.4 4.6"') + arrowhead(51, 14, 1, 0, 6.5), 0.571, 31.1, 29.4)


@reg("io.github.insilmaril.vym", PURPLE_SOFT)
def vym():
    out = ink_rrect(20, 26, 24, 13, 6.5)
    out += ink_stroke("M44 32Q52 32 52 20", 3.4) + ink_stroke("M44 34Q52 34 52 46", 3.4) + ink_stroke("M20 32Q12 32 12 20", 3.4) + ink_stroke("M20 34Q12 34 12 46", 3.4)
    out += ink_rrect(42, 6, 20, 10, 5) + ink_rrect(42, 48, 20, 10, 5) + ink_rrect(2, 6, 20, 10, 5) + ink_rrect(2, 48, 20, 10, 5)
    return fit(out, 0.491, 32.2, 32.0)


@reg("io.github.intoolswetrust.JSignPdf", INDIGO_SOFT)
def jsignpdf():
    out = path("M12 4H38L52 18V60H12Z", INK) + dim(path("M38 4V18H52Z", INK), .5)
    out += ink_stroke("M18 28H32", 2.8, HOLE) + ink_stroke("M18 34H26", 2.8, HOLE)
    return fit(out + ink_stroke("M18 48Q22 38 26 47T34 47T44 43", 3.2, HOLE), 0.541, 32.0, 32.2)


@reg("io.github.iptux_src.iptux", BROWN_DARK)
def iptux():
    out = ink_rrect(4, 8, 56, 38, 12) + poly([(18, 44), (14, 58), (31, 46)], INK, 2)
    out += ink_stroke("M32 19L22 35L42 35Z", 2.6, HOLE)
    return fit(out + ink_circle(32, 19, 4.4, HOLE) + ink_circle(22, 35, 4.4, HOLE) + ink_circle(42, 35, 4.4, HOLE), 0.577, 31.9, 32.3)


@reg("io.github.itprojects.MasVisGtk", INDIGO_LIGHT)
def masvisgtk():
    out = ink_stroke("M5 54H59", 3.8)
    for x, y in ((12, 42), (20, 32), (28, 26), (36, 12), (44, 34), (52, 44)):
        out += ink_stroke(f"M{x} 50V{y}", 4)
    return fit(out + ink_circle(36, 6, 3), 0.546, 31.9, 36.6)


@reg("io.github.ja2_stracciatella.JA2-Stracciatella", YELLOW_DARK)
def ja2_stracciatella():
    out = dim(rot(ink_rrect(25, 8, 30, 38, 9), 16, 40, 27), .55)
    out += rot(ink_rrect(10, 14, 30, 40, 9, INK, f' stroke="{HOLE}" stroke-width="2.8"') + ink_circle(25, 22, 3, HOLE) + ink_stroke("M17 33H33", 3, HOLE) + ink_stroke("M17 41H33", 3, HOLE) + ink_stroke("M17 48H27", 3, HOLE), -12, 25, 34)
    return fit(out, 0.646, 33.5, 31.8)


@reg("io.github.jacalz.hegelmote", BLUE_GREY_SOFT)
def hegelmote():
    out = ink_rrect(4, 14, 56, 34, 6) + ink_circle(20, 31, 11, HOLE) + ink_stroke("M20 31V23", 3.4) + ink_circle(20, 31, 3.2)
    out += ink_rrect(36, 22, 20, 11, 2.5, HOLE) + ink_stroke("M38 41H54", 3.2, HOLE)
    return fit(out + ink_rrect(10, 52, 9, 5, 2) + ink_rrect(45, 52, 9, 5, 2), 0.586, 31.8, 32.9)


@reg("io.github.jacalz.rymdport", LIGHT_BLUE_DARK)
def rymdport():
    out = ring_c(24, 32, 20, 3.8) + ring_c(30, 32, 14, 3.8) + ring_c(36, 32, 8, 3.8)
    return fit(out + ink_stroke("M42 32H55", 4.2) + arrowhead(56, 32, 1, 0, 6.5), 0.610, 32.4, 31.8)


@reg("io.github.jardon.Outlet", AMBER_DARK)
def outlet():
    out = ink_rrect(6, 6, 52, 52, 12) + ink_circle(32, 32, 16, HOLE)
    return fit(out + ink_rrect(23, 25, 4.6, 13, 2.3) + ink_rrect(36.4, 25, 4.6, 13, 2.3) + ink_circle(32, 44, 2.8), 0.582, 32.1, 32.1)


@reg("io.github.jchempaint.JChemPaint", PINK_LIGHT)
def jchempaint():
    out = hexring(25, 32, 17, 4.2)
    for k in (0, 2, 4):
        a, b = pt(25, 32, 11, -90 + 60 * k + 12), pt(25, 32, 11, -90 + 60 * (k + 1) - 12)
        out += ink_stroke(f"M{f(a[0])} {f(a[1])}L{f(b[0])} {f(b[1])}", 3)
    x, y = pt(25, 32, 17, 30)
    return fit(out + ink_stroke(f"M{f(x)} {f(y)}L50 46", 4) + ring_c(54, 48, 5, 3.6), 0.626, 34.3, 37.0)


@reg("io.github.jmberesford.Retrom", TEAL_DEEP)
def retrom():
    out = ink_rrect(10, 4, 44, 54, 6) + ink_rrect(16, 11, 32, 22, 2.5, HOLE)
    out += ink_stroke("M21 19H43", 2.8) + ink_stroke("M21 26H35", 2.8) + ink_rrect(18, 42, 28, 8, 1.8, HOLE)
    return fit(out + poly([(10, 4), (22, 4), (10, 16)], HOLE, .4), 0.548, 30.7, 30.0)


@reg("io.github.johannesboehler2.BmiCalculator", DEEP_ORANGE_DARK)
def bmicalculator():
    out = ink_rrect(6, 6, 52, 52, 11) + path("M15 38A17 17 0 0 1 49 38Z", HOLE)
    out += ink_stroke("M32 38L39 25", 3.4) + ink_circle(32, 38, 3)
    return fit(out + ink_rrect(13, 44, 15, 8, 3, HOLE) + ink_rrect(36, 44, 15, 8, 3, HOLE), 0.574, 32.1, 32.1)


@reg("io.github.johnfactotum.Runemaster", DEEP_PURPLE_DEEP)
def runemaster():
    out = ink_rrect(10, 4, 44, 56, 18)
    return fit(out + ink_stroke("M25 16V48", 4.6, HOLE) + ink_stroke("M25 27L42 15", 4.6, HOLE) + ink_stroke("M25 39L42 27", 4.6, HOLE), 0.642, 32.1, 31.7)


@reg("io.github.jorchube.monitorets", LIGHT_BLUE_DEEP)
def monitorets():
    out = dim(ink_rrect(4, 8, 56, 11, 5.5), .38) + ink_rrect(4, 8, 38, 11, 5.5)
    out += dim(ink_rrect(4, 26, 56, 11, 5.5), .38) + ink_rrect(4, 26, 22, 11, 5.5)
    return fit(out + dim(ink_rrect(4, 44, 56, 11, 5.5), .38) + ink_rrect(4, 44, 47, 11, 5.5), 0.538, 31.7, 31.4)


@reg("io.github.jordanl2.ModularCalculator", GREY_DEEP)
def modularcalculator():
    return fit(ring_c(17, 17, 8, 5.4) + ring_c(47, 47, 8, 5.4) + ink_stroke("M51 8L13 56", 5.6), 0.554, 32.1, 31.8)


@reg("io.github.josephmawa.Bella", BLUE_LIGHT)
def bella():
    out = "".join(ink_circle(*pt(32, 32, 14.5, -90 + 72 * k), 11) for k in range(5))
    return fit(out + ink_circle(32, 32, 7.5, HOLE) + ink_circle(32, 32, 3), 0.728, 31.9, 32.0)


@reg("io.github.josephmawa.Egghead", YELLOW_DARK)
def egghead():
    out = path("M32 4C46 4 54 26 54 38C54 50 44 60 32 60C20 60 10 50 10 38C10 26 18 4 32 4Z", INK)
    out += ring_c(24, 35, 6.5, 3, HOLE) + ring_c(40, 35, 6.5, 3, HOLE) + ink_stroke("M30.5 35H33.5", 3, HOLE) + ink_stroke("M25 49Q32 54 39 49", 3.2, HOLE)
    return fit(out, 0.661, 32.0, 31.8)


@reg("io.github.josephmawa.EncodingExplorer", RED_DEEP)
def encodingexplorer():
    out = ring_c(32, 32, 24, 4.4)
    out += rot(poly([(32, 11), (39, 32), (25, 32)], INK, 1.6) + dim(poly([(32, 53), (39, 32), (25, 32)], INK, 1.6), .5), 40)
    out += ink_stroke("M32 4V8", 3.2) + ink_stroke("M32 56V60", 3.2) + ink_stroke("M4 32H8", 3.2) + ink_stroke("M56 32H60", 3.2)
    return fit(out + ink_circle(32, 32, 3.2, HOLE), 0.630, 31.9, 32.1)


@reg("io.github.josephmawa.Gauge", CYAN)
def gauge():
    out = ink_stroke("M12 50A26 26 0 1 1 52 50", 6) + ink_stroke("M32 34L45 19", 4.6) + ink_circle(32, 34, 5.6)
    return fit(out + ink_stroke("M32 14V19", 3.2) + ink_stroke("M14 34H19", 3.2) + ink_stroke("M50 34H45", 3.2), 0.638, 31.8, 33.4)


@reg("io.github.josephmawa.SpellingBee", ORANGE_DEEP)
def spellingbee():
    out = dim(rot(ell(21, 20, 11, 6), -24, 21, 20) + rot(ell(43, 20, 11, 6), 24, 43, 20), .6)
    out += ell(32, 38, 16, 20) + ink_stroke("M19 35H45", 4.4, HOLE) + ink_stroke("M21 46H43", 4.4, HOLE)
    out += poly([(29, 56), (35, 56), (32, 62)], INK, 1.2) + ink_stroke("M27 20Q23 12 17 10", 3) + ink_stroke("M37 20Q41 12 47 10", 3)
    return fit(out, 0.637, 32.1, 33.1)


@reg("io.github.josephmawa.TextCompare", PURPLE_DARK)
def textcompare():
    out = ink_rrect(4, 8, 26, 48, 4) + ink_rrect(34, 8, 26, 48, 4)
    for y, a, b in ((18, 24, 54), (26, 20, 54), (34, 24, 48), (42, 18, 54)):
        out += ink_stroke(f"M10 {y}H{a}", 2.8, HOLE) + ink_stroke(f"M40 {y}H{b}", 2.8, HOLE)
    return fit(out, 0.527, 31.9, 32.0)


@reg("io.github.jotd666.gods-deluxe", ORANGE_DEEP)
def gods_deluxe():
    out = path("M10 36Q10 12 32 12Q54 12 54 36V50Q54 56 48 56H42V44H22V56H16Q10 56 10 50Z", INK)
    out += ink_rrect(17, 28, 13, 5, 2.5, HOLE) + ink_rrect(34, 28, 13, 5, 2.5, HOLE) + ink_stroke("M16 14Q32 -2 48 14", 4.6)
    return fit(out, 0.630, 32.0, 33.2)


@reg("io.github.juancarlosbernal.FolderPlay", BROWN_DEEP)
def folderplay():
    out = path("M4 14Q4 10 8 10H24L30 17H56Q60 17 60 21V50Q60 54 56 54H8Q4 54 4 50Z", INK)
    return fit(out + poly([(26, 25), (26, 46), (44, 35.5)], HOLE, 2.6), 0.544, 31.8, 32.0)


@reg("io.github.juergenfleiss.aTrain", INDIGO_SOFT)
def atrain():
    out = ink_rrect(4, 26, 5, 12, 2.5) + ink_rrect(13, 16, 5, 32, 2.5) + ink_rrect(22, 22, 5, 20, 2.5)
    return fit(out + ink_rrect(34, 14, 26, 6, 3) + ink_rrect(34, 26, 18, 6, 3) + ink_rrect(34, 38, 26, 6, 3) + ink_rrect(34, 50, 14, 6, 3), 0.622, 32.8, 29.1)


@reg("io.github.julian_hochhaus.LG4X_V2", YELLOW_DARK)
def lg4x_v2():
    out = dim(path("M6 52C16 52 20 12 32 12C44 12 48 52 58 52Z", INK), .4)
    out += ink_stroke("M4 52C18 52 22 20 32 20C42 20 46 52 60 52", 4.4) + ink_stroke("M4 58H60", 3.2)
    for x, y in ((14, 44), (24, 26), (40, 24), (50, 44)):
        out += ink_circle(x, y, 2.8)
    return fit(out, 0.570, 32.0, 44.6)


@reg("io.github.justinrdonnelly.bouncer", BLUE_GREY_DARK)
def bouncer():
    out = ink_circle(32, 22, 13) + path("M8 60Q8 38 32 38Q56 38 56 60Z", INK)
    out += ink_rrect(18, 18, 12, 7.5, 3.2, HOLE) + ink_rrect(34, 18, 12, 7.5, 3.2, HOLE) + ink_stroke("M30 20.5H34", 2.6, HOLE)
    return fit(out + poly([(32, 47), (25, 42), (25, 52)], HOLE, 1.2) + poly([(32, 47), (39, 42), (39, 52)], HOLE, 1.2), 0.598, 32.0, 40.1)


@reg("io.github.kaii_lb.hgui", LIGHT_BLUE_DEEP)
def hgui():
    out = ink_rrect(4, 8, 56, 48, 8, "none", ' stroke="INK" stroke-width="4"')
    out += ink_stroke("M4 21H60", 3.4) + ink_circle(12, 14.5, 2) + ink_circle(19, 14.5, 2)
    out += ink_stroke("M14 33H50", 3.2) + ink_circle(24, 33, 4.6, INK, f' stroke="{HOLE}" stroke-width="2"')
    return fit(out + ink_stroke("M14 45H50", 3.2) + ink_circle(41, 45, 4.6, INK, f' stroke="{HOLE}" stroke-width="2"'), 0.519, 32.2, 32.0)


@reg("io.github.kalaksi.Lightkeeper", AMBER_DEEP)
def lightkeeper():
    out = path("M26 22H38L42 56H22Z", INK) + ink_rrect(25, 12, 14, 10, 2) + poly([(23, 12), (32, 3), (41, 12)], INK, 2)
    out += ink_stroke("M24.5 33H39.5", 3, HOLE, ) + ink_stroke("M23.5 44H40.5", 3, HOLE) + ink_rrect(16, 56, 32, 4, 2)
    return fit(out + dim(poly([(43, 15), (62, 6), (62, 22)], INK, 1.4) + poly([(21, 15), (2, 6), (2, 22)], INK, 1.4), .55), 0.505, 31.8, 26.1)


@reg("io.github.kaschpal.timetable", PINK_SOFT)
def timetable():
    out = ink_rrect(4, 8, 56, 48, 6)
    out += line(4, 22, 60, 22, HOLE, 2.8, "butt") + line(4, 36, 60, 36, HOLE, 2.8, "butt") + line(4, 46, 60, 46, HOLE, 2.8, "butt")
    out += line(21, 22, 21, 56, HOLE, 2.8, "butt") + line(40, 22, 40, 56, HOLE, 2.8, "butt")
    return fit(out + dim(ink_rrect(24, 38.5, 14, 6, 1.5, HOLE), 1) + ink_rrect(7, 12, 10, 5, 2, HOLE), 0.537, 31.8, 31.7)


@reg("io.github.kelvinnovais.Kasasa", TEAL)
def kasasa():
    out = poly([(32, 6), (58, 28), (52, 28), (52, 56), (12, 56), (12, 28), (6, 28)], INK, 3.4) + ink_rrect(42, 11, 6, 12, 1.2)
    return fit(out + path("M25 56V43Q25 38 30 38H34Q39 38 39 43V56Z", HOLE) + ink_circle(32, 27, 4.6, HOLE), 0.605, 32.0, 34.8)


@reg("io.github.khaled_0.TubeSync", DEEP_ORANGE_DEEP)
def tubesync():
    return fit(arc_arrow(32, 32, 24, 200, 340) + arc_arrow(32, 32, 24, 20, 160) + poly([(26, 22), (26, 42), (44, 32)], INK, 3.4), 0.614, 32.2, 31.9)


@reg("io.github.klassenserver7b.danceinterpreter-rs", DEEP_PURPLE)
def danceinterpreter_rs():
    out = ink_circle(30, 11, 6.5) + ink_stroke("M30 21L33 38", 5.4) + ink_stroke("M31 25L12 12", 4.8) + ink_stroke("M31 25L52 15", 4.8)
    return fit(out + ink_stroke("M33 38L20 58", 5) + ink_stroke("M33 38L48 48L52 58", 5), 0.562, 31.8, 35.3)


@reg("io.github.koromelodev.mindmate", CYAN_DARK)
def mindmate():
    out = ""
    for m in (1, -1):
        def X(x):
            return x if m == 1 else 64 - x
        out += ink_circle(X(21), 21, 12) + ink_circle(X(17), 35, 11) + ink_circle(X(27), 34, 10)
        out += ink_stroke(f"M{X(11)} 23Q{X(17)} 16 {X(24)} 23", 2.6, HOLE) + ink_stroke(f"M{X(9)} 37Q{X(15)} 30 {X(22)} 37", 2.6, HOLE)
    return fit(out + ink_stroke("M32 12V46", 3, HOLE) + ink_rrect(28, 44, 8, 13, 3), 0.695, 31.9, 30.6)


@reg("io.github.kovzol.bibref", GREY_DEEP)
def bibref():
    out = ink_rrect(10, 4, 44, 54, 5) + ink_circle(23, 25, 5.6, HOLE) + ink_circle(41, 25, 5.6, HOLE)
    out += ink_stroke("M18 27Q16 38 25 41", 3.2, HOLE) + ink_stroke("M36 27Q34 38 43 41", 3.2, HOLE)
    return fit(out + ink_stroke("M19 51H45", 3, HOLE), 0.566, 32.0, 31.0)


@reg("io.github.kovzol.geogebra-discovery", BLUE_DARK)
def geogebra_discovery():
    out = ink_circle(32, 10, 6) + ink_stroke("M32 14L14 56", 4.8) + ink_stroke("M32 14L50 56", 4.8) + ink_stroke("M22.5 38H41.5", 3.6)
    return fit(out + dim(ink_stroke("M2 50Q32 30 62 50", 3.2), .6), 0.547, 32.1, 38.0)


@reg("io.github.kriptolix.Poliedros", YELLOW_DARK)
def poliedros():
    h = [pt(32, 32, 26, -90 + 60 * k) for k in range(6)]
    t = [pt(32, 32, 11, a) for a in (-90, 30, 150)]
    out = hx(32, 32, 26, -90, INK, 3.4)
    out += ink_stroke("M" + "L".join(f"{f(a)} {f(b)}" for a, b in t) + "Z", 2.6, HOLE)
    for i, (a, b) in enumerate(t):
        for j in (2 * i - 1, 2 * i + 1):
            x, y = h[j % 6]
            out += ink_stroke(f"M{f(a)} {f(b)}L{f(x)} {f(y)}", 2.6, HOLE)
    return fit(out, 0.667, 32.2, 31.9)


@reg("io.github.ksharindam.chemcanvas", RED)
def chemcanvas():
    out = ink_stroke("M4 46L17 34L30 46L43 34L56 46", 4.2) + ink_stroke("M30 46V26", 4.2) + ring_c(30, 19, 6, 3.8)
    return fit(out + ink_stroke("M36 49L49 37", 3), 0.643, 29.8, 39.9)


@reg("io.github.ktgw0316.LightZone", CYAN)
def lightzone():
    out = '<defs><clipPath id="lz"><circle cx="32" cy="32" r="25"/></clipPath></defs><g clip-path="url(#lz)">'
    for k, o in enumerate((1, .8, .6, .4, .22)):
        out += dim(ink_rrect(4, 6 + k * 11.4, 56, 9, 0), o)
    return fit(out + "</g>", 0.741, 31.9, 31.8)


@reg("io.github.kukuruzka165.materialgram", ORANGE_DARK)
def materialgram():
    out = poly([(6, 31), (58, 8), (43, 55), (31, 41), (24, 52), (22, 38)], INK, 2.6)
    return fit(out + ink_stroke("M22 38L47 20", 3, HOLE), 0.604, 35.0, 26.7)


@reg("io.github.kyuyrii.zordeer", PURPLE_DEEP)
def zordeer():
    out = poly([(20, 28), (44, 28), (40, 50), (32, 58), (24, 50)], INK, 4)
    out += rot(ell(13, 34, 7, 3.6), -22, 13, 34) + rot(ell(51, 34, 7, 3.6), 22, 51, 34)
    out += ink_stroke("M25 27Q17 15 16 4", 3.6) + ink_stroke("M20 15L10 12", 3.2) + ink_stroke("M39 27Q47 15 48 4", 3.6) + ink_stroke("M44 15L54 12", 3.2)
    return fit(out + ink_circle(27, 38, 2.6, HOLE) + ink_circle(37, 38, 2.6, HOLE) + ink_circle(32, 53, 3.4, HOLE), 0.595, 31.9, 28.7)


@reg("io.github.labbots.NiimPrintX", GREY_DARK)
def niimprintx():
    out = ink_rrect(4, 10, 56, 30, 5)
    for x, w in ((11, 2.6), (16, 4.4), (23, 2.6), (28, 5), (36, 2.6), (41, 4.4), (48, 2.6)):
        out += ink_rrect(x, 16, w, 18, .8, HOLE)
    return fit(out + ink_rrect(10, 46, 44, 8, 4) + ink_stroke("M20 58H44", 3.4), 0.573, 32.0, 29.9)


@reg("io.github.ladaapp.lada", BROWN)
def lada():
    out = ink_rrect(6, 6, 52, 52, 6) + ink_rrect(18, 10, 28, 44, 2, HOLE)
    for y in (12, 23, 34, 45):
        out += ink_rrect(9, y, 5, 6, 1.2, HOLE) + ink_rrect(50, y, 5, 6, 1.2, HOLE)
    for x, y, o in ((21, 14, 1), (33, 14, .4), (21, 26, .4), (33, 26, 1), (21, 38, 1), (33, 38, .6)):
        out += dim(ink_rrect(x, y, 10, 10, 1.6), o)
    return fit(out, 0.539, 32.1, 32.1)


@reg("io.github.laserlicht.TowerOops", INDIGO_DARK)
def toweroops():
    out = ink_rrect(6, 48, 26, 9, 2) + ink_rrect(35, 48, 23, 9, 2) + ink_rrect(12, 37, 22, 9, 2) + ink_rrect(37, 37, 17, 9, 2)
    out += ink_rrect(18, 26, 24, 9, 2) + rot(ink_rrect(24, 7, 28, 9, 2), 24, 38, 12)
    return fit(out, 0.562, 31.9, 35.1)


@reg("io.github.lavenderdotpet.LibreQuake", YELLOW_DARK)
def librequake():
    out = poly([(6, 40), (10, 16), (26, 6), (44, 10), (58, 26), (56, 50), (36, 58), (14, 56)], INK, 3.6)
    return fit(out + ink_stroke("M30 8L26 22L37 30L28 43L34 58", 3.4, HOLE), 0.610, 32.2, 33.9)


@reg("io.github.lawstorant.boxflat", BLUE_GREY_DEEP)
def boxflat():
    out = ring_c(32, 32, 24, 5) + ink_stroke("M8 32H24", 5) + ink_stroke("M40 32H56", 5) + ink_stroke("M32 42V56", 5) + ink_circle(32, 32, 9)
    return fit(out + ink_rrect(30, 8, 4, 5.4, 1, HOLE) + ink_circle(32, 32, 3, HOLE), 0.698, 31.9, 31.9)


@reg("io.github.leo030303.drizzle", LIGHT_BLUE)
def drizzle():
    out = ink_circle(20, 29, 10) + ink_circle(33, 23, 14) + ink_circle(46, 30, 9) + ink_rrect(10, 29, 45, 12, 6)
    return fit(out + ink_stroke("M20 49L16 58", 4) + ink_stroke("M32 49L28 58", 4) + ink_stroke("M44 49L40 58", 4), 0.675, 28.4, 35.7)


@reg("io.github.leolost2605.emergency-alerts", AMBER_DARK)
def emergency_alerts():
    return fit(poly([(32, 7), (58, 54), (6, 54)], INK, 7) + ink_stroke("M32 24V38", 5, HOLE) + ink_circle(32, 46, 3.2, HOLE), 0.541, 32.0, 37.9)


@reg("io.github.leolost2605.gradebook", PINK_DARK)
def gradebook():
    out = poly([(32, 10), (60, 24), (32, 38), (4, 24)], INK, 2.6)
    out += path("M16 33V45Q32 55 48 45V33L32 41Z", INK) + ink_stroke("M55 27V43", 3.2) + ink_circle(55, 46, 3.4)
    return fit(out, 0.611, 31.9, 31.8)


@reg("io.github.lethal_guitar.RigelEngine", TEAL_LIGHT)
def rigelengine():
    out = ink_rrect(6, 20, 38, 17, 6) + ink_rrect(40, 24, 17, 9, 3) + poly([(14, 37), (27, 37), (22, 57), (12, 57)], INK, 2.4)
    out += ink_circle(21, 28.5, 3.6, HOLE) + ink_stroke("M30 28.5H37", 3, HOLE)
    return fit(out + star4(55, 11, 7), 0.533, 34.3, 31.6)


@reg("io.github.letslearn_app.letslearn", DEEP_ORANGE)
def letslearn():
    out = path("M4 40Q18 38 31 44V58Q18 52 4 54Z", INK) + path("M60 40Q46 38 33 44V58Q46 52 60 54Z", INK)
    out += ink_stroke("M32 42V24", 3.6) + path("M32 32Q17 32 15 17Q30 17 32 32Z", INK) + path("M32 25Q44 25 49 10Q34 10 32 25Z", INK)
    return fit(out, 0.574, 31.8, 37.7)


@reg("io.github.limo_app.limo", DEEP_PURPLE_LIGHT)
def limo():
    out = ink_rrect(12, 16, 40, 38, 4) + ink_circle(32, 12, 6.4) + ink_circle(56, 35, 6.4)
    return fit(out + ink_circle(12, 35, 6.4, HOLE) + ink_circle(32, 54, 6.4, HOLE), 0.653, 33.9, 33.9)


@reg("io.github.lincity_ng.lincity-ng", INDIGO_SOFT)
def lincity_ng():
    out = ink_rrect(4, 28, 13, 30, 2) + ink_rrect(20, 10, 15, 48, 2) + ink_rrect(38, 22, 11, 36, 2) + ink_rrect(52, 34, 8, 24, 2)
    for y in (16, 26, 36, 46):
        out += ink_rrect(24, y, 7, 5, 1, HOLE)
    return fit(out + ink_rrect(8, 34, 5, 5, 1, HOLE) + ink_rrect(8, 44, 5, 5, 1, HOLE) + ink_rrect(42, 28, 4, 5, 1, HOLE) + ink_rrect(42, 38, 4, 5, 1, HOLE), 0.576, 32.0, 40.4)


@reg("io.github.listen1.Listen1", GREY_DEEP)
def listen1():
    out = ink_rrect(12, 4, 40, 56, 9) + ink_circle(32, 19, 6, HOLE) + ink_circle(32, 42, 12, HOLE) + ink_circle(32, 42, 4.4)
    return fit(out, 0.596, 32.0, 31.7)


@reg("io.github.lloura.DuelPy", BLUE_DEEP)
def duelpy():
    def sword(a):
        s = poly([(32, 2), (36.5, 8), (36.5, 40), (27.5, 40), (27.5, 8)], INK, 1.6) + ink_rrect(19, 40, 26, 5, 2.5)
        s += ink_rrect(29.5, 45, 5, 10, 2) + ink_circle(32, 58, 3.4)
        return rot(s, a, 32, 32)
    return fit(sword(-38) + sword(38), 0.617, 32.1, 31.1)


@reg("io.github.lluciocc.Vish", YELLOW_DARK)
def vish():
    out = ell(28, 33, 22, 14) + poly([(44, 33), (60, 19), (60, 47)], INK, 2.6) + path("M24 21Q32 8 40 18Z", INK)
    return fit(out + ink_circle(14, 29, 2.8, HOLE) + ink_stroke("M26 24Q31 33 26 42", 3, HOLE), 0.630, 35.7, 33.0)


@reg("io.github.lo2dev.Echo", RED_LIGHT)
def echo():
    out = ink_circle(12, 32, 6)
    for r, o in ((16, 1), (28, .75), (40, .5)):
        a, b = pt(12, 32, r, -46), pt(12, 32, r, 46)
        out += dim(ink_stroke(f"M{f(a[0])} {f(a[1])}A{r} {r} 0 0 1 {f(b[0])} {f(b[1])}", 4.6), o)
    return fit(out, 0.598, 37.0, 32.0)


@reg("io.github.loot.loot", CYAN)
def loot():
    out = ink_rrect(6, 28, 52, 28, 4) + path("M6 30V22Q6 9 20 9H44Q58 9 58 22V30Z", INK)
    out += line(6, 30, 58, 30, HOLE, 3.2, "butt")
    return fit(out + ink_rrect(26, 26, 12, 15, 3, INK, f' stroke="{HOLE}" stroke-width="2.8"') + ink_circle(32, 32.5, 2.2, HOLE), 0.582, 31.9, 34.7)


@reg("io.github.lruzicka.Needly", ORANGE_DEEP)
def needly():
    out = ink_stroke("M8 58L46 15", 4.2) + ring_c(49, 11, 4, 2.8) + dim(ink_stroke("M52 14Q63 29 47 39Q33 48 41 58", 3.4), .75)
    return fit(out, 0.530, 29.6, 33.5)


@reg("io.github.ltiber.Pwall", PURPLE)
def pwall():
    out = ink_rrect(4, 8, 24, 12, 2) + ink_rrect(31, 8, 29, 12, 2)
    out += ink_rrect(4, 24, 12, 12, 2) + ink_rrect(19, 24, 24, 12, 2) + ink_rrect(46, 24, 14, 12, 2)
    return fit(out + ink_rrect(4, 40, 29, 12, 2) + ink_rrect(36, 40, 24, 12, 2), 0.534, 32.0, 30.0)


@reg("io.github.lullabyX.sone", PURPLE_LIGHT)
def sone():
    return fit(ring_c(32, 32, 24, 4.8) + ink_stroke("M13 32Q19 17 26 32T38 32T51 32", 4.6), 0.701, 32.0, 32.0)


@reg("io.github.lxndr.gswatcher", BROWN_LIGHT)
def gswatcher():
    out = ink_rrect(4, 6, 42, 17, 4) + ink_rrect(4, 27, 42, 17, 4)
    out += ink_circle(12, 14.5, 2.8, HOLE) + ink_circle(12, 35.5, 2.8, HOLE) + ink_stroke("M20 14.5H38", 3, HOLE) + ink_stroke("M20 35.5H38", 3, HOLE)
    return fit(out + ink_circle(44, 44, 14, HOLE) + ring_c(43, 43, 9, 4.4) + ink_stroke("M50 50L59 59", 5.6), 0.477, 33.1, 34.4)


@reg("io.github.maddecoder.Classic-RBDOOM-3-BFG", INDIGO_DEEP)
def classic_rbdoom_3_bfg():
    out = ink_circle(32, 26, 22) + ink_rrect(19, 38, 26, 20, 6)
    out += ink_circle(22, 28, 6.4, HOLE) + ink_circle(42, 28, 6.4, HOLE) + poly([(32, 34), (27.5, 43), (36.5, 43)], HOLE, 1)
    return fit(out + ink_stroke("M27 49V56", 2.8, HOLE) + ink_stroke("M32 49V56", 2.8, HOLE) + ink_stroke("M37 49V56", 2.8, HOLE), 0.672, 32.0, 31.4)


@reg("io.github.magnush.mhWaveEdit", YELLOW_DARK)
def mhwaveedit():
    out = dim(ink_rrect(24, 6, 20, 52, 4), .35)
    for k, h in enumerate((10, 22, 14, 34, 44, 28, 40, 18, 24, 12, 8)):
        out += ink_rrect(5 + k * 5, 32 - h / 2, 3.4, h, 1.7)
    return fit(out + ink_stroke("M24 6V58", 2.6) + ink_stroke("M44 6V58", 2.6), 0.637, 34.0, 31.9)


@reg("io.github.mak448a.QTCord", BLUE_GREY)
def qtcord():
    out = ink_rrect(6, 8, 52, 38, 12) + poly([(20, 44), (16, 58), (32, 46)], INK, 2)
    return fit(out + ink_stroke("M27 17L23 38", 3.2, HOLE) + ink_stroke("M39 17L35 38", 3.2, HOLE) + ink_stroke("M17 25H46", 3.2, HOLE) + ink_stroke("M15 32H43", 3.2, HOLE), 0.602, 31.6, 32.8)


@reg("io.github.marco_calautti.DeltaPatcher", LIGHT_BLUE_LIGHT)
def deltapatcher():
    out = ink_stroke("M32 7L58 54H6Z", 5.2) + rot(ink_rrect(17, 33, 30, 11, 5.5, INK, f' stroke="{HOLE}" stroke-width="2.8"'), -32, 32, 38.5)
    return fit(out + rot(ink_circle(27, 38.5, 1.8, HOLE) + ink_circle(37, 38.5, 1.8, HOLE), -32, 32, 38.5), 0.557, 31.8, 37.6)


@reg("io.github.masakk1.press", AMBER_DEEP)
def press():
    out = ink_rrect(6, 6, 52, 40, 9) + ink_rrect(12, 10, 40, 27, 5, HOLE)
    return fit(out + ink_stroke("M23 17L32 27L41 17", 4.6) + ink_rrect(10, 51, 44, 6, 3), 0.570, 31.6, 31.4)


@reg("io.github.masterbillwoo.RiseOfThePenguinsGB", PINK_DEEP)
def riseofthepenguinsgb():
    out = ell(32, 34, 18, 24) + ell(32, 40, 11, 17, HOLE)
    out += path("M15 26Q3 36 9 49Q16 45 17 37Z", INK) + path("M49 26Q61 36 55 49Q48 45 47 37Z", INK)
    out += poly([(28, 25), (36, 25), (32, 31)], HOLE, 1) + ink_circle(26, 20, 2.6, HOLE) + ink_circle(38, 20, 2.6, HOLE)
    return fit(out + ell(24, 58, 6.5, 2.8) + ell(40, 58, 6.5, 2.8), 0.696, 31.9, 36.4)


@reg("io.github.mbugni.AliensEradicationTC", TEAL_SOFT)
def alienseradicationtc():
    out = path("M19 26Q19 9 32 9Q45 9 45 26Z", INK) + ell(32, 30, 27, 8)
    out += ink_circle(15, 31, 2.4, HOLE) + ink_circle(32, 34, 2.4, HOLE) + ink_circle(49, 31, 2.4, HOLE)
    return fit(out + dim(poly([(23, 41), (41, 41), (53, 61), (11, 61)], INK, 1.4), .5), 0.606, 31.9, 39.7)


@reg("io.github.mcthesw.easy-nats", DEEP_ORANGE_LIGHT)
def easy_nats():
    out = ink_rrect(22, 22, 20, 20, 6)
    for x, y in ((12, 12), (52, 12), (12, 52), (52, 52)):
        out += ink_stroke(f"M{x} {y}L{32} {32}", 3.2) + ring_c(x, y, 6, 3.6)
    return fit(out + ink_circle(32, 32, 3.4, HOLE), 0.515, 31.8, 31.8)


@reg("io.github.meehow.Receiver", DEEP_PURPLE_SOFT)
def receiver():
    out = ink_rrect(4, 24, 56, 34, 7) + ink_stroke("M18 24L46 8", 3.4) + ink_circle(46, 8, 2.6)
    out += ink_circle(42, 41, 11, HOLE) + ink_stroke("M42 41L48 34", 3.2) + ink_circle(42, 41, 2.6)
    return fit(out + ink_stroke("M11 34H26", 3.2, HOLE) + ink_stroke("M11 41H26", 3.2, HOLE) + ink_stroke("M11 48H26", 3.2, HOLE), 0.558, 32.0, 35.3)


@reg("io.github.megakode.Wallrus", LIGHT_BLUE_DARK)
def wallrus():
    out = ell(32, 30, 24, 21) + ell(32, 41, 14, 11, HOLE) + ink_circle(27, 38, 1.8) + ink_circle(37, 38, 1.8) + ink_circle(32, 43, 1.8)
    out += ell(32, 34, 5.4, 3.6) + ink_rrect(23, 46, 5.4, 15, 2.7) + ink_rrect(35.6, 46, 5.4, 15, 2.7)
    return fit(out + ink_circle(20, 23, 2.8, HOLE) + ink_circle(44, 23, 2.8, HOLE), 0.701, 32.0, 35.3)


@reg("io.github.meypod.al-quran", GREY_DEEP)
def al_quran():
    out = ink_rrect(13, 13, 38, 38, 3.4) + rot(ink_rrect(13, 13, 38, 38, 3.4), 45, 32, 32)
    return fit(out + ink_circle(32, 32, 11, HOLE) + ink_circle(32, 32, 4.4), 0.729, 32.0, 31.7)


@reg("io.github.mezoahmedii.Picker", BLUE)
def picker():
    tube = ink_rrect(26, 4, 12, 9, 4.5) + ink_rrect(21, 12, 22, 6, 3) + ink_rrect(26, 18, 12, 28, 2.5) + poly([(26, 46), (38, 46), (32, 60)], INK, 2)
    tube += ink_rrect(29.4, 30, 5.2, 12, 1.2, HOLE)
    return fit(rot(tube, 40, 32, 32), 0.648, 31.6, 32.0)


@reg("io.github.mfat.jottr", YELLOW_DARK)
def jottr():
    out = ink_rrect(10, 8, 38, 50, 5) + ink_stroke("M22 20H38", 3, HOLE) + ink_stroke("M22 30H38", 3, HOLE) + ink_stroke("M22 40H32", 3, HOLE)
    for y in (16, 27, 38, 49):
        out += ink_rrect(4, y, 12, 4.4, 2.2)
    return fit(out + rot(ink_rrect(46, 14, 8, 30, 3, INK, f' stroke="{HOLE}" stroke-width="2.6"') + poly([(46, 44), (54, 44), (50, 56)], INK, 1.6), 22, 50, 36), 0.547, 32.9, 34.7)
