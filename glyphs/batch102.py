# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 102: ser_player to nip4."""
from lm import (
    AMBER_DARK, AMBER_DEEP, BLUE, BLUE_DARK, BLUE_DEEP, BLUE_GREY, BLUE_GREY_DARK,
    BLUE_GREY_DEEP, BLUE_GREY_LIGHT, BLUE_LIGHT, BROWN, BROWN_DARK, BROWN_DEEP, BROWN_LIGHT,
    BROWN_SOFT, CYAN_DARK, CYAN_DEEP, DEEP_ORANGE, DEEP_ORANGE_DEEP, DEEP_ORANGE_LIGHT,
    DEEP_PURPLE, DEEP_PURPLE_DEEP, DEEP_PURPLE_LIGHT, DEEP_PURPLE_SOFT, f, GREY, GREY_DARK,
    GREY_DEEP, HOLE, INDIGO, INDIGO_DEEP, INDIGO_SOFT, INK, LIGHT_BLUE_DEEP, ORANGE_DARK,
    ORANGE_DEEP, path, PINK, PINK_DEEP, PINK_LIGHT, poly, pt, PURPLE, PURPLE_DARK, PURPLE_DEEP,
    PURPLE_LIGHT, PURPLE_SOFT, RED, RED_DARK, RED_DEEP, RED_LIGHT, TEAL, TEAL_DEEP, TEAL_LIGHT,
)
from glyphs.kit import (
    arc_arrow, arrowhead, asterisk, bubble, crescent, dim, ell, ellring, fit, hashmark, hexring, hs, hx, ink_circle, ink_stroke, mirror, pet, petal, registry, ring_c, ink_rrect, rot, spiral, star4)

ICONS, SMALL, reg, _ = registry()


@reg("org.free_astro.ser_player", DEEP_PURPLE)
def ser_player():
    out = crescent(28, 34, 21) + star4(48, 16, 9)
    return fit(out, 0.703, 32.1, 30.9)


@reg("org.freeciv.gtk4", PURPLE_SOFT)
def gtk4():
    out = ink_rrect(12, 26, 40, 28, 2) + ink_rrect(12, 13, 9, 15, 1) + ink_rrect(27.5, 13, 9, 15, 1) + ink_rrect(43, 13, 9, 15, 1) + path("M25 54V42Q25 33 32 33Q39 33 39 42V54Z", HOLE)
    return fit(out, 0.729, 32.0, 33.5)


@reg("org.freecol.FreeCol", RED)
def freecol():
    out = path("M8 41H56L48 55H16Z", INK) + ink_rrect(30, 8, 4, 34, 2) + poly([(37, 11), (54, 36), (37, 36)], INK, 2) + poly([(27, 17), (12, 36), (27, 36)], INK, 2)
    return fit(out, 0.726, 32.0, 31.5)


@reg("org.freedesktop.appstream-glib", CYAN_DEEP)
def appstream_glib():
    out = hx(32, 32, 23, -90, INK, 3)
    for a in (210, -30, 90):
        p = pt(32, 32, 23, a)
        out += ink_stroke(f"M32 32L{f(p[0])} {f(p[1])}", 3, HOLE)
    return fit(out, 0.735, 32.0, 32.0)


@reg("org.freedesktop.appstream.cli", BROWN_LIGHT)
def cli():
    out = ink_rrect(8, 12, 48, 40, 8) + ink_stroke("M18 25L28 32L18 39", 4.6, HOLE) + ink_stroke("M33 41H46", 4.6, HOLE)
    return fit(out, 0.733, 32.0, 32.0)


@reg("org.freedesktop.appstream.generator", INDIGO)
def generator():
    out = poly([(38, 6), (16, 36), (29, 36), (24, 58), (48, 26), (34, 26)], INK, 2)
    return fit(out, 0.667, 32.0, 32.0)


@reg("org.freedesktop.dabrain34.squared", AMBER_DARK)
def squared():
    out = ink_rrect(8, 8, 22, 22, 5) + ink_rrect(34, 8, 22, 22, 5) + ink_rrect(8, 34, 22, 22, 5) + ink_rrect(34, 34, 22, 22, 5) + ink_rrect(40, 40, 10, 10, 2, HOLE)
    return fit(out, 0.644, 32.0, 32.0)


@reg("org.freeorion.FreeOrion", PINK_DEEP)
def freeorion():
    out = spiral(32, 32, 4, 23, 1.7, 0, 5.4) + ink_circle(32, 32, 5.5)
    return fit(out, 0.796, 29.2, 30.1)


@reg("org.gabmus.swatch", TEAL)
def swatch():
    def card(a):
        return rot(ink_rrect(25, 6, 14, 44, 4, INK, hs(2.6)), a, 32, 54)
    out = card(-36) + card(36) + card(0)
    return fit(out, 0.558, 32.0, 29.6)


@reg("org.garudalinux.firedragon", DEEP_ORANGE)
def firedragon():
    out = path("M32 6C36 18 50 26 50 40C50 50 42 58 32 58C22 58 14 50 14 40C14 32 18 26 22 22C22 28 26 32 29 32C28 22 28 14 32 6Z", INK) + path("M32 53C27 53 24 50 24 46C24 42 29 39 32 34C35 39 40 42 40 46C40 50 37 53 32 53Z", HOLE)
    return fit(out, 0.696, 32.0, 32.1)


