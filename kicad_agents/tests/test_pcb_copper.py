"""Routing extraction, net identity and board overlay regression tests."""

import json
import math
import re
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

from kicad_agents.pcb_copper import (
    add_copper_svg, arc_path, copper_svg, explorer_copper, extract_copper,
)
from kicad_agents.project_html_agent import generate_board_explorer
from kicad_agents.sexpr import loads


PCB = '''(kicad_pcb (version 20221018)
  (layers (0 "F.Cu" signal) (1 "In1.Cu" power) (31 "B.Cu" signal))
  (net 0 "") (net 1 "GND") (net 2 "USB_D+")
  (segment (start 10 20) (end 15 20) (width .25) (layer "F.Cu") (net 2))
  (arc (start 15 20) (mid 16 21) (end 15 22) (width .25) (layer "B.Cu") (net 2))
  (via (at 15 20) (size .6) (drill .3) (layers "F.Cu" "B.Cu") (net 2))
  (via blind (at 12 20) (size .5) (drill .2) (layers "F.Cu" "In1.Cu") (net 1))
  (footprint "Test" (layer "F.Cu") (at 10 20 90)
    (property "Reference" "U1")
    (pad "1" smd roundrect (at 2 0 120) (size 2 1) (roundrect_rratio .25) (layers "F.Cu") (net 2 "USB_D+"))
    (pad "2" thru_hole circle (at 0 0 90) (size 2 2) (drill 1) (layers "*.Cu" "*.Mask") (net 1 "GND"))
    (pad "3" smd rect (at 0 1) (size 1 1) (layers "F.Cu") (net 0 ""))
    (pad "3" smd rect (at 0 2) (size 1 1) (layers "F.Cu") (net 0 ""))
    (pad "" np_thru_hole circle (at 5 5) (size 1 1) (drill 1) (layers "*.Cu")))
  (footprint "Back" (layer "B.Cu") (at 15 20 -90)
    (fp_text reference "J1")
    (pad "1" smd custom (at 2 0 -90) (size 1 1) (layers "B.Cu") (net 2 "USB_D+")
      (options (anchor rect)) (primitives (gr_poly (pts (xy 0 0) (xy 2 0) (xy 2 1)) (width 0) (fill yes)))))
  (zone (net 1) (layer "F.Cu")
    (polygon (pts (xy 0 0) (xy 20 0) (xy 20 30)))
    (filled_polygon (layer "F.Cu") (pts (xy 1 1) (xy 19 1) (xy 19 29))))
  (zone (net 1) (layer "B.Cu") (polygon (pts (xy 0 0) (xy 20 0) (xy 20 30))))
  (zone (net 0) (layer "F.Cu") (keepout (tracks not_allowed))))'''


