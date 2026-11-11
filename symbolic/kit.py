# SPDX-License-Identifier: MIT
"""Drawing kit for the small one-colour (symbolic) icons.

16x16 grid, one colour (#bebebe, which GTK repaints in the text colour),
1.5px strokes with round ends and joins, rounded corners and circles
wherever a shape allows. Clear before clever.
"""
import math

C = "#bebebe"
SW = 1.5


def svg(body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">'
            f'<g fill="none" stroke="{C}" stroke-width="{SW}" stroke-linecap="round" '
            f'stroke-linejoin="round">{body}</g></svg>\n')


def n(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def p(d, extra=""):
    """A stroked path."""
    return f'<path d="{d}"{extra}/>'


def s(d, extra=""):
    """A solid shape."""
    edge = "" if "stroke=" in extra else ' stroke="none"'
    return f'<path d="{d}" fill="{C}"{edge}{extra}/>'


def c(cx, cy, r, extra=""):
    return f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}"{extra}/>'


def dot(cx, cy, r=1.1, extra=""):
    return f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" fill="{C}" stroke="none"{extra}/>'


def r(x, y, w, h, rx=2, extra=""):
    return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="{n(rx)}"{extra}/>'


def rs(x, y, w, h, rx=1, extra=""):
    return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="{n(rx)}" fill="{C}" stroke="none"{extra}/>'


def ln(x1, y1, x2, y2, extra=""):
    return f'<path d="M{n(x1)} {n(y1)}L{n(x2)} {n(y2)}"{extra}/>'


def arc(cx, cy, rad, a0, a1, extra=""):
    """Stroked arc from angle a0 to a1 (degrees, clockwise, 0 = east)."""
    x0, y0 = cx + rad * math.cos(math.radians(a0)), cy + rad * math.sin(math.radians(a0))
    x1, y1 = cx + rad * math.cos(math.radians(a1)), cy + rad * math.sin(math.radians(a1))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f'<path d="M{n(x0)} {n(y0)}A{n(rad)} {n(rad)} 0 {large} 1 {n(x1)} {n(y1)}"{extra}/>'


FAINT = ' opacity=".35"'


def slash():
    """The 'off' stroke drawn over a symbol."""
    return ln(2.5, 2.5, 13.5, 13.5)


def outlined(doc, name="?"):
    """The same icon with every line turned into a filled outline.

    Newer GTK paints symbolic icons with its own reader, which fills shapes
    and ignores strokes unless they are specially tagged, so a line-drawn
    icon comes out blank there. Filled outlines look the same everywhere."""
    from picosvg.svg import SVG
    try:
        out = SVG.fromstring(doc).topicosvg().tostring()
    except Exception as e:
        raise ValueError(f"picosvg could not outline symbolic icon {name!r}: {e}") from e
    return out.replace("<defs/>", "").replace("<path ", '<path class="foreground-fill" ') + "\n"
