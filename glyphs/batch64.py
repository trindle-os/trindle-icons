# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 64: sm.puri.Stream to spflashtool.

Same rules as batch01: tile is the palette step nearest the brand colour,
the mark is INK, HOLE is the tile showing through, extra shades come
from the palette.
"""
from lm import *
from glyphs.kit import arc, ell_b, gear_j, registry, ring_b, star_h
from glyphs.kit import shared_discord

ICONS, SMALL, reg, small = registry()

@reg("sm.puri.Stream", BLUE_DEEP)
def stream():
    play = poly([(26, 14), (42, 24), (26, 34)], INK, 4)
    bar = line(16, 43, 48, 43, INK, 3)
    return play + bar + circle(23, 43, 4.5, INK)

@reg("smplayer", BLUE_GREY_DEEP)
def smplayer():
    reel = circle(CX, CY, 17, INK)
    holes = "".join(circle(*pt(CX, CY, 9.5, a), 5, HOLE) for a in (0, 90, 180, 270))
    dots = "".join(circle(*pt(CX, CY, 2.4, a), 1.1, HOLE) for a in (30, 150, 270))
    return reel + holes + dots

@reg("sound-juicer", ORANGE_DEEP)
def sound_juicer():
    disc_ = cut(cpath(30, 28, 16) + cpath(30, 28, 4.5), INK)
    drop = path("M42 30C45.5 35 48.5 39 48.5 42.5A6.5 6.5 0 0 1 35.5 42.5C35.5 39 38.5 35 42 30Z",
                ORANGE_SOFT, f' stroke="{HOLE}" stroke-width="2.5"')
    return disc_ + drop

@reg("sound-recorder", RED)
def sound_recorder():
    mic = rrect(26, 12, 12, 21, 6, INK)
    holder = stroke("M20.5 27A11.5 11.5 0 0 0 43.5 27", INK, 3.2)
    stand = line(32, 39, 32, 46, INK, 3.2) + line(25.5, 46.5, 38.5, 46.5, INK, 3.2)
    return mic + holder + stand

@reg("soundcloud", DEEP_ORANGE)
def soundcloud():
    cloud = path("M30 22.5C31.5 19.5 35 17.5 38.5 17.5C44 17.5 48 21.5 48.5 27"
                 "C51 27.5 51 29 51 32C51 36 48.5 39 45 39H30Z", INK)
    bars = "".join(rrect(x, 39 - h, 2.2, h, 1.1, INK) for x, h in
                   [(13, 8), (16.5, 12), (20, 14), (23.5, 17), (27, 19)])
    return cloud + bars

@reg("soundkonverter", BROWN_SOFT)
def soundkonverter():
    arrows = (stroke(arc(29, 28, 12, 200, 330), INK, 3.6) +
              poly([(36.5, 16), (44.5, 20), (37, 25)], INK, 1.5) +
              stroke(arc(29, 28, 12, 20, 150), INK, 3.6) +
              poly([(21.5, 40), (13.5, 36), (21, 31)], INK, 1.5))
    badge = circle(41, 40, 10, HOLE) + circle(41, 40, 8, INK)
    note = (line(43, 35, 43, 43, HOLE, 1.8) + circle(40.8, 43.3, 2.3, HOLE) +
            line(43, 35, 46, 36, HOLE, 1.8))
    return arrows + badge + note

@reg("soundnode", PINK_DARK)
def soundnode():
    nodes = [(37, 14.5), (24, 21), (42, 24), (33, 30), (16.5, 34), (27, 42), (41, 39)]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (1, 4), (3, 4), (3, 6), (4, 5), (5, 6), (3, 5), (2, 6), (0, 3)]
    out = "".join(line(*nodes[a], *nodes[b], PINK_SOFT, 1.6) for a, b in edges)
    return out + "".join(circle(x, y, 3.3, INK) for x, y in nodes)

@reg("soundux", TEAL)
def soundux():
    duck = path("M20 20C20 15 23.5 12 27.5 12C31.5 12 34.5 15 34.5 19C34.5 22.5 32.5 24.5 31 26"
                "C33 28 36 28.5 39 27.5C42 26.5 45 23.5 48 22.5C49 29 48 36 43.5 40.5"
                "C40 44 35 45.5 29 45.5C22 45.5 16.5 41 16.5 35C16.5 30.5 19 28 22 26.5"
                "C21 25 20 23 20 20Z", INK)
    beak = poly([(19.5, 18), (13.5, 20), (19.5, 22.5)], INK, 2)
    eye = circle(27.5, 18.5, 2, HOLE)
    wing = stroke("M26 34C29 38 35 38.5 40 35.5", HOLE, 2.4)
    return duck + beak + eye + wing

@reg("soundwire", BROWN)
def soundwire():
    zig = stroke("M22 13L45 16.5L19 23L46 27L18 33.5L45 37.5L21 43.5L41 46.5", ORANGE_LIGHT, 4.4)
    return zig

@reg("sonic-visualiser", DEEP_ORANGE_DEEP)
def sonic_visualiser():
    return stroke("M13 31H18L20.5 25L23 36L25.5 19L28 41L30.5 14L33 45L35.5 21"
                  "L38 38L40.5 26L43 33L45.5 29H51", INK, 2.6)

@reg("sonic-pi", PINK_LIGHT)
def sonic_pi():
    pi = (line(14, 23, 29, 23, INK, 3.6) + line(17.5, 23, 17.5, 38, INK, 3.6) +
          line(25.5, 23, 25.5, 38, INK, 3.6))
    waves = (stroke("M35 22.5A11 11 0 0 1 35 37.5", INK, 2.8) +
             stroke("M40 17.5A17 17 0 0 1 40 42.5", INK, 2.8) +
             stroke("M45 13A23 23 0 0 1 45 47", INK, 2.8))
    return pi + waves

@reg("sonobus", PURPLE)
def sonobus():
    segs = [(-148, -42, INK), (-38, 28, BLUE_SOFT), (32, 138, INK), (142, 208, BLUE_SOFT)]
    return "".join(stroke(arc(CX, CY, 13, a0, a1), c, 7).replace('stroke-linecap="round"', 'stroke-linecap="butt"')
                   for a0, a1, c in segs)

@reg("soulseek", BLUE_DEEP)
def soulseek():
    wing_l = path("M31 29C25 29 18.5 26 14.5 19C19.5 21.5 24 22 28.5 21.5C29 18 30 15.5 33 13.5"
                  "C36 12.5 38.5 14 39.5 16L42 17L39.5 18C39.5 20 39 21.5 38 22.5"
                  "C42 23 46 21.5 49.5 19C47 25 41 29 35 29.5Z", INK)
    body = path("M31 29H35.5C36 34 35 38 32.5 41L35 46H28.5L29.5 41C28.5 37 29 32.5 31 29Z", INK)
    return wing_l + body + circle(35.5, 16.5, 1.1, HOLE)

@reg("spek", PINK_SOFT)
def spek():
    band = stroke("M16.5 34V27A15.5 15.5 0 0 1 47.5 27V34", INK, 3.6)
    cups = rrect(12.5, 27, 7, 15, 3.5, INK) + rrect(44.5, 27, 7, 15, 3.5, INK)
    face = circle(CX, 33, 12.5, INK)
    snout = ell_b(CX, 37, 5.5, 4, HOLE)
    nost = circle(29.8, 37, 1.2, INK) + circle(34.2, 37, 1.2, INK)
    eyes = circle(27, 29.5, 1.8, HOLE) + circle(37, 29.5, 1.8, HOLE)
    return band + cups + face + snout + nost + eyes

@reg("speedcrunch", PINK_DARK)
def speedcrunch():
    lines = "".join(rrect(15, y, w, 2.8, 1.4, INK) for y, w in
                    [(14, 20), (19.5, 14), (25, 20), (30.5, 11), (36, 16)])
    badge = circle(40, 38, 11, HOLE) + circle(40, 38, 9, ORANGE_LIGHT)
    eq = line(35.5, 35.5, 44.5, 35.5, INK, 2.6) + line(35.5, 40.5, 44.5, 40.5, INK, 2.6)
    return lines + badge + eq

def _mushroom(spots):
    cap = path("M14 31C14 19.5 22 12 32 12C42 12 50 19.5 50 31C50 33 48.5 34 46.5 34"
               "H17.5C15.5 34 14 33 14 31Z", INK)
    stem = path("M22 34H42L42.5 41.5C42.5 45 40 47 37 47H27C24 47 21.5 45 21.5 41.5Z", INK)
    gap = line(20, 34.5, 44, 34.5, HOLE, 1.6, "butt")
    eyes = rrect(26.5, 37, 2.8, 6, 1.4, HOLE) + rrect(34.7, 37, 2.8, 6, 1.4, HOLE)
    return cap + stem + gap + eyes + spots

@reg("smbx13", RED)
def smbx13():
    spots = (ell_b(32, 20.5, 6, 5, HOLE) + ell_b(18, 25.5, 3.3, 4.8, HOLE) +
             ell_b(46, 25.5, 3.3, 4.8, HOLE))
    return _mushroom(spots)

@reg("smc", LIGHT_BLUE)
def smc():
    return _mushroom(ell_b(32, 21, 9.5, 6.5, HOLE))

def _m_badge():
    disc_ = circle(CX, CY, 16.5, INK)
    m = poly([(19.5, 40), (22.5, 19.5), (27, 19.5), (32, 29), (37, 19.5), (41.5, 19.5),
              (44.5, 40), (39, 40), (37.5, 29.5), (33.5, 36), (30.5, 36), (26.5, 29.5), (25, 40)],
             HOLE, 1.2)
    return disc_ + m

@reg("smw-leveledit", DEEP_ORANGE_LIGHT)
def smw_leveledit():
    return _m_badge()

@reg("smw-worldedit", BLUE)
def smw_worldedit():
    return _m_badge()

@reg("smw", RED_DEEP)
def smw():
    cap = path("M14.5 32C14.5 20 22 13 32 13C41 13 47 18.5 48 26C50.5 27 51.5 29.5 50.5 32Z", INK)
    emblem = circle(30, 23, 6.3, HOLE)
    m = stroke("M26.5 26V20.5L30 24L33.5 20.5V26", INK, 2)
    stache = path("M17.5 40C20 36 25.5 35.5 32 37.5C38.5 35.5 44 36 46.5 40"
                  "C43.5 44 38 42.5 32 41.5C26 42.5 20.5 44 17.5 40Z", INK)
    return cap + emblem + m + stache

@reg("smilla", DEEP_PURPLE)
def smilla():
    cols = {(0, 0): AMBER_SOFT, (2, 1): RED_SOFT, (1, 3): BLUE_SOFT, (3, 4): AMBER, (4, 5): AMBER_SOFT}
    out = ""
    for r in range(6):
        for c in range(5):
            out += rrect(14 + c * 5.6 + r * 1.9, 13 + r * 5.6, 4.8, 4.8, .9, cols.get((c, r), INK))
    return out

@reg("smokinguns", BROWN)
def smokinguns():
    def gun():
        barrel = rrect(-2, -24, 4, 26, 1.5, INK)
        cyl = rrect(-3.8, 0, 7.6, 8, 2.5, INK)
        grip = path("M-1 7L5.5 13.5C7.5 15.5 7 18.5 4.5 19.5L1.5 20.5C0 16 -2 12 -3.5 8Z", INK)
        guard = stroke("M-1 10C-4 11 -4.5 14 -2.5 15", INK, 1.8)
        return barrel + cyl + grip + guard
    return (g(gun(), "translate(21 31) rotate(42)") +
            g(g(gun(), "scale(-1 1)"), "translate(43 31) rotate(-42)"))

@reg("snes9x", DEEP_PURPLE_DEEP)
def snes9x():
    return (circle(32, 17.5, 6.3, DEEP_PURPLE_SOFT) + circle(19.5, 30, 6.3, DEEP_PURPLE_SOFT) +
            circle(44.5, 30, 6.3, INK) + circle(32, 42.5, 6.3, INK))

@reg("so.libdb.gtkcord4", PURPLE_LIGHT)
def gtkcord4():
    return shared_discord()

def _sword(w=3.2):
    blade = poly([(15, 45), (17.5, 40), (37, 20.5), (39.5, 23), (20, 42.5)], INK, 1.5)
    guard = line(33, 18.5, 41.5, 27, INK, w)
    hilt = line(39, 21, 43.5, 16.5, INK, w)
    return blade + guard + hilt + circle(45, 15, 3.2, INK)

@reg("solarus", ORANGE_DEEP)
def solarus():
    sun = path("M13.5 42A18.5 18.5 0 0 1 50.5 42Z", ORANGE_SOFT)
    return sun + _sword()

@reg("solarus-launcher", AMBER_DEEP)
def solarus_launcher():
    pad = path("M22 20H42C47.5 20 51 24.5 51 30C51 35.5 47.5 40 42 40C38.5 40 36.5 37 34 37"
               "H30C27.5 37 25.5 40 22 40C16.5 40 13 35.5 13 30C13 24.5 16.5 20 22 20Z", INK)
    dpad = line(17.5, 30, 26.5, 30, HOLE, 3.2, "butt") + line(22, 25.5, 22, 34.5, HOLE, 3.2, "butt")
    btn = "".join(circle(x, y, 2, HOLE) for x, y in [(42, 25.5), (42, 34.5), (37.5, 30), (46.5, 30)])
    return pad + dpad + btn

@reg("solarus-quest-editor", AMBER_DARK)
def solarus_quest_editor():
    shield = path("M15 13H49V30C49 39 42 45 32 48.5C22 45 15 39 15 30Z", INK)
    brush = (line(22, 40, 37, 25, HOLE, 3.4) +
             path("M36 24C38 20 41.5 18 44.5 18.5C45 21.5 43 25 39 27Z", HOLE))
    hammer = (line(42, 40, 28, 26, HOLE, 3.4) +
              g(rrect(-6, -3.5, 12, 7, 1.5, HOLE), "translate(26 23) rotate(-45)"))
    return shield + brush + hammer

@reg("soma", TEAL_DARK)
def soma():
    face = path("M30 12.5C40 12.5 48 20.5 48 31C48 40.5 42 47.5 34 48.5C31 45 29 39 28.5 31"
                "C28 24 28.5 17.5 30 12.5Z", INK)
    eye = path("M26 27.5C30 22.5 38.5 22 44 27.5C38.5 33 30 32.5 26 27.5Z", HOLE)
    iris = circle(35, 27.5, 3.8, INK) + circle(35, 27.5, 1.6, HOLE)
    drips = (rrect(31.5, 31.5, 2.4, 8, 1.2, HOLE) + rrect(35.5, 31.5, 2.4, 5, 1.2, HOLE))
    tubes = (stroke("M16 18C20 18.5 24 21 26.5 25", INK, 3.2) +
             stroke("M15 28C19 28 23 30 26 33", INK, 3.2))
    return face + eye + iris + drips + tubes

@reg("somafm", RED_DEEP)
def somafm():
    return stroke("M41 20.5V17H23V21.5L41 38.5V43H23V39.5", INK, 5)

@reg("somiibo", BLUE)
def somiibo():
    ant = (line(29, 22, 26, 14, INK, 2.6) + circle(25.5, 13.5, 3, INK) +
           line(35, 22, 40, 15.5, INK, 2.6) + circle(40.5, 15, 3, INK))
    head = circle(32, 34, 12, INK)
    eye = circle(32, 34, 6.5, HOLE) + circle(32, 34, 4, INK) + circle(33.2, 32.6, 1.4, HOLE)
    return ant + head + eye

@reg("songkick", PINK)
def songkick():
    s = stroke("M29 22.5C28 20.5 26 19.5 23.5 19.5C20.5 19.5 18.5 21.2 18.5 23.5"
               "C18.5 28.5 29.5 27.5 29.5 33.5C29.5 36.5 27 38.5 23.5 38.5"
               "C20.5 38.5 18.5 37.5 17.5 35", INK, 4)
    k = line(35, 14, 35, 38.5, INK, 4.2) + line(46, 22, 36.5, 30.5, INK, 4.2) + line(39.5, 28.5, 47, 38.5, INK, 4.2)
    return s + k

@reg("sonic-mania", BLUE_DEEP)
def sonic_mania():
    head = path("M26 18C31 15.5 38 15.5 42.5 19C47 22.5 48.5 28 47.5 33.5L50 36.5L46 38"
                "C43.5 43 38.5 46 32.5 46C28 46 24 44 22 41L13 44L18.5 36.5L12 32L19 29L14 21.5"
                "L22 23L20 14Z", INK)
    ear = poly([(32, 16.5), (35, 10.5), (38.5, 17)], INK, 2)
    mask = path("M31.5 32C31 25.5 34 21.5 38.5 21.5C41 21.5 42.5 23 43 25C44.5 23 47 23 47.5 25.5"
                "C48 29 46 33 43 33.5C40 36 33 36.5 31.5 32Z", HOLE)
    pupils = ell_b(39.5, 28, 1.6, 2.8, INK) + ell_b(45, 28, 1.2, 2.4, INK)
    muzzle = path("M34 38C38 40 43 39.5 46 36.5C45 41 41 43.5 37 43C35 42.5 34 40.5 34 38Z", HOLE)
    return head + ear + mask + pupils + muzzle

@reg("space-engineers", BLUE_GREY_DARK)
def space_engineers():
    helmet = circle(33, 17.5, 5.2, INK)
    body = path("M27 24H39C41 24 42 25.5 42 27.5L41.5 36H38.5L38 48H34.5L33 38L31.5 48H28L27.5 36"
                "C26 34 25.5 31 25.5 28Z", INK)
    arm = stroke("M28 26L23 21L22.5 12.5", INK, 3.6)
    hand = rrect(20.5, 9.5, 4, 5.5, 1.5, INK)
    visor = ell_b(34.5, 17.5, 2.6, 2, HOLE)
    return helmet + visor + body + arm + hand

@reg("space-pirates-and-zombies", LIGHT_BLUE_DEEP)
def spaz():
    back = ell_b(CX, 31, 20, 6, "none", f' stroke="#5BC6F7" stroke-width="3" transform="rotate(-20 32 31)"')
    planet = circle(CX, 30, 12.5, INK)
    front = stroke("M12.8 36.5C14 40 23 39.5 32 36.8C41 34 50.5 29 51.5 24.5", HOLE, 6)
    front2 = stroke("M12.8 36.5C14 40 23 39.5 32 36.8C41 34 50.5 29 51.5 24.5", LIGHT_BLUE_SOFT, 3)
    return back + planet + front + front2

@reg("space.fips.Fips", BROWN_SOFT)
def fips():
    shell = path("M15 38C15 27 22 19.5 31 18.5C38 18 42 21 44 25C45.5 28 45 33 42 36"
                 "C40 38.5 37 38.5 35 37C33 40 33 44 36 47H21C17 45 15 42 15 38Z", INK)
    bands = (stroke("M21 24C24 28 24.5 36 21.5 45", HOLE, 1.8) +
             stroke("M28 20C31.5 25 32 33 28.5 45", HOLE, 1.8) +
             stroke("M35.5 19.5C38 23 39 28 38 33", HOLE, 1.8))
    head = path("M37 24C40 20 45 19.5 48 21.5C50 23 50.5 25.5 49 27C46.5 29 42 29.5 38.5 28Z", INK)
    ear = poly([(38, 22.5), (36.5, 13.5), (42.5, 20)], INK, 2)
    specs = ring_b(42, 23.5, 2.2, HOLE, 1.2) + ring_b(46.8, 23.2, 2.2, HOLE, 1.2)
    return shell + bands + head + ear + specs

@reg("spec-ops-the-line", AMBER)
def spec_ops():
    s = stroke("M29 17.5C28 15.5 25.5 14.5 23 14.5C19.5 14.5 17 16.5 17 19"
               "C17 25 29.5 23.5 29.5 30C29.5 33 26.5 35.5 23 35.5C20 35.5 17.5 34.5 16.5 32", INK, 4.2)
    o = ell_b(40.5, 25, 6.5, 9.5, "none", f' stroke="{INK}" stroke-width="4.2"')
    bar = rrect(14.5, 41.5, 35, 4.5, 1, INK)
    return s + o + bar

@reg("speed-dreams", RED_DEEP)
def speed_dreams():
    d = cut("M22 18H34C42 18 46 22.5 44.5 29.5C43 37.5 36.5 43 28 43H15Z"
            "M27.5 25L25 36H29C33.5 36 36.5 33 37.3 29.5C38 26.5 36.5 25 33.5 25Z", INK)
    stripes = (line(12, 23, 26, 23, HOLE, 2.2, "butt") + line(11, 30, 24, 30, HOLE, 2.2, "butt"))
    s = stroke("M50 11.5C49 10.5 47.5 10 46 10.2C44 10.5 43 12 43.8 13.3"
               "C44.8 15 49 14.8 49 17C49 18.7 47 19.8 45 19.5C43.5 19.3 42.5 18.7 42 18", INK, 2.4)
    return d + stripes + s

@reg("smartsim", CYAN_DEEP)
def smartsim():
    pins = "".join(rrect(x, 12, 2.2, 3, .6, INK) + rrect(x, 45, 2.2, 3, .6, INK)
                   for x in range(18, 46, 5))
    pins += "".join(rrect(12, y, 3, 2.2, .6, INK) + rrect(49, y, 3, 2.2, .6, INK)
                    for y in range(18, 46, 5))
    chip = rrect(15, 15, 34, 30, 3, INK)
    s = stroke("M38 22.5H28.5C26.5 22.5 25.5 23.5 25.5 25.5V27C25.5 29 26.5 30 28.5 30"
               "H35.5C37.5 30 38.5 31 38.5 33V34.5C38.5 36.5 37.5 37.5 35.5 37.5H26", HOLE, 4)
    return pins + chip + s

@reg("soapui", CYAN_DEEP)
def soapui():
    diamond = g(rrect(18, 16, 28, 28, 5, INK), "rotate(45 32 30)")
    s = stroke("M37 22.5C35.5 20.8 33.8 20.2 31.5 20.2C28 20.2 25.8 22.2 25.8 24.8"
               "C25.8 30 38.2 29 38.2 35C38.2 37.8 35.5 39.8 32 39.8C29.2 39.8 27.2 38.8 25.8 37", HOLE, 4.4)
    return diamond + s

@reg("sofastats", BROWN)
def sofastats():
    back = rrect(18, 16, 28, 18, 3, INK)
    seat = rrect(20, 31, 24, 7, 1.5, BROWN_SOFT)
    arms = rrect(13, 25, 7, 16, 2.5, INK) + rrect(44, 25, 7, 16, 2.5, INK)
    base = rrect(17, 38, 30, 4, 1, INK)
    legs = rrect(18, 41, 3.2, 5, .8, INK) + rrect(42.8, 41, 3.2, 5, .8, INK)
    return back + seat + arms + base + legs

@reg("software-properties", BLUE_GREY_DEEP)
def software_properties():
    cog = gear_j(CX, CY, 14, INK)
    arrow = (rrect(29, 18, 6, 11, 1, HOLE) + poly([(22.5, 28), (41.5, 28), (32, 39.5)], HOLE, 1.5))
    return cog + arrow

@reg("software-store", BLUE_DEEP)
def software_store():
    handle = stroke("M26 20V16.5C26 14.5 27 13.5 29 13.5H35C37 13.5 38 14.5 38 16.5V20", INK, 3)
    bag = rrect(14, 19, 36, 28, 4, INK)
    arrow = (line(32, 25, 32, 36, HOLE, 3.4) + stroke("M26.5 31.5L32 37L37.5 31.5", HOLE, 3.4) +
             line(25, 41.5, 39, 41.5, HOLE, 3))
    return handle + bag + arrow

@reg("solaar", TEAL)
def solaar():
    spokes = "".join(line(*pt(CX, CY, 9, a), *pt(CX, CY, 16.5, a), INK, 4.2) for a in range(0, 360, 60))
    return spokes + ring_b(CX, CY, 6.8, INK, 3.8)

@reg("solfege", DEEP_PURPLE_LIGHT)
def solfege():
    head = g(ell_b(0, 0, 7.5, 5.8, INK), "translate(25 41) rotate(-22)")
    stem = line(30.5, 40, 30.5, 14, INK, 3.4)
    flag = path("M29 12.5C33 15 41 18 44 23C46 27 45 32 42.5 35C43 30 41.5 25.5 36 23.5L29 21Z", INK)
    return head + stem + flag

@reg("spacefm", BLUE)
def spacefm():
    house = poly([(32, 12.5), (50, 29), (45, 29), (45, 46), (19, 46), (19, 29), (14, 29)], INK, 2.5)
    door = rrect(28.5, 35, 7, 11, 1, HOLE)
    return house + door

@reg("spacemacs", DEEP_PURPLE_LIGHT)
def spacemacs():
    planet = circle(34, 32, 15, DEEP_PURPLE_DEEP)
    swoosh = path("M14.5 17C22 12 34 13.5 46 44C43 36 34.5 26 27 22.5L28.5 30C24 24.5 20 20 14.5 17Z", INK)
    tail = stroke("M12.5 22C13 16.5 17 12.5 22.5 11", INK, 2.6)
    return planet + swoosh + tail

@reg("spaceview", LIGHT_BLUE_DARK)
def spaceview():
    band = ring_b(CX, CY, 13.5, INK, 6)
    used = stroke(arc(CX, CY, 13.5, -90, 0), ORANGE_LIGHT, 6)
    core = circle(CX, CY, 7.5, LIGHT_BLUE_SOFT)
    return band + used + core

@reg("sparkleshare", ORANGE_DEEP)
def sparkleshare():
    back = path("M14 18A3 3 0 0 1 17 15H26L29.5 18.5H47A3 3 0 0 1 50 21.5V26H14Z", ORANGE_SOFT)
    front = rrect(14, 21.5, 36, 25, 3.5, INK)
    return back + front + star_h(32, 34.5, 8, 3.6, HOLE, 2)

@reg("sparklogosmall", BLUE_DEEP)
def webex():
    w = stroke("M15 21C15 17.5 19 17 20.5 20.5L25.5 36C27 40 30 40 31 36L32 32"
               "L33 36C34 40 37 40 38.5 36L43.5 20.5C45 17 49 17.5 49 21", INK, 5.5)
    return w

@reg("spflashtool", ORANGE_DEEP)
def spflashtool():
    ant = (rrect(17, 12, 3, 3, 0, INK) + rrect(20, 15, 3, 3, 0, INK) +
           rrect(44, 12, 3, 3, 0, INK) + rrect(41, 15, 3, 3, 0, INK))
    head = rrect(20, 18, 24, 3.2, 0, INK) + rrect(17, 21, 30, 6, 0, INK)
    eyes = rrect(22, 22, 3.2, 3, 0, HOLE) + rrect(38.8, 22, 3.2, 3, 0, HOLE)
    body = rrect(17, 28.5, 30, 11, 0, INK)
    base = rrect(14, 42, 36, 5.5, 1.5, INK)
    return ant + head + eyes + body + base

@small("smokinguns")
def smokinguns_s():
    out = ""
    for sx in (1, -1):
        gun = (line(0, 0, 0, -28, INK, 4.2) + rrect(-4, -2, 8, 8, 2.5, INK) +
               path("M-2 5L6 13L1 16L-4 7Z", INK, f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"'))
        out += g(g(gun, f"scale({sx} 1)"), f"translate({32 - 10 * sx} 37) rotate({45 * sx})")
    return out

@small("smilla")
def smilla_s():
    cols = {(0, 0): AMBER_SOFT, (2, 1): RED_SOFT, (1, 2): BLUE_SOFT}
    return "".join(rrect(14 + c * 9 + r * 3, 13 + r * 9.5, 7.5, 7.5, 1.2, cols.get((c, r), INK))
                   for r in range(4) for c in range(3))

@small("soundnode")
def soundnode_s():
    nodes = [(36, 14), (19, 22), (44, 30), (31, 31), (23, 44)]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (1, 4), (0, 3)]
    out = "".join(line(*nodes[a], *nodes[b], PINK_SOFT, 2.4) for a, b in edges)
    return out + "".join(circle(x, y, 4.5, INK) for x, y in nodes)

@small("sonic-visualiser")
def sonic_visualiser_s():
    return stroke("M13 30H18L22 18L27 42L32 12L37 44L42 22L46 30H51", INK, 3.4)

@small("sonic-pi")
def sonic_pi_s():
    pi = (line(13, 22, 30, 22, INK, 4.4) + line(17.5, 22, 17.5, 40, INK, 4.4) +
          line(26, 22, 26, 40, INK, 4.4))
    waves = (stroke("M37 20A12 12 0 0 1 37 40", INK, 3.6) +
             stroke("M44 14A19 19 0 0 1 44 46", INK, 3.6))
    return pi + waves

@small("soma")
def soma_s():
    face = path("M28 12C40 12 49 20 49 31C49 41 42 48 33 48.5C29 44 26.5 38 26 31"
                "C25.5 24 26 17.5 28 12Z", INK)
    eye = path("M19 29C25 21 38 21 46 29C38 37 25 37 19 29Z", HOLE)
    return face + eye + circle(33, 29, 5.5, INK) + circle(33, 29, 2.2, HOLE)

@small("sonic-mania")
def sonic_mania_s():
    head = path("M27 17C32 14.5 39 15 43.5 19C48 23 49 29 47.5 34.5C45.5 42 39.5 46 32.5 46"
                "C28 46 24.5 44 22 41L12 43.5L18.5 36L11 31L19 28.5L13 20L22.5 22L20.5 12.5Z", INK)
    mask = path("M31 32C30.5 25 34 21 39 21C43 21 47.5 24 47 29C46.5 34 41 36 36 35.5"
                "C33.5 35.3 31.5 34 31 32Z", HOLE)
    return head + mask + ell_b(40.5, 28, 2.2, 3.6, INK)

@small("space.fips.Fips")
def fips_s():
    shell = path("M14 40C14 28 21 19.5 31 19C38.5 18.5 43.5 22.5 45 28C46 33 43 37.5 38 38"
                 "C36 41 36.5 44.5 38 47H20C16 45.5 14 43 14 40Z", INK)
    bands = stroke("M24 22C28 28 28 38 25 46", HOLE, 2.6) + stroke("M33 19.5C37 25 38 31 36.5 37", HOLE, 2.6)
    head = path("M37 25C40 20 45.5 19 49 21.5C51.5 23.5 51.5 26.5 49.5 28C46.5 30.5 41.5 31 38 29.5Z", INK)
    ear = poly([(38, 23), (36, 12.5), (43.5, 20.5)], INK, 2.5)
    return shell + bands + head + ear

@small("spek")
def spek_s():
    band = stroke("M15.5 32V27A16.5 16.5 0 0 1 48.5 27V32", INK, 4)
    cups = rrect(11, 26, 8, 16, 4, INK) + rrect(45, 26, 8, 16, 4, INK)
    face = circle(CX, 33, 12, INK)
    snout = ell_b(CX, 36.5, 6.5, 5, HOLE)
    return band + cups + face + snout + circle(29.5, 36.5, 1.6, INK) + circle(34.5, 36.5, 1.6, INK)

@small("speedcrunch")
def speedcrunch_s():
    lines = "".join(rrect(13, y, w, 4.2, 2.1, INK) for y, w in [(13, 24), (21, 16), (29, 12)])
    badge = circle(39, 37, 13, HOLE) + circle(39, 37, 11, ORANGE_LIGHT)
    eq = line(33.5, 33.5, 44.5, 33.5, INK, 3.4) + line(33.5, 40.5, 44.5, 40.5, INK, 3.4)
    return lines + badge + eq

@small("solarus-launcher")
def solarus_launcher_s():
    pad = path("M22 19H42C47.5 19 51 24 51 30C51 36 47.5 41 42 41C38.5 41 36.5 38 34 38"
               "H30C27.5 38 25.5 41 22 41C16.5 41 13 36 13 30C13 24 16.5 19 22 19Z", INK)
    dpad = line(16.5, 30, 27.5, 30, HOLE, 4.2, "butt") + line(22, 24.5, 22, 35.5, HOLE, 4.2, "butt")
    return pad + dpad + circle(38.5, 30, 3, HOLE) + circle(45, 30, 3, HOLE)

@small("speed-dreams")
def speed_dreams_s():
    d = cut("M20 16H34C43 16 48 21 46.5 29C45 38 38 44 28.5 44H13Z"
            "M27 24L24.5 36H29C33.5 36 37 33 38 29.5C38.8 26 37 24 33.5 24Z", INK)
    return d + line(10, 22, 24, 22, HOLE, 3, "butt") + line(9, 30, 22, 30, HOLE, 3, "butt")
