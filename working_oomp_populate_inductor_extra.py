def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_inductor_0603_10_micro_henry"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Inductor 10µH 0603"
        part["name_readable"] = "Inductor 10µH 0603"
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~", "type": "passive"},
            "pin_2": {"number": "2", "name": "~", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:L",
            "machine_solder": "Inductor_SMD:L_0603_1608Metric",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["L"],
            "symbols": ["Device:L"],
            "footprints": ["Inductor_SMD:L_0603_1608Metric"],
        }

    current = "electronic_inductor_0603_4_7_micro_henry"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Inductor 4.7µH 0603"
        part["name_readable"] = "Inductor 4.7µH 0603"
        part["manufacturer"] = "Sunlord"
        part["part_number_manufacturer"] = "SDFL1608Q4R7KTF"
        part["part_number_lcsc"] = "C1034"
        part["product_url"] = "https://www.lcsc.com/product-detail/C1034.html"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8724361421347237888-C1034.pdf"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]

    current = "electronic_inductor_0805_1_micro_henry"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Inductor 1µH 0805"
        part["name_readable"] = "Inductor 1µH 0805"
        part["manufacturer"] = "Sunlord"
        part["part_number_manufacturer"] = "SDFL2012Q1R0KTF"
        part["part_number_lcsc"] = "C1042"
        part["product_url"] = "https://www.lcsc.com/product-detail/C1042.html"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8755215269118005248-C1042.pdf"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]

    current = "electronic_inductor_0805_2_2_micro_henry"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Inductor 2.2µH 0805"
        part["name_readable"] = "Inductor 2.2µH 0805"
        part["manufacturer"] = "FH (Guangdong Fenghua Advanced Tech)"
        part["part_number_manufacturer"] = "CMI201209U2R2KT"
        part["part_number_lcsc"] = "C1043"
        part["product_url"] = "https://www.lcsc.com/product-detail/C1043.html"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579705814512091136-C1043.pdf"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]

    current = "electronic_inductor_0805_5_6_micro_henry"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Inductor 5.6µH 0805"
        part["name_readable"] = "Inductor 5.6µH 0805"
        part["manufacturer"] = "FH (Guangdong Fenghua Advanced Tech)"
        part["part_number_manufacturer"] = "CMI201209X5R6KT"
        part["part_number_lcsc"] = "C1045"
        part["product_url"] = "https://www.lcsc.com/product-detail/C1045.html"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710118277140480-C1045.pdf"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]

    current = "electronic_inductor_1206_2_2_micro_henry"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Inductor 2.2µH 1206"
        part["name_readable"] = "Inductor 2.2µH 1206"
        part["manufacturer"] = "FH (Guangdong Fenghua Advanced Tech)"
        part["part_number_manufacturer"] = "CMI321609U2R2KT"
        part["part_number_lcsc"] = "C1048"
        part["product_url"] = "https://www.lcsc.com/product-detail/C1048.html"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710131607048192-C1048.pdf"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]

    current = "electronic_inductor_1206_4_7_micro_henry"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Inductor 4.7µH 1206"
        part["name_readable"] = "Inductor 4.7µH 1206"
        part["manufacturer"] = "FH (Guangdong Fenghua Advanced Tech)"
        part["part_number_manufacturer"] = "CMI321609U4R7KT"
        part["part_number_lcsc"] = "C1049"
        part["product_url"] = "https://www.lcsc.com/product-detail/C1049.html"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579705847531814912-C1049.pdf"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]

    current = "electronic_inductor_1206_5_6_micro_henry"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Inductor 5.6µH 1206"
        part["name_readable"] = "Inductor 5.6µH 1206"
        part["manufacturer"] = "FH (Guangdong Fenghua Advanced Tech)"
        part["part_number_manufacturer"] = "CMI321609U5R6KT"
        part["part_number_lcsc"] = "C1050"
        part["product_url"] = "https://www.lcsc.com/product-detail/C1050.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C1050.pdf"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]

    current = "electronic_inductor_1206_10_micro_henry"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Inductor 10µH 1206"
        part["name_readable"] = "Inductor 10µH 1206"
        part["manufacturer"] = "FH (Guangdong Fenghua Advanced Tech)"
        part["part_number_manufacturer"] = "CMI321609X100KT"
        part["part_number_lcsc"] = "C1051"
        part["product_url"] = "https://www.lcsc.com/product-detail/C1051.html"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579705850359185408-C1051.pdf"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]

    # JLC C1035 / Sunlord SDFL1608S100KTF full-stage technical data, verified
    # against the Sunlord Multilayer Chip Ferrite Inductor SDFL series
    # catalogue (rev. 2025/5/23, 6 pages): product identification page 1
    # decodes SDFL chip ferrite inductor / 1608 [0603] 1.6 x 0.8 mm / Q
    # material / S100 = 10 uH / K = +-10% / T tape & reel / F hazardous-
    # substance-free, and states the operating temperature -40 to +85 C. The
    # SDFL1608 Series table page 3 lists SDFL1608S100 TF: 10 uH, min Q 30 at
    # the 2 MHz L/Q test frequency, min SRF 17 MHz, max DCR 1.85 ohm, max
    # rated current 3 mA, thickness 0.8 +-0.15 mm. Dimensions page 1
    # (SDFL1608 [0603]): L 1.6 +-0.15, W 0.8 +-0.15, T 0.8 +-0.15, terminal
    # width a 0.3 +-0.2 mm. Purchasing identity fields come from the registry.
    current = "electronic_inductor_0603_10_micro_henry_sunlord_sdfl1608s100ktf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "1608 (0603 imperial), SDFL thin type"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8755215265330278400-C1035.pdf"
        part["electrical"] = {
            "inductance": "10 uH",
            "inductance_tolerance": "+-10%",
            "minimum_q": "30",
            "q_test_frequency": "2 MHz",
            "minimum_self_resonant_frequency": "17 MHz",
            "maximum_dc_resistance": "1.85 ohm",
            "maximum_rated_current": "3 mA",
            "operating_temperature": "-40 to +85 C",
            "hazardous_substance_free": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Sunlord Multilayer Chip Ferrite Inductor SDFL series catalogue, rev. 2025/5/23",
            "pages": [1, 3],
            "notes": "SDFL1608 [0603] row: L 1.6+-0.15 mm, W 0.8+-0.15 mm, T 0.8+-0.15 mm, terminal width a 0.3+-0.2 mm. SDFL1608 Series table (page 3) lists SDFL1608S100 TF: 10 uH, min Q 30 at 2 MHz, min SRF 17 MHz, DCR max 1.85 ohm, rated current max 3 mA.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "terminal_1", "type": "passive"},
            "pin_2": {"number": "2", "name": "terminal_2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:L",
            "machine_solder": "Inductor_SMD:L_0603_1608Metric",
            "hand_solder": "Inductor_SMD:L_0603_1608Metric_Pad1.05x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Sunlord SDFL1608S100KTF (C1035): 10 uH +-10%, Q 30 at 2 MHz, SRF 17 MHz, DCR 1.85 ohm, 3 mA; reconfirmed live 2026-09-30.",
            "The Sunlord ordering decode covers the full suffix: SDFL chip ferrite inductor, 1608 [0603] 1.6 x 0.8 mm, Q material, S100 = 10 uH, K = +-10%, T tape and reel, F hazardous-substance-free.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions above.",
            "The 3 mA / 1.85 ohm ratings belong to this exact purchasing choice; the generic 0603 10 uH row stays unrated.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # Apply individually reviewed JLC house choices after other supplier data.
    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="inductor")
