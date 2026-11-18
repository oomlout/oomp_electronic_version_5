def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_ferrite_bead_0805_220_ohm_2_amp_murata_blm21pg221sn1d"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "BLM21PG221SN1D"
        extras_dict[current]["part_number_lcsc"] = "C85840"

    current = "electronic_ferrite_bead_0805_15_ohm_1_5_amp_tdk_mmz2012r150at000"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "MMZ2012R150AT000"
        extras_dict[current]["part_number_manufacturer_tdk"] = "MMZ2012R150AT000"
        extras_dict[current]["part_number_lcsc"] = "C275464"
        extras_dict[current]["manufacturer"] = "TDK"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C275464.html"
        extras_dict[current]["product_url_manufacturer"] = "https://product.tdk.com/en/search/emc/emc/beads/info?part_no=MMZ2012R150AT000"
        extras_dict[current]["datasheet_url"] = "https://product.tdk.com/en/system/files/dam/doc/product/emc/emc/beads/catalog/beads_commercial_signal_mmz2012_en.pdf"
        extras_dict[current]["datasheet_url_lcsc"] = "https://www.lcsc.com/datasheet/C275464.pdf"
        extras_dict[current]["package_name_manufacturer"] = "MMZ2012"
        extras_dict[current]["electrical"] = {
            "impedance_at_100_mhz": "15 ohm",
            "impedance_tolerance": "+/-25%",
            "maximum_dc_resistance": "0.05 ohm",
            "maximum_rated_current": "1.5 A",
            "operating_temperature": "-55 to +125 C",
        }
        extras_dict[current]["ferrite_bead_dimensions_mm"] = {
            "body_length": 2.0,
            "body_length_tolerance": 0.2,
            "body_width": 1.25,
            "body_width_tolerance": 0.2,
            "body_height": 0.85,
            "body_height_tolerance": 0.2,
            "terminal_length": 0.5,
            "terminal_length_tolerance": 0.3,
            "recommended_pad_length": 0.8,
            "recommended_pad_width": 1.2,
            "recommended_pad_gap": 1.0,
        }
        extras_dict[current]["pins"] = {}
        ferrite_bead_pins = [
            ["1", "terminal_1"],
            ["2", "terminal_2"],
        ]
        for pin_index in range(len(ferrite_bead_pins)):
            pin = ferrite_bead_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": "passive",
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate historical supplier URL resolves to TDK MMZ2012R150AT000, LCSC C275464.",
            "The schematic value 1.5A is the rated current; the component is a 15 ohm at 100 MHz ferrite bead.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1002 / Sunlord GZ1608D601TF, verified against the Sunlord
    # Multilayer Chip Ferrite Bead GZ series catalogue (rev. 2024/6/19, 12
    # pages): product identification page 1 decodes GZ (general chip bead) /
    # 1608 [0603] 1.6 x 0.8 mm / D material / 601 = 600 ohm / T tape & reel /
    # F hazardous-substance-free, so the full ordering suffix is covered. The
    # GZ1608 TYPE table page 3 lists GZ1608D601TF: 600 +-25% ohm at 100 MHz,
    # max DCR 0.45 ohm, max rated current 200 mA, thickness 0.8 +-0.15 mm.
    # Shape and dimensions page 1 (GZ1608 [0603]): L 1.6 +-0.15, W 0.8
    # +-0.15, T 0.8 +-0.15, terminal width a 0.3 +-0.2 mm. Purchasing
    # identity fields come from the registry.
    current = "electronic_ferrite_bead_0603_600_ohm_200_milliamp_sunlord_gz1608d601tf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "1608 (0603 imperial)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579709915062976512-C1002.pdf"
        part["electrical"] = {
            "impedance_at_100_mhz": "600 ohm",
            "impedance_tolerance": "+-25%",
            "maximum_dc_resistance": "0.45 ohm",
            "maximum_rated_current": "200 mA",
            "test_frequency": "100 MHz",
            "operating_temperature": "-55 to +125 C (JLC listing)",
            "number_of_circuits": "1",
            "hazardous_substance_free": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["ferrite_bead_dimensions_mm"] = {
            "body_length": 1.6,
            "body_length_tolerance": 0.15,
            "body_width": 0.8,
            "body_width_tolerance": 0.15,
            "body_height": 0.8,
            "body_height_tolerance": 0.15,
            "terminal_length": 0.3,
            "terminal_length_tolerance": 0.2,
        }
        part["dimension_reference"] = {
            "document": "Sunlord Multilayer Chip Ferrite Bead GZ series catalogue, rev. 2024/6/19",
            "pages": [1, 3],
            "notes": "GZ1608 [0603] row: L 1.6+-0.15 mm, W 0.8+-0.15 mm, T 0.8+-0.15 mm, terminal width a 0.3+-0.2 mm. GZ1608 TYPE table (page 3) lists GZ1608D601TF at 600 +-25% ohm / 100 MHz, DCR max 0.45 ohm, rated current max 200 mA.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "terminal_1", "type": "passive"},
            "pin_2": {"number": "2", "name": "terminal_2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:FerriteBead_Small",
            "machine_solder": "Inductor_SMD:L_0603_1608Metric",
            "hand_solder": "Inductor_SMD:L_0603_1608Metric_Pad1.05x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Sunlord GZ1608D601TF (C1002): 600 ohm at 100 MHz, DCR 450 mOhm, 200 mA, 1 circuit, +-25%, -55 to +125 C; reconfirmed live 2026-09-30.",
            "The Sunlord ordering decode covers the full suffix: GZ general chip bead, 1608 [0603] 1.6 x 0.8 mm, D material, 601 = 600 ohm, T tape and reel, F hazardous-substance-free.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions above.",
            "Rated-current derating above +85 C applies only to beads rated 1000 mA and above, so it does not apply to this 200 mA part.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1015 / Sunlord GZ2012D101TF, verified against the Sunlord part
    # specification SPEC No. GZ10190000 Rev. 01 (10 pages): scope page 4
    # applies to GZ2012D101TF exactly; Section 3 lists 100 +-25% ohm at
    # 100 MHz, max DCR 0.15 ohm, max rated current 800 mA, operating
    # temperature -55 to +125 C. Table 4-1 page 5 (2012 [0805]): L 2.0
    # (+0.3/-0.1), W 1.25 +-0.2, T 0.85 +-0.2, terminal width a 0.5 +-0.3;
    # recommended reflow land A 0.80-1.20 (gap), B 0.80-1.20 (length each
    # side), C 0.90-1.60 (width). Purchasing identity fields come from the
    # registry.
    current = "electronic_ferrite_bead_0805_100_ohm_800_milliamp_sunlord_gz2012d101tf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "2012 (0805 imperial)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756360797033779200-C1015.pdf"
        part["electrical"] = {
            "impedance_at_100_mhz": "100 ohm",
            "impedance_tolerance": "+-25%",
            "maximum_dc_resistance": "0.15 ohm",
            "maximum_rated_current": "800 mA",
            "test_frequency": "100 MHz",
            "operating_temperature": "-55 to +125 C",
            "number_of_circuits": "1",
            "hazardous_substance_free": True,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.85}
        part["ferrite_bead_dimensions_mm"] = {
            "body_length": 2.0,
            "body_length_tolerance": 0.2,
            "body_width": 1.25,
            "body_width_tolerance": 0.2,
            "body_height": 0.85,
            "body_height_tolerance": 0.2,
            "terminal_length": 0.5,
            "terminal_length_tolerance": 0.3,
            "recommended_pad_length": 1.0,
            "recommended_pad_width": 1.25,
            "recommended_pad_gap": 1.0,
        }
        part["dimension_reference"] = {
            "document": "Sunlord Specifications for Multi-layer Chip Ferrite Bead, SPEC No. GZ10190000 Rev. 01",
            "pages": [4, 5, 8],
            "notes": "Table 4-1 page 5, 2012 [0805]: L 2.0 (+0.3/-0.1) mm, W 1.25+-0.2 mm, T 0.85+-0.2 mm, terminal width a 0.5+-0.3 mm. Recommended reflow land (Fig. 4-2/Table 4-1): gap A 0.80-1.20 mm, land length B 0.80-1.20 mm each side, land width C 0.90-1.60 mm; the recommended_pad_* values are the midpoints of those stated ranges, not guaranteed limits. Section 3 page 4 lists GZ2012D101TF: 100 +-25% ohm at 100 MHz, DCR max 0.15 ohm, rated current max 800 mA.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "terminal_1", "type": "passive"},
            "pin_2": {"number": "2", "name": "terminal_2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:FerriteBead_Small",
            "machine_solder": "Inductor_SMD:L_0805_2012Metric",
            "hand_solder": "Inductor_SMD:L_0805_2012Metric_Pad1.05x1.20mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Sunlord GZ2012D101TF (C1015): 100 ohm at 100 MHz, DCR 150 mOhm, 800 mA, 1 circuit, +-25%, -55 to +125 C; reconfirmed live 2026-09-30.",
            "The Sunlord part specification is scoped to GZ2012D101TF exactly (scope, page 4) and its electrical table matches the JLC listing value for value.",
            "Non-polarized two-terminal chip; the standard built-in 0805 chip renderer draws the package from the verified dimensions above.",
            "Rated-current derating above +85 C applies only to beads rated over 1000 mA, so it does not apply to this 800 mA part.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1017 / Sunlord GZ2012D601TF, verified against the Sunlord
    # Multilayer Chip Ferrite Bead GZ series catalogue (rev. 2024/6/19; the
    # same series PDF JLC attaches to every GZ part page): product
    # identification page 1 decodes GZ general chip bead / 2012 [0805]
    # 2.0 x 1.25 mm / D material / 601 = 600 ohm / T tape & reel / F
    # hazardous-substance-free. The GZ2012 TYPE table page 3 lists
    # GZ2012D601TF: 600 +-25% ohm at 100 MHz, max DCR 0.30 ohm, max rated
    # current 500 mA. Shape and dimensions page 1 (2012 [0805]): L 2.0
    # (+0.3/-0.1), W 1.25 +-0.2, T 0.85 +-0.2, terminal width a 0.5 +-0.3
    # mm. Purchasing identity fields come from the registry.
    current = "electronic_ferrite_bead_0805_600_ohm_500_milliamp_sunlord_gz2012d601tf"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_ferrite_bead_0603_600_ohm_200_milliamp_sunlord_gz1608d601tf"
        part["package_name_manufacturer"] = "2012 (0805 imperial)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8565214663970209792-C1017.pdf"
        part["electrical"] = {
            "impedance_at_100_mhz": "600 ohm",
            "impedance_tolerance": "+-25%",
            "maximum_dc_resistance": "0.3 ohm",
            "maximum_rated_current": "500 mA",
            "test_frequency": "100 MHz",
            "operating_temperature": "-55 to +125 C (JLC listing)",
            "number_of_circuits": "1",
            "hazardous_substance_free": True,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.85}
        part["ferrite_bead_dimensions_mm"] = {
            "body_length": 2.0,
            "body_length_tolerance": 0.2,
            "body_width": 1.25,
            "body_width_tolerance": 0.2,
            "body_height": 0.85,
            "body_height_tolerance": 0.2,
            "terminal_length": 0.5,
            "terminal_length_tolerance": 0.3,
        }
        part["dimension_reference"] = {
            "document": "Sunlord Multilayer Chip Ferrite Bead GZ series catalogue, rev. 2024/6/19",
            "pages": [1, 3, 10],
            "notes": "2012 [0805] row: L 2.0 (+0.3/-0.1) mm, W 1.25+-0.2 mm, T 0.85+-0.2 mm, terminal width a 0.5+-0.3 mm. GZ2012 TYPE table (page 3) lists GZ2012D601TF at 600 +-25% ohm / 100 MHz, DCR max 0.30 ohm, rated current max 500 mA; per-part impedance curve page 10.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "terminal_1", "type": "passive"},
            "pin_2": {"number": "2", "name": "terminal_2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:FerriteBead_Small",
            "machine_solder": "Inductor_SMD:L_0805_2012Metric",
            "hand_solder": "Inductor_SMD:L_0805_2012Metric_Pad1.05x1.20mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Sunlord GZ2012D601TF (C1017): 600 ohm at 100 MHz, DCR 300 mOhm, 500 mA, 1 circuit, +-25%, -55 to +125 C; reconfirmed live 2026-09-30.",
            "The Sunlord ordering decode covers the full suffix: GZ general chip bead, 2012 [0805] 2.0 x 1.25 mm, D material, 601 = 600 ohm, T tape and reel, F hazardous-substance-free.",
            "Non-polarized two-terminal chip; the standard built-in 0805 chip renderer draws the package from the verified dimensions above.",
            "Rated-current derating above +85 C applies only to beads rated 1000 mA and above, so it does not apply to this 500 mA part.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # Apply individually reviewed JLC house choices after other supplier data.
    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="ferrite_bead")
