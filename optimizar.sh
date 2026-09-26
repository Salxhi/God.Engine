#!/usr/bin/env bash
# Uso: ./optimizar.sh <carpeta-origen> <planeta-XX>
# Ej:  ./optimizar.sh ~/Descargas/vacaciones planeta-01
set -e

ORIGEN="$1"
DEST="Universo/fotos/$2"

if [ -z "$ORIGEN" ] || [ -z "$2" ]; then
  echo "Uso: ./optimizar.sh <carpeta-origen> <planeta-01..planeta-10|sol>"
  exit 1
fi

mkdir -p "$DEST"
i=1
for f in "$ORIGEN"/*.{jpg,jpeg,png,JPG,JPEG,PNG,heic,HEIC}; do
  [ -e "$f" ] || continue
  out="$DEST/foto-$(printf '%02d' $i).webp"
  echo "→ $f  →  $out"
  if command -v magick >/dev/null 2>&1; then
    magick "$f" -auto-orient -resize '1200x1200>' -quality 80 -strip "$out"
  elif command -v convert >/dev/null 2>&1; then
    convert "$f" -auto-orient -resize '1200x1200>' -quality 80 -strip "$out"
  elif command -v cwebp >/dev/null 2>&1; then
    cwebp -q 80 -resize 1200 0 -metadata none "$f" -o "$out"
  else
    echo "ERROR: instala imagemagick o webp. Ej: sudo apt install imagemagick webp"
    exit 1
  fi
  i=$((i+1))
done

echo ""
echo "Listo. $(($i-1)) imágenes en $DEST"
echo "Tamaño total: $(du -sh "$DEST" | cut -f1)"
