# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 100: Corluma to wiremapper."""
from lm import (
    AMBER, AMBER_DARK, BLUE, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DEEP, BLUE_GREY_LIGHT,
    BLUE_GREY_SOFT, BROWN, BROWN_LIGHT, BROWN_SOFT, circle, CYAN, CYAN_DEEP, CYAN_LIGHT,
    DEEP_ORANGE, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT, DEEP_PURPLE, DEEP_PURPLE_LIGHT,
    DEEP_PURPLE_SOFT, f, GREY_DEEP, HOLE, INDIGO, INDIGO_DEEP, INDIGO_LIGHT, INK, LIGHT_BLUE,
    LIGHT_BLUE_SOFT, ORANGE, ORANGE_DARK, ORANGE_DEEP, path, PINK, PINK_DEEP, PINK_LIGHT, poly,
    pt, PURPLE, PURPLE_DEEP, RED, RED_DEEP, RED_LIGHT, TEAL, TEAL_DEEP, TEAL_SOFT, YELLOW,
    YELLOW_DARK,
)
from glyphs.kit import (
    arc_arrow, arrowhead, asterisk, cells, crescent, dim, ell, ellring, fit, hexring, hs, hx, ink_circle, ink_stroke, pie, registry, ring_c, ink_rrect, rot, SB, spiral, star4, star5, wedge)

ICONS, SMALL, reg, _ = registry()


@reg("net.corluma.Corluma", RED)
def corluma():
    out = ink_circle(32, 22, 18) + poly([(21, 34), (43, 34), (39, 46), (25, 46)], INK, 1.5) + ink_rrect(24, 48, 16, 6, 3) + ink_rrect(27, 56, 10, 5, 2.5)
    out += ink_stroke("M25 26L30 31L34 21L39 28", 2.8, HOLE)
    return fit(out, 0.649, 32.0, 32.5)


@reg("net.darkradiant.DarkRadiant", CYAN)
def darkradiant():
    out = hx(32, 32, 28, -90, INK, 3)
    for a in (90, -30, 210):
        x, y = pt(32, 32, 27, a)
        out += ink_stroke(f"M32 32L{f(x)} {f(y)}", 3, HOLE)
    return fit(out, 0.627, 32.0, 32.0)


@reg("net.dengine.Doomsday", RED_DEEP)
def doomsday():
    out = ink_circle(32, 38, 20) + poly([(14, 32), (8, 8), (28, 22)], INK, 2) + poly([(50, 32), (56, 8), (36, 22)], INK, 2)
    out += poly([(20, 33), (30, 38), (20, 43)], HOLE, 1) + poly([(44, 33), (34, 38), (44, 43)], HOLE, 1)
    out += ink_stroke("M24 50L28 54L32 50L36 54L40 50", 2.8, HOLE)
    return fit(out, 0.523, 32.0, 32.5)


@reg("net.displaycal.DisplayCAL", BLUE_DEEP)
def displaycal():
    out = ink_rrect(4, 6, 56, 38, 6) + ink_rrect(10, 12, 44, 26, 3, HOLE) + ink_rrect(28, 44, 8, 8, 1) + ink_rrect(18, 52, 28, 6, 3)
    out += pie(32, 25, 10, -90, 150)
    return fit(out, 0.518, 32.0, 32.0)


@reg("net.donnybeelo.Convey", RED_LIGHT)
def convey():
    out = ink_stroke("M8 20H44", 5) + arrowhead(44, 20, 1, 0, 11) + ink_stroke("M20 44H56", 5) + arrowhead(20, 44, -1, 0, 11)
    return fit(out, 0.63, 32.0, 32.0)


@reg("net.emulicious.Emulicious", AMBER_DARK)
def emulicious():
    out = ink_rrect(12, 2, 40, 60, 7) + ink_rrect(17, 8, 30, 24, 3, HOLE)
    out += ink_rrect(18, 43, 14, 4.4, 2.2, HOLE) + ink_rrect(22.8, 38.2, 4.4, 14, 2.2, HOLE) + ink_circle(42, 46, 3.6, HOLE) + ink_circle(48, 40, 3.6, HOLE)
    return fit(out, 0.553, 32.0, 32.0)


@reg("net.eudic.dict", BLUE_GREY_LIGHT)
def dict_icon():
    out = path("M32 14Q20 6 4 10V52Q20 48 32 56Z", INK) + path("M32 14Q44 6 60 10V52Q44 48 32 56Z", INK)
    out += ink_stroke("M32 16V54", 2.6, HOLE) + ink_stroke("M11 22Q18 20 25 24", 2.4, HOLE) + ink_stroke("M11 32Q18 30 25 34", 2.4, HOLE) + ink_stroke("M39 24Q46 20 53 22", 2.4, HOLE) + ink_stroke("M39 34Q46 30 53 32", 2.4, HOLE)
    return fit(out, 0.519, 32.0, 32.3)


@reg("net.ffkkinos.Wildcard", PURPLE)
def wildcard():
    return fit(asterisk(32, 32, 28, 7.4), 0.583, 32.0, 32.0)


@reg("net.freerct.FreeRCT", TEAL_DEEP)
def freerct():
    out = ink_stroke("M4 54C10 54 14 12 28 12C42 12 38 44 46 44C54 44 56 24 60 18", 4.6)
    out += ink_stroke("M12 38V58", 3) + ink_stroke("M28 16V58", 3) + ink_stroke("M46 48V58", 3) + ink_stroke("M4 59H60", 3)
    return fit(out, 0.483, 32.0, 35.1)


