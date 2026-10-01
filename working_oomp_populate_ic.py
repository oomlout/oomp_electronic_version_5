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
        "taxonomy_2": "ic", "taxonomy_3": "soic_8",
        "taxonomy_4": "amplifier", "taxonomy_5": "operational_amplifier_dual",
        "taxonomy_14": "texas_instruments", "taxonomy_15": "lm358dr",
        "name_short": "LM358DR Dual Op Amp",
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
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_3_3_volt",
        "taxonomy_14": "shanghai_belling", "taxonomy_15": "bl1117_33cx",
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
        "taxonomy_2": "ic", "taxonomy_3": "soic_16",
        "taxonomy_4": "driver", "taxonomy_5": "darlington_array",
        "taxonomy_14": "toshiba", "taxonomy_15": "uln2003afwg",
        "name_short": "ULN2003AFWG Darlington Array",
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
        "taxonomy_2": "ic", "taxonomy_3": "to_92_3",
        "taxonomy_4": "power_management", "taxonomy_5": "voltage_reference",
        "taxonomy_14": "jiangsu_changjing_electronics_technology_co_ltd", "taxonomy_15": "cj431_ta",
        "name_short": "CJ431-TA Voltage Reference (TO-92)",
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
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_89_3",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_5_volt",
        "taxonomy_14": "jiangsu_changjing_electronics_technology_co_ltd", "taxonomy_15": "cj78l05",
        "name_short": "CJ78L05 5V Regulator",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "to_220",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_15_volt",
        "taxonomy_14": "stmicroelectronics", "taxonomy_15": "l7815cv_dg",
        "name_short": "L7815CV-DG 15V Regulator",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "to_220",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_negative_15_volt",
        "taxonomy_14": "stmicroelectronics", "taxonomy_15": "l7915cv_dg",
        "name_short": "L7915CV-DG -15V Regulator",
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
        # TI 74HC through-hole DIP logic from the JLC house-parts queue
        # (first DIP-body logic rows in this list).
        ["dip_14", "logic", "hex_inverter", "texas_instruments", "sn74hc04n"],
        ["dip_14", "logic", "quad_2_input_nand_gate", "texas_instruments", "sn74hc00n"],
        ["dip_14", "logic", "quad_2_input_nor_gate", "texas_instruments", "sn74hc02n"],
        ["dip_14", "logic", "quad_2_input_and_gate", "texas_instruments", "sn74hc08n"],
        ["dip_14", "logic", "quad_2_input_or_gate", "texas_instruments", "sn74hc32n"],
        ["dip_14", "logic", "quad_2_input_xor_gate", "texas_instruments", "sn74hc86n"],
        ["dip_14", "logic", "triple_3_input_nand_gate", "texas_instruments", "sn74hc10n"],
        ["dip_14", "logic", "quad_bus_buffer_tri_state", "texas_instruments", "sn74hc125n"],
        ["dip_16", "logic", "synchronous_4_bit_binary_counter", "texas_instruments", "sn74hc163n"],
        ["dip_16", "logic", "quad_d_type_flip_flop", "texas_instruments", "sn74hc175n"],
        ["dip_20", "logic", "octal_d_type_transparent_latch_tri_state", "texas_instruments", "sn74hc373n"],
        ["dip_20", "logic", "octal_bus_transceiver_tri_state", "texas_instruments", "sn74hc245n"],
        ["dip_14", "logic", "quad_2_input_nand_gate_open_collector", "texas_instruments", "sn74hc03n"],
        ["dip_14", "logic", "hex_schmitt_trigger_inverter", "texas_instruments", "sn74hc14n"],
        ["dip_14", "logic", "serial_in_parallel_out_shift_register", "texas_instruments", "sn74hc164n"],
        ["soic_14", "logic", "serial_in_parallel_out_shift_register", "texas_instruments", "sn74hc164dr"],
        ["dip_16", "logic", "parallel_in_serial_out_shift_register", "texas_instruments", "sn74hc165n"],
        ["dip_20", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74hc244n"],
        ["dip_16", "logic", "3_to_8_line_decoder_demultiplexer", "texas_instruments", "sn74hc138n"],
        # TO-220 linear regulator from the same L78xx family as L7815CV-DG.
        ["to_220", "power_management", "linear_voltage_regulator_12_volt", "stmicroelectronics", "l7812cv_dg"],
        ["to_220", "power_management", "linear_voltage_regulator_8_volt", "stmicroelectronics", "l7808cv_dg"],
        ["to_220", "power_management", "linear_voltage_regulator_9_volt", "stmicroelectronics", "l7809cv_dg"],
        ["to_220", "power_management", "linear_voltage_regulator_5_volt", "stmicroelectronics", "l7805cv_dg"],
        ["to_220", "power_management", "linear_voltage_regulator_6_volt", "stmicroelectronics", "l7806cv_dg"],
        ["to_220", "power_management", "linear_voltage_regulator_24_volt", "stmicroelectronics", "l7824cv_dg"],
        # Negative L79xx rails beside the existing negative_15_volt row.
        ["to_220", "power_management", "linear_voltage_regulator_negative_12_volt", "stmicroelectronics", "l7912cv_dg"],
        ["to_220", "power_management", "linear_voltage_regulator_negative_5_volt", "stmicroelectronics", "l7905cv_dg"],
        # DIP optocouplers (first optocoupler rows in this list).
        ["dip_6", "optocoupler", "darlington_output_optocoupler", "onsemi", "4n33m"],
        ["dip_6", "optocoupler", "phototransistor_output_optocoupler", "onsemi", "4n35m"],
        ["dip_8", "optocoupler", "logic_output_optocoupler", "onsemi", "6n139m"],
        ["dip_8", "optocoupler", "gate_driver_optocoupler", "toshiba", "tlp250_f"],
        # SMD Toshiba optocouplers.
        ["sop_4", "optocoupler", "photodarlington_output_optocoupler", "toshiba", "tlp127_tpl_u_f"],
        ["sop_8", "optocoupler", "gate_driver_optocoupler", "toshiba", "tlp350_tp1_f"],
        ["soic_6", "optocoupler", "gate_driver_optocoupler", "toshiba", "tlp701_tp_f"],
        # PWM / DC-DC controllers and comparator from the JLC queue.
        ["dip_8", "power_management", "current_mode_pwm_controller", "stmicroelectronics", "uc3845bn"],
        ["dip_8", "power_management", "current_mode_pwm_controller", "stmicroelectronics", "uc3842bn"],
        ["dip_8", "power_management", "current_mode_pwm_controller", "stmicroelectronics", "uc3843bn"],
        ["dip_8", "power_management", "dc_dc_converter", "stmicroelectronics", "mc34063ecn"],
        ["pdip_14", "comparator", "quad_differential_comparator", "texas_instruments", "lm239n"],
        # More DIP logic: HC latch, LS buffer, CD4000 series.
        ["dip_20", "logic", "octal_d_type_transparent_latch_tri_state", "texas_instruments", "sn74hc573an"],
        ["dip_14", "logic", "hex_buffer_open_collector", "texas_instruments", "sn74ls07n"],
        ["dip_16", "logic", "14_stage_binary_counter_oscillator", "texas_instruments", "cd4060be"],
        ["dip_14", "logic", "dual_d_type_flip_flop", "texas_instruments", "cd4013be"],
        ["dip_16", "logic", "8_channel_analog_multiplexer_demultiplexer", "texas_instruments", "cd4051be"],
        ["dip_16", "logic", "differential_4_channel_analog_multiplexer_demultiplexer", "texas_instruments", "cd4052be"],
        ["dip_16", "logic", "triple_2_channel_analog_multiplexer_demultiplexer", "texas_instruments", "cd4053be"],
        # Third DIP batch: CD4000 glue, amp/comparator/drivers, PWM.
        ["dip_14", "logic", "quad_bilateral_analog_switch", "texas_instruments", "cd4066be"],
        ["dip_14", "logic", "hex_inverter", "texas_instruments", "cd4069ube"],
        ["dip_14", "logic", "quad_2_input_and_gate", "texas_instruments", "cd4081be"],
        ["dip_8", "driver", "dual_peripheral_and_gate_driver", "texas_instruments", "sn75451bp"],
        ["dip_8", "amplifier", "dual_jfet_input_operational_amplifier", "texas_instruments", "lf353p"],
        ["dip_8", "amplifier", "dual_operational_amplifier", "texas_instruments", "lm2904p"],
        ["dip_8", "comparator", "dual_differential_comparator", "texas_instruments", "lm393p"],
        ["dip_8", "power_management", "current_mode_pwm_controller", "texas_instruments", "tl3842p"],
        ["dip_8", "power_management", "current_mode_pwm_controller", "texas_instruments", "tl3845p"],
        ["dip_8", "amplifier", "dual_operational_amplifier", "texas_instruments", "lm358p"],
        ["dip_16", "power_management", "pwm_control_circuit", "texas_instruments", "tl494cn"],
        ["dip_8", "interface", "rs485_rs422_transceiver", "texas_instruments", "sn75176bp"],
        # Fourth DIP batch: quad amps/comparator, CD4000 glue, precision amp.
        ["dip_14", "amplifier", "quad_operational_amplifier", "texas_instruments", "lm224n"],
        ["dip_14", "amplifier", "quad_jfet_input_operational_amplifier", "texas_instruments", "lf347n"],
        ["dip_16", "logic", "quad_2_channel_analog_multiplexer", "texas_instruments", "sn74hc157n"],
        ["dip_8", "comparator", "single_differential_comparator_open_collector", "texas_instruments", "lm311p"],
        ["dip_16", "logic", "dual_bcd_up_counter", "texas_instruments", "cd4518be"],
        ["dip_16", "logic", "bcd_to_decimal_decoder", "texas_instruments", "cd4028be"],
        ["dip_8", "amplifier", "single_precision_operational_amplifier", "texas_instruments", "op07cp"],
        ["dip_14", "logic", "quad_2_input_nor_gate", "texas_instruments", "cd4001be"],
        ["dip_14", "logic", "quad_2_input_nand_gate", "texas_instruments", "cd4011be"],
        ["dip_14", "logic", "dual_4_input_and_gate", "texas_instruments", "cd4082be"],
        ["dip_16", "logic", "14_stage_ripple_carry_binary_counter", "texas_instruments", "cd4020be"],
        ["dip_14", "logic", "monostable_astable_multivibrator", "texas_instruments", "cd4047be"],
        # Fifth DIP batch: shift register, comparators, HC flops, CD4000,
        # TRIAC optocouplers, LS decade counter, SG3525 PWM.
        ["dip_16", "logic", "8_stage_shift_register", "texas_instruments", "cd4014be"],
        ["dip_8", "comparator", "dual_differential_comparator", "texas_instruments", "lm293p"],
        ["to_92_3", "power_management", "adjustable_shunt_voltage_reference", "texas_instruments", "tl431aclp"],
        ["dip_8", "amplifier", "dual_operational_amplifier", "texas_instruments", "lm258p"],
        ["dip_20", "logic", "octal_d_type_flip_flop_tri_state", "texas_instruments", "sn74hc374n"],
        ["dip_20", "logic", "octal_d_type_flip_flop", "texas_instruments", "sn74hc273n"],
        ["dip_16", "logic", "dual_jk_flip_flop", "texas_instruments", "cd4027be"],
        ["dip_6", "optocoupler", "triac_output_optocoupler", "onsemi", "moc3023m"],
        ["dip_6", "optocoupler", "phototransistor_output_optocoupler", "onsemi", "4n25m"],
        ["dip_6", "optocoupler", "triac_output_optocoupler", "onsemi", "moc3021m"],
        ["dip_14", "logic", "decade_counter", "texas_instruments", "sn74ls90n"],
        ["dip_16", "power_management", "pwm_controller", "onsemi", "sg3525ang"],
        # Sixth DIP batch: onsemi second sources of the ST power parts.
        ["dip_8", "power_management", "dc_dc_converter", "onsemi", "mc34063ap1g"],
        ["dip_8", "power_management", "current_mode_pwm_controller", "onsemi", "uc3842bng"],
        ["dip_8", "power_management", "current_mode_pwm_controller", "onsemi", "uc3843bng"],
        ["dip_8", "power_management", "current_mode_pwm_controller", "onsemi", "uc3844bng"],
        ["dip_8", "power_management", "current_mode_pwm_controller", "onsemi", "uc3845bng"],
        # Seventh DIP batch: VIPer offline converters, op-amps, CD4000 glue,
        # logic-output optocouplers, a CPLD and an 8051 MCU.
        ["dip_8", "power_management", "offline_switching_converter", "stmicroelectronics", "viper12adipe"],
        ["dip_8", "power_management", "offline_switching_converter", "stmicroelectronics", "viper22adipe"],
        ["dip_8", "amplifier", "dual_operational_amplifier", "texas_instruments", "ne5532p"],
        ["dip_16", "logic", "bcd_to_7_segment_latch_decoder_driver", "texas_instruments", "cd4511be"],
        ["dip_14", "logic", "dual_4_input_or_gate", "texas_instruments", "cd4072be"],
        ["dip_14", "amplifier", "quad_operational_amplifier", "texas_instruments", "lm348n"],
        ["dip_14", "logic", "quad_2_input_or_gate", "texas_instruments", "cd4071be"],
        ["dip_8", "optocoupler", "logic_output_optocoupler", "onsemi", "6n137m"],
        ["dip_4", "optocoupler", "phototransistor_output_optocoupler", "sharp_microelectronics", "pc817x2nszw"],
        ["dip_4", "optocoupler", "phototransistor_output_optocoupler", "everlight", "el817_b_f"],
        ["tqfp_144", "cpld", "cpld_1270_macrocells", "intel_altera", "epm1270t144c5n"],
        ["dip_20", "microcontroller", "8_bit_8051", "microchip", "at89c2051_24pu"],
        # Infineon IR21xx half-bridge gate drivers (first driver rows in
        # this list; DIP-8 and SOIC-8 bodies).
        ["dip_8", "driver", "half_bridge_gate_driver", "infineon", "ir2101pbf"],
        ["soic_8", "driver", "half_bridge_gate_driver", "infineon", "ir2101strpbf"],
        ["soic_8", "driver", "half_bridge_gate_driver", "infineon", "ir2103strpbf"],
        ["soic_8", "driver", "half_bridge_gate_driver", "infineon", "irs2103strpbf"],
        ["soic_8", "driver", "half_bridge_gate_driver", "infineon", "ir2104strpbf"],
        ["soic_8", "driver", "half_bridge_gate_driver", "infineon", "ir2108strpbf"],
        # More IR21xx gate drivers plus the IR2520 ballast controller and the
        # IR2153 self-oscillating driver.  soic_16/soic_28 (300 mil) bodies
        # are new package tokens here.
        ["soic_8", "driver", "half_bridge_gate_driver", "infineon", "ir2109strpbf"],
        ["dip_14", "driver", "half_bridge_gate_driver", "infineon", "ir2110pbf"],
        ["soic_16", "driver", "half_bridge_gate_driver", "infineon", "ir2110strpbf"],
        ["soic_8", "driver", "half_bridge_gate_driver", "infineon", "ir2111spbf"],
        ["dip_14", "driver", "half_bridge_gate_driver", "infineon", "ir2112pbf"],
        ["soic_16", "driver", "half_bridge_gate_driver", "infineon", "ir2112spbf"],
        ["dip_14", "driver", "half_bridge_gate_driver", "infineon", "ir2113pbf"],
        ["soic_16", "driver", "half_bridge_gate_driver", "infineon", "ir2113strpbf"],
        ["soic_8", "driver", "high_side_gate_driver", "infineon", "ir2117strpbf"],
        ["soic_28", "driver", "three_phase_gate_driver", "infineon", "ir2136strpbf"],
        ["dip_8", "driver", "fluorescent_ballast_controller", "infineon", "ir2520dpbf"],
        ["dip_8", "driver", "self_oscillating_half_bridge_driver", "infineon", "ir2153pbf"],
        ["soic_8", "driver", "self_oscillating_half_bridge_driver", "infineon", "ir21531strpbf"],
        ["soic_8", "driver", "self_oscillating_half_bridge_driver", "infineon", "irs2153dstrpbf"],
        ["soic_14", "driver", "cfl_controller", "infineon", "ir2156strpbf"],
        ["soic_8", "driver", "half_bridge_gate_driver", "infineon", "ir2184strpbf"],
        # Microchip 24-series I2C serial EEPROMs; the 24FC512 sits in the wide
        # 208 mil SOIC-8 body, the rest in the standard 150 mil one.
        ["soic_8", "memory", "i2c_eeprom_1_kbit", "microchip", "24lc01bt_i_sn"],
        ["soic_8", "memory", "i2c_eeprom_2_kbit", "microchip", "24lc02bt_i_sn"],
        ["soic_8", "memory", "i2c_eeprom_8_kbit", "microchip", "24lc08bt_i_sn"],
        ["soic_8", "memory", "i2c_eeprom_16_kbit", "microchip", "24lc16bt_i_sn"],
        ["soic_8", "memory", "i2c_eeprom_256_kbit", "microchip", "24lc256t_i_sn"],
        ["soic_8_208mil", "memory", "i2c_eeprom_512_kbit", "microchip", "24fc512t_i_sm"],
        ["soic_8", "memory", "i2c_eeprom_64_kbit", "microchip", "24lc64t_i_sn"],
        ["soic_8", "memory", "spi_eeprom_64_kbit", "microchip", "25lc640t_i_sn"],
        # onsemi 74AC/74ACT fast CMOS logic in SOIC/TSSOP bodies; the wide
        # 300 mil SOIC-20 is a new package token here.
        ["soic_14", "logic", "hex_inverter", "onsemi", "74ac04scx"],
        ["soic_14", "logic", "quad_2_input_and_gate", "onsemi", "74ac08scx"],
        ["tssop_16", "logic", "3_to_8_line_decoder_demultiplexer", "onsemi", "74ac138mtcx"],
        ["soic_14", "logic", "hex_schmitt_trigger_inverter", "onsemi", "74ac14scx"],
        ["soic_20_300mil", "logic", "octal_bus_buffer_tri_state_inverting", "onsemi", "74ac240scx"],
        ["soic_20_300mil", "logic", "octal_bus_transceiver_tri_state", "onsemi", "74ac245scx"],
        ["soic_14", "logic", "quad_2_input_nand_gate", "onsemi", "74act00scx"],
        ["soic_14", "logic", "hex_inverter", "onsemi", "74act04scx"],
        ["soic_14", "logic", "quad_2_input_and_gate", "onsemi", "74act08scx"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "onsemi", "74act244mtcx"],
        # onsemi 74ACT32 plus the Nexperia/NXP fast-CMOS wave: single-gate
        # SOT-23-5 logic, the TSSOP-48 16-bit transceiver and the nxp /
        # philips makers are new tokens here.
        ["soic_14", "logic", "quad_2_input_or_gate", "onsemi", "74act32scx"],
        ["soic_14", "logic", "hex_schmitt_trigger_inverter", "nexperia", "74ahc14d_118"],
        ["sot_23_5", "logic", "single_schmitt_trigger_inverter", "nexperia", "74ahc1g14gv_125"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "nexperia", "74ahc244pw_118"],
        ["tssop_20", "logic", "octal_bus_transceiver_tri_state", "nexperia", "74ahc245pw_118"],
        ["soic_16", "logic", "serial_in_parallel_out_shift_register", "nexperia", "74ahc595d_118"],
        ["tssop_48", "logic", "16_bit_bus_transceiver_tri_state", "nexperia", "74alvc164245dgg_11"],
        ["soic_20_300mil", "logic", "octal_d_type_transparent_latch", "nxp_semiconductors", "74f373d"],
        ["soic_20_300mil", "logic", "octal_d_type_flip_flop_common_enable", "philips_semiconductors", "74f377ad"],
        ["soic_14", "logic", "quad_2_input_nand_gate", "nexperia", "74hc00d_653"],
        ["tssop_14", "logic", "quad_2_input_nand_gate", "nexperia", "74hc00pw_118"],
        ["soic_14", "logic", "quad_2_input_nor_gate", "nexperia", "74hc02d_653"],
        # Continuing the 74HC SMD wave: open-collector inverter, 3-input NAND,
        # monostable, tri-state buffers, Schmitt NAND and the decoder pair;
        # onsemi's MC-hosted 74HC04 lands in TSSOP-14.
        ["tssop_14", "logic", "hex_inverter", "onsemi", "mc74hc04adtr2g"],
        ["soic_14", "logic", "hex_inverter", "nexperia", "74hc04d_653"],
        ["soic_14", "logic", "hex_inverter_open_collector", "nexperia", "74hc05d_118"],
        ["soic_14", "logic", "quad_2_input_and_gate", "nexperia", "74hc08d_653"],
        ["soic_14", "logic", "triple_3_input_nand_gate", "nexperia", "74hc10d_653"],
        ["soic_16", "logic", "dual_retriggerable_monostable_multivibrator", "nexperia", "74hc123d_653"],
        ["soic_14", "logic", "quad_bus_buffer_tri_state", "nexperia", "74hc125d_653"],
        ["tssop_14", "logic", "quad_bus_buffer_tri_state", "nexperia", "74hc125pw_118"],
        ["soic_14", "logic", "quad_bus_buffer_tri_state", "nexperia", "74hc126d_653"],
        ["soic_14", "logic", "quad_2_input_nand_gate_schmitt_trigger", "nexperia", "74hc132d_653"],
        ["soic_16", "logic", "3_to_8_line_decoder_demultiplexer", "nexperia", "74hc138d_653"],
        ["soic_16", "logic", "dual_2_to_4_line_decoder_demultiplexer", "nexperia", "74hc139d_653"],
        # Next 74HC SMD slice: Schmitt inverter, latch/flip-flop/counter block,
        # both shift-register directions, multiplexer and the 237/238 decoders.
        ["tssop_14", "logic", "hex_schmitt_trigger_inverter", "nexperia", "74hc14pw_118"],
        ["soic_20_300mil", "logic", "octal_d_type_transparent_latch_tri_state", "nexperia", "74hc573d_653"],
        ["soic_16", "logic", "quad_2_to_1_line_multiplexer", "nexperia", "74hc157d_653"],
        ["soic_16", "logic", "synchronous_4_bit_binary_counter", "nexperia", "74hc161d_653"],
        ["tssop_14", "logic", "serial_in_parallel_out_shift_register", "nexperia", "74hc164pw_118"],
        ["soic_16", "logic", "parallel_in_serial_out_shift_register", "nexperia", "74hc165d_653"],
        ["soic_16", "logic", "quad_d_type_flip_flop", "nexperia", "74hc175d_653"],
        ["soic_14", "logic", "dual_4_input_and_gate", "nexperia", "74hc21d_653"],
        ["soic_16", "logic", "3_to_8_line_decoder_demultiplexer_latched", "nexperia", "74hc237d_653"],
        ["soic_16", "logic", "3_to_8_line_decoder_demultiplexer", "nexperia", "74hc238d_653"],
        ["soic_20_300mil", "logic", "octal_bus_buffer_tri_state", "nexperia", "74hc244d_653"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "nexperia", "74hc244pw_118"],
        # Tranche-70 74HC slice: onsemi's wide-body 244, the 245 transceiver
        # pair, 3-state multiplexer, bilateral switch, NOR/NAND/OR gates, the
        # inverting hex buffer and the 373/374/377 register block.
        ["soic_20_300mil", "logic", "octal_bus_buffer_tri_state", "onsemi", "mm74hc244wmx"],
        ["soic_20_300mil", "logic", "octal_bus_transceiver_tri_state", "nexperia", "74hc245d_653"],
        ["tssop_20", "logic", "octal_bus_transceiver_tri_state", "nexperia", "74hc245pw_118"],
        ["soic_16", "logic", "quad_2_to_1_line_multiplexer_tri_state", "nexperia", "74hc257d_653"],
        ["soic_14", "logic", "quad_bilateral_analog_switch", "nexperia", "74hc4066d_653"],
        ["soic_14", "logic", "triple_3_input_nor_gate", "nexperia", "74hc27d_653"],
        ["soic_14", "logic", "8_input_nand_gate", "nexperia", "74hc30d_653"],
        ["soic_14", "logic", "quad_2_input_or_gate", "nexperia", "74hc32d_653"],
        ["soic_16", "logic", "hex_bus_buffer_tri_state_inverting", "nexperia", "74hc366d_653"],
        ["soic_20_300mil", "logic", "octal_d_type_transparent_latch_tri_state", "nexperia", "74hc373d_653"],
        ["soic_20_300mil", "logic", "octal_d_type_flip_flop_tri_state", "nexperia", "74hc374d_653"],
        ["soic_20_300mil", "logic", "octal_d_type_flip_flop_common_enable", "nexperia", "74hc377d_653"],
        # Tranche-71 74HC4xxx slice: ripple counters, the 4051/4052/4053 analog
        # multiplexer family, the latched 4094 shift register, the 541 buffer
        # and the first AVR microcontrollers; tqfp_44 is a new package token.
        ["soic_14", "logic", "dual_4_bit_binary_ripple_counter", "nexperia", "74hc393d_653"],
        ["tssop_16", "logic", "8_channel_analog_multiplexer_demultiplexer", "nexperia", "74hc4051pw_118"],
        ["tssop_16", "logic", "dual_4_channel_analog_multiplexer_demultiplexer", "nexperia", "74hc4052pw_118"],
        ["soic_16", "logic", "triple_2_channel_analog_multiplexer_demultiplexer", "nexperia", "74hc4053d_653"],
        ["tssop_16", "logic", "triple_2_channel_analog_multiplexer_demultiplexer", "nexperia", "74hc4053pw_118"],
        ["soic_16", "logic", "14_stage_binary_ripple_counter_oscillator", "nexperia", "74hc4060d_653"],
        ["tssop_14", "logic", "quad_bilateral_analog_switch", "nexperia", "74hc4066pw_118"],
        ["soic_16", "logic", "serial_in_parallel_out_shift_register_latched_tri_state", "nexperia", "74hc4094d_653"],
        ["tssop_16", "logic", "serial_in_parallel_out_shift_register_latched_tri_state", "nexperia", "74hc4094pw_118"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "nexperia", "74hc541pw_118"],
        ["tqfp_44", "microcontroller", "8_bit_avr_16_kb_flash", "microchip", "atmega16a_au"],
        ["tqfp_44", "microcontroller", "8_bit_avr_32_kb_flash", "microchip", "atmega32a_au"],
        # Tranche-72: the plain L7815CV beside the -DG L78xx siblings, plus the
        # TSSOP bodies of the 573 latch and 595 shift register.
        ["to_220", "power_management", "linear_voltage_regulator_15_volt", "stmicroelectronics", "l7815cv"],
        ["tssop_20", "logic", "octal_d_type_transparent_latch_tri_state", "nexperia", "74hc573pw_118"],
        ["tssop_16", "logic", "serial_in_parallel_out_shift_register", "nexperia", "74hc595pw_118"],
        # Tranche-73: the 74HC comparator/XOR/74 pair and the TTL-input 74HCT
        # mirrors of gates already carried for 74HC.
        ["tssop_14", "logic", "dual_d_type_flip_flop_set_reset", "nexperia", "74hc74pw_118"],
        ["soic_16", "logic", "4_bit_magnitude_comparator", "nexperia", "74hc85d_653"],
        ["soic_14", "logic", "quad_2_input_xor_gate", "nexperia", "74hc86d_653"],
        ["soic_14", "logic", "quad_2_input_nor_gate", "nexperia", "74hct02d_653"],
        ["soic_14", "logic", "quad_2_input_and_gate", "nexperia", "74hct08d_653"],
        ["soic_16", "logic", "dual_retriggerable_monostable_multivibrator", "nexperia", "74hct123d_653"],
        ["soic_14", "logic", "quad_bus_buffer_tri_state", "nexperia", "74hct125d_653"],
        ["soic_14", "logic", "quad_2_input_nand_gate_schmitt_trigger", "nexperia", "74hct132d_653"],
        ["tssop_14", "logic", "quad_2_input_nand_gate_schmitt_trigger", "nexperia", "74hct132pw_118"],
        ["soic_16", "logic", "3_to_8_line_decoder_demultiplexer", "nexperia", "74hct138d_653"],
        ["soic_14", "logic", "hex_schmitt_trigger_inverter", "nexperia", "74hct14d_653"],
        ["tssop_14", "logic", "hex_schmitt_trigger_inverter", "nexperia", "74hct14pw_118"],
        # Tranche-74: the HCT SMD register/mux/buffer tail plus onsemi's
        # low-voltage 74LCX Schmitt inverter and 16-bit buffer; tssop_48
        # covers the MTD body beside the DGG one.
        ["soic_16", "logic", "quad_2_to_1_line_multiplexer", "nexperia", "74hct157d_653"],
        ["soic_20_300mil", "logic", "octal_bus_buffer_tri_state", "nexperia", "74hct244d_653"],
        ["soic_20_300mil", "logic", "octal_bus_transceiver_tri_state", "nexperia", "74hct245d_653"],
        ["tssop_20", "logic", "octal_bus_transceiver_tri_state", "nexperia", "74hct245pw_118"],
        ["soic_14", "logic", "quad_2_input_or_gate", "nexperia", "74hct32d_653"],
        ["soic_20_300mil", "logic", "octal_d_type_transparent_latch_tri_state", "nexperia", "74hct373d_653"],
        ["tssop_20", "logic", "octal_d_type_transparent_latch_tri_state", "onsemi", "74hct373mtcx"],
        ["soic_14", "logic", "quad_bilateral_analog_switch", "nexperia", "74hct4066d_118"],
        ["soic_20_300mil", "logic", "octal_d_type_flip_flop_tri_state", "nexperia", "74hct574d_653"],
        ["soic_14", "logic", "quad_2_input_xor_gate", "nexperia", "74hct86d_653"],
        ["tssop_14", "logic", "hex_schmitt_trigger_inverter", "onsemi", "74lcx14mtcx"],
        ["tssop_48", "logic", "16_bit_bus_buffer_tri_state", "onsemi", "74lcx16244mtdx"],
        # Tranche-75: the low-voltage LVC family mirrors (07 open-drain buffer,
        # 08/125/138/14) plus onsemi's LCX 16-bit register and transceiver and
        # TI's LV123A monostable.
        ["tssop_48", "logic", "16_bit_d_type_flip_flop_tri_state", "onsemi", "74lcx16374mtdx"],
        ["tssop_20", "logic", "octal_bus_transceiver_tri_state", "onsemi", "74lcx245mtcx"],
        ["tssop_16", "logic", "dual_retriggerable_monostable_multivibrator", "texas_instruments", "sn74lv123apwr"],
        ["soic_14", "logic", "hex_buffer_open_collector", "nexperia", "74lvc07ad_118"],
        ["tssop_14", "logic", "hex_buffer_open_collector", "nexperia", "74lvc07apw_118"],
        ["soic_14", "logic", "quad_2_input_and_gate", "nexperia", "74lvc08ad_118"],
        ["tssop_14", "logic", "quad_2_input_and_gate", "nexperia", "74lvc08apw_118"],
        ["soic_14", "logic", "quad_bus_buffer_tri_state", "nexperia", "74lvc125ad_118"],
        ["tssop_14", "logic", "quad_bus_buffer_tri_state", "nexperia", "74lvc125apw_118"],
        ["soic_16", "logic", "3_to_8_line_decoder_demultiplexer", "nexperia", "74lvc138ad_118"],
        ["tssop_16", "logic", "3_to_8_line_decoder_demultiplexer", "nexperia", "74lvc138apw_118"],
        ["soic_14", "logic", "hex_schmitt_trigger_inverter", "nexperia", "74lvc14ad_118"],
        # Tranche-76: the LVC tail - 16-bit DGG bodies, the single-gate SOT-23-5
        # Schmitt buffer, the dual-gate SOT-363 inverter (sot_363 token new
        # here) and the 244/245/32APW small-outline set.
        ["tssop_14", "logic", "hex_schmitt_trigger_inverter", "nexperia", "74lvc14apw_118"],
        ["soic_16", "logic", "quad_2_to_1_line_multiplexer", "nexperia", "74lvc157ad_118"],
        ["tssop_16", "logic", "quad_2_to_1_line_multiplexer", "nexperia", "74lvc157apw_118"],
        ["tssop_48", "logic", "16_bit_bus_transceiver_tri_state", "nexperia", "74lvc162245adgg_11"],
        ["tssop_48", "logic", "16_bit_bus_buffer_tri_state", "nexperia", "74lvc16244adgg_118"],
        ["tssop_48", "logic", "16_bit_d_type_flip_flop_tri_state", "nexperia", "74lvc16374adgg_118"],
        ["sot_23_5", "logic", "single_schmitt_trigger_buffer", "nexperia", "74lvc1g17gv_125"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "nexperia", "74lvc244apw_118"],
        ["soic_20_300mil", "logic", "octal_bus_transceiver_tri_state", "nexperia", "74lvc245ad_118"],
        ["tssop_20", "logic", "octal_bus_transceiver_tri_state", "nexperia", "74lvc245apw_118"],
        ["sot_363", "logic", "dual_schmitt_trigger_inverter", "nexperia", "74lvc2g14gw_125"],
        ["tssop_14", "logic", "quad_2_input_or_gate", "nexperia", "74lvc32apw_118"],
        # Tranche-77: LVC register/latch bodies, the translating LVC4245 and
        # LVX3245 in TSSOP-24, and onsemi's VHC gate set.
        ["tssop_24", "logic", "octal_bus_transceiver_tri_state", "nexperia", "74lvc4245apw_118"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "nexperia", "74lvc541apw_118"],
        ["soic_20_300mil", "logic", "octal_d_type_transparent_latch_tri_state", "nexperia", "74lvc573ad_118"],
        ["tssop_20", "logic", "octal_d_type_transparent_latch_tri_state", "nexperia", "74lvc573apw_118"],
        ["soic_20_300mil", "logic", "octal_d_type_flip_flop_tri_state", "nexperia", "74lvc574ad_118"],
        ["soic_14", "logic", "dual_d_type_flip_flop_set_reset", "nexperia", "74lvc74ad_118"],
        ["tssop_14", "logic", "dual_d_type_flip_flop_set_reset", "nexperia", "74lvc74apw_118"],
        ["tssop_24", "logic", "octal_bus_transceiver_tri_state", "onsemi", "74lvx3245mtcx"],
        ["soic_14", "logic", "quad_2_input_and_gate", "onsemi", "74vhc08mx"],
        ["tssop_14", "logic", "quad_bus_buffer_tri_state", "onsemi", "74vhc125mtcx"],
        ["tssop_16", "logic", "3_to_8_line_decoder_demultiplexer", "onsemi", "74vhc138mtcx"],
        ["tssop_14", "logic", "hex_schmitt_trigger_inverter", "onsemi", "74vhc14mtcx"],
        # Tranche-78: VHC tail, the MICROWIRE 93-series EEPROM, ADI op-amp and
        # RS-232 transceivers, the AM26LS31/32 differential pair, and the two
        # remaining AMS1117 rails; ssop_28_208mil is a new package token.
        ["tssop_14", "logic", "quad_2_input_or_gate", "onsemi", "74vhc32mtcx"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "onsemi", "74vhct244amtcx"],
        ["soic_8", "memory", "microwire_eeprom_2_kbit", "microchip", "93lc56bt_i_sn"],
        ["tssop_14", "amplifier", "operational_amplifier_quad_rail_to_rail", "analog_devices", "ad8694aruz_reel"],
        ["soic_16", "interface", "rs_232_transceiver", "analog_devices", "adm202earnz_reel"],
        ["ssop_28_208mil", "interface", "rs_232_transceiver", "analog_devices", "adm213earsz_reel"],
        ["soic_16", "interface", "quad_differential_line_driver", "texas_instruments", "am26ls31cdr"],
        ["soic_16", "interface", "quad_differential_line_receiver", "texas_instruments", "am26ls32acdr"],
        ["sot_223_3", "power_management", "linear_voltage_regulator_1_8_volt", "advanced_monolithic_systems", "ams1117_1_8"],
        ["sot_223_3", "power_management", "linear_voltage_regulator_adjustable", "advanced_monolithic_systems", "ams1117_adj"],
        # Tranche-79: the Atmel memory family - I2C/SPI/MICROWIRE EEPROM
        # spread across the value ladder, a 32 Mbit SPI NOR flash (renesas
        # maker), the GAL-class ATF16V8 EEPLD (first pld category row) and
        # the 128 KB AVR in TQFP-64 (new package token).
        ["soic_8", "memory", "i2c_eeprom_2_kbit", "microchip", "at24c02c_sshm_t"],
        ["soic_8", "memory", "i2c_eeprom_4_kbit", "microchip", "at24c04c_sshm_t"],
        ["soic_8", "memory", "i2c_eeprom_128_kbit", "microchip", "at24c128c_sshm_t"],
        ["soic_8", "memory", "i2c_eeprom_16_kbit", "microchip", "at24c16c_sshm_t"],
        ["soic_8", "memory", "i2c_eeprom_256_kbit", "microchip", "at24c256c_sshl_t"],
        ["soic_8", "memory", "i2c_eeprom_64_kbit", "microchip", "at24c64d_sshm_t"],
        ["soic_8", "memory", "spi_eeprom_16_kbit", "microchip", "at25160b_sshl_t"],
        ["soic_8_208mil", "memory", "spi_nor_flash_32_mbit", "renesas", "at25df321a_sh_t"],
        ["soic_8", "memory", "microwire_eeprom_1_kbit", "microchip", "at93c46dn_sh_t"],
        ["soic_8", "memory", "microwire_eeprom_16_kbit", "microchip", "at93c86a_10su_2_7t"],
        ["dip_20", "pld", "eepld_16v8b", "microchip", "atf16v8b_15pu"],
        ["tqfp_64", "microcontroller", "8_bit_avr_128_kb_flash", "microchip", "atmega128a_au"],
        # Tranche-80: TI specialty and 4000/74HC40xxx wave - battery charger,
        # sub-GHz RF transceiver (first rf rows), the CD40xx analog switch
        # family, the ACT245 transceiver, addressable latch, 8-input NAND and
        # the 4046 PLL (first clock_management rows).
        ["qfn_20_ep", "power_management", "battery_charger_ic", "texas_instruments", "bq24070rhlr"],
        ["qfn_32_ep", "rf", "sub_ghz_rf_transceiver", "texas_instruments", "cc1020rssr"],
        ["soic_14", "logic", "quad_bilateral_analog_switch", "texas_instruments", "cd4016bm96"],
        ["soic_16", "logic", "dual_4_channel_analog_multiplexer_demultiplexer", "texas_instruments", "cd4052bm96"],
        ["tssop_16", "logic", "dual_4_channel_analog_multiplexer_demultiplexer", "texas_instruments", "cd4052bpwr"],
        ["soic_24_300mil", "logic", "16_channel_analog_multiplexer", "texas_instruments", "cd4067bm96"],
        ["soic_20_300mil", "logic", "octal_bus_transceiver_tri_state", "texas_instruments", "cd74act245m96"],
        ["soic_16", "logic", "8_bit_addressable_latch", "texas_instruments", "cd74hc259m96"],
        ["soic_14", "logic", "8_input_nand_gate", "texas_instruments", "cd74hc30m96"],
        ["soic_16", "clock_management", "pll_with_vco", "texas_instruments", "cd74hc4046am96"],
        ["tssop_16", "clock_management", "pll_with_vco", "texas_instruments", "cd74hc4046apwr"],
        ["soic_16", "logic", "triple_2_channel_analog_multiplexer_demultiplexer", "texas_instruments", "cd74hc4053m96"],
        # Tranche-81: the CD74HC/HCT tail (4053/4075/4052/4514/93/00/139/541/74),
        # the Cypress zero-delay clock buffer and the Vishay DG419 SPDT switch.
        ["tssop_16", "logic", "triple_2_channel_analog_multiplexer_demultiplexer", "texas_instruments", "cd74hc4053pwr"],
        ["soic_14", "logic", "triple_3_input_or_gate", "texas_instruments", "cd74hc4075m96"],
        ["soic_16", "logic", "dual_4_channel_analog_multiplexer_demultiplexer", "texas_instruments", "cd74hc4052m96"],
        ["soic_24_300mil", "logic", "4_to_16_line_decoder_demultiplexer_latched", "texas_instruments", "cd74hc4514m96"],
        ["soic_14", "logic", "4_bit_binary_ripple_counter", "texas_instruments", "cd74hc93m96"],
        ["soic_14", "logic", "quad_2_input_nand_gate", "texas_instruments", "cd74hct00m96"],
        ["soic_16", "logic", "dual_2_to_4_line_decoder_demultiplexer", "texas_instruments", "cd74hct139m96"],
        ["soic_16", "logic", "triple_2_channel_analog_multiplexer_demultiplexer", "texas_instruments", "cd74hct4053m96"],
        ["soic_20_300mil", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "cd74hct541m96"],
        ["soic_14", "logic", "dual_d_type_flip_flop_set_reset", "texas_instruments", "cd74hct74m96"],
        ["soic_16", "clock_management", "zero_delay_clock_buffer", "infineon_cypress_semicon", "cy2308sxi_1"],
        ["soic_8", "logic", "spdt_analog_switch", "vishay_intertech", "dg419dy_t1_e3"],
        # Tranche-82: VHC monostable/inverter, the LVDS receiver, the FOD817
        # and HCPL optocoupler set (first broadcom_limited maker) and the
        # HEF4000 CMOS quartet.
        ["tssop_14", "logic", "hex_inverter", "onsemi", "74vhc04mtcx"],
        ["soic_16", "logic", "dual_retriggerable_monostable_multivibrator", "onsemi", "74vhc123amx"],
        ["soic_16", "interface", "quad_lvds_line_receiver", "texas_instruments", "ds90lv032atmx_nopb"],
        ["sop_4", "optocoupler", "phototransistor_output_optocoupler", "onsemi", "fod817as"],
        ["soic_8", "optocoupler", "phototransistor_output_optocoupler", "broadcom_limited", "hcpl_0501_500e"],
        ["soic_8", "optocoupler", "phototransistor_output_optocoupler", "broadcom_limited", "hcpl_0600_500e"],
        ["soic_14", "logic", "quad_2_input_nor_gate", "nexperia", "hef4001bt_653"],
        ["soic_14", "logic", "hex_schmitt_trigger_inverter", "nexperia", "hef40106bt_653"],
        ["soic_14", "logic", "quad_2_input_nand_gate", "nexperia", "hef4011bt_653"],
        ["soic_14", "logic", "dual_d_type_flip_flop_set_reset", "nexperia", "hef4013bt_653"],
        # Tranche-83: the HEF4000 tail (4014/4021 shifters, 4027 JK pair,
        # 4053/4066 switches, 4060 counter-oscillator, unbuffered 4069, 4070
        # XOR), TI's CD4053 and the 541/573 HC pair.
        ["soic_16", "logic", "parallel_in_serial_out_shift_register", "nexperia", "hef4014bt"],
        ["soic_16", "logic", "parallel_in_serial_out_shift_register", "nexperia", "hef4021bt_653"],
        ["soic_16", "logic", "dual_jk_flip_flop_set_reset", "nexperia", "hef4027bt_653"],
        ["soic_16", "logic", "triple_2_channel_analog_multiplexer_demultiplexer", "nexperia", "hef4053bt_653"],
        ["soic_16", "logic", "14_stage_binary_ripple_counter_oscillator", "nexperia", "hef4060bt_653"],
        ["soic_14", "logic", "quad_bilateral_analog_switch", "nexperia", "hef4066bt_653"],
        ["soic_14", "logic", "hex_inverter_unbuffered", "nexperia", "hef4069ubt_653"],
        ["soic_14", "logic", "quad_2_input_xor_gate", "nexperia", "hef4070bt_653"],
        ["soic_16", "logic", "triple_2_channel_analog_multiplexer_demultiplexer", "texas_instruments", "cd4053bm96"],
        ["soic_20_300mil", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74hc541dwr"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74hc541pwr"],
        ["tssop_20", "logic", "octal_d_type_transparent_latch_tri_state", "texas_instruments", "sn74hc573apwr"],
        # Tranche-84: the TI SN74HC/HCT wave in SOIC/TSSOP, the inverting 240
        # in the 208 mil SO-20 body (soic_20_208mil token new here) and the
        # 244 in SSOP-20-208mil (also new).
        ["tssop_14", "logic", "dual_d_type_flip_flop_set_reset", "texas_instruments", "sn74hc74pwr"],
        ["soic_14", "logic", "dual_d_type_flip_flop_set_reset", "texas_instruments", "sn74hc74dr"],
        ["soic_14", "logic", "quad_2_input_xor_gate", "texas_instruments", "sn74hc86dr"],
        ["soic_14", "logic", "quad_2_input_nand_gate", "texas_instruments", "sn74hct00dr"],
        ["soic_14", "logic", "hex_inverter", "texas_instruments", "sn74hct04dr"],
        ["soic_14", "logic", "quad_2_input_and_gate", "texas_instruments", "sn74hct08dr"],
        ["soic_14", "logic", "hex_schmitt_trigger_inverter", "texas_instruments", "sn74hct14dr"],
        ["soic_16", "logic", "quad_2_to_1_line_multiplexer", "texas_instruments", "sn74hct157dr"],
        ["soic_20_208mil", "logic", "octal_bus_buffer_tri_state_inverting", "texas_instruments", "sn74hct240nsr"],
        ["ssop_20_208mil", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74hct244dbr"],
        ["soic_20_300mil", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74hct244dwr"],
        ["soic_20_208mil", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74hct244nsr"],
        # Tranche-85: the HCT SMD tail plus the first 74LS and 74F rows in
        # the family file.
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74hct244pwr"],
        ["tssop_20", "logic", "octal_bus_transceiver_tri_state", "texas_instruments", "sn74hct245pwr"],
        ["soic_14", "logic", "quad_2_input_or_gate", "texas_instruments", "sn74hct32dr"],
        ["soic_20_300mil", "logic", "octal_d_type_transparent_latch_tri_state", "texas_instruments", "sn74hct573dwr"],
        ["soic_20_300mil", "logic", "octal_d_type_flip_flop_tri_state", "texas_instruments", "sn74hct574dwr"],
        ["soic_14", "logic", "dual_d_type_flip_flop_set_reset", "texas_instruments", "sn74hct74drg4"],
        ["soic_14", "logic", "quad_2_input_nor_gate", "texas_instruments", "sn74ls02dr"],
        ["soic_14", "logic", "hex_inverter", "texas_instruments", "sn74ls04dr"],
        ["soic_14", "logic", "hex_inverter_open_collector", "texas_instruments", "sn74ls05dr"],
        ["soic_14", "logic", "quad_2_input_and_gate", "texas_instruments", "sn74ls08dr"],
        ["soic_20_300mil", "logic", "octal_d_type_transparent_latch_tri_state", "texas_instruments", "sn74f573dwr"],
        ["soic_14", "logic", "dual_d_type_flip_flop_set_reset", "texas_instruments", "sn74f74dr"],
        # Tranche-86: the TI SN74HC core wave; the 04 lands in a 208 mil
        # SO-14 body (soic_14_208mil token new here) beside the 148 priority
        # encoder and the 151 eight-line mux.
        ["tssop_14", "logic", "quad_2_input_nand_gate", "texas_instruments", "sn74hc00pwr"],
        ["tssop_14", "logic", "hex_inverter", "texas_instruments", "sn74hc04pwr"],
        ["soic_14", "logic", "hex_inverter", "texas_instruments", "sn74hc04dr"],
        ["soic_14_208mil", "logic", "hex_inverter", "texas_instruments", "sn74hc04nsr"],
        ["soic_14", "logic", "triple_3_input_nand_gate", "texas_instruments", "sn74hc10dr"],
        ["soic_16", "logic", "3_to_8_line_decoder_demultiplexer", "texas_instruments", "sn74hc138dr"],
        ["soic_16", "logic", "8_to_3_line_priority_encoder", "texas_instruments", "sn74hc148dr"],
        ["soic_14", "logic", "hex_schmitt_trigger_inverter", "texas_instruments", "sn74hc14dr"],
        ["tssop_14", "logic", "hex_schmitt_trigger_inverter", "texas_instruments", "sn74hc14pwr"],
        ["soic_16", "logic", "8_to_1_line_data_selector_multiplexer", "texas_instruments", "sn74hc151dr"],
        ["soic_16", "logic", "quad_2_to_1_line_multiplexer", "texas_instruments", "sn74hc157dr"],
        ["soic_16", "logic", "synchronous_4_bit_binary_counter", "texas_instruments", "sn74hc161dr"],
        # Tranche-87: the HC register group (174/175/273), the dual 4-input
        # NAND, the Q1-automotive 21, the 241/244/365 buffers and the 266
        # open-drain XNOR.
        ["soic_14", "logic", "serial_in_parallel_out_shift_register", "nexperia", "74hc164d_653"],
        ["soic_16", "logic", "hex_d_type_flip_flop_clear", "texas_instruments", "sn74hc174dr"],
        ["soic_16", "logic", "quad_d_type_flip_flop", "texas_instruments", "sn74hc175dr"],
        ["tssop_14", "logic", "dual_4_input_nand_gate", "texas_instruments", "sn74hc20pwr"],
        ["soic_14", "logic", "dual_4_input_and_gate", "texas_instruments", "sn74hc21qdrq1"],
        ["soic_20_300mil", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74hc241dwr"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74hc244pwr"],
        ["soic_14", "logic", "quad_2_input_xnor_gate_open_drain", "texas_instruments", "sn74hc266dr"],
        ["tssop_20", "logic", "octal_d_type_flip_flop_clear", "texas_instruments", "sn74hc273pwr"],
        ["soic_14", "logic", "quad_2_input_or_gate", "texas_instruments", "sn74hc32dr"],
        ["tssop_14", "logic", "quad_2_input_or_gate", "texas_instruments", "sn74hc32pwr"],
        ["soic_16", "logic", "hex_bus_buffer_tri_state", "texas_instruments", "sn74hc365dr"],
        # Tranche-88: the HC373/374 register bodies, the 4040 ripple counter
        # (soic_16_208mil token new here) and the 4066 switch in SSOP-14
        # (ssop_14_208mil also new), plus the MaxLinear RS-232/LDO/supervisor set.
        ["soic_20_300mil", "logic", "octal_d_type_transparent_latch_tri_state", "texas_instruments", "sn74hc373dwr"],
        ["soic_20_300mil", "logic", "octal_d_type_flip_flop_tri_state", "texas_instruments", "sn74hc374dwr"],
        ["soic_20_208mil", "logic", "octal_d_type_flip_flop_tri_state", "texas_instruments", "sn74hc374nsr"],
        ["tssop_20", "logic", "octal_d_type_flip_flop_tri_state", "texas_instruments", "sn74hc374pwr"],
        ["soic_16_208mil", "logic", "12_stage_binary_ripple_counter", "texas_instruments", "sn74hc4040dr"],
        ["ssop_14_208mil", "logic", "quad_bilateral_analog_switch", "texas_instruments", "sn74hc4066dbr"],
        ["ssop_20_208mil", "interface", "rs_232_transceiver", "maxlinear", "sp3223eea_l_tr"],
        ["soic_16", "interface", "rs_232_transceiver", "maxlinear", "sp3232eben_l_tr"],
        ["ssop_28_208mil", "interface", "rs_232_transceiver", "maxlinear", "sp3243eea_l_tr"],
        ["sot_23_5", "power_management", "linear_voltage_regulator_3_3_volt", "maxlinear", "sp6201em5_l_3_3_tr"],
        ["soic_8", "power_management", "processor_supervisor_watchdog", "maxlinear", "sp706sen_l_tr"],
        ["sot_223_3", "power_management", "linear_voltage_regulator_3_3_volt", "maxlinear", "spx1117m3_l_3_3_tr"],
        # Tranche-89: the SPX5205 LDO rail trio plus the adjustable version,
        # ST's 202/232 RS-232 quartet, the SA555 timer (first timer category
        # row), the Vishay optocoupler, the SJA1000 CAN controller and the
        # SN65HVD3082 RS-485 transceiver.
        ["sot_23_5", "power_management", "linear_voltage_regulator_adjustable", "maxlinear", "spx5205m5_l_tr"],
        ["sot_23_5", "power_management", "linear_voltage_regulator_3_3_volt", "maxlinear", "spx5205m5_l_3_3_tr"],
        ["sot_23_5", "power_management", "linear_voltage_regulator_5_volt", "maxlinear", "spx5205m5_l_5_0_tr"],
        ["soic_16", "interface", "rs_232_transceiver", "stmicroelectronics", "st202cdr"],
        ["soic_16", "interface", "rs_232_transceiver", "stmicroelectronics", "st202ecdr"],
        ["soic_16", "interface", "rs_232_transceiver", "stmicroelectronics", "st232cdr"],
        ["soic_16", "interface", "rs_232_transceiver", "stmicroelectronics", "st232ebdr"],
        ["soic_8", "timer", "555_precision_timer", "texas_instruments", "sa555dr"],
        ["sop_4", "optocoupler", "phototransistor_output_optocoupler", "vishay_intertech", "sfh6106_1x001t"],
        ["soic_28", "interface", "can_controller", "nxp_semiconductors", "sja1000t_n1_118"],
        ["soic_8", "interface", "rs_485_transceiver", "texas_instruments", "sn65hvd3082edr"],
        # Tranche-90: the ABT 16-bit buffers (DL SSOP-48-300mil token new
        # here), the ACT TTL-input quartet, the classic bipolar 7406 and the
        # AHC08 AND gate, plus the LVDS32 driver.
        ["soic_16", "interface", "quad_lvds_line_driver", "texas_instruments", "sn65lvds32dr"],
        ["soic_14", "logic", "hex_inverter_open_collector", "texas_instruments", "sn7406dr"],
        ["tssop_48", "logic", "16_bit_bus_buffer_tri_state", "texas_instruments", "sn74abt162244dggr"],
        ["ssop_48_300mil", "logic", "16_bit_bus_buffer_tri_state", "texas_instruments", "sn74abt162244dlrg4"],
        ["soic_20_208mil", "logic", "octal_bus_buffer_tri_state_inverting", "texas_instruments", "sn74abt240ansr"],
        ["soic_14", "logic", "hex_inverter", "texas_instruments", "sn74act04dr"],
        ["soic_20_300mil", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74act244dwr"],
        ["soic_20_208mil", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74act244nsr"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74act244pwr"],
        ["tssop_20", "logic", "octal_bus_transceiver_tri_state", "texas_instruments", "sn74act245pwr"],
        ["soic_14", "logic", "dual_d_type_flip_flop_set_reset", "texas_instruments", "sn74act74dr"],
        ["soic_14", "logic", "quad_2_input_and_gate", "texas_instruments", "sn74ahc08dr"],
        # Tranche-91: the AHC tail, Toshiba single-gate pack, the NXP LIN/CAN
        # transceiver trio and the ST 4558/TL062 dual op-amps.
        ["soic_16", "logic", "dual_retriggerable_monostable_multivibrator", "texas_instruments", "sn74ahc123adr"],
        ["ssop_14_208mil", "logic", "quad_bus_buffer_tri_state", "texas_instruments", "sn74ahc125dbr"],
        ["soic_14", "logic", "quad_bus_buffer_tri_state", "texas_instruments", "sn74ahc125dr"],
        ["soic_16", "logic", "dual_2_to_4_line_decoder_demultiplexer", "texas_instruments", "sn74ahc139dr"],
        ["soic_14", "logic", "hex_schmitt_trigger_inverter", "texas_instruments", "sn74ahc14dr"],
        ["sot_23_5", "logic", "single_or_gate", "toshiba", "tc7s32f"],
        ["sot_23_5", "logic", "single_inverter", "toshiba", "tc7su04f_lf"],
        ["soic_8", "interface", "lin_transceiver", "nxp_semiconductors", "tja1020t_cm_118"],
        ["soic_8", "interface", "can_transceiver", "nxp_semiconductors", "tja1040t_cm_118"],
        ["soic_8", "interface", "can_transceiver", "nxp_semiconductors", "tja1050t_cm_118"],
        ["soic_8", "amplifier", "operational_amplifier_dual", "stmicroelectronics", "tjm4558cdt"],
        ["soic_8", "amplifier", "operational_amplifier_dual_jfet_low_power", "stmicroelectronics", "tl062cdt"],
        # Tranche-92: the TL0xx/TL07x/TL08x JFET op-amp ladder in SOIC bodies
        # and the TL431 shunt regulators (SOIC-8 and SOT-23-3).
        ["soic_8", "amplifier", "operational_amplifier_dual_jfet_low_power", "texas_instruments", "tl062idr"],
        ["soic_14", "amplifier", "operational_amplifier_quad_jfet_low_power", "stmicroelectronics", "tl064acdt"],
        ["soic_14", "amplifier", "operational_amplifier_quad_jfet_low_power", "stmicroelectronics", "tl064cdt"],
        ["soic_14", "amplifier", "operational_amplifier_quad_jfet_low_power", "texas_instruments", "tl064idrg4"],
        ["soic_8", "amplifier", "operational_amplifier_dual_jfet_input", "texas_instruments", "tl072idr"],
        ["soic_14", "amplifier", "operational_amplifier_quad_jfet_input", "stmicroelectronics", "tl074cdt"],
        ["soic_14", "amplifier", "operational_amplifier_quad_jfet_input", "texas_instruments", "tl074idr"],
        ["soic_8", "amplifier", "operational_amplifier_single_jfet_input", "stmicroelectronics", "tl081cdt"],
        ["soic_8", "amplifier", "operational_amplifier_dual_jfet_input", "texas_instruments", "tl082idr"],
        ["soic_8", "power_management", "shunt_regulator", "stmicroelectronics", "tl431acdt"],
        ["soic_8", "power_management", "shunt_regulator", "texas_instruments", "tl431aidr"],
        ["sot_23_3", "power_management", "shunt_regulator", "texas_instruments", "tl431bcdbzr"],
        # Tranche-93: TL431 C/I grades, the TL594 PWM controller, the TL7705
        # supervisor, the TLC LinCMOS op-amp ladder, the CMOS TLC555 timers,
        # the TC7660 charge pump and the Toshiba SOT-353 Schmitt inverter.
        ["soic_8", "power_management", "shunt_regulator", "texas_instruments", "tl431cdr"],
        ["soic_8", "power_management", "shunt_regulator", "stmicroelectronics", "tl431idt"],
        ["soic_16", "power_management", "pwm_controller", "texas_instruments", "tl594cdr"],
        ["soic_8", "power_management", "voltage_supervisor_5_volt", "texas_instruments", "tl7705bidr"],
        ["soic_8", "amplifier", "operational_amplifier_dual_rail_to_rail", "texas_instruments", "tlc2272cdr"],
        ["soic_14", "amplifier", "operational_amplifier_quad_rail_to_rail", "texas_instruments", "tlc2274idr"],
        ["soic_8", "amplifier", "operational_amplifier_dual_low_power", "texas_instruments", "tlc27l2cdr"],
        ["soic_8", "amplifier", "operational_amplifier_dual_cmos", "texas_instruments", "tlc27m2cdr"],
        ["soic_8", "timer", "555_precision_timer", "texas_instruments", "tlc555cdr"],
        ["soic_8", "timer", "555_precision_timer", "texas_instruments", "tlc555idr"],
        ["soic_8", "power_management", "charge_pump_voltage_inverter", "microchip", "tc7660eoa713"],
        ["sot_353_5", "logic", "single_schmitt_trigger_inverter", "toshiba", "tc7s14fu_lf"],
        # Tranche-94: the LVC/LVCR/LVTH 16-bit bodies, the LVCC translating
        # transceiver, the 75176/75189/75451 classic interface drivers.
        ["tssop_24", "logic", "octal_bus_transceiver_tri_state", "texas_instruments", "sn74lvcc4245apwr"],
        ["tssop_48", "logic", "16_bit_bus_transceiver_tri_state", "texas_instruments", "sn74lvch16245adggr"],
        ["ssop_48_300mil", "logic", "16_bit_bus_transceiver_tri_state", "texas_instruments", "sn74lvch16245adlr"],
        ["tssop_20", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74lvch244apwr"],
        ["tssop_48", "logic", "16_bit_registered_bus_transceiver", "texas_instruments", "sn74lvcr162245dggr"],
        ["tssop_14", "logic", "quad_bus_buffer_tri_state", "texas_instruments", "sn74lvth125pwr"],
        ["tssop_48", "logic", "16_bit_bus_buffer_tri_state", "texas_instruments", "sn74lvth162244dggr"],
        ["ssop_48_300mil", "logic", "16_bit_bus_transceiver_tri_state", "texas_instruments", "sn74lvth16245adlr"],
        ["tssop_48", "logic", "16_bit_d_type_transparent_latch_tri_state", "texas_instruments", "sn74lvth16373dggr"],
        ["soic_8", "interface", "rs485_rs422_transceiver", "texas_instruments", "sn75176bdr"],
        ["soic_14", "interface", "quad_rs232_line_receiver", "texas_instruments", "sn75189adr"],
        ["soic_8", "driver", "peripheral_driver", "texas_instruments", "sn75451bdr"],
        # Tranche-95: the 75453 dual driver, SP232 RS-232, the TLP124 opto,
        # TLV431 low-voltage shunt references, the TPIC6B595 power shift
        # register, TPS60110 charge pump, TPS62000/62067 bucks and the
        # TPS763/793 LDO rails (htssop/wson tokens new here).
        ["soic_8", "driver", "dual_peripheral_driver", "texas_instruments", "sn75453bdr"],
        ["soic_16", "interface", "rs_232_transceiver", "maxlinear", "sp232een_l_tr"],
        ["sop_4", "optocoupler", "phototransistor_output_optocoupler", "toshiba", "tlp124_bv_tpl_f"],
        ["soic_8", "power_management", "shunt_regulator", "texas_instruments", "tlv431aidr"],
        ["sot_23_5", "power_management", "shunt_regulator", "texas_instruments", "tlv431bidbvr"],
        ["soic_20_300mil", "logic", "power_logic_octal_shift_register_driver", "texas_instruments", "tpic6b595dwr"],
        ["htssop_20_ep", "power_management", "charge_pump_regulated_converter", "texas_instruments", "tps60110pwpr"],
        ["vssop_10", "power_management", "buck_converter", "texas_instruments", "tps62000dgsr"],
        ["wson_8_ep_2x2", "power_management", "buck_converter", "texas_instruments", "tps62067dsgr"],
        ["sot_23_5", "power_management", "linear_voltage_regulator_1_8_volt", "texas_instruments", "tps76318dbvr"],
        ["sot_23_5", "power_management", "linear_voltage_regulator_3_3_volt", "texas_instruments", "tps76333dbvr"],
        ["sot_23_5", "power_management", "linear_voltage_regulator_1_8_volt", "texas_instruments", "tps79318dbvr"],
        # Tranche-96: TPS793 2.85V/3.0V rails, the ST comparator/timer/op-amp
        # set, the UC28xx/38xx current-mode PWM family, the UC3854 PFC
        # controller and the UCC2802 BiCMOS controller.
        ["sot_23_5", "power_management", "linear_voltage_regulator_2_85_volt", "texas_instruments", "tps793285dbvr"],
        ["sot_23_5", "power_management", "linear_voltage_regulator_3_volt", "texas_instruments", "tps79330dbvr"],
        ["soic_8", "comparator", "dual_differential_comparator", "stmicroelectronics", "ts393idt"],
        ["soic_14", "timer", "555_precision_timer_dual", "stmicroelectronics", "ts556idttr"],
        ["soic_8", "amplifier", "operational_amplifier_dual_rail_to_rail", "stmicroelectronics", "ts912bidt"],
        ["soic_8", "amplifier", "operational_amplifier_single", "stmicroelectronics", "ua741cdt"],
        ["soic_8", "power_management", "current_mode_pwm_controller", "onsemi", "uc2842bd1r2g"],
        ["soic_8", "power_management", "current_mode_pwm_controller", "onsemi", "uc3842bd1r2g"],
        ["soic_8", "power_management", "current_mode_pwm_controller", "onsemi", "uc3844bd1r2g"],
        ["soic_8", "power_management", "current_mode_pwm_controller", "stmicroelectronics", "uc3845bd1013tr"],
        ["soic_16", "power_management", "power_factor_correction_controller", "texas_instruments", "uc3854dwtr"],
        ["soic_8", "power_management", "current_mode_pwm_controller", "texas_instruments", "ucc2802dtr"],
        # Tranche-97: the ALVC/ALVCH/AS 16-bit bodies, the AVCH4T translating
        # transceiver, the CB3Q/CBT FET switch family (new ssop_16_4_4mm and
        # ssop_24_208mil package tokens) and the UCC38C40 PWM controller.
        ["soic_8", "power_management", "current_mode_pwm_controller", "texas_instruments", "ucc38c40dr"],
        ["soic_20_208mil", "logic", "8_bit_identity_comparator", "texas_instruments", "sn74als688nsr"],
        ["tssop_48", "logic", "16_bit_bus_buffer_tri_state", "texas_instruments", "sn74alvc16244adggrg4"],
        ["tssop_48", "logic", "16_bit_bus_transceiver_tri_state", "texas_instruments", "sn74alvc164245dggr"],
        ["tssop_48", "logic", "16_bit_d_type_flip_flop_tri_state", "texas_instruments", "sn74alvch16374dggr"],
        ["soic_20_208mil", "logic", "octal_bus_buffer_tri_state", "texas_instruments", "sn74as244ansr"],
        ["tssop_16", "logic", "4_bit_voltage_translating_transceiver", "texas_instruments", "sn74avch4t245pwr"],
        ["ssop_16_4_4mm", "logic", "quad_2_channel_fet_multiplexer", "texas_instruments", "sn74cb3q3257dbqr"],
        ["soic_20_300mil", "logic", "octal_fet_bus_switch", "texas_instruments", "sn74cbt3244dwr"],
        ["tssop_24", "logic", "10_bit_fet_bus_switch", "texas_instruments", "sn74cbt3384apwrg4"],
        ["ssop_24_208mil", "logic", "10_bit_fet_bus_switch", "texas_instruments", "sn74cbtd3384dbr"],
        ["tssop_24", "logic", "10_bit_fet_bus_switch", "texas_instruments", "sn74cbtd3384pwr"],
        # Tranche-98: the CBTLV low-voltage FET switch and the first 74F
        # standard gates (00/04/157A/21/32) plus the F373 latch.
        ["tssop_20", "logic", "octal_fet_bus_switch", "texas_instruments", "sn74cbtlv3245apwr"],
        ["soic_14", "logic", "quad_2_input_nand_gate", "texas_instruments", "sn74f00dr"],
        ["soic_14", "logic", "hex_inverter", "texas_instruments", "sn74f04dr"],
        ["soic_16", "logic", "quad_2_to_1_line_multiplexer", "texas_instruments", "sn74f157adr"],
        ["soic_14", "logic", "dual_4_input_and_gate", "texas_instruments", "sn74f21dr"],
        ["soic_14", "logic", "quad_2_input_or_gate", "texas_instruments", "sn74f32dr"],
        ["soic_20_300mil", "logic", "octal_d_type_transparent_latch_tri_state", "texas_instruments", "sn74f373dwr"],
        # Tranche-103: the DIP-8 TL072CP and the TLP185 SOP-4 optocoupler.
        ["dip_8", "amplifier", "operational_amplifier_dual_jfet_input", "texas_instruments", "tl072cp"],
        ["sop_4", "optocoupler", "phototransistor_output_optocoupler", "toshiba", "tlp185_gb_tplse"],
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
