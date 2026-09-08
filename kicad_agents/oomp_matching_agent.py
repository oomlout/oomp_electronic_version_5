"""Explainable OOMP component matcher intended for use by an AI agent or pipeline."""

import argparse
import json
import math
import re
from difflib import SequenceMatcher
from pathlib import Path

import yaml


PACKAGE_SIZES = ["0201", "0402", "0603", "0805", "1206", "1205", "1210", "2512", "3216", "1010", "5050"]
LED_COLORS = ["warm_white", "white", "yellow", "green", "blue", "pink", "red", "rgb"]

# Value/MPN fragments that identify an exact OOMP part already in the
# catalogue. Consulted before candidate ranking so generic values ("SS14")
# resolve without per-project override files. A proposal is only accepted if
# the target part exists, so stale rows stay inert.
KNOWN_PART_ALIASES = {
    # Soldered/e-radionica breakout parts identified by exact value/MPN.
    "attiny404_ssnr": "electronic_ic_soic_14_microcontroller_8_bit_avr_microchip_attiny404_ssnr",
    "tps613222a": "electronic_ic_sot_23_5_power_management_boost_converter_texas_instruments_tps613222a",
    "lm393": "electronic_ic_soic_8_logic_comparator_lm393",
    "rt9080_3_3": "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_3_3_volt_richtek_rt9080_33",
    "opa344": "electronic_ic_sot_23_5_amplifier_operational_amplifier_texas_instruments_opa344",
    "si7211_b_00_iv": "electronic_ic_sot_23_5_sensor_hall_effect_silicon_labs_si7211_b_00_iv",
    "si7201_b_06_iv": "electronic_ic_sot_23_sensor_hall_effect_silicon_labs_si7201_b_06_iv",
    "hx711": "electronic_ic_sop_16_converter_load_cell_amplifier_avia_semiconductor_hx711",
    "df5a5_6lfu": "electronic_diode_tvs_sot_353_toshiba_df5a5_6lfu",
    "pesd3v3l4ug": "electronic_diode_esd_array_sot_353_nexperia_pesd3v3l4ug",
    "dt1042_04so": "electronic_diode_tvs_array_sot_26_diodes_incorporated_dt1042_04so",
    "m4_dioda": "electronic_diode_rectifier_sma_m4",
    "mmbt4403": "electronic_transistor_sot_23_bipolar_pnp_40_volt_600_milliamp_onsemi_mmbt4403",
    "nmos_dual": "electronic_transistor_sot_363_6_mosfet_n_channel_dual",
    "q_npn_bce": "electronic_transistor_sot_23_bipolar_npn",
    # Soldered boards draw bare "NPN"/"PNP"/"NMOS" values on SOT-23-3
    # footprints with no MPN; the underscore suffix defeats the word-boundary
    # match, so the spelled-out schematic values get their own rows.
    "npn": "electronic_transistor_sot_23_bipolar_npn",
    "npn_sot_23_3": "electronic_transistor_sot_23_bipolar_npn",
    "pnp": "electronic_transistor_sot_23_bipolar_pnp",
    "nmos": "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode",
    "dfe201612e_2r2m_p2": "electronic_inductor_0806_2_2_micro_henry",
    "dshp03ts_s": "electronic_switch_slide_surface_mount_dpdt_ck_dshp03ts_s",
    "tc33x_2_103e": "electronic_potentiometer_trimmer_through_hole_10_kilo_ohm_bourns_tc33x_2_103e",
    "mq_x": "electronic_sensor_mq_6_pin",
    "tcrt5000l": "electronic_sensor_tcrt5000_4_pin_vishay_tcrt5000l",
    "am312": "electronic_sensor_pir_3_pin_am312",
    "apds_9960": "electronic_sensor_apds_9960_broadcom_apds_9960",
    # Soldered's easyC socket is the 1.25 mm JST GH part.  Qwiic/STEMMA QT
    # uses the separate 1.00 mm JST SH family and must not be conflated with
    # it merely because both are four-pin board connectors.
    "easyc_smd": "electronic_connector_easyc_1_25_mm_pitch_surface_mount_right_angle_4_pin_jst_sm04b_gh_tf",
    "u_fl": "electronic_connector_u_fl_surface_mount_i_pex_u_fl_r_smt_1",
    "sma_edge": "electronic_connector_sma_edge_mount",
    "kf235_5_0_2p": "electronic_connector_terminal_block_5_mm_pitch_through_hole_2_pin_kf235_5_0_2p",
    "cr1220_holder": "electronic_connector_coin_cell_holder_through_hole_cr1220",
    "cp2102n": "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102n_a01_gqfn28r",
    "ap2112k_3_3": "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_diodes_ap2112k_3_3",
    "lis3dhtr": "electronic_sensor_accelerometer_lga_16_st_lis3dhtr",
    "lis3dh": "electronic_sensor_accelerometer_lga_16_st_lis3dhtr",
    "adxl345": "electronic_sensor_accelerometer_lga_14_analog_devices_adxl345",
    "pts810": "electronic_switch_tactile_surface_mount_pts810",
    "gt_tc026x_hxxx_lx": "electronic_switch_tactile_through_hole_gt_tc026x_hxxx_lx",
    "b3fs_100xp": "electronic_switch_tactile_surface_mount_omron_b3fs_100xp",
    "prtr5v0u2x": "electronic_diode_tvs_array_sot_143_nxp_prtr5v0u2x",
    "se5218": "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_se5218",
    "se5218alg": "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_se5218alg",
    "ccs811b_jopr": "electronic_sensor_air_quality_lga_20_ams_ccs811b_jopr",
    "bat20j": "electronic_diode_schottky_sod_323_infineon_bat20j",
    "tlc555cd": "electronic_ic_soic_8_timer_555_timer_texas_instruments_tlc555cd",
    "sgm358yms_tr": "electronic_ic_msop_8_amplifier_operational_amplifier_sg_micro_sgm358yms_tr",
    "acs712": "electronic_ic_soic_8_sensor_hall_effect_current_sensor_allegro_acs712",
    "ltr_507als_01": "electronic_sensor_light_proximity_ch_6_liteon_ltr_507als_01",
    "l86_m33": "electronic_sensor_gnss_module_quectel_l86_m33",
    "attiny1604_ssnr": "electronic_ic_soic_14_microcontroller_8_bit_avr_microchip_attiny1604_ssnr",
    "ch342f": "electronic_ic_qfn_24_converter_usb_to_serial_converter_wch_ch342f",
    "74hc4066bq": "electronic_ic_qfn_14_logic_analog_switch_nexperia_74hc4066bq",
    "ap7361c_3_3v": "electronic_ic_dfn_8_power_management_linear_voltage_regulator_diodes_ap7361c_3_3v",
    "ads1219ipw": "electronic_ic_tssop_16_converter_analog_to_digital_converter_texas_instruments_ads1219ipw",
    "ade7953acpz": "electronic_ic_qfn_28_power_meter_energy_metering_analog_devices_ade7953acpz",
    "ina228": "electronic_ic_vssop_10_power_monitor_current_monitor_texas_instruments_ina228",
    "pca9554pw": "electronic_ic_tssop_16_logic_io_expander_texas_instruments_pca9554pw",
    "ch340e": "electronic_ic_msop_10_converter_usb_to_serial_converter_wch_ch340e",
    "my1690x_16s": "electronic_ic_so_16_audio_audio_player_my_semi_my1690x_16s",
    "cy8cmbr3102": "electronic_ic_soic_8_capacitive_touch_controller_controller_infineon_cy8cmbr3102",
    "ml414h": "electronic_battery_coin_cell_6_8_mm_maxell_ml414h",
    "ad8495armz": "electronic_ic_msop_8_amplifier_thermocouple_amplifier_texas_instruments_ad8495armz",
    "ina219": "electronic_ic_sot_23_8_power_monitor_current_monitor_texas_instruments_ina219",
    "bmp388": "electronic_sensor_pressure_temperature_lga_10_bosch_bmp388",
    "w25q16jvuxiq": "electronic_ic_uson_8_memory_spi_nor_flash_winbond_w25q16jvuxiq",
    "stm32f103c8tx": "electronic_ic_lqfp_48_microcontroller_stm32_st_stm32f103c8tx",
    "esp32_s3_wroom_1": "electronic_ic_esp32_s3_wroom_1_microcontroller_wifi_bluetooth_8_mb_flash_espressif_esp32_s3_wroom_1_n8",
    "ne555dr": "electronic_ic_soic_8_timer_555_timer_texas_instruments_ne555dr",
    "tc33x_2_105e": "electronic_potentiometer_trimmer_through_hole_1_mega_ohm_bourns_tc33x_2_105e",
    "tl431acdbz": "electronic_ic_sot_23_3_power_management_shunt_regulator_texas_instruments_tl431acdbz",
    "lsm9ds1tr": "electronic_sensor_imu_lga_24_st_lsm9ds1tr",
    "dan_f10n": "electronic_sensor_gnss_module_u_blox_dan_f10n",
    "ipx_connector_with_sma": "electronic_connector_rf_cable_assembly_ipx_to_sma_ipx_connector_with_sma",
    "header_female_5x2_1_27mm_smd": "electronic_connector_header_1_27_mm_pitch_surface_mount_10_pin_socket_header_female_5x2_1_27_mm_smd",
    "sam_m8q": "electronic_sensor_gnss_module_u_blox_sam_m8q",
    "neo_f10n": "electronic_sensor_gnss_module_u_blox_neo_f10n",
    "bmv080": "electronic_sensor_particulate_matter_module_bosch_bmv080",
    "rfcmf1220100m4t": "electronic_transformer_surface_mount_usb_coilcraft_rfcmf1220100m4t",
    # The full schematic value "CP2102N-Axx-xQFN28" -- the bare "cp2102n" alias
    # above cannot match it because the word-boundary rule stops at the
    # following underscore.
    "cp2102n_axx_xqfn28": "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102n_a01_gqfn28r",
    "xc6206p332mr": "electronic_ic_sot_23_power_management_linear_voltage_regulator_3_3_volt_torex_xc6206p332mr",
    "xc6206p502mr": "electronic_ic_sot_23_power_management_linear_voltage_regulator_5_volt_torex_xc6206p502mr",
    "atmega328p_a": "electronic_ic_tqfp_32_7_mm_x_7_mm_microcontroller_8_bit_avr_microchip_atmega328p_au",
    # The Uno schematic writes the AMS1117 suffix with a trailing V.
    "ams1117_3_3": "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_3_3_volt_advanced_monolithic_systems_ams1117_3_3",
    "ams1117_3_3v": "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_3_3_volt_advanced_monolithic_systems_ams1117_3_3",
    "ams1117_5v": "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_5_volt_advanced_monolithic_systems_ams1117_5",
    "ch340c": "electronic_ic_sop_16_converter_usb_to_serial_converter_wch_ch340c",
    # Pico board MCU: same RP2040 the Bus Pirate 5 uses.
    "rp2040": "electronic_ic_qfn_56_7_mm_x_7_mm_microcontroller_dual_core_arm_cortex_m0_plus_raspberry_pi_rp2040",
    # BSS138 on SparkFun boards: the part's generic_match rules list KiCad's
    # symbol/footprint names, but SparkFun ships its own symbol and footprint,
    # so the value itself (which is the bare MPN there) aliases straight to the
    # stocked onsemi variant.
    "bss138": "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_220_milliamp_onsemi_bss138",
    "jst_sh_2pin_1mm_c145954": "electronic_connector_jst_sh_1_mm_pitch_surface_mount_right_angle_2_pin_jst_sm02b_srss_tb",
    "pesd0402": "electronic_diode_esd_0402_littelfuse_pesd0402",
    "ss14": "electronic_diode_schottky_sod_123_ss14",
    "bat54w": "electronic_diode_schottky_sod_323_bat54w",
    "1ss400": "electronic_diode_schottky_sod_523_1ss400",
    # Schematic values that are really MPNs of catalogue capacitors.
    "cl10a226mpcnube": "electronic_capacitor_0603_22_micro_farad",
    # Soldered radial electrolytic (16 V, 681 code = 680 uF, 8 mm x 14.5 mm).
    "emzr160ara681mha0g": "electronic_capacitor_8_mm_diameter_14_5_mm_tall_electrolytic_680_micro_farad_16_volt",
    "c1608x7s1a475k080ac": "electronic_capacitor_0603_4_7_micro_farad",
    # 2N7002 carries an opt-in generic_match rule in its populate data, so it
    # is intentionally not aliased here (BSS138 above needs the alias because
    # SparkFun boards use their own symbol/footprint names).
}


