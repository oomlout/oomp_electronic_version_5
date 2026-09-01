def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_3_pin_socket_kinghelm_kh_2_54fh_1x3p_h8_5"
    if current in extras_dict:
        extras_dict[current]["name_short"] = "Female Socket 3 Pin"
        extras_dict[current]["part_number_manufacturer"] = "KH-2.54FH-1X3P-H8.5"
        extras_dict[current]["part_number_manufacturer_kinghelm"] = "KH-2.54FH-1X3P-H8.5"
        extras_dict[current]["part_number_lcsc"] = "C2932670"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C2932670.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C2932670.pdf"
        extras_dict[current]["manufacturer"] = "Kinghelm"
        extras_dict[current]["connector_dimensions_mm"] = {
            "body_length": 7.62,
            "body_width": 2.5,
            "insulation_height": 8.5,
            "pin_pitch": 2.54,
            "pin_width": 0.64,
            "pin_thickness": 0.4,
            "recommended_hole_diameter": 1.02,
        }
        extras_dict[current]["electrical"] = {
            "current_rating": "3 A",
            "withstand_voltage": "1000 V AC",
            "contact_resistance_maximum": "20 milliohm",
            "operating_temperature": "-40 to +105 C",
        }
        extras_dict[current]["pins"] = {}
        connector_pins = [
            ["1", "pin_1"],
            ["2", "pin_2"],
            ["3", "pin_3"],
        ]
        for pin_index in range(len(connector_pins)):
            pin = connector_pins[pin_index]
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

    current = "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "TYPE-C-31-M-12"
        extras_dict[current]["part_number_lcsc"] = "C165948"
        extras_dict[current]["pins"] = {}
        usb_c_pins = [
            ["A1", "gnd", "power"],
            ["B12", "gnd", "power"],
            ["A4", "vbus", "power"],
            ["B9", "vbus", "power"],
            ["A5", "cc1", "signal"],
            ["B8", "sbu2", "signal"],
            ["A6", "dp1", "signal"],
            ["B7", "dn2", "signal"],
            ["A7", "dn1", "signal"],
            ["B6", "dp2", "signal"],
            ["A8", "sbu1", "signal"],
            ["B5", "cc2", "signal"],
            ["A9", "vbus", "power"],
            ["B4", "vbus", "power"],
            ["A12", "gnd", "power"],
            ["B1", "gnd", "power"],
        ]
        for pin_index in range(len(usb_c_pins)):
            pin = usb_c_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_connector_jst_sh_1_mm_pitch_surface_mount_right_angle_9_pin_jst_sm09b_srss_tb"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "SM09B-SRSS-TB"
        extras_dict[current]["part_number_lcsc"] = "C160408"
        extras_dict[current]["pins"] = {}
        connector_pins = [
            ["1", "pin_1"], ["2", "pin_2"], ["3", "pin_3"],
            ["4", "pin_4"], ["5", "pin_5"], ["6", "pin_6"],
            ["7", "pin_7"], ["8", "pin_8"], ["9", "gnd"],
        ]
        for pin_index in range(len(connector_pins)):
            pin = connector_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0], "name": pin[1], "type": "signal"
            }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_connector_usb_a_surface_mount_4_pin_shenzhen_jing_tuo_jin_electronics_912121a2023s10100"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "912-121A2023S10100"
        extras_dict[current]["part_number_lcsc"] = "C42428"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "vbus",
            "number": "1",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "usb_negative",
            "number": "2",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "usb_positive",
            "number": "3",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "gnd",
            "number": "4",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "shield",
            "number": "5",
            "type": "shield",
        }
        extras_dict[current]["pins"]["pin_6"] = {
            "name": "shield",
            "number": "6",
            "type": "shield",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
