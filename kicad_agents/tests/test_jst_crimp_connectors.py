"""Keep JST library identities, variant geometry and cable mates consistent."""
from collections import Counter
import json
from pathlib import Path

from kicad_agents.component_addition_agent import _load_populated_definition
from kicad_agents.jst_crimp_batch import evidence_record
from oomp_populate_helper import build_oomp_id
from working_oomp_populate_connector import main as populate
from working_oomp_populate_connector_jst_cable_data import CONTACTS, HOUSINGS, PARTS, PDF_OWNERS
from working_oomp_populate_connector_ph_data import PARTS as PH_HEADERS


def test_catalogue_scope_and_order_codes():
    assert Counter(row["family"] for row in HOUSINGS) == {"sh": 30, "gh": 14, "ph": 15, "xh": 19}
    assert Counter(row["family"] for row in CONTACTS) == {"sh": 1, "gh": 1, "ph": 3, "xh": 3}
    assert len({row["mpn"] for row in PARTS}) == len({row["id"] for row in PARTS}) == len(PARTS)
    by_mpn = {row["mpn"]: row for row in PARTS}
    assert by_mpn["SHR-02V-S-B"]["dimensions_mm"]["length"] == 5
    assert by_mpn["SHR-02V-S"]["dimensions_mm"]["length"] == 3
    assert by_mpn["GHR-15V-S"]["dimensions_mm"]["length"] == 20
    assert by_mpn["XHP-2(10.0)-U"]["filled_cavities"] == 3
    assert by_mpn["XHP-2(10.0)-U"]["pitch_mm"] == 10
    assert by_mpn["XHP-6(5.0)-U"]["filled_cavities"] == 5
    assert by_mpn["XHP-6(5.0)-U"]["pitch_mm"] == 5


def test_reciprocal_mates_use_active_cavities_and_family():
    by_id = {row["id"]: row for row in PARTS}
    for housing in HOUSINGS:
        assert not housing["pins"]
        assert housing["related_parts"]
        for mate in housing["related_parts"]:
            contact = by_id[mate["oomp_id"]]
            assert contact["family"] == housing["family"]
            assert mate["quantity"] == housing["positions"]
            assert any(item["oomp_id"] == housing["id"] for item in contact["related_parts"])
    for row in [CONTACTS[0], HOUSINGS[0], HOUSINGS[-1]]:
        definition = _load_populated_definition(evidence_record(row))
        assert definition["kicad"]["applicability"] == "not_applicable"
        assert definition["dimension_reference"]["pdf_page"] == row["pdf_page"]
        assert definition.get("oomp_datasheet_common_with", row["id"]) == PDF_OWNERS[row["family"]]


def test_ph_migration_preserves_exact_boomele_selection():
    root = Path(__file__).resolve().parents[2]
    migration = json.loads((root / "migrations/ph_header_ids.json").read_text(encoding="utf-8"))
    assert {row["old"]: row["new"] for row in migration} == {row["old"]: row["id"] for row in PH_HEADERS}
    definitions = []
    populate(options=definitions)
    ids = Counter(build_oomp_id({"taxonomy_1": "electronic", **row}) for row in definitions)
    for row in PH_HEADERS:
        assert row["old"] not in ids and ids[row["id"]] == 1
        definition = _load_populated_definition({"family": "connector", "part_id": row["id"]})
        assert definition["part_number_manufacturer"] == row["mpn"]
        assert definition["part_number_jlcpcb"] == row["code"]
        assert definition["manufacturer"].startswith("BOOMELE")
