# SPDX-License-Identifier: GPL-3.0-or-later
"""Batch 6: alc to aperture-desk-job.

Same rules as batch01: tile from the palette step nearest the brand
colour, mark in INK, HOLE for cut-throughs, any second shade another
palette step.
"""
from lm import *
from glyphs.kit import ell_b, gear, registry, ring_b, star_c

ICONS, SMALL, reg, small = registry()

MIRROR = "matrix(-1 0 0 1 64 0)"

@reg("alc", GREY_DEEP)
def alc():
    ears = (g(ell_b(24, 20, 4.6, 10.5, INK), "rotate(-14 24 20)") +
            g(ell_b(40, 20, 4.6, 10.5, INK), "rotate(14 40 20)"))
    inner = (g(ell_b(24, 19, 1.8, 6.5, HOLE), "rotate(-14 24 19)") +
             g(ell_b(40, 19, 1.8, 6.5, HOLE), "rotate(14 40 19)"))
    head = ell_b(32, 37.5, 13, 10.5, INK)
    face = (circle(27, 35.5, 1.9, HOLE) + circle(37, 35.5, 1.9, HOLE) +
            ell_b(32, 40.5, 2.4, 1.7, PINK_SOFT))
    return ears + inner + head + face

@reg("alexandra", ORANGE_DARK)
def alexandra():
    reels = (circle(22.5, 19.5, 6.5, INK) + circle(22.5, 19.5, 2.6, HOLE) +
             circle(35.5, 19.5, 6.5, INK) + circle(35.5, 19.5, 2.6, HOLE))
    body = rrect(15, 26.5, 28, 18, 4, INK)
    lens = poly([(41, 32), (49.5, 27.5), (49.5, 43.5), (41, 39)], INK, 2.5)
    return reels + body + lens

@reg("alltomp3", DEEP_ORANGE)
def alltomp3():
    return (ring_b(CX, CY, 15.5, INK, 3) +
            poly([(28, 22.5), (40.5, 30), (28, 37.5)], INK, 3.5))

@reg("alltray", INDIGO)
def alltray():
    frame = rrect(16.5, 14.5, 31, 31, 5, "none",
                  f' stroke="{INK}" stroke-width="3.2"')
    corner = poly([(31, 14.5), (47.5, 14.5), (47.5, 31)], INK, 3)
    return frame + corner

@reg("allusion", TEAL_LIGHT)
def allusion():
    return path("M31.5 12.5C35 12.5 36 18 37 24C38.5 32 49 35.5 49 42"
                "C49 47 44 47 39.5 46C35 45 29.5 44.5 24.5 46C19.5 47.5 15 46.5 15 42.5"
                "C15 37.5 25 35 27 27C28.5 20 28.5 12.5 31.5 12.5Z", INK)

@reg("almanah", RED_DEEP)
def almanah():
    book = rrect(17, 11.5, 30, 37, 4, INK) + rrect(21.5, 11.5, 2.6, 37, 0, HOLE)
    lock = (stroke("M30 29V25.5A4.5 4.5 0 0 1 39 25.5V29", HOLE, 3) +
            rrect(27, 28.5, 15, 12, 2.5, HOLE) + circle(34.5, 34.5, 2, INK))
    return book + lock

@reg("alterator", ORANGE_DEEP)
def alterator():
    return gear(CX, CY, 17, 12.5, 9, INK) + circle(CX, CY, 6.5, HOLE)

@reg("altmediawriter", AMBER_DEEP)
def altmediawriter():
    stick = rrect(19.5, 11.5, 25, 29, 5, INK)
    plug = (rrect(25, 39, 14, 9.5, 2, INK) + rrect(28, 42, 2.8, 2.8, .5, HOLE) +
            rrect(33.2, 42, 2.8, 2.8, .5, HOLE))
    peng = (ell_b(31, 29, 6, 8, HOLE) + circle(32, 20, 4.4, HOLE) +
            poly([(35, 18.5), (40.5, 20.5), (35, 22.3)], HOLE, 1.2) +
            ell_b(33, 30, 3.3, 6, INK) + circle(33, 19.5, 1.1, INK))
    return stick + plug + peng

