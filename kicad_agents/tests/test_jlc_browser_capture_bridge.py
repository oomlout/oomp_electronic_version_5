"""Checks for the local browser-evidence handoff."""
import unittest

from kicad_agents.jlc_house_parts.browser_capture_bridge import validate_capture
from kicad_agents.jlc_house_parts.intake_from_capture import observation_from_capture


ROW = {
    "code": "C14857", "retired": False, "tier": "basic",
    "jlcpcb_url": "https://jlcpcb.com/partdetail/15529-CL21C470JBANNNC/C14857",
    "manufacturer": "Samsung Electro-Mechanics", "mpn": "CL21C470JBANNNC",
    "package": "0805", "ledger_id": "JLC_C14857",
}
CAPTURE = {
    "code": ROW["code"], "official_url": ROW["jlcpcb_url"],
    "manufacturer": ROW["manufacturer"], "mpn": ROW["mpn"],
    "package": ROW["package"], "tier_label": "Basic",
    "description": "47pF 50V C0G ±5% 0805 MLCC",
    "datasheet_url": "https://example.com/C14857.pdf",
    "specifications": {"Category": "Capacitors", "Capacitance": "47pF"},
    "visible_text": "CL21C470JBANNNC Basic C14857 47pF",
}


class BrowserCaptureBridgeTests(unittest.TestCase):
    def test_valid_capture_can_be_classified_without_inheriting_category_as_rating(self):
        capture = validate_capture(CAPTURE, {ROW["code"]: ROW})
        result = observation_from_capture(
            capture, ROW, part_id="electronic_capacitor_0805_47_pico_farad",
            family="capacitor", pin_count=2,
            compatibility_notes="Reviewed same value and package on the live page.",
            evidence_notes=["Browser page showed the complete Samsung MPN."])
        self.assertEqual(result["specifications"], {"Capacitance": "47pF"})
        self.assertIn("browser_staging/C14857.json", result["evidence_notes"][-1])

    def test_rejects_mismatched_identity_and_house_tier(self):
        for change in ({"mpn": "CL21C470JBANNND"}, {"tier_label": "Extended"},
                       {"code": ["C14857"]}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_capture({**CAPTURE, **change}, {ROW["code"]: ROW})


if __name__ == "__main__":
    unittest.main()
