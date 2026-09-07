import copy
import tempfile
import unittest
from pathlib import Path

from kicad_agents.project_html_agent import _component_record, _lcsc_part_number


class ExplorerDistributorTests(unittest.TestCase):
    def setUp(self):
        self.component = {
            "reference": "U1",
            "oomp": {"status": "matched", "oomp_id": "electronic_test"},
            "pcb": {"properties": {"LCSC": "C123"}},
        }

    def test_catalogue_number_precedes_bom_number(self):
        self.assertEqual(_lcsc_part_number(self.component, {"part_number_lcsc": " c456 "}), "C456")

    def test_distributor_metadata_and_bom_fallbacks(self):
        self.assertEqual(_lcsc_part_number(self.component, {"distributors": [{"key": "lcsc", "part_number": "C789"}]}), "C789")
        self.assertEqual(_lcsc_part_number(self.component, {}), "C123")
        self.component["pcb"]["properties"] = {}
        self.component["schematic"] = {"units": [{"properties": {"LCSC Part #": "456"}}]}
        self.assertEqual(_lcsc_part_number(self.component, {}), "C456")

    def test_unmatched_and_invalid_numbers_do_not_create_links(self):
        for status in ["unmatched", "ambiguous", "not_applicable"]:
            component = copy.deepcopy(self.component)
            component["oomp"]["status"] = status
            self.assertEqual(_lcsc_part_number(component, {"part_number_lcsc": "C456"}), "")
        self.component["pcb"]["properties"] = {}
        for value in ["", "-", "None", "javascript:alert(1)", "C123\" onclick=\"bad", "C12/C34"]:
            self.assertEqual(_lcsc_part_number(self.component, {"part_number_lcsc": value}), "")

    def test_record_embeds_canonical_link(self):
        with tempfile.TemporaryDirectory() as directory:
            record = _component_record(self.component, Path(directory), {"part_number_lcsc": "C456"})
        self.assertEqual(record["lcsc_part_number"], "C456")
        self.assertEqual(record["lcsc_url"], "https://www.lcsc.com/product-detail/C456.html")
