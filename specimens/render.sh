#!/bin/sh
# Рендер образцов в PNG 1080x1080 (Chromium из /opt/pw-browsers).
# Окно берётся выше нужного: headless-режим съедает часть высоты, лишнее обрезается.
cd "$(dirname "$0")"
CH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
for n in "$@"; do
  $CH --headless=new --no-sandbox --disable-gpu --hide-scrollbars --allow-file-access-from-files \
      --force-device-scale-factor=1 --window-size=1080,1230 --virtual-time-budget=4000 \
      --screenshot="$PWD/$n.png" "file://$PWD/$n.html" >/dev/null 2>&1
  python3 -c "from PIL import Image; im=Image.open('$n.png'); im.crop((0,0,1080,1080)).save('$n.png'); print('$n.png', Image.open('$n.png').size)"
done