@reg("org.gemrb.gemrb", BLUE)
def gemrb():
    out = poly([(18, 12), (46, 12), (56, 26), (32, 54), (8, 26)], INK, 2.5) + ink_stroke("M8 26H56", 2.8, HOLE) + ink_stroke("M24 26L32 54L40 26", 2.8, HOLE) + ink_stroke("M18 12L24 26M46 12L40 26", 2.8, HOLE)
    return fit(out, 0.713, 32.0, 33.0)


@reg("org.genivi.DLTViewer", ORANGE_DEEP)
def dltviewer():
    out = ""
    for y, w in ((14, 30), (29, 32), (44, 20)):
        out += ink_circle(12, y + 3, 4.5) + ink_rrect(23, y, w, 6, 3)
    return fit(out, 0.71, 31.2, 32.0)


@reg("org.gephi.Gephi", PURPLE_LIGHT)
def gephi():
    nodes = [(13, 18, 6), (51, 13, 5), (55, 42, 7), (20, 52, 6)]
    out = ""
    for x, y, r in nodes:
        out += ink_stroke(f"M32 32L{x} {y}", 3.6)
    out += ink_stroke("M13 18L51 13", 3.6) + ink_circle(32, 32, 9)
    for x, y, r in nodes:
        out += ink_circle(x, y, r)
    return fit(out, 0.638, 34.5, 33.0)


@reg("org.getoutline.OutlineClient", GREY)
def outlineclient():
    out = path("M32 6L53 14V32C53 45 44 53 32 58C20 53 11 45 11 32V14Z", INK) + ink_circle(32, 27, 6, HOLE) + ink_rrect(29.5, 30, 5, 14, 2, HOLE)
    return fit(out, 0.692, 32.0, 32.0)


@reg("org.getoutline.OutlineManager", BLUE_GREY_DARK)
def outlinemanager():
    out = ""
    for y in (8, 25, 42):
        out += ink_rrect(8, y, 48, 14, 5) + ink_circle(17, y + 7, 2.8, HOLE) + ink_rrect(26, y + 5, 24, 4, 2, HOLE)
    return fit(out, 0.644, 32.0, 32.0)


@reg("org.getzola.zola", LIGHT_BLUE_DEEP)
def zola():
    out = ink_stroke("M16 14H48L16 50H48", 7.5)
    return fit(out, 0.737, 32.0, 32.0)


@reg("org.gitfourchette.gitfourchette", DEEP_ORANGE)
def gitfourchette():
    out = ink_stroke("M19 8V28", 5.4) + ink_stroke("M32 8V36", 5.4) + ink_stroke("M45 8V28", 5.4) + ink_stroke("M19 24V28Q19 37 32 37Q45 37 45 28V24", 5.4) + ink_stroke("M32 37V57", 6.4)
    return fit(out, 0.655, 32.0, 32.8)


@reg("org.gnome.HexGL", DEEP_PURPLE_DEEP)
def hexgl():
    out = hexring(32, 32, 24, 5) + ink_stroke("M23 26L32 34L41 26", 4.6) + ink_stroke("M23 37L32 45L41 37", 4.6)
    return fit(out, 0.679, 32.0, 32.0)


@reg("org.gnome.Manuals", BLUE_GREY_LIGHT)
def manuals():
    out = path("M31 15Q19 9 6 13V50Q19 46 31 53Z", INK) + path("M33 15Q45 9 58 13V50Q45 46 33 53Z", INK) + ink_stroke("M12 24Q19 22 25 25", 2.8, HOLE) + ink_stroke("M39 25Q45 22 52 24", 2.8, HOLE)
    return fit(out, 0.637, 32.0, 32.2)


@reg("org.gnome.gitlab.TitouanReal.Era", RED_DEEP)
def era():
    out = ink_rrect(10, 6, 44, 6, 3) + ink_rrect(10, 52, 44, 6, 3) + poly([(15, 14), (49, 14), (32, 32)], INK, 2) + poly([(32, 32), (15, 50), (49, 50)], INK, 2) + poly([(32, 41), (25, 48), (39, 48)], HOLE)
    return fit(out, 0.626, 32.0, 32.0)


@reg("org.gnome.gitlab.bazylevnik0.Convolution", CYAN_DEEP)
def convolution():
    out = ""
    for x in range(3):
        for y in range(3):
            sq = ink_rrect(9 + 17 * x, 9 + 17 * y, 15, 15, 3.5)
            out += sq if (x, y) == (1, 1) else dim(sq, 0.55)
    out += ink_circle(32, 32, 3.2, HOLE)
    return fit(out, 0.62, 33.5, 33.5)


@reg("org.gnome.gitlab.cheywood.Buffer", BROWN)
def buffer():
    out = path("M12 8H38L52 22V56H12Z", INK) + ink_stroke("M38 8V22H52", 2.8, HOLE) + ink_stroke("M21 35H43", 3.4, HOLE) + ink_stroke("M21 45H35", 3.4, HOLE)
    return fit(out, 0.66, 32.0, 32.0)


@reg("org.gnome.gitlab.cheywood.Pulp", ORANGE_DEEP)
def pulp():
    out = ink_circle(32, 32, 23) + ring_c(32, 32, 19, 2.6, HOLE) + asterisk(32, 32, 15, 3.2, HOLE)
    return fit(out, 0.783, 32.0, 32.0)


