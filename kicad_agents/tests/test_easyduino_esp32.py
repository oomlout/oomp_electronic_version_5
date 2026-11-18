import copy
import unittest
from unittest.mock import patch

import working_svg
import working_oomp_populate_ic
import working_oomp_populate_diode
import working_oomp_populate_transistor
import working_oomp_populate_connector
import working_oomp_populate_switch
import working_oomp_populate_extra_detail
from oomp_populate_helper import build_oomp_id
from kicad_agents.oomp_matching_agent import match_component, proposed_oomp_id
from kicad_agents.kicad_library_agent import select_sources


class Esp32PopulationTests(unittest.TestCase):
    MATCHES = {
        "D1": "electronic_diode_tvs_array_sot_143_littelfuse_sp0503bahtg",
        "J1": "electronic_connector_usb_c_surface_mount_16_pin_shou_han_type_c_16pin_2md_073",
        "Q1": "electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050",
        "SW1": "electronic_switch_tactile_surface_mount_xunpu_ts_1088_ar02016",
        "U2": "electronic_ic_microcontroller_wifi_bluetooth_8_mb_flash_esp32_wroom_32e_espressif_esp32_wroom_32e_n8",
        "U3": "electronic_ic_power_management_linear_voltage_regulator_3_3_volt_sot_223_3_advanced_monolithic_systems_ams1117_3_3",
    }

    def setUp(self):
        options = []
        for module in [working_oomp_populate_ic, working_oomp_populate_diode,
                       working_oomp_populate_transistor, working_oomp_populate_connector,
                       working_oomp_populate_switch]:
            module.main(options=options)
        for part in options:
            part["taxonomy_1"] = "electronic"
        working_oomp_populate_extra_detail.main(extras=options)
        self.parts = {build_oomp_id(part): part for part in options}

    def test_verified_board_parts_match_from_component_evidence(self):
        cases = [
            ("D1", "SP0503BAHT", "Package_TO_SOT_SMD:SOT-143", "Power_Protection:SP0503BAHT"),
            ("J1", "USB_C_Receptacle_USB2.0", "Connector_USB:USB_C_Receptacle_G-Switch_GT-USB-7010ASV", "Connector:USB_C_Receptacle_USB2.0"),
            ("Q1", "SS8050", "Package_TO_SOT_SMD:SOT-23W", "Device:Q_NPN_BCE"),
            ("SW1", "SW_Push", "Button_Switch_SMD:SW_Push_SPST_NO_Alps_SKRK", "Switch:SW_Push"),
            ("U2", "ESP32-WROOM-E", "Espressif:ESP32-WROOM-32E", "Espressif:ESP32-WROOM-E"),
            ("U3", "AMS1117-3.3", "Package_TO_SOT_SMD:SOT-223-3_TabPin2", "Regulator_Linear:AMS1117-3.3"),
        ]
        for reference, value, footprint, library_id in cases:
            with self.subTest(reference=reference):
                component = {"reference": reference, "schematic": {"units": [{"library_id": library_id, "properties": {"Value": value, "Footprint": footprint}}]}}
                self.assertEqual(proposed_oomp_id(component), self.MATCHES[reference])

    def test_new_package_rows_are_physical_uniform_scale(self):
        for reference in ["D1", "J1", "Q1", "SW1", "U2", "U3"]:
            with self.subTest(reference=reference):
                part = copy.deepcopy(self.parts[self.MATCHES[reference]])
                self.assertTrue(part["part_number_manufacturer"])
                self.assertTrue(part["part_number_lcsc"].startswith("C"))
                geometry = part["package_drawing"]
                dimensions = working_svg._get_assembly_drawing_dimensions(part)
                with patch.object(working_svg.opsvg, "se"):
                    working_svg._add_component_outline(part, dimensions["outline_width"], dimensions["outline_height"])
                self.assertEqual(len(part["diagram_pin_positions"]), len(geometry["pins"]))
                for drawn, row in zip(part["diagram_pin_positions"], geometry["pins"]):
                    self.assertEqual(drawn["number"], row[0])
                    self.assertAlmostEqual(drawn["pos"][0], row[2] * 10)
                    self.assertAlmostEqual(drawn["pos"][1], row[3] * 10)
                    self.assertAlmostEqual(drawn["size"][0], row[4] * 10)
                    self.assertAlmostEqual(drawn["size"][1], row[5] * 10)

    def test_exact_ordering_codes_and_pinouts(self):
        module = self.parts[self.MATCHES["U2"]]
        self.assertEqual(module["part_number_manufacturer"], "ESP32-WROOM-32E-N8")
        self.assertEqual(len(module["pins"]), 39)
        self.assertEqual(module["pins"]["pin_2"]["name"], "3v3")
        cp2102 = self.parts["electronic_ic_converter_usb_to_serial_converter_qfn_28_5_mm_x_5_mm_silicon_labs_cp2102_gmr"]
        self.assertEqual(len(cp2102["pins"]), 29)
        self.assertEqual(cp2102["pins"]["pin_25"]["name"], "rxd")
        self.assertEqual(cp2102["pins"]["pin_26"]["name"], "txd")

    def test_unverified_project_master_is_not_silently_adopted(self):
        from unittest.mock import Mock
        masters = Mock()
        masters.hand_solder.return_value = ""
        for reference in ["J1", "SW1"]:
            part = self.parts[self.MATCHES[reference]]
            sources, issues = select_sources(part, masters, {"footprints": ["Connector_USB:wrong_manufacturer"]})
            expected = '' if reference == 'J1' else 'Button_Switch_SMD:SW_SPST_TS-1088-xR020'
            self.assertEqual(sources["machine_solder"], expected)
            if reference == 'J1':
                self.assertTrue(issues)
        masters.footprint_path.assert_not_called()
