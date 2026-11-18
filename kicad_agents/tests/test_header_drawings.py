import re
import unittest
from pathlib import Path

import working_svg


def _header(pin_count=10, orientation="through_hole", post=6.0, tail=3.0):
    return {
        "taxonomy_1": "electronic",
        "taxonomy_2": "connector",
        "taxonomy_3": "header",
        "taxonomy_4": "2_54_mm_pitch",
        "taxonomy_5": orientation,
        "taxonomy_6": f"{pin_count}_pin",
        "taxonomy_7": "male",
        "header_dimensions_mm": {
            "pin_pitch": 2.54,
            "pin_square": 0.64,
            "plastic_height": 2.5,
            "plastic_width": 2.5,
            "pin_length_post": post,
            "pin_length_tail": tail,
            "pin_length_total": 11.6,
            "pcb_hole_diameter": 1.02,
        },
    }


class HeaderDrawingTests(unittest.TestCase):
    def test_bounded_rows_do_not_inflate_one_pin_or_merge_forty(self):
        self.assertEqual(working_svg._header_row_extent_for_slot(_header(1), 24), 8.0)
        self.assertEqual(working_svg._header_row_extent_for_slot(_header(10), 24), 24.0)
        self.assertEqual(working_svg._header_row_extent_for_slot(_header(40), 24), 24.0)

    def test_front_cells_preserve_250_to_254_datasheet_ratio(self):
        part = _header(10)
        working_svg._add_254_header_physical_outline(part, width=30, height=4)
        expected_collar = 3.0 * 2.5 / 2.54
        self.assertAlmostEqual(part["diagram_outline_width"], expected_collar, places=6)
        self.assertEqual(len(part["diagram_pin_positions"]), 10)

    def test_right_angle_front_silhouette_is_centred_as_a_whole(self):
        part = _header(1, "through_hole_right_angle_long_pin", post=3.0, tail=6.0)
        row_extent = 8.0
        dimensions = working_svg._header_dimensions(part)
        scale = row_extent / dimensions["pin_pitch"]
        collar = dimensions["plastic_width"] * scale
        tail = dimensions["pin_length_tail"] * scale
        body_x = working_svg._header_front_center_x(part, row_extent)
        silhouette_left = body_x - collar / 2 - tail
        silhouette_right = body_x + collar / 2
        self.assertAlmostEqual((silhouette_left + silhouette_right) / 2, 0.0, places=6)

    def test_straight_side_offsets_carrier_between_six_and_three_mm_legs(self):
        part = _header()
        working_svg._add_254_header_side_view(part, width=24, height=32)
        geometry = part["header_side_geometry"]
        self.assertFalse(geometry["right_angle"])
        self.assertAlmostEqual((geometry["pin_top"] + geometry["pin_bottom"]) / 2, 0.0, places=6)
        self.assertLess((geometry["body_top"] + geometry["body_bottom"]) / 2, 0.0)

    def test_short_and_long_right_angle_profiles_remain_distinct(self):
        short = _header(10, "through_hole_right_angle_short_pin", post=6.0, tail=3.0)
        long = _header(10, "through_hole_right_angle_long_pin", post=3.0, tail=6.0)
        working_svg._add_254_header_side_view(short, width=28, height=32)
        working_svg._add_254_header_side_view(long, width=28, height=32)
        short_geometry = short["header_side_geometry"]
        long_geometry = long["header_side_geometry"]
        self.assertEqual(short_geometry["mating_length"], 6.0)
        self.assertEqual(short_geometry["board_length"], 3.0)
        self.assertEqual(long_geometry["mating_length"], 3.0)
        self.assertEqual(long_geometry["board_length"], 6.0)

        for geometry in (short_geometry, long_geometry):
            horizontal_midpoint = (
                geometry["mating_start_x"] + geometry["bend_x"]
            ) / 2
            vertical_midpoint = (
                geometry["board_end_y"] + geometry["body_top"]
            ) / 2
            self.assertAlmostEqual(horizontal_midpoint, 0.0, places=6)
            self.assertAlmostEqual(vertical_midpoint, 0.0, places=6)

    def test_every_generated_header_has_complete_views_and_declared_pin_count(self):
        parts_root = Path(__file__).resolve().parents[2] / "parts"
        part_pattern = re.compile(
            r"^electronic_connector_header_2_54_mm_pitch_through_hole_"
            r"(?:(?:right_angle_(?:short|long)_pin_)?)(\d+)_pin$"
        )
        diagram_stems = (
            "working_svg_assembly",
            "working_svg_assembly_pins",
            "working_svg_outline",
            "working_svg_part_id",
            "working_svg_md5_6_alpha",
            "working_svg_bip_39_3_word",
            "working_svg_square",
            "working_svg_square_pins",
            "working_svg_square_schematic",
            "working_svg_dimensioned",
            "working_svg_dimensioned_titles",
            "working_svg_schematic",
            "working_svg_schematic_pins",
            "working_svg_schematic_part_id",
            "working_svg_schematic_md5_6_alpha",
            "working_svg_schematic_bip_39_3_word",
            "working_svg_top",
            "working_svg_bottom",
            "working_svg_side",
        )

        matched_parts = []
        for part_directory in sorted(parts_root.iterdir()):
            match = part_pattern.fullmatch(part_directory.name)
            if not match:
                continue
            matched_parts.append(part_directory)
            pin_count = int(match.group(1))
            data_directory = part_directory / "data"

            for stem in diagram_stems:
                for suffix in (".svg", ".png"):
                    output = data_directory / f"{stem}{suffix}"
                    self.assertTrue(output.is_file(), f"missing {output}")
                    self.assertGreater(output.stat().st_size, 0, f"empty {output}")

            top_svg = (data_directory / "working_svg_top.svg").read_text(
                encoding="utf-8"
            )
            bottom_svg = (data_directory / "working_svg_bottom.svg").read_text(
                encoding="utf-8"
            )
            self.assertEqual(
                top_svg.count("<polygon "),
                pin_count,
                f"wrong collar count for {part_directory.name}",
            )
            self.assertEqual(
                bottom_svg.count("<circle "),
                pin_count,
                f"wrong PCB-hole count for {part_directory.name}",
            )

        self.assertEqual(len(matched_parts), 120)


if __name__ == "__main__":
    unittest.main()
