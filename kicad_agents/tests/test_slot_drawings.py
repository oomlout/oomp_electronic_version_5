"""Slot drawings retain circular radii, full dimensions and board orientation."""

import copy
import unittest
from unittest.mock import patch
from xml.etree import ElementTree

import working_svg
from kicad_agents.project_summary_agent import _svg_mounting_hole, _mirrored_mounting_hole


class SlotDrawingTests(unittest.TestCase):
    def test_component_slots_use_radius_and_centre_spacing(self):
        sizes = [[2, 4], [4, 2], [3, 5], [2, 2]]
        for width, height in sizes:
            with self.subTest(width=width, height=height):
                with patch.object(working_svg.opsvg, "se") as draw:
                    working_svg._add_slot_outline({}, width, height, "component.hole", [3, 7, 0])
                details = draw.call_args_list[0].kwargs
                self.assertEqual(details["shape"], "slot")
                self.assertEqual(details["r"], min(width, height) / 2)
                self.assertEqual(details["w"] + 2 * details["r"], max(width, height))
                self.assertEqual(details["rot"][2], 90 if height > width else 0)
                self.assertEqual(details["pos"], [3, 7, 0])
                expected_count = 1 if width == height else 3
                self.assertEqual(draw.call_count, expected_count)
                for call in draw.call_args_list[1:]:
                    self.assertEqual(call.kwargs["shape"], "circle")
                    self.assertEqual(call.kwargs["r"], details["r"])
                    self.assertEqual(call.kwargs["color"], "none")

    def test_board_slot_and_plating_have_circular_caps(self):
        for width, height in [[2, 4], [4, 2]]:
            row = {
                "style": "slot", "plating": "plated", "pad_shape": "oval", "rotation": 30,
                "pad_size_mm": {"x": width + 1, "y": height + 1},
                "drill_size_mm": {"x": width, "y": height},
            }
            before = copy.deepcopy(row)
            shapes = _svg_mounting_hole(row, 10, 20)
            self.assertEqual(row, before)
            self.assertEqual(len(shapes), 2)
            for shape in shapes:
                element = ElementTree.fromstring(shape)
                self.assertEqual(element.tag, "g")
                self.assertEqual(element[0].tag, "path")
                self.assertEqual(element[0].attrib["d"].count("A "), 2)
                self.assertIn(" L ", element[0].attrib["d"])
                expected_rotation = 120 if height > width else 30
                self.assertEqual(element.attrib["transform"], f"rotate({expected_rotation:.4f} 10.0000 20.0000)")
            drill = ElementTree.fromstring(shapes[1])
            self.assertEqual(len(drill.findall("circle")), 2)
            for circle in drill.findall("circle"):
                self.assertEqual(float(circle.attrib["r"]), min(width, height) / 2)
                self.assertEqual(circle.attrib["style"], "fill: none")
            mirrored = ElementTree.fromstring(_mirrored_mounting_hole(row, 10, 20)[1])
            expected_rotation = 60 if height > width else -30
            self.assertEqual(mirrored.attrib["transform"], f"rotate({expected_rotation:.4f} 10.0000 20.0000)")

    def test_round_holes_and_rectangular_pads_stay_their_original_shape(self):
        row = {
            "style": "round", "plating": "plated", "pad_shape": "rect",
            "pad_size_mm": {"x": 3, "y": 3}, "drill_size_mm": {"x": 2, "y": 2},
        }
        shapes = _svg_mounting_hole(row, 0, 0)
        self.assertEqual(ElementTree.fromstring(shapes[0]).tag, "rect")
        self.assertEqual(ElementTree.fromstring(shapes[1]).tag, "circle")


if __name__ == "__main__":
    unittest.main()
