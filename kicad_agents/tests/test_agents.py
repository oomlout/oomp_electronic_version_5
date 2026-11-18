import re
import tempfile
import unittest
from pathlib import Path
import yaml
from kicad_agents.oomp_matching_agent import OompPartIndex, capacitance_taxonomy, match_component, parse_resistance_ohms
from kicad_agents.component_addition_agent import validate_record
from kicad_agents.pipeline_audit_agent import run_audit
from kicad_agents.sexpr import value
from action_regenerate_all import _is_browser_action
import working_oomp_populate_mounting_hole
import working_oomp_populate_diode
import working_oomp_populate_diode_extra
import working_oomp_populate_connector
import working_oomp_populate_connector_extra
import working_oomp_populate_ferrite_bead
import working_oomp_populate_ferrite_bead_extra
import working_oomp_populate_display
import working_oomp_populate_display_extra
import working_oomp_populate_transistor
import working_oomp_populate_transistor_extra
import working_oomp_populate_ic
import working_oomp_populate_ic_extra
import working_oomp_metadata
import svg_help
REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PARTS_DIRECTORY = REPOSITORY_ROOT / 'parts'
USB_A_PART = PARTS_DIRECTORY / 'electronic_connector_usb_a_surface_mount_4_pin_shenzhen_jing_tuo_jin_electronics_912121a2023s10100'
USB_C_PART = PARTS_DIRECTORY / 'electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12'
USB_A_SOURCE = REPOSITORY_ROOT / 'parts_source' / USB_A_PART.name

class DistributorMetadataTests(unittest.TestCase):

    def test_multiple_lcsc_and_manufacturer_numbers_normalise(self):
        part = {'manufacturer': 'JST', 'part_number_manufacturer': 'SM04B-SRSS-TB', 'part_number_lcsc': 'C160404', 'product_url': 'https://www.lcsc.com/product-detail/C160404.html', 'part_numbers_lcsc': [{'part_number': 'C160404', 'product_name': 'SM04B-SRSS-TB(LF)(SN)'}, {'part_number': '160404', 'product_name': 'duplicate should be dropped'}, {'part_number': 'C999999'}], 'part_numbers_manufacturer': [{'manufacturer': 'SparkFun', 'part_number': 'PRT-14417'}, {'manufacturer': 'JST', 'part_number': 'SM04B-SRSS-TB'}]}
        working_oomp_metadata.add_readable_metadata([part])
        lcsc_entries = [entry for entry in part['distributors'] if entry['key'] == 'lcsc']
        self.assertEqual([(entry['part_number'], entry.get('product_name', '')) for entry in lcsc_entries], [('C160404', 'SM04B-SRSS-TB(LF)(SN)'), ('C999999', '')])
        self.assertEqual(lcsc_entries[0]['url'], 'https://www.lcsc.com/product-detail/C160404.html')
        self.assertEqual(lcsc_entries[1]['url'], 'https://www.lcsc.com/product-detail/C999999.html')
        self.assertEqual(part['manufacturers'], [{'manufacturer': 'SparkFun', 'part_number': 'PRT-14417'}, {'manufacturer': 'JST', 'part_number': 'SM04B-SRSS-TB'}])

    def test_singular_fields_become_primary_entries(self):
        part = {'part_number_lcsc': 'C2765186', 'part_number_manufacturer': 'TYPE-C 16PIN 2MD(073)'}
        working_oomp_metadata.add_readable_metadata([part])
        self.assertEqual(part['distributors'][0]['key'], 'lcsc')
        self.assertEqual(part['distributors'][0]['part_number'], 'C2765186')
        self.assertEqual(part['manufacturers'], [{'manufacturer': '', 'part_number': 'TYPE-C 16PIN 2MD(073)'}])
        empty = {}
        working_oomp_metadata.add_readable_metadata([empty])
        self.assertEqual(empty['distributors'], [])
        self.assertEqual(empty['manufacturers'], [])

class AssemblyStrokeTests(unittest.TestCase):

    def test_stroke_widths_are_constant_regardless_of_canvas_size(self):
        small = '<svg viewBox="0 0 3 3"><rect stroke-width="0.8"/><rect stroke-width="0.6"/></svg>'
        large = '<svg viewBox="0 0 30 30"><rect stroke-width="0.8"/><rect stroke-width="0.6"/></svg>'
        small_widths = re.findall('stroke-width="[^"]+"', svg_help._scale_assembly_strokes(small))
        large_widths = re.findall('stroke-width="[^"]+"', svg_help._scale_assembly_strokes(large))
        self.assertEqual(small_widths, large_widths)
        self.assertEqual(small_widths, ['stroke-width="0.0716"', 'stroke-width="0.0537"'])

