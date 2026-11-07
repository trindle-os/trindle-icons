#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later
# Put the packages where apt downloads them: the trindle-icons-apt R2
set -eu

here=$(cd "$(dirname "$0")/../.." && pwd)
repo=${1:-$here/dist/apt}
key=${ICONS_APT_KEY_FILE:?set ICONS_APT_KEY_FILE to the R2 token file}
rclone=${RCLONE:?set RCLONE to the rclone binary}
host=${APT_HOST:-icons.trindle.org}

[ -f "$repo/dists/stable/InRelease" ] || { echo "$repo is not a built repository" >&2; exit 1; }
[ -f "$key" ] || { echo "no key at $key. Ask the maintainer for the token file." >&2; exit 1; }

val() { sed -n "s/^$1=//p" "$key" | tr -d "\"' \r"; }
bucket=$(val R2_BUCKET); bucket=${bucket:-trindle-icons-apt}

conf=$(mktemp)
got=$(mktemp)
trap 'rm -f "$conf" "$got"' EXIT
chmod 600 "$conf"
cat > "$conf" <<CONF
[r2]
type = s3
provider = Cloudflare
access_key_id = $(val R2_ACCESS_KEY_ID)
secret_access_key = $(val R2_SECRET_ACCESS_KEY)
endpoint = $(val R2_ENDPOINT)
acl = private
no_check_bucket = true
CONF

for deb in "$repo"/pool/main/*.deb; do
    [ -f "$deb" ] || continue
    echo "  $(basename "$deb")"
    "$rclone" --config "$conf" copyto "$deb" "r2:$bucket/pool/main/$(basename "$deb")"
    curl -fsSL -o "$got" "https://$host/pool/main/$(basename "$deb")" || { echo "could not download https://$host/pool/main/$(basename "$deb")" >&2; exit 1; }
    gothash=$(sha256sum "$got" | cut -d' ' -f1)
    want=$(sha256sum "$deb" | cut -d' ' -f1)
    [ "$gothash" = "$want" ] || { echo "https://$host serves a different $(basename "$deb")" >&2; exit 1; }
done
echo "Packages are up at https://$host. Now upload the signed index."
