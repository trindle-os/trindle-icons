# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 22: distribution logos, archlinux to rosa.

Each tile takes the palette step nearest the distro's own brand colour.
The mark is drawn in INK (white, or near-black on pale tiles); HOLE is
the tile colour showing through the mark; any other shade is another
step from the same palette.
"""
from lm import *
from glyphs.kit import crescent_c, registry, ring_b, star_e
from glyphs.kit import shared_opensuse

ICONS, SMALL, reg, small = registry()

def D(name):
    return "distributor-logo-" + name

ARCH = ("M32 11.5C30.4 15.5 29.4 18 27.9 21.3C28.9 22.3 30.2 23.6 32.3 25"
        "C30 24 28.4 23.1 27.1 22.1C24.6 27.2 20.8 34.4 15.5 47.5C19.6 45.2 22.8 43.7 25.7 42.7"
        "C25.6 42.1 25.5 41.4 25.5 40.8C25.6 36 28.4 32.5 32 32.5C35.6 32.5 38.4 36.5 38.3 41"
        "C38.3 41.6 38.2 42.1 38.1 42.7C41 43.7 44.3 45.2 48.5 47.5C47.5 44.7 46.5 42.3 45.6 40.1"
        "C43.8 38.7 42 37.5 39 36.4C40.9 36.5 42.6 37.1 44.6 37.9C39.8 26.8 36.1 18.3 32 11.5Z")

@reg(D("archlinux"), BLUE_DEEP)
def archlinux():
    return path(ARCH, INK)

@reg(D("archman"), RED_DEEP)
def archman():
    tri = path("M32 11.5L48.5 47.5C44 44.5 39.5 43 35 42.5H29C24.5 43 20 44.5 15.5 47.5Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return tri + circle(32, 35, 8, HOLE) + ring_b(32, 35, 5.6, INK, 2.4) + star_e(32, 35.6, 3.4, 1.5, INK)

@reg(D("artix"), LIGHT_BLUE_DEEP)
def artix():
    return (poly([(30, 12), (37.7, 32), (25.5, 25)], INK, 1.5)
            + poly([(24.6, 28.7), (42.6, 35.7), (14, 48)], INK, 1.5)
            + poly([(44.3, 38.5), (50, 48), (36.1, 43.4)], INK, 1.5))

@reg(D("blackarch"), BLUE_GREY_DARK)
def blackarch():
    arch = stroke("M16 47L32 15L48 47", INK, 3) + stroke("M23 47C25 39 39 39 41 47", INK, 3)
    blade = poly([(30.5, 18), (33.5, 18), (33.5, 43), (32, 47.5), (30.5, 43)], INK, 1)
    guard = line(26, 20.5, 38, 20.5, INK, 3)
    hilt = line(32, 11, 32, 18, INK, 3.2)
    return arch + blade + guard + hilt

@reg(D("endeavouros"), DEEP_PURPLE)
def endeavouros():
    sliver = path("M31 13C25 22 19.5 33 15.5 43C17 43.5 18.5 43.5 20 43C24 32 28 22 31 13Z", RED_SOFT)
    sail = path("M32.5 12C38.5 21 45 32 49 41.5C50 44 48.5 45.5 45.5 45.5H20C24 33.5 28.5 22 32.5 12Z", INK)
    base = path("M20 45.5H45.5C46.5 45.5 47.5 45.3 48 45C45 47 40 48 35 48H19.5Z", DEEP_PURPLE_SOFT)
    return sliver + sail + base

@reg(D("manjaro"), TEAL_LIGHT)
def manjaro():
    return (path("M15 13H37V23.5H25.5V47H15Z", INK) + rrect(27.5, 25.5, 9.5, 21.5, .5, INK)
            + rrect(39, 13, 10, 34, .5, INK))

@reg(D("hyperbola"), GREY_DARK)
def hyperbola():
    top = path("M36.5 13C35.5 19 38 24.5 42.5 24.5C45.5 24.5 48.5 20 50 13"
               "C47 17 43.5 18.5 40.5 18C38 17.5 37 15.5 36.5 13Z", INK)
    arch = path("M13.5 47C19 38 28 29.5 36.5 27.5C41 26.5 43.5 29.5 43.5 35V47.5"
                "C41.5 42 39 37.5 35 37.5C28 37.5 20 41.5 13.5 47Z", INK)
    return top + arch

@reg(D("debian"), PINK_DEEP)
def debian():
    return stroke("M34 25.5C30.5 24.5 27.5 27.5 28 31C28.5 35 33 37.5 37.5 35.5"
                  "C42.5 33 44 26.5 41 21.5C37.5 15.5 29 14 23.5 18C17.5 22.5 16.5 31 19.5 38"
                  "C21.5 42.5 24.5 45.5 28 47.5", INK, 4)

@reg(D("devuan"), GREY_DARK)
def devuan():
    return path("M47 16C33 19 15.5 26.5 16 36C16.5 43.5 31 44.5 46.5 41"
                "C33.5 41.5 22.5 40.5 22.5 35.5C22.5 29 35 21.5 47 16Z", INK,
                f' stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"')

@reg(D("deepin"), LIGHT_BLUE_DEEP)
def deepin():
    swirl = (stroke("M18.5 25C24 20.5 33 20 38 24.5", HOLE, 2.6)
             + stroke("M22 34C21 28 26 24 32 25.5C37 27 38.5 32 36 35.5", HOLE, 2.6)
             + stroke("M47.5 30C46 37 40 41.5 33 41C28 40.5 25.5 37 27.5 33.5", HOLE, 2.6))
    return circle(CX, CY, 16.5, INK) + swirl

@reg(D("bunsenlabs"), AMBER_DEEP)
def bunsenlabs():
    flame = path("M33 11C34.5 18 43.5 22.5 43.5 33.5C43.5 41.5 38.5 47.5 32 47.5"
                 "C25.5 47.5 20.5 42.5 20.5 35.5C20.5 28.5 25.5 25 27 19C30 22 30.5 25.5 30 28.5"
                 "C32.5 24.5 34.5 18.5 33 11Z", INK)
    core = path("M32.5 32C35 35.5 37 37 37 40.5A4.8 4.8 0 0 1 27.5 40.5C27.5 37 30.5 35.5 32.5 32Z", HOLE)
    return flame + core

@reg(D("bodhi-linux"), BLUE)
def bodhi():
    leaf = path("M17 17C23 11.5 36 12 43 19.5C49.5 26.5 47 35.5 46.5 43.5L50.5 49L44.5 46.5"
                "C36.5 47 26.5 47.5 19.5 40C13 33 12 22 17 17Z", INK)
    vein = stroke("M20 20C28 27 37 36 45.5 45.5", HOLE, 2.2)
    return leaf + vein

@reg(D("linux-mint"), GREY_DEEP)
def linux_mint():
    badge = path("M14 13H21V17H43A6 6 0 0 1 49 23V39A9 9 0 0 1 40 48H24A9 9 0 0 1 15 39V20H14Z", INK)
    lm = stroke("M21 16V34A7 7 0 0 0 28 41H36A6 6 0 0 0 42 35V28.5A4 4 0 0 0 34 28.5V35"
                "M34 28.5A4 4 0 0 0 26 28.5V35", HOLE, 3)
    return badge + lm

@reg(D("lubuntu"), BLUE_DEEP)
def lubuntu():
    body = stroke("M42.5 18.5C40 14.5 33 14.5 30.5 19C28.5 23 31.5 26.5 34 29"
                  "C38 33 36.5 41.5 29 43.5L25 48", INK, 3.2)
    beak = poly([(40, 17), (50, 18.5), (41, 20.5)], INK, 1)
    wings = (stroke("M27 24C22 23.5 18 21 16 17", INK, 3)
             + stroke("M27 29.5C21.5 29.5 17.5 28 15 25.5", INK, 3)
             + stroke("M28 35C22 35.5 18 34.5 15.5 33", INK, 3))
    return body + beak + wings + circle(35, 19.5, 1.5, HOLE)

@reg(D("pop-os"), CYAN_DEEP)
def pop_os():
    p = stroke("M22 42L26 22", INK, 4.4) + ring_b(29.5, 26.5, 5.8, INK, 4.2)
    bang = line(42, 15, 39.5, 31, INK, 4.6) + circle(38.6, 37.5, 2.6, INK)
    return p + bang + rrect(16, 43, 32, 4, 2, INK)

@reg(D("peppermint"), RED_DEEP)
def peppermint():
    out = circle(CX, CY, 16.5, INK)
    for k in range(6):
        a = 60 * k
        p0 = pt(CX, CY, 14, a)
        p1 = pt(CX, CY, 14, a + 30)
        c0 = pt(CX, CY, 8, a - 30)
        c1 = pt(CX, CY, 8, a)
        out += path(f"M{CX} {CY}Q{f(c0[0])} {f(c0[1])} {f(p0[0])} {f(p0[1])}"
                    f"A14 14 0 0 1 {f(p1[0])} {f(p1[1])}"
                    f"Q{f(c1[0])} {f(c1[1])} {CX} {CY}Z", HOLE)
    return out

@reg(D("lxle"), GREY_DARK)
def lxle():
    bar = rrect(15, 12, 5, 36, 1, INK)
    x = (poly([(25, 12), (32, 12), (48, 26), (41, 26)], INK)
         + poly([(40, 12), (48, 12), (43, 17), (35, 17)], INK)
         + poly([(33, 21), (29, 26), (25, 26), (29, 21)], INK))
    e = (path("M30 30H48V35H31V43H48V48H30A5 5 0 0 1 25 43V35A5 5 0 0 1 30 30Z", INK)
         + poly([(36, 39), (48, 36), (48, 39.5), (36, 41)], INK))
    return bar + x + e

@reg(D("fedora"), BLUE_DEEP)
def fedora():
    bubble = path("M32 13.5A16.5 16.5 0 1 1 32 46.5H18.5A3 3 0 0 1 15.5 43.5V30A16.5 16.5 0 0 1 32 13.5Z", INK)
    fl = stroke("M24 40.5H28.5A4 4 0 0 0 32.5 36.5V26A4.5 4.5 0 0 1 37 21.5H41", HOLE, 4)
    bar = stroke("M26 31.5H39", HOLE, 4)
    return bubble + fl + bar

@reg(D("korora"), GREY_DARK)
def korora():
    back = path("M31 12H49V30A6 6 0 0 1 43 36H31A6 6 0 0 1 25 30V18A6 6 0 0 1 31 12Z", INK)
    front_edge = path("M15 48V32A9 9 0 0 1 24 23H30A9 9 0 0 1 39 32V39A9 9 0 0 1 30 48Z", HOLE)
    front = path("M18.5 44.5V32A5.5 5.5 0 0 1 24 26.5H30A5.5 5.5 0 0 1 35.5 32V39A5.5 5.5 0 0 1 30 44.5Z", INK)
    return back + front_edge + front

@reg(D("rhel"), RED_DEEP)
def rhel():
    hat = path("M22.5 17C25 14.5 29 15.5 32.5 16.8C35.5 15.5 39 14.5 41 17C43 20 44 25.5 45 29"
               "C48.5 30 51 31.5 51 34C51 38.5 42.5 40.5 31.5 38C21 35.5 13 32 13 27.5"
               "C13 25.5 15 24.5 18 24.5C18.5 26 20 27.5 23 28.5C21.5 25 21 20 22.5 17Z", INK)
    band = stroke("M20.5 26C28 30.5 37 31.5 44 30", HOLE, 2.4)
    return hat + band

@reg(D("condres"), TEAL)
def condres():
    return (poly([(14, 14), (50, 14), (32, 46)], INK, 2.5)
            + poly([(24, 14), (40, 14), (32, 29)], HOLE, 1))

def _tux(body, belly, cap=None):
    out = (path("M32 12C38 12 41 17 41 23C41 26 42 28 44.5 32C47.5 37 48 41 46 43.5"
                "L18 43.5C16 41 16.5 37 19.5 32C22 28 23 26 23 23C23 17 26 12 32 12Z", body)
           + path("M32 25C37.5 25 41 31 41 37C41 41.5 37 44 32 44C27 44 23 41.5 23 37"
                  "C23 31 26.5 25 32 25Z", belly)
           + circle(28.5, 19.5, 2.4, belly) + circle(35.5, 19.5, 2.4, belly)
           + circle(29, 20, 1.1, body) + circle(35, 20, 1.1, body)
           + path("M27.5 23.5C29.5 22 34.5 22 36.5 23.5C35.5 26 33.5 27 32 27C30.5 27 28.5 26 27.5 23.5Z", AMBER)
           + path("M17.5 46C17.5 43 20 41.5 23 42L29 45C29.5 47.5 27 48.5 24 48Z", AMBER)
           + path("M46.5 46C46.5 43 44 41.5 41 42L35 45C34.5 47.5 37 48.5 40 48Z", AMBER))
    if cap:
        out += path("M22.5 18C22.5 12.5 27 10 32 10C37.5 10 41.5 12.5 41.5 17.5H47"
                    "C47.5 19 46.5 20 45 20H23Z", cap)
    return out

@reg(D("knoppix"), GREY_LIGHT)
def knoppix():
    return _tux(INK, HOLE)

@reg(D("madlinux"), BLUE_DEEP)
def madlinux():
    return _tux(BLUE_DARK, INK, cap=INK)

@reg(D("calculate-linux"), ORANGE_DEEP)
def calculate():
    head = path("M15 49V28C15 19 21 13 29 13C35 13 39 16.5 40.5 21L49 23.5C50 24.5 49.5 26 48 26.3"
                "L40.5 27.5C39.5 32.5 35.5 36 31 38C37 40 43.5 42 49 45.5V49Z", INK)
    beak = path("M39.5 20.5L49.5 23.2C50.5 24.2 50 25.8 48.5 26.2L39.8 27.8Z", AMBER_SOFT)
    cap = path("M15 42V28C15 19 21 13 29 13C35 13 39 16.5 40.5 21L39.8 27.8"
               "C36 24.5 31 25 27 29C23 33 20 37.5 15 42Z", ORANGE_DARK)
    eye = circle(30, 20.5, 3.4, INK) + circle(30.8, 20.5, 1.6, ORANGE_DARK)
    return head + cap + beak + eye

@reg(D("freebsd"), RED_DEEP)
def freebsd():
    ball = circle(31, 32, 14, INK)
    horns = (path("M18.5 21.5C15 18.5 14 14.5 15.5 11C17.5 14.5 21.5 16.5 25 17.5C22 18 20 19.5 18.5 21.5Z", INK)
             + path("M38 16.5C41.5 13 45.5 11.5 49.5 12.5C50 16 49 20 46.5 23C45.5 20 42 17.5 38 16.5Z", INK))
    return ball + horns

@reg(D("dragonflybsd"), AMBER_DARK)
def dragonfly():
    def wing(cx, cy, rx, ry, rot):
        return f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" transform="rotate({rot} {f(cx)} {f(cy)})" fill="{INK}"/>'
    wings = (wing(23, 20.5, 9.5, 3.8, -12) + wing(41, 20.5, 9.5, 3.8, 12)
             + wing(23.5, 28, 8.5, 3.2, 14) + wing(40.5, 28, 8.5, 3.2, -14))
    body = (rrect(29.2, 17, 5.6, 32, 2.8, HOLE) + rrect(30.5, 18, 3, 30, 1.5, INK)
            + circle(32, 15, 3.8, HOLE) + circle(32, 15, 2.8, INK))
    return wings + body

@reg(D("ghostbsd"), TEAL_DEEP)
def ghostbsd():
    return stroke("M40 19C36.5 14 25.5 14.5 22.5 21C20 26.5 23.5 31.5 29 30.5"
                  "C34 29.5 37.5 23 39.5 18L32 42C30 47.5 22 48 19.5 43", INK, 4.2)

@reg(D("midnightbsd"), BLUE_GREY_DARK)
def midnightbsd():
    moon = crescent_c((31, 30), 16.5, (38.5, 24), 13, INK)
    cat = (path("M38.5 47C36.5 47 36 45 36.5 42.5C37 40 38 37.5 39.5 36.5L39 33.5L41 35H43.5L45.5 33.5"
                "L45.2 36.5C46.2 37.5 46.5 39 46 40.5C47.5 42 48 44.5 47 47Z", INK)
           + stroke("M47 45.5C49.5 44.5 50.5 42 49.5 39.5", INK, 1.8))
    return moon + cat

@reg(D("netbsd"), ORANGE_DEEP)
def netbsd():
    pole = line(26, 13, 19, 48, INK, 4.2)
    flag = path("M25 14C31 10.5 37 16.5 44 13.5C47 12.5 49 13.5 50 15"
                "C47.5 21.5 42 26.5 35 26C30.5 25.5 27 24.5 23 26.5Z", INK)
    streaks = (stroke("M31 17.5C35.5 19.5 40.5 18.5 45 17", HOLE, 1.8)
               + stroke("M30 22C34 23.5 38.5 23 42.5 21.5", HOLE, 1.8))
    return pole + flag + streaks

@reg(D("openbsd"), AMBER_DEEP)
def openbsd():
    body = star_e(33, 31, 15.5, 12, INK, n=14, rounding=1.2)
    tail = poly([(13.5, 24), (20.5, 30.5), (13.5, 37.5)], INK, 2)
    eye = circle(39, 26.5, 3.4, HOLE) + circle(39.8, 26.8, 1.6, INK)
    fin = stroke("M28 35C31 37.5 34.5 37.5 36.5 35", HOLE, 2)
    return tail + body + eye + fin

@reg(D("aryalinux"), ORANGE_DEEP)
def aryalinux():
    one = poly([(16, 47), (22, 47), (27, 13), (21, 13)], INK, 1.5)
    stem = poly([(28, 47), (34.5, 47), (40, 13), (33.5, 13)], INK, 1.5)
    foot = rrect(29, 41.5, 19, 5.5, 1, INK)
    return one + stem + foot

@reg(D("backbox"), BLUE_DEEP)
def backbox():
    outer = poly([(23, 13), (49, 13), (49, 38), (40, 47), (15, 47), (15, 21)], INK, 3)
    inner = poly([(25, 17.5), (44.5, 17.5), (44.5, 36), (38, 42.5), (19.5, 42.5), (19.5, 23)], HOLE, 2)
    return outer + inner

@reg(D("kali-linux"), BLUE_DEEP)
def kali():
    body = stroke("M41 21.5C33.5 20 27.5 24.5 27.5 30.5C27.5 36.5 33 39 39.5 39.5"
                  "C44.5 40 47.5 43 48.5 48", INK, 3)
    head = poly([(37.5, 19.5), (43.5, 20.5), (49.5, 25), (44, 25.8), (40, 24.5)], INK, 1.5)
    whiskers = (stroke("M38.5 19.5C31 14 22 11.5 13 11.5", INK, 2.2)
                + stroke("M37 21C30.5 18 23 17.5 14.5 18.5", INK, 2.2)
                + stroke("M34 22.5C29 22 23 23 18 25.5", INK, 2.2))
    return body + head + whiskers

@reg(D("kaos"), BLUE_DEEP)
def kaos():
    left = path("M20.5 47C17 40 16 26 21 17C23 14 26 14.5 26.5 18C27 26 25.5 37 20.5 47Z", INK)
    upper = path("M26 34C28 25 36 16 46 15C49 15 50 17 48 19.5C42 26 35 31 26 34Z", INK)
    lower = path("M28 37C35 33 44 34 49.5 40C51 42 50 44 47.5 44C40 44 33 41.5 28 37Z", INK)
    return left + upper + lower

@reg(D("linux-lite"), AMBER_DEEP)
def linux_lite():
    feather = path("M41 11C31.5 14 23 24 22 34.5C21.5 39.5 23 43.5 25.5 46"
                   "C33 42 40 33 42.5 22C43.3 18 42.5 14 41 11Z", INK)
    quill = stroke("M39.5 16C35 27 30 37 24.5 48", HOLE, 1.8) + line(24.5, 45, 22, 50, INK, 2.2)
    return feather + quill

@reg(D("mac"), BLUE_DEEP)
def mac():
    right = rrect(15, 13, 34, 34, 6, INK)
    left = path("M21 13H34C31.5 19.5 29.5 25.5 29 32H33.5C33.5 37.5 34 42.5 35 47H21"
                "A6 6 0 0 1 15 41V19A6 6 0 0 1 21 13Z", BLUE_SOFT)
    face = (line(24.5, 20.5, 24.5, 25.5, BLUE_DARK, 2.6) + line(40, 20.5, 40, 25.5, BLUE_DARK, 2.6)
            + stroke("M21.5 35.5C28 40.5 36.5 40.5 43 35.5", BLUE_DARK, 2.6))
    return right + left + face

@reg(D("ms-dos"), INDIGO)
def ms_dos():
    ms = (stroke("M17 27V14L22.5 22L28 14V27", INK, 3)
          + stroke("M44 15.5C42.5 13.5 35 13 35 17.5C35 21.5 44.5 19.5 44.5 23.5C44.5 27.5 37 27.5 34.5 25.5", INK, 3))
    dos = (stroke("M14.5 33.5V46H17.5A6 6 0 0 0 17.5 33.5Z", AMBER_SOFT, 2.8)
           + ring_b(31, 39.75, 5.6, PINK_SOFT, 2.8)
           + stroke("M48.5 35C47 33 40.5 32.5 40.5 36.5C40.5 40 49 38.5 49 42.5C49 46.5 42 46.5 40 44.5", AMBER_SOFT, 2.8))
    return ms + dos

@reg(D("mx"), BLUE_GREY_DARK)
def mx():
    mount = poly([(13, 47), (28.5, 27.5), (34, 34), (38.5, 29.5), (51, 47)], INK, 2)
    cross = (line(21, 14, 47, 44.5, HOLE, 6) + line(21, 14, 47, 44.5, INK, 3)
             + line(44, 14, 33.5, 25.5, INK, 3))
    return mount + cross

@reg(D("netrunner"), BLUE_DARK)
def netrunner():
    disc_ = circle(CX, CY, 16.5, BLUE_GREY_LIGHT)
    arrow = poly([(16, 26.5), (47, 15), (36.5, 46), (31.5, 31.5)], BLUE_GREY_DARK, 4)
    inner = poly([(20.5, 27), (43, 18.5), (35.5, 40.5), (32, 30)], INK, 1.5)
    return disc_ + arrow + inner

@reg(D("nixos"), BLUE_DARK)
def nixos():
    y = CY - 8
    sx, sy = pt(CX - 4.6, y, 7.6, -120)
    one = (line(CX - 13.5, y, CX + 3.5, y, "C", 3.4, cap="butt")
           + line(CX - 4.6, y, sx, sy, "C", 3.4, cap="butt"))
    out = ""
    for k in range(6):
        c = INK if k % 2 == 0 else BLUE_SOFT
        out += g(one.replace('"C"', f'"{c}"'), f"rotate({60 * k} {CX} {CY})")
    return out

@reg(D("openmandriva"), BLUE_DEEP)
def openmandriva():
    return (circle(CX, CY, 16.5, INK) + circle(34.5, 27.5, 12.8, HOLE)
            + circle(34.5, 27.5, 10, INK) + circle(35, 27, 7, HOLE))

@reg(D("opensuse"), BLUE_GREY_LIGHT)
def opensuse():
    return shared_opensuse()

@reg(D("parrot"), CYAN)
def parrot():
    return poly([(16, 17.5), (23.5, 13.5), (35, 15.5), (49.5, 42), (43, 38.5),
                 (40, 49), (38, 36), (33.5, 32), (27, 19.5), (21, 19.5),
                 (20.5, 25), (17.5, 21.5)], INK, 1.5)

@reg(D("pclinuxos"), BLUE_DEEP)
def pclinuxos():
    bull = (path("M23 34C23 30.5 25.5 28.5 29 28L37.5 27.5C40.5 27.5 42.5 28.5 43.5 30.5"
                 "C44.3 32 44 34 43 35.5L43.5 40H41L40 36.5C37 37 34 37 31 36.5L30 40H27.5L27 36"
                 "C25.5 36 24 35.5 23 34Z", INK)
            + path("M24.5 29.5C21.5 30 19.5 32.5 19.5 35.5L22.5 37L25.5 34.5Z", INK)
            + stroke("M22.5 31C20.5 29 20.5 26.5 22.5 25", INK, 1.8)
            + stroke("M43.5 30.5C45.5 29 46 26.5 45 24", INK, 1.8))
    return ring_b(CX, CY, 16, INK, 3.4) + bull

@reg(D("pisilinux"), PINK_DEEP)
def pisilinux():
    head = path("M17.5 23L16.5 12L25.5 17C29.5 16 34.5 16 38.5 17L47.5 12L46.5 23"
                "C48.5 26.5 49.5 30 49 34C47.5 42.5 40.5 47 32 47C23.5 47 16.5 42.5 15 34"
                "C14.5 30 15.5 26.5 17.5 23Z", INK)
    eyes = (f'<ellipse cx="25.5" cy="31" rx="3" ry="3.6" fill="{HOLE}"/>'
            f'<ellipse cx="38.5" cy="31" rx="3" ry="3.6" fill="{HOLE}"/>')
    nose = poly([(29.5, 37), (34.5, 37), (32, 39.5)], HOLE, 1.2)
    stripes = (line(32, 19.5, 32, 24, HOLE, 2) + line(28, 20, 28.5, 23.5, HOLE, 1.8)
               + line(36, 20, 35.5, 23.5, HOLE, 1.8))
    return head + eyes + nose + stripes

@reg(D("puppy-linux"), GREY_DARK)
def puppy():
    head = path("M17 26C16 19 22 14 30 14H37C44.5 14 49 19 49 26V34C49 42 43 47 35 47"
                "H29C21 47 16 41.5 16 34Z", INK)
    ear = path("M15 17C17 13 22 12 26 14C25 20 22.5 25 18.5 28C16 25 14.5 21 15 17Z", GREY_LIGHT)
    eye = circle(25.5, 32.5, 5, HOLE) + circle(26, 32.5, 2.2, INK)
    nose = f'<ellipse cx="43.5" cy="31" rx="3" ry="2.4" fill="{HOLE}"/>'
    mouth = stroke("M35 39.5C38 41.5 42 41 44.5 38.5", HOLE, 2)
    return head + ear + eye + nose + mouth

@reg(D("pureos"), BLUE_GREY_DARK)
def pureos():
    return rrect(16.5, 20.5, 31, 19, 1.5, "none", f' stroke="{INK}" stroke-width="4.2"')

@reg(D("raspbian"), RED_DEEP)
def raspbian():
    leaves = (path("M31 21C26 21.5 19.5 19.5 18.5 13.5C24 12.5 29.5 15 31 21Z", INK)
              + path("M33 21C38 21.5 44.5 19.5 45.5 13.5C40 12.5 34.5 15 33 21Z", INK))
    berry = "".join(circle(x, y, 4.6, INK) for x, y in
                    [(27, 26.5), (37, 26.5), (22.5, 33.5), (32, 33), (41.5, 33.5),
                     (26.5, 40), (37.5, 40), (32, 45)])
    seams = "".join(ring_b(x, y, 4.6, HOLE, 1) for x, y in
                    [(32, 33), (26.5, 40), (37.5, 40)])
    return leaves + berry + seams

@reg(D("rosa"), INDIGO_DEEP)
def rosa():
    return (ring_b(CX, CY, 15, INK, 3.6)
            + stroke("M20 42C19 30 27 19 43 17.5", INK, 3.6))

@reg(D("freedos"), BLUE_GREY_LIGHT)
def freedos():
    body = path("M14 42C13 29.5 20 19.5 30.5 19.5C38.5 19.5 42.5 24.5 43.5 31.5"
                "C45.5 28.5 48 26.5 51 25.5C50 31.5 50 36.5 51 42Z", INK)
    eyes = (circle(23, 33, 3.8, HOLE) + circle(31.5, 33, 3.8, HOLE)
            + circle(23.8, 33.5, 1.7, INK) + circle(32.3, 33.5, 1.7, INK))
    return body + eyes

@small(D("archman"))
def archman_s():
    tri = path("M32 11.5L48.5 47.5C44 44.5 39.5 43 35 42.5H29C24.5 43 20 44.5 15.5 47.5Z", INK,
               f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    return tri + circle(32, 35, 6.5, HOLE) + circle(32, 35, 3, INK)

@small(D("ms-dos"))
def ms_dos_s():
    return (stroke("M13.5 22V38H16.5A6 8 0 0 0 16.5 22Z", INK, 3.4)
            + ring_b(31.5, 30, 5.6, INK, 3.4)
            + stroke("M50 23.5C48.5 21.5 42 21 42 25.5C42 29.5 50.5 28.5 50.5 33"
                     "C50.5 37.5 44 38 41.5 36", INK, 3.4))

@small(D("kali-linux"))
def kali_s():
    body = stroke("M41 21.5C33.5 20 27.5 24.5 27.5 30.5C27.5 36.5 33 39 39.5 39.5"
                  "C44.5 40 47.5 43 48.5 48", INK, 3.4)
    head = poly([(37, 19), (43.5, 20), (50, 25), (44, 26.5), (39.5, 25)], INK, 2)
    return (body + head + stroke("M38.5 19.5C31 14 22 12 14 12.5", INK, 2.6)
            + stroke("M36 22C30 20 23 20.5 16 23", INK, 2.6))

@small(D("lubuntu"))
def lubuntu_s():
    body = stroke("M42.5 18.5C40 14.5 33 14.5 30.5 19C28.5 23 31.5 26.5 34 29"
                  "C38 33 36.5 41.5 29 43.5L25 48", INK, 3.6)
    beak = poly([(40, 16.5), (50, 18.5), (41, 21)], INK, 1.5)
    wings = (stroke("M27 24.5C22 24 18 21.5 16 18", INK, 3.4)
             + stroke("M27.5 32C22 32.5 18 31 15.5 28.5", INK, 3.4))
    return body + beak + wings

@small(D("lxle"))
def lxle_s():
    bar = rrect(14.5, 12, 6, 36, 1, INK)
    x = stroke("M27 13.5L47 26M47 13.5L27 26", INK, 4.4)
    e = (path("M30 30H48V35.5H31.5V42.5H48V48H30A5 5 0 0 1 25 43V35A5 5 0 0 1 30 30Z", INK))
    return bar + x + e

@small(D("pclinuxos"))
def pclinuxos_s():
    bull = (path("M20 35C20 30 24 27.5 29 27.5H38C42 27.5 44.5 29.5 44.5 33V40H40.5L39.5 37H30L29 40H25"
                 "L24.5 37.5C22 37.5 20 36.5 20 35Z", INK)
            + stroke("M22.5 30C20.5 28 20.5 25.5 22.5 24", INK, 2.6))
    return ring_b(CX, CY, 16, INK, 3.4) + bull

@small(D("peppermint"))
def peppermint_s():
    out = circle(CX, CY, 16.5, INK)
    for k in range(4):
        a = 90 * k
        p0 = pt(CX, CY, 13.5, a)
        p1 = pt(CX, CY, 13.5, a + 45)
        c0 = pt(CX, CY, 8, a - 35)
        c1 = pt(CX, CY, 8, a + 10)
        out += path(f"M{CX} {CY}Q{f(c0[0])} {f(c0[1])} {f(p0[0])} {f(p0[1])}"
                    f"A13.5 13.5 0 0 1 {f(p1[0])} {f(p1[1])}"
                    f"Q{f(c1[0])} {f(c1[1])} {CX} {CY}Z", HOLE)
    return out

@small(D("raspbian"))
def raspbian_s():
    leaves = (path("M31 22C26 22.5 19 20 18 13.5C24 12.5 29.5 15.5 31 22Z", INK)
              + path("M33 22C38 22.5 45 20 46 13.5C40 12.5 34.5 15.5 33 22Z", INK))
    berry = path("M32 22.5C40 22.5 45.5 27 45.5 33.5C45.5 41 39 48 32 48"
                 "C25 48 18.5 41 18.5 33.5C18.5 27 24 22.5 32 22.5Z", INK)
    seeds = (stroke("M21.5 31C28 35 36 35 42.5 31", HOLE, 2.2)
             + stroke("M23.5 40C29 43 35 43 40.5 40", HOLE, 2.2))
    return leaves + berry + seeds

@small(D("puppy-linux"))
def puppy_s():
    head = path("M17 26C16 19 22 14 30 14H37C44.5 14 49 19 49 26V34C49 42 43 47 35 47"
                "H29C21 47 16 41.5 16 34Z", INK)
    return head + circle(26, 31.5, 5.5, HOLE) + f'<ellipse cx="42.5" cy="31" rx="3.6" ry="3" fill="{HOLE}"/>'

@small(D("openbsd"))
def openbsd_s():
    body = star_e(33, 31, 15.5, 12.5, INK, n=9, rounding=1.5)
    tail = poly([(13.5, 23.5), (21, 30.5), (13.5, 38)], INK, 2)
    return tail + body + circle(39, 27, 3.6, HOLE)
