import copy
from datetime import datetime, timezone
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
import yaml
from kicad_agents.jlc_house_parts_agent import build_intake_scaffold, check_record, check_intake_record, population
from kicad_agents.jlc_house_parts_agent import normalize_capture, generic_hint, code_options, read_json, SOURCE
from working_oomp_populate_jlc import set_preferred_jlc
from working_oomp_metadata import add_distributor_links


class HousePartsTests(unittest.TestCase):
    def test_population_has_unique_ids_for_house_part_matching(self):
        _, duplicates = population()
        self.assertEqual(duplicates, {})

    def test_scaffold_requires_browser_identity_and_explicit_decision(self):
        official = "https://jlcpcb.com/partdetail/Maker-MPN123/C123"
        row = dict(code="C123", ledger_id="JLC_C123", manufacturer="Maker", mpn="MPN123",
                   package="0603", tier="basic", jlcpcb_url=official)
        observed = dict(official_url=official, code="C123", manufacturer="Maker", mpn="MPN123",
                        package="0603", tier_label="Basic", description="100 ohm resistor",
                        captured_on=datetime.now(timezone.utc).date().isoformat(),
                        part_id="electronic_resistor_0603_100_ohm", family="resistor", pin_count=2,
                        compatibility_notes="Manually checked generic value and package",
                        evidence_notes=["Live Basic page checked"],
                        specifications={"Resistance": "100Ω"})
        capture, page, record = build_intake_scaffold(row, observed)
        self.assertIn("web_page_distributor_jlc.txt", capture)
        self.assertIn("Method: browser-observed", page)
        self.assertEqual(record["jlc_selection"]["ratings"], {"Resistance": "100Ω"})
        self.assertFalse(record["jlc_selection"]["footprint_checked"])
        with self.assertRaisesRegex(ValueError, "Observed mpn differs"):
            build_intake_scaffold(row, dict(observed, mpn="DIFFERENT"))
        with self.assertRaisesRegex(ValueError, "class differs"):
            build_intake_scaffold(row, dict(observed, tier_label="Extended"))

    def test_capture_covers_all_rows_without_retired_queue_items(self):
        rows = normalize_capture(read_json(SOURCE))
        self.assertEqual(len(rows), 2004)
        active = [r for r in rows if not r["retired"]]
        self.assertEqual(len(active), 1586)
        self.assertEqual(sum(r["tier"] == "basic" for r in active), 351)
        self.assertTrue(all(r["last_seen"] == "2026-09-18 08:22:22" for r in active))

    def test_bad_capture_fails_closed(self):
        rows = read_json(SOURCE)[:1]
        with self.assertRaises(ValueError): normalize_capture(rows + rows)
        rows[0]["cells"][1] = "extended"
        with self.assertRaises(ValueError): normalize_capture(rows)

    def test_resistance_scale_and_capacitance_hints(self):
        row = dict(package="0603", category="Resistors: Chip Resistor - Surface Mount", description="100mW 10kΩ 75V")
        self.assertEqual(generic_hint(row), "electronic_resistor_0603_10000_ohm")
        row["description"] = "0.22Ω 100mW"
        self.assertEqual(generic_hint(row), "electronic_resistor_0603_0_22_ohm")
        row.update(category="Capacitors: Multilayer Ceramic Capacitors MLCC - SMD/SMT", description="50V 0.1uF X7R")
        self.assertEqual(generic_hint(row), "electronic_capacitor_0603_100_nano_farad")
        row["package"] = "SOT-23"
        self.assertEqual(generic_hint(row), "")

    def test_preference_preserves_previous_options_and_is_idempotent(self):
        part = dict(taxonomy_2="resistor", taxonomy_3="0603", taxonomy_4="10000_ohm",
                    manufacturer="YAGEO", part_number_manufacturer="RC0603FR-0710KL", part_number_lcsc="C98220")
        selection = dict(tier="basic", official_url="https://jlcpcb.com/partdetail/C25804", verified_on="2026-09-24")
        args = dict(code="C25804", manufacturer="UNI-ROYAL", mpn="0603WAF1002T5E", selection=selection)
        set_preferred_jlc(part, **args)
        first = copy.deepcopy(part)
        set_preferred_jlc(part, **args)
        self.assertEqual(part, first)
        self.assertEqual(code_options(part), {"C25804", "C98220"})
        self.assertEqual(part["taxonomy_4"], "10000_ohm")
        self.assertEqual(part["part_number_jlcpcb"], part["part_number_lcsc"])
        add_distributor_links(part)
        self.assertTrue(any(x["key"] == "jlcpcb" and x["part_number"] == "C25804" for x in part["distributors"]))

    def test_exact_identity_cannot_be_silently_replaced(self):
        part = dict(taxonomy_14="vendor", taxonomy_15="device_a", part_number_manufacturer="A")
        with self.assertRaises(ValueError):
            set_preferred_jlc(part, code="C123", manufacturer="Vendor", mpn="B",
                              selection=dict(tier="basic", official_url="https://jlcpcb.com", verified_on="2026-09-24"))
        self.assertEqual(part["part_number_manufacturer"], "A")

    def test_gate_rejects_unverified_identity_even_if_component_check_passes(self):
        record = dict(ledger_id="JLC_C123", part_id="electronic_test", pin_count=2,
                      datasheet_required=True, research=dict(lcsc_part_number="C123", manufacturer_part_number="MPN"),
                      jlc_selection={})
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "record.yaml"
            path.write_text(yaml.safe_dump(record), encoding="utf-8")
            with patch("kicad_agents.component_addition_agent.validate_implementation", return_value=dict(status="pass", errors=[], part_id="electronic_test")), patch("kicad_agents.jlc_house_parts_agent.population", return_value=({}, {})):
                result = check_record(dict(ledger_id="JLC_C123", code="C123", mpn="MPN"), path)
        self.assertEqual(result["status"], "fail")
        self.assertTrue(any("Official" in error for error in result["errors"]))

    def test_intake_accepts_saved_page_and_population_without_datasheet(self):
        code, mpn, maker, part_id = "C123", "MPN-123", "Maker", "electronic_test"
        official = "https://jlcpcb.com/partdetail/Maker-MPN123/C123"
        selection = dict(verified_on=datetime.now(timezone.utc).date().isoformat(),
                         official_url=official, tier="basic", compatibility_notes="Exact identity")
        row = dict(ledger_id="JLC_C123", code=code, mpn=mpn, manufacturer=maker)
        part = dict(part_number_lcsc=code, part_number_jlcpcb=code,
                    part_number_manufacturer=mpn, manufacturer=maker, jlcpcb_selection=selection)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            capture = root / "web_page_distributor_jlc.txt"
            capture.write_text(f"Source URL: {official}\n{code} {mpn} {maker} Basic\n", encoding="utf-8")
            record = dict(ledger_id="JLC_C123", family="resistor", part_id=part_id, datasheet_required=True,
                          research=dict(lcsc_part_number=code, manufacturer_part_number=mpn,
                                        manufacturer=maker, browser_sources=[official],
                                        webpage_capture=capture.name, evidence_notes=["Exact identity"]),
                          jlc_selection=selection)
            path = root / "record.yaml"
            path.write_text(yaml.safe_dump(record), encoding="utf-8")
            with patch("kicad_agents.jlc_house_parts_agent.ROOT", root), patch(
                "kicad_agents.jlc_house_parts_agent.population", return_value=({part_id: part}, {})):
                self.assertEqual(check_intake_record(row, path)["status"], "pass")
                capture.unlink()
                result = check_intake_record(row, path)
                self.assertEqual(result["status"], "fail")
                self.assertTrue(any("webpage" in error for error in result["errors"]))

    def test_promotion_gate_allows_old_supplier_before_verified_choice_is_applied(self):
        code, mpn, maker, part_id = "C123", "MPN-123", "Maker", "electronic_test"
        official = "https://jlcpcb.com/partdetail/Maker-MPN123/C123"
        selection = dict(verified_on=datetime.now(timezone.utc).date().isoformat(),
                         official_url=official, tier="basic", compatibility_notes="Verified value and size")
        row = dict(ledger_id="JLC_C123", code=code, mpn=mpn, manufacturer=maker)
        part = dict(part_number_lcsc="C999", part_number_manufacturer="OLD", manufacturer="Old")
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "page.txt").write_text(f"{official} {code} {mpn} {maker}", encoding="utf-8")
            record = dict(ledger_id="JLC_C123", family="resistor", part_id=part_id,
                          research=dict(lcsc_part_number=code, manufacturer_part_number=mpn,
                                        manufacturer=maker, browser_sources=[official],
                                        webpage_capture="page.txt", evidence_notes=["Browser verified"]),
                          jlc_selection=selection)
            path = root / "record.yaml"
            path.write_text(yaml.safe_dump(record), encoding="utf-8")
            with patch("kicad_agents.jlc_house_parts_agent.ROOT", root), patch(
                "kicad_agents.jlc_house_parts_agent.population", return_value=({part_id: part}, {})):
                self.assertEqual(check_intake_record(row, path, population_required=False)["status"], "pass")
                self.assertEqual(check_intake_record(row, path)["status"], "fail")

    def test_weaker_house_choices_keep_generic_preferences(self):
        parts, duplicates = population()
        generic_id = "electronic_capacitor_0603_4_7_micro_farad"
        rated_id = generic_id + "_16_volt"
        self.assertNotIn(generic_id, duplicates)
        self.assertNotIn(rated_id, duplicates)
        self.assertEqual(parts[generic_id]["part_number_lcsc"], "C69335")
        self.assertEqual(parts[rated_id]["part_number_jlcpcb"], "C19666")
        self.assertEqual(parts[rated_id]["generic_oomp_id"], generic_id)
        self.assertEqual(parts[rated_id]["electrical"]["rated_voltage"], "16 V")
        generic_id = "electronic_capacitor_0402_4_7_micro_farad"
        rated_id = generic_id + "_10_volt_20_percent"
        self.assertNotIn(generic_id, duplicates)
        self.assertNotIn(rated_id, duplicates)
        self.assertEqual(parts[generic_id]["part_number_lcsc"], "C368809")
        self.assertEqual(parts[rated_id]["part_number_jlcpcb"], "C23733")
        self.assertEqual(parts[rated_id]["generic_oomp_id"], generic_id)
        self.assertEqual(parts[rated_id]["electrical"]["tolerance"], "+/-20%")

        generic_id = "electronic_capacitor_0805_10_micro_farad"
        rated_id = generic_id + "_50_volt"
        self.assertNotIn(generic_id, duplicates)
        self.assertNotIn(rated_id, duplicates)
        self.assertEqual(parts[generic_id]["part_number_jlcpcb"], "C15850")
        self.assertEqual(parts[rated_id]["part_number_jlcpcb"], "C440198")
        self.assertEqual(parts[rated_id]["generic_oomp_id"], generic_id)
        self.assertEqual(parts[rated_id]["electrical"]["rated_voltage"], "50 V")
        generic_id = "electronic_capacitor_0402_100_nano_farad"
        rated_id = generic_id + "_50_volt"
        self.assertNotIn(generic_id, duplicates)
        self.assertNotIn(rated_id, duplicates)
        self.assertEqual(parts[generic_id]["part_number_jlcpcb"], "C1525")
        self.assertEqual(parts[rated_id]["part_number_jlcpcb"], "C307331")
        self.assertEqual(parts[rated_id]["generic_oomp_id"], generic_id)
        self.assertEqual(parts[rated_id]["electrical"]["rated_voltage"], "50 V")
        generic_id = "electronic_capacitor_0603_10_micro_farad"
        rated_id = generic_id + "_25_volt_20_percent"
        self.assertNotIn(generic_id, duplicates)
        self.assertNotIn(rated_id, duplicates)
        self.assertEqual(parts[generic_id]["part_number_lcsc"], "C19702")
        self.assertEqual(parts[rated_id]["part_number_jlcpcb"], "C96446")
        self.assertEqual(parts[rated_id]["generic_oomp_id"], generic_id)
        self.assertEqual(parts[rated_id]["electrical"]["rated_voltage"], "25 V")
        self.assertEqual(parts[rated_id]["electrical"]["tolerance"], "+/-20%")

    def test_crystal_esr_variant_preserves_generic_choice(self):
        parts, duplicates = population()
        generic_id = "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf"
        variant_id = generic_id + "_80_ohm_esr"
        self.assertNotIn(generic_id, duplicates)
        self.assertNotIn(variant_id, duplicates)
        self.assertEqual(parts[generic_id]["part_number_lcsc"], "C133334")
        self.assertEqual(parts[variant_id]["part_number_jlcpcb"], "C9002")
        self.assertEqual(parts[variant_id]["generic_oomp_id"], generic_id)
        self.assertEqual(parts[variant_id]["electrical"]["equivalent_series_resistance"], "80 ohm")


if __name__ == "__main__":
    unittest.main()