# Exact component signatures recovered from verified project matches.  Unlike
# the former per-project, per-reference dictionaries, these are reusable
# matcher rules: a signature requires the value, footprint and symbol identity
# to agree.  This keeps a bare value such as ``LED`` or ``SW_Push`` from being
# over-matched on unrelated boards.
EXACT_COMPONENT_MATCHES = {
    ("12mhz", "crystal_crystal_smd_3225_4pin_3_2x2_5mm", "device_crystal_gnd24_small"): "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf",
    ("12mhz", "project_tool_mini_reva2_xtal_4p_3225", "project_tool_mini_reva2_eagle_import_xtal_4p_3225"): "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf",
    ("1_5a", "inductor_smd_l_0805_2012metric", "kicad5_device_ferrite_bead_small"): "electronic_ferrite_bead_0805_15_ohm_1_5_amp_tdk_mmz2012r150at000",
    ("1n4148wt", "diode_smd_d_sod_523", "diode_1n4148ws"): "electronic_diode_switching_sod_523f_onsemi_1n4148wt",
    ("22u", "capacitor_tantalum_smd_cp_eia_3216_10_kemet_i", "device_c_polarized"): "electronic_capacitor_3216_avx_a_tantalum_22_micro_farad_10_volt",
    ("aip74hc595ta", "package_so_tssop_16_4_4x5mm_p0_65mm", "74xx_74ahct595"): "electronic_ic_tssop_16_logic_serial_in_parallel_out_shift_register_wuxi_i_core_elec_aip74hc595ta16_tr",
    ("aip74hct245ta", "package_so_tssop_20_4_4x6_5mm_p0_65mm", "74xx_74hc245"): "electronic_ic_tssop_20_logic_octal_bus_transceiver_wuxi_i_core_elec_aip74hct245ta20_tr",
    ("aip74lvc1t45gc363_tr", "package_to_sot_smd_sot_363_sc_70_6", "logic_leveltranslator_sn74lvc1t45dck"): "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
    ("ams1117_3_3", "package_to_sot_smd_sot_223_3_tabpin2", "regulator_linear_ams1117_3_3"): "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_3_3_volt_advanced_monolithic_systems_ams1117_3_3",
    ("ap2127", "package_to_sot_smd_sot_23_5", "dp_vreg_mcp1824"): "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_3_3_volt_diodes_ap2127k_3_3trg1",
    ("bas40t_05", "package_to_sot_smd_sot_523", "diode_bat54c"): "electronic_diode_schottky_dual_common_cathode_sot_523_diodes_incorporated_bas40t_05",
    ("bcm857", "package_to_sot_smd_sot_363_sc_70_6", "kicad5_device_q_dual_pnp_pnp_e1b1c2e2b2c1"): "electronic_transistor_sot_363_6_bipolar_pnp_dual_matched_pair_45_volt_100_milliamp_diodes_incorporated_bcm857bs_7_f",
    ("cd4067", "package_so_tssop_24_4_4x7_8mm_p0_65mm", "74xx_cd74hc4067m"): "electronic_ic_tssop_24_logic_16_channel_analog_multiplexer_nexperia_74hct4067pw118",
    ("ch343p", "project_tool_mini_reva2_qfn16_l3_0_w3_0_p0_50_ep1_7", "project_tool_mini_reva2_eagle_import_interface_ch343p"): "electronic_ic_qfn_16_3_mm_x_3_mm_converter_usb_to_serial_converter_wch_ch343p",
    ("conn_01x02_pin", "connector_pinheader_2_54mm_pinheader_1x02_p2_54mm_vertical", "connector_conn_01x02_pin"): "electronic_connector_header_2_54_mm_pitch_through_hole_2_pin",
    ("conn_01x03", "connector_pinsocket_2_54mm_pinsocket_1x03_p2_54mm_vertical", "connector_generic_conn_01x03"): "electronic_connector_header_2_54_mm_pitch_through_hole_3_pin_socket_kinghelm_kh_2_54fh_1x3p_h8_5",
    ("conn_01x03_mountingpin", "connector_jst_jst_sh_bm03b_srss_tb_1x03_1mp_p1_00mm_vertical", "connector_generic_mountingpin_conn_01x03_mountingpin"): "electronic_connector_jst_sh_1_mm_pitch_surface_mount_vertical_3_pin_jst_bm03b_srss_tb",
    ("conn_01x09", "connector_jst_jst_sh_sm09b_srss_tb_1x09_1mp_p1_00mm_horizontal", "connector_generic_conn_01x09"): "electronic_connector_jst_sh_1_mm_pitch_surface_mount_right_angle_9_pin_jst_sm09b_srss_tb",
    ("conn_01x10", "connector_pinheader_2_54mm_pinheader_1x10_p2_54mm_vertical", "connector_generic_conn_01x10"): "electronic_connector_header_2_54_mm_pitch_through_hole_10_pin",
    ("conn_06lock", "project_tool_mini_reva2_1x06_lock", "project_tool_mini_reva2_eagle_import_conn_06lock"): "electronic_connector_header_2_54_mm_pitch_through_hole_6_pin",
    ("adxl345patrick", "lga14_1_1_patrick", "kicad_file_eagle_import_testing_adxl345patrick"): "electronic_sensor_accelerometer_lga_14_analog_devices_adxl345",
    ("esp32_wroom_e", "espressif_esp32_wroom_32e", "espressif_esp32_wroom_e"): "electronic_ic_esp32_wroom_32e_microcontroller_wifi_bluetooth_8_mb_flash_espressif_esp32_wroom_32e_n8",
    ("fb_2a", "project_tool_mini_reva2_pkg_c_0805", "project_tool_mini_reva2_eagle_import_inductor_0805"): "electronic_ferrite_bead_0805_220_ohm_2_amp_murata_blm21pg221sn1d",
    ("led", "led_smd_led_0402_1005metric", "device_led"): "electronic_led_0402_blue",
    ("lmv321", "package_to_sot_smd_sot_23_5", "comparator_lmv331"): "electronic_ic_sot_23_5_amplifier_operational_single_rail_to_rail_input_output_gainsil_lmv321_tr",
    ("lmv321a", "package_to_sot_smd_sot_23_5", "comparator_lmv331"): "electronic_ic_sot_23_5_amplifier_operational_single_precision_rail_to_rail_input_output_gainsil_gs321a_tr",
    ("lmv324", "package_so_tssop_14_4_4x5mm_p0_65mm", "amplifier_operational_lm324"): "electronic_ic_tssop_14_amplifier_operational_quad_rail_to_rail_output_texas_instruments_lmv324ipwr",
    ("lmv331", "package_to_sot_smd_sot_23_5", "comparator_lmv331"): "electronic_ic_sot_23_5_comparator_single_open_collector_texas_instruments_lmv331idbvr",
    ("me6211a33pg_n", "package_to_sot_smd_sot_89_3", "regulator_linear_ap2204ra_3_3"): "electronic_ic_sot_89_3_power_management_linear_voltage_regulator_3_3_volt_microne_me6211a33pg_n",
    ("mmbt7002k", "package_to_sot_smd_sot_23", "transistor_fet_bss138"): "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_300_milliamp_cbi_mmbt7002k",
    ("mmdt3906", "package_to_sot_smd_sot_363_sc_70_6", "kicad5_device_q_dual_pnp_pnp_e1b1c2e2b2c1"): "electronic_transistor_sot_363_6_bipolar_pnp_dual_general_purpose_40_volt_200_milliamp_cbi_mmdt3906dw",
    ("mt29f1g01abafdwb", "dp_memory_u_pdfn_8", "dp_memory_mt29f1g01abafdwb"): "electronic_ic_updfn_8_memory_spi_nand_flash_1_gbit_micron_mt29f1g01abafdwb",
    ("rp2040", "rp_silicon_rp2040_qfn_56", "rp_silicon_rp2040"): "electronic_ic_qfn_56_7_mm_x_7_mm_microcontroller_dual_core_arm_cortex_m0_plus_raspberry_pi_rp2040",
    ("rt9742cgj5", "project_tool_mini_reva2_pkg_sot23_5", "project_tool_mini_reva2_eagle_import_power_switch_rt9742_en_active_high"): "electronic_ic_tsot_23_5_power_management_high_side_power_switch_with_flag_richtek_rt9742cgj5",
    ("si2301", "package_to_sot_smd_sot_523", "transistor_fet_bss84"): "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
    ("sk6812_mini_e", "dp_led_sk6812_mini_e", "dp_led_sk6812_mini_e"): "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
    ("sk6812_side_a_b", "dp_led_sk6812_side_a_b", "dp_led_sk6812_side_a_b"): "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a",
    ("sl2_1a", "project_tool_mini_reva2_soic127p604x185_16n", "project_tool_mini_reva2_eagle_import_usb_hub_sl2_1a"): "electronic_ic_sop_16_controller_usb_hub_controller_4_port_corechips_sl21a",
    ("sn74lvc1g57dbv", "project_tool_mini_reva2_sot95p280x145_6n", "project_tool_mini_reva2_eagle_import_logic_multi_sn74lvc1g57dbv"): "electronic_ic_sot_23_6_logic_configurable_multi_function_gate_texas_instruments_sn74lvc1g57dbvr",
    ("sp0503baht", "package_to_sot_smd_sot_143", "power_protection_sp0503baht"): "electronic_diode_tvs_array_sot_143_littelfuse_sp0503bahtg",
    ("srv05_4_p_t7", "project_tool_mini_reva2_sot95p280x145_6n", "project_tool_mini_reva2_eagle_import_diode_tvs_srv05_4"): "electronic_diode_tvs_array_sot_23_6_protek_srv054pt7",
    ("ss8050", "package_to_sot_smd_sot_23w", "device_q_npn_bce"): "electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050",
    ("sw_push", "button_switch_smd_sw_push_spst_no_alps_skrk", "switch_sw_push"): "electronic_switch_tactile_surface_mount_xunpu_ts_1088_ar02016",
    ("tft_20_qt200h1201", "dp_lcd_tft_20_qt200h1201", "dp_lcd_tft_20_qt200h1201"): "electronic_display_tft_2_inch_240_x_320_pixel_ips_spi_12_pin_szhtc_qt200h1201",
    ("type_c_31_m_12", "usb_c_hro_type_c_31_m_12", "usb_c_type_c_31_m_12"): "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12",
    ("usb_a_female", "project_tool_mini_reva2_jing_912_121a2023s10100", "project_tool_mini_reva2_eagle_import_usb_a_female_jing_912_121a2023s10100"): "electronic_connector_usb_a_surface_mount_4_pin_shenzhen_jing_tuo_jin_electronics_912121a2023s10100",
    ("usb_c", "project_tool_mini_reva2_usbc_c_31_m_12", "project_tool_mini_reva2_eagle_import_usbc_usb_c_12"): "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12",
    ("usb_c_receptacle_usb2_0", "connector_usb_usb_c_receptacle_g_switch_gt_usb_7010asv", "connector_usb_c_receptacle_usb2_0"): "electronic_connector_usb_c_surface_mount_16_pin_shou_han_type_c_16pin_2md_073",
    ("w25q128jvsiq", "package_so_sop_8_5_28x5_23mm_p1_27mm", "dp_memory_xm25qh128a"): "electronic_ic_sop_8_5_28_mm_x_5_23_mm_memory_spi_nor_flash_128_mbit_winbond_w25q128jvsiq",
}


