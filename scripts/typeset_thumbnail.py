"""Typeset clean thumbnail lettering over generated artwork; no semantic image edits."""
from pathlib import Path
import argparse
import json
import shutil

from PIL import Image, ImageDraw, ImageFont


def render(config):
    source = Path(config["source"]).expanduser().resolve()
    output = Path(config["output_dir"]).expanduser().resolve()
    stem = config.get("stem", "thumbnail")
    if not stem or Path(stem).name != stem or any(c in stem for c in '<>:"/\\|?*'):
        raise ValueError("stem must be a plain filename without extension or path characters")
    width, height = map(int, config.get("size", [1080, 1920]))
    if width <= 0 or height <= 0:
        raise ValueError("size must contain positive width and height")
    font_path = Path(config.get("font", Path(__file__).resolve().parents[1] / "assets/fonts/Bangers/Bangers-Regular.ttf")).expanduser().resolve()
    files = {
        "native": output / ("native-artwork" + source.suffix.lower()),
        "artwork": output / "artwork-no-text.png",
        "type": output / "typography-layer.png",
        "png": output / (stem + ".png"),
        "jpg": output / (stem + ".jpg"),
        "layout": output / "layout.json",
        "preview": output / "preview.png",
    }
    conflicts = [str(p) for p in files.values() if p.exists()]
    if conflicts:
        raise FileExistsError("Use a new versioned output folder; existing files: " + ", ".join(conflicts))
    with Image.open(source) as image:
        art = image.convert("RGBA").resize((width, height), Image.Resampling.LANCZOS)
    overlay = Image.new("RGBA", (width, height))
    headline = config.get("headline")
    chosen_size = None
    if headline:
        lines = headline["lines"]
        if not lines or any(not line["text"].strip() for line in lines):
            raise ValueError("headline lines must contain nonempty text")
        x, y, box_width, box_height = map(int, headline["box"])
        if min(x, y) < 0 or min(box_width, box_height) <= 0 or x + box_width > width or y + box_height > height:
            raise ValueError("headline box must be entirely inside the canvas")
        scale = 3
        stroke = int(headline.get("stroke", 8))
        gap = int(headline.get("gap", 12))
        smallest = int(headline.get("min_font", 60))
        largest = int(headline.get("max_font", 235))
        if stroke < 0 or gap < 0 or smallest <= 0 or largest < smallest:
            raise ValueError("invalid font-size, stroke or gap settings")
        probe = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
        for size in range(largest, smallest - 1, -1):
            font = ImageFont.truetype(str(font_path), size * scale)
            boxes = [probe.textbbox((0, 0), line["text"], font=font, stroke_width=stroke * scale) for line in lines]
            widths = [b[2] - b[0] for b in boxes]
            heights = [b[3] - b[1] for b in boxes]
            if max(widths) + 4 * scale <= box_width * scale and sum(heights) + gap * scale * (len(lines) - 1) + 4 * scale * (len(lines) + 1) <= box_height * scale:
                chosen_size = size
                break
        if chosen_size is None:
            raise ValueError("headline does not fit; shorten copy or choose a larger measured free box")
        cursor = y + 2
        for line, bounds, line_width, line_height in zip(lines, boxes, widths, heights):
            patch = Image.new("RGBA", (line_width + 12, line_height + 12))
            draw = ImageDraw.Draw(patch)
            draw.text((6 - bounds[0], 6 - bounds[1]), line["text"], font=font,
                      fill=line.get("color", "#ffffff"), stroke_width=stroke * scale,
                      stroke_fill=headline.get("stroke_color", "#070c1a"))
            patch = patch.resize((round(patch.width / scale), round(patch.height / scale)), Image.Resampling.LANCZOS)
            overlay.alpha_composite(patch, (x + (box_width - patch.width) // 2, cursor))
            cursor += patch.height + gap
        overlay_bounds = overlay.getbbox()
        if overlay_bounds and not (x <= overlay_bounds[0] and y <= overlay_bounds[1] and overlay_bounds[2] <= x + box_width and overlay_bounds[3] <= y + box_height):
            raise ValueError("rendered text exceeds the reserved headline box")
    final = Image.alpha_composite(art, overlay).convert("RGB")
    output.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, files["native"])
    art.save(files["artwork"])
    overlay.save(files["type"])
    final.save(files["png"], optimize=True)
    final.save(files["jpg"], quality=95, subsampling=0, optimize=True)
    preview_width = 180 if height > width else 384
    final.resize((preview_width, round(preview_width * height / width)), Image.Resampling.LANCZOS).save(files["preview"])
    layout = dict(config, chosen_font_size=chosen_size, font=str(font_path), output_files={k: str(v) for k, v in files.items()})
    files["layout"].write_text(json.dumps(layout, indent=2), encoding="utf-8")
    if headline:
        font_dir = output / "fonts"
        font_dir.mkdir(exist_ok=True)
        shutil.copy2(font_path, font_dir / font_path.name)
        for name in ("OFL.txt", "LICENSE.txt"):
            license_path = font_path.parent / name
            if license_path.is_file():
                shutil.copy2(license_path, font_dir / name)
    return layout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    args = parser.parse_args()
    result = render(json.loads(args.config.read_text(encoding="utf-8")))
    print(json.dumps(result["output_files"], indent=2))


if __name__ == "__main__":
    main()

