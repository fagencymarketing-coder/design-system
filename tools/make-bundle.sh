#!/bin/sh
# Собирает папку и ZIP для загрузки в проект Claude Design: dist/claude-design-upload(.zip)
set -e
cd "$(dirname "$0")/.."
B=dist/claude-design-upload; rm -rf dist; mkdir -p $B/rules $B/tokens $B/assets
cp -r templates $B/templates; rm -f $B/templates/previews/_sheet.png
cp tokens/v2.css $B/tokens/v2.css
for d in icons marks team director experts; do cp -r assets/$d $B/assets/$d; done
cp assets/logo.png assets/logo-full.png assets/logo-full-white.png assets/logo-mark-white.png assets/pattern-1.png assets/pattern-2.png assets/badge-round.png $B/assets/
cp docs/readme-v2.md docs/team-photos.md docs/director-photos.md $B/rules/
sed 's#docs/readme-v2.md#rules/readme-v2.md#g; s#docs/team-photos.md#rules/team-photos.md#g; s#docs/director-photos.md#rules/director-photos.md#g' docs/claude-design-readme.md > $B/readme.md
sed -i 's#docs/#rules/#g; s#specimens/#templates/previews/#g' $B/rules/*.md
(cd dist && zip -qr claude-design-upload.zip claude-design-upload)
du -sh dist/claude-design-upload.zip