@reg("org.gnome.gitlab.dqpb.GMetronome", AMBER_DEEP)
def gmetronome():
    out = poly([(24, 8), (40, 8), (54, 56), (10, 56)], INK, 4) + ink_stroke("M32 49L43 17", 3.8, HOLE) + ink_circle(39, 28, 4.6, HOLE)
    return fit(out, 0.594, 32.0, 32.0)


@reg("org.gnome.gitlab.johannesjh.favagtk", PINK)
def favagtk():
    out = rot(ink_rrect(3, 24, 58, 17, 8.5) + ink_circle(17, 32.5, 5, HOLE) + ink_circle(32, 32.5, 5, HOLE) + ink_circle(47, 32.5, 5, HOLE), -35, 32, 32)
    return fit(out, 0.708, 32.2, 32.4)


@reg("org.gnome.gitlab.powimod.aion-task", TEAL_DEEP)
def aion_task():
    out = ""
    for y in (14, 29):
        out += ink_rrect(9, y - 6, 14, 12, 3.4) + ink_rrect(31, y - 3, 23, 6, 3)
    out += ink_rrect(9, 38, 15, 14, 3.5) + ink_rrect(13, 42, 7, 6, 1, HOLE) + ink_rrect(31, 42, 23, 6, 3)
    return fit(out, 0.685, 30.4, 28.9)


@reg("org.gnu.liquidwar6", GREY_DEEP)
def liquidwar6():
    out = path("M32 6Q52 30 52 40A20 20 0 0 1 12 40Q12 30 32 6Z", INK) + ink_stroke("M22 40Q22 47 29 51", 3.6, HOLE)
    return fit(out, 0.67, 32.0, 33.1)


@reg("org.gnuhealth.mygnuhealth", BLUE_DEEP)
def mygnuhealth():
    out = path("M32 56C8 40 6 22 19 15C26 11 30 15 32 19C34 15 38 11 45 15C58 22 56 40 32 56Z", INK) + ink_stroke("M13 33H24L28 24L35 42L39 33H51", 3.4, HOLE)
    return fit(out, 0.842, 32.0, 34.6)


@reg("org.godotengine.Godot3Sharp", LIGHT_BLUE_DEEP)
def godot3sharp():
    out = hexring(32, 32, 25, 4.6) + hashmark(32, 32, 11, 4.2)
    return fit(out, 0.661, 32.0, 32.0)


@reg("org.godotengine.GodotSharp", CYAN_DEEP)
def godotsharp():
    out = hashmark(32, 32, 21, 6.4)
    return fit(out, 0.742, 32.0, 32.0)


@reg("org.goldcoinproject.goldcoin-qt", ORANGE_DARK)
def goldcoin_qt():
    out = ""
    for yc in (42, 30, 18):
        out += f'<ellipse cx="32" cy="{yc + 8}" rx="20" ry="8" fill="{INK}" stroke="{HOLE}" stroke-width="2.6"/>'
        out += ink_rrect(12, yc, 40, 8, 0)
        out += f'<ellipse cx="32" cy="{yc}" rx="20" ry="8" fill="{INK}" stroke="{HOLE}" stroke-width="2.6"/>'
    return fit(out, 0.75, 32.0, 34.0)


@reg("org.gpodder.gpodder-adaptive", BLUE_GREY_DEEP)
def gpodder_adaptive():
    a1, a2 = pt(32, 28, 19, 120), pt(32, 28, 11, 120)
    b1, b2 = pt(32, 28, 19, 60), pt(32, 28, 11, 60)
    out = ink_circle(32, 28, 5.5) + ink_stroke(f"M{f(a1[0])} {f(a1[1])}A19 19 0 1 1 {f(b1[0])} {f(b1[1])}", 4.6) + ink_stroke(f"M{f(a2[0])} {f(a2[1])}A11 11 0 1 1 {f(b2[0])} {f(b2[1])}", 4.6) + poly([(32, 33), (25, 56), (39, 56)], INK, 2)
    return fit(out, 0.716, 32.0, 31.9)


@reg("org.gpxsee.GPXSee", LIGHT_BLUE_DEEP)
def gpxsee():
    out = ink_stroke("M12 48C20 20 28 54 36 32S48 18 52 16", 5) + ink_circle(12, 48, 6.5) + ink_circle(52, 16, 6.5)
    return fit(out, 0.639, 32.0, 32.0)


@reg("org.grisbi.Grisbi", DEEP_ORANGE_DEEP)
def grisbi():
    out = ink_rrect(6, 16, 52, 32, 5) + ink_circle(32, 32, 8.5, HOLE) + ink_circle(15, 25, 2.8, HOLE) + ink_circle(49, 39, 2.8, HOLE)
    return fit(out, 0.692, 32.0, 32.0)


@reg("org.groestlcoin.electrum-grs", DEEP_PURPLE)
def electrum_grs():
    out = "".join(rot(ellring(32, 32, 24, 9.5, 3.8), a, 32, 32) for a in (0, 60, 120)) + ink_circle(32, 32, 5.8)
    return fit(out, 0.692, 32.0, 32.0)


