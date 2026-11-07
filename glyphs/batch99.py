# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 99: the fourteenth hundred apps from the gap list (flags/app-gap-list-full.md),
rows 1301 to 1400, Gelly to prunr. Each is a simple original mark on its own tile."""
from lm import *
from glyphs.kit import (
    arrowhead, asterisk, cells, crescent, dim, ell, fit, H, hexring, I, ink_circle, ink_stroke,
    lem, registry, ring_c, rl, rot, SB, star4, wedge,
)

ICONS, SMALL, reg, _ = registry()

@reg("io.m51.Gelly", RED)
def i1301():
    out = path("M8 36Q8 6 32 6Q56 6 56 36Z", I)
    for x in (16, 32, 48):
        out += ink_stroke(f"M{x} 36Q{x - 5} 46 {x} 52Q{x + 4} 58 {x}  62", 4.4)
    out += ink_stroke("M18 26Q21 16 30 14", 3.4, H)
    return fit(out, 0.553, 31.8, 35.0)

@reg("io.mango3d.LycheeSlicer", CYAN)
def i1302():
    out = poly([(25, 0), (39, 0), (32, 11)], I, 1.5) + rl(18, 16, 28, 10, 3) + rl(12, 30, 40, 10, 3) + rl(6, 44, 52, 10, 3)
    return fit(out, 0.507, 31.8, 26.4)

@reg("io.mimiri.notes", BROWN_LIGHT)
def i1303():
    out = rl(12, 6, 42, 52, 6)
    for y in (16, 32, 48):
        out += rl(5, y - 3, 17, 6, 3) + ink_circle(17, y, 1.6, H)
    out += ink_stroke("M30 18H46", 3.4, H) + ink_stroke("M30 30H46", 3.4, H) + ink_stroke("M30 42H40", 3.4, H)
    return fit(out, 0.557, 29.4, 31.8)

@reg("io.naox.InnerBreeze", INDIGO_LIGHT)
def i1304():
    out = ink_stroke("M6 22H38Q50 22 50 14Q50 8 44 8Q39 8 39 13", 4.4)
    out += ink_stroke("M6 34H46Q58 34 58 43Q58 51 51 51Q46 51 46 46", 4.4)
    out += ink_stroke("M6 46H28Q35 46 35 52Q35 57 31 57", 4.4)
    return fit(out, 0.59, 32.0, 32.4)

@reg("io.osdn.simplesok", YELLOW_DARK)
def i1305():
    out = rl(6, 6, 52, 52, 7) + rl(13, 13, 38, 38, 3, H) + ink_stroke("M19 19L45 45", 5.4) + ink_stroke("M45 19L19 45", 5.4)
    return fit(out, 0.548, 31.8, 31.8)

@reg("io.ossia.score", PINK_DEEP)
def i1306():
    out = rl(4, 8, 24, 11, 3) + rl(20, 24, 32, 11, 3) + rl(8, 40, 28, 11, 3) + rl(40, 40, 18, 11, 3)
    out += ink_stroke("M46 3V61", 7, H) + ink_stroke("M46 3V61", 3.2)
    return fit(out, 0.514, 30.8, 32.0)

@reg("io.pslab.PSLab", TEAL_DARK)
def i1307():
    out = rl(4, 8, 56, 42, 7) + rl(10, 14, 44, 30, 3, H) + ink_stroke("M13 29Q20 12 27 29T41 29T53 29", 3.6) + rl(20, 52, 24, 6, 3)
    return fit(out, 0.539, 31.8, 32.8)

@reg("io.qt.qtdesignstudio", GREY_LIGHT)
def i1308():
    out = ink_stroke("M12 12H50V46H12Z", 3)
    for x, y in ((12, 12), (50, 12), (12, 46)):
        out += rl(x - 5, y - 5, 10, 10, 2.5)
    out += poly([(36, 30), (36, 56), (43, 49), (48, 60), (53, 58), (48, 47), (57, 47)], H, 6)
    out += poly([(36, 30), (36, 56), (43, 49), (48, 60), (53, 58), (48, 47), (57, 47)], I, 1.6)
    return fit(out, 0.497, 33.4, 35.0)

@reg("io.scottlabs.reManager", BLUE_SOFT)
def i1309():
    out = rl(3, 10, 58, 42, 6) + rl(9, 16, 46, 30, 2, H)
    out += ink_stroke("M22 40L44 22", 8, H) + ink_stroke("M22 40L44 22", 4.2) 
    return fit(out, 0.555, 32.0, 30.8)

@reg("io.sourceforge.YSoccer", ORANGE)
def i1310():
    out = ring_c(32, 32, 26, 4.4) + poly([pt(32, 32, 10, -90 + 72 * k) for k in range(5)], I, 2)
    for k in range(5):
        a = -90 + 72 * k
        x0, y0 = pt(32, 32, 12, a)
        x1, y1 = pt(32, 32, 24, a)
        out += ink_stroke(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", 3.4)
    return fit(out, 0.657, 32.0, 32.0)

@reg("io.sourceforge.clonekeenplus", PURPLE)
def i1311():
    out = ink_stroke("M18 8H46", 5) + ink_stroke("M32 8V18", 4.4) + ink_stroke("M32 18L22 24L42 30L22 36L42 42L32 46", 3.6) + ink_stroke("M32 46V56", 4.4) + ink_stroke("M22 58H42", 4.4)
    return fit(out, 0.6, 32.0, 32.8)

@reg("io.sourceforge.klatexformula.klatexformula", INDIGO_SOFT)
def i1312():
    out = ink_stroke("M42 12Q36 4 30 14V46Q28 60 18 54", 5.4) + ink_circle(46, 14, 4.4) + ink_circle(16, 52, 4.4)
    return fit(out, 0.64, 30.8, 32.2)

@reg("io.sourceforge.pentobi", BLUE_GREY_LIGHT)
def i1313():
    A = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
    B = [(1, 0), (2, 0), (2, 1)]
    return fit(cells(A, 15, 17, 6, 6) + dim(cells(B, 15, 17, 6, 6), .5), 0.553, 30.4, 30.4)

@reg("io.sourceforge.pipewalker.PipeWalker", LIGHT_BLUE_LIGHT)
def i1314():
    out = ink_stroke("M12 16H36V48", 11) + ink_stroke("M36 34H54", 11)
    out += ink_stroke("M12 16H34V46", 3.4, H) + ink_stroke("M34 34H50", 3.4, H)
    out += rl(3, 8, 7, 16, 2.5) + rl(28, 49, 16, 7, 2.5) + rl(53, 26, 7, 16, 2.5)
    return fit(out, 0.516, 31.4, 31.8)

@reg("io.sourceforge.pysolfc.PySolFC", DEEP_ORANGE_DEEP)
def i1315():
    out = rl(10, 4, 44, 56, 6)
    out += path("M32 12C32 12 17 24 17 34C17 40 23 43 28 40C27 46 26 49 23 52H41C38 49 37 46 36 40C41 43 47 40 47 34C47 24 32 12 32 12Z", H)
    return fit(out, 0.557, 31.8, 31.8)

@reg("io.sourceforge.trigger_rally.TriggerRally", DEEP_PURPLE_DEEP)
def i1316():
    out = poly([(23, 4), (41, 4), (60, 58), (4, 58)], I, 3) + rl(30.5, 9, 3, 7, 1, H) + rl(30, 21, 4, 10, 1.2, H) + rl(29, 37, 6, 14, 1.5, H)
    return fit(out, 0.461, 32.0, 31.0)

@reg("io.sourceforge.wsjt.wsjtx", AMBER_DARK)
def i1317():
    out = ink_stroke("M6 32H58", 4) + ink_stroke("M14 21V43", 4.4) + ink_stroke("M26 12V52", 4.4) + ink_stroke("M38 18V46", 4.4) + ink_stroke("M50 23V41", 4.4)
    return fit(rot(out, -25, 32, 32), 0.637, 31.8, 34.4)

@reg("io.sourceforge.xtrkcad_fork.xtrkcad", RED_LIGHT)
def i1318():
    cx, cy = 6, 58
    out = ink_stroke(f"M{cx} {cy - 28}A28 28 0 0 1 {cx + 28} {cy}", 3.6) + ink_stroke(f"M{cx} {cy - 46}A46 46 0 0 1 {cx + 46} {cy}", 3.6)
    for a in (-82, -62, -42, -22, -6):
        x0, y0 = pt(cx, cy, 24, a)
        x1, y1 = pt(cx, cy, 50, a)
        out += ink_stroke(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", 3.4)
    return fit(out, 0.541, 30.8, 33.2)

@reg("io.speedofsound.SpeedOfSound", CYAN_SOFT)
def i1319():
    out = rl(22, 3, 20, 32, 10) + ink_stroke("M27 13H37", 3, H) + ink_stroke("M27 21H37", 3, H) + ink_stroke("M13 28Q13 46 32 46Q51 46 51 28", 4.4) + ink_stroke("M32 46V57", 4.4) + ink_stroke("M21 58H43", 4.4)
    return fit(out, 0.605, 31.8, 31.6)

@reg("io.stoplight.studio", BROWN)
def i1320():
    out = ink_stroke("M24 6Q16 6 16 14V24Q16 32 8 32Q16 32 16 40V50Q16 58 24 58", 4.6) + ink_stroke("M40 6Q48 6 48 14V24Q48 32 56 32Q48 32 48 40V50Q48 58 40 58", 4.6) + ink_circle(32, 32, 4.4)
    return fit(out, 0.612, 32.0, 32.0)

@reg("io.tdarr.Tdarr_Node", INDIGO)
def i1321():
    out = hexring(32, 32, 26, 4.4) + poly([(25, 21), (25, 43), (43, 32)], I, 2.4)
    return fit(out, 0.657, 31.8, 32.0)

@reg("io.tdarr.Tdarr_Server", YELLOW)
def i1322():
    out = ""
    for y in (4, 24, 44):
        out += rl(5, y, 54, 16, 5) + ink_circle(15, y + 8, 2.8, H) + ink_stroke(f"M26 {y + 8}H48", 3, H)
    return fit(out, 0.504, 32.0, 31.8)

@reg("io.tether.QVAC.Workbench", PINK_LIGHT)
def i1323():
    out = star4(32, 16, 15) + rl(4, 36, 56, 8, 3) + rl(10, 44, 7, 16, 2) + rl(47, 44, 7, 16, 2) + rl(17, 50, 30, 4, 1.5)
    return fit(out, 0.515, 31.8, 30.2)

@reg("io.thenexusavenger.Nexus-LU-Launcher", TEAL_LIGHT)
def i1324():
    out = rl(6, 24, 52, 34, 5) + rl(10, 12, 12, 14, 3) + rl(26, 12, 12, 14, 3) + rl(42, 12, 12, 14, 3)
    return fit(out, 0.567, 31.8, 34.8)

@reg("io.trezor.suite", GREY_DEEP)
def i1325():
    out = rl(14, 3, 36, 58, 8) + rl(20, 10, 24, 18, 3, H) + ink_circle(32, 42, 5.4, H) + rl(30, 45, 4, 9, 1.5, H)
    return fit(out, 0.596, 31.8, 32.0)

@reg("io.unobserved.espansoGUI", BLUE_DEEP)
def i1326():
    out = rl(4, 24, 12, 16, 4) + ink_stroke("M21 32H32", 4.4) + arrowhead(30, 32, 1, 0, 8) + rl(40, 12, 20, 6, 3) + rl(40, 29, 20, 6, 3) + rl(40, 46, 20, 6, 3)
    return fit(out, 0.556, 31.8, 31.8)

@reg("io.unobserved.furtherance", ORANGE_DARK)
def i1327():
    out = ring_c(32, 37, 22, 4.6) + rl(26, 4, 12, 7, 2.5) + ink_stroke("M32 37V23", 4.4) + ink_stroke("M32 37L42 43", 4.4) + ink_stroke("M48 12L53 17", 4.4) + ink_circle(32, 37, 3.4)
    return fit(out, 0.644, 32.0, 32.6)

@reg("io.vikunja.Vikunja", PURPLE_LIGHT)
def i1328():
    out = ""
    for k, y in enumerate((12, 31, 50)):
        if k < 2:
            out += rl(6, y - 5, 14, 14, 3.4)
        else:
            out += ink_stroke(f"M6 {y - 5}H20V{y + 9}H6Z", 3.4)
        out += rl(30, y, 28, 6, 3)
    return fit(out, 0.503, 30.2, 33.2)

@reg("io.welle.welle-gui", ORANGE_LIGHT)
def i1329():
    out = rl(3, 20, 58, 38, 7) + ink_stroke("M42 20L54 5", 3.6) + ink_circle(54, 5, 2.8) + ink_circle(20, 39, 11, H) + ink_circle(20, 39, 3.6) + ink_stroke("M37 32H53", 3.4, H) + ink_stroke("M37 40H53", 3.4, H) + rl(37, 46, 16, 5, 2.5, H)
    return fit(out, 0.498, 32.0, 30.0)

@reg("ir.NonFree.VCMusic", BLUE_GREY)
def i1330():
    out = ink_circle(32, 32, 26) + ring_c(32, 32, 17.5, 2.4, H) + ink_circle(32, 32, 8.5, H) + ink_circle(32, 32, 2.6) + ink_stroke("M14 22Q17 14 24 10", 2.6, H)
    return fit(out, 0.709, 31.8, 31.8)

@reg("it.andreafontana.hideout", LIGHT_BLUE)
def i1331():
    out = poly([(32, 5), (60, 56), (4, 56)], I, 3) + poly([(32, 28), (43, 56), (21, 56)], H) + ink_stroke("M2 59H62", 3)
    return fit(out, 0.447, 32.0, 32.0)

@reg("it.astrogods.AstroGods", DEEP_ORANGE)
def i1332():
    out = poly([(6, 46), (6, 16), (20, 30), (32, 10), (44, 30), (58, 16), (58, 46)], I, 3) + rl(6, 49, 52, 9, 3) + ink_circle(32, 38, 4.4, H)
    return fit(out, 0.538, 32.0, 33.2)

@reg("it.belloworld.mercurygram", DEEP_PURPLE_LIGHT)
def i1333():
    out = poly([(4, 30), (60, 6), (44, 58), (30, 40)], I, 2.5) + ink_stroke("M58 8L30 40", 3, H) + poly([(30, 40), (33, 58), (42, 48)], I, 1.8)
    return fit(out, 0.473, 32.0, 32.0)

@reg("it.cuteworks.pacmanlogviewer", BLUE_SOFT)
def i1334():
    out = path("M32 32L54.5 19A26 26 0 1 0 54.5 45Z", I, ' stroke="INK" stroke-width="3" stroke-linejoin="round"') + ink_circle(31, 17, 3.6, H) + ink_circle(58, 32, 3.8)
    return fit(out, 0.65, 33.0, 32.0)

@reg("it.dottorblaster.cauldron", RED_DEEP)
def i1335():
    out = path("M9 28H55Q55 56 32 56Q9 56 9 28Z", I) + rl(4, 21, 56, 9, 4.5) + rl(14, 52, 7, 9, 2) + rl(43, 52, 7, 9, 2) + ink_circle(22, 9, 5.4) + ink_circle(37, 12, 3.8) + ink_circle(45, 3, 3)
    out += ink_stroke("M17 38Q19 47 27 50", 3, H)
    return fit(out, 0.534, 31.8, 30.4)

@reg("it.fabiodistasio.AntaresSQL", CYAN_DEEP)
def i1336():
    out = ell(32, 14, 22, 9) + path("M10 14V48Q10 58 32 58Q54 58 54 48V14Q54 24 32 24Q10 24 10 14Z", I)
    out += SB("M10 30Q32 40 54 30", 3, H) + SB("M10 44Q32 54 54 44", 3, H)
    return fit(out, 0.631, 32.0, 31.4)

@reg("it.mijorus.collector", BROWN_DARK)
def i1337():
    out = ink_stroke("M32 6V24", 4.8) + arrowhead(32, 22, 0, 1, 9) + path("M4 38H20L24 46H40L44 38H60V58H4Z", I, ' stroke="INK" stroke-width="3" stroke-linejoin="round"')
    return fit(out, 0.465, 32.0, 31.4)

@reg("it.mijorus.whisper", INDIGO_LIGHT)
def i1338():
    out = path("M56 5Q20 6 12 38Q10 46 11 52Q22 48 30 40Q50 26 56 5Z", I) + ink_stroke("M6 60L22 44", 3.4) + ink_stroke("M18 48L44 20", 2.4, H)
    return fit(out, 0.488, 30.0, 33.4)

@reg("it.mq1.TinyWiiBackupManager", YELLOW_SOFT)
def i1339():
    out = ink_circle(32, 32, 26) + ink_circle(32, 32, 7, H) + ring_c(32, 32, 14, 2.2, H) + ink_stroke("M13 24Q17 14 27 10", 3, H)
    return fit(out, 0.709, 31.8, 31.8)

@reg("it.unibo.tuprolog.ide", PINK)
def i1340():
    out = rl(3, 8, 58, 48, 7) + rl(9, 21, 46, 29, 3, H) + ink_circle(19, 30, 3.2) + ink_circle(19, 42, 3.2) + rl(26, 34, 13, 5, 2.5) + rl(44, 34, 6, 5, 2.5)
    return fit(out, 0.534, 32.0, 31.8)

@reg("jp.nonbili.meron", TEAL)
def i1341():
    out = path("M5 24A27 27 0 0 0 59 24Z", I) + path("M11 26A21 21 0 0 0 53 26Z", H) + ell(24, 38, 2, 3.4) + ell(32, 42, 2, 3.4) + ell(40, 38, 2, 3.4) + ink_stroke("M32 22V10Q32 5 38 5", 3.4)
    return fit(out, 0.689, 32.0, 27.2)

@reg("jp.nonbili.nora", GREY)
def i1342():
    out = ink_stroke("M11 42V32Q11 8 32 8Q53 8 53 32V42", 5) + rl(5, 36, 15, 22, 7) + rl(44, 36, 15, 22, 7)
    return fit(out, 0.534, 32.0, 31.6)

@reg("la.ogri.strongbox", BLUE_LIGHT)
def i1343():
    out = rl(5, 5, 54, 48, 7) + rl(11, 11, 42, 36, 3, H) + ring_c(32, 29, 9.5, 3.6) + ink_stroke("M32 29L39 22", 3.4) + rl(11, 53, 11, 7, 2) + rl(42, 53, 11, 7, 2)
    return fit(out, 0.522, 32.0, 32.4)

@reg("land.arcana.TarotCanvas", ORANGE_LIGHT)
def i1344():
    out = rl(13, 3, 38, 58, 6) + rl(18, 8, 28, 48, 3, "none", ' stroke="HOLE" stroke-width="2.4"') + crescent(29, 36, 10, H) + star4(39, 21, 6.5, H)
    return fit(out, 0.573, 32.0, 32.0)

@reg("life.bolls.bolls", PURPLE_DEEP)
def i1345():
    out = path("M30 14Q20 7 4 10V50Q20 46 30 54Z", I) + path("M34 14Q44 7 60 10V50Q44 46 34 54Z", I)
    out += ink_stroke("M10 21Q17 20 24 24", 2.8, H) + ink_stroke("M10 31Q17 30 24 34", 2.8, H) + ink_stroke("M40 24Q47 20 54 21", 2.8, H) + ink_stroke("M40 34Q47 30 54 31", 2.8, H)
    return fit(out, 0.53, 31.8, 31.4)

@reg("lol.janjic.Splitcat", BLUE_GREY)
def i1346():
    out = ink_circle(32, 37, 22) + poly([(9, 26), (11, 5), (28, 17)], I, 3) + poly([(55, 26), (53, 5), (36, 17)], I, 3)
    out += ell(23, 37, 3, 4.2, H) + ell(41, 37, 3, 4.2, H) + poly([(29, 46), (35, 46), (32, 50)], H, 1.2) + SB("M32 3V63", 3, H)
    return fit(out, 0.51, 32.0, 33.0)

@reg("lol.siembra.tuxtypeplus", BLUE_GREY_DARK)
def i1347():
    out = rl(5, 6, 54, 50, 10) + rl(11, 11, 42, 34, 6, H) + ink_stroke("M22 21H42", 5.4) + ink_stroke("M32 21V36", 5.4)
    return fit(out, 0.569, 32.0, 30.8)

@reg("lv.martinsz.millionaire", LIGHT_BLUE_LIGHT)
def i1348():
    out = poly([(4, 32), (16, 9), (48, 9), (60, 32), (48, 55), (16, 55)], I, 3) + ink_stroke("M24 25Q24 17 32 17Q40 17 40 25Q40 31 32 34V37", 4.6, H) + ink_circle(32, 46, 3.2, H)
    return fit(out, 0.63, 32.0, 32.0)

@reg("me.acristoffers.Lachesis", DEEP_ORANGE_SOFT)
def i1349():
    out = rl(12, 3, 36, 9, 3) + rl(12, 52, 36, 9, 3) + rl(18, 11, 24, 42, 2)
    out += SB("M18 21L42 27", 2.8, H) + SB("M18 31L42 37", 2.8, H) + SB("M18 41L42 47", 2.8, H) + ink_stroke("M42 48Q57 46 55 34Q53 25 59 21", 3)
    return fit(out, 0.509, 36.2, 32.0)

@reg("me.ahola.aphototoollibre", DEEP_PURPLE)
def i1350():
    out = rl(3, 10, 58, 44, 7) + rl(9, 16, 46, 32, 3, H) + poly([(9, 48), (23, 28), (33, 40), (41, 32), (55, 48)], I, 2) + ink_circle(42, 24, 4.4)
    return fit(out, 0.553, 32.0, 31.8)

@reg("me.amankhanna.opendeck", AMBER)
def i1351():
    out = rl(3, 6, 58, 52, 8)
    for j, y in enumerate((12, 35)):
        for i, x in enumerate((9, 25, 41)):
            out += rl(x, y, 14, 17, 3, H)
    return fit(out, 0.521, 32.0, 31.8)

@reg("me.breakgim.runa", RED)
def i1352():
    out = ink_stroke("M20 6V58", 5.4) + ink_stroke("M20 8H34L46 20L34 32H20", 5.4) + ink_stroke("M32 32L48 58", 5.4)
    return fit(out, 0.577, 34.0, 32.0)

@reg("me.broken_by.PdfMetadataEditor", CYAN_LIGHT)
def i1353():
    out = path("M8 3H34L46 15V56H8Z", I) + poly([(34, 3), (34, 15), (46, 15)], H) + ink_stroke("M15 26H36", 3.2, H) + ink_stroke("M15 35H30", 3.2, H)
    tag = [(30, 40), (52, 40), (62, 50), (52, 60), (30, 60)]
    out += poly(tag, H, 9) + poly(tag, I, 3) + ink_circle(53, 50, 2.4, H)
    return fit(out, 0.44, 37.2, 33.8)

@reg("me.drewol.Unnamed-SDVX-Clone", BROWN_LIGHT)
def i1354():
    out = ring_c(17, 17, 11, 4.2) + ink_stroke("M17 17L17 9", 3.4) + ring_c(47, 17, 11, 4.2) + ink_stroke("M47 17L53 12", 3.4) + rl(4, 38, 56, 7, 3.5) + rl(34, 32, 12, 19, 3.5) + rl(6, 54, 24, 6, 3) + rl(34, 54, 24, 6, 3)
    return fit(out, 0.503, 32.0, 31.8)

@reg("me.dumke.Reinschrift", INDIGO_DEEP)
def i1355():
    out = path("M17 4H47L51 24L32 60L13 24Z", I, ' stroke="INK" stroke-width="2.6" stroke-linejoin="round"') + ink_stroke("M32 32V56", 2.6, H) + ink_circle(32, 27, 4.4, H) + SB("M13 24H51", 2.4, H)
    return fit(out, 0.562, 32.0, 32.0)

@reg("me.dumke.deliveries", YELLOW_DARK)
def i1356():
    out = rl(2, 12, 35, 34, 4) + path("M40 21H50Q54 21 57 26L62 33V46H40Z", I)
    out += poly([(44, 25), (50, 25), (56, 33), (44, 33)], H, 1)
    out += ink_circle(16, 49, 10, H) + ink_circle(50, 49, 10, H) + ink_circle(16, 49, 7.4) + ink_circle(50, 49, 7.4) + ink_circle(16, 49, 2.6, H) + ink_circle(50, 49, 2.6, H)
    return fit(out, 0.513, 31.8, 35.4)

@reg("me.fouquet.Stencil", PINK_DARK)
def i1357():
    out = ink_stroke("M9 58L25 20", 6.4) + ink_stroke("M55 58L39 20", 6.4) + ink_stroke("M26 12L32 4L38 12", 6.4) + ink_stroke("M23 43H41", 6.4)
    return fit(out, 0.481, 32.0, 30.8)

@reg("me.nathandyer.Kepublicity", TEAL_LIGHT)
def i1358():
    out = rl(14, 3, 36, 58, 6) + rl(19, 8, 26, 38, 2, H) + rl(23, 13, 18, 4, 2) + rl(23, 21, 18, 4, 2) + rl(23, 29, 18, 4, 2) + rl(23, 37, 11, 4, 2) + rl(25, 51, 14, 5, 2.5, H)
    return fit(out, 0.582, 31.8, 32.0)

@reg("me.njean.shootingpactris", GREY_SOFT)
def i1359():
    out = cells([(0, 0), (1, 0), (1, 1), (2, 1)], 13, 15, 6, 4) + path("M16 42L29 36A13 13 0 1 0 29 56Z", I, ' stroke="INK" stroke-width="2" stroke-linejoin="round"')
    out = out.replace("M16 42L29 36A13 13 0 1 0 29 56Z", "M15 51L26.5 44.5A13 13 0 1 0 26.5 57.5Z")
    out += rl(34, 48, 24, 6, 3)
    return fit(out, 0.498, 29.4, 34.4)

@reg("me.sanchezrodriguez.passes", BLUE)
def i1360():
    out = rl(3, 12, 58, 40, 6) + ink_circle(3, 32, 6.4, H) + ink_circle(61, 32, 6.4, H) + SB("M44 15V49", 2.4, H, ' stroke-dasharray="4 3"')
    for x, w in ((11, 3), (17, 2), (22, 4), (29, 2), (34, 3)):
        out += rl(x, 22, w, 20, .8, H)
    return fit(out, 0.528, 32.0, 31.8)

@reg("me.sergiotarxz.Exd", ORANGE)
def i1361():
    out = ink_stroke("M44 8H18V56H44", 6.4) + ink_stroke("M18 32H38", 6.4)
    return fit(out, 0.607, 30.8, 31.8)

@reg("me.sergiotarxz.JapaChar", PURPLE)
def i1362():
    out = ink_stroke("M18 6H46V58H18Z", 5.4) + ink_stroke("M18 32H46", 5.4) 
    return fit(out, 0.577, 32.0, 32.0)

@reg("me.simakis.dropboxignore", BLUE_GREY_SOFT)
def i1363():
    out = path("M4 14Q4 8 10 8H24L30 16H54Q60 16 60 22V50Q60 56 54 56H10Q4 56 4 50Z", I) + ink_circle(32, 38, 20, H) + ring_c(32, 38, 13.5, 4.6) + ink_stroke("M22.5 28.5L41.5 47.5", 4.6)
    return fit(out, 0.53, 31.8, 32.8)

@reg("me.spaceinbox.actioneer", BLUE_GREY_LIGHT)
def i1364():
    out = rl(5, 26, 54, 34, 5) + rot(rl(5, 8, 54, 13, 3) + SB("M17 8L11 21", 3.4, H) + SB("M31 8L25 21", 3.4, H) + SB("M45 8L39 21", 3.4, H), -9, 5, 21) + poly([(26, 36), (26, 52), (40, 44)], H, 2)
    return fit(out, 0.479, 31.2, 30.0)

@reg("me.spaceinbox.swiftynotes", LIGHT_BLUE_DEEP)
def i1365():
    out = dim(rl(16, 3, 44, 44, 5), .55) + rl(1, 12, 52, 52, 8, H) + rl(4, 15, 46, 46, 5) + ink_stroke("M12 28H42", 3.4, H) + ink_stroke("M12 38H42", 3.4, H) + ink_stroke("M12 48H30", 3.4, H)
    return fit(out, 0.464, 30.4, 33.4)

@reg("me.timschneeberger.GalaxyBudsClient", DEEP_ORANGE_DEEP)
def i1366():
    bud = ink_circle(17, 20, 12.5) + rot(rl(12, 26, 10, 32, 5), 10, 17, 26) + ink_circle(16, 18, 4.6, H)
    return fit(bud + g(bud, "translate(64 0) scale(-1 1)"), 0.562, 32.0, 32.4)

@reg("menu.kando.Kando", DEEP_PURPLE_DARK)
def i1367():
    out = ""
    for k, (a0, a1) in enumerate(((-85, -5), (5, 85), (95, 175), (185, 265))):
        w = wedge(32, 32, 11, 29, a0, a1)
        out += dim(w, .5) if k == 2 else w
    return fit(out + ink_circle(32, 32, 5.4), 0.639, 32.0, 32.0)

@reg("mobi.snowball.Snowball", LIGHT_BLUE_SOFT)
def i1368():
    out = asterisk(32, 32, 26, 3.8)
    for a in (90, 150, 210, 270, 330, 30):
        x, y = pt(32, 32, 16, a)
        for d in (-42, 42):
            x1, y1 = pt(x, y, 8.5, a + d)
            out += ink_stroke(f"M{f(x)} {f(y)}L{f(x1)} {f(y1)}", 3.4)
    return fit(out + ink_circle(32, 32, 4.4), 0.666, 32.0, 32.0)

@reg("moe.clover.mm3d", RED_SOFT)
def i1369():
    out = ink_stroke("M32 6L6 54H58Z", 3.4) + ink_stroke("M32 6V36", 3.4) + ink_stroke("M6 54L32 36L58 54", 3.4)
    for x, y in ((32, 6), (6, 54), (58, 54), (32, 36)):
        out += ink_circle(x, y, 5.2)
    return fit(out, 0.456, 31.8, 29.8)

@reg("moe.emmaexe.ntfyDesktop", CYAN)
def i1370():
    out = path("M32 6Q18 6 18 24V34L9 46H55L46 34V24Q46 6 32 6Z", I, ' stroke="INK" stroke-width="2" stroke-linejoin="round"') + path("M24 50Q24 58 32 58Q40 58 40 50Z", I) + ink_circle(32, 5, 3.4)
    return fit(out, 0.638, 31.8, 29.6)

@reg("moe.karaokes.mugen", BROWN)
def i1371():
    return fit(lem(32, 32, 26, 7), 0.631, 32.0, 32.0)

@reg("moe.launcher.an-anime-game-launcher", INDIGO)
def i1372():
    return fit(star4(30, 34, 26) + star4(52, 12, 9) + star4(11, 12, 6), 0.538, 32.6, 31.4)

@reg("moe.launcher.honkers-launcher", YELLOW_LIGHT)
def i1373():
    out = poly([(16, 8), (48, 8), (60, 26), (32, 58), (4, 26)], I, 3) + SB("M4 26H60", 2.6, H) + SB("M20 26L32 8L44 26", 2.6, H) + SB("M20 26L32 58L44 26", 2.6, H)
    return fit(out, 0.585, 32.0, 33.8)

@reg("moe.launcher.sleepy-launcher", PINK_LIGHT)
def i1374():
    out = crescent(26, 34, 24) + ink_stroke("M42 8H54L42 22H54", 4) + ink_stroke("M46 32H54L46 42H54", 3.4)
    return fit(out, 0.508, 28.8, 31.8)

@reg("moe.launcher.the-honkers-railway-launcher", TEAL_DEEP)
def i1375():
    out = rl(9, 4, 46, 44, 11) + rl(15, 10, 34, 18, 4, H) + ink_circle(21, 39, 4, H) + ink_circle(43, 39, 4, H) + rl(28, 37, 8, 4, 2, H) + rl(6, 52, 52, 5, 2.5) + ink_stroke("M20 52L16 62", 3.4) + ink_stroke("M44 52L48 62", 3.4)
    return fit(out, 0.545, 31.8, 33.8)

@reg("moe.nomm.Nomm", GREY_DEEP)
def i1376():
    out = rl(8, 16, 42, 42, 4) + ink_circle(29, 13, 8.4) + ink_circle(52, 37, 8.4) + ink_circle(8, 37, 7, H) + ink_circle(29, 58, 7, H)
    return fit(out, 0.611, 30.6, 34.8)

@reg("moe.sable.client", BLUE_DARK)
def i1377():
    out = rl(4, 6, 56, 40, 10) + poly([(14, 44), (12, 59), (29, 46)], I, 2.4) + rl(13, 17, 36, 5, 2.5, H) + rl(13, 28, 24, 5, 2.5, H)
    return fit(out, 0.538, 31.8, 33.0)

@reg("moe.tsuna.tsukimi", ORANGE_LIGHT)
def i1378():
    out = ink_circle(32, 32, 26) + poly([(26, 20), (26, 44), (46, 32)], H, 2.4) + ink_circle(14, 20, 2.6, H)
    return fit(out, 0.709, 31.8, 31.8)

@reg("moe.tundra.Tundra", PURPLE_SOFT)
def i1379():
    out = poly([(4, 56), (24, 14), (44, 56)], I, 2) + poly([(26, 56), (43, 26), (60, 56)], H, 6) + poly([(26, 56), (43, 26), (60, 56)], I, 2)
    out += poly([(24, 14), (17, 29), (21, 26), (25, 30), (28, 26), (31, 29)], H)
    return fit(out, 0.51, 33.0, 36.0)

@reg("mx.pwmc.Svgvi", ORANGE_DEEP)
def i1380():
    out = ink_stroke("M18 14L5 32L18 50", 5) + ink_stroke("M46 14L59 32L46 50", 5) + ink_stroke("M37 10L27 54", 5)
    return fit(out, 0.636, 32.0, 32.0)

@reg("net._86box._86Box", BLUE_GREY)
def i1381():
    out = rl(14, 14, 36, 36, 5)
    for p in (17, 29, 41):
        out += rl(p, 4, 6, 12, 1.5) + rl(p, 48, 6, 12, 1.5) + rl(4, p, 12, 6, 1.5) + rl(48, p, 12, 6, 1.5)
    out += rl(21, 21, 22, 22, 3, H) + ink_circle(32, 32, 4.4)
    return fit(out, 0.592, 31.8, 31.8)

@reg("net.andyofniall.missingno", LIGHT_BLUE)
def i1382():
    out = rl(6, 5, 40, 9, 1.5) + rl(20, 17, 38, 9, 1.5) + rl(4, 29, 54, 9, 1.5) + rl(14, 41, 34, 9, 1.5) + rl(28, 53, 30, 9, 1.5)
    out += rl(22, 29, 6, 9, 0, H) + rl(41, 29, 5, 9, 0, H)
    return fit(out, 0.482, 30.8, 33.4)

@reg("net.armatik.Kitsune", DEEP_ORANGE_LIGHT)
def i1383():
    out = poly([(32, 58), (4, 30), (6, 4), (24, 18), (40, 18), (58, 4), (60, 30)], I, 3) + ink_stroke("M15 31L25 36", 3.6, H) + ink_stroke("M49 31L39 36", 3.6, H) + ink_circle(32, 51, 3.6, H)
    return fit(out, 0.478, 32.0, 31.0)

@reg("net.atns.MegaMesh", DEEP_PURPLE_LIGHT)
def i1384():
    out = rl(6, 6, 52, 52, 12, "none", ' stroke="INK" stroke-width="3.6"') + ink_stroke("M22 6Q14 32 22 58", 3.4) + ink_stroke("M42 6Q50 32 42 58", 3.4) + ink_stroke("M6 22Q32 14 58 22", 3.4) + ink_stroke("M6 42Q32 50 58 42", 3.4)
    return fit(out, 0.552, 32.0, 32.0)

@reg("net.audiorelay.AudioRelay", BLUE_GREY_LIGHT)
def i1385():
    out = poly([(4, 24), (17, 24), (33, 10), (33, 54), (17, 40), (4, 40)], I, 2.5) + ink_stroke("M43 22Q51 32 43 42", 4.2) + ink_stroke("M50 14Q64 32 50 50", 4.2)
    return fit(out, 0.636, 30.8, 32.0)

@reg("net.base_art.Glide", RED_DEEP)
def i1386():
    out = ell(32, 28, 29, 5.6) + ell(32, 34, 3.6, 24) + ell(32, 55, 10, 3.4)
    return fit(out, 0.629, 32.0, 34.0)

@reg("net.biniou.LeBiniou", CYAN_DARK)
def i1387():
    out = ink_circle(32, 32, 9)
    for k in range(16):
        a = 22.5 * k
        r1 = 15 + (k % 4) * 3.4 + 4
        x0, y0 = pt(32, 32, 15, a)
        x1, y1 = pt(32, 32, r1 + 5, a)
        out += ink_stroke(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", 3.4)
    return fit(out, 0.518, 32.0, 32.0)

@reg("net.blip.Blip", BROWN_LIGHT)
def i1388():
    out = ring_c(32, 32, 26, 4) + ring_c(32, 32, 13, 3.2) + dim(path("M32 32L55 21A26 26 0 0 1 58 32Z".replace("55 21", "50.6 12.1").replace("58 32", "58 32"), I), .55)
    out += ink_stroke("M32 32L50.6 12.1", 3.4) + ink_circle(20, 22, 4.2) + ink_circle(32, 32, 3.4)
    return fit(out, 0.644, 31.8, 31.8)

@reg("net.blockattack.game", INDIGO_SOFT)
def i1389():
    out = rl(4, 4, 26, 26, 4) + rl(34, 4, 26, 26, 4) + rl(4, 34, 26, 26, 4) + rl(34, 34, 26, 26, 4)
    out += ink_circle(17, 17, 7, H) + poly([(47, 9), (54, 17), (47, 25), (40, 17)], H) + poly([(17, 39), (25, 52), (9, 52)], H, 1.4) + rl(41, 41, 12, 12, 2, H)
    return fit(out, 0.487, 31.8, 31.8)

@reg("net.blumia.pineapple-pictures", YELLOW)
def i1390():
    out = ell(32, 41, 17, 21) + poly([(32, 22), (19, 7), (27, 14), (32, 0), (37, 14), (45, 7)], I, 1.6)
    for d in ("M22 29L38 50", "M42 29L26 50", "M18 40L33 58", "M46 40L31 58", "M32 26V38"):
        out += SB(d, 2.4, H)
    return fit(out, 0.593, 32.0, 30.4)

@reg("net.blumia.pineapple-steam-recording-exporter", PINK)
def i1391():
    out = rl(3, 14, 38, 34, 6) + poly([(46, 27), (61, 16), (61, 46), (46, 35)], I, 2) + ink_circle(13, 24, 3.4, H) + rl(10, 52, 28, 5, 2.5)
    return fit(out, 0.524, 32.4, 35.4)

@reg("net.bontal.Catalyst", TEAL)
def i1392():
    out = path("M24 4H40V8H38V24L57 52Q60 58 53 58H11Q4 58 7 52L26 24V8H24Z", I) + path("M17 42H47L53 51Q55 55 51 55H13Q9 55 11 51Z", H) + ink_circle(33, 30, 2.6, H) + ink_circle(38, 36, 2, H)
    return fit(out, 0.514, 32.0, 30.8)

@reg("net.carrotindustries.usbkvm", GREY_LIGHT)
def i1393():
    out = rl(11, 3, 42, 30, 5) + rl(19, 10, 7, 8, 1.5, H) + rl(38, 10, 7, 8, 1.5, H) + rl(24, 33, 16, 8, 2) + ink_stroke("M32 41V58", 6)
    return fit(out, 0.549, 32.0, 32.0)

@reg("net.casimirlab.frigoligo", BLUE_LIGHT)
def i1394():
    out = rl(13, 3, 38, 56, 7) + SB("M13 24H51", 2.8, H) + rl(40, 9, 4, 10, 2, H) + rl(40, 30, 4, 16, 2, H) + rl(17, 59, 8, 3, 1.5) + rl(39, 59, 8, 3, 1.5)
    return fit(out, 0.571, 32.0, 32.4)

@reg("net.charlesschaefer.addictiontracker", ORANGE_DEEP)
def i1395():
    def link(cx, cy):
        return rot(rl(cx - 17, cy - 9, 34, 18, 9, "none", ' stroke="INK" stroke-width="5"'), 45, cx, cy)
    return fit(link(23, 23) + link(41, 41), 0.578, 31.8, 32.0)

@reg("net.christianbeier.MultiVNC", PURPLE_DEEP)
def i1396():
    out = rl(22, 4, 38, 28, 4) + rl(27, 9, 28, 18, 2, H) + rl(0, 20, 46, 34, 7, H) + rl(3, 23, 40, 28, 4) + rl(8, 28, 30, 18, 2, H) + rl(20, 51, 6, 7, 1) + rl(11, 57, 24, 4, 2)
    return fit(out, 0.471, 29.8, 32.4)

@reg("net.clonehero.CloneHero", ORANGE_DARK)
def i1397():
    out = ell(32, 46, 17, 13) + ink_circle(32, 30, 10.5) + rl(29, 2, 6, 30, 2) + rl(26, 0, 12, 9, 2.5) + rl(23, 44, 18, 3.4, 1.7, H) + ink_circle(32, 52, 4.4, H) + rl(23, 33, 18, 3.4, 1.7, H)
    return fit(rot(out, 38, 32, 32), 0.589, 31.6, 31.0)

@reg("net.codelogistics.letters", BLUE_GREY_LIGHT)
def i1398():
    out = rl(3, 11, 58, 42, 6) + ink_stroke("M8 17L32 37L56 17", 4.4, H)
    return fit(out, 0.555, 32.0, 32.0)

@reg("net.codelogistics.webapps", LIGHT_BLUE_SOFT)
def i1399():
    out = rl(3, 6, 58, 52, 7) + rl(9, 12, 46, 6, 3, H) + rl(9, 24, 20, 14, 2.5, H) + rl(35, 24, 20, 14, 2.5, H) + rl(9, 42, 20, 11, 2.5, H) + rl(35, 42, 20, 11, 2.5, H)
    return fit(out, 0.515, 32.0, 31.8)

@reg("net.conceptualspace.prunr", DEEP_ORANGE)
def i1400():
    out = ring_c(18, 48, 9, 4.4) + ring_c(46, 48, 9, 4.4) + ink_stroke("M24 40L46 5", 4.6) + ink_stroke("M40 40L18 5", 4.6) + ink_circle(32, 28.3, 2.8, H)
    return fit(out, 0.557, 31.8, 30.8)
