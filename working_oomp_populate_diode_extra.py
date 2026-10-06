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

    current = "electronic_diode_switching_sod_123_jiangsu_changjing_electronics_technology_co_ltd_1n4148w"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Jiangsu Changjing Electronics Technology Co., Ltd."
        part["part_number_manufacturer"] = "1N4148W"
        part["part_number_lcsc"] = "C2099"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2099.html"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710253822164992-C2099.pdf"
        part["package_name_manufacturer"] = "SOD-123"
        part["electrical"] = {
            "maximum_dc_reverse_voltage": "100 V",
            "maximum_rectified_current": "150 mA",
            "maximum_power_dissipation": "500 mW",
            "forward_voltage_at_test_current": "1.25 V at 150 mA",
            "reverse_recovery_time": "4 ns",
            "non_repetitive_peak_forward_surge_current": "2 A",
            "reverse_leakage_current": "1 uA at 75 V",
        }

    # JLC C2128 / Jiangsu Changjing 1N4148WS full-stage technical data,
    # verified against the Changjing BAV16WS/1N4148WS SOD-323 specification
    # (May 2011, browser-downloaded to this part; anchors the SOD-323
    # switching-diode family): maximum ratings page 1 - VR 100 V (RMS 71 V),
    # IFM 300 mA, IO 150 mA, IFSM 2.0 A @1 us, Pd 200 mW, RthJA 625 C/W,
    # Tj 150 C, Tstg -55 to +150 C; electrical ratings page 1 - VF 1.25 V at
    # IF = 150 mA (0.715 V @1 mA, 0.855 V @10 mA, 1.0 V @50 mA), IR 1 uA at
    # VR = 75 V, CT 2 pF, trr 4 ns; marking T6/T4. Package SOD-323: body
    # 1.70 x 1.30 mm, H 0.95 mm per the EIA SC-76 outline used by the KiCad
    # Diode_SMD:D_SOD-323 master. Live JLC description confirms the same
    # ratings. Pin 1 = cathode (KiCad D_SOD-323 pad 1 = K), pin 2 = anode.
    current = "electronic_diode_switching_sod_323_onsemi_1n4148ws"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOD-323 (SC-76)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707645118504960-C2128.pdf"
        part["dimensions_mm"] = {"length": 1.7, "width": 1.3, "height": 0.95}
        part["dimension_reference"] = {
            "document": "Changjing BAV16WS/1N4148WS SOD-323 specification, May 2011 (C2128)",
            "pages": [1, 2],
            "notes": "SOD-323 / EIA SC-76 outline: body 1.70 x 1.30 mm, height 0.95 mm; the 2-page datasheet carries no dimension drawing, so the outline follows the KiCad Diode_SMD:D_SOD-323 master geometry.",
        }
        part["electrical"] = {
            "maximum_dc_reverse_voltage": "100 V (RMS 71 V)",
            "maximum_rectified_current": "150 mA (continuous forward 300 mA)",
            "maximum_power_dissipation": "200 mW",
            "forward_voltage_at_test_current": "1.25 V at 150 mA",
            "reverse_recovery_time": "4 ns",
            "non_repetitive_peak_forward_surge_current": "2 A (t = 1 us)",
            "reverse_leakage_current": "1 uA at 75 V",
            "terminal_capacitance": "2 pF (VR = 0 V, f = 1 MHz)",
            "operating_temperature": "-55 to +150 C (storage; Tj 150 C)",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_SMD:D_SOD-323",
            "hand_solder": "Diode_SMD:D_SOD-323",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing 1N4148WS (C2128): 100 V, 150 mA switching diode in SOD-323; reconfirmed live 2026-10-01 (stock 2,452,437).",
            "Browser-downloaded the Changjing BAV16WS/1N4148WS SOD-323 datasheet (2 pages, May 2011) into this part; it anchors the SOD-323 switching-diode family.",
            "Pin 1 = K (cathode), pin 2 = A (anode); the KiCad Diode_SMD:D_SOD-323 master has pad 1 as cathode, matching.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2480 / MDD SS14 full-stage technical data, verified against the
    # MDD SS12-SS1200 SMA series specification (Rev 2025A5,
    # browser-downloaded to this part; anchors the SMA schottky family):
    # the ratings table column blocks (rendered page 1) give for SS14 -
    # VRRM 40 V (VRMS 28 V, VDC 40 V), I(AV) 1.0 A, IFSM 25 A (8.3 ms JEDEC),
    # VF max 0.70 V at 1.0 A (the 0.70 column block spans SS13-SS14), IR
    # 0.3 mA max at 25 C / 10 mA at 100 C at rated voltage, CJ 110 pF,
    # RthJA 90 C/W, TJ/TSTG -55 to +150 C; mechanical data - JEDEC
    # DO-214AC/SMA molded body, color band denotes the cathode end. Body
    # 4.50 x 2.80 x 2.30 mm, 5.30 mm overall including terminal ends, per
    # the mechanical numbers; pad geometry follows the KiCad Diode_SMD:D_SMA
    # master. Note: the live JLC description cites 550 mV @1 A, which
    # contradicts the vendor table (0.70 V for SS14; 550 mV is the SS12
    # column) - the vendor datasheet governs. Pin 1 = K (banded end),
    # pin 2 = A.
    current = "electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss14"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMA (JEDEC DO-214AC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757911605285789697-C2480.pdf"
        part["dimensions_mm"] = {"length": 4.5, "width": 2.8, "height": 2.3}
        part["dimension_reference"] = {
            "document": "MDD SS12-SS1200 SMA series specification, Rev 2025A5 (C2480)",
            "pages": [1],
            "notes": "JEDEC DO-214AC/SMA molded body: 4.50 x 2.80 x 2.30 mm body, 5.30 mm overall including terminal ends (mechanical data page 1); pad geometry per the KiCad Diode_SMD:D_SMA master; color band = cathode.",
        }
        part["electrical"] = {
            "maximum_dc_reverse_voltage": "40 V (VRRM; VRMS 28 V)",
            "maximum_rectified_current": "1.0 A average forward rectified",
            "forward_voltage_at_test_current": "0.70 V max at 1.0 A",
            "non_repetitive_peak_forward_surge_current": "25 A (8.3 ms half sine, JEDEC)",
            "reverse_leakage_current": "0.3 mA max at 25 C, rated voltage (10 mA at 100 C)",
            "terminal_capacitance": "110 pF typical (1 MHz, VR = 4.0 V)",
            "thermal_resistance": "90 C/W junction to ambient",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SMA",
            "hand_solder": "Diode_SMD:D_SMA_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic MDD SS14 (C2480): 40 V 1.0 A schottky rectifier in SMA (DO-214AC); reconfirmed live 2026-10-02 (stock 1,170,064).",
            "Browser-downloaded the MDD SS12-SS1200 series datasheet (3 pages, Rev 2025A5) into this part; it anchors the SMA schottky family (SS12-SS1200 columns).",
            "VF discrepancy recorded: the live JLC description cites 550 mV @1 A, but the vendor table's 0.70 V column block spans SS13-SS14 (550 mV is the SS12 column) - the vendor datasheet governs, 0.70 V recorded.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2488 / MDD MB10S-50MIL full-stage technical data, verified against
    # the MDD MB1S-MB10S MBS series specification (Rev 2024A2,
    # browser-downloaded to this part; anchors the MBS bridge family):
    # ratings table page 1 - MB10S column: VRRM 1000 V (VRMS 700 V, VDC
    # 1000 V), I(AV) 1.0 A at TC = 115 C, IFSM 35 A (8.3 ms JEDEC), VF 1.1 V
    # per leg at 1.0 A, IR 5.0 uA at 25 C / 40 uA at 125 C at rated voltage,
    # CJ 13 pF per leg, RthJA/RthJC 85/25 C/W, Tj/Tstg -55 to +150 C;
    # mechanical data page 1 - JEDEC MBS molded body, polarity symbol
    # marking on body, drawing pins (2)(1) top and (3)(4) bottom with + on
    # the right and - on the left: physical pinout 1 = + (DC out), 2 = ~
    # (AC in), 3 = - (DC out), 4 = ~ (AC in), matching the KiCad
    # Device:D_Bridge_+A-A symbol (pin 1 +, pin 3 -, pins 2/4 AC)
    # pad-for-pad with the Diode_Bridge_Vishay_MBLS footprint (the closest
    # official master; MBS-compatible outline). Outline: body ~4.5-4.9 mm
    # long, 2.6 mm wide, 7.0 mm max overall with leads, 3.0 mm max height.
    current = "electronic_diode_bridge_rectifier_mbs_mdd_microdiode_semiconductor_mb10s_50mil"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "MBS (JEDEC bridge rectifier outline, 50 mil pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707626420436992-C2488.pdf"
        part["dimensions_mm"] = {"length": 4.6, "width": 2.6, "height": 2.2}
        part["dimension_reference"] = {
            "document": "MDD MB1S-MB10S MBS series specification, Rev 2024A2 (C2488)",
            "pages": [1],
            "notes": "JEDEC MBS molded body: 4.5-4.9 mm body length (7.0 mm max overall with leads), 2.6 mm width, 2.2 mm body height (3.0 mm max); polarity symbol on body; pad geometry per the KiCad Diode_Bridge_Vishay_MBLS master.",
        }
        part["electrical"] = {
            "maximum_dc_reverse_voltage": "1000 V (VRRM; VRMS 700 V)",
            "maximum_rectified_current": "1.0 A average forward at TC = 115 C",
            "forward_voltage_at_test_current": "1.1 V max per leg at 1.0 A",
            "non_repetitive_peak_forward_surge_current": "35 A (8.3 ms half sine, JEDEC)",
            "reverse_leakage_current": "5.0 uA max at 25 C, rated voltage (40 uA at 125 C)",
            "terminal_capacitance": "13 pF per leg (1 MHz, VR = 4 V)",
            "thermal_resistance": "85 C/W per leg junction to ambient (25 C/W junction to case)",
            "operating_temperature": "-55 to +150 C",
            "configuration": "single-phase glass-passivated bridge (4 diodes)",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "+", "type": "passive"},
            "pin_2": {"number": "2", "name": "~", "type": "passive"},
            "pin_3": {"number": "3", "name": "-", "type": "passive"},
            "pin_4": {"number": "4", "name": "~", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_SMD:Diode_Bridge_Vishay_MBLS",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic MDD MB10S-50MIL (C2488): 1000 V 1.0 A single-phase bridge rectifier in MBS; reconfirmed live 2026-10-02 (stock 674,978).",
            "Browser-downloaded the MDD MB1S-MB10S series datasheet (3 pages, Rev 2024A2) into this part; it anchors the MBS bridge family (MB1S-MB10S voltage columns).",
            "Pinout per the page 1 drawing: pins (2)(1) on the top edge and (3)(4) on the bottom edge with + on the right and - on the left, giving 1 = +, 2 = ~, 3 = -, 4 = ~; the KiCad Device:D_Bridge_+A-A symbol pairs pad-for-pad with Diode_Bridge_Vishay_MBLS.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2500 / Nexperia BAV99,215 full-stage technical data, verified
    # against the Nexperia BAV99 product data sheet (1 July 2022,
    # browser-downloaded to this part; anchors the SOT-23 dual switching
    # diode family): high-speed switching diode pair in series connection,
    # SOT23 (TO-236AB). Pinning table 2: pin 1 = A1 (anode diode 1), pin 2
    # = K2 (cathode diode 2), pin 3 = K1/A2 (series common). Limiting
    # values table 5: VR 100 V per diode, IF 215 mA single diode loaded /
    # 125 mA double diode loaded, IFRM 500 mA, IFSM 0.5 A (tp = 1 s), Ptot
    # 250 mW, Tj 150 C; quick reference page 1: trr <= 4 ns, Cd <= 1.5 pF,
    # IR <= 0.5 uA at VR = 80 V; the live JLC description adds VF 1.25 V at
    # 150 mA. POLARITY MIRROR recorded: the KiCad Diode:BAV99 symbol numbers
    # its pins 1 = K / 2 = A / 3 = junction, mirrored vs the Nexperia
    # pinning (1 = A1, 2 = K2) - real designs must compensate (custom
    # symbol or pin swap) before assembly.
    current = "electronic_diode_switching_dual_series_sot_23_nexperia_bav99_215"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (TO-236AB)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707661585616896-C2500.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.0}
        part["dimension_reference"] = {
            "document": "Nexperia BAV99 product data sheet, 1 July 2022 (C2500)",
            "pages": [2, 4],
            "notes": "SOT23 (TO-236AB) outline per the Package_TO_SOT_SMD:SOT-23 master geometry; the datasheet package drawing carries the outline and pinning.",
        }
        part["electrical"] = {
            "configuration": "dual high-speed switching diode, series connection",
            "maximum_dc_reverse_voltage": "100 V per diode",
            "maximum_rectified_current": "215 mA single diode loaded (125 mA double diode loaded)",
            "forward_voltage_at_test_current": "1.25 V at 150 mA (per the live JLC description)",
            "reverse_recovery_time": "4 ns max (IF = 10 mA, IR = 10 mA)",
            "non_repetitive_peak_forward_surge_current": "0.5 A (tp = 1 s); IFRM 500 mA (tp = 1 us)",
            "reverse_leakage_current": "0.5 uA max at VR = 80 V",
            "diode_capacitance": "1.5 pF max",
            "power_dissipation": "250 mW per device (Tamb <= 25 C)",
            "operating_temperature": "-55 to +150 C (Tj)",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A1", "type": "signal"},
            "pin_2": {"number": "2", "name": "K2", "type": "signal"},
            "pin_3": {"number": "3", "name": "K1_A2", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BAV99",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Nexperia BAV99,215 (C2500): dual series switching diode, 100 V, 215 mA, 4 ns in SOT-23; reconfirmed live 2026-10-02 (stock 1,146,158).",
            "Browser-downloaded the Nexperia BAV99 product data sheet (10 pages, 1 July 2022) into this part; it anchors the SOT-23 dual switching diode family.",
            "POLARITY MIRROR: the pinning table gives 1 = A1, 2 = K2, 3 = K1/A2, but the KiCad Diode:BAV99 symbol numbers pins 1 = K / 2 = A / 3 = junction - mirrored vs the vendor; designs must compensate (custom symbol or pin swap) before assembly.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # Apply individually reviewed JLC house choices after other supplier data.
    # === BEGIN generated family batch (tmp/zener_batch.py) — regenerated, do not hand-edit ===
    # JLC C2103 / Changjing BZT52C10 10 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710284371988480-C2103.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "10 V at IZT 5 mA",
            "zener_tolerance": "+-5% (9.5 to 10.5 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "200nA at rated voltage",
            "dynamic_impedance": "ZZT 20Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2103 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C10 (C2103): 10 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 10 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2104 / Changjing BZT52C15 15 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c15"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710288020623360-C2104.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "15 V at IZT 5 mA",
            "zener_tolerance": "+-5% (14.25 to 15.75 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "100nA at rated voltage",
            "dynamic_impedance": "ZZT 30Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2104 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C15 (C2104): 15 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 15 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2105 / Changjing BZT52C16 16 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c16"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710296032018432-C2105.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "16 V at IZT 5 mA",
            "zener_tolerance": "+-5% (15.2 to 16.8 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "100nA at rated voltage",
            "dynamic_impedance": "ZZT 40Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2105 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C16 (C2105): 16 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 16 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2107 / Changjing BZT52C20 20 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c20"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710314436214784-C2107.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "20 V at IZT 5 mA",
            "zener_tolerance": "+-5% (19 to 21 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "100nA at rated voltage",
            "dynamic_impedance": "ZZT 55Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2107 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C20 (C2107): 20 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 20 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2108 / Changjing BZT52C22 22 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c22"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710317846593536-C2108.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "22 V at IZT 5 mA",
            "zener_tolerance": "+-5% (20.9 to 23.1 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "100nA at rated voltage",
            "dynamic_impedance": "ZZT 55Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2108 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C22 (C2108): 22 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 22 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2109 / Changjing BZT52C24 24 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c24"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710321467899904-C2109.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "24 V at IZT 5 mA",
            "zener_tolerance": "+-5% (22.8 to 25.2 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "100nA at rated voltage",
            "dynamic_impedance": "ZZT 70Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2109 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C24 (C2109): 24 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 24 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2110 / Changjing BZT52C33 33 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c33"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710325863530496-C2110.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "33 V at IZT 5 mA",
            "zener_tolerance": "+-5% (31.35 to 34.65 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "100nA at rated voltage",
            "dynamic_impedance": "ZZT 80Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2110 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C33 (C2110): 33 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 33 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2111 / Changjing BZT52C39 39 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c39"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710329888440320-C2111.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "39 V at IZT 5 mA",
            "zener_tolerance": "+-5% (37.05 to 40.95 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "100nA at rated voltage",
            "dynamic_impedance": "ZZT 130Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2111 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C39 (C2111): 39 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 39 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2112 / Changjing BZT52C3V3 3.3 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c3v3"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710333424099328-C2112.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "3.3 V at IZT 5 mA",
            "zener_tolerance": "+-5% (3.135 to 3.465 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "5uA at rated voltage",
            "dynamic_impedance": "ZZT 95Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2112 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C3V3 (C2112): 3.3 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 3.3 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2113 / Changjing BZT52C3V6 3.6 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c3v6"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710337375408128-C2113.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "3.6 V at IZT 5 mA",
            "zener_tolerance": "+-5% (3.42 to 3.78 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "5uA at rated voltage",
            "dynamic_impedance": "ZZT 90Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2113 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C3V6 (C2113): 3.6 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 3.6 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2114 / Changjing BZT52C3V9 3.9 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c3v9"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710340640063488-C2114.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "3.9 V at IZT 5 mA",
            "zener_tolerance": "+-5% (3.705 to 4.095 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "3uA at rated voltage",
            "dynamic_impedance": "ZZT 90Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2114 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C3V9 (C2114): 3.9 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 3.9 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2115 / Changjing BZT52C4V3 4.3 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c4v3"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586185287675858944-C2115.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "4.3 V at IZT 5 mA",
            "zener_tolerance": "+-5% (4.085 to 4.515 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "3uA at rated voltage",
            "dynamic_impedance": "ZZT 90Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2115 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C4V3 (C2115): 4.3 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 4.3 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2116 / Changjing BZT52C4V7 4.7 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c4v7"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710344148934656-C2116.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "4.7 V at IZT 5 mA",
            "zener_tolerance": "+-5% (4.465 to 4.935 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "3uA at rated voltage",
            "dynamic_impedance": "ZZT 80Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2116 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C4V7 (C2116): 4.7 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 4.7 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2117 / Changjing BZT52C5V1 5.1 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c5v1"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710347718426624-C2117.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "5.1 V at IZT 5 mA",
            "zener_tolerance": "+-5% (4.845 to 5.355 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "2uA at rated voltage",
            "dynamic_impedance": "ZZT 60Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2117 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C5V1 (C2117): 5.1 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 5.1 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2119 / Changjing BZT52C5V6 5.6 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c5v6"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710355201200128-C2119.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "5.6 V at IZT 5 mA",
            "zener_tolerance": "+-5% (5.32 to 5.88 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "1uA at rated voltage",
            "dynamic_impedance": "ZZT 40Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2119 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C5V6 (C2119): 5.6 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 5.6 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2120 / Changjing BZT52C6V8 6.8 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c6v8"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710359340568576-C2120.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "6.8 V at IZT 5 mA",
            "zener_tolerance": "+-5% (6.46 to 7.14 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "2uA at rated voltage",
            "dynamic_impedance": "ZZT 15Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2120 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C6V8 (C2120): 6.8 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 6.8 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2121 / Changjing BZT52C7V5 7.5 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c7v5"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710362662866944-C2121.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "7.5 V at IZT 5 mA",
            "zener_tolerance": "+-5% (7.125 to 7.875 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "1uA at rated voltage",
            "dynamic_impedance": "ZZT 15Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2121 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C7V5 (C2121): 7.5 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 7.5 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2122 / Changjing BZT52C8V2 8.2 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c8v2_wd"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586185288741212160-C2122.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "8.2 V at IZT 5 mA",
            "zener_tolerance": "+-5% (7.79 to 8.61 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "700nA at rated voltage",
            "dynamic_impedance": "ZZT 15Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2122 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C8V2 (C2122): 8.2 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 8.2 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2123 / Changjing BZT52C9V1 9.1 V zener (generated family batch 2026-10-04)
    current = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c9v1"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10"
        part["package_name_manufacturer"] = "SOD-123"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710365871235072-C2123.pdf"
        part["electrical"] = {
            "zener_voltage_nominal": "9.1 V at IZT 5 mA",
            "zener_tolerance": "+-5% (8.645 to 9.555 V)",
            "power_dissipation": "500 mW (ceramic PCB derating)",
            "forward_voltage": "0.9 V at IF = 10 mA",
            "reverse_leakage_current": "500nA at rated voltage",
            "dynamic_impedance": "ZZT 15Ω max",
            "operating_temperature": "-55 to +150 C (Tj and storage)",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 1.25, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing BZT52C2V4-BZT52C43 zener specification Rev 2.1, package outline page 4 (C2123 provenance)",
            "pages": [4],
            "notes": "SOD-123 body D 1.50-1.70 mm long, A2 1.05-1.15 mm high, A max 1.25 mm; E 2.60-2.80 mm terminal span, E1 3.55-3.85 mm overall length. Pad geometry follows the KiCad Diode_SMD:D_SOD-123 master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Diode:BZT52Bxx",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "Diode_SMD:D_SOD-123",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing BZT52C9V1 (C2123): 9.1 V zener, 500 mW, SOD-123; identity and ratings observed live at intake 2026-09-28.",
            "Family batch 2026-10-04 over the shared Changjing BZT52C2V4-BZT52C43 datasheet (oomp_datasheet_common_with = electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10): the ratings table pages 1-2 give the 9.1 V row and the package outline page 4 gives SOD-123 dimensions. Pin 1 = cathode (marked end), pin 2 = anode; KiCad D_SOD-123 pad 1 is the cathode. Symbol Diode:BZT52Bxx is the only BZT52 symbol KiCad 10 ships - the B/C tolerance series share the same xx-template symbol graphics; the tolerance lives in the part number.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated family batch (tmp/zener_batch.py) ===

    # === BEGIN generated family batch (tmp/sma_batch.py) — regenerated, do not hand-edit ===
    # JLC C2479 / MDD SS12 SMA schottky (generated family batch 2026-10-04)
    current = "electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss12"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss14"
        part["package_name_manufacturer"] = "SMA (DO-214AC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756679312927789056-C2479.pdf"
        part["electrical"] = {
            "maximum_dc_reverse_voltage": "20 V (VRRM)",
            "maximum_rectified_current": "1.0 A average forward rectified",
            "forward_voltage_at_test_current": "0.55 V max at 1.0 A (vendor table column; the live JLC description cites 550mV@1A)",
            "non_repetitive_peak_forward_surge_current": "25 A (8.3 ms half sine, JEDEC)",
            "reverse_leakage_current": "0.3 mA max at 25 C at rated voltage (10 mA at 100 C); live JLC lists 300uA@20V",
            "terminal_capacitance": "110 pF typical (1 MHz)",
            "thermal_resistance": "90 C/W junction to ambient",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 4.5, "width": 2.8, "height": 2.3}
        part["dimension_reference"] = {
            "document": "MDD SS12-SS1200 SMA specification Rev 2025A5, mechanical data page 3 (C2479 provenance)",
            "pages": [3],
            "notes": "JEDEC DO-214AC/SMA molded body 4.50 x 2.80 x 2.30 mm, 5.30 mm overall including terminal ends; color band denotes the cathode. Pad geometry follows the KiCad Diode_SMD:D_SMA master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SMA",
            "hand_solder": "Diode_SMD:D_SMA_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic MDD SS12 (C2479): 20 V 1.0 A schottky rectifier in SMA (DO-214AC); identity and ratings observed live at intake 2026-09-29.",
            "Family batch 2026-10-04 over the shared MDD SS12-SS1200 datasheet (oomp_datasheet_common_with = electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss14): the ratings table column block for SS12 gives VF 0.55 V max at 1.0 A and the mechanical page gives the DO-214AC outline. Pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2481 / MDD SS16 SMA schottky (generated family batch 2026-10-04)
    current = "electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss16"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss14"
        part["package_name_manufacturer"] = "SMA (DO-214AC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757911609207734272-C2481.pdf"
        part["electrical"] = {
            "maximum_dc_reverse_voltage": "60 V (VRRM)",
            "maximum_rectified_current": "1.0 A average forward rectified",
            "forward_voltage_at_test_current": "0.70 V max at 1.0 A (vendor table column; the live JLC description cites 700mV@1A)",
            "non_repetitive_peak_forward_surge_current": "25 A (8.3 ms half sine, JEDEC)",
            "reverse_leakage_current": "0.3 mA max at 25 C at rated voltage (10 mA at 100 C); live JLC lists 300uA@60V",
            "terminal_capacitance": "110 pF typical (1 MHz)",
            "thermal_resistance": "90 C/W junction to ambient",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 4.5, "width": 2.8, "height": 2.3}
        part["dimension_reference"] = {
            "document": "MDD SS12-SS1200 SMA specification Rev 2025A5, mechanical data page 3 (C2481 provenance)",
            "pages": [3],
            "notes": "JEDEC DO-214AC/SMA molded body 4.50 x 2.80 x 2.30 mm, 5.30 mm overall including terminal ends; color band denotes the cathode. Pad geometry follows the KiCad Diode_SMD:D_SMA master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SMA",
            "hand_solder": "Diode_SMD:D_SMA_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic MDD SS16 (C2481): 60 V 1.0 A schottky rectifier in SMA (DO-214AC); identity and ratings observed live at intake 2026-09-29.",
            "Family batch 2026-10-04 over the shared MDD SS12-SS1200 datasheet (oomp_datasheet_common_with = electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss14): the ratings table column block for SS16 gives VF 0.70 V max at 1.0 A and the mechanical page gives the DO-214AC outline. Pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2482 / MDD SS110 SMA schottky (generated family batch 2026-10-04)
    current = "electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss110"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss14"
        part["package_name_manufacturer"] = "SMA (DO-214AC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757911614610132992-C2482.pdf"
        part["electrical"] = {
            "maximum_dc_reverse_voltage": "100 V (VRRM)",
            "maximum_rectified_current": "1.0 A average forward rectified",
            "forward_voltage_at_test_current": "0.85 V max at 1.0 A (vendor table column; the live JLC description cites 850mV@1A)",
            "non_repetitive_peak_forward_surge_current": "25 A (8.3 ms half sine, JEDEC)",
            "reverse_leakage_current": "0.3 mA max at 25 C at rated voltage (10 mA at 100 C); live JLC lists 200uA@100V",
            "terminal_capacitance": "110 pF typical (1 MHz)",
            "thermal_resistance": "90 C/W junction to ambient",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 4.5, "width": 2.8, "height": 2.3}
        part["dimension_reference"] = {
            "document": "MDD SS12-SS1200 SMA specification Rev 2025A5, mechanical data page 3 (C2482 provenance)",
            "pages": [3],
            "notes": "JEDEC DO-214AC/SMA molded body 4.50 x 2.80 x 2.30 mm, 5.30 mm overall including terminal ends; color band denotes the cathode. Pad geometry follows the KiCad Diode_SMD:D_SMA master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SMA",
            "hand_solder": "Diode_SMD:D_SMA_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic MDD SS110 (C2482): 100 V 1.0 A schottky rectifier in SMA (DO-214AC); identity and ratings observed live at intake 2026-09-29.",
            "Family batch 2026-10-04 over the shared MDD SS12-SS1200 datasheet (oomp_datasheet_common_with = electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss14): the ratings table column block for SS110 gives VF 0.85 V max at 1.0 A and the mechanical page gives the DO-214AC outline. Pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated family batch (tmp/sma_batch.py) ===

    # === BEGIN generated family batch (tmp/sma_anchors.py) — regenerated, do not hand-edit ===
    # JLC C8678 / MDD SS34 SMA schottky - anchor of the SS32 THRU SS3200 (3.0 A), Rev 2024A5 family (generated 2026-10-04)
    current = "electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss34"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMA (DO-214AC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586172667476496384-C8678.pdf"
        part["electrical"] = {
            "maximum_dc_reverse_voltage": "40 V (VRRM)",
            "maximum_rectified_current": "3.0 A average forward rectified",
            "forward_voltage_at_test_current": "0.55 V at 3.0 A max",
            "non_repetitive_peak_forward_surge_current": "80 A (8.3 ms half sine, JEDEC)",
            "reverse_leakage_current": "500 uA at 40 V max at 25 C at rated voltage",
            "thermal_resistance": "see specification page 1",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 4.5, "width": 2.8, "height": 2.3}
        part["dimension_reference"] = {
            "document": "MDD SS32 THRU SS3200 (3.0 A), Rev 2024A5 specification, mechanical data page 3 (C8678 provenance)",
            "pages": [3],
            "notes": "JEDEC DO-214AC/SMA molded body 4.50 x 2.80 x 2.30 mm, 5.30 mm overall including terminal ends; color band denotes the cathode. Pad geometry follows the KiCad Diode_SMD:D_SMA master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SMA",
            "hand_solder": "Diode_SMD:D_SMA_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic MDD SS34 (C8678): 40 V schottky rectifier in SMA (DO-214AC); identity and ratings observed live at intake 2026-09-24.",
            "Family batch 2026-10-04: downloaded the MDD SS32 THRU SS3200 (3.0 A), Rev 2024A5 specification into this part (3 pages); ratings page 1 - VF 0.55 V at 3.0 A max, IR 500 uA at 40 V; mechanical page 3 - DO-214AC outline. Pin 1 = cathode (banded end), pin 2 = anode; this part anchors its current-series family.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C14996 / MDD SS210 SMA schottky - anchor of the SS22 THRU SS2200 (2.0 A), Rev 2024A4 family (generated 2026-10-04)
    current = "electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss210"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMA (DO-214AC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707575901667328-C14996.pdf"
        part["electrical"] = {
            "maximum_dc_reverse_voltage": "100 V (VRRM)",
            "maximum_rectified_current": "2.0 A average forward rectified",
            "forward_voltage_at_test_current": "0.85 V at 2.0 A max",
            "non_repetitive_peak_forward_surge_current": "50 A (8.3 ms half sine, JEDEC)",
            "reverse_leakage_current": "500 uA at 100 V max at 25 C at rated voltage",
            "thermal_resistance": "see specification page 1",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 4.5, "width": 2.8, "height": 2.3}
        part["dimension_reference"] = {
            "document": "MDD SS22 THRU SS2200 (2.0 A), Rev 2024A4 specification, mechanical data page 3 (C14996 provenance)",
            "pages": [3],
            "notes": "JEDEC DO-214AC/SMA molded body 4.50 x 2.80 x 2.30 mm, 5.30 mm overall including terminal ends; color band denotes the cathode. Pad geometry follows the KiCad Diode_SMD:D_SMA master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SMA",
            "hand_solder": "Diode_SMD:D_SMA_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic MDD SS210 (C14996): 100 V schottky rectifier in SMA (DO-214AC); identity and ratings observed live at intake 2026-09-24.",
            "Family batch 2026-10-04: downloaded the MDD SS22 THRU SS2200 (2.0 A), Rev 2024A4 specification into this part (3 pages); ratings page 1 - VF 0.85 V at 2.0 A max, IR 500 uA at 100 V; mechanical page 3 - DO-214AC outline. Pin 1 = cathode (banded end), pin 2 = anode; this part anchors its current-series family.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C22452 / MDD SS54 SMA schottky - anchor of the SS52 THRU SS5200 (5.0 A), Rev 2024A4 family (generated 2026-10-04)
    current = "electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss54"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMA (DO-214AC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707587430322176-C22452.pdf"
        part["electrical"] = {
            "maximum_dc_reverse_voltage": "40 V (VRRM)",
            "maximum_rectified_current": "5.0 A average forward rectified",
            "forward_voltage_at_test_current": "0.55 V at 5.0 A max",
            "non_repetitive_peak_forward_surge_current": "120 A (8.3 ms half sine, JEDEC)",
            "reverse_leakage_current": "500 uA at 40 V max at 25 C at rated voltage",
            "thermal_resistance": "see specification page 1",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 4.5, "width": 2.8, "height": 2.3}
        part["dimension_reference"] = {
            "document": "MDD SS52 THRU SS5200 (5.0 A), Rev 2024A4 specification, mechanical data page 3 (C22452 provenance)",
            "pages": [3],
            "notes": "JEDEC DO-214AC/SMA molded body 4.50 x 2.80 x 2.30 mm, 5.30 mm overall including terminal ends; color band denotes the cathode. Pad geometry follows the KiCad Diode_SMD:D_SMA master.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SMA",
            "hand_solder": "Diode_SMD:D_SMA_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic MDD SS54 (C22452): 40 V schottky rectifier in SMA (DO-214AC); identity and ratings observed live at intake 2026-09-24.",
            "Family batch 2026-10-04: downloaded the MDD SS52 THRU SS5200 (5.0 A), Rev 2024A4 specification into this part (3 pages); ratings page 1 - VF 0.55 V at 5.0 A max, IR 500 uA at 40 V; mechanical page 3 - DO-214AC outline. Pin 1 = cathode (banded end), pin 2 = anode; this part anchors its current-series family.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated family batch (tmp/sma_anchors.py) ===

    # === BEGIN generated family batch (tmp/diode_tail.py) — regenerated, do not hand-edit ===
    # === END generated family batch (tmp/diode_tail.py) ===

    # === BEGIN generated family batch (tmp/tht_batch.py) — regenerated, do not hand-edit ===
    # JLC C2456 / 1N4001 DO-41 (SOD-81) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_rectifier_do_41_mdd_microdiode_semiconductor_1n4001"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-41 (SOD-81) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887224000139264-C2456.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "50V",
                "forward_voltage": "1.1V@1A",
                "forward_current": "1A",
                "reverse_recovery_time": "see live listing",
                "reverse_leakage_current": "5uA@50V",
                "operating_temperature": "-55℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 5.2, "width": 2.7, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD 1N4001 series specification (C2456 provenance)",
            "pages": [1],
            "notes": "DO-41 axial molded body 5.2 x 2.7 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) 1N4001 (C2456); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-41 (SOD-81) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2457 / 1N4007G DO-41 (SOD-81) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_rectifier_do_41_mdd_microdiode_semiconductor_1n4007g"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_rectifier_do_41_mdd_microdiode_semiconductor_1n4001"
        part["package_name_manufacturer"] = "DO-41 (SOD-81) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887223840215040-C2457.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "1kV",
                "forward_voltage": "1.1V@1A",
                "forward_current": "1A",
                "reverse_recovery_time": "see live listing",
                "reverse_leakage_current": "5uA@1kV",
                "operating_temperature": "-65℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 5.2, "width": 2.7, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD 1N4007G series specification (C2456 provenance)",
            "pages": [1],
            "notes": "DO-41 axial molded body 5.2 x 2.7 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) 1N4007G (C2457); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2456; Package outline and polarity follow the DO-41 (SOD-81) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2461 / 6A10 R-6 (P600) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_rectifier_r_6_mdd_microdiode_semiconductor_6a10"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "R-6 (P600) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887223831826432-C2461.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "1kV",
                "forward_voltage": "1V@6A",
                "forward_current": "6A",
                "reverse_recovery_time": "see live listing",
                "reverse_leakage_current": "10uA@1kV",
                "operating_temperature": "-55℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.5, "width": 6.5, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD 6A10 series specification (C2461 provenance)",
            "pages": [1],
            "notes": "R-6 / P600 axial molded body 9.5 x 6.5 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_P600_R-6_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_P600_R-6_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) 6A10 (C2461); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the R-6 (P600) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2462 / 10A10 R-6 (P600) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_rectifier_r_6_mdd_microdiode_semiconductor_10a10"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "R-6 (P600) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757912848654061568-C2462.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "1kV",
                "forward_voltage": "1V@10A",
                "forward_current": "10A",
                "reverse_recovery_time": "see live listing",
                "reverse_leakage_current": "10uA@1kV",
                "operating_temperature": "-50℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.5, "width": 6.5, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD 10A10 series specification (C2462 provenance)",
            "pages": [1],
            "notes": "R-6 / P600 axial molded body 9.5 x 6.5 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_P600_R-6_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_P600_R-6_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) 10A10 (C2462); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the R-6 (P600) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2467 / FR157 DO-15 THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_fast_recovery_do_15_mdd_microdiode_semiconductor_fr157"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-15 THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887194409054209-C2467.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "1kV",
                "forward_voltage": "1.3V@1.5A",
                "forward_current": "1.5A",
                "reverse_recovery_time": "500ns",
                "reverse_leakage_current": "5uA@1kV",
                "operating_temperature": "-65℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 7.6, "width": 3.6, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD FR157 series specification (C2467 provenance)",
            "pages": [1],
            "notes": "DO-15 axial molded body 7.6 x 3.6 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-15_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-15_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) FR157 (C2467); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-15 THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2468 / FR207 DO-15 THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_fast_recovery_do_15_mdd_microdiode_semiconductor_fr207"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-15 THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887194409054208-C2468.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "1kV",
                "forward_voltage": "1.3V@2A",
                "forward_current": "2A",
                "reverse_recovery_time": "500ns",
                "reverse_leakage_current": "5uA@1kV",
                "operating_temperature": "-65℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 7.6, "width": 3.6, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD FR207 series specification (C2468 provenance)",
            "pages": [1],
            "notes": "DO-15 axial molded body 7.6 x 3.6 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-15_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-15_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) FR207 (C2468); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-15 THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2471 / HER307 DO-201AD THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_fast_recovery_do_201ad_mdd_microdiode_semiconductor_her307"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_fast_recovery_do_201ad_mdd_microdiode_semiconductor_her303"
        part["package_name_manufacturer"] = "DO-201AD THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757912860733657088-C2471.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "800V",
                "forward_voltage": "1.7V@3A",
                "forward_current": "3A",
                "reverse_recovery_time": "70ns",
                "reverse_leakage_current": "5uA@800V",
                "operating_temperature": "-65℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.5, "width": 5.5, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD HER307 series specification (C3076 provenance)",
            "pages": [1],
            "notes": "DO-201AD axial molded body 9.5 x 5.5 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) HER307 (C2471); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c3076; Package outline and polarity follow the DO-201AD THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2473 / SF18 DO-41 (SOD-81) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_fast_recovery_do_41_mdd_microdiode_semiconductor_sf18"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-41 (SOD-81) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887194412437504-C2473.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "600V",
                "forward_voltage": "1.7V@1A",
                "forward_current": "1A",
                "reverse_recovery_time": "35ns",
                "reverse_leakage_current": "5uA@600V",
                "operating_temperature": "-65℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 5.2, "width": 2.7, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD SF18 series specification (C2473 provenance)",
            "pages": [1],
            "notes": "DO-41 axial molded body 5.2 x 2.7 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) SF18 (C2473); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-41 (SOD-81) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2476 / 1N5822 DO-201AD THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_schottky_do_201ad_mdd_microdiode_semiconductor_1n5822"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-201AD THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887194409189376-C2476.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "40V",
                "forward_voltage": "525mV@3A",
                "forward_current": "3A",
                "reverse_recovery_time": "see live listing",
                "reverse_leakage_current": "500uA@40V",
                "operating_temperature": "-65℃~+125℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.5, "width": 5.5, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD 1N5822 series specification (C2476 provenance)",
            "pages": [1],
            "notes": "DO-201AD axial molded body 9.5 x 5.5 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) 1N5822 (C2476); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-201AD THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2478 / SR360 DO-201AD THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_schottky_do_201ad_mdd_microdiode_semiconductor_sr360"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-201AD THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887194442878977-C2478.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "60V",
                "forward_voltage": "700mV@3A",
                "forward_current": "3A",
                "reverse_recovery_time": "see live listing",
                "reverse_leakage_current": "500uA@60V",
                "operating_temperature": "-50℃~+125℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.5, "width": 5.5, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD SR360 series specification (C2478 provenance)",
            "pages": [1],
            "notes": "DO-201AD axial molded body 9.5 x 5.5 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) SR360 (C2478); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-201AD THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2487 / MB6S-50MIL MBS / MBS-6 SMD bridge (generated THT batch 2026-10-05)
    current = "electronic_diode_bridge_rectifier_mbs_mdd_microdiode_semiconductor_mb6s_50mil"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_bridge_rectifier_mbs_mdd_microdiode_semiconductor_mb10s_50mil"
        part["package_name_manufacturer"] = "MBS / MBS-6 SMD bridge"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586177291718438912-C2487.pdf"
        part["electrical"] = {
                "repetitive_peak_reverse_voltage": "600V",
                "output_rectified_current": "1A",
                "forward_voltage_per_leg": "1.1V@400mA",
                "surge_current": "35A",
                "operating_temperature": "-55℃~+150℃",
                "polarized": False
        }
        part["dimensions_mm"] = {"length": 4.6, "width": 3.5, "height": 2.2}
        part["dimension_reference"] = {
            "document": "MDD MB6S-50MIL series specification (C2488 provenance)",
            "pages": [1],
            "notes": "MBS flat bridge (4.6 x 3.5 mm), same Vishay MBLS master the completed MB10S uses.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "+",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "~",
                        "type": "passive"
                },
                "pin_3": {
                        "number": "3",
                        "name": "-",
                        "type": "passive"
                },
                "pin_4": {
                        "number": "4",
                        "name": "~",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_SMD:Diode_Bridge_Vishay_MBLS",
            "hand_solder": "Diode_SMD:Diode_Bridge_Vishay_MBLS",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) MB6S-50MIL (C2487); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2488; Package outline and polarity follow the MBS / MBS-6 SMD bridge master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2491 / MB10F-50MIL MBF flat SMD bridge (generated THT batch 2026-10-05)
    current = "electronic_diode_bridge_rectifier_mbf_mdd_microdiode_semiconductor_mb10f_50mil"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "MBF flat SMD bridge"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8767723273876312064-C2491.pdf"
        part["electrical"] = {
                "repetitive_peak_reverse_voltage": "1kV",
                "output_rectified_current": "1A",
                "forward_voltage_per_leg": "1.1V@500mA",
                "surge_current": "35A",
                "operating_temperature": "-55℃~+150℃",
                "polarized": False
        }
        part["dimensions_mm"] = {"length": 4.6, "width": 3.5, "height": 2.2}
        part["dimension_reference"] = {
            "document": "MDD MB10F-50MIL series specification (C2491 provenance)",
            "pages": [1],
            "notes": "MB10F flat bridge; the MBLS master geometry is the closest KiCad master (same 4-pin flat outline), noted honestly.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "+",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "~",
                        "type": "passive"
                },
                "pin_3": {
                        "number": "3",
                        "name": "-",
                        "type": "passive"
                },
                "pin_4": {
                        "number": "4",
                        "name": "~",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_SMD:Diode_Bridge_Vishay_MBLS",
            "hand_solder": "Diode_SMD:Diode_Bridge_Vishay_MBLS",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) MB10F-50MIL (C2491); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the MBF flat SMD bridge master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode. MBF flat outline uses the MBLS master as the nearest KiCad match, noted honestly.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2497 / KBL410 KBL THT bridge (generated THT batch 2026-10-05)
    current = "electronic_diode_bridge_rectifier_kbl_mdd_microdiode_semiconductor_kbl410"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "KBL THT bridge"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887028910342144-C2497.pdf"
        part["electrical"] = {
                "repetitive_peak_reverse_voltage": "1kV",
                "output_rectified_current": "4A",
                "forward_voltage_per_leg": "1.1V@4A",
                "surge_current": "200A",
                "operating_temperature": "-55℃~+150℃",
                "polarized": False
        }
        part["dimensions_mm"] = {"length": 28.6, "width": 7.3, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD KBL410 series specification (C2497 provenance)",
            "pages": [1],
            "notes": "KBL inline bridge, 28.6 mm body, Vishay master geometry.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "+",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "~",
                        "type": "passive"
                },
                "pin_3": {
                        "number": "3",
                        "name": "-",
                        "type": "passive"
                },
                "pin_4": {
                        "number": "4",
                        "name": "~",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_THT:Diode_Bridge_Vishay_KBL",
            "hand_solder": "Diode_THT:Diode_Bridge_Vishay_KBL",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) KBL410 (C2497); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the KBL THT bridge master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2508 / BZX55C3V6 DO-35 (SOD-27) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_35_st_semtech_bzx55c3v6"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_do_35_st_semtech_bzx55c2v4"
        part["package_name_manufacturer"] = "DO-35 (SOD-27) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887196367118336-C2508.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "3.6V",
                "power_dissipation": "500mW",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "2uA@1V",
                "operating_temperature": "-55℃~+175℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 3.0, "width": 1.8, "height": 4.0}
        part["dimension_reference"] = {
            "document": "ST BZX55C3V6 series specification (C2504 provenance)",
            "pages": [1],
            "notes": "DO-35 axial glass body ~3.0 mm dia x 4.0 mm, 0.5 mm leads, 7.62 mm pitch horizontal mount.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists ST(Semtech) BZX55C3V6 (C2508); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2504; Package outline and polarity follow the DO-35 (SOD-27) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2509 / BZX55C3V9 DO-35 (SOD-27) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_35_st_semtech_bzx55c3v9"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_do_35_st_semtech_bzx55c2v4"
        part["package_name_manufacturer"] = "DO-35 (SOD-27) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887196354940928-C2509.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "3.9V",
                "power_dissipation": "500mW",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "2uA",
                "operating_temperature": "see live listing",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 3.0, "width": 1.8, "height": 4.0}
        part["dimension_reference"] = {
            "document": "ST BZX55C3V9 series specification (C2504 provenance)",
            "pages": [1],
            "notes": "DO-35 axial glass body ~3.0 mm dia x 4.0 mm, 0.5 mm leads, 7.62 mm pitch horizontal mount.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists ST(Semtech) BZX55C3V9 (C2509); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2504; Package outline and polarity follow the DO-35 (SOD-27) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2516 / BZX55C7V5 DO-35 (SOD-27) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_35_st_semtech_bzx55c7v5"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_do_35_st_semtech_bzx55c2v4"
        part["package_name_manufacturer"] = "DO-35 (SOD-27) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887196686831616-C2516.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "7.5V",
                "power_dissipation": "500mW",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "100nA",
                "operating_temperature": "see live listing",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 3.0, "width": 1.8, "height": 4.0}
        part["dimension_reference"] = {
            "document": "ST BZX55C7V5 series specification (C2504 provenance)",
            "pages": [1],
            "notes": "DO-35 axial glass body ~3.0 mm dia x 4.0 mm, 0.5 mm leads, 7.62 mm pitch horizontal mount.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists ST(Semtech) BZX55C7V5 (C2516); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2504; Package outline and polarity follow the DO-35 (SOD-27) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2518 / BZX55C9V1 DO-35 (SOD-27) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_35_st_semtech_bzx55c9v1"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_do_35_st_semtech_bzx55c2v4"
        part["package_name_manufacturer"] = "DO-35 (SOD-27) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887196685750272-C2518.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "9.1V",
                "power_dissipation": "500mW",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "100nA",
                "operating_temperature": "see live listing",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 3.0, "width": 1.8, "height": 4.0}
        part["dimension_reference"] = {
            "document": "ST BZX55C9V1 series specification (C2504 provenance)",
            "pages": [1],
            "notes": "DO-35 axial glass body ~3.0 mm dia x 4.0 mm, 0.5 mm leads, 7.62 mm pitch horizontal mount.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists ST(Semtech) BZX55C9V1 (C2518); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2504; Package outline and polarity follow the DO-35 (SOD-27) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2528 / BZX55C24 DO-35 (SOD-27) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_35_st_semtech_bzx55c24"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_do_35_st_semtech_bzx55c2v4"
        part["package_name_manufacturer"] = "DO-35 (SOD-27) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887223831420928-C2528.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "24V",
                "power_dissipation": "500mW",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "100nA@18V",
                "operating_temperature": "-55℃~+175℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 3.0, "width": 1.8, "height": 4.0}
        part["dimension_reference"] = {
            "document": "ST BZX55C24 series specification (C2504 provenance)",
            "pages": [1],
            "notes": "DO-35 axial glass body ~3.0 mm dia x 4.0 mm, 0.5 mm leads, 7.62 mm pitch horizontal mount.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists ST(Semtech) BZX55C24 (C2528); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2504; Package outline and polarity follow the DO-35 (SOD-27) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2534 / 1N4731A DO-41 (SOD-81) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_41_st_semtech_1n4731a"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-41 (SOD-81) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887223828172800-C2534.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "4.3V",
                "power_dissipation": "1W",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "50uA",
                "operating_temperature": "see live listing",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 5.2, "width": 2.7, "height": 4.0}
        part["dimension_reference"] = {
            "document": "ST 1N4731A series specification (C2534 provenance)",
            "pages": [1],
            "notes": "DO-41 axial molded body 5.2 x 2.7 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists ST(Semtech) 1N4731A (C2534); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-41 (SOD-81) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2545 / 1N4742A DO-41 (SOD-81) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_41_st_semtech_1n4742a"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_do_41_st_semtech_1n4731a"
        part["package_name_manufacturer"] = "DO-41 (SOD-81) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887199751921664-C2545.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "12V",
                "power_dissipation": "1W",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "5uA",
                "operating_temperature": "-65℃~+200℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 5.2, "width": 2.7, "height": 4.0}
        part["dimension_reference"] = {
            "document": "ST 1N4742A series specification (C2534 provenance)",
            "pages": [1],
            "notes": "DO-41 axial molded body 5.2 x 2.7 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists ST(Semtech) 1N4742A (C2545); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2534; Package outline and polarity follow the DO-41 (SOD-81) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2555 / 1N4752A DO-41 (SOD-81) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_41_st_semtech_1n4752a"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_do_41_st_semtech_1n4731a"
        part["package_name_manufacturer"] = "DO-41 (SOD-81) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887200725676032-C2555.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "33V",
                "power_dissipation": "1W",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "5uA",
                "operating_temperature": "see live listing",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 5.2, "width": 2.7, "height": 4.0}
        part["dimension_reference"] = {
            "document": "ST 1N4752A series specification (C2534 provenance)",
            "pages": [1],
            "notes": "DO-41 axial molded body 5.2 x 2.7 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists ST(Semtech) 1N4752A (C2555); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2534; Package outline and polarity follow the DO-41 (SOD-81) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2556 / 1N4753A DO-41 (SOD-81) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_41_st_semtech_1n4753a"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_do_41_st_semtech_1n4731a"
        part["package_name_manufacturer"] = "DO-41 (SOD-81) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887200876670976-C2556.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "36V",
                "power_dissipation": "1W",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "5uA",
                "operating_temperature": "see live listing",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 5.2, "width": 2.7, "height": 4.0}
        part["dimension_reference"] = {
            "document": "ST 1N4753A series specification (C2534 provenance)",
            "pages": [1],
            "notes": "DO-41 axial molded body 5.2 x 2.7 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists ST(Semtech) 1N4753A (C2556); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2534; Package outline and polarity follow the DO-41 (SOD-81) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3058 / 1N4004 DO-41 (SOD-81) THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_rectifier_do_41_mdd_microdiode_semiconductor_1n4004"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_rectifier_do_41_mdd_microdiode_semiconductor_1n4001"
        part["package_name_manufacturer"] = "DO-41 (SOD-81) THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887224876613632-C3058.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "400V",
                "forward_voltage": "1.1V@1A",
                "forward_current": "1A",
                "reverse_recovery_time": "see live listing",
                "reverse_leakage_current": "5uA@400V",
                "operating_temperature": "-55℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 5.2, "width": 2.7, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD 1N4004 series specification (C2456 provenance)",
            "pages": [1],
            "notes": "DO-41 axial molded body 5.2 x 2.7 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) 1N4004 (C3058); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2456; Package outline and polarity follow the DO-41 (SOD-81) THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3061 / 1N5404 DO-201AD THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_rectifier_do_201ad_mdd_microdiode_semiconductor_1n5404"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_rectifier_do_201ad_mdd_microdiode_semiconductor_1n5401"
        part["package_name_manufacturer"] = "DO-201AD THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887254797967360-C3061.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "400V",
                "forward_voltage": "1.2V@3A",
                "forward_current": "3A",
                "reverse_recovery_time": "see live listing",
                "reverse_leakage_current": "5uA@400V",
                "operating_temperature": "-65℃~+175℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.5, "width": 5.5, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD 1N5404 series specification (C2459 provenance)",
            "pages": [1],
            "notes": "DO-201AD axial molded body 9.5 x 5.5 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) 1N5404 (C3061); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2459; Package outline and polarity follow the DO-201AD THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3075 / HER205 DO-15 THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_fast_recovery_do_15_mdd_microdiode_semiconductor_her205"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_fast_recovery_do_15_mdd_microdiode_semiconductor_her204"
        part["package_name_manufacturer"] = "DO-15 THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887253506932736-C3075.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "400V",
                "forward_voltage": "1.3V@2A",
                "forward_current": "2A",
                "reverse_recovery_time": "70ns",
                "reverse_leakage_current": "5uA@400V",
                "operating_temperature": "-65℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 7.6, "width": 3.6, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD HER205 series specification (C3074 provenance)",
            "pages": [1],
            "notes": "DO-15 axial molded body 7.6 x 3.6 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-15_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-15_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) HER205 (C3075); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c3074; Package outline and polarity follow the DO-15 THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3076 / HER303 DO-201AD THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_fast_recovery_do_201ad_mdd_microdiode_semiconductor_her303"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-201AD THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757912767934681088-C3076.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "200V",
                "forward_voltage": "1V@3A",
                "forward_current": "3A",
                "reverse_recovery_time": "50ns",
                "reverse_leakage_current": "5uA@200V",
                "operating_temperature": "-65℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.5, "width": 5.5, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD HER303 series specification (C3076 provenance)",
            "pages": [1],
            "notes": "DO-201AD axial molded body 9.5 x 5.5 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) HER303 (C3076); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-201AD THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3078 / KBL406 KBL THT bridge (generated THT batch 2026-10-05)
    current = "electronic_diode_bridge_rectifier_kbl_mdd_microdiode_semiconductor_kbl406"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_bridge_rectifier_kbl_mdd_microdiode_semiconductor_kbl410"
        part["package_name_manufacturer"] = "KBL THT bridge"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588886812937240576-C3078.pdf"
        part["electrical"] = {
                "repetitive_peak_reverse_voltage": "600V",
                "output_rectified_current": "4A",
                "forward_voltage_per_leg": "1.1V@4A",
                "surge_current": "200A",
                "operating_temperature": "-55℃~+150℃",
                "polarized": False
        }
        part["dimensions_mm"] = {"length": 28.6, "width": 7.3, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD KBL406 series specification (C2497 provenance)",
            "pages": [1],
            "notes": "KBL inline bridge, 28.6 mm body, Vishay master geometry.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "+",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "~",
                        "type": "passive"
                },
                "pin_3": {
                        "number": "3",
                        "name": "-",
                        "type": "passive"
                },
                "pin_4": {
                        "number": "4",
                        "name": "~",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_THT:Diode_Bridge_Vishay_KBL",
            "hand_solder": "Diode_THT:Diode_Bridge_Vishay_KBL",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) KBL406 (C3078); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c2497; Package outline and polarity follow the KBL THT bridge master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3082 / KBPC1010 KBPC THT bridge (8 A) (generated THT batch 2026-10-05)
    current = "electronic_diode_bridge_rectifier_kbpc_8_mdd_microdiode_semiconductor_kbpc1010"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "KBPC THT bridge (8 A)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887028909936640-C3082.pdf"
        part["electrical"] = {
                "repetitive_peak_reverse_voltage": "1kV",
                "output_rectified_current": "10A",
                "forward_voltage_per_leg": "1V@5A",
                "surge_current": "150A",
                "operating_temperature": "-65℃~+125℃",
                "polarized": False
        }
        part["dimensions_mm"] = {"length": 28.6, "width": 28.6, "height": 7.3}
        part["dimension_reference"] = {
            "document": "MDD KBPC1010 series specification (C3082 provenance)",
            "pages": [1],
            "notes": "KBPC square bridge, GeneSiC KBPC_T master geometry.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "+",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "~",
                        "type": "passive"
                },
                "pin_3": {
                        "number": "3",
                        "name": "-",
                        "type": "passive"
                },
                "pin_4": {
                        "number": "4",
                        "name": "~",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_THT:Diode_Bridge_GeneSiC_KBPC_T",
            "hand_solder": "Diode_THT:Diode_Bridge_GeneSiC_KBPC_T",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) KBPC1010 (C3082); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the KBPC THT bridge (8 A) master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3083 / KBPC5010 KBPC THT bridge (25 A) (generated THT batch 2026-10-05)
    current = "electronic_diode_bridge_rectifier_kbpc_25_mdd_microdiode_semiconductor_kbpc5010"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "KBPC THT bridge (25 A)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896971872878592-C3083.pdf"
        part["electrical"] = {
                "repetitive_peak_reverse_voltage": "1kV",
                "output_rectified_current": "50A",
                "forward_voltage_per_leg": "1.1V@25A",
                "surge_current": "400A",
                "operating_temperature": "-65℃~+150℃",
                "polarized": False
        }
        part["dimensions_mm"] = {"length": 28.6, "width": 28.6, "height": 7.3}
        part["dimension_reference"] = {
            "document": "MDD KBPC5010 series specification (C3083 provenance)",
            "pages": [1],
            "notes": "KBPC square bridge, GeneSiC KBPC_T master geometry.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "+",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "~",
                        "type": "passive"
                },
                "pin_3": {
                        "number": "3",
                        "name": "-",
                        "type": "passive"
                },
                "pin_4": {
                        "number": "4",
                        "name": "~",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_THT:Diode_Bridge_GeneSiC_KBPC_T",
            "hand_solder": "Diode_THT:Diode_Bridge_GeneSiC_KBPC_T",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) KBPC5010 (C3083); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the KBPC THT bridge (25 A) master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3084 / KBPC608 BR-6 THT bridge (KBPC-6 outline) (generated THT batch 2026-10-05)
    current = "electronic_diode_bridge_rectifier_br_6_mdd_microdiode_semiconductor_kbpc608"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "BR-6 THT bridge (KBPC-6 outline)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887028905201664-C3084.pdf"
        part["electrical"] = {
                "repetitive_peak_reverse_voltage": "800V",
                "output_rectified_current": "6A",
                "forward_voltage_per_leg": "1V@3A",
                "surge_current": "125A",
                "operating_temperature": "-55℃~+125℃",
                "polarized": False
        }
        part["dimensions_mm"] = {"length": 28.6, "width": 28.6, "height": 7.3}
        part["dimension_reference"] = {
            "document": "MDD KBPC608 series specification (C3084 provenance)",
            "pages": [1],
            "notes": "BR-6 uses the KBPC-6 square bridge outline; GeneSiC KBPC_T master geometry.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "+",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "~",
                        "type": "passive"
                },
                "pin_3": {
                        "number": "3",
                        "name": "-",
                        "type": "passive"
                },
                "pin_4": {
                        "number": "4",
                        "name": "~",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_THT:Diode_Bridge_GeneSiC_KBPC_T",
            "hand_solder": "Diode_THT:Diode_Bridge_GeneSiC_KBPC_T",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) KBPC608 (C3084); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the BR-6 THT bridge (KBPC-6 outline) master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3085 / KBPC610 BR-6 THT bridge (KBPC-6 outline) (generated THT batch 2026-10-05)
    current = "electronic_diode_bridge_rectifier_br_6_mdd_microdiode_semiconductor_kbpc610"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_bridge_rectifier_br_6_mdd_microdiode_semiconductor_kbpc608"
        part["package_name_manufacturer"] = "BR-6 THT bridge (KBPC-6 outline)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887028909395968-C3085.pdf"
        part["electrical"] = {
                "repetitive_peak_reverse_voltage": "1kV",
                "output_rectified_current": "6A",
                "forward_voltage_per_leg": "1V@3A",
                "surge_current": "125A",
                "operating_temperature": "-55℃~+125℃",
                "polarized": False
        }
        part["dimensions_mm"] = {"length": 28.6, "width": 28.6, "height": 7.3}
        part["dimension_reference"] = {
            "document": "MDD KBPC610 series specification (C3084 provenance)",
            "pages": [1],
            "notes": "BR-6 uses the KBPC-6 square bridge outline; GeneSiC KBPC_T master geometry.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "+",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "~",
                        "type": "passive"
                },
                "pin_3": {
                        "number": "3",
                        "name": "-",
                        "type": "passive"
                },
                "pin_4": {
                        "number": "4",
                        "name": "~",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_THT:Diode_Bridge_GeneSiC_KBPC_T",
            "hand_solder": "Diode_THT:Diode_Bridge_GeneSiC_KBPC_T",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) KBPC610 (C3085); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c3084; Package outline and polarity follow the BR-6 THT bridge (KBPC-6 outline) master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3087 / KBU808 KBU THT bridge (generated THT batch 2026-10-05)
    current = "electronic_diode_bridge_rectifier_kbu_mdd_microdiode_semiconductor_kbu808"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "KBU THT bridge"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887028918595584-C3087.pdf"
        part["electrical"] = {
                "repetitive_peak_reverse_voltage": "800V",
                "output_rectified_current": "8A",
                "forward_voltage_per_leg": "1.1V@8A",
                "surge_current": "300A",
                "operating_temperature": "-55℃~+150℃",
                "polarized": False
        }
        part["dimensions_mm"] = {"length": 28.6, "width": 7.3, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD KBU808 series specification (C3087 provenance)",
            "pages": [1],
            "notes": "KBU inline bridge, Vishay master geometry.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "+",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "~",
                        "type": "passive"
                },
                "pin_3": {
                        "number": "3",
                        "name": "-",
                        "type": "passive"
                },
                "pin_4": {
                        "number": "4",
                        "name": "~",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_THT:Diode_Bridge_Vishay_KBU",
            "hand_solder": "Diode_THT:Diode_Bridge_Vishay_KBU",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) KBU808 (C3087); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the KBU THT bridge master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3090 / RL207 DO-15 THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_rectifier_do_15_mdd_microdiode_semiconductor_rl207"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-15 THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887225022603264-C3090.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "1kV",
                "forward_voltage": "1.1V@2A",
                "forward_current": "2A",
                "reverse_recovery_time": "see live listing",
                "reverse_leakage_current": "5uA@1kV",
                "operating_temperature": "-50℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 7.6, "width": 3.6, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD RL207 series specification (C3090 provenance)",
            "pages": [1],
            "notes": "DO-15 axial molded body 7.6 x 3.6 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-15_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-15_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) RL207 (C3090); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-15 THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3092 / SF28 Tape DO-15 THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_fast_recovery_do_15_mdd_microdiode_semiconductor_sf28_tape"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-15 THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887200884789248-C3092.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "600V",
                "forward_voltage": "1.7V@2A",
                "forward_current": "2A",
                "reverse_recovery_time": "35ns",
                "reverse_leakage_current": "5uA",
                "operating_temperature": "-65℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 7.6, "width": 3.6, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD SF28 Tape series specification (C3092 provenance)",
            "pages": [1],
            "notes": "DO-15 axial molded body 7.6 x 3.6 mm, 10.16 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-15_P10.16mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-15_P10.16mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) SF28 Tape (C3092); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-15 THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3093 / SF36 DO-201AD THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_fast_recovery_do_201ad_mdd_microdiode_semiconductor_sf36"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-201AD THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887201128464384-C3093.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "400V",
                "forward_voltage": "1.25V@3A",
                "forward_current": "3A",
                "reverse_recovery_time": "35ns",
                "reverse_leakage_current": "10uA@400V",
                "operating_temperature": "-65℃~+150℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.5, "width": 5.5, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD SF36 series specification (C3093 provenance)",
            "pages": [1],
            "notes": "DO-201AD axial molded body 9.5 x 5.5 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D",
            "machine_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) SF36 (C3093); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-201AD THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3094 / SR540 DO-201AD THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_schottky_do_201ad_mdd_microdiode_semiconductor_sr540"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-201AD THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887200892772352-C3094.pdf"
        part["electrical"] = {
                "maximum_dc_reverse_voltage": "40V",
                "forward_voltage": "550mV@5A",
                "forward_current": "5A",
                "reverse_recovery_time": "see live listing",
                "reverse_leakage_current": "500uA@40V",
                "operating_temperature": "-50℃~+125℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.5, "width": 5.5, "height": 4.0}
        part["dimension_reference"] = {
            "document": "MDD SR540 series specification (C3094 provenance)",
            "pages": [1],
            "notes": "DO-201AD axial molded body 9.5 x 5.5 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-201AD_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) SR540 (C3094); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-201AD THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3096 / W06 DIP-4 THT bridge (generated THT batch 2026-10-05)
    current = "electronic_diode_bridge_rectifier_dip_4_mdd_microdiode_semiconductor_w06"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DIP-4 THT bridge"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896940221714432-C3096.pdf"
        part["electrical"] = {
                "repetitive_peak_reverse_voltage": "600V",
                "output_rectified_current": "1.5A",
                "forward_voltage_per_leg": "1V@1.5A",
                "surge_current": "40A",
                "operating_temperature": "-55℃~+125℃",
                "polarized": False
        }
        part["dimensions_mm"] = {"length": 8.6, "width": 6.5, "height": 3.6}
        part["dimension_reference"] = {
            "document": "MDD W06 series specification (C3096 provenance)",
            "pages": [1],
            "notes": "DIP-4 bridge, 7.62 mm row width, 5.08 mm pitch per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "+",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "~",
                        "type": "passive"
                },
                "pin_3": {
                        "number": "3",
                        "name": "-",
                        "type": "passive"
                },
                "pin_4": {
                        "number": "4",
                        "name": "~",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Bridge_+A-A",
            "machine_solder": "Diode_THT:Diode_Bridge_DIP-4_W7.62mm_P5.08mm",
            "hand_solder": "Diode_THT:Diode_Bridge_DIP-4_W7.62mm_P5.08mm",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists MDD(Microdiode Semiconductor) W06 (C3096); identity and ratings observed live at intake 2026-09-29.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DIP-4 THT bridge master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C5306 / 1N5339BRLG DO-27 THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_27_onsemi_1n5339brlg"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "DO-27 THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588886973339602944-C5306.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "5.6V",
                "power_dissipation": "5W",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "2uA",
                "operating_temperature": "-65℃~+200℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.0, "width": 5.3, "height": 4.3}
        part["dimension_reference"] = {
            "document": "onsemi 1N5339BRLG series specification (C5306 provenance)",
            "pages": [1],
            "notes": "DO-27 axial molded body 9.0 x 5.3 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-27_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-27_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi 1N5339BRLG (C5306); identity and ratings observed live at intake 2026-09-30.",
            "THT family batch 2026-10-05: Own downloaded series specification; Package outline and polarity follow the DO-27 THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C5307 / 1N5338BRLG DO-27 THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_27_onsemi_1n5338brlg"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_do_27_onsemi_1n5339brlg"
        part["package_name_manufacturer"] = "DO-27 THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588886973343797248-C5307.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "5.1V",
                "power_dissipation": "5W",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "1uA",
                "operating_temperature": "-65℃~+200℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.0, "width": 5.3, "height": 4.3}
        part["dimension_reference"] = {
            "document": "onsemi 1N5338BRLG series specification (C5306 provenance)",
            "pages": [1],
            "notes": "DO-27 axial molded body 9.0 x 5.3 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-27_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-27_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi 1N5338BRLG (C5307); identity and ratings observed live at intake 2026-09-30.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c5306; Package outline and polarity follow the DO-27 THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C5308 / 1N5350BRLG DO-27 THT axial (generated THT batch 2026-10-05)
    current = "electronic_diode_zener_do_27_onsemi_1n5350brlg"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_diode_zener_do_27_onsemi_1n5339brlg"
        part["package_name_manufacturer"] = "DO-27 THT axial"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588886975416324096-C5308.pdf"
        part["electrical"] = {
                "zener_voltage_nominal": "13V",
                "power_dissipation": "5W",
                "forward_voltage": "see live listing",
                "reverse_leakage_current": "1uA",
                "operating_temperature": "-65℃~+200℃",
                "polarized": True
        }
        part["dimensions_mm"] = {"length": 9.0, "width": 5.3, "height": 4.3}
        part["dimension_reference"] = {
            "document": "onsemi 1N5350BRLG series specification (C5306 provenance)",
            "pages": [1],
            "notes": "DO-27 axial molded body 9.0 x 5.3 mm, 12.70 mm pitch horizontal mount per the KiCad master.",
        }
        part["pins"] = {
                "pin_1": {
                        "number": "1",
                        "name": "K",
                        "type": "passive"
                },
                "pin_2": {
                        "number": "2",
                        "name": "A",
                        "type": "passive"
                }
        }
        part["kicad"] = {
            "symbol": "Device:D_Zener",
            "machine_solder": "Diode_THT:D_DO-27_P12.70mm_Horizontal",
            "hand_solder": "Diode_THT:D_DO-27_P12.70mm_Horizontal",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi 1N5350BRLG (C5308); identity and ratings observed live at intake 2026-09-30.",
            "THT family batch 2026-10-05: Shares the series pdf anchored on c5306; Package outline and polarity follow the DO-27 THT axial master; axial THT convention pin 1 = cathode (banded end), pin 2 = anode.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated family batch (tmp/tht_batch.py) ===

    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="diode")
