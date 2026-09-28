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

    # Apply individually reviewed JLC house choices after other supplier data.
    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="inductor")