@reg("org.groestlcoin.groestlcoin-qt", DEEP_PURPLE_SOFT)
def groestlcoin_qt():
    out = hx(32, 32, 24, -90, INK, 4) + ink_stroke("M41 25A11.3 11.3 0 1 0 43 34H33", 4.6, HOLE)
    return fit(out, 0.692, 32.0, 32.0)


@reg("org.guerinoni.qTsConverter", RED_LIGHT)
def qtsconverter():
    out = ink_stroke("M10 22H40", 5) + arrowhead(51, 22, 1, 0, 9) + ink_stroke("M54 42H24", 5) + arrowhead(13, 42, -1, 0, 9)
    return fit(out, 0.626, 32.0, 32.0)


@reg("org.gweatherrouting.gweatherrouting", CYAN_DEEP)
def gweatherrouting():
    out = ink_stroke("M8 22H36Q46 22 46 14Q46 8 40 8Q35 8 35 13", 4.8) + ink_stroke("M8 34H48Q58 34 58 42Q58 50 50 50Q44 50 44 45", 4.8) + ink_stroke("M8 46H26", 4.8)
    return fit(out, 0.63, 33.0, 29.0)


@reg("org.hdfgroup.HDFCompass", BROWN_DARK)
def hdfcompass():
    out = ring_c(32, 32, 23, 4.6) + rot(poly([(32, 14), (39, 32), (25, 32)], INK, 1.5) + dim(poly([(32, 50), (39, 32), (25, 32)], INK, 1.5), 0.5), 40, 32, 32) + ink_circle(32, 32, 3, HOLE)
    return fit(out, 0.713, 32.0, 32.0)


@reg("org.hdfgroup.HDFView", INDIGO_DEEP)
def hdfview():
    out = ink_rrect(8, 10, 48, 44, 6) + ink_stroke("M8 24H56", 2.8, HOLE) + ink_stroke("M8 39H56", 2.8, HOLE) + ink_stroke("M24 24V54", 2.8, HOLE) + ink_stroke("M40 24V54", 2.8, HOLE)
    return fit(out, 0.684, 32.0, 32.0)


@reg("org.hikounomizu.HikouNoMizu", AMBER_DEEP)
def hikounomizu():
    out = ink_circle(32, 32, 7) + ring_c(32, 32, 15, 4.6) + ring_c(32, 32, 23, 4.6)
    return fit(out, 0.713, 32.0, 32.0)


@reg("org.hlwd.sonofman", PINK_DEEP)
def sonofman():
    out = ink_rrect(27, 5, 10, 54, 3.5) + ink_rrect(13, 19, 38, 10, 3.5)
    return fit(out, 0.667, 32.0, 32.0)


@reg("org.hnefatafl.hnefatafl_client", TEAL)
def hnefatafl_client():
    out = ink_rrect(30, 3, 4, 14, 2) + ink_rrect(25, 8, 14, 4, 2) + ink_circle(32, 23, 7) + poly([(27, 26), (37, 26), (45, 50), (19, 50)], INK, 3) + ink_rrect(13, 50, 38, 8, 4)
    return fit(out, 0.643, 32.0, 30.5)


@reg("org.imitationpickles.barbie", GREY_DEEP)
def barbie():
    out = poly([(32, 32), (7, 15), (7, 49)], INK, 4) + poly([(32, 32), (57, 15), (57, 49)], INK, 4) + ink_rrect(24, 24, 16, 16, 6) + ink_stroke("M13 32H22", 2.8, HOLE) + ink_stroke("M42 32H51", 2.8, HOLE)
    return fit(out, 0.636, 32.0, 32.0)


@reg("org.indii.mendingwall", BLUE_LIGHT)
def mendingwall():
    out = ""
    for y, cuts in ((10, (8, 30, 34, 56)), (26, (8, 18, 22, 42, 46, 56)), (42, (8, 30, 34, 56))):
        for k in range(0, len(cuts), 2):
            out += ink_rrect(cuts[k], y, cuts[k + 1] - cuts[k], 12, 2.5)
    return fit(out, 0.651, 32.0, 32.0)


@reg("org.ioquake3.ioquake3", ORANGE_DEEP)
def ioquake3():
    out = ring_c(32, 32, 16, 4.6) + ink_stroke("M32 6V19", 4.6) + ink_stroke("M32 45V58", 4.6) + ink_stroke("M6 32H19", 4.6) + ink_stroke("M45 32H58", 4.6) + ink_circle(32, 32, 3.4)
    return fit(out, 0.637, 32.0, 32.0)


@reg("org.jacktrip.JackTrip", PURPLE_DARK)
def jacktrip():
    out = rot(path("M28 17V12Q28 6 32 6Q36 6 36 12V17Z", INK) + ink_rrect(27, 20, 10, 9, 1) + ink_rrect(27, 31, 10, 9, 1) + ink_rrect(21, 43, 22, 15, 4), 35, 32, 32)
    return fit(out, 0.7, 29.1, 34.0)


@reg("org.jflap.JFLAP", CYAN_DEEP)
def jflap():
    out = ring_c(16, 18, 9, 4.6) + ring_c(47, 46, 9, 4.6) + ring_c(47, 46, 3.6, 2.6) + ink_stroke("M23 25L37 40", 4.6) + arrowhead(39, 42, .707, .707, 8)
    return fit(out, 0.638, 31.5, 32.0)