def normalize_text(value):
    value = str(value or "").strip().lower()
    value = value.replace("µ", "u").replace("μ", "u").replace("ω", "ohm").replace("Ω", "ohm")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def _engineering_number(value, suffixes):
    normalized = str(value or "").strip().lower().replace("µ", "u").replace("μ", "u")
    normalized = normalized.replace("ohms", "").replace("ohm", "").replace("Ω", "")
    normalized = normalized.replace("farads", "").replace("farad", "").replace("f", "")
    normalized = normalized.replace(" ", "")

    middle_match = re.fullmatch(r"(\d+)([a-z])(\d+)", normalized)
    if middle_match and middle_match.group(2) in suffixes:
        whole = float(middle_match.group(1))
        decimal = float("0." + middle_match.group(3))
        return (whole + decimal) * suffixes[middle_match.group(2)]

    normal_match = re.fullmatch(r"(\d+(?:\.\d+)?)([a-z]?)", normalized)
    if normal_match and normal_match.group(2) in suffixes:
        return float(normal_match.group(1)) * suffixes[normal_match.group(2)]
    return None


def parse_resistance_ohms(value):
    # "15mR"/"15mΩ" is fifteen milliohms; KiCad's lowercase m before the unit
    # marker means milli on shunt resistors (the bare-letter path below keeps
    # its historic mega reading for plain "15m").
    milli_text = str(value or "").strip().lower().replace("ω", "r").replace("Ω", "r")
    milli_match = re.fullmatch(r"(\d+(?:\.\d+)?)\s*mr", milli_text)
    if milli_match:
        parsed = float(milli_match.group(1)) / 1000
        if abs(parsed - round(parsed)) < 1e-9:
            return int(round(parsed))
        return round(parsed, 6)
    parsed = _engineering_number(value, {"": 1, "r": 1, "k": 1000, "m": 1000000})
    if parsed is None:
        return None
    if abs(parsed - round(parsed)) < 1e-9:
        return int(round(parsed))
    return round(parsed, 6)


