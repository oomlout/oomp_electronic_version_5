def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_ic_esp32_wroom_32e_microcontroller_wifi_bluetooth_8_mb_flash_espressif_esp32_wroom_32e_n8"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Espressif"
        part["part_number_manufacturer"] = "ESP32-WROOM-32E-N8"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["part_number_lcsc"] = "C701342"
        part["product_url"] = "https://www.lcsc.com/product-detail/C701342.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C701342.pdf"
        part["category"] = "mcu"
        part["dimensions_mm"] = {"length": 18.0, "width": 25.5, "height": 3.1}
        part["dimension_reference"] = {"document": "ESP32-WROOM-32E/32UE v1.6", "pages": [3, 10, 11, 12, 25], "notes": "Top view: 0.45x0.9mm castellations on 1.27mm pitch. Exposed underside GND pad is not shown through the shield."}
        names = ["gnd", "3v3", "en", "sensor_vp", "sensor_vn", "io34", "io35", "io32", "io33",
                 "io25", "io26", "io27", "io14", "io12", "gnd", "io13", "nc", "nc", "nc",
                 "nc", "nc", "nc", "io15", "io2", "io0", "io4", "io16", "io17", "io5",
                 "io18", "io19", "nc", "io21", "rxd0", "txd0", "io22", "io23", "gnd", "gnd_ep"]
        part["pins"] = {}
        for index, name in enumerate(names):
            number = str(index + 1)
            pin_type = "signal"
            if name == "nc":
                pin_type = "no_connect"
            if name in ["gnd", "gnd_ep"]:
                pin_type = "gnd"
            if name == "3v3":
                pin_type = "power"
            part["pins"]["pin_" + number] = {"number": number, "name": name, "type": pin_type}
        pads = []
        for index in range(14):
            pads.append([str(index + 1), "left", -8.775, 5.26 - index * 1.27, .45, .9])
            pads.append([str(38 - index), "right", 8.775, 5.26 - index * 1.27, .45, .9])
        for index in range(10):
            pads.append([str(15 + index), "bottom", -5.715 + index * 1.27, -12.525, .9, .45])
        part["package_drawing"] = {
            "overall": [18, 25.5], "body": [18, 25.5], "pins": pads,
            "boxes": [[0, -2.9, 15.8, 17.6], [0, 9.655, 18, 6.19]],
        }
        part["kicad"] = {"symbol": "RF_Module:ESP32-WROOM-32E", "machine_solder": "RF_Module:ESP32-WROOM-32E", "hand_solder": ""}
        part["electrical"] = {"flash": "8 MB", "supply": "3.0 to 3.6 V", "antenna": "PCB"}

    current = "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_3_3_volt_advanced_monolithic_systems_ams1117_3_3"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Advanced Monolithic Systems"
        part["part_number_manufacturer"] = "AMS1117-3.3"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["part_number_lcsc"] = "C6186"
        part["product_url"] = "https://www.lcsc.com/product-detail/C6186.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C6186.pdf"
        part["name_readable_override"] = "Regulator AMS1117-3.3 3.3V SOT-223"
        part["name_short"] = "Regulator AMS1117-3.3"
        part["category"] = "power_management"
        part["dimensions_mm"] = {"length": 6.5, "width": 7.0}
        part["dimension_reference"] = {"document": "AMS1117 datasheet", "pages": [1, 7], "notes": "Nominal SOT-223 dimensions; tab is VOUT, pin 2."}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "gnd", "type": "gnd"},
            "pin_2": {"number": "2", "name": "vout", "type": "power"},
            "pin_3": {"number": "3", "name": "vin", "type": "power"},
        }
        part["package_drawing"] = {
            "overall": [6.5, 7.0], "body": [6.5, 3.5],
            "pins": [["1", "bottom", -2.29, -2.625, .74, 1.75],
                     ["2", "bottom", 0, -2.625, .74, 1.75],
                     ["3", "bottom", 2.29, -2.625, .74, 1.75],
                     ["2", "top", 0, 2.625, 3.05, 1.75]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:AMS1117-3.3", "machine_solder": "Package_TO_SOT_SMD:SOT-223-3_TabPin2", "hand_solder": ""}

    current = "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102_gmr"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Silicon Labs"
        part["part_number_manufacturer"] = "CP2102-GMR"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["name_short"] = "USB Serial CP2102-GMR"
        part["part_number_lcsc"] = "C6568"
        part["product_url"] = "https://www.lcsc.com/product-detail/C6568.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C6568.pdf"
        part["category"] = "interface"
        part["dimensions_mm"] = {"length": 5.0, "width": 5.0}
        part["dimension_reference"] = {"document": "CP2102/9 Rev. 1.8", "pages": [11, 12, 13]}
        part["ic_dimensions_mm"] = {"body_length": 5.0, "body_width": 5.0, "body_height": .9,
                                     "pin_pitch": .5, "pin_width": .23, "pin_length": .55}
        names = ["dcd", "ri", "gnd", "usb_d_plus", "usb_d_minus", "vdd", "regin",
                 "vbus", "reset_n", "nc", "suspend_n", "suspend", "nc", "nc",
                 "nc", "nc", "nc", "nc", "nc", "nc", "nc", "nc",
                 "cts", "rts", "rxd", "txd", "dsr", "dtr", "gnd_ep"]
        part["pins"] = {}
        for index, name in enumerate(names):
            number = str(index + 1)
            part["pins"][f"pin_{number}"] = {"number": number, "name": name, "type": "no_connect" if name == "nc" else "signal"}
        pads = []
        offsets = [1.5, 1.0, .5, 0, -.5, -1.0, -1.5]
        for index, offset in enumerate(offsets):
            pads.append([str(index + 1), "left", -2.225, offset, .55, .23])
            pads.append([str(index + 8), "bottom", -offset, -2.225, .23, .55])
            pads.append([str(index + 15), "right", 2.225, -offset, .55, .23])
            pads.append([str(index + 22), "top", offset, 2.225, .23, .55])
        pads.append(["29", "center", 0, 0, 3.15, 3.15])
        part["package_drawing"] = {"overall": [5, 5], "body": [5, 5], "pins": pads, "pin_one": [-2.1, 2.1]}
        part["kicad"] = {"symbol": "", "machine_solder": "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm", "hand_solder": ""}
        part["research_notes"] = ["This is CP2102, not CP2102N. Easyduino U1 has conflicting symbol/value and LCSC identity; do not auto-match it.",
                                  "Exposed GND pad uses KiCad identifier 29; it is unnumbered in the datasheet.",
                                  "Installed KiCad 10 masters do not contain the original CP2102 symbol. CP2102N is not substituted; symbol selection is pending."]

    current = "electronic_ic_qfn_16_3_mm_x_3_mm_converter_usb_to_serial_converter_wch_ch343p"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "CH343P"
        extras_dict[current]["part_number_lcsc"] = "C2846043"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_0"] = {
            "name": "gnd",
            "number": "0",
            "type": "gnd",
        }
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "vio",
            "number": "1",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "gnd",
            "number": "2",
            "type": "gnd",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "vdd5",
            "number": "3",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "txd",
            "number": "4",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "rxd",
            "number": "5",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_6"] = {
            "name": "v3",
            "number": "6",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_7"] = {
            "name": "ud_positive",
            "number": "7",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_8"] = {
            "name": "ud_negative",
            "number": "8",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_9"] = {
            "name": "vbus",
            "number": "9",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_10"] = {
            "name": "act",
            "number": "10",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_11"] = {
            "name": "dcd",
            "number": "11",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_12"] = {
            "name": "dtr_tnow",
            "number": "12",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_13"] = {
            "name": "rts",
            "number": "13",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_14"] = {
            "name": "dsr",
            "number": "14",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_15"] = {
            "name": "cts",
            "number": "15",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_16"] = {
            "name": "ri",
            "number": "16",
            "type": "signal",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    bus_pirate_parts = [
        {
            "id": "electronic_ic_tssop_16_logic_serial_in_parallel_out_shift_register_wuxi_i_core_elec_aip74hc595ta16_tr",
            "mpn": "AiP74HC595TA16.TR",
            "lcsc": "C5121351",
            "pins": [["1", "qb"], ["2", "qc"], ["3", "qd"], ["4", "qe"], ["5", "qf"], ["6", "qg"], ["7", "qh"], ["8", "gnd"], ["9", "qh_prime"], ["10", "srclr"], ["11", "srclk"], ["12", "rclk"], ["13", "oe"], ["14", "ser"], ["15", "qa"], ["16", "vcc"]],
        },
        {
            "id": "electronic_ic_tssop_20_logic_octal_bus_transceiver_wuxi_i_core_elec_aip74hct245ta20_tr",
            "mpn": "AiP74HCT245TA20.TR",
            "lcsc": "C5354847",
            "pins": [["1", "direction"], ["2", "a0"], ["3", "a1"], ["4", "a2"], ["5", "a3"], ["6", "a4"], ["7", "a5"], ["8", "a6"], ["9", "a7"], ["10", "gnd"], ["11", "b7"], ["12", "b6"], ["13", "b5"], ["14", "b4"], ["15", "b3"], ["16", "b2"], ["17", "b1"], ["18", "b0"], ["19", "ce"], ["20", "vcc"]],
        },
        {
            "id": "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
            "mpn": "AiP74LVC1T45GC363.TR",
            "lcsc": "C5162250",
            "pins": [["1", "vcca"], ["2", "gnd"], ["3", "a"], ["4", "b"], ["5", "direction"], ["6", "vccb"]],
        },
        {
            "id": "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_3_3_volt_diodes_ap2127k_3_3trg1",
            "mpn": "AP2127K-3.3TRG1",
            "lcsc": "C156285",
            "pins": [["1", "vin"], ["2", "gnd"], ["3", "enable"], ["4", "adjust"], ["5", "vout"]],
        },
        {
            "id": "electronic_ic_sot_89_3_power_management_linear_voltage_regulator_3_3_volt_microne_me6211a33pg_n",
            "mpn": "ME6211A33PG-N",
            "lcsc": "C236673",
            "pins": [["1", "gnd"], ["2", "vin"], ["3", "vout"]],
        },
        {
            "id": "electronic_ic_sop_8_5_28_mm_x_5_23_mm_memory_spi_nor_flash_128_mbit_winbond_w25q128jvsiq",
            "mpn": "W25Q128JVSIQ",
            "lcsc": "C97521",
            "pins": [["1", "chip_select"], ["2", "data_out_io1"], ["3", "write_protect_io2"], ["4", "gnd"], ["5", "data_in_io0"], ["6", "clock"], ["7", "hold_io3"], ["8", "vcc"]],
        },
        {
            "id": "electronic_ic_updfn_8_memory_spi_nand_flash_1_gbit_micron_mt29f1g01abafdwb",
            "mpn": "MT29F1G01ABAFDWB",
            "lcsc": "C2905686",
            "pins": [["1", "chip_select"], ["2", "data_out_io1"], ["3", "write_protect_io2"], ["4", "gnd"], ["5", "data_in_io0"], ["6", "clock"], ["7", "hold_io3"], ["8", "vcc"]],
        },
        {
            "id": "electronic_ic_qfn_56_7_mm_x_7_mm_microcontroller_dual_core_arm_cortex_m0_plus_raspberry_pi_rp2040",
            "mpn": "RP2040",
            "lcsc": "C2040",
            "pins": [["1", "iovdd"], ["2", "gpio0"], ["3", "gpio1"], ["4", "gpio2"], ["5", "gpio3"], ["6", "gpio4"], ["7", "gpio5"], ["8", "gpio6"], ["9", "gpio7"], ["10", "iovdd"], ["11", "gpio8"], ["12", "gpio9"], ["13", "gpio10"], ["14", "gpio11"], ["15", "gpio12"], ["16", "gpio13"], ["17", "gpio14"], ["18", "gpio15"], ["19", "testen"], ["20", "xin"], ["21", "xout"], ["22", "iovdd"], ["23", "dvdd"], ["24", "swclk"], ["25", "swd"], ["26", "run"], ["27", "gpio16"], ["28", "gpio17"], ["29", "gpio18"], ["30", "gpio19"], ["31", "gpio20"], ["32", "gpio21"], ["33", "iovdd"], ["34", "gpio22"], ["35", "gpio23"], ["36", "gpio24"], ["37", "gpio25"], ["38", "gpio26_adc0"], ["39", "gpio27_adc1"], ["40", "gpio28_adc2"], ["41", "gpio29_adc3"], ["42", "iovdd"], ["43", "adc_avdd"], ["44", "vreg_in"], ["45", "vreg_vout"], ["46", "usb_dm"], ["47", "usb_dp"], ["48", "usb_vdd"], ["49", "iovdd"], ["50", "dvdd"], ["51", "qspi_sd3"], ["52", "qspi_sclk"], ["53", "qspi_sd0"], ["54", "qspi_sd2"], ["55", "qspi_sd1"], ["56", "qspi_ss"], ["57", "gnd"]],
        },
        {
            "id": "electronic_ic_tssop_24_logic_16_channel_analog_multiplexer_nexperia_74hct4067pw118",
            "mpn": "74HCT4067PW,118",
            "lcsc": "",
            "pins": [["1", "common"], ["2", "channel_7"], ["3", "channel_6"], ["4", "channel_5"], ["5", "channel_4"], ["6", "channel_3"], ["7", "channel_2"], ["8", "channel_1"], ["9", "channel_0"], ["10", "select_0"], ["11", "select_1"], ["12", "gnd"], ["13", "select_3"], ["14", "select_2"], ["15", "enable"], ["16", "channel_15"], ["17", "channel_14"], ["18", "channel_13"], ["19", "channel_12"], ["20", "channel_11"], ["21", "channel_10"], ["22", "channel_9"], ["23", "channel_8"], ["24", "vcc"]],
        },
    ]
    for bus_pirate_part in bus_pirate_parts:
        current = bus_pirate_part["id"]
        if current not in extras_dict:
            continue
        extras_dict[current]["part_number_manufacturer"] = bus_pirate_part["mpn"]
        if bus_pirate_part["lcsc"] != "":
            extras_dict[current]["part_number_lcsc"] = bus_pirate_part["lcsc"]
        extras_dict[current]["pins"] = {}
        for pin_index in range(len(bus_pirate_part["pins"])):
            pin = bus_pirate_part["pins"][pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": "signal",
            }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_sot_23_5_amplifier_operational_single_rail_to_rail_input_output_gainsil_lmv321_tr"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "LMV321-TR"
        extras_dict[current]["part_number_manufacturer_gainsil"] = "LMV321-TR"
        extras_dict[current]["part_number_lcsc"] = "C362273"
        extras_dict[current]["manufacturer"] = "Gainsil"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C362273.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C362273.pdf"
        extras_dict[current]["package_name_manufacturer"] = "SOT23-5"
        extras_dict[current]["marking_code"] = "321"
        extras_dict[current]["name_short"] = "IC LMV321-TR SOT-23-5 Single Rail To Rail Input Output Op Amp"
        extras_dict[current]["electrical"] = {
            "amplifier_count": 1,
            "input_output_style": "rail-to-rail input and output",
            "minimum_supply_voltage": "2.1 V",
            "maximum_supply_voltage": "5.5 V",
            "typical_gain_bandwidth_product": "1 MHz",
            "typical_slew_rate": "0.6 V/us",
            "typical_quiescent_current_per_amplifier": "40 uA",
            "maximum_input_offset_voltage": "3.5 mV",
            "typical_input_bias_current": "1 pA",
            "operating_temperature": "-40 to +125 C",
            "input_filter": "embedded RF anti-EMI filter",
        }
        extras_dict[current]["ic_dimensions_mm"] = {
            "body_length": 2.92,
            "body_length_min": 2.82,
            "body_length_max": 3.02,
            "body_width": 1.6,
            "body_width_min": 1.5,
            "body_width_max": 1.7,
            "overall_width": 2.8,
            "overall_width_min": 2.65,
            "overall_width_max": 2.95,
            "body_height": 1.15,
            "body_height_min": 1.05,
            "body_height_max": 1.25,
            "pin_pitch": 0.95,
            "pin_width": 0.4,
            "pin_width_min": 0.3,
            "pin_width_max": 0.5,
            "pin_length": 0.45,
            "pin_length_min": 0.3,
            "pin_length_max": 0.6,
        }
        extras_dict[current]["package_dimensions_manufacturer_mm"] = {
            "A_minimum": 1.05,
            "A_maximum": 1.25,
            "A1_minimum": 0.0,
            "A1_maximum": 0.1,
            "A2_minimum": 1.05,
            "A2_maximum": 1.15,
            "b_minimum": 0.3,
            "b_maximum": 0.5,
            "c_minimum": 0.1,
            "c_maximum": 0.2,
            "D_minimum": 2.82,
            "D_maximum": 3.02,
            "E_minimum": 1.5,
            "E_maximum": 1.7,
            "E1_minimum": 2.65,
            "E1_maximum": 2.95,
            "e_basic": 0.95,
            "e1_basic": 1.9,
            "L_minimum": 0.3,
            "L_maximum": 0.6,
            "theta_minimum_degrees": 0,
            "theta_maximum_degrees": 8,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 2.92,
            "width": 2.8,
        }
        extras_dict[current]["pins"] = {}
        amplifier_pins = [
            ["1", "in_positive", "input"],
            ["2", "vss", "power"],
            ["3", "in_negative", "input"],
            ["4", "output", "output"],
            ["5", "vdd", "power"],
        ]
        for pin_index in range(len(amplifier_pins)):
            pin = amplifier_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate analogue component page identifies U404, U506 and U603 as Gainsil LMV321 devices in SOT-23-5.",
            "The exact supplier listing resolves to Gainsil LMV321-TR, LCSC C362273.",
            "The Gainsil datasheet confirms the five-pin assignment, rail-to-rail input and output, 2.1 V to 5.5 V supply range and package dimensions.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_sot_23_5_amplifier_operational_single_precision_rail_to_rail_input_output_gainsil_gs321a_tr"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "GS321A-TR"
        extras_dict[current]["part_number_manufacturer_gainsil"] = "GS321A-TR"
        extras_dict[current]["part_number_lcsc"] = "C431318"
        extras_dict[current]["manufacturer"] = "Gainsil"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C431318.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C431318.pdf"
        extras_dict[current]["package_name_manufacturer"] = "SOT23-5"
        extras_dict[current]["marking_code"] = "321"
        extras_dict[current]["name_short"] = "IC GS321A-TR SOT-23-5 Precision Rail To Rail Input Output Op Amp"
        extras_dict[current]["electrical"] = {
            "amplifier_count": 1,
            "input_output_style": "rail-to-rail input and output",
            "minimum_supply_voltage": "2.1 V",
            "maximum_supply_voltage": "5.5 V",
            "typical_gain_bandwidth_product": "1 MHz",
            "typical_slew_rate": "0.6 V/us",
            "typical_quiescent_current_per_amplifier": "40 uA",
            "maximum_input_offset_voltage": "0.4 mV",
            "typical_input_bias_current": "1 pA",
            "operating_temperature": "-40 to +125 C",
            "input_filter": "embedded RF anti-EMI filter",
        }
        extras_dict[current]["ic_dimensions_mm"] = {
            "body_length": 2.92,
            "body_length_min": 2.82,
            "body_length_max": 3.02,
            "body_width": 1.6,
            "body_width_min": 1.5,
            "body_width_max": 1.7,
            "overall_width": 2.8,
            "overall_width_min": 2.65,
            "overall_width_max": 2.95,
            "body_height": 1.15,
            "body_height_min": 1.05,
            "body_height_max": 1.25,
            "pin_pitch": 0.95,
            "pin_width": 0.4,
            "pin_width_min": 0.3,
            "pin_width_max": 0.5,
            "pin_length": 0.45,
            "pin_length_min": 0.3,
            "pin_length_max": 0.6,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 2.92,
            "width": 2.8,
        }
        extras_dict[current]["pins"] = {}
        amplifier_pins = [
            ["1", "in_positive", "input"],
            ["2", "vss", "power"],
            ["3", "in_negative", "input"],
            ["4", "output", "output"],
            ["5", "vdd", "power"],
        ]
        for pin_index in range(len(amplifier_pins)):
            pin = amplifier_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate analogue page calls for an A-grade LMV321-class device at U601 and links Gainsil GS321A as an example.",
            "The exact active supplier listing resolves to Gainsil GS321A-TR, LCSC C431318.",
            "The Gainsil datasheet confirms 0.4 mV maximum input offset voltage, rail-to-rail input and output, the five-pin assignment and package dimensions.",
            "The discontinued Onsemi LMV321AS5X example was not selected because its listed offset specification does not meet the project's stated A-grade target.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_sot_23_5_comparator_single_open_collector_texas_instruments_lmv331idbvr"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "LMV331IDBVR"
        extras_dict[current]["part_number_manufacturer_texas_instruments"] = "LMV331IDBVR"
        extras_dict[current]["part_number_lcsc"] = "C34731"
        extras_dict[current]["manufacturer"] = "Texas Instruments"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C34731.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C34731.pdf"
        extras_dict[current]["package_name_manufacturer"] = "DBV SOT-23-5"
        extras_dict[current]["name_short"] = "IC LMV331IDBVR SOT-23-5 Single Open Collector Comparator"
        extras_dict[current]["electrical"] = {
            "comparator_count": 1,
            "output_style": "open collector",
            "input_common_mode": "includes ground",
            "minimum_supply_voltage": "2.7 V",
            "maximum_supply_voltage": "5.5 V",
            "maximum_input_offset_voltage": "7 mV",
            "typical_input_bias_current": "250 nA",
            "typical_supply_current": "40 uA",
            "typical_output_saturation_voltage": "200 mV",
            "minimum_output_sink_current_at_5_v": "10 mA",
            "typical_high_to_low_propagation_delay_at_5_v": "600 ns",
            "typical_low_to_high_propagation_delay_at_5_v": "450 ns",
            "operating_temperature": "-40 to +125 C",
        }
        extras_dict[current]["ic_dimensions_mm"] = {
            "body_length": 2.9,
            "body_length_min": 2.75,
            "body_length_max": 3.05,
            "body_width": 1.6,
            "body_width_min": 1.45,
            "body_width_max": 1.75,
            "overall_width": 2.8,
            "overall_width_min": 2.6,
            "overall_width_max": 3.0,
            "body_height_max": 1.45,
            "pin_pitch": 0.95,
            "pin_width": 0.4,
            "pin_width_min": 0.3,
            "pin_width_max": 0.5,
            "pin_length": 0.45,
            "pin_length_min": 0.3,
            "pin_length_max": 0.6,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 2.9,
            "width": 2.8,
        }
        extras_dict[current]["pins"] = {}
        comparator_pins = [
            ["1", "in_positive", "input"],
            ["2", "gnd", "power"],
            ["3", "in_negative", "input"],
            ["4", "output", "open_collector_output"],
            ["5", "vcc", "power"],
        ]
        for pin_index in range(len(comparator_pins)):
            pin = comparator_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate analogue page identifies U602 as an LMV331 comparator in SOT-23-5 and links this exact TI example.",
            "The supplier listing resolves to Texas Instruments LMV331IDBVR, LCSC C34731.",
            "The TI datasheet confirms the open-collector output, 2.7 V to 5.5 V supply range, five-pin assignment and DBV package dimensions.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_tssop_14_amplifier_operational_quad_rail_to_rail_output_texas_instruments_lmv324ipwr"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "LMV324IPWR"
        extras_dict[current]["part_number_manufacturer_texas_instruments"] = "LMV324IPWR"
        extras_dict[current]["part_number_lcsc"] = "C398929"
        extras_dict[current]["manufacturer"] = "Texas Instruments"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C398929.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C398929.pdf"
        extras_dict[current]["package_name_manufacturer"] = "PW TSSOP-14"
        extras_dict[current]["package_drawing_url"] = "https://www.ti.com/lit/pdf/mpds360a"
        extras_dict[current]["marking_code"] = "MV324I"
        extras_dict[current]["name_short"] = "IC LMV324IPWR TSSOP-14 Quad Rail To Rail Output Op Amp"
        extras_dict[current]["electrical"] = {
            "amplifier_count": 4,
            "output_style": "rail-to-rail output",
            "minimum_supply_voltage": "2.7 V",
            "maximum_supply_voltage": "5.5 V",
            "typical_gain_bandwidth_product": "1 MHz",
            "typical_slew_rate": "1 V/us",
            "typical_total_quiescent_current": "410 uA",
            "maximum_input_offset_voltage": "7 mV",
            "typical_input_bias_current": "250 nA",
            "typical_output_current": "60 mA",
            "operating_temperature": "-40 to +125 C",
        }
        extras_dict[current]["ic_dimensions_mm"] = {
            "body_length": 5.0,
            "body_length_min": 4.9,
            "body_length_max": 5.1,
            "body_width": 4.4,
            "body_width_min": 4.3,
            "body_width_max": 4.5,
            "overall_width": 6.4,
            "overall_width_min": 6.2,
            "overall_width_max": 6.6,
            "body_height_max": 1.2,
            "pin_pitch": 0.65,
            "pin_width": 0.235,
            "pin_width_min": 0.17,
            "pin_width_max": 0.3,
            "pin_length": 0.625,
            "pin_length_min": 0.5,
            "pin_length_max": 0.75,
            "lead_thickness": 0.1,
            "lead_thickness_min": 0.05,
            "lead_thickness_max": 0.15,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 5.0,
            "width": 6.4,
        }
        extras_dict[current]["pins"] = {}
        amplifier_pins = [
            ["1", "1out", "output"],
            ["2", "1in-", "input"],
            ["3", "1in+", "input"],
            ["4", "vcc+", "power"],
            ["5", "2in+", "input"],
            ["6", "2in-", "input"],
            ["7", "2out", "output"],
            ["8", "3out", "output"],
            ["9", "3in-", "input"],
            ["10", "3in+", "input"],
            ["11", "gnd", "power"],
            ["12", "4in+", "input"],
            ["13", "4in-", "input"],
            ["14", "4out", "output"],
        ]
        for pin_index in range(len(amplifier_pins)):
            pin = amplifier_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate analogue component page identifies U504 and U505 as LMV324 devices in TSSOP-14 and links this TI orderable example.",
            "The exact supplier page resolves to Texas Instruments LMV324IPWR, LCSC C398929.",
            "The TI datasheet confirms this variant is a quad 2.7 V to 5.5 V operational amplifier with rail-to-rail output and the complete fourteen-pin assignment.",
            "The official TI PW0014A package drawing supplies the dimensions used by the physical diagrams.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_sop_16_controller_usb_hub_controller_4_port_corechips_sl21a"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "SL2.1A"
        extras_dict[current]["part_number_lcsc"] = "C192893"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "dm4",
            "number": "1",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "dp4",
            "number": "2",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "dm3",
            "number": "3",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "dp3",
            "number": "4",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "dm2",
            "number": "5",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_6"] = {
            "name": "dp2",
            "number": "6",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_7"] = {
            "name": "dm1",
            "number": "7",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_8"] = {
            "name": "dp1",
            "number": "8",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_9"] = {
            "name": "udm",
            "number": "9",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_10"] = {
            "name": "udp",
            "number": "10",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_11"] = {
            "name": "vcc5",
            "number": "11",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_12"] = {
            "name": "vss",
            "number": "12",
            "type": "gnd",
        }
        extras_dict[current]["pins"]["pin_13"] = {
            "name": "vdd33",
            "number": "13",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_14"] = {
            "name": "vdd18",
            "number": "14",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_15"] = {
            "name": "xout",
            "number": "15",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_16"] = {
            "name": "xin",
            "number": "16",
            "type": "signal",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_sot_23_6_logic_configurable_multi_function_gate_texas_instruments_sn74lvc1g57dbvr"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "SN74LVC1G57DBVR"
        extras_dict[current]["part_number_lcsc"] = "C485080"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "in1",
            "number": "1",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "gnd",
            "number": "2",
            "type": "gnd",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "in0",
            "number": "3",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "y",
            "number": "4",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "vcc",
            "number": "5",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_6"] = {
            "name": "in2",
            "number": "6",
            "type": "signal",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_tsot_23_5_power_management_high_side_power_switch_with_flag_richtek_rt9742cgj5"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "RT9742CGJ5"
        extras_dict[current]["part_number_lcsc"] = "C250546"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "vout",
            "number": "1",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "gnd",
            "number": "2",
            "type": "gnd",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "flg",
            "number": "3",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "en",
            "number": "4",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "vin",
            "number": "5",
            "type": "power",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