@reg("org.jjazzlab.JJazzLab", BLUE_GREY)
def jjazzlab():
    out = ink_rrect(8, 12, 48, 40, 5)
    for x in (20, 32, 44):
        out += ink_stroke(f"M{x} 34V52", 2.8, HOLE) + ink_rrect(x - 4, 12, 8, 23, 2, HOLE)
    return fit(out, 0.702, 32.0, 32.0)


@reg("org.jousse.vincent.Pomodorolm", RED)
def pomodorolm():
    out = ink_circle(32, 37, 21) + ink_rrect(30, 6, 4, 13, 2) + "".join(petal(32, 21, 14, 4.2, a, HOLE) for a in (-165, -125, -55, -15))
    return fit(out, 0.692, 32.0, 32.0)


@reg("org.jreleaser.cli", DEEP_ORANGE)
def cli_icon():
    out = path("M32 5Q47 18 44 42L32 50L20 42Q17 18 32 5Z", INK) + ink_circle(32, 24, 5.6, HOLE) + poly([(21, 34), (9, 48), (23, 45)], INK, 2) + poly([(43, 34), (55, 48), (41, 45)], INK, 2) + poly([(26, 52), (32, 61), (38, 52)], INK, 2)
    return fit(out, 0.632, 32.0, 33.5)


@reg("org.karapulse.Karapulse", DEEP_PURPLE_DEEP)
def karapulse():
    out = ink_rrect(23, 6, 18, 30, 9) + ink_stroke("M15 28Q15 47 32 47Q49 47 49 28", 4.8) + ink_stroke("M32 47V57", 4.8) + ink_stroke("M21 57H43", 4.8) + ink_stroke("M23 17H41", 3, HOLE) + ink_stroke("M23 24H41", 3, HOLE)
    return fit(out, 0.673, 32.0, 32.8)


@reg("org.kartkrew.RingRacers", BROWN_SOFT)
def ringracers():
    out = ring_c(32, 32, 22, 5.2) + ink_circle(32, 32, 7.5) + ink_stroke("M12 32H25", 5.2) + ink_stroke("M39 32H52", 5.2) + ink_stroke("M32 39V52", 5.2)
    return fit(out, 0.735, 32.0, 32.0)


@reg("org.kde.CrowTranslate", RED)
def crowtranslate():
    out = ink_rrect(6, 7, 31, 27, 5) + ink_rrect(27, 30, 31, 27, 5, INK, hs(3)) + ink_stroke("M14 27L21.5 13L29 27", 3.4, HOLE) + ink_stroke("M17 22.5H26", 3, HOLE) + ink_stroke("M35 43H51", 3.2, HOLE) + ink_stroke("M43 37V49", 3.2, HOLE)
    return fit(out, 0.604, 32.0, 32.0)


@reg("org.kde.amarok", CYAN_DARK)
def amarok():
    out = ink_stroke("M12 40V32A20 20 0 0 1 52 32V40", 5.4) + ink_rrect(7, 36, 13, 20, 5.5) + ink_rrect(44, 36, 13, 20, 5.5)
    return fit(out, 0.642, 32.0, 32.6)


@reg("org.kde.angelfish", BROWN_DEEP)
def angelfish():
    out = ell(26, 32, 17, 13) + poly([(38, 32), (58, 18), (58, 46)], INK, 2.5) + poly([(18, 22), (31, 8), (33, 22)], INK, 2) + poly([(21, 42), (31, 56), (33, 42)], INK, 2) + ink_circle(18, 29, 3, HOLE)
    return fit(out, 0.71, 34.1, 32.0)


@reg("org.kde.audex", INDIGO)
def audex():
    out = ink_circle(32, 32, 23) + ring_c(32, 32, 14, 2.8, HOLE) + ink_circle(32, 32, 6, HOLE) + ink_stroke("M42 12Q50 16 54 24", 3, HOLE)
    return fit(out, 0.783, 32.0, 32.0)


@reg("org.kde.calindori", AMBER_DEEP)
def calindori():
    out = ink_rrect(8, 14, 48, 42, 7) + ink_stroke("M8 28H56", 2.8, HOLE) + ink_rrect(19, 6, 6, 14, 3) + ink_rrect(39, 6, 6, 14, 3) + ink_rrect(15, 34, 8, 7, 1.5, HOLE) + ink_rrect(28, 34, 8, 7, 1.5, HOLE) + ink_rrect(41, 34, 8, 7, 1.5, HOLE) + ink_rrect(15, 45, 8, 7, 1.5, HOLE) + ink_rrect(28, 45, 8, 7, 1.5, HOLE)
    return fit(out, 0.647, 32.0, 31.0)


@reg("org.kde.calligra", PINK)
def calligra():
    out = path("M32 5L47 28Q47 41 32 58Q17 41 17 28Z", INK) + ink_stroke("M32 38V56", 3, HOLE) + ink_circle(32, 30, 4.2, HOLE)
    return fit(out, 0.686, 32.0, 31.5)


@reg("org.kde.dragonplayer", TEAL_DEEP)
def dragonplayer():
    out = ring_c(32, 32, 22, 5.2) + poly([(26, 22), (26, 42), (44, 32)], INK, 2.5)
    return fit(out, 0.735, 32.0, 32.0)


@reg("org.kde.drawy", GREY_DEEP)
def drawy():
    out = rot(ink_rrect(26, 4, 12, 36, 3) + poly([(26, 41), (38, 41), (32, 56)], INK, 1.5) + ink_stroke("M26 13H38", 2.8, HOLE), 40, 32, 32)
    return fit(out, 0.73, 34.5, 29.6)


