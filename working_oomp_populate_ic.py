def main(**kwargs):
    options = kwargs.get("options", [])

    # Soldered/e-radionica breakout ICs identified by exact MPN in the
    # schematics (added with the unmatched-components batch).
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_14",
        "taxonomy_4": "microcontroller", "taxonomy_5": "8_bit_avr",
        "taxonomy_14": "microchip", "taxonomy_15": "attiny404_ssnr",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23_5",
        "taxonomy_4": "power_management", "taxonomy_5": "boost_converter",
        "taxonomy_14": "texas_instruments", "taxonomy_15": "tps613222a",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_8",
        "taxonomy_4": "logic", "taxonomy_5": "comparator",
        "taxonomy_15": "lm393",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_8",
        "taxonomy_4": "amplifier", "taxonomy_5": "operational_amplifier_dual_jfet_input",
        "taxonomy_14": "stmicroelectronics", "taxonomy_15": "tl072cdt",
        "name_short": "TL072CDT Dual JFET Input Op Amp",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_8",
        "taxonomy_4": "amplifier", "taxonomy_5": "operational_amplifier_dual_low_noise",
        "taxonomy_14": "texas_instruments", "taxonomy_15": "ne5532dr",
        "name_short": "NE5532DR Dual Low-Noise Op Amp",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_8",
        "taxonomy_4": "amplifier", "taxonomy_5": "operational_amplifier_dual",
        "taxonomy_14": "onsemi", "taxonomy_15": "lm358dr2g",
        "name_short": "LM358DR2G Dual Op Amp",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_14",
        "taxonomy_4": "amplifier", "taxonomy_5": "operational_amplifier_quad",
        "taxonomy_14": "stmicroelectronics", "taxonomy_15": "lm324dt",
        "name_short": "LM324DT Quad Op Amp",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_8",
        "taxonomy_4": "amplifier", "taxonomy_5": "operational_amplifier_precision",
        "taxonomy_14": "texas_instruments", "taxonomy_15": "op07cdr",
        "name_short": "OP07CDR Precision Op Amp",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23_5",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_3_3_volt",
        "taxonomy_14": "richtek", "taxonomy_15": "rt9080_33",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23_5",
        "taxonomy_4": "amplifier", "taxonomy_5": "operational_amplifier",
        "taxonomy_14": "texas_instruments", "taxonomy_15": "opa344",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23_5",
        "taxonomy_4": "sensor", "taxonomy_5": "hall_effect",
        "taxonomy_14": "silicon_labs", "taxonomy_15": "si7211_b_00_iv",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23",
        "taxonomy_4": "sensor", "taxonomy_5": "hall_effect",
        "taxonomy_14": "silicon_labs", "taxonomy_15": "si7201_b_06_iv",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sop_16",
        "taxonomy_4": "converter", "taxonomy_5": "load_cell_amplifier",
        "taxonomy_14": "avia_semiconductor", "taxonomy_15": "hx711",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "esp32_wroom_32e", "taxonomy_4": "microcontroller",
        "taxonomy_5": "wifi_bluetooth_8_mb_flash", "taxonomy_14": "espressif",
        "taxonomy_15": "esp32_wroom_32e_n8", "name_short": "ESP32-WROOM-32E-N8 8MB",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_223_3",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_3_3_volt",
        "taxonomy_14": "advanced_monolithic_systems", "taxonomy_15": "ams1117_3_3",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_223_3",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_5_volt",
        "taxonomy_14": "advanced_monolithic_systems", "taxonomy_15": "ams1117_5",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_3_3_volt",
        "taxonomy_14": "torex", "taxonomy_15": "xc6206p332mr",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_5_volt",
        "taxonomy_14": "torex", "taxonomy_15": "xc6206p502mr",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "tqfp_32_7_mm_x_7_mm",
        "taxonomy_4": "microcontroller", "taxonomy_5": "8_bit_avr",
        "taxonomy_14": "microchip", "taxonomy_15": "atmega328p_au",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sop_16",
        "taxonomy_4": "converter", "taxonomy_5": "usb_to_serial_converter",
        "taxonomy_14": "wch", "taxonomy_15": "ch340c",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "qfn_28_5_mm_x_5_mm",
        "taxonomy_4": "converter", "taxonomy_5": "usb_to_serial_converter",
        "taxonomy_14": "silicon_labs", "taxonomy_15": "cp2102n_a01_gqfn28r",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "esp32_s3_wroom_1",
        "taxonomy_4": "microcontroller", "taxonomy_5": "wifi_bluetooth_8_mb_flash",
        "taxonomy_14": "espressif", "taxonomy_15": "esp32_s3_wroom_1_n8",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "qfn_28_5_mm_x_5_mm",
        "taxonomy_4": "converter", "taxonomy_5": "usb_to_serial_converter",
        "taxonomy_14": "silicon_labs", "taxonomy_15": "cp2102_gmr",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_8",
        "taxonomy_4": "interface", "taxonomy_5": "rs_485_transceiver",
        "taxonomy_14": "maxlinear", "taxonomy_15": "sp485een_l_tr",
        "name_short": "SP485EEN-L/TR RS-485 Transceiver",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_8",
        "taxonomy_4": "interface", "taxonomy_5": "rs_485_transceiver",
        "taxonomy_14": "maxlinear", "taxonomy_15": "sp3485en_l_tr",
        "name_short": "SP3485EN-L/TR RS-485 Transceiver",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "tssop_16",
        "taxonomy_4": "interface", "taxonomy_5": "rs_232_transceiver",
        "taxonomy_14": "maxlinear", "taxonomy_15": "sp3232eey_l_tr",
        "name_short": "SP3232EEY-L/TR RS-232 Transceiver",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_14",
        "taxonomy_4": "logic", "taxonomy_5": "hex_schmitt_trigger_inverter",
        "taxonomy_14": "nexperia", "taxonomy_15": "74hc14d_653",
        "name_short": "74HC14D,653 Hex Schmitt Trigger Inverter",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_16",
        "taxonomy_4": "logic", "taxonomy_5": "serial_in_parallel_out_shift_register",
        "taxonomy_14": "nexperia", "taxonomy_15": "74hc595d_118",
        "name_short": "74HC595D,118 8-Bit Shift Register",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "smd_4p",
        "taxonomy_4": "optocoupler", "taxonomy_5": "phototransistor_output",
        "taxonomy_14": "lite_on", "taxonomy_15": "ltv_817s_ta1_c",
        "name_short": "LTV-817S-TA1-C Optocoupler",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sop_4_175mil",
        "taxonomy_4": "optocoupler", "taxonomy_5": "phototransistor_output",
        "taxonomy_14": "lite_on", "taxonomy_15": "ltv_217_b_g",
        "name_short": "LTV-217-B-G Optocoupler",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_8_ep",
        "taxonomy_4": "power_management", "taxonomy_5": "buck_converter",
        "taxonomy_14": "texas_instruments", "taxonomy_15": "tps5430ddar",
        "name_short": "TPS5430DDAR Buck Converter",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_16",
        "taxonomy_4": "driver", "taxonomy_5": "darlington_array",
        "taxonomy_14": "texas_instruments", "taxonomy_15": "uln2003adr",
        "name_short": "ULN2003ADR Darlington Array",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "soic_8",
        "taxonomy_4": "power_management", "taxonomy_5": "buck_converter",
        "taxonomy_14": "xlsemi", "taxonomy_15": "xl1509_5_0e1",
        "name_short": "XL1509-5.0E1 Buck Converter",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23",
        "taxonomy_4": "power_management", "taxonomy_5": "voltage_reference",
        "taxonomy_14": "jiangsu_changjing_electronics_technology_co_ltd", "taxonomy_15": "cj431",
        "name_short": "CJ431 Voltage Reference",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_3_3_volt",
        "taxonomy_14": "torex_semicon", "taxonomy_15": "xc6206p332mr_g",
        "name_short": "XC6206P332MR-G LDO 3.3V",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_89_3",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_3_3_volt",
        "taxonomy_14": "holtek_semicon", "taxonomy_15": "ht7533_1",
        "name_short": "HT7533-1 LDO 3.3V",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "to_252_2_dpak",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_5_volt",
        "taxonomy_14": "stmicroelectronics", "taxonomy_15": "l78m05abdt_tr",
        "name_short": "L78M05ABDT-TR 5V Regulator",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_89_3",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_5_volt",
        "taxonomy_14": "utc_unisonic_tech", "taxonomy_15": "78l05g_ab3_r",
        "name_short": "78L05G-AB3-R 5V Regulator",
    })

    packages = ["qfn_16_3_mm_x_3_mm"]
    ic_types = ["converter"]
    functions = ["usb_to_serial_converter"]
    manufacturers = ["wch"]
    part_numbers = ["ch343p"]

    for package in packages:
        for ic_type in ic_types:
            for function in functions:
                for manufacturer in manufacturers:
                    for part_number in part_numbers:
                        option = {}
                        option["taxonomy_2"] = "ic"
                        option["taxonomy_3"] = package
                        option["taxonomy_4"] = ic_type
                        option["taxonomy_5"] = function
                        option["taxonomy_14"] = manufacturer
                        option["taxonomy_15"] = part_number
                        options.append(option)

    # Additional unmatched-project IC identities.  This is intentionally the
    # lightweight population layer only; datasheet, pinout, dimensions, and
    # exact matching records are added in the subsequent ledger pass.
    unmatched_ics = [
        ["module_esp_12s", "microcontroller", "wifi_bluetooth", "espressif", "esp_12s"],
        ["qfn_32_5_mm_x_5_mm", "microcontroller", "8_bit_avr", "microchip", "atmega328p_mu"],
        ["sot_23_3", "power_management", "linear_voltage_regulator_3_3_volt", "microchip", "mcp1700t_3302e_tt"],
        ["tssop_14", "converter", "thermocouple_to_digital_converter", "maxim", "max31856"],
        ["qfn_32_5_mm_x_5_mm", "trusted_platform_module", "trusted_platform_module", "infineon", "slb9670"],
        ["qfn_32_5_mm_x_5_mm", "trusted_platform_module", "trusted_platform_module", "infineon", "slb9665"],
        ["sop_16", "converter", "usb_to_serial_converter", "wch", "ch343g"],
        ["sot_223_4", "power_management", "linear_voltage_regulator_3_3_volt", "st", "ld1117_3_3"],
        ["qfn_33_5_mm_x_5_mm", "microcontroller", "wifi_bluetooth", "espressif", "esp8285h16"],
        ["lqfp_48", "microcontroller", "stm32", "st", "stm32f103c8tx"],
        ["uson_8", "memory", "spi_nor_flash", "winbond", "w25q16jvuxiq"],
        ["sot_23_5", "power_management", "linear_voltage_regulator", "", "se5218"],
        ["sot_23_5", "power_management", "linear_voltage_regulator", "", "se5218alg"],
        ["soic_8", "timer", "555_timer", "texas_instruments", "tlc555cd"],
        ["soic_8", "timer", "555_timer", "texas_instruments", "ne555dr"],
        ["msop_8", "amplifier", "operational_amplifier", "sg_micro", "sgm358yms_tr"],
        ["soic_14", "microcontroller", "8_bit_avr", "microchip", "attiny1604_ssnr"],
        ["soic_8", "sensor", "hall_effect_current_sensor", "allegro", "acs712"],
        ["soic_8", "capacitive_touch_controller", "controller", "infineon", "cy8cmbr3102"],
        ["qfn_24", "converter", "usb_to_serial_converter", "wch", "ch342f"],
        ["qfn_14", "logic", "analog_switch", "nexperia", "74hc4066bq"],
        ["dfn_8", "power_management", "linear_voltage_regulator", "diodes", "ap7361c_3_3v"],
        ["tssop_16", "converter", "analog_to_digital_converter", "texas_instruments", "ads1219ipw"],
        ["qfn_28", "power_meter", "energy_metering", "analog_devices", "ade7953acpz"],
        ["vssop_10", "power_monitor", "current_monitor", "texas_instruments", "ina228"],
        ["sot_23_8", "power_monitor", "current_monitor", "texas_instruments", "ina219"],
        ["tssop_16", "logic", "io_expander", "texas_instruments", "pca9554pw"],
        ["msop_10", "converter", "usb_to_serial_converter", "wch", "ch340e"],
        ["sot_23_5", "power_management", "linear_voltage_regulator", "diodes", "ap2112k_3_3"],
        ["sot_23_3", "power_management", "shunt_regulator", "texas_instruments", "tl431acdbz"],
        ["msop_8", "amplifier", "thermocouple_amplifier", "texas_instruments", "ad8495armz"],
        ["so_16", "audio", "audio_player", "my_semi", "my1690x_16s"],
    ]
    for package, ic_type, function, manufacturer, part_number in unmatched_ics:
        option = {
            "taxonomy_2": "ic",
            "taxonomy_3": package,
            "taxonomy_4": ic_type,
            "taxonomy_5": function,
            "taxonomy_15": part_number,
            "name_short": part_number.replace("_", " ").upper(),
        }
        if manufacturer:
            option["taxonomy_14"] = manufacturer
        options.append(option)

    # Exact Bus Pirate 5 devices.  Keep each row independent so package,
    # function, manufacturer, or suffix changes are easy to edit later.
    bus_pirate_ics = [
        ["tssop_16", "logic", "serial_in_parallel_out_shift_register", "wuxi_i_core_elec", "aip74hc595ta16_tr"],
        ["tssop_20", "logic", "octal_bus_transceiver", "wuxi_i_core_elec", "aip74hct245ta20_tr"],
        ["sot_363_6", "logic", "single_bit_dual_supply_transceiver", "wuxi_i_core_elec", "aip74lvc1t45gc363_tr"],
        ["sot_23_5", "amplifier", "operational_single_rail_to_rail_input_output", "gainsil", "lmv321_tr"],
        ["sot_23_5", "amplifier", "operational_single_precision_rail_to_rail_input_output", "gainsil", "gs321a_tr"],
        ["sot_23_5", "comparator", "single_open_collector", "texas_instruments", "lmv331idbvr"],
        ["tssop_14", "amplifier", "operational_quad_rail_to_rail_output", "texas_instruments", "lmv324ipwr"],
        ["sot_23_5", "power_management", "linear_voltage_regulator_3_3_volt", "diodes", "ap2127k_3_3trg1"],
        ["sot_89_3", "power_management", "linear_voltage_regulator_3_3_volt", "microne", "me6211a33pg_n"],
        ["sop_8_5_28_mm_x_5_23_mm", "memory", "spi_nor_flash_128_mbit", "winbond", "w25q128jvsiq"],
        ["updfn_8", "memory", "spi_nand_flash_1_gbit", "micron", "mt29f1g01abafdwb"],
        ["qfn_56_7_mm_x_7_mm", "microcontroller", "dual_core_arm_cortex_m0_plus", "raspberry_pi", "rp2040"],
        ["tssop_24", "logic", "16_channel_analog_multiplexer", "nexperia", "74hct4067pw118"],
    ]
    for bus_pirate_ic in bus_pirate_ics:
        option = {}
        option["taxonomy_2"] = "ic"
        option["taxonomy_3"] = bus_pirate_ic[0]
        option["taxonomy_4"] = bus_pirate_ic[1]
        option["taxonomy_5"] = bus_pirate_ic[2]
        option["taxonomy_14"] = bus_pirate_ic[3]
        option["taxonomy_15"] = bus_pirate_ic[4]
        options.append(option)

    packages = ["sot_23_6"]
    ic_types = ["logic"]
    functions = ["configurable_multi_function_gate"]
    manufacturers = ["texas_instruments"]
    part_numbers = ["sn74lvc1g57dbvr"]

    for package in packages:
        for ic_type in ic_types:
            for function in functions:
                for manufacturer in manufacturers:
                    for part_number in part_numbers:
                        option = {}
                        option["taxonomy_2"] = "ic"
                        option["taxonomy_3"] = package
                        option["taxonomy_4"] = ic_type
                        option["taxonomy_5"] = function
                        option["taxonomy_14"] = manufacturer
                        option["taxonomy_15"] = part_number
                        options.append(option)

    packages = ["sop_16"]
    ic_types = ["controller"]
    functions = ["usb_hub_controller_4_port"]
    manufacturers = ["corechips"]
    part_numbers = ["sl21a"]

    for package in packages:
        for ic_type in ic_types:
            for function in functions:
                for manufacturer in manufacturers:
                    for part_number in part_numbers:
                        option = {}
                        option["taxonomy_2"] = "ic"
                        option["taxonomy_3"] = package
                        option["taxonomy_4"] = ic_type
                        option["taxonomy_5"] = function
                        option["taxonomy_14"] = manufacturer
                        option["taxonomy_15"] = part_number
                        options.append(option)

    packages = ["tsot_23_5"]
    ic_types = ["power_management"]
    functions = ["high_side_power_switch_with_flag"]
    manufacturers = ["richtek"]
    part_numbers = ["rt9742cgj5"]

    for package in packages:
        for ic_type in ic_types:
            for function in functions:
                for manufacturer in manufacturers:
                    for part_number in part_numbers:
                        option = {}
                        option["taxonomy_2"] = "ic"
                        option["taxonomy_3"] = package
                        option["taxonomy_4"] = ic_type
                        option["taxonomy_5"] = function
                        option["taxonomy_14"] = manufacturer
                        option["taxonomy_15"] = part_number
                        options.append(option)


if __name__ == "__main__":
    main()