class CopperTests(unittest.TestCase):
    def setUp(self):
        self.copper = extract_copper(loads(PCB))

    def test_tracks_vias_layers_and_real_fills(self):
        self.assertEqual(len(self.copper["tracks"]), 2)
        self.assertEqual(self.copper["tracks"][0]["net"], "USB_D+")
        self.assertEqual(self.copper["tracks"][1]["mid"], [16, 21])
        self.assertEqual(self.copper["vias"][0]["layers"], ["F.Cu", "In1.Cu", "B.Cu"])
        self.assertEqual(self.copper["vias"][1]["layers"], ["F.Cu", "In1.Cu"])
        self.assertEqual(len(self.copper["zones"]), 1)
        self.assertEqual(self.copper["zones"][0]["points"][0], [1, 1])
        self.assertEqual(len(self.copper["warnings"]), 1)

    def test_absolute_pad_angles_and_footprint_local_centres(self):
        pads = self.copper["pads"]
        self.assertEqual(len(pads), 5)  # Exclude non-plated mechanical hole.
        self.assertEqual(pads[0]["position"], [10, 18])
        self.assertEqual(pads[0]["rotation"], -120)
        self.assertEqual(pads[-1]["position"], [15, 22])
        self.assertEqual(pads[-1]["rotation"], 90)
        self.assertEqual(pads[1]["layers"], self.copper["layers"])
        self.assertEqual(pads[1]["drill"], {"size": [1, 1], "offset": [0, 0]})
        self.assertEqual(pads[2]["net"], "")
        self.assertEqual(pads[3]["net"], "")

    def test_modern_named_nets_and_old_empty_net(self):
        pcb = '(kicad_pcb (segment (start 0 0) (end 1 0) (layer "F.Cu") (net "0")))'
        self.assertEqual(extract_copper(loads(pcb))["tracks"][0]["net"], "0")
        pcb = '(kicad_pcb (segment (start 0 0) (end 1 0) (layer "F.Cu") (net "Net-(U1-Pin_3)")))'
        self.assertEqual(extract_copper(loads(pcb))["tracks"][0]["net"], "Net-(U1-Pin_3)")

    def test_net_indices_isolate_boards_and_keep_duplicate_physical_pads(self):
        data = {"pcb_files": [{"source_file": source, "copper": self.copper} for source in ["a.pcb", "b.pcb"]]}
        copper = explorer_copper(data)
        self.assertEqual(len(copper["nets"]), 4)
        usb = next(net for net in copper["nets"] if net["name"] == "USB_D+")
        self.assertEqual({(p["reference"], p["number"]) for p in usb["pins"]}, {("U1", "1"), ("J1", "1")})
        self.assertEqual(usb["track_count"], 2)
        self.assertEqual(usb["via_count"], 1)
        self.assertEqual(len({net["id"] for net in copper["nets"]}), 4)
        self.assertEqual(sum(not f["net_id"] for f in copper["features"]), 4)

    def test_svg_rotation_custom_polygon_escaping_and_mirroring(self):
        data = explorer_copper({"pcb_files": [{"source_file": "board", "copper": self.copper}]})
        data["features"][-1]["reference"] = 'J"<&'
        drawing = copper_svg(data["features"])
        root = ET.fromstring('<svg>' + drawing + '</svg>')
        self.assertTrue(any(g.get("data-reference") == 'J"<&' for g in root))
        self.assertIn('rotate(-120.0)', drawing)
        self.assertIn('rx="0.25"', drawing)
        self.assertIn('<polygon', drawing)
        self.assertIn('class="pad-drill"', drawing)
        board = '<svg viewBox="5 10 20 30"><rect/><g class="board-component"></g></svg>'
        top = add_copper_svg(board, drawing)
        back = add_copper_svg(board, drawing, mirror=True)
        self.assertLess(top.index('class="copper-base"'), top.index('class="board-component"'))
        self.assertLess(top.index('class="copper-overlay"'), top.index('class="board-component"'))
        self.assertGreater(top.index('class="copper-overlay"'), top.index('class="copper-base"'))
        self.assertIn('translate(30.000000 0) scale(-1 1)', back)
        ET.fromstring(back)

    def test_arcs_include_correct_major_minor_sweep_and_collinear_fallback(self):
        self.assertIn('A 1.000000 1.000000 0 0 1', arc_path([1, 0], [math.sqrt(.5), math.sqrt(.5)], [0, 1]))
        self.assertIn('A 1.000000 1.000000 0 1 0', arc_path([1, 0], [-1, 0], [0, 1]))
        self.assertEqual(arc_path([0, 0], [1, 1], [2, 2]), 'M 0 0 L 1 1 L 2 2')

    def test_single_file_html_contains_safe_data_and_interactive_controls(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            output = project / 'data' / 'generated_data'
            (output / 'src').mkdir(parents=True)
            (output / 'src' / 'board.svg').write_text('<svg viewBox="0 0 20 30"><rect/><g class="board-component" data-reference="U1"/></svg>')
            self.copper["pads"][0]["net"] = '</script><script>alert(1)</script>'
            data = {"pcb_files": [{"source_file": "board", "copper": self.copper}], "components": [{
                "reference": "U1", "pcb": {"side": "front", "source_file": "board", "pads": [{
                    "number": "1", "net": '</script><script>alert(1)</script>'}]}, "oomp": {}}]}
            path = generate_board_explorer(project, data, {})
            text = path.read_text(encoding='utf-8')
            self.assertNotIn('</script><script>alert(1)', text)
            for control in ['copper-data', 'net-select', 'net-search', 'copper-layer', 'show-fills', 'show-traces']:
                self.assertIn(f'id="{control}"', text)
            self.assertIn("menu.className = 'pin-menu'", text)
            self.assertNotRegex(text, r'<script[^>]+src=')
            embedded = re.search(r'<script id="component-data" type="application/json">(.*?)</script>', text, re.S).group(1)
            self.assertTrue(json.loads(embedded)[0]["pads"][0]["net_id"])


if __name__ == '__main__':
    unittest.main()
