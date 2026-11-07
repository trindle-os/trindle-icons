# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 98: the thirteenth hundred apps from the gap list (flags/app-gap-list-full.md),
rows 1201 to 1300, Wattage to navigator. Each is a simple original mark on its own tile."""
from lm import *
from glyphs.kit import (
    arc_arrow, arrowhead, asterisk, bubble, cells, crescent, dim, ell, ellring, fit, gear_o, H,
    hexring, hs, hx, I, ink_circle, ink_rrect, ink_stroke, pet, registry, ring_c, rot, star4,
    star5, wedge,
)

ICONS, SMALL, reg, _ = registry()

@reg("io.github.v81d.Wattage", AMBER)
def i1201():
    out = poly([(38, 4), (14, 36), (29, 36), (24, 60), (50, 26), (34, 26)], I, 2.4)
    return fit(out, 0.615, 31.8, 31.8)

@reg("io.github.vallabhvidy.CubeTimer", BLUE)
def i1202():
    out = hx(32, 32, 26) + ink_stroke("M32 32V58", 3, H) + ink_stroke("M32 32L9.5 19", 3, H) + ink_stroke("M32 32L54.5 19", 3, H)
    return fit(out, 0.674, 32.0, 32.0)

@reg("io.github.vani_tty1.memerist", PINK_LIGHT)
def i1203():
    out = ink_rrect(6, 6, 52, 52, 8) + ink_rrect(11, 11, 42, 10, 3, H) + ink_rrect(11, 43, 42, 10, 3, H)
    out += ink_circle(32, 32, 7) + ink_circle(29.5, 30.5, 1.4, H) + ink_circle(34.5, 30.5, 1.4, H)
    return fit(out, 0.553, 31.8, 31.8)

@reg("io.github.victoralvesf.aonsoku", DEEP_PURPLE)
def i1204():
    out = ink_stroke("M26 46V14L50 8V40", 4.6) + ink_rrect(24, 11, 28, 8, 2.5) + ell(19, 46, 9, 7) + ell(43, 40, 9, 7)
    return fit(out, 0.602, 31.0, 29.4)

@reg("io.github.vikdevelop.SaveDesktop", CYAN)
def i1205():
    out = ink_rrect(5, 8, 54, 38, 6) + ink_rrect(10, 13, 44, 28, 2, H) + ink_stroke("M32 17V33", 4.4) + ink_stroke("M24 26L32 34L40 26", 4.4) + ink_stroke("M32 46V54", 4.4) + ink_stroke("M20 56H44", 4.4)
    return fit(out, 0.54, 32.0, 33.0)

@reg("io.github.vinser.burnfix", RED_DEEP)
def i1206():
    out = ink_circle(32, 32, 26) + ink_circle(32, 32, 7, H) + ring_c(32, 32, 16, 2.4, H)
    out += rot(ink_rrect(-2, 24, 68, 16, 7, I, hs(3)) + ink_stroke("M26 32H38", 3, H), -40, 32, 32)
    return fit(out, 0.523, 32.0, 32.0)

@reg("io.github.vinser.pixyne", CYAN_LIGHT)
def i1207():
    pts = [(1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3)]
    return fit(cells(pts, 12, 14, 4, 4), 0.633, 30.8, 30.8)

@reg("io.github.vireshwali.Bing-r", TEAL)
def i1208():
    out = ink_stroke("M18 6V58", 6.4) + ink_stroke("M18 30Q18 24 32 24Q50 24 50 41Q50 58 32 58Q18 58 18 52", 6.4) + ink_circle(52, 10, 5)
    return fit(out, 0.535, 35.8, 31.8)

@reg("io.github.vmkspv.lenspect", DEEP_PURPLE_SOFT)
def i1209():
    out = ring_c(32, 32, 24, 4.4) + hexring(32, 32, 12, 4) + ink_circle(32, 32, 3.4)
    return fit(out, 0.707, 32.0, 32.0)

@reg("io.github.vmkspv.netsleuth", RED_LIGHT)
def i1210():
    out = ink_stroke("M12 14L36 10", 3.4) + ink_stroke("M12 14L16 40", 3.4) + ink_stroke("M36 10L16 40", 3.4)
    out += ink_circle(12, 14, 6) + ink_circle(36, 10, 6) + ink_circle(16, 40, 6) + ring_c(42, 40, 10, 4.4) + ink_stroke("M49 47L58 56", 5.4)
    return fit(out, 0.494, 33.2, 31.2)

@reg("io.github.voidforce.qsprawl", YELLOW_DARK)
def i1211():
    out = ink_rrect(5, 5, 32, 54, 5) + ink_rrect(41, 5, 18, 24, 4) + ink_rrect(41, 33, 18, 12, 3) + ink_rrect(41, 49, 18, 10, 3)
    return fit(out, 0.506, 32.0, 32.0)

@reg("io.github.voxelcubes.deepqt", INDIGO_DEEP)
def i1212():
    L = [[(10, 18), (10, 46)], [(32, 10), (32, 32), (32, 54)], [(54, 24), (54, 40)]]
    out = ""
    for a, b in zip(L, L[1:]):
        for p in a:
            for q in b:
                out += ink_stroke(f"M{p[0]} {p[1]}L{q[0]} {q[1]}", 2.2)
    for col in L:
        for p in col:
            out += ink_circle(p[0], p[1], 6.2)
    return fit(out, 0.576, 32.0, 32.0)

@reg("io.github.voxelcubes.hand-tex", DEEP_ORANGE_LIGHT)
def i1213():
    out = ink_stroke("M46 10H17L34 32L17 54H47", 6) + ink_stroke("M8 62Q16 56 24 61T40 61", 3)
    return fit(out, 0.539, 28.2, 36.0)

@reg("io.github.voxelcubes.panelcleaner", BLUE_LIGHT)
def i1214():
    out = ink_rrect(4, 5, 56, 28, 4) + ink_rrect(4, 37, 26, 22, 4) + ink_rrect(34, 37, 26, 22, 4) + star4(46, 18, 8, H) + star4(17, 48, 6, H)
    return fit(out, 0.5, 31.8, 32.0)

@reg("io.github.wanglin2.mind-map", BLUE_GREY)
def i1215():
    out = ""
    for x, y in ((10, 12), (54, 12), (10, 52), (54, 52)):
        out += ink_stroke(f"M32 32Q{(x + 32) / 2 + (6 if y < 30 else -6)} {(y + 32) / 2} {x} {y}", 3.4)
    for x, y in ((10, 12), (54, 12), (10, 52), (54, 52)):
        out += ink_rrect(x - 8, y - 5, 16, 10, 4)
    return fit(out + ink_circle(32, 32, 10), 0.497, 31.8, 32.0)

@reg("io.github.wartybix.Constrict", AMBER_SOFT)
def i1216():
    out = ink_rrect(26, 6, 12, 52, 3) + poly([(4, 18), (22, 32), (4, 46)], I, 2.4) + poly([(60, 18), (42, 32), (60, 46)], I, 2.4)
    return fit(out, 0.57, 31.8, 31.8)

@reg("io.github.waylyrics.Waylyrics", YELLOW_DARK)
def i1217():
    out = ink_stroke("M20 38V12L30 9", 4) + ell(14, 40, 7, 5.4) + ink_rrect(28, 22, 30, 5, 2.5) + ink_rrect(8, 52, 50, 5, 2.5) + ink_rrect(8, 44, 38, 5, 2.5) + ink_rrect(34, 33, 24, 5, 2.5)
    return fit(out, 0.539, 32.4, 32.0)

@reg("io.github.wazzaps.Fingerpaint", BLUE_GREY_LIGHT)
def i1218():
    out = ink_stroke("M12 52V30Q12 8 32 8Q52 8 52 30V40", 4) + ink_stroke("M20 56V30Q20 16 32 16Q44 16 44 30V50", 4) + ink_stroke("M28 58V32Q28 24 32 24Q36 24 36 32V42Q36 50 40 54", 4)
    return fit(out, 0.629, 31.8, 32.8)

@reg("io.github.wdaniau.fstl", DEEP_ORANGE_DEEP)
def i1219():
    out = hexring(32, 32, 26, 4.4) + ink_stroke("M32 32V58", 4.4) + ink_stroke("M32 32L9.5 19", 4.4) + ink_stroke("M32 32L54.5 19", 4.4) + hx(32, 32, 7)
    return fit(out, 0.657, 31.8, 32.0)

@reg("io.github.weclaw1.ScoreTracker", PINK)
def i1220():
    out = ink_rrect(4, 34, 16, 24, 3) + ink_rrect(24, 22, 16, 36, 3) + ink_rrect(44, 42, 16, 16, 3) + star5(32, 9, 9)
    return fit(out, 0.473, 31.8, 28.6)

@reg("io.github.weiteck.Lyricade", LIGHT_BLUE_SOFT)
def i1221():
    out = ink_circle(32, 14, 8) + ink_stroke("M32 20V40", 5.4) + ink_rrect(6, 40, 52, 16, 6) + ink_circle(18, 48, 3, H) + ink_circle(46, 48, 3, H) + ink_rrect(26, 45, 12, 6, 2, H)
    return fit(out, 0.55, 31.8, 30.8)

@reg("io.github.wesenseged.Amharic-bible", DEEP_PURPLE_DEEP)
def i1222():
    out = ink_rrect(10, 4, 44, 56, 6) + ink_rrect(10, 4, 8, 56, 4, H) + ink_stroke("M36 16V42", 5, H) + ink_stroke("M26 25H46", 5, H)
    return fit(out, 0.549, 31.8, 31.8)

@reg("io.github.wesenseged.Pagume", ORANGE_LIGHT)
def i1223():
    out = ink_rrect(6, 10, 52, 48, 8) + ink_rrect(12, 26, 40, 26, 3, H) + ink_rrect(18, 4, 6, 14, 3) + ink_rrect(40, 4, 6, 14, 3) + crescent(30, 39, 10)
    return fit(out, 0.541, 31.8, 30.8)

@reg("io.github.wh201906.serialtest", BLUE_GREY_DEEP)
def i1224():
    out = poly([(6, 14), (58, 14), (50, 50), (14, 50)], I, 5)
    for k in range(5):
        out += ink_circle(16 + k * 8, 26, 2.8, H)
    for k in range(4):
        out += ink_circle(20 + k * 8, 38, 2.8, H)
    return fit(out + ink_rrect(10, 52, 44, 5, 2), 0.524, 32.0, 34.2)

@reg("io.github.whelanh.scidCommunity", AMBER_DARK)
def i1225():
    out = ink_circle(32, 15, 10) + ink_rrect(22, 22, 20, 5, 2) + poly([(26, 26), (38, 26), (45, 49), (19, 49)], I, 2) + ink_rrect(12, 49, 40, 9, 3)
    return fit(out, 0.579, 31.8, 31.4)

@reg("io.github.woelper.Oculante", TEAL_LIGHT)
def i1226():
    out = path("M3 32Q32 4 61 32Q32 60 3 32Z", I, ' stroke="INK" stroke-width="3" stroke-linejoin="round"') + ink_circle(32, 32, 14, H) + ink_circle(32, 32, 7)
    return fit(out, 0.612, 32.0, 32.0)

@reg("io.github.wojciech_graj.OrbVis", LIGHT_BLUE_DEEP)
def i1227():
    out = rot(ellring(32, 32, 27, 10, 3.6), 55, 32, 32) + rot(ellring(32, 32, 27, 10, 3.6), -55, 32, 32) + ink_circle(32, 32, 7) + ink_circle(51, 15, 4.4)
    return fit(out, 0.62, 34.0, 32.0)

@reg("io.github.word_sys.word-sys-pdf-editor", RED_SOFT)
def i1228():
    out = path("M10 4H38L54 20V60H10Z", I, ' stroke="INK" stroke-width="3" stroke-linejoin="round"') + path("M38 4V20H54Z", H) + ink_stroke("M20 30H44", 3.4, H) + ink_stroke("M20 38H44", 3.4, H) + ink_stroke("M20 46H34", 3.4, H)
    return fit(out, 0.502, 32.0, 32.0)

@reg("io.github.xaos_project.XaoS", CYAN_DEEP)
def i1229():
    out = ink_circle(26, 32, 19) + ink_circle(51, 32, 9) + ink_circle(59, 32, 3.4) + ink_circle(36, 12, 5.4) + ink_circle(36, 52, 5.4)
    return fit(out, 0.674, 34.6, 32.0)

@reg("io.github.xfuentes.smart-video-processor", INDIGO_DEEP)
def i1230():
    out = ink_rrect(4, 10, 56, 44, 5)
    for k in range(4):
        out += ink_rrect(8, 15 + k * 10, 5, 6, 1.4, H) + ink_rrect(51, 15 + k * 10, 5, 6, 1.4, H)
    return fit(out + ink_rrect(17, 14, 30, 36, 2, H) + poly([(28, 22), (28, 42), (40, 32)], I, 1.8), 0.55, 31.8, 31.8)

@reg("io.github.xiaoyifang.goldendict_ng", YELLOW)
def i1231():
    out = ink_rrect(8, 4, 48, 52, 6) + ink_rrect(8, 52, 48, 8, 3) + ink_stroke("M20 44L32 14L44 44", 5, H) + ink_stroke("M24 34H40", 4.4, H)
    return fit(out, 0.519, 31.8, 31.8)

@reg("io.github.xolatgames.marknpaul", DEEP_ORANGE)
def i1232():
    out = rot(ink_rrect(24, 4, 16, 34, 4) + poly([(24, 38), (40, 38), (32, 54)], I, 2) + ink_rrect(24, 12, 16, 7, 0, H), 35, 32, 30) + ink_stroke("M6 58H34", 4.4)
    return fit(out, 0.526, 27.8, 32.8)

@reg("io.github.yamanqd.antware", RED_DARK)
def i1233():
    out = ink_circle(32, 14, 7) + ell(32, 29, 7.5, 8) + ell(32, 48, 10, 11)
    for y, dx in ((24, 20), (32, 24), (41, 22)):
        out += ink_stroke(f"M32 {y}L{32 - dx} {y + 7}", 3) + ink_stroke(f"M32 {y}L{32 + dx} {y + 7}", 3)
    out += ink_stroke("M29 9L22 2", 3) + ink_stroke("M35 9L42 2", 3)
    return fit(out, 0.601, 32.0, 29.8)

@reg("io.github.yesser_studios.Pong", LIGHT_BLUE_LIGHT)
def i1234():
    out = ink_rrect(4, 14, 9, 28, 3) + ink_rrect(51, 24, 9, 28, 3) + ink_circle(32, 30, 6)
    out += "".join(ink_rrect(30, 4 + k * 10, 4, 6, 1.5, I) for k in range(6) if k != 3)
    return fit(out, 0.556, 31.8, 31.8)

@reg("io.github.yesser_studios.Yesser-Calculator", YELLOW_DARK)
def i1235():
    out = ink_rrect(9, 3, 46, 58, 7) + ink_rrect(15, 9, 34, 14, 3, H) + ink_stroke("M42 16H44", 3, I)
    for x in (15, 28, 41):
        for y in (29, 40, 51):
            out += ink_rrect(x, y, 8, 7, 2, H)
    return fit(out, 0.543, 32.0, 32.0)

@reg("io.github.yucling.open-orpheus", YELLOW_LIGHT)
def i1236():
    out = ink_stroke("M14 56Q4 12 22 8", 4.4) + ink_stroke("M50 56Q60 12 42 8", 4.4) + ink_stroke("M18 10Q32 18 46 10", 4.4) + ink_stroke("M10 56H54", 4.4)
    for x in (24, 32, 40):
        out += ink_stroke(f"M{x} 15V54", 2.4)
    return fit(out, 0.538, 32.0, 32.0)

@reg("io.github.yuxshao.ptcollab", AMBER)
def i1237():
    out = ink_rrect(4, 8, 56, 48, 5, I)
    for x, y, w in ((9, 14, 14), (26, 22, 12), (40, 14, 16), (14, 32, 20), (38, 36, 14), (12, 46, 10), (28, 46, 22)):
        out += ink_rrect(x, y, w, 6, 2, H)
    return fit(out, 0.531, 31.8, 31.8)

@reg("io.github.zaedus.spider", PURPLE_DARK)
def i1238():
    out = ell(32, 38, 11, 13) + ink_circle(32, 20, 7)
    for y0, mid, end in ((30, (10, 20), (6, 36)), (36, (6, 34), (4, 50)), (42, (8, 46), (8, 60)), (46, (14, 54), (16, 63))):
        out += ink_stroke(f"M{32 - 10} {y0}L{mid[0]} {mid[1]}L{end[0]} {end[1]}", 3) + ink_stroke(f"M{32 + 10} {y0}L{64 - mid[0]} {mid[1]}L{64 - end[0]} {end[1]}", 3)
    return fit(out + ink_circle(29, 19, 1.8, H) + ink_circle(35, 19, 1.8, H), 0.556, 32.0, 38.8)

@reg("io.github.zefr0x.hashes", BLUE_DEEP)
def i1239():
    out = ink_stroke("M24 8L18 56", 6) + ink_stroke("M44 8L38 56", 6) + ink_stroke("M8 24H56", 6) + ink_stroke("M8 42H56", 6)
    return fit(out, 0.607, 32.0, 32.0)

@reg("io.github.zerospades.ZeroSpades", DEEP_PURPLE_DARK)
def i1240():
    out = ink_circle(21, 37, 12.5) + ink_circle(43, 37, 12.5) + poly([(32, 4), (56, 34), (8, 34)], I, 3) + poly([(32, 38), (42, 60), (22, 60)], I, 2)
    return fit(out, 0.604, 32.0, 31.8)

@reg("io.github.zhrexl.thisweekinmylife", YELLOW_SOFT)
def i1241():
    out = ink_rrect(10, 4, 46, 56, 6) + ink_rrect(16, 10, 34, 44, 2, H) + ink_stroke("M22 22H44", 3.4) + ink_stroke("M22 31H44", 3.4) + ink_stroke("M22 40H36", 3.4)
    for y in (14, 28, 42):
        out += ink_rrect(5, y, 10, 5, 2.5)
    return fit(out, 0.523, 30.4, 31.8)

@reg("io.github.zingytomato.netpeek", RED_DEEP.replace(RED_DEEP, RED))
def i1242():
    out = ink_circle(32, 52, 5) + ink_stroke("M20 40Q32 28 44 40", 4.6) + ink_stroke("M10 30Q32 8 54 30", 4.6) + ink_stroke("M2 20Q32 -8 62 20", 4.6)
    return fit(out, 0.546, 32.0, 30.4)

@reg("io.gitlab.ForTheCommunity.torrentsdigger", BROWN)
def i1243():
    out = rot(poly([(24, 36), (40, 36), (44, 60), (20, 60)], I, 3) + ink_rrect(29, 4, 6, 34, 3) + ink_rrect(20, 4, 24, 6, 3), 30, 32, 32)
    return fit(out + ink_circle(14, 52, 4), 0.596, 30.8, 33.2)

@reg("io.gitlab.GCstar.GCstar", YELLOW.replace(YELLOW, AMBER_LIGHT))
def i1244():
    out = dim(ink_rrect(14, 4, 44, 50, 6), .5) + ink_rrect(6, 12, 44, 48, 6) + star5(28, 36, 15, H)
    return fit(out, 0.524, 31.8, 31.8)

@reg("io.gitlab.JBeaumont81.Etesync-Knotes", INDIGO)
def i1245():
    out = path("M6 6H58V40L40 58H6Z", I, ' stroke="INK" stroke-width="3" stroke-linejoin="round"') + path("M58 40H40V58Z", H) + ink_stroke("M16 18H46", 3.4, H) + ink_stroke("M16 28H46", 3.4, H) + ink_stroke("M16 38H30", 3.4, H)
    return fit(out, 0.487, 32.0, 32.0)

@reg("io.gitlab.LibreGames.jumpnbump", ORANGE_SOFT)
def i1246():
    out = ell(24, 10, 4.4, 10) + ell(40, 10, 4.4, 10) + ink_circle(32, 28, 11) + ell(32, 47, 14, 12) + ink_circle(46, 53, 4.4) + ink_circle(28, 26, 1.6, H) + ink_circle(36, 26, 1.6, H)
    return fit(out, 0.596, 34.0, 29.4)

@reg("io.gitlab.adhami3310.Footage", CYAN.replace(CYAN, CYAN_DEEP))
def i1247():
    out = ink_rrect(6, 24, 52, 34, 4) + rot(ink_rrect(6, 10, 52, 12, 3), -9, 6, 22)
    for x in (14, 28, 42):
        out += rot(ink_stroke(f"M{x} 22L{x + 6} 11", 3.6, H), -9, 6, 22)
    return fit(out + ink_circle(32, 41, 8, H) + poly([(30, 37), (30, 45), (37, 41)], I, 1), 0.502, 31.2, 30.0)

@reg("io.gitlab.aimtrain.aimtrain", PINK_DEEP)
def i1248():
    out = ring_c(28, 36, 22, 4) + ring_c(28, 36, 11, 4) + ink_circle(28, 36, 3.4) + ink_stroke("M30 34L56 8", 4) + poly([(44, 6), (58, 6), (58, 20)], I, 1.8)
    return fit(out, 0.485, 31.4, 32.4)

@reg("io.gitlab.azymohliad.WatchMate", INDIGO_LIGHT)
def i1249():
    out = ink_rrect(20, 2, 24, 14, 4) + ink_rrect(20, 48, 24, 14, 4) + ink_circle(32, 32, 19) + ink_circle(32, 32, 14.5, H) + ink_stroke("M32 32V23", 3.4) + ink_stroke("M32 32L39 36", 3.4)
    return fit(out, 0.594, 32.0, 31.8)

@reg("io.gitlab.ballz.Ballz", DEEP_ORANGE_SOFT)
def i1250():
    out = ink_circle(20, 42, 15, I, hs(2.8)) + ink_circle(44, 42, 15, I, hs(2.8)) + ink_circle(32, 20, 15, I, hs(2.8))
    out += ink_stroke("M13 36Q14 32 18 30", 3, H) + ink_stroke("M37 36Q38 32 42 30", 3, H) + ink_stroke("M25 14Q26 10 30 8", 3, H)
    return fit(out, 0.567, 31.8, 30.8)

@reg("io.gitlab.bitseater.kmeteo", BLUE_LIGHT.replace(BLUE_LIGHT, BLUE_SOFT))
def i1251():
    out = ink_circle(40, 20, 11) + "".join(rot(ink_rrect(38.5, 1, 3, 6, 1.5), a, 40, 20) for a in range(0, 360, 45))
    out += ink_circle(20, 44, 13, I, hs(3)) + ink_circle(36, 40, 16, I, hs(3)) + ink_circle(48, 48, 10, I, hs(3)) + ink_rrect(18, 46, 32, 12, 6, I, hs(3))
    return fit(out, 0.53, 32.4, 30.2)

@reg("io.gitlab.blahord.blarock", RED_DARK)
def i1252():
    out = rot(ink_rrect(28, 2, 8, 34, 2) + ink_rrect(26, 2, 12, 8, 3) + ink_circle(32, 44, 13) + ink_circle(32, 32, 9) + ink_circle(32, 44, 5, H) + ink_rrect(25, 40, 14, 3, 1.5, H), 38, 32, 32)
    return fit(out, 0.656, 32.6, 30.2)

@reg("io.gitlab.coolreader_ng.crqt-ng", DEEP_ORANGE_DARK)
def i1253():
    out = ink_rrect(12, 3, 40, 58, 6) + ink_rrect(17, 9, 30, 38, 2, H) + ink_circle(32, 54, 3.2, H)
    for y in (15, 22, 29):
        out += ink_stroke(f"M22 {y}H42", 2.6)
    return fit(out + ink_stroke("M22 37H34", 2.6), 0.564, 31.8, 32.0)

@reg("io.gitlab.cyberphantom52.sudoku_solver", BLUE_GREY_DEEP)
def i1254():
    out = ink_rrect(4, 4, 56, 56, 5) + ink_rrect(8, 8, 48, 48, 2, H)
    out += ink_stroke("M24 8V56", 2.6) + ink_stroke("M40 8V56", 2.6) + ink_stroke("M8 24H56", 2.6) + ink_stroke("M8 40H56", 2.6)
    return fit(out + ink_rrect(25, 25, 14, 14, 1.4) + ink_stroke("M12 12L20 20", 3.4) + ink_stroke("M44 47H52", 3.2), 0.494, 31.8, 31.8)

@reg("io.gitlab.daikhan.stable", ORANGE_SOFT.replace(ORANGE_SOFT, PURPLE_LIGHT))
def i1255():
    out = poly([(32, 4), (60, 24), (60, 58), (4, 58), (4, 24)], I, 3) + ink_rrect(16, 28, 32, 30, 2, H) + ink_stroke("M16 28L48 58", 4, I) + ink_stroke("M48 28L16 58", 4, I) + ink_stroke("M32 12V18", 4, H)
    return fit(out, 0.463, 32.0, 31.2)

@reg("io.gitlab.dev_nis.one-click-backup", TEAL.replace(TEAL, TEAL_DEEP))
def i1256():
    out = ink_rrect(16, 14, 32, 34, 8) + ell(32, 14, 16, 6) + ink_stroke("M16 30Q32 38 48 30", 3, H) + ink_stroke("M16 40Q32 48 48 40", 3, H) + ink_rrect(16, 14, 32, 3, 0, H)
    out = ell(32, 18, 17, 7) + ink_rrect(15, 18, 34, 26, 0) + ell(32, 44, 17, 7) + ink_stroke("M15 30Q32 39 49 30", 3, H) + ink_stroke("M15 40Q32 49 49 40", 3, H)
    return fit(out + arc_arrow(32, 32, 28, 140, 40, 4, 6), 0.514, 31.8, 28.6)

@reg("io.gitlab.elescoute.password", DEEP_ORANGE_LIGHT)
def i1257():
    out = ink_rrect(3, 16, 58, 32, 9)
    for x in (16, 32, 48):
        out += asterisk(x, 32, 6.4, 3.4, H)
    return fit(out, 0.616, 32.0, 31.8)

@reg("io.gitlab.elescoute.spacelaunch", INDIGO_DARK)
def i1258():
    out = path("M32 2Q46 16 44 40H20Q18 16 32 2Z", I) + ink_circle(32, 22, 5.4, H) + poly([(20, 28), (8, 46), (21, 42)], I, 2) + poly([(44, 28), (56, 46), (43, 42)], I, 2) + path("M26 46H38L32 62Z", I)
    return fit(out, 0.624, 32.0, 31.8)

@reg("io.gitlab.floodlight.Presenter", PINK_SOFT)
def i1259():
    out = ink_rrect(4, 4, 56, 36, 4) + ink_rrect(9, 9, 46, 26, 1.5, H) + wedge(24, 22, 0, 12, -90, 160) + ink_stroke("M38 18H50", 3.4) + ink_stroke("M38 27H50", 3.4) + ink_stroke("M32 40V50", 4.4) + ink_stroke("M32 50L18 62", 4.4) + ink_stroke("M32 50L46 62", 4.4)
    return fit(out, 0.474, 31.8, 34.0)

@reg("io.gitlab.gjwu.pdf-tinkerer", GREY)
def i1260():
    out = dim(ink_rrect(22, 4, 34, 44, 4), .5) + ink_rrect(6, 14, 34, 46, 4) + ink_stroke("M13 26H33", 3, H) + ink_stroke("M13 34H33", 3, H) + gear_o(46, 46, 9, 8, I, True)
    return fit(out, 0.505, 32.6, 31.8)

@reg("io.gitlab.guillermop.Counters", ORANGE)
def i1261():
    out = ""
    for x in (10, 22, 34, 46):
        out += ink_stroke(f"M{x} 8V54", 5.6)
    return fit(out + ink_stroke("M4 46L58 16", 5.6), 0.547, 30.8, 30.8)

@reg("io.gitlab.hinnerkm.Kairos", DEEP_PURPLE_LIGHT)
def i1262():
    out = ring_c(32, 32, 25, 4.8) + wedge(32, 32, 0, 18, -90, 30) + ink_stroke("M32 32L32 12", 4) + ink_stroke("M32 7V9", 3)
    return fit(out, 0.677, 32.0, 32.0)

@reg("io.gitlab.ilshat_apps.gitpulsar", BROWN_DARK)
def i1263():
    out = ink_stroke("M18 12V52", 4.4) + ink_stroke("M18 42Q18 28 40 24", 4.4) + ink_circle(18, 12, 7.4) + ink_circle(18, 52, 7.4) + ink_circle(44, 22, 7.4) + ink_circle(44, 22, 2.6, H)
    return fit(out + ink_stroke("M4 36H10L13 30L17 40", 2.4), 0.634, 27.0, 32.0)

@reg("io.gitlab.ilshat_apps.manuscript", YELLOW.replace(YELLOW, BROWN_SOFT))
def i1264():
    out = path("M54 4Q26 6 14 38L18 42Q28 36 34 32Q30 40 24 46L28 50Q54 34 54 4Z", I, ' stroke="INK" stroke-width="2" stroke-linejoin="round"') + ink_stroke("M14 50L8 60", 3.4) + ink_stroke("M18 58H56", 4)
    return fit(out, 0.486, 32.0, 32.4)

@reg("io.gitlab.jazztickets.choria", BLUE.replace(BLUE, BLUE_GREY_LIGHT))
def i1265():
    out = rot(poly([(32, 2), (38, 10), (38, 40), (26, 40), (26, 10)], I, 2) + ink_rrect(16, 40, 32, 6, 2) + ink_rrect(29, 46, 6, 12, 2) + ink_circle(32, 61, 3.4) + ink_stroke("M32 12V34", 2, H), 40, 32, 32)
    return fit(out, 0.577, 31.0, 32.8)

@reg("io.gitlab.jazztickets.emptyclip", ORANGE_DEEP)
def i1266():
    out = rot(ink_rrect(16, 12, 30, 46, 5) + ink_rrect(19, 3, 24, 10, 5) + ink_stroke("M22 28L40 28L22 36L40 36L22 44L40 44", 2.6, H), 12, 32, 32)
    return fit(out, 0.631, 30.4, 30.6)

@reg("io.gitlab.jazztickets.irrlamb", CYAN_DEEP.replace(CYAN_DEEP, LIGHT_BLUE_SOFT))
def i1267():
    out = ink_circle(32, 26, 20) + ink_stroke("M20 22Q22 14 30 11", 3.6, H) + ink_rrect(6, 52, 52, 8, 3)
    return fit(out, 0.511, 31.8, 32.8)

@reg("io.gitlab.jazztickets.openflap", GREY_SOFT.replace(GREY_SOFT, GREY))
def i1268():
    out = ell(28, 34, 22, 18) + poly([(48, 28), (62, 33), (48, 40)], I, 1.6) + ell(20, 38, 11, 6, H) + ink_circle(38, 26, 5, H) + ink_circle(39, 26, 2.2)
    return fit(out, 0.659, 34.2, 33.8)

@reg("io.gitlab.leesonwai.Tactics", RED_DEEP.replace(RED_DEEP, PINK_LIGHT))
def i1269():
    out = ink_stroke("M6 10L22 26", 5.4) + ink_stroke("M22 10L6 26", 5.4) + ring_c(48, 46, 10, 5) + ink_stroke("M18 52Q16 40 30 38Q44 36 40 26", 3.4) + arrowhead(40, 26, 0, -1, 6)
    return fit(out, 0.498, 32.0, 33.0)

@reg("io.gitlab.lekernelpanic.sound-probe", CYAN_DARK)
def i1270():
    out = poly([(4, 24), (16, 24), (30, 10), (30, 54), (16, 40), (4, 40)], I, 3) + ink_stroke("M40 22Q48 32 40 42", 4) + ink_stroke("M47 14Q60 32 47 50", 4)
    return fit(out, 0.673, 29.0, 32.0)

@reg("io.gitlab.liferooter.TextPieces", PURPLE)
def i1271():
    out = ink_stroke("M22 6Q14 6 14 14V24Q14 30 7 32Q14 34 14 40V50Q14 58 22 58", 4.6) + ink_stroke("M42 6Q50 6 50 14V24Q50 30 57 32Q50 34 50 40V50Q50 58 42 58", 4.6)
    return fit(out, 0.593, 32.0, 32.0)

@reg("io.gitlab.metadatacleaner.metadatacleaner", LIGHT_BLUE_DEEP.replace(LIGHT_BLUE_DEEP, LIGHT_BLUE_SOFT))
def i1272():
    out = path("M4 32L26 6H56Q60 6 60 10V38L34 60Q32 62 30 60L6 36Q3 33 4 32Z", I, ' stroke="INK" stroke-width="2" stroke-linejoin="round"') + ink_circle(46, 20, 5, H) + star4(28, 38, 10, H)
    return fit(out, 0.48, 31.8, 33.4)

@reg("io.gitlab.persiangolf.voicegen", PINK.replace(PINK, PURPLE_SOFT))
def i1273():
    out = bubble(4, 6, 56, 40) 
    for k, h in enumerate((8, 18, 28, 14, 22, 10, 16)):
        out += ink_rrect(11 + k * 6.6, 26 - h / 2, 3.6, h, 1.8, H)
    return fit(out, 0.547, 31.8, 30.8)

@reg("io.gitlab.stone_kingdoms.StoneKingdoms", GREY_DARK)
def i1274():
    out = ink_rrect(14, 16, 36, 44, 2)
    for x in (10, 25, 40):
        out += ink_rrect(x, 4, 14, 16, 2)
    out += ink_rrect(18, 20, 28, 3, 0, H) + path("M24 60V44Q24 36 32 36Q40 36 40 44V60Z", H) + ink_rrect(28, 24, 8, 6, 1.5, H) 
    return fit(out, 0.538, 31.8, 31.8)

@reg("io.gitlab.zulfian1732.jollpi-text-editor", RED_LIGHT.replace(RED_LIGHT, LIGHT_BLUE_LIGHT))
def i1275():
    out = ink_rrect(8, 4, 48, 56, 6) + ink_stroke("M20 18H44", 6, H) + ink_stroke("M32 18V46", 6, H) + ink_rrect(41, 38, 3.6, 14, 1.8, H)
    return fit(out, 0.537, 31.8, 31.8)

@reg("io.gitlab.zulfian1732.munquet", PINK_SOFT.replace(PINK_SOFT, RED_SOFT))
def i1276():
    out = "".join(ink_circle(*pt(32, 24, 12.5, -90 + 72 * k), 9) for k in range(5)) + ink_circle(32, 24, 7, H) + ink_stroke("M32 38Q32 50 36 60", 4.4) + path("M34 48Q48 36 56 44Q48 52 34 48Z", I)
    return fit(out, 0.623, 33.4, 32.4)

@reg("io.gpt4all.gpt4all", INDIGO.replace(INDIGO, DEEP_PURPLE))
def i1277():
    out = path("M10 6H54Q60 6 60 12V36Q60 42 54 42H30L16 56V42H10Q4 42 4 36V12Q4 6 10 6Z", I, hs(3)) + star4(32, 24, 12, H) + star4(47, 12, 4, H)
    return fit(out, 0.503, 32.0, 31.0)

@reg("io.greenfire.Greenery", TEAL_LIGHT.replace(TEAL_LIGHT, ORANGE_DEEP))
def i1278():
    out = ink_stroke("M32 62V30", 4.4) + pet(32, 40, 26, 11, -150, 2.4) + pet(32, 30, 28, 12, -35, 2.4) + ink_rrect(18, 54, 28, 8, 3)
    return fit(out, 0.54, 32.2, 38.4)

@reg("io.howl.Editor", BROWN)
def i1279():
    out = poly([(10, 4), (24, 14), (40, 14), (54, 4), (54, 40), (46, 58), (18, 58), (10, 40)], I, 5) + ink_circle(23, 30, 9.6, H) + ink_circle(41, 30, 9.6, H) + ink_circle(23, 30, 4.4) + ink_circle(41, 30, 4.4) + poly([(28, 36), (36, 36), (32, 46)], H, 1.6)
    return fit(out, 0.497, 32.0, 31.0)

@reg("io.httpie.Httpie", DEEP_ORANGE.replace(DEEP_ORANGE, DEEP_ORANGE_DEEP))
def i1280():
    out = wedge(28, 36, 0, 24, 0, 270) + wedge(32, 32, 0, 24, 270, 360)
    return fit(out, 0.75, 41.8, 21.8)

@reg("io.itch.amcsquad.amcsquad", TEAL_DEEP.replace(TEAL_DEEP, INDIGO_DEEP))
def i1281():
    out = path("M32 4L58 14V34Q58 52 32 62Q6 52 6 34V14Z", I, ' stroke="INK" stroke-width="2" stroke-linejoin="round"')
    out += ink_stroke("M18 22L32 32L46 22", 4.6, H) + ink_stroke("M18 32L32 42L46 32", 4.6, H)
    return fit(out, 0.562, 32.0, 33.0)

@reg("io.itch.doctorm64.skippybot", YELLOW_DARK.replace(YELLOW_DARK, ORANGE_LIGHT))
def i1282():
    out = ink_rrect(9, 18, 46, 38, 10) + ink_stroke("M32 18V8", 3.6) + ink_circle(32, 7, 4.4) + ink_circle(22, 34, 6.4, H) + ink_circle(42, 34, 6.4, H) + ink_stroke("M22 47H42", 3.6, H) + ink_rrect(3, 30, 5, 12, 2) + ink_rrect(56, 30, 5, 12, 2)
    return fit(out, 0.598, 32.0, 29.2)

@reg("io.itch.domestique_baston.domestique_baston", AMBER_DARK.replace(AMBER_DARK, BLUE_GREY_DARK))
def i1283():
    out = ring_c(14, 44, 11, 4) + ring_c(50, 44, 11, 4) + ink_stroke("M14 44L26 22H44L50 44", 3.8) + ink_stroke("M26 22L34 44H14", 3.8) + ink_stroke("M34 44L44 22", 3.8) + ink_stroke("M22 14H32", 4.4) + ink_stroke("M42 16H50", 4.4)
    return fit(out, 0.556, 32.0, 34.4)

@reg("io.itch.domestique_baston.java_jolt", BROWN_DEEP)
def i1284():
    out = path("M8 18H42V40Q42 54 25 54Q8 54 8 40Z", I) + ring_c(46, 30, 7, 4.4) + ink_rrect(6, 56, 40, 5, 2.5) + poly([(28, 22), (18, 36), (25, 36), (22, 47), (33, 31), (26, 31)], H, 1.4)
    return fit(out + ink_stroke("M16 4Q12 8 16 12", 3) + ink_stroke("M26 4Q22 8 26 12", 3) + ink_stroke("M36 4Q32 8 36 12", 3), 0.504, 30.4, 31.8)

@reg("io.itch.domestique_baston.kindergarten_massaker", AMBER.replace(AMBER, AMBER_SOFT))
def i1285():
    out = ink_rrect(4, 38, 24, 22, 3) + ink_rrect(32, 38, 24, 22, 3) + rot(ink_rrect(16, 12, 24, 22, 3), -8, 28, 24) + ink_stroke("M10 49H22", 3.4, H) + ink_stroke("M38 49H50", 3.4, H) + ink_circle(28, 22, 4, H)
    return fit(out, 0.536, 29.8, 35.2)

@reg("io.itch.keyikedalube_ndang.Type-Off", DEEP_PURPLE_DEEP.replace(DEEP_PURPLE_DEEP, INDIGO_SOFT))
def i1286():
    out = ink_rrect(4, 3, 56, 52, 9) + ink_rrect(11, 9, 42, 36, 5, H) + poly([(32, 15), (44, 29), (36, 29), (36, 39), (28, 39), (28, 29), (20, 29)], I, 1.6) + ink_rrect(8, 57, 48, 5, 2.5)
    return fit(out, 0.5, 31.8, 32.4)

@reg("io.itch.nordup.TheGates", GREY_SOFT.replace(GREY_SOFT, GREY_LIGHT))
def i1287():
    out = ink_rrect(4, 22, 10, 40, 2) + ink_rrect(50, 22, 10, 40, 2) + ink_rrect(2, 16, 14, 8, 2) + ink_rrect(48, 16, 14, 8, 2) + ink_stroke("M14 62V32Q14 14 32 14Q50 14 50 32V62", 4.4)
    for x in (22, 32, 42):
        out += ink_stroke(f"M{x} 18V62", 3)
    return fit(out + ink_stroke("M16 38H48", 3) + ink_stroke("M16 50H48", 3), 0.512, 31.8, 38.0)

@reg("io.itch.tx00100xt.SeriousSamClassic", YELLOW.replace(YELLOW, RED_DARK))
def i1288():
    out = ink_rrect(4, 20, 24, 22, 8) + ink_rrect(36, 20, 24, 22, 8) + ink_rrect(24, 24, 16, 5, 2.5) + ink_stroke("M6 24L2 18", 4) + ink_stroke("M58 24L62 18", 4) + ink_stroke("M16 32H20", 3, H)
    return fit(out + ink_stroke("M10 52Q32 62 54 52", 4.4), 0.491, 31.8, 37.4)

@reg("io.itch.tx00100xt.SeriousSamClassic-VK", CYAN.replace(CYAN, LIGHT_BLUE_DARK))
def i1289():
    out = poly([(32, 4), (60, 58), (4, 58)], I, 3) + poly([(32, 28), (44, 51), (20, 51)], H, 1.4) + poly([(32, 18), (36, 26), (28, 26)], H, 1)
    return fit(out, 0.461, 32.0, 31.0)

@reg("io.itsterminal.WebPConverter", GREY_SOFT.replace(GREY_SOFT, DEEP_PURPLE_SOFT))
def i1290():
    out = arc_arrow(32, 32, 26, -160, -20, 4.4, 6.5) + arc_arrow(32, 32, 26, 20, 160, 4.4, 6.5) + poly([(14, 44), (26, 24), (34, 36), (40, 30), (50, 44)], I, 2.4) + ink_circle(40, 20, 4)
    return fit(out, 0.574, 32.0, 32.0)

@reg("io.jor.bugdom2", RED_DEEP.replace(RED_DEEP, RED_LIGHT))
def i1291():
    out = ink_circle(32, 14, 8) + ink_stroke("M27 8L22 2", 3) + ink_stroke("M37 8L42 2", 3) + ink_circle(32, 38, 22) + ink_stroke("M32 18V60", 3.4, H)
    for x, y in ((21, 34), (43, 34), (22, 48), (42, 48)):
        out += ink_circle(x, y, 3.6, H)
    return fit(out, 0.575, 31.8, 31.2)

@reg("io.jor.cromagrally", ORANGE_SOFT.replace(ORANGE_SOFT, ORANGE_DEEP))
def i1292():
    out = path("M3 42V32Q3 28 8 27L18 25L26 14Q28 12 31 12H44Q47 12 49 15L55 27L58 28Q61 29 61 33V42Z", I, hs(2)) + poly([(27, 17), (44, 17), (50, 27), (22, 27)], H, 1.4) + ink_circle(17, 44, 9.4, I, hs(3)) + ink_circle(47, 44, 9.4, I, hs(3)) + ink_circle(17, 44, 3, H) + ink_circle(47, 44, 3, H)
    return fit(out, 0.595, 31.8, 33.0)

@reg("io.jor.mightymike", GREY_DEEP)
def i1293():
    out = ink_rrect(22, 28, 20, 8, 3) + ink_rrect(10, 12, 12, 40, 4) + ink_rrect(42, 12, 12, 40, 4) + ink_rrect(3, 20, 8, 24, 3) + ink_rrect(53, 20, 8, 24, 3)
    return fit(out, 0.609, 32.0, 31.8)

@reg("io.jor.nanosaur", AMBER_DARK.replace(AMBER_DARK, AMBER_DARK))
def i1294():
    out = ell(32, 40, 22, 13)
    for x, h in ((20, 9), (30, 14), (40, 12), (49, 8)):
        out += poly([(x - 5, 32), (x, 32 - h - 4), (x + 5, 32)], I, 1.6)
    out += ink_circle(10, 40, 7) + ink_rrect(3, 40, 10, 6, 3) + poly([(52, 38), (62, 50), (50, 46)], I, 1.6) + ink_rrect(18, 46, 7, 14, 2.5) + ink_rrect(38, 46, 7, 14, 2.5) + ink_circle(9, 37, 1.6, H)
    return fit(out, 0.568, 32.8, 36.4)

@reg("io.jor.nanosaur2", BLUE.replace(BLUE, BLUE_DARK))
def i1295():
    out = path("M32 18L2 6Q8 24 12 32Q22 28 32 34Q42 28 52 32Q56 24 62 6Z", I, hs(2.4)) + ell(32, 30, 5, 13) + poly([(32, 42), (28, 58), (36, 58)], I, 1.4)
    return fit(out, 0.457, 31.8, 31.6)

@reg("io.jor.ottomatic", PINK_DEEP.replace(PINK_DEEP, PINK_DARK))
def i1296():
    out = gear_o(32, 34, 20, 10, I, False) + ink_rrect(18, 24, 28, 20, 5, H) + ink_circle(26, 34, 3.6) + ink_circle(38, 34, 3.6) + ink_stroke("M32 14V6", 3.4) + ink_circle(32, 5, 3.4)
    return fit(out, 0.653, 31.8, 30.0)

@reg("io.kapsa.drive", BLUE_LIGHT.replace(BLUE_LIGHT, BLUE_GREY_DEEP))
def i1297():
    out = ink_rrect(4, 18, 56, 30, 7) + ink_stroke("M12 34H34", 4, H) + ink_circle(47, 34, 3.6, H) + poly([(10, 18), (15, 8), (49, 8), (54, 18)], I, 2) 
    return fit(out + ink_rrect(8, 52, 10, 5, 2) + ink_rrect(46, 52, 10, 5, 2), 0.55, 31.8, 32.0)

@reg("io.keet.Keet", CYAN.replace(CYAN, CYAN_LIGHT))
def i1298():
    out = dim(bubble(20, 4, 40, 28), .55) + bubble(4, 24, 42, 30) + ink_rrect(11, 33, 28, 4, 2, H) + ink_rrect(11, 41, 18, 4, 2, H)
    return fit(out, 0.496, 31.8, 33.8)

@reg("io.kinvolk.Headlamp", YELLOW_SOFT)
def i1299():
    out = path("M6 44Q6 14 30 14Q54 14 54 44Z", I) + ink_rrect(4, 44, 52, 8, 3) + ink_circle(30, 34, 6.4, H) + ink_stroke("M42 6L48 12", 3.6) + ink_stroke("M54 2L62 4", 3.6) + ink_stroke("M60 20L64 24", 3.6)
    return fit(out, 0.477, 34.8, 26.0)

@reg("io.kurrent.navigator", BLUE_DARK.replace(BLUE_DARK, INDIGO_LIGHT))
def i1300():
    out = ring_c(32, 32, 26, 4.4) + rot(poly([(32, 8), (40, 32), (32, 56), (24, 32)], I, 1.8) + poly([(32, 8), (40, 32), (24, 32)], H, 1), 45, 32, 32) + ink_circle(32, 32, 3, H)
    return fit(out, 0.657, 32.0, 32.0)
