import json
import re
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
from kicad_agents.project_summary_agent import _orientation_rotation
from kicad_agents.sexpr import children, load, tag, value
import working_oomp_populate_project


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_PROJECT = REPOSITORY_ROOT / "project" / "electrolama" / "pt1"
SAMPLE_SCHEMATIC = SAMPLE_PROJECT / "git" / "pt1" / "pcba" / "Rev A2" / "pt1-RevA2.kicad_sch"
PARTS_DIRECTORY = REPOSITORY_ROOT / "parts"
PROJECT_PART = PARTS_DIRECTORY / "oomp_project_github_electrolama_pt1_current"
USB_A_PART = PARTS_DIRECTORY / "electronic_connector_usb_a_surface_mount_4_pin_shenzhen_jing_tuo_jin_electronics_912121a2023s10100"
USB_C_PART = PARTS_DIRECTORY / "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12"
USB_A_SOURCE = REPOSITORY_ROOT / "parts_source" / USB_A_PART.name
USB_C_SOURCE = REPOSITORY_ROOT / "parts_source" / USB_C_PART.name


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
        self.assertEqual(
            second_action["actions"][0]["file_output"],
            "generated_data/src/board_pins.png",
        )

        readme = (PROJECT_PART / "README.md").read_text(encoding="utf-8")
        self.assertIn("https://github.com/electrolama/pt1", readme)
        self.assertIn(
            "![PCB component placement](https://raw.githubusercontent.com/oomlout/oomp_electronic_version_5/main/parts/oomp_project_github_electrolama_pt1_current/generated_data/src/board.svg)",
            readme,
        )
        self.assertNotIn("](../", readme)
        self.assertNotIn("project_summary_llm", readme)
        self.assertIn(
            "| References | Quantity | Description | Value | Footprint | OOMP part |",
            readme,
        )
        self.assertIn(
            "https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts/electronic_capacitor_0402_10_nano_farad",
            readme,
        )
        self.assertNotIn("/parts/electronic_capacitor_0402_10_nano_farad/README.md", readme)
        self.assertTrue((PROJECT_PART / "generated_data" / "src" / "board.svg").is_file())
        self.assertTrue((PROJECT_PART / "generated_data" / "src" / "board_pins.svg").is_file())
        board_pins_png_path = PROJECT_PART / "generated_data" / "src" / "board_pins.png"
        self.assertTrue(board_pins_png_path.is_file())
        self.assertIn("## Board with pins", readme)
        self.assertIn(
            "![PCB component placement with pin names](https://raw.githubusercontent.com/oomlout/oomp_electronic_version_5/main/parts/oomp_project_github_electrolama_pt1_current/generated_data/src/board_pins.png)",
            readme,
        )
        from PIL import Image

        with Image.open(board_pins_png_path) as board_pins_image:
            self.assertEqual(max(board_pins_image.size), 1600)
        self.assertFalse(any((PROJECT_PART / "generated_data").glob("*llm*")))

        assembly_svg_path = PARTS_DIRECTORY / "electronic_resistor_0402_2200_ohm" / "working_svg_assembly.svg"
        self.assertTrue(assembly_svg_path.is_file())
        assembly_svg = assembly_svg_path.read_text(encoding="utf-8")
        self.assertIn('width="1.0000mm" height="0.5000mm"', assembly_svg)
        self.assertIn('vector-effect="non-scaling-stroke"', assembly_svg)
        self.assertIn('stroke-width="0.22"', assembly_svg)
        self.assertNotIn('stroke-width="0.18"', assembly_svg)
        self.assertNotIn('stroke-width="0.8"', assembly_svg)

        assembly_pins_svg_path = PARTS_DIRECTORY / "electronic_resistor_0402_2200_ohm" / "working_svg_assembly_pins.svg"
        self.assertTrue(assembly_pins_svg_path.is_file())
        assembly_pins_svg = assembly_pins_svg_path.read_text(encoding="utf-8")
        self.assertIn(">pin 1</text>", assembly_pins_svg)
        self.assertIn(">pin 2</text>", assembly_pins_svg)
        self.assertIn('transform="rotate(-90.000', assembly_pins_svg)

        board_svg = (PROJECT_PART / "generated_data" / "src" / "board.svg").read_text(encoding="utf-8")
        self.assertIn('transform="translate(155.8761 106.1286) rotate(-90.0000)"', board_svg)
        self.assertIn('width="2.4800" height="15.2400"', board_svg)
        self.assertIn('preserveAspectRatio="xMidYMid meet"', board_svg)
        self.assertNotIn('preserveAspectRatio="none"', board_svg)
        self.assertIn('class="indicator" transform="translate(156.0031 99.7786)"', board_svg)
        self.assertIn(
            '<g transform="translate(6.3500 0.1270) rotate(-90)">',
            board_svg,
        )
        self.assertNotIn(">SJ1</text>", board_svg)
        self.assertNotIn("UNK_HOLE", board_svg)

        board_pins_svg = (PROJECT_PART / "generated_data" / "src" / "board_pins.svg").read_text(encoding="utf-8")
        self.assertIn(">vbus</text>", board_pins_svg)
        self.assertIn(">pin 1</text>", board_pins_svg)
        self.assertNotIn(">SJ1</text>", board_pins_svg)
        self.assertNotIn("UNK_HOLE", board_pins_svg)
        small_reference = re.search(r'font-size="([0-9.]+)"[^>]*>R1</text>', board_pins_svg)
        self.assertIsNotNone(small_reference)
        self.assertLess(float(small_reference.group(1)), 0.22)

    def test_j1_orientation_uses_footprint_pad_one(self):
        local_bounds = {
            "min_x": -1.3716,
            "min_y": -1.2446,
            "max_x": 14.0716,
            "max_y": 1.4986,
        }
        pads = [
            {
                "number": "1",
                "local_position": {"x": 0.0, "y": 0.0},
            }
        ]
        pin_one_svg = {"x": 1.24, "y": 1.27}
        rotation = _orientation_rotation(
            2.48,
            15.24,
            local_bounds,
            pads,
            pin_one_svg,
        )
        self.assertEqual(rotation, -90)

    def test_nearly_square_ic_orientation_is_not_forced_by_pad_extents(self):
        local_bounds = {
            "min_x": -2.125,
            "min_y": -1.8,
            "max_x": 2.125,
            "max_y": 1.8,
        }
        pads = [
            {
                "number": "1",
                "local_position": {"x": -1.25, "y": -0.95},
            }
        ]
        pin_one_svg = {"x": 0.3759, "y": 0.5657}
        rotation = _orientation_rotation(
            2.8,
            2.9,
            local_bounds,
            pads,
            pin_one_svg,
        )
        self.assertEqual(rotation, 0)


