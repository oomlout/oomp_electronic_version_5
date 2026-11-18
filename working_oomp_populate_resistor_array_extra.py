def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    # JLC C1980 / UNI-ROYAL 4D03WGJ0472T5E full-stage technical data, verified
    # against the Uniroyal Chip Resistor Array Series specification
    # (2017/06/12, browser-downloaded to this part; the family anchor for the
    # 4D03 arrays): type designation page 4 decodes 4D03 = convex 4 x 0603
    # isolated array, 0472 = 4.7 kOhm (47 x 10^2), J = +-5%; the equivalent
    # circuit (page 4) shows R1 = pins 1-8, R2 = 2-7, R3 = 3-6, R4 = 4-5;
    # convex dimensions page 5: L 3.20+-0.20, W 1.60+-0.20, T 0.50+-0.10,
    # pad pitch P 0.80+-0.10 mm; ratings page 6: 1/16 W per element, max
    # working voltage 50 V, max overload 300 V, TCR +-200 ppm/C (>=10 Ohm),
    # operating -55 to +155 C; marking page 8 decodes 0472. Live JLC
    # description confirms 4 x 4.7 kOhm, 62.5 mW, +-5%, +-200 ppm/C.
    # KiCad masters: Device:R_Pack04_Split symbol pins pair 1-8 / 2-7 /
    # 3-6 / 4-5, matching both the datasheet circuit and the
    # Resistor_SMD:R_Array_Convex_4x0603 footprint pads; no HandSolder
    # variant exists for the array footprint.
    current = "electronic_resistor_array_4_x_0603_convex_4700_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4D03 (0603x4 convex, 3.20 x 1.60 mm, T 0.50 mm)"
        part["datasheet_url"] = "https://jlcpcb.com/partdetail/4D03WGJ0472T5E/C1980"
        part["electrical"] = {
            "resistance": "4 x 4.7 kOhm (0472) isolated",
            "tolerance": "+-5% (J)",
            "power": "1/16 W (62.5 mW) per element",
            "rated_voltage": "50 V max working voltage",
            "overload_voltage": "300 V max",
            "temperature_coefficient": "+-200 ppm/C (>=10 Ohm)",
            "operating_temperature": "-55 to +155 C",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Uniroyal Chip Resistor Array Series specification, 2017/06/12 (C1980)",
            "pages": [4, 5, 6, 8],
            "notes": "4D03 convex: L 3.20+-0.20 mm, W 1.60+-0.20 mm, T 0.50+-0.10 mm, pad pitch P 0.80+-0.10 mm (page 5 dimensions table); equivalent circuit page 4; ratings page 6.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04_Split",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic UNI-ROYAL 4D03WGJ0472T5E (C1980): 4 x 4.7 kOhm, 1/16 W, +-5%, +-200 ppm/C in 0603x4 convex; reconfirmed live 2026-10-01 (stock 2,009,626).",
            "Browser-downloaded the Uniroyal array series datasheet (14 pages, 2017/06/12) into this part; it anchors the resistor-array family (no shared copy).",
            "Pin pairing per the datasheet equivalent circuit and the KiCad masters: R1 = 1-8, R2 = 2-7, R3 = 3-6, R4 = 4-5 (Device:R_Pack04_Split matches Resistor_SMD:R_Array_Convex_4x0603 pad-for-pad).",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # Apply individually reviewed JLC house choices after other supplier data.
    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="resistor_array")

    # === BEGIN generated resistor array batch (tmp/array_batch.py) — regenerated, do not hand-edit ===
    # JLC C1952 / UNI-ROYAL(Uniroyal Elec) 4D03WGJ0000T5E - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0603_convex_0_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710137981980672-C1952.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.6}
        part["dimension_reference"] = {
            "document": "4D03WGJ0000T5E datasheet (C1952 provenance)",
            "pages": [1],
            "notes": "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "0Ω",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-400ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0603 (1608) convex resistor network UNI-ROYAL(Uniroyal Elec) 4D03WGJ0000T5E (C1952); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0603 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C1959 / FH (Guangdong Fenghua Advanced Tech) RC-ML08W300JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0603_convex_30_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710143820726272-C1959.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.6}
        part["dimension_reference"] = {
            "document": "RC-ML08W300JT datasheet (C1959 provenance)",
            "pages": [1],
            "notes": "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "30Ω",
            "tolerance": "+-5%",
            "power_per_element": "1/16W",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-100ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0603 (1608) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-ML08W300JT (C1959); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0603 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C1966 / FH (Guangdong Fenghua Advanced Tech) RC-ML08W271JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0603_convex_270_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588901506267688960-C1966.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.6}
        part["dimension_reference"] = {
            "document": "RC-ML08W271JT datasheet (C1966 provenance)",
            "pages": [1],
            "notes": "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "270Ω",
            "tolerance": "+-5%",
            "power_per_element": "1/16W",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-100ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0603 (1608) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-ML08W271JT (C1966); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0603 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C1973 / FH (Guangdong Fenghua Advanced Tech) RC-ML08W152JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0603_convex_1500_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710147402797056-C1973.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.6}
        part["dimension_reference"] = {
            "document": "RC-ML08W152JT datasheet (C1973 provenance)",
            "pages": [1],
            "notes": "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "1.5kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-100ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0603 (1608) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-ML08W152JT (C1973); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0603 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C1983 / FH (Guangdong Fenghua Advanced Tech) RC-ML08W682JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0603_convex_6800_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710160133996544-C1983.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.6}
        part["dimension_reference"] = {
            "document": "RC-ML08W682JT datasheet (C1983 provenance)",
            "pages": [1],
            "notes": "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "6.8kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-100ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0603 (1608) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-ML08W682JT (C1983); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0603 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C1990 / RALEC RTA03-4D303JTP - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0603_convex_30000_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710177798782976-C1990.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.6}
        part["dimension_reference"] = {
            "document": "RTA03-4D303JTP datasheet (C1990 provenance)",
            "pages": [1],
            "notes": "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "30kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0603 (1608) convex resistor network RALEC RTA03-4D303JTP (C1990); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0603 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C1992 / FH (Guangdong Fenghua Advanced Tech) RC-ML08W363JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0603_convex_36000_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588901506267959296-C1992.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.6}
        part["dimension_reference"] = {
            "document": "RC-ML08W363JT datasheet (C1992 provenance)",
            "pages": [1],
            "notes": "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "36kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-100ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0603 (1608) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-ML08W363JT (C1992); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0603 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C1996 / UNI-ROYAL(Uniroyal Elec) 4D03WGJ0104T5E - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0603_convex_100000_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710181992947712-C1996.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.6}
        part["dimension_reference"] = {
            "document": "4D03WGJ0104T5E datasheet (C1996 provenance)",
            "pages": [1],
            "notes": "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "100kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0603 (1608) convex resistor network UNI-ROYAL(Uniroyal Elec) 4D03WGJ0104T5E (C1996); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0603 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2001 / FH (Guangdong Fenghua Advanced Tech) RC-MT08W000JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_0_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588918443948695552-C2001.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "RC-MT08W000JT datasheet (C2001 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "0Ω",
            "tolerance": "+-5%",
            "power_per_element": "1/16W",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-MT08W000JT (C2001); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2002 / FH (Guangdong Fenghua Advanced Tech) RC-MT08W3R0JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_3_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710186057502720-C2002.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "RC-MT08W3R0JT datasheet (C2002 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "3Ω",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-400ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-MT08W3R0JT (C2002); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2004 / FH (Guangdong Fenghua Advanced Tech) RC-MT08W200JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_20_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710190054674432-C2004.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "RC-MT08W200JT datasheet (C2004 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "20Ω",
            "tolerance": "+-5%",
            "power_per_element": "1/16W",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-100ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-MT08W200JT (C2004); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2006 / FH (Guangdong Fenghua Advanced Tech) RC-MT08W270JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_27_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710194227732480-C2006.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "RC-MT08W270JT datasheet (C2006 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "27Ω",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-MT08W270JT (C2006); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2007 / FH (Guangdong Fenghua Advanced Tech) RC-MT08W300JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_30_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710198065659904-C2007.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "RC-MT08W300JT datasheet (C2007 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "30Ω",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-MT08W300JT (C2007); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2011 / FH (Guangdong Fenghua Advanced Tech) RC-MT08W201JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_200_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710201307992064-C2011.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "RC-MT08W201JT datasheet (C2011 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "200Ω",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-MT08W201JT (C2011); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2017 / FH (Guangdong Fenghua Advanced Tech) RC-MT08W222JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_2200_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710204856238080-C2017.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "RC-MT08W222JT datasheet (C2017 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "2.2kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-MT08W222JT (C2017); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2018 / FH (Guangdong Fenghua Advanced Tech) RC-MT08W332JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_3300_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710208694026240-C2018.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "RC-MT08W332JT datasheet (C2018 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "3.3kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-MT08W332JT (C2018); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C20197 / UNI-ROYAL(Uniroyal Elec) 4D03WGJ0102T5E - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0603_convex_1000_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579705782488580096-C20197.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.6}
        part["dimension_reference"] = {
            "document": "4D03WGJ0102T5E datasheet (C20197 provenance)",
            "pages": [1],
            "notes": "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "1kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0603 (1608) convex resistor network UNI-ROYAL(Uniroyal Elec) 4D03WGJ0102T5E (C20197); identity and ratings observed live at intake 2026-09-25.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0603 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2021 / FH (Guangdong Fenghua Advanced Tech) RC-MT08W512JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_5100_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710211849764864-C2021.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "RC-MT08W512JT datasheet (C2021 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "5.1kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-100ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-MT08W512JT (C2021); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2022 / FH (Guangdong Fenghua Advanced Tech) RC-MT08W203JT - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_20000_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710214813515776-C2022.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "RC-MT08W203JT datasheet (C2022 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "20kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network FH (Guangdong Fenghua Advanced Tech) RC-MT08W203JT (C2022); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2028 / UNI-ROYAL(Uniroyal Elec) 4D02WGJ0473TCE - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0402_convex_47000_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710217954639872-C2028.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.0, "height": 0.5}
        part["dimension_reference"] = {
            "document": "4D02WGJ0473TCE datasheet (C2028 provenance)",
            "pages": [1],
            "notes": "4x0402 (1005) convex resistor network, ROHM MNR04-style, 2.0 x 1.0 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "47kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0402",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0402 (1005) convex resistor network UNI-ROYAL(Uniroyal Elec) 4D02WGJ0473TCE (C2028); identity and ratings observed live at intake 2026-09-28.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0402 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C29718 / UNI-ROYAL(Uniroyal Elec) 4D03WGJ0103T5E - resistor array family batch 2026-10-06
    current = "electronic_resistor_array_4_x_0603_convex_10000_ohm_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579705779290898432-C29718.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.6}
        part["dimension_reference"] = {
            "document": "4D03WGJ0103T5E datasheet (C29718 provenance)",
            "pages": [1],
            "notes": "4x0603 (1608) convex resistor network, ROHM MNR14-style, 3.2 x 1.6 mm body; eight terminals in two columns, four isolated elements across the left/right pad pairs.",
        }
        part["electrical"] = {
            "resistance": "10kΩ",
            "tolerance": "+-5%",
            "power_per_element": "62.5mW",
            "elements": 4,
            "terminals": 8,
            "configuration": "four isolated resistors (convex isolated network)",
            "temperature_coefficient": "+-200ppm/ C",
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R1.1", "type": "passive"},
            "pin_2": {"number": "2", "name": "R2.1", "type": "passive"},
            "pin_3": {"number": "3", "name": "R3.1", "type": "passive"},
            "pin_4": {"number": "4", "name": "R4.1", "type": "passive"},
            "pin_5": {"number": "5", "name": "R4.2", "type": "passive"},
            "pin_6": {"number": "6", "name": "R3.2", "type": "passive"},
            "pin_7": {"number": "7", "name": "R2.2", "type": "passive"},
            "pin_8": {"number": "8", "name": "R1.2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:R_Pack04",
            "machine_solder": "Resistor_SMD:R_Array_Convex_4x0603",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 4x0603 (1608) convex resistor network UNI-ROYAL(Uniroyal Elec) 4D03WGJ0103T5E (C29718); identity and ratings observed live at intake 2026-09-25.",
            "Convex isolated resistor network mapped to the KiCad Device:R_Pack04 master and the Resistor_SMD:R_Array_Convex_4x0603 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated resistor array batch (tmp/array_batch.py) ===