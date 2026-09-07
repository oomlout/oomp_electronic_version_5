def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_diode_tvs_array_sot_143_littelfuse_sp0503bahtg"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Littelfuse"
        part["part_number_manufacturer"] = "SP0503BAHTG"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["part_number_lcsc"] = "C7074"
        part["product_url"] = "https://www.lcsc.com/product-detail/C7074.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C7074.pdf"
        part["dimensions_mm"] = {"length": 2.92, "width": 2.37}
        part["dimension_reference"] = {"document": "Littelfuse SP05 Series, revised 08/12/15", "pages": [1, 3]}
        part["pins"] = {}
        for number, name in [["1", "gnd"], ["2", "io_1"], ["3", "io_2"], ["4", "io_3"]]:
            part["pins"]["pin_" + number] = {"number": number, "name": name, "type": "gnd" if number == "1" else "signal"}
        part["package_drawing"] = {
            "overall": [2.92, 2.37], "body": [2.92, 1.3],
            "pins": [["1", "bottom", -.76, -.9175, .825, .535],
                     ["2", "bottom", .96, -.9175, .4, .535],
                     ["3", "top", .96, .9175, .4, .535],
                     ["4", "top", -.96, .9175, .4, .535]],
            "pin_one": [-1.0, -.35],
        }
        part["kicad"] = {"symbol": "Power_Protection:SP0503BAHT", "machine_solder": "Package_TO_SOT_SMD:SOT-143", "hand_solder": "Package_TO_SOT_SMD:SOT-143_Handsoldering"}
        part["research_notes"] = ["Upstream ESD_Protection.pdf is a TECH PUBLIC document, not the Littelfuse BOM device; do not use that PDF as this part's datasheet."]

    current = "electronic_diode_tvs_array_sot_23_6_protek_srv054pt7"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "SRV05-4-P-T7"
        extras_dict[current]["part_number_lcsc"] = "C85364"

    current = "electronic_diode_switching_sod_523f_onsemi_1n4148wt"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "1N4148WT"
        extras_dict[current]["part_number_lcsc"] = "C232841"
        extras_dict[current]["manufacturer"] = "onsemi"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C232841.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C232841.pdf"
        extras_dict[current]["package_name_manufacturer"] = "SOD-523F"
        extras_dict[current]["electrical"] = {
            "maximum_dc_reverse_voltage": "75 V",
            "maximum_rectified_current": "300 mA",
            "maximum_power_dissipation": "200 mW",
            "reverse_recovery_time": "4 ns",
        }
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "cathode",
            "number": "1",
            "type": "passive",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "anode",
            "number": "2",
            "type": "passive",
        }

    current = "electronic_diode_schottky_dual_common_cathode_sot_523_diodes_incorporated_bas40t_05"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "BAS40T-05"
        extras_dict[current]["manufacturer"] = "Diodes Incorporated"
        extras_dict[current]["package_name_manufacturer"] = "SOT-523"
        extras_dict[current]["datasheet_url_legacy"] = "http://www.diodes.com/_files/datasheets/ds11005.pdf"
        extras_dict[current]["datasheet_status"] = "legacy project URL now redirects to the equivalent BAT54 family datasheet; no exact BAS40T-05 PDF was claimed"
        extras_dict[current]["research_notes"] = [
            "LCSC has no exact BAS40T-05 result and suggests BAS40W-05 instead.",
            "The bare MPN is retained without an invented -7 or -7-F order suffix.",
            "Bus Pirate uses the BAT54C common-cathode symbol and a SOT-523 footprint.",
        ]
        extras_dict[current]["electrical"] = {
            "maximum_dc_reverse_voltage": "40 V",
            "maximum_rectified_current": "200 mA",
            "configuration": "dual common cathode",
        }
        extras_dict[current]["diode_dimensions_mm"] = {
            "body_length": 1.6,
            "body_width": 0.8,
            "overall_width": 1.6,
        }
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "anode_1",
            "number": "1",
            "type": "passive",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "anode_2",
            "number": "2",
            "type": "passive",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "common_cathode",
            "number": "3",
            "type": "passive",
        }

    # Generic Schottky diodes
    current = "electronic_diode_schottky_sod_123_ss14"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Schottky Diode SOD-123 (generic)"
        part["name_readable"] = "Schottky Diode SOD-123 (generic)"
        part["name_proper"] = "Schottky Diode SOD-123 (generic)"
        part["dimensions_mm"] = {"length": 3.5, "width": 1.6}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky"],
            "symbols": ["Device:D_Schottky"],
            "footprints": ["Diode_SMD:D_SOD-123"],
        }

    current = "electronic_diode_schottky_sod_323_bat54w"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Schottky Diode SOD-323 (generic)"
        part["name_readable"] = "Schottky Diode SOD-323 (generic)"
        part["name_proper"] = "Schottky Diode SOD-323 (generic)"
        part["dimensions_mm"] = {"length": 2.1, "width": 1.25}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SOD-323",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky", "BAT60A", "PMEG4005EJ"],
            "symbols": ["Device:D_Schottky", "SparkFun-DiscreteSemi:D_Schottky_3A_10V_0.28V", "SparkFun-DiscreteSemi:D_Schottky_0.5A_40V_0.42V"],
            "footprints": ["Diode_SMD:D_SOD-323", "SparkFun-Semiconductor-Standard:SOD-323"],
        }

    current = "electronic_diode_schottky_sod_523_1ss400"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Schottky Diode SOD-523 (generic)"
        part["name_readable"] = "Schottky Diode SOD-523 (generic)"
        part["name_proper"] = "Schottky Diode SOD-523 (generic)"
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SOD-523",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky"],
            "symbols": ["Device:D_Schottky"],
            "footprints": ["Diode_SMD:D_SOD-523"],
        }

    # Stale generic entries (kept for compatibility)
    current = "electronic_diode_schottky_sod_123_generic_ss14"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Schottky Diode SOD-123 (generic)"
        part["name_readable"] = "Schottky Diode SOD-123 (generic)"
        part["name_proper"] = "Schottky Diode SOD-123 (generic)"
        part["dimensions_mm"] = {"length": 3.5, "width": 1.6}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky"],
            "symbols": ["Device:D_Schottky"],
            "footprints": ["Diode_SMD:D_SOD-123"],
        }

    current = "electronic_diode_schottky_sod_323_generic_bat54w"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Schottky Diode SOD-323 (generic)"
        part["name_readable"] = "Schottky Diode SOD-323 (generic)"
        part["name_proper"] = "Schottky Diode SOD-323 (generic)"
        part["dimensions_mm"] = {"length": 2.1, "width": 1.25}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SOD-323",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky", "BAT60A", "PMEG4005EJ"],
            "symbols": ["Device:D_Schottky", "SparkFun-DiscreteSemi:D_Schottky_3A_10V_0.28V", "SparkFun-DiscreteSemi:D_Schottky_0.5A_40V_0.42V"],
            "footprints": ["Diode_SMD:D_SOD-323", "SparkFun-Semiconductor-Standard:SOD-323"],
        }

    current = "electronic_diode_schottky_sod_523_generic_1ss400"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Schottky Diode SOD-523 (generic)"
        part["name_readable"] = "Schottky Diode SOD-523 (generic)"
        part["name_proper"] = "Schottky Diode SOD-523 (generic)"
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SOD-523",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky"],
            "symbols": ["Device:D_Schottky"],
            "footprints": ["Diode_SMD:D_0402_1005Metric", "Diode_SMD:D_SOD-523"],
        }

    # SparkFun-specific diodes/protection
    current = "electronic_diode_tvs_sot_353_toshiba_df5a5_6lfu"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Toshiba"
        part["part_number_manufacturer"] = "DF5A5.6LFU"
        part["part_number_lcsc"] = "C5445"
        part["product_url"] = "https://www.lcsc.com/product-detail/C5445.html"
        part["datasheet_url"] = "https://www.toshiba.semicon-storage.com/info/docget.jsp?did=22260&prodname=df5a5.6lfu"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode_1", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
            "pin_3": {"number": "3", "name": "cathode_2", "type": "passive"},
            "pin_4": {"number": "4", "name": "cathode_3", "type": "passive"},
            "pin_5": {"number": "5", "name": "cathode_4", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Power_Protection:DF5A5.6LFU",
            "machine_solder": "Package_TO_SOT_SMD:SOT-353",
            "hand_solder": "",
        }

    current = "electronic_diode_esd_0402_littelfuse_pesd0402"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Littelfuse"
        part["part_number_manufacturer"] = "PESD0402"
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~", "type": "passive"},
            "pin_2": {"number": "2", "name": "~", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Power_Protection:TVS",
            "machine_solder": "Diode_SMD:D_0402_1005Metric",
            "hand_solder": "",
        }

    current = "electronic_diode_esd_array_sot_353_nexperia_pesd3v3l4ug"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Nexperia"
        part["part_number_manufacturer"] = "PESD3V3L4UG"
        part["part_number_lcsc"] = "C70500"
        part["product_url"] = "https://www.lcsc.com/product-detail/C70500.html"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode_1", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
            "pin_3": {"number": "3", "name": "cathode_2", "type": "passive"},
            "pin_4": {"number": "4", "name": "cathode_3", "type": "passive"},
            "pin_5": {"number": "5", "name": "cathode_4", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Power_Protection:PESDxL4UF",
            "machine_solder": "Package_TO_SOT_SMD:SOT-353",
            "hand_solder": "",
        }

    current = "electronic_diode_tvs_array_sot_26_diodes_incorporated_dt1042_04so"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Diodes Incorporated"
        part["part_number_manufacturer"] = "DT1042-04SO"
        part["part_number_lcsc"] = "C460064"
        part["product_url"] = "https://www.lcsc.com/product-detail/C460064.html"
        part["dimensions_mm"] = {"length": 3.0, "width": 1.6}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "io_1", "type": "signal"},
            "pin_2": {"number": "2", "name": "io_2", "type": "signal"},
            "pin_3": {"number": "3", "name": "gnd", "type": "gnd"},
            "pin_4": {"number": "4", "name": "io_3", "type": "signal"},
            "pin_5": {"number": "5", "name": "vcc", "type": "power"},
            "pin_6": {"number": "6", "name": "io_4", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Power_Protection:SRV05-4",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23-6",
            "hand_solder": "",
        }

    current = "electronic_diode_schottky_sod_323_infineon_bat60a"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Infineon"
        part["part_number_manufacturer"] = "BAT60A"
        part["part_number_lcsc"] = "C520634"
        part["product_url"] = "https://www.lcsc.com/product-detail/C520634.html"
        part["dimensions_mm"] = {"length": 2.1, "width": 1.25}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SOD-323",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky", "BAT60A"],
            "symbols": ["Device:D_Schottky"],
            "footprints": ["Diode_SMD:D_SOD-323"],
        }
