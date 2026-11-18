def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})
    current = "electronic_switch_tactile_surface_mount_xunpu_ts_1088_ar02016"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XUNPU"
        part["part_number_manufacturer"] = "TS-1088-AR02016"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["part_number_lcsc"] = "C720477"
        part["product_url"] = "https://www.lcsc.com/product-detail/C720477.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C720477.pdf"
        part["category"] = "switch"
        part["dimensions_mm"] = {"length": 4.8, "width": 3.0, "height": 2.0}
        part["dimension_reference"] = {"document": "XUNPU TS-1088", "pages": [1], "notes": "4x3 body, 4.8mm terminal span, 1.3mm terminal width; AR02016 is 2mm high, 1.6N."}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "contact_1", "type": "passive"},
            "pin_2": {"number": "2", "name": "contact_2", "type": "passive"},
        }
        part["package_drawing"] = {
            "overall": [4.8, 3], "body": [4, 3],
            "pins": [["1", "left", -2.2, 0, .4, 1.3], ["2", "right", 2.2, 0, .4, 1.3]],
            "circles": [[0, 0, .85]],
        }
        part["kicad"] = {"symbol": "Switch:SW_Push", "machine_solder": "", "hand_solder": "", "allow_project_fallback": False}
        part["research_notes"] = ["Nonpolar contacts numbered 1/2 using schematic convention. No exact XUNPU master footprint verified; the upstream Alps_SKRK footprint is retained, not certified interchangeable."]

    # Generic match for SW_Push tactile switches used in Easyduino and SparkFun projects
    current = "electronic_switch_tactile_surface_mount_xunpu_ts_1088_ar02016"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_match"] = {
            "values": ["SW_Push", "SW_SPST", "SW_Tactile"],
            "symbols": ["Switch:SW_Push", "Switch:SW_SPST"],
            "footprints": [
                "Button_Switch_SMD:SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS",
                "Button_Switch_SMD:SW_Push_SPST_NO_Alps_SKRK",
                "Bluepill_Library:ALPSALPINE_SKRPACE010",
                "RP2040:ALPSALPINE_SKRPACE010",
            ],
        }

    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="switch")

    # === BEGIN generated switch batch (tmp/switch_batch.py) — regenerated, do not hand-edit ===
    # JLC C318884 / XKB Connection TS-1187A-B-A-B - switch family batch 2026-10-06
    current = "electronic_switch_tactile_surface_mount_xkb_connection_ts_1187a_b_a_b"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TS-1187A-B-A-B SMD tactile switch, 5.1 x 5.1 x 1.5 mm, 4 bridged pads (1-1 / 2-2)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8550724022091735040-C318884.pdf"
        part["dimensions_mm"] = {"length": 6.0, "width": 5.1, "height": 1.5}
        part["dimension_reference"] = {
            "document": "TS-1187A-B-A-B datasheet (C318884 provenance)",
            "pages": [1],
            "notes": "TS-1187A-B-A-B SMD tactile switch, 5.1 x 5.1 x 1.5 mm, 4 bridged pads (1-1 / 2-2).",
        }
        part["electrical"] = {
            "circuit": "SPST",
            "current_rating": "50mA",
            "voltage_rating": "12V",
            "operating_force": "1.6N",
            "positions": 1,
            "actuator": "Round Button",
            "operating_temperature": "-30 C~+85 C",
            "device_type": "tactile push switch"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Switch:SW_Push",
            "machine_solder": "Button_Switch_SMD:SW_Push_1P1T_XKB_TS-1187A",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists XKB Connection TS-1187A-B-A-B (C318884); identity and ratings observed live at intake 2026-09-25.",
            "Mapped to the KiCad Switch:SW_Push master and the Button_Switch_SMD:SW_Push_1P1T_XKB_TS-1187A footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C4674 / Cixi Tonver Elec HAM-05HWA-R - switch family batch 2026-10-06
    current = "electronic_switch_dip_switch_through_hole_spst_5_position_raised_actuator_cixi_tonver_ham_05hwa_r"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "5-pos SPST slide DIP switch, THT 2.54 mm, 9.78 x 14.88 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887124779143168-C4674.pdf"
        part["dimensions_mm"] = {"length": 9.78, "width": 14.88, "height": 5.6}
        part["dimension_reference"] = {
            "document": "HAM-05HWA-R datasheet (C4674 provenance)",
            "pages": [1],
            "notes": "5-pos SPST slide DIP switch, THT 2.54 mm, 9.78 x 14.88 mm body.",
        }
        part["electrical"] = {
            "circuit": "SPST",
            "current_rating": "25mA",
            "voltage_rating": "24V",
            "positions": "05",
            "actuator": "2.54mm 24V 25mA 5 Black SPST Slide, Rocked 插件,P=2.54mm DIP Switches ROHS",
            "operating_temperature": "-30 to +85 C",
            "device_type": "slide DIP switch"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
            "pin_3": {"number": "3", "name": "3", "type": "passive"},
            "pin_4": {"number": "4", "name": "4", "type": "passive"},
            "pin_5": {"number": "5", "name": "5", "type": "passive"},
            "pin_6": {"number": "6", "name": "6", "type": "passive"},
            "pin_7": {"number": "7", "name": "7", "type": "passive"},
            "pin_8": {"number": "8", "name": "8", "type": "passive"},
            "pin_9": {"number": "9", "name": "9", "type": "passive"},
            "pin_10": {"number": "10", "name": "10", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Switch:SW_DIP_x05",
            "machine_solder": "Button_Switch_THT:SW_DIP_SPSTx05_Slide_9.78x14.88mm_W7.62mm_P2.54mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Cixi Tonver Elec HAM-05HWA-R (C4674); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Switch:SW_DIP_x05 master and the Button_Switch_THT:SW_DIP_SPSTx05_Slide_9.78x14.88mm_W7.62mm_P2.54mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C4681 / Cixi Tonver Elec YAM-09HWAG - switch family batch 2026-10-06
    current = "electronic_switch_dip_switch_through_hole_spst_9_position_raised_actuator_cixi_tonver_yam_09hwag"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "9-pos SPST slide DIP switch, THT 2.54 mm, 9.78 x 25.04 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588894937223450624-C4681.pdf"
        part["dimensions_mm"] = {"length": 9.78, "width": 25.04, "height": 5.6}
        part["dimension_reference"] = {
            "document": "YAM-09HWAG datasheet (C4681 provenance)",
            "pages": [1],
            "notes": "9-pos SPST slide DIP switch, THT 2.54 mm, 9.78 x 25.04 mm body.",
        }
        part["electrical"] = {
            "circuit": "SPST",
            "current_rating": "25mA",
            "voltage_rating": "24V",
            "positions": "09",
            "actuator": "2,000 cycles 2.54mm 24V 25mA 9 Black SPST Slide, Rocked 插件,P=2.54mm DIP Switches ROHS",
            "operating_temperature": "-30 to +85 C",
            "device_type": "slide DIP switch"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
            "pin_3": {"number": "3", "name": "3", "type": "passive"},
            "pin_4": {"number": "4", "name": "4", "type": "passive"},
            "pin_5": {"number": "5", "name": "5", "type": "passive"},
            "pin_6": {"number": "6", "name": "6", "type": "passive"},
            "pin_7": {"number": "7", "name": "7", "type": "passive"},
            "pin_8": {"number": "8", "name": "8", "type": "passive"},
            "pin_9": {"number": "9", "name": "9", "type": "passive"},
            "pin_10": {"number": "10", "name": "10", "type": "passive"},
            "pin_11": {"number": "11", "name": "11", "type": "passive"},
            "pin_12": {"number": "12", "name": "12", "type": "passive"},
            "pin_13": {"number": "13", "name": "13", "type": "passive"},
            "pin_14": {"number": "14", "name": "14", "type": "passive"},
            "pin_15": {"number": "15", "name": "15", "type": "passive"},
            "pin_16": {"number": "16", "name": "16", "type": "passive"},
            "pin_17": {"number": "17", "name": "17", "type": "passive"},
            "pin_18": {"number": "18", "name": "18", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Switch:SW_DIP_x09",
            "machine_solder": "Button_Switch_THT:SW_DIP_SPSTx09_Slide_9.78x25.04mm_W7.62mm_P2.54mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Cixi Tonver Elec YAM-09HWAG (C4681); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Switch:SW_DIP_x09 master and the Button_Switch_THT:SW_DIP_SPSTx09_Slide_9.78x25.04mm_W7.62mm_P2.54mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C4682 / Cixi Tonver Elec HAD-08HWAG-R - switch family batch 2026-10-06
    current = "electronic_switch_dip_switch_surface_mount_spst_8_position_raised_actuator_cixi_tonver_had_08hwag_r"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "8-pos SPST slide DIP switch, SMD 2.54 mm raised actuator, 9.78 x 22.5 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588934135590739968-C4682.pdf"
        part["dimensions_mm"] = {"length": 9.78, "width": 22.5, "height": 5.6}
        part["dimension_reference"] = {
            "document": "HAD-08HWAG-R datasheet (C4682 provenance)",
            "pages": [1],
            "notes": "8-pos SPST slide DIP switch, SMD 2.54 mm raised actuator, 9.78 x 22.5 mm body.",
        }
        part["electrical"] = {
            "circuit": "SPST",
            "current_rating": "25mA",
            "voltage_rating": "24V",
            "positions": "08",
            "actuator": "2.54mm 24V 25mA 8 Black SPST Slide, Rocked SMD,P=2.54mm DIP Switches ROHS",
            "operating_temperature": "-30 to +85 C",
            "device_type": "slide DIP switch"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
            "pin_3": {"number": "3", "name": "3", "type": "passive"},
            "pin_4": {"number": "4", "name": "4", "type": "passive"},
            "pin_5": {"number": "5", "name": "5", "type": "passive"},
            "pin_6": {"number": "6", "name": "6", "type": "passive"},
            "pin_7": {"number": "7", "name": "7", "type": "passive"},
            "pin_8": {"number": "8", "name": "8", "type": "passive"},
            "pin_9": {"number": "9", "name": "9", "type": "passive"},
            "pin_10": {"number": "10", "name": "10", "type": "passive"},
            "pin_11": {"number": "11", "name": "11", "type": "passive"},
            "pin_12": {"number": "12", "name": "12", "type": "passive"},
            "pin_13": {"number": "13", "name": "13", "type": "passive"},
            "pin_14": {"number": "14", "name": "14", "type": "passive"},
            "pin_15": {"number": "15", "name": "15", "type": "passive"},
            "pin_16": {"number": "16", "name": "16", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Switch:SW_DIP_x08",
            "machine_solder": "Button_Switch_SMD:SW_DIP_SPSTx08_Slide_9.78x22.5mm_W8.61mm_P2.54mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Cixi Tonver Elec HAD-08HWAG-R (C4682); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Switch:SW_DIP_x08 master and the Button_Switch_SMD:SW_DIP_SPSTx08_Slide_9.78x22.5mm_W8.61mm_P2.54mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C4684 / Cixi Tonver Elec HAD-08LWAG-2 - switch family batch 2026-10-06
    current = "electronic_switch_dip_switch_surface_mount_spst_8_position_recessed_actuator_cixi_tonver_had_08lwag_2"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "8-pos SPST slide DIP switch, SMD 2.54 mm recessed actuator, 9.78 x 22.5 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588935192085450753-C4684.pdf"
        part["dimensions_mm"] = {"length": 9.78, "width": 22.5, "height": 5.6}
        part["dimension_reference"] = {
            "document": "HAD-08LWAG-2 datasheet (C4684 provenance)",
            "pages": [1],
            "notes": "8-pos SPST slide DIP switch, SMD 2.54 mm recessed actuator, 9.78 x 22.5 mm body.",
        }
        part["electrical"] = {
            "circuit": "SPST",
            "current_rating": "25mA",
            "voltage_rating": "24V",
            "positions": "08",
            "actuator": "2.54mm 24V 25mA 8 Black SPST Slide, Recessed SMD,P=2.54mm DIP Switches ROHS",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "slide DIP switch"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
            "pin_3": {"number": "3", "name": "3", "type": "passive"},
            "pin_4": {"number": "4", "name": "4", "type": "passive"},
            "pin_5": {"number": "5", "name": "5", "type": "passive"},
            "pin_6": {"number": "6", "name": "6", "type": "passive"},
            "pin_7": {"number": "7", "name": "7", "type": "passive"},
            "pin_8": {"number": "8", "name": "8", "type": "passive"},
            "pin_9": {"number": "9", "name": "9", "type": "passive"},
            "pin_10": {"number": "10", "name": "10", "type": "passive"},
            "pin_11": {"number": "11", "name": "11", "type": "passive"},
            "pin_12": {"number": "12", "name": "12", "type": "passive"},
            "pin_13": {"number": "13", "name": "13", "type": "passive"},
            "pin_14": {"number": "14", "name": "14", "type": "passive"},
            "pin_15": {"number": "15", "name": "15", "type": "passive"},
            "pin_16": {"number": "16", "name": "16", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Switch:SW_DIP_x08",
            "machine_solder": "Button_Switch_SMD:SW_DIP_SPSTx08_Slide_9.78x22.5mm_W8.61mm_P2.54mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Cixi Tonver Elec HAD-08LWAG-2 (C4684); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Switch:SW_DIP_x08 master and the Button_Switch_SMD:SW_DIP_SPSTx08_Slide_9.78x22.5mm_W8.61mm_P2.54mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C4686 / Cixi Tonver Elec HAM-10LWA-R - switch family batch 2026-10-06
    current = "electronic_switch_dip_switch_through_hole_spst_10_position_recessed_actuator_cixi_tonver_ham_10lwa_r"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "10-pos SPST slide DIP switch, THT 2.54 mm, 9.78 x 27.58 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896694347419649-C4686.pdf"
        part["dimensions_mm"] = {"length": 9.78, "width": 27.58, "height": 5.6}
        part["dimension_reference"] = {
            "document": "HAM-10LWA-R datasheet (C4686 provenance)",
            "pages": [1],
            "notes": "10-pos SPST slide DIP switch, THT 2.54 mm, 9.78 x 27.58 mm body.",
        }
        part["electrical"] = {
            "circuit": "SPST",
            "current_rating": "25mA",
            "voltage_rating": "24V",
            "positions": "10",
            "actuator": "10 2.54mm 24V 25mA Black SPST Slide, Recessed 插件,P=2.54mm DIP Switches ROHS",
            "operating_temperature": "-30 to +85 C",
            "device_type": "slide DIP switch"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
            "pin_3": {"number": "3", "name": "3", "type": "passive"},
            "pin_4": {"number": "4", "name": "4", "type": "passive"},
            "pin_5": {"number": "5", "name": "5", "type": "passive"},
            "pin_6": {"number": "6", "name": "6", "type": "passive"},
            "pin_7": {"number": "7", "name": "7", "type": "passive"},
            "pin_8": {"number": "8", "name": "8", "type": "passive"},
            "pin_9": {"number": "9", "name": "9", "type": "passive"},
            "pin_10": {"number": "10", "name": "10", "type": "passive"},
            "pin_11": {"number": "11", "name": "11", "type": "passive"},
            "pin_12": {"number": "12", "name": "12", "type": "passive"},
            "pin_13": {"number": "13", "name": "13", "type": "passive"},
            "pin_14": {"number": "14", "name": "14", "type": "passive"},
            "pin_15": {"number": "15", "name": "15", "type": "passive"},
            "pin_16": {"number": "16", "name": "16", "type": "passive"},
            "pin_17": {"number": "17", "name": "17", "type": "passive"},
            "pin_18": {"number": "18", "name": "18", "type": "passive"},
            "pin_19": {"number": "19", "name": "19", "type": "passive"},
            "pin_20": {"number": "20", "name": "20", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Switch:SW_DIP_x10",
            "machine_solder": "Button_Switch_THT:SW_DIP_SPSTx10_Slide_9.78x27.58mm_W7.62mm_P2.54mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Cixi Tonver Elec HAM-10LWA-R (C4686); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Switch:SW_DIP_x10 master and the Button_Switch_THT:SW_DIP_SPSTx10_Slide_9.78x27.58mm_W7.62mm_P2.54mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C720477 / XUNPU TS-1088-AR02016 - switch family batch 2026-10-06
    current = "electronic_switch_tactile_surface_mount_xunpu_ts_1088_ar02016"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TS-1088-AR02016 SMD tactile switch, 3.9 x 3.0 x 2.0 mm, 2 pads"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588886944055513088-C720477.pdf"
        part["dimensions_mm"] = {"length": 3.9, "width": 3.0, "height": 2.0}
        part["dimension_reference"] = {
            "document": "TS-1088-AR02016 datasheet (C720477 provenance)",
            "pages": [1],
            "notes": "TS-1088-AR02016 SMD tactile switch, 3.9 x 3.0 x 2.0 mm, 2 pads.",
        }
        part["electrical"] = {
            "circuit": "SPST",
            "current_rating": "50mA",
            "voltage_rating": "12V",
            "operating_force": "1.6N",
            "positions": 1,
            "actuator": "Round Button",
            "operating_temperature": "-30 C~+80 C",
            "device_type": "tactile push switch"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Switch:SW_Push",
            "machine_solder": "Button_Switch_SMD:SW_SPST_TS-1088-xR020",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists XUNPU TS-1088-AR02016 (C720477); identity and ratings observed live at intake 2026-09-24.",
            "Mapped to the KiCad Switch:SW_Push master and the Button_Switch_SMD:SW_SPST_TS-1088-xR020 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated switch batch (tmp/switch_batch.py) ===