def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_fuse_0402_resettable"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Polyfuse 0402"
        part["name_readable"] = "Resettable Fuse 0402"
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~", "type": "passive"},
            "pin_2": {"number": "2", "name": "~", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_0402_1005Metric",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["Polyfuse"],
            "symbols": ["Device:Polyfuse"],
            "footprints": ["Fuse:Fuse_0402_1005Metric"],
        }

    current = "electronic_fuse_1206_resettable"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Polyfuse 1206"
        part["name_readable"] = "Resettable Fuse 1206"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~", "type": "passive"},
            "pin_2": {"number": "2", "name": "~", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_1206_3216Metric",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["Polyfuse"],
            "symbols": ["Device:Polyfuse"],
            "footprints": ["Fuse:Fuse_1206_3216Metric"],
        }

    current = "electronic_fuse_0603_resettable_bourns_mf_fsmf"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Bourns"
        part["part_number_manufacturer"] = "MF-FSMF"
        part["name_short"] = "Bourns MF-FSMF 0603 Resettable Fuse"
        part["name_readable"] = "Bourns MF-FSMF Series 0603 Resettable Fuse"
        part["datasheet_url"] = "https://www.bourns.com/docs/product-datasheets/mffsmf.pdf"
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.6}
        part["dimension_reference"] = {
            "document": "Bourns MF-FSMF Series datasheet",
            "notes": "0603 low-profile surface-mount PTC series; electrical suffix is intentionally unspecified because the source schematic only gives the series footprint.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~", "type": "passive"},
            "pin_2": {"number": "2", "name": "~", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_0603_1608Metric",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["MF-FSMF", "Polyfuse"],
            "symbols": ["Device:Polyfuse"],
            "footprints": ["Fuse:Fuse_0603_1608Metric", "MF-FSMF"],
        }

    # Apply explicitly promoted browser-reviewed JLC identities (manufacturer,
    # MPN, LCSC code) to the fuse family, matching the other families'
    # reviewed-choice enrichment.
    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="fuse")

    # === BEGIN generated fuse batch (tmp/fuse_batch.py) — regenerated, do not hand-edit ===
    # JLC C3102 / PTTC(Polytronics Tech) SMD1812P110TF - fuse family batch 2026-10-06
    current = "electronic_fuse_1812_resettable_pttc_polytronics_tech_smd1812p110tf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "1812 (4532 metric) resettable PPTC, 4.5 x 3.2 x 2.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711410760716288-C3102.pdf"
        part["dimensions_mm"] = {"length": 4.5, "width": 3.2, "height": 2.4}
        part["dimension_reference"] = {
            "document": "SMD1812P110TF datasheet (C3102 provenance)",
            "pages": [1],
            "notes": "1812 (4532 metric) resettable PPTC, 4.5 x 3.2 x 2.4 mm.",
        }
        part["electrical"] = {
            "interrupt_rating": "100A",
            "resettable": True,
            "device_type": "resettable PPTC fuse",
            "operating_temperature": "-40 C~+85 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_1812_4532Metric",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists PTTC(Polytronics Tech) SMD1812P110TF (C3102); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Polyfuse master and the Fuse:Fuse_1812_4532Metric footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3105 / Littelfuse 0466002.NRHF - fuse family batch 2026-10-06
    current = "electronic_fuse_1206_disposable_littelfuse_0466002_nrhf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "1206 (3216 metric) one-shot fuse, 3.2 x 1.6 x 1.1 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711421149732864-C3105.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.1}
        part["dimension_reference"] = {
            "document": "0466002.NRHF datasheet (C3105 provenance)",
            "pages": [1],
            "notes": "1206 (3216 metric) one-shot fuse, 3.2 x 1.6 x 1.1 mm.",
        }
        part["electrical"] = {
            "current_rating": "2A",
            "interrupt_rating": "50A",
            "resettable": False,
            "device_type": "one-shot fuse",
            "operating_temperature": "-55 C~+90 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Fuse",
            "machine_solder": "Fuse:Fuse_1206_3216Metric",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Littelfuse 0466002.NRHF (C3105); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Fuse master and the Fuse:Fuse_1206_3216Metric footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3107 / Littelfuse RF1404-000 - fuse family batch 2026-10-06
    current = "electronic_fuse_1812_resettable_littelfuse_rf1404_000"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "1812 (4532 metric) resettable PPTC, 4.5 x 3.2 x 2.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588907433410908160-C3107.pdf"
        part["dimensions_mm"] = {"length": 4.5, "width": 3.2, "height": 2.4}
        part["dimension_reference"] = {
            "document": "RF1404-000 datasheet (C3107 provenance)",
            "pages": [1],
            "notes": "1812 (4532 metric) resettable PPTC, 4.5 x 3.2 x 2.4 mm.",
        }
        part["electrical"] = {
            "resettable": True,
            "device_type": "resettable PPTC fuse",
            "operating_temperature": "-40 C~+85 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_1812_4532Metric",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Littelfuse RF1404-000 (C3107); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Polyfuse master and the Fuse:Fuse_1812_4532Metric footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3117 / Xucheng Elec 5F.2000210000R1 - fuse family batch 2026-10-06
    current = "electronic_fuse_5_2_x_20_mm_glass_plugin_disposable_xucheng_elec_5f_2000210000r1"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588907149796130816-C3117.pdf"
        part["dimensions_mm"] = {"length": 20.0, "width": 5.2, "height": 6.5}
        part["dimension_reference"] = {
            "document": "5F.2000210000R1 datasheet (C3117 provenance)",
            "pages": [1],
            "notes": "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span.",
        }
        part["electrical"] = {
            "current_rating": "2A",
            "interrupt_rating": "35A@250VAC",
            "resettable": False,
            "device_type": "one-shot fuse",
            "operating_temperature": "-40 C~+125 C",
            "mounting": "clip-mounted 5x20 glass tube (companion clips C3130)"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Fuse",
            "machine_solder": "Fuse:Fuseholder_Littelfuse_100_series_5x20mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Xucheng Elec 5F.2000210000R1 (C3117); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Fuse master and the Fuse:Fuseholder_Littelfuse_100_series_5x20mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3118 / Xucheng Elec 5G.3000210000S1 - fuse family batch 2026-10-06
    current = "electronic_fuse_5_2_x_20_mm_glass_plugin_disposable_xucheng_elec_5g_3000210000s1"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588918477948669952-C3118.pdf"
        part["dimensions_mm"] = {"length": 20.0, "width": 5.2, "height": 6.5}
        part["dimension_reference"] = {
            "document": "5G.3000210000S1 datasheet (C3118 provenance)",
            "pages": [1],
            "notes": "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span.",
        }
        part["electrical"] = {
            "current_rating": "3A",
            "interrupt_rating": "100A@250VAC",
            "resettable": False,
            "device_type": "one-shot fuse",
            "operating_temperature": "-40 C~+125 C",
            "mounting": "clip-mounted 5x20 glass tube (companion clips C3130)"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Fuse",
            "machine_solder": "Fuse:Fuseholder_Littelfuse_100_series_5x20mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Xucheng Elec 5G.3000210000S1 (C3118); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Fuse master and the Fuse:Fuseholder_Littelfuse_100_series_5x20mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3121 / Xucheng Elec 7A 250VACGlass Tube Fuse - fuse family batch 2026-10-06
    current = "electronic_fuse_5_2_x_20_mm_glass_plugin_disposable_xucheng_elec_7a_250vacglass_tube_fuse"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588907149645271040-C3121.pdf"
        part["dimensions_mm"] = {"length": 20.0, "width": 5.2, "height": 6.5}
        part["dimension_reference"] = {
            "document": "7A 250VACGlass Tube Fuse datasheet (C3121 provenance)",
            "pages": [1],
            "notes": "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span.",
        }
        part["electrical"] = {
            "current_rating": "7A",
            "resettable": False,
            "device_type": "one-shot fuse",
            "operating_temperature": "-40 to +85 C",
            "mounting": "clip-mounted 5x20 glass tube (companion clips C3130)"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Fuse",
            "machine_solder": "Fuse:Fuseholder_Littelfuse_100_series_5x20mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Xucheng Elec 7A 250VACGlass Tube Fuse (C3121); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Fuse master and the Fuse:Fuseholder_Littelfuse_100_series_5x20mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3122 / Xucheng Elec 5F.0010220000R1 - fuse family batch 2026-10-06
    current = "electronic_fuse_5_2_x_20_mm_glass_plugin_disposable_xucheng_elec_5f_0010220000r1"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588918541659877376-C3122.pdf"
        part["dimensions_mm"] = {"length": 20.0, "width": 5.2, "height": 6.5}
        part["dimension_reference"] = {
            "document": "5F.0010220000R1 datasheet (C3122 provenance)",
            "pages": [1],
            "notes": "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span.",
        }
        part["electrical"] = {
            "current_rating": "10A",
            "interrupt_rating": "100A",
            "resettable": False,
            "device_type": "one-shot fuse",
            "operating_temperature": "-40 C~+125 C",
            "mounting": "clip-mounted 5x20 glass tube (companion clips C3130)"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Fuse",
            "machine_solder": "Fuse:Fuseholder_Littelfuse_100_series_5x20mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Xucheng Elec 5F.0010220000R1 (C3122); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Fuse master and the Fuse:Fuseholder_Littelfuse_100_series_5x20mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3123 / Xucheng Elec 5F.0500210000R1 - fuse family batch 2026-10-06
    current = "electronic_fuse_5_2_x_20_mm_glass_plugin_disposable_xucheng_elec_5f_0500210000r1"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588907149645000704-C3123.pdf"
        part["dimensions_mm"] = {"length": 20.0, "width": 5.2, "height": 6.5}
        part["dimension_reference"] = {
            "document": "5F.0500210000R1 datasheet (C3123 provenance)",
            "pages": [1],
            "notes": "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span.",
        }
        part["electrical"] = {
            "current_rating": "500mA",
            "interrupt_rating": "35A",
            "resettable": False,
            "device_type": "one-shot fuse",
            "operating_temperature": "-40 C~+125 C",
            "mounting": "clip-mounted 5x20 glass tube (companion clips C3130)"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Fuse",
            "machine_solder": "Fuse:Fuseholder_Littelfuse_100_series_5x20mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Xucheng Elec 5F.0500210000R1 (C3123); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Fuse master and the Fuse:Fuseholder_Littelfuse_100_series_5x20mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3124 / Xucheng Elec 5F.1600210000R1 - fuse family batch 2026-10-06
    current = "electronic_fuse_5_2_x_20_mm_glass_plugin_disposable_xucheng_elec_5f_1600210000r1"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588918541470457856-C3124.pdf"
        part["dimensions_mm"] = {"length": 20.0, "width": 5.2, "height": 6.5}
        part["dimension_reference"] = {
            "document": "5F.1600210000R1 datasheet (C3124 provenance)",
            "pages": [1],
            "notes": "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span.",
        }
        part["electrical"] = {
            "current_rating": "1.6A",
            "interrupt_rating": "35A@250VAC",
            "resettable": False,
            "device_type": "one-shot fuse",
            "operating_temperature": "-40 C~+125 C",
            "mounting": "clip-mounted 5x20 glass tube (companion clips C3130)"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Fuse",
            "machine_solder": "Fuse:Fuseholder_Littelfuse_100_series_5x20mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Xucheng Elec 5F.1600210000R1 (C3124); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Fuse master and the Fuse:Fuseholder_Littelfuse_100_series_5x20mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3128 / Xucheng Elec 0.2A 250VACGlass Tube Fuse - fuse family batch 2026-10-06
    current = "electronic_fuse_5_2_x_20_mm_glass_plugin_disposable_xucheng_elec_0_2a_250vacglass_tube_fuse"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588907149631741952-C3128.pdf"
        part["dimensions_mm"] = {"length": 20.0, "width": 5.2, "height": 6.5}
        part["dimension_reference"] = {
            "document": "0.2A 250VACGlass Tube Fuse datasheet (C3128 provenance)",
            "pages": [1],
            "notes": "5.2 x 20 mm glass tube fuse (nominal 5x20), clip-mounted span.",
        }
        part["electrical"] = {
            "current_rating": "200mA",
            "interrupt_rating": "35A",
            "resettable": False,
            "device_type": "one-shot fuse",
            "operating_temperature": "-40 to +85 C",
            "mounting": "clip-mounted 5x20 glass tube (companion clips C3130)"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Fuse",
            "machine_solder": "Fuse:Fuseholder_Littelfuse_100_series_5x20mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Xucheng Elec 0.2A 250VACGlass Tube Fuse (C3128); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Fuse master and the Fuse:Fuseholder_Littelfuse_100_series_5x20mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5392 / Littelfuse RXEF010 - fuse family batch 2026-10-06
    current = "electronic_fuse_radial_5_08_mm_pitch_resettable_littelfuse_rxef010"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "radial-lead resettable PPTC (TE RXEF010), 5.08 mm offset radial leads, 7.4 x 6.6 x 3.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887202222366720-C5392.pdf"
        part["dimensions_mm"] = {"length": 7.4, "width": 6.6, "height": 3.0}
        part["dimension_reference"] = {
            "document": "RXEF010 datasheet (C5392 provenance)",
            "pages": [1],
            "notes": "radial-lead resettable PPTC (TE RXEF010), 5.08 mm offset radial leads, 7.4 x 6.6 x 3.0 mm body.",
        }
        part["electrical"] = {
            "interrupt_rating": "40A",
            "resettable": True,
            "device_type": "resettable PPTC fuse",
            "operating_temperature": "-40 to +85 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_Bourns_MF-RG500",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Littelfuse RXEF010 (C5392); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Polyfuse master and the Fuse:Fuse_Bourns_MF-RG500 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5395 / Littelfuse RUEF110 - fuse family batch 2026-10-06
    current = "electronic_fuse_radial_5_08_mm_pitch_resettable_littelfuse_ruef110"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "radial-lead resettable PPTC (TE RUEF110), 5.08 mm offset radial leads, 7.4 x 6.6 x 3.0 mm body"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887583602851840-C5395.pdf"
        part["dimensions_mm"] = {"length": 7.4, "width": 6.6, "height": 3.0}
        part["dimension_reference"] = {
            "document": "RUEF110 datasheet (C5395 provenance)",
            "pages": [1],
            "notes": "radial-lead resettable PPTC (TE RUEF110), 5.08 mm offset radial leads, 7.4 x 6.6 x 3.0 mm body.",
        }
        part["electrical"] = {
            "interrupt_rating": "100A",
            "resettable": True,
            "device_type": "resettable PPTC fuse",
            "operating_temperature": "-40 to +85 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_Bourns_MF-RG500",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Littelfuse RUEF110 (C5395); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Polyfuse master and the Fuse:Fuse_Bourns_MF-RG500 footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5418 / Littelfuse MINISMDC020F-2 - fuse family batch 2026-10-06
    current = "electronic_fuse_1812_resettable_littelfuse_minismdc020f_2"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "1812 (4532 metric) resettable PPTC, 4.5 x 3.2 x 2.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588907115751100416-C5418.pdf"
        part["dimensions_mm"] = {"length": 4.5, "width": 3.2, "height": 2.4}
        part["dimension_reference"] = {
            "document": "MINISMDC020F-2 datasheet (C5418 provenance)",
            "pages": [1],
            "notes": "1812 (4532 metric) resettable PPTC, 4.5 x 3.2 x 2.4 mm.",
        }
        part["electrical"] = {
            "interrupt_rating": "100A",
            "resettable": True,
            "device_type": "resettable PPTC fuse",
            "operating_temperature": "-40 C~+85 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_1812_4532Metric",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Littelfuse MINISMDC020F-2 (C5418); identity and ratings observed live at intake.",
            "Mapped to the KiCad Device:Polyfuse master and the Fuse:Fuse_1812_4532Metric footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated fuse batch (tmp/fuse_batch.py) ===