def resistance_taxonomy(value):
    resistance = parse_resistance_ohms(value)
    if resistance is None:
        return ""
    if isinstance(resistance, int):
        return str(resistance)
    return ("%.6f" % resistance).rstrip("0").rstrip(".").replace(".", "_")


def parse_capacitance_farads(value):
    return _engineering_number(
        value,
        {"": 1, "p": 1e-12, "n": 1e-9, "u": 1e-6, "m": 1e-3},
    )


def capacitance_taxonomy(value):
    farads = parse_capacitance_farads(value)
    if farads is None:
        return ""
    units = [
        (1e-12, "pico_farad"),
        (1e-9, "nano_farad"),
        (1e-6, "micro_farad"),
        (1e-3, "milli_farad"),
        (1, "farad"),
    ]
    selected_multiplier, selected_name = units[0]
    for multiplier, unit_name in units:
        scaled = farads / multiplier
        if scaled >= 1 and abs(scaled - round(scaled, 6)) < 1e-6:
            selected_multiplier = multiplier
            selected_name = unit_name
    scaled = farads / selected_multiplier
    if abs(scaled - round(scaled)) < 1e-7:
        number = str(int(round(scaled)))
    else:
        number = ("%.6f" % scaled).rstrip("0").rstrip(".").replace(".", "_")
    return f"{number}_{selected_name}"


def parse_inductance_henries(value):
    """Only values with an explicit inductance unit ("33nH", "10uH", "4.7uH")."""
    match = re.fullmatch(
        r"(\d+(?:\.\d+)?)\s*(nh|uh|µh|μh|mh|h)",
        str(value or "").strip().lower().replace("henry", "h").replace("henries", "h"),
    )
    if not match:
        return None
    suffix = {"nh": 1e-9, "uh": 1e-6, "µh": 1e-6, "μh": 1e-6, "mh": 1e-3, "h": 1.0}
    return float(match.group(1)) * suffix[match.group(2)]


def inductance_taxonomy(value):
    henries = parse_inductance_henries(value)
    if henries is None:
        return ""
    units = [
        (1e-9, "nano_henry"),
        (1e-6, "micro_henry"),
        (1e-3, "milli_henry"),
        (1.0, "henry"),
    ]
    selected_multiplier, selected_name = units[0]
    for multiplier, unit_name in units:
        scaled = henries / multiplier
        if scaled >= 1 and abs(scaled - round(scaled, 6)) < 1e-6:
            selected_multiplier = multiplier
            selected_name = unit_name
    scaled = henries / selected_multiplier
    if abs(scaled - round(scaled)) < 1e-7:
        number = str(int(round(scaled)))
    else:
        number = ("%.6f" % scaled).rstrip("0").rstrip(".").replace(".", "_")
    return f"{number}_{selected_name}"


def _first_schematic_unit(component):
    schematic = component.get("schematic") or {}
    units = schematic.get("units") or []
    return units[0] if units else {}


def _strip_import_library_prefix(footprint):
    """Eagle-imported boards keep the source library in the footprint id
    ("Adafruit LIS3DH-import-fps:JST_SH4" / "kicad_file:0805-NO"); that
    library name is an import artifact, so only the footprint name after
    the colon identifies the package."""
    text = str(footprint or "")
    library, separator, name = text.rpartition(":")
    if separator and (library.strip().lower() == "kicad_file" or "import" in library.lower()):
        return name.strip()
    return text


def component_fields(component):
    unit = _first_schematic_unit(component)
    properties = unit.get("properties") or {}
    pcb = component.get("pcb") or {}
    return {
        "reference": component.get("reference", ""),
        "value": properties.get("Value") or pcb.get("value") or "",
        "footprint": _strip_import_library_prefix(
            properties.get("Footprint") or pcb.get("library_id") or ""
        ),
        "library_id": unit.get("library_id", ""),
        "mpn": properties.get("MPN") or properties.get("Manufacturer Part Number") or "",
        "manufacturer": properties.get("Manufacturer") or properties.get("Manufacturer Name") or "",
    }


