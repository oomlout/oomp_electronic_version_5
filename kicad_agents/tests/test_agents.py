import json
import re
import tempfile
import unittest
from pathlib import Path

import yaml

from kicad_agents.kicad_processing_agent import process_project
from kicad_agents.oomp_matching_agent import (
    OompPartIndex,
    capacitance_taxonomy,
    match_component,
    parse_resistance_ohms,
)
from kicad_agents.project_summary_agent import _orientation_rotation
from kicad_agents.browser_research_agent import (
    build_browser_research_queue,
    import_browser_datasheet,
)
from kicad_agents.component_addition_agent import validate_record
from kicad_agents.pipeline_audit_agent import run_audit
from kicad_agents.sexpr import children, load, tag, value
import working_oomp_populate_project
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


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_PROJECT = REPOSITORY_ROOT / "project" / "electrolama" / "pt1"
SAMPLE_SCHEMATIC = SAMPLE_PROJECT / "git" / "pt1" / "pcba" / "Rev A2" / "pt1-RevA2.kicad_sch"
PARTS_DIRECTORY = REPOSITORY_ROOT / "parts"
PROJECT_PART = PARTS_DIRECTORY / "oomp_project_github_electrolama_pt1_current"
BUS_PIRATE_PART = PARTS_DIRECTORY / "oomp_project_github_dangerousprototypes_buspirate5_hardware_5_rev10a"
USB_A_PART = PARTS_DIRECTORY / "electronic_connector_usb_a_surface_mount_4_pin_shenzhen_jing_tuo_jin_electronics_912121a2023s10100"
USB_C_PART = PARTS_DIRECTORY / "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12"
USB_A_SOURCE = REPOSITORY_ROOT / "parts_source" / USB_A_PART.name
USB_C_SOURCE = REPOSITORY_ROOT / "parts_source" / USB_C_PART.name


class SExpressionTests(unittest.TestCase):
    def test_reads_modern_sample_schematic(self):
        root = load(SAMPLE_SCHEMATIC)
        self.assertEqual(tag(root), "kicad_sch")
        self.assertEqual(value(root, "version"), "20260306")
        self.assertEqual(len(children(root, "symbol")), 64)
        self.assertEqual(len(children(root, "wire")), 177)


