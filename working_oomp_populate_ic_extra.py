def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

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
