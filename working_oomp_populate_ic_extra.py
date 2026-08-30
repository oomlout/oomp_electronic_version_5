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