class MatchingAgentTests(unittest.TestCase):
    def test_normalizes_engineering_values(self):
        self.assertEqual(parse_resistance_ohms("5k1"), 5100)
        self.assertEqual(parse_resistance_ohms("2.2k"), 2200)
        self.assertEqual(parse_resistance_ohms("100k"), 100000)
        self.assertEqual(parse_resistance_ohms("0R2"), 0.2)
        self.assertEqual(capacitance_taxonomy("10n"), "10_nano_farad")
        self.assertEqual(capacitance_taxonomy("4u7"), "4_7_micro_farad")

    def test_exact_basic_component_match(self):
        index = OompPartIndex(PARTS_DIRECTORY)
        component = {
            "reference": "R4",
            "schematic": {
                "units": [
                    {
                        "library_id": "Device:R",
                        "on_board": True,
                        "properties": {"Value": "2k2", "Footprint": "Resistor_SMD:R_0402"},
                    }
                ]
            },
            "pcb": {"library_id": "R_0402"},
        }
        result = match_component(index, component)
        self.assertEqual(result["status"], "matched")
        self.assertEqual(result["oomp_id"], "electronic_resistor_0402_2200_ohm")

    def test_onsemi_1n4148wt_is_an_exact_two_pin_diode_definition(self):
        options = []
        working_oomp_populate_diode.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "1n4148wt"
        )
        self.assertEqual(option["taxonomy_3"], "switching")
        self.assertEqual(option["taxonomy_4"], "sod_523f")
        self.assertEqual(option["taxonomy_14"], "onsemi")

        part_id = "electronic_diode_switching_sod_523f_onsemi_1n4148wt"
        extras = {part_id: dict(option)}
        working_oomp_populate_diode_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_lcsc"], "C232841")
        self.assertEqual(extras[part_id]["pins"]["pin_1"]["name"], "cathode")
        self.assertEqual(extras[part_id]["pins"]["pin_2"]["name"], "anode")

    def test_bas40t_05_keeps_exact_bare_mpn_without_invented_lcsc_code(self):
        options = []
        working_oomp_populate_diode.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "bas40t_05"
        )
        self.assertEqual(option["taxonomy_3"], "schottky_dual_common_cathode")
        self.assertEqual(option["taxonomy_4"], "sot_523")
        self.assertEqual(option["taxonomy_14"], "diodes_incorporated")

        part_id = "electronic_diode_schottky_dual_common_cathode_sot_523_diodes_incorporated_bas40t_05"
        extras = {part_id: dict(option)}
        working_oomp_populate_diode_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "BAS40T-05")
        self.assertNotIn("part_number_lcsc", extras[part_id])
        self.assertEqual(extras[part_id]["pins"]["pin_3"]["name"], "common_cathode")

    def test_kinghelm_three_pin_socket_has_exact_mpn_and_lcsc_code(self):
        options = []
        working_oomp_populate_connector.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "kh_2_54fh_1x3p_h8_5"
        )
        self.assertEqual(option["taxonomy_3"], "header")
        self.assertEqual(option["taxonomy_6"], "3_pin")
        self.assertEqual(option["taxonomy_7"], "socket")
        self.assertEqual(option["taxonomy_14"], "kinghelm")

        part_id = "electronic_connector_header_2_54_mm_pitch_through_hole_3_pin_socket_kinghelm_kh_2_54fh_1x3p_h8_5"
        extras = {part_id: dict(option)}
        working_oomp_populate_connector_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "KH-2.54FH-1X3P-H8.5")
        self.assertEqual(extras[part_id]["part_number_lcsc"], "C2932670")
        self.assertEqual(extras[part_id]["connector_dimensions_mm"]["body_length"], 7.62)
        self.assertEqual(extras[part_id]["pins"]["pin_3"]["number"], "3")

    def test_tdk_mmz2012_ferrite_bead_has_exact_mpn_and_lcsc_code(self):
        options = []
        working_oomp_populate_ferrite_bead.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "mmz2012r150at000"
        )
        self.assertEqual(option["taxonomy_3"], "0805")
        self.assertEqual(option["taxonomy_4"], "15_ohm")
        self.assertEqual(option["taxonomy_5"], "1_5_amp")
        self.assertEqual(option["taxonomy_14"], "tdk")

        part_id = "electronic_ferrite_bead_0805_15_ohm_1_5_amp_tdk_mmz2012r150at000"
        extras = {part_id: dict(option)}
        working_oomp_populate_ferrite_bead_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "MMZ2012R150AT000")
        self.assertEqual(extras[part_id]["part_number_lcsc"], "C275464")
        self.assertEqual(extras[part_id]["electrical"]["maximum_dc_resistance"], "0.05 ohm")
        self.assertEqual(extras[part_id]["pins"]["pin_2"]["number"], "2")

    def test_qt200h1201_display_has_exact_mpn_and_no_invented_lcsc_code(self):
        options = []
        working_oomp_populate_display.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "qt200h1201"
        )
        self.assertEqual(option["taxonomy_3"], "tft")
        self.assertEqual(option["taxonomy_4"], "2_inch")
        self.assertEqual(option["taxonomy_8"], "12_pin")
        self.assertEqual(option["taxonomy_14"], "szhtc")

        part_id = "electronic_display_tft_2_inch_240_x_320_pixel_ips_spi_12_pin_szhtc_qt200h1201"
        extras = {part_id: dict(option)}
        working_oomp_populate_display_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "QT200H1201")
        self.assertNotIn("part_number_lcsc", extras[part_id])
        self.assertEqual(extras[part_id]["controller"], "ST7789V")
        self.assertEqual(extras[part_id]["pins"]["pin_12"]["name"], "gnd")
        self.assertEqual(extras[part_id]["display_dimensions_mm"]["active_width"], 30.6)

    def test_cbi_mmbt7002k_has_exact_identity_limits_and_pinout(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "mmbt7002k"
        )
        self.assertEqual(option["taxonomy_3"], "sot_23")
        self.assertEqual(option["taxonomy_5"], "n_channel")
        self.assertEqual(option["taxonomy_14"], "cbi")

        part_id = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_300_milliamp_cbi_mmbt7002k"
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "MMBT7002K")
        self.assertEqual(extras[part_id]["part_number_lcsc"], "C2879714")
        self.assertEqual(extras[part_id]["electrical"]["maximum_drain_source_voltage"], "60 V")
        self.assertEqual(extras[part_id]["pins"]["pin_1"]["name"], "gate")
        self.assertEqual(extras[part_id]["pins"]["pin_2"]["name"], "source")
        self.assertEqual(extras[part_id]["pins"]["pin_3"]["name"], "drain")

    def test_cbi_bc2301t_uses_special_order_sot_523_without_wrong_lcsc_code(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "bc2301t_2_8a"
        )
        self.assertEqual(option["taxonomy_3"], "sot_523")
        self.assertEqual(option["taxonomy_5"], "p_channel")
        self.assertEqual(option["taxonomy_14"], "cbi")

        part_id = "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a"
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "BC2301T-2.8A")
        self.assertNotIn("part_number_lcsc", extras[part_id])
        self.assertEqual(extras[part_id]["electrical"]["maximum_continuous_drain_current"], "-2.8 A")
        self.assertEqual(extras[part_id]["transistor_dimensions_mm"]["body_length_maximum"], 1.7)
        self.assertEqual(extras[part_id]["pins"]["pin_1"]["name"], "gate")
        self.assertEqual(extras[part_id]["pins"]["pin_2"]["name"], "source")
        self.assertEqual(extras[part_id]["pins"]["pin_3"]["name"], "drain")

    def test_diodes_bcm857bs_is_exact_matched_pair_with_ebcebc_pinout(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "bcm857bs_7_f"
        )
        self.assertEqual(option["taxonomy_3"], "sot_363_6")
        self.assertEqual(option["taxonomy_4"], "bipolar")
        self.assertEqual(option["taxonomy_5"], "pnp")
        self.assertEqual(option["taxonomy_6"], "dual_matched_pair")
        self.assertEqual(option["taxonomy_14"], "diodes_incorporated")

        part_id = "electronic_transistor_sot_363_6_bipolar_pnp_dual_matched_pair_45_volt_100_milliamp_diodes_incorporated_bcm857bs_7_f"
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "BCM857BS-7-F")
        self.assertEqual(extras[part_id]["part_number_lcsc"], "C105896")
        self.assertEqual(extras[part_id]["pins"]["pin_1"]["name"], "emitter_1")
        self.assertEqual(extras[part_id]["pins"]["pin_2"]["name"], "base_1")
        self.assertEqual(extras[part_id]["pins"]["pin_3"]["name"], "collector_2")
        self.assertEqual(extras[part_id]["pins"]["pin_4"]["name"], "emitter_2")
        self.assertEqual(extras[part_id]["pins"]["pin_5"]["name"], "base_2")
        self.assertEqual(extras[part_id]["pins"]["pin_6"]["name"], "collector_1")
        self.assertEqual(extras[part_id]["electrical"]["maximum_base_emitter_voltage_difference"], "2 mV")

    def test_cbi_mmdt3906dw_is_exact_general_purpose_dual_pnp(self):
        options = []
        working_oomp_populate_transistor.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "mmdt3906dw"
        )
        self.assertEqual(option["taxonomy_3"], "sot_363_6")
        self.assertEqual(option["taxonomy_5"], "pnp")
        self.assertEqual(option["taxonomy_6"], "dual_general_purpose")
        self.assertEqual(option["taxonomy_14"], "cbi")

        part_id = "electronic_transistor_sot_363_6_bipolar_pnp_dual_general_purpose_40_volt_200_milliamp_cbi_mmdt3906dw"
        extras = {part_id: dict(option)}
        working_oomp_populate_transistor_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "MMDT3906DW")
        self.assertEqual(extras[part_id]["part_number_lcsc"], "C2836075")
        self.assertEqual(extras[part_id]["marking_code"], "K3N")
        self.assertEqual(extras[part_id]["pins"]["pin_1"]["name"], "emitter_1")
        self.assertEqual(extras[part_id]["pins"]["pin_6"]["name"], "collector_1")
        self.assertEqual(extras[part_id]["electrical"]["maximum_continuous_collector_current"], "-200 mA")

    def test_gainsil_lmv321_tr_has_exact_identity_pinout_and_dimensions(self):
        options = []
        working_oomp_populate_ic.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "lmv321_tr"
        )
        self.assertEqual(option["taxonomy_3"], "sot_23_5")
        self.assertEqual(option["taxonomy_4"], "amplifier")
        self.assertEqual(option["taxonomy_14"], "gainsil")

        part_id = "electronic_ic_sot_23_5_amplifier_operational_single_rail_to_rail_input_output_gainsil_lmv321_tr"
        extras = {part_id: dict(option)}
        working_oomp_populate_ic_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "LMV321-TR")
        self.assertEqual(extras[part_id]["part_number_lcsc"], "C362273")
        self.assertEqual(extras[part_id]["pins"]["pin_1"]["name"], "in_positive")
        self.assertEqual(extras[part_id]["pins"]["pin_2"]["name"], "vss")
        self.assertEqual(extras[part_id]["pins"]["pin_3"]["name"], "in_negative")
        self.assertEqual(extras[part_id]["pins"]["pin_4"]["name"], "output")
        self.assertEqual(extras[part_id]["pins"]["pin_5"]["name"], "vdd")
        self.assertEqual(extras[part_id]["ic_dimensions_mm"]["body_length_max"], 3.02)
        self.assertEqual(extras[part_id]["electrical"]["maximum_supply_voltage"], "5.5 V")

    def test_ti_lmv324ipwr_has_exact_identity_pinout_and_dimensions(self):
        options = []
        working_oomp_populate_ic.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "lmv324ipwr"
        )
        self.assertEqual(option["taxonomy_3"], "tssop_14")
        self.assertEqual(option["taxonomy_4"], "amplifier")
        self.assertEqual(option["taxonomy_14"], "texas_instruments")

        part_id = "electronic_ic_tssop_14_amplifier_operational_quad_rail_to_rail_output_texas_instruments_lmv324ipwr"
        extras = {part_id: dict(option)}
        working_oomp_populate_ic_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "LMV324IPWR")
        self.assertEqual(extras[part_id]["part_number_lcsc"], "C398929")
        self.assertEqual(extras[part_id]["pins"]["pin_1"]["name"], "1out")
        self.assertEqual(extras[part_id]["pins"]["pin_4"]["name"], "vcc+")
        self.assertEqual(extras[part_id]["pins"]["pin_11"]["name"], "gnd")
        self.assertEqual(extras[part_id]["pins"]["pin_14"]["name"], "4out")
        self.assertEqual(extras[part_id]["ic_dimensions_mm"]["pin_pitch"], 0.65)
        self.assertEqual(extras[part_id]["electrical"]["output_style"], "rail-to-rail output")

    def test_gainsil_gs321a_tr_meets_precision_offset_target(self):
        options = []
        working_oomp_populate_ic.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "gs321a_tr"
        )
        self.assertEqual(option["taxonomy_3"], "sot_23_5")
        self.assertEqual(option["taxonomy_5"], "operational_single_precision_rail_to_rail_input_output")
        self.assertEqual(option["taxonomy_14"], "gainsil")

        part_id = "electronic_ic_sot_23_5_amplifier_operational_single_precision_rail_to_rail_input_output_gainsil_gs321a_tr"
        extras = {part_id: dict(option)}
        working_oomp_populate_ic_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "GS321A-TR")
        self.assertEqual(extras[part_id]["part_number_lcsc"], "C431318")
        self.assertEqual(extras[part_id]["electrical"]["maximum_input_offset_voltage"], "0.4 mV")
        self.assertEqual(extras[part_id]["pins"]["pin_1"]["name"], "in_positive")
        self.assertEqual(extras[part_id]["pins"]["pin_5"]["name"], "vdd")

    def test_ti_lmv331idbvr_has_open_collector_output_and_exact_pinout(self):
        options = []
        working_oomp_populate_ic.main(options=options)
        option = next(
            option
            for option in options
            if option.get("taxonomy_15") == "lmv331idbvr"
        )
        self.assertEqual(option["taxonomy_3"], "sot_23_5")
        self.assertEqual(option["taxonomy_4"], "comparator")
        self.assertEqual(option["taxonomy_5"], "single_open_collector")

        part_id = "electronic_ic_sot_23_5_comparator_single_open_collector_texas_instruments_lmv331idbvr"
        extras = {part_id: dict(option)}
        working_oomp_populate_ic_extra.main(extras_dict=extras)
        self.assertEqual(extras[part_id]["part_number_manufacturer"], "LMV331IDBVR")
        self.assertEqual(extras[part_id]["part_number_lcsc"], "C34731")
        self.assertEqual(extras[part_id]["electrical"]["output_style"], "open collector")
        self.assertEqual(extras[part_id]["pins"]["pin_1"]["name"], "in_positive")
        self.assertEqual(extras[part_id]["pins"]["pin_2"]["name"], "gnd")
        self.assertEqual(extras[part_id]["pins"]["pin_4"]["type"], "open_collector_output")
        self.assertEqual(extras[part_id]["pins"]["pin_5"]["name"], "vcc")

    def test_board_features_and_mounting_holes_are_classified_separately(self):
        index = OompPartIndex(PARTS_DIRECTORY)
        solder_jumper = {
            "reference": "SJ1",
            "schematic": {
                "units": [
                    {
                        "on_board": True,
                        "properties": {"Value": "SJ2W", "Footprint": "Project:SJ_2"},
                    }
                ]
            },
            "pcb": {"library_id": "SJ_2"},
        }
        solder_jumper_result = match_component(index, solder_jumper)
        self.assertEqual(solder_jumper_result["status"], "not_applicable")
        self.assertFalse(solder_jumper_result["accepted"])

        mounting_hole = {
            "reference": "UNK_HOLE_0",
            "schematic": {"units": []},
            "pcb": {
                "library_id": "dummyfp0",
                "is_mounting_hole": True,
                "mounting_holes": [
                    {"oomp_id": "mechanical_mounting_hole_2_mm_round_unplated"}
                ],
            },
        }
        mounting_hole_result = match_component(index, mounting_hole)
        self.assertEqual(mounting_hole_result["status"], "matched")
        self.assertEqual(
            mounting_hole_result["oomp_id"],
            "mechanical_mounting_hole_2_mm_round_unplated",
        )


class ProcessingAgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary_directory = tempfile.TemporaryDirectory()
        cls.output_directory = Path(cls.temporary_directory.name) / "generated_data"
        cls.project_data, _ = process_project(
            SAMPLE_PROJECT,
            PARTS_DIRECTORY,
            output_directory=cls.output_directory,
        )
        cls.components = {
            component["reference"]: component for component in cls.project_data["components"]
        }

    @classmethod
    def tearDownClass(cls):
        cls.temporary_directory.cleanup()

    def test_project_counts_and_formats(self):
        summary = self.project_data["summary"]
        self.assertEqual(summary["schematic_symbol_count"], 64)
        self.assertEqual(summary["pcb_footprint_count"], 37)
        self.assertEqual(summary["component_count"], 67)
        self.assertEqual(summary["mounting_hole_count"], 9)
        self.assertEqual(summary["dedicated_mounting_hole_count"], 3)
        json.loads((self.output_directory / "project.json").read_text(encoding="utf-8"))
        yaml.safe_load((self.output_directory / "project.yaml").read_text(encoding="utf-8"))

    def test_c1_positions_connectivity_size_and_match(self):
        component = self.components["C1"]
        schematic_unit = component["schematic"]["units"][0]
        self.assertEqual(schematic_unit["position"]["x"], 73.66)
        self.assertEqual(schematic_unit["position"]["y"], 40.64)
        self.assertEqual(schematic_unit["position"]["rotation"], 90.0)
        self.assertEqual(schematic_unit["pins"][0]["position"], {"x": 73.66, "y": 38.1})
        self.assertEqual(schematic_unit["pins"][0]["net"], "VUSB_IN")
        self.assertEqual(schematic_unit["size"]["local_graphics"]["width"], 5.2324)
        self.assertEqual(component["pcb"]["position"]["x"], 149.7511)
        self.assertEqual(component["pcb"]["position"]["y"], 119.1286)
        self.assertEqual(component["oomp"]["oomp_id"], "electronic_capacitor_0402_10_nano_farad")

    def test_pcb_rotation_is_converted_from_kicad_to_svg_coordinates(self):
        j1_position = self.components["J1"]["pcb"]["position"]
        con2_position = self.components["CON2"]["pcb"]["position"]
        self.assertEqual(j1_position["rotation_kicad"], -90.0)
        self.assertEqual(j1_position["rotation"], 90.0)
        self.assertEqual(con2_position["rotation_kicad"], -90.0)
        self.assertEqual(con2_position["rotation"], 90.0)

        con2_pads = self.components["CON2"]["pcb"]["pads"]
        con2_ground = next(pad for pad in con2_pads if pad["number"] == "GND@1")
        self.assertEqual(con2_ground["position"], {"x": 145.7561, "y": 96.7536})

    def test_mounting_holes_retain_drill_plating_and_positions(self):
        holes = self.project_data["mounting_holes"]
        self.assertEqual(len(holes), 9)

        standalone_hole = self.components["UNK_HOLE_0"]
        self.assertTrue(standalone_hole["pcb"]["is_mounting_hole"])
        self.assertEqual(
            standalone_hole["oomp"]["oomp_id"],
            "mechanical_mounting_hole_2_mm_round_unplated",
        )
        standalone_record = standalone_hole["pcb"]["mounting_holes"][0]
        self.assertEqual(standalone_record["drill_size"]["diameter"], 2.0)
        self.assertEqual(standalone_record["plating"], "unplated")
        self.assertEqual(standalone_record["position"], {"x": 141.7511, "y": 93.3786})

        usb_a_holes = self.components["CON3"]["pcb"]["mounting_holes"]
        self.assertEqual(len(usb_a_holes), 2)
        self.assertTrue(all(hole["plating"] == "plated" for hole in usb_a_holes))
        self.assertTrue(all(hole["drill_size"]["diameter"] == 0.8 for hole in usb_a_holes))

        header_holes = self.components["J1"]["pcb"]["mounting_holes"]
        self.assertEqual(header_holes, [])
        mounting_hole_items = self.project_data["mounting_hole_items"]
        self.assertEqual(len(mounting_hole_items), 9)
        self.assertEqual([item["reference"] for item in mounting_hole_items], [f"MH{number}" for number in range(1, 10)])
        self.assertTrue(all(item["classification"]["taxonomy_path"][0:2] == ["mechanical", "mounting_hole"] for item in mounting_hole_items))
        self.assertTrue((self.output_directory / "components" / "MH1" / "oomp" / "working.yaml").is_file())
        self.assertTrue((self.output_directory / "mounting_holes.json").is_file())
        self.assertTrue((self.output_directory / "mounting_holes.yaml").is_file())

    def test_component_folder_contract_and_oomp_copy(self):
        component_directory = self.output_directory / "components" / "C1"
        expected_files = [
            component_directory / "component.json",
            component_directory / "component.yaml",
            component_directory / "schematic" / "working.yaml",
            component_directory / "schematic" / "size.yaml",
            component_directory / "pcb" / "working.yaml",
            component_directory / "pcb" / "size.yaml",
            component_directory / "oomp" / "match.yaml",
            component_directory / "oomp" / "working.yaml",
        ]
        for expected_file in expected_files:
            self.assertTrue(expected_file.is_file(), expected_file)
        copied = component_directory / "oomp" / "working.yaml"
        source = PARTS_DIRECTORY / "electronic_capacitor_0402_10_nano_farad" / "working.yaml"
        self.assertEqual(copied.read_bytes(), source.read_bytes())

    def test_unmatched_and_non_physical_are_separate(self):
        unmatched = json.loads((self.output_directory / "unmatched_parts.json").read_text(encoding="utf-8"))
        unmatched_references = {component["reference"] for component in unmatched["components"]}
        self.assertIn("IC1", unmatched_references)
        self.assertNotIn("#GND1", unmatched_references)
        self.assertEqual(self.components["#GND1"]["oomp"]["status"], "not_applicable")