def infer_kind(fields):
    reference = fields["reference"].upper()
    evidence = " ".join(
        normalize_text(fields[field_name])
        for field_name in ["value", "footprint", "library_id"]
    )
    if reference.startswith("LED") or "led" in evidence or "ws2812" in evidence:
        return "led"
    if "r_array" in evidence or reference.startswith("RN"):
        return "resistor_array"
    if reference.startswith("R") and not reference.startswith("REF"):
        return "resistor"
    # Inductors first: an explicit inductance unit beats any footprint or
    # reference hint (SparkFun draws fitted inductors with capacitor symbols).
    if parse_inductance_henries(fields["value"]) is not None:
        return "inductor"
    if "ferrite" in evidence:
        return "ferrite_bead"
    # A resistance written on a capacitor-referenced symbol means the board
    # fitted a resistor there (SparkFun USB current limiters say "470Ohm" on
    # C-prefixed references).
    if reference.startswith("C") and not reference.startswith("CON"):
        value_text = str(fields["value"] or "")
        if "ohm" in normalize_text(value_text) or (
            parse_resistance_ohms(value_text) is not None
            and parse_capacitance_farads(value_text) is None
        ):
            return "resistor"
        return "capacitor"
    if reference.startswith("Q") or "transistor" in evidence or "mosfet" in evidence:
        return "transistor"
    # Diodes: D-prefixed references, or schottky/tvs/rectifier/zener in evidence
    if reference.startswith("D") and not reference.startswith("DN"):
        return "diode"
    if any(d in evidence for d in ["d_schottky", "d_tvs", "d_rectifier", "d_zener", "d_zener_sod"]):
        return "diode"
    # Resettable PTC fuses (SparkFun draws them on F references with a fuse
    # symbol; the value is a voltage/hold/trip rating triplet, not an MPN).
    if reference.startswith("F") and not reference.startswith("FID") and "fuse" in evidence:
        return "fuse"
    # Generic through-hole 2.54 mm pin headers: KiCad's Conn_01xNN symbols on
    # PinHeader_1xNN_P2.54mm footprints, and SparkFun's 1xNN footprints (2.54 mm
    # with or without an explicit _P2.54mm suffix). A SparkFun 1xNN footprint is
    # a 2.54 mm header whatever symbol sits on it -- SparkFun also uses
    # I2C_01xNN and friends on the same footprints -- so the footprint alone is
    # sufficient there. JST and other finer-pitch Conn_01xNN symbols stay
    # excluded from the symbol-driven branch.
    sparkfun_header_footprint = bool(
        re.fullmatch(r"sparkfun_connector_1x\d+(_p2_54mm)?", normalize_text(fields["footprint"]))
    )
    # e-radionica (Soldered) boards use their own header footprints:
    # HEADER_MALE_NX1 is the plain 2.54 mm header row; HEADER-UPDI is the
    # 1x03 UPDI programming header.
    erad_header_footprint = bool(
        re.search(r"header_male_\d+x\d+", normalize_text(fields["footprint"]))
    ) or "header_updi" in normalize_text(fields["footprint"])
    dual_row_header_footprint = bool(re.search(r"pinheader_2x\d+_p2_54mm", normalize_text(fields["footprint"])))
    # Eagle libraries name plain 2.54 mm headers "1X06_ROUND_70" and friends;
    # the footprint name alone carries the pin count.
    eagle_header_footprint = bool(re.match(r"1x\d+", normalize_text(fields["footprint"])))
    if sparkfun_header_footprint or erad_header_footprint or dual_row_header_footprint or eagle_header_footprint or (
        "conn_01x" in evidence
        and "jst" not in evidence
        and "pinheader" in evidence
        and "2_54mm" in evidence
    ):
        return "connector_header"
    if reference.startswith("Y") and "crystal" in evidence:
        return "crystal"
    # USB-C and other connectors
    if "usb_c_receptacle" in evidence or "usb_c" in evidence:
        return "connector"
    if reference.startswith("J") and ("conn_" in evidence or "header" in evidence or "receptacle" in evidence):
        return "connector"
    # Eagle-import boards label connectors CONN<nn> and draw the 1 mm JST SH
    # socket under its raw footprint name (JST_SH4).
    if reference.startswith("CONN") or re.fullmatch(r"jst_sh\d+", normalize_text(fields["footprint"])):
        return "connector"
    return ""


def infer_package_size(fields):
    evidence = " ".join([fields["footprint"], fields["library_id"], fields["value"]]).lower()
    for package_size in PACKAGE_SIZES:
        if re.search(rf"(?<!\d){re.escape(package_size)}(?!\d)", evidence):
            return package_size
    if any(token in evidence for token in ["din0207", "quarter_watt", "axial_6", "axial-din0207"]):
        return "quarter_watt_through_hole"
    return ""


def infer_led_color(fields):
    evidence = normalize_text(" ".join([fields["value"], fields["library_id"]]))
    for color in LED_COLORS:
        if color in evidence:
            return color
    return ""


