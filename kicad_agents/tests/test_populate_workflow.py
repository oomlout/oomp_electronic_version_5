"""The documented source-only workflow keeps defaults and overrides editable."""

import unittest
from unittest.mock import patch

import action_generate
import working_oomp_populate_svg
import working_oomp_populate_category
import working_oomp_populate
import working_oomp_populate_led
from working_oomp_metadata import readable_name
from kicad_agents.kicad_processing_agent import _footprint_record, _symbol_record, _add_connectivity_cross_checks
from kicad_agents.sexpr import loads
from pathlib import Path


class PopulateWorkflowTests(unittest.TestCase):
    def test_led_strips_and_filaments_are_not_populated(self):
        options = []
        working_oomp_populate_led.main(options=options)
        retired_families = []
        for option in options:
            led_style = str(option.get('taxonomy_3', ''))
            if led_style == 'filament_3_volt' or led_style.startswith('strip_'):
                retired_families.append(led_style)
        self.assertEqual(retired_families, [])

    def test_categories_are_populated_and_overrides_persist(self):
        examples = [
            ['resistor', '', 'resistor'], ['resistor_array', '', 'resistor'],
            ['capacitor', '', 'capacitor'], ['connector', '', 'connector'],
            ['ic', 'microcontroller', 'mcu'], ['ic', 'memory', 'memory'],
            ['ic', 'logic', 'logic'], ['ic', 'unknown', 'ic'],
        ]
        for family, function, expected in examples:
            part = {'taxonomy_1': 'electronic', 'taxonomy_2': family, 'taxonomy_4': function}
            working_oomp_populate_category.add_category(part)
            self.assertEqual(part['category'], expected)
            part['category'] = 'Custom Type'
            for _ in range(2):
                working_oomp_populate_category.add_category(part)
                self.assertEqual(part['category'], 'custom_type')
                self.assertEqual(part['category_name'], 'Custom type')
        with patch.object(working_oomp_populate, 'write_extras') as write:
            working_oomp_populate.main()
        components = [part for part in write.call_args.args[0] if part.get('taxonomy_1') in ['electronic', 'mechanical']]
        self.assertGreater(len(components), 100)
        self.assertTrue(all(part.get('category') and part.get('category_name') for part in components))
        self.assertTrue(any(part['category'] == 'mcu' for part in components))

    def test_unmatched_category_is_only_a_coarse_hint(self):
        classify = working_oomp_populate_category.unmatched_category
        for reference, library, category in [
            ['U1', 'MCU_Microchip_ATmega:ATmega328P-A', 'mcu'],
            ['U2', 'Memory_Flash:W25Q', 'memory'], ['U3', '74xx:74HC595', 'logic'],
            ['C10', 'Device:C', 'capacitor'], ['CON2', '', 'connector'],
            ['U4', 'Custom:Unknown', 'ic'], ['REF1', '', 'other'],
        ]:
            self.assertEqual(classify(reference, library), category)

    def test_normal_generation_preserves_pngs_and_updates_navigation(self):
        with patch.object(action_generate.working_oomp_populate, 'main') as populate, \
             patch.object(action_generate.working_oomp, 'main') as define, \
             patch.object(action_generate, 'run_actions', return_value=(3, 0)) as actions, \
             patch('kicad_agents.kicad_library_agent.package_libraries'):
            action_generate.generate('electronic_resistor_0603_2000_ohm')
        filters = ['electronic_resistor_0603_2000_ohm', 'navigation']
        populate.assert_called_once_with()
        define.assert_called_once_with(filter=filters, regenerate_pngs=False)
        actions.assert_called_once_with(filter_text=filters, regenerate_pngs=False)

    def test_name_and_datasheet_geometry_survive_default_generation(self):
        option = {'taxonomy_1': 'electronic', 'taxonomy_2': 'ic', 'taxonomy_3': 'sot_23_5',
                  'name_readable_override': 'Example op amp',
                  'ic_dimensions_mm': {'body_length': 3.01, 'body_height': 1.15}}
        for _ in range(2):
            working_oomp_populate_svg.add_svg_details(option)
            self.assertEqual(option['ic_dimensions_mm']['body_length'], 3.01)
            self.assertEqual(option['ic_dimensions_mm']['body_height'], 1.15)
            self.assertEqual(option['ic_dimensions_mm']['pin_pitch'], .95)
        self.assertEqual(readable_name(option), 'Example op amp')

    def test_module_with_mounting_holes_does_not_classify_signal_pins_as_holes(self):
        root = loads('''(footprint "Module:Arduino_UNO_R3_WithMountingHoles"
          (property "Reference" "A1") (layer "F.Cu") (at 10 20)
          (pad "" np_thru_hole circle (at 0 0) (size 3.2 3.2) (drill 3.2) (layers "*.Cu"))
          (pad "1" thru_hole circle (at 2 0) (size 2 2) (drill 1) (layers "*.Cu") (net "GND")))''')
        directory = Path.cwd()
        record = _footprint_record(root, directory / 'board.kicad_pcb', directory)
        self.assertFalse(record['is_mounting_hole'])
        self.assertEqual(len(record['mounting_holes']), 1)
        self.assertEqual(record['mounting_holes'][0]['role'], 'mounting')
        self.assertFalse(record['pads'][1]['is_mounting_hole'])

    def test_schematic_y_up_library_becomes_y_down_sheet(self):
        library = loads('''(symbol "Device:C" (symbol "C_1_1"
          (pin passive line (at 0 3.81 270) (length 2) (name "") (number "1"))
          (pin passive line (at 0 -3.81 90) (length 2) (name "") (number "2"))))''')
        directory = Path.cwd()
        for angle, expected in [[0, (10, 16.19)], [90, (6.19, 20)], [180, (10, 23.81)], [270, (13.81, 20)]]:
            symbol = loads(f'(symbol (lib_id "Device:C") (property "Reference" "C1") (at 10 20 {angle}) (unit 1))')
            record = _symbol_record(symbol, {'Device:C': library}, directory / 'root.kicad_sch', directory)
            pin = record['pins'][0]['position']
            self.assertAlmostEqual(pin['x'], expected[0])
            self.assertAlmostEqual(pin['y'], expected[1])

    def test_root_local_net_prefix_does_not_flatten_child_sheet_names(self):
        components = [{'schematic': {'units': [{'source_file': source, 'pins': [{'number': '1', 'net': 'DATA'}]}]},
                       'pcb': {'pads': [{'number': '1', 'net': net}]}} for source, net in
                      [('root.kicad_sch', '/DATA'), ('child.kicad_sch', '/other/DATA')]]
        _add_connectivity_cross_checks(components, root_schematic='root.kicad_sch')
        self.assertEqual(components[0]['connectivity_cross_check']['agree_count'], 1)
        self.assertEqual(components[1]['connectivity_cross_check']['disagree_count'], 1)


if __name__ == '__main__':
    unittest.main()