@reg("org.kde.francis", BLUE)
def francis():
    out = ring_c(32, 37, 19, 5.2) + ink_rrect(26, 4, 12, 6, 2) + ink_rrect(30, 9, 4, 8, 1) + ink_stroke("M32 37V26", 4.4) + ink_stroke("M32 37L40 42", 4.4) + ink_stroke("M49 17L53 13", 4.4)
    return fit(out, 0.661, 32.9, 31.2)


@reg("org.kde.gcompris-teachers", ORANGE_DARK)
def gcompris_teachers():
    out = poly([(32, 10), (59, 25), (32, 40), (5, 25)], INK, 2.5) + path("M15 36V47Q32 58 49 47V36L32 44Z", INK) + ink_stroke("M55 28V44", 3.2) + ink_circle(55, 46, 3.4)
    return fit(out, 0.637, 32.0, 30.6)


@reg("org.kde.glaxnimate", PURPLE_DEEP)
def glaxnimate():
    out = ink_stroke("M12 48C12 12 52 12 52 48", 5.2) + ink_rrect(7, 43, 10, 10, 2) + ink_rrect(47, 43, 10, 10, 2) + ink_circle(32, 16, 4.6)
    return fit(out, 0.648, 32.0, 32.2)


@reg("org.kde.hana", ORANGE_DEEP)
def hana():
    out = "".join(ink_circle(*pt(32, 32, 13.5, -90 + 72 * k), 9.4) for k in range(5)) + ink_circle(32, 32, 5.6, HOLE)
    return fit(out, 0.809, 32.0, 30.6)


@reg("org.kde.iconexplorer", BLUE_GREY_DEEP)
def iconexplorer():
    out = ring_c(26, 26, 17, 5.2) + ink_stroke("M39 39L56 56", 7) + ink_rrect(18, 18, 7, 7, 1.5) + ink_rrect(27, 18, 7, 7, 1.5) + ink_rrect(18, 27, 7, 7, 1.5) + ink_circle(30.5, 30.5, 3.6)
    return fit(out, 0.571, 33.0, 33.0)


@reg("org.kde.itinerary", LIGHT_BLUE_DEEP)
def itinerary():
    out = ink_rrect(8, 19, 48, 37, 7) + ink_stroke("M23 19V14Q23 9 28 9H36Q41 9 41 14V19", 4.6) + ink_stroke("M8 35H56", 3, HOLE) + ink_rrect(28, 32, 8, 8, 2, HOLE)
    return fit(out, 0.653, 32.0, 31.4)


@reg("org.kde.kalm", DEEP_ORANGE_DEEP)
def kalm():
    out = pet(32, 52, 38, 12, -90) + pet(32, 52, 31, 11, -132) + pet(32, 52, 31, 11, -48) + pet(32, 52, 22, 9, -168) + pet(32, 52, 22, 9, -12)
    return fit(out, 0.818, 32.0, 34.4)


@reg("org.kde.kbackup", DEEP_PURPLE_LIGHT)
def kbackup():
    out = arc_arrow(32, 32, 22, -60, 235, 5.2, 8) + ink_stroke("M32 20V32L40 37", 4.6)
    return fit(out, 0.688, 32.0, 32.0)


@reg("org.kde.kcharselect", INDIGO_SOFT)
def kcharselect():
    out = ink_stroke("M12 50H26Q13 43 13 29Q13 11 32 11Q51 11 51 29Q51 43 38 50H52", 5.4)
    return fit(out, 0.67, 32.0, 30.5)


@reg("org.kde.kcolorchooser", RED_DARK)
def kcolorchooser():
    out = ink_circle(32, 32, 23)
    for k in range(6):
        p = pt(32, 32, 24, 30 + 60 * k)
        out += ink_stroke(f"M32 32L{f(p[0])} {f(p[1])}", 2.8, HOLE)
    out += ink_circle(32, 32, 8.5, HOLE)
    return fit(out, 0.783, 32.0, 32.0)


@reg("org.kde.kdiff3", CYAN_DEEP)
def kdiff3():
    out = ink_rrect(7, 9, 28, 38, 4.5) + ink_rrect(29, 18, 28, 38, 4.5, INK, hs(3)) + ink_stroke("M14 28H28", 3.6, HOLE) + ink_stroke("M37 37H51", 3.6, HOLE) + ink_stroke("M44 30V44", 3.6, HOLE)
    return fit(out, 0.633, 32.0, 32.5)


@reg("org.kde.keepsecret", BROWN)
def keepsecret():
    out = ink_stroke("M20 28V22Q20 8 32 8Q44 8 44 22V28", 5.6) + ink_rrect(11, 26, 42, 31, 7) + ink_circle(32, 38, 5.4, HOLE) + ink_rrect(29.8, 40, 4.4, 10, 2, HOLE)
    return fit(out, 0.673, 32.0, 31.1)


@reg("org.kde.kgeotag", INDIGO_DEEP)
def kgeotag():
    out = path("M32 59C18 43 12 35 12 25A20 20 0 0 1 52 25C52 35 46 43 32 59Z", INK) + ink_circle(32, 25, 8, HOLE)
    return fit(out, 0.67, 32.0, 31.9)