class ElectronicPartReadmeTests(unittest.TestCase):
    def test_part_readme_uses_pinout_hero_and_small_previews(self):
        part_directory = PARTS_DIRECTORY / "electronic_resistor_0402_2200_ohm"
        working = yaml.safe_load((part_directory / "working.yaml").read_text(encoding="utf-8"))
        preview_action = working["oomlout_ai_roboclick_1"]
        preview_actions = preview_action["actions"]

        self.assertEqual(len(preview_actions), 8)
        self.assertTrue(all(action["command"] == "image_resize" for action in preview_actions))
        self.assertTrue(all(action["maximum_dimension"] == 300 for action in preview_actions))
        self.assertTrue(all(action["allow_upscale"] is False for action in preview_actions))

        readme = (part_directory / "README.md").read_text(encoding="utf-8")
        self.assertIn("![Resistor 0402 2200 Ohm pinout](working_svg_square_pins.svg)", readme)
        self.assertIn("## At a glance", readme)
        self.assertNotIn("## Diagram gallery", readme)
        self.assertNotIn("<img", readme)
        self.assertIn("## Files", readme)
        self.assertIn("![Pinout drawing](working_svg_square_pins_300.png)", readme)
        self.assertIn("![Outline](working_svg_outline_300.png)", readme)
        self.assertNotIn("[Outline drawing](working_svg_outline.svg)", readme)
        self.assertNotIn("[View the datasheet](datasheet.pdf)", readme)

        from PIL import Image

        preview_files = sorted(part_directory.glob("working_svg*_300.png"))
        self.assertEqual(len(preview_files), 8)
        for preview_file in preview_files:
            with Image.open(preview_file) as preview_image:
                self.assertLessEqual(max(preview_image.size), 300)


