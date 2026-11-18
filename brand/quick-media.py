#!/usr/bin/env python3
"""Generate editable AI Society quick-media SVGs from one JSON brief."""
import argparse
import csv
import json
import os
from pathlib import Path
import subprocess
import tempfile
from xml.etree import ElementTree as ET

BRAND = Path(__file__).resolve().parent
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
TOKENS = json.loads((BRAND / "tokens.json").read_text(encoding="utf-8"))
MEDIA = TOKENS["quickMedia"]

# Coordinates are baselines in the export canvas. The Story leaves a separate
# clear band for the native link sticker below the available text slots.
LAYOUTS = {
    "landscape-5x3": dict(logo=112, lead=190, title=320, size=112, detail=510, line=637, footer=715, type=50),
    "feed-4x5": dict(logo=116, lead=292, title=493, size=114, detail=760, line=933, footer=1030, type=47),
    "story-9x16": dict(logo=116, lead=460, title=650, size=114, detail=912, line=1062, footer=1155, type=47),
    "luma-1x1": dict(logo=144, title=535, size=110),
    "link-1200x627": dict(logo=90, lead=128, title=229, size=89, detail=424, type=37),
}
EXAMPLE = {
    "lead": "WORKSHOP",
    "title": ["Build a", "tiny game"],
    "detail": "No coding experience needed.",
    "when": "Thu 12 Mar · 18:30",
    "where": "Ravelin Library",
    "action": "Sign up required",
}
LIMITS = {"lead": 22, "detail": 45, "when": 32, "where": 32, "action": 21}
HEADLINE_LIMIT = 17
FONTS = {"lead": ("mono", 500), "headline-1": ("display", 800), "headline-2": ("display", 800),
         "detail": ("sans", 500), "when": ("sans", 600), "where": ("sans", 500), "action": ("sans", 600)}


def element(parent, tag, text=None, **attrs):
    node = ET.SubElement(parent, f"{{{SVG}}}{tag}", {key.replace("_", "-"): str(value) for key, value in attrs.items()})
    node.text = text
    return node


def read_copy(data):
    if not isinstance(data, dict):
        raise ValueError("Provide a JSON object for the brief.")
    if unknown := data.keys() - (LIMITS.keys() | {"title"}):
        raise ValueError(f"Unknown brief fields: {', '.join(sorted(unknown))}")
    lines = data.get("title")
    if not isinstance(lines, list) or not 1 <= len(lines) <= 2:
        raise ValueError("Provide one or two headline lines in title.")
    slots = {f"headline-{index}": value for index, value in enumerate(lines, 1)}
    if any(not isinstance(line, str) or not line.strip() for line in lines):
        raise ValueError("Headline lines must contain text.")
    slots.update({field: data.get(field, "") for field in LIMITS})
    for slot, value in slots.items():
        if (not isinstance(value, str) or len(value) > LIMITS.get(slot, HEADLINE_LIMIT)
                or any(ord(char) < 32 for char in value)):
            raise ValueError(f"{slot} must be one line with up to {LIMITS.get(slot, HEADLINE_LIMIT)} characters.")
    return slots