@reg("org.kde.kjournaldbrowser", AMBER_DEEP)
def kjournaldbrowser():
    out = ink_rrect(13, 7, 38, 50, 5) + path("M36 7V29L41.5 24L47 29V7Z", HOLE) + ink_stroke("M20 20H29", 3.2, HOLE) + ink_stroke("M20 30H29", 3.2, HOLE) + ink_stroke("M20 40H43", 3.2, HOLE)
    return fit(out, 0.698, 32.0, 32.0)


@reg("org.kde.klevernotes", PINK_DEEP)
def klevernotes():
    out = "".join(ink_circle(32 + dx, 28 + dy, 10.4) for dx, dy in ((-10.5, -10.5), (10.5, -10.5), (-10.5, 10.5), (10.5, 10.5))) + ink_stroke("M32 38Q38 50 50 55", 4.6) + ink_circle(32, 28, 3.8, HOLE)
    return fit(out, 0.655, 32.0, 32.1)


@reg("org.kde.kodaskanna", TEAL_LIGHT)
def kodaskanna():
    out = ink_stroke("M8 20V8H20", 4.6) + ink_stroke("M56 20V8H44", 4.6) + ink_stroke("M8 44V56H20", 4.6) + ink_stroke("M56 44V56H44", 4.6)
    for x, w in ((17, 4), (24, 3), (30, 7), (40, 3), (46, 4)):
        out += ink_rrect(x, 18, w, 28, 1.2)
    return fit(out, 0.568, 32.0, 32.0)


@reg("org.kde.kommit", GREY_DEEP)
def kommit():
    out = ink_stroke("M6 32H22", 5.4) + ink_stroke("M42 32H58", 5.4) + ring_c(32, 32, 10.5, 5.4)
    return fit(out, 0.626, 32.0, 32.0)


@reg("org.kde.komodo", BLUE_DARK)
def komodo():
    out = ink_stroke("M19 11V53", 7.4) + ink_stroke("M47 11L20 34", 7.4) + ink_stroke("M27 30L49 53", 7.4)
    return fit(out, 0.696, 34.0, 32.0)


@reg("org.kde.kongress", ORANGE_DEEP)
def kongress():
    out = bubble(6, 8, 32, 21) + mirror(bubble(8, 33, 30, 17))
    return fit(out, 0.628, 31.0, 33.9)


@reg("org.kde.ktrip", PURPLE)
def ktrip():
    out = ink_rrect(14, 7, 36, 41, 9) + ink_rrect(19, 13, 26, 14, 3, HOLE) + ink_circle(24, 38, 3.2, HOLE) + ink_circle(40, 38, 3.2, HOLE) + ink_stroke("M20 50L13 58", 4.6) + ink_stroke("M44 50L51 58", 4.6)
    return fit(out, 0.62, 32.0, 33.6)


@reg("org.kde.kwave", BROWN_LIGHT)
def kwave():
    out = ""
    for k, h in enumerate((10, 24, 40, 26, 46, 22, 12)):
        out += ink_rrect(9 + 7.4 * k, 32 - h / 2, 5, h, 2.5)
    return fit(out, 0.727, 33.8, 32.0)


@reg("org.kde.okular.kirigami", BLUE_GREY)
def kirigami():
    out = "".join(rot(poly([(32, 32), (32, 8), (55, 8)], INK, 1.5), a, 32, 32) for a in (0, 90, 180, 270))
    return fit(out, 0.604, 32.0, 32.0)


@reg("org.kde.optiimage", LIGHT_BLUE_DEEP)
def optiimage():
    out = ink_rrect(8, 12, 48, 40, 6) + ink_circle(22, 25, 5, HOLE) + poly([(8, 52), (24, 35), (34, 46), (42, 38), (56, 52)], HOLE)
    return fit(out, 0.714, 32.0, 32.0)


@reg("org.kde.peruse", DEEP_ORANGE_LIGHT)
def peruse():
    out = ink_rrect(7, 9, 25, 21, 3.5) + ink_rrect(36, 9, 21, 21, 3.5) + ink_rrect(7, 34, 17, 21, 3.5) + ink_rrect(28, 34, 29, 21, 3.5)
    return fit(out, 0.632, 32.0, 32.0)


@reg("org.kde.picmi", DEEP_PURPLE)
def picmi():
    rows = [".X.X.", "XXXXX", "XXXXX", ".XXX.", "..X.."]
    out = ""
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == "X":
                out += ink_rrect(8 + 10.4 * c, 9 + 10.4 * r, 8.6, 8.6, 1.8)
    return fit(out, 0.716, 33.1, 34.1)


@reg("org.kde.plasmatube", PURPLE_LIGHT)
def plasmatube():
    out = ink_rrect(5, 13, 54, 38, 13) + poly([(26, 23), (26, 41), (42, 32)], HOLE, 2.5)
    return fit(out, 0.667, 32.0, 32.0)


@reg("org.kde.qrca", RED_DEEP)
def qrca():
    out = ""
    for x, y in ((7, 7), (39, 7), (7, 39)):
        out += ink_rrect(x, y, 18, 18, 3) + ink_rrect(x + 4, y + 4, 10, 10, 1, HOLE) + ink_rrect(x + 6.5, y + 6.5, 5, 5, 1)
    out += ink_rrect(38, 38, 8, 8, 1.5) + ink_rrect(49, 38, 8, 8, 1.5) + ink_rrect(38, 49, 8, 8, 1.5) + ink_rrect(49, 49, 8, 8, 1.5)
    return fit(out, 0.592, 32.0, 32.0)