@reg("net.goatattack.goatattack", BLUE_GREY)
def goatattack():
    out = ink_stroke("M24 22Q8 22 10 4", 5) + ink_stroke("M40 22Q56 22 54 4", 5)
    out += poly([(24, 22), (40, 22), (44, 42), (32, 56), (20, 42)], INK, 5) + poly([(28, 52), (36, 52), (32, 64)], INK, 2)
    out += ink_circle(26, 34, 2.8, HOLE) + ink_circle(38, 34, 2.8, HOLE) + ink_circle(30, 46, 1.6, HOLE) + ink_circle(34, 46, 1.6, HOLE)
    return fit(out, 0.473, 32.0, 33.2)


@reg("net.gpro.gproapp", INDIGO_LIGHT)
def gproapp():
    out = ink_rrect(6, 4, 5, 58, 2.5)
    for r in range(3):
        for c in range(4):
            if (r + c) % 2 == 0:
                out += ink_rrect(13 + c * 12.5, 6 + r * 12, 11.5, 11, 1.5)
    return fit(out, 0.471, 34.0, 33.0)


@reg("net.gradator.gtkatlantic", YELLOW)
def gtkatlantic():
    out = ink_rrect(4, 46, 56, 9, 4.5) + ink_rrect(16, 8, 32, 42, 5) + ink_rrect(16, 34, 32, 7, 0, HOLE)
    return fit(out, 0.534, 32.0, 31.5)


@reg("net.granjow.slowmovideo", INDIGO)
def slowmovideo():
    out = spiral(26, 33, 2, 15, 2.3, 0, 5) + ink_stroke("M4 56H52Q60 56 58 46", 6) + ink_stroke("M52 47L49 37", 3.4) + ink_stroke("M58 46L61 37", 3.4)
    return fit(out, 0.517, 31.9, 38.8)


@reg("net.gwyddion.Gwyddion", YELLOW_DARK)
def gwyddion():
    out = ""
    for y in (14, 32, 50):
        out += ink_stroke(f"M3 {y}Q12 {y - 14} 22 {y}T42 {y}T61 {y}", 4.4)
    return fit(out, 0.509, 32.0, 32.0)


@reg("net.hhoney.candy", PINK_DEEP)
def candy():
    out = poly([(20, 28), (5, 17), (5, 47), (20, 36)], INK, 2.4) + poly([(44, 28), (59, 17), (59, 47), (44, 36)], INK, 2.4)
    out += ink_circle(32, 32, 14) + ink_stroke("M27 22Q34 32 27 42", 2.6, HOLE)
    return fit(out, 0.576, 32.0, 32.0)


@reg("net.hhoney.rota", DEEP_PURPLE_LIGHT)
def rota():
    return fit(arc_arrow(32, 32, 22, -170, -20, 5, 9) + arc_arrow(32, 32, 22, 10, 160, 5, 9), 0.604, 32.0, 32.0)


@reg("net.hhoney.tinycrate", DEEP_ORANGE)
def tinycrate():
    out = ink_rrect(5, 8, 54, 48, 5) + ink_stroke("M5 24H59", 2.8, HOLE) + ink_stroke("M5 40H59", 2.8, HOLE) + ink_stroke("M13 52L51 12", 3.4, HOLE)
    return fit(out, 0.543, 32.0, 32.0)


@reg("net.huitsi.ParallelOverhead", LIGHT_BLUE)
def paralleloverhead():
    out = ink_stroke("M8 54L34 8", 5.4) + ink_stroke("M24 58L48 16", 5.4) + ink_stroke("M40 58L58 28", 5.4)
    return fit(out, 0.523, 33.0, 33.0)


@reg("net.huitsi.PhantomOverload", DEEP_ORANGE_DEEP)
def phantomoverload():
    out = path("M8 58V30Q8 6 32 6Q56 6 56 30V58L47 50L39.5 58L32 50L24.5 58L17 50Z", INK)
    out += ink_circle(23, 28, 4.6, HOLE) + ink_circle(41, 28, 4.6, HOLE) + ell(32, 41, 5, 4, HOLE)
    return fit(out, 0.525, 32.0, 32.0)


@reg("net.imaginaryinfinity.Squiid", INDIGO_DEEP)
def squiid():
    out = path("M32 2Q52 14 47 34H17Q12 14 32 2Z", INK) + ink_stroke("M22 36Q20 48 12 58", 4.4) + ink_stroke("M28 38V62", 4.4) + ink_stroke("M36 38V62", 4.4) + ink_stroke("M42 36Q44 48 52 58", 4.4)
    out += ink_circle(26, 27, 3.2, HOLE) + ink_circle(38, 27, 3.2, HOLE)
    return fit(out, 0.543, 32.0, 33.1)


@reg("net.jockx.Kulki", AMBER)
def kulki():
    out = ink_circle(26, 28, 21) + ink_stroke("M14 22Q17 13 27 10", 3.6, HOLE) + ink_circle(47, 47, 13, INK, hs(3.6))
    return fit(out, 0.565, 32.5, 33.5)


@reg("net.krafting.HexColordle", BLUE_GREY_SOFT)
def hexcolordle():
    out = hx(32, 32, 28, -90, INK, 3)
    out += ink_stroke("M27 19L24 45", 3.4, HOLE) + ink_stroke("M38 19L35 45", 3.4, HOLE) + ink_stroke("M19 28H43", 3.4, HOLE) + ink_stroke("M18 38H41", 3.4, HOLE)
    return fit(out, 0.627, 32.0, 32.0)


@reg("net.krafting.Lovaflow", TEAL)
def lovaflow():
    out = path("M32 58C6 40 2 24 6 16C10 6 26 6 32 20C38 6 54 6 58 16C62 24 58 40 32 58Z", INK)
    out += ink_stroke("M14 32Q20 24 26 32T38 32T50 32", 3, HOLE)
    return fit(out, 0.583, 32.0, 33.5)


