"""Helpers used explicitly by browser-verified family populate-extra entries.

This module does not import a catalogue or apply unreviewed matches globally.
"""
from copy import deepcopy
import json
from pathlib import Path
import re


def set_preferred_jlc(part, *, code, manufacturer, mpn, selection):
    """Set one verified purchasing identity, keeping previous alternatives.

    For generic passives this is a purchasing preference, not a new taxonomy.
    Exact manufacturer identities must not be changed to a different device.
    The caller is responsible for verifying electrical/physical compatibility.
    """
    if not re.fullmatch(r"C[0-9]+", code):
        raise ValueError("Use the JLCPCB/LCSC C-number, not an internal numeric ID")
    if not manufacturer or not mpn:
        raise ValueError("Verified manufacturer and full ordering MPN are required")
    if selection.get("tier") not in ("basic", "preferred_extended"):
        raise ValueError("House preference needs verified Basic or Preferred status")
    if not selection.get("official_url") or not selection.get("verified_on"):
        raise ValueError("Record official-page provenance before setting preference")
    exact = bool(part.get("taxonomy_14") or part.get("taxonomy_15"))
    if exact and part.get("part_number_manufacturer") not in (None, "", mpn):
        raise ValueError("Do not replace the manufacturer identity of an exact OOMP part")
    if exact and part.get("manufacturer") and part["manufacturer"].casefold() != manufacturer.casefold():
        raise ValueError("Resolve manufacturer spelling/identity explicitly for an exact part")

    supplier_choices = deepcopy(part.get("part_numbers_lcsc") or [])
    old_code = part.get("part_number_lcsc")
    if old_code and not any(x.get("part_number") == old_code for x in supplier_choices):
        supplier_choices.append({"part_number": old_code})
    chosen = next((x for x in supplier_choices if x.get("part_number") == code), {"part_number": code})
    part["part_numbers_lcsc"] = [chosen] + [x for x in supplier_choices if x.get("part_number") != code]

    identities = deepcopy(part.get("part_numbers_manufacturer") or [])
    old_mpn = part.get("part_number_manufacturer")
    old_identity = {"manufacturer": part.get("manufacturer", ""), "part_number": old_mpn}
    if old_mpn and old_identity not in identities:
        identities.append(old_identity)
    identity = {"manufacturer": manufacturer, "part_number": mpn}
    part["part_numbers_manufacturer"] = [identity] + [x for x in identities if x != identity]
    part.update(manufacturer=manufacturer, part_number_manufacturer=mpn,
                part_number_lcsc=code, part_number_jlcpcb=code,
                part_number_lcsc_url=f"https://www.lcsc.com/product-detail/{code}.html",
                part_number_jlcpcb_url=selection["official_url"],
                product_url=selection["official_url"], jlcpcb_selection=deepcopy(selection))


def apply_reviewed_jlc_choices(extras_dict, *, family):
    """Apply only explicitly promoted browser-reviewed identities for a family.

    The discovery catalogue is deliberately not read here. Each row in the
    reviewed registry comes from an individual browser record and page capture.
    """
    registry = Path(__file__).resolve().parent / "kicad_agents/jlc_house_parts/reviewed_choices.json"
    if not registry.is_file():
        return
    choices = json.loads(registry.read_text(encoding="utf-8"))
    seen_codes, seen_ids = set(), set()
    for choice in choices:
        code = choice["code"]
        part_id = choice["part_id"]
        if code in seen_codes or part_id in seen_ids:
            raise ValueError(f"Duplicate reviewed JLC choice: {code} / {part_id}")
        seen_codes.add(code)
        seen_ids.add(part_id)
        if choice["family"] != family or part_id not in extras_dict:
            continue
        set_preferred_jlc(extras_dict[part_id], code=code,
                          manufacturer=choice["manufacturer"], mpn=choice["mpn"],
                          selection=choice["selection"])
