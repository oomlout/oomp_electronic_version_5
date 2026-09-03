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
