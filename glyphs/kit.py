# SPDX-License-Identifier: GPL-3.0-or-later
"""Shared registry and drawing helpers for the glyph batches.

Drawing rules, the same in every batch: each tile takes the palette step nearest the
app's own brand colour; the mark is drawn in INK (white, or near-black on pale tiles);
HOLE is the tile colour showing through the mark; any other shade is another step
from the same palette.
"""
import math
from lm import (
    BLUE_SOFT, circle, cpath, cut, CX, CY, f, g, HOLE, INK, line, path, poly, pt, rrect, stroke,
    YELLOW_DARK,
)


def registry():
    ICONS, SMALL = {}, {}

    def reg(name, tile):
        def deco(fn):
            ICONS[name] = (fn, tile)
            return fn
        return deco

    def small(name):
        def deco(fn):
            SMALL[name] = fn
            return fn
        return deco

    return ICONS, SMALL, reg, small


def arc_b(cx, cy, r, a0, a1, colour, w):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return stroke(f"M{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 {large} 1 {f(x1)} {f(y1)}", colour, w)


def arc(cx, cy, r, a0, a1):
    """Arc path fragment, clockwise on screen from angle a0 to a1."""
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 {large} 1 {f(x1)} {f(y1)}"


def arrowhead(x, y, dx, dy, s=6, c=INK):
    px, py = -dy, dx
    return poly([(x + dx * s, y + dy * s), (x + px * s * .9, y + py * s * .9), (x - px * s * .9, y - py * s * .9)], c, 1.4)


def ink_stroke(d, w=4, c=INK):
    return stroke(d, c, w)


def arc_arrow(cx, cy, r, a0, a1, w=4.4, s=6, c=INK):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    big = 1 if (a1 - a0) % 360 > 180 else 0
    t = math.radians(a1)
    return ink_stroke(f"M{f(x0)} {f(y0)}A{r} {r} 0 {big} 1 {f(x1)} {f(y1)}", w, c) + arrowhead(x1, y1, -math.sin(t), math.cos(t), s, c)


