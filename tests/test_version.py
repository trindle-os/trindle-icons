# SPDX-License-Identifier: GPL-3.0-or-later
"""Fails if the README version badge differs from the VERSION file."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    with open(os.path.join(ROOT, "VERSION"), encoding="utf-8") as fh:
        version = fh.read().strip()
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
        badges = re.findall(r"badge/version-([\w.]+)-", fh.read())
    if badges != [version]:
        print(f"README version badge {badges} does not match VERSION {version}", file=sys.stderr)
        return 1
    print("version badge matches VERSION")
    return 0


if __name__ == "__main__":
    sys.exit(main())