@reg("altus", BLUE_DARK)
def altus():
    wing = poly([(15, 14), (39, 21), (31, 33)], INK, 2)
    body = poly([(31, 33), (39, 21), (49, 24.5), (43.5, 29)], BLUE_SOFT, 2)
    tail = poly([(31, 33), (37.5, 30.5), (24.5, 47)], INK, 2)
    return wing + body + tail

@reg("amarok", BLUE_DEEP)
def amarok():
    wolf = path("M14 31L20 28.5L19.5 21L25.5 24.5C29 19.5 34 16.5 38.5 15L45 10"
                "C47 9.5 47.5 11.5 46.5 13.5L43.5 17.5L49.5 18L45 22L40 24"
                "C39 30 39.5 39 41 48H27C26.5 42 23 37.5 17 35.5L20.5 34Z", INK)
    eye = path("M30 25C31 22.5 33 21.5 35 21.5C34 23.5 32.5 25 30 25Z", HOLE)
    return wolf + eye

@reg("amazon-store", BLUE_GREY_DARK)
def amazon():
    a = (ring_b(29.5, 29.5, 5.5, INK, 3.8) +
         stroke("M24.5 19.5C26.5 16.5 35 16 35 22.5V35.5", INK, 3.8))
    smile = (stroke("M16.5 40C24.5 45.5 36.5 46 44.5 40.5", ORANGE, 3.2) +
             stroke("M40.5 38.5L45.5 39.5L45 44.5", ORANGE, 3))
    return a + smile

@reg("amd", RED_DEEP)
def amd():
    d = ("M14.2 14.1L24 24H40V39.9L50 49.9V14.1Z"
         "M24 26.3L14 36.1V50H28.75L38.6 40H24Z")
    return g(path(d, INK), "translate(32 30) scale(.92) translate(-32 -32)")

@reg("angrysearch", RED_DEEP)
def angrysearch():
    return "".join(rrect(x, y, 13, 13, 3.5, INK) for x in (17.5, 33.5) for y in (15.5, 31.5))

@reg("anoise", ORANGE_DEEP)
def anoise():
    return circle(CX, CY, 16.5, INK) + stroke("M28.5 21L37.5 30L28.5 39", HOLE, 5)

@reg("another-redis-desktop-manager", RED_DEEP)
def redis_dm():
    s = poly(star_c(30, 32, 14, 6.3, -104), "none")
    s = s.replace('fill="none"', f'fill="none" stroke="{INK}" stroke-width="3.8" stroke-linejoin="round"')
    return s + circle(45.5, 15.5, 3.3, INK)

@reg("anydesk", RED)
def anydesk():
    left = g(rrect(17, 22, 16, 16, 2.5, "none", f' stroke="{INK}" stroke-width="3.2"'), "rotate(45 25 30)")
    right = g(rrect(28, 20, 20, 20, 3, INK, f' stroke="{HOLE}" stroke-width="2.4"'), "rotate(45 38 30)")
    return left + right

@reg("apachedirectorystudio", BLUE_DEEP)
def apachedirectorystudio():
    trunk = stroke("M32 46V30", INK, 4.2)
    boughs = (stroke("M32 34L22 24L18 25", INK, 3) + stroke("M32 34L42 24L46 25", INK, 3) +
              stroke("M32 30L25 18L20 15", INK, 2.8) + stroke("M32 30L39 18L44 15", INK, 2.8) +
              stroke("M32 31V13", INK, 2.8) + stroke("M25 18L27 13", INK, 2.4) +
              stroke("M39 18L37 13", INK, 2.4) + stroke("M22 24L16 20", INK, 2.4) +
              stroke("M42 24L48 20", INK, 2.4))
    roots = stroke("M24 47L32 43L40 47", INK, 2.8)
    return boughs + trunk + roots

@reg("aperture-desk-job", DEEP_ORANGE)
def aperture():
    disc = cut(cpath(CX, CY, 16.5) + cpath(CX, CY, 7), INK)
    bands = (rrect(14, 20.2, 36, 2.8, 0, HOLE) + rrect(14, 37, 36, 2.8, 0, HOLE))
    return disc + bands

