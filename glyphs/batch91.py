# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 91: the sixth hundred apps from the gap list (flags/app-gap-list-full.md),
rows 501 to 600, easyroam to subscribi. Each is a simple original mark on its own tile."""
from lm import *
from glyphs.kit import (
    arrowhead, dim, ell, fit_b, H, I, ink_circle, ink_stroke, registry, ring_c, rot, star4,
    star5,
)

ICONS, SMALL, reg, _ = registry()

@reg("de.easyroam.easyroam", PURPLE)
def easyroam():
    out = ink_circle(32, 42, 4.5, I) + ink_stroke("M23.5 33.5A12 12 0 0 1 40.5 33.5", 4.6) + ink_stroke("M16.4 26.4A22 22 0 0 1 47.6 26.4", 4.6)
    return fit_b(out + line(14, 54, 50, 54, I, 3.6) + arrowhead(14, 54, -1, 0, 5) + arrowhead(50, 54, 1, 0, 5), 0.58)

@reg("de.fabrik19.mos-Launcher", DEEP_PURPLE)
def moslauncher():
    out = rrect(10, 10, 18, 18, 4, I) + rrect(10, 34, 18, 18, 4, I) + rrect(34, 34, 18, 18, 4, I)
    return fit_b(out + ink_stroke("M38 14H50V26", 5) + ink_stroke("M50 14L36 28", 5), 0.68)

@reg("de.flose.Kochbuch", GREY)
def kochbuch():
    out = rrect(14, 28, 36, 24, 5, I) + rrect(11, 22, 42, 7, 3.5, I) + rrect(28, 15, 8, 7, 3, I)
    out += rrect(5, 33, 9, 5, 2.5, I) + rrect(50, 33, 9, 5, 2.5, I) + line(21, 41, 43, 41, H, 2.6)
    return fit_b(out + ink_stroke("M22 12Q19 8 22 4", 3) + ink_stroke("M42 12Q39 8 42 4", 3), 0.68)

@reg("de.gonicus.bubbles", BLUE_DARK)
def bubbles():
    return fit_b(ring_c(24, 38, 13, 4.6) + ring_c(45, 22, 9, 4.2) + ring_c(44, 47, 6, 3.8) + ink_stroke("M16 33A9 9 0 0 1 22 28", 2.8), 0.7)

@reg("de.gonicus.gonnect", AMBER_LIGHT)
def gonnect():
    return fit_b(ink_stroke("M18 18C16 36 26 48 46 46", 8) + ink_circle(18, 17, 6) + ink_circle(47, 46, 6)
               + ink_stroke("M34 14A16 16 0 0 1 50 30", 3.8) + ink_stroke("M34 22A8 8 0 0 1 42 30", 3.8), 0.72)

@reg("de.haeckerfelix.AudioSharing", PINK_DEEP)
def audiosharing():
    out = ink_circle(26, 44, 7) + line(32, 44, 32, 14, I, 4.6) + poly([(32, 12), (45, 18), (45, 27), (32, 21)], I, 1.2)
    return fit_b(out + ink_stroke("M12 33Q6 41 12 49", 3.6) + ink_stroke("M52 33Q58 41 52 49", 3.6), 0.68)

@reg("de.halaszovich.PMbrowser", TEAL_DEEP)
def pmbrowser():
    return fit_b(ring_c(32, 30, 18, 4.8) + ink_stroke("M18 30C22 19 27 19 32 30S42 41 46 30", 4.2) + line(32, 8, 32, 12, I, 3.2), 0.85)

@reg("de.helden_software.helden5", BROWN_DEEP)
def helden5():
    out = path("M14 12H50V32Q50 46 32 54Q14 46 14 32Z", I)
    return fit_b(out + line(32, 18, 32, 44, H, 3.4) + line(24, 26, 40, 26, H, 3.4) + poly([(32, 48), (29.5, 42), (34.5, 42)], H, .6), 0.79)

@reg("de.hohnstaedt.xca", INDIGO)
def xca():
    out = rrect(8, 12, 48, 34, 4, I) + line(16, 22, 40, 22, H, 3) + line(16, 30, 30, 30, H, 3)
    out += poly([(39, 48), (36, 58), (42, 55), (46, 59), (48, 49)], I, 1)
    out += ink_circle(44, 42, 8.5, I, f' stroke="{H}" stroke-width="2.4"') + ink_circle(44, 42, 3.2, H)
    return fit_b(out, 0.61)

@reg("de.hummdudel.Libellus", YELLOW_LIGHT)
def libellus():
    out = rrect(16, 12, 32, 34, 3, I)
    for y in (24, 31, 38):
        out += line(22, y, 42 if y != 38 else 34, y, H, 3)
    out += rrect(10, 7, 44, 10, 5, I, f' stroke="{H}" stroke-width="2.2"') + rrect(10, 41, 44, 10, 5, I, f' stroke="{H}" stroke-width="2.2"')
    return fit_b(out, 0.67)

@reg("de.informationsanarchistik.teapot.megamichi.berrypaper", RED_DEEP)
def berrypaper():
    out = path("M32 54C16 46 10 32 14 24Q32 16 50 24C54 32 48 46 32 54Z", I)
    leaf = path("M32 22L22 14L29 18L32 8L35 18L42 14Z", I, f' stroke="{H}" stroke-width="2.2" stroke-linejoin="round"')
    for x, y in ((24, 32), (32, 30), (40, 32), (28, 40), (36, 40), (32, 47)):
        out += ell(x, y, 1.7, 2.5, H)
    return fit_b(out + leaf, 0.84)

@reg("de.informationsanarchistik.teapot.megamichi.duckrun", CYAN)
def duckrun():
    out = ell(30, 38, 18, 11) + line(40, 28, 37, 34, I, 10) + ink_circle(42, 21, 9) + poly([(49, 19), (58, 23), (49, 27)], I, 1)
    out += poly([(14, 33), (5, 27), (11, 40)], I, 1.2) + ink_circle(44, 19, 2, H) + ink_stroke("M22 38Q30 44 38 36", 2.8, H)
    return fit_b(out + line(25, 48, 22, 56, I, 3.4) + line(35, 48, 38, 56, I, 3.4) + line(18, 56, 26, 56, I, 3) + line(34, 56, 42, 56, I, 3), 0.64)

@reg("de.leopoldluley.Clapgrep", DEEP_ORANGE_LIGHT)
def clapgrep():
    out = ring_c(26, 26, 16, 5.2) + line(38, 38, 53, 53, I, 7)
    for a in (0, 60, 120):
        x1, y1 = pt(26, 26, 7, a)
        x2, y2 = pt(26, 26, 7, a + 180)
        out += line(x1, y1, x2, y2, I, 3.2)
    return fit_b(out, 0.58)

@reg("de.lernsoftware_filius.Filius", DEEP_PURPLE)
def filius():
    out = rrect(20, 8, 24, 12, 3, I) + ink_circle(27, 14, 1.8, H) + ink_circle(37, 14, 1.8, H)
    out += ink_stroke("M32 20V28M32 28H16V36M32 28H48V36", 3.4)
    out += rrect(6, 36, 20, 14, 3, I) + rrect(38, 36, 20, 14, 3, I) + rrect(13, 50, 6, 4, 1, I) + rrect(45, 50, 6, 4, 1, I)
    return fit_b(out + rrect(10, 40, 12, 6, 1, H) + rrect(42, 40, 12, 6, 1, H), 0.63)

@reg("de.linuxguides.RechnungsAssistent", AMBER_DARK)
def rechnung():
    out = path("M16 8H48V54L43 50L38 54L32 50L26 54L21 50L16 54Z", I)
    return fit_b(out + ink_stroke("M39 24A8 8 0 1 0 39 38", 3.4, H) + line(21, 28, 34, 28, H, 2.8) + line(21, 34, 34, 34, H, 2.8) + line(22, 44, 42, 44, H, 2.6), 0.7)

@reg("de.marlam.gencolormap", BLUE_GREY)
def gencolormap():
    out = ""
    for i in range(3):
        for j in range(3):
            out += dim(rrect(10 + i * 15, 10 + j * 15, 13, 13, 3.4, I), round(.3 + .7 * (i + j) / 4, 2))
    return fit_b(out, 0.66)

@reg("de.marlam.qv", LIGHT_BLUE_DARK)
def qv():
    out = rrect(6, 12, 52, 38, 6, I) + rrect(11, 17, 42, 28, 3, H)
    return fit_b(out + path("M17 31Q32 15 47 31Q32 47 17 31Z", I) + ink_circle(32, 31, 5.4, H) + ink_circle(32, 31, 2.4, I), 0.66)

@reg("de.mediathekview.MediathekView", ORANGE_LIGHT)
def mediathek():
    out = rrect(8, 18, 48, 32, 6, I) + rrect(13, 23, 38, 22, 3, H) + poly([(28, 28), (28, 40), (40, 34)], I, 1.2)
    return fit_b(out + line(24, 55, 40, 55, I, 4) + ink_stroke("M23 7L32 16L41 7", 3.4), 0.69)

@reg("de.nagstamon.nagstamon", PURPLE_DEEP)
def nagstamon():
    return fit_b(poly([(32, 8), (57, 51), (7, 51)], I, 5) + line(32, 24, 32, 36, H, 4.6) + ink_circle(32, 43, 2.8, H), 0.57)

@reg("de.nicokimmel.shadowcast-electron", BROWN_LIGHT)
def shadowcast():
    return fit_b(ink_stroke("M10 22V14H54V46H34", 4.6) + ink_circle(10, 46, 3.6) + ink_stroke("M10 34A12 12 0 0 1 22 46", 4.6) + ink_stroke("M10 24A22 22 0 0 1 32 46", 4.6), 0.65)

@reg("de.philippun1.Snoop", GREY_LIGHT)
def snoop():
    out = rrect(8, 40, 48, 14, 4, I) + ell(21, 27, 9, 10) + ell(43, 27, 9, 10)
    return fit_b(out + ink_circle(24, 26, 4.2, H) + ink_circle(46, 26, 4.2, H), 0.62)

@reg("de.philippun1.turtle", BLUE_DEEP)
def turtle():
    out = path("M10 42C10 22 54 22 54 42Z", I) + rrect(15, 40, 10, 10, 3, I) + rrect(39, 40, 10, 10, 3, I)
    out += ink_circle(57, 36, 6) + poly([(8, 40), (1, 44), (9, 46)], I, 1) + ink_circle(59, 34, 1.6, H)
    return fit_b(out + ink_stroke("M32 27V41M22 30L19 41M42 30L45 41", 2.6, H), 0.58)

@reg("de.renew.Renew", AMBER_DEEP)
def renew():
    out = ring_c(13, 28, 8, 4.2) + ink_circle(13, 28, 2.6) + rrect(28, 17, 8, 22, 1.5, I) + ring_c(51, 28, 8, 4.2)
    out += line(22, 28, 26, 28, I, 3.2) + arrowhead(24, 28, 1, 0, 4) + line(37, 28, 40, 28, I, 3.2) + arrowhead(39, 28, 1, 0, 4)
    return fit_b(out + ink_stroke("M13 38V51H51V40", 3.2) + arrowhead(51, 41, 0, -1, 4.6), 0.67)

@reg("de.schmidhuberj.DieBahn", PINK_DEEP)
def diebahn():
    out = path("M6 42V27Q6 20 14 20H34Q49 20 58 38V42Z", I)
    for x in (11, 21, 31):
        out += rrect(x, 25, 7, 7, 1.6, H)
    out += poly([(40, 24), (50, 33), (40, 33)], H, .6) + line(6, 37, 56, 37, H, 2)
    out += ink_circle(17, 46, 4.4) + ink_circle(38, 46, 4.4) + line(4, 53, 60, 53, I, 3.4)
    return fit_b(out, 0.53)

@reg("de.scrylab.ScryLab", TEAL)
def scrylab():
    out = ink_circle(32, 26, 16, I) + ink_stroke("M22 22A10 10 0 0 1 28 16", 3, H) + star4(35, 30, 5, H)
    out += poly([(20, 50), (44, 50), (38, 41), (26, 41)], I, 1.4) + rrect(16, 49, 32, 6, 3, I)
    return fit_b(out + star4(51, 10, 6), 0.62)

@reg("de.sesu8642.feudaltactics", BROWN_LIGHT)
def feudal():
    out = path("M14 54V18H21V24H27V18H37V24H43V18H50V54Z", I) + path("M26 54V44A6 6 0 0 1 38 44V54Z", H)
    out += rrect(30, 28, 4, 8, 2, H) + line(32, 4, 32, 16, I, 2.8) + poly([(32, 4), (43, 8), (32, 12)], I, .8)
    return fit_b(out, 0.67)

@reg("de.swsnr.turnon", INDIGO)
def turnon():
    return fit_b(ink_stroke("M22 14A19 19 0 1 0 42 14", 5.6) + line(32, 6, 32, 30, I, 5.6) + rrect(24, 54, 16, 5, 2.5, I), 0.68)

@reg("de.syping.gta5view", YELLOW_DARK)
def gta5view():
    out = path("M5 42V35Q5 31 9 31H15L22 20H42L50 31Q59 32 59 37V42Z", I)
    out += poly([(24, 23), (40, 23), (45, 30), (19, 30)], H, .6) + line(32, 23, 32, 30, I, 2)
    out += ink_circle(18, 43, 7.4, I, f' stroke="{H}" stroke-width="2.6"') + ink_circle(46, 43, 7.4, I, f' stroke="{H}" stroke-width="2.6"')
    return fit_b(out + ink_circle(18, 43, 2.4, H) + ink_circle(46, 43, 2.4, H), 0.68)

@reg("de.thejackimonster.ChuckleExpress", RED)
def chuckle():
    out = ink_circle(32, 30, 21, I) + ink_stroke("M17 27Q22 19 28 26", 3.2, H) + ink_stroke("M36 26Q42 19 47 27", 3.2, H)
    return fit_b(out + path("M19 34H45Q45 49 32 49Q19 49 19 34Z", H) + ell(32, 46, 6, 3, I), 0.95)

@reg("de.til7701.Puzzled", CYAN_DARK)
def puzzled():
    out = rrect(14, 20, 32, 32, 3, I) + ink_circle(30, 18, 6.4) + ink_circle(48, 36, 6.4) + ink_circle(14, 36, 6.4, H) + ink_circle(30, 52, 6.4, H)
    return fit_b(out, 0.74)

@reg("de.turtle_coding_gbr.turtlements", DEEP_ORANGE_DARK)
def turtlements():
    return fit_b(ink_stroke("M10 12H54V52H18V28H42V40H30", 4.6) + arrowhead(30, 40, -1, 0, 7.5), 0.6)

@reg("de.wagnermartin.Plattenalbum", DEEP_PURPLE)
def plattenalbum():
    out = rrect(6, 20, 36, 36, 3, I) + line(12, 47, 26, 47, H, 3) + line(12, 52, 20, 52, H, 3)
    out += ink_circle(40, 26, 21, I, f' stroke="{H}" stroke-width="2.8"') + ring_c(40, 26, 13, 1.8, H) + ink_circle(40, 26, 6, H) + ink_circle(40, 26, 2, I)
    return fit_b(out, 0.57)

@reg("de.wger.flutter", ORANGE_DARK)
def wger():
    out = rrect(24, 28, 16, 4.4, 1, I) + rrect(16, 15, 8, 30, 3, I) + rrect(8, 21, 6, 18, 2.5, I)
    out += rrect(40, 15, 8, 30, 3, I) + rrect(50, 21, 6, 18, 2.5, I)
    return fit_b(rot(out, -35), 0.8)

@reg("de.willuhn.Jameica", BLUE_GREY_LIGHT)
def jameica():
    out = rrect(6, 14, 52, 38, 5, I) + rrect(6, 23, 52, 8, 0, H) + rrect(12, 37, 11, 8, 2, H) + line(30, 41, 50, 41, H, 3.2)
    return fit_b(out, 0.62)

@reg("de.wwwtech.gitte", LIGHT_BLUE_DEEP)
def gitte():
    out = rrect(8, 8, 48, 48, 6, I) + line(8, 32, 56, 32, H, 2.4)
    out += line(14, 20, 26, 20, H, 3.6) + line(20, 14, 20, 26, H, 3.6) + line(33, 20, 50, 20, H, 3.2)
    out += line(14, 44, 26, 44, H, 3.6) + line(33, 44, 50, 44, H, 3.2)
    return fit_b(out, 0.61)

@reg("de.z_ray.Facetracker", ORANGE_DEEP)
def facetracker():
    out = ink_stroke("M8 20V8H20", 3.8) + ink_stroke("M44 8H56V20", 3.8) + ink_stroke("M8 40V52H20", 3.8) + ink_stroke("M44 52H56V40", 3.8)
    out += ell(32, 30, 10, 13) + ink_circle(28, 27, 2, H) + ink_circle(36, 27, 2, H) + line(28.5, 37, 35.5, 37, H, 2.4)
    return fit_b(out, 0.58)

@reg("de.z_ray.OptimusUI", PURPLE_DEEP)
def optimus():
    out = rrect(14, 14, 36, 36, 5, I)
    for p in (22, 32, 42):
        out += line(p, 6, p, 14, I, 3.4) + line(p, 50, p, 58, I, 3.4) + line(6, p, 14, p, I, 3.4) + line(50, p, 58, p, I, 3.4)
    return fit_b(out + line(21, 26, 38, 26, H, 3) + arrowhead(38, 26, 1, 0, 4.6, H) + line(43, 37, 26, 37, H, 3) + arrowhead(26, 37, -1, 0, 4.6, H), 0.64)

@reg("de.zwarf.picplanner", BLUE_GREY_LIGHT)
def picplanner():
    out = rrect(8, 12, 48, 42, 6, I) + rrect(17, 6, 6, 12, 3, I, f' stroke="{H}" stroke-width="1.8"') + rrect(41, 6, 6, 12, 3, I, f' stroke="{H}" stroke-width="1.8"')
    out += ink_circle(32, 35, 14, H) + ink_circle(32, 35, 9.5, I) + ink_circle(32, 35, 3.4, H)
    for a in (0, 120, 240):
        x, y = pt(32, 35, 9.5, a + 30)
        out += line(32, 35, x, y, H, 2)
    return fit_b(out, 0.64)

@reg("dev.aa55.yetty", GREY_LIGHT)
def yetty():
    out = ink_circle(32, 31, 14)
    for a in range(9):
        out += ink_circle(*pt(32, 31, 15, a * 40)[:2], 6, I)
    return fit_b(out + ell(25.5, 29, 2.8, 3.6, H) + ell(38.5, 29, 2.8, 3.6, H) + ink_stroke("M26 39Q32 43 38 39", 3, H), 0.91)

@reg("dev.aadhil.devtpro", BLUE)
def devtpro():
    out = ink_circle(32, 16, 10.5) + rrect(28, 4, 8, 12, 0, H) + rrect(28, 22, 8, 28, 3, I) + ink_circle(32, 52, 6.6) + ink_circle(32, 52, 2.8, H)
    return fit_b(rot(out, 40), 0.7)

@reg("dev.andy128k.Hearts", AMBER)
def hearts():
    heart = "M32 44L21 33Q16 26 22 22Q28 19 32 26Q36 19 42 22Q48 26 43 33Z"
    return fit_b(rrect(15, 8, 34, 48, 5, I) + path(heart, H) + path("M23 18L19 14Q18 12 20 11Q22 10 23 12Q24 10 26 11Q28 12 27 14Z", H), 0.68)

@reg("dev.appoutlet.DisCorkie", PINK_LIGHT)
def discorkie():
    out = rrect(19, 26, 26, 30, 6, I) + rrect(26, 10, 12, 22, 3, I) + rrect(26, 4, 12, 9, 2.4, I) + line(26, 14, 38, 14, H, 2.4)
    return fit_b(out + rrect(24, 38, 16, 11, 2, H) + star4(52, 12, 7) + star4(11, 20, 5), 0.61)

@reg("dev.bambosh.UnofficialHomestuckCollection", TEAL)
def homestuck():
    out = rrect(42, 10, 7, 14, 1, I) + poly([(7, 30), (32, 8), (57, 30)], I, 2.6) + rrect(14, 28, 36, 26, 2, I)
    return fit_b(out + rrect(27, 38, 10, 16, 2, H) + rrect(18, 33, 6, 6, 1, H) + rrect(40, 33, 6, 6, 1, H), 0.68)

@reg("dev.bragefuglseth.Fretboard", BROWN_DARK)
def fretboard():
    out = line(10, 10, 54, 10, I, 6.4)
    for x in (13, 24.3, 35.7, 47):
        out += line(x, 10, x, 54, I, 3)
    for y in (24, 38, 52):
        out += line(11, y, 49, y, I, 3)
    ring_ = f' stroke="{H}" stroke-width="2.4"'
    return fit_b(out + ink_circle(30, 31, 5, I, ring_) + ink_circle(41, 45, 5, I, ring_), 0.61)

@reg("dev.creeperkatze.full-steam-ahead", INDIGO)
def steam():
    out = rrect(6, 26, 32, 18, 4, I) + rrect(38, 16, 16, 28, 2, I) + rrect(42, 21, 8, 9, 1.5, H)
    out += rrect(11, 14, 8, 12, 1, I) + rrect(9, 11, 12, 5, 2.5, I) + rrect(26, 22, 7, 5, 2, I)
    for x in (15, 29, 46):
        out += ink_circle(x, 48, 6, I, f' stroke="{H}" stroke-width="2"') + ink_circle(x, 48, 1.8, H)
    return fit_b(out + line(3, 56, 60, 56, I, 3) + ink_circle(14, 6, 3.4) + ink_circle(7, 2, 2.4), 0.5)

@reg("dev.de4th.jazz2", YELLOW_DARK)
def jazz2():
    out = ell(23, 14, 5, 13) + ell(41, 14, 5, 13) + ell(23, 15, 2, 8, H) + ell(41, 15, 2, 8, H) + ell(32, 38, 15, 14)
    return fit_b(out + ink_circle(26, 35, 2.4, H) + ink_circle(38, 35, 2.4, H) + poly([(29.5, 41), (34.5, 41), (32, 44)], H, 1) + ink_stroke("M28 48Q32 51 36 48", 2.4, H), 0.66)

@reg("dev.deimoshall.DecryptIt", RED_LIGHT)
def decryptit():
    out = rrect(14, 28, 36, 26, 5, I) + ink_stroke("M22 28V19A10 10 0 0 1 42 19V23", 5.4) + ink_circle(32, 38, 4.2, H) + rrect(30, 38, 4, 9, 1.5, H)
    return fit_b(out, 0.71)

@reg("dev.deimoshall.Metamorphosis", CYAN_DEEP)
def metamorphosis():
    sq = rrect(4, 20, 20, 20, 3.4, "none", f' stroke="{I}" stroke-width="4.4"')
    return fit_b(sq + ring_c(51, 30, 10, 4.4) + line(28, 30, 38, 30, I, 3.6) + arrowhead(38, 30, 1, 0, 5.5), 0.64)

@reg("dev.dergs.Tonearm", DEEP_ORANGE_DEEP)
def tonearm():
    out = dim(ink_circle(24, 38, 18, I), .38) + ink_circle(46, 14, 9.4) + ink_circle(46, 14, 3.4, H) + ink_stroke("M46 24V36L30 49", 4.6)
    return fit_b(out + rot(rrect(21, 47, 13, 6, 2, I), 30, 28, 50) + rrect(43, 2, 6, 4, 1, I), 0.62)

@reg("dev.diegovsky.Riff", DEEP_PURPLE_DEEP)
def riff():
    out = path("M32 8C47 8 55 18 51 31C47 43 38 52 32 55C26 52 17 43 13 31C9 18 17 8 32 8Z", I)
    return fit_b(out + ink_stroke("M21 28L26.5 39L32 21L37.5 39L43 28", 3.4, H), 0.8)

@reg("dev.edfloreshz.Calculator", LIGHT_BLUE_DEEP)
def calculator():
    out = rrect(8, 8, 48, 48, 8, I)
    out += line(15, 21, 27, 21, H, 3.8) + line(21, 15, 21, 27, H, 3.8) + line(37, 21, 49, 21, H, 3.8)
    out += line(16, 37, 26, 47, H, 3.8) + line(26, 37, 16, 47, H, 3.8)
    out += line(37, 42, 49, 42, H, 3.8) + ink_circle(43, 36, 2.2, H) + ink_circle(43, 48, 2.2, H)
    return fit_b(out, 0.62)

@reg("dev.edfloreshz.Tasks", BLUE_GREY_DEEP)
def tasks():
    out = ""
    for x, n in ((8, 3), (25, 2), (42, 1)):
        for k in range(n):
            out += rrect(x, 10 + k * 15, 14, 12, 3, I)
    return fit_b(out, 0.64)

@reg("dev.ensoft.ecode", LIGHT_BLUE_DEEP)
def ecode():
    out = ink_stroke("M25 10Q17 10 17 18V24Q17 30 10 30Q17 30 17 36V42Q17 50 25 50", 4.6) + ink_stroke("M39 10Q47 10 47 18V24Q47 30 54 30Q47 30 47 36V42Q47 50 39 50", 4.6)
    return fit_b(out + line(32, 20, 32, 40, I, 3.8), 0.81)

@reg("dev.fishies.godl", ORANGE)
def godl():
    return fit_b(ink_stroke("M45.8 18.4A18 18 0 1 0 49.7 33.1H34", 6), 0.95)

@reg("dev.ftb.ftb-app", PURPLE_LIGHT)
def ftbapp():
    out = poly([(13, 20), (8, 5), (25, 16)], I, 1.4) + poly([(51, 20), (56, 5), (39, 16)], I, 1.4) + rrect(12, 16, 40, 36, 7, I)
    out += rrect(19, 26, 9, 9, 1.5, H) + rrect(36, 26, 9, 9, 1.5, H) + rrect(19, 40, 26, 6, 1, H)
    return fit_b(out + poly([(22, 40), (28, 40), (25, 45)], I, .5) + poly([(36, 40), (42, 40), (39, 45)], I, .5), 0.57)

@reg("dev.geopjr.Archives", GREY)
def archives():
    out = rrect(14, 6, 36, 50, 4, I)
    for k, y in enumerate((9, 15, 21)):
        out += rrect(25 if k % 2 == 0 else 32, y, 7, 5.2, 1, H)
    return fit_b(out + rrect(26, 28, 12, 16, 3.4, H) + rrect(29.4, 34, 5.2, 6, 1.2, I), 0.67)

@reg("dev.geopjr.Calligraphy", GREY_DARK)
def calligraphy():
    out = path("M24 8H40L48 26Q46 40 32 56Q18 40 16 26Z", I) + ink_circle(32, 28, 4.2, H) + line(32, 31, 32, 50, H, 2.8)
    return fit_b(out + line(24, 18, 40, 18, H, 2.4), 0.77)

@reg("dev.geopjr.Turntable", BLUE)
def turntable():
    out = rrect(8, 8, 48, 48, 6, I) + ink_circle(29, 33, 17, H) + ink_circle(29, 33, 8, I) + ink_circle(29, 33, 2.4, H)
    return fit_b(out + ink_circle(50, 15, 3.4, H) + line(50, 15, 50, 40, H, 3), 0.61)

@reg("dev.hdos.HDOS", AMBER_DARK)
def hdos():
    out = poly([(18, 10), (46, 10), (58, 24), (32, 54), (6, 24)], I, 2)
    return fit_b(out + ink_stroke("M6 24H58", 2.2, H) + ink_stroke("M18 10L24 24L32 54L40 24L46 10", 2.2, H) + ink_stroke("M24 24L32 10L40 24", 2.2, H), 0.72)

@reg("dev.heppen.webapps", PINK_LIGHT)
def webapps():
    out = rrect(8, 10, 48, 44, 6, I) + line(8, 22, 56, 22, H, 2.4) + ink_circle(15, 16, 1.8, H) + ink_circle(21, 16, 1.8, H)
    out += rrect(14, 28, 15, 10, 2, H) + rrect(35, 28, 15, 10, 2, H) + rrect(14, 42, 15, 7, 2, H) + rrect(35, 42, 15, 7, 2, H)
    return fit_b(out, 0.64)

@reg("dev.ibrahimcetin.reins", TEAL)
def reins():
    out = ring_c(13, 42, 8.5, 4.4) + ring_c(51, 42, 8.5, 4.4) + line(21.5, 42, 42.5, 42, I, 4.6)
    out += ink_stroke("M13 33C13 22 21 15 29 12", 4.2) + ink_stroke("M51 33C51 22 43 15 35 12", 4.2)
    return fit_b(out + ink_circle(32, 10, 4.8) + ink_circle(32, 42, 3, H), 0.6)

@reg("dev.invrs.oxide", BROWN_DARK)
def oxide():
    out = line(32, 22, 18, 46, I, 4.6) + line(32, 22, 46, 46, I, 4.6)
    for cx, cy, r in ((32, 22, 14), (18, 47, 8.4), (46, 47, 8.4)):
        out += ink_circle(cx, cy, r, I, f' stroke="{H}" stroke-width="2.4"')
    return fit_b(out + ring_c(32, 22, 6, 3, H), 0.66)

@reg("dev.j7126.combat_tracker", INDIGO_LIGHT)
def combat():
    hexp = [pt(32, 30, 22, -90 + 60 * k) for k in range(6)]
    out = poly(hexp, I, 1.6)
    tri = [pt(32, 30, 11, -90 + 120 * k) for k in range(3)]
    out += path("M" + "L".join(f"{f(x)} {f(y)}" for x, y in tri) + "Z", "none", f' stroke="{H}" stroke-width="2.4" stroke-linejoin="round"')
    for k in range(3):
        tx, ty = tri[k]
        for d in (-60, 60):
            hx, hy = pt(32, 30, 22, -90 + 120 * k + d)
            out += line(tx, ty, hx, hy, H, 2)
    return fit_b(out, 0.88)

@reg("dev.jamiethalacker.window_painter", YELLOW_DARK)
def windowpainter():
    out = rrect(10, 8, 36, 14, 4.5, I) + ink_stroke("M46 15H54V30H32V40", 3.8) + rrect(27, 40, 10, 15, 3.5, I)
    return fit_b(out + line(17, 15, 38, 15, H, 2.4), 0.69)

@reg("dev.khcrysalis.PlumeImpactor", RED_DEEP)
def plume():
    out = path("M52 8C26 8 10 24 12 54C38 54 54 36 52 8Z", I)
    out += ink_stroke("M12 54L42 20", 2.8, H) + ink_stroke("M26 40L24 26M34 32L34 18M22 46L12 40M40 24L50 26", 2.4, H)
    return fit_b(out, 0.64)

@reg("dev.krtirtho.Flemozi", CYAN_DEEP)
def flemozi():
    out = ink_circle(32, 30, 21, I) + rrect(13, 23, 16, 12, 5, H) + rrect(35, 23, 16, 12, 5, H) + line(28, 27, 36, 27, H, 2.6)
    return fit_b(out + ink_stroke("M22 42Q32 51 42 42", 3.6, H), 0.95)

@reg("dev.lasheen.qr", DEEP_ORANGE)
def qr():
    def finder(x, y):
        return rrect(x, y, 17, 17, 3, I) + rrect(x + 3, y + 3, 11, 11, 1.5, H) + rrect(x + 5.8, y + 5.8, 5.4, 5.4, 1, I)
    out = finder(7, 7) + finder(40, 7) + finder(7, 40)
    for x, y in ((27, 8), (27, 18), (27, 38), (38, 29), (49, 29), (40, 41), (50, 51), (29, 49)):
        out += rrect(x, y, 6, 6, 1, I)
    return fit_b(out, 0.56)

@reg("dev.levz.TinyImageFinder", DEEP_PURPLE_LIGHT)
def tinyimage():
    out = ring_c(28, 26, 17, 5.2) + line(41, 39, 54, 52, I, 7.4)
    return fit_b(out + poly([(16, 34), (23, 22), (28, 29), (32, 24), (40, 34)], I, 1) + ink_circle(33, 16, 3.2), 0.57)

@reg("dev.linwood.butterfly", GREY_LIGHT)
def butterfly():
    out = rot(ell(20, 22, 13, 11), -20, 20, 22) + rot(ell(44, 22, 13, 11), 20, 44, 22) + ell(22, 43, 9, 9) + ell(42, 43, 9, 9)
    out += ink_circle(20, 22, 4, H) + ink_circle(44, 22, 4, H) + rrect(29.5, 14, 5, 38, 2.5, I, f' stroke="{H}" stroke-width="1.6"')
    return fit_b(out + ink_stroke("M31 14Q28 6 23 4M33 14Q36 6 41 4", 2.6), 0.69)

@reg("dev.lunarsrl.NovaMusic", BLUE_GREY_DARK)
def novamusic():
    out = poly([pt(32, 30, 23 if k % 2 == 0 else 15, -90 + 18 * k) for k in range(20)], I, 1.2)
    return fit_b(out + ink_circle(27, 38, 4.8, H) + line(31, 38, 31, 20, H, 3.2) + ink_stroke("M31 21Q39 23 38 30", 3, H), 0.85)

@reg("dev.mariinkys.Cedilla", LIGHT_BLUE_LIGHT)
def cedilla():
    return fit_b(ink_stroke("M43.3 14.7A16 16 0 1 0 43.3 37.3", 7.4) + ink_stroke("M32 42Q33 47 36 48Q41 50 39 54Q36 57 30 55", 3.8), 0.72)

@reg("dev.mariinkys.Clockode", ORANGE)
def clockode():
    out = ring_c(32, 30, 13, 4.6) + ink_stroke("M32 22V30L38 34", 3.6)
    return fit_b(out + ink_stroke("M14 21L7 30L14 39", 4.2) + ink_stroke("M50 21L57 30L50 39", 4.2), 0.74)

@reg("dev.mariinkys.Oboete", PURPLE_DARK)
def oboete():
    back = dim(rot(rrect(14, 12, 28, 38, 4.4, I), -15, 28, 31), .5)
    front = rot(rrect(24, 12, 28, 38, 4.4, I) + ink_stroke("M31 25Q31 19 38 19Q45 19 45 25Q45 30 38 33V36", 3.8, H) + ink_circle(38, 42, 2.4, H), 7, 38, 31)
    return fit_b(back + front, 0.77)

@reg("dev.mariinkys.StarryDex", AMBER_DEEP)
def starrydex():
    out = rrect(14, 6, 36, 52, 7, I) + rrect(20, 12, 24, 22, 3, H) + star5(32, 24, 9.4)
    return fit_b(out + ink_circle(25, 46, 3.8, H) + line(33, 43, 44, 43, H, 3) + line(33, 50, 44, 50, H, 3), 0.65)

@reg("dev.mohfy.quizbite", GREY_DARK)
def quizbite():
    out = ink_circle(32, 28, 21, I) + poly([(14, 40), (10, 57), (29, 48)], I, 2)
    return fit_b(out + ink_stroke("M23 22Q23 13 32 13Q41 13 41 20Q41 27 32 30V34", 4.6, H) + ink_circle(32, 41.5, 2.8, H), 0.56)

@reg("dev.mooday.GstPipelineStudio", BLUE_LIGHT)
def gstpipeline():
    out = rrect(5, 23, 15, 15, 3.4, I) + rrect(24, 23, 15, 15, 3.4, I) + rrect(44, 8, 15, 15, 3.4, I) + rrect(44, 38, 15, 15, 3.4, I)
    return fit_b(out + line(20, 30.5, 24, 30.5, I, 3.2) + ink_stroke("M39 30.5H42V15.5H44", 3.2) + ink_stroke("M39 30.5H42V45.5H44", 3.2), 0.59)

@reg("dev.mrquantumoff.mcmodpackmanager", AMBER_DEEP)
def pickaxe():
    out = ink_stroke("M8 24Q32 4 56 24", 7) + line(32, 13, 32, 58, I, 6.4)
    return fit_b(rot(out, 35), 0.64)

@reg("dev.neovide.neovide", PINK_DEEP)
def neovide():
    out = dim(rrect(14, 38, 10, 14, 1.4, I), .22) + dim(rrect(22, 30, 10, 18, 1.4, I), .4) + dim(rrect(30, 22, 10, 20, 1.4, I), .64)
    return fit_b(out + rrect(38, 10, 13, 26, 1.8, I), 0.72)

def cloud(dx=0, dy=0):
    return (ink_circle(22 + dx, 38 + dy, 9) + ink_circle(33 + dx, 29 + dy, 12) + ink_circle(45 + dx, 38 + dy, 8)
            + rrect(14 + dx, 36 + dy, 39, 11, 5.5, I))

@reg("dev.nicx.mimick", TEAL_DEEP)
def mimick():
    out = dim(cloud(7, -9), .42) + cloud(-3, 6)
    return fit_b(out + ink_stroke("M29 51V34", 3.8, H) + ink_stroke("M22 41L29 34L36 41", 3.8, H), 0.7)

@reg("dev.oswald.vkCommander", BROWN)
def vkcommander():
    return fit_b(ink_stroke("M10 14L24 48L38 14", 7) + ink_stroke("M44 22L52 29L44 36", 4.6) + line(43, 46, 56, 46, I, 4.6), 0.64)

@reg("dev.overlayed.Overlayed", INDIGO_DEEP)
def overlayed():
    out = dim(rrect(6, 8, 38, 30, 5.4, I), .48) + rrect(20, 24, 38, 30, 5.4, I, f' stroke="{H}" stroke-width="3.2"')
    return fit_b(out + line(28, 35, 50, 35, H, 3.2) + line(28, 44, 42, 44, H, 3.2), 0.6)

@reg("dev.pantheum.janus", YELLOW_DARK)
def janus():
    left = poly([(31, 10), (22, 12), (19, 22), (11, 34), (19, 36), (19, 41), (22, 48), (31, 52)], I, 2.4)
    right = poly([(33, 10), (42, 12), (45, 22), (53, 34), (45, 36), (45, 41), (42, 48), (33, 52)], I, 2.4)
    return fit_b(left + right + ink_circle(24, 24, 2.2, H) + ink_circle(40, 24, 2.2, H) + line(32, 8, 32, 54, H, 1.8), 0.86)

@reg("dev.paullee.scraterpreter.Scrape", RED)
def scrape():
    return fit_b(ink_stroke("M14 8Q24 28 12 54", 5.6) + ink_stroke("M30 6Q40 28 28 56", 5.6) + ink_stroke("M46 8Q56 28 44 54", 5.6), 0.59)

@reg("dev.paullee.scraterpreter.Scrapec", CYAN_LIGHT)
def scrapec():
    out = poly([(10, 10), (54, 10), (50, 28), (14, 28)], I, 2.6) + line(18, 19, 46, 19, H, 2.6) + rrect(25, 28, 14, 7, 2, I) + rrect(28, 35, 8, 20, 4, I)
    return fit_b(out, 0.65)

@reg("dev.project516.titledgames.microwave-man", DEEP_ORANGE)
def microwave():
    out = rrect(6, 12, 52, 36, 5.4, I) + rrect(11, 17, 31, 26, 3, H) + path("M17 36H35A9 9 0 0 1 17 36Z", I)
    out += rrect(47, 18, 7, 6, 1.5, H) + line(47, 31, 53, 31, H, 3) + line(47, 38, 53, 38, H, 3)
    return fit_b(out + rrect(12, 48, 9, 5, 1.5, I) + rrect(43, 48, 9, 5, 1.5, I) + ink_stroke("M22 30Q25 26 22 22M30 30Q33 26 30 22", 2.2, I), 0.67)

@reg("dev.qwery.AddWater", DEEP_PURPLE_DARK)
def addwater():
    out = path("M32 6C32 6 14 28 14 40A18 18 0 0 0 50 40C50 28 32 6 32 6Z", I)
    return fit_b(out + line(24, 40, 40, 40, H, 4) + line(32, 32, 32, 48, H, 4), 0.71)

@reg("dev.restfox.Restfox", AMBER)
def restfox():
    out = path("M6 8L22 18H42L58 8L53 34Q51 45 32 56Q13 45 11 34Z", I)
    return fit_b(out + poly([(17, 29), (27, 33), (19, 37)], H, 1.2) + poly([(47, 29), (37, 33), (45, 37)], H, 1.2) + poly([(27.5, 46), (36.5, 46), (32, 51.5)], H, 1.2), 0.59)

@reg("dev.rotstein.SmashedPumpkin", BLUE_GREY_DARK)
def pumpkin():
    out = ell(21, 36, 10, 15) + ell(43, 36, 10, 15) + ell(32, 35, 10, 17) + rrect(29, 11, 6, 10, 2.4, I)
    return fit_b(out + ink_stroke("M32 22L28 29L35 33L30 42", 2.8, H) + ink_stroke("M12 30Q10 36 12 42", 2, H), 0.8)

@reg("dev.schlaubi.Tonbrett", LIGHT_BLUE_LIGHT)
def tonbrett():
    out = rrect(8, 8, 22, 22, 5, I) + rrect(34, 8, 22, 22, 5, I) + rrect(8, 34, 22, 22, 5, I) + rrect(34, 34, 22, 22, 5, I)
    out += ink_circle(19, 19, 4.6, H) + poly([(44, 14), (44, 25), (52, 19.5)], H, 1.2) + rrect(14, 40, 10, 10, 1.8, H) + ink_stroke("M39 46L43 41L47 51L51 46", 2.8, H)
    return fit_b(out, 0.6)

@reg("dev.serebit.Waycheck", ORANGE_DEEP)
def waycheck():
    out = rrect(8, 8, 48, 34, 6, "none", f' stroke="{I}" stroke-width="4.6"') + ink_stroke("M22 20H42M22 29H34", 5)
    return fit_b(out + ink_stroke("M9 54Q15 48 21 54T33 54T45 54T57 54", 3.6), 0.55)

@reg("dev.serwin.AbeRE", PURPLE_DARK)
def abere():
    out = ink_stroke("M48 12H26Q14 12 14 24Q14 34 26 34H42", 5.4) + arrowhead(46, 34, 1, 0, 7)
    return fit_b(out + line(14, 46, 50, 46, I, 3.8) + line(14, 55, 36, 55, I, 3.8), 0.61)

@reg("dev.serwin.AnarchRE", BLUE_GREY_SOFT)
def anarchre():
    return fit_b(ring_c(32, 30, 22, 4.8) + ink_stroke("M24 43L32 16L40 43", 5) + line(26.5, 34, 37.5, 34, I, 4.4), 0.82)

@reg("dev.slimevr.SlimeVR", GREY_DEEP)
def slimevr():
    out = path("M10 50Q7 22 32 12Q57 22 54 50Z", I) + ell(32, 51, 27, 5) + poly([(50, 6), (46, 12), (54, 12)], I, 1.6) + ink_circle(50, 13, 3.4)
    return fit_b(out + ink_circle(23, 33, 4, H) + ink_circle(41, 33, 4, H) + ink_stroke("M26 42Q32 47 38 42", 3, H) + ink_stroke("M15 30Q17 23 24 19", 2.8, H), 0.58)

@reg("dev.stewlab.PortaWar", BLUE_DEEP)
def portawar():
    out = path("M10 56V28A22 22 0 0 1 54 28V56Z", I) + path("M19 56V28A13 13 0 0 1 45 28V56Z", H)
    return fit_b(out + ring_c(32, 38, 9, 3.4) + ring_c(32, 38, 3.6, 3) + line(32, 46, 32, 56, I, 3), 0.59)

@reg("dev.storyapps.starc", AMBER_DEEP)
def starc():
    out = ink_stroke("M8 46C18 46 23 44 28 30C32 19 34 10 38 10C44 10 47 40 57 46", 4.6) + line(8, 54, 57, 54, I, 3.8)
    return fit_b(out + ink_circle(38, 10, 4.6, I) + ink_circle(8, 46, 3.2), 0.55)

@reg("dev.tchx84.Gameeky", PINK)
def gameeky():
    out = rrect(16, 14, 32, 22, 5.4, I) + line(32, 14, 32, 7, I, 3) + ink_circle(32, 5.5, 3) + rrect(20, 40, 24, 16, 4, I)
    out += rrect(8, 41, 8, 13, 3.4, I) + rrect(48, 41, 8, 13, 3.4, I)
    return fit_b(out + ink_circle(25, 25, 3.8, H) + ink_circle(39, 25, 3.8, H) + line(28, 31.5, 36, 31.5, H, 2.6), 0.61)

@reg("dev.ters.Chordcat", TEAL_LIGHT)
def chordcat():
    out = poly([(11, 24), (13, 6), (27, 18)], I, 1.8) + poly([(53, 24), (51, 6), (37, 18)], I, 1.8) + rrect(11, 15, 42, 42, 5, I)
    for x in (22, 32, 42):
        out += line(x, 22, x, 51, H, 2.2)
    for y in (32, 42):
        out += line(17, y, 47, y, H, 2.2)
    return fit_b(out + ink_circle(22, 37, 4.4, I, f' stroke="{H}" stroke-width="2.4"') + ink_circle(42, 47, 4.4, I, f' stroke="{H}" stroke-width="2.4"'), 0.62)

@reg("dev.ters.LocalTranslate", BROWN)
def localtranslate():
    out = ring_c(28, 26, 18, 4.4) + f'<ellipse cx="28" cy="26" rx="8" ry="18" fill="none" stroke="{I}" stroke-width="3.6"/>' + line(10, 26, 46, 26, I, 3.6)
    out += rrect(38, 36, 22, 16, 5, I, f' stroke="{H}" stroke-width="2.6"') + poly([(42, 51), (42, 58), (49, 51)], I, 1.2)
    return fit_b(out + line(43, 43, 55, 43, H, 2.4), 0.59)

@reg("dev.tony4.subscribi", INDIGO_DARK)
def subscribi():
    out = path("M30 8C22 8 16 14 16 24V34L10 44H50L44 34V24C44 14 38 8 30 8Z", I) + ink_circle(30, 50, 5.4, I)
    return fit_b(out + ink_circle(48, 14, 9.4, I, f' stroke="{H}" stroke-width="2.6"') + line(43.5, 14, 52.5, 14, H, 3) + line(48, 9.5, 48, 18.5, H, 3), 0.62)