@reg("org.kde.ruqola", ORANGE_DARK)
def ruqola():
    out = path("M10 53Q6 20 42 8Q57 28 44 43Q30 56 10 53Z", INK) + ink_stroke("M13 50L40 21", 3.2, HOLE) + ink_stroke("M27 36L24 25", 2.8, HOLE) + ink_stroke("M33 29L44 29", 2.8, HOLE)
    return fit(out, 0.693, 29.8, 30.8)


@reg("org.kde.telly-skout", BROWN_DEEP)
def telly_skout():
    out = ink_rrect(7, 21, 50, 36, 6) + ink_rrect(12, 26, 32, 26, 3, HOLE) + ink_circle(50.5, 33, 3, HOLE) + ink_circle(50.5, 44, 3, HOLE) + ink_stroke("M22 8L32 18L42 8", 4.6)
    return fit(out, 0.618, 32.0, 31.4)


@reg("org.kde.vvave", INDIGO)
def vvave():
    out = ink_stroke("M7 24Q15 11 22 24T36 24T50 24T58 20", 5) + ink_stroke("M6 43Q13 31 21 43T35 43T49 43T58 38", 5)
    return fit(out, 0.632, 32.0, 33.2)


@reg("org.kekikakademi.eFatura", AMBER_DEEP)
def efatura():
    out = path("M13 6H51V58L45 52L38.5 58L32 52L25.5 58L19 52L13 58Z", INK) + ink_stroke("M22 18H42", 3.4, HOLE) + ink_stroke("M22 28H42", 3.4, HOLE) + ink_stroke("M22 38H34", 3.4, HOLE)
    return fit(out, 0.64, 32.0, 32.0)


@reg("org.keyoxide.Keyoxide", PINK_LIGHT)
def keyoxide():
    out = rot(ink_circle(17, 32, 12.5) + ink_circle(17, 32, 5, HOLE) + ink_rrect(27, 29, 29, 6, 3) + ink_rrect(41, 34, 6, 9, 1.5) + ink_rrect(50, 34, 6, 7, 1.5), -35, 32, 32)
    return fit(out, 0.735, 31.8, 35.0)


@reg("org.keystore_explorer.KeyStoreExplorer", TEAL)
def keystoreexplorer():
    out = ink_rrect(8, 8, 48, 44, 7) + ink_rrect(14, 51, 9, 7, 2) + ink_rrect(41, 51, 9, 7, 2) + ring_c(29, 30, 10.5, 3.4, HOLE) + ink_circle(29, 30, 3.2, HOLE) + ink_stroke("M48 24V36", 3.4, HOLE)
    return fit(out, 0.647, 32.0, 33.0)


@reg("org.koderoots.chatqt", GREY_DARK)
def chatqt():
    out = bubble(7, 8, 50, 33) + ink_stroke("M17 19H47", 3.6, HOLE) + ink_stroke("M17 29H36", 3.6, HOLE)
    return fit(out, 0.692, 32.0, 29.4)


@reg("org.koderoots.musik", BLUE_DEEP)
def musik():
    out = ink_circle(19, 47, 8) + ink_circle(45, 41, 8) + ink_rrect(24.5, 13, 4.6, 34, 1.5) + ink_rrect(50.5, 7, 4.6, 34, 1.5) + poly([(24.5, 13), (55, 7), (55, 16), (24.5, 22)], INK, 1.5)
    return fit(out, 0.626, 33.4, 30.6)


@reg("org.kryogenix.hushboard", ORANGE_DEEP)
def hushboard():
    out = ink_rrect(5, 15, 54, 36, 6)
    for k in range(5):
        out += ink_rrect(11 + 9.6 * k, 21, 6.2, 6.2, 1.2, HOLE) + ink_rrect(11 + 9.6 * k, 31, 6.2, 6.2, 1.2, HOLE)
    out += ink_rrect(19, 41, 26, 5, 2, HOLE)
    return fit(out, 0.667, 32.0, 33.0)


@reg("org.lamport.tla.toolbox", PURPLE_DEEP)
def toolbox():
    out = ink_rrect(7, 24, 50, 32, 6) + ink_stroke("M21 24V16Q21 11 26 11H38Q43 11 43 16V24", 4.6) + ink_stroke("M7 38H57", 3, HOLE) + ink_rrect(27.5, 34, 9, 9, 2, HOLE)
    return fit(out, 0.645, 32.0, 32.4)


@reg("org.libretrainsim.Libre-TrainSim", BLUE_GREY_LIGHT)
def libre_trainsim():
    out = ink_stroke("M26 8L10 56", 5.4) + ink_stroke("M38 8L54 56", 5.4) + ink_stroke("M24 16H40", 4) + ink_stroke("M20 28H44", 4) + ink_stroke("M14 44H50", 4.4)
    return fit(out, 0.582, 32.0, 32.0)


@reg("org.libvips.nip4", BLUE_GREY_DEEP)
def nip4():
    out = ink_stroke("M41 9V54", 8) + ink_stroke("M41 11L11 38H55", 8)
    return fit(out, 0.679, 33.0, 31.5)