def _swarm():
    claw = path("M19.5 45L21.5 30C23.5 21 28 14 33.5 11.5C38.5 13 41.5 18.5 42.5 25.5"
                "C44 33 46.5 40.5 44.5 48C41 43 38 36 36.5 30.5L33.5 21.5"
                "C31 27 29 36 27.5 45.5Z", INK)
    teeth = (poly([(37.8, 24), (43, 25.5), (38.8, 27.5)], HOLE, .8) +
             poly([(39.3, 30), (44.5, 32), (40.2, 33.5)], HOLE, .8) +
             poly([(40.7, 36), (46, 38.5), (41.8, 39.5)], HOLE, .8) +
             poly([(18, 37), (22.5, 35.5), (21.5, 39)], HOLE, .8))
    return g(claw + teeth, "rotate(10 32 30)")

@reg("alien-swarm", BLUE_GREY_DARK)
def alien_swarm():
    return _swarm()

@reg("alien-swarm-reactive-drop", DEEP_ORANGE_DARK)
def alien_swarm_rd():
    return _swarm()

@reg("alien-isolation", ORANGE_DARK)
def alien_isolation():
    egg = path("M32 11.5C40.5 11.5 46.5 23.5 46.5 32.5C46.5 42 40 48.5 32 48.5"
               "C24 48.5 17.5 42 17.5 32.5C17.5 23.5 23.5 11.5 32 11.5Z", INK)
    slit = stroke("M22.5 32L30.5 43L40 34", YELLOW_LIGHT, 3.8)
    seam = stroke("M22.5 32L30.5 43L40 34", HOLE, 7.5)
    return egg + seam + slit

@reg("alienarena", BLUE_GREY)
def alienarena():
    rim = ring_b(CX, CY, 14.5, INK, 4.5)
    eye = path("M19 25.5C24 25 28.5 28 29 33C24 33.5 20 30.5 19 25.5Z", INK)
    return rim + eye + g(eye, MIRROR)

@reg("alienblaster", TEAL_DEEP)
def alienblaster():
    wings = path("M25 24H39L49 40C49 43 47 44.5 44 44.5H20C17 44.5 15 43 15 40Z", INK)
    rails = (rrect(19.5, 22, 4, 21, 2, INK, f' stroke="{HOLE}" stroke-width="1.8"') +
             rrect(40.5, 22, 4, 21, 2, INK, f' stroke="{HOLE}" stroke-width="1.8"'))
    ship = path("M27 43V22C27 16.5 29.5 12.5 32 11C34.5 12.5 37 16.5 37 22V43"
                "C37 46 35 47.5 32 47.5C29 47.5 27 46 27 43Z", INK,
                f' stroke="{HOLE}" stroke-width="2"')
    return wings + rails + ship + ell_b(32, 35, 3.2, 4.2, HOLE)

@reg("alienfx", BLUE_DEEP)
def alienfx():
    head = path("M32 11.5C42 11.5 48 18.5 48 27C48 37 38.5 48.5 32 48.5"
                "C25.5 48.5 16 37 16 27C16 18.5 22 11.5 32 11.5Z", INK)
    eye = path("M19.5 27C24 26.5 28.5 29 29.5 34C25 34.5 21 31.5 19.5 27Z", HOLE)
    return head + eye + g(eye, MIRROR)

def _subs(cx, cy, s=1.0, w=4.2):
    d = "M37.5 23.5H28.5L25.5 26.5V28.5L28 31H36L38.5 33.5V35.5L35.5 38.5H26.5"
    return g(stroke(d, HOLE, w), f"translate({cx} {cy}) scale({s}) translate(-32 -31)")

@reg("allegorithmic-Substance_Alchemist", ORANGE_DEEP)
def substance_alchemist():
    return poly([(32, 11.5), (50, 45), (14, 45)], INK, 5) + _subs(32, 34.5, .9)

@reg("allegorithmic-Substance_B2M", TEAL_LIGHT)
def substance_b2m():
    return gear(CX, CY, 17, 13.5, 8, INK, .5, 2.5) + _subs(32, 30, .85)

