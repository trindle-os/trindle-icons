#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later
set -eu

here=$(cd "$(dirname "$0")/../.." && pwd)
version=${1:-$(cat "$here/VERSION")}
repo=${2:-$here/dist/apt}
export GNUPGHOME="${GNUPGHOME:?set GNUPGHOME to the signing key folder}"
key="Trindle Icons Archive"
suite=stable
component=main

mkdir -p "$repo/pool/$component"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

deb() { # package name, theme folder, description
    pkg=$1 theme=$2 desc=$3
    root="$work/$pkg"
    [ -f "$here/$theme/index.theme" ] || { echo "$theme is not built (no index.theme). Run build.py first." >&2; exit 1; }
    mkdir -p "$root/DEBIAN" "$root/usr/share/icons"
    cp -a "$here/$theme" "$root/usr/share/icons/$theme"
    mkdir -p "$root/usr/share/doc/$pkg"
    {
        cat <<COPYRIGHT
Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: Trindle Icons
Source: https://github.com/trindle-os/trindle-icons

Files: *
Copyright: 2026 The Trindle project
License: GPL-3.0-or-later

Files: usr/share/icons/$theme/symbolic/*/*.svg
Copyright: 2026 The Trindle project
License: MIT

License: GPL-3.0-or-later
 On Debian systems, the full text of the GNU General Public License
 version 3 can be found in /usr/share/common-licenses/GPL-3.

License: MIT
COPYRIGHT
        sed -e 1,2d -e 's/^$/./' -e 's/^/ /' "$here/symbolic/LICENSE"
    } > "$root/usr/share/doc/$pkg/copyright"
    chmod -R u=rwX,go=rX "$root"
    size=$(du -sk "$root/usr" | cut -f1)
    cat > "$root/DEBIAN/control" <<CONTROL
Package: $pkg
Version: $version
Architecture: all
Maintainer: Trindle <icons@trindle.org>
Installed-Size: $size
Depends: papirus-icon-theme
Section: x11
Priority: optional
Homepage: https://github.com/trindle-os/trindle-icons
Description: $desc
 Flat app icons for Trindle and other Linux desktops: each app's own mark in white,
 lifted off a tile in the app's brand colour. Covers the apps in Papirus
 and popular apps Papirus leaves out; everything else comes from Papirus.
CONTROL
    cat > "$root/DEBIAN/postinst" <<POSTINST
#!/bin/sh
set -e
gtk-update-icon-cache -q /usr/share/icons/$theme 2>/dev/null || true
POSTINST
    chmod 755 "$root/DEBIAN/postinst"
    cat > "$root/DEBIAN/postrm" <<POSTRM
#!/bin/sh
set -e
if [ "\$1" = remove ] || [ "\$1" = purge ]; then
    rm -f /usr/share/icons/$theme/icon-theme.cache
    rmdir /usr/share/icons/$theme 2>/dev/null || true
fi
exit 0
POSTRM
    chmod 755 "$root/DEBIAN/postrm"
    echo "interest-noawait /usr/share/icons/Papirus" > "$root/DEBIAN/triggers"
    dpkg-deb --root-owner-group -Zxz --build "$root" "$repo/pool/$component/${pkg}_${version}_all.deb" >/dev/null
}

deb trindle-circle-icon-theme Trindle-Circle "Trindle Circle icon theme (circles)"

for arch in all amd64 arm64; do
    dir="$repo/dists/$suite/$component/binary-$arch"
    mkdir -p "$dir"
    (cd "$repo" && apt-ftparchive packages "pool/$component") > "$dir/Packages"
    gzip -9fkn "$dir/Packages"
done

(cd "$repo" && apt-ftparchive \
    -o "APT::FTPArchive::Release::Origin=Trindle" \
    -o "APT::FTPArchive::Release::Label=Trindle Icons" \
    -o "APT::FTPArchive::Release::Suite=$suite" \
    -o "APT::FTPArchive::Release::Codename=$suite" \
    -o "APT::FTPArchive::Release::Architectures=all amd64 arm64" \
    -o "APT::FTPArchive::Release::Components=$component" \
    -o "APT::FTPArchive::Release::Description=Trindle icon themes" \
    release "dists/$suite") > "$repo/dists/$suite/Release"

rm -f "$repo/dists/$suite/Release.gpg" "$repo/dists/$suite/InRelease"
gpg --batch --yes --default-key "$key" --armor --detach-sign \
    -o "$repo/dists/$suite/Release.gpg" "$repo/dists/$suite/Release"
gpg --batch --yes --default-key "$key" --clearsign \
    -o "$repo/dists/$suite/InRelease" "$repo/dists/$suite/Release"
gpg --batch --armor --export "$key" > "$repo/key.asc"

echo "Repository written to $repo"
ls -la "$repo/pool/$component"
