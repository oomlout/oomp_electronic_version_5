"""Regression checks for the duplicate-listing repairs, without filesystem writes."""

from copy import deepcopy
from unittest.mock import patch

import pytest
import working_oomp_metadata as metadata
import working_oomp_populate_connector as connectors
import working_oomp_populate_connector_extra as connector_extras
import working_oomp_populate_lcsc_extra as lcsc
import working_oomp_populate_lcsc_research_data as research
import working_oomp_populate_resistor as resistors
from oomp_populate_helper import build_oomp_id


def test_rejected_research_never_supplies_a_purchase_identity():
    rejected = {key: {} for key, row in research.LCSC_RESEARCH.items()
                if row.get("research_status") == "rejected"}
    assert len(rejected) == 35
    lcsc.main(extras_dict=rejected)
    for part in rejected.values():
        assert not part.get("part_number_lcsc")
        assert not part.get("part_number_manufacturer")
        assert part["lcsc_research_status"] == "rejected"


@pytest.mark.parametrize("change", [
    {"manufacturer": "Other maker"},
    {"part_number_manufacturer": "B3B-XH-A"},
    {"lcsc_description": "ESD DIODE DFN1006-2"},
])
def test_conflicting_listing_is_rejected_before_supplier_fields_are_filled(change):
    part = {"taxonomy_2": "connector", "manufacturer": "JST", "part_number_manufacturer": "B2B-XH-A"}
    row = {**part, "part_number_lcsc": "C_TEST", **change}
    with patch.object(research, "LCSC_RESEARCH", {"test": row}):
        lcsc.main(extras_dict={"test": part})
    assert not part.get("part_number_lcsc")
    assert part["part_number_manufacturer"] == "B2B-XH-A"


def test_matching_listing_and_explicit_variant_can_be_used():
    part = {"manufacturer": "JST", "part_number_manufacturer": "B2B-XH-A"}
    row = {**part, "part_number_lcsc": "C_TEST"}
    with patch.object(research, "LCSC_RESEARCH", {"test": row}):
        lcsc.main(extras_dict={"test": part})
    assert part["part_number_lcsc"] == "C_TEST"
    assert lcsc.rejection_reason({**part, "procurement_variant": "black"}, row)
    assert not lcsc.rejection_reason({**part, "procurement_variant": "black"}, {**row, "procurement_variant": "black"})


def populated_connectors():
    rows = []
    connectors.main(options=rows)
    parts = {build_oomp_id({"taxonomy_1": "electronic", **row}): deepcopy(row) for row in rows}
    connector_extras.main(extras_dict=parts)
    lcsc.main(extras_dict=parts)
    return parts


def test_black_qwiic_purchases_use_sparkfun_and_keep_standard_jst_separate():
    parts = populated_connectors()
    for orientation, mpn, sku, standard_code in [
        ("right_angle", "sm04b_srss_tb", "PRT-14417", "C160404"),
        ("vertical", "bm04b_srss_tb", "PRT-16766", "C160390"),
    ]:
        prefix = f"electronic_connector_jst_sh_1_mm_pitch_surface_mount_{orientation}_4_pin_"
        black = parts[prefix + "black_jst_" + mpn]
        assert not black.get("part_number_lcsc")
        assert black["part_number_sparkfun"] == sku
        metadata.add_distributor_links(black)
        assert "Black Qwiic" in metadata.readable_name(black)
        assert [d["key"] for d in black["distributors"]] == ["sparkfun"]
        assert black["distributors"][0]["url"] == black["product_url"]
        assert parts[prefix + "jst_" + mpn]["part_number_lcsc"] == standard_code


def test_terminal_catalogue_links_are_reciprocal_without_claiming_compatibility():
    parts = populated_connectors()
    linked = {key: part for key, part in parts.items() if part.get("catalogue_relationships")}
    assert len(linked) == 22
    for key, part in linked.items():
        link = part["catalogue_relationships"][0]
        assert link["compatibility_verified"] is False
        target = linked[link["oomp_id"]]
        assert target["catalogue_relationships"][0]["oomp_id"] == key
        assert target["catalogue_role"] != part["catalogue_role"]


def test_restored_resistors_are_populated_exactly_once():
    rows = []
    resistors.main(options=rows)
    ids = [build_oomp_id({"taxonomy_1": "electronic", **r}) for r in rows]
    assert len(ids) == len(set(ids))
    for package in ("0201", "quarter_watt_through_hole"):
        assert ids.count(f"electronic_resistor_{package}_2000_ohm") == 1


def test_web_details_show_procurement_and_catalogue_relationship_limitations():
    from webserver.services.electronics import component_details
    details = component_details({
        "procurement_notes": "No verified supplier assigned.",
        "catalogue_relationships": [{"oomp_id": "electronic_example", "relationship": "Named product candidate",
                                     "notes": "Dimensions must be verified.", "compatibility_verified": False}],
    })
    assert "No verified supplier assigned." in details["notes"]
    assert "Dimensions must be verified." in details["notes"]
    assert details["links"][0]["label"] == "Named product candidate"
