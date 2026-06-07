#!/usr/bin/env python
"""Generate contact sheets and palette metadata for a scientific figure gallery."""

from __future__ import print_function

import argparse
import colorsys
import json
import os
from collections import Counter

from PIL import Image, ImageDraw, ImageFont, ImageOps


EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"}


def iter_images(folder):
    for dirpath, _, filenames in os.walk(folder):
        for name in filenames:
            if os.path.splitext(name)[1].lower() in EXTENSIONS:
                yield os.path.join(dirpath, name)


def quantize_channel(value, step=16):
    rounded = int(round(value / float(step)) * step)
    return max(0, min(255, rounded))


def to_hex(rgb):
    return "#%02x%02x%02x" % rgb


def dominant_palette(image, max_pixels=100000, n=10):
    image = ImageOps.exif_transpose(image).convert("RGB")
    image.thumbnail((900, 900), Image.LANCZOS)
    pixels = list(image.getdata())
    step = max(1, len(pixels) // max_pixels)
    counts = Counter()
    for r, g, b in pixels[::step]:
        _, saturation, value = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
        if value > 0.965 and saturation < 0.12:
            continue
        if value < 0.16 and saturation < 0.25:
            continue
        if saturation < 0.10:
            continue
        rgb = tuple(quantize_channel(v) for v in (r, g, b))
        counts[rgb] += 1
    return [{"hex": to_hex(rgb), "count": count} for rgb, count in counts.most_common(n)]


def load_font(size):
    for name in ("Arial.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            pass
    return ImageFont.load_default()


def make_contact_sheet(files, output_path, thumb_w=420, thumb_h=300, columns=4):
    label_h = 34
    rows = (len(files) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * thumb_w, max(1, rows * (thumb_h + label_h))), "white")
    draw = ImageDraw.Draw(sheet)
    font = load_font(16)
    for idx, path in enumerate(files):
        with Image.open(path) as image:
            image = ImageOps.exif_transpose(image).convert("RGB")
            image.thumbnail((thumb_w - 16, thumb_h - 16), Image.LANCZOS)
            x = (idx % columns) * thumb_w + (thumb_w - image.width) // 2
            y = (idx // columns) * (thumb_h + label_h) + 8
            sheet.paste(image, (x, y))
        label = "%02d %s" % (idx + 1, os.path.basename(path)[:28])
        draw.text(((idx % columns) * thumb_w + 8, (idx // columns) * (thumb_h + label_h) + thumb_h + 6), label, fill=(20, 20, 20), font=font)
    sheet.save(output_path, quality=92)


def main():
    parser = argparse.ArgumentParser(description="Scan a scientific figure gallery.")
    parser.add_argument("gallery", help="Folder containing reference figure images")
    parser.add_argument("--out", default="gallery_scan", help="Output folder")
    args = parser.parse_args()

    files = sorted(iter_images(args.gallery))
    if not os.path.isdir(args.out):
        os.makedirs(args.out)

    manifest = []
    for path in files:
        with Image.open(path) as image:
            width, height = image.size
            palette = dominant_palette(image)
        manifest.append({
            "file": os.path.basename(path),
            "path": os.path.abspath(path),
            "width": width,
            "height": height,
            "aspect_ratio": round(width / float(height), 4),
            "palette": palette,
        })

    with open(os.path.join(args.out, "manifest.json"), "w", encoding="utf-8") as handle:
        json.dump({"count": len(manifest), "images": manifest}, handle, ensure_ascii=False, indent=2)

    make_contact_sheet(files, os.path.join(args.out, "contact_sheet.jpg"))
    print("Scanned %d images into %s" % (len(files), os.path.abspath(args.out)))


if __name__ == "__main__":
    main()