def proposed_oomp_id(component):
    fields = component_fields(component)
    kind = infer_kind(fields)
    package_size = infer_package_size(fields)

    pcb = component.get("pcb") or {}
    mounting_holes = pcb.get("mounting_holes") or []
    if pcb.get("is_mounting_hole", False) and len(mounting_holes) > 0:
        return str(mounting_holes[0].get("oomp_id", ""))

    exact_signature = tuple(
        normalize_text(fields[field_name])
        for field_name in ("value", "footprint", "library_id")
    )
    exact_match = EXACT_COMPONENT_MATCHES.get(exact_signature)
    if exact_match:
        return exact_match

    # Known value/MPN aliases point straight at an exact catalogue part.
    # A bare value may only alias when the schematic carries no MPN -- a
    # specific MPN ("BSS138-13-F") means the exact identity is known and needs
    # its own part. An MPN alias requires the normalized MPN to be exact.
    value_normalized = normalize_text(fields["value"])
    mpn_normalized = normalize_text(fields["mpn"])
    # Footprint-qualified identities: the bare schematic value is ambiguous
    # across packages, so the footprint picks the catalogue part.
    footprint_name = normalize_text(fields["footprint"])
    # Common imported footprints carry the exact switch or capacitor identity
    # even when the schematic value is only a generic symbol/value.
    if "pts810" in footprint_name:
        return "electronic_switch_tactile_surface_mount_pts810"
    if "gt_tc026x_hxxx_lx" in footprint_name:
        return "electronic_switch_tactile_through_hole_gt_tc026x_hxxx_lx"
    if "b3fs_100x" in footprint_name:
        return "electronic_switch_tactile_surface_mount_omron_b3fs_100xp"
    if "ml414h" in footprint_name or "ml414h" in value_normalized:
        return "electronic_battery_coin_cell_6_8_mm_maxell_ml414h"
    if normalize_text(fields["value"]) in {"10uf", "10u"} and "0805" in footprint_name:
        return "electronic_capacitor_0805_10_micro_farad"
    if "1x01_1x1mm" in footprint_name:
        return "electronic_connector_header_2_54_mm_pitch_through_hole_1_pin"
    if "audio_jack_3_5mm_trrs" in footprint_name:
        return "electronic_connector_audio_jack_surface_mount_right_angle_trrs_3_5_mm_audio_jack_3_5_mm_trrs"
    if "microsd_external_pin" in footprint_name:
        return "electronic_connector_micro_sd_push_push_micro_sd_external_pin"
    if "microsd_friction_fit" in footprint_name:
        return "electronic_connector_micro_sd_friction_fit_micro_sd_friction_fit"
    if "terminal_kf235_5_0_2p" in footprint_name:
        return "electronic_connector_terminal_block_5_mm_pitch_through_hole_2_pin_kf235_5_0_2p"
    if "jst_smd_1_25mm_6_locking" in footprint_name or "jst_1_25mm_6_locking" in footprint_name:
        return "electronic_connector_jst_1_25_mm_pitch_surface_mount_6_pin_locking_jst_smd_1_25_mm_6_locking"
    if "2x10_2_0mm_male_pins_vertical_smd_pegs" in footprint_name:
        return "electronic_connector_gnss_header_2_mm_pitch_surface_mount_20_pin_plug_in_conn_02x10_gnss_plug_in_header"
    if "screwterminal_1x03_p3_5mm" in footprint_name or "screw_terminal_1x03_p3_5mm" in footprint_name:
        return "electronic_connector_terminal_block_3_5_mm_pitch_through_hole_3_pin_screw_terminal_1x03_p3_5_mm"
    if "c_0603_1608metric" in footprint_name and any(
        marker in normalize_text(fields.get("library_id", "")) for marker in ("inductor", "coil", "ferrite")
    ):
        if normalize_text(fields.get("value", "")) == "470ohm":
            return "electronic_inductor_0603_470_ohm"
        if normalize_text(fields.get("value", "")) == "30ohm":
            return "electronic_inductor_0603_30_ohm"
    if "sparkfun_switch_navigation_smd_9_9x9_9mm" in footprint_name:
        return "electronic_switch_navigation_surface_mount_9_9_mm"
    if "sparkfun_switch_navigation_smd_7_5x7_5mm" in footprint_name:
        return "electronic_switch_navigation_surface_mount_7_5_mm"
    if "rollerencoder_rollerencoder" in footprint_name:
        return "electronic_switch_roller_encoder_through_hole_roller_encoder_switch"
    if re.search(r"\bbss138\b", value_normalized) and "sot363" in footprint_name:
        # A BSS138-style value drawn on SOT-363 (SC-70-6) is the I2C
        # level-shifter dual FET, not the single SOT-23 BSS138.
        return "electronic_transistor_sot_363_6_mosfet_n_channel_dual"
    if re.search(r"\b1n4148\b", value_normalized):
        # The 1N4148 order suffix follows the package.
        if "sod_323" in footprint_name:
            return "electronic_diode_switching_sod_323_onsemi_1n4148ws"
        if "sod_523f" in footprint_name:
            return "electronic_diode_switching_sod_523f_onsemi_1n4148wt"
    if mpn_normalized:
        if mpn_normalized in KNOWN_PART_ALIASES:
            return KNOWN_PART_ALIASES[mpn_normalized]
    else:
        for alias, oomp_id in KNOWN_PART_ALIASES.items():
            # \b keeps "2N7002" from matching the "2N7002K" variant.
            if re.search(rf"\b{re.escape(alias)}\b", value_normalized):
                return oomp_id

    if kind == "resistor":
        resistance = resistance_taxonomy(fields["value"])
        if package_size and resistance != "":
            return f"electronic_resistor_{package_size}_{resistance}_ohm"

    if kind == "resistor_array":
        resistance = resistance_taxonomy(fields["value"])
        if resistance != "":
            return f"electronic_resistor_array_4_x_0402_convex_{resistance}_ohm_8_pin"

    if kind == "capacitor":
        capacitance = capacitance_taxonomy(fields["value"])
        if package_size and capacitance:
            evidence = normalize_text(
                " ".join([fields["footprint"], fields["library_id"], fields["value"]])
            )
            if "tantal" in evidence or "kemet" in evidence or "eia" in evidence:
                if package_size == "3216":
                    # AVX-A / Kemet-I tantalum family: nominal voltage per value.
                    voltage = "10_volt" if capacitance.startswith("22_") else "16_volt"
                    return f"electronic_capacitor_{package_size}_avx_a_tantalum_{capacitance}_{voltage}"
            return f"electronic_capacitor_{package_size}_{capacitance}"

    if kind == "inductor":
        inductance = inductance_taxonomy(fields["value"])
        if package_size and inductance:
            return f"electronic_inductor_{package_size}_{inductance}"

    if kind == "ferrite_bead":
        # The generic catalogue bead (created for the Soldered "0603L" boards);
        # specific MPNs keep coming through aliases and overrides.
        if package_size == "0603":
            return "electronic_ferrite_bead_0603_600_ohm_500_milliamp"

    if kind == "led" and package_size:
        value_text = normalize_text(fields["value"])
        library_text = normalize_text(fields["library_id"])
        color = infer_led_color(fields)
        if "ws2812" in value_text or "ws2812" in library_text:
            if package_size == "1010":
                return "electronic_led_1010_rgb_ws2812b_xinglight_1010rgbc"
            if package_size == "5050":
                return "electronic_led_5050_rgb_ws2812b_worldsemi_ws2812b_b_w"
        if color:
            return f"electronic_led_{package_size}_{color}"
        return f"electronic_led_{package_size}"

    if kind == "connector_header":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])
        dual_row = False
        pin_count = None
        m = re.search(r"conn_01x(\d+)", value_text)
        if m:
            pin_count = int(m.group(1))
        else:
            m = re.search(r"pinheader_1x(\d+)_p2_54mm", footprint_text) or re.fullmatch(
                r"sparkfun_connector_1x(\d+)(?:_p2_54mm)?", footprint_text
            ) or re.match(r"1x(\d+)", footprint_text)
            if m:
                pin_count = int(m.group(1))
        if not pin_count:
            # Dual-row headers (ICSP and friends): PinHeader_2x03_P2.54mm.
            m = re.search(r"pinheader_2x(\d+)_p2_54mm", footprint_text)
            if m:
                pin_count = 2 * int(m.group(1))
                dual_row = True
        if not pin_count:
            # e-radionica HEADER_MALE_NX1 and the 1x03 UPDI header.
            m = re.search(r"header_male_(\d+)x(\d+)", footprint_text)
            if m:
                pin_count = int(m.group(1)) * int(m.group(2))
            elif "header_updi" in footprint_text or "header_updi" in value_text:
                pin_count = 3
        if pin_count:
            if dual_row:
                return f"electronic_connector_header_2_54_mm_pitch_through_hole_dual_row_{pin_count}_pin"
            return f"electronic_connector_header_2_54_mm_pitch_through_hole_{pin_count}_pin"

    if kind == "crystal":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])

        # Parse frequency
        freq_match = re.search(r"(\d+(?:_\d+)?)[_\s]*(mhz|khz)", value_text)
        if not freq_match:
            return ""
        freq_num = freq_match.group(1).replace("_", ".")
        freq_unit = freq_match.group(2)
        if freq_unit == "mhz":
            freq_taxonomy = freq_num.replace(".", "_") + "_mhz"
        else:
            freq_taxonomy = freq_num.replace(".", "_") + "_khz"

        # Parse package and pin count from footprint
        pkg_match = re.search(r"crystal_smd_(\d+)_(\d)pin", footprint_text)
        if not pkg_match:
            # Size-styled footprints ("Crystal_SMD_3.2x2.5mm") name the body;
            # a 3225 body is the standard 4-pad ceramic resonator can.
            size_match = re.search(r"crystal_smd_(\d+)_(\d)x(\d+)_(\d+)mm", footprint_text)
            if not size_match:
                return ""
            package = f"{size_match.group(1)}{size_match.group(2)}{size_match.group(3)}{size_match.group(4)}"
            pin_count = "4_pin" if package in ("3225", "2520") else "2_pin"
        else:
            package = pkg_match.group(1)
            pin_count = pkg_match.group(2) + "_pin"

        # Default load capacitance by frequency
        if "32_768" in freq_taxonomy:
            load_cap = "12_5_pf"
        else:
            load_cap = "20_pf"

        return f"electronic_crystal_{package}_surface_mount_{pin_count}_{freq_taxonomy}_{load_cap}"

    if kind == "diode":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])
        library_text = normalize_text(fields["library_id"])

        # Determine diode type
        diode_type = ""
        if "schottky" in value_text or "schottky" in library_text:
            diode_type = "schottky"
        elif "tvs" in value_text or "tvs" in library_text or "esd" in value_text or "pesd" in value_text:
            diode_type = "tvs"
        elif "zener" in value_text or "zener" in library_text:
            diode_type = "zener"
        elif "switching" in value_text or "switching" in library_text:
            diode_type = "switching"
        elif "rectifier" in value_text or "rectifier" in library_text:
            diode_type = "rectifier"
        else:
            # Default for generic D_Schottky and similar
            diode_type = "schottky"

        # Determine package from footprint
        package = ""
        for pkg_token in ["sod_123", "sod_323", "sod_523f", "sod_523", "sot_23", "sot_143", "sot_523", "d_0402", "d_0603"]:
            if pkg_token in footprint_text or pkg_token in library_text:
                if pkg_token.startswith("d_"):
                    package = pkg_token[2:]
                else:
                    package = pkg_token
                break

        if diode_type and package:
            return f"electronic_diode_{diode_type}_{package}"

    if kind == "fuse" and package_size:
        return f"electronic_fuse_{package_size}_resettable"

    if kind == "connector":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])
        library_text = normalize_text(fields["library_id"])

        # Qwiic / STEMMA QT boards draw the 1 mm JST SH socket under the raw
        # eagle footprint name (JST_SH4); the catalogue carries the
        # right-angle part for every pin count.
        m = re.fullmatch(r"jst_sh(\d+)", footprint_text)
        if m:
            pin_count = int(m.group(1))
            return (
                "electronic_connector_jst_sh_1_mm_pitch_surface_mount_right_angle_"
                f"{pin_count}_pin_jst_sm{pin_count:02d}b_srss_tb"
            )

        # USB-C receptacle
        if "usb_c" in value_text or "usb_c" in library_text or "usb_c" in footprint_text:
            return "electronic_connector_usb_c_surface_mount_16_pin"

    return ""


