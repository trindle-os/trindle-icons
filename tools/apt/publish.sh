#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later
set -eu

here=$(cd "$(dirname "$0")/../.." && pwd)
repo=${1:-$here/dist/apt}
key=${ICONS_APT_KEY_FILE:?set ICONS_APT_KEY_FILE to the R2 token file}
rclone=${RCLONE:?set RCLONE to the rclone binary}
host=${APT_HOST:-icons.trindle.org}

[ -f "$repo/dists/stable/InRelease" ] || { echo "$repo is not a built repository" >&2; exit 1; }
[ -f "$key" ] || { echo "no key at $key. Ask the maintainer for the token file." >&2; exit 1; }

val() {
    v=$(sed -n "s/^$1=//p" "$key" | tr -d "\"' \r")
    [ -n "$v" ] || { echo "$key has no $1" >&2; exit 1; }
    printf '%s' "$v"
}
bucket=$(sed -n 's/^R2_BUCKET=//p' "$key" | tr -d "\"' \r"); bucket=${bucket:-trindle-icons-apt}

RCLONE_CONFIG=/dev/null
RCLONE_CONFIG_R2_TYPE=s3
RCLONE_CONFIG_R2_PROVIDER=Cloudflare
RCLONE_CONFIG_R2_ACCESS_KEY_ID=$(val R2_ACCESS_KEY_ID)
RCLONE_CONFIG_R2_SECRET_ACCESS_KEY=$(val R2_SECRET_ACCESS_KEY)
RCLONE_CONFIG_R2_ENDPOINT=$(val R2_ENDPOINT)
RCLONE_CONFIG_R2_ACL=private
RCLONE_CONFIG_R2_NO_CHECK_BUCKET=true
export RCLONE_CONFIG RCLONE_CONFIG_R2_TYPE RCLONE_CONFIG_R2_PROVIDER RCLONE_CONFIG_R2_ACCESS_KEY_ID \
    RCLONE_CONFIG_R2_SECRET_ACCESS_KEY RCLONE_CONFIG_R2_ENDPOINT RCLONE_CONFIG_R2_ACL RCLONE_CONFIG_R2_NO_CHECK_BUCKET

got=$(mktemp)
trap 'rm -f "$got"' EXIT
trap 'exit 130' INT TERM HUP

for deb in "$repo"/pool/main/*.deb; do
    [ -f "$deb" ] || continue
    name=$(basename "$deb")
    want=$(sha256sum "$deb" | cut -d' ' -f1)
    echo "  $name"
    if curl -fsSL -o "$got" "https://$host/pool/main/$name" 2>/dev/null; then
        [ "$(sha256sum "$got" | cut -d' ' -f1)" = "$want" ] && continue
        echo "$name is already published with different contents. Raise VERSION and build again." >&2
        exit 1
    fi
    "$rclone" copyto "$deb" "r2:$bucket/pool/main/$name"
    curl -fsSL -o "$got" "https://$host/pool/main/$name" || { echo "could not download https://$host/pool/main/$name" >&2; exit 1; }
    [ "$(sha256sum "$got" | cut -d' ' -f1)" = "$want" ] || { echo "https://$host serves a different $name" >&2; exit 1; }
done

echo "Packages are up. Uploading the signed index."
"$rclone" copy "$repo/dists" "r2:$bucket/dists"
[ ! -f "$repo/key.asc" ] || "$rclone" copyto "$repo/key.asc" "r2:$bucket/key.asc"
echo "Published at https://$host."