@reg("allegorithmic-Substance_Designer", DEEP_ORANGE)
def substance_designer():
    tabs = circle(15.5, 30, 3.2, INK) + circle(48.5, 30, 3.2, INK) + circle(32, 13.5, 3.2, INK)
    return tabs + rrect(17.5, 15.5, 29, 29, 4, INK) + _subs(32, 30, .95)

@reg("allegorithmic-Substance_Painter", RED_DEEP)
def substance_painter():
    dots = circle(20, 14.5, 2.8, INK) + circle(46.5, 45, 3.2, INK)
    return dots + circle(CX, CY, 14, INK) + _subs(32, 30, .9)

@reg("alligator", ORANGE_DEEP)
def alligator():
    jaws = stroke("M21 37L34 12.5", INK, 5) + stroke("M22 42L49 37", INK, 5)
    head = circle(21, 39, 7.5, INK)
    eye = circle(20.5, 36.5, 3.4, HOLE) + circle(20.2, 36.8, 1.6, INK)
    return jaws + head + eye

@reg("anatine", BLUE)
def anatine():
    body = path("M15 37C15 32 19.5 30.5 24 32C28.5 33.5 33.5 32 36.5 29C40.5 29.5 44.5 27.5 48.5 22.5"
                "C50.5 29 50 36 47 41C44 46 38 48.5 31 48.5C21.5 48.5 15 44.5 15 37Z", INK)
    head = circle(26.5, 21, 8.5, INK)
    beak = poly([(19, 18.5), (12.5, 21.5), (19, 24.5)], INK, 2.5)
    wing = stroke("M33.5 40C37.5 41 41.5 39.5 43.5 35.5", HOLE, 2.6)
    return body + head + beak + wing + circle(26, 19, 1.9, HOLE)

@reg("anjuta", PURPLE)
def anjuta():
    knight = path("M19.5 47.5H45C46 37 44.5 27.5 39.5 20.5C36.5 16.5 32.5 14 29 14L27.5 10.5"
                  "L24.5 15C20.5 17.5 17.5 21.5 15.5 26.5C14.5 29.5 17 32 20 30.5"
                  "L27.5 27C27.5 33.5 21.5 38 19.5 47.5Z", INK)
    return knight + circle(27.5, 20.5, 1.9, HOLE)

def _eye(iris):
    lid = path("M13.5 32C19.5 20 38 14 50.5 21C45.5 37.5 25 43 13.5 32Z", INK)
    return lid + circle(32.5, 28.5, 7.5, iris) + circle(32.5, 28.5, 3.4, INK)

@reg("amnesia-a-machine-for-pigs", BLUE_DEEP)
def amnesia_pigs():
    return _eye(HOLE)

@reg("amnesia-rebirth", RED_DEEP)
def amnesia_rebirth():
    return _eye(HOLE)

@reg("amnesia-the-dark-descent", BROWN_LIGHT)
def amnesia_tdd():
    return _eye(HOLE)

@reg("american-truck-simulator", RED_DEEP)
def ats():
    wheel = circle(CX, CY, 16.5, INK) + circle(CX, CY, 12.5, INDIGO_DEEP)
    spokes = "".join(line(*pt(CX, CY, 3, a), *pt(CX, CY, 11.5, a), INK, 2.4)
                     for a in range(0, 360, 45))
    return wheel + spokes + circle(CX, CY, 3.4, INK)

@reg("among-us", RED)
def among_us():
    pack = rrect(15.5, 22, 8, 17, 3.5, INK)
    body = path("M22.5 21C22.5 14.5 27 11 33 11C39.5 11 44 15 44 21.5V44.5"
                "C44 46.5 42.5 48 40.5 48H37.5C35.5 48 34.5 46.8 34.5 45V42H31.5V45"
                "C31.5 46.8 30.5 48 28.5 48H26C24 48 22.5 46.5 22.5 44.5Z", INK)
    visor = rrect(29.5, 17, 18.5, 10, 5, CYAN_SOFT, f' stroke="{HOLE}" stroke-width="1.6"')
    return pack + body + visor

