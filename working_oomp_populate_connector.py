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

    # Connector footprints found in the expanded unmatched-project report.
    # These are population identities only; exact drawing and manufacturer
    # records are deliberately deferred to the connector research pass.
    unmatched_connectors = [
        {
            "type": "header", "pitch": "1_27_mm_pitch",
            "mounting": "surface_mount", "pins": "10_pin", "style": "socket",
            "part_number": "header_female_5x2_1_27_mm_smd",
            "name_short": "1.27 mm 2x5 SMD Female Header",
        },
        {
            "type": "micro_sd", "style": "push_push",
            "part_number": "micro_sd_external_pin",
            "name_short": "microSD Push-Push Socket",
        },
        {
            "type": "micro_sd", "style": "friction_fit",
            "part_number": "micro_sd_friction_fit",
            "name_short": "microSD Friction-Fit Socket",
        },
        {
            "type": "jst", "pitch": "1_25_mm_pitch", "mounting": "surface_mount",
            "pins": "6_pin", "style": "locking",
            "part_number": "jst_smd_1_25_mm_6_locking",
            "name_short": "JST 1.25 mm 6-Pin Locking Connector",
        },
        {
            "type": "audio_jack", "size": "3_5_mm", "style": "trrs",
            "mounting": "surface_mount_right_angle",
            "part_number": "audio_jack_3_5_mm_trrs",
            "name_short": "3.5 mm TRRS Audio Jack",
        },
        {
            "type": "terminal_block", "pitch": "3_5_mm_pitch",
            "mounting": "through_hole", "pins": "3_pin",
            "part_number": "screw_terminal_1x03_p3_5_mm",
            "name_short": "3.5 mm 3-Pin Screw Terminal",
        },
        {
            "type": "gnss_header", "pitch": "2_mm_pitch",
            "mounting": "surface_mount", "pins": "20_pin",
            "style": "plug_in",
            "part_number": "conn_02x10_gnss_plug_in_header",
            "name_short": "2x10 2.0 mm GNSS Plug-In Header",
        },
        {
            "type": "rf_cable_assembly", "style": "ipx_to_sma",
            "part_number": "ipx_connector_with_sma",
            "name_short": "IPX-to-SMA RF Cable Assembly",
        },
    ]
    for connector in unmatched_connectors:
        option = {
            "taxonomy_2": "connector",
            "taxonomy_3": connector["type"],
        }
        for key, value in connector.items():
            if key in {"type", "name_short"}:
                continue
            option[f"taxonomy_{ {'pitch': 4, 'mounting': 5, 'pins': 6, 'style': 7, 'part_number': 15}.get(key, 8) }"] = value
        option["name_short"] = connector["name_short"]
        options.append(option)

    # JST header families (SH 1.0 mm, PH 2.0 mm, XH 2.5 mm): one part per
    # available pin count, including the SparkFun black Qwiic specials. The
    # editable table with drawings and KiCad matches lives in
    # working_oomp_populate_connector_jst_data.py.
    import working_oomp_populate_connector_jst_data

    for jst_part in working_oomp_populate_connector_jst_data.JST_HEADERS:
        option = {"taxonomy_2": "connector"}
        option.update(jst_part["taxonomy"])
        options.append(option)

    # New connector families (JST PH/XH mountings, 2.54 mm right-angle
    # headers short/long pin, dual-row ICSP header): editable table in
    # working_oomp_populate_connector_families_data.py.
    import working_oomp_populate_connector_families_data

    for family_part in working_oomp_populate_connector_families_data.CONNECTOR_FAMILIES:
        option = {"taxonomy_2": "connector"}
        option.update(family_part["taxonomy"])
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

    # easyC connector: Soldered's 4-pin 1.25 mm side-entry SMD socket
    # (JST GH compatible), used by every easyC breakout.
    options.append({
        "taxonomy_2": "connector", "taxonomy_3": "easyc", "taxonomy_4": "1_25_mm_pitch",
        "taxonomy_5": "surface_mount_right_angle", "taxonomy_6": "4_pin",
        "taxonomy_14": "jst", "taxonomy_15": "sm04b_gh_tf",
        "name_short": "easyC Connector SM04B-GH-TF",
    })
    # RF connectors and terminal blocks seen on GNSS and sensor breakouts.
    options.append({
        "taxonomy_2": "connector", "taxonomy_3": "u_fl", "taxonomy_4": "surface_mount",
        "taxonomy_14": "i_pex", "taxonomy_15": "u_fl_r_smt_1",
        "name_short": "U.FL Receptacle",
    })
    options.append({
        "taxonomy_2": "connector", "taxonomy_3": "sma", "taxonomy_4": "edge_mount",
        "name_short": "SMA Edge Connector",
    })
    options.append({
        "taxonomy_2": "connector", "taxonomy_3": "terminal_block", "taxonomy_4": "5_mm_pitch",
        "taxonomy_5": "through_hole", "taxonomy_6": "2_pin",
        "taxonomy_15": "kf235_5_0_2p",
        "name_short": "Terminal Block KF235-5.0-2P",
    })
    options.append({
        "taxonomy_2": "connector", "taxonomy_3": "coin_cell_holder", "taxonomy_4": "through_hole",
        "taxonomy_5": "cr1220",
        "name_short": "CR1220 Coin Cell Holder",
    })

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
