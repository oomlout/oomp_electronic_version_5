def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer_yxc"] = "X322512MSB4SI"
        extras_dict[current]["part_number_lcsc_yxc"] = "C9002"

    current = "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf_80_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf"
        part["category"] = "crystal"
        part["electrical"] = {
            "frequency": "12 MHz",
            "load_capacitance": "20 pF",
            "equivalent_series_resistance": "80 ohm",
            "frequency_tolerance": "+/-10 ppm",
            "frequency_stability": "+/-20 ppm",
            "operating_temperature": "-40 to +85 C",
        }
        part["research_notes"] = [
            "80 ohm ESR purchasing variant. The generic 12 MHz 20 pF choice retains its 50 ohm C133334 preference.",
            "Pad orientation and crystal pin mapping remain for the full pass.",
        ]

    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="crystal")

    # === BEGIN generated crystal batch (tmp/crystal_batch.py) — regenerated, do not hand-edit ===
    # JLC C115962 / YXC Crystal Oscillators X50328MSB2GI - crystal family batch 2026-10-06
    current = "electronic_crystal_5032_surface_mount_2_pin_8_mhz_20_pf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD 5032 2-pad glass-sealed crystal, 5.0 x 3.2 x 1.2 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756945667811872768-C115962.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 3.2, "height": 1.2}
        part["dimension_reference"] = {
            "document": "X50328MSB2GI datasheet (C115962 provenance)",
            "pages": [1],
            "notes": "SMD 5032 2-pad glass-sealed crystal, 5.0 x 3.2 x 1.2 mm.",
        }
        part["electrical"] = {
            "frequency": "8 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-40 C~+85 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_5032-2Pin_5.0x3.2mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD5032-2P YXC Crystal Oscillators X50328MSB2GI (C115962); identity and ratings observed live at intake 2026-09-24.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_5032-2Pin_5.0x3.2mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C12674 / YXC Crystal Oscillators X49SM8MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_8_mhz_20_pf_70_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C12674.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM8MSD2SC datasheet (C12674 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "8 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM8MSD2SC (C12674); identity and ratings observed live at intake 2026-09-24.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C13738 / YXC Crystal Oscillators X322516MLB4SI - crystal family batch 2026-10-06
    current = "electronic_crystal_3225_surface_mount_4_pin_16_mhz_9_pf_50_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD 3225 4-pad crystal, 3.2 x 2.5 x 0.7 mm (pads 1/3 terminals, 2/4 ground)"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C13738.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 2.5, "height": 0.7}
        part["dimension_reference"] = {
            "document": "X322516MLB4SI datasheet (C13738 provenance)",
            "pages": [1],
            "notes": "SMD 3225 4-pad crystal, 3.2 x 2.5 x 0.7 mm (pads 1/3 terminals, 2/4 ground).",
        }
        part["electrical"] = {
            "frequency": "16 MHz",
            "load_capacitance": "9pF",
            "operating_temperature": "-40 C~+85 C",
            "device_type": "quartz crystal",
            "padout": "pad 1 input, pad 3 output, pads 2 and 4 ground"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "G", "type": "passive"},
            "pin_3": {"number": "3", "name": "3", "type": "passive"},
            "pin_4": {"number": "4", "name": "G", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal_GND24",
            "machine_solder": "Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD3225-4P YXC Crystal Oscillators X322516MLB4SI (C13738); identity and ratings observed live at intake 2026-09-24.",
            "Mapped to the KiCad Device:Crystal_GND24 master and the Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2195 / YXC Crystal Oscillators X49SD3579545MSD2SC-1 - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_3_579545_mhz_20_pf_160_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947092063428608-C2195.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD3579545MSD2SC-1 datasheet (C2195 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "3.579545 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD3579545MSD2SC-1 (C2195); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2196 / YXC Crystal Oscillators X49SD36864MSD2SC-1 - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_3_6864_mhz_20_pf_160_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947149781381120-C2196.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD36864MSD2SC-1 datasheet (C2196 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "3.6864 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD36864MSD2SC-1 (C2196); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2198 / YXC Crystal Oscillators X49SD5MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_5_mhz_20_pf_80_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947215858311168-C2198.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD5MSD2SC datasheet (C2198 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "5 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD5MSD2SC (C2198); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2200 / YXC Crystal Oscillators X49SD73728MSD2SC-1 - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_7_3728_mhz_20_pf_70_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947219575005184-C2200.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD73728MSD2SC-1 datasheet (C2200 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "7.3728 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD73728MSD2SC-1 (C2200); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2202 / YXC Crystal Oscillators X49SD10MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_10_mhz_20_pf_60_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947223076708352-C2202.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD10MSD2SC datasheet (C2202 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "10 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD10MSD2SC (C2202); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2203 / YXC Crystal Oscillators X49SD110592MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_11_0592_mhz_20_pf_50_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947226335817728-C2203.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD110592MSD2SC datasheet (C2203 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "11.0592 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD110592MSD2SC (C2203); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2206 / YXC Crystal Oscillators X49SD1431818MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_14_31818_mhz_20_pf_50_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947229486010368-C2206.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD1431818MSD2SC datasheet (C2206 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "14.31818 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD1431818MSD2SC (C2206); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2210 / YXC Crystal Oscillators X49SD18432MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_18_432_mhz_20_pf_45_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947245264441344-C2210.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD18432MSD2SC datasheet (C2210 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "18.432 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD18432MSD2SC (C2210); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2212 / YXC Crystal Oscillators X49SD221184MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_22_1184_mhz_20_pf_45_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947248675086336-C2212.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD221184MSD2SC datasheet (C2212 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "22.1184 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD221184MSD2SC (C2212); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2213 / YXC Crystal Oscillators X49SD24MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_24_mhz_20_pf_35_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947251912683520-C2213.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD24MSD2SC datasheet (C2213 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "24 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD24MSD2SC (C2213); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2214 / YXC Crystal Oscillators X49SD24576MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_24_576_mhz_20_pf_35_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947255255949312-C2214.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD24576MSD2SC datasheet (C2214 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "24.576 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD24576MSD2SC (C2214); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2216 / YXC Crystal Oscillators X49SD27MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_27_mhz_20_pf_35_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947261232697344-C2216.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD27MSD2SC datasheet (C2216 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "27 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD27MSD2SC (C2216); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2220 / YXC Crystal Oscillators X49SD30MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_30_mhz_20_pf_35_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947267448655872-C2220.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD30MSD2SC datasheet (C2220 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "30 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD30MSD2SC (C2220); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2224 / YXC Crystal Oscillators X49SD49152MSD2SC-1 - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_4_9152_mhz_20_pf_120_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947274008276992-C2224.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD49152MSD2SC-1 datasheet (C2224 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "4.9152 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD49152MSD2SC-1 (C2224); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2226 / YXC Crystal Oscillators X49SD4096MSD2SC-1 - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_4_096_mhz_20_pf_120_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947277183770624-C2226.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD4096MSD2SC-1 datasheet (C2226 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "4.096 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD4096MSD2SC-1 (C2226); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2227 / YXC Crystal Oscillators X49SD26MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_26_mhz_20_pf_35_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947280404590592-C2227.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD26MSD2SC datasheet (C2227 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "26 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD26MSD2SC (C2227); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2228 / YXC Crystal Oscillators X49SD19.0699MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_through_hole_2_pin_19_0699_mhz_20_pf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895637760434176-C2228.pdf"
        part["dimensions_mm"] = {"length": 11.5, "width": 4.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "X49SD19.0699MSD2SC datasheet (C2228 provenance)",
            "pages": [1],
            "notes": "HC-49S (HC-49/US slim) through-hole can, 11.5 x 4.5 x 3.6 mm, 4.88 mm row spacing.",
        }
        part["electrical"] = {
            "frequency": "19.0699 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_HC49-U_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S YXC Crystal Oscillators X49SD19.0699MSD2SC (C2228); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_HC49-U_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2236 / YXC Crystal Oscillators X206032768KGB2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_dt_26_through_hole_2_pin_32_768_khz_12_5_pf_50000_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "DT-26 cylindrical 32.768 kHz tuning-fork crystal, D2.0 x 6.0 mm, vertical THT"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756945078508236800-C2236.pdf"
        part["dimensions_mm"] = {"length": 6.0, "width": 2.1, "height": 5.5}
        part["dimension_reference"] = {
            "document": "X206032768KGB2SC datasheet (C2236 provenance)",
            "pages": [1],
            "notes": "DT-26 cylindrical 32.768 kHz tuning-fork crystal, D2.0 x 6.0 mm, vertical THT.",
        }
        part["electrical"] = {
            "frequency": "32.768 kHz",
            "load_capacitance": "12.5pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_C26-LF_D2.1mm_L6.5mm_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists DT-26 YXC Crystal Oscillators X206032768KGB2SC (C2236); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_C26-LF_D2.1mm_L6.5mm_Vertical footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2237 / YXC Crystal Oscillators X49SM3579545MSD2SC-1 - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_3_579545_mhz_20_pf_160_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947286733930496-C2237.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM3579545MSD2SC-1 datasheet (C2237 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "3.579545 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM3579545MSD2SC-1 (C2237); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2238 / YXC Crystal Oscillators X49SM36864MSD2SC-1 - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_3_6864_mhz_20_pf_160_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947290026729472-C2238.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM36864MSD2SC-1 datasheet (C2238 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "3.6864 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM36864MSD2SC-1 (C2238); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2240 / YXC Crystal Oscillators X49SM5MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_5_mhz_20_pf_80_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947293113196544-C2240.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM5MSD2SC datasheet (C2240 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "5 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM5MSD2SC (C2240); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2242 / YXC Crystal Oscillators X49SM73728MSD2SC-1 - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_7_3728_mhz_20_pf_70_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947296410054656-C2242.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM73728MSD2SC-1 datasheet (C2242 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "7.3728 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM73728MSD2SC-1 (C2242); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2244 / YXC Crystal Oscillators X49SM10MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_10_mhz_20_pf_60_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947303901081600-C2244.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM10MSD2SC datasheet (C2244 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "10 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM10MSD2SC (C2244); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2245 / YXC Crystal Oscillators X49SM110592MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_11_0592_mhz_20_pf_50_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947307126636544-C2245.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM110592MSD2SC datasheet (C2245 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "11.0592 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM110592MSD2SC (C2245); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2247 / YXC Crystal Oscillators X49SM1356MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_13_56_mhz_20_pf_50_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947319658811392-C2247.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM1356MSD2SC datasheet (C2247 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "13.56 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM1356MSD2SC (C2247); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2250 / YXC Crystal Oscillators X49SM18432MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_18_432_mhz_20_pf_45_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947326143746048-C2250.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM18432MSD2SC datasheet (C2250 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "18.432 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM18432MSD2SC (C2250); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2252 / YXC Crystal Oscillators X49SM221184MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_22_1184_mhz_20_pf_45_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947329285009408-C2252.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM221184MSD2SC datasheet (C2252 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "22.1184 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM221184MSD2SC (C2252); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2253 / YXC Crystal Oscillators X49SM24MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_24_mhz_20_pf_35_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947332460097536-C2253.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM24MSD2SC datasheet (C2253 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "24 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM24MSD2SC (C2253); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2254 / YXC Crystal Oscillators X49SM24576MSD2SC - crystal family batch 2026-10-06
    current = "electronic_crystal_hc_49s_smd_surface_mount_2_pin_24_576_mhz_20_pf_35_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756947340018233344-C2254.pdf"
        part["dimensions_mm"] = {"length": 11.4, "width": 4.8, "height": 3.8}
        part["dimension_reference"] = {
            "document": "X49SM24576MSD2SC datasheet (C2254 provenance)",
            "pages": [1],
            "notes": "HC-49S SMD (bend leads), 11.4 x 4.8 x 3.8 mm.",
        }
        part["electrical"] = {
            "frequency": "24.576 MHz",
            "load_capacitance": "20pF",
            "operating_temperature": "-20 C~+70 C",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_HC49-SD",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HC-49S-SMD YXC Crystal Oscillators X49SM24576MSD2SC (C2254); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_HC49-SD footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C32346 / Seiko Epson Q13FC13500004 - crystal family batch 2026-10-06
    current = "electronic_crystal_3215_surface_mount_2_pin_32_768_khz_12_5_pf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD 3215 2-pad 32.768 kHz tuning-fork crystal, 3.2 x 1.5 x 0.9 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8629475189274984448-C32346.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.5, "height": 0.9}
        part["dimension_reference"] = {
            "document": "Q13FC13500004 datasheet (C32346 provenance)",
            "pages": [1],
            "notes": "SMD 3215 2-pad 32.768 kHz tuning-fork crystal, 3.2 x 1.5 x 0.9 mm.",
        }
        part["electrical"] = {
            "frequency": "32.768 kHz",
            "device_type": "quartz crystal"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal",
            "machine_solder": "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD3215-2P Seiko Epson Q13FC13500004 (C32346); identity and ratings observed live at intake 2026-09-24.",
            "Mapped to the KiCad Device:Crystal master and the Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C9002 / YXC Crystal Oscillators X322512MSB4SI - crystal family batch 2026-10-06
    current = "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf_80_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD 3225 4-pad crystal, 3.2 x 2.5 x 0.7 mm (pads 1/3 terminals, 2/4 ground)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756945081792782336-C9002.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 2.5, "height": 0.7}
        part["dimension_reference"] = {
            "document": "X322512MSB4SI datasheet (C9002 provenance)",
            "pages": [1],
            "notes": "SMD 3225 4-pad crystal, 3.2 x 2.5 x 0.7 mm (pads 1/3 terminals, 2/4 ground).",
        }
        part["electrical"] = {
            "frequency": "12 MHz",
            "device_type": "quartz crystal",
            "padout": "pad 1 input, pad 3 output, pads 2 and 4 ground"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "G", "type": "passive"},
            "pin_3": {"number": "3", "name": "3", "type": "passive"},
            "pin_4": {"number": "4", "name": "G", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal_GND24",
            "machine_solder": "Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD3225-4P YXC Crystal Oscillators X322512MSB4SI (C9002); identity and ratings observed live at intake 2026-09-24.",
            "Mapped to the KiCad Device:Crystal_GND24 master and the Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C9006 / YXC Crystal Oscillators X322525MOB4SI - crystal family batch 2026-10-06
    current = "electronic_crystal_3225_surface_mount_4_pin_25_mhz_12_pf_50_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD 3225 4-pad crystal, 3.2 x 2.5 x 0.7 mm (pads 1/3 terminals, 2/4 ground)"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C9006.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 2.5, "height": 0.7}
        part["dimension_reference"] = {
            "document": "X322525MOB4SI datasheet (C9006 provenance)",
            "pages": [1],
            "notes": "SMD 3225 4-pad crystal, 3.2 x 2.5 x 0.7 mm (pads 1/3 terminals, 2/4 ground).",
        }
        part["electrical"] = {
            "frequency": "25 MHz",
            "load_capacitance": "12pF",
            "operating_temperature": "-40 C~+85 C",
            "device_type": "quartz crystal",
            "padout": "pad 1 input, pad 3 output, pads 2 and 4 ground"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "G", "type": "passive"},
            "pin_3": {"number": "3", "name": "3", "type": "passive"},
            "pin_4": {"number": "4", "name": "G", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:Crystal_GND24",
            "machine_solder": "Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD3225-4P YXC Crystal Oscillators X322525MOB4SI (C9006); identity and ratings observed live at intake 2026-09-24.",
            "Mapped to the KiCad Device:Crystal_GND24 master and the Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated crystal batch (tmp/crystal_batch.py) ===