class ProjectPartTests(unittest.TestCase):
    def test_browser_research_queue_is_explicit_and_browser_only(self):
        project_data = {
            "components": [
                {
                    "reference": "U1",
                    "pcb": {
                        "value": "example123",
                        "library_id": "Package_SO:SOIC-8",
                        "exclude_from_bom": False,
                    },
                    "oomp": {
                        "status": "unmatched",
                        "inferred": {"mpn": "EXAMPLE123"},
                        "candidates": [],
                    },
                },
                {
                    "reference": "C1",
                    "pcb": {
                        "value": "DNF",
                        "library_id": "Capacitor_SMD:C_0402_1005Metric",
                        "exclude_from_bom": False,
                    },
                    "oomp": {"status": "unmatched"},
                },
            ]
        }
        queue = build_browser_research_queue(project_data)
        self.assertEqual(queue["task_count"], 1)
        self.assertEqual(queue["tasks"][0]["references"], ["U1"])
        self.assertIn("https://www.lcsc.com/search?q=", queue["tasks"][0]["browser_urls"]["lcsc_search"])
        self.assertIs(queue["network_policy"]["python_http_clients_allowed"], False)

    def test_browser_datasheet_import_validates_pdf_and_writes_provenance(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            downloaded_file = temporary_path / "download.pdf"
            downloaded_file.write_bytes(b"%PDF-1.7\nexample")
            parts_source_directory = temporary_path / "parts_source"
            destination = import_browser_datasheet(
                "electronic_ic_test",
                downloaded_file,
                "https://example.com/datasheet.pdf",
                parts_source_directory,
            )
            self.assertTrue(destination.is_file())
            provenance = yaml.safe_load((destination.parent / "datasheet_source.yaml").read_text(encoding="utf-8"))
            self.assertEqual(provenance["acquisition_method"], "interactive_browser")
            self.assertEqual(provenance["file_size_bytes"], len(b"%PDF-1.7\nexample"))
            self.assertEqual(len(provenance["sha256"]), 64)
            # Re-importing the exact same browser download is deliberately
            # idempotent so provenance can be repaired after a manual copy.
            second_destination = import_browser_datasheet(
                "electronic_ic_test",
                downloaded_file,
                "https://example.com/datasheet.pdf",
                parts_source_directory,
            )
            self.assertEqual(second_destination, destination)

    def test_component_addition_record_rejects_ambiguous_identity_fields(self):
        record = {
            "ledger_id": "E9999",
            "family": "transistor",
            "part_id": "Electronic Bad Part",
            "package": "sot_23",
            "exact_identity": True,
            "research": {
                "manufacturer": "",
                "manufacturer_part_number": "",
                "lcsc_part_number": "105896",
                "browser_sources": [],
                "evidence_notes": [],
            },
        }
        errors, warnings = validate_record(record)
        self.assertGreaterEqual(len(errors), 6)
        self.assertEqual(warnings, [])

    def test_mounting_hole_populator_uses_editable_size_and_style_arrays(self):
        options = []
        working_oomp_populate_mounting_hole.main(options=options)
        self.assertEqual(len(options), 34)
        two_mm_unplated = next(
            option
            for option in options
            if option["taxonomy_3"] == "2_mm"
            and option["taxonomy_4"] == "round"
            and option["taxonomy_5"] == "unplated"
        )
        self.assertEqual(two_mm_unplated["taxonomy_1"], "mechanical")
        self.assertEqual(two_mm_unplated["hole_diameter_mm"], 2.0)
        self.assertEqual(two_mm_unplated["hole_size_mm"], {"x": 2.0, "y": 2.0})

    def test_project_populator_defaults_to_current_and_allows_version_records(self):
        options = []
        working_oomp_populate_project.main(options=options)
        self.assertEqual(len(options), 2)
        project = next(option for option in options if option["project_github_repository"] == "pt1")
        taxonomy = [project[f"taxonomy_{number}"] for number in range(1, 7)]
        self.assertEqual(taxonomy, ["oomp", "project", "github", "electrolama", "pt1", "current"])
        self.assertEqual(project["project_file_folder"], "pcba/Rev A2")
        self.assertEqual(project["project_file_basename"], "pt1-RevA2")
        bus_pirate = next(option for option in options if option["project_github_repository"] == "buspirate5_hardware")
        bus_taxonomy = [bus_pirate[f"taxonomy_{number}"] for number in range(1, 7)]
        self.assertEqual(
            bus_taxonomy,
            ["oomp", "project", "github", "dangerousprototypes", "buspirate5_hardware", "5_rev10a"],
        )
        self.assertIs(bus_pirate["project_sparse_checkout"], True)
        self.assertEqual(bus_pirate["project_file_folder"], "bus_pirate_pcb/5-REV10A")

    def test_generated_project_part_has_always_run_actions_and_local_assets(self):
        working = yaml.safe_load((PROJECT_PART / "working.yaml").read_text(encoding="utf-8"))
        first_action = working["oomlout_ai_roboclick_1"]
        second_action = working["oomlout_ai_roboclick_2"]
        self.assertEqual(first_action["file_test"], "")
        self.assertEqual(second_action["file_test"], "")
        self.assertEqual(first_action["actions"][0]["command"], "run_python")
        self.assertEqual(second_action["actions"][0]["command"], "run_python")
        self.assertIs(second_action["actions"][0]["regenerate_pngs"], False)
        self.assertEqual(len(second_action["actions"]), 6)
        self.assertEqual(second_action["actions"][1]["file_destination"], "generated_data/src/board_300.png")
        self.assertEqual(second_action["actions"][2]["file_destination"], "generated_data/src/board_pins_300.png")
        self.assertEqual(second_action["actions"][3]["file_destination"], "generated_data/src/board_bottom_300.png")
        self.assertEqual(second_action["actions"][4]["file_destination"], "generated_data/src/board_pins_bottom_300.png")
        self.assertEqual(second_action["actions"][5]["file_destination"], "generated_data/src/board_mechanical_300.png")
        self.assertEqual(
            second_action["actions"][0]["file_output"],
            "generated_data/src/board_pins.png",
        )

        readme = (PROJECT_PART / "README.md").read_text(encoding="utf-8")
        self.assertIn("https://github.com/electrolama/pt1", readme)
        self.assertIn(
            "![PCB component placement](https://raw.githubusercontent.com/oomlout/oomp_electronic_version_5/main/parts/oomp_project_github_electrolama_pt1_current/generated_data/src/board.svg)",
            readme,
        )
        self.assertNotIn("](../", readme)
        self.assertNotIn("project_summary_llm", readme)
        self.assertIn(
            "| References | Quantity | Description | Value | Footprint | OOMP part |",
            readme,
        )
        self.assertIn(
            "https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts/electronic_capacitor_0402_10_nano_farad",
            readme,
        )
        self.assertNotIn("/parts/electronic_capacitor_0402_10_nano_farad/README.md", readme)
        self.assertTrue((PROJECT_PART / "generated_data" / "src" / "board.svg").is_file())
        self.assertTrue((PROJECT_PART / "generated_data" / "src" / "board_pins.svg").is_file())
        self.assertTrue((PROJECT_PART / "generated_data" / "src" / "board_bottom.svg").is_file())
        self.assertTrue((PROJECT_PART / "generated_data" / "src" / "board_pins_bottom.svg").is_file())
        board_png_path = PROJECT_PART / "generated_data" / "src" / "board.png"
        board_300_png_path = PROJECT_PART / "generated_data" / "src" / "board_300.png"
        board_pins_png_path = PROJECT_PART / "generated_data" / "src" / "board_pins.png"
        board_pins_300_png_path = PROJECT_PART / "generated_data" / "src" / "board_pins_300.png"
        board_bottom_png_path = PROJECT_PART / "generated_data" / "src" / "board_bottom.png"
        board_bottom_300_png_path = PROJECT_PART / "generated_data" / "src" / "board_bottom_300.png"
        board_pins_bottom_png_path = PROJECT_PART / "generated_data" / "src" / "board_pins_bottom.png"
        board_pins_bottom_300_png_path = PROJECT_PART / "generated_data" / "src" / "board_pins_bottom_300.png"
        board_mechanical_png_path = PROJECT_PART / "generated_data" / "src" / "board_mechanical.png"
        board_mechanical_300_png_path = PROJECT_PART / "generated_data" / "src" / "board_mechanical_300.png"
        self.assertTrue(board_png_path.is_file())
        self.assertTrue(board_300_png_path.is_file())
        self.assertTrue(board_pins_png_path.is_file())
        self.assertTrue(board_pins_300_png_path.is_file())
        self.assertTrue(board_bottom_png_path.is_file())
        self.assertTrue(board_bottom_300_png_path.is_file())
        self.assertTrue(board_pins_bottom_png_path.is_file())
        self.assertTrue(board_pins_bottom_300_png_path.is_file())
        self.assertTrue(board_mechanical_png_path.is_file())
        self.assertTrue(board_mechanical_300_png_path.is_file())
        self.assertIn("## Board with pins", readme)
        self.assertIn("## Bottom board with pins", readme)
        self.assertIn(
            "![PCB component placement with pin names](https://raw.githubusercontent.com/oomlout/oomp_electronic_version_5/main/parts/oomp_project_github_electrolama_pt1_current/generated_data/src/board_pins.png)",
            readme,
        )
        from PIL import Image

        with Image.open(board_pins_png_path) as board_pins_image:
            self.assertEqual(max(board_pins_image.size), 1600)
        with Image.open(board_png_path) as board_image:
            self.assertEqual(max(board_image.size), 1600)
        with Image.open(board_300_png_path) as board_300_image:
            self.assertEqual(max(board_300_image.size), 300)
        with Image.open(board_pins_300_png_path) as board_pins_300_image:
            self.assertEqual(max(board_pins_300_image.size), 300)
        with Image.open(board_bottom_300_png_path) as board_bottom_300_image:
            self.assertEqual(max(board_bottom_300_image.size), 300)
        with Image.open(board_pins_bottom_300_png_path) as board_pins_bottom_300_image:
            self.assertEqual(max(board_pins_bottom_300_image.size), 300)
        with Image.open(board_mechanical_png_path) as board_mechanical_image:
            self.assertEqual(max(board_mechanical_image.size), 1600)
        with Image.open(board_mechanical_300_png_path) as board_mechanical_300_image:
            self.assertEqual(max(board_mechanical_300_image.size), 300)
        self.assertFalse(any((PROJECT_PART / "generated_data").glob("*llm*")))

        assembly_svg_path = PARTS_DIRECTORY / "electronic_resistor_0402_2200_ohm" / "working_svg_assembly.svg"
        self.assertTrue(assembly_svg_path.is_file())
        assembly_svg = assembly_svg_path.read_text(encoding="utf-8")
        self.assertIn('width="1.0000mm" height="0.5000mm"', assembly_svg)
        self.assertIn('vector-effect="non-scaling-stroke"', assembly_svg)
        self.assertIn('stroke-width="0.22"', assembly_svg)
        self.assertNotIn('stroke-width="0.18"', assembly_svg)
        self.assertNotIn('stroke-width="0.8"', assembly_svg)

        assembly_pins_svg_path = PARTS_DIRECTORY / "electronic_resistor_0402_2200_ohm" / "working_svg_assembly_pins.svg"
        self.assertTrue(assembly_pins_svg_path.is_file())
        assembly_pins_svg = assembly_pins_svg_path.read_text(encoding="utf-8")
        self.assertIn(">pin 1</text>", assembly_pins_svg)
        self.assertIn(">pin 2</text>", assembly_pins_svg)
        self.assertIn('transform="rotate(-90.000', assembly_pins_svg)

        board_svg = (PROJECT_PART / "generated_data" / "src" / "board.svg").read_text(encoding="utf-8")
        self.assertIn('transform="translate(155.8761 106.1286) rotate(90.0000)"', board_svg)
        self.assertIn('width="2.4800" height="15.2400"', board_svg)
        self.assertIn('preserveAspectRatio="xMidYMid meet"', board_svg)
        self.assertNotIn('preserveAspectRatio="none"', board_svg)
        self.assertIn('class="indicator" transform="translate(155.7491 112.4786)"', board_svg)
        self.assertIn('transform="translate(6.3500 0.1270) rotate(-90)"', board_svg)
        self.assertNotIn(">SJ1</text>", board_svg)
        self.assertNotIn("UNK_HOLE", board_svg)
        self.assertEqual(board_svg.count('class="mounting-hole"'), 9)

        board_pins_svg = (PROJECT_PART / "generated_data" / "src" / "board_pins.svg").read_text(encoding="utf-8")
        self.assertIn(">vbus</text>", board_pins_svg)
        self.assertIn(">pin 1</text>", board_pins_svg)
        self.assertNotIn(">SJ1</text>", board_pins_svg)
        self.assertNotIn("UNK_HOLE", board_pins_svg)
        small_reference = re.search(r'font-size="([0-9.]+)"[^>]*>R1</text>', board_pins_svg)
        self.assertIsNotNone(small_reference)
        self.assertLess(float(small_reference.group(1)), 0.22)

        mechanical_svg = (PROJECT_PART / "generated_data" / "src" / "board_mechanical.svg").read_text(encoding="utf-8")
        self.assertIn(">0,0</text>", mechanical_svg)
        self.assertIn(">MH1 CON1</tspan>", mechanical_svg)
        self.assertEqual(mechanical_svg.count('class="mounting-hole"'), 9)
        self.assertIn(
            "| `MH7` | `UNK_HOLE_0` | Mounting Hole 2 mm Round Unplated | `mechanical / mounting_hole / 2_mm / round / unplated` | mounting | diameter 2 mm |",
            readme,
        )
        self.assertTrue((PROJECT_PART / "generated_data" / "mounting_hole_summary.json").is_file())
        self.assertTrue((PROJECT_PART / "generated_data" / "mounting_hole_summary.yaml").is_file())
        self.assertTrue((PROJECT_PART / "generated_data" / "components" / "MH7" / "component.yaml").is_file())
        self.assertTrue((PROJECT_PART / "generated_data" / "components" / "MH7" / "oomp" / "working.yaml").is_file())
        mounting_hole_item = yaml.safe_load(
            (PROJECT_PART / "generated_data" / "components" / "MH7" / "component.yaml").read_text(encoding="utf-8")
        )
        self.assertEqual(mounting_hole_item["oomp"]["status"], "matched")
        self.assertEqual(mounting_hole_item["classification"]["taxonomy_path"][0:2], ["mechanical", "mounting_hole"])

    def test_bus_pirate_explorer_is_self_contained_and_linked_to_oomp_parts(self):
        explorer_path = BUS_PIRATE_PART / "generated_data" / "board_explorer.html"
        review_path = BUS_PIRATE_PART / "generated_data" / "lcsc_review.yaml"
        self.assertTrue(explorer_path.is_file())
        self.assertTrue(review_path.is_file())
        explorer = explorer_path.read_text(encoding="utf-8")
        self.assertIn('<style id="oomp-board-style">', explorer)
        self.assertIn('<script id="component-data" type="application/json">', explorer)
        self.assertIn('data-reference="U103"', explorer)
        self.assertIn('class="board-view" data-side="front"', explorer)
        self.assertIn('class="board-view" data-side="back"', explorer)
        self.assertIn('class="side-button" type="button" data-side="back"', explorer)
        self.assertIn("working_svg_square_pins", (BUS_PIRATE_PART / "generated_data" / "src" / "components" / "manifest.yaml").read_text(encoding="utf-8"))
        self.assertIn("https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts/electronic_ic_qfn_56_7_mm_x_7_mm_microcontroller_dual_core_arm_cortex_m0_plus_raspberry_pi_rp2040", explorer)
        self.assertNotRegex(explorer, r'<script[^>]+src=')
        self.assertNotRegex(explorer, r'<link[^>]+stylesheet')

        bus_project = json.loads((BUS_PIRATE_PART / "generated_data" / "project.json").read_text(encoding="utf-8"))
        self.assertEqual(len(bus_project["mounting_hole_items"]), 6)
        self.assertTrue(all(item["oomp"]["status"] == "matched" for item in bus_project["mounting_hole_items"]))
        self.assertEqual(bus_project["mounting_hole_items"][0]["reference"], "MH1")
        self.assertTrue((PARTS_DIRECTORY / "mechanical_mounting_hole_0_7_mm_round_unplated" / "working.yaml").is_file())

        board_top = (BUS_PIRATE_PART / "generated_data" / "src" / "board.svg").read_text(encoding="utf-8")
        board_bottom = (BUS_PIRATE_PART / "generated_data" / "src" / "board_bottom.svg").read_text(encoding="utf-8")
        self.assertNotIn('data-reference="J301"', board_top)
        self.assertIn('data-reference="J301"', board_bottom)
        self.assertNotIn('data-reference="U103"', board_bottom)
        self.assertIn('mirrored horizontally', (BUS_PIRATE_PART / "README.md").read_text(encoding="utf-8"))

    def test_j1_orientation_uses_footprint_pad_one(self):
        local_bounds = {
            "min_x": -1.3716,
            "min_y": -1.2446,
            "max_x": 14.0716,
            "max_y": 1.4986,
        }
        pads = [
            {
                "number": "1",
                "local_position": {"x": 0.0, "y": 0.0},
            }
        ]
        pin_one_svg = {"x": 1.24, "y": 1.27}
        rotation = _orientation_rotation(
            2.48,
            15.24,
            local_bounds,
            pads,
            pin_one_svg,
        )
        self.assertEqual(rotation, -90)

    def test_nearly_square_ic_orientation_is_not_forced_by_pad_extents(self):
        local_bounds = {
            "min_x": -2.125,
            "min_y": -1.8,
            "max_x": 2.125,
            "max_y": 1.8,
        }
        pads = [
            {
                "number": "1",
                "local_position": {"x": -1.25, "y": -0.95},
            }
        ]
        pin_one_svg = {"x": 0.3759, "y": 0.5657}
        rotation = _orientation_rotation(
            2.8,
            2.9,
            local_bounds,
            pads,
            pin_one_svg,
        )
        self.assertEqual(rotation, 0)


class ElectronicPartReadmeTests(unittest.TestCase):
    def test_part_readme_uses_pinout_hero_and_small_previews(self):
        part_directory = PARTS_DIRECTORY / "electronic_resistor_0402_2200_ohm"
        working = yaml.safe_load((part_directory / "working.yaml").read_text(encoding="utf-8"))
        preview_action = working["oomlout_ai_roboclick_1"]
        preview_actions = preview_action["actions"]

        self.assertEqual(len(preview_actions), 9)
        self.assertEqual(preview_actions[0]["command"], "run_python")
        self.assertEqual(preview_actions[0]["file_python"], "kicad_agents/component_svg_action.py")
        self.assertEqual(preview_actions[0]["part_id"], part_directory.name)
        resize_actions = preview_actions[1:]
        self.assertTrue(all(action["command"] == "image_resize" for action in resize_actions))
        self.assertTrue(all(action["maximum_dimension"] == 300 for action in resize_actions))
        self.assertTrue(all(action["allow_upscale"] is False for action in resize_actions))
        self.assertTrue(all(action["regenerate_pngs"] is False for action in resize_actions))

        readme = (part_directory / "README.md").read_text(encoding="utf-8")
        self.assertIn("![Resistor 0402 2200 Ohm pinout](working_svg_square_pins.svg)", readme)
        self.assertIn("## At a glance", readme)
        self.assertNotIn("## Diagram gallery", readme)
        self.assertNotIn("<img", readme)
        self.assertIn("## Files", readme)
        self.assertIn("![Pinout drawing](working_svg_square_pins_300.png)", readme)
        self.assertIn("![Outline](working_svg_outline_300.png)", readme)
        self.assertNotIn("[Outline drawing](working_svg_outline.svg)", readme)
        self.assertNotIn("[View the datasheet](datasheet.pdf)", readme)

        from PIL import Image

        preview_files = sorted(part_directory.glob("working_svg*_300.png"))
        self.assertEqual(len(preview_files), 8)
        for preview_file in preview_files:
            with Image.open(preview_file) as preview_image:
                self.assertLessEqual(max(preview_image.size), 300)

    def test_default_generated_pipeline_has_no_llm_actions_or_direct_http_clients(self):
        audit = run_audit(REPOSITORY_ROOT)
        self.assertEqual(audit["status"], "pass", audit["findings"])


class UsbConnectorDiagramTests(unittest.TestCase):
    def test_usb_a_uses_datasheet_dimensions_and_named_pins(self):
        working = yaml.safe_load((USB_A_SOURCE / "working.yaml").read_text(encoding="utf-8"))
        self.assertEqual(working["dimensions_mm"], {"length": 14.3, "width": 10.6})
        self.assertEqual(working["connector_dimensions_mm"]["contact_count"], 4)
        self.assertEqual(working["connector_dimensions_mm"]["contact_pitch"], 2.0)
        self.assertEqual(working["pins"]["pin_2"]["name"], "usb_negative")
        self.assertEqual(working["pins"]["pin_5"]["type"], "shield")

        assembly_svg = (USB_A_PART / "working_svg_assembly.svg").read_text(encoding="utf-8")
        self.assertIn('width="14.3000mm" height="10.6000mm"', assembly_svg)
        self.assertIn('data-pin-one-identifiers="VBUS|1"', assembly_svg)

        local_bounds = {
            "min_x": -7.15,
            "min_y": -4.575,
            "max_x": 7.15,
            "max_y": 6.025,
        }
        pads = [
            {
                "number": "VBUS",
                "local_position": {"x": 3.5, "y": 5.3},
            }
        ]
        rotation = _orientation_rotation(
            14.3,
            10.6,
            local_bounds,
            pads,
            {"x": 2.696, "y": 2.12, "identifiers": ["VBUS", "1"]},
        )
        self.assertEqual(rotation, 180)

    def test_usb_c_uses_datasheet_pinout_and_physical_size(self):
        working = yaml.safe_load((USB_C_PART / "working.yaml").read_text(encoding="utf-8"))
        self.assertEqual(working["dimensions_mm"], {"length": 8.94, "width": 7.35})
        dimensions = working["connector_dimensions_mm"]
        self.assertEqual(dimensions["pcb_pad_count"], 12)
        self.assertEqual(dimensions["pcb_power_pad_width"], 0.6)
        self.assertEqual(dimensions["pcb_signal_pad_width"], 0.3)
        self.assertEqual(dimensions["pcb_pad_length"], 1.5)
        self.assertEqual(len(working["pins"]), 16)
        self.assertEqual(working["pins"]["pin_1"], {"name": "gnd", "number": "A1", "type": "power"})
        self.assertEqual(working["pins"]["pin_16"], {"name": "gnd", "number": "B1", "type": "power"})

        readme = (USB_C_PART / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Datasheet", readme)
        self.assertIn("[View the datasheet](datasheet.pdf)", readme)
        self.assertIn("(working_svg_top.svg)", readme)
        self.assertIn("(working_svg_top_300.png)", readme)
        self.assertIn("(working_svg_bottom_300.png)", readme)
        self.assertIn("(working_svg_side_300.png)", readme)

        pinout_svg = (USB_C_PART / "working_svg_square_pins.svg").read_text(encoding="utf-8")
        self.assertIn("Connector USB C", pinout_svg)
        self.assertIn("A1 gnd", pinout_svg)
        self.assertIn("B1 gnd", pinout_svg)
        self.assertNotIn(">pin 1<", pinout_svg)

        assembly_svg = (USB_C_PART / "working_svg_assembly.svg").read_text(encoding="utf-8")
        self.assertIn('width="8.9400" height="7.3500"', assembly_svg)
        self.assertEqual(assembly_svg.count('width="0.6000"'), 4)
        self.assertEqual(assembly_svg.count('width="0.3000"'), 8)

        assembly_pins_svg = (USB_C_PART / "working_svg_assembly_pins.svg").read_text(encoding="utf-8")
        self.assertEqual(assembly_pins_svg.count("</text>"), 12)
        self.assertIn(">gnd</text>", assembly_pins_svg)
        self.assertIn(">vbus</text>", assembly_pins_svg)
        self.assertIn(">cc1</text>", assembly_pins_svg)
        self.assertIn('transform="rotate(-90.000', assembly_pins_svg)

        connector_view_names = ["top", "bottom", "side"]
        for connector_view_name in connector_view_names:
            self.assertTrue((USB_C_PART / f"working_svg_{connector_view_name}.svg").is_file())
            self.assertTrue((USB_C_PART / f"working_svg_{connector_view_name}.png").is_file())


if __name__ == "__main__":
    unittest.main()