class MatchingAgentTests(unittest.TestCase):

    def test_normalizes_engineering_values(self):
        self.assertEqual(parse_resistance_ohms('5k1'), 5100)
        self.assertEqual(parse_resistance_ohms('2.2k'), 2200)
        self.assertEqual(parse_resistance_ohms('100k'), 100000)
        self.assertEqual(parse_resistance_ohms('0R2'), 0.2)
        self.assertEqual(capacitance_taxonomy('10n'), '10_nano_farad')
        self.assertEqual(capacitance_taxonomy('4u7'), '4_7_micro_farad')

    def test_exact_basic_component_match(self):
        index = OompPartIndex(PARTS_DIRECTORY)
        component = {'reference': 'R4', 'schematic': {'units': [{'library_id': 'Device:R', 'on_board': True, 'properties': {'Value': '2k2', 'Footprint': 'Resistor_SMD:R_0402'}}]}, 'pcb': {'library_id': 'R_0402'}}
        result = match_component(index, component)
        self.assertEqual(result['status'], 'matched')
        self.assertEqual(result['oomp_id'], 'electronic_resistor_0402_2200_ohm')

    def test_onsemi_1n4148wt_is_an_exact_two_pin_diode_definition(self):
        options = []
        working_oomp_populate_diode.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == '1n4148wt'))
        self.assertEqual(option['taxonomy_3'], 'switching')
        self.assertEqual(option['taxonomy_4'], 'sod_523f')
        self.assertEqual(option['taxonomy_14'], 'onsemi')
        part_id = 'electronic_diode_switching_sod_523f_onsemi_1n4148wt'
        extras = {part_id: dict(option)}
        working_oomp_populate_diode_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_lcsc'], 'C232841')
        self.assertEqual(extras[part_id]['pins']['pin_1']['name'], 'cathode')
        self.assertEqual(extras[part_id]['pins']['pin_2']['name'], 'anode')

    def test_bas40t_05_keeps_exact_bare_mpn_without_invented_lcsc_code(self):
        options = []
        working_oomp_populate_diode.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'bas40t_05'))
        self.assertEqual(option['taxonomy_3'], 'schottky_dual_common_cathode')
        self.assertEqual(option['taxonomy_4'], 'sot_523')
        self.assertEqual(option['taxonomy_14'], 'diodes_incorporated')
        part_id = 'electronic_diode_schottky_dual_common_cathode_sot_523_diodes_incorporated_bas40t_05'
        extras = {part_id: dict(option)}
        working_oomp_populate_diode_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'BAS40T-05')
        self.assertNotIn('part_number_lcsc', extras[part_id])
        self.assertEqual(extras[part_id]['pins']['pin_3']['name'], 'common_cathode')

    def test_kinghelm_three_pin_socket_has_exact_mpn_and_lcsc_code(self):
        options = []
        working_oomp_populate_connector.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'kh_2_54fh_1x3p_h8_5'))
        self.assertEqual(option['taxonomy_3'], 'header')
        self.assertEqual(option['taxonomy_6'], '3_pin')
        self.assertEqual(option['taxonomy_7'], 'socket')
        self.assertEqual(option['taxonomy_14'], 'kinghelm')
        part_id = 'electronic_connector_header_2_54_mm_pitch_through_hole_3_pin_socket_kinghelm_kh_2_54fh_1x3p_h8_5'
        extras = {part_id: dict(option)}
        working_oomp_populate_connector_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'KH-2.54FH-1X3P-H8.5')
        self.assertEqual(extras[part_id]['part_number_lcsc'], 'C2932670')
        self.assertEqual(extras[part_id]['connector_dimensions_mm']['body_length'], 7.62)
        self.assertEqual(extras[part_id]['pins']['pin_3']['number'], '3')

    def test_tdk_mmz2012_ferrite_bead_has_exact_mpn_and_lcsc_code(self):
        options = []
        working_oomp_populate_ferrite_bead.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'mmz2012r150at000'))
        self.assertEqual(option['taxonomy_3'], '0805')
        self.assertEqual(option['taxonomy_4'], '15_ohm')
        self.assertEqual(option['taxonomy_5'], '1_5_amp')
        self.assertEqual(option['taxonomy_14'], 'tdk')
        part_id = 'electronic_ferrite_bead_0805_15_ohm_1_5_amp_tdk_mmz2012r150at000'
        extras = {part_id: dict(option)}
        working_oomp_populate_ferrite_bead_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'MMZ2012R150AT000')
        self.assertEqual(extras[part_id]['part_number_lcsc'], 'C275464')
        self.assertEqual(extras[part_id]['electrical']['maximum_dc_resistance'], '0.05 ohm')
        self.assertEqual(extras[part_id]['pins']['pin_2']['number'], '2')

    def test_qt200h1201_display_has_exact_mpn_and_no_invented_lcsc_code(self):
        options = []
        working_oomp_populate_display.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'qt200h1201'))
        self.assertEqual(option['taxonomy_3'], 'tft')
        self.assertEqual(option['taxonomy_4'], '2_inch')
        self.assertEqual(option['taxonomy_8'], '12_pin')
        self.assertEqual(option['taxonomy_14'], 'szhtc')
        part_id = 'electronic_display_tft_2_inch_240_x_320_pixel_ips_spi_12_pin_szhtc_qt200h1201'
        extras = {part_id: dict(option)}
        working_oomp_populate_display_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'QT200H1201')
        self.assertNotIn('part_number_lcsc', extras[part_id])
        self.assertEqual(extras[part_id]['controller'], 'ST7789V')
        self.assertEqual(extras[part_id]['pins']['pin_12']['name'], 'gnd')
        self.assertEqual(extras[part_id]['display_dimensions_mm']['active_width'], 30.6)

    def test_cbi_mmbt7002k_has_exact_identity_limits_and_pinout(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'mmbt7002k'))
        self.assertEqual(option['taxonomy_3'], 'sot_23')
        self.assertEqual(option['taxonomy_5'], 'n_channel')
        self.assertEqual(option['taxonomy_14'], 'cbi')
        part_id = 'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_300_milliamp_cbi_mmbt7002k'
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'MMBT7002K')
        self.assertEqual(extras[part_id]['part_number_lcsc'], 'C2879714')
        self.assertEqual(extras[part_id]['electrical']['maximum_drain_source_voltage'], '60 V')
        self.assertEqual(extras[part_id]['pins']['pin_1']['name'], 'gate')
        self.assertEqual(extras[part_id]['pins']['pin_2']['name'], 'source')
        self.assertEqual(extras[part_id]['pins']['pin_3']['name'], 'drain')

    def test_generic_2n7002_is_separate_from_exact_supplier_variants(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == '2n7002'))
        self.assertEqual(option['taxonomy_3'], 'sot_23')
        self.assertEqual(option['taxonomy_5'], 'n_channel')
        self.assertEqual(option['taxonomy_14'], '')
        part_id = 'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_2n7002'
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_generic'], '2N7002')
        self.assertNotIn('part_number_lcsc', extras[part_id])
        self.assertNotIn('part_number_manufacturer', extras[part_id])
        self.assertEqual(extras[part_id]['pins']['pin_1']['name'], 'gate')
        self.assertEqual(extras[part_id]['pins']['pin_2']['name'], 'source')
        self.assertEqual(extras[part_id]['pins']['pin_3']['name'], 'drain')
        self.assertEqual(extras[part_id]['transistor_dimensions_mm']['body_length_maximum'], 3.0)
        self.assertEqual(extras[part_id]['transistor_dimensions_mm']['lead_length_maximum'], 0.45)
        self.assertIn('generic', extras[part_id]['name_readable_override'])
        self.assertIn('Representative', extras[part_id]['datasheet_note'])

    def test_nexperia_2n7002_preserves_exact_ordering_suffix(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == '2n7002_215'))
        self.assertEqual(option['taxonomy_14'], 'nexperia')
        part_id = 'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_300_milliamp_nexperia_2n7002_215'
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        part = extras[part_id]
        self.assertEqual(part['part_number_manufacturer'], '2N7002,215')
        self.assertEqual(part['part_number_manufacturer_nexperia'], '2N7002,215')
        self.assertEqual(part['part_number_lcsc'], 'C65189')
        self.assertNotIn('generic_match', part)
        self.assertNotIn('part_number_generic', part)
        for number, name in [['1', 'gate'], ['2', 'source'], ['3', 'drain']]:
            self.assertEqual(part['pins']['pin_' + number]['name'], name)
        self.assertEqual(part['transistor_dimensions_mm']['body_length_maximum'], 3.0)
        self.assertEqual(part['transistor_dimensions_mm']['lead_length_maximum'], 0.45)
        self.assertIn('solder point 25 C', part['electrical']['maximum_power_dissipation'])
        self.assertEqual(part['kicad']['symbol'], 'Transistor_FET:2N7002')
        self.assertNotEqual(part['kicad']['machine_solder'], part['kicad']['hand_solder'])

    def test_generic_bss138_has_its_own_reference_dimensions(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'bss138'))
        self.assertEqual(option['taxonomy_14'], '')
        part_id = 'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_bss138'
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        part = extras[part_id]
        self.assertEqual(part['part_number_generic'], 'BSS138')
        self.assertNotIn('part_number_manufacturer', part)
        self.assertNotIn('part_number_lcsc', part)
        self.assertIn('Representative onsemi', part['datasheet_note'])
        self.assertEqual(part['package_drawing']['overall'], [2.9, 2.4])
        self.assertEqual(part['transistor_dimensions_mm']['lead_width_nominal'], 0.44)
        self.assertEqual(part['transistor_dimensions_mm']['body_length_maximum'], 3.04)
        for number, name in [['1', 'gate'], ['2', 'source'], ['3', 'drain']]:
            self.assertEqual(part['pins']['pin_' + number]['name'], name)
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / part_id
            directory.mkdir()
            (directory / 'working.yaml').write_text(yaml.safe_dump(part), encoding='utf-8')
            index = OompPartIndex(temporary)
            properties = {'Value': 'BSS138', 'Footprint': 'Package_TO_SOT_SMD:SOT-23'}
            unit = {'library_id': 'Transistor_FET:BSS138', 'on_board': True, 'properties': properties}
            component = {'reference': 'Q1', 'schematic': {'units': [unit]}}
            self.assertEqual(match_component(index, component)['oomp_id'], part_id)
            properties['MPN'] = 'BSS138-13-F'
            self.assertFalse(match_component(index, component)['accepted'])

    def test_onsemi_bss138_keeps_exact_identity_separate_from_generic(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'bss138' and option.get('taxonomy_14') == 'onsemi'))
        part_id = 'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_220_milliamp_onsemi_bss138'
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        part = extras[part_id]
        self.assertEqual(part['manufacturer'], 'onsemi')
        self.assertEqual(part['part_number_manufacturer'], 'BSS138')
        self.assertEqual(part['part_number_manufacturer_onsemi'], 'BSS138')
        self.assertEqual(part['part_number_lcsc'], 'C52895')
        self.assertNotIn('generic_match', part)
        self.assertNotIn('part_number_generic', part)
        self.assertEqual(part['package_drawing']['overall'], [2.9, 2.4])
        self.assertEqual(part['transistor_dimensions_mm']['lead_width_nominal'], 0.44)
        for number, name in [['1', 'gate'], ['2', 'source'], ['3', 'drain']]:
            self.assertEqual(part['pins']['pin_' + number]['name'], name)
        self.assertIn('ambient 25 C', part['electrical']['maximum_continuous_drain_current'])
        self.assertEqual(part['kicad']['symbol'], 'Transistor_FET:BSS138')

    def test_generic_match_requires_value_symbol_package_and_no_exact_identity(self):
        part_id = 'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_2n7002'
        extras = {part_id: {'taxonomy_2': 'transistor', 'taxonomy_3': 'sot_23'}}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / part_id
            directory.mkdir()
            (directory / 'working.yaml').write_text(yaml.safe_dump(extras[part_id]), encoding='utf-8')
            index = OompPartIndex(temporary)
            properties = {'Value': '2N7002', 'Footprint': 'Package_TO_SOT_SMD:SOT-23'}
            unit = {'library_id': 'Transistor_FET:2N7002', 'on_board': True, 'properties': properties}
            component = {'reference': 'Q1', 'schematic': {'units': [unit]}, 'pcb': {'value': '2N7002'}}
            result = match_component(index, component)
            self.assertEqual(result['oomp_id'], part_id)
            self.assertEqual(result['identity_scope'], 'generic_family')
            for field_name, value in [['MPN', '2N7002,215'], ['Manufacturer', 'Nexperia'], ['Value', '2N7002K'], ['Footprint', 'Package_TO_SOT_SMD:SOT-23-5']]:
                original = dict(properties)
                properties[field_name] = value
                self.assertFalse(match_component(index, component)['accepted'])
                properties.clear()
                properties.update(original)
            unit['library_id'] = 'Device:Q_NMOS_DGS'
            self.assertFalse(match_component(index, component)['accepted'])

    def test_cbi_bc2301t_uses_special_order_sot_523_without_wrong_lcsc_code(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'bc2301t_2_8a'))
        self.assertEqual(option['taxonomy_3'], 'sot_523')
        self.assertEqual(option['taxonomy_5'], 'p_channel')
        self.assertEqual(option['taxonomy_14'], 'cbi')
        part_id = 'electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a'
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'BC2301T-2.8A')
        self.assertNotIn('part_number_lcsc', extras[part_id])
        self.assertEqual(extras[part_id]['electrical']['maximum_continuous_drain_current'], '-2.8 A')
        self.assertEqual(extras[part_id]['transistor_dimensions_mm']['body_length_maximum'], 1.7)
        self.assertEqual(extras[part_id]['pins']['pin_1']['name'], 'gate')
        self.assertEqual(extras[part_id]['pins']['pin_2']['name'], 'source')
        self.assertEqual(extras[part_id]['pins']['pin_3']['name'], 'drain')

    def test_diodes_bcm857bs_is_exact_matched_pair_with_ebcebc_pinout(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'bcm857bs_7_f'))
        self.assertEqual(option['taxonomy_3'], 'sot_363_6')
        self.assertEqual(option['taxonomy_4'], 'bipolar')
        self.assertEqual(option['taxonomy_5'], 'pnp')
        self.assertEqual(option['taxonomy_6'], 'dual_matched_pair')
        self.assertEqual(option['taxonomy_14'], 'diodes_incorporated')
        part_id = 'electronic_transistor_sot_363_6_bipolar_pnp_dual_matched_pair_45_volt_100_milliamp_diodes_incorporated_bcm857bs_7_f'
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'BCM857BS-7-F')
        self.assertEqual(extras[part_id]['part_number_lcsc'], 'C105896')
        self.assertEqual(extras[part_id]['pins']['pin_1']['name'], 'emitter_1')
        self.assertEqual(extras[part_id]['pins']['pin_2']['name'], 'base_1')
        self.assertEqual(extras[part_id]['pins']['pin_3']['name'], 'collector_2')
        self.assertEqual(extras[part_id]['pins']['pin_4']['name'], 'emitter_2')
        self.assertEqual(extras[part_id]['pins']['pin_5']['name'], 'base_2')
        self.assertEqual(extras[part_id]['pins']['pin_6']['name'], 'collector_1')
        self.assertEqual(extras[part_id]['electrical']['maximum_base_emitter_voltage_difference'], '2 mV')

    def test_cbi_mmdt3906dw_is_exact_general_purpose_dual_pnp(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'mmdt3906dw'))
        self.assertEqual(option['taxonomy_3'], 'sot_363_6')
        self.assertEqual(option['taxonomy_5'], 'pnp')
        self.assertEqual(option['taxonomy_6'], 'dual_general_purpose')
        self.assertEqual(option['taxonomy_14'], 'cbi')
        part_id = 'electronic_transistor_sot_363_6_bipolar_pnp_dual_general_purpose_40_volt_200_milliamp_cbi_mmdt3906dw'
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'MMDT3906DW')
        self.assertEqual(extras[part_id]['part_number_lcsc'], 'C2836075')
        self.assertEqual(extras[part_id]['marking_code'], 'K3N')
        self.assertEqual(extras[part_id]['pins']['pin_1']['name'], 'emitter_1')
        self.assertEqual(extras[part_id]['pins']['pin_6']['name'], 'collector_1')
        self.assertEqual(extras[part_id]['electrical']['maximum_continuous_collector_current'], '-200 mA')

    def test_gainsil_lmv321_tr_has_exact_identity_pinout_and_dimensions(self):
        options = []
        working_oomp_populate_ic.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'lmv321_tr'))
        self.assertEqual(option['taxonomy_5'], 'sot_23_5')
        self.assertEqual(option['taxonomy_3'], 'amplifier')
        self.assertEqual(option['taxonomy_14'], 'gainsil')
        part_id = 'electronic_ic_amplifier_operational_single_rail_to_rail_input_output_sot_23_5_gainsil_lmv321_tr'
        extras = {part_id: dict(option)}
        working_oomp_populate_ic_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'LMV321-TR')
        self.assertEqual(extras[part_id]['part_number_lcsc'], 'C362273')
        self.assertEqual(extras[part_id]['pins']['pin_1']['name'], 'in_positive')
        self.assertEqual(extras[part_id]['pins']['pin_2']['name'], 'vss')
        self.assertEqual(extras[part_id]['pins']['pin_3']['name'], 'in_negative')
        self.assertEqual(extras[part_id]['pins']['pin_4']['name'], 'output')
        self.assertEqual(extras[part_id]['pins']['pin_5']['name'], 'vdd')
        self.assertEqual(extras[part_id]['ic_dimensions_mm']['body_length_max'], 3.02)
        self.assertEqual(extras[part_id]['electrical']['maximum_supply_voltage'], '5.5 V')

    def test_ti_lmv324ipwr_has_exact_identity_pinout_and_dimensions(self):
        options = []
        working_oomp_populate_ic.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'lmv324ipwr'))
        self.assertEqual(option['taxonomy_5'], 'tssop_14')
        self.assertEqual(option['taxonomy_3'], 'amplifier')
        self.assertEqual(option['taxonomy_14'], 'texas_instruments')
        part_id = 'electronic_ic_amplifier_operational_quad_rail_to_rail_output_tssop_14_texas_instruments_lmv324ipwr'
        extras = {part_id: dict(option)}
        working_oomp_populate_ic_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'LMV324IPWR')
        self.assertEqual(extras[part_id]['part_number_lcsc'], 'C398929')
        self.assertEqual(extras[part_id]['pins']['pin_1']['name'], '1out')
        self.assertEqual(extras[part_id]['pins']['pin_4']['name'], 'vcc+')
        self.assertEqual(extras[part_id]['pins']['pin_11']['name'], 'gnd')
        self.assertEqual(extras[part_id]['pins']['pin_14']['name'], '4out')
        self.assertEqual(extras[part_id]['ic_dimensions_mm']['pin_pitch'], 0.65)
        self.assertEqual(extras[part_id]['electrical']['output_style'], 'rail-to-rail output')

    def test_gainsil_gs321a_tr_meets_precision_offset_target(self):
        options = []
        working_oomp_populate_ic.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'gs321a_tr'))
        self.assertEqual(option['taxonomy_5'], 'sot_23_5')
        self.assertEqual(option['taxonomy_4'], 'operational_single_precision_rail_to_rail_input_output')
        self.assertEqual(option['taxonomy_14'], 'gainsil')
        part_id = 'electronic_ic_amplifier_operational_single_precision_rail_to_rail_input_output_sot_23_5_gainsil_gs321a_tr'
        extras = {part_id: dict(option)}
        working_oomp_populate_ic_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'GS321A-TR')
        self.assertEqual(extras[part_id]['part_number_lcsc'], 'C431318')
        self.assertEqual(extras[part_id]['electrical']['maximum_input_offset_voltage'], '0.4 mV')
        self.assertEqual(extras[part_id]['pins']['pin_1']['name'], 'in_positive')
        self.assertEqual(extras[part_id]['pins']['pin_5']['name'], 'vdd')

    def test_ti_lmv331idbvr_has_open_collector_output_and_exact_pinout(self):
        options = []
        working_oomp_populate_ic.main(options=options)
        option = next((option for option in options if option.get('taxonomy_15') == 'lmv331idbvr'))
        self.assertEqual(option['taxonomy_5'], 'sot_23_5')
        self.assertEqual(option['taxonomy_3'], 'comparator')
        self.assertEqual(option['taxonomy_4'], 'single_open_collector')
        part_id = 'electronic_ic_comparator_single_open_collector_sot_23_5_texas_instruments_lmv331idbvr'
        extras = {part_id: dict(option)}
        working_oomp_populate_ic_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]['part_number_manufacturer'], 'LMV331IDBVR')
        self.assertEqual(extras[part_id]['part_number_lcsc'], 'C34731')
        self.assertEqual(extras[part_id]['electrical']['output_style'], 'open collector')
        self.assertEqual(extras[part_id]['pins']['pin_1']['name'], 'in_positive')
        self.assertEqual(extras[part_id]['pins']['pin_2']['name'], 'gnd')
        self.assertEqual(extras[part_id]['pins']['pin_4']['type'], 'open_collector_output')
        self.assertEqual(extras[part_id]['pins']['pin_5']['name'], 'vcc')

    def test_board_features_and_mounting_holes_are_classified_separately(self):
        index = OompPartIndex(PARTS_DIRECTORY)
        solder_jumper = {'reference': 'SJ1', 'schematic': {'units': [{'on_board': True, 'properties': {'Value': 'SJ2W', 'Footprint': 'Project:SJ_2'}}]}, 'pcb': {'library_id': 'SJ_2'}}
        solder_jumper_result = match_component(index, solder_jumper)
        self.assertEqual(solder_jumper_result['status'], 'not_applicable')
        self.assertFalse(solder_jumper_result['accepted'])
        mounting_hole = {'reference': 'UNK_HOLE_0', 'schematic': {'units': []}, 'pcb': {'library_id': 'dummyfp0', 'is_mounting_hole': True, 'mounting_holes': [{'oomp_id': 'mechanical_mounting_hole_2_mm_round_unplated'}]}}
        mounting_hole_result = match_component(index, mounting_hole)
        self.assertEqual(mounting_hole_result['status'], 'matched')
        self.assertEqual(mounting_hole_result['oomp_id'], 'mechanical_mounting_hole_2_mm_round_unplated')
        dnf_component = {'reference': 'R102', 'schematic': {'units': [{'on_board': True, 'properties': {'Value': 'DNF', 'Footprint': 'Resistor_SMD:R_0402_1005Metric'}}]}, 'pcb': {'library_id': 'Device:R_Small', 'value': 'DNF'}}
        dnf_result = match_component(index, dnf_component)
        self.assertEqual(dnf_result['status'], 'not_applicable')
        self.assertIn('do-not-fit', dnf_result['reasons'][0])
        dnp_component = {'reference': 'C603', 'schematic': {'units': [{'on_board': True, 'properties': {'Value': 'DNP', 'Footprint': 'Capacitor_SMD:C_0402_1005Metric'}}]}, 'pcb': {'library_id': 'Device:C_Small', 'value': 'DNP'}}
        dnp_result = match_component(index, dnp_component)
        self.assertEqual(dnp_result['status'], 'not_applicable')
        self.assertIn('do-not-populate', dnp_result['reasons'][0])
        self.assertEqual(mounting_hole_result['status'], 'matched')
        self.assertEqual(mounting_hole_result['oomp_id'], 'mechanical_mounting_hole_2_mm_round_unplated')

