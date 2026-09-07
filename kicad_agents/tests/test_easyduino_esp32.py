import copy
import unittest
from unittest.mock import patch

import working_svg
import working_oomp_populate_project
import working_oomp_populate_ic
import working_oomp_populate_diode
import working_oomp_populate_transistor
import working_oomp_populate_connector
import working_oomp_populate_switch
import working_oomp_populate_extra_detail
from oomp_populate_helper import build_oomp_id
from kicad_agents.oomp_matching_agent import match_component
from kicad_agents.kicad_library_agent import select_sources


class Esp32PopulationTests(unittest.TestCase):
    def setUp(self):
        projects = []
        working_oomp_populate_project.main(options=projects)
        self.project = next(p for p in projects if p.get("project_board") == "esp32")
        options = []
        for module in [working_oomp_populate_ic, working_oomp_populate_diode,
                       working_oomp_populate_transistor, working_oomp_populate_connector,
                       working_oomp_populate_switch]:
            module.main(options=options)
        for part in options:
            part["taxonomy_1"] = "electronic"
        working_oomp_populate_extra_detail.main(extras=options)
        self.parts = {build_oomp_id(part): part for part in options}

    def test_project_and_explicit_conflicts(self):
        self.assertEqual(build_oomp_id(self.project), "oomp_project_github_hanqaqa_easyduino_esp32_current")
        self.assertEqual(self.project["project_file_path"], "ESP32/Easyduino_ESP32")
        self.assertEqual(set(self.project["project_match_blocked"]), {"U1", "U4"})
        self.assertNotIn("U1", self.project["project_match_overrides"])
        component = {"reference": "U1", "pcb": {"value": "CP2102N", "library_id": "Interface_USB:CP2102N"}}
        result = match_component(None, component, blocked=self.project["project_match_blocked"])
        self.assertFalse(result["accepted"])
        self.assertIn("CP2102-GMR", result["reasons"][0])

    def test_new_package_rows_are_physical_uniform_scale(self):
        for reference in ["D1", "J1", "Q1", "SW1", "U2", "U3"]:
            with self.subTest(reference=reference):
                part = copy.deepcopy(self.parts[self.project["project_match_overrides"][reference]])
                self.assertTrue(part["part_number_manufacturer"])
                self.assertTrue(part["part_number_lcsc"].startswith("C"))
                geometry = part["package_drawing"]
                dimensions = working_svg._get_assembly_drawing_dimensions(part)
                with patch.object(working_svg.opsvg, "se"):
                    working_svg._add_component_outline(part, dimensions["outline_width"], dimensions["outline_height"])
                self.assertEqual(len(part["diagram_pin_positions"]), len(geometry["pins"]))
                for drawn, row in zip(part["diagram_pin_positions"], geometry["pins"]):
                    self.assertEqual(drawn["number"], row[0])
                    self.assertAlmostEqual(drawn["pos"][0], row[2] * 10)
                    self.assertAlmostEqual(drawn["pos"][1], row[3] * 10)
                    self.assertAlmostEqual(drawn["size"][0], row[4] * 10)
                    self.assertAlmostEqual(drawn["size"][1], row[5] * 10)

    def test_exact_ordering_codes_and_pinouts(self):
        module = self.parts[self.project["project_match_overrides"]["U2"]]
        self.assertEqual(module["part_number_manufacturer"], "ESP32-WROOM-32E-N8")
        self.assertEqual(len(module["pins"]), 39)
        self.assertEqual(module["pins"]["pin_2"]["name"], "3v3")
        cp2102 = self.parts["electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102_gmr"]
        self.assertEqual(len(cp2102["pins"]), 29)
        self.assertEqual(cp2102["pins"]["pin_25"]["name"], "rxd")
        self.assertEqual(cp2102["pins"]["pin_26"]["name"], "txd")

    def test_unverified_project_master_is_not_silently_adopted(self):
        from unittest.mock import Mock
        masters = Mock()
        masters.hand_solder.return_value = ""
        for reference in ["J1", "SW1"]:
            part = self.parts[self.project["project_match_overrides"][reference]]
            sources, issues = select_sources(part, masters, {"footprints": ["Connector_USB:wrong_manufacturer"]})
            self.assertEqual(sources["machine_solder"], "")
            self.assertTrue(issues)
        masters.footprint_path.assert_not_called()
