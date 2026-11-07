# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 87: the second hundred apps from the gap list (flags/app-gap-list-full.md),
rows 101 to 200, wps_365 to calculator. Each is a simple original mark on its own tile."""
from lm import *
from glyphs.kit import H, I, ink_stroke, registry, ring_d

ICONS, SMALL, reg, _ = registry()

@reg("cn.wps.wps_365", RED)
def wps():
    return ink_stroke("M13 19L21 43L32 24L43 43L51 19", 5.5)

@reg("cn.xfangfang.wiliwili", LIGHT_BLUE)
def wiliwili():
    return (ink_stroke("M24 13L30 20L36 13", 3.2) + rrect(13, 20, 38, 26, 7, I)
            + poly([(28, 28), (28, 40), (38, 34)], H, 2))

@reg("co.logonoff.awakeonlan", DEEP_ORANGE)
def awakeonlan():
    return ink_stroke("M23 20A15 15 0 1 0 41 20", 4.5) + line(32, 11, 32, 30, I, 4.5)

@reg("codes.loers.Karlender", TEAL)
def karlender():
    out = rrect(13, 16, 38, 32, 6, I) + rrect(13, 16, 38, 9, 4, I)
    out += line(22, 12, 22, 20, I, 4) + line(42, 12, 42, 20, I, 4)
    for x, y in ((20, 31), (30, 31), (40, 31), (20, 39), (30, 39)):
        out += rrect(x - 3, y - 3, 6, 6, 1.5, H)
    return out

@reg("codes.merritt.FeelingFinder", AMBER)
def feelingfinder():
    return (circle(32, 30, 19, I) + circle(25.5, 25, 3, H) + circle(38.5, 25, 3, H)
            + ink_stroke("M23 34Q32 44 41 34", 3.6, H))

@reg("codes.merritt.Nyrna", DEEP_PURPLE)
def nyrna():
    return ring_d(32, 30, 18, 4) + rrect(25, 21, 5, 18, 2, I) + rrect(34, 21, 5, 18, 2, I)

@reg("codes.merritt.adventurelist", BROWN_SOFT)
def adventurelist():
    return (poly([(10, 46), (26, 20), (36, 34), (42, 26), (54, 46)], I, 2)
            + line(42, 26, 42, 11, I, 3) + poly([(42, 11), (53, 15), (42, 19)], I, 1.5))

@reg("codes.merritt.bargain", PINK)
def bargain():
    tag = poly([(14, 32), (30, 14), (48, 14), (48, 32), (30, 48)], I, 3)
    return tag + circle(40, 22, 3.4, H) + ink_stroke("M26 40L38 26", 3.2, H)

@reg("com.VK.Messenger", BLUE)
def vkmessenger():
    return (circle(32, 28, 19, I) + poly([(17, 38), (14, 50), (28, 45)], I, 2)
            + ink_stroke("M24 22L32 36L40 22", 4.2, H))

@reg("com.a_chacon.chaski", CYAN)
def chaski():
    return (poly([(12, 30), (52, 12), (38, 48), (30, 35)], I, 2.4)
            + line(30, 35, 52, 12, H, 2.6))

@reg("com.actualbudget.actual", BROWN_LIGHT)
def actual():
    return circle(32, 30, 19, I) + ink_stroke("M24 40L32 20L40 40M27 34H37", 4.2, H)

@reg("com.adilhanney.no_more_background", PURPLE_LIGHT)
def nomorebg():
    out = rrect(13, 14, 38, 34, 6, I, ' opacity=".5"')
    for (x, y) in ((13, 14), (32, 14), (22.5, 31), (41.5, 31)):
        out += rrect(x + 2, y + 2, 7, 7, 1.5, I)
    return out + ink_stroke("M16 45L48 17", 3.6, H)

@reg("com.adilhanney.ricochlime", LIGHT_BLUE_SOFT)
def ricochlime():
    blob = path("M20 42C14 42 14 30 22 28C22 18 42 18 42 28C50 30 50 42 44 42Z", I)
    return blob + circle(28, 33, 2.4, H) + circle(37, 33, 2.4, H) + ink_stroke("M12 18L20 12", 3)

@reg("com.adilhanney.saber", INDIGO_DEEP)
def saber():
    nib = poly([(32, 46), (22, 28), (28, 14), (36, 14), (42, 28)], I, 2.4)
    return nib + circle(32, 27, 3, H) + line(32, 30, 32, 44, H, 2.4)

@reg("com.adilhanney.super_nonogram", ORANGE)
def nonogram():
    out = ""
    pat = ["10110", "11011", "01110", "11011", "10101"]
    for r, row in enumerate(pat):
        for c, ch in enumerate(row):
            if ch == "1":
                out += rrect(13 + c * 8, 11 + r * 8, 7, 7, 1.5, I)
    return out

@reg("com.adilhanney.timing", RED_DEEP)
def timing():
    return (ring_d(32, 33, 16, 4) + line(27, 11, 37, 11, I, 4) + line(32, 11, 32, 17, I, 4)
            + ink_stroke("M32 33L40 25", 4) + line(44, 18, 48, 14, I, 3.4))

@reg("com.agatanawrot.karambola", YELLOW_LIGHT)
def karambola():
    pts = []
    for k in range(10):
        r = 19 if k % 2 == 0 else 9
        pts.append(pt(32, 30, r, -90 + k * 36))
    return poly(pts, I, 3)

@reg("com.agateau.PixelWheels", BROWN_DEEP)
def pixelwheels():
    out = rrect(24, 12, 16, 36, 5, I) + rrect(27, 19, 10, 8, 2, H)
    for x, y in ((18, 16), (40, 16), (18, 36), (40, 36)):
        out += rrect(x, y, 6, 11, 2, I)
    return out

@reg("com.agateau.nanonote", TEAL_LIGHT)
def nanonote():
    pg = path("M17 12H37L47 22V48H17Z", I)
    return pg + path("M37 12V22H47Z", H, ' opacity=".5"') + line(23, 31, 41, 31, H, 3) + line(23, 38, 36, 38, H, 3)

@reg("com.alliedbits.ABCalcPlus", PURPLE_DEEP)
def abcalc():
    out = rrect(12, 12, 40, 36, 5, "none", ' stroke="INK" stroke-width="4"')
    for y, xs in ((22, (24, 30, 42)), (31, (22, 36, 42)), (40, (28, 34, 40))):
        out += line(14, y, 50, y, I, 1.8)
        for x in xs:
            out += rrect(x - 2.5, y - 4, 5, 8, 2.5, I)
    return out

def pix(rows, ox=14, oy=12, s=6.4, gap=1):
    out = ""
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == "1":
                out += rrect(ox + c * s, oy + r * s, s - gap, s - gap, 1, I)
    return out

@reg("com.almaarijstudios.pxjr", PINK_LIGHT)
def pxjr():
    return pix(["00111", "00111", "00011", "00011", "10011", "11111", "01110"], 15, 11, 5.5, 0.8)

@reg("com.almaarijstudios.pxjrprof", BLUE_DEEP)
def pxjrprof():
    return pix(["11110", "11111", "11011", "11110", "11000", "11000", "11000"], 15, 11, 5.5, 0.8)

@reg("com.aloxbook.AloxBook", DEEP_PURPLE_LIGHT)
def aloxbook():
    return (path("M32 18C26 14 19 14 13 16V45C19 43 26 43 32 47Z", I)
            + path("M32 18C38 14 45 14 51 16V45C45 43 38 43 32 47Z", I, ' opacity=".6"')
            + line(32, 18, 32, 47, H, 2))

@reg("com.alpineclient.AlpineClient", INDIGO_SOFT)
def alpine():
    m = poly([(8, 46), (24, 16), (34, 34), (41, 24), (56, 46)], I, 2)
    return m + poly([(24, 16), (18, 27), (24, 24), (30, 28)], H, 1)

@reg("com.ampl.ide", BLUE_LIGHT)
def amplide():
    return ink_stroke("M22 19L11 30L22 41", 4.5) + ink_stroke("M42 19L53 30L42 41", 4.5) + line(36, 15, 28, 45, I, 4)

@reg("com.andr2i.scrolex", AMBER_DEEP)
def scrolex():
    return (rrect(21, 10, 22, 40, 11, I) + rrect(29.5, 16, 5, 9, 2.5, H)
            + ink_stroke("M13 24L13 36", 3) + ink_stroke("M51 24L51 36", 3))

@reg("com.apifox.Apifox", DEEP_ORANGE_LIGHT)
def apifox():
    return (poly([(13, 14), (25, 22), (39, 22), (51, 14), (49, 34), (32, 49), (15, 34)], I, 2.4)
            + circle(25, 31, 2.6, H) + circle(39, 31, 2.6, H) + poly([(29, 39), (35, 39), (32, 43)], H, 1))

@reg("com.aresvalley.artemis", DEEP_PURPLE_SOFT)
def artemis():
    return (circle(32, 38, 4, I) + ink_stroke("M22 30A14 14 0 0 1 42 30", 3.6) + ink_stroke("M16 24A22 22 0 0 1 48 24", 3.6)
            + line(32, 38, 32, 50, I, 4))

@reg("com.artemchep.keyguard", TEAL_DEEP)
def keyguard():
    return (circle(23, 24, 11, I) + circle(23, 24, 4.5, H) + rrect(30, 28, 22, 6, 3, I)
            + rrect(41, 33, 5, 9, 2, I) + rrect(48, 33, 5, 7, 2, I)).replace(
        '<rect x="30" y="28" width="22" height="6"', '<rect x="29" y="30" width="23" height="6"')

@reg("com.arviceblot.eso-addon-manager", YELLOW_DARK)
def esoaddon():
    return rrect(14, 24, 34, 24, 3, I) + circle(31, 24, 6, I) + circle(48, 36, 6, I) + circle(31, 24, 2.4, H)

@reg("com.authormore.penpotdesktop", INDIGO)
def penpot():
    return (ink_stroke("M14 42C14 22 34 36 48 16", 3.6) + rrect(10, 40, 8, 8, 2, I) + rrect(44, 11, 8, 8, 2, I)
            + line(14, 42, 26, 46, I, 2.6) + line(36, 20, 48, 16, I, 2.6))

@reg("com.axantum.xecrets.ez", PINK_DEEP)
def ez():
    return (ink_stroke("M22 28V22A10 10 0 0 1 42 22V28", 4.5) + rrect(16, 28, 32, 21, 6, I)
            + circle(32, 37, 3.4, H) + line(32, 38, 32, 43, H, 3))

@reg("com.bandpassrecords.dpm", INDIGO_DARK)
def dpm():
    return ring_d(32, 30, 18, 4) + ring_d(32, 30, 9, 3) + circle(32, 30, 2.5, I) + ink_stroke("M42 14L50 12", 3)

@reg("com.basemark.BasemarkGPU", ORANGE_DEEP)
def basemark():
    out = rrect(12, 16, 40, 26, 5, I) + circle(30, 29, 8.5, H) + circle(30, 29, 3, I)
    for k in range(3):
        out += line(22 + k * 8, 42, 22 + k * 8, 48, I, 3)
    return out + line(44, 22, 44, 36, H, 3)

@reg("com.beavernotes.beavernotes", BROWN)
def beaver():
    return (circle(20, 17, 6, I) + circle(44, 17, 6, I) + circle(32, 30, 17, I)
            + circle(26, 26, 2.4, H) + circle(38, 26, 2.4, H)
            + rrect(26, 34, 5.5, 9, 1.5, H) + rrect(32.5, 34, 5.5, 9, 1.5, H))

@reg("com.behringer.XAirEdit", BLUE_GREY)
def xair():
    out = ""
    for x, ky in ((17, 22), (32, 34), (47, 18)):
        out += line(x, 12, x, 48, I, 3.2) + rrect(x - 7, ky - 4, 14, 8, 3, I)
    return out

@reg("com.belmoussaoui.ashpd.demo", CYAN_DEEP)
def ashpd():
    return (rrect(12, 14, 32, 28, 5, I) + rrect(16, 19, 24, 18, 2, H)
            + ink_stroke("M36 46L52 30M42 30H52V40", 4))

@reg("com.belmoussaoui.snowglobe", INDIGO_LIGHT)
def snowglobe():
    out = circle(32, 27, 18, I) + rrect(20, 41, 24, 9, 3, I)
    for x, y in ((24, 22), (33, 18), (40, 26), (29, 31), (37, 34)):
        out += circle(x, y, 2, H)
    return out

@reg("com.besoeasy.gupt", PURPLE_DARK)
def gupt():
    gh = path("M17 46V28A15 15 0 0 1 47 28V46L40 41L32 46L24 41Z", I)
    return gh + circle(26, 28, 3, H) + circle(38, 28, 3, H)

@reg("com.bespokesynth.BespokeSynth", RED_DARK)
def bespoke():
    return (rrect(11, 16, 14, 14, 4, I) + circle(18, 23, 3, H) + rrect(39, 34, 14, 14, 4, I) + circle(46, 41, 3, H)
            + ink_stroke("M25 23C40 23 24 41 39 41", 4))

@reg("com.bestaticpy.bestatic", ORANGE_DARK)
def bestatic():
    return ring_d(32, 30, 18, 4) + ink_stroke("M32 12C22 22 22 38 32 48C42 38 42 22 32 12", 3.2) + line(14, 30, 50, 30, I, 3.2)

@reg("com.binarynonsense.acbr", DEEP_ORANGE)
def acbr():
    return (rrect(13, 12, 18, 16, 3, I) + rrect(34, 12, 17, 16, 3, I)
            + rrect(13, 31, 38, 17, 3, I) + poly([(25, 40), (33, 36), (40, 40), (33, 44)], H, 1))

@reg("com.bishwasaha.Koncentro", DEEP_PURPLE_DEEP)
def koncentro():
    return ink_stroke("M14 22V14H22M42 14H50V22M50 38V46H42M22 46H14V38", 4.2) + circle(32, 30, 7, I) + ring_d(32, 30, 12, 2.4)

@reg("com.bjareholt.johan.SimpleDiary", BROWN_LIGHT)
def simplediary():
    return (rrect(16, 11, 30, 38, 4, I) + line(23, 22, 38, 22, H, 3) + line(23, 29, 38, 29, H, 3)
            + poly([(40, 11), (40, 25), (45, 21), (50, 25), (50, 11)], I, 0))

@reg("com.bktus.gpgfrontend", TEAL_DARK)
def gpgfront():
    return (path("M32 11L49 17V31C49 40 42 46 32 50C22 46 15 40 15 31V17Z", I)
            + circle(32, 27, 4.4, H) + rrect(30, 29, 4, 11, 1.5, H))

@reg("com.blitterstudio.amiberry", RED)
def amiberry():
    c = circle(32, 30, 19, I)
    return c + ink_stroke("M32 11V49M13 30H51M18 18Q32 26 46 18M18 42Q32 34 46 42", 2.6, H)

@reg("com.blockstream.Green", LIGHT_BLUE_LIGHT)
def green():
    return (rrect(12, 17, 38, 28, 6, I) + rrect(38, 27, 16, 10, 5, I) + circle(44, 32, 2.4, H)
            + line(18, 17, 40, 12, I, 4))

@reg("com.blunix.currency_converter", AMBER)
def currency():
    return ink_stroke("M14 22H46M38 14L46 22L38 30", 4.5) + ink_stroke("M50 40H18M26 32L18 40L26 48", 4.5)

@reg("com.bolwarratechnologies.this_note", DEEP_ORANGE_DEEP)
def thisnote():
    return rrect(14, 15, 36, 33, 4, I) + circle(32, 15, 5.5, I) + circle(32, 15, 2.2, H) + line(21, 28, 43, 28, H, 3) + line(21, 36, 36, 36, H, 3)

@reg("com.brainscanmedia.SafeScript", INDIGO_DEEP)
def safescript():
    pg = path("M17 11H37L47 21V49H17Z", I)
    return pg + circle(32, 34, 4, H) + rrect(30.5, 36, 3, 8, 1, H)

@reg("com.budgetwithbuckets.Buckets", BLUE_DEEP)
def buckets():
    return poly([(15, 22), (49, 22), (44, 49), (20, 49)], I, 2) + ink_stroke("M18 22C18 8 46 8 46 22", 3.4) + line(21, 29, 43, 29, H, 2.4)

@reg("com.cassidyjames.butler", ORANGE_DARK)
def butler():
    return path("M13 40C13 25 21 19 32 19C43 19 51 25 51 40Z", I) + circle(32, 15, 3.6, I) + rrect(10, 40, 44, 6, 3, I)

@reg("com.cassidyjames.clairvoyant", DEEP_PURPLE)
def clairvoyant():
    return (circle(32, 26, 16, I) + path("M18 46H46L42 38H22Z", I) + ink_stroke("M24 22Q27 18 32 18", 3, H)
            + poly([(40, 24), (42, 28), (46, 29), (42, 30), (40, 34), (38, 30), (34, 29), (38, 28)], H, 0))

@reg("com.cassidyjames.dippi", RED_LIGHT)
def dippi():
    out = rrect(10, 22, 44, 20, 4, I)
    for k, x in enumerate(range(17, 50, 7)):
        out += line(x, 22, x, 32 if k % 2 == 0 else 28, H, 2.6)
    return out

@reg("com.cassidyjames.plausible", TEAL_SOFT)
def plausible():
    return ink_stroke("M13 12V47H51", 3.4) + ink_stroke("M18 40L28 28L35 34L48 17", 4.2) + circle(48, 17, 3.4, I)

@reg("com.cburch.Logisim", INDIGO)
def logisim():
    return path("M20 14H32A16 16 0 0 1 32 46H20Z", I) + line(11, 23, 20, 23, I, 3.4) + line(11, 37, 20, 37, I, 3.4) + line(48, 30, 55, 30, I, 3.4)

@reg("com.cerebralnomad.recipescribe", DEEP_ORANGE_SOFT)
def recipescribe():
    return path("M20 30C12 28 13 16 23 17C25 10 39 10 41 17C51 16 52 28 44 30V38H20Z", I) + rrect(20, 41, 24, 7, 2, I)

@reg("com.cherry_ai.CherryStudio", RED_DEEP)
def cherry():
    return (circle(22, 40, 9, I) + circle(42, 38, 9, I) + ink_stroke("M22 31C22 22 30 16 38 14M42 29C42 22 40 17 38 14", 3)
            + path("M38 14C44 9 50 11 52 14C47 18 41 18 38 14Z", I))

@reg("com.chirpmyradio.chirp", GREY_DEEP)
def chirp():
    return (rrect(15, 22, 34, 26, 5, I) + circle(26, 36, 7, H) + circle(26, 36, 2.4, I)
            + line(38, 31, 44, 31, H, 3) + line(38, 38, 44, 38, H, 3) + line(40, 22, 46, 10, I, 3.4))

@reg("com.chowdsp.BYOD", PURPLE_LIGHT)
def byod():
    return (rrect(17, 11, 30, 38, 6, I) + circle(26, 21, 3.4, H) + circle(38, 21, 3.4, H)
            + circle(32, 41, 4.2, H) + rrect(28, 28, 8, 3, 1.5, H))

@reg("com.chroniclogic.Zatikon", BROWN_DARK)
def zatikon():
    out = line(15, 14, 49, 46, I, 4.5) + line(49, 14, 15, 46, I, 4.5)
    return out + line(21, 20, 27, 14, I, 4) + line(43, 20, 37, 14, I, 4) + line(16, 40, 22, 46, I, 4) + line(48, 40, 42, 46, I, 4)

@reg("com.cinecred.cinecred", LIGHT_BLUE_DEEP)
def cinecred():
    return (line(32, 14, 32, 14.1, I, 1) + rrect(22, 13, 20, 5, 2, I) + line(18, 25, 46, 25, I, 3) + line(24, 32, 40, 32, I, 3)
            + line(18, 39, 46, 39, I, 3) + line(26, 46, 38, 46, I, 3))

@reg("com.claudiocambra.brickbuster", DEEP_ORANGE)
def brickbuster():
    out = ""
    for c in range(4):
        out += rrect(13 + c * 10, 13, 9, 7, 1.5, I)
    for c in range(3):
        out += rrect(18 + c * 10, 22, 9, 7, 1.5, I)
    return out + circle(38, 37, 3.4, I) + rrect(22, 45, 20, 4, 2, I)

@reg("com.cloudchewie.cloudotp", LIGHT_BLUE_LIGHT)
def cloudotp():
    cl = path("M20 44C11 44 10 31 19 29C20 18 38 16 41 26C52 25 54 44 44 44Z", I)
    return cl + circle(32, 34, 3, H) + rrect(30.5, 35, 3, 6, 1, H)

@reg("com.clustta.clustta", DEEP_PURPLE_SOFT)
def clustta():
    return (ring_d(24, 24, 10, 3.6) + ring_d(40, 24, 10, 3.6) + ring_d(32, 38, 10, 3.6))

@reg("com.coeck_studios.Dinonuggys-Journey", LIGHT_BLUE_DEEP)
def dino():
    back = poly([(22, 26), (26, 19), (30, 26)], I, 1) + poly([(30, 26), (34, 19), (38, 26)], I, 1)
    return (path("M12 38C12 28 22 26 30 27C32 17 44 15 50 21C52 25 46 29 40 29C42 36 42 41 36 45H20Z", I)
            + back + rrect(21, 42, 6, 8, 2, I) + rrect(33, 42, 6, 8, 2, I) + circle(44, 22, 1.8, H)
            + poly([(12, 38), (7, 43), (16, 43)], I, 1))

@reg("com.connorcode.mslicer", PINK_LIGHT)
def mslicer():
    cube = poly([(32, 11), (50, 21), (50, 40), (32, 50), (14, 40), (14, 21)], I, 2)
    return cube + line(14, 26, 32, 36, H, 2.4) + line(32, 36, 50, 26, H, 2.4) + line(32, 36, 32, 50, H, 2.4)

@reg("com.core447.StreamController", TEAL_DEEP)
def streamcontroller():
    out = ""
    for r in range(2):
        for c in range(3):
            out += rrect(12 + c * 14, 16 + r * 16, 12, 13, 3.5, I, ' opacity="1"' if (r + c) % 2 == 0 else ' opacity=".5"')
    return out

@reg("com.corsixth.corsixth", RED)
def corsixth():
    return rrect(24, 11, 16, 38, 4, I) + rrect(13, 22, 38, 16, 4, I)

@reg("com.cyberbotics.webots", CYAN)
def webots():
    return (line(32, 10, 32, 17, I, 3) + circle(32, 9, 2.8, I) + rrect(15, 17, 34, 28, 8, I)
            + circle(25, 29, 4, H) + circle(39, 29, 4, H) + line(25, 38, 39, 38, H, 3))

@reg("com.daidouji.oneko", ORANGE_LIGHT)
def oneko():
    cat = path("M14 44V17L25 25H39L50 17V44C50 50 42 52 32 52C22 52 14 50 14 44Z", I)
    return cat + circle(25, 34, 2.6, H) + circle(39, 34, 2.6, H) + poly([(30, 39), (34, 39), (32, 42)], H, 0.8)

@reg("com.daniel15.wcc", DEEP_PURPLE_DARK)
def wcc():
    return ink_stroke("M46 20A17 17 0 1 0 46 42", 4.6) + ink_stroke("M21 24L26 38L32 28L38 38L43 24", 3.4)

@reg("com.danklinux.dankcalendar", PINK_DARK)
def dankcal():
    return (rrect(13, 15, 38, 34, 6, I) + circle(24, 12, 3.4, I) + circle(40, 12, 3.4, I)
            + ink_stroke("M28 27L33 24V42", 4.4, H))

@reg("com.darhon.syncbackup", BLUE)
def syncbackup():
    return (ink_stroke("M44 24A14 14 0 0 0 20 22M20 36A14 14 0 0 0 44 38", 4.2) + poly([(18, 14), (22, 28), (30, 22)], I, 1.5)
            + poly([(46, 46), (42, 32), (34, 38)], I, 1.5))

@reg("com.dekomote.vermouth", INDIGO_LIGHT)
def vermouth():
    return (poly([(12, 14), (52, 14), (32, 36)], I, 2) + line(32, 36, 32, 48, I, 3.6) + line(22, 49, 42, 49, I, 3.6)
            + circle(40, 20, 3.4, H) + line(36, 10, 44, 28, H, 2))

@reg("com.diffingo.fwbackups", AMBER_DEEP)
def fwbackups():
    return path("M11 18C11 15 13 13 16 13H26L31 19H48C51 19 53 21 53 24V43C53 46 51 48 48 48H16C13 48 11 46 11 43Z", I) + ink_stroke("M32 27V41M25 35L32 42L39 35", 3.6, H)

@reg("com.digitalgex.RustDiff", DEEP_ORANGE_DEEP)
def rustdiff():
    return (rrect(11, 13, 19, 35, 4, I) + rrect(34, 13, 19, 35, 4, I)
            + ink_stroke("M16 25H25", 3, H) + ink_stroke("M39 25H48M43.5 20.5V29.5", 3, H) + line(16, 36, 25, 36, H, 3) + line(39, 36, 48, 36, H, 3))

@reg("com.dingtalk.DingTalk", LIGHT_BLUE)
def dingtalk():
    return path("M32 11C24 11 19 17 19 25V34L13 42H51L45 34V25C45 17 40 11 32 11Z", I) + circle(32, 48, 4, I)

@reg("com.diy_fever.DIYLayoutCreator", GREY_DEEP)
def diylayout():
    out = ""
    for x, w in ((11, 12), (25, 8), (35, 8), (45, 8)):
        out += rrect(x, 15, w, 9, 2.2, I)
    for x, w in ((11, 8), (21, 14), (37, 16)):
        out += rrect(x, 27, w, 9, 2.2, I)
    out += rrect(11, 39, 10, 9, 2.2, I) + rrect(23, 39, 20, 9, 2.2, I) + rrect(45, 39, 8, 9, 2.2, I)
    return out

@reg("com.djoffe.gnukem", AMBER_LIGHT)
def gnukem():
    out = circle(32, 30, 4.4, I) + ring_d(32, 30, 19, 3)
    for a in (-90, 30, 150):
        x1, y1 = pt(32, 30, 8, a - 28)
        x2, y2 = pt(32, 30, 17, a - 28)
        x3, y3 = pt(32, 30, 17, a + 28)
        x4, y4 = pt(32, 30, 8, a + 28)
        out += poly([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], I, 1.5)
    return out

@reg("com.donhopkins.Micropolis", DEEP_PURPLE_LIGHT)
def micropolis():
    return rrect(12, 24, 12, 24, 2, I) + rrect(26, 12, 12, 36, 2, I) + rrect(40, 30, 12, 18, 2, I) + rrect(30, 18, 4, 4, 1, H) + rrect(30, 26, 4, 4, 1, H)

@reg("com.doycho.euterpe.gtk", PINK_SOFT)
def euterpe():
    return circle(24, 41, 7.5, I) + ink_stroke("M31 41V16L48 22V28L31 23", 4.2) + line(31, 16, 31, 41, I, 4.2)

@reg("com.dreamsourcelab.DSView", INDIGO)
def dsview():
    return ink_stroke("M10 40H18V20H28V40H36V20H42V40H54", 4)

@reg("com.dygma.bazecor", RED_DEEP)
def bazecor():
    out = ""
    for r in range(3):
        for c in range(2):
            out += rrect(11 + c * 10, 14 + r * 11 + c * 2, 8, 9, 2, I)
            out += rrect(44 - c * 10 + 0, 14 + r * 11 + c * 2, 8, 9, 2, I)
    return out + rrect(26, 38, 12, 9, 3, I)

@reg("com.easyeda.EasyEDAPro", CYAN_DEEP)
def easyeda():
    return (rrect(22, 20, 20, 20, 3, I) + ink_stroke("M22 26H12M22 34H16V44M42 26H52M42 34H48V44M28 20V12M36 20V12", 3)
            + circle(12, 26, 2.8, I) + circle(16, 46, 2.8, I) + circle(52, 26, 2.8, I) + circle(48, 46, 2.8, I))

@reg("com.ekonomikas.merkato", DEEP_ORANGE_LIGHT)
def merkato():
    return (path("M12 24L16 12H48L52 24Z", I) + rrect(15, 24, 34, 4, 0, I, ' opacity="0"') + path("M12 24H52V28C52 32 44 32 42 28C40 32 24 32 22 28C20 32 12 32 12 28Z", I)
            + rrect(16, 33, 32, 15, 2, I) + rrect(27, 38, 10, 10, 2, H))

@reg("com.eminfedar.vaktisalah", ORANGE_DARK)
def vakti():
    return path("M40 12C28 13 20 22 22 33C24 43 34 49 44 46C33 44 29 34 33 26C35 21 38 17 40 12Z", I) + poly([(44, 16), (46, 21), (51, 22), (47, 25), (48, 30), (44, 27), (40, 30), (41, 25), (37, 22), (42, 21)], I, 0)

@reg("com.empesol.timetracker", YELLOW_DARK)
def timetracker():
    return (rrect(16, 11, 32, 5, 2, I) + rrect(16, 44, 32, 5, 2, I)
            + path("M19 16H45C45 27 36 28 36 30C36 32 45 33 45 44H19C19 33 28 32 28 30C28 28 19 27 19 16Z", I)
            + path("M25 40H39C38 36 34 35 32 35C30 35 26 36 25 40Z", H))

@reg("com.emqx.MQTTX", PURPLE)
def mqttx():
    return (circle(32, 30, 8, I) + ink_stroke("M32 22V12M24.7 34L15 40M39.3 34L49 40", 3.4)
            + ring_d(32, 10, 4, 3) + ring_d(13, 41, 4, 3) + ring_d(51, 41, 4, 3))

@reg("com.endlessnetwork.MidnightmareTeddy", BROWN_SOFT)
def teddy():
    return (circle(19, 17, 7, I) + circle(45, 17, 7, I) + circle(32, 32, 18, I) + circle(19, 17, 3, H) + circle(45, 17, 3, H)
            + circle(32, 38, 8, H) + circle(32, 36, 2.6, I) + circle(25, 27, 2.4, H) + circle(39, 27, 2.4, H))

@reg("com.endlessnetwork.passage", INDIGO_DARK)
def passage():
    return path("M16 48V28A16 16 0 0 1 48 28V48Z", I) + path("M26 48V32A6 6 0 0 1 38 32V48Z", H) + line(10, 48, 54, 48, I, 3.4)

@reg("com.endlessnetwork.whitehouse", RED_DARK)
def whitehouse():
    out = poly([(10, 22), (32, 10), (54, 22)], I, 2) + rrect(12, 40, 40, 6, 1, I) + rrect(10, 46, 44, 4, 1, I)
    for x in (16, 26, 36, 46):
        out += rrect(x - 2, 25, 4, 15, 1, I)
    return out

@reg("com.enjoyingfoss.Parlera", TEAL_LIGHT)
def parlera():
    return rrect(11, 15, 24, 24, 5, I) + rrect(29, 25, 24, 24, 5, H, ' stroke="INK" stroke-width="2.4"') + ink_stroke("M17 33L23 21L29 33M19.5 29H26.5", 3, H) + ink_stroke("M37 33H45M41 33V43", 3)

@reg("com.enjoyingfoss.feeel", RED_LIGHT)
def feeel():
    return line(20, 30, 44, 30, I, 4.4) + rrect(10, 20, 8, 20, 3, I) + rrect(46, 20, 8, 20, 3, I) + rrect(5, 25, 6, 10, 2, I) + rrect(53, 25, 6, 10, 2, I)

@reg("com.epicgames.ut2004", DEEP_PURPLE_DARK)
def ut2004():
    sk = path("M16 28A16 16 0 0 1 48 28C48 34 44 36 44 40V44H20V40C20 36 16 34 16 28Z", I)
    return sk + circle(25, 29, 4.4, H) + circle(39, 29, 4.4, H) + poly([(30, 35), (34, 35), (32, 39)], H, 0.6) + line(27, 44, 27, 49, I, 3) + line(37, 44, 37, 49, I, 3) + line(32, 44, 32, 49, I, 3)

@reg("com.epicgames.ut99", YELLOW)
def ut99():
    return path("M32 8C39 15 41 26 39 38H25C23 26 25 15 32 8Z", I) + circle(32, 24, 3.6, H) + poly([(25, 33), (13, 44), (26, 41)], I, 1.5) + poly([(39, 33), (51, 44), (38, 41)], I, 1.5) + path("M27 43H37L32 52Z", I)

@reg("com.esrille.furiganapad", PURPLE_SOFT)
def furigana():
    return (rrect(11, 11, 42, 38, 5, I) + line(20, 20, 26, 20, H, 2.2) + line(33, 20, 39, 20, H, 2.2)
            + line(17, 29, 31, 29, H, 4) + line(35, 29, 47, 29, H, 4) + line(20, 38, 26, 38, H, 2.2) + line(17, 44, 40, 44, H, 4))

@reg("com.evepreview.manager", BLUE_DARK)
def evepreview():
    return rrect(10, 10, 28, 22, 4, I, ' opacity=".55"') + rrect(22, 22, 28, 22, 4, I) + rrect(26, 26, 20, 11, 2, H)

@reg("com.exok.Celeste64", RED)
def celeste():
    s = path("M32 20C44 16 50 26 46 36C43 44 36 49 32 50C28 49 21 44 18 36C14 26 20 16 32 20Z", I)
    leaf = poly([(32, 20), (24, 12), (32, 14), (40, 12)], I, 1.6)
    return s + leaf + circle(25, 31, 1.8, H) + circle(39, 31, 1.8, H) + circle(32, 36, 1.8, H) + circle(28, 42, 1.8, H) + circle(36, 42, 1.8, H)

@reg("com.expidusos.calculator", GREY_DARK)
def calculator():
    return (rrect(13, 11, 38, 38, 6, I) + ink_stroke("M21 22H31M26 17V27", 3.2, H) + ink_stroke("M37 22H44", 3.2, H)
            + ink_stroke("M21 36L30 44M30 36L21 44", 3.2, H) + ink_stroke("M37 40H44", 3.2, H) + circle(40.5, 35, 0.01, H) + circle(40.5, 45, 0.01, H))
