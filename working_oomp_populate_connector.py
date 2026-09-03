def main(**kwargs):
    options = kwargs.get("options", [])
    options.append({
        "taxonomy_2": "connector", "taxonomy_3": "usb_c", "taxonomy_4": "surface_mount",
        "taxonomy_5": "16_pin", "taxonomy_14": "shou_han", "taxonomy_15": "type_c_16pin_2md_073",
        "name_short": "USB-C TYPE-C 16PIN 2MD(073)",
    })

    connector_types = ["usb_c"]
    mounting_types = ["surface_mount"]
    pin_counts = ["16_pin"]
    manufacturers = ["korean_hroparts_elec"]
    part_numbers = ["typec31m12"]

    for connector_type in connector_types:
        for mounting_type in mounting_types:
            for pin_count in pin_counts:
                for manufacturer in manufacturers:
                    for part_number in part_numbers:
                        option = {}
                        option["taxonomy_2"] = "connector"
                        option["taxonomy_3"] = connector_type
                        option["taxonomy_4"] = mounting_type
                        option["taxonomy_5"] = pin_count
                        option["taxonomy_14"] = manufacturer
                        option["taxonomy_15"] = part_number
                        options.append(option)

    # Compact JST-SH connector used for the Bus Pirate buffered I/O header.
    connectors = [
        {
            "type": "jst_sh",
            "pitch": "1_mm_pitch",
            "mounting": "surface_mount_right_angle",
            "pins": "9_pin",
            "manufacturer": "jst",
            "part_number": "sm09b_srss_tb",
        },
    ]
    for connector in connectors:
        option = {}
        option["taxonomy_2"] = "connector"
        option["taxonomy_3"] = connector["type"]
        option["taxonomy_4"] = connector["pitch"]
        option["taxonomy_5"] = connector["mounting"]
        option["taxonomy_6"] = connector["pins"]
        option["taxonomy_14"] = connector["manufacturer"]
        option["taxonomy_15"] = connector["part_number"]
        options.append(option)

    connector_types = ["header"]
    pitches = ["2_54_mm_pitch"]
    mounting_types = ["through_hole"]
    pin_counts = [
        "1_pin",
        "2_pin",
        "3_pin",
        "4_pin",
        "5_pin",
        "6_pin",
        "7_pin",
        "8_pin",
        "9_pin",
        "10_pin",
        "11_pin",
        "12_pin",
        "13_pin",
        "14_pin",
        "15_pin",
        "16_pin",
        "17_pin",
        "18_pin",
        "19_pin",
        "20_pin",
        "21_pin",
        "22_pin",
        "23_pin",
        "24_pin",
        "25_pin",
        "26_pin",
        "27_pin",
        "28_pin",
        "29_pin",
        "30_pin",
        "31_pin",
        "32_pin",
        "33_pin",
        "34_pin",
        "35_pin",
        "36_pin",
        "37_pin",
        "38_pin",
        "39_pin",
        "40_pin",
    ]

    for connector_type in connector_types:
        for pitch in pitches:
            for mounting_type in mounting_types:
                for pin_count in pin_counts:
                    option = {}
                    option["taxonomy_2"] = "connector"
                    option["taxonomy_3"] = connector_type
                    option["taxonomy_4"] = pitch
                    option["taxonomy_5"] = mounting_type
                    option["taxonomy_6"] = pin_count
                    options.append(option)

    # Exact vertical female socket used as the purchasable match for the
    # Bus Pirate J201 generic 1x3 KiCad socket footprint.
    sockets = [
        {
            "type": "header",
            "pitch": "2_54_mm_pitch",
            "mounting": "through_hole",
            "pins": "3_pin",
            "style": "socket",
            "manufacturer": "kinghelm",
            "part_number": "kh_2_54fh_1x3p_h8_5",
        },
    ]
    for socket in sockets:
        option = {}
        option["taxonomy_2"] = "connector"
        option["taxonomy_3"] = socket["type"]
        option["taxonomy_4"] = socket["pitch"]
        option["taxonomy_5"] = socket["mounting"]
        option["taxonomy_6"] = socket["pins"]
        option["taxonomy_7"] = socket["style"]
        option["taxonomy_14"] = socket["manufacturer"]
        option["taxonomy_15"] = socket["part_number"]
        options.append(option)

    connector_types = ["usb_a"]
    mounting_types = ["surface_mount"]
    pin_counts = ["4_pin"]
    manufacturers = ["shenzhen_jing_tuo_jin_electronics"]
    part_numbers = ["912121a2023s10100"]

    for connector_type in connector_types:
        for mounting_type in mounting_types:
            for pin_count in pin_counts:
                for manufacturer in manufacturers:
                    for part_number in part_numbers:
                        option = {}
                        option["taxonomy_2"] = "connector"
                        option["taxonomy_3"] = connector_type
                        option["taxonomy_4"] = mounting_type
                        option["taxonomy_5"] = pin_count
                        option["taxonomy_14"] = manufacturer
                        option["taxonomy_15"] = part_number
                        options.append(option)


if __name__ == "__main__":
    main()