class UsbConnectorDiagramTests(unittest.TestCase):
    def test_usb_a_uses_datasheet_dimensions_and_named_pins(self):
        working = yaml.safe_load((USB_A_SOURCE / "working.yaml").read_text(encoding="utf-8"))
        self.assertEqual(working["dimensions_mm"], {"length": 14.3, "width": 10.6})
        self.assertEqual(working["connector_dimensions_mm"]["contact_count"], 4)
        self.assertEqual(working["connector_dimensions_mm"]["contact_pitch"], 2.0)
        self.assertEqual(working["pins"]["pin_2"]["name"], "usb_negative")
        self.assertEqual(working["pins"]["pin_5"]["type"], "shield")

        assembly_svg = (USB_A_PART / "working_svg_assembly.svg").read_text(encoding="utf-8")
        self.assertIn('width="14.3000mm" height="10.6000mm"', assembly_svg)
        self.assertIn('data-pin-one-identifiers="VBUS|1"', assembly_svg)

        local_bounds = {
            "min_x": -7.15,
            "min_y": -4.575,
            "max_x": 7.15,
            "max_y": 6.025,
        }
        pads = [
            {
                "number": "VBUS",
                "local_position": {"x": 3.5, "y": 5.3},
            }
        ]
        rotation = _orientation_rotation(
            14.3,
            10.6,
            local_bounds,
            pads,
            {"x": 2.696, "y": 2.12, "identifiers": ["VBUS", "1"]},
        )
        self.assertEqual(rotation, 180)

    def test_usb_c_uses_datasheet_pinout_and_physical_size(self):
        working = yaml.safe_load((USB_C_SOURCE / "working.yaml").read_text(encoding="utf-8"))
        self.assertEqual(working["dimensions_mm"], {"length": 8.94, "width": 7.35})
        self.assertEqual(len(working["pins"]), 16)
        self.assertEqual(working["pins"]["pin_1"], {"name": "gnd", "number": "A1", "type": "power"})
        self.assertEqual(working["pins"]["pin_16"], {"name": "gnd", "number": "B1", "type": "power"})

        readme = (USB_C_PART / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Datasheet", readme)
        self.assertIn("[View the datasheet](datasheet.pdf)", readme)

        pinout_svg = (USB_C_PART / "working_svg_square_pins.svg").read_text(encoding="utf-8")
        self.assertIn("Connector USB C", pinout_svg)
        self.assertIn("A1 gnd", pinout_svg)
        self.assertIn("B1 gnd", pinout_svg)
        self.assertNotIn(">pin 1<", pinout_svg)

        assembly_svg = (USB_C_PART / "working_svg_assembly.svg").read_text(encoding="utf-8")
        self.assertIn('width="8.9400mm" height="7.3500mm"', assembly_svg)

        assembly_pins_svg = (USB_C_PART / "working_svg_assembly_pins.svg").read_text(encoding="utf-8")
        self.assertEqual(assembly_pins_svg.count("</text>"), 16)
        self.assertIn(">gnd</text>", assembly_pins_svg)
        self.assertIn(">vbus</text>", assembly_pins_svg)
        self.assertIn(">cc1</text>", assembly_pins_svg)
        self.assertIn('transform="rotate(-90.000', assembly_pins_svg)


if __name__ == "__main__":
    unittest.main()