def arc_arrow_b(cx, cy, r, a0, a1, colour, w, head):
    """Clockwise arc from a0 to a1 (degrees) ending in a triangular head."""
    s, e = pt(cx, cy, r, a0), pt(cx, cy, r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    arc = stroke(f"M{f(s[0])} {f(s[1])}A{f(r)} {f(r)} 0 {large} 1 {f(e[0])} {f(e[1])}", colour, w)
    t = math.radians(a1 + 90)
    dx, dy = math.cos(t), math.sin(t)
    nx, ny = pt(0, 0, 1, a1)
    tip = (e[0] + dx * head, e[1] + dy * head)
    b1 = (e[0] + nx * head, e[1] + ny * head)
    b2 = (e[0] - nx * head, e[1] - ny * head)
    return arc + poly([tip, b1, b2], colour, 1.5)


def arc_c(cx, cy, r, a0, a1, colour, w):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    big = 1 if (a1 - a0) % 360 > 180 else 0
    return stroke(f"M{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 {big} 1 {f(x1)} {f(y1)}", colour, w)


def _arc_c(cx, cy, r, a0, a1):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 1 if a1 > a0 else 0
    return f"M{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 {large} {sweep} {f(x1)} {f(y1)}"


def arc_d(cx, cy, r, a0, a1, colour, w, extra=""):
    p0, p1 = pt(cx, cy, r, a0), pt(cx, cy, r, a1)
    big = 1 if (a1 - a0) % 360 > 180 else 0
    return stroke(f"M{f(p0[0])} {f(p0[1])}A{f(r)} {f(r)} 0 {big} 1 {f(p1[0])} {f(p1[1])}",
                  colour, w, extra)


def arc_e(cx, cy, r, a0, a1):
    """Clockwise arc path from angle a0 to a1 (degrees)."""
    p0, p1 = pt(cx, cy, r, a0), pt(cx, cy, r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M{f(p0[0])} {f(p0[1])}A{f(r)} {f(r)} 0 {large} 1 {f(p1[0])} {f(p1[1])}"


def arc_f(cx, cy, r, a0, a1):
    p0, p1 = pt(cx, cy, r, a0), pt(cx, cy, r, a1)
    big = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M{f(p0[0])} {f(p0[1])}A{f(r)} {f(r)} 0 {big} 1 {f(p1[0])} {f(p1[1])}"


def arc_g(cx, cy, r, a0, a1):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    big = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 {big} 1 {f(x1)} {f(y1)}"


def arc_h(cx, cy, r, a0, a1, sweep=1):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 {large} {sweep} {f(x1)} {f(y1)}"


def arrowhead_b(x, y, deg, size, fill):
    tip = pt(x, y, size, deg)
    l = pt(x, y, size * .75, deg + 120)
    r = pt(x, y, size * .75, deg - 120)
    return poly([tip, l, r], fill, 1.5)


def arrowhead_c(x, y, deg, colour, s=5):
    """Filled triangle pointing along deg with its tip at (x, y)."""
    tip = (x, y)
    b1 = pt(x, y, s * 1.4, deg + 180 - 35)
    b2 = pt(x, y, s * 1.4, deg + 180 + 35)
    return poly([tip, b1, b2], colour, 1.6)


def arrowhead_d(cx, cy, r, a, colour, size=3.6):
    """Small triangle at angle a on a circle, pointing clockwise."""
    tip = pt(cx, cy, r, a + 9)
    b1 = pt(cx, cy, r + size, a - 4)
    b2 = pt(cx, cy, r - size, a - 4)
    return poly([tip, b1, b2], colour, 1.6)


def arrowhead_e(x, y, deg, colour, s=5):
    """Filled triangle pointing along deg with its tip at (x, y)."""
    b1 = pt(x, y, s * 1.4, deg + 180 - 35)
    b2 = pt(x, y, s * 1.4, deg + 180 + 35)
    return poly([(x, y), b1, b2], colour, 1.6)


def asterisk(cx, cy, r, w=3.4, c=INK):
    return "".join(ink_stroke(f"M{f(pt(cx, cy, r, a)[0])} {f(pt(cx, cy, r, a)[1])}L{f(pt(cx, cy, r, a + 180)[0])} {f(pt(cx, cy, r, a + 180)[1])}", w, c) for a in (90, 150, 210))


def badge(cx, cy, colour, r=9):
    return circle(cx, cy, r + 2, HOLE) + circle(cx, cy, r, colour)


def badge_b(cx, cy, colour):
    return circle(cx, cy, 10.5, HOLE) + circle(cx, cy, 9, colour)


def badge_c(cx, cy, r):
    """A round badge punched out of whatever sits under it."""
    return circle(cx, cy, r + 2, HOLE) + circle(cx, cy, r, INK)


def badge_d(cx, cy, colour):
    return circle(cx, cy, 9, HOLE) + circle(cx, cy, 7.5, colour)


def badge_e(cx, cy, colour, r=9):
    return circle(cx, cy, r + 1.8, HOLE) + circle(cx, cy, r, colour)


def badge_f(sym, fill, cx=42, cy=40, r=9):
    return circle(cx, cy, r + 2.2, HOLE) + circle(cx, cy, r, fill) + sym


def bars(xs, base, w, heights, c=INK):
    return "".join(rrect(x, base - h, w, h, w / 2.5, c) for x, h in zip(xs, heights))


def ink_rrect(x, y, w, h, r, fill=INK, extra=""):
    return rrect(x, y, w, h, r, fill, extra)


def bubble(x, y, w, h, c=INK):
    return ink_rrect(x, y, w, h, 8, c) + poly([(x + 10, y + h - 2), (x + 10, y + h + 9), (x + 22, y + h - 2)], c, 1.5)


def bubble_b(cx=32, cy=28, w=32, h=22, tail=True):
    out = rrect(cx - w / 2, cy - h / 2, w, h, 8, INK)
    if tail:
        out += poly([(cx - 9, cy + h / 2 - 2), (cx - 12, cy + h / 2 + 8), (cx + 2, cy + h / 2 - 2)], INK, 2)
    return out


def cells(pts, size=12, pitch=14, ox=4, oy=6, c=INK):
    return "".join(ink_rrect(ox + x * pitch, oy + y * pitch, size, size, 2.5, c) for x, y in pts)


def _chrome():
    """Three segments whose edges run tangent to the centre ring."""
    out = ""
    for k in range(3):
        a0 = -90 + 120 * k
        a1 = a0 + 120
        t0 = pt(CX, CY, 8, a0 + 90)
        o0 = (t0[0] + 13.86 * math.cos(math.radians(a0)),
              t0[1] + 13.86 * math.sin(math.radians(a0)))
        t1 = pt(CX, CY, 8, a1 + 90)
        o1 = (t1[0] + 13.86 * math.cos(math.radians(a1)),
              t1[1] + 13.86 * math.sin(math.radians(a1)))
        d = (f"M{f(t0[0])} {f(t0[1])}L{f(o0[0])} {f(o0[1])}"
             f"A16 16 0 0 1 {f(o1[0])} {f(o1[1])}L{f(t1[0])} {f(t1[1])}Z")
        out += path(d, INK, f' stroke="{HOLE}" stroke-width="1.8" stroke-linejoin="round"')
    return out + circle(CX, CY, 8.4, HOLE) + circle(CX, CY, 6, INK)


def _chrome_b(cx, cy, R, seg, gap, sw):
    """Wheel of radius R: three segments round a centre dot."""
    out = ""
    ri, lo = R * .5, R * .866
    for k in range(3):
        a0 = -90 + 120 * k
        a1 = a0 + 120
        t0 = pt(cx, cy, ri, a0 + 90)
        o0 = (t0[0] + lo * math.cos(math.radians(a0)), t0[1] + lo * math.sin(math.radians(a0)))
        t1 = pt(cx, cy, ri, a1 + 90)
        o1 = (t1[0] + lo * math.cos(math.radians(a1)), t1[1] + lo * math.sin(math.radians(a1)))
        d = (f"M{f(t0[0])} {f(t0[1])}L{f(o0[0])} {f(o0[1])}"
             f"A{f(R)} {f(R)} 0 0 1 {f(o1[0])} {f(o1[1])}L{f(t1[0])} {f(t1[1])}Z")
        out += path(d, seg, f' stroke="{gap}" stroke-width="{f(sw)}" stroke-linejoin="round"')
    return out + circle(cx, cy, ri + sw * .6, gap) + circle(cx, cy, ri * .75, seg)


def crescent(cx, cy, r, c=INK):
    return path(f"M{f(cx)} {f(cy - r)}A{f(r)} {f(r)} 0 1 0 {f(cx)} {f(cy + r)}A{f(r * 1.4)} {f(r * 1.4)} 0 0 1 {f(cx)} {f(cy - r)}Z", c)


def ink_path(d, fill=INK, extra=""):
    return path(d, fill, extra)


def crescent_b(cx, cy, r, c=INK):
    return ink_path(f"M{f(cx)} {f(cy - r)}A{f(r)} {f(r)} 0 1 0 {f(cx)} {f(cy + r)}A{f(r * 1.4)} {f(r * 1.4)} 0 0 1 {f(cx)} {f(cy - r)}Z", c)


def crescent_c(c1, r1, c2, r2, fill):
    """Disc (c1, r1) with disc (c2, r2) bitten out of it, as one path."""
    (x1, y1), (x2, y2) = c1, c2
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy)
    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h = math.sqrt(max(r1 * r1 - a * a, 0))
    mx, my = x1 + a * dx / d, y1 + a * dy / d
    p1 = (mx + h * dy / d, my - h * dx / d)
    p2 = (mx - h * dy / d, my + h * dx / d)
    return path(f"M{f(p1[0])} {f(p1[1])}A{f(r1)} {f(r1)} 0 1 0 {f(p2[0])} {f(p2[1])}"
                f"A{f(r2)} {f(r2)} 0 0 1 {f(p1[0])} {f(p1[1])}Z", fill)


def crescent_d(cx, cy, r, ox, oy, r2):
    """Disc (cx,cy,r) minus disc (ox,oy,r2), as one path."""
    dx, dy = ox - cx, oy - cy
    d = math.hypot(dx, dy)
    a = (r * r - r2 * r2 + d * d) / (2 * d)
    h = math.sqrt(r * r - a * a)
    mx, my = cx + a * dx / d, cy + a * dy / d
    p1 = (mx + h * dy / d, my - h * dx / d)
    p2 = (mx - h * dy / d, my + h * dx / d)
    return (f"M{f(p1[0])} {f(p1[1])}A{f(r)} {f(r)} 0 1 0 {f(p2[0])} {f(p2[1])}"
            f"A{f(r2)} {f(r2)} 0 0 1 {f(p1[0])} {f(p1[1])}Z")


def crescent_e(c1, r1, c2, r2, fill):
    """The part of circle 1 not covered by circle 2."""
    (x1, y1), (x2, y2) = c1, c2
    d = math.hypot(x2 - x1, y2 - y1)
    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h = math.sqrt(r1 * r1 - a * a)
    mx, my = x1 + a * (x2 - x1) / d, y1 + a * (y2 - y1) / d
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    p = (mx + h * uy, my - h * ux)
    q = (mx - h * uy, my + h * ux)
    dd = (f"M{f(p[0])} {f(p[1])}A{f(r1)} {f(r1)} 0 1 0 {f(q[0])} {f(q[1])}"
          f"A{f(r2)} {f(r2)} 0 0 1 {f(p[0])} {f(p[1])}Z")
    return path(dd, fill)


def dim(content, o):
    return f'<g opacity="{o}">{content}</g>'


def _doc(body, fold_colour):
    sheet = path("M20 11H37L46 20V46A3 3 0 0 1 43 49H20A3 3 0 0 1 17 46V14A3 3 0 0 1 20 11Z", INK)
    fold = path("M37 11V17A3 3 0 0 0 40 20H46Z", fold_colour)
    return sheet + fold + body


def ell(cx, cy, rx, ry, c=INK):
    return f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{c}"/>'


def ell_b(cx, cy, rx, ry, fill, extra=""):
    return f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{fill}"{extra}/>'


def ell_c(cx, cy, rx, ry, fill):
    return path(f"M{f(cx - rx)} {f(cy)}a{f(rx)} {f(ry)} 0 1 0 {f(2 * rx)} 0"
                f"a{f(rx)} {f(ry)} 0 1 0 {f(-2 * rx)} 0Z", fill)


def ell_d(cx, cy, rx, ry, fill, rot=0):
    e = (f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{fill}"/>')
    return g(e, f"rotate({rot} {f(cx)} {f(cy)})") if rot else e


def ell_e(cx, cy, rx, ry, fill, extra=""):
    return path(f"M{f(cx - rx)} {f(cy)}a{f(rx)} {f(ry)} 0 1 0 {f(2 * rx)} 0"
                f"a{f(rx)} {f(ry)} 0 1 0 {f(-2 * rx)} 0Z", fill, extra)


def ell_f(cx, cy, rx, ry, fill, rot=0, extra=""):
    return (f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{fill}" '
            f'transform="rotate({f(rot)} {f(cx)} {f(cy)})"{extra}/>')


def ell_g(cx, cy, rx, ry):
    return (f"M{f(cx - rx)} {f(cy)}a{f(rx)} {f(ry)} 0 1 0 {f(2 * rx)} 0"
            f"a{f(rx)} {f(ry)} 0 1 0 {f(-2 * rx)} 0Z")


def ellipse(cx, cy, rx, ry, fill, rot=0):
    return (f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{fill}" '
            f'transform="rotate({f(rot)} {f(cx)} {f(cy)})"/>')


def ellipse_b(cx, cy, rx, ry, colour, w, rot=0):
    return (f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="none" '
            f'stroke="{colour}" stroke-width="{f(w)}" transform="rotate({rot} {f(cx)} {f(cy)})"/>')


def ellipse_c(cx, cy, rx, ry, colour, w=None):
    if w is None:
        return f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{colour}"/>'
    return (f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="none" '
            f'stroke="{colour}" stroke-width="{f(w)}"/>')


def ellipse_d(cx, cy, rx, ry, colour):
    return f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{colour}"/>'


def ellipse_f(cx, cy, rx, ry, colour, extra=""):
    return (f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" '
            f'fill="{colour}"{extra}/>')


def ellipse_g(cx, cy, rx, ry, fill, rot=0):
    return (f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{fill}" '
            f'transform="rotate({rot} {f(cx)} {f(cy)})"/>')


def ellipse_i(cx, cy, rx, ry, fill):
    return (f"M{f(cx - rx)} {f(cy)}a{f(rx)} {f(ry)} 0 1 0 {f(2 * rx)} 0"
            f"a{f(rx)} {f(ry)} 0 1 0 {f(-2 * rx)} 0Z"), fill


def ellring(cx, cy, rx, ry, w=4, c=INK, extra=""):
    return f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="none" stroke="{c}" stroke-width="{w}"{extra}/>'


def ering(cx, cy, rx, ry, colour, w, rot=0):
    return (f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="none" '
            f'stroke="{colour}" stroke-width="{f(w)}" transform="rotate({f(rot)} {f(cx)} {f(cy)})"/>')


def ering_b(cx, cy, rx, ry, colour, w):
    return ell_b(cx, cy, rx, ry, "none", f' stroke="{colour}" stroke-width="{f(w)}"')


def ering_c(cx, cy, rx, ry, colour, w):
    return (f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="none" '
            f'stroke="{colour}" stroke-width="{f(w)}"/>')


def fit(content, k, cx=32, cy=30):
    """Centre the mark on the tile and size it so it keeps a clear margin inside the round tile."""
    return g(content, f"translate(32 30) scale({k}) translate({f(-cx)} {f(-cy)})")


def fit_b(content, k):
    """Shrink a mark about the tile's centre so it keeps a clear margin inside the round tile."""
    return g(content, f"translate(32 30) scale({k}) translate(-32 -30)")


def _gear(cx, cy, r_out, r_in, teeth, fill, tooth_w=0.5):
    """Chunky gear outline as a filled polygon (no hole)."""
    pts = []
    step = 360 / teeth
    for k in range(teeth):
        a = -90 + step * k
        h = step * tooth_w / 2
        pts += [pt(cx, cy, r_in, a - step / 2 + 2), pt(cx, cy, r_out, a - h),
                pt(cx, cy, r_out, a + h), pt(cx, cy, r_in, a + step / 2 - 2)]
    return poly(pts, fill, 2)


def gear(cx, cy, ro, ri, n, fill, tw=.55, rounding=2):
    pts = []
    step = 360 / n
    for k in range(n):
        a = step * k - 90
        h = step * tw / 2
        pts += [pt(cx, cy, ri, a - h), pt(cx, cy, ro, a - h * .62),
                pt(cx, cy, ro, a + h * .62), pt(cx, cy, ri, a + h)]
    return poly(pts, fill, rounding)


def _gear_b(cx, cy, r, fill, hole):
    teeth = "".join(g(rrect(cx - 1.7, cy - r - 2, 3.4, 4, 1, fill), f"rotate({45 * k} {f(cx)} {f(cy)})")
                    for k in range(8))
    return teeth + circle(cx, cy, r, fill) + circle(cx, cy, r * .42, hole)


def gear_d(cx, cy, R, r, n=8, tooth=.42):
    """Gear outline as a path: n flat-topped teeth between radius r and R."""
    pts = []
    step = 360 / n
    for k in range(n):
        a = -90 + step * k
        w = step * tooth / 2
        pts += [pt(cx, cy, r, a - w * 1.45), pt(cx, cy, R, a - w),
                pt(cx, cy, R, a + w), pt(cx, cy, r, a + w * 1.45)]
    return "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z"


def gear_b(cx, cy, R, r, colour, n=8):
    return path(gear_d(cx, cy, R, r, n), colour,
                f' stroke="{colour}" stroke-width="2" stroke-linejoin="round"')


def _gear_c(cx, cy, r, colour, hole):
    teeth = "".join(g(rrect(cx - 1.6, cy - r - 1.8, 3.2, 4, 0.8, colour), f"rotate({45 * k} {f(cx)} {f(cy)})")
                    for k in range(8))
    return teeth + circle(cx, cy, r, colour) + circle(cx, cy, r * 0.42, hole)


def gear_c(cx, cy, r, fill, hole, n=8, hr=None):
    teeth = "".join(g(rrect(cx - r * .2, cy - r - r * .3, r * .4, r * .6, r * .1, fill),
                      f"rotate({360 / n * k} {f(cx)} {f(cy)})") for k in range(n))
    return teeth + circle(cx, cy, r, fill) + circle(cx, cy, hr or r * .42, hole)


def _gear_d(cx, cy, r, n, tw, th, fill, hole, hr):
    teeth = "".join(g(rrect(cx - tw / 2, cy - r - th, tw, th + 3, 1.2, fill),
                      f"rotate({f(360 / n * k)} {f(cx)} {f(cy)})") for k in range(n))
    return teeth + circle(cx, cy, r, fill) + circle(cx, cy, hr, hole)


def _gear_e(cx, cy, r, colour, hole):
    teeth = "".join(g(rrect(cx - 1.8, cy - r - 2, 3.6, 4, 1, colour), f"rotate({45 * k} {f(cx)} {f(cy)})")
                    for k in range(8))
    return teeth + circle(cx, cy, r, colour) + circle(cx, cy, r * .4, hole)


def gear_e(cx, cy, r, n, tw, th, colour, rot=0):
    """Round body with n rounded teeth sticking out by th."""
    teeth = "".join(g(rrect(cx - tw / 2, cy - r - th, tw, th + 3, 1.2, colour),
                      f"rotate({f(rot + 360 / n * k)} {f(cx)} {f(cy)})") for k in range(n))
    return teeth + circle(cx, cy, r, colour)


def _gear_f(cx, cy, r, fill, teeth=8):
    pts = []
    step = 360 / teeth
    for k in range(teeth):
        a = k * step
        pts += [pt(cx, cy, r, a - step * .2), pt(cx, cy, r, a + step * .2),
                pt(cx, cy, r * .74, a + step * .32), pt(cx, cy, r * .74, a + step * .68)]
    return poly(pts, fill, 1.2)


def gear_f(cx, cy, ro, ri, n, colour, rounding=1.5):
    step = 360 / n
    pts = []
    for k in range(n):
        a = step * k - 90
        pts += [pt(cx, cy, ri, a - .32 * step), pt(cx, cy, ro, a - .17 * step),
                pt(cx, cy, ro, a + .17 * step), pt(cx, cy, ri, a + .32 * step)]
    return poly(pts, colour, rounding)


def _gear_g(cx, cy, ro, ri, n, col):
    pts, w = [], 360 / n
    for k in range(n):
        a = w * k
        pts += [pt(cx, cy, ri, a - w * .32), pt(cx, cy, ro, a - w * .17),
                pt(cx, cy, ro, a + w * .17), pt(cx, cy, ri, a + w * .32)]
    return poly(pts, col, 1)


def gear_g(cx, cy, r, colour, hole, teeth=8):
    t = "".join(g(rrect(cx - 1.9, cy - r - 2.2, 3.8, 4.5, 1, colour), f"rotate({360 / teeth * k} {f(cx)} {f(cy)})")
                for k in range(teeth))
    return t + circle(cx, cy, r, colour) + circle(cx, cy, r * .42, hole)


def _gear_h(cx, cy, r, teeth, fill):
    out = ""
    for k in range(teeth):
        out += g(rrect(cx - 2.2, cy - r - 2.6, 4.4, 5, 1.2, fill), f"rotate({360 / teeth * k} {cx} {cy})")
    return out + cut(cpath(cx, cy, r) + cpath(cx, cy, r * .45), fill)


def gear_h(cx, cy, r, fill, hole, n=8, hr=None):
    teeth = "".join(g(rrect(cx - r * .22, cy - r - r * .28, r * .44, r * .6, r * .1, fill),
                      f"rotate({f(360 / n * k)} {f(cx)} {f(cy)})") for k in range(n))
    return teeth + circle(cx, cy, r, fill) + circle(cx, cy, hr or r * .42, hole)


def rot_b(content, deg, cx=32, cy=30):
    return g(content, f"rotate({f(deg)} {f(cx)} {f(cy)})")


def _gear_i(cx, cy, r, colour, hole):
    teeth = "".join(rot_b(rrect(cx - 2.2, cy - r - 2.6, 4.4, 5.5, 1.2, colour), 45 * k, cx, cy)
                    for k in range(8))
    return teeth + circle(cx, cy, r, colour) + circle(cx, cy, r * .42, hole)


def gear_i(cx, cy, r, fill, hole, n=8, hr=None):
    teeth = "".join(g(rrect(cx - r * .22, cy - r - r * .28, r * .44, r * .6, r * .1, fill),
                      f"rotate({f(360 / n * k)} {f(cx)} {f(cy)})") for k in range(n))
    return teeth + circle(cx, cy, r, fill) + (circle(cx, cy, hr or r * .42, hole) if hole else "")


def _gear_j(cx, cy, ro, ri, n, fill):
    step = 360 / n
    pts = []
    for i in range(n):
        a = -90 + step * i
        pts += [pt(cx, cy, ri, a - step * .3), pt(cx, cy, ro, a - step * .17),
                pt(cx, cy, ro, a + step * .17), pt(cx, cy, ri, a + step * .3)]
    return poly(pts, fill, 2.5)


def gear_j(cx, cy, r, fill, n=8):
    teeth = "".join(g(rrect(cx - r * .22, cy - r - r * .3, r * .44, r * .6, r * .1, fill),
                      f"rotate({f(360 / n * k)} {f(cx)} {f(cy)})") for k in range(n))
    return teeth + circle(cx, cy, r, fill)


def _gear_k(cx, cy, r, teeth, fill, tw=5, th=5.5):
    out = ""
    for k in range(teeth):
        out += g(rrect(cx - tw / 2, cy - r - th + 1.5, tw, th, 1.4, fill),
                 f"rotate({f(360 / teeth * k)} {f(cx)} {f(cy)})")
    return out + circle(cx, cy, r, fill)


def gear_k(cx, cy, r, fill, hole, n=8, hr=None):
    teeth = "".join(g(rrect(cx - r * .2, cy - r - r * .26, r * .4, r * .56, r * .08, fill),
                      f"rotate({f(360 / n * k)} {f(cx)} {f(cy)})") for k in range(n))
    return teeth + circle(cx, cy, r, fill) + (circle(cx, cy, hr or r * .42, hole) if hole else "")


def _gear_l(cx, cy, r_out, r_in, teeth, col):
    pts = []
    for k in range(teeth * 4):
        a = 360 / (teeth * 4) * k + 360 / teeth / 8
        r = r_out if k % 4 in (0, 1) else r_in
        pts.append(pt(cx, cy, r, a - 90))
    return poly(pts, col, 2.5)


def gear_l(cx, cy, r, teeth, tw, th, fill, rot=0):
    out = circle(cx, cy, r, fill)
    for k in range(teeth):
        a = rot + 360 / teeth * k
        out += g(rrect(cx - tw / 2, cy - r - th, tw, th + 2, 1.2, fill), f"rotate({f(a)} {f(cx)} {f(cy)})")
    return out


def _gear_m(cx, cy, ro, ri, n, fill):
    pts = []
    for k in range(n):
        a = 360 / n * k
        for da, r in [(-.24, ri), (-.13, ro), (.13, ro), (.24, ri)]:
            pts.append(pt(cx, cy, r, a + da * 360 / n))
    return poly(pts, fill, 1)


def gear_m(cx, cy, r, colour, hole, teeth=8, hr=None):
    pts = []
    for k in range(teeth * 4):
        a = 360 / (teeth * 4) * k - 90
        rr = r if (k % 4) in (0, 1) else r * 0.78
        pts.append(pt(cx, cy, rr, a))
    out = poly(pts, colour, 1.5)
    return out + circle(cx, cy, hr if hr else r * 0.36, hole)


def gear_n(cx, cy, r, tooth, fill, n=8):
    out = circle(cx, cy, r, fill)
    for k in range(n):
        out += g(rrect(cx - tooth / 2, cy - r - tooth * .8, tooth, tooth * 1.4, tooth * .3, fill),
                 f"rotate({360 / n * k} {f(cx)} {f(cy)})")
    return out


def ink_circle(cx, cy, r, fill=INK, extra=""):
    return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}"{extra}/>'


def rot(content, a, cx=32, cy=30):
    return g(content, f"rotate({a} {cx} {cy})")


def gear_o(cx, cy, r, n=8, c=INK, hole=True):
    out = ink_circle(cx, cy, r)
    for k in range(n):
        out += rot(ink_rrect(cx - 3.4, cy - r - 4.5, 6.8, 8, 1.5, c), 360 / n * k, cx, cy)
    return out + (ink_circle(cx, cy, r * .42, HOLE) if hole else "")


def hashmark(cx, cy, s, w=4.5, c=INK):
    return (ink_stroke(f"M{f(cx - s * .25)} {f(cy - s)}L{f(cx - s * .5)} {f(cy + s)}", w, c)
            + ink_stroke(f"M{f(cx + s * .5)} {f(cy - s)}L{f(cx + s * .25)} {f(cy + s)}", w, c)
            + ink_stroke(f"M{f(cx - s)} {f(cy - s * .38)}H{f(cx + s)}", w, c)
            + ink_stroke(f"M{f(cx - s)} {f(cy + s * .38)}H{f(cx + s)}", w, c))


def _hex(cx, cy, r, rot=-90):
    return [pt(cx, cy, r, rot + 60 * k) for k in range(6)]


def hexring(x, y, r, w=3.4, c=INK):
    d = "M" + "L".join(f"{f(a)} {f(b)}" for a, b in [pt(x, y, r, -90 + 60 * k) for k in range(6)]) + "Z"
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linejoin="round"/>'


def hs(w=2.6):
    return f' stroke="{HOLE}" stroke-width="{w}" stroke-linejoin="round"'


def hx(x, y, r, a=-90, c=INK, rd=3):
    return poly([pt(x, y, r, a + 60 * k) for k in range(6)], c, rd)


def _jb(letters):
    """Square with two letters and an underscore."""
    return rrect(15, 13, 34, 34, 3, INK) + letters + rrect(20.5, 38.5, 12, 3.2, 1.6, HOLE)


def lem(cx, cy, a, w=6.2, c=INK):
    pts = []
    for k in range(73):
        t = math.radians(5 * k)
        d = 1 + math.sin(t) ** 2
        pts.append((cx + a * math.cos(t) / d, cy + a * 1.5 * math.sin(t) * math.cos(t) / d))
    return ink_stroke("M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z", w, c)


def mirror(content):
    return g(content, "translate(64 0) scale(-1 1)")


def pet(cx, cy, r, w, a, sw=2.6):
    d = f"M{f(cx)} {f(cy)}Q{f(cx + r * .5)} {f(cy - w)} {f(cx + r)} {f(cy)}Q{f(cx + r * .5)} {f(cy + w)} {f(cx)} {f(cy)}Z"
    return rot(path(d, INK, hs(sw)), a, cx, cy)


def petal(cx, cy, r, w, a, c=INK):
    """A pointed petal from the centre outwards at angle a."""
    return rot(path(f"M{f(cx)} {f(cy)}Q{f(cx + r * .5)} {f(cy - w)} {f(cx + r)} {f(cy)}Q{f(cx + r * .5)} {f(cy + w)} {f(cx)} {f(cy)}Z", c), a, cx, cy)


def petal_b(cx, cy, r, w, a, c=INK):
    """A pointed petal from the centre outwards at angle a."""
    return rot(ink_path(f"M{f(cx)} {f(cy)}Q{f(cx + r * .5)} {f(cy - w)} {f(cx + r)} {f(cy)}Q{f(cx + r * .5)} {f(cy + w)} {f(cx)} {f(cy)}Z", c), a, cx, cy)


def pie(cx, cy, r, a0, a1, c=INK):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    big = 1 if (a1 - a0) % 360 > 180 else 0
    return path(f"M{f(cx)} {f(cy)}L{f(x0)} {f(y0)}A{r} {r} 0 {big} 1 {f(x1)} {f(y1)}Z", c)


def pie_b(cx, cy, r, a0, a1, colour, extra=""):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return path(f"M{f(cx)} {f(cy)}L{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 {large} 1 {f(x1)} {f(y1)}Z",
                colour, extra)


def pie_c(cx, cy, r, a0, a1, colour):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    big = 1 if (a1 - a0) % 360 > 180 else 0
    return path(f"M{f(cx)} {f(cy)}L{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 {big} 1 {f(x1)} {f(y1)}Z", colour)


def _ring(cx, cy, r, colour, w):
    return (f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="none" '
            f'stroke="{colour}" stroke-width="{f(w)}"/>')


def ring_b(cx, cy, r, colour, w, extra=""):
    return (f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="none" '
            f'stroke="{colour}" stroke-width="{f(w)}"{extra}/>')


def ring_c(cx, cy, r, w=4, c=INK):
    return ink_circle(cx, cy, r, "none", f' stroke="{c}" stroke-width="{w}"')


def ring_d(cx, cy, r, w=4, c=INK):
    return circle(cx, cy, r, "none", f' stroke="{c}" stroke-width="{w}"')


def ring_e(cx, cy, r, colour, w):
    return circle(cx, cy, r, "none", f' stroke="{colour}" stroke-width="{f(w)}"')


def SB(d, w=3, c=INK, extra=""):
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="butt"{extra}/>'


def sector(cx, cy, r0, r1, a0, a1):
    p0, p1 = pt(cx, cy, r1, a0), pt(cx, cy, r1, a1)
    q1, q0 = pt(cx, cy, r0, a1), pt(cx, cy, r0, a0)
    return (f"M{f(p0[0])} {f(p0[1])}A{f(r1)} {f(r1)} 0 0 1 {f(p1[0])} {f(p1[1])}"
            f"L{f(q1[0])} {f(q1[1])}A{f(r0)} {f(r0)} 0 0 0 {f(q0[0])} {f(q0[1])}Z")


def sector_b(cx, cy, r1, r2, a0, a1):
    """Annulus sector from angle a0 to a1 (degrees, clockwise)."""
    p0, p1 = pt(cx, cy, r2, a0), pt(cx, cy, r2, a1)
    q1, q0 = pt(cx, cy, r1, a1), pt(cx, cy, r1, a0)
    big = 1 if (a1 - a0) % 360 > 180 else 0
    return (f"M{f(p0[0])} {f(p0[1])}A{f(r2)} {f(r2)} 0 {big} 1 {f(p1[0])} {f(p1[1])}"
            f"L{f(q1[0])} {f(q1[1])}A{f(r1)} {f(r1)} 0 {big} 0 {f(q0[0])} {f(q0[1])}Z")


def shrink(content, k=.8, ox=29, oy=27):
    return g(content, f"translate({ox} {oy}) scale({k}) translate(-32 -30)")


def _slabs(top, bot):
    t = path("M16 14H48V25H37L35 28H16Z", top,
             f' stroke="{top}" stroke-width="2.5" stroke-linejoin="round"')
    b = path("M16 31H34L36 28H48V45H16Z", bot,
             f' stroke="{bot}" stroke-width="2.5" stroke-linejoin="round"')
    return rot_b(t + b, 10)


def spiral(cx, cy, r0, r1, turns, a0=0, w=5, c=INK):
    n = int(turns * 36)
    pts = [pt(cx, cy, r0 + (r1 - r0) * k / n, a0 + 360 * turns * k / n) for k in range(n + 1)]
    return ink_stroke("M" + "L".join(f"{f(a)} {f(b)}" for a, b in pts), w, c)


def spiral_b(cx, cy, r0, r1, turns, a0=0):
    n = int(turns * 36)
    pts = []
    for i in range(n + 1):
        t = i / n
        a = math.radians(a0 + 360 * turns * t)
        r = r0 + (r1 - r0) * t
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts)


