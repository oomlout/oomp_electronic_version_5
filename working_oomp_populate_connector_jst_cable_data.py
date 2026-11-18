"""Natural-white JST SH, GH, PH and XH cable parts from the JST family drawings."""
from copy import deepcopy
from pathlib import Path
import re

from oomp_populate_helper import build_oomp_id
from working_oomp_populate_connector_crimp_data import MODEL_ASSETS


FAMILIES = {
    # Pitch, manufacturer series number, housing plastic and document owner.
    "sh": (1, 231, "PBT", "SHR-02V-S-B"),
    "gh": (1.25, 105, "PBT", "GHR-02V-S"),
    "ph": (2, 199, "PA", "PHR-2"),
    "xh": (2.5, 277, "PA 6", "XHP-1"),
}
SOURCE_ROOT = Path(__file__).resolve().parent / "parts_source"


def token(value):
    return re.sub(r"[^a-z0-9]+", "_", str(value).lower()).strip("_")


def _row(family, mpn, kind, positions, style, dimensions, page, pitch=None, **qualifiers):
    family_pitch, series, _, _ = FAMILIES[family]
    pitch = family_pitch if pitch is None else pitch
    taxonomy = {
        "taxonomy_2": "connector", "taxonomy_3": f"jst_{family}",
        "taxonomy_4": f"{token(pitch)}_mm_pitch", "taxonomy_5": kind,
        "taxonomy_6": f"{positions}_pin", "taxonomy_7": style,
        "taxonomy_14": "jst", "taxonomy_15": token(mpn), **qualifiers,
    }
    return {
        "id": build_oomp_id({"taxonomy_1": "electronic", **taxonomy}),
        "family": family, "mpn": mpn, "taxonomy": taxonomy, "positions": positions,
        "pitch_mm": pitch, "pdf_page": page,
        "product_url": f"https://www.jst-mfg.com/product/index.php?lang=2&series={series}",
        "datasheet_url": f"https://www.jst-mfg.com/product/pdf/eng/e{family.upper()}.pdf",
        "dimensions_mm": dict(zip(("length", "width", "height"), dimensions)),
        "related_parts": [],
    }


def _contact(family, mpn, awg, insulation, dimensions, low_force=False):
    small, large = awg
    gauge = f"{small}–{large} AWG"
    pitch = FAMILIES[family][0]
    row = _row(family, mpn, "crimp", 1, "socket", dimensions, 3 if family == "xh" else 2,
               taxonomy_8=f"{large}_to_{small}_awg", taxonomy_9="tin")
    notes = "Low insertion force" if low_force else "Standard insertion force"
    row.update(
        role="cable_crimp_contact",
        name=f"JST {family.upper()} crimp socket {gauge}, tin ({mpn})",
        pins={"pin_1": {"number": "1", "name": "contact", "type": "passive"}},
        details={
            "component_role": "Female crimp contact with one conductive terminal",
            "series": f"JST {family.upper()}", "pitch": f"{pitch} mm (housing pitch)",
            "wire_size": gauge, "insulation_outer_diameter": f"{insulation[0]}–{insulation[1]} mm",
            "contact_material": "Phosphor bronze" if family == "xh" else "Copper alloy",
            "contact_finish": "Tin", "packaging": "Reel", "insertion_force": notes,
        },
        label={"primary": "CRIMP SOCKET", "details": [
            f"JST {family.upper()} / {pitch} mm", f"{gauge} / TIN", mpn,
        ]},
        dimension_note="Nominal labelled drawing spans. The reference envelope omits small projecting lances and burrs.",
    )
    if family == "gh":
        row["dimension_note"] = ("The drawing labels the 4.8 mm length, 0.8 mm socket width and 0.55 mm "
                                 "socket height. The open wing height is a 1.4 mm reference estimate "
                                 "from the side view.")
    return row


def _housing(family, mpn, count, dimensions, *, protrusions=None, pitch=None, filled=0):
    qualifiers = {}
    if protrusions is not None:
        qualifiers["taxonomy_8"] = "with_protrusions" if protrusions else "without_protrusions"
    if filled:
        qualifiers["taxonomy_8"] = "plugged_cavities"
    page = {"sh": 2, "gh": 3, "ph": 3, "xh": 4}[family]
    row = _row(family, mpn, "housing", count, "white", dimensions, page, pitch, **qualifiers)
    pitch = row["pitch_mm"]
    details = {
        "component_role": "Empty insulating housing with contacts supplied separately",
        "series": f"JST {family.upper()}", "pitch": f"{pitch} mm",
        "positions": f"{count}, single row", "housing_color": "Natural (white)",
        "housing_material": FAMILIES[family][2], "contacts_required": f"{count}, sold separately",
    }
    if protrusions is not None:
        details["end_protrusions"] = "Present" if protrusions else "Absent"
    if family == "gh":
        details["locking_style"] = "Positive latch, standard natural-white keying"
    if filled:
        details["filled_cavities"] = f"{filled} resin-filled positions on the 2.5 mm moulding grid"
    row.update(
        role="cable_housing", pins={}, details=details, protrusions=protrusions,
        filled_cavities=filled,
        name=f"JST {family.upper()} {pitch} mm {count}-position white housing ({mpn})",
        label={"primary": f"{count}-POS HOUSING", "details": [
            f"JST {family.upper()} / {pitch} mm / WHITE",
            f"Empty: needs {count} crimp contacts" if count > 1 else "Empty: needs 1 crimp contact",
            mpn,
        ]},
        dimension_note="Nominal along-row length from dimension B. Reference geometry simplifies retention and edge details.",
    )
    return row