class OompPartIndex:
    def __init__(self, parts_directory):
        self.parts_directory = Path(parts_directory).resolve()
        self.parts = []
        self.by_id = {}
        self.generic_parts = []
        self._load()

    def _load(self):
        if not self.parts_directory.is_dir():
            raise FileNotFoundError(f"OOMP parts directory does not exist: {self.parts_directory}")
        for part_directory in sorted(self.parts_directory.iterdir()):
            working_yaml = part_directory / "working.yaml"
            if not part_directory.is_dir() or not working_yaml.is_file():
                continue
            part = {
                "oomp_id": part_directory.name,
                "directory": str(part_directory),
                "working_yaml": str(working_yaml),
                "tokens": set(part_directory.name.lower().split("_")),
            }
            self.parts.append(part)
            self.by_id[part["oomp_id"]] = part
            # Generic family matching is opt-in population data, never a guess
            # from a similar suffix. The C loader keeps the metadata pass small.
            if part_directory.name.startswith("electronic_"):
                loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
                metadata = yaml.load(working_yaml.read_text(encoding="utf-8"), Loader=loader) or {}
                rules = metadata.get("generic_match") or {}
                if rules:
                    self.generic_parts.append({
                        "oomp_id": part_directory.name,
                        "kind": metadata.get("taxonomy_2", ""),
                        "package": metadata.get("taxonomy_3", ""),
                        "rules": rules,
                    })

    def generic_matches(self, fields):
        if fields.get("mpn") or fields.get("manufacturer"):
            return []
        matches = []
        for part in self.generic_parts:
            rules = part["rules"]
            checks = [
                ["value", "values"],
                ["library_id", "symbols"],
                ["footprint", "footprints"],
            ]
            agrees = True
            for field_name, rule_name in checks:
                accepted_values = []
                for accepted_value in rules.get(rule_name, []):
                    accepted_values.append(normalize_text(accepted_value))
                if normalize_text(fields.get(field_name, "")) not in accepted_values:
                    agrees = False
            if agrees:
                matches.append(part)
        return matches

    def candidate_parts(self, kind):
        if kind:
            prefix = f"electronic_{kind}_"
            if kind == "mounting_hole":
                prefix = "mechanical_mounting_hole_"
            return [part for part in self.parts if part["oomp_id"].startswith(prefix)]
        return []


def _is_board_feature(fields):
    """Silkscreen art, fiducials, test points, standoffs and solder-jumper
    traces live on the board but are never purchased, like DNF parts."""
    footprint = normalize_text(fields["footprint"])
    library_id = normalize_text(fields["library_id"])
    value = normalize_text(fields["value"])
    reference_upper = str(fields.get("reference", "")).upper()
    board_feature_evidence = " ".join([footprint, library_id, value])
    if "buzzard" in board_feature_evidence or "kibuzzard" in board_feature_evidence:
        return True
    if "fiducial" in board_feature_evidence or reference_upper.startswith("FID") or reference_upper.startswith("FD"):
        return True
    if "standoff" in board_feature_evidence:
        return True
    if "testpoint" in board_feature_evidence or "test_point" in board_feature_evidence or (
        reference_upper.startswith("TP") and "test" in board_feature_evidence
    ):
        return True
    if "logo" in board_feature_evidence or "oshw" in board_feature_evidence:
        return True
    if "soldered_graphics" in board_feature_evidence or "sparkfun_aesthetic" in board_feature_evidence:
        return True
    if "smd_jumper" in board_feature_evidence or "jumper_2_nc" in board_feature_evidence or (
        value.startswith("smd_jumper")
    ):
        return True
    # KiCad's standard SolderJumper-* footprints are exposed copper option
    # pads, not purchased components.  Treat them as board features even when
    # the schematic reference is not prefixed SJ (common in imported boards).
    if "solderjumper" in footprint or "solder_jumper" in footprint:
        return True
    # Jumper_2_NC_Trace / Jumper_3_NC-2_Trace and friends: NC solder-blob
    # traces, not purchased parts.
    if "jumper" in board_feature_evidence and ("_trace" in board_feature_evidence or "_nc" in board_feature_evidence or "nc_" in board_feature_evidence):
        return True
    # Jumper_2_NO / Jumper_3_NO: unpopulated solder-blob option pads.
    if re.search(r"jumper_\d+_no", board_feature_evidence):
        return True
    # Soldered "PAD_2x1.5": exposed probe/sensing pads etched in the board copper.
    if value.startswith("pad_") and reference_upper.startswith("PAD"):
        return True
    # Footprint-only outline graphics (SparkFun "BMV080_Outline" on REF**).
    # "NOOUTLINE" is an Eagle-import pad naming artifact (0805-NO /
    # CHIPLED_0603_NOOUTLINE are ordinary two-pad parts), so it must not count.
    if re.search(r"(?<!no)outline", board_feature_evidence):
        return True
    # Eagle-import boards carry silkscreen art and board graphics as U$-numbered
    # footprints (logos, revision features, connector artwork); real parts keep
    # lettered references.
    if reference_upper.startswith("U$"):
        return True
    if value in ("measure",) and "jumper" in board_feature_evidence:
        return True
    return False


def _is_physical_component(component):
    reference = component.get("reference", "")
    reference_upper = reference.upper()
    fields = component_fields(component)
    footprint = normalize_text(fields["footprint"])

    pcb = component.get("pcb") or {}
    if pcb.get("is_mounting_hole", False):
        return True

    if reference_upper.startswith("SJ"):
        return False
    if reference_upper.startswith("UNK_HOLE"):
        return False
    if footprint.startswith("dummyfp"):
        return False
    if reference.startswith("#"):
        return False
    value_upper = str(fields.get("value", "")).strip().upper()
    if value_upper in ("DNF", "DNP"):
        return False
    if _is_board_feature(fields):
        return False
    if component.get("pcb"):
        return True
    for unit in (component.get("schematic") or {}).get("units", []):
        if unit.get("on_board") and (unit.get("properties") or {}).get("Footprint"):
            return True
    return False