@reg("net.krafting.PedantiK", PINK)
def pedantik():
    out = ink_stroke("M16 58V8H33Q49 8 49 22Q49 36 33 36H16", 7) + circle(49, 52, 5.5, INK)
    return fit(out, 0.507, 37.5, 33.0)


@reg("net.krafting.Playlifin", CYAN_DEEP)
def playlifin():
    out = ink_stroke("M5 16H28", 4.6) + ink_stroke("M5 32H28", 4.6) + ink_stroke("M5 48H20", 4.6) + poly([(36, 14), (36, 54), (62, 34)], INK, 4)
    return fit(out, 0.515, 33.4, 34.0)


@reg("net.krafting.PlaylifinVoyager", GREY_DEEP)
def playlifinvoyager():
    out = ring_c(32, 32, 22, 4.4) + poly([(26, 21), (26, 43), (44, 32)], INK, 2.4)
    for a in (0, 90, 180, 270):
        x0, y0 = pt(32, 32, 27, a)
        x1, y1 = pt(32, 32, 33, a)
        out += ink_stroke(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", 4)
    return fit(out, 0.529, 32.0, 32.0)


@reg("net.krafting.PleasureDVR", DEEP_ORANGE_LIGHT)
def pleasuredvr():
    out = ink_rrect(4, 8, 56, 40, 8) + ink_rrect(10, 14, 44, 28, 4, HOLE) + ink_circle(32, 28, 8) + ink_rrect(14, 50, 9, 7, 2) + ink_rrect(41, 50, 9, 7, 2)
    return fit(out, 0.544, 32.0, 32.5)


@reg("net.krafting.Reddy", CYAN_LIGHT)
def reddy():
    out = ink_stroke("M32 20L38 6L50 11", 3.4) + ink_circle(52, 12, 5.4) + ink_circle(8, 32, 6.4) + ink_circle(56, 32, 6.4) + ell(32, 38, 24, 19)
    out += ink_circle(23, 36, 4.2, HOLE) + ink_circle(41, 36, 4.2, HOLE) + ink_stroke("M24 47Q32 53 40 47", 3, HOLE)
    return fit(out, 0.567, 32.0, 30.6)


@reg("net.krafting.SemantiK", DEEP_PURPLE)
def semantik():
    out = ink_stroke("M32 10L10 50", 3.4) + ink_stroke("M32 10L54 50", 3.4) + ink_stroke("M10 50H54", 3.4)
    out += ink_circle(32, 10, 9, INK, hs(3)) + ink_circle(10, 50, 9, INK, hs(3)) + ink_circle(54, 50, 9, INK, hs(3))
    return fit(out, 0.479, 32.0, 30.0)


@reg("net.kubux.Muehle", ORANGE_DARK)
def muehle():
    st = ' stroke="INK" stroke-width="3.4"'
    out = ink_rrect(4, 4, 56, 56, 0, "none", st) + ink_rrect(16, 16, 32, 32, 0, "none", st) + ink_rrect(26, 26, 12, 12, 0, "none", st)
    out += ink_stroke("M32 4V16", 3.4) + ink_stroke("M32 48V60", 3.4) + ink_stroke("M4 32H16", 3.4) + ink_stroke("M48 32H60", 3.4)
    out += ink_circle(4, 4, 6) + ink_circle(60, 60, 6) + ink_circle(60, 4, 6, HOLE, st) + ink_circle(32, 16, 5)
    return fit(out, 0.401, 32.9, 31.1)


@reg("net.labymod.LabyMod", BROWN)
def labymod():
    return fit(ink_stroke("M6 6H58V58H12V20H44V44H26", 4.6), 0.474, 32.0, 32.0)


@reg("net.launchpad.Gnuclad", PINK_LIGHT)
def gnuclad():
    out = ""
    for d in ("M4 32H16", "M16 16V48", "M16 16H34", "M34 8V24", "M34 8H60", "M34 24H60", "M16 48H44", "M44 40V58", "M44 40H60", "M44 58H60"):
        out += ink_stroke(d, 3.8)
    return fit(out, 0.47, 32.0, 33.0)


@reg("net.line72.campcounselor", ORANGE)
def campcounselor():
    out = poly([(32, 4), (60, 54), (4, 54)], INK, 4) + poly([(32, 30), (43, 54), (21, 54)], HOLE, 1) + ink_stroke("M2 59H62", 3)
    return fit(out, 0.437, 32.0, 31.2)


@reg("net.lockbook.Lockbook", BLUE)
def lockbook():
    out = ink_stroke("M18 28V20Q18 6 32 6Q46 6 46 20V28", 6.4) + ink_rrect(8, 28, 48, 32, 7) + ink_circle(32, 41, 5.4, HOLE) + ink_rrect(30, 43, 4, 10, 1.6, HOLE)
    return fit(out, 0.538, 32.0, 31.4)


@reg("net.longturn.freeciv21", ORANGE_DEEP)
def freeciv21():
    out = ink_rrect(4, 30, 14, 30, 2) + ink_rrect(20, 10, 18, 50, 2) + ink_rrect(40, 24, 12, 36, 2) + ink_rrect(54, 38, 8, 22, 2)
    for x, y in ((24, 16), (24, 28), (24, 40), (7.5, 36), (7.5, 47), (43, 30), (43, 42)):
        out += ink_rrect(x, y, 6 if x < 30 else 5, 6, 1, HOLE)
    return fit(out, 0.495, 33.0, 35.0)


@reg("net.lrclib.lrcget", PURPLE_DEEP)
def lrcget():
    out = ink_stroke("M22 12V46", 4.4) + ink_stroke("M50 6V42", 4.4) + poly([(22, 10), (50, 4), (50, 14), (22, 20)], INK, 1.5)
    out += ell(15, 48, 9.5, 7) + ell(43, 44, 9.5, 7) + ink_stroke("M6 60H58", 3.4)
    return fit(out, 0.467, 32.0, 32.5)


@reg("net.mkiol.Jupii", TEAL_SOFT)
def jupii():
    out = ink_stroke("M4 20V14Q4 8 10 8H54Q60 8 60 14V50Q60 56 54 56H32", 4.4) + ink_stroke("M4 44A14 14 0 0 1 18 58", 4.4) + ink_stroke("M4 30A28 28 0 0 1 32 58", 4.4) + ink_circle(7, 56, 3.6)
    return fit(out, 0.491, 32.0, 33.0)


@reg("net.newpipe.NewPipe", RED)
def newpipe():
    out = SB("M8 16H30Q50 16 50 36V52", 17) + ink_rrect(2, 3, 7, 26, 2) + ink_rrect(36, 52, 28, 7, 2) + poly([(18, 9.5), (18, 22.5), (29, 16)], HOLE, 1)
    return fit(out, 0.451, 33.0, 31.0)


@reg("net.nmlgc.rec98.sh01", CYAN)
def sh01():
    return fit(star4(32, 32, 30) + ink_circle(32, 32, 6, HOLE), 0.611, 32.0, 32.0)


@reg("net.nogasgofast.adventure_wrench", RED_DEEP)
def adventure_wrench():
    out = ink_circle(32, 15, 14) + ink_rrect(27, 0, 10, 14, 0, HOLE) + ink_rrect(28, 22, 8, 32, 3) + ink_circle(32, 57, 6.6) + ink_circle(32, 57, 2.6, HOLE)
    return fit(rot(out, 40, 32, 32), 0.564, 33.1, 31.3)


@reg("net.odamex.Odamex", BLUE_DEEP)
def odamex():
    out = ink_circle(32, 32, 28) + ink_circle(32, 26, 12, HOLE) + ink_circle(32, 26, 6) + ink_stroke("M13 46L19 52L25 46L32 52L39 46L45 52L51 46", 3, HOLE)
    return fit(out, 0.658, 32.0, 32.0)


@reg("net.openbve_project.OpenBVE", RED_LIGHT)
def openbve():
    out = ink_rrect(10, 2, 44, 46, 10) + ink_rrect(16, 10, 32, 16, 4, HOLE) + ink_circle(20, 37, 4, HOLE) + ink_circle(44, 37, 4, HOLE) + ink_stroke("M2 60H62", 3.6) + ink_stroke("M18 52L12 62", 3.4) + ink_stroke("M46 52L52 62", 3.4)
    return fit(out, 0.439, 32.0, 32.9)


@reg("net.openhabittracker.OpenHabitTracker", BLUE_GREY_DEEP)
def openhabittracker():
    out = ink_rrect(5, 10, 54, 50, 7) + ink_rrect(16, 3, 6, 12, 3) + ink_rrect(42, 3, 6, 12, 3) + ink_stroke("M5 25H59", 2.6, HOLE) + ink_stroke("M18 38H46M18 48H36", 5, HOLE)
    return fit(out, 0.51, 32.0, 31.5)


@reg("net.peercoin.peercoin-qt", BROWN_SOFT)
def peercoin_qt():
    out = ring_c(32, 32, 27, 5) + path("M18 46Q14 20 46 16Q50 44 18 46Z", INK) + ink_stroke("M22 42L36 26", 2.6, HOLE)
    return fit(out, 0.625, 32.0, 32.0)


@reg("net.pixieditor.PixiEditor", PURPLE)
def pixieditor():
    pts = [(1, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (1, 3), (2, 3), (3, 3), (2, 4)]
    return fit(cells(pts, 11, 12, 2, 2), 0.553, 31.5, 31.5)


@reg("net.pokerth.PokerTH", TEAL_DEEP)
def pokerth():
    out = ink_rrect(10, 2, 44, 60, 7) + path("M32 12Q52 28 46 38Q42 46 34 40Q35 46 40 52H24Q29 46 30 40Q22 46 18 38Q12 28 32 12Z", HOLE)
    return fit(out, 0.536, 32.0, 32.0)


@reg("net.portswigger.BurpSuite-Community", BLUE_GREY)
def burpsuite_community():
    return fit(poly([(38, 2), (12, 36), (28, 36), (22, 62), (52, 25), (35, 25)], INK, 4), 0.551, 32.0, 32.0)


@reg("net.ptilouk.littlebrats", INDIGO_LIGHT)
def littlebrats():
    out = ink_circle(32, 20, 17) + ink_stroke("M18 24Q32 12 46 24", 2.8, HOLE) + ink_stroke("M32 8V32", 2.8, HOLE) + ink_rrect(29, 36, 6, 14, 3) + ring_c(32, 57, 6, 3.8)
    return fit(out, 0.598, 32.0, 34.0)


@reg("net.ptilouk.superfluous", YELLOW)
def superfluous():
    out = ink_rrect(24, 4, 36, 36, 7) + ink_rrect(14, 14, 36, 36, 7, INK, hs(3.2)) + ink_rrect(4, 24, 36, 36, 7, INK, hs(3.2))
    return fit(out, 0.507, 32.0, 32.0)


@reg("net.purrdata.PurrData", INDIGO)
def purrdata():
    out = poly([(8, 34), (8, 4), (28, 16)], INK, 3) + poly([(56, 34), (56, 4), (36, 16)], INK, 3) + ell(32, 38, 25, 21)
    out += ell(22, 35, 3.4, 4.6, HOLE) + ell(42, 35, 3.4, 4.6, HOLE) + poly([(28, 43), (36, 43), (32, 48)], HOLE, 1)
    out += ink_stroke("M10 50H20", 2.2, HOLE) + ink_stroke("M44 50H54", 2.2, HOLE)
    return fit(out, 0.495, 32.0, 30.8)


@reg("net.qcde.QCDE", YELLOW_DARK)
def qcde():
    st = ' stroke="INK" stroke-width="3.6"'
    return fit(ink_rrect(4, 4, 26, 26, 5) + ink_rrect(34, 4, 26, 26, 5) + ink_rrect(4, 34, 26, 26, 5) + ink_rrect(35.8, 35.8, 22.4, 22.4, 4, "none", st), 0.493, 32.0, 32.0)


@reg("net.qsl.QSSTV", PINK_DEEP)
def qsstv():
    out = path("M6 14Q6 48 42 54Q38 18 6 14Z", INK) + ink_stroke("M18 30L38 14", 3.4) + ink_circle(40, 12, 4.6) + ink_stroke("M44 30A12 12 0 0 1 52 40", 3.4) + ink_stroke("M50 20A24 24 0 0 1 60 40", 3.4) + ink_stroke("M22 54L18 62", 3.4)
    return fit(out, 0.528, 33.9, 35.5)


@reg("net.rosebirch.nextgroove", DEEP_PURPLE_LIGHT)
def nextgroove():
    out = ink_circle(32, 32, 28) + ring_c(32, 32, 21, 2.4, HOLE) + ring_c(32, 32, 15, 2.4, HOLE) + ink_circle(32, 32, 8, HOLE) + ink_circle(32, 32, 2.6)
    return fit(out, 0.658, 32.0, 32.0)


@reg("net.rpdev.OpenTodoList", DEEP_ORANGE)
def opentodolist():
    st = ' stroke="INK" stroke-width="3.6"'
    out = ""
    for i, (y, x2) in enumerate(((4, 58), (24, 58), (44, 46))):
        out += ink_rrect(5, y, 16, 16, 3.5, "none", st) + ink_stroke(f"M30 {y + 8}H{x2}", 4.6)
    out += circle(13, 12, 3.6, INK)
    return fit(out, 0.471, 31.8, 31.5)


@reg("net.sf.metronomek", LIGHT_BLUE)
def metronomek():
    out = poly([(22, 4), (42, 4), (56, 60), (8, 60)], INK, 4) + ink_stroke("M32 52L43 16", 3.6, HOLE) + ink_circle(39, 28, 4.2, HOLE) + ink_stroke("M18 52H46", 2.6, HOLE)
    return fit(out, 0.477, 32.0, 32.0)


@reg("net.sourceforge.DuneLegacy", DEEP_ORANGE_DEEP)
def dunelegacy():
    out = ink_circle(42, 20, 14) + path("M2 62V46Q20 24 40 44Q50 54 62 44V62Z", INK, hs(3.4)) + path("M2 62V58Q22 46 40 58Q50 62 62 56V62Z", INK, hs(3.4))
    return fit(out, 0.453, 32.0, 34.0)


@reg("net.sourceforge.GrandOrgue", INDIGO_DEEP)
def grandorgue():
    out = ""
    for x, h in ((3, 34), (15, 46), (27, 58), (39, 46), (51, 34)):
        out += ink_rrect(x, 62 - h, 10, h, 3) + ink_rrect(x + 2, 62 - h + 10, 6, 4, 1, HOLE)
    return fit(out, 0.467, 32.0, 33.0)


@reg("net.sourceforge.Pdfedit", AMBER)
def pdfedit():
    out = poly([(8, 2), (36, 2), (52, 18), (52, 62), (8, 62)], INK, 3) + ink_stroke("M36 4V18H50", 2.6, HOLE) + ink_stroke("M16 28H34", 3, HOLE) + ink_stroke("M16 38H40", 3, HOLE)
    out += rot(ink_rrect(38, 30, 9, 26, 2, INK, hs(2.8)) + poly([(38, 55), (47, 55), (42.5, 65)], INK, 1), -38, 42, 44)
    return fit(out, 0.469, 31.2, 32.0)


@reg("net.sourceforge.QtSpim", BLUE_GREY_SOFT)
def qtspim():
    out = ink_rrect(14, 14, 36, 36, 5)
    for x in (19, 30, 41):
        out += ink_rrect(x, 4, 4, 10, 1.6) + ink_rrect(x, 50, 4, 10, 1.6)
    for y in (19, 30, 41):
        out += ink_rrect(4, y, 10, 4, 1.6) + ink_rrect(50, y, 10, 4, 1.6)
    out += ink_rrect(25, 25, 14, 14, 2.5, HOLE)
    return fit(out, 0.609, 32.0, 32.0)


@reg("net.sourceforge.SDL-Ball", TEAL)
def sdl_ball():
    out = ink_circle(44, 22, 11) + ink_stroke("M32 30L10 46", 3.6) + ink_stroke("M28 18L8 30", 3.6) + ink_stroke("M36 36L22 56", 3.6) + ink_rrect(8, 56, 48, 7, 3.5)
    return fit(out, 0.537, 31.1, 37.0)


@reg("net.sourceforge.artha.Artha", PINK)
def artha():
    out = ring_c(28, 28, 21, 5.4) + ink_stroke("M43 43L59 59", 7.4) + ink_stroke("M18 38L28 15L38 38", 4.2) + ink_stroke("M21 31H35", 3.4)
    return fit(out, 0.466, 33.5, 33.5)


@reg("net.sourceforge.audmes.audmes", CYAN_DEEP)
def audmes():
    out = ink_stroke("M2 22Q9 4 16 22T30 22T44 22T58 22", 4.4) + ink_rrect(2, 40, 60, 18, 3.5)
    for i, x in enumerate(range(10, 58, 8)):
        out += ink_stroke(f"M{x} 40V{47 if i % 2 else 52}", 2.6, HOLE)
    return fit(out, 0.493, 30.9, 34.4)


@reg("net.sourceforge.ddrescueview", GREY_DEEP)
def ddrescueview():
    out = ""
    for k in range(8):
        w = wedge(32, 32, 14, 29, k * 45 + 3, k * 45 + 42)
        out += dim(w, .32) if k in (2, 5, 6) else w
    out += ring_c(32, 32, 5, 3.6)
    return fit(out, 0.636, 32.0, 32.0)


@reg("net.sourceforge.dmidiplayer", DEEP_ORANGE_LIGHT)
def dmidiplayer():
    out = ink_rrect(3, 8, 58, 48, 5)
    for sx in (18, 32, 46):
        out += ink_rrect(sx - 5, 8, 10, 28, 2.5, HOLE) + ink_rrect(sx - 1.3, 36, 2.6, 20, 0, HOLE)
    return fit(out, 0.519, 32.0, 32.0)


@reg("net.sourceforge.efaxgtk", LIGHT_BLUE_SOFT)
def efaxgtk():
    out = ink_rrect(16, 2, 32, 24, 2.5) + ink_stroke("M22 9H42", 2.4, HOLE) + ink_stroke("M22 16H36", 2.4, HOLE)
    out += ink_rrect(3, 24, 58, 28, 7, INK, hs(3)) + ink_rrect(10, 31, 20, 6, 2, HOLE) + ink_circle(42, 34, 3, HOLE) + ink_circle(52, 34, 3, HOLE)
    out += ink_rrect(16, 48, 32, 14, 1.8, INK, hs(3))
    return fit(out, 0.556, 32.0, 32.0)


@reg("net.sourceforge.fspclient", DEEP_PURPLE)
def fspclient():
    out = path("M3 14Q3 8 9 8H23L30 16H55Q61 16 61 22V52Q61 58 55 58H9Q3 58 3 52Z", INK) + ink_stroke("M32 24V42", 5, HOLE) + arrowhead(32, 42, 0, 1, 10, HOLE)
    return fit(out, 0.51, 32.0, 33.0)


@reg("net.sourceforge.jpdftweak.jPdfTweak", BROWN_LIGHT)
def jpdftweak():
    out = ink_rrect(8, 2, 48, 60, 7)
    for y, cx in ((18, 26), (32, 40), (46, 30)):
        out += ink_stroke(f"M18 {y}H46", 2.6, HOLE) + ink_circle(cx, y, 4.4, HOLE)
    return fit(out, 0.519, 32.0, 32.0)


@reg("net.sourceforge.kmetronome", BROWN)
def kmetronome():
    out = dim(ink_stroke("M8 42A28 28 0 0 1 56 42", 3.4), .55)
    out += ink_rrect(14, 54, 36, 7, 3.5) + ink_stroke("M32 54L44 14", 4.6) + ink_circle(40.5, 26, 6.6)
    return fit(out, 0.636, 32.0, 36.4)


@reg("net.sourceforge.kmidimon", PINK_LIGHT)
def kmidimon():
    out = path("M5 38A27 27 0 0 1 59 38V50Q59 58 51 58H13Q5 58 5 50Z", INK)
    for x, y in ((14, 42), (21, 28), (32, 23), (43, 28), (50, 42)):
        out += ink_circle(x, y, 3.6, HOLE)
    out += ink_rrect(27, 50, 10, 8, 0, HOLE)
    return fit(out, 0.561, 32.0, 34.5)


@reg("net.sourceforge.lgames.Barrage", ORANGE)
def barrage():
    pts = [pt(32, 32, 30 if k % 2 == 0 else 16, -90 + 15 * k) for k in range(24)]
    return fit(poly(pts, INK, 1.8) + ink_circle(32, 32, 7, HOLE), 0.598, 32.0, 32.0)


@reg("net.sourceforge.lgames.LBreakoutHD", BLUE)
def lbreakouthd():
    out = ink_rrect(24, 4, 16, 9, 2) + ink_rrect(14.5, 16, 16, 9, 2) + ink_rrect(33.5, 16, 16, 9, 2) + ink_rrect(5, 28, 16, 9, 2) + ink_rrect(24, 28, 16, 9, 2) + ink_rrect(43, 28, 16, 9, 2)
    out += ink_circle(40, 46, 5) + ink_rrect(10, 56, 34, 6, 3)
    return fit(out, 0.526, 32.0, 33.0)


@reg("net.sourceforge.lgames.LGeneral", ORANGE_DEEP)
def lgeneral():
    out = hx(22, 14, 13, 0) + hx(43, 26, 13, 0) + star5(43, 26, 8, HOLE) + hx(22, 38, 13, 0) + hexring(43, 50, 12, 3.6)
    return fit(out, 0.517, 32.5, 32.5)


@reg("net.sourceforge.lgames.LPairs2", PURPLE_DEEP)
def lpairs2():
    c1 = rot(ink_rrect(4, 12, 28, 40, 5, INK, hs(3)) + ink_circle(18, 32, 7, HOLE), -13, 18, 32)
    c2 = rot(ink_rrect(32, 12, 28, 40, 5, INK, hs(3)) + poly([(46, 24), (54, 40), (38, 40)], HOLE, 2), 13, 46, 32)
    return fit(c1 + c2, 0.543, 31.9, 32.0)


@reg("net.sourceforge.m64py.M64Py", TEAL_SOFT)
def m64py():
    out = ink_rrect(2, 6, 60, 28, 14) + ink_rrect(2, 22, 18, 40, 9) + ink_rrect(44, 22, 18, 40, 9) + ink_rrect(24, 22, 16, 40, 8)
    out += ink_rrect(8, 17, 12, 4, 1.5, HOLE) + ink_rrect(12, 13, 4, 12, 1.5, HOLE) + ink_circle(32, 16, 4.4, HOLE) + ink_circle(47, 20, 3, HOLE) + ink_circle(54, 14, 3, HOLE)
    return fit(out, 0.496, 32.0, 34.0)


@reg("net.sourceforge.molsketch", RED)
def molsketch():
    out = hexring(24, 38, 17, 3.8) + ring_c(24, 38, 7, 2.8) + ink_stroke("M38 29L52 20", 3.8) + ink_circle(54, 18, 7) + ink_stroke("M24 55V62", 3.8)
    return fit(out, 0.532, 34.1, 37.5)


@reg("net.sourceforge.quakespasm.Quakespasm", CYAN)
def quakespasm():
    return fit(ring_c(30, 30, 22, 7.4) + ink_stroke("M40 40L58 58", 8.4) + ink_circle(30, 30, 4.4), 0.475, 33.2, 33.2)


@reg("net.sourceforge.scidvspc.scidvspc", RED_DEEP)
def scidvspc():
    out = ink_circle(32, 14, 11) + ink_rrect(21, 26, 22, 6, 3) + poly([(26, 31), (38, 31), (43, 52), (21, 52)], INK, 3) + ink_rrect(12, 52, 40, 10, 4.5)
    return fit(out, 0.547, 32.0, 32.5)


@reg("net.sourceforge.squirrel_sql", BLUE_DEEP)
def squirrel_sql():
    out = path("M5 14V50Q5 61 32 61Q59 61 59 50V14Z", INK) + ell(32, 14, 27, 10) + ellring(32, 14, 15, 4.4, 2.6, HOLE)
    out += ink_stroke("M5 30Q32 46 59 30", 2.8, HOLE) + ink_stroke("M5 44Q32 60 59 44", 2.8, HOLE)
    return fit(out, 0.549, 32.0, 32.5)


@reg("net.sourceforge.tomatoes.IHaveNoTomatoes", RED_LIGHT)
def ihavenotomatoes():
    out = ink_circle(32, 37, 26) + ink_rrect(29.5, 2, 5, 11, 2.5) + star5(32, 19, 13, HOLE)
    return fit(out, 0.606, 32.0, 32.5)


@reg("net.sourceforge.uhexen2.uhexen2", PURPLE)
def uhexen2():
    return fit(ink_stroke("M32 4L58 48H6Z", 5.4) + ink_stroke("M32 60L6 16H58Z", 5.4), 0.556, 32.0, 32.0)


@reg("net.sourceforge.wavbreaker", DEEP_PURPLE_SOFT)
def wavbreaker():
    out = ""
    for x, h in ((4, 16), (11, 32), (18, 22), (25, 40)):
        out += ink_stroke(f"M{x} {32 - h / 2}V{32 + h / 2}", 4.4)
    for x, h in ((39, 36), (46, 18), (53, 30), (60, 12)):
        out += ink_stroke(f"M{x} {32 - h / 2}V{32 + h / 2}", 4.4)
    out += ink_stroke("M36 2L29 28L36 34L29 62", 3.4)
    return fit(out, 0.581, 32.0, 32.0)


@reg("net.sourceforge.wxEDID", PURPLE)
def wxedid():
    out = poly([(3, 12), (61, 12), (61, 34), (51, 46), (13, 46), (3, 34)], INK, 4) + SB("M32 46V62", 10)
    for x in range(12, 54, 6):
        out += ink_stroke(f"M{x} 21V32", 2.6, HOLE)
    return fit(out, 0.466, 32.0, 36.0)


@reg("net.stabyourself.nottetris2", TEAL_DEEP)
def nottetris2():
    pts = [(1, 0), (2, 0), (0, 1), (1, 1), (2, 2), (1, 3), (2, 3), (3, 3)]
    return fit(cells(pts, 13, 15, 3, 3), 0.464, 32.0, 32.0)


@reg("net.tabletopclub.TabletopClub", BLUE_GREY)
def tabletopclub():
    out = ink_rrect(8, 8, 48, 48, 11)
    for x, y in ((20, 20), (44, 20), (32, 32), (20, 44), (44, 44)):
        out += ink_circle(x, y, 4.6, HOLE)
    return fit(rot(out, -12), 0.627, 32.5, 32.0)


@reg("net.tedomum.CapBattleship", INDIGO_LIGHT)
def capbattleship():
    out = path("M2 38H62L53 52H12Z", INK) + ink_rrect(22, 26, 22, 12, 2) + ink_rrect(29, 15, 8, 11, 2) + ink_rrect(8, 28, 12, 10, 3) + ink_stroke("M8 31H2", 3.4) + ink_stroke("M4 60Q12 55 20 60T36 60T52 60", 3)
    return fit(out, 0.522, 31.1, 39.5)


@reg("net.tidycustoms.Publii", YELLOW)
def publii():
    out = ring_c(32, 32, 26, 5) + ellring(32, 32, 11, 26, 3.6) + ink_stroke("M6 32H58", 3.6) + ink_stroke("M10 18H54", 3) + ink_stroke("M10 46H54", 3)
    return fit(out, 0.647, 32.0, 32.0)


@reg("net.trowell.kotoba", INDIGO)
def kotoba():
    out = path("M0 12Q32 22 64 12L60 3Q32 12 4 3Z", INK) + ink_rrect(10, 22, 44, 6, 2) + ink_rrect(14, 22, 7, 40, 2) + ink_rrect(43, 22, 7, 40, 2) + ink_rrect(29, 12, 6, 10, 1)
    return fit(out, 0.457, 32.0, 32.5)


@reg("net.trowell.typesetter", YELLOW_DARK)
def typesetter():
    return fit(ink_rrect(8, 6, 48, 10, 2) + ink_rrect(8, 6, 7, 20, 2) + ink_rrect(49, 6, 7, 20, 2) + ink_rrect(27.5, 6, 9, 48, 2) + ink_rrect(18, 52, 28, 8, 2), 0.523, 32.0, 33.0)


@reg("net.unvanquished.Unvanquished", PINK_DEEP)
def unvanquished():
    return fit(ink_stroke("M6 34L32 10L58 34", 7.4) + ink_stroke("M6 56L32 32L58 56", 7.4), 0.482, 32.0, 33.0)


@reg("net.windower.Lumoria", DEEP_PURPLE_LIGHT)
def lumoria():
    return fit(crescent(26, 32, 25) + star4(49, 17, 12) + star4(50, 46, 7), 0.559, 31.1, 30.9)


@reg("net.zdechov.app.AcronymDecoder", DEEP_ORANGE)
def acronymdecoder():
    out = ink_stroke("M5 58L21 8L37 58", 6.4) + ink_stroke("M11 42H31", 5) + ink_stroke("M46 18H60", 4.4) + ink_stroke("M46 32H60", 4.4) + ink_stroke("M46 46H56", 4.4)
    return fit(out, 0.464, 32.0, 33.0)


@reg("net.zdechov.app.C-evo", LIGHT_BLUE)
def c_evo():
    return fit(arc_arrow(32, 32, 22, 38, 322, 7, 10), 0.583, 31.9, 32.0)


@reg("net.zdechov.app.LazFuck", DEEP_ORANGE_DEEP)
def lazfuck():
    return fit(ink_stroke("M16 6H5V58H16", 5.4) + ink_stroke("M48 6H59V58H48", 5.4) + ink_stroke("M25 20L40 32L25 44", 6), 0.461, 32.0, 32.0)


@reg("net.zdechov.app.TransLines", INDIGO_DEEP)
def translines():
    out = ink_stroke("M8 56H28L46 38V12", 5.4) + ink_stroke("M46 38H58", 5.4)
    for x, y in ((8, 56), (46, 12), (58, 38)):
        out += ink_circle(x, y, 7) + ink_circle(x, y, 3, HOLE)
    return fit(out, 0.459, 33.0, 34.0)


@reg("net.zdechov.app.Tunneler", AMBER)
def tunneler():
    out = ink_rrect(3, 40, 58, 20, 10) + ink_rrect(14, 26, 36, 14, 3, INK, hs(2.4)) + ink_rrect(24, 14, 18, 13, 3, INK, hs(2.4)) + ink_rrect(40, 18, 22, 5, 2.5)
    for x in (15, 32, 49):
        out += ink_circle(x, 50, 3.6, HOLE)
    return fit(out, 0.544, 32.5, 37.0)


@reg("net.zdechov.app.vCardStudio", BLUE_GREY_SOFT)
def vcardstudio():
    out = ink_rrect(2, 10, 60, 44, 7) + ink_circle(20, 27, 6.6, HOLE) + path("M8 47Q8 36 20 36Q32 36 32 47Z", HOLE)
    out += ink_stroke("M39 22H55", 3.4, HOLE) + ink_stroke("M39 32H55", 3.4, HOLE) + ink_stroke("M39 42H49", 3.4, HOLE)
    return fit(out, 0.536, 32.0, 32.0)


@reg("net.zdechov.app.x2048", TEAL)
def x2048():
    out = ink_rrect(4, 4, 56, 56, 11) + ink_stroke("M19 23Q19 13 32 13Q45 13 45 24Q45 32 19 51H46", 5, HOLE)
    return fit(out, 0.528, 32.0, 32.0)


@reg("net.zdechov.app.xTactics", PINK)
def xtactics():
    out = ring_c(32, 32, 21, 4.4) + ink_rrect(27.5, 27.5, 9, 9, 1.5)
    for a in (0, 90, 180, 270):
        x0, y0 = pt(32, 32, 12, a)
        x1, y1 = pt(32, 32, 32, a)
        out += ink_stroke(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", 4.4)
    return fit(out, 0.541, 32.0, 32.0)


@reg("net.zgcoder.skycheckers", CYAN_DEEP)
def skycheckers():
    pts = [(c, r) for r in range(3) for c in range(3) if (r + c) % 2 == 0]
    return fit(rot(cells(pts, 13, 14.5, 10.25, 10.25), 45, 32, 32), 0.645, 32.0, 30.9)


@reg("nl.brixit.wiremapper", GREY_DEEP)
def wiremapper():
    out = ink_rrect(22, 12, 24, 40, 6) + ink_rrect(28, 22, 12, 4, 2, HOLE) + ink_rrect(28, 36, 12, 4, 2, HOLE)
    out += ink_stroke("M2 20H22", 3.8) + ink_stroke("M2 32H22", 3.8) + ink_stroke("M2 44H22", 3.8) + ink_stroke("M46 22H54L61 12", 3.8) + ink_stroke("M46 42H54L61 52", 3.8)
    return fit(out, 0.493, 31.5, 32.0)