def compose(format_name, theme_name, slots):
    spec = MEDIA["formats"][format_name]
    width, height = spec["width"], spec["height"]
    x, y = (spec["safeInset"][axis] for axis in ("x", "y"))
    layout = LAYOUTS[format_name]
    theme = MEDIA["themes"][theme_name]
    bg, fg = (TOKENS["colors"][theme[key]] for key in ("background", "foreground"))
    is_cover = format_name == "luma-1x1"
    root = ET.Element(f"{{{SVG}}}svg", {
        "width": str(width), "height": str(height), "viewBox": f"0 0 {width} {height}",
        "role": "img", "aria-labelledby": "asset-title asset-description",
    })
    headline = " ".join(slots[key] for key in ("headline-1", "headline-2") if slots.get(key))
    element(root, "title", f"{headline} | AI Society", id="asset-title")
    desc_slots = ("lead", "detail", "when", "where", "action") if "footer" in layout else ("lead", "detail")
    descriptions = [slots[key] for key in desc_slots if slots.get(key)]
    element(root, "desc", " · ".join(descriptions) or "University of Portsmouth AI Society", id="asset-description")
    root.append(ET.Comment("Copy before editing. Replace or clear slot text. Preserve the viewBox, theme and logo."))
    element(root, "rect", width=width, height=height, fill=bg)
    logo_source = ET.parse(BRAND / "logos/logo-stacked.svg").getroot()
    logo = logo_source.find(f".//{{{SVG}}}symbol[@id='brand-logo']")
    defs = element(root, "defs")
    defs.append(logo)
    logo_width = layout["logo"]
    logo_x = (width - logo_width) // 2 if is_cover else width - x - logo_width
    element(root, "use", href="#brand-logo", x=logo_x, y=y, width=logo_width,
            height=round(logo_width * 583 / 692), color=fg, id="logo", aria_hidden="true")

    def draw(slot, at_x, at_y, size, anchor="start"):
        family, weight = FONTS[slot]
        attributes = {"letter_spacing": "-0.03em"} if family == "display" else {}
        element(root, "text", slots.get(slot, ""), id=f"slot-{slot}", data_slot=slot,
                            x=at_x, y=at_y, fill=fg, font_size=size, font_weight=weight,
                            font_family=TOKENS["typography"][family]["family"], text_anchor=anchor, **attributes)

    title_size = layout["size"]
    first_line = layout["title"] + (0 if slots.get("headline-2") else title_size // 2)
    if is_cover:
        draw("headline-1", width // 2, first_line, title_size, "middle")
        draw("headline-2", width // 2, layout["title"] + title_size, title_size, "middle")
        # The Luma thumbnail carries the title and identity. Native fields carry logistics.
        root.find(f"{{{SVG}}}desc").text = "University of Portsmouth AI Society event cover"
        return root

    draw("lead", x, layout["lead"], round(layout["type"] * .74))
    draw("headline-1", x, first_line, title_size)
    draw("headline-2", x, layout["title"] + title_size, title_size)
    draw("detail", x, layout["detail"], layout["type"])
    if "footer" in layout:
        if any(slots.get(key) for key in ("when", "where", "action")):
            element(root, "path", d=f"M{x} {layout['line']}H{width-x}", stroke=fg,
                    stroke_opacity=".33", stroke_width="2")
        draw("when", x, layout["footer"], layout["type"])
        draw("where", x, layout["footer"] + round(layout["type"] * 1.3), round(layout["type"] * .94))
        draw("action", width - x, layout["footer"] + round(layout["type"] * 1.3),
             round(layout["type"] * .96), "end")
    return root


def verify_layout(svg_path, root, format_name):
    spec = MEDIA["formats"][format_name]
    inset = spec["safeInset"]
    output = subprocess.run(["inkscape", str(svg_path), "--query-all"],
                            capture_output=True, text=True, check=True).stdout
    active = {"logo"} | {node.get("id") for node in root.findall(f"{{{SVG}}}text") if node.text}
    bounds = {row[0]: tuple(map(float, row[1:])) for row in csv.reader(output.splitlines())
              if len(row) == 5 and row[0] in active}
    if bounds.keys() != active:
        raise ValueError(f"{format_name}: could not measure every active slot")
    for index, (slot, (x, y, w, h)) in enumerate(bounds.items()):
        if (x < inset["x"] - 2 or y < inset["y"] - 2
                or x + w > spec["width"] - inset["x"] + 2 or y + h > spec["height"] - inset["y"] + 2):
            raise ValueError(f"{format_name}: {slot} runs beyond the safe area. Shorten the text.")
        for other, (ox, oy, ow, oh) in list(bounds.items())[index + 1:]:
            if x < ox + ow and ox < x + w and y < oy + oh and oy < y + h:
                raise ValueError(f"{format_name}: {slot} overlaps {other}. Shorten the text.")


def write_card(path, root, format_name, png):
    ET.indent(root, space="  ")
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)
    if png:
        verify_layout(path, root, format_name)
        raster = path.with_suffix(".png")
        subprocess.run(["inkscape", str(path), "--export-area-page", f"--export-filename={raster}"],
                       capture_output=True, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Destination directory")
    parser.add_argument("--brief", type=Path, help="JSON campaign brief. Omit to build the editable examples.")
    parser.add_argument("--theme", choices=MEDIA["themes"], help="Omit to generate both themes.")
    parser.add_argument("--format", choices=MEDIA["formats"], action="append", help="Omit to generate all formats.")
    parser.add_argument("--png", action="store_true", help="Check layout and export PNGs using Inkscape.")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        data = json.loads(args.brief.read_text(encoding="utf-8")) if args.brief else EXAMPLE
        slots = read_copy(data)
        with tempfile.TemporaryDirectory(dir=args.output) as work:
            stage = Path(work)
            for format_name in dict.fromkeys(args.format or MEDIA["formats"]):
                for theme in (args.theme,) if args.theme else MEDIA["themes"]:
                    path = stage / f"{format_name}-{theme}.svg"
                    write_card(path, compose(format_name, theme, slots), format_name, args.png)
            for path in sorted(stage.iterdir()):
                os.replace(path, args.output / path.name)
                print(path.name)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    except subprocess.CalledProcessError as error:
        parser.error(f"Inkscape could not render a card (exit {error.returncode}).")


if __name__ == "__main__":
    main()
