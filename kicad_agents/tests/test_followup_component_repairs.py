import unittest
from pathlib import Path

import yaml

import working_oomp_populate_led_extra
import working_oomp_populate_unmatched_extra
from kicad_agents.oomp_matching_agent import proposed_oomp_id


ROOT = Path(__file__).resolve().parents[2]


class FollowupComponentRepairTests(unittest.TestCase):
    def load_part(self, part_id):
        return yaml.safe_load((ROOT / "parts" / part_id / "working.yaml").read_text(encoding="utf-8"))

    def test_lsm9ds1_pinout_matches_st_table(self):
        part = self.load_part("electronic_sensor_imu_lga_24_st_lsm9ds1tr")
        expected = {
            1: "VDDIO", 2: "SCL/SPC", 3: "VDDIO", 4: "SDA/SDI/SDO",
            5: "SDO_A/G", 6: "SDO_M", 7: "CS_A/G", 8: "CS_M",
            9: "DRDY_M", 10: "INT_M", 11: "INT1_A/G", 12: "INT2_A/G",
            13: "DEN_A/G", 14: "RES", 15: "RES", 16: "RES", 17: "RES",
            18: "RES", 19: "GND", 20: "GND", 21: "CAP", 22: "VDD",
            23: "VDD", 24: "C1",
        }
        self.assertEqual({i: part["pins"][f"pin_{i}"]["name"] for i in range(1, 25)}, expected)

    def test_pca9554_pw_pin_eight_to_sixteen_is_not_shifted(self):
        part = self.load_part("electronic_ic_tssop_16_logic_io_expander_texas_instruments_pca9554pw")
        self.assertEqual(
            [part["pins"][f"pin_{i}"]["name"] for i in range(8, 17)],
            ["VSS", "P4", "P5", "P6", "P7", "INT", "SCL", "SDA", "VDD"],
        )

    def test_easyc_has_four_contacts_and_all_mechanical_views(self):
        part_id = "electronic_connector_easyc_1_25_mm_pitch_surface_mount_right_angle_4_pin_jst_sm04b_gh_tf"
        part = self.load_part(part_id)
        self.assertEqual(part["connector_dimensions_mm"]["pitch"], 1.25)
        self.assertEqual(len(part["pins"]), 4)
        data = ROOT / "parts" / part_id / "data"
        for view in ("working_svg_top", "working_svg_bottom", "working_svg_side"):
            self.assertTrue((data / f"{view}.svg").is_file())
            self.assertGreater((data / f"{view}.svg").stat().st_size, 0)

    def test_non_applicable_jumper_features_have_no_reconstructed_folders(self):
        root = ROOT / "parts/oomp_project_github_sparkfun_spark_fun_qwiic_directional_pad_qwiic_directional_pad_current/data/generated_data/components"
        for reference in ("JP1", "JP2", "JP3"):
            self.assertFalse((root / reference).exists())

    def test_buspirate_j302_canonical_rotation_is_corrected(self):
        pcb = ROOT / "parts/oomp_project_github_dangerousprototypes_buspirate5_hardware_5_rev10a/data/kicad_file.kicad_pcb"
        original = ROOT / "parts/oomp_project_github_dangerousprototypes_buspirate5_hardware_5_rev10a/data/original/kicad_file.kicad_pcb"
        self.assertIn('(at 129.9 116.82 180)', pcb.read_text(encoding="utf-8"))
        self.assertIn('(at 129.9 116.82)', original.read_text(encoding="utf-8"))

    def test_shared_package_repairs_use_datasheet_envelopes(self):
        ids = [
            "electronic_sensor_pressure_temperature_lga_10_bosch_bmp388",
            "electronic_sensor_accelerometer_lga_14_analog_devices_adxl345",
            "electronic_sensor_accelerometer_lga_16_st_lis3dhtr",
            "electronic_sensor_particulate_matter_module_bosch_bmv080",
            "electronic_ic_qfn_24_converter_usb_to_serial_converter_wch_ch342f",
            "electronic_resistor_1210_0_1_ohm",
            "electronic_crystal_5032_surface_mount_2_pin_8_mhz_20_pf",
            "electronic_crystal_3215_surface_mount_2_pin_32_768_khz_12_5_pf",
            "electronic_connector_u_fl_surface_mount_i_pex_u_fl_r_smt_1",
            "electronic_switch_roller_encoder_through_hole_roller_encoder_switch",
        ]
        extras = {part_id: {} for part_id in ids}
        working_oomp_populate_unmatched_extra.main(extras_dict=extras)

        self.assertEqual(len(extras[ids[0]]["pins"]), 10)
        self.assertEqual(extras[ids[0]]["package_drawing"]["pins"][0][2:4], [0.25, -0.7625])
        self.assertGreater(extras[ids[1]]["package_drawing"]["overall"][1], 3.0)
        self.assertGreater(extras[ids[2]]["package_drawing"]["overall"][0], 3.0)
        self.assertEqual(len(extras[ids[3]]["pins"]), 13)
        self.assertEqual(extras[ids[3]]["pins"]["pin_8"]["name"], "VDDIO")
        ch342_pins = extras[ids[4]]["package_drawing"]["pins"]
        self.assertEqual([round(ch342_pins[i][2], 2) for i in range(6)], [-1.25, -0.75, -0.25, 0.25, 0.75, 1.25])
        self.assertEqual(len(extras[ids[5]]["pins"]), 2)
        self.assertEqual(len(extras[ids[6]]["pins"]), 2)
        self.assertEqual(extras[ids[6]]["dimensions_mm"]["length"], 5.0)
        self.assertEqual(extras[ids[7]]["dimensions_mm"]["length"], 3.2)
        self.assertEqual(len(extras[ids[8]]["pins"]), 3)
        self.assertEqual(len(extras[ids[9]]["pins"]), 4)

    def test_tc33x_family_has_one_surface_mount_drawing(self):
        ids = [
            "electronic_potentiometer_trimmer_through_hole_10_kilo_ohm_bourns_tc33x_2_103e",
            "electronic_potentiometer_trimmer_through_hole_1_mega_ohm_bourns_tc33x_2_105e",
        ]
        extras = {part_id: {} for part_id in ids}
        working_oomp_populate_unmatched_extra.main(extras_dict=extras)
        for part_id in ids:
            self.assertEqual(extras[part_id]["form_factor"], "tc33x_2")
            self.assertEqual(extras[part_id]["mounting"], "surface_mount")
            self.assertEqual(len(extras[part_id]["package_drawing"]["pins"]), 3)

    def test_imported_adxl_and_bottom_green_led_match_canonical_parts(self):
        adxl_component = {
            "reference": "U1",
            "schematic": {"units": [{"library_id": "Sensor_Motion:ADXL343", "properties": {"Value": "ADXL343", "Footprint": "ADXL345 STEMMA QT-import-fps:LGA14"}}]},
            "pcb": {},
        }
        self.assertEqual(proposed_oomp_id(adxl_component), "electronic_sensor_accelerometer_lga_14_analog_devices_adxl343")
        led_component = {
            "reference": "D1",
            "schematic": {"units": [{"library_id": "Device:LED", "properties": {"Value": "Green LED", "Footprint": "SparkFun-LED-import-fps:LED_1206_Bottom_Green"}}]},
            "pcb": {},
        }
        self.assertEqual(proposed_oomp_id(led_component), "electronic_led_1206_bottom_green")
        led = {"electronic_led_1206_bottom_green": {}}
        working_oomp_populate_led_extra.main(extras_dict=led)
        self.assertEqual(len(led["electronic_led_1206_bottom_green"]["pins"]), 2)


if __name__ == "__main__":
    unittest.main()
