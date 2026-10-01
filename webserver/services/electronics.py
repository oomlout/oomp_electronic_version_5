"""Presentation of collected component facts without changing source records."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

TIER_OPTIONS = (("basic", "Basic"), ("extended", "Extended"), ("unknown", "Unclassified"))


def mapping(value: Any) -> dict:
    return value if isinstance(value, dict) else {}


def entries(value: Any) -> list[dict]:
    return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []


def readable(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "Yes" if value else "No"
    if isinstance(value, dict):
        return "; ".join(f"{str(key).replace('_', ' ')}: {readable(item)}" for key, item in value.items())
    if isinstance(value, list):
        return "; ".join(readable(item) for item in value)
    return str(value)


def safe_url(value: Any) -> str:
    value = str(value or "").strip()
    try:
        parsed = urlsplit(value)
        return value if parsed.scheme in {"https", "http"} and parsed.netloc else ""
    except ValueError:
        return ""


def component_details(data: dict) -> dict:
    page = mapping(data.get("part_page"))
    selection = mapping(data.get("jlcpcb_selection"))
    raw_tier = str(selection.get("tier") or selection.get("tier_label_observed") or "").strip().lower().replace(" ", "_")
    tier = "basic" if raw_tier == "basic" else "extended" if raw_tier in {"extended", "preferred_extended", "preferred"} else "unknown"
    tier_label = "Preferred Extended" if raw_tier in {"preferred", "preferred_extended"} else dict(TIER_OPTIONS)[tier]
    manufacturers = entries(data.get("part_numbers_manufacturer")) or entries(data.get("manufacturers"))
    manufacturer = data.get("manufacturer") or next((item.get("manufacturer") for item in manufacturers if item.get("manufacturer")), "")
    mpn = data.get("part_number_manufacturer") or next((item.get("part_number") for item in manufacturers if item.get("part_number")), "")
    links: list[dict] = []

    def add_link(label: str, value: Any, url: Any) -> None:
        url = safe_url(url)
        if url and not any(item["url"] == url for item in links):
            links.append({"label": label, "value": readable(value), "url": url})

    lcsc = data.get("part_number_lcsc", "")
    add_link("LCSC", lcsc, data.get("part_number_lcsc_url") or (f"https://www.lcsc.com/product-detail/{lcsc}.html" if re.fullmatch(r"C\d+", str(lcsc)) else ""))
    add_link("JLCPCB", data.get("part_number_jlcpcb", ""), data.get("part_number_jlcpcb_url") or selection.get("official_url"))
    for item in entries(data.get("distributors")):
        add_link(item.get("title") or str(item.get("key", "Supplier")).upper(), item.get("part_number", ""), item.get("url"))
    for item in entries(data.get("part_numbers_lcsc")):
        code = str(item.get("part_number", ""))
        add_link("LCSC", code, item.get("url") or (f"https://www.lcsc.com/product-detail/{code}.html" if re.fullmatch(r"C\d+", code) else ""))
    for item in entries(page.get("identifiers")):
        add_link(item.get("title", "Supplier"), item.get("value", ""), item.get("url"))
    add_link("Product page", "", data.get("product_url"))
    add_link("Datasheet source", "", data.get("datasheet_url"))
    add_link("GitHub", "", data.get("link_github") or page.get("repository_url"))

    facts = []
    for label, value in (
        ("Manufacturer", manufacturer), ("Manufacturer part number", mpn),
        ("Package", data.get("package_name_manufacturer") or data.get("taxonomy_3")),
        ("LCSC part number", lcsc), ("JLCPCB part number", data.get("part_number_jlcpcb")),
        ("Stock at verification", selection.get("stock_observed")),
        ("Purchase MOQ at verification", selection.get("purchase_moq_observed")),
        ("PCBA minimum at verification", selection.get("pcba_min_qty_observed")),
        ("Verified on", selection.get("verified_on")),
    ):
        if value is not None and value != "":
            facts.append({"label": label, "value": readable(value)})

    groups = []
    for title, values in (
        ("Electrical specifications", data.get("electrical")),
        ("Supplier ratings", selection.get("ratings")),
        ("Dimensions (mm)", data.get("dimensions_mm")),
        ("KiCad libraries", data.get("kicad")),
        ("Dimension reference", data.get("dimension_reference")),
    ):
        rows = [{"label": str(key).replace("_", " ").capitalize(), "value": readable(value)}
                for key, value in mapping(values).items() if value is not None and value != ""]
        if rows:
            groups.append({"title": title, "rows": rows})
    names = []
    for item in entries(data.get("part_numbers_lcsc")):
        if item.get("product_name"):
            names.append({"label": str(item.get("part_number", "LCSC")), "value": readable(item["product_name"])})
    for item in manufacturers:
        names.append({"label": readable(item.get("manufacturer", "Manufacturer")), "value": readable(item.get("part_number", ""))})
    if names:
        groups.append({"title": "Collected names and ordering codes", "rows": names})
    notes = data.get("research_notes") or []
    notes = notes if isinstance(notes, list) else [notes]
    notes = [readable(note) for note in notes if note]
    if selection.get("compatibility_notes"):
        notes.insert(0, readable(selection["compatibility_notes"]))
    pins = entries(page.get("pins")) or [mapping(pin) for pin in mapping(data.get("pins")).values()]
    return {"tier": tier, "tier_label": tier_label, "manufacturer": readable(manufacturer), "mpn": readable(mpn),
            "summary": readable(data.get("lcsc_description") or data.get("description") or page.get("summary")),
            "links": links, "facts": facts, "groups": groups, "notes": notes, "pins": pins}


def is_label_svg(relative_path: str) -> bool:
    name = Path(relative_path).name.lower()
    return name.endswith(".svg") and (name.startswith("label") or name in {
        "working_svg_part_id.svg", "working_svg_md5_6_alpha.svg", "working_svg_bip_39_3_word.svg",
    })


def diagram_gallery(data: dict, files: list[dict]) -> list[dict]:
    available = {file["relative_path"] for file in files if file["is_image"]}
    page = mapping(data.get("part_page"))
    candidates = [mapping(page.get("main_image")), *entries(page.get("diagrams"))]
    # Older parts may not yet have a part_page manifest.
    for stem, title in (("working_svg_assembly_pins", "Assembly pinout"), ("working_svg_schematic", "Schematic"),
                        ("working_svg_dimensioned", "Dimensions"), ("kicad/kicad_symbol_unit_1", "KiCad symbol"),
                        ("kicad/kicad_footprint_machine_solder", "Machine solder footprint"),
                        ("kicad/kicad_footprint_hand_solder", "Hand solder footprint")):
        candidates.append({"title": title, "svg": f"data/{stem}.svg", "png": f"data/{stem}.png", "preview": f"data/{stem}_300.png"})
    gallery = []
    seen = set()
    for item in candidates:
        original = next((item.get(key) for key in ("svg", "png", "preview") if item.get(key) in available), None)
        if not original or original in seen:
            continue
        seen.add(original)
        gallery.append({"title": item.get("title", "Diagram"), "relative_path": original,
                        "preview": next((item.get(key) for key in ("preview", "png", "svg") if item.get(key) in available), original)})
    return gallery