def _star(cx, cy, ro, ri, n=5, rot=-90):
    return [pt(cx, cy, ro if k % 2 == 0 else ri, rot + 180 / n * k) for k in range(2 * n)]


def star4(cx, cy, r, c=INK):
    k = r * .28
    return poly([(cx, cy - r), (cx + k, cy - k), (cx + r, cy), (cx + k, cy + k), (cx, cy + r), (cx - k, cy + k), (cx - r, cy), (cx - k, cy - k)], c, .6)


def star4_b(cx, cy, r, c=INK):
    k = r * .22
    return poly([(cx, cy - r), (cx + k, cy - k), (cx + r, cy), (cx + k, cy + k), (cx, cy + r), (cx - k, cy + k), (cx - r, cy), (cx - k, cy - k)], c, .6)


def star5(cx, cy, r, c=INK):
    return poly([pt(cx, cy, r if k % 2 == 0 else r * .45, -90 + 36 * k) for k in range(10)], c, 1)


def _star_b(cx, cy, r, colour, rounding=1.2):
    pts = [pt(cx, cy, r if k % 2 == 0 else r * .45, -90 + 36 * k) for k in range(10)]
    return poly(pts, colour, rounding)


def star_b(cx, cy, ro, ri, colour, rounding=1.2):
    return poly([pt(cx, cy, ro if k % 2 == 0 else ri, -90 + 36 * k) for k in range(10)],
                colour, rounding)


