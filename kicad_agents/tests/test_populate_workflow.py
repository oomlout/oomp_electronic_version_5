import unittest
from unittest.mock import patch
import working_oomp_metadata
import working_oomp
import action_generate
import working_oomp_populate_svg
import working_oomp_populate_category
import working_oomp_populate
import working_oomp_populate_led
from working_oomp_metadata import readable_name
'The documented source-only workflow keeps defaults and overrides editable.'

class PopulateWorkflowTests(unittest.TestCase):

    def setUp(self):
        # Population tests must not deduplicate or rewrite real checkout files.
        for name, result in [('collect_common_with_keys', {}),
                             ('restore_common_with_keys', None), ('deduplicate', None)]:
            boundary = patch('action_dedupe_datasheets.' + name, return_value=result)
            boundary.start()
            self.addCleanup(boundary.stop)

    def test_component_navigation_refresh_only_selects_ancestors(self):
        from kicad_agents.component_addition_agent import navigation_part_ids
        definition = {'taxonomy_1': 'electronic', 'taxonomy_2': 'transistor', 'taxonomy_3': 'sot_23', 'taxonomy_14': '', 'taxonomy_15': '2n7002'}
        self.assertEqual(navigation_part_ids(definition), ['navigation', 'navigation_electronic', 'navigation_electronic_transistor', 'navigation_electronic_transistor_sot_23'])

    def test_populate_step_does_not_generate_navigation_entries(self):
        with patch.object(working_oomp_metadata, 'add_navigation_parts') as add_navigation:
            with patch.object(working_oomp_populate, 'write_extras'):
                working_oomp_populate.main()
        add_navigation.assert_not_called()

    def test_missing_source_file_does_not_create_file_copy_action(self):
        part = {'name': 'electronic_connector_jst_ph_2_mm_pitch_surface_mount_right_angle_10_pin_jst_s10b_ph_sm4_tb', 'file_copy': [{'file_source': 'parts_source/__missing_datasheet_for_populate_test__/datasheet.pdf', 'file_destination': 'datasheet.pdf'}]}
        working_oomp.add_part_build_actions(part, 0)
        actions = []
        for key, value in part.items():
            if key.startswith('oomlout_ai_roboclick_') and isinstance(value, dict):
                actions.extend(value.get('actions', []))
        self.assertNotIn('file_copy', [action.get('command') for action in actions])

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
        examples = [['resistor', '', 'resistor'], ['resistor_array', '', 'resistor'], ['capacitor', '', 'capacitor'], ['connector', '', 'connector'], ['ic', 'microcontroller', 'mcu'], ['ic', 'memory', 'memory'], ['ic', 'logic', 'logic'], ['ic', 'unknown', 'ic']]
        for family, function, expected in examples:
            part = {'taxonomy_1': 'electronic', 'taxonomy_2': family, ('taxonomy_3' if family == 'ic' else 'taxonomy_4'): function}
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
        self.assertTrue(all((part.get('category') and part.get('category_name') for part in components)))
        self.assertTrue(any((part['category'] == 'mcu' for part in components)))

    def test_unmatched_category_is_only_a_coarse_hint(self):
        classify = working_oomp_populate_category.unmatched_category
        for reference, library, category in [['U1', 'MCU_Microchip_ATmega:ATmega328P-A', 'mcu'], ['U2', 'Memory_Flash:W25Q', 'memory'], ['U3', '74xx:74HC595', 'logic'], ['C10', 'Device:C', 'capacitor'], ['CON2', '', 'connector'], ['U4', 'Custom:Unknown', 'ic'], ['REF1', '', 'other']]:
            self.assertEqual(classify(reference, library), category)

    def test_normal_generation_preserves_pngs_and_updates_navigation(self):
        with patch.object(action_generate.working_oomp_populate, 'main') as populate, patch.object(action_generate.working_oomp, 'main') as define, patch.object(action_generate.action_generate_navigation, 'generate') as navigation, patch.object(action_generate, 'run_actions', return_value=(3, 0)) as actions, patch('kicad_agents.kicad_library_agent.package_libraries'):
            action_generate.generate('electronic_resistor_0603_2000_ohm')
        filters = ['electronic_resistor_0603_2000_ohm']
        populate.assert_called_once_with()
        define.assert_called_once_with(filter=filters, regenerate_pngs=False)
        navigation.assert_called_once_with(filter_text='electronic_resistor_0603_2000_ohm')
        actions.assert_called_once_with(filter_text=filters, regenerate_pngs=False, honour_normal_gates=True)

    def test_name_and_datasheet_geometry_survive_default_generation(self):
        option = {'taxonomy_1': 'electronic', 'taxonomy_2': 'ic', 'taxonomy_3': 'amplifier', 'taxonomy_4': 'operational_single', 'taxonomy_5': 'sot_23_5', 'name_readable_override': 'Example op amp', 'ic_dimensions_mm': {'body_length': 3.01, 'body_height': 1.15}}
        for _ in range(2):
            working_oomp_populate_svg.add_svg_details(option)
            self.assertEqual(option['ic_dimensions_mm']['body_length'], 3.01)
            self.assertEqual(option['ic_dimensions_mm']['body_height'], 1.15)
            self.assertEqual(option['ic_dimensions_mm']['pin_pitch'], 0.95)
        self.assertEqual(readable_name(option), 'Example op amp')
if __name__ == '__main__':
    unittest.main()
