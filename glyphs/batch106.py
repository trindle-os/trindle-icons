# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 106: CubeTimer to Browser."""
from lm import (
    AMBER, BLUE, BLUE_DARK, BLUE_GREY, BROWN, CYAN_DEEP, DEEP_ORANGE, DEEP_PURPLE, f, GREY_DEEP,
    HOLE, INDIGO, INDIGO_SOFT, INK, LIGHT_BLUE_SOFT, ORANGE, path, PINK, poly, pt, PURPLE,
    RED_DEEP, TEAL, YELLOW_DARK,
)
from glyphs.kit import (
    bubble, dim, ell, fit, ink_circle, ink_stroke, petal, registry, ring_c, ink_rrect, star4_b)

ICONS, SMALL, reg, _ = registry()


@reg("xyz.aguno.CubeTimer", DEEP_PURPLE)
def cubetimer():
    out = "".join(ink_rrect(9 + 16 * x, 14 + 16 * y, 14, 14, 3.5) for x in range(3) for y in range(3))
    out += ink_rrect(26, 3, 12, 6, 2.5) + ink_rrect(30, 8, 4, 5, 1)
    return fit(out, 0.541, 32.0, 31.5)


@reg("xyz.audiostellar.AudioStellar", CYAN_DEEP)
def audiostellar():
    out = star4_b(29, 35, 25) + ink_circle(29, 35, 5, HOLE) + star4_b(51, 13, 9)
    return fit(out, 0.559, 32.0, 32.0)


@reg("xyz.hyperplay.HyperPlay", DEEP_ORANGE)
def hyperplay():
    out = poly([(24, 8), (56, 32), (24, 56)], INK, 5) + ink_rrect(4, 22, 12, 5, 2.5) + ink_rrect(4, 30, 16, 5, 2.5) + ink_rrect(4, 38, 12, 5, 2.5)
    return fit(out, 0.664, 31.2, 32.0)


@reg("xyz.mx_moment.moment", TEAL)
def moment():
    out = poly([(16, 10), (48, 10), (32, 32)], INK, 3) + poly([(32, 32), (16, 54), (48, 54)], INK, 3)
    out += ink_rrect(11, 3, 42, 7, 3.5) + ink_rrect(11, 54, 42, 7, 3.5) + poly([(32, 41), (25, 50), (39, 50)], HOLE, 1)
    return fit(out, 0.553, 32.0, 32.0)


@reg("xyz.nokarin.FrameExtractor", PINK)
def frameextractor():
    out = ink_rrect(5, 11, 54, 42, 6)
    out += "".join(ink_rrect(9, y, 5, 6, 1.5, HOLE) + ink_rrect(50, y, 5, 6, 1.5, HOLE) for y in (17, 29, 41))
    out += ink_rrect(19, 17, 26, 30, 3, HOLE) + poly([(28, 24), (40, 32), (28, 40)], INK, 2)
    return fit(out, 0.598, 32.0, 32.0)


@reg("xyz.nokarin.aqloss", BLUE)
def aqloss():
    out = ink_circle(32, 32, 26) + ink_stroke("M13 32Q19 18 25 32T37 32T49 32", 4.6, HOLE)
    return fit(out, 0.73, 32.0, 32.0)


@reg("xyz.parlatype.Parlatype", YELLOW_DARK)
def parlatype():
    out = bubble(5, 6, 54, 38) + ink_rrect(13, 15, 38, 4.4, 2.2, HOLE) + ink_rrect(13, 24, 26, 4.4, 2.2, HOLE) + ink_rrect(13, 33, 32, 4.4, 2.2, HOLE)
    return fit(out, 0.58, 32.0, 29.9)


@reg("xyz.rescribe.rescribe", PURPLE)
def rescribe():
    out = path("M32 58L19 39Q8 24 17 8H47Q56 24 45 39Z", INK) + ink_circle(32, 27, 4.8, HOLE) + ink_stroke("M32 33V55", 3.4, HOLE)
    return fit(out, 0.658, 32.0, 32.9)