def _star_c(cx=32, cy=31, R=18):
    pts = [pt(cx, cy, R if k % 2 == 0 else R * .42, -90 + 36 * k) for k in range(10)]
    out = poly(pts, INK, 2.5)
    for k in range(5):
        tip = pts[2 * k]
        side = pts[2 * k + 1]
        out += poly([(cx, cy), tip, side], YELLOW_DARK, 1)
    return out


def star_c(cx, cy, ro, ri, rot=-90):
    return [pt(cx, cy, ro if k % 2 == 0 else ri, rot + 36 * k) for k in range(10)]


def _star_d(cx, cy, ro, ri, fill, rot=-90, rounding=1.2):
    pts = [pt(cx, cy, ro if k % 2 == 0 else ri, rot + 36 * k) for k in range(10)]
    return poly(pts, fill, rounding)


def star_d(cx, cy, ro, colour, rounding=1.2):
    return poly([pt(cx, cy, ro if k % 2 == 0 else ro * .45, -90 + 36 * k) for k in range(10)],
                colour, rounding)


def _star_e(cx, cy, ro, ri, col, rounding=1.5):
    return poly([pt(cx, cy, ro if k % 2 == 0 else ri, -90 + 36 * k) for k in range(10)], col, rounding)


def star_e(cx, cy, ro, ri, fill, n=5, rot=-90, rounding=0):
    return poly([pt(cx, cy, ro if k % 2 == 0 else ri, rot + 180 / n * k) for k in range(2 * n)],
                fill, rounding)