class ProjectPartTests(unittest.TestCase):

    def test_component_addition_record_rejects_ambiguous_identity_fields(self):
        record = {'ledger_id': 'E9999', 'family': 'transistor', 'part_id': 'Electronic Bad Part', 'package': 'sot_23', 'exact_identity': True, 'research': {'manufacturer': '', 'manufacturer_part_number': '', 'lcsc_part_number': '105896', 'browser_sources': [], 'evidence_notes': []}}
        errors, warnings = validate_record(record)
        self.assertGreaterEqual(len(errors), 6)
        self.assertEqual(warnings, [])

    def test_mounting_hole_populator_uses_editable_size_and_style_arrays(self):
        options = []
        working_oomp_populate_mounting_hole.main(options=options)
        self.assertEqual(len(options), 50)
        two_mm_unplated = next((option for option in options if option['taxonomy_3'] == '2_mm' and option['taxonomy_4'] == 'round' and (option['taxonomy_5'] == 'unplated')))
        self.assertEqual(two_mm_unplated['taxonomy_1'], 'mechanical')
        self.assertEqual(two_mm_unplated['hole_diameter_mm'], 2.0)
        self.assertEqual(two_mm_unplated['hole_size_mm'], {'x': 2.0, 'y': 2.0})

class ElectronicPartReadmeTests(unittest.TestCase):

    def test_part_readme_uses_pinout_hero_and_small_previews(self):
        part_directory = PARTS_DIRECTORY / 'electronic_resistor_0402_2200_ohm'
        working = yaml.safe_load((part_directory / 'working.yaml').read_text(encoding='utf-8'))
        library_action = working['oomlout_ai_roboclick_1']['actions'][0]
        self.assertEqual(library_action['file_output'], 'data/kicad/manifest.yaml')
        self.assertEqual(working['oomlout_ai_roboclick_1']['file_test'], 'data/kicad/manifest.yaml')
        preview_action = working['oomlout_ai_roboclick_2']
        preview_actions = preview_action['actions']
        self.assertEqual(preview_action['file_test'], 'data/working_svg_square_pins_300.png')
        svg_action = next((action for action in preview_actions if action.get('file_python') == 'kicad_agents/component_svg_action.py'))
        self.assertEqual(svg_action['command'], 'run_python')
        self.assertEqual(svg_action['part_id'], part_directory.name)
        resize_actions = [action for action in preview_actions if action['command'] == 'image_resize']
        self.assertEqual(len(resize_actions), 11)
        self.assertTrue(all((action['command'] == 'image_resize' for action in resize_actions)))
        self.assertTrue(all((action['maximum_dimension'] == 300 for action in resize_actions)))
        self.assertTrue(all((action['allow_upscale'] is False for action in resize_actions)))
        self.assertTrue(all((action['regenerate_pngs'] is False for action in resize_actions)))
        readme = (part_directory / 'README.md').read_text(encoding='utf-8')
        self.assertIn('![Resistor 2200 Ohm 0402 pinout](data/working_svg_square_pins.svg)', readme)
        self.assertIn('## At a glance', readme)
        self.assertNotIn('## Diagram gallery', readme)
        self.assertNotIn('<img', readme)
        self.assertIn('## Files', readme)
        self.assertIn('![Pinout drawing](data/working_svg_square_pins_300.png)', readme)
        self.assertIn('![Assembly](data/working_svg_assembly_300.png)', readme)
        self.assertIn('![Assembly pinout](data/working_svg_assembly_pins_300.png)', readme)
        self.assertIn('![Outline](data/working_svg_outline_300.png)', readme)
        self.assertNotIn('[Outline drawing](data/working_svg_outline.svg)', readme)
        self.assertNotIn('[View the datasheet](data/datasheet.pdf)', readme)
        from PIL import Image
        preview_files = sorted((part_directory / 'data').glob('working_svg*_300.png'))
        self.assertEqual(len(preview_files), 11)
        for preview_file in preview_files:
            with Image.open(preview_file) as preview_image:
                self.assertLessEqual(max(preview_image.size), 300)

    def test_default_generated_pipeline_has_no_llm_actions_or_direct_http_clients(self):
        audit = run_audit(REPOSITORY_ROOT)
        self.assertEqual(audit['status'], 'pass', audit['findings'])