@reg("xyz.riothedev.emojify", AMBER)
def emojify():
    out = ink_circle(32, 32, 26) + ell(23, 26, 3.6, 5, HOLE) + ell(41, 26, 3.6, 5, HOLE) + ink_stroke("M19 38Q32 52 45 38", 4.6, HOLE)
    return fit(out, 0.73, 32.0, 32.0)


@reg("xyz.rust4diva.Rust4Diva", RED_DEEP)
def rust4diva():
    out = poly([(9, 46), (9, 20), (21, 31), (32, 14), (43, 31), (55, 20), (55, 46)], INK, 4)
    out += ink_rrect(9, 47, 46, 9, 3.5) + ink_circle(9, 17, 4.2) + ink_circle(32, 10, 4.2) + ink_circle(55, 17, 4.2) + ink_circle(32, 37, 3.8, HOLE)
    return fit(out, 0.584, 32.0, 30.9)


@reg("xyz.safeworlds.midiconn", INDIGO_SOFT)
def midiconn():
    out = ring_c(19, 32, 12, 6) + ring_c(45, 32, 12, 6) + ink_stroke("M28 32H36", 5)
    return fit(out, 0.68, 32.0, 32.0)


@reg("xyz.slothlife.Diveboard", BLUE_DARK)
def diveboard():
    out = ink_rrect(4, 18, 56, 32, 13) + ink_rrect(10, 24, 19, 20, 8, HOLE) + ink_rrect(35, 24, 19, 20, 8, HOLE) + ink_stroke("M54 18V6", 5)
    return fit(out, 0.581, 32.0, 26.8)


@reg("xyz.slothlife.Jogger", ORANGE)
def jogger():
    out = ink_circle(41, 9, 6) + ink_stroke("M38 19L30 34", 6.4) + ink_stroke("M36 22L24 26L22 36", 4.8) + ink_stroke("M36 22L48 28L54 22", 4.8)
    out += ink_stroke("M30 34L43 41L41 56", 6) + ink_stroke("M30 34L21 47L8 49", 6)
    return fit(out, 0.594, 30.8, 31.0)


@reg("xyz.splashmapper.Splash", INDIGO)
def splash():
    out = ink_circle(32, 32, 11) + "".join(petal(32, 32, 27 if k % 2 == 0 else 21, 6.5, 45 * k) for k in range(8))
    return fit(out, 0.714, 32.0, 32.0)


@reg("xyz.stuerz.BilligSweeper", BLUE_GREY)
def billigsweeper():
    out = ink_circle(32, 32, 15) + "".join(ink_stroke(f"M{f(pt(32, 32, 15, a)[0])} {f(pt(32, 32, 15, a)[1])}L{f(pt(32, 32, 25, a)[0])} {f(pt(32, 32, 25, a)[1])}", 5.4) for a in range(0, 360, 45))
    out += ink_circle(26, 26, 3.8, HOLE)
    return fit(out, 0.688, 32.0, 32.0)


@reg("xyz.tytanium.DoorKnocker", BROWN)
def doorknocker():
    out = path("M12 58V26Q12 6 32 6Q52 6 52 26V58Z", INK) + ink_circle(32, 22, 3.6, HOLE) + ring_c(32, 36, 8.5, 3.8, HOLE) + ink_rrect(27, 48, 10, 4, 2, HOLE)
    return fit(out, 0.582, 32.0, 32.0)


@reg("xyz.woxel.Woxel", LIGHT_BLUE_SOFT)
def woxel():
    out = poly([(32, 5), (57, 19), (32, 33), (7, 19)], INK, 2)
    out += dim(poly([(7, 24), (30, 37), (30, 61), (7, 48)], INK, 2), .65) + dim(poly([(34, 37), (57, 24), (57, 48), (34, 61)], INK, 2), .4)
    return fit(out, 0.631, 32.0, 33.0)


@reg("zone.dos.Browser", GREY_DEEP)
def browser():
    out = ink_rrect(5, 9, 54, 46, 7) + ink_rrect(11, 15, 22, 4.4, 2.2, HOLE) + ink_rrect(10, 26, 44, 23, 3, HOLE)
    out += ink_stroke("M17 31L24 37.5L17 44", 3.8) + ink_stroke("M29 44H40", 3.8)
    return fit(out, 0.583, 32.0, 32.0)
