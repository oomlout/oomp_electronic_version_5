import json
import tempfile
import unittest
from pathlib import Path

import yaml

from kicad_agents.kicad_processing_agent import process_project
from kicad_agents.oomp_matching_agent import (
    OompPartIndex,
    capacitance_taxonomy,
    match_component,
    parse_resistance_ohms,
)
from kicad_agents.sexpr import children, load, tag, value
import working_oomp_populate_project


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_PROJECT = REPOSITORY_ROOT / "project" / "electrolama" / "pt1"
SAMPLE_SCHEMATIC = SAMPLE_PROJECT / "git" / "pt1" / "pcba" / "Rev A2" / "pt1-RevA2.kicad_sch"
PARTS_DIRECTORY = REPOSITORY_ROOT / "parts"
PROJECT_PART = PARTS_DIRECTORY / "oomp_project_github_electrolama_pt1_current"


class SExpressionTests(unittest.TestCase):
    def test_reads_modern_sample_schematic(self):
        root = load(SAMPLE_SCHEMATIC)
        self.assertEqual(tag(root), "kicad_sch")
        self.assertEqual(value(root, "version"), "20260306")
        self.assertEqual(len(children(root, "symbol")), 64)
        self.assertEqual(len(children(root, "wire")), 177)


class MatchingAgentTests(unittest.TestCase):
    def test_normalizes_engineering_values(self):
        self.assertEqual(parse_resistance_ohms("5k1"), 5100)
        self.assertEqual(parse_resistance_ohms("2.2k"), 2200)
        self.assertEqual(parse_resistance_ohms("100k"), 100000)
        self.assertEqual(capacitance_taxonomy("10n"), "10_nano_farad")
        self.assertEqual(capacitance_taxonomy("4u7"), "4_7_micro_farad")

    def test_exact_basic_component_match(self):
        index = OompPartIndex(PARTS_DIRECTORY)
        component = {
            "reference": "R4",
            "schematic": {
                "units": [
                    {
                        "library_id": "Device:R",
                        "on_board": True,
                        "properties": {"Value": "2k2", "Footprint": "Resistor_SMD:R_0402"},
                    }
                ]
            },
            "pcb": {"library_id": "R_0402"},
        }
        result = match_component(index, component)
        self.assertEqual(result["status"], "matched")
        self.assertEqual(result["oomp_id"], "electronic_resistor_0402_2200_ohm")

    def test_board_features_are_not_applicable(self):
        index = OompPartIndex(PARTS_DIRECTORY)
        components = [
            {
                "reference": "SJ1",
                "schematic": {
                    "units": [
                        {
                            "on_board": True,
                            "properties": {"Value": "SJ2W", "Footprint": "Project:SJ_2"},
                        }
                    ]
                },
                "pcb": {"library_id": "SJ_2"},
            },
            {
                "reference": "UNK_HOLE_0",
                "schematic": {"units": []},
                "pcb": {"library_id": "dummyfp0"},
            },
        ]
        for component in components:
            result = match_component(index, component)
            self.assertEqual(result["status"], "not_applicable")
            self.assertFalse(result["accepted"])


class ProcessingAgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary_directory = tempfile.TemporaryDirectory()
        cls.output_directory = Path(cls.temporary_directory.name) / "generated_data"
        cls.project_data, _ = process_project(
            SAMPLE_PROJECT,
            PARTS_DIRECTORY,
            output_directory=cls.output_directory,
        )
        cls.components = {
            component["reference"]: component for component in cls.project_data["components"]
        }

    @classmethod
    def tearDownClass(cls):
        cls.temporary_directory.cleanup()

    def test_project_counts_and_formats(self):
        summary = self.project_data["summary"]
        self.assertEqual(summary["schematic_symbol_count"], 64)
        self.assertEqual(summary["pcb_footprint_count"], 37)
        self.assertEqual(summary["component_count"], 67)
        json.loads((self.output_directory / "project.json").read_text(encoding="utf-8"))
        yaml.safe_load((self.output_directory / "project.yaml").read_text(encoding="utf-8"))

    def test_c1_positions_connectivity_size_and_match(self):
        component = self.components["C1"]
        schematic_unit = component["schematic"]["units"][0]
        self.assertEqual(schematic_unit["position"]["x"], 73.66)
        self.assertEqual(schematic_unit["position"]["y"], 40.64)
        self.assertEqual(schematic_unit["position"]["rotation"], 90.0)
        self.assertEqual(schematic_unit["pins"][0]["position"], {"x": 73.66, "y": 38.1})
        self.assertEqual(schematic_unit["pins"][0]["net"], "VUSB_IN")
        self.assertEqual(schematic_unit["size"]["local_graphics"]["width"], 5.2324)
        self.assertEqual(component["pcb"]["position"]["x"], 149.7511)
        self.assertEqual(component["pcb"]["position"]["y"], 119.1286)
        self.assertEqual(component["oomp"]["oomp_id"], "electronic_capacitor_0402_10_nano_farad")

    def test_component_folder_contract_and_oomp_copy(self):
        component_directory = self.output_directory / "components" / "C1"
        expected_files = [
            component_directory / "component.json",
            component_directory / "component.yaml",
            component_directory / "schematic" / "working.yaml",
            component_directory / "schematic" / "size.yaml",
            component_directory / "pcb" / "working.yaml",
            component_directory / "pcb" / "size.yaml",
            component_directory / "oomp" / "match.yaml",
            component_directory / "oomp" / "working.yaml",
        ]
        for expected_file in expected_files:
            self.assertTrue(expected_file.is_file(), expected_file)
        copied = component_directory / "oomp" / "working.yaml"
        source = PARTS_DIRECTORY / "electronic_capacitor_0402_10_nano_farad" / "working.yaml"
        self.assertEqual(copied.read_bytes(), source.read_bytes())

    def test_unmatched_and_non_physical_are_separate(self):
        unmatched = json.loads((self.output_directory / "unmatched_parts.json").read_text(encoding="utf-8"))
        unmatched_references = {component["reference"] for component in unmatched["components"]}
        self.assertIn("IC1", unmatched_references)
        self.assertNotIn("#GND1", unmatched_references)
        self.assertEqual(self.components["#GND1"]["oomp"]["status"], "not_applicable")


class ProjectPartTests(unittest.TestCase):
    def test_project_populator_defaults_to_current_and_allows_version_records(self):
        options = []
        working_oomp_populate_project.main(options=options)
        self.assertEqual(len(options), 1)
        project = options[0]
        taxonomy = [project[f"taxonomy_{number}"] for number in range(1, 7)]
        self.assertEqual(taxonomy, ["oomp", "project", "github", "electrolama", "pt1", "current"])
        self.assertEqual(project["project_file_folder"], "pcba/Rev A2")
        self.assertEqual(project["project_file_basename"], "pt1-RevA2")

    def test_generated_project_part_has_always_run_actions_and_local_assets(self):
        working = yaml.safe_load((PROJECT_PART / "working.yaml").read_text(encoding="utf-8"))
        first_action = working["oomlout_ai_roboclick_1"]
        second_action = working["oomlout_ai_roboclick_2"]
        self.assertEqual(first_action["file_test"], "")
        self.assertEqual(second_action["file_test"], "")
        self.assertEqual(first_action["actions"][0]["command"], "run_python")
        self.assertEqual(second_action["actions"][0]["command"], "run_python")

        readme = (PROJECT_PART / "README.md").read_text(encoding="utf-8")
        self.assertIn("https://github.com/electrolama/pt1", readme)
        self.assertIn("![PCB component placement](generated_data/src/board.svg)", readme)
        self.assertNotIn("project_summary_llm", readme)
        self.assertTrue((PROJECT_PART / "generated_data" / "src" / "board.svg").is_file())
        self.assertFalse(any((PROJECT_PART / "generated_data").glob("*llm*")))


if __name__ == "__main__":
    unittest.main()
