"""Write a concise, human-editable review list for uncertain BOM matches."""

from __future__ import annotations

import json
from pathlib import Path

import yaml


# Notes from the quick LCSC browser pass.  Add or edit one row when a human
# confirms an exact manufacturer suffix; the generated list stays mechanical.
SEARCH_NOTES = {
    "1N4148WT": "Search results include nearby 1N4148W/WT suffixes from several manufacturers; choose the exact fitted maker.",
    "BAS40T-05": "The closest prominent LCSC result was BAS40W-05, not the exact T suffix.",
    "BCM857": "The bare value omits an order suffix; the first LCSC result was a different DFN package.",
    "LMV321": "Generic value has many manufacturers and order suffixes.",
    "LMV321A": "Generic value has many manufacturers and order suffixes.",
    "LMV324": "Generic value has many manufacturers and order suffixes.",
    "LMV331": "Generic value has many manufacturers and order suffixes.",
    "MMDT3906": "Exact base number exists from multiple manufacturers; select the fitted manufacturer.",
    "SI2301": "The leading search result is SOT-23 while this PCB uses SOT-523; suffix/manufacturer must be checked.",
    "MT29F1G01ABAFDWB": "LCSC C2905686 is MT29F1G01ABAFDWB-IT:F; confirm that temperature/order suffix.",
    "SK6812-side-a_b": "The board footprint accepts A/B orientation while LCSC C5378721 is SK6812SIDE-A.",
    "12Mhz": "Matched to the generic 3225 12 MHz / 20 pF OOMP part; confirm load capacitance.",
    "1.5A": "Inductor/ferrite value only states current; impedance and manufacturer part number are missing.",
    "SW_SPST": "Generic switch value; the PTS810 footprint alone does not identify the fitted height/force suffix.",
    "4P_button_sw": "GT-TC026X-HXXX-LX is a family placeholder with unresolved height and force suffixes.",
    "TFT_20_QT200H1201": "Display module has no supplier or exact manufacturer field in the board.",
    "Conn_01x03": "Generic 2.54 mm socket; manufacturer and height are unspecified.",
}


def write_lcsc_review(project_data, output_directory):
    output_directory = Path(output_directory).resolve()
    grouped = {}
    for component in project_data.get("components", []):
        pcb = component.get("pcb") or {}
        if pcb == {} or pcb.get("exclude_from_bom", False):
            continue
        reference = str(component.get("reference") or "")
        value = str(pcb.get("value") or "")
        if (
            value.upper() == "DNF"
            or reference.upper().startswith("FID")
            or reference.upper().startswith("H")
            or reference.upper().startswith("SJ")
            or pcb.get("is_mounting_hole", False)
        ):
            continue
        if reference.lower().startswith("logo"):
            continue
        match = component.get("oomp") or {}
        needs_review = not bool(match.get("oomp_id")) or value in SEARCH_NOTES
        if not needs_review:
            continue
        key = (value, str(pcb.get("library_id") or ""))
        if key not in grouped:
            properties = pcb.get("properties") or {}
            grouped[key] = {
                "value": value,
                "footprint": key[1],
                "references": [],
                "historical_supplier_link": str(properties.get("Supplier") or "").strip(),
                "current_oomp_match": str(match.get("oomp_id") or ""),
                "review_reason": SEARCH_NOTES.get(value, "No high-confidence OOMP/LCSC identity was found from the available value and footprint."),
                "resolution": "",
            }
        grouped[key]["references"].append(reference)

    items = list(grouped.values())
    items.sort(key=lambda item: item["references"][0] if item["references"] else item["value"])
    review = {
        "format_version": 1,
        "help": "Fill resolution after checking the fitted BOM or purchase records, then move confirmed mappings into working_oomp_populate_project.py and the appropriate populate-extra file.",
        "item_count": len(items),
        "items": items,
    }
    output_directory.mkdir(parents=True, exist_ok=True)
    with (output_directory / "lcsc_review.json").open("w", encoding="utf-8") as output_file:
        json.dump(review, output_file, indent=2, ensure_ascii=False)
        output_file.write("\n")
    with (output_directory / "lcsc_review.yaml").open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(review, output_file, sort_keys=False, allow_unicode=True)
    return review
