import csv
import tempfile
import unittest
import zipfile
from pathlib import Path

import yaml

from action_regenerate_all import _normal_gate_is_complete
from action_regenerate_part import _check_files_complete
from kicad_agents.production_jlc_agent import (
    JLC_BOM_COLUMNS,
    JLC_CPL_COLUMNS,
    PUBLIC_OUTPUT_FILENAMES,
    _automatic_skip_reasons,
    _available_gerber_layers,
    _parse_position_file,
    _stable_zip,
    _validate_public_output_layout,
    build_component_rows,
)


MINIMAL_BOARD = """(kicad_pcb
  (version 20240108)
  (generator pcbnew)
  (layers
    (0 \"F.Cu\" signal)
    (2 \"B.Cu\" signal)
    (13 \"F.Paste\" user)
    (15 \"B.Paste\" user)
    (5 \"F.SilkS\" user \"F.Silkscreen\")
    (7 \"B.SilkS\" user \"B.Silkscreen\")
    (1 \"F.Mask\" user)
    (3 \"B.Mask\" user)
    (25 \"Edge.Cuts\" user))
  (footprint \"Resistor_SMD:R_0603_1608Metric\"
    (layer \"F.Cu\")
    (at 10 20 90)
    (property \"Reference\" \"R1\")
    (property \"Value\" \"2.2k\")
    (pad \"1\" smd roundrect (at -0.8 0) (size 0.9 0.95) (layers \"F.Cu\" \"F.Paste\" \"F.Mask\"))
    (pad \"2\" smd roundrect (at 0.8 0) (size 0.9 0.95) (layers \"F.Cu\" \"F.Paste\" \"F.Mask\")))
)"""