def _star_f(cx, cy, r, fill, k=.32):
    return poly([pt(cx, cy, r if i % 2 == 0 else r * k, -90 + 45 * i) for i in range(8)], fill, 1)


def star_f(cx, cy, n, r0, r1, rot=-90):
    return [pt(cx, cy, r0 if k % 2 == 0 else r1, rot + 180 / n * k) for k in range(2 * n)]


def star_g(cx, cy, ro, ri, colour, rounding=1):
    pts = [pt(cx, cy, ro if k % 2 == 0 else ri, -90 + 36 * k) for k in range(10)]
    return poly(pts, colour, rounding)


def star_h(cx, cy, r1, r2, fill, rounding=0, rot=-90):
    pts = [pt(cx, cy, r1 if k % 2 == 0 else r2, rot + 36 * k) for k in range(10)]
    return poly(pts, fill, rounding)


def wedge(cx, cy, r0, r1, a0, a1, c=INK):
    p = lambda r, a: "%s %s" % tuple(f(v) for v in pt(cx, cy, r, a))
    return path(f"M{p(r0, a0)}L{p(r1, a0)}A{r1} {r1} 0 0 1 {p(r1, a1)}L{p(r0, a1)}A{r0} {r0} 0 0 0 {p(r0, a0)}Z", c)


