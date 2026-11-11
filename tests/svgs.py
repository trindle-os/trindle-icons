# SPDX-License-Identifier: GPL-3.0-or-later
"""Shared by the tests that read built icons."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def own_svgs(*themes):
    """Yield built SVGs without following the symlinks into Papirus's own folders."""
    for theme in themes:
        for d, _, names in os.walk(os.path.join(ROOT, theme)):
            for n in names:
                p = os.path.join(d, n)
                if n.endswith(".svg") and not os.path.islink(p):
                    yield p
