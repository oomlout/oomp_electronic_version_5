"""Slot drawings retain circular radii, full dimensions and board orientation."""

import copy
import unittest
from unittest.mock import patch
from xml.etree import ElementTree

import working_svg


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




if __name__ == "__main__":
    unittest.main()