def wedge_b(cx, cy, r0, r1, a0, a1):
    """Filled ring segment path."""
    p0, p1 = pt(cx, cy, r1, a0), pt(cx, cy, r1, a1)
    q1, q0 = pt(cx, cy, r0, a1), pt(cx, cy, r0, a0)
    lg = 1 if (a1 - a0) % 360 > 180 else 0
    return (f"M{f(p0[0])} {f(p0[1])}A{f(r1)} {f(r1)} 0 {lg} 1 {f(p1[0])} {f(p1[1])}"
            f"L{f(q1[0])} {f(q1[1])}A{f(r0)} {f(r0)} 0 {lg} 0 {f(q0[0])} {f(q0[1])}Z")


def shared_brave():
    head = poly([(22, 12), (42, 12), (46.5, 16), (49, 21), (46, 33),
                 (32, 47.5), (18, 33), (15, 21), (17.5, 16)], INK, 3.5)
    nose = poly([(27, 33), (37, 33), (32, 38.5)], HOLE, 2.5)
    eyes = (poly([(20, 23), (27.5, 26.5), (25, 29.5), (21, 27)], HOLE, 1.5) +
            poly([(44, 23), (36.5, 26.5), (39, 29.5), (43, 27)], HOLE, 1.5))
    brow = poly([(28, 16.5), (36, 16.5), (32, 20)], HOLE, 1.5)
    return g(head + eyes + brow + nose, "translate(32 30) scale(.9) translate(-32 -30)")