CONTACTS = [
    _contact("sh", "SSH-003T-P0.2-H", (32, 28), (0.4, 0.8), (3.9, 0.8, 1.35)),
    _contact("gh", "SSHL-002T-P0.2", (30, 26), (0.76, 1.0), (4.8, 0.8, 1.4), low_force=True),
    _contact("ph", "SPH-004T-P0.5S", (32, 28), (0.5, 0.9), (5.7, 1.5, 2.08)),
    _contact("ph", "SPH-002T-P0.5S", (30, 24), (0.8, 1.5), (5.7, 1.5, 2.08)),
    _contact("ph", "SPH-002T-P0.5L", (28, 24), (0.8, 1.5), (5.7, 1.5, 2.08), low_force=True),
    _contact("xh", "SXH-001T-P0.6N", (26, 22), (1.3, 1.9), (5.6, 1.9, 2.35), low_force=True),
    _contact("xh", "SXH-002T-P0.6", (30, 26), (0.9, 1.3), (6.1, 1.95, 2.4)),
    _contact("xh", "SXH-001T-P0.6", (28, 22), (0.9, 1.9), (6.1, 1.95, 2.4)),
]

HOUSINGS = [
    *(_housing("sh", f"SHR-{n:02}V-S-B", n, (n + 3, 5, 2.8), protrusions=True)
      for n in (*range(2, 17), 20)),
    *(_housing("sh", f"SHR-{n:02}V-S", n, (n + 1, 5, 2.8), protrusions=False)
      for n in range(2, 16)),
    *(_housing("gh", f"GHR-{n:02}V-S", n, (1.25 * (n + 1), 5.7, 4.15))
      for n in range(2, 16)),
    *(_housing("ph", f"PHR-{n}", n, (round(2 * n + 1.8, 2), 6.85, 4.5))
      for n in range(2, 17)),
    *(_housing("xh", f"XHP-{n}", n, (round(2.5 * n + 2.3, 2), 7.75, 5.7))
      for n in (*range(1, 17), 20)),
    _housing("xh", "XHP-2(10.0)-U", 2, (14.8, 7.75, 5.7), pitch=10, filled=3),
    _housing("xh", "XHP-6(5.0)-U", 6, (29.8, 7.75, 5.7), pitch=5, filled=5),
]
PARTS = CONTACTS + HOUSINGS
PDF_OWNERS = {row["family"]: row["id"] for row in HOUSINGS
              if row["mpn"] == FAMILIES[row["family"]][3]}

for housing in HOUSINGS:
    for contact in CONTACTS:
        if housing["family"] != contact["family"]:
            continue
        housing["related_parts"].append({
            "relationship": "Contact option", "oomp_id": contact["id"], "name": contact["name"],
            "quantity": housing["positions"], "evidence_url": housing["datasheet_url"],
            "notes": "Quantity fills the active cavities. Select the contact for the wire gauge and insulation diameter.",
        })
        contact["related_parts"].append({
            "relationship": "Fits housing", "oomp_id": housing["id"], "name": housing["name"],
            "evidence_url": housing["datasheet_url"],
            "notes": f"Order {housing['positions']} contacts separately to fill the housing.",
        })


def apply_extras(extras_dict):
    for row in PARTS:
        if row["id"] not in extras_dict:
            continue
        part = extras_dict[row["id"]]
        for field in ("header_dimensions_mm", "generic_match"):
            part.pop(field, None)
        length, width, height = row["dimensions_mm"].values()
        part.update(
            name_short=row["name"], name_readable_override=row["name"], manufacturer="JST",
            part_number_manufacturer=row["mpn"], product_url=row["product_url"],
            datasheet_url=row["datasheet_url"], component_role=row["role"], pcb_mountable=False,
            diagram_name=f"JST {row['family'].upper()} {row['mpn']}",
            dimensions_mm=deepcopy(row["dimensions_mm"]), pins=deepcopy(row["pins"]),
            connector_details=deepcopy(row["details"]), related_parts=deepcopy(row["related_parts"]),
            label_drawer_overrides=deepcopy(row["label"]),
            drawing_note="Nominal drawing spans. See the manufacturer's drawing for feature dimensions and crimp tooling.",
            dimension_reference={
                "manufacturer": "JST", "product_url": row["product_url"],
                "datasheet_url": row["datasheet_url"], "pdf_page": row["pdf_page"],
                "checked_on": "2026-11-16", "notes": row["dimension_note"],
            },
            package_drawing={
                "overall": [length, width], "body": [length, width], "pins": [],
                "side": {"overall": [width, height], "body": [width, height], "pins": []},
            },
            kicad={
                "applicability": "not_applicable", "symbol": "", "machine_solder": "",
                "hand_solder": "", "allow_project_fallback": False,
                "reason": "Cable-assembly component without board-mounted pads.",
            },
        )
        owner = PDF_OWNERS[row["family"]]
        if owner != row["id"]:
            part["oomp_datasheet_common_with"] = owner
        assets = ["datasheet.pdf"] if (SOURCE_ROOT / owner / "datasheet.pdf").is_file() else []
        if all((SOURCE_ROOT / row["id"] / name).is_file() for name in MODEL_ASSETS):
            assets.extend(MODEL_ASSETS)
            part["model_3d"] = dict(zip(("step", "render", "provenance"),
                                       (f"data/{name}" for name in MODEL_ASSETS)))
        part["file_copy"] = [
            {"file_source": f"parts_source/{row['id']}/{name}", "file_destination": name}
            for name in assets
        ]