class RepositoryOrganizationTests(unittest.TestCase):

    def test_readme_local_links_resolve(self):
        from urllib.parse import unquote
        pages = list(PARTS_DIRECTORY.glob('*/README.md'))
        pages.append(REPOSITORY_ROOT / 'README.md')
        pages.extend((REPOSITORY_ROOT / 'navigation').rglob('README.md'))
        missing = []
        for page in pages:
            for target in re.findall('\\]\\(([^)]+)\\)', page.read_text(encoding='utf-8')):
                if target.startswith(('http:', 'https:', '#', 'mailto:')):
                    continue
                relative = unquote(target.split('#')[0])
                if relative and (not (page.parent / relative).exists()):
                    missing.append((str(page.relative_to(REPOSITORY_ROOT)), target))
        self.assertEqual(missing, [])

    def test_pinout_preview_action_exists_with_non_pinout_hero(self):
        for part_id in [USB_C_PART.name, 'mechanical_mounting_hole_3_2_mm_round_unplated']:
            working = yaml.safe_load((PARTS_DIRECTORY / part_id / 'working.yaml').read_text(encoding='utf-8'))
            destinations = []
            for key, block in working.items():
                if str(key).startswith('oomlout_') and isinstance(block, dict):
                    for action in block.get('actions', []):
                        if action.get('command') == 'image_resize':
                            destinations.append(action.get('file_destination'))
            self.assertIn('data/working_svg_square_pins_300.png', destinations)

    def test_migration_preserves_conflicting_files(self):
        from kicad_agents.migrate_part_data_layout import migrate_part_directory
        with tempfile.TemporaryDirectory() as temporary:
            part = Path(temporary) / 'sample_part'
            source = part / 'generated_data' / 'notes.txt'
            destination = part / 'data' / 'generated_data' / 'notes.txt'
            source.parent.mkdir(parents=True)
            destination.parent.mkdir(parents=True)
            source.write_text('legacy notes', encoding='utf-8')
            destination.write_text('new notes', encoding='utf-8')
            with self.assertRaises(FileExistsError):
                migrate_part_directory(part)
            self.assertEqual(source.read_text(encoding='utf-8'), 'legacy notes')
            self.assertEqual(destination.read_text(encoding='utf-8'), 'new notes')

    def test_force_regeneration_does_not_persist_force_flag(self):
        from unittest.mock import patch
        import action_regenerate_all
        with patch.object(action_regenerate_all.working_oomp_populate, 'main') as populate:
            with patch.object(action_regenerate_all.working_oomp, 'main') as define:
                with patch.object(action_regenerate_all, 'migrate_parts', return_value={'items': 0}):
                    with patch.object(action_regenerate_all, 'run_actions', return_value=(1, 0)):
                        with patch('kicad_agents.kicad_library_agent.package_libraries'):
                            action_regenerate_all.regenerate_all(filter_text='sample')
        populate.assert_called_once_with(regenerate_pngs=False, filter='sample')
        define.assert_called_once_with(regenerate_pngs=False, filter='sample')

    def test_migration_keeps_root_board_explorer(self):
        from kicad_agents.migrate_part_data_layout import migrate_part_directory
        with tempfile.TemporaryDirectory() as temporary:
            part = Path(temporary)
            explorer = part / 'board_explorer.html'
            explorer.write_text('standalone explorer', encoding='utf-8')
            self.assertEqual(migrate_part_directory(part), [])
            self.assertEqual(explorer.read_text(encoding='utf-8'), 'standalone explorer')

    def test_part_roots_only_contain_readme_working_explorer_and_data(self):
        allowed_names = ['README.md', 'working.yaml', 'web.yaml', 'data']
        violations = []
        for part_directory in PARTS_DIRECTORY.iterdir():
            if not part_directory.is_dir():
                continue
            for child in part_directory.iterdir():
                if child.name not in allowed_names:
                    violations.append(str(child.relative_to(REPOSITORY_ROOT)))
        self.assertEqual(violations, [])
    def test_navigation_has_parent_children_and_absolute_part_links(self):
        root_navigation = (REPOSITORY_ROOT / 'navigation' / 'README.md').read_text(encoding='utf-8')
        capacitor_navigation = (REPOSITORY_ROOT / 'navigation' / 'electronic' / 'capacitor' / '0402' / 'README.md').read_text(encoding='utf-8')
        self.assertIn('[Electronic](electronic/README.md)', root_navigation)
        self.assertIn('[Up one level](../README.md)', capacitor_navigation)
        self.assertIn('https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts/electronic_capacitor_0402_100_nano_farad', capacitor_navigation)

    def test_readable_name_and_extensible_distributor_link_are_generated(self):
        capacitor = PARTS_DIRECTORY / 'electronic_capacitor_0402_100_nano_farad'
        usb_connector = PARTS_DIRECTORY / 'electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12'
        capacitor_working = yaml.safe_load((capacitor / 'working.yaml').read_text(encoding='utf-8'))
        usb_working = yaml.safe_load((usb_connector / 'working.yaml').read_text(encoding='utf-8'))
        self.assertEqual(capacitor_working['name_readable'], 'Capacitor 100 nF 0402')
        self.assertEqual(usb_working['name_readable'], 'Connector USB-C TYPE-C-31-M-12')
        self.assertEqual(usb_working['link_github'], 'https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts/' + usb_connector.name)
        lcsc = next((row for row in usb_working['distributors'] if row['key'] == 'lcsc'))
        self.assertEqual(lcsc['part_number'], 'C165948')
        self.assertEqual(lcsc['url'], 'https://www.lcsc.com/product-detail/C165948.html')
        self.assertIn('[`C165948`](https://www.lcsc.com/product-detail/C165948.html)', (usb_connector / 'README.md').read_text(encoding='utf-8'))

    def test_full_regeneration_entrypoint_skips_only_browser_actions(self):
        self.assertTrue((REPOSITORY_ROOT / 'action_regenerate_all.bat').is_file())
        self.assertTrue(_is_browser_action({'command': 'run_python', 'file_python': 'browser_research_agent.py'}))
        self.assertFalse(_is_browser_action({'command': 'run_python', 'file_python': 'kicad_agents/interactive_html_bom_action.py'}))
        for command in ['new_chat', 'query', 'add_image', 'ai_file_save']:
            self.assertTrue(_is_browser_action({'command': command}))

    def test_readable_names_keep_capacitance_voltage_and_crystal_load(self):
        from working_oomp_metadata import readable_name
        examples = [[['electronic', 'capacitor', '6_3_mm_diameter_5_4_mm_tall', 'electrolytic', '220_micro_farad', '10_volt'], 'Capacitor 220 uF 10 V Electrolytic 6.3 mm diameter x 5.4 mm tall'], [['electronic', 'capacitor', '3216_avx_a', 'tantalum', '4_7_micro_farad', '16_volt'], 'Capacitor 4.7 uF 16 V Tantalum 3216 AVX A'], [['electronic', 'crystal', '3225', '12_mhz', '20_pf', '4_pin'], 'Crystal 12 MHz 20 pF 3225 4-pin'], [['electronic', 'connector', 'header', '2_54_mm_pitch', 'through_hole', '10_pin'], 'Connector Header 2.54 mm pitch through-hole 10 pin']]
        for taxonomy, expected in examples:
            part = {}
            for index in range(len(taxonomy)):
                part[f'taxonomy_{index + 1}'] = taxonomy[index]
            self.assertEqual(readable_name(part), expected)