def shared_vivaldi():
    base = circle(CX, CY, 16.5, INK)
    v = stroke("M22.5 22L30 37.5Q32 41 34 37.5L41.5 22", HOLE, 5.5)
    return base + v + circle(41.5, 22, 2.75, HOLE)


def shared_discord():
    pad = path("M19 18.5C22.5 16.5 26 15.5 28.5 15.2L29.5 17.5C31.2 17.2 32.8 17.2 34.5 17.5"
               "L35.5 15.2C38 15.5 41.5 16.5 45 18.5C49 25 50.5 32 49.8 39"
               "C46.5 41.5 43.2 43 40 44L38 40.5C39.3 40 40.5 39.3 41.5 38.6"
               "C35.5 41.5 28.5 41.5 22.5 38.6C23.5 39.3 24.7 40 26 40.5L24 44"
               "C20.8 43 17.5 41.5 14.2 39C13.5 32 15 25 19 18.5Z", INK)
    eyes = (path("M26.3 26.5a3.3 3.7 0 1 0 0.01 0Z", HOLE) +
            path("M37.7 26.5a3.3 3.7 0 1 0 0.01 0Z", HOLE))
    return pad + eyes


def shared_lo_writer():
    lines = "".join(rrect(22, y, w, 2.6, 1.3, HOLE) for y, w in
                    [(24, 19), (29, 19), (34, 19), (39, 12)])
    return _doc(lines, BLUE_SOFT)