def _rank_candidates(index, component, proposed_id, kind, maximum=5):
    fields = component_fields(component)
    package_size = infer_package_size(fields)
    query_tokens = set(
        normalize_text(
            " ".join(
                [kind, infer_package_size(fields), fields["value"], fields["footprint"], fields["library_id"]]
            )
        ).split("_")
    )
    query_numeric_value = None
    if kind == "resistor":
        query_numeric_value = parse_resistance_ohms(fields["value"])
    elif kind == "capacitor":
        query_numeric_value = parse_capacitance_farads(fields["value"])

    def candidate_numeric_value(part_id):
        if kind == "resistor":
            match = re.search(r"_([0-9]+(?:_[0-9]+)?)_ohm$", part_id)
            return float(match.group(1).replace("_", ".")) if match else None
        if kind == "capacitor":
            match = re.search(r"_([0-9]+(?:_[0-9]+)?)_(pico|nano|micro|milli)_farad(?:_|$)", part_id)
            if not match:
                return None
            number = float(match.group(1).replace("_", "."))
            multipliers = {"pico": 1e-12, "nano": 1e-9, "micro": 1e-6, "milli": 1e-3}
            return number * multipliers[match.group(2)]
        return None

    candidates = []
    for part in index.candidate_parts(kind):
        part_tokens = part["tokens"]
        union = query_tokens | part_tokens
        token_score = len(query_tokens & part_tokens) / len(union) if union else 0
        text_score = SequenceMatcher(None, proposed_id or normalize_text(fields["value"]), part["oomp_id"]).ratio()
        candidate_value = candidate_numeric_value(part["oomp_id"])
        same_package = bool(package_size and f"_{package_size}_" in part["oomp_id"])
        reasons = ["same component family"]
        if same_package:
            reasons.append("same package size")
        if query_numeric_value is not None and candidate_value is not None:
            if query_numeric_value == candidate_value:
                numeric_score = 1.0
                reasons.append("same normalized value")
            elif query_numeric_value > 0 and candidate_value > 0:
                numeric_score = max(0.0, 1.0 - abs(math.log10(candidate_value / query_numeric_value)))
                reasons.append("nearby normalized value")
            else:
                numeric_score = 0.0
            score = round(numeric_score * 0.7 + float(same_package) * 0.25 + text_score * 0.05, 4)
        else:
            score = round(token_score * 0.65 + text_score * 0.35, 4)
        candidates.append({"oomp_id": part["oomp_id"], "score": score, "reasons": reasons})
    candidates.sort(key=lambda candidate: (-candidate["score"], candidate["oomp_id"]))
    return candidates[:maximum]


def match_component(index, component, overrides=None, blocked=None):
    overrides = overrides or {}
    reference = component.get("reference", "")
    fields = component_fields(component)
    kind = infer_kind(fields)
    pcb = component.get("pcb") or {}
    if pcb.get("is_mounting_hole", False):
        kind = "mounting_hole"
    package_size = infer_package_size(fields)
    proposed_id = proposed_oomp_id(component)

    result = {
        "status": "unmatched",
        "accepted": False,
        "oomp_id": None,
        "confidence": 0.0,
        "proposed_oomp_id": proposed_id or None,
        "inferred": {
            "kind": kind or None,
            "package_size": package_size or None,
            "value": fields["value"] or None,
            "mpn": fields["mpn"] or None,
        },
        "reasons": [],
        "candidates": [],
    }

    if not _is_physical_component(component):
        result["status"] = "not_applicable"
        reference_upper = reference.upper()
        footprint = normalize_text(fields["footprint"])
        value_upper = str(fields.get("value", "")).strip().upper()
        if value_upper in ("DNF", "DNP"):
            result["reasons"].append("Component is marked do-not-fit / do-not-populate and has no purchased OOMP part requirement.")
        elif _is_board_feature(fields):
            if reference_upper.startswith("U$"):
                result["reasons"].append("Eagle-import U$ footprints are board artwork (logos and board graphics), not purchased OOMP parts.")
            else:
                result["reasons"].append("Fiducials, logos, test points, standoffs and solder-jumper traces are board features, not purchased OOMP parts.")
        elif reference_upper.startswith("SJ"):
            result["reasons"].append("PCB solder jumpers are board features, not purchased OOMP parts.")
        elif reference_upper.startswith("UNK_HOLE") or footprint.startswith("dummyfp"):
            result["reasons"].append("Mechanical or dummy mounting holes do not require OOMP parts.")
        else:
            result["reasons"].append("The symbol has no physical PCB/OOMP part requirement.")
        return result

    if reference in (blocked or {}):
        # A blocked reference is a documented decision, not an unexplained
        # failure: it keeps the reason text and leaves the unmatched report
        # to genuinely unexplained components.
        result["status"] = "blocked"
        result["reasons"].append(str(blocked[reference]))
        return result

    override_id = overrides.get(reference)
    if override_id:
        if override_id in index.by_id:
            result.update(
                {
                    "status": "matched",
                    "accepted": True,
                    "oomp_id": override_id,
                    "confidence": 1.0,
                    "reasons": ["Accepted from the AI/human match override file."],
                }
            )
        else:
            result["reasons"].append(f"Override refers to missing OOMP part: {override_id}")
        return result

    explicit_ids = []
    for library_id in [fields.get("footprint", ""), fields.get("library_id", "")]:
        if ":" not in library_id:
            continue
        nickname, entry = library_id.split(":", 1)
        if nickname in ["OOMP", "OOMP_MachineSolder", "OOMP_HandSolder"] and entry not in explicit_ids:
            explicit_ids.append(entry)
    if explicit_ids:
        if len(explicit_ids) == 1 and explicit_ids[0] in index.by_id:
            result.update(status="matched", accepted=True, oomp_id=explicit_ids[0], confidence=1.0,
                          reasons=["Explicit OOMP KiCad library identifier."])
        else:
            result.update(status="ambiguous", reasons=["Conflicting or unavailable explicit OOMP library identifiers."])
        return result

    if proposed_id and proposed_id in index.by_id:
        result.update(
            {
                "status": "matched",
                "accepted": True,
                "oomp_id": proposed_id,
                "confidence": 1.0,
                "reasons": [
                    "Exact OOMP ID constructed from component type, package size, and normalized value."
                ],
            }
        )
        return result

    generic_matches = index.generic_matches(fields)
    if len(generic_matches) == 1:
        generic_part = generic_matches[0]
        result.update(
            status="matched",
            accepted=True,
            oomp_id=generic_part["oomp_id"],
            confidence=1.0,
            identity_scope="generic_family",
            reasons=["Generic value, symbol and footprint agree with the populated matching rule; no manufacturer or MPN was supplied."],
        )
        result["inferred"]["kind"] = generic_part["kind"]
        result["inferred"]["package_size"] = generic_part["package"]
        return result
    if len(generic_matches) > 1:
        result.update(status="ambiguous", reasons=["More than one populated generic family rule matches this component."])
        return result

    result["candidates"] = _rank_candidates(index, component, proposed_id, kind)
    if not kind:
        result["reasons"].append("No supported OOMP component family could be inferred.")
    elif not package_size:
        result["reasons"].append("Component family was inferred, but package size was not.")
    elif proposed_id:
        result["reasons"].append("The exact normalized component is not present in the OOMP parts directory.")
    else:
        result["reasons"].append("The component value could not be normalized into an OOMP ID.")
    return result


def load_overrides(path):
    if path is None or not Path(path).is_file():
        return {}
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    if "matches" in data:
        data = data["matches"] or {}
    return {str(reference): str(oomp_id) for reference, oomp_id in data.items()}


def main():
    parser = argparse.ArgumentParser(description="Match extracted KiCad components to OOMP parts.")
    parser.add_argument("component_file", help="JSON file containing one component or a components list")
    parser.add_argument("--parts-dir", default="parts", help="OOMP parts directory")
    parser.add_argument("--overrides", help="Optional YAML reference-to-OOMP override file")
    parser.add_argument("--output", help="Optional JSON output file; stdout is used when omitted")
    arguments = parser.parse_args()

    source_data = json.loads(Path(arguments.component_file).read_text(encoding="utf-8"))
    components = source_data.get("components", source_data) if isinstance(source_data, dict) else source_data
    one_component = isinstance(components, dict)
    if one_component:
        components = [components]

    index = OompPartIndex(arguments.parts_dir)
    overrides = load_overrides(arguments.overrides)
    results = [
        {
            "reference": component.get("reference", ""),
            "match": match_component(index, component, overrides=overrides),
        }
        for component in components
    ]
    output_data = results[0] if one_component else {"matches": results}
    rendered = json.dumps(output_data, indent=2, ensure_ascii=False) + "\n"
    if arguments.output:
        output_path = Path(arguments.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
