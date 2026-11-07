# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 96: the eleventh hundred apps from the gap list (flags/app-gap-list-full.md),
rows 1001 to 1100, tvhplayer to QLogExplorer. Each is a simple original mark on its own tile."""
from lm import *
from glyphs.kit import (
    arc_arrow, arrowhead, asterisk, crescent, dim, ell, ellring, fit, H, hexring, hs, I,
    ink_circle, ink_rrect, ink_stroke, lem, pet, petal, registry, ring_c, rot, star4, star5,
    wedge,
)

ICONS, SMALL, reg, _ = registry()

@reg("io.github.mfat.tvhplayer", BLUE_LIGHT)
def i1001():
    out = ink_rrect(6, 18, 52, 36, 8) + ink_rrect(12, 24, 40, 24, 4, H)
    out += poly([(28, 29), (28, 43), (40, 36)], I, 2) + ink_stroke("M24 8L32 17L42 8", 3.8)
    return fit(out + ink_rrect(14, 54, 8, 5, 2) + ink_rrect(42, 54, 8, 5, 2), 0.621, 32.0, 34.3)

@reg("io.github.mhhemati0.WebArchive", YELLOW_DARK)
def i1002():
    out = ink_rrect(6, 8, 52, 14, 4) + ink_rrect(10, 24, 44, 32, 5) + ink_rrect(26, 13, 12, 4, 2, H)
    out += ring_c(32, 40, 10, 3.2, H) + ink_stroke("M32 30V50", 3, H) + ellring(32, 40, 4.5, 10, 3, H) + ink_stroke("M22 40H42", 3, H)
    return fit(out, 0.577, 31.9, 29.7)

@reg("io.github.mhogomchungu.sirikali", RED_DARK)
def i1003():
    out = path("M6 16Q6 10 12 10H24L30 17H52Q58 17 58 23V48Q58 54 52 54H12Q6 54 6 48Z", I)
    out += ink_rrect(23, 34, 18, 14, 3.4, H) + ink_stroke("M27 34V30Q27 24 32 24Q37 24 37 30V34", 3.4, H)
    return fit(out + ink_circle(32, 40, 2.4, I), 0.580, 32.0, 32.2)

@reg("io.github.microgamercz.piki", CYAN)
def i1004():
    out = ell(32, 36, 21, 19) + ink_stroke("M32 18Q30 10 25 8", 3.8) + ink_stroke("M32 18Q35 10 40 9", 3.8)
    out += ink_circle(23, 32, 3.4, H) + ink_circle(41, 32, 3.4, H) + poly([(27, 39), (37, 39), (32, 47)], H, 2)
    return fit(out + ink_stroke("M25 54V59", 3.8) + ink_stroke("M39 54V59", 3.8), 0.652, 31.8, 33.3)

@reg("io.github.mihnea_radulescu.imagefanreloaded", ORANGE_DEEP)
def i1005():
    out = rot(ink_rrect(17, 10, 30, 38, 4), -26, 32, 58) + rot(ink_rrect(17, 10, 30, 38, 4), 26, 32, 58)
    out += ink_rrect(17, 12, 30, 38, 4, I, hs(3))
    return fit(out + poly([(21, 44), (30, 31), (35, 38), (39, 33), (44, 44)], H, 1.8) + ink_circle(37, 22, 3.4, H), 0.559, 32.0, 25.7)

@reg("io.github.mihnea_radulescu.passwordsecure", PURPLE_SOFT)
def i1006():
    out = ink_circle(32, 32, 25) + ring_c(32, 32, 20, 2.8, H)
    return fit(out + ink_circle(32, 27, 6, H) + poly([(28, 30), (36, 30), (40, 47), (24, 47)], H, 2), 0.740, 31.9, 32.0)

@reg("io.github.mihnea_radulescu.quickpdfjoin", INDIGO_SOFT)
def i1007():
    out = rot(ink_rrect(4, 14, 32, 44, 4.4), -9, 20, 36)
    out += ink_stroke("M11 28H27", 3.4, H) + ink_stroke("M11 37H27", 3.4, H) + ink_stroke("M11 46H22", 3.4, H)
    out += rot(ink_rrect(28, 6, 32, 44, 4.4, I, hs(3.4)), 9, 44, 28)
    return fit(out + rot(ink_stroke("M35 20H51", 3.4, H) + ink_stroke("M35 29H51", 3.4, H) + ink_stroke("M35 38H46", 3.4, H), 9, 44, 28), 0.501, 35.0, 32.4)

@reg("io.github.mike632t.x11-calc", BROWN_DARK)
def i1008():
    out = ink_rrect(10, 4, 44, 56, 7) + ink_rrect(15, 9, 34, 13, 3, H)
    for r in range(3):
        for c in range(3):
            out += ink_rrect(15 + c * 12.5, 28 + r * 10, 8.5, 7, 2, H)
    return fit(out, 0.563, 31.7, 31.8)

@reg("io.github.milkshiift.GoofCord", INDIGO_LIGHT)
def i1009():
    out = ink_rrect(5, 7, 54, 40, 15) + poly([(17, 44), (13, 59), (31, 47)], I, 2.6)
    out += ell(22, 25, 3.4, 5.4, H) + ell(41, 24, 4.4, 4.4, H) + ink_stroke("M19 35Q32 44 45 33", 3.6, H)
    return fit(out, 0.577, 31.5, 34.4)

@reg("io.github.mimoguz.TriPeaks-GDX", YELLOW_DARK)
def i1010():
    out = ink_rrect(10, 4, 44, 56, 7) + poly([(32, 16), (43, 32), (32, 48), (21, 32)], H, 2.4)
    out += poly([(19, 12), (23, 17), (19, 22), (15, 17)], H, 1.4) + poly([(45, 42), (49, 47), (45, 52), (41, 47)], H, 1.4)
    return fit(out, 0.563, 31.7, 31.8)

@reg("io.github.mimoguz.tripeaks_neue", BLUE_GREY_SOFT)
def i1011():
    out = poly([(2, 56), (17, 26), (32, 56)], I, 3) + poly([(34, 56), (49, 30), (62, 56)], I, 3)
    out += path("M12 56L32 10L52 56Z", I, hs(3.2))
    out += poly([(26, 24), (32, 14), (38, 24), (35, 27), (32, 23), (29, 27)], H, 1.2)
    return fit(out, 0.542, 32.1, 42.9)

@reg("io.github.mlm_games.asteroids_revenge", LIGHT_BLUE_DEEP)
def i1012():
    out = poly([(12, 20), (26, 8), (42, 12), (54, 24), (56, 40), (44, 54), (28, 58), (14, 48), (6, 34)], I, 5)
    return fit(out + ink_circle(26, 26, 5.4, H) + ink_circle(43, 38, 6.4, H) + ink_circle(24, 45, 3.6, H), 0.662, 31.6, 32.8)

@reg("io.github.mlm_games.cavern-cravers", AMBER_DEEP)
def i1013():
    out = poly([(14, 10), (50, 10), (60, 26), (32, 58), (4, 26)], I, 4)
    return fit(out + ink_stroke("M6 26H58", 3.4, H) + ink_stroke("M24 12L19 26L32 54", 3.2, H) + ink_stroke("M40 12L45 26L32 54", 3.2, H), 0.613, 32.0, 29.8)

@reg("io.github.mlm_games.free-the-bugs", PINK_LIGHT)
def i1014():
    out = ell(32, 38, 13, 17) + ink_circle(32, 17, 7.4) + ink_stroke("M32 25V54", 3.2, H)
    for y, y2 in ((31, 26), (40, 42), (48, 57)):
        out += ink_stroke(f"M21 {y}L8 {y2}", 3.8) + ink_stroke(f"M43 {y}L56 {y2}", 3.8)
    return fit(out + ink_stroke("M29 11L23 4", 3.6) + ink_stroke("M35 11L41 4", 3.6), 0.542, 32.1, 35.2)

@reg("io.github.mlm_games.imagot", TEAL_DEEP)
def i1015():
    out = ink_stroke("M18 4V46H60", 5.4) + ink_stroke("M4 18H46V60", 5.4)
    return fit(out + ink_circle(32, 32, 6.4), 0.544, 32.1, 32.0)

@reg("io.github.mlm_games.mages", DEEP_ORANGE_DEEP)
def i1016():
    out = path("M31 4Q41 6 42 14Q36 14 40 42H17Q26 24 31 4Z", I) + ell(30, 45, 27, 8)
    return fit(out + ink_stroke("M19 38Q30 45 41 39", 3.6, H) + star5(31, 25, 5.4, H), 0.628, 30.0, 33.5)

@reg("io.github.mlm_games.plutonic", DEEP_PURPLE)
def i1017():
    out = rot(path("M4 32A28 9 0 0 1 60 32", "none", f' stroke="{I}" stroke-width="4" stroke-linecap="round"'), -22, 32, 32)
    out += ink_circle(32, 32, 15)
    front = path("M4 32A28 9 0 0 0 60 32", "none", ' stroke="HOLE" stroke-width="9"')
    front2 = path("M4 32A28 9 0 0 0 60 32", "none", f' stroke="{I}" stroke-width="4" stroke-linecap="round"')
    return fit(out + rot(front + front2, -22, 32, 32) + ink_circle(52, 8, 4.2), 0.559, 29.7, 26.7)

@reg("io.github.mlm_games.pomodorot", INDIGO_SOFT)
def i1018():
    out = ell(32, 38, 25, 21) + ink_stroke("M32 20V8", 4.6)
    for a in (15, 65, 115, 165):
        out += petal(32, 24, 14, 4.2, a, H)
    return fit(out, 0.690, 31.9, 32.6)

@reg("io.github.mlm_games.yadaw", GREY)
def i1019():
    out = ink_stroke("M14 6V58", 4) + ink_stroke("M32 6V58", 4) + ink_stroke("M50 6V58", 4)
    for x, y in ((14, 36), (32, 16), (50, 40)):
        out += ink_rrect(x - 8, y, 16, 10, 3.4, I, hs(3))
        out += ink_stroke(f"M{x - 3} {y + 5}H{x + 3}", 2.8, H)
    return fit(out, 0.551, 31.9, 31.8)

@reg("io.github.mmarco94.tambourine", BLUE_DARK)
def i1020():
    out = ink_circle(32, 32, 26) + ink_circle(32, 32, 14, H)
    for k in range(5):
        out += rot(ink_rrect(27.5, 7, 9, 13, 4.5, H) + ink_circle(32, 13.5, 2.6), 72 * k, 32, 32)
    return fit(out, 0.712, 31.9, 31.9)

@reg("io.github.mmp.Vice", YELLOW_DARK)
def i1021():
    out = poly([(16, 8), (48, 8), (60, 40), (4, 40)], I, 5) + ink_rrect(4, 40, 56, 14, 4)
    dash = lambda y, x0, x1, d: path(f"M{x0} {y}H{x1}", "none", f' stroke="{H}" stroke-width="4.4" stroke-dasharray="{d}"')
    return fit(out + dash(17, 21, 43, "5 2.4") + dash(25, 17, 47, "5 2.4") + dash(33, 13, 51, "5 2.4") + ink_stroke("M22 47H42", 3.6, H), 0.564, 32.1, 33.8)

@reg("io.github.monsler.Kalorite", RED_DEEP)
def i1022():
    out = path("M32 3C35 17 52 22 52 40A20 20 0 0 1 12 40C12 32 16 27 21 23C21 29 25 32 28 32C25 22 27 11 32 3Z", I)
    return fit(out + path("M32 34C34 41 41 43 41 49A9 9 0 0 1 23 49C23 45 26 43 29 40C30 38 31 36 32 34Z", H), 0.652, 32.0, 31.7)

@reg("io.github.moonlight_mod.moonlight-installer", CYAN)
def i1023():
    out = crescent(27, 24, 19) + ink_stroke("M46 26V43", 4.8) + poly([(37, 41), (55, 41), (46, 52)], I, 2.4)
    return fit(out + ink_stroke("M35 59H57", 4.8), 0.548, 36.6, 35.4)

@reg("io.github.moooossee.Moose", ORANGE_DARK)
def i1024():
    out = poly([(24, 34), (40, 34), (37, 52), (32, 59), (27, 52)], I, 6)
    for s in (1, -1):
        def X(x):
            return 32 + s * (x - 32)
        out += ink_stroke(f"M{X(24)} 35Q{X(11)} 32 {X(10)} 14", 4.4) + ink_stroke(f"M{X(10)} 14L{X(5)} 5", 3.8)
        out += ink_stroke(f"M{X(13)} 25L{X(4)} 22", 3.8) + ink_stroke(f"M{X(18)} 31L{X(16)} 19", 3.8)
    return fit(out + ink_circle(26, 42, 2, H) + ink_circle(38, 42, 2, H), 0.515, 32.2, 25.6)

@reg("io.github.mpc_qt.mpc-qt", PURPLE_DARK)
def i1025():
    out = ink_rrect(5, 10, 54, 44, 6) + ink_rrect(16, 14, 32, 36, 3, H)
    for y in (15, 25, 35, 44):
        out += ink_rrect(8, y, 5, 6, 1.4, H) + ink_rrect(51, y, 5, 6, 1.4, H)
    return fit(out + poly([(27, 23), (27, 41), (41, 32)], I, 2.4), 0.573, 32.0, 31.9)

@reg("io.github.mrmyhuang.cbetar2", BLUE_DARK)
def i1026():
    out = pet(32, 52, 34, 10, -142) + pet(32, 52, 34, 10, -38) + pet(32, 52, 38, 11, -112) + pet(32, 52, 38, 11, -68)
    out += pet(32, 52, 42, 12, -90, 3)
    return fit(out + ink_stroke("M12 58Q32 64 52 58", 3.8), 0.621, 32.0, 38.6)

@reg("io.github.mrstickypiston.stickyhours", BROWN_DEEP)
def i1027():
    out = path("M6 6H58V38L38 58H6Z", I) + path("M38 58V44Q38 40 42 40H58Z", H)
    return fit(out + ring_c(27, 28, 13, 3.6, H) + ink_stroke("M27 20V28L33 32", 3.6, H), 0.508, 31.8, 32.1)
    return fit(out, 0.515, 31.1, 33.2)

@reg("io.github.msx80.DoorsOfDoomOmicron", YELLOW_DARK)
def i1029():
    out = path("M8 60V28Q8 4 32 4Q56 4 56 28V60Z", I)
    out += path("M18 56V30Q18 14 32 14Q46 14 46 30V56", "none", ' stroke="HOLE" stroke-width="3.4" stroke-linejoin="round"')
    return fit(out + ink_stroke("M32 14V56", 3.4, H) + ink_circle(26, 38, 2.6, H) + ink_circle(38, 38, 2.6, H), 0.559, 31.7, 37.0)

@reg("io.github.msx80.turnsofwar", BLUE_GREY_DARK)
def i1030():
    out = hexring(32, 32, 27, 4.6) + poly([(29, 12), (35, 12), (35, 36), (32, 41), (29, 36)], I, 1.6)
    return fit(out + ink_stroke("M22 38H42", 4.4) + ink_stroke("M32 40V50", 4.6) + ink_circle(32, 51.5, 2.8), 0.631, 31.8, 32.1)

@reg("io.github.mukonqi.nottodbox", LIGHT_BLUE)
def i1031():
    out = ink_rrect(8, 8, 48, 48, 10, "none", f' stroke="{I}" stroke-width="5.6"')
    return fit(out + ink_stroke("M18 46L46 18", 5.6) + ink_stroke("M18 18L28 28", 4.6), 0.567, 32.1, 32.1)

@reg("io.github.muse_sequencer.Muse", AMBER_DARK)
def i1032():
    out = ink_rrect(5, 10, 54, 44, 6)
    for x in (19, 32, 45):
        out += ink_rrect(x - 4.4, 10, 8.8, 24, 2.4, H) + ink_stroke(f"M{x} 34V54", 3, H)
    return fit(out, 0.573, 32.0, 31.9)

@reg("io.github.myst6re.makoureactor", PINK_SOFT)
def i1033():
    out = ink_circle(32, 32, 5.4)
    for a in (-90, 30, 150):
        out += wedge(32, 32, 9, 26, a - 30, a + 30)
    return fit(out, 0.712, 32.0, 31.9)

@reg("io.github.nacho.mecalin", TEAL)
def i1034():
    out = ink_rrect(5, 6, 25, 26, 6.4) + ink_rrect(34, 6, 25, 26, 6.4) + ink_rrect(9, 38, 46, 16, 6.4)
    out += ink_stroke("M11 25L17.5 12L24 25", 3.6, H) + ink_stroke("M13.5 20H21.5", 3.4, H)
    return fit(out + ink_rrect(39, 11, 15, 16, 3.4, H) + ink_stroke("M26 46H38", 3.4, H), 0.576, 31.7, 27.9)

@reg("io.github.nacho.mundi", DEEP_ORANGE)
def i1035():
    out = ring_c(32, 27, 21, 5) + ellring(32, 27, 9, 21, 3.6) + ink_stroke("M11 27H53", 3.6) + ink_stroke("M16 15H48", 3.2) + ink_stroke("M16 39H48", 3.2)
    return fit(out + ink_stroke("M32 48V57", 4.6) + ink_stroke("M20 59H44", 5), 0.613, 32.0, 33.8)

@reg("io.github.naikari.Naikari", DEEP_PURPLE_LIGHT)
def i1036():
    out = ink_rrect(12, 24, 38, 16, 7) + poly([(50, 24), (62, 32), (50, 40)], I, 3)
    out += ink_rrect(2, 20, 14, 8, 2.4) + ink_rrect(2, 36, 14, 8, 2.4) + poly([(22, 24), (30, 8), (40, 24)], I, 2.4)
    return fit(out + ink_circle(40, 32, 3.4, H) + ink_circle(30, 32, 3.4, H) + ink_stroke("M18 32H22", 3, H), 0.588, 31.6, 31.9)

@reg("io.github.namhyung.dwarview", ORANGE_DARK)
def i1037():
    out = ink_rrect(21, 4, 22, 13, 3.4) + ink_rrect(4, 27, 22, 13, 3.4) + ink_rrect(38, 27, 22, 13, 3.4)
    out += ink_rrect(4, 49, 18, 11, 3.4) + ink_rrect(32, 49, 14, 11, 3.4) + ink_rrect(50, 49, 11, 11, 3.4)
    out += ink_stroke("M32 17V22H15V27", 3.4) + ink_stroke("M32 22H49V27", 3.4) + ink_stroke("M13 40V49", 3.4) + ink_stroke("M49 40V45H39V49", 3.4) + ink_stroke("M49 45H55V49", 3.4)
    return fit(out, 0.534, 32.5, 37.6)

@reg("io.github.narunlifescience.AlphaPlot", GREY)
def i1038():
    out = ink_stroke("M8 4V56H60", 4.8) + ink_stroke("M14 44Q22 10 32 32T54 14", 4.4)
    return fit(out + ink_circle(14, 44, 3.8) + ink_circle(54, 14, 3.8), 0.472, 33.7, 29.8)

@reg("io.github.nate_xyz.Conjure", BLUE_DEEP)
def i1039():
    out = ink_stroke("M8 56L38 26", 7) + ink_stroke("M16 48L22 42", 7.8, H) + star4(46, 18, 14)
    return fit(out + star4(15, 17, 6.4) + star4(54, 46, 6.4), 0.541, 29.9, 34.1)

@reg("io.github.nate_xyz.Paleta", YELLOW_DARK)
def i1040():
    out = path("M32 5C16 5 4 16 4 31C4 46 16 59 31 59C38 59 41 55 40 51C39 47 42 44 47 44H51C58 44 61 38 60 31C59 16 47 5 32 5Z", I)
    return fit(out + ink_circle(19, 29, 4.8, H) + ink_circle(32, 18, 4.8, H) + ink_circle(46, 25, 4.8, H) + ink_circle(19, 44, 4.2, H), 0.656, 32.0, 31.2)

@reg("io.github.nate_xyz.Resonance", RED)
def i1041():
    out = ink_stroke("M20 6V26Q20 37 32 37Q44 37 44 26V6", 5.6) + ink_stroke("M32 37V57", 5.6)
    return fit(out + ink_stroke("M10 12Q5 20 10 28", 3.6) + ink_stroke("M54 12Q59 20 54 28", 3.6), 0.619, 31.9, 29.5)

@reg("io.github.nearinfinitybrowser.nearinfinity", CYAN)
def i1042():
    return fit(lem(32, 32, 27, 7), 0.608, 31.8, 32.0)

@reg("io.github.neil_morrison44.pocket-sync", ORANGE_DEEP)
def i1043():
    out = ink_rrect(13, 4, 38, 56, 9) + ink_rrect(18, 9, 28, 22, 3.4, H)
    out += ink_stroke("M23 43H33", 4, H) + ink_stroke("M28 38V48", 4, H) + ink_circle(41, 40, 3.2, H) + ink_circle(45, 47, 3.2, H)
    return fit(out, 0.607, 31.7, 31.8)

@reg("io.github.nelson_lang.Nelson", PURPLE_DEEP)
def i1044():
    out = ink_stroke("M20 6H10V58H20", 5) + ink_stroke("M44 6H54V58H44", 5)
    return fit(out + ink_rrect(21, 15, 9, 11, 2.6) + ink_circle(40, 20.5, 5) + ink_circle(25.5, 43, 5) + ink_rrect(35, 37, 9, 11, 2.6), 0.506, 31.7, 31.8)

@reg("io.github.nest_desktop.nest-desktop", DEEP_PURPLE_LIGHT)
def i1045():
    out = ink_stroke("M27 28L18 16L9 14", 3.8) + ink_stroke("M18 16L16 5", 3.6) + ink_stroke("M37 28L46 16L55 11", 3.8) + ink_stroke("M46 16L51 5", 3.6)
    out += ink_stroke("M24 37L10 40L5 50", 3.8) + ink_stroke("M41 38L57 44", 3.8) + ink_stroke("M32 44V57", 3.8)
    return fit(out + ink_circle(32, 34, 10) + ink_circle(32, 34, 3.6, H) + ink_circle(32, 59, 3.4), 0.544, 28.7, 28.7)

@reg("io.github.nikelaz.CTLDash", BROWN)
def i1046():
    out = ink_stroke("M7 44A25 25 0 0 1 57 44", 6.4) + ink_stroke("M32 44L44 24", 4.8) + ink_circle(32, 44, 5.6)
    return fit(out + ink_stroke("M9 56H55", 4.6), 0.655, 32.1, 44.0)

@reg("io.github.nokse22.Exhibit", INDIGO_DARK)
def i1047():
    def face(p, o):
        d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in p) + "Z"
        return dim(path(d, I, hs(2.6)), o)
    out = face([(32, 6), (54.5, 19), (32, 32), (9.5, 19)], 1)
    out += face([(9.5, 19), (32, 32), (32, 58), (9.5, 45)], .72) + face([(54.5, 19), (54.5, 45), (32, 58), (32, 32)], .48)
    return fit(out, 0.679, 31.8, 31.9)

@reg("io.github.nokse22.asciidraw", YELLOW_DARK)
def i1048():
    out = ink_rrect(6, 18, 36, 38, 5, "none", f' stroke="{I}" stroke-width="4.6" stroke-dasharray="9 6"')
    pen = ink_rrect(41, 4, 11, 32, 2.6, I, hs(3)) + poly([(41, 37), (52, 37), (46.5, 49)], I, 1.6)
    return fit(out + rot(pen, 32, 46, 27) + ink_stroke("M44 55H58", 4.4), 0.501, 34.4, 32.8)

@reg("io.github.nokse22.high-tide", BLUE_GREY_DEEP)
def i1049():
    out = path("M12 40A20 20 0 0 1 52 40Z", I) + ink_stroke("M4 48Q12 41 20 48T36 48T52 48T60 48", 4.6) + ink_stroke("M10 58Q18 52 26 58T42 58T58 58", 4.6)
    return fit(out + ink_stroke("M32 6V12", 4) + ink_stroke("M13 14L17 18", 4) + ink_stroke("M51 14L47 18", 4), 0.548, 33.9, 37.8)

@reg("io.github.nokse22.inspector", LIGHT_BLUE_LIGHT)
def i1050():
    out = ink_rrect(5, 8, 42, 38, 5, "none", f' stroke="{I}" stroke-width="4.4" stroke-dasharray="8 5"')
    cur = path("M30 24V58L39 49L45 61L52 58L46 46H58Z", I, hs(3))
    return fit(out + cur, 0.526, 28.9, 33.2)

@reg("io.github.nokse22.teleprompter", AMBER_DEEP)
def i1051():
    out = ink_rrect(5, 4, 54, 56, 8)
    out += dim(ink_stroke("M23 17H49", 3.8, H), .4) + dim(ink_stroke("M23 27H45", 3.8, H), .7) + ink_stroke("M23 37H50", 3.8, H) + dim(ink_stroke("M23 47H41", 3.8, H), .7)
    return fit(out + poly([(10, 31), (10, 43), (17, 37)], H, 1.4), 0.523, 31.9, 32.0)

@reg("io.github.nokse22.trivia-quiz", PINK_DARK)
def i1052():
    out = ink_circle(32, 28, 26) + poly([(14, 46), (9, 60), (27, 52)], I, 2.6)
    return fit(out + ink_stroke("M23 22Q23 12 32 12Q42 12 42 21Q42 27 35 30Q32 32 32 36", 5.4, H) + ink_circle(32, 44, 3.4, H), 0.554, 27.4, 34.0)

@reg("io.github.nokse22.ultimate-tic-tac-toe", TEAL_LIGHT)
def i1053():
    out = ink_stroke("M24 5V59", 4.6) + ink_stroke("M41 5V59", 4.6) + ink_stroke("M5 23H59", 4.6) + ink_stroke("M5 41H59", 4.6)
    out += ink_stroke("M10 9L19 18", 4) + ink_stroke("M19 9L10 18", 4) + ring_c(32, 32, 5.4, 3.6) + ink_stroke("M46 45L55 54", 4) + ink_stroke("M55 45L46 54", 4)
    return fit(out, 0.548, 32.4, 31.2)

@reg("io.github.noobping.keycord", DEEP_ORANGE_LIGHT)
def i1054():
    out = ring_c(32, 9, 6.4, 3.8)
    for a in (-24, 24):
        out += rot(ring_c(32, 25, 6.4, 4) + ink_stroke("M32 31V56", 4.8) + ink_stroke("M32 45H40", 4.4) + ink_stroke("M32 52H38", 4.4), a, 32, 9)
    return fit(out, 0.607, 32.0, 31.1)

@reg("io.github.noobping.listenmoe", DEEP_PURPLE_SOFT)
def i1055():
    out = ink_stroke("M12 40V30Q12 6 32 6Q52 6 52 30V40", 5.6) + ink_rrect(4, 34, 16, 24, 7) + ink_rrect(44, 34, 16, 24, 7)
    return fit(out + path("M32 56C20 48 25 37 32 44C39 37 44 48 32 56Z", I), 0.566, 32.2, 36.0)

@reg("io.github.nostar.DroidStar", INDIGO_SOFT)
def i1056():
    out = ink_stroke("M32 16L17 58", 4.6) + ink_stroke("M32 16L47 58", 4.6) + ink_stroke("M24 38H40", 4) + ink_stroke("M20 49H44", 4) + ink_circle(32, 13, 4.8)
    return fit(out + ink_stroke("M20 6Q13 13 20 20", 3.8) + ink_stroke("M44 6Q51 13 44 20", 3.8) + ink_stroke("M14 1Q3 13 14 25", 3.6) + ink_stroke("M50 1Q61 13 50 25", 3.6), 0.529, 32.1, 28.7)

@reg("io.github.noxworld_dev.OpenNox", GREY)
def i1057():
    return fit(ring_c(32, 32, 25, 4.6) + poly([(37, 14), (21, 35), (31, 35), (27, 50), (44, 28), (34, 28)], I, 2.4), 0.678, 32.0, 31.9)

@reg("io.github.nuttyartist.notes", BLUE)
def i1058():
    out = ink_rrect(14, 6, 42, 52, 6) + ink_stroke("M29 22H46", 3.6, H) + ink_stroke("M29 32H46", 3.6, H) + ink_stroke("M29 42H40", 3.6, H)
    for y in (12, 24, 36, 48):
        out += ink_rrect(8, y, 14, 5.6, 2.8, I, hs(2.4))
    return fit(out, 0.570, 32.3, 32.1)

@reg("io.github.nyre221.kiview", YELLOW_DARK)
def i1059():
    out = path("M12 4H40L54 18V60H12Z", I) + path("M40 4V14Q40 18 44 18H54Z", H)
    return fit(out + poly([(18, 52), (28, 36), (34, 45), (39, 39), (48, 52)], H, 1.8) + ink_circle(26, 24, 3.6, H), 0.531, 33.1, 32.2)

@reg("io.github.obiwankennedy.HotShots", RED_LIGHT)
def i1060():
    out = ring_c(32, 32, 25, 4.6)
    for k in range(6):
        a, b = pt(32, 32, 25, 60 * k - 80), pt(32, 32, 9, 60 * k - 20)
        out += ink_stroke(f"M{f(a[0])} {f(a[1])}L{f(b[0])} {f(b[1])}", 4)
    return fit(out, 0.678, 32.0, 31.9)

@reg("io.github.olaproeis.Ferrite", CYAN)
def i1061():
    d = "M17 6V34Q17 54 32 54Q47 54 47 34V6"
    out = path(d, "none", f' stroke="{I}" stroke-width="11" stroke-linejoin="round"')
    return fit(out + line(10, 17, 24, 17, H, 3.4, "butt") + line(40, 17, 54, 17, H, 3.4, "butt"), 0.607, 32.1, 29.0)

@reg("io.github.onionware_github.onionmedia", ORANGE_DARK)
def i1062():
    out = ell(32, 40, 23, 19) + poly([(22, 26), (42, 26), (35, 9), (29, 9)], I, 4) + ink_stroke("M32 11Q36 4 45 3", 4)
    return fit(out + ink_stroke("M32 24C22 32 22 48 32 58", 3.4, H) + ink_stroke("M32 24C42 32 42 48 32 58", 3.4, H), 0.608, 34.2, 29.1)

@reg("io.github.openhv.OpenHV", PURPLE)
def i1063():
    out = ink_rrect(4, 38, 56, 20, 10) + ink_circle(17, 48, 4, H) + ink_circle(32, 48, 4, H) + ink_circle(47, 48, 4, H)
    out += ink_rrect(11, 25, 42, 16, 5, I, hs(3)) + ink_rrect(21, 11, 22, 16, 5, I, hs(3))
    return fit(out + ink_rrect(40, 15, 22, 6, 3), 0.554, 33.5, 35.1)

@reg("io.github.openlf2.OpenLF2", AMBER_DEEP)
def i1064():
    out = ink_circle(29, 24, 21) + ink_rrect(13, 40, 30, 20, 4) + ell(49, 31, 9, 7)
    out += ink_stroke("M13 46H43", 3.4, H) + ink_stroke("M42 20Q50 26 44 36", 3.4, H) + ink_stroke("M18 16Q22 12 28 12", 3.4, H)
    return fit(rot(out, -22, 30, 36), 0.622, 27.2, 33.7)

@reg("io.github.opennumismat.open-numismat", BROWN_LIGHT)
def i1065():
    return fit(ink_circle(32, 32, 26) + ring_c(32, 32, 20, 3.2, H) + star5(32, 33, 12, H), 0.712, 31.9, 31.9)

@reg("io.github.orontee.Argos", INDIGO_DEEP)
def i1066():
    out = path("M3 32Q32 4 61 32Q32 60 3 32Z", I) + ink_circle(32, 32, 13, H) + ink_circle(32, 32, 6.6)
    return fit(out + ink_circle(28, 28, 2.4, H), 0.642, 31.8, 31.9)

@reg("io.github.ostapkonst.HashVerifier", YELLOW_DARK)
def i1067():
    return fit(path("M32 3L55 12V30C55 45 45 55 32 61C19 55 9 45 9 30V12Z", I) + ink_stroke("M27 20L24 44M39 20L36 44M19 29H44M18 37H43", 4.4, H), 0.623, 32.2, 30.9)

@reg("io.github.otaxhu.MQTTy", BLUE_GREY)
def i1068():
    out = ink_stroke("M32 34V12", 3.8) + ink_stroke("M32 34L11 50", 3.8) + ink_stroke("M32 34L53 50", 3.8)
    out += ink_circle(32, 34, 9) + ink_circle(32, 34, 3.4, H) + ink_circle(32, 9, 6.4) + ink_circle(8, 52, 6.4) + ink_circle(56, 52, 6.4)
    return fit(out, 0.536, 32.0, 37.1)

@reg("io.github.pantheon_tweaks.pantheon-tweaks", LIGHT_BLUE_DARK)
def i1069():
    out = poly([(3, 24), (32, 5), (61, 24)], I, 3.4) + ink_rrect(8, 27, 48, 6, 2)
    for x in (10, 22.5, 35, 47.5):
        out += ink_rrect(x, 36, 7, 17, 2.4)
    return fit(out + ink_rrect(4, 55, 56, 6, 2.4) + ink_circle(32, 19, 3.4, H), 0.532, 32.0, 38.4)

@reg("io.github.paulwedeck.settlers-remake", AMBER_DARK)
def i1070():
    out = ink_rrect(10, 28, 44, 30, 3) + ink_rrect(42, 8, 8, 16, 2) + path("M3 33L32 8L61 33Z", I, hs(3.4))
    return fit(out + path("M26 58V47Q26 41 32 41Q38 41 38 47V58Z", H) + ink_rrect(14, 38, 8, 8, 2, H) + ink_rrect(42, 38, 8, 8, 2, H), 0.600, 32.0, 34.2)

@reg("io.github.pd_l2ork.Pd_L2Ork", PINK_DEEP)
def i1071():
    out = path("M5 5H58L51 14L58 23H5Z", I) + ink_rrect(18, 40, 40, 18, 3.4)
    return fit(out + ink_stroke("M13 23V32H30V40", 3.6) + ink_rrect(9, 11, 8, 6, 1.6, H) + ink_rrect(24, 47, 28, 4, 2, H), 0.506, 31.6, 30.4)

@reg("io.github.pejuko.follamac", TEAL_SOFT)
def i1072():
    out = path("M24 60C25 44 27 34 29 25L44 26C43 36 44 48 47 60Z", I) + ell(37, 18, 11, 12)
    out += rot(ell(30, 6, 3.4, 8), -12, 30, 6) + rot(ell(43, 6, 3.4, 8), 12, 43, 6)
    out += ell(46, 24, 8, 6) + ink_circle(40, 15, 2.6, H) + ink_circle(50, 24, 1.8, H)
    return fit(out + ink_stroke("M27 40Q35 44 45 40", 3, H), 0.569, 35.5, 29.2)

@reg("io.github.pemsley.Alexandria", DEEP_ORANGE_DARK)
def i1073():
    out = poly([(23, 59), (41, 59), (37, 26), (27, 26)], I, 2.8) + ink_rrect(24, 13, 16, 13, 2.6) + poly([(22, 13), (32, 3), (42, 13)], I, 2.6)
    out += ink_rrect(29, 16, 6, 6, 1.6, H) + ink_stroke("M26 40H38", 3.6, H) + ink_rrect(17, 57, 30, 5, 2)
    return fit(out + ink_stroke("M3 12L17 16", 3.6) + ink_stroke("M3 24L17 20", 3.6) + ink_stroke("M61 12L47 16", 3.6) + ink_stroke("M61 24L47 20", 3.6), 0.523, 32.1, 29.0)

@reg("io.github.pemsley.coot", DEEP_PURPLE_DARK)
def i1074():
    out = ink_stroke("M23 28L12 14", 4.6) + ink_stroke("M38 28L50 20", 4.6) + ink_stroke("M37 42L46 52", 4.6) + ink_stroke("M22 41L14 50", 4.6)
    out += ink_circle(30, 34, 11) + ink_circle(30, 34, 4.4, H) + ink_circle(10, 12, 6.6) + ink_circle(54, 17, 5.4) + ink_circle(49, 56, 7) + ink_circle(11, 54, 4.4)
    return fit(out, 0.511, 29.5, 33.9)

@reg("io.github.petitlapin.Li-ri", INDIGO_LIGHT)
def i1075():
    a = ink_rrect(6, 22, 34, 20, 10, "none", f' stroke="{I}" stroke-width="5.4"')
    b = ink_rrect(22, 22, 34, 20, 10, "none", f' stroke="{H}" stroke-width="10"') + ink_rrect(22, 22, 34, 20, 10, "none", f' stroke="{I}" stroke-width="5.4"')
    return fit(rot(a + b, -40, 31, 32) + rot(path("M6 32A10 10 0 0 1 16 22H24", "none", f' stroke="{I}" stroke-width="5.4" stroke-linecap="round"'), -40, 31, 32), 0.641, 31.7, 31.4)

@reg("io.github.phase1geo.textshine", GREY)
def i1076():
    out = ink_rrect(4, 9, 42, 11, 3.4) + ink_rrect(19.5, 9, 11.5, 44, 3.4)
    return fit(out + star4(47, 40, 14) + star4(53, 11, 6.4), 0.581, 32.7, 25.8)

@reg("io.github.phastmike.tags", BLUE_LIGHT)
def i1077():
    out = poly([(8, 10), (28, 10), (57, 39), (39, 57), (10, 28)], I, 5) + ink_circle(21, 23, 4.6, H)
    return fit(out + ink_stroke("M36 5H48L62 19", 3.8), 0.569, 32.4, 27.6)

@reg("io.github.philipk.boilr", YELLOW_DARK)
def i1078():
    out = path("M9 28H55V45Q55 57 43 57H21Q9 57 9 45Z", I) + ink_rrect(6, 21, 52, 8, 4) + ink_rrect(27, 14, 10, 8, 3)
    out += ink_rrect(1, 33, 9, 6, 3) + ink_rrect(54, 33, 9, 6, 3) + ink_stroke("M9 42H55", 3.4, H)
    return fit(out + ink_stroke("M20 14Q15 10 20 6Q24 2 20 -1", 3.4) + ink_stroke("M44 14Q49 10 44 6Q40 2 44 -1", 3.4), 0.563, 31.9, 27.8)

@reg("io.github.philippkosarev.bmi", RED_SOFT)
def i1079():
    out = ink_circle(22, 11, 7) + ink_rrect(8, 22, 28, 22, 9) + ink_rrect(9, 42, 11, 18, 5) + ink_rrect(24, 42, 11, 18, 5)
    return fit(out + ink_stroke("M50 10V54", 3.6) + arrowhead(50, 12, 0, -1, 7) + arrowhead(50, 52, 0, 1, 7), 0.553, 31.1, 32.0)

@reg("io.github.picocrypt.Picocrypt", CYAN)
def i1080():
    out = ink_rrect(10, 28, 44, 32, 8) + ink_stroke("M19 28V20Q19 7 32 7Q45 7 45 20V28", 6)
    return fit(out + ink_circle(32, 40, 4.8, H) + ink_stroke("M32 43V51", 4, H), 0.610, 32.0, 34.4)

@reg("io.github.picocrypt_ng.Picocrypt-NG", ORANGE_DEEP)
def i1081():
    out = ink_rrect(8, 30, 38, 29, 8) + ink_stroke("M17 30V21Q17 8 29 8Q41 8 41 17", 6)
    return fit(out + ink_circle(27, 41, 4.6, H) + ink_stroke("M27 44V51", 4, H) + star4(53, 38, 10) + star4(55, 15, 5), 0.570, 35.0, 35.0)

@reg("io.github.pieterdd.RcloneShuttle", PURPLE_LIGHT)
def i1082():
    out = ink_circle(19, 38, 12) + ink_circle(34, 27, 16) + ink_circle(48, 38, 12) + ink_rrect(8, 38, 52, 18, 9)
    out += ink_stroke("M19 36H42", 3.8, H) + poly([(40, 30), (40, 42), (49, 36)], H, 1.8)
    return fit(out + ink_stroke("M27 47H50", 3.8, H) + poly([(29, 41), (29, 53), (20, 47)], H, 1.8), 0.667, 33.9, 38.8)

@reg("io.github.pieterdd.StretchBreak", INDIGO_SOFT)
def i1083():
    out = ink_circle(32, 11, 6.6) + ink_stroke("M32 21V40", 5.4) + ink_stroke("M32 27L15 9", 5.4) + ink_stroke("M32 27L49 9", 5.4)
    return fit(out + ink_stroke("M32 40L19 59", 5.4) + ink_stroke("M32 40L45 59", 5.4) + ink_stroke("M8 28Q5 36 8 44", 3.4) + ink_stroke("M56 28Q59 36 56 44", 3.4), 0.582, 32.1, 32.8)

@reg("io.github.piotrek_k._2dTaskBoard", BROWN_SOFT)
def i1084():
    out = ink_rrect(4, 6, 17, 52, 4.4) + ink_rrect(23.5, 6, 17, 52, 4.4) + ink_rrect(43, 6, 17, 52, 4.4)
    out += ink_rrect(7, 11, 11, 11, 2.4, H) + ink_rrect(7, 26, 11, 8, 2.4, H)
    out += ink_rrect(26.5, 11, 11, 17, 2.4, H) + ink_rrect(26.5, 32, 11, 8, 2.4, H) + ink_rrect(26.5, 44, 11, 8, 2.4, H)
    return fit(out + ink_rrect(46, 11, 11, 8, 2.4, H) + ink_rrect(46, 23, 11, 12, 2.4, H), 0.510, 32.1, 31.9)

@reg("io.github.pleromix.IceBox", INDIGO)
def i1085():
    out = ink_rrect(5, 25, 54, 34, 6) + ink_rrect(3, 15, 58, 11, 4.4, I, hs(3)) + ink_stroke("M19 15V9Q19 4 24 4H40Q45 4 45 9V15", 4)
    return fit(out + asterisk(32, 42, 11, 3.8, H), 0.540, 31.9, 33.8)

@reg("io.github.plrigaux.sysd-manager", YELLOW_DARK)
def i1086():
    out = ink_circle(32, 32, 19)
    for k in range(8):
        out += rot(ink_rrect(27, 4, 10, 13, 2.8), 45 * k, 32, 32)
    return fit(out + ink_circle(32, 32, 11, H) + poly([(29, 26), (29, 38), (39, 32)], I, 1.8), 0.660, 31.9, 32.0)

@reg("io.github.polypixeldev.Polypass", BLUE_GREY_LIGHT)
def i1087():
    out = ink_rrect(5, 6, 54, 48, 7) + ink_rrect(11, 12, 42, 36, 4, H) + ring_c(29, 30, 9, 4) + ink_stroke("M29 30V23", 3.4)
    out += ink_stroke("M45 24V36", 4) + ink_rrect(12, 54, 10, 6, 2) + ink_rrect(42, 54, 10, 6, 2)
    return fit(out, 0.544, 31.7, 31.3)

@reg("io.github.pr_starfighter.starfighter", LIGHT_BLUE_DEEP)
def i1088():
    out = poly([(32, 3), (40, 28), (61, 48), (61, 56), (44, 49), (38, 59), (26, 59), (20, 49), (3, 56), (3, 48), (24, 28)], I, 3)
    return fit(out + ell(32, 31, 3.6, 8, H) + ink_stroke("M32 46V54", 3.4, H), 0.518, 32.0, 37.4)

@reg("io.github.prateekmedia.pstube", AMBER_DEEP)
def i1089():
    out = ink_rrect(3, 12, 58, 40, 13) + poly([(25, 22), (25, 42), (42, 32)], H, 2.8)
    return fit(out, 0.606, 31.8, 31.8)

@reg("io.github.ptitSeb.hydracastlelabyrinth", PINK)
def i1090():
    out = ink_rrect(10, 30, 44, 30, 2) + ink_rrect(5, 14, 16, 46, 2) + ink_rrect(43, 14, 16, 46, 2)
    for x in (5, 12, 18):
        out += ink_rrect(x, 7, 4.4, 9, 1.2) + ink_rrect(x + 38, 7, 4.4, 9, 1.2)
    out += ink_rrect(26, 22, 5, 9, 1.2) + ink_rrect(34, 22, 5, 9, 1.2)
    return fit(out + path("M25 60V47Q25 39 32 39Q39 39 39 47V60Z", H) + ink_rrect(10, 24, 5, 9, 2.4, H) + ink_rrect(49, 24, 5, 9, 2.4, H), 0.494, 32.5, 33.2)

@reg("io.github.pyfa_org.Pyfa", TEAL_DARK)
def i1091():
    out = ring_c(32, 32, 17, 4.4) + ink_stroke("M32 3V16", 4.4) + ink_stroke("M32 48V61", 4.4) + ink_stroke("M3 32H16", 4.4) + ink_stroke("M48 32H61", 4.4)
    return fit(out + poly([(32, 24), (40, 32), (32, 40), (24, 32)], I, 1.8), 0.597, 32.0, 31.9)

@reg("io.github.q962.ClipboardServer", DEEP_ORANGE_DEEP)
def i1092():
    out = ink_rrect(8, 8, 48, 52, 7) + ink_rrect(21, 3, 22, 11, 4, I, hs(3))
    out += ink_rrect(15, 22, 34, 12, 3.4, H) + ink_rrect(15, 38, 34, 12, 3.4, H)
    return fit(out + ink_circle(21, 28, 2.4) + ink_circle(21, 44, 2.4) + ink_stroke("M28 28H43", 3.2) + ink_stroke("M28 44H43", 3.2), 0.563, 32.2, 33.5)

@reg("io.github.q962.PictureWindow", DEEP_PURPLE_DEEP)
def i1093():
    out = ink_rrect(3, 6, 58, 52, 8) + ink_stroke("M3 22H61", 3, H) + ink_circle(10, 14, 2.4, H) + ink_circle(18, 14, 2.4, H)
    out += ink_rrect(9, 28, 46, 24, 3.4, H) + poly([(13, 48), (24, 35), (31, 43), (37, 37), (51, 48)], I, 2.4)
    return fit(out + ink_circle(44, 34, 3, I), 0.518, 31.8, 31.7)

@reg("io.github.qcanvas.QCanvasApp", ORANGE_DEEP)
def i1094():
    out = ink_rrect(8, 5, 48, 32, 4.4) + ink_stroke("M16 28Q25 12 33 24T49 14", 3.8, H) + ink_rrect(14, 37, 36, 4.6, 2.3)
    return fit(out + ink_stroke("M32 41V56", 4.4) + ink_stroke("M24 41L14 60", 4.4) + ink_stroke("M40 41L50 60", 4.4), 0.532, 32.1, 32.6)

@reg("io.github.qier222.YesPlayMusic", GREY)
def i1095():
    out = ink_circle(30, 33, 25) + ring_c(30, 33, 19, 2.8, H) + ring_c(30, 33, 14, 2.4, H) + ink_circle(30, 33, 8, H) + ink_circle(30, 33, 2.6)
    arm = ink_stroke("M57 4L45 22", 8, H) + ink_stroke("M57 4L45 22", 4) + ink_circle(58, 4, 4.4)
    return fit(out + arm, 0.531, 36.5, 25.4)

@reg("io.github.quantum_mutnauq.fast_reader_gtk", BLUE_DARK)
def i1096():
    out = ink_rrect(9, 3, 42, 58, 7) + ink_stroke("M19 21L27 29L19 37", 4.6, H) + ink_stroke("M32 21L40 29L32 37", 4.6, H)
    return fit(out + ink_stroke("M19 49H38", 3.8, H) + poly([(41, 3), (49, 3), (49, 15), (45, 11), (41, 15)], H, 0.8), 0.544, 30.9, 31.1)

@reg("io.github.quantum_mutnauq.pictures_converter_gtk", YELLOW_DARK)
def i1097():
    out = ink_rrect(17, 17, 30, 30, 4.4) + poly([(21, 42), (28, 32), (33, 38), (37, 34), (43, 42)], H, 1.8) + ink_circle(39, 25, 3, H)
    return fit(out + arc_arrow(32, 32, 27, -155, -25, 4.6, 7) + arc_arrow(32, 32, 27, 25, 155, 4.6, 7), 0.545, 32.1, 31.8)

@reg("io.github.quotient_im.Quaternion", RED_DARK)
def i1098():
    out = dim(ellring(32, 34, 27, 11, 3), .55) + ink_stroke("M32 34V10", 4.4) + arrowhead(32, 16, 0, -1, 7)
    out += ink_stroke("M32 34L12 46", 4.4) + arrowhead(16, 43.7, -.866, .5, 7) + ink_stroke("M32 34L52 46", 4.4) + arrowhead(48, 43.7, .866, .5, 7)
    return fit(out + ink_circle(32, 34, 4.4), 0.652, 32.0, 33.9)

@reg("io.github.ra3xdh.qucs_s", CYAN)
def i1099():
    out = ring_c(8, 20, 4, 3.4) + ink_stroke("M12 20H16L20 8L28 32L36 8L44 32L48 20H54V40", 4)
    return fit(out + ink_stroke("M44 41H64", 4.2) + ink_stroke("M48 48H60", 4.2) + ink_stroke("M52 55H56", 4.2), 0.545, 33.3, 32.7)

@reg("io.github.rafaelfassi.QLogExplorer", ORANGE_DARK)
def i1100():
    out = ""
    for y, e in ((8, 58), (22, 50), (36, 56)):
        out += ink_rrect(4, y, 11, 8, 2.4) + ink_stroke(f"M21 {y + 4}H{e}", 4.2)
    out += ink_circle(42, 44, 16, H) + ring_c(42, 44, 11.5, 4.6) + ink_stroke("M51 53L60 62", 5.6)
    return fit(out, 0.464, 33.2, 36.0)