class ProductionJlcTests(unittest.TestCase):
    def test_normal_generation_honours_existing_gate(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mode = {
                "file_test": "gate.yaml",
                "honour_gate_in_normal_run": True,
                "always_run_on_regeneration": True,
            }
            self.assertFalse(_normal_gate_is_complete(root, mode))
            (root / "gate.yaml").write_text("status: generated\n", encoding="utf-8")
            self.assertTrue(_normal_gate_is_complete(root, mode))

    def test_regeneration_mode_does_not_treat_gate_as_a_skip_marker(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "gate.yaml").write_text("status: generated\n", encoding="utf-8")
            self.assertTrue(_check_files_complete(root, {"file_test": "gate.yaml"}))
            self.assertFalse(
                _check_files_complete(
                    root,
                    {"file_test": "gate.yaml", "always_run_on_regeneration": True},
                )
            )

    def test_non_bom_parts_are_skipped_automatically(self):
        examples = [
            ("SJ1", {"value": "SolderJumper"}),
            ("FID1", {"value": "Fiducial"}),
            ("LOGO1", {"value": "Logo"}),
            ("R9", {"value": "DNF"}),
            ("H1", {"value": "MountingHole", "is_mounting_hole": True}),
        ]
        for reference, footprint in examples:
            with self.subTest(reference=reference):
                self.assertTrue(_automatic_skip_reasons(reference, footprint))

    def test_public_output_layout_only_allows_four_jlc_files_and_data(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "data").mkdir()
            for filename in PUBLIC_OUTPUT_FILENAMES:
                (root / filename).write_text("test", encoding="utf-8")
            _validate_public_output_layout(root)
            (root / "raw_file.txt").write_text("wrong level", encoding="utf-8")
            with self.assertRaises(RuntimeError):
                _validate_public_output_layout(root)

    def test_jlc_layers_use_protel_compatible_silkscreen_names(self):
        with tempfile.TemporaryDirectory() as temporary:
            board = Path(temporary) / "board.kicad_pcb"
            board.write_text(MINIMAL_BOARD, encoding="utf-8")
            self.assertEqual(
                _available_gerber_layers(board),
                [
                    "F.Cu",
                    "B.Cu",
                    "F.Paste",
                    "B.Paste",
                    "F.Silkscreen",
                    "B.Silkscreen",
                    "F.Mask",
                    "B.Mask",
                    "Edge.Cuts",
                ],
            )

    def test_component_rows_are_jlc_shaped_and_keep_oomp_pad_names(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            project = root / "parts" / "project"
            data = project / "data"
            data.mkdir(parents=True)
            board = data / "kicad_file.kicad_pcb"
            board.write_text(MINIMAL_BOARD, encoding="utf-8")
            part_id = "electronic_resistor_0603_2200_ohm"
            part_directory = root / "parts" / part_id
            part_directory.mkdir(parents=True)
            (part_directory / "working.yaml").write_text(
                yaml.safe_dump(
                    {
                        "part_number_lcsc": "C4190",
                        "manufacturer": "Uniroyal",
                        "part_number_manufacturer": "0603WAF2201T5E",
                    }
                ),
                encoding="utf-8",
            )
            production_footprints = [
                {
                    "reference": "R1",
                    "value": "2.2k",
                    "library_id": "Resistor_SMD:R_0603_1608Metric",
                    "properties": {"Reference": "R1", "Value": "2.2k"},
                    "pads": [{"number": "1", "type": "smd", "net": "GND", "position": {"x": 10, "y": 20}}],
                }
            ]
            metadata_footprints = [
                {
                    "reference": "R1",
                    "pads": [
                        {"number": "input", "type": "smd", "net": "SIG", "position": {"x": 10, "y": 20}},
                        {"number": "output", "type": "smd", "net": "GND", "position": {"x": 11, "y": 20}},
                    ],
                }
            ]
            details = {
                "directory": str(project),
                "production_board_resolved": str(board),
                "project_match_overrides": {"R1": part_id},
                "production_exclude_references": [],
                "production_lcsc_overrides": {},
                "production_rotation_offsets": {"R1": 90},
                "production_position_offsets_mm": {"R1": [0.1, -0.2]},
            }
            positions = [
                {"reference": "R1", "value": "2.2k", "footprint": "R_0603", "x": 10, "y": -20, "rotation": 90, "side": "top"}
            ]
            bom, cpl, components, skipped, unmatched = build_component_rows(
                positions, production_footprints, metadata_footprints, details, root / "parts"
            )
            self.assertEqual(list(bom[0]), JLC_BOM_COLUMNS)
            self.assertEqual(bom[0]["LCSC Part #"], "C4190")
            self.assertEqual(list(cpl[0]), JLC_CPL_COLUMNS)
            self.assertEqual(cpl[0]["Mid X"], "10.1000")
            self.assertEqual(cpl[0]["Mid Y"], "-20.2000")
            self.assertEqual(cpl[0]["Rotation"], "180.00")
            self.assertEqual([pad["name"] for pad in components[0]["pads"]], ["input", "output"])
            self.assertEqual(components[0]["pad_name_source"], "oomp_design")
            self.assertEqual(skipped, [])
            self.assertEqual(unmatched, [])

    def test_position_reader_and_zip_are_repeatable(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            position = root / "position.csv"
            with position.open("w", newline="", encoding="utf-8") as output_file:
                writer = csv.writer(output_file)
                writer.writerow(["Ref", "Val", "Package", "PosX", "PosY", "Rot", "Side"])
                writer.writerow(["U1", "MCU", "QFN", "1.25", "-2.5", "-90", "bottom"])
            rows = _parse_position_file(position)
            self.assertEqual(rows[0]["reference"], "U1")
            self.assertEqual(rows[0]["side"], "bottom")

            source = root / "gerbers"
            source.mkdir()
            (source / "board.gtl").write_text("same", encoding="utf-8")
            first = root / "first.zip"
            second = root / "second.zip"
            _stable_zip(source, first)
            _stable_zip(source, second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with zipfile.ZipFile(first) as archive:
                self.assertEqual(archive.namelist(), ["board.gtl"])


if __name__ == "__main__":
    unittest.main()