class UsbConnectorDiagramTests(unittest.TestCase):

    def test_usb_a_uses_datasheet_dimensions_and_named_pins(self):
        working = yaml.safe_load((USB_A_SOURCE / 'working.yaml').read_text(encoding='utf-8'))
        self.assertEqual(working['dimensions_mm'], {'length': 14.3, 'width': 10.6})
        self.assertEqual(working['connector_dimensions_mm']['contact_count'], 4)
        self.assertEqual(working['connector_dimensions_mm']['contact_pitch'], 2.0)
        self.assertEqual(working['pins']['pin_2']['name'], 'usb_negative')
        self.assertEqual(working['pins']['pin_5']['type'], 'shield')
        assembly_svg = (USB_A_PART / 'data' / 'working_svg_assembly.svg').read_text(encoding='utf-8')
        self.assertIn('width="14.3000mm" height="10.6000mm"', assembly_svg)
        self.assertIn('data-pin-one-identifiers="VBUS|1"', assembly_svg)

    def test_usb_c_uses_datasheet_pinout_and_physical_size(self):
        working = yaml.safe_load((USB_C_PART / 'working.yaml').read_text(encoding='utf-8'))
        self.assertEqual(working['dimensions_mm'], {'length': 8.94, 'width': 7.35})
        dimensions = working['connector_dimensions_mm']
        self.assertEqual(dimensions['pcb_pad_count'], 12)
        self.assertEqual(dimensions['pcb_power_pad_width'], 0.6)
        self.assertEqual(dimensions['pcb_signal_pad_width'], 0.3)
        self.assertEqual(dimensions['pcb_pad_length'], 1.5)
        self.assertEqual(len(working['pins']), 16)
        self.assertEqual(working['pins']['pin_1'], {'name': 'gnd', 'number': 'A1', 'type': 'power'})
        self.assertEqual(working['pins']['pin_16'], {'name': 'gnd', 'number': 'B1', 'type': 'power'})
        readme = (USB_C_PART / 'README.md').read_text(encoding='utf-8')
        self.assertIn('## Datasheet', readme)
        self.assertIn('[View the datasheet](data/datasheet.pdf)', readme)
        self.assertIn('(data/working_svg_top.svg)', readme)
        self.assertIn('(data/working_svg_top_300.png)', readme)
        self.assertIn('(data/working_svg_bottom_300.png)', readme)
        self.assertIn('(data/working_svg_side_300.png)', readme)
        pinout_svg = (USB_C_PART / 'data' / 'working_svg_square_pins.svg').read_text(encoding='utf-8')
        self.assertIn('Connector USB-C', pinout_svg)
        self.assertIn('TYPE-C-31-M-12', pinout_svg)
        self.assertIn('A1 gnd', pinout_svg)
        self.assertIn('B1 gnd', pinout_svg)
        self.assertNotIn('>pin 1<', pinout_svg)
        assembly_svg = (USB_C_PART / 'data' / 'working_svg_assembly.svg').read_text(encoding='utf-8')
        self.assertIn('width="8.9400" height="7.3500"', assembly_svg)
        self.assertEqual(assembly_svg.count('width="0.6000"'), 4)
        self.assertEqual(assembly_svg.count('width="0.3000"'), 8)
        assembly_pins_svg = (USB_C_PART / 'data' / 'working_svg_assembly_pins.svg').read_text(encoding='utf-8')
        self.assertEqual(assembly_pins_svg.count('</text>'), 12)
        self.assertIn('>gnd</text>', assembly_pins_svg)
        self.assertIn('>vbus</text>', assembly_pins_svg)
        self.assertIn('>cc1</text>', assembly_pins_svg)
        self.assertIn('transform="rotate(-90.000', assembly_pins_svg)
        connector_view_names = ['top', 'bottom', 'side']
        for connector_view_name in connector_view_names:
            self.assertTrue((USB_C_PART / 'data' / f'working_svg_{connector_view_name}.svg').is_file())
            self.assertTrue((USB_C_PART / 'data' / f'working_svg_{connector_view_name}.png').is_file())