@reg("ant-downloader", GREY_DARK)
def ant_downloader():
    half = (stroke("M21.5 20C18 17 18 13 20.5 10.5", INK, 2.6) +
            poly([(25.5, 13.5), (30.5, 19), (30.5, 34), (20, 29)], INK, 2) +
            stroke("M20 40L14.5 42.5L16 47.5", INK, 2.6))
    eyeband = path("M21 41C26 35.5 38 35.5 43 41C38 46.5 26 46.5 21 41Z", INK)
    return half + g(half, MIRROR) + eyeband + ell_b(32, 41, 2.2, 3.2, HOLE)

def _droid_head(cx, base, r, eye_r):
    dome = path(f"M{f(cx - r)} {f(base)}A{f(r)} {f(r)} 0 0 1 {f(cx + r)} {f(base)}Z", INK)
    ant = (line(*pt(cx, base, r * .78, -120), *pt(cx, base, r * 1.12, -120), INK, max(2.2, r * .16)) +
           line(*pt(cx, base, r * .78, -60), *pt(cx, base, r * 1.12, -60), INK, max(2.2, r * .16)))
    eyes = (circle(cx - r * .45, base - r * .38, eye_r, HOLE) +
            circle(cx + r * .45, base - r * .38, eye_r, HOLE))
    return dome + ant + eyes

@reg("anbox", TEAL)
def anbox():
    head = _droid_head(32, 22, 9.5, 1.4)
    body = path("M22.5 24H41.5V37A2.5 2.5 0 0 1 39 39.5H25A2.5 2.5 0 0 1 22.5 37Z", INK)
    arms = rrect(16.5, 24, 4.5, 13, 2.25, INK) + rrect(43, 24, 4.5, 13, 2.25, INK)
    legs = rrect(26, 36, 4.5, 11.5, 2.25, INK) + rrect(33.5, 36, 4.5, 11.5, 2.25, INK)
    return head + body + arms + legs

@reg("android-sdk", TEAL_DARK)
def android_sdk():
    return _droid_head(32, 39, 17, 2.2)

def _studio():
    head = _droid_head(32, 22, 9, 1.4)
    compass = (ring_b(32, 28, 3.4, INK, 2.6) +
               line(30.2, 31, 22, 47, INK, 3.6) + line(33.8, 31, 42, 47, INK, 3.6) +
               stroke("M23.5 39.5Q32 44 40.5 39.5", INK, 2.4))
    return head + compass

@reg("androidstudio", BLUE_DEEP)
def androidstudio():
    return _studio()

@reg("androidstudio-preview", AMBER_DEEP)
def androidstudio_preview():
    return _studio()

@reg("android-file-transfer", INDIGO)
def android_file_transfer():
    sheet = path("M25 12H39L47 20V45A3 3 0 0 1 44 48H25A3 3 0 0 1 22 45V15A3 3 0 0 1 25 12Z", INK)
    fold = path("M39 12V17A3 3 0 0 0 42 20H47Z", INDIGO_SOFT)
    rows = [(23, 17), (29, 12), (35, 17), (41, 9)]
    out = "".join(line(15, y, 19.5, y, INK, 3) for y, _ in rows[:3])
    out += sheet + fold
    out += "".join(line(24.5, y, 24.5 + w, y, HOLE, 3) for y, w in rows)
    return out

@reg("android-messages-desktop", BLUE_DEEP)
def android_messages():
    bubble = (rrect(15, 17, 34, 26, 8, INK) +
              poly([(15, 14.5), (26, 17.5), (17, 25)], INK, 2))
    lines = (rrect(21, 23, 22, 3, 1.5, HOLE) + rrect(21, 28.5, 22, 3, 1.5, HOLE) +
             rrect(21, 34, 15, 3, 1.5, HOLE))
    return bubble + lines

@reg("angular-console", BLUE_DEEP)
def angular_console():
    out = ""
    for y, x in [(17, 37), (27, 27), (37, 21)]:
        out += line(15, y, 47, y, INK, 2.6)
        out += circle(x, y, 3.8, INK) + circle(x, y, 1.6, HOLE)
    badge = circle(42.5, 40.5, 8.5, RED, f' stroke="{HOLE}" stroke-width="1.8"')
    a = stroke("M38.5 45L42.5 35.5L46.5 45M40 41.5H45", INK, 2.3)
    return out + badge + a

