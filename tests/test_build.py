# SPDX-License-Identifier: GPL-3.0-or-later
"""Build script checks on a tiny temp fixture. Run: venv/bin/python tests/test_build.py"""
import contextlib, io, os, sys, tempfile, types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import build  # noqa: E402


def run(argv):
    err = io.StringIO()
    with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
        code = build.main(argv)
    return code, err.getvalue()


err = io.StringIO()
try:
    with contextlib.redirect_stderr(err):
        build.main(["square"])
    raise AssertionError("an extra argument was accepted")
except SystemExit as e:
    assert e.code == 2 and "usage" in err.getvalue()

with tempfile.TemporaryDirectory() as tmp:
    papirus = os.path.join(tmp, "Papirus")
    os.makedirs(papirus)
    os.makedirs(os.path.join(papirus, "sub"))
    with open(os.path.join(papirus, "sub", "c.svg"), "w") as fh:
        fh.write("<svg/>")
    os.symlink("sub/c.svg", os.path.join(papirus, "b.svg"))
    os.symlink("b.svg", os.path.join(papirus, "a.svg"))
    extra = os.path.join(tmp, "extra.txt")
    with open(extra, "w") as fh:
        fh.write("# note\none two three\n")

    build.SRC = os.path.join(tmp, "nowhere")
    code, msg = run([])
    assert code == 1 and "Papirus apps folder not found" in msg, msg
    build.SRC = papirus
    build.PAPIRUS = os.path.join(tmp, "nowhere")
    code, msg = run([])
    assert code == 1 and "Installed Papirus theme not found" in msg, msg
    with open(os.path.join(papirus, "index.theme"), "w") as fh:
        fh.write("[Icon Theme]\nDirectories=\n")
    build.PAPIRUS = papirus

    build.EXTRA = extra
    try:
        build.alias_links({})
        raise AssertionError("bad alias line was accepted")
    except ValueError as e:
        assert "line 2" in str(e)
    with open(extra, "w") as fh:
        fh.write("# none\n")

    build.THEME = os.path.join(tmp, "theme")
    build.load = lambda: ({"c": (lambda: "", "#123456")}, {})
    build.write_symbolic = lambda theme: 0
    code, _ = run([])
    assert code == 1, code

    os.remove(os.path.join(papirus, "a.svg"))
    code, _ = run([])
    assert code == 0, code

import importlib, pkgutil
mods = [types.SimpleNamespace(ICONS={"dup": (None, "#fff")}), types.SimpleNamespace(ICONS={"dup": (None, "#fff")})]
real = importlib.reload(build)
saved = pkgutil.iter_modules, importlib.import_module
pkgutil.iter_modules = lambda paths: [types.SimpleNamespace(name="batch_a"), types.SimpleNamespace(name="batch_b")]
importlib.import_module = lambda n: mods[0] if n.endswith(".batch_a") else mods[1]
try:
    real.load()
    raise AssertionError("duplicate name accepted")
except ValueError as e:
    assert "dup" in str(e)
finally:
    pkgutil.iter_modules, importlib.import_module = saved

with tempfile.TemporaryDirectory() as tmp:
    src, out = os.path.join(tmp, "src"), os.path.join(tmp, "out")
    os.makedirs(src)
    os.makedirs(out)
    open(os.path.join(src, "brave.svg"), "w").close()
    os.symlink("brave.svg", os.path.join(src, "brave-browser.svg"))
    os.symlink("brave.svg", os.path.join(src, "pinta.svg"))
    extra = os.path.join(tmp, "extra_aliases.txt")
    open(extra, "w").close()
    build.SRC, build.EXTRA = src, extra
    links = dict(build.alias_links({"brave": None, "pinta": None}))
    assert "pinta.svg" not in links, "our pinta icon was replaced by an alias"
    assert links.get("brave-browser.svg") == "brave.svg", "a plain alias was not linked"

print("ok")
