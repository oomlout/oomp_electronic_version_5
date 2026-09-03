def main(**kwargs):
    options = kwargs.get("options", [])
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
        "taxonomy_2": "ic", "taxonomy_3": "qfn_28_5_mm_x_5_mm",
        "taxonomy_4": "converter", "taxonomy_5": "usb_to_serial_converter",
        "taxonomy_14": "silicon_labs", "taxonomy_15": "cp2102_gmr",
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