def shared_steam():
    base = circle(CX, CY, 16.5, INK)
    arm = path("M16 33L23.5 36L34.5 29L38.5 23Z", HOLE,
               f' stroke="{HOLE}" stroke-width="2" stroke-linejoin="round"')
    big = circle(37.5, 24.5, 6.8, HOLE) + circle(37.5, 24.5, 4.5, INK) + circle(37.5, 24.5, 3, HOLE)
    small = circle(24.5, 37, 4.8, HOLE) + circle(24.5, 37, 2.2, INK)
    return base + arm + big + small


def shared_gimp_s():
    head = path("M16 24C15 17 19 12 24 13L27.5 18.5H35L40 12.5C45 13 48 18 47 24"
                "C46.5 29 43 32 43 36C43 42 38 46.5 32 46.5C24 46.5 18 41 18 34"
                "C18 30 16.5 28 16 24Z", INK)
    return head + circle(26, 26, 5.5, HOLE) + circle(38, 26, 5.5, HOLE)


def shared_kde_s():
    gear = _gear(CX, CY, 17, 13.5, 7, INK, .45) + circle(CX, CY, 9.5, HOLE)
    k = (line(28, 23.5, 28, 36.5, INK, 4) + line(29, 30.5, 36.5, 23, INK, 4) +
         line(31.5, 29.5, 37, 37, INK, 4))
    return gear + k


def shared_opensuse():
    head = path("M14.5 32C14.5 23 22 17 31.5 17C41.5 17 49.5 22.5 49.5 30.5"
                "C49.5 34.5 47 36 44 35.5C40.5 39 35.5 40.5 29.5 40.5C21 40.5 14.5 38 14.5 32Z", INK)
    eye = circle(40.5, 25.5, 5.2, HOLE) + circle(40.5, 25.5, 3.4, INK) + circle(42, 24.5, 1.5, HOLE)
    tail = stroke("M17 40C17.5 45 22 47.5 26 46C29 45 29 41.5 27 40.5", INK, 3)
    return head + eye + tail


FIREFOX_BODY = path('M22 13C16.5 16.5 14.5 22.5 15 29C15.8 39.5 23.5 47.5 33 47.5C42.5 47.5 49.5 40 49.5 30.5C49.5 22.5 44.5 15.5 37 13.5C41.5 17 44 22 43.5 27.5C43 33.5 38 38 32.5 38C26.5 38 22 33.5 22 27.5C22 23 24 19.5 27.5 17.5Z', INK)


EDGE_OUTER = path('M16 31C16 20 23 13.5 32.5 13.5C42 13.5 48.5 20 48.5 27.5C48.5 33 44 36 38.5 36C33 36 30.5 33.5 30.5 31C30.5 29 32 28 33 27.5C28 27 23 31 23 37C23 43 29 47 35 47C28 49 16 44 16 31Z', INK)


WHATSAPP_RING = path('M32 14A16 16 0 1 1 23.6 43.6L15.5 46L18 38A16 16 0 0 1 32 14Z', INK) + path('M32 17.5A12.5 12.5 0 1 1 25.2 40.5L20.8 41.8L22.1 37.4A12.5 12.5 0 0 1 32 17.5Z', HOLE)


WHATSAPP_PHONE = path('M26 24.5C26.5 23.2 27.5 22.8 28.5 23L30.2 26.8C30.3 27.4 29.7 28.3 29.2 28.8C30.3 31.2 32.3 33.2 34.7 34.3C35.2 33.8 36.1 33.2 36.7 33.3L40.5 35C40.7 36 40.3 37 39 37.5C34.5 39 24.5 29 26 24.5Z', INK)


GIMP_HEAD = path('M16 24C15 17 19 12 24 13L27.5 18.5H35L40 12.5C45 13 48 18 47 24C46.5 29 43 32 43 36C43 42 38 46.5 32 46.5C24 46.5 18 41 18 34C18 30 16.5 28 16 24Z', INK)
