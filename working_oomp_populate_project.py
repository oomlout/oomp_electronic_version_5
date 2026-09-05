import re


def _normalize_project_slug(value):
    if value is None:
        return ""
    normalized = str(value).strip()
    normalized = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", normalized)
    normalized = normalized.lower()
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    return normalized


def _select_active_version(versions):
    if not versions:
        return {"version": "current", "git_ref": "main"}

    current_versions = [
        details
        for details in versions
        if str(details.get("version", "current")).strip().lower() == "current"
    ]
    if current_versions:
        return current_versions[0]

    numeric_versions = []
    for details in versions:
        raw_version = str(details.get("version", "current")).strip()
        version_string = raw_version.lower().removeprefix("v")
        digits = [int(part) for part in re.findall(r"\d+", version_string)]
        numeric_versions.append((digits, details))
    if numeric_versions:
        _, selected = max(numeric_versions, key=lambda item: (item[0] or [0],))
        return selected
    return versions[0]


def _collapse_historial_versions(versions):
    if not versions:
        return [{"version": "current"}]

    version_labels = []
    for details in versions:
        label = str(details.get("version", "current")).strip()
        if label:
            version_labels.append(label)

    if len(set(version_labels)) <= 1:
        return list(versions)

    return [_select_active_version(versions)]