@reg("antidote", LIGHT_BLUE_DEEP)
def antidote():
    flask = path("M26 12H38V22L48 42.5C49.5 45.5 48 48 44.5 48H19.5C16 48 14.5 45.5 16 42.5L26 22Z", INK,
                 f' stroke="{INK}" stroke-width="2" stroke-linejoin="round"')
    liquid = path("M22 34H42L45.5 41.5C46.5 43.5 45.5 45 43.5 45H20.5C18.5 45 17.5 43.5 18.5 41.5Z", HOLE)
    drop = path("M32 31.5C34.5 35 36 37 36 39A4 4 0 0 1 28 39C28 37 29.5 35 32 31.5Z", INK)
    rim = rrect(23, 10.5, 18, 4, 2, INK)
    return flask + rim + liquid + drop

@reg("antigravity", BLUE)
def antigravity():
    return stroke("M16 46C22.5 42 23.5 14 32 14C40.5 14 41.5 42 48 46", INK, 6.5)

@reg("ao-app", INDIGO_LIGHT)
def ao_app():
    hexa = [pt(CX, CY, 17.5, -90 + 60 * k) for k in range(6)]
    lower = poly(hexa, INDIGO_DEEP, 3)
    upper = poly([hexa[0], hexa[1], (hexa[1][0], 26.5), (hexa[4][0], 37), hexa[4], hexa[5]], INK, 3)
    return lower + upper

@reg("aoi", BLUE)
def aoi():
    sq = rrect(31, 13, 18, 18, 3.5, INK)
    disc = circle(33, 37, 11, INK, f' stroke="{HOLE}" stroke-width="2.2"')
    tri = poly([(24, 12.5), (34, 31), (14, 31)], INK, 3)
    tri_edge = poly([(24, 12.5), (34, 31), (14, 31)], HOLE, 7.4)
    return sq + disc + tri_edge + tri

@reg("amsynth", ORANGE_DEEP)
def amsynth():
    return stroke("M17.5 46V14.5H30.5V45.5H46.5V33", INK, 5)

@small("apachedirectorystudio")
def apache_s():
    return (stroke("M32 47V29", INK, 4.5) + stroke("M32 34L20 22", INK, 3.6) +
            stroke("M32 34L44 22", INK, 3.6) + stroke("M32 30V14", INK, 3.6) +
            stroke("M24 48L32 44L40 48", INK, 3))

@small("angular-console")
def angular_console_s():
    out = ""
    for y, x in [(19, 36), (31, 24)]:
        out += line(15, y, 47, y, INK, 3) + circle(x, y, 4.5, INK)
    return out + circle(42, 41, 8.5, RED, f' stroke="{HOLE}" stroke-width="2"')

@small("android-file-transfer")
def aft_s():
    sheet = path("M25 12H39L47 20V45A3 3 0 0 1 44 48H25A3 3 0 0 1 22 45V15A3 3 0 0 1 25 12Z", INK)
    out = line(15, 25, 19, 25, INK, 4) + line(15, 35, 19, 35, INK, 4) + sheet
    return out + line(25, 25, 38, 25, HOLE, 4) + line(25, 35, 40, 35, HOLE, 4)

@small("alc")
def alc_s():
    ears = (g(ell_b(24, 20, 5, 10.5, INK), "rotate(-14 24 20)") +
            g(ell_b(40, 20, 5, 10.5, INK), "rotate(14 40 20)"))
    return ears + ell_b(32, 37.5, 13.5, 11, INK) + circle(27, 36, 2.2, HOLE) + circle(37, 36, 2.2, HOLE)

@small("allegorithmic-Substance_Alchemist")
def substance_alchemist_s():
    return poly([(32, 10.5), (51, 46), (13, 46)], INK, 5) + _subs(32, 35, .95, 4.4)

@small("allegorithmic-Substance_B2M")
def substance_b2m_s():
    return gear(CX, CY, 17.5, 14.5, 8, INK, .5, 2.5) + _subs(32, 30, 1, 4.4)