def main(**kwargs):
    options = kwargs.get("options", [])

    # Add projects here.  Each version is a plain dictionary so an older board
    # revision can point at a tag/commit and a different KiCad file stem.
    projects = [
        {
            "github_user": "electrolama",
            "github_repository": "pt1",
            "repository_url": "https://github.com/electrolama/pt1.git",
            "versions": [
                {
                    "version": "current",
                    "git_ref": "main",
                    "project_file_folder": "pcba/Rev A2",
                    "project_file_basename": "pt1-RevA2",
                    "project_file_path": "pcba/Rev A2/pt1-RevA2",
                    "project_file_path_original": "C:\\gh\\oomp_electronic_version_5\\project\\electrolama\\pt1\\git\\pt1\\pcba\\Rev A2\\pt1-RevA2",
                    "match_overrides": {
                        "CON1": "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12",
                        "CON2": "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12",
                        "CON3": "electronic_connector_usb_a_surface_mount_4_pin_shenzhen_jing_tuo_jin_electronics_912121a2023s10100",
                        "D1": "electronic_diode_tvs_array_sot_23_6_protek_srv054pt7",
                        "D2": "electronic_diode_tvs_array_sot_23_6_protek_srv054pt7",
                        "IC1": "electronic_ic_qfn_16_3_mm_x_3_mm_converter_usb_to_serial_converter_wch_ch343p",
                        "IC2": "electronic_ic_sop_16_controller_usb_hub_controller_4_port_corechips_sl21a",
                        "IC3": "electronic_ic_sot_23_6_logic_configurable_multi_function_gate_texas_instruments_sn74lvc1g57dbvr",
                        "IC4": "electronic_ic_tsot_23_5_power_management_high_side_power_switch_with_flag_richtek_rt9742cgj5",
                        "J1": "electronic_connector_header_2_54_mm_pitch_through_hole_6_pin",
                        "L1": "electronic_ferrite_bead_0805_220_ohm_2_amp_murata_blm21pg221sn1d",
                        "XT1": "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf",
                    },
                }
            ],
        },
        {
            "github_user": "dangerousprototypes",
            "github_repository": "buspirate5_hardware",
            "github_url": "https://github.com/DangerousPrototypes/BusPirate5-hardware",
            "repository_url": "https://github.com/DangerousPrototypes/BusPirate5-hardware.git",
            "versions": [
                {
                    "version": "5_rev10a",
                    "git_ref": "main",
                    "sparse_checkout": True,
                    "project_file_folder": "bus_pirate_pcb/5-REV10A",
                    "project_file_basename": "REV10a",
                    "project_file_path": "bus_pirate_pcb/5-REV10A/REV10a",
                    "project_file_path_original": "",
                    "match_overrides": {
                        "D401": "electronic_diode_switching_sod_523f_onsemi_1n4148wt",
                        "D601": "electronic_diode_switching_sod_523f_onsemi_1n4148wt",
                        "D602": "electronic_diode_switching_sod_523f_onsemi_1n4148wt",
                        "D603": "electronic_diode_switching_sod_523f_onsemi_1n4148wt",
                        "D500": "electronic_diode_schottky_dual_common_cathode_sot_523_diodes_incorporated_bas40t_05",
                        "D501": "electronic_diode_schottky_dual_common_cathode_sot_523_diodes_incorporated_bas40t_05",
                        "D502": "electronic_diode_schottky_dual_common_cathode_sot_523_diodes_incorporated_bas40t_05",
                        "D503": "electronic_diode_schottky_dual_common_cathode_sot_523_diodes_incorporated_bas40t_05",
                        "D504": "electronic_diode_schottky_dual_common_cathode_sot_523_diodes_incorporated_bas40t_05",
                        "J201": "electronic_connector_header_2_54_mm_pitch_through_hole_3_pin_socket_kinghelm_kh_2_54fh_1x3p_h8_5",
                        "J202": "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12",
                        "J301": "electronic_connector_header_2_54_mm_pitch_through_hole_10_pin",
                        "J302": "electronic_connector_jst_sh_1_mm_pitch_surface_mount_right_angle_9_pin_jst_sm09b_srss_tb",
                        "L201": "electronic_ferrite_bead_0805_15_ohm_1_5_amp_tdk_mmz2012r150at000",
                        "LCD201": "electronic_display_tft_2_inch_240_x_320_pixel_ips_spi_12_pin_szhtc_qt200h1201",
                        "Q202": "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_300_milliamp_cbi_mmbt7002k",
                        "Q300": "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
                        "Q301": "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
                        "Q302": "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
                        "Q303": "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
                        "Q304": "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
                        "Q305": "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
                        "Q306": "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
                        "Q307": "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
                        "Q401": "electronic_transistor_sot_363_6_bipolar_pnp_dual_matched_pair_45_volt_100_milliamp_diodes_incorporated_bcm857bs_7_f",
                        "Q402": "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
                        "Q601": "electronic_transistor_sot_363_6_bipolar_pnp_dual_general_purpose_40_volt_200_milliamp_cbi_mmdt3906dw",
                        "Q602": "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a",
                        "U404": "electronic_ic_sot_23_5_amplifier_operational_single_rail_to_rail_input_output_gainsil_lmv321_tr",
                        "U504": "electronic_ic_tssop_14_amplifier_operational_quad_rail_to_rail_output_texas_instruments_lmv324ipwr",
                        "U505": "electronic_ic_tssop_14_amplifier_operational_quad_rail_to_rail_output_texas_instruments_lmv324ipwr",
                        "U506": "electronic_ic_sot_23_5_amplifier_operational_single_rail_to_rail_input_output_gainsil_lmv321_tr",
                        "U601": "electronic_ic_sot_23_5_amplifier_operational_single_precision_rail_to_rail_input_output_gainsil_gs321a_tr",
                        "U602": "electronic_ic_sot_23_5_comparator_single_open_collector_texas_instruments_lmv331idbvr",
                        "U603": "electronic_ic_sot_23_5_amplifier_operational_single_rail_to_rail_input_output_gainsil_lmv321_tr",
                        "Y101": "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf",
                        "LED701": "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a",
                        "LED702": "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
                        "LED703": "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
                        "LED704": "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a",
                        "LED705": "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
                        "LED706": "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
                        "LED707": "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a",
                        "LED708": "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a",
                        "LED710": "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
                        "LED712": "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a",
                        "LED713": "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
                        "LED714": "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
                        "LED715": "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
                        "LED716": "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a",
                        "LED717": "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a",
                        "LED718": "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
                        "LED719": "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
                        "LED720": "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a",
                        "U102": "electronic_ic_sop_8_5_28_mm_x_5_23_mm_memory_spi_nor_flash_128_mbit_winbond_w25q128jvsiq",
                        "U103": "electronic_ic_qfn_56_7_mm_x_7_mm_microcontroller_dual_core_arm_cortex_m0_plus_raspberry_pi_rp2040",
                        "U105": "electronic_ic_updfn_8_memory_spi_nand_flash_1_gbit_micron_mt29f1g01abafdwb",
                        "U301": "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
                        "U302": "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
                        "U303": "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
                        "U304": "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
                        "U305": "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
                        "U306": "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
                        "U307": "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
                        "U308": "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
                        "U401": "electronic_ic_sot_89_3_power_management_linear_voltage_regulator_3_3_volt_microne_me6211a33pg_n",
                        "U402": "electronic_ic_tssop_24_logic_16_channel_analog_multiplexer_nexperia_74hct4067pw118",
                        "U403": "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_3_3_volt_diodes_ap2127k_3_3trg1",
                        "U501": "electronic_ic_tssop_16_logic_serial_in_parallel_out_shift_register_wuxi_i_core_elec_aip74hc595ta16_tr",
                        "U502": "electronic_ic_tssop_16_logic_serial_in_parallel_out_shift_register_wuxi_i_core_elec_aip74hc595ta16_tr",
                        "U503": "electronic_ic_tssop_20_logic_octal_bus_transceiver_wuxi_i_core_elec_aip74hct245ta20_tr",
                    },
                }
            ],
        },
        {
            "github_user": "hanqaqa",
            "github_repository": "easyduino",
            "github_url": "https://github.com/Hanqaqa/Easyduino",
            "repository_url": "https://github.com/Hanqaqa/Easyduino.git",
            "versions": [
                {
                    "board": "atmega328p_arduino_nano",
                    "board_name": "ATmega328P Arduino Nano",
                    "board_url": "https://github.com/Hanqaqa/Easyduino/tree/master/Atmega328p%20Arduino%20Nano",
                    "version": "current",
                    "git_ref": "master",
                    "sparse_checkout": True,
                    "project_file_folder": "Atmega328p Arduino Nano",
                    "project_file_basename": "Easyduino_Atmega_Nano",
                    "project_file_path": "Atmega328p Arduino Nano/Easyduino_Atmega_Nano",
                },
                {
                    "board": "atmega328p_arduino_uno",
                    "board_name": "ATmega328P Arduino Uno",
                    "board_url": "https://github.com/Hanqaqa/Easyduino/tree/master/Atmega328p%20Arduino%20Uno",
                    "version": "current",
                    "git_ref": "master",
                    "sparse_checkout": True,
                    "project_file_folder": "Atmega328p Arduino Uno",
                    "project_file_basename": "Easyduino_Atmega",
                    "project_file_path": "Atmega328p Arduino Uno/Easyduino_Atmega",
                    "match_overrides": {
                        "J2": "electronic_connector_header_2_54_mm_pitch_through_hole_2_pin",
                    },
                },
                {
                    "board": "esp32",
                    "board_name": "ESP32",
                    "board_url": "https://github.com/Hanqaqa/Easyduino/tree/master/ESP32",
                    "version": "current",
                    "git_ref": "master",
                    "sparse_checkout": True,
                    "project_file_folder": "ESP32",
                    "project_file_basename": "Easyduino_ESP32",
                    "project_file_path": "ESP32/Easyduino_ESP32",
                    "match_overrides": {
                        "C5": "electronic_capacitor_3216_avx_a_tantalum_22_micro_farad_10_volt",
                        "C7": "electronic_capacitor_3216_avx_a_tantalum_22_micro_farad_10_volt",
                        "C8": "electronic_capacitor_3216_avx_a_tantalum_22_micro_farad_10_volt",
                        "D1": "electronic_diode_tvs_array_sot_143_littelfuse_sp0503bahtg",
                        "D2": "electronic_led_0402_blue",
                        "J1": "electronic_connector_usb_c_surface_mount_16_pin_shou_han_type_c_16pin_2md_073",
                        "Q1": "electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050",
                        "Q2": "electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050",
                        "SW1": "electronic_switch_tactile_surface_mount_xunpu_ts_1088_ar02016",
                        "SW2": "electronic_switch_tactile_surface_mount_xunpu_ts_1088_ar02016",
                        "U2": "electronic_ic_esp32_wroom_32e_microcontroller_wifi_bluetooth_8_mb_flash_espressif_esp32_wroom_32e_n8",
                        "U3": "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_3_3_volt_advanced_monolithic_systems_ams1117_3_3",
                    },
                    "match_blocked": {
                        "U1": "BOM C6568, upstream PDF and README identify CP2102-GMR, but the actual schematic symbol is CP2102N-Axx-xQFN28. CP2102-GMR has been added to OOMP; confirm which chip is intended before accepting a match.",
                        "U4": "ESP32-DevKitC is a combined 38-pad carrier/header footprint, not an additional DevKit board: the source photo shows two 19-pin male headers. Both headers already exist as electronic_connector_header_2_54_mm_pitch_through_hole_19_pin, but a one-footprint-to-two-parts mapping needs confirmation. Do not buy another DevKitC.",
                    },
                    "review_notes": [
                        "J1: C2765186 and the supplied USBC.pdf identify SHOU HAN TYPE-C 16PIN 2MD(073), while the footprint is named G-Switch GT-USB-7010ASV. OOMP follows the BOM/PDF identity; the original footprint remains unchanged pending land-pattern verification.",
                        "D1: C7074 is Littelfuse SP0503BAHTG. The upstream ESD_Protection.pdf is TECH PUBLIC, so OOMP uses the downloaded Littelfuse datasheet instead.",
                        "C5/C7/C8: C11366 is AVX TAJA226K010RNJ, 22uF 10V, A-case 3216-18. The upstream Kemet-I footprint name specifies a lower 1.0mm body; verify clearance for the actual 1.8mm capacitor.",
                        "SW1/SW2: C720477 is XUNPU TS-1088-AR02016, not Alps. The original Alps_SKRK footprint is retained; exact master compatibility has not been certified.",
                    ],
                },
                {
                    "board": "esp32s3",
                    "board_name": "ESP32S3",
                    "board_url": "https://github.com/Hanqaqa/Easyduino/tree/master/ESP32S3",
                    "version": "current",
                    "git_ref": "master",
                    "sparse_checkout": True,
                    "project_file_folder": "ESP32S3",
                    "project_file_basename": "Easyduino_ESP32S3",
                    "project_file_path": "ESP32S3/Easyduino_ESP32S3",
                },
                {
                    "board": "raspberry_pi_pico_2040",
                    "board_name": "Raspberry Pi Pico 2040",
                    "board_url": "https://github.com/Hanqaqa/Easyduino/tree/master/Raspberry%20Pi%20Pico%202040",
                    "version": "current",
                    "git_ref": "master",
                    "sparse_checkout": True,
                    "project_file_folder": "Raspberry Pi Pico 2040",
                    "project_file_basename": "Easyduino_RP2040",
                    "project_file_path": "Raspberry Pi Pico 2040/Easyduino_RP2040",
                },
                {
                    "board": "stm32f103_bluepill",
                    "board_name": "STM32F103 Bluepill",
                    "board_url": "https://github.com/Hanqaqa/Easyduino/tree/master/STM32F103%20Bluepill",
                    "version": "current",
                    "git_ref": "master",
                    "sparse_checkout": True,
                    "project_file_folder": "STM32F103 Bluepill",
                    "project_file_basename": "Easyduino_STM32F103",
                    "project_file_path": "STM32F103 Bluepill/Easyduino_STM32F103",
                },
            ],
        },
    ]

    def add_soldered_project(
        repo_slug,
        board_slug,
        board_name,
        project_file_folder,
        project_file_basename,
        version_folder,
        git_ref="main",
    ):
        repo_url = f"https://github.com/SolderedElectronics/{repo_slug}"
        projects.append(
            {
                "github_user": "SolderedElectronics",
                "github_repository": repo_slug,
                "github_url": repo_url,
                "repository_url": f"{repo_url}.git",
                "versions": [
                    {
                        "board": board_slug,
                        "board_name": board_name,
                        "board_url": repo_url,
                        "version": "current",
                        "git_ref": git_ref,
                        "sparse_checkout": True,
                        "project_file_folder": project_file_folder,
                        "project_file_basename": project_file_basename,
                        "project_file_path": f"{project_file_folder}/{project_file_basename}",
                    }
                ],
            }
        )

    def add_variant_family(base_repo_slug, base_board_slug, base_board_name, project_file_basename, version_folder, variants):
        for repo_suffix, board_suffix, name_suffix in variants:
            add_soldered_project(
                f"{base_repo_slug}{repo_suffix}",
                f"{base_board_slug}{board_suffix}",
                f"{base_board_name}{name_suffix}",
                f"CAD/{version_folder}",
                project_file_basename,
                version_folder,
            )

    # Soldered Electronics sensor boards.
    for mq_number, repo_slug, qwiic, easyc in [
        (2, "Butane--LPG---Smoke-sensor-MQ2-breakout-hardware-design", True, True),
        (3, "Alcohol--Ethanol-sensor-MQ3-breakout-hardware-design", True, True),
        (4, "Methane.-CNG-sensor-MQ4-breakout-hardware-design", True, True),
        (5, "Natural-gas--LPG-sensor-MQ5-breakout-hardware-design", True, True),
        (6, "LPG--Butane-sensor-MQ6-breakout-hardware-design", True, True),
        (7, "CO-sensor-MQ7-breakout-hardware-design", True, True),
        (8, "Hydrogen-sensor-MQ8-breakout-hardware-design", True, True),
        (9, "CO--flammable-gasses-sensor-MQ9-breakout-hardware-design", True, True),
        (131, "Ozone-sensor-MQ131-breakout-hardware-design", True, True),
        (135, "Air-quality-sensor-MQ135-breakout-hardware-design", True, True),
        (136, "Hydrogen-Sulfide-sensor-MQ136-breakout-hardware-design", False, True),
        (137, "Ammonia-sensor-MQ137-breakout-hardware-design", True, True),
        (138, "VOC-sensor-MQ138-breakout-hardware-design", False, False),
        (214, "Methane--Natural-gas-sensor-MQ214-breakout-hardware-design", False, True),
    ]:
        base_name = f"MQ{mq_number} Breakout"
        add_soldered_project(
            repo_slug,
            f"sensor_gas_mq{mq_number}_breakout",
            base_name,
            f"CAD/V1.1.1",
            "MQ Breakout",
            "V1.1.1",
        )
        if qwiic:
            add_soldered_project(
                repo_slug.replace("-hardware-design", "-qwiic-hardware-design"),
                f"sensor_gas_mq{mq_number}_qwiic",
                f"{base_name} qwiic",
                f"CAD/V1.1.1",
                "MQ Breakout",
                "V1.1.1",
            )
        if easyc:
            add_soldered_project(
                repo_slug.replace("-hardware-design", "-with-easyC-hardware-design"),
                f"sensor_gas_mq{mq_number}_easyc",
                f"{base_name} easyC",
                f"CAD/V1.1.1",
                "MQ Breakout",
                "V1.1.1",
            )

    add_soldered_project(
        "Benzene--Toluene--Acetone--Formaldehyde-sensor-MQ138-breakout-hardware-design",
        "sensor_gas_mq138_breakout",
        "MQ138 Breakout",
        "CAD/V1.1.1",
        "MQ Breakout",
        "V1.1.1",
    )
    add_soldered_project(
        "Benzene--Toluene--Acetone--Formaldehyde-sensor-MQ138-breakout-with-easyC-hardware-design",
        "sensor_gas_mq138_easyc",
        "MQ138 Breakout easyC",
        "CAD/V1.1.1",
        "MQ Breakout",
        "V1.1.1",
    )

    add_soldered_project(
        "Air-quality-sensor-CCS811-breakout-hardware-design",
        "sensor_air_quality_ccs811",
        "CCS811 Breakout",
        "CAD/V1.1.1",
        "CCS811_breakout",
        "V1.1.1",
    )
    add_soldered_project(
        "Pressure---temperature-sensor-BMP388-breakout-hardware-design",
        "sensor_pressure_temp_bmp388",
        "BMP388 Breakout",
        "CAD/V1.0.0",
        "Pressure & temperature sensor BMP388 breakout",
        "V1.0.0",
    )
    add_soldered_project(
        "Thermocouple-sensor-AD8495-breakout-hardware-design",
        "sensor_thermocouple_ad8495",
        "AD8495 Breakout",
        "CAD/V1.0.0",
        "K-pair-adapter",
        "V1.0.0",
    )
    add_soldered_project(
        "Capacitive-soil-sensor-hardware-design",
        "sensor_capacitive_soil",
        "Capacitive Soil Sensor",
        "CAD/V2.0.0",
        "Capacitive soil sensor",
        "V2.0.0",
    )
    add_soldered_project(
        "Digital-light---proximity-sensor-LTR-507ALS-breakout-hardware-design",
        "sensor_light_ltr507als",
        "LTR-507ALS Breakout",
        "CAD/V1.1.1",
        "Light_sensor_LTR-507ALS-01",
        "V1.1.1",
    )
    add_soldered_project(
        "Color-and-gesture-sensor-APDS-9960-breakout-hardware-design",
        "sensor_color_gesture_apds9960",
        "APDS-9960 Breakout",
        "CAD/V1.1.1",
        "APDS9960_breakout",
        "V1.1.1",
    )
    add_soldered_project(
        "Color---gesture-sensor-APDS-9960-breakout-hardware-design",
        "sensor_color_gesture_apds9960",
        "APDS-9960 Breakout",
        "CAD/V1.1.1",
        "APDS9960_breakout",
        "V1.1.1",
    )

    add_soldered_project(
        "Simple-light-sensor-board-hardware-design",
        "sensor_light_simple",
        "Simple Light Sensor",
        "CAD/V1.1.1",
        "Simple_sensor",
        "V1.1.1",
    )
    add_soldered_project(
        "Simple-light-sensor-board-with-easyC-hardware-design",
        "sensor_light_simple_easyc",
        "Simple Light Sensor easyC",
        "CAD/V1.1.2",
        "Simple_sensor_easyC",
        "V1.1.2",
    )
    add_soldered_project(
        "Simple-light-sensor-board-qwiic-hardware-design",
        "sensor_light_simple_qwiic",
        "Simple Light Sensor qwiic",
        "CAD/V1.1.2",
        "Simple_sensor_easyC",
        "V1.1.2",
    )
    add_soldered_project(
        "Simple-fire-sensor-board-hardware-design",
        "sensor_fire_simple",
        "Simple Fire Sensor",
        "CAD/V1.1.1",
        "Simple_sensor",
        "V1.1.1",
    )
    add_soldered_project(
        "Simple-fire-sensor-board-with-easyC-hardware-design",
        "sensor_fire_simple_easyc",
        "Simple Fire Sensor easyC",
        "CAD/V1.1.2",
        "Simple_sensor_easyC",
        "V1.1.2",
    )
    add_soldered_project(
        "Simple-fire-sensor-board-qwiic-hardware-design",
        "sensor_fire_simple_qwiic",
        "Simple Fire Sensor qwiic",
        "CAD/V1.1.2",
        "Simple_sensor_easyC",
        "V1.1.2",
    )
    add_variant_family(
        "PIR-Movement-sensor-board",
        "sensor_pir_movement",
        "PIR Movement Sensor",
        "PIR_movement_sensor",
        "V1.1.1",
        [("-hardware-design", "", ""), ("-with-easyC-hardware-design", "_easyc", " easyC"), ("-qwiic-hardware-design", "_qwiic", " qwiic")],
    )
    add_variant_family(
        "Obstacle-sensor",
        "sensor_obstacle",
        "Obstacle Sensor",
        "Obstacle_sensor",
        "V1.1.1",
        [("-TCRT5000-breakout-hardware-design", "_tcrt5000", " TCRT5000"), ("-with-easyC-hardware-design", "_easyc", " easyC"), ("-qwiic-hardware-design", "_qwiic", " qwiic")],
    )
    add_variant_family(
        "Ultrasonic-sensor",
        "sensor_ultrasonic",
        "Ultrasonic Sensor",
        "Ultrasonic_sensor",
        "V1.1.1",
        [("-with-easyC-hardware-design", "_easyc", " easyC"), ("-qwiic-hardware-design", "_qwiic", " qwiic")],
    )
    add_variant_family(
        "Hall-effect-sensor-breakout-with-analog-output",
        "sensor_hall_analog",
        "Hall Effect Analog Output",
        "Hall_effect_sensor_analog",
        "V1.1.1",
        [("-hardware-design", "", ""), ("---easyC-hardware-design", "_easyc", " easyC"), ("---qwiic-hardware-design", "_qwiic", " qwiic")],
    )
    add_variant_family(
        "Hall-effect-sensor-breakout-with-digital-output",
        "sensor_hall_digital",
        "Hall Effect Digital Output",
        "Hall_effect_sensor_digital",
        "V1.1.1",
        [("-hardware-design", "", ""), ("---easyC-hardware-design", "_easyc", " easyC"), ("---qwiic-hardware-design", "_qwiic", " qwiic")],
    )

    add_soldered_project(
        "Voltage---current-sensor-INA219-breakout-hardware-design",
        "sensor_power_ina219",
        "INA219 Breakout",
        "CAD/V1.0.0",
        "INA219_breakout",
        "V1.0.0",
    )
    add_soldered_project(
        "Current-sensor-30A-ACS712-breakout-hardware-design",
        "sensor_current_acs712_30a",
        "ACS712 30A",
        "CAD/V2.0.0",
        "ACS712_breakout",
        "V2.0.0",
    )
    add_soldered_project(
        "Load-cell-ampfilier-HX711-board-hardware-design",
        "sensor_load_cell_hx711",
        "HX711 Load Cell",
        "CAD/V1.1.1",
        "HX711",
        "V1.1.1",
    )
    add_soldered_project(
        "Load-cell-ampfilier-HX711-board-with-easy-C-hardware-design",
        "sensor_load_cell_hx711_easyc",
        "HX711 Load Cell easyC",
        "CAD/V1.1.1",
        "HX711_breakout_easyC",
        "V1.1.1",
    )

    add_soldered_project(
        "Accelerometer---Gyroscope---Magnetometer-LSM9DS1TR-breakout-hardware-design",
        "sensor_imu_lsm9ds1tr",
        "LSM9DS1TR IMU",
        "CAD/V1.2.2",
        "Accelerometer_Gyroscope_Magnetometer LSM9DS1TR breakout",
        "V1.2.2",
    )
    add_soldered_project(
        "GNSS-GPS-L86-M33-breakout-hardware-design",
        "sensor_gnss_l86m33",
        "L86-M33 GNSS",
        "CAD/V1.2.0",
        "GNSS_breakout_L86-M33",
        "V1.2.0",
    )
    add_soldered_project(
        "GNSS-GPS-L86-M33-breakout-with-easyC-hardware-design",
        "sensor_gnss_l86m33_easyc",
        "L86-M33 GNSS easyC",
        "CAD/V1.1.0",
        "GNSS GPS L86-M33 breakout with easyC",
        "V1.1.0",
    )

    add_soldered_project(
        "PMS7003-sensor-adapter-hardware-design",
        "sensor_pms7003_adapter",
        "PMS7003 Adapter",
        "CAD/V1.1.1",
        "PMS7003_sensor_adapter",
        "V1.1.1",
    )
    add_soldered_project(
        "Slider-potentiometer-breakout-hardware-design",
        "input_slider_potentiometer",
        "Slider Potentiometer",
        "CAD/V1.1.1",
        "Slider_potentiometer",
        "V1.1.1",
    )
    add_soldered_project(
        "Slider-potentiometer-breakout-with-easyC-hardware-design",
        "input_slider_potentiometer_easyc",
        "Slider Potentiometer easyC",
        "CAD/V1.1.1",
        "Slider_potentiometer",
        "V1.1.1",
    )
    add_soldered_project(
        "Rotary-encoder-board-with-easyC-hardware-design",
        "input_rotary_encoder_easyc",
        "Rotary Encoder easyC",
        "CAD/V1.1.0",
        "Rotary encoder with easyC",
        "V1.1.0",
    )

    sparkfun_projects = [
        {
            "github_repository": "SparkFun_Particulate_Matter_Sensor_Breakout_BMV080",
            "board": "particulate_matter_bmv080",
            "board_name": "Particulate Matter Sensor BMV080",
            "project_file_basename": "SparkFun_BMV080",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_BMV080",
            "repo_url": "https://github.com/sparkfun/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080",
            "versions": [
                {"version": "current", "git_ref": "main"},
                {"version": "v1.0.0", "git_ref": "v1.0.0"},
            ],
        },
        {
            "github_repository": "SparkFun_Capacitive_Soil_Moisture_Sensor_CY8CMBR3102",
            "board": "capacitive_soil_moisture_cy8cmbr3102",
            "board_name": "Capacitive Soil Moisture Sensor CY8CMBR3102",
            "project_file_basename": "SparkFun_Capacitive_Soil_Moisture_Sensor",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_Capacitive_Soil_Moisture_Sensor",
            "repo_url": "https://github.com/sparkfun/SparkFun_Capacitive_Soil_Moisture_Sensor_CY8CMBR3102",
            "versions": [
                {"version": "current", "git_ref": "main"},
                {"version": "v1.0.0", "git_ref": "v1.0.0"},
            ],
        },
        {
            "github_repository": "SparkFun_Qwiic_Current_Sensor_INA2XX",
            "board": "qwiic_current_sensor_ina2xx",
            "board_name": "Qwiic Current Sensor INA2XX",
            "project_file_basename": "SparkFun_Qwiic_Current_Sensor_INA2XX",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_Qwiic_Current_Sensor_INA2XX",
            "repo_url": "https://github.com/sparkfun/SparkFun_Qwiic_Current_Sensor_INA2XX",
            "versions": [
                {"version": "current", "git_ref": "main"},
                {"version": "v1.0.0", "git_ref": "v1.0.0"},
            ],
        },
        {
            "github_repository": "SparkFun_Qwiic_Current_Sensor_ADE7953",
            "board": "qwiic_current_sensor_ade7953",
            "board_name": "Qwiic Current Sensor ADE7953",
            "project_file_basename": "SparkFun_Qwiic_Current_Sensor_ADE7953",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_Qwiic_Current_Sensor_ADE7953",
            "repo_url": "https://github.com/sparkfun/SparkFun_Qwiic_Current_Sensor_ADE7953",
            "versions": [
                {"version": "current", "git_ref": "main"},
                {"version": "v1.0.0", "git_ref": "v1.0.0"},
            ],
        },
        {
            "github_repository": "SparkFun_Qwiic_ADC_ADS1219",
            "board": "qwiic_adc_ads1219",
            "board_name": "Qwiic ADC ADS1219",
            "project_file_basename": "Qwiic_ADC_ADS1219",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/Qwiic_ADC_ADS1219",
            "repo_url": "https://github.com/sparkfun/SparkFun_Qwiic_ADC_ADS1219",
            "versions": [
                {"version": "current", "git_ref": "main"},
                {"version": "v1.0.0", "git_ref": "v1.0.0"},
            ],
        },
        {
            "github_repository": "SparkFun_Qwiic_Navigation_Switch",
            "board": "qwiic_navigation_switch",
            "board_name": "Qwiic Navigation Switch",
            "project_file_basename": "SparkFun_Qwiic_Navigation",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_Qwiic_Navigation",
            "repo_url": "https://github.com/sparkfun/SparkFun_Qwiic_Navigation_Switch",
            "versions": [
                {"version": "current", "git_ref": "main"},
            ],
        },
        {
            "github_repository": "SparkFun_Qwiic_Directional_Pad",
            "board": "qwiic_directional_pad",
            "board_name": "Qwiic Directional Pad",
            "project_file_basename": "SparkFun_Qwiic_Directional_Pad",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_Qwiic_Directional_Pad",
            "repo_url": "https://github.com/sparkfun/SparkFun_Qwiic_Directional_Pad",
            "versions": [
                {"version": "current", "git_ref": "main"},
            ],
        },
        {
            "github_repository": "SparkFun_Roller_Encoder_Breakout",
            "board": "roller_encoder_breakout",
            "board_name": "Roller Encoder Breakout",
            "project_file_basename": "SparkFun_Roller_Encoder_Breakout",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_Roller_Encoder_Breakout",
            "repo_url": "https://github.com/sparkfun/SparkFun_Roller_Encoder_Breakout",
            "versions": [
                {"version": "current", "git_ref": "main"},
            ],
        },
        {
            "github_repository": "SparkFun_Audio_Player_Breakout_MY1690X-16S",
            "board": "audio_player_breakout_my1690x_16s",
            "board_name": "Audio Player Breakout MY1690X-16S",
            "project_file_basename": "SparkFun_Audio_Player_Breakout_MY1690X-16S",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_Audio_Player_Breakout_MY1690X-16S",
            "repo_url": "https://github.com/sparkfun/SparkFun_Audio_Player_Breakout_MY1690X-16S",
            "versions": [
                {"version": "current", "git_ref": "main"},
            ],
        },
        {
            "github_repository": "SparkFun_Qwiic_GNSS_SAM-M8Q",
            "board": "qwiic_gnss_sam_m8q",
            "board_name": "Qwiic GNSS SAM-M8Q",
            "project_file_basename": "SparkFun_Qwiic_GNSS_SAM-M8Q",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_Qwiic_GNSS_SAM-M8Q",
            "repo_url": "https://github.com/sparkfun/SparkFun_Qwiic_GNSS_SAM-M8Q",
            "versions": [
                {"version": "current", "git_ref": "main"},
                {"version": "v0.1", "git_ref": "v01"},
            ],
        },
        {
            "github_repository": "SparkFun_GNSS_DAN-F10N",
            "board": "gnss_dan_f10n",
            "board_name": "GNSS DAN-F10N",
            "project_file_basename": "SparkFun_GNSS_DAN-F10N",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_GNSS_DAN-F10N",
            "repo_url": "https://github.com/sparkfun/SparkFun_GNSS_DAN-F10N",
            "versions": [
                {"version": "current", "git_ref": "main"},
                {"version": "v1.0", "git_ref": "v10"},
            ],
        },
        {
            "github_repository": "SparkFun_u-blox_NEO-F10N",
            "board": "ublox_neo_f10n",
            "board_name": "u-blox NEO-F10N",
            "project_file_basename": "SparkFun_NEO-F10N",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_NEO-F10N",
            "repo_url": "https://github.com/sparkfun/SparkFun_u-blox_NEO-F10N",
            "versions": [
                {"version": "current", "git_ref": "main"},
            ],
        },
        {
            "github_repository": "SparkFun_GNSS_Flex_Breakout",
            "board": "gnss_flex_breakout",
            "board_name": "GNSS Flex Breakout",
            "project_file_basename": "SparkFun_GNSS_Flex_Breakout",
            "project_file_folder": "Hardware",
            "project_file_path": "Hardware/SparkFun_GNSS_Flex_Breakout",
            "repo_url": "https://github.com/sparkfun/SparkFun_GNSS_Flex_Breakout",
            "versions": [
                {"version": "current", "git_ref": "main"},
                {"version": "v1.0", "git_ref": "v10"},
                {"version": "v1.1", "git_ref": "v11"},
            ],
        },
    ]

    for sparkfun_project in sparkfun_projects:
        active_version = _select_active_version(sparkfun_project.get("versions", [{"version": "current", "git_ref": "main"}]))
        projects.append(
            {
                "github_user": "sparkfun",
                "github_repository": sparkfun_project["github_repository"],
                "github_url": sparkfun_project["repo_url"],
                "repository_url": f"{sparkfun_project['repo_url']}.git",
                "versions": [
                    {
                        "board": sparkfun_project["board"],
                        "board_name": sparkfun_project["board_name"],
                        "board_url": sparkfun_project["repo_url"],
                        "version": active_version.get("version", "current"),
                        "git_ref": active_version.get("git_ref", "main"),
                        "sparse_checkout": True,
                        "project_file_folder": sparkfun_project["project_file_folder"],
                        "project_file_basename": sparkfun_project["project_file_basename"],
                        "project_file_path": sparkfun_project["project_file_path"],
                    }
                ],
            }
        )

    project_file_extensions = [
        ".kicad_pcb",
        ".kicad_sch",
        ".kicad_pro",
    ]

    for project in projects:
        versions = project.get("versions", [])
        versions = _collapse_historial_versions(versions)

        for version_details in versions:
            version_details = dict(version_details)
            option = {}
            option["taxonomy_1"] = "oomp"
            option["taxonomy_2"] = "project"
            option["taxonomy_3"] = "github"
            option["taxonomy_4"] = _normalize_project_slug(project["github_user"])
            option["taxonomy_5"] = _normalize_project_slug(project["github_repository"])
            # Optional board level distinguishes several boards in one repo.
            # Omit it for single-board projects so existing IDs stay unchanged.
            board = _normalize_project_slug(version_details.get("board", ""))
            if board:
                option["taxonomy_6"] = board
                option["taxonomy_7"] = _normalize_project_slug(version_details.get("version", "current"))
                option["project_board"] = board
                option["project_board_name"] = version_details.get("board_name", board.replace("_", " "))
                option["project_board_url"] = version_details.get("board_url", "")
            else:
                option["taxonomy_6"] = _normalize_project_slug(version_details.get("version", "current"))

            option["project_github_user"] = _normalize_project_slug(project["github_user"])
            option["project_github_repository"] = project["github_repository"]
            option["project_github_url"] = project.get(
                "github_url",
                f"https://github.com/{project['github_user']}/{project['github_repository']}",
            )
            option["project_git_url"] = project["repository_url"]
            option["project_git_ref"] = version_details.get("git_ref", "main")
            option["project_sparse_checkout"] = bool(version_details.get("sparse_checkout", False))
            option["project_version"] = version_details.get("version", "current")
            option["project_file_folder"] = version_details.get("project_file_folder", "")
            option["project_file_basename"] = version_details.get("project_file_basename", "")
            option["project_file_path"] = version_details.get("project_file_path", "")
            option["project_file_path_original"] = version_details.get("project_file_path_original", "")
            option["project_file_extensions"] = list(project_file_extensions)
            option["project_match_overrides"] = dict(version_details.get("match_overrides", {}))
            option["project_match_blocked"] = dict(version_details.get("match_blocked", {}))
            option["project_review_notes"] = list(version_details.get("review_notes", []))
            options.append(option)


if __name__ == "__main__":
    main()