@small("allegorithmic-Substance_Designer")
def substance_designer_s():
    return rrect(15, 13, 34, 34, 5, INK) + _subs(32, 30, 1.1, 4.4)

@small("allegorithmic-Substance_Painter")
def substance_painter_s():
    return circle(CX, CY, 16.5, INK) + _subs(32, 30, 1.05, 4.4)

@small("almanah")
def almanah_s():
    book = rrect(16, 11, 32, 38, 4, INK) + rrect(20.5, 11, 3, 38, 0, HOLE)
    return book + stroke("M30 29V25A4.5 4.5 0 0 1 39 25V29", HOLE, 3.2) + rrect(26.5, 28, 16, 13, 2.5, HOLE)

@small("altmediawriter")
def altmediawriter_s():
    stick = rrect(18.5, 10.5, 27, 30, 5, INK) + rrect(24.5, 39, 15, 10, 2, INK)
    return stick + ell_b(31.5, 29, 6.5, 8.5, HOLE) + circle(32, 19.5, 5, HOLE)

@small("amazon-store")
def amazon_s():
    a = ring_b(29.5, 28.5, 6, INK, 4.2) + stroke("M24 18C26.5 14.5 36 14 36 21.5V35", INK, 4.2)
    return a + stroke("M16 41C24.5 47 37 47.5 46 41.5", ORANGE, 3.6)

@small("american-truck-simulator")
def ats_s():
    wheel = circle(CX, CY, 17, INK) + circle(CX, CY, 12, INDIGO_DEEP)
    spokes = "".join(line(*pt(CX, CY, 2, a), *pt(CX, CY, 11, a), INK, 3)
                     for a in range(0, 360, 60))
    return wheel + spokes

@small("anydesk")
def anydesk_s():
    left = g(rrect(16, 21, 18, 18, 3, INK), "rotate(45 25 30)")
    right = g(rrect(28, 20, 20, 20, 3, INK, f' stroke="{HOLE}" stroke-width="3.5"'), "rotate(45 38 30)")
    return left + right

@small("alien-isolation")
def alien_isolation_s():
    egg = path("M32 11C41 11 47.5 23.5 47.5 32.5C47.5 42.5 40.5 49 32 49"
               "C23.5 49 16.5 42.5 16.5 32.5C16.5 23.5 23 11 32 11Z", INK)
    return egg + stroke("M22 31L30.5 43L41 33", YELLOW_LIGHT, 4.6)

@small("alienblaster")
def alienblaster_s():
    wings = path("M24 25H40L50 42C50 44.5 48 45.5 45 45.5H19C16 45.5 14 44.5 14 42Z", INK)
    ship = path("M26.5 44V22C26.5 16 29.5 12 32 10.5C34.5 12 37.5 16 37.5 22V44Z", INK,
                f' stroke="{HOLE}" stroke-width="2.6" stroke-linejoin="round"')
    return wings + ship

@small("ant-downloader")
def ant_downloader_s():
    half = (stroke("M21 21C17.5 18 17.5 14 20 11", INK, 3) +
            poly([(25, 13), (30.5, 19), (30.5, 34), (19, 29)], INK, 2))
    eyeband = path("M19 41C25 34.5 39 34.5 45 41C39 47.5 25 47.5 19 41Z", INK)
    return half + g(half, MIRROR) + eyeband + ell_b(32, 41, 2.8, 4, HOLE)

@small("another-redis-desktop-manager")
def redis_dm_s():
    return poly(star_c(30, 32, 16, 7.5, -104), INK, 3) + circle(46, 15, 3.8, INK)

def _eye_s():
    lid = path("M12.5 32C19 19 38.5 12.5 51.5 20C46.5 38.5 24.5 44.5 12.5 32Z", INK)
    return lid + circle(32.5, 28.5, 9, HOLE) + circle(32.5, 28.5, 4.2, INK)

for _n in ("amnesia-a-machine-for-pigs", "amnesia-rebirth", "amnesia-the-dark-descent"):
    SMALL[_n] = _eye_s
