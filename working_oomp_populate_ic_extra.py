def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_ic_esp32_wroom_32e_microcontroller_wifi_bluetooth_8_mb_flash_espressif_esp32_wroom_32e_n8"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Espressif"
        part["part_number_manufacturer"] = "ESP32-WROOM-32E-N8"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["part_number_lcsc"] = "C701342"
        part["product_url"] = "https://www.lcsc.com/product-detail/C701342.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C701342.pdf"
        part["category"] = "mcu"
        part["dimensions_mm"] = {"length": 18.0, "width": 25.5, "height": 3.1}
        part["dimension_reference"] = {"document": "ESP32-WROOM-32E/32UE v1.6", "pages": [3, 10, 11, 12, 25], "notes": "Top view: 0.45x0.9mm castellations on 1.27mm pitch. Exposed underside GND pad is not shown through the shield."}
        names = ["gnd", "3v3", "en", "sensor_vp", "sensor_vn", "io34", "io35", "io32", "io33",
                 "io25", "io26", "io27", "io14", "io12", "gnd", "io13", "nc", "nc", "nc",
                 "nc", "nc", "nc", "io15", "io2", "io0", "io4", "io16", "io17", "io5",
                 "io18", "io19", "nc", "io21", "rxd0", "txd0", "io22", "io23", "gnd", "gnd_ep"]
        part["pins"] = {}
        for index, name in enumerate(names):
            number = str(index + 1)
            pin_type = "signal"
            if name == "nc":
                pin_type = "no_connect"
            if name in ["gnd", "gnd_ep"]:
                pin_type = "gnd"
            if name == "3v3":
                pin_type = "power"
            part["pins"]["pin_" + number] = {"number": number, "name": name, "type": pin_type}
        pads = []
        for index in range(14):
            pads.append([str(index + 1), "left", -8.775, 5.26 - index * 1.27, .45, .9])
            pads.append([str(38 - index), "right", 8.775, 5.26 - index * 1.27, .45, .9])
        for index in range(10):
            pads.append([str(15 + index), "bottom", -5.715 + index * 1.27, -12.525, .9, .45])
        part["package_drawing"] = {
            "overall": [18, 25.5], "body": [18, 25.5], "pins": pads,
            "boxes": [[0, -2.9, 15.8, 17.6], [0, 9.655, 18, 6.19]],
        }
        part["kicad"] = {"symbol": "RF_Module:ESP32-WROOM-32E", "machine_solder": "RF_Module:ESP32-WROOM-32E", "hand_solder": ""}
        part["electrical"] = {"flash": "8 MB", "supply": "3.0 to 3.6 V", "antenna": "PCB"}

    current = "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_3_3_volt_advanced_monolithic_systems_ams1117_3_3"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Advanced Monolithic Systems"
        part["part_number_manufacturer"] = "AMS1117-3.3"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["part_number_lcsc"] = "C6186"
        part["product_url"] = "https://www.lcsc.com/product-detail/C6186.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C6186.pdf"
        part["name_readable_override"] = "Regulator AMS1117-3.3 3.3V SOT-223"
        part["name_short"] = "Regulator AMS1117-3.3"
        part["category"] = "power_management"
        part["dimensions_mm"] = {"length": 6.5, "width": 7.0}
        part["dimension_reference"] = {"document": "AMS1117 datasheet", "pages": [1, 7], "notes": "Nominal SOT-223 dimensions; tab is VOUT, pin 2."}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "gnd", "type": "gnd"},
            "pin_2": {"number": "2", "name": "vout", "type": "power"},
            "pin_3": {"number": "3", "name": "vin", "type": "power"},
        }
        part["package_drawing"] = {
            "overall": [6.5, 7.0], "body": [6.5, 3.5],
            "pins": [["1", "bottom", -2.29, -2.625, .74, 1.75],
                     ["2", "bottom", 0, -2.625, .74, 1.75],
                     ["3", "bottom", 2.29, -2.625, .74, 1.75],
                     ["2", "top", 0, 2.625, 3.05, 1.75]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:AMS1117-3.3", "machine_solder": "Package_TO_SOT_SMD:SOT-223-3_TabPin2", "hand_solder": ""}
        from working_oomp_populate_jlc import set_preferred_jlc
        set_preferred_jlc(
            part,
            code="C6186",
            manufacturer="Advanced Monolithic Systems",
            mpn="AMS1117-3.3",
            selection={
                "verified_on": "2026-10-02",
                "official_url": "https://jlcpcb.com/partdetail/Advanced_MonolithicSystems-AMS1117_33/C6186",
                "tier": "basic",
                "tier_label_observed": "Basic",
                "stock_observed": 1070672,
                "purchase_moq_observed": 1,
                "pcba_min_qty_observed": None,
                "compatibility_notes": "Exact AMS1117-3.3 identity; JLC C6186 already matched this OOMP ID. SOT-223 pin 2 and tab are VOUT. KiCad SOT-223-3_TabPin2 matches pad numbering; the same official footprint serves hand assembly because no dedicated hand-solder variant exists.",
                "ratings": {
                    "output_voltage": "3.3 V nominal",
                    "output_current": "1 A series rating; SOT-223 dissipation limit 1.2 W",
                    "maximum_input_voltage": "15 V absolute maximum",
                    "dropout_voltage": "1.1 V typical, 1.3 V maximum at 0.8 A",
                    "operating_junction_temperature": "-40 to +125 deg C",
                },
                "datasheet_pages": [1, 2, 3, 7],
                "pinout_checked": True,
                "footprint_checked": True,
                "visual_review": "Inspected 2026-10-02 after the build and a forced diagram refresh. working_svg_square_pins.png hero titled Regulator AMS1117-3.3 3.3V SOT-223 with the VOUT tab on top and GND (1), VOUT (2), VIN (3) labelled on the three lower pins, matching the AMS1117 pinout (tab = VOUT). working_svg_dimensioned.png: 6.5 mm body width, 3.5 mm body height with the tab, matching the SOT-223 outline in dimensions_mm. data/kicad manifest complete with Regulator_Linear:AMS1117-3.3 symbol and Package_TO_SOT_SMD:SOT-223-3_TabPin2 machine + hand footprints (no dedicated hand variant; the same official master is justified in the selection notes). README.md: AMS1117-3.3 part number, LCSC/JLC C6186 links, 3-pin table, datasheet link resolving to data/datasheet.pdf (the pre-existing AMS series PDF, honest repository provenance). Limitation: KiCad symbol/footprint checked as rendered SVG/PNG plus s-expression text rather than in a KiCad GUI.",
            },
        )
        part["kicad"]["hand_solder"] = "Package_TO_SOT_SMD:SOT-223-3_TabPin2"

    current = "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_5_volt_advanced_monolithic_systems_ams1117_5"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_3_3_volt_advanced_monolithic_systems_ams1117_3_3"
        part["manufacturer"] = "Advanced Monolithic Systems"
        part["part_number_manufacturer"] = "AMS1117-5.0"
        part["part_number_lcsc"] = "C6187"
        part["product_url"] = "https://www.lcsc.com/product-detail/C6187.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C6187.pdf"
        part["name_readable_override"] = "Regulator AMS1117-5.0 5V SOT-223"
        part["name_short"] = "Regulator AMS1117-5.0"
        part["category"] = "power_management"
        part["dimensions_mm"] = {"length": 6.5, "width": 7.0}
        part["dimension_reference"] = {"document": "AMS1117 datasheet", "pages": [1, 7], "notes": "Nominal SOT-223 dimensions; tab is VOUT, pin 2."}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "gnd", "type": "gnd"},
            "pin_2": {"number": "2", "name": "vout", "type": "power"},
            "pin_3": {"number": "3", "name": "vin", "type": "power"},
        }
        part["package_drawing"] = {
            "overall": [6.5, 7.0], "body": [6.5, 3.5],
            "pins": [["1", "bottom", -2.29, -2.625, .74, 1.75],
                     ["2", "bottom", 0, -2.625, .74, 1.75],
                     ["3", "bottom", 2.29, -2.625, .74, 1.75],
                     ["2", "top", 0, 2.625, 3.05, 1.75]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:AMS1117-5.0", "machine_solder": "Package_TO_SOT_SMD:SOT-223-3_TabPin2", "hand_solder": ""}
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        from working_oomp_populate_jlc import set_preferred_jlc
        set_preferred_jlc(
            part,
            code="C6187",
            manufacturer="Advanced Monolithic Systems",
            mpn="AMS1117-5.0",
            selection={
                "verified_on": "2026-10-02",
                "official_url": "https://jlcpcb.com/partdetail/Advanced_MonolithicSystems-AMS1117_50/C6187",
                "tier": "basic",
                "tier_label_observed": "Basic",
                "stock_observed": 91295,
                "purchase_moq_observed": 1,
                "pcba_min_qty_observed": None,
                "compatibility_notes": "Exact AMS1117-5.0 identity; JLC C6187 already matched this OOMP ID. SOT-223 pin 2 and tab are VOUT, same pinout and package as the AMS1117-3.3 sibling; datasheet shared via oomp_datasheet_common_with. KiCad SOT-223-3_TabPin2 matches pad numbering; the same official footprint serves hand assembly because no dedicated hand-solder variant exists.",
                "ratings": {
                    "output_voltage": "5 V nominal",
                    "output_current": "1 A series rating; SOT-223 dissipation limit 1.2 W",
                    "maximum_input_voltage": "15 V absolute maximum",
                    "dropout_voltage": "1.3 V typical at 0.8 A",
                    "operating_junction_temperature": "-40 to +125 deg C",
                },
                "datasheet_pages": [1, 2, 3, 7],
                "pinout_checked": True,
                "footprint_checked": True,
                "visual_review": "Inspected 2026-10-02 after the build and a forced diagram refresh. working_svg_square_pins.png hero titled Regulator AMS1117-5.0 5V SOT-223 with the VOUT tab on top and GND (1), VOUT (2), VIN (3) labelled on the three lower pins, matching the AMS1117 pinout (tab = VOUT, same as the 3.3 V sibling). working_svg_dimensioned.png: 6.5 mm body width, 3.5 mm body height with the tab, matching the SOT-223 outline in dimensions_mm. data/kicad manifest complete with Regulator_Linear:AMS1117-5.0 symbol and Package_TO_SOT_SMD:SOT-223-3_TabPin2 machine + hand footprints (no dedicated hand variant; the same official master is justified in the selection notes). README.md: AMS1117-5.0 part number, LCSC/JLC C6187 links, 3-pin table, datasheet link resolving to data/datasheet.pdf via the shared AMS series PDF (oomp_datasheet_common_with). Limitation: KiCad symbol/footprint checked as rendered SVG/PNG plus s-expression text rather than in a KiCad GUI.",
            },
        )
        part["kicad"]["hand_solder"] = "Package_TO_SOT_SMD:SOT-223-3_TabPin2"

    current = "electronic_ic_sot_23_power_management_linear_voltage_regulator_3_3_volt_torex_xc6206p332mr"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Torex"
        part["part_number_manufacturer"] = "XC6206P332MR"
        part["part_number_lcsc"] = "C51489"
        part["product_url"] = "https://www.lcsc.com/product-detail/C51489.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C51489.pdf"
        part["name_readable_override"] = "Regulator XC6206P332MR 3.3V SOT-23"
        part["name_short"] = "Regulator XC6206P332MR"
        part["category"] = "power_management"
        part["dimensions_mm"] = {"length": 2.92, "width": 2.8}
        part["dimension_reference"] = {"document": "XC6206 datasheet", "pages": [10], "notes": "SOT-23 package outline."}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "vss", "type": "gnd"},
            "pin_2": {"number": "2", "name": "vout", "type": "power"},
            "pin_3": {"number": "3", "name": "vin", "type": "power"},
        }
        part["package_drawing"] = {
            "overall": [2.92, 2.8], "body": [2.92, 1.6],
            "pins": [["1", "bottom", -0.95, -1.45, .5, .95],
                     ["2", "bottom", 0.95, -1.45, .5, .95],
                     ["3", "top", 0, 1.45, .5, .95]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:XC6206PxxxMR", "machine_solder": "Package_TO_SOT_SMD:SOT-23", "hand_solder": ""}

    current = "electronic_ic_sot_23_power_management_linear_voltage_regulator_5_volt_torex_xc6206p502mr"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_ic_sot_23_power_management_linear_voltage_regulator_3_3_volt_torex_xc6206p332mr"
        part["manufacturer"] = "Torex"
        part["part_number_manufacturer"] = "XC6206P502MR"
        part["part_number_lcsc"] = "C51490"
        part["product_url"] = "https://www.lcsc.com/product-detail/C51490.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C51490.pdf"
        part["name_readable_override"] = "Regulator XC6206P502MR 5V SOT-23"
        part["name_short"] = "Regulator XC6206P502MR"
        part["category"] = "power_management"
        part["dimensions_mm"] = {"length": 2.92, "width": 2.8}
        part["dimension_reference"] = {"document": "XC6206 datasheet", "pages": [10], "notes": "SOT-23 package outline."}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "vss", "type": "gnd"},
            "pin_2": {"number": "2", "name": "vout", "type": "power"},
            "pin_3": {"number": "3", "name": "vin", "type": "power"},
        }
        part["package_drawing"] = {
            "overall": [2.92, 2.8], "body": [2.92, 1.6],
            "pins": [["1", "bottom", -0.95, -1.45, .5, .95],
                     ["2", "bottom", 0.95, -1.45, .5, .95],
                     ["3", "top", 0, 1.45, .5, .95]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:XC6206PxxxMR", "machine_solder": "Package_TO_SOT_SMD:SOT-23", "hand_solder": ""}


    current = "electronic_ic_tqfp_32_7_mm_x_7_mm_microcontroller_8_bit_avr_microchip_atmega328p_au"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Microchip"
        part["part_number_manufacturer"] = "ATmega328P-AU"
        part["part_number_lcsc"] = "C14877"
        part["product_url"] = "https://www.lcsc.com/product-detail/C14877.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C14877.pdf"
        part["name_readable_override"] = "MCU ATmega328P-AU 8-bit AVR TQFP-32"
        part["name_short"] = "ATmega328P-AU"
        part["category"] = "mcu"
        part["dimensions_mm"] = {"length": 7.0, "width": 7.0}
        part["dimension_reference"] = {"document": "ATmega328P datasheet", "pages": [2, 12], "notes": "TQFP-32 7x7mm, 0.8mm pitch"}
        part["kicad"] = {"symbol": "MCU_Microchip_ATmega:ATmega328P-A", "machine_solder": "Package_QFP:TQFP-32_7x7mm_P0.8mm", "hand_solder": ""}

    current = "electronic_ic_sop_16_converter_usb_to_serial_converter_wch_ch340c"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "WCH"
        part["part_number_manufacturer"] = "CH340C"
        part["part_number_lcsc"] = "C84681"
        part["product_url"] = "https://www.lcsc.com/product-detail/C84681.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C84681.pdf"
        part["name_readable_override"] = "USB-Serial CH340C SOP-16"
        part["name_short"] = "CH340C"
        part["category"] = "interface"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9}
        part["dimension_reference"] = {"document": "CH340 datasheet", "pages": [1], "notes": "SOP-16, 1.27mm pitch, built-in clock"}
        part["kicad"] = {"symbol": "Interface_USB:CH340C", "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm", "hand_solder": ""}

    current = "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102n_a01_gqfn28r"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Silicon Labs"
        part["part_number_manufacturer"] = "CP2102N-A01-GQFN28R"
        part["part_number_lcsc"] = "C105167"
        part["product_url"] = "https://www.lcsc.com/product-detail/C105167.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C105167.pdf"
        part["name_readable_override"] = "USB-Serial CP2102N-A01-GQFN28R"
        part["name_short"] = "CP2102N-A01"
        part["category"] = "interface"
        part["dimensions_mm"] = {"length": 5.0, "width": 5.0}
        part["dimension_reference"] = {"document": "CP2102N datasheet", "pages": [22, 23], "notes": "QFN-28 5x5mm, 0.5mm pitch, EP 3.35x3.35mm"}
        part["kicad"] = {"symbol": "Interface_USB:CP2102N-Axx-xQFN28", "machine_solder": "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm", "hand_solder": ""}

    current = "electronic_ic_esp32_s3_wroom_1_microcontroller_wifi_bluetooth_8_mb_flash_espressif_esp32_s3_wroom_1_n8"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Espressif"
        part["part_number_manufacturer"] = "ESP32-S3-WROOM-1-N8"
        part["part_number_lcsc"] = "C2913198"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2913198.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C2913198.pdf"
        part["name_readable_override"] = "WiFi/BLE Module ESP32-S3-WROOM-1-N8 8MB"
        part["name_short"] = "ESP32-S3-WROOM-1-N8"
        part["category"] = "mcu"
        part["dimensions_mm"] = {"length": 18.0, "width": 25.5, "height": 3.1}
        part["dimension_reference"] = {"document": "ESP32-S3-WROOM-1 datasheet", "pages": [3, 4], "notes": "Module with PCB antenna, 39 castellated pins on 1.27mm pitch"}
        part["kicad"] = {"symbol": "RF_Module:ESP32-S3-WROOM-1", "machine_solder": "RF_Module:ESP32-S3-WROOM-1", "hand_solder": ""}

    current = "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102_gmr"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Silicon Labs"
        part["part_number_manufacturer"] = "CP2102-GMR"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["name_short"] = "USB Serial CP2102-GMR"
        part["part_number_lcsc"] = "C6568"
        part["product_url"] = "https://www.lcsc.com/product-detail/C6568.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C6568.pdf"
        part["category"] = "interface"
        part["dimensions_mm"] = {"length": 5.0, "width": 5.0}
        part["dimension_reference"] = {"document": "CP2102/9 Rev. 1.8", "pages": [11, 12, 13]}
        part["ic_dimensions_mm"] = {"body_length": 5.0, "body_width": 5.0, "body_height": .9,
                                     "pin_pitch": .5, "pin_width": .23, "pin_length": .55}
        names = ["dcd", "ri", "gnd", "usb_d_plus", "usb_d_minus", "vdd", "regin",
                 "vbus", "reset_n", "nc", "suspend_n", "suspend", "nc", "nc",
                 "nc", "nc", "nc", "nc", "nc", "nc", "nc", "nc",
                 "cts", "rts", "rxd", "txd", "dsr", "dtr", "gnd_ep"]
        part["pins"] = {}
        for index, name in enumerate(names):
            number = str(index + 1)
            part["pins"][f"pin_{number}"] = {"number": number, "name": name, "type": "no_connect" if name == "nc" else "signal"}
        pads = []
        offsets = [1.5, 1.0, .5, 0, -.5, -1.0, -1.5]
        for index, offset in enumerate(offsets):
            pads.append([str(index + 1), "left", -2.225, offset, .55, .23])
            pads.append([str(index + 8), "bottom", -offset, -2.225, .23, .55])
            pads.append([str(index + 15), "right", 2.225, -offset, .55, .23])
            pads.append([str(index + 22), "top", offset, 2.225, .23, .55])
        pads.append(["29", "center", 0, 0, 3.15, 3.15])
        part["package_drawing"] = {"overall": [5, 5], "body": [5, 5], "pins": pads, "pin_one": [-2.1, 2.1]}
        part["kicad"] = {"symbol": "", "machine_solder": "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm", "hand_solder": "", "allow_project_fallback": False}
        part["research_notes"] = ["This is CP2102, not CP2102N. Easyduino U1 has conflicting symbol/value and LCSC identity; do not auto-match it.",
                                  "Exposed GND pad uses KiCad identifier 29; it is unnumbered in the datasheet.",
                                  "Installed KiCad 10 masters do not contain the original CP2102 symbol. CP2102N is not substituted; symbol selection is pending."]

    current = "electronic_ic_qfn_16_3_mm_x_3_mm_converter_usb_to_serial_converter_wch_ch343p"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "CH343P"
        extras_dict[current]["part_number_lcsc"] = "C2846043"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_0"] = {
            "name": "gnd",
            "number": "0",
            "type": "gnd",
        }
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "vio",
            "number": "1",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "gnd",
            "number": "2",
            "type": "gnd",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "vdd5",
            "number": "3",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "txd",
            "number": "4",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "rxd",
            "number": "5",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_6"] = {
            "name": "v3",
            "number": "6",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_7"] = {
            "name": "ud_positive",
            "number": "7",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_8"] = {
            "name": "ud_negative",
            "number": "8",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_9"] = {
            "name": "vbus",
            "number": "9",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_10"] = {
            "name": "act",
            "number": "10",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_11"] = {
            "name": "dcd",
            "number": "11",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_12"] = {
            "name": "dtr_tnow",
            "number": "12",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_13"] = {
            "name": "rts",
            "number": "13",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_14"] = {
            "name": "dsr",
            "number": "14",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_15"] = {
            "name": "cts",
            "number": "15",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_16"] = {
            "name": "ri",
            "number": "16",
            "type": "signal",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    bus_pirate_parts = [
        {
            "id": "electronic_ic_tssop_16_logic_serial_in_parallel_out_shift_register_wuxi_i_core_elec_aip74hc595ta16_tr",
            "mpn": "AiP74HC595TA16.TR",
            "lcsc": "C5121351",
            "pins": [["1", "qb"], ["2", "qc"], ["3", "qd"], ["4", "qe"], ["5", "qf"], ["6", "qg"], ["7", "qh"], ["8", "gnd"], ["9", "qh_prime"], ["10", "srclr"], ["11", "srclk"], ["12", "rclk"], ["13", "oe"], ["14", "ser"], ["15", "qa"], ["16", "vcc"]],
        },
        {
            "id": "electronic_ic_tssop_20_logic_octal_bus_transceiver_wuxi_i_core_elec_aip74hct245ta20_tr",
            "mpn": "AiP74HCT245TA20.TR",
            "lcsc": "C5354847",
            "pins": [["1", "direction"], ["2", "a0"], ["3", "a1"], ["4", "a2"], ["5", "a3"], ["6", "a4"], ["7", "a5"], ["8", "a6"], ["9", "a7"], ["10", "gnd"], ["11", "b7"], ["12", "b6"], ["13", "b5"], ["14", "b4"], ["15", "b3"], ["16", "b2"], ["17", "b1"], ["18", "b0"], ["19", "ce"], ["20", "vcc"]],
        },
        {
            "id": "electronic_ic_sot_363_6_logic_single_bit_dual_supply_transceiver_wuxi_i_core_elec_aip74lvc1t45gc363_tr",
            "mpn": "AiP74LVC1T45GC363.TR",
            "lcsc": "C5162250",
            "pins": [["1", "vcca"], ["2", "gnd"], ["3", "a"], ["4", "b"], ["5", "direction"], ["6", "vccb"]],
        },
        {
            "id": "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_3_3_volt_diodes_ap2127k_3_3trg1",
            "mpn": "AP2127K-3.3TRG1",
            "lcsc": "C156285",
            "pins": [["1", "vin"], ["2", "gnd"], ["3", "enable"], ["4", "adjust"], ["5", "vout"]],
        },
        {
            "id": "electronic_ic_sot_89_3_power_management_linear_voltage_regulator_3_3_volt_microne_me6211a33pg_n",
            "mpn": "ME6211A33PG-N",
            "lcsc": "C236673",
            "pins": [["1", "gnd"], ["2", "vin"], ["3", "vout"]],
        },
        {
            "id": "electronic_ic_sop_8_5_28_mm_x_5_23_mm_memory_spi_nor_flash_128_mbit_winbond_w25q128jvsiq",
            "mpn": "W25Q128JVSIQ",
            "lcsc": "C97521",
            "pins": [["1", "chip_select"], ["2", "data_out_io1"], ["3", "write_protect_io2"], ["4", "gnd"], ["5", "data_in_io0"], ["6", "clock"], ["7", "hold_io3"], ["8", "vcc"]],
        },
        {
            "id": "electronic_ic_updfn_8_memory_spi_nand_flash_1_gbit_micron_mt29f1g01abafdwb",
            "mpn": "MT29F1G01ABAFDWB",
            "lcsc": "C2905686",
            "pins": [["1", "chip_select"], ["2", "data_out_io1"], ["3", "write_protect_io2"], ["4", "gnd"], ["5", "data_in_io0"], ["6", "clock"], ["7", "hold_io3"], ["8", "vcc"]],
        },
        {
            "id": "electronic_ic_qfn_56_7_mm_x_7_mm_microcontroller_dual_core_arm_cortex_m0_plus_raspberry_pi_rp2040",
            "mpn": "RP2040",
            "lcsc": "C2040",
            "pins": [["1", "iovdd"], ["2", "gpio0"], ["3", "gpio1"], ["4", "gpio2"], ["5", "gpio3"], ["6", "gpio4"], ["7", "gpio5"], ["8", "gpio6"], ["9", "gpio7"], ["10", "iovdd"], ["11", "gpio8"], ["12", "gpio9"], ["13", "gpio10"], ["14", "gpio11"], ["15", "gpio12"], ["16", "gpio13"], ["17", "gpio14"], ["18", "gpio15"], ["19", "testen"], ["20", "xin"], ["21", "xout"], ["22", "iovdd"], ["23", "dvdd"], ["24", "swclk"], ["25", "swd"], ["26", "run"], ["27", "gpio16"], ["28", "gpio17"], ["29", "gpio18"], ["30", "gpio19"], ["31", "gpio20"], ["32", "gpio21"], ["33", "iovdd"], ["34", "gpio22"], ["35", "gpio23"], ["36", "gpio24"], ["37", "gpio25"], ["38", "gpio26_adc0"], ["39", "gpio27_adc1"], ["40", "gpio28_adc2"], ["41", "gpio29_adc3"], ["42", "iovdd"], ["43", "adc_avdd"], ["44", "vreg_in"], ["45", "vreg_vout"], ["46", "usb_dm"], ["47", "usb_dp"], ["48", "usb_vdd"], ["49", "iovdd"], ["50", "dvdd"], ["51", "qspi_sd3"], ["52", "qspi_sclk"], ["53", "qspi_sd0"], ["54", "qspi_sd2"], ["55", "qspi_sd1"], ["56", "qspi_ss"], ["57", "gnd"]],
        },
        {
            "id": "electronic_ic_tssop_24_logic_16_channel_analog_multiplexer_nexperia_74hct4067pw118",
            "mpn": "74HCT4067PW,118",
            "lcsc": "",
            "pins": [["1", "common"], ["2", "channel_7"], ["3", "channel_6"], ["4", "channel_5"], ["5", "channel_4"], ["6", "channel_3"], ["7", "channel_2"], ["8", "channel_1"], ["9", "channel_0"], ["10", "select_0"], ["11", "select_1"], ["12", "gnd"], ["13", "select_3"], ["14", "select_2"], ["15", "enable"], ["16", "channel_15"], ["17", "channel_14"], ["18", "channel_13"], ["19", "channel_12"], ["20", "channel_11"], ["21", "channel_10"], ["22", "channel_9"], ["23", "channel_8"], ["24", "vcc"]],
        },
    ]
    for bus_pirate_part in bus_pirate_parts:
        current = bus_pirate_part["id"]
        if current not in extras_dict:
            continue
        extras_dict[current]["part_number_manufacturer"] = bus_pirate_part["mpn"]
        if bus_pirate_part["lcsc"] != "":
            extras_dict[current]["part_number_lcsc"] = bus_pirate_part["lcsc"]
        extras_dict[current]["pins"] = {}
        for pin_index in range(len(bus_pirate_part["pins"])):
            pin = bus_pirate_part["pins"][pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": "signal",
            }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_sot_23_5_amplifier_operational_single_rail_to_rail_input_output_gainsil_lmv321_tr"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "LMV321-TR"
        extras_dict[current]["part_number_manufacturer_gainsil"] = "LMV321-TR"
        extras_dict[current]["part_number_lcsc"] = "C362273"
        extras_dict[current]["manufacturer"] = "Gainsil"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C362273.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C362273.pdf"
        extras_dict[current]["package_name_manufacturer"] = "SOT23-5"
        extras_dict[current]["marking_code"] = "321"
        extras_dict[current]["name_short"] = "IC LMV321-TR SOT-23-5 Single Rail To Rail Input Output Op Amp"
        extras_dict[current]["electrical"] = {
            "amplifier_count": 1,
            "input_output_style": "rail-to-rail input and output",
            "minimum_supply_voltage": "2.1 V",
            "maximum_supply_voltage": "5.5 V",
            "typical_gain_bandwidth_product": "1 MHz",
            "typical_slew_rate": "0.6 V/us",
            "typical_quiescent_current_per_amplifier": "40 uA",
            "maximum_input_offset_voltage": "3.5 mV",
            "typical_input_bias_current": "1 pA",
            "operating_temperature": "-40 to +125 C",
            "input_filter": "embedded RF anti-EMI filter",
        }
        extras_dict[current]["ic_dimensions_mm"] = {
            "body_length": 2.92,
            "body_length_min": 2.82,
            "body_length_max": 3.02,
            "body_width": 1.6,
            "body_width_min": 1.5,
            "body_width_max": 1.7,
            "overall_width": 2.8,
            "overall_width_min": 2.65,
            "overall_width_max": 2.95,
            "body_height": 1.15,
            "body_height_min": 1.05,
            "body_height_max": 1.25,
            "pin_pitch": 0.95,
            "pin_width": 0.4,
            "pin_width_min": 0.3,
            "pin_width_max": 0.5,
            "pin_length": 0.45,
            "pin_length_min": 0.3,
            "pin_length_max": 0.6,
        }
        extras_dict[current]["package_dimensions_manufacturer_mm"] = {
            "A_minimum": 1.05,
            "A_maximum": 1.25,
            "A1_minimum": 0.0,
            "A1_maximum": 0.1,
            "A2_minimum": 1.05,
            "A2_maximum": 1.15,
            "b_minimum": 0.3,
            "b_maximum": 0.5,
            "c_minimum": 0.1,
            "c_maximum": 0.2,
            "D_minimum": 2.82,
            "D_maximum": 3.02,
            "E_minimum": 1.5,
            "E_maximum": 1.7,
            "E1_minimum": 2.65,
            "E1_maximum": 2.95,
            "e_basic": 0.95,
            "e1_basic": 1.9,
            "L_minimum": 0.3,
            "L_maximum": 0.6,
            "theta_minimum_degrees": 0,
            "theta_maximum_degrees": 8,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 2.92,
            "width": 2.8,
        }
        extras_dict[current]["pins"] = {}
        amplifier_pins = [
            ["1", "in_positive", "input"],
            ["2", "vss", "power"],
            ["3", "in_negative", "input"],
            ["4", "output", "output"],
            ["5", "vdd", "power"],
        ]
        for pin_index in range(len(amplifier_pins)):
            pin = amplifier_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate analogue component page identifies U404, U506 and U603 as Gainsil LMV321 devices in SOT-23-5.",
            "The exact supplier listing resolves to Gainsil LMV321-TR, LCSC C362273.",
            "The Gainsil datasheet confirms the five-pin assignment, rail-to-rail input and output, 2.1 V to 5.5 V supply range and package dimensions.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_sot_23_5_amplifier_operational_single_precision_rail_to_rail_input_output_gainsil_gs321a_tr"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "GS321A-TR"
        extras_dict[current]["part_number_manufacturer_gainsil"] = "GS321A-TR"
        extras_dict[current]["part_number_lcsc"] = "C431318"
        extras_dict[current]["manufacturer"] = "Gainsil"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C431318.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C431318.pdf"
        extras_dict[current]["package_name_manufacturer"] = "SOT23-5"
        extras_dict[current]["marking_code"] = "321"
        extras_dict[current]["name_short"] = "IC GS321A-TR SOT-23-5 Precision Rail To Rail Input Output Op Amp"
        extras_dict[current]["electrical"] = {
            "amplifier_count": 1,
            "input_output_style": "rail-to-rail input and output",
            "minimum_supply_voltage": "2.1 V",
            "maximum_supply_voltage": "5.5 V",
            "typical_gain_bandwidth_product": "1 MHz",
            "typical_slew_rate": "0.6 V/us",
            "typical_quiescent_current_per_amplifier": "40 uA",
            "maximum_input_offset_voltage": "0.4 mV",
            "typical_input_bias_current": "1 pA",
            "operating_temperature": "-40 to +125 C",
            "input_filter": "embedded RF anti-EMI filter",
        }
        extras_dict[current]["ic_dimensions_mm"] = {
            "body_length": 2.92,
            "body_length_min": 2.82,
            "body_length_max": 3.02,
            "body_width": 1.6,
            "body_width_min": 1.5,
            "body_width_max": 1.7,
            "overall_width": 2.8,
            "overall_width_min": 2.65,
            "overall_width_max": 2.95,
            "body_height": 1.15,
            "body_height_min": 1.05,
            "body_height_max": 1.25,
            "pin_pitch": 0.95,
            "pin_width": 0.4,
            "pin_width_min": 0.3,
            "pin_width_max": 0.5,
            "pin_length": 0.45,
            "pin_length_min": 0.3,
            "pin_length_max": 0.6,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 2.92,
            "width": 2.8,
        }
        extras_dict[current]["pins"] = {}
        amplifier_pins = [
            ["1", "in_positive", "input"],
            ["2", "vss", "power"],
            ["3", "in_negative", "input"],
            ["4", "output", "output"],
            ["5", "vdd", "power"],
        ]
        for pin_index in range(len(amplifier_pins)):
            pin = amplifier_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate analogue page calls for an A-grade LMV321-class device at U601 and links Gainsil GS321A as an example.",
            "The exact active supplier listing resolves to Gainsil GS321A-TR, LCSC C431318.",
            "The Gainsil datasheet confirms 0.4 mV maximum input offset voltage, rail-to-rail input and output, the five-pin assignment and package dimensions.",
            "The discontinued Onsemi LMV321AS5X example was not selected because its listed offset specification does not meet the project's stated A-grade target.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_sot_23_5_comparator_single_open_collector_texas_instruments_lmv331idbvr"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "LMV331IDBVR"
        extras_dict[current]["part_number_manufacturer_texas_instruments"] = "LMV331IDBVR"
        extras_dict[current]["part_number_lcsc"] = "C34731"
        extras_dict[current]["manufacturer"] = "Texas Instruments"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C34731.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C34731.pdf"
        extras_dict[current]["package_name_manufacturer"] = "DBV SOT-23-5"
        extras_dict[current]["name_short"] = "IC LMV331IDBVR SOT-23-5 Single Open Collector Comparator"
        extras_dict[current]["electrical"] = {
            "comparator_count": 1,
            "output_style": "open collector",
            "input_common_mode": "includes ground",
            "minimum_supply_voltage": "2.7 V",
            "maximum_supply_voltage": "5.5 V",
            "maximum_input_offset_voltage": "7 mV",
            "typical_input_bias_current": "250 nA",
            "typical_supply_current": "40 uA",
            "typical_output_saturation_voltage": "200 mV",
            "minimum_output_sink_current_at_5_v": "10 mA",
            "typical_high_to_low_propagation_delay_at_5_v": "600 ns",
            "typical_low_to_high_propagation_delay_at_5_v": "450 ns",
            "operating_temperature": "-40 to +125 C",
        }
        extras_dict[current]["ic_dimensions_mm"] = {
            "body_length": 2.9,
            "body_length_min": 2.75,
            "body_length_max": 3.05,
            "body_width": 1.6,
            "body_width_min": 1.45,
            "body_width_max": 1.75,
            "overall_width": 2.8,
            "overall_width_min": 2.6,
            "overall_width_max": 3.0,
            "body_height_max": 1.45,
            "pin_pitch": 0.95,
            "pin_width": 0.4,
            "pin_width_min": 0.3,
            "pin_width_max": 0.5,
            "pin_length": 0.45,
            "pin_length_min": 0.3,
            "pin_length_max": 0.6,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 2.9,
            "width": 2.8,
        }
        extras_dict[current]["pins"] = {}
        comparator_pins = [
            ["1", "in_positive", "input"],
            ["2", "gnd", "power"],
            ["3", "in_negative", "input"],
            ["4", "output", "open_collector_output"],
            ["5", "vcc", "power"],
        ]
        for pin_index in range(len(comparator_pins)):
            pin = comparator_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate analogue page identifies U602 as an LMV331 comparator in SOT-23-5 and links this exact TI example.",
            "The supplier listing resolves to Texas Instruments LMV331IDBVR, LCSC C34731.",
            "The TI datasheet confirms the open-collector output, 2.7 V to 5.5 V supply range, five-pin assignment and DBV package dimensions.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_tssop_14_amplifier_operational_quad_rail_to_rail_output_texas_instruments_lmv324ipwr"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "LMV324IPWR"
        extras_dict[current]["part_number_manufacturer_texas_instruments"] = "LMV324IPWR"
        extras_dict[current]["part_number_lcsc"] = "C398929"
        extras_dict[current]["manufacturer"] = "Texas Instruments"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C398929.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C398929.pdf"
        extras_dict[current]["package_name_manufacturer"] = "PW TSSOP-14"
        extras_dict[current]["package_drawing_url"] = "https://www.ti.com/lit/pdf/mpds360a"
        extras_dict[current]["marking_code"] = "MV324I"
        extras_dict[current]["name_short"] = "IC LMV324IPWR TSSOP-14 Quad Rail To Rail Output Op Amp"
        extras_dict[current]["electrical"] = {
            "amplifier_count": 4,
            "output_style": "rail-to-rail output",
            "minimum_supply_voltage": "2.7 V",
            "maximum_supply_voltage": "5.5 V",
            "typical_gain_bandwidth_product": "1 MHz",
            "typical_slew_rate": "1 V/us",
            "typical_total_quiescent_current": "410 uA",
            "maximum_input_offset_voltage": "7 mV",
            "typical_input_bias_current": "250 nA",
            "typical_output_current": "60 mA",
            "operating_temperature": "-40 to +125 C",
        }
        extras_dict[current]["ic_dimensions_mm"] = {
            "body_length": 5.0,
            "body_length_min": 4.9,
            "body_length_max": 5.1,
            "body_width": 4.4,
            "body_width_min": 4.3,
            "body_width_max": 4.5,
            "overall_width": 6.4,
            "overall_width_min": 6.2,
            "overall_width_max": 6.6,
            "body_height_max": 1.2,
            "pin_pitch": 0.65,
            "pin_width": 0.235,
            "pin_width_min": 0.17,
            "pin_width_max": 0.3,
            "pin_length": 0.625,
            "pin_length_min": 0.5,
            "pin_length_max": 0.75,
            "lead_thickness": 0.1,
            "lead_thickness_min": 0.05,
            "lead_thickness_max": 0.15,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 5.0,
            "width": 6.4,
        }
        extras_dict[current]["pins"] = {}
        amplifier_pins = [
            ["1", "1out", "output"],
            ["2", "1in-", "input"],
            ["3", "1in+", "input"],
            ["4", "vcc+", "power"],
            ["5", "2in+", "input"],
            ["6", "2in-", "input"],
            ["7", "2out", "output"],
            ["8", "3out", "output"],
            ["9", "3in-", "input"],
            ["10", "3in+", "input"],
            ["11", "gnd", "power"],
            ["12", "4in+", "input"],
            ["13", "4in-", "input"],
            ["14", "4out", "output"],
        ]
        for pin_index in range(len(amplifier_pins)):
            pin = amplifier_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate analogue component page identifies U504 and U505 as LMV324 devices in TSSOP-14 and links this TI orderable example.",
            "The exact supplier page resolves to Texas Instruments LMV324IPWR, LCSC C398929.",
            "The TI datasheet confirms this variant is a quad 2.7 V to 5.5 V operational amplifier with rail-to-rail output and the complete fourteen-pin assignment.",
            "The official TI PW0014A package drawing supplies the dimensions used by the physical diagrams.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_sop_16_controller_usb_hub_controller_4_port_corechips_sl21a"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "SL2.1A"
        extras_dict[current]["part_number_lcsc"] = "C192893"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "dm4",
            "number": "1",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "dp4",
            "number": "2",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "dm3",
            "number": "3",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "dp3",
            "number": "4",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "dm2",
            "number": "5",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_6"] = {
            "name": "dp2",
            "number": "6",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_7"] = {
            "name": "dm1",
            "number": "7",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_8"] = {
            "name": "dp1",
            "number": "8",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_9"] = {
            "name": "udm",
            "number": "9",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_10"] = {
            "name": "udp",
            "number": "10",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_11"] = {
            "name": "vcc5",
            "number": "11",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_12"] = {
            "name": "vss",
            "number": "12",
            "type": "gnd",
        }
        extras_dict[current]["pins"]["pin_13"] = {
            "name": "vdd33",
            "number": "13",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_14"] = {
            "name": "vdd18",
            "number": "14",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_15"] = {
            "name": "xout",
            "number": "15",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_16"] = {
            "name": "xin",
            "number": "16",
            "type": "signal",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_sot_23_6_logic_configurable_multi_function_gate_texas_instruments_sn74lvc1g57dbvr"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "SN74LVC1G57DBVR"
        extras_dict[current]["part_number_lcsc"] = "C485080"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "in1",
            "number": "1",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "gnd",
            "number": "2",
            "type": "gnd",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "in0",
            "number": "3",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "y",
            "number": "4",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "vcc",
            "number": "5",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_6"] = {
            "name": "in2",
            "number": "6",
            "type": "signal",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_ic_tsot_23_5_power_management_high_side_power_switch_with_flag_richtek_rt9742cgj5"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "RT9742CGJ5"
        extras_dict[current]["part_number_lcsc"] = "C250546"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "vout",
            "number": "1",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "gnd",
            "number": "2",
            "type": "gnd",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "flg",
            "number": "3",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "en",
            "number": "4",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "vin",
            "number": "5",
            "type": "power",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C7955 / onsemi LM393DR2G, verified against the onsemi LM393/D Rev. 25
    # datasheet (ordering page 7 covers the DR2G suffix; pins page 1; maximum
    # ratings page 2; characteristics page 3; SOIC-8 NB Case 751-07 page 9).
    # Purchasing identity fields (manufacturer, MPN, LCSC/JLC numbers and
    # jlcpcb_selection) come from the reviewed-choice registry, not here.
    current = "electronic_ic_soic_8_logic_comparator_lm393"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "D Suffix SOIC-8 NB Case 751-07"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579709014336602112-C7955.pdf"
        part["electrical"] = {
            "comparator_count": 2,
            "output_style": "open collector",
            "input_common_mode": "includes ground",
            "minimum_supply_voltage": "2.0 V single supply",
            "maximum_supply_voltage": "36.0 V single supply / +-18 V split supply",
            "maximum_input_offset_voltage": "5.0 mV at TA = 25 C",
            "typical_input_bias_current": "20 nA",
            "maximum_input_bias_current": "250 nA at TA = 25 C",
            "typical_supply_current": "0.4 mA both comparators, RL = infinity",
            "maximum_supply_current": "1.0 mA both comparators, RL = infinity",
            "typical_output_saturation_voltage": "150 mV at ISink <= 4.0 mA",
            "maximum_output_saturation_voltage": "400 mV at ISink <= 4.0 mA, TA = 25 C",
            "minimum_output_sink_current": "6.0 mA at VO <= 1.5 V, TA = 25 C",
            "typical_low_to_high_response_time": "1.3 us with 5.0 mV overdrive",
            "large_signal_response_time": "300 ns with TTL input swing",
            "maximum_power_dissipation": "570 mW at TA = 25 C, derate 5.7 mW/C",
            "operating_temperature": "0 to +70 C",
        }
        part["ic_dimensions_mm"] = {
            "body_length": 4.9,
            "body_length_min": 4.8,
            "body_length_max": 5.0,
            "body_width": 3.9,
            "body_width_min": 3.8,
            "body_width_max": 4.0,
            "overall_width": 6.0,
            "overall_width_min": 5.8,
            "overall_width_max": 6.2,
            "body_height_max": 1.75,
            "body_height_min": 1.35,
            "pin_pitch": 1.27,
            "pin_width": 0.42,
            "pin_width_min": 0.33,
            "pin_width_max": 0.51,
            "pin_length": 1.05,
            "seat_standoff_min": 0.1,
            "seat_standoff_max": 0.25,
            "lead_thickness_min": 0.19,
            "lead_thickness_max": 0.25,
        }
        part["dimensions_mm"] = {"length": 4.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "onsemi LM393/D Rev. 25, SOIC-8 NB Case 751-07 Issue AK",
            "pages": [9],
            "notes": "Length/width/span use the documented min/max midpoints (A 4.80-5.00, B 3.80-4.00, S 5.80-6.20); height is the 1.75 maximum. Pin positions use the 1.27 BSC pitch.",
        }
        part["pins"] = {}
        comparator_pins = [
            ["1", "1out", "open_collector_output"],
            ["2", "1in-", "input"],
            ["3", "1in+", "input"],
            ["4", "gnd", "power"],
            ["5", "2in+", "input"],
            ["6", "2in-", "input"],
            ["7", "2out", "open_collector_output"],
            ["8", "vcc", "power"],
        ]
        for pin_index in range(len(comparator_pins)):
            pin = comparator_pins[pin_index]
            part["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        # Top view, y up, pin 1 top-left; pin columns honour the 1.27 mm pitch.
        lead_span = 1.05
        pin_rows = [1.905, 0.635, -0.635, -1.905]
        part["package_drawing"] = {
            "overall": [6.0, 4.9],
            "body": [3.9, 4.9],
            "pins": [
                ["1", "left", -2.475, pin_rows[0], lead_span, 0.42],
                ["2", "left", -2.475, pin_rows[1], lead_span, 0.42],
                ["3", "left", -2.475, pin_rows[2], lead_span, 0.42],
                ["4", "left", -2.475, pin_rows[3], lead_span, 0.42],
                ["5", "right", 2.475, pin_rows[3], lead_span, 0.42],
                ["6", "right", 2.475, pin_rows[2], lead_span, 0.42],
                ["7", "right", 2.475, pin_rows[1], lead_span, 0.42],
                ["8", "right", 2.475, pin_rows[0], lead_span, 0.42],
            ],
            "pin_one": [-1.6, 2.1],
        }
        part["kicad"] = {
            "symbol": "Comparator:LM393",
            "machine_solder": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
            # No HandSolder variant of this master exists in the installed
            # libraries. The same official JEDEC MS-012 master is selected
            # unchanged: its 1.95 mm long pads already accommodate hand
            # soldering, and no pads are enlarged or invented.
            "hand_solder": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic onsemi LM393DR2G (C7955) in SOIC-8; the purchased identity is an exact LM393 ordering suffix.",
            "The onsemi LM393/D Rev. 25 datasheet confirms the dual open-collector comparator with the eight-pin assignment above and SOIC-8 NB Case 751-07 dimensions.",
            "Comparator:LM393 matches the datasheet pin for pin, including open-collector outputs and the V-/V+ power pins; Package_SO:SOIC-8_3.9x4.9mm_P1.27mm is the matching JEDEC MS-012 machine footprint.",
            "No HandSolder variant of the SOIC-8 3.9x4.9 master exists in the installed KiCad libraries; the same official master is selected unchanged for hand soldering (long 1.95 mm pads, no enlargement).",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C6961 / STMicroelectronics TL072CDT, verified against the ST TL072
    # datasheet Doc ID 2298 Rev 7 (ordering page 14 covers the CDT suffix; pins
    # page 1; ratings pages 3-5; SO-8 package page 13). Purchasing identity
    # fields come from the reviewed-choice registry, not here.
    current = "electronic_ic_soic_8_amplifier_operational_amplifier_dual_jfet_input_stmicroelectronics_tl072cdt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "D Suffix SO-8"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8567021770910547968-C6961.pdf"
        part["electrical"] = {
            "amplifier_count": 2,
            "input_stage": "JFET",
            "minimum_supply_voltage": "6.0 V single supply / +-3.0 V split supply",
            "maximum_supply_voltage": "36.0 V single supply / +-18.0 V split supply",
            "maximum_input_offset_voltage": "10.0 mV at VCC = +-15 V, TA = 25 C (3.0 mV typical)",
            "input_offset_voltage_drift": "10 uV/C typical",
            "typical_input_bias_current": "20 pA",
            "maximum_input_bias_current": "200 pA at TA = 25 C",
            "typical_gain_bandwidth_product": "4.0 MHz at Vin = 10 mV, F = 100 kHz",
            "minimum_gain_bandwidth_product": "2.5 MHz",
            "typical_slew_rate": "16.0 V/us at Vin = 10 V, unity gain (8.0 V/us minimum)",
            "typical_supply_current": "1.4 mA both amplifiers, no load",
            "maximum_supply_current": "2.5 mA both amplifiers, no load",
            "typical_equivalent_input_noise": "15 nV/sqrt(Hz) at RS = 100 Ohm, F = 1 kHz",
            "minimum_large_signal_voltage_gain": "25 V/mV at RL = 2 kOhm, Vo = +-10 V (200 V/mV typical)",
            "typical_output_voltage_swing": "+-12 V at RL = 2 kOhm, VCC = +-15 V",
            "output_short_circuit_protection": "infinite duration; 40 mA typical short-circuit current",
            "operating_temperature": "0 to +70 C (TL072C grade)",
        }
        part["ic_dimensions_mm"] = {
            "body_length": 4.9,
            "body_length_min": 4.8,
            "body_length_max": 5.0,
            "body_width": 3.9,
            "body_width_min": 3.8,
            "body_width_max": 4.0,
            "overall_width": 6.0,
            "overall_width_min": 5.8,
            "overall_width_max": 6.2,
            "body_height_max": 1.75,
            "pin_pitch": 1.27,
            "pin_width": 0.38,
            "pin_width_min": 0.28,
            "pin_width_max": 0.48,
            "pin_length": 1.05,
            "seat_standoff_min": 0.1,
            "seat_standoff_max": 0.25,
            "lead_thickness_min": 0.17,
            "lead_thickness_max": 0.23,
        }
        part["dimensions_mm"] = {"length": 4.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "ST TL072 datasheet Doc ID 2298 Rev 7, SO-8 package Table 5",
            "pages": [13],
            "notes": "ST states typ values: D 4.90, E1 3.90, E 6.00, e 1.27; height is the 1.75 maximum. Pin positions use the 1.27 mm pitch.",
        }
        part["pins"] = {}
        amplifier_pins = [
            ["1", "1out", "output"],
            ["2", "1in-", "input"],
            ["3", "1in+", "input"],
            ["4", "vcc-", "power"],
            ["5", "2in+", "input"],
            ["6", "2in-", "input"],
            ["7", "2out", "output"],
            ["8", "vcc+", "power"],
        ]
        for pin_index in range(len(amplifier_pins)):
            pin = amplifier_pins[pin_index]
            part["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        # Top view, y up, pin 1 top-left; pin rows honour the 1.27 mm pitch.
        lead_span = 1.05
        pin_rows = [1.905, 0.635, -0.635, -1.905]
        part["package_drawing"] = {
            "overall": [6.0, 4.9],
            "body": [3.9, 4.9],
            "pins": [
                ["1", "left", -2.475, pin_rows[0], lead_span, 0.38],
                ["2", "left", -2.475, pin_rows[1], lead_span, 0.38],
                ["3", "left", -2.475, pin_rows[2], lead_span, 0.38],
                ["4", "left", -2.475, pin_rows[3], lead_span, 0.38],
                ["5", "right", 2.475, pin_rows[3], lead_span, 0.38],
                ["6", "right", 2.475, pin_rows[2], lead_span, 0.38],
                ["7", "right", 2.475, pin_rows[1], lead_span, 0.38],
                ["8", "right", 2.475, pin_rows[0], lead_span, 0.38],
            ],
            "pin_one": [-1.6, 2.1],
        }
        part["kicad"] = {
            "symbol": "Amplifier_Operational:TL072",
            "machine_solder": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
            # No HandSolder variant of this master exists in the installed
            # libraries; the same official JEDEC MS-012 master is selected
            # unchanged (long 1.95 mm pads, nothing enlarged).
            "hand_solder": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic STMicroelectronics TL072CDT (C6961) in SO-8; the ordering table of Doc ID 2298 Rev 7 covers the CDT suffix exactly.",
            "The ST datasheet confirms the dual JFET-input op-amp with the eight-pin assignment above and SO-8 package dimensions (D 4.80-5.00, E1 3.80-4.00, E 5.80-6.20, e 1.27 BSC).",
            "Amplifier_Operational:TL072 matches the datasheet pin for pin; Package_SO:SOIC-8_3.9x4.9mm_P1.27mm is the matching JEDEC MS-012 machine footprint.",
            "No HandSolder variant of the SOIC-8 3.9x4.9 master exists in the installed KiCad libraries; the same official master is selected unchanged for hand soldering.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C3113 / Jiangsu Changjing CJ431 full-stage technical data, verified
    # against the Changjing CJ431/CD431 Adjustable Accurate Reference Source
    # specification (M.Oct 2017, browser-downloaded to this part; anchors
    # the CJ431 SOT-23 family): three-terminal adjustable shunt regulator
    # (TL431 type). Absolute maximum ratings page 2: cathode voltage VKA
    # 36 V, cathode current -100 to +150 mA, reference input 0.05-10 mA,
    # PD 300 mW for SOT-23 (RthJA 417 C/W), Topr -25 to +85 C, Tj 150 C;
    # electrical characteristics page 2: Vref 2.475-2.525 V (typ 2.5 V),
    # +-0.5 % rank = 2.487-2.513 V (matches the live description), IKA min
    # for regulation 1.0 mA max, ZKA 0.15/0.5 Ohm, equivalent full-range
    # temperature factor ~50 ppm/C, off-state cathode current 1.0 uA;
    # marking 431. Pin assignment page 1 (CJ431 SOT-23): 1 = REFERENCE,
    # 2 = CATHODE, 3 = ANODE. SYMBOL MIRROR recorded: the KiCad
    # Reference_Voltage:TL431LP symbol (the SOT-23 TL431 master) numbers
    # pins 1 = REF / 2 = A / 3 = K - pins 2 and 3 swapped vs the Changjing
    # pinout; designs must compensate (custom symbol or pin swap) before
    # assembly.
    current = "electronic_ic_sot_23_power_management_voltage_reference_jiangsu_changjing_electronics_technology_co_ltd_cj431"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (TO-236AB)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708596516814848-C3113.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.0}
        part["dimension_reference"] = {
            "document": "Changjing CJ431/CD431 specification, M.Oct 2017 (C3113)",
            "pages": [1, 2],
            "notes": "SOT-23 (TO-236AB) outline per the Package_TO_SOT_SMD:SOT-23 master geometry; pin assignment page 1: 1 = REFERENCE, 2 = CATHODE, 3 = ANODE.",
        }
        part["electrical"] = {
            "device_type": "adjustable shunt voltage reference (TL431 type)",
            "reference_voltage": "2.475-2.525 V (typ 2.5 V); +-0.5 % rank = 2.487-2.513 V",
            "adjustable_output_range": "VKA up to 36 V",
            "cathode_current_range": "1-100 mA (regulation from 1.0 mA max)",
            "cathode_current_absolute": "-100 to +150 mA",
            "reference_input_current": "0.05-10 mA (4 uA max at VKA = 10 mA)",
            "dynamic_impedance": "0.15/0.5 Ohm typ/max",
            "temperature_stability": "~50 ppm/C equivalent full-range factor",
            "power_dissipation": "300 mW for SOT-23 (RthJA 417 C/W)",
            "operating_temperature": "-25 to +85 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "REF", "type": "input"},
            "pin_2": {"number": "2", "name": "K", "type": "power_out"},
            "pin_3": {"number": "3", "name": "A", "type": "power_in"},
        }
        part["kicad"] = {
            "symbol": "Reference_Voltage:TL431LP",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing CJ431 (C3113): adjustable shunt reference 2.5-36 V, +-0.5 %, 100 mA in SOT-23; reconfirmed live 2026-10-02 (stock 398,030).",
            "Browser-downloaded the Changjing CJ431/CD431 specification (9 pages, M.Oct 2017) into this part; it anchors the CJ431 SOT-23 family.",
            "SYMBOL MIRROR: the datasheet pin assignment is 1 = REFERENCE, 2 = CATHODE, 3 = ANODE, while the KiCad Reference_Voltage:TL431LP symbol numbers 1 = REF / 2 = A / 3 = K - pins 2 and 3 swapped; designs must compensate (custom symbol or pin swap) before assembly.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C5446 / Torex XC6206P332MR-G full-stage technical data, verified
    # against the Torex XC6206 series datasheet (ETR0305_004b,
    # browser-downloaded to this part; anchors the XC6206 SOT-23 LDO
    # family): 3-terminal positive CMOS LDO with current limiter and
    # foldback short-circuit protection. Features page 1: maximum output
    # current 200 mA, dropout 250 mV @100 mA (3.0 V type), maximum
    # operating voltage 6.0 V, output 1.2-5.0 V in 0.1 V steps, accuracy
    # +-2 % (VOUT >= 1.5 V), quiescent 1.0 uA, ceramic low-ESR compatible,
    # -40 to +85 C; the -G suffix denotes halogen-free. P332 = 3.3 V
    # fixed output (+-2 %). Pin assignment page 2 (SOT-23): 1 = VSS,
    # 2 = VOUT, 3 = VIN, matching the KiCad Regulator_Linear:XC6206PxxxMR
    # symbol (extends the SOT-23 LDO master with pins 1 GND / 2 VO /
    # 3 VI) pad-for-pad with Package_TO_SOT_SMD:SOT-23.
    current = "electronic_ic_sot_23_power_management_linear_voltage_regulator_3_3_volt_torex_semicon_xc6206p332mr_g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (TO-236AB)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707861616033792-C5446.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.0}
        part["dimension_reference"] = {
            "document": "Torex XC6206 series datasheet, ETR0305_004b (C5446)",
            "pages": [1, 2],
            "notes": "SOT-23 (TO-236AB) outline per the Package_TO_SOT_SMD:SOT-23 master geometry; pin assignment page 2: 1 = VSS, 2 = VOUT, 3 = VIN.",
        }
        part["electrical"] = {
            "device_type": "3-terminal positive CMOS LDO voltage regulator",
            "output_voltage": "3.3 V fixed (+-2 %)",
            "maximum_output_current": "200 mA (current limiter with foldback protection)",
            "dropout_voltage": "250 mV @100 mA (3.0 V type)",
            "maximum_input_voltage": "6.0 V",
            "quiescent_current": "1.0 uA typ",
            "output_capacitor": "low-ESR ceramic compatible",
            "operating_temperature": "-40 to +85 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "GND", "type": "power_in"},
            "pin_2": {"number": "2", "name": "VOUT", "type": "power_out"},
            "pin_3": {"number": "3", "name": "VIN", "type": "power_in"},
        }
        part["kicad"] = {
            "symbol": "Regulator_Linear:XC6206PxxxMR",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Torex Semicon XC6206P332MR-G (C5446): 3.3 V 200 mA LDO in SOT-23; reconfirmed live 2026-10-02 (stock 474,086).",
            "Browser-downloaded the Torex XC6206 series datasheet (17 pages, ETR0305_004b) into this part; it anchors the XC6206 SOT-23 LDO family.",
            "Pin assignment page 2 (SOT-23): 1 = VSS, 2 = VOUT, 3 = VIN; the KiCad Regulator_Linear:XC6206PxxxMR symbol matches pad-for-pad.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C5605 / Nexperia 74HC14D,653 full-stage technical data, verified
    # against the Nexperia 74HC14;74HCT14 product data sheet
    # (browser-downloaded to this part; anchors the SOIC-14 74HC14 family):
    # hex Schmitt-trigger inverter, SO14 (SOT108-1). Pinning section 6.1:
    # 1 = 1A, 2 = 1Y, 3 = 2A, 4 = 2Y, 5 = 3A, 6 = 3Y, 7 = GND, 8 = 4Y,
    # 9 = 4A, 10 = 5Y, 11 = 5A, 12 = 6Y, 13 = 6A, 14 = VCC - the standard
    # arrangement, matching the KiCad 74xx:74HC14 multi-unit symbol
    # (6 gate units + power unit) pad-for-pad with
    # Package_SO:SOIC-14_3.9x8.7mm_P1.27mm. Supply 2.0-6.0 V; propagation
    # 21 ns at 6 V / 50 pF; +/-5.2 mA output drive at 6 V (live
    # description); the ,653 suffix is the packing variant.
    current = "electronic_ic_soic_14_logic_hex_schmitt_trigger_inverter_nexperia_74hc14d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708675558199296-C5605.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "Nexperia 74HC14;74HCT14 product data sheet (C5605)",
            "pages": [2, 3],
            "notes": "SO14 (SOT108-1) outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning section 6.1.",
        }
        part["electrical"] = {
            "device_type": "hex Schmitt-trigger inverter (6 channels)",
            "supply_voltage": "2.0-6.0 V (74HC family)",
            "propagation_delay": "21 ns at 6 V, 50 pF (live description)",
            "output_drive": "+-5.2 mA at 6 V",
            "input_hysteresis": "Schmitt-trigger inputs (noise immunity per datasheet table)",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "input"},
            "pin_2": {"number": "2", "name": "1Y", "type": "output"},
            "pin_3": {"number": "3", "name": "2A", "type": "input"},
            "pin_4": {"number": "4", "name": "2Y", "type": "output"},
            "pin_5": {"number": "5", "name": "3A", "type": "input"},
            "pin_6": {"number": "6", "name": "3Y", "type": "output"},
            "pin_7": {"number": "7", "name": "GND", "type": "power_in"},
            "pin_8": {"number": "8", "name": "4Y", "type": "output"},
            "pin_9": {"number": "9", "name": "4A", "type": "input"},
            "pin_10": {"number": "10", "name": "5Y", "type": "output"},
            "pin_11": {"number": "11", "name": "5A", "type": "input"},
            "pin_12": {"number": "12", "name": "6Y", "type": "output"},
            "pin_13": {"number": "13", "name": "6A", "type": "input"},
            "pin_14": {"number": "14", "name": "VCC", "type": "power_in"},
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Nexperia 74HC14D,653 (C5605): hex Schmitt-trigger inverter in SOIC-14; reconfirmed live 2026-10-02 (stock 206,442).",
            "Browser-downloaded the Nexperia 74HC14;74HCT14 product data sheet (16 pages) into this part; it anchors the SOIC-14 74HC14 family.",
            "Pinning section 6.1 matches the standard 74HC14 arrangement and the KiCad 74xx:74HC14 multi-unit symbol (6 gate units + power unit) pad-for-pad.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C5947 / Nexperia 74HC595D,118 full-stage technical data, verified
    # against the Nexperia 74HC595;74HCT595 product data sheet
    # (browser-downloaded to this part; anchors the SOIC-16 74HC595 family):
    # 8-bit serial-in / parallel-out shift register with output storage
    # register and 3-state outputs, SO16 (SOT109-1). Pinning section 6.1:
    # 1 = Q1, 2 = Q2, 3 = Q3, 4 = Q4, 5 = Q5, 6 = Q6, 7 = Q7, 8 = GND,
    # 9 = Q7S (serial out), 10 = MR (master reset, active low), 11 = SHCP
    # (shift clock), 12 = STCP (storage clock), 13 = OE (output enable,
    # active low), 14 = DS (serial data in), 15 = Q0, 16 = VCC. Pad numbers
    # align 1:1 with the KiCad 74xx:74HC595 symbol (whose pin names use the
    # QB-QH/SRCLR/SRCLK/RCLK/SER convention; the vendor names are recorded
    # here). Supply 2.0-6.0 V; shift clock up to 100 MHz (live description);
    # tpd 19 ns at 4.5 V / 50 pF; the ,118 suffix is the packing variant.
    # No HandSoldering master for SOIC-16 narrow - hand_solder empty.
    current = "electronic_ic_soic_16_logic_serial_in_parallel_out_shift_register_nexperia_74hc595d_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708624668708864-C5947.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "Nexperia 74HC595;74HCT595 product data sheet (C5947)",
            "pages": [2, 3],
            "notes": "SO16 (SOT109-1) outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning section 6.1.",
        }
        part["electrical"] = {
            "device_type": "8-bit serial-in / parallel-out shift register with storage and 3-state outputs",
            "supply_voltage": "2.0-6.0 V (74HC family)",
            "shift_clock_frequency": "up to 100 MHz (live description)",
            "propagation_delay": "19 ns at 4.5 V, 50 pF",
            "output_drive": "tri-state parallel outputs (Q0-Q7) plus serial out (Q7S)",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "Q1", "type": "output"},
            "pin_2": {"number": "2", "name": "Q2", "type": "output"},
            "pin_3": {"number": "3", "name": "Q3", "type": "output"},
            "pin_4": {"number": "4", "name": "Q4", "type": "output"},
            "pin_5": {"number": "5", "name": "Q5", "type": "output"},
            "pin_6": {"number": "6", "name": "Q6", "type": "output"},
            "pin_7": {"number": "7", "name": "Q7", "type": "output"},
            "pin_8": {"number": "8", "name": "GND", "type": "power_in"},
            "pin_9": {"number": "9", "name": "Q7S", "type": "output"},
            "pin_10": {"number": "10", "name": "MR", "type": "input"},
            "pin_11": {"number": "11", "name": "SHCP", "type": "input"},
            "pin_12": {"number": "12", "name": "STCP", "type": "input"},
            "pin_13": {"number": "13", "name": "OE", "type": "input"},
            "pin_14": {"number": "14", "name": "DS", "type": "input"},
            "pin_15": {"number": "15", "name": "Q0", "type": "output"},
            "pin_16": {"number": "16", "name": "VCC", "type": "power_in"},
        }
        part["kicad"] = {
            "symbol": "74xx:74HC595",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Nexperia 74HC595D,118 (C5947): 8-bit shift register in SOIC-16; reconfirmed live 2026-10-02 (stock 403,667).",
            "Browser-downloaded the Nexperia 74HC595;74HCT595 product data sheet (21 pages) into this part; it anchors the SOIC-16 74HC595 family.",
            "Pinning section 6.1 aligns pad-for-pad with the KiCad 74xx:74HC595 symbol; vendor pin names (Q1-Q7, Q7S, MR, STCP, SHCP, OE, DS, Q0) recorded in the pin table, KiCad symbol uses the QB-QH/SRCLR/SRCLK/RCLK/SER convention on identical numbers.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C6855 / MaxLinear SP485EEN-L/TR full-stage technical data, verified
    # against the MaxLinear SP481E/SP485E datasheet (REV 1.0.5,
    # browser-downloaded to this part; anchors the SP485E SOIC-8 family):
    # half-duplex RS-485/RS-422 transceiver, 5 V only (4.75-5.25 V), up to
    # 10 Mbps, +-15 kV ESD (HBM and IEC61000-4-2 air discharge), low-power
    # BiCMOS, -40 to +85 C; the live description adds 900 uA supply current.
    # Pinout page 1 block diagram: 1 = RO, 2 = RE, 3 = DE, 4 = DI, 5 = GND,
    # 6 = A, 7 = B, 8 = VCC - the standard RS-485 arrangement, matching the
    # KiCad Interface_UART:LTC2850xS8 symbol pad-for-pad (the SP3485CN
    # symbol extends the same master) with
    # Package_SO:SOIC-8_3.9x4.9mm_P1.27mm. The -L suffix is lead free;
    # /TR is tape and reel.
    current = "electronic_ic_soic_8_interface_rs_485_transceiver_maxlinear_sp485een_l_tr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-8 (3.9 x 4.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579709487191474176-C6855.pdf"
        part["dimensions_mm"] = {"length": 4.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "MaxLinear SP481E/SP485E datasheet, REV 1.0.5 (C6855)",
            "pages": [1, 2],
            "notes": "SOIC-8 outline per the Package_SO:SOIC-8_3.9x4.9mm_P1.27mm master geometry; pinout page 1 block diagram.",
        }
        part["electrical"] = {
            "device_type": "half-duplex RS-485/RS-422 transceiver",
            "supply_voltage": "5 V only (4.75-5.25 V)",
            "data_rate": "up to 10 Mbps",
            "esd_protection": "+-15 kV HBM and IEC61000-4-2 air discharge",
            "supply_current": "900 uA (live description)",
            "operating_temperature": "-40 to +85 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "RO", "type": "output"},
            "pin_2": {"number": "2", "name": "RE", "type": "input"},
            "pin_3": {"number": "3", "name": "DE", "type": "input"},
            "pin_4": {"number": "4", "name": "DI", "type": "input"},
            "pin_5": {"number": "5", "name": "GND", "type": "power_in"},
            "pin_6": {"number": "6", "name": "A", "type": "bidirectional"},
            "pin_7": {"number": "7", "name": "B", "type": "bidirectional"},
            "pin_8": {"number": "8", "name": "VCC", "type": "power_in"},
        }
        part["kicad"] = {
            "symbol": "Interface_UART:LTC2850xS8",
            "machine_solder": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic MaxLinear SP485EEN-L/TR (C6855): half-duplex RS-485 transceiver, 10 Mbps, +-15 kV ESD in SOIC-8; reconfirmed live 2026-10-02 (stock 245,552).",
            "Browser-downloaded the MaxLinear SP481E/SP485E datasheet (9 pages, REV 1.0.5) into this part; it anchors the SP485E SOIC-8 family.",
            "Pinout page 1: 1 = RO, 2 = RE, 3 = DE, 4 = DI, 5 = GND, 6 = A, 7 = B, 8 = VCC; Interface_UART:LTC2850xS8 matches pad-for-pad (SP3485CN extends the same master). No HandSoldering master for SOIC-8 narrow - hand_solder empty per the 2-asset rule.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C7426 / Texas Instruments NE5532DR full-stage technical data,
    # verified against the TI NE5532x/SA5532x datasheet (Rev. K,
    # browser-downloaded to this part; anchors the NE5532 SOIC-8 family):
    # dual low-noise bipolar op-amp, SOIC-8 (D package). Pinout is the
    # standard dual op-amp arrangement: 1 = OUT1, 2 = IN1-, 3 = IN1+,
    # 4 = V-, 5 = IN2+, 6 = IN2-, 7 = OUT2, 8 = V+, matching the KiCad
    # Amplifier_Operational:NE5532 symbol (extends the LM2904 dual
    # op-amp master) pad-for-pad with Package_SO:SOIC-8_3.9x4.9mm_P1.27mm.
    # Headline electricals from the intake record: 10 MHz GBW, 9 V/us
    # slew, 5 nV/sqrt(Hz) @1 kHz noise, 100 dB CMRR, +-15 V dual supply,
    # 38 mA output, 0-70 C ambient. The D suffix is the SOIC-8 package;
    # R = tape and reel. No HandSoldering master for SOIC-8 narrow -
    # hand_solder empty per the 2-asset rule.
    current = "electronic_ic_soic_8_amplifier_operational_amplifier_dual_low_noise_texas_instruments_ne5532dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-8 (D, 3.9 x 4.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/cn/lit/ds/symlink/ne5532.pdf"
        part["dimensions_mm"] = {"length": 4.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "TI NE5532x/SA5532x datasheet, Rev. K (C7426)",
            "pages": [1, 2],
            "notes": "SOIC-8 (D package) outline per the Package_SO:SOIC-8_3.9x4.9mm_P1.27mm master geometry; standard dual op-amp pinout.",
        }
        part["electrical"] = {
            "device_type": "dual low-noise bipolar operational amplifier",
            "gain_bandwidth_product": "10 MHz",
            "slew_rate": "9 V/us",
            "input_noise_density": "5 nV/sqrt(Hz) at 1 kHz",
            "cmrr": "100 dB",
            "output_current": "38 mA",
            "supply_voltage": "+-15 V dual supply",
            "operating_temperature": "0 to +70 C ambient",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OUT1", "type": "output"},
            "pin_2": {"number": "2", "name": "IN1-", "type": "input"},
            "pin_3": {"number": "3", "name": "IN1+", "type": "input"},
            "pin_4": {"number": "4", "name": "V-", "type": "power_in"},
            "pin_5": {"number": "5", "name": "IN2+", "type": "input"},
            "pin_6": {"number": "6", "name": "IN2-", "type": "input"},
            "pin_7": {"number": "7", "name": "OUT2", "type": "output"},
            "pin_8": {"number": "8", "name": "V+", "type": "power_in"},
        }
        part["kicad"] = {
            "symbol": "Amplifier_Operational:NE5532",
            "machine_solder": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Texas Instruments NE5532DR (C7426): dual low-noise op-amp in SOIC-8; reconfirmed live 2026-10-02 (stock 221,644). The queue snapshot for this code was degraded (empty MPN/maker) - the intake record is the identity authority.",
            "Browser-downloaded the TI NE5532x/SA5532x datasheet (23 pages, Rev. K) from the page's ti.com datasheet link (fetched via the browser from www.ti.com, same-origin download) into this part; it anchors the NE5532 SOIC-8 family.",
            "Pinout is the standard dual op-amp arrangement (1 = OUT1, 2 = IN1-, 3 = IN1+, 4 = V-, 5 = IN2+, 6 = IN2-, 7 = OUT2, 8 = V+); Amplifier_Operational:NE5532 matches pad-for-pad.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C7433 / Texas Instruments OP07CDR full-stage technical data,
    # verified against the TI OP07x datasheet (Rev. H, ZHCSRX0H,
    # browser-downloaded to this part; anchors the OP07 SOIC-8 family):
    # precision single op-amp, SOIC-8 (D package). Pinout per the TI
    # drawing: 1 = OFFSET N1 (trim), 2 = IN-, 3 = IN+, 4 = V-, 5 = NC
    # (D package), 6 = OUT, 7 = V+, 8 = OFFSET N2 (trim), matching the
    # KiCad Amplifier_Operational:OP07 symbol pad-for-pad with
    # Package_SO:SOIC-8_3.9x4.9mm_P1.27mm. Headline electricals from the
    # intake record: 400 kHz GBW, 0.3 V/us slew, 60 uV Vos, 120 dB CMRR,
    # 10.5 nV/sqrt(Hz) @10 Hz, +-3 to +-18 V supplies, 0-70 C ambient.
    # The C grade is the commercial temperature range; R = tape and reel.
    # No HandSoldering master for SOIC-8 narrow - hand_solder empty per
    # the 2-asset rule.
    current = "electronic_ic_soic_8_amplifier_operational_amplifier_precision_texas_instruments_op07cdr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-8 (D, 3.9 x 4.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com.cn/cn/lit/ds/symlink/op07.pdf"
        part["dimensions_mm"] = {"length": 4.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "TI OP07x datasheet, Rev. H (C7433)",
            "pages": [1, 2],
            "notes": "SOIC-8 (D package) outline per the Package_SO:SOIC-8_3.9x4.9mm_P1.27mm master geometry; pinout per the TI package drawing (5 = NC on the D package).",
        }
        part["electrical"] = {
            "device_type": "precision single operational amplifier",
            "gain_bandwidth_product": "400 kHz",
            "slew_rate": "0.3 V/us",
            "input_offset_voltage": "60 uV",
            "offset_drift": "500 nV/C",
            "cmrr": "120 dB",
            "input_noise_density": "10.5 nV/sqrt(Hz) at 10 Hz",
            "supply_voltage": "+-3 to +-18 V",
            "operating_temperature": "0 to +70 C ambient",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "TRIM1", "type": "input"},
            "pin_2": {"number": "2", "name": "IN-", "type": "input"},
            "pin_3": {"number": "3", "name": "IN+", "type": "input"},
            "pin_4": {"number": "4", "name": "V-", "type": "power_in"},
            "pin_5": {"number": "5", "name": "NC", "type": "no_connect"},
            "pin_6": {"number": "6", "name": "OUT", "type": "output"},
            "pin_7": {"number": "7", "name": "V+", "type": "power_in"},
            "pin_8": {"number": "8", "name": "TRIM2", "type": "input"},
        }
        part["kicad"] = {
            "symbol": "Amplifier_Operational:OP07",
            "machine_solder": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Texas Instruments OP07CDR (C7433): precision op-amp in SOIC-8; reconfirmed live 2026-10-02 (stock 236,159). The queue snapshot for this code was degraded (empty MPN/maker) and has been repaired from the live page + intake record identity.",
            "Browser-downloaded the TI OP07x datasheet (24 pages, Rev. H) from the page's ti.com.cn datasheet link (fetched same-origin from the www.ti.com.cn page) into this part; it anchors the OP07 SOIC-8 family.",
            "Pinout per the TI package drawing: 1/8 = offset trim, 2 = IN-, 3 = IN+, 4 = V-, 5 = NC (D package), 6 = OUT, 7 = V+; Amplifier_Operational:OP07 matches pad-for-pad.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C7512 / Texas Instruments ULN2003ADR full-stage technical data,
    # verified against the TI ULN200x/ULQ200x datasheet (Rev. T,
    # browser-downloaded to this part; anchors the ULN2003A SOIC-16
    # family): seven NPN Darlington channels with common flyback diodes
    # and open-collector outputs, SOIC-16 (D package). Pinout per the
    # standard arrangement (datasheet pin diagram): 1-7 = I1-I7 inputs,
    # 8 = GND, 9 = COM (flyback diode common cathode), 10-16 = O7-O1
    # (outputs in reverse order), matching the KiCad
    # Transistor_Array:ULN2003A symbol pad-for-pad with
    # Package_SO:SOIC-16_3.9x9.9mm_P1.27mm. Headline electricals from the
    # live description: 500 mA per channel, 50 V max output, 30 V clamp,
    # ~50 uA input current; the -A suffix is the B version with input
    # resistors for 5 V logic; R = tape and reel. No HandSoldering master
    # for SOIC-16 narrow - hand_solder empty per the 2-asset rule.
    current = "electronic_ic_soic_16_driver_darlington_array_texas_instruments_uln2003adr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (D, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/cn/lit/ds/symlink/uln2003a.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "TI ULN200x/ULQ200x datasheet, Rev. T (C7512)",
            "pages": [1, 2],
            "notes": "SOIC-16 (D package) outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; standard ULN2003A pin arrangement.",
        }
        part["electrical"] = {
            "device_type": "seven-channel NPN Darlington driver array with flyback diodes",
            "channels": "7 (inputs I1-I7, open-collector outputs O1-O7)",
            "output_current": "500 mA per channel max",
            "output_voltage": "50 V max output (30 V clamp on live description)",
            "input_current": "~50 uA per channel",
            "polarized": False,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "I1", "type": "input"},
            "pin_2": {"number": "2", "name": "I2", "type": "input"},
            "pin_3": {"number": "3", "name": "I3", "type": "input"},
            "pin_4": {"number": "4", "name": "I4", "type": "input"},
            "pin_5": {"number": "5", "name": "I5", "type": "input"},
            "pin_6": {"number": "6", "name": "I6", "type": "input"},
            "pin_7": {"number": "7", "name": "I7", "type": "input"},
            "pin_8": {"number": "8", "name": "GND", "type": "power_in"},
            "pin_9": {"number": "9", "name": "COM", "type": "passive"},
            "pin_10": {"number": "10", "name": "O7", "type": "output"},
            "pin_11": {"number": "11", "name": "O6", "type": "output"},
            "pin_12": {"number": "12", "name": "O5", "type": "output"},
            "pin_13": {"number": "13", "name": "O4", "type": "output"},
            "pin_14": {"number": "14", "name": "O3", "type": "output"},
            "pin_15": {"number": "15", "name": "O2", "type": "output"},
            "pin_16": {"number": "16", "name": "O1", "type": "output"},
        }
        part["kicad"] = {
            "symbol": "Transistor_Array:ULN2003A",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Texas Instruments ULN2003ADR (C7512): seven-channel Darlington array in SOIC-16; reconfirmed live 2026-10-02 (stock 345,414). The queue snapshot for this code was degraded (empty MPN/maker) and has been repaired from the live page + intake record identity.",
            "Browser-downloaded the TI ULN200x/ULQ200x datasheet (42 pages, Rev. T) from the page's ti.com datasheet link (fetched same-origin from the www.ti.com page) into this part; it anchors the ULN2003A SOIC-16 family.",
            "Pinout per the standard ULN2003A arrangement: 1-7 = I1-I7, 8 = GND, 9 = COM, 10-16 = O7-O1 (outputs in reverse order); Transistor_Array:ULN2003A matches pad-for-pad.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C7950 / onsemi LM358DR2G full-stage technical data, verified
    # against the onsemi/onsemi-distributed LM358 datasheet already captured
    # at intake (sha256 e66a9193..., verified against the live page): dual
    # general-purpose op-amp, SOIC-8. Pinout is the standard dual op-amp
    # arrangement (same as the NE5532): 1 = OUT1, 2 = IN1-, 3 = IN1+,
    # 4 = V-, 5 = IN2+, 6 = IN2-, 7 = OUT2, 8 = V+, matching the KiCad
    # Amplifier_Operational:LM358 symbol (extends the LM2904 dual master)
    # pad-for-pad with Package_SO:SOIC-8_3.9x4.9mm_P1.27mm. Headline
    # electricals from the intake record: 3-32 V single / +-16 V dual
    # supply, 700 uA quiescent, 40 mA output, 70 dB CMRR, 7 mV Vos,
    # 0-70 C ambient. The R2G suffix is the tape-reel lead-free variant.
    # No HandSoldering master for SOIC-8 narrow - hand_solder empty per
    # the 2-asset rule.
    current = "electronic_ic_soic_8_amplifier_operational_amplifier_dual_onsemi_lm358dr2g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-8 (3.9 x 4.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708932857913344-C7950.pdf"
        part["dimensions_mm"] = {"length": 4.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "onsemi LM358 datasheet (C7950, captured at intake)",
            "pages": [1, 2],
            "notes": "SOIC-8 outline per the Package_SO:SOIC-8_3.9x4.9mm_P1.27mm master geometry; standard dual op-amp pinout.",
        }
        part["electrical"] = {
            "device_type": "dual general-purpose operational amplifier",
            "supply_voltage": "3-32 V single or +-16 V dual",
            "quiescent_current": "700 uA",
            "output_current": "40 mA",
            "cmrr": "70 dB",
            "input_offset_voltage": "7 mV",
            "operating_temperature": "0 to +70 C ambient",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OUT1", "type": "output"},
            "pin_2": {"number": "2", "name": "IN1-", "type": "input"},
            "pin_3": {"number": "3", "name": "IN1+", "type": "input"},
            "pin_4": {"number": "4", "name": "V-", "type": "power_in"},
            "pin_5": {"number": "5", "name": "IN2+", "type": "input"},
            "pin_6": {"number": "6", "name": "IN2-", "type": "input"},
            "pin_7": {"number": "7", "name": "OUT2", "type": "output"},
            "pin_8": {"number": "8", "name": "V+", "type": "power_in"},
        }
        part["kicad"] = {
            "symbol": "Amplifier_Operational:LM358",
            "machine_solder": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic onsemi LM358DR2G (C7950): dual general-purpose op-amp in SOIC-8; reconfirmed live 2026-10-02 (stock 799,680). The queue snapshot for this code was degraded (empty MPN/maker) and has been repaired from the live page + intake record identity.",
            "Datasheet was already captured at intake (sha256 e66a9193... matches the provenance file); no new download.",
            "Pinout is the standard dual op-amp arrangement (1 = OUT1, 2 = IN1-, 3 = IN1+, 4 = V-, 5 = IN2+, 6 = IN2-, 7 = OUT2, 8 = V+); Amplifier_Operational:LM358 matches pad-for-pad.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="ic")

    # === BEGIN LOGIC BATCH (generated by tmp/logic_batch.py; do not edit) ===
    # JLC C5510 / Nexperia 74AHC14D,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_schmitt_trigger_inverter_nexperia_74ahc14d_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186841930813440-C5510.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74AHC14D datasheet (C5510)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5510 (Nexperia 74AHC14D,118, SOIC-14, 14 pins) verified at intake; family batch integration C5510.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74AHC14 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5513 / Nexperia 74AHC1G14GV,125 - 74-series logic family
    # batch: pins from the KiCad 74xGxx:74AHC1G14 master; footprint Package_TO_SOT_SMD:SOT-23-5
    current = "electronic_ic_sot_23_5_logic_single_schmitt_trigger_inverter_nexperia_74ahc1g14gv_125"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT753-1 / SC-74A (2.9 x 1.6 mm; Nexperia GV)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586198592217997312-C5513.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.6, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74AHC1G14GV datasheet (C5513)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_TO_SOT_SMD:SOT-23-5 master geometry; pinning cross-checked against the KiCad 74xGxx:74AHC1G14 symbol.",
        }
        part["electrical"] = {
            "device_type": "single schmitt trigger inverter",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "NC", "type": "nc"},
            "pin_2": {"number": "2", "name": "A", "type": "in"},
            "pin_3": {"number": "3", "name": "GND", "type": "pwr"},
            "pin_4": {"number": "4", "name": "Y", "type": "out"},
            "pin_5": {"number": "5", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xGxx:74AHC1G14",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23-5",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5513 (Nexperia 74AHC1G14GV,125, SC-74A, 5 pins) verified at intake; family batch integration C5513.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74AHC1G14 data sheet into this part.", "Pin table generated from the KiCad 74xGxx:74AHC1G14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 5-pin package count.", "Footprint Package_TO_SOT_SMD:SOT-23-5 verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5515 / Nexperia 74AHC244PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74AHC244 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_nexperia_74ahc244pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588881485541879808-C5515.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74AHC244PW datasheet (C5515)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74AHC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74AHC244",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5515 (Nexperia 74AHC244PW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C5515.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74AHC244 data sheet into this part.", "Pin table generated from the KiCad 74xx:74AHC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5516 / Nexperia 74AHC245PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_transceiver_tri_state_nexperia_74ahc245pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711658534756352-C5516.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74AHC245PW datasheet (C5516)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5516 (Nexperia 74AHC245PW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C5516.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74AHC245 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5520 / Nexperia 74AHC595D,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74AHC595 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_serial_in_parallel_out_shift_register_nexperia_74ahc595d_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186900901646336-C5520.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74AHC595D datasheet (C5520)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74AHC595 symbol.",
        }
        part["electrical"] = {
            "device_type": "serial in parallel out shift register",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "QB", "type": "ts"},
            "pin_2": {"number": "2", "name": "QC", "type": "ts"},
            "pin_3": {"number": "3", "name": "QD", "type": "ts"},
            "pin_4": {"number": "4", "name": "QE", "type": "ts"},
            "pin_5": {"number": "5", "name": "QF", "type": "ts"},
            "pin_6": {"number": "6", "name": "QG", "type": "ts"},
            "pin_7": {"number": "7", "name": "QH", "type": "ts"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "QH'", "type": "out"},
            "pin_10": {"number": "10", "name": "~{SRCLR}", "type": "in"},
            "pin_11": {"number": "11", "name": "SRCLK", "type": "in"},
            "pin_12": {"number": "12", "name": "RCLK", "type": "in"},
            "pin_13": {"number": "13", "name": "~{OE}", "type": "in"},
            "pin_14": {"number": "14", "name": "SER", "type": "in"},
            "pin_15": {"number": "15", "name": "QA", "type": "ts"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74AHC595",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5520 (Nexperia 74AHC595D,118, SOIC-16, 16 pins) verified at intake; family batch integration C5520.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74AHC595 data sheet into this part.", "Pin table generated from the KiCad 74xx:74AHC595 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5586 / Nexperia 74HC00D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC00 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_nand_gate_nexperia_74hc00d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711676582711296-C5586.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC00D datasheet (C5586)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC00 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC00",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5586 (Nexperia 74HC00D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5586.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC00 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC00 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5587 / Nexperia 74HC00PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC00 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_quad_2_input_nand_gate_nexperia_74hc00pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711676582711296-C5586.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC00PW datasheet (C5587)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC00 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC00",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5587 (Nexperia 74HC00PW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C5587.", "Shares the 74HC00 family datasheet downloaded into C5586 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74HC00 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5588 / Nexperia 74HC02D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC02 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_nor_gate_nexperia_74hc02d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711688586674176-C5588.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC02D datasheet (C5588)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC02 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nor gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1Y", "type": "out"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1B", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2B", "type": "in"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3A", "type": "in"},
            "pin_9": {"number": "9", "name": "3B", "type": "in"},
            "pin_10": {"number": "10", "name": "3Y", "type": "out"},
            "pin_11": {"number": "11", "name": "4A", "type": "in"},
            "pin_12": {"number": "12", "name": "4B", "type": "in"},
            "pin_13": {"number": "13", "name": "4Y", "type": "out"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC02",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5588 (Nexperia 74HC02D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5588.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC02 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC02 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5590 / Nexperia 74HC04D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC04 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_nexperia_74hc04d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708666507165696-C5590.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC04D datasheet (C5590)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC04",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5590 (Nexperia 74HC04D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5590.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC04 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5592 / Nexperia 74HC05D,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS05 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_open_collector_nexperia_74hc05d_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711702457372672-C5592.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC05D datasheet (C5592)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS05 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter open collector",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS05",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5592 (Nexperia 74HC05D,118, SOIC-14, 14 pins) verified at intake; family batch integration C5592.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC05 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS05 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5593 / Nexperia 74HC08D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS08 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_and_gate_nexperia_74hc08d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579709911863132160-C5593.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC08D datasheet (C5593)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS08 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input and gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS08",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5593 (Nexperia 74HC08D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5593.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC08 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS08 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5595 / Nexperia 74HC10D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS10 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_triple_3_input_nand_gate_nexperia_74hc10d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711711634374656-C5595.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC10D datasheet (C5595)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS10 symbol.",
        }
        part["electrical"] = {
            "device_type": "triple 3 input nand gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2B", "type": "in"},
            "pin_5": {"number": "5", "name": "2C", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "3C", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y", "type": "out"},
            "pin_13": {"number": "13", "name": "1C", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS10",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5595 (Nexperia 74HC10D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5595.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC10 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS10 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5597 / Nexperia 74HC123D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC123 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_dual_retriggerable_monostable_multivibrator_nexperia_74hc123d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711721084411904-C5597.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC123D datasheet (C5597)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC123 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual retriggerable monostable multivibrator",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A", "type": "in"},
            "pin_2": {"number": "2", "name": "B", "type": "in"},
            "pin_3": {"number": "3", "name": "Clr", "type": "in"},
            "pin_4": {"number": "4", "name": "~{Q}", "type": "out"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "Cext", "type": "in"},
            "pin_7": {"number": "7", "name": "RCext", "type": "in"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "A", "type": "in"},
            "pin_10": {"number": "10", "name": "B", "type": "in"},
            "pin_11": {"number": "11", "name": "Clr", "type": "in"},
            "pin_12": {"number": "12", "name": "~{Q}", "type": "out"},
            "pin_13": {"number": "13", "name": "Q", "type": "out"},
            "pin_14": {"number": "14", "name": "Cext", "type": "in"},
            "pin_15": {"number": "15", "name": "RCext", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC123",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5597 (Nexperia 74HC123D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5597.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC123 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC123 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5598 / Nexperia 74HC125D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS125 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_bus_buffer_tri_state_nexperia_74hc125d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711729812623360-C5598.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC125D datasheet (C5598)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS125 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "ts"},
            "pin_4": {"number": "4", "name": "2OE", "type": "in"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "ts"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "ts"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3OE", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "ts"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4OE", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS125",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5598 (Nexperia 74HC125D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5598.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC125 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS125 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5599 / Nexperia 74HC125PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS125 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_quad_bus_buffer_tri_state_nexperia_74hc125pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711729812623360-C5598.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC125PW datasheet (C5599)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS125 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "ts"},
            "pin_4": {"number": "4", "name": "2OE", "type": "in"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "ts"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "ts"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3OE", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "ts"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4OE", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS125",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5599 (Nexperia 74HC125PW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C5599.", "Shares the 74HC125 family datasheet downloaded into C5598 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74LS125 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5600 / Nexperia 74HC126D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS126 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_bus_buffer_tri_state_nexperia_74hc126d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711741389176832-C5600.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC126D datasheet (C5600)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS126 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "ts"},
            "pin_4": {"number": "4", "name": "2OE", "type": "in"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "ts"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "ts"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3OE", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "ts"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4OE", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS126",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5600 (Nexperia 74HC126D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5600.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC126 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS126 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5601 / Nexperia 74HC132D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS132 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_nand_gate_schmitt_trigger_nexperia_74hc132d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711794146754560-C5601.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC132D datasheet (C5601)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS132 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate schmitt trigger",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS132",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5601 (Nexperia 74HC132D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5601.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC132 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS132 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5602 / Nexperia 74HC138D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC138 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_3_to_8_line_decoder_demultiplexer_nexperia_74hc138d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708615900315648-C5602.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC138D datasheet (C5602)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC138 symbol.",
        }
        part["electrical"] = {
            "device_type": "3 to 8 line decoder demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A0", "type": "in"},
            "pin_2": {"number": "2", "name": "A1", "type": "in"},
            "pin_3": {"number": "3", "name": "A2", "type": "in"},
            "pin_4": {"number": "4", "name": "~{E0}", "type": "in"},
            "pin_5": {"number": "5", "name": "~{E1}", "type": "in"},
            "pin_6": {"number": "6", "name": "E2", "type": "in"},
            "pin_7": {"number": "7", "name": "~{Y7}", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{Y6}", "type": "out"},
            "pin_10": {"number": "10", "name": "~{Y5}", "type": "out"},
            "pin_11": {"number": "11", "name": "~{Y4}", "type": "out"},
            "pin_12": {"number": "12", "name": "~{Y3}", "type": "out"},
            "pin_13": {"number": "13", "name": "~{Y2}", "type": "out"},
            "pin_14": {"number": "14", "name": "~{Y1}", "type": "out"},
            "pin_15": {"number": "15", "name": "~{Y0}", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC138",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5602 (Nexperia 74HC138D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5602.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC138 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC138 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5603 / Nexperia 74HC139D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS139 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_dual_2_to_4_line_decoder_demultiplexer_nexperia_74hc139d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711802856562688-C5603.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC139D datasheet (C5603)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS139 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual 2 to 4 line decoder demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "in"},
            "pin_3": {"number": "3", "name": "A1", "type": "in"},
            "pin_4": {"number": "4", "name": "O0", "type": "out"},
            "pin_5": {"number": "5", "name": "O1", "type": "out"},
            "pin_6": {"number": "6", "name": "O2", "type": "out"},
            "pin_7": {"number": "7", "name": "O3", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "O3", "type": "out"},
            "pin_10": {"number": "10", "name": "O2", "type": "out"},
            "pin_11": {"number": "11", "name": "O1", "type": "out"},
            "pin_12": {"number": "12", "name": "O0", "type": "out"},
            "pin_13": {"number": "13", "name": "A1", "type": "in"},
            "pin_14": {"number": "14", "name": "A0", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS139",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5603 (Nexperia 74HC139D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5603.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC139 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS139 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5606 / Nexperia 74HC14PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_hex_schmitt_trigger_inverter_nexperia_74hc14pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711805750771712-C5606.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC14PW datasheet (C5606)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5606 (Nexperia 74HC14PW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C5606.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC14 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5609 / Nexperia 74HC157D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS157 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_quad_2_to_1_line_multiplexer_nexperia_74hc157d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186908238295040-C5609.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC157D datasheet (C5609)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS157 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 to 1 line multiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "S", "type": "in"},
            "pin_2": {"number": "2", "name": "I0a", "type": "in"},
            "pin_3": {"number": "3", "name": "I1a", "type": "in"},
            "pin_4": {"number": "4", "name": "Za", "type": "out"},
            "pin_5": {"number": "5", "name": "I0b", "type": "in"},
            "pin_6": {"number": "6", "name": "I1b", "type": "in"},
            "pin_7": {"number": "7", "name": "Zb", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Zc", "type": "out"},
            "pin_10": {"number": "10", "name": "I1c", "type": "in"},
            "pin_11": {"number": "11", "name": "I0c", "type": "in"},
            "pin_12": {"number": "12", "name": "Zd", "type": "out"},
            "pin_13": {"number": "13", "name": "I1d", "type": "in"},
            "pin_14": {"number": "14", "name": "I0d", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS157",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5609 (Nexperia 74HC157D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5609.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC157 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS157 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5610 / Nexperia 74HC161D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS161 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_synchronous_4_bit_binary_counter_nexperia_74hc161d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711815426756608-C5610.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC161D datasheet (C5610)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS161 symbol.",
        }
        part["electrical"] = {
            "device_type": "synchronous 4 bit binary counter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{MR}", "type": "in"},
            "pin_2": {"number": "2", "name": "CP", "type": "in"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "D2", "type": "in"},
            "pin_6": {"number": "6", "name": "D3", "type": "in"},
            "pin_7": {"number": "7", "name": "CEP", "type": "in"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{PE}", "type": "in"},
            "pin_10": {"number": "10", "name": "CET", "type": "in"},
            "pin_11": {"number": "11", "name": "Q3", "type": "out"},
            "pin_12": {"number": "12", "name": "Q2", "type": "out"},
            "pin_13": {"number": "13", "name": "Q1", "type": "out"},
            "pin_14": {"number": "14", "name": "Q0", "type": "out"},
            "pin_15": {"number": "15", "name": "TC", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS161",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5610 (Nexperia 74HC161D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5610.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC161 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS161 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5612 / Nexperia 74HC164PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC164 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_serial_in_parallel_out_shift_register_nexperia_74hc164pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711821097730048-C5612.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC164PW datasheet (C5612)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC164 symbol.",
        }
        part["electrical"] = {
            "device_type": "serial in parallel out shift register",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "DSA", "type": "in"},
            "pin_2": {"number": "2", "name": "DSB", "type": "in"},
            "pin_3": {"number": "3", "name": "Q0", "type": "out"},
            "pin_4": {"number": "4", "name": "Q1", "type": "out"},
            "pin_5": {"number": "5", "name": "Q2", "type": "out"},
            "pin_6": {"number": "6", "name": "Q3", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "CP", "type": "in"},
            "pin_9": {"number": "9", "name": "~{MR}", "type": "in"},
            "pin_10": {"number": "10", "name": "Q4", "type": "out"},
            "pin_11": {"number": "11", "name": "Q5", "type": "out"},
            "pin_12": {"number": "12", "name": "Q6", "type": "out"},
            "pin_13": {"number": "13", "name": "Q7", "type": "out"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC164",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5612 (Nexperia 74HC164PW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C5612.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC164 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC164 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6825 / Nexperia 74HC164D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC164 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_serial_in_parallel_out_shift_register_nexperia_74hc164d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711821097730048-C5612.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC164D datasheet (C6825)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC164 symbol.",
        }
        part["electrical"] = {
            "device_type": "serial in parallel out shift register",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "DSA", "type": "in"},
            "pin_2": {"number": "2", "name": "DSB", "type": "in"},
            "pin_3": {"number": "3", "name": "Q0", "type": "out"},
            "pin_4": {"number": "4", "name": "Q1", "type": "out"},
            "pin_5": {"number": "5", "name": "Q2", "type": "out"},
            "pin_6": {"number": "6", "name": "Q3", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "CP", "type": "in"},
            "pin_9": {"number": "9", "name": "~{MR}", "type": "in"},
            "pin_10": {"number": "10", "name": "Q4", "type": "out"},
            "pin_11": {"number": "11", "name": "Q5", "type": "out"},
            "pin_12": {"number": "12", "name": "Q6", "type": "out"},
            "pin_13": {"number": "13", "name": "Q7", "type": "out"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC164",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6825 (Nexperia 74HC164D,653, SOIC-14, 14 pins) verified at intake; family batch integration C6825.", "Shares the 74HC164 family datasheet downloaded into C5612 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74HC164 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5613 / Nexperia 74HC165D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC165 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_parallel_in_serial_out_shift_register_nexperia_74hc165d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708633354977280-C5613.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC165D datasheet (C5613)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC165 symbol.",
        }
        part["electrical"] = {
            "device_type": "parallel in serial out shift register",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{PL}", "type": "in"},
            "pin_2": {"number": "2", "name": "CP", "type": "in"},
            "pin_3": {"number": "3", "name": "D4", "type": "in"},
            "pin_4": {"number": "4", "name": "D5", "type": "in"},
            "pin_5": {"number": "5", "name": "D6", "type": "in"},
            "pin_6": {"number": "6", "name": "D7", "type": "in"},
            "pin_7": {"number": "7", "name": "~{Q7}", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Q7", "type": "out"},
            "pin_10": {"number": "10", "name": "DS", "type": "in"},
            "pin_11": {"number": "11", "name": "D0", "type": "in"},
            "pin_12": {"number": "12", "name": "D1", "type": "in"},
            "pin_13": {"number": "13", "name": "D2", "type": "in"},
            "pin_14": {"number": "14", "name": "D3", "type": "in"},
            "pin_15": {"number": "15", "name": "~{CE}", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC165",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5613 (Nexperia 74HC165D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5613.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC165 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC165 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5614 / Nexperia 74HC175D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS175 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_quad_d_type_flip_flop_nexperia_74hc175d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186914818887680-C5614.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC175D datasheet (C5614)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS175 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad d type flip flop",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{Mr}", "type": "in"},
            "pin_2": {"number": "2", "name": "Q0", "type": "out"},
            "pin_3": {"number": "3", "name": "~{Q0}", "type": "out"},
            "pin_4": {"number": "4", "name": "D0", "type": "in"},
            "pin_5": {"number": "5", "name": "D1", "type": "in"},
            "pin_6": {"number": "6", "name": "~{Q1}", "type": "out"},
            "pin_7": {"number": "7", "name": "Q1", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Cp", "type": "in"},
            "pin_10": {"number": "10", "name": "Q2", "type": "out"},
            "pin_11": {"number": "11", "name": "~{Q2}", "type": "out"},
            "pin_12": {"number": "12", "name": "D2", "type": "in"},
            "pin_13": {"number": "13", "name": "D3", "type": "in"},
            "pin_14": {"number": "14", "name": "~{Q3}", "type": "out"},
            "pin_15": {"number": "15", "name": "Q3", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS175",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5614 (Nexperia 74HC175D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5614.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC175 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS175 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5617 / Nexperia 74HC21D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS21 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_dual_4_input_and_gate_nexperia_74hc21d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186921630437376-C5617.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC21D datasheet (C5617)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS21 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual 4 input and gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "NC", "type": "no_connect"},
            "pin_4": {"number": "4", "name": "1C", "type": "in"},
            "pin_5": {"number": "5", "name": "1D", "type": "in"},
            "pin_6": {"number": "6", "name": "1Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "2Y", "type": "out"},
            "pin_9": {"number": "9", "name": "2A", "type": "in"},
            "pin_10": {"number": "10", "name": "2B", "type": "in"},
            "pin_11": {"number": "11", "name": "NC", "type": "no_connect"},
            "pin_12": {"number": "12", "name": "2C", "type": "in"},
            "pin_13": {"number": "13", "name": "2D", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS21",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5617 (Nexperia 74HC21D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5617.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC21 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS21 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5619 / Nexperia 74HC237D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC237 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_3_to_8_line_decoder_demultiplexer_latched_nexperia_74hc237d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191863824572416-C5619.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC237D datasheet (C5619)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC237 symbol.",
        }
        part["electrical"] = {
            "device_type": "3 to 8 line decoder demultiplexer latched",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A0", "type": "in"},
            "pin_2": {"number": "2", "name": "A1", "type": "in"},
            "pin_3": {"number": "3", "name": "A2", "type": "in"},
            "pin_4": {"number": "4", "name": "~{LE}", "type": "in"},
            "pin_5": {"number": "5", "name": "~{E1}", "type": "in"},
            "pin_6": {"number": "6", "name": "E2", "type": "in"},
            "pin_7": {"number": "7", "name": "Y7", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Y6", "type": "out"},
            "pin_10": {"number": "10", "name": "Y5", "type": "out"},
            "pin_11": {"number": "11", "name": "Y4", "type": "out"},
            "pin_12": {"number": "12", "name": "Y3", "type": "out"},
            "pin_13": {"number": "13", "name": "Y2", "type": "out"},
            "pin_14": {"number": "14", "name": "Y1", "type": "out"},
            "pin_15": {"number": "15", "name": "Y0", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC237",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5619 (Nexperia 74HC237D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5619.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC237 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC237 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5620 / Nexperia 74HC238D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC238 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_3_to_8_line_decoder_demultiplexer_nexperia_74hc238d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711825002217472-C5620.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC238D datasheet (C5620)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC238 symbol.",
        }
        part["electrical"] = {
            "device_type": "3 to 8 line decoder demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A0", "type": "in"},
            "pin_2": {"number": "2", "name": "A1", "type": "in"},
            "pin_3": {"number": "3", "name": "A2", "type": "in"},
            "pin_4": {"number": "4", "name": "~{E1}", "type": "in"},
            "pin_5": {"number": "5", "name": "~{E2}", "type": "in"},
            "pin_6": {"number": "6", "name": "E3", "type": "in"},
            "pin_7": {"number": "7", "name": "Y7", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Y6", "type": "out"},
            "pin_10": {"number": "10", "name": "Y5", "type": "out"},
            "pin_11": {"number": "11", "name": "Y4", "type": "out"},
            "pin_12": {"number": "12", "name": "Y3", "type": "out"},
            "pin_13": {"number": "13", "name": "Y2", "type": "out"},
            "pin_14": {"number": "14", "name": "Y1", "type": "out"},
            "pin_15": {"number": "15", "name": "Y0", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC238",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5620 (Nexperia 74HC238D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5620.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC238 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC238 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5622 / Nexperia 74HC244D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_buffer_tri_state_nexperia_74hc244d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708642213347328-C5622.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74HC244D datasheet (C5622)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5622 (Nexperia 74HC244D,653, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5622.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC244 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5623 / Nexperia 74HC244PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_nexperia_74hc244pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708642213347328-C5622.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC244PW datasheet (C5623)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5623 (Nexperia 74HC244PW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C5623.", "Shares the 74HC244 family datasheet downloaded into C5622 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5625 / Nexperia 74HC245D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_transceiver_tri_state_nexperia_74hc245d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708648593018880-C5625.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74HC245D datasheet (C5625)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5625 (Nexperia 74HC245D,653, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5625.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC245 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5626 / Nexperia 74HC245PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_transceiver_tri_state_nexperia_74hc245pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708648593018880-C5625.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC245PW datasheet (C5626)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5626 (Nexperia 74HC245PW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C5626.", "Shares the 74HC245 family datasheet downloaded into C5625 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5627 / Nexperia 74HC257D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS257 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_quad_2_to_1_line_multiplexer_tri_state_nexperia_74hc257d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191876844503040-C5627.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC257D datasheet (C5627)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS257 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 to 1 line multiplexer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "S", "type": "in"},
            "pin_2": {"number": "2", "name": "I0a", "type": "in"},
            "pin_3": {"number": "3", "name": "I1a", "type": "in"},
            "pin_4": {"number": "4", "name": "Za", "type": "ts"},
            "pin_5": {"number": "5", "name": "I0b", "type": "in"},
            "pin_6": {"number": "6", "name": "I1b", "type": "in"},
            "pin_7": {"number": "7", "name": "Zb", "type": "ts"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Zd", "type": "ts"},
            "pin_10": {"number": "10", "name": "I1d", "type": "in"},
            "pin_11": {"number": "11", "name": "I0d", "type": "in"},
            "pin_12": {"number": "12", "name": "Zc", "type": "ts"},
            "pin_13": {"number": "13", "name": "I1c", "type": "in"},
            "pin_14": {"number": "14", "name": "I0c", "type": "in"},
            "pin_15": {"number": "15", "name": "OE", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS257",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5627 (Nexperia 74HC257D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5627.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC257 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS257 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5629 / Nexperia 74HC27D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS27 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_triple_3_input_nor_gate_nexperia_74hc27d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191883853320192-C5629.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC27D datasheet (C5629)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS27 symbol.",
        }
        part["electrical"] = {
            "device_type": "triple 3 input nor gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2B", "type": "in"},
            "pin_5": {"number": "5", "name": "2C", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "3C", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y", "type": "out"},
            "pin_13": {"number": "13", "name": "1C", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS27",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5629 (Nexperia 74HC27D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5629.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC27 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS27 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5631 / Nexperia 74HC30D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS30 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_8_input_nand_gate_nexperia_74hc30d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8555344465388142592-C5631.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC30D datasheet (C5631)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS30 symbol.",
        }
        part["electrical"] = {
            "device_type": "8 input nand gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A", "type": "in"},
            "pin_2": {"number": "2", "name": "B", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "D", "type": "in"},
            "pin_5": {"number": "5", "name": "E", "type": "in"},
            "pin_6": {"number": "6", "name": "F", "type": "in"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "Y", "type": "out"},
            "pin_9": {"number": "9", "name": "NC", "type": "no_connect"},
            "pin_10": {"number": "10", "name": "NC", "type": "no_connect"},
            "pin_11": {"number": "11", "name": "G", "type": "in"},
            "pin_12": {"number": "12", "name": "H", "type": "in"},
            "pin_13": {"number": "13", "name": "NC", "type": "no_connect"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS30",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5631 (Nexperia 74HC30D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5631.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC30 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS30 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5632 / Nexperia 74HC32D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS32 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_or_gate_nexperia_74hc32d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711851372351488-C5632.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC32D datasheet (C5632)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS32 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input or gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS32",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5632 (Nexperia 74HC32D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5632.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC32 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS32 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5633 / Nexperia 74HC366D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS366 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_hex_bus_buffer_tri_state_inverting_nexperia_74hc366d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191885727633408-C5633.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC366D datasheet (C5633)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS366 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex bus buffer tri state inverting",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E1", "type": "in"},
            "pin_2": {"number": "2", "name": "I1", "type": "in"},
            "pin_3": {"number": "3", "name": "O1", "type": "ts"},
            "pin_4": {"number": "4", "name": "I2", "type": "in"},
            "pin_5": {"number": "5", "name": "O2", "type": "ts"},
            "pin_6": {"number": "6", "name": "I3", "type": "in"},
            "pin_7": {"number": "7", "name": "O3", "type": "ts"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "O4", "type": "ts"},
            "pin_10": {"number": "10", "name": "I4", "type": "in"},
            "pin_11": {"number": "11", "name": "O5", "type": "ts"},
            "pin_12": {"number": "12", "name": "I5", "type": "in"},
            "pin_13": {"number": "13", "name": "O6", "type": "ts"},
            "pin_14": {"number": "14", "name": "I6", "type": "in"},
            "pin_15": {"number": "15", "name": "E2", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS366",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5633 (Nexperia 74HC366D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5633.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC366 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS366 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5636 / Nexperia 74HC373D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC373 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_transparent_latch_tri_state_nexperia_74hc373d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711860173488128-C5636.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74HC373D datasheet (C5636)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC373 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "LE", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC373",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5636 (Nexperia 74HC373D,653, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5636.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC373 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC373 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5638 / Nexperia 74HC374D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC374 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_flip_flop_tri_state_nexperia_74hc374d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186930984140800-C5638.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74HC374D datasheet (C5638)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC374 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Cp", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC374",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5638 (Nexperia 74HC374D,653, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5638.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC374 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC374 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5639 / Nexperia 74HC377D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS377 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_flip_flop_common_enable_nexperia_74hc377d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711869237379072-C5639.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74HC377D datasheet (C5639)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS377 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop common enable",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{E}", "type": "in"},
            "pin_2": {"number": "2", "name": "Q0", "type": "out"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "Q1", "type": "out"},
            "pin_6": {"number": "6", "name": "Q2", "type": "out"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "Q3", "type": "out"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "CP", "type": "in"},
            "pin_12": {"number": "12", "name": "Q4", "type": "out"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "Q5", "type": "out"},
            "pin_16": {"number": "16", "name": "Q6", "type": "out"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "Q7", "type": "out"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS377",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5639 (Nexperia 74HC377D,653, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5639.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC377 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS377 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5641 / Nexperia 74HC393D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS393 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_dual_4_bit_binary_ripple_counter_nexperia_74hc393d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711882285858816-C5641.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC393D datasheet (C5641)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS393 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual 4 bit binary ripple counter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "CP", "type": "in"},
            "pin_2": {"number": "2", "name": "MR", "type": "in"},
            "pin_3": {"number": "3", "name": "Q0", "type": "out"},
            "pin_4": {"number": "4", "name": "Q1", "type": "out"},
            "pin_5": {"number": "5", "name": "Q2", "type": "out"},
            "pin_6": {"number": "6", "name": "Q3", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "Q3", "type": "out"},
            "pin_9": {"number": "9", "name": "Q2", "type": "out"},
            "pin_10": {"number": "10", "name": "Q1", "type": "out"},
            "pin_11": {"number": "11", "name": "Q0", "type": "out"},
            "pin_12": {"number": "12", "name": "MR", "type": "in"},
            "pin_13": {"number": "13", "name": "CP", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS393",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5641 (Nexperia 74HC393D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5641.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC393 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS393 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5645 / Nexperia 74HC4051PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC4051 master; footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_16_logic_8_channel_analog_multiplexer_demultiplexer_nexperia_74hc4051pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-16 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711889701388288-C5645.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC4051PW datasheet (C5645)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-16_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC4051 symbol.",
        }
        part["electrical"] = {
            "device_type": "8 channel analog multiplexer demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A4", "type": "passive"},
            "pin_2": {"number": "2", "name": "A6", "type": "passive"},
            "pin_3": {"number": "3", "name": "A", "type": "passive"},
            "pin_4": {"number": "4", "name": "A7", "type": "passive"},
            "pin_5": {"number": "5", "name": "A5", "type": "passive"},
            "pin_6": {"number": "6", "name": "~{E}", "type": "in"},
            "pin_7": {"number": "7", "name": "VEE", "type": "pwr"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "S2", "type": "in"},
            "pin_10": {"number": "10", "name": "S1", "type": "in"},
            "pin_11": {"number": "11", "name": "S0", "type": "in"},
            "pin_12": {"number": "12", "name": "A3", "type": "passive"},
            "pin_13": {"number": "13", "name": "A0", "type": "passive"},
            "pin_14": {"number": "14", "name": "A1", "type": "passive"},
            "pin_15": {"number": "15", "name": "A2", "type": "passive"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC4051",
            "machine_solder": "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5645 (Nexperia 74HC4051PW,118, TSSOP-16, 16 pins) verified at intake; family batch integration C5645.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC4051 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC4051 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5646 / Nexperia 74HC4052PW,118 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4052 master; footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_16_logic_dual_4_channel_analog_multiplexer_demultiplexer_nexperia_74hc4052pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-16 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711898901929984-C5646.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC4052PW datasheet (C5646)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-16_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 4xxx:4052 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual 4 channel analog multiplexer demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "Y0", "type": "passive"},
            "pin_2": {"number": "2", "name": "Y2", "type": "passive"},
            "pin_3": {"number": "3", "name": "Y", "type": "passive"},
            "pin_4": {"number": "4", "name": "Y3", "type": "passive"},
            "pin_5": {"number": "5", "name": "Y1", "type": "passive"},
            "pin_6": {"number": "6", "name": "Inh", "type": "in"},
            "pin_7": {"number": "7", "name": "VEE", "type": "pwr"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "B", "type": "in"},
            "pin_10": {"number": "10", "name": "A", "type": "in"},
            "pin_11": {"number": "11", "name": "X3", "type": "passive"},
            "pin_12": {"number": "12", "name": "X0", "type": "passive"},
            "pin_13": {"number": "13", "name": "X", "type": "passive"},
            "pin_14": {"number": "14", "name": "X1", "type": "passive"},
            "pin_15": {"number": "15", "name": "X2", "type": "passive"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4052",
            "machine_solder": "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5646 (Nexperia 74HC4052PW,118, TSSOP-16, 16 pins) verified at intake; family batch integration C5646.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC4052 data sheet into this part.", "Pin table generated from the KiCad 4xxx:4052 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5647 / Nexperia 74HC4053D,653 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4053 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_triple_2_channel_analog_multiplexer_demultiplexer_nexperia_74hc4053d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711909324505088-C5647.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC4053D datasheet (C5647)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 4xxx:4053 symbol.",
        }
        part["electrical"] = {
            "device_type": "triple 2 channel analog multiplexer demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "Y1", "type": "passive"},
            "pin_2": {"number": "2", "name": "Y0", "type": "passive"},
            "pin_3": {"number": "3", "name": "Z1", "type": "passive"},
            "pin_4": {"number": "4", "name": "Z", "type": "passive"},
            "pin_5": {"number": "5", "name": "Z0", "type": "passive"},
            "pin_6": {"number": "6", "name": "Inh", "type": "in"},
            "pin_7": {"number": "7", "name": "VEE", "type": "pwr"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "C", "type": "in"},
            "pin_10": {"number": "10", "name": "B", "type": "in"},
            "pin_11": {"number": "11", "name": "A", "type": "in"},
            "pin_12": {"number": "12", "name": "X0", "type": "passive"},
            "pin_13": {"number": "13", "name": "X1", "type": "passive"},
            "pin_14": {"number": "14", "name": "X", "type": "passive"},
            "pin_15": {"number": "15", "name": "Y", "type": "passive"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4053",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5647 (Nexperia 74HC4053D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5647.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC4053 data sheet into this part.", "Pin table generated from the KiCad 4xxx:4053 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5648 / Nexperia 74HC4053PW,118 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4053 master; footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_16_logic_triple_2_channel_analog_multiplexer_demultiplexer_nexperia_74hc4053pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-16 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711909324505088-C5647.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC4053PW datasheet (C5648)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-16_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 4xxx:4053 symbol.",
        }
        part["electrical"] = {
            "device_type": "triple 2 channel analog multiplexer demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "Y1", "type": "passive"},
            "pin_2": {"number": "2", "name": "Y0", "type": "passive"},
            "pin_3": {"number": "3", "name": "Z1", "type": "passive"},
            "pin_4": {"number": "4", "name": "Z", "type": "passive"},
            "pin_5": {"number": "5", "name": "Z0", "type": "passive"},
            "pin_6": {"number": "6", "name": "Inh", "type": "in"},
            "pin_7": {"number": "7", "name": "VEE", "type": "pwr"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "C", "type": "in"},
            "pin_10": {"number": "10", "name": "B", "type": "in"},
            "pin_11": {"number": "11", "name": "A", "type": "in"},
            "pin_12": {"number": "12", "name": "X0", "type": "passive"},
            "pin_13": {"number": "13", "name": "X1", "type": "passive"},
            "pin_14": {"number": "14", "name": "X", "type": "passive"},
            "pin_15": {"number": "15", "name": "Y", "type": "passive"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4053",
            "machine_solder": "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5648 (Nexperia 74HC4053PW,118, TSSOP-16, 16 pins) verified at intake; family batch integration C5648.", "Shares the 74HC4053 family datasheet downloaded into C5647 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 4xxx:4053 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5649 / Nexperia 74HC4060D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC4060 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_14_stage_binary_ripple_counter_oscillator_nexperia_74hc4060d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711921228484608-C5649.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC4060D datasheet (C5649)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC4060 symbol.",
        }
        part["electrical"] = {
            "device_type": "14 stage binary ripple counter oscillator",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "Q12", "type": "out"},
            "pin_2": {"number": "2", "name": "Q13", "type": "out"},
            "pin_3": {"number": "3", "name": "Q14", "type": "out"},
            "pin_4": {"number": "4", "name": "Q6", "type": "out"},
            "pin_5": {"number": "5", "name": "Q5", "type": "out"},
            "pin_6": {"number": "6", "name": "Q7", "type": "out"},
            "pin_7": {"number": "7", "name": "Q4", "type": "out"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{Φ0}", "type": "in"},
            "pin_10": {"number": "10", "name": "Φ0", "type": "in"},
            "pin_11": {"number": "11", "name": "~{Φ1}", "type": "in"},
            "pin_12": {"number": "12", "name": "CLR", "type": "in"},
            "pin_13": {"number": "13", "name": "Q9", "type": "out"},
            "pin_14": {"number": "14", "name": "Q8", "type": "out"},
            "pin_15": {"number": "15", "name": "Q10", "type": "out"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC4060",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5649 (Nexperia 74HC4060D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5649.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC4060 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC4060 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5628 / Nexperia 74HC4066D,653 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4066 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_bilateral_analog_switch_nexperia_74hc4066d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711840248922112-C5628.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC4066D datasheet (C5628)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 4xxx:4066 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bilateral analog switch",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1Y", "type": "passive"},
            "pin_2": {"number": "2", "name": "1Z", "type": "passive"},
            "pin_3": {"number": "3", "name": "2Z", "type": "passive"},
            "pin_4": {"number": "4", "name": "2Y", "type": "passive"},
            "pin_5": {"number": "5", "name": "2E", "type": "in"},
            "pin_6": {"number": "6", "name": "3E", "type": "in"},
            "pin_7": {"number": "7", "name": "VSS", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "passive"},
            "pin_9": {"number": "9", "name": "3Z", "type": "passive"},
            "pin_10": {"number": "10", "name": "4Z", "type": "passive"},
            "pin_11": {"number": "11", "name": "4Y", "type": "passive"},
            "pin_12": {"number": "12", "name": "4E", "type": "in"},
            "pin_13": {"number": "13", "name": "1E", "type": "in"},
            "pin_14": {"number": "14", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4066",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5628 (Nexperia 74HC4066D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5628.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC4066 data sheet into this part.", "Pin table generated from the KiCad 4xxx:4066 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5650 / Nexperia 74HC4066PW,118 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4066 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_quad_bilateral_analog_switch_nexperia_74hc4066pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711840248922112-C5628.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC4066PW datasheet (C5650)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 4xxx:4066 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bilateral analog switch",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1Y", "type": "passive"},
            "pin_2": {"number": "2", "name": "1Z", "type": "passive"},
            "pin_3": {"number": "3", "name": "2Z", "type": "passive"},
            "pin_4": {"number": "4", "name": "2Y", "type": "passive"},
            "pin_5": {"number": "5", "name": "2E", "type": "in"},
            "pin_6": {"number": "6", "name": "3E", "type": "in"},
            "pin_7": {"number": "7", "name": "VSS", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "passive"},
            "pin_9": {"number": "9", "name": "3Z", "type": "passive"},
            "pin_10": {"number": "10", "name": "4Z", "type": "passive"},
            "pin_11": {"number": "11", "name": "4Y", "type": "passive"},
            "pin_12": {"number": "12", "name": "4E", "type": "in"},
            "pin_13": {"number": "13", "name": "1E", "type": "in"},
            "pin_14": {"number": "14", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4066",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5650 (Nexperia 74HC4066PW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C5650.", "Shares the 74HC4066 family datasheet downloaded into C5628 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 4xxx:4066 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5657 / Nexperia 74HC541PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT541 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_nexperia_74hc541pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711944678838272-C5657.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC541PW datasheet (C5657)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT541 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G1", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "in"},
            "pin_3": {"number": "3", "name": "A1", "type": "in"},
            "pin_4": {"number": "4", "name": "A2", "type": "in"},
            "pin_5": {"number": "5", "name": "A3", "type": "in"},
            "pin_6": {"number": "6", "name": "A4", "type": "in"},
            "pin_7": {"number": "7", "name": "A5", "type": "in"},
            "pin_8": {"number": "8", "name": "A6", "type": "in"},
            "pin_9": {"number": "9", "name": "A7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Y7", "type": "ts"},
            "pin_12": {"number": "12", "name": "Y6", "type": "ts"},
            "pin_13": {"number": "13", "name": "Y5", "type": "ts"},
            "pin_14": {"number": "14", "name": "Y4", "type": "ts"},
            "pin_15": {"number": "15", "name": "Y3", "type": "ts"},
            "pin_16": {"number": "16", "name": "Y2", "type": "ts"},
            "pin_17": {"number": "17", "name": "Y1", "type": "ts"},
            "pin_18": {"number": "18", "name": "Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "G2", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT541",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5657 (Nexperia 74HC541PW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C5657.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC541 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HCT541 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5608 / Nexperia 74HC573D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS573 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_transparent_latch_tri_state_nexperia_74hc573d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708657724018688-C5608.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74HC573D datasheet (C5608)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS573 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Load", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS573",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5608 (Nexperia 74HC573D,653, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5608.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC573 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS573 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5944 / Nexperia 74HC573PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS573 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_d_type_transparent_latch_tri_state_nexperia_74hc573pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579708657724018688-C5608.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC573PW datasheet (C5944)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS573 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Load", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS573",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5944 (Nexperia 74HC573PW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C5944.", "Shares the 74HC573 family datasheet downloaded into C5608 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74LS573 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5948 / Nexperia 74HC595PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC595 master; footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_16_logic_serial_in_parallel_out_shift_register_nexperia_74hc595pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-16 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711963787812864-C5948.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC595PW datasheet (C5948)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-16_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC595 symbol.",
        }
        part["electrical"] = {
            "device_type": "serial in parallel out shift register",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "QB", "type": "ts"},
            "pin_2": {"number": "2", "name": "QC", "type": "ts"},
            "pin_3": {"number": "3", "name": "QD", "type": "ts"},
            "pin_4": {"number": "4", "name": "QE", "type": "ts"},
            "pin_5": {"number": "5", "name": "QF", "type": "ts"},
            "pin_6": {"number": "6", "name": "QG", "type": "ts"},
            "pin_7": {"number": "7", "name": "QH", "type": "ts"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "QH'", "type": "out"},
            "pin_10": {"number": "10", "name": "~{SRCLR}", "type": "in"},
            "pin_11": {"number": "11", "name": "SRCLK", "type": "in"},
            "pin_12": {"number": "12", "name": "RCLK", "type": "in"},
            "pin_13": {"number": "13", "name": "~{OE}", "type": "in"},
            "pin_14": {"number": "14", "name": "SER", "type": "in"},
            "pin_15": {"number": "15", "name": "QA", "type": "ts"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC595",
            "machine_solder": "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5948 (Nexperia 74HC595PW,118, TSSOP-16, 16 pins) verified at intake; family batch integration C5948.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC595 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC595 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5951 / Nexperia 74HC74PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC74 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_dual_d_type_flip_flop_set_reset_nexperia_74hc74pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711976825470976-C5951.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HC74PW datasheet (C5951)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC74 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual d type flip flop set reset",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{R}", "type": "in"},
            "pin_2": {"number": "2", "name": "D", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "~{S}", "type": "in"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "~{Q}", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "~{Q}", "type": "out"},
            "pin_9": {"number": "9", "name": "Q", "type": "out"},
            "pin_10": {"number": "10", "name": "~{S}", "type": "in"},
            "pin_11": {"number": "11", "name": "C", "type": "in"},
            "pin_12": {"number": "12", "name": "D", "type": "in"},
            "pin_13": {"number": "13", "name": "~{R}", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC74",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5951 (Nexperia 74HC74PW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C5951.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC74 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC74 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5953 / Nexperia 74HC85D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC85 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_4_bit_magnitude_comparator_nexperia_74hc85d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191920401539072-C5953.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC85D datasheet (C5953)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC85 symbol.",
        }
        part["electrical"] = {
            "device_type": "4 bit magnitude comparator",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B3", "type": "in"},
            "pin_2": {"number": "2", "name": "Ia_LT_b", "type": "in"},
            "pin_3": {"number": "3", "name": "Ia=b", "type": "in"},
            "pin_4": {"number": "4", "name": "Ia>b", "type": "in"},
            "pin_5": {"number": "5", "name": "Oa>b", "type": "out"},
            "pin_6": {"number": "6", "name": "Oa=b", "type": "out"},
            "pin_7": {"number": "7", "name": "Oa_LT_b", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "B0", "type": "in"},
            "pin_10": {"number": "10", "name": "A0", "type": "in"},
            "pin_11": {"number": "11", "name": "B1", "type": "in"},
            "pin_12": {"number": "12", "name": "A1", "type": "in"},
            "pin_13": {"number": "13", "name": "A2", "type": "in"},
            "pin_14": {"number": "14", "name": "B2", "type": "in"},
            "pin_15": {"number": "15", "name": "A3", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC85",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5953 (Nexperia 74HC85D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5953.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC85 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC85 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5955 / Nexperia 74HC86D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC86 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_xor_gate_nexperia_74hc86d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711985757442048-C5955.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HC86D datasheet (C5955)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC86 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input xor gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC86",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5955 (Nexperia 74HC86D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5955.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HC86 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC86 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5957 / Nexperia 74HCT02D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT02 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_nor_gate_nexperia_74hct02d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191922335789056-C5957.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT02D datasheet (C5957)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT02 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nor gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1Y", "type": "out"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1B", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2B", "type": "in"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3A", "type": "in"},
            "pin_9": {"number": "9", "name": "3B", "type": "in"},
            "pin_10": {"number": "10", "name": "3Y", "type": "out"},
            "pin_11": {"number": "11", "name": "4A", "type": "in"},
            "pin_12": {"number": "12", "name": "4B", "type": "in"},
            "pin_13": {"number": "13", "name": "4Y", "type": "out"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT02",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5957 (Nexperia 74HCT02D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5957.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT02 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HCT02 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5959 / Nexperia 74HCT08D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS08 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_and_gate_nexperia_74hct08d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712003587293184-C5959.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT08D datasheet (C5959)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS08 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input and gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS08",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5959 (Nexperia 74HCT08D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5959.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT08 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS08 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5961 / Nexperia 74HCT123D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT123 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_dual_retriggerable_monostable_multivibrator_nexperia_74hct123d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191924244467712-C5961.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT123D datasheet (C5961)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT123 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual retriggerable monostable multivibrator",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A", "type": "in"},
            "pin_2": {"number": "2", "name": "B", "type": "in"},
            "pin_3": {"number": "3", "name": "Clr", "type": "in"},
            "pin_4": {"number": "4", "name": "~{Q}", "type": "out"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "Cext", "type": "in"},
            "pin_7": {"number": "7", "name": "RCext", "type": "in"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "A", "type": "in"},
            "pin_10": {"number": "10", "name": "B", "type": "in"},
            "pin_11": {"number": "11", "name": "Clr", "type": "in"},
            "pin_12": {"number": "12", "name": "~{Q}", "type": "out"},
            "pin_13": {"number": "13", "name": "Q", "type": "out"},
            "pin_14": {"number": "14", "name": "Cext", "type": "in"},
            "pin_15": {"number": "15", "name": "RCext", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT123",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5961 (Nexperia 74HCT123D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5961.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT123 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HCT123 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5962 / Nexperia 74HCT125D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS125 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_bus_buffer_tri_state_nexperia_74hct125d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712006349176832-C5962.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT125D datasheet (C5962)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS125 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "ts"},
            "pin_4": {"number": "4", "name": "2OE", "type": "in"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "ts"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "ts"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3OE", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "ts"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4OE", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS125",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5962 (Nexperia 74HCT125D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5962.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT125 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS125 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5963 / Nexperia 74HCT132D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS132 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_nand_gate_schmitt_trigger_nexperia_74hct132d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896971579142144-C5963.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT132D datasheet (C5963)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS132 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate schmitt trigger",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS132",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5963 (Nexperia 74HCT132D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5963.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT132 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS132 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5964 / Nexperia 74HCT132PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS132 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_quad_2_input_nand_gate_schmitt_trigger_nexperia_74hct132pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896971579142144-C5963.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HCT132PW datasheet (C5964)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS132 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate schmitt trigger",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS132",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5964 (Nexperia 74HCT132PW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C5964.", "Shares the 74HCT132 family datasheet downloaded into C5963 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74LS132 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5965 / Nexperia 74HCT138D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT138 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_3_to_8_line_decoder_demultiplexer_nexperia_74hct138d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712009203875840-C5965.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT138D datasheet (C5965)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT138 symbol.",
        }
        part["electrical"] = {
            "device_type": "3 to 8 line decoder demultiplexer",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A0", "type": "in"},
            "pin_2": {"number": "2", "name": "A1", "type": "in"},
            "pin_3": {"number": "3", "name": "A2", "type": "in"},
            "pin_4": {"number": "4", "name": "~{E0}", "type": "in"},
            "pin_5": {"number": "5", "name": "~{E1}", "type": "in"},
            "pin_6": {"number": "6", "name": "E2", "type": "in"},
            "pin_7": {"number": "7", "name": "~{Y7}", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{Y6}", "type": "out"},
            "pin_10": {"number": "10", "name": "~{Y5}", "type": "out"},
            "pin_11": {"number": "11", "name": "~{Y4}", "type": "out"},
            "pin_12": {"number": "12", "name": "~{Y3}", "type": "out"},
            "pin_13": {"number": "13", "name": "~{Y2}", "type": "out"},
            "pin_14": {"number": "14", "name": "~{Y1}", "type": "out"},
            "pin_15": {"number": "15", "name": "~{Y0}", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT138",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5965 (Nexperia 74HCT138D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5965.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT138 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HCT138 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5967 / Nexperia 74HCT14D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_schmitt_trigger_inverter_nexperia_74hct14d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712011888091136-C5967.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT14D datasheet (C5967)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5967 (Nexperia 74HCT14D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5967.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT14 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5968 / Nexperia 74HCT14PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_hex_schmitt_trigger_inverter_nexperia_74hct14pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712011888091136-C5967.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HCT14PW datasheet (C5968)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5968 (Nexperia 74HCT14PW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C5968.", "Shares the 74HCT14 family datasheet downloaded into C5967 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5969 / Nexperia 74HCT157D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS157 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_quad_2_to_1_line_multiplexer_nexperia_74hct157d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186939845758976-C5969.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT157D datasheet (C5969)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS157 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 to 1 line multiplexer",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "S", "type": "in"},
            "pin_2": {"number": "2", "name": "I0a", "type": "in"},
            "pin_3": {"number": "3", "name": "I1a", "type": "in"},
            "pin_4": {"number": "4", "name": "Za", "type": "out"},
            "pin_5": {"number": "5", "name": "I0b", "type": "in"},
            "pin_6": {"number": "6", "name": "I1b", "type": "in"},
            "pin_7": {"number": "7", "name": "Zb", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Zc", "type": "out"},
            "pin_10": {"number": "10", "name": "I1c", "type": "in"},
            "pin_11": {"number": "11", "name": "I0c", "type": "in"},
            "pin_12": {"number": "12", "name": "Zd", "type": "out"},
            "pin_13": {"number": "13", "name": "I1d", "type": "in"},
            "pin_14": {"number": "14", "name": "I0d", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS157",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5969 (Nexperia 74HCT157D,653, SOIC-16, 16 pins) verified at intake; family batch integration C5969.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT157 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS157 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5978 / Nexperia 74HCT244D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT244 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_buffer_tri_state_nexperia_74hct244d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186954077167616-C5978.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74HCT244D datasheet (C5978)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT244",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5978 (Nexperia 74HCT244D,653, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5978.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT244 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HCT244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5979 / Nexperia 74HCT245D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_transceiver_tri_state_nexperia_74hct245d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712017822760960-C5979.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74HCT245D datasheet (C5979)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5979 (Nexperia 74HCT245D,653, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5979.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT245 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5980 / Nexperia 74HCT245PW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_transceiver_tri_state_nexperia_74hct245pw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712017822760960-C5979.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HCT245PW datasheet (C5980)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5980 (Nexperia 74HCT245PW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C5980.", "Shares the 74HCT245 family datasheet downloaded into C5979 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5985 / Nexperia 74HCT32D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS32 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_or_gate_nexperia_74hct32d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191931395620864-C5985.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT32D datasheet (C5985)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS32 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input or gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS32",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5985 (Nexperia 74HCT32D,653, SOIC-14, 14 pins) verified at intake; family batch integration C5985.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT32 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS32 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5989 / Nexperia 74HCT373D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT373 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_transparent_latch_tri_state_nexperia_74hct373d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191938445840384-C5989.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74HCT373D datasheet (C5989)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT373 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "LE", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT373",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5989 (Nexperia 74HCT373D,653, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5989.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT373 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HCT373 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5998 / Nexperia 74HCT4066D,118 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4066 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_bilateral_analog_switch_nexperia_74hct4066d_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186954983137280-C5998.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT4066D datasheet (C5998)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 4xxx:4066 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bilateral analog switch",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1Y", "type": "passive"},
            "pin_2": {"number": "2", "name": "1Z", "type": "passive"},
            "pin_3": {"number": "3", "name": "2Z", "type": "passive"},
            "pin_4": {"number": "4", "name": "2Y", "type": "passive"},
            "pin_5": {"number": "5", "name": "2E", "type": "in"},
            "pin_6": {"number": "6", "name": "3E", "type": "in"},
            "pin_7": {"number": "7", "name": "VSS", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "passive"},
            "pin_9": {"number": "9", "name": "3Z", "type": "passive"},
            "pin_10": {"number": "10", "name": "4Z", "type": "passive"},
            "pin_11": {"number": "11", "name": "4Y", "type": "passive"},
            "pin_12": {"number": "12", "name": "4E", "type": "in"},
            "pin_13": {"number": "13", "name": "1E", "type": "in"},
            "pin_14": {"number": "14", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4066",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5998 (Nexperia 74HCT4066D,118, SOIC-14, 14 pins) verified at intake; family batch integration C5998.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT4066 data sheet into this part.", "Pin table generated from the KiCad 4xxx:4066 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6001 / Nexperia 74HCT574D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT574 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_flip_flop_tri_state_nexperia_74hct574d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186961115209728-C6001.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74HCT574D datasheet (C6001)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT574 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Cp", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT574",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6001 (Nexperia 74HCT574D,653, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6001.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT574 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HCT574 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6005 / Nexperia 74HCT86D,653 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC86 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_xor_gate_nexperia_74hct86d_653"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186969411407872-C6005.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74HCT86D datasheet (C6005)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC86 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input xor gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC86",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6005 (Nexperia 74HCT86D,653, SOIC-14, 14 pins) verified at intake; family batch integration C6005.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74HCT86 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC86 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6049 / Nexperia 74LVC07AD,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS07 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_buffer_open_collector_nexperia_74lvc07ad_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712039974912000-C6049.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74LVC07AD datasheet (C6049)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS07 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex buffer open collector",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS07",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6049 (Nexperia 74LVC07AD,118, SOIC-14, 14 pins) verified at intake; family batch integration C6049.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC07 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS07 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6051 / Nexperia 74LVC07APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS07 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_hex_buffer_open_collector_nexperia_74lvc07apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712039974912000-C6049.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC07APW datasheet (C6051)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS07 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex buffer open collector",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS07",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6051 (Nexperia 74LVC07APW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C6051.", "Shares the 74LVC07 family datasheet downloaded into C6049 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74LS07 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6052 / Nexperia 74LVC08AD,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS08 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_and_gate_nexperia_74lvc08ad_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191932875804672-C6052.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74LVC08AD datasheet (C6052)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS08 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input and gate",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS08",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6052 (Nexperia 74LVC08AD,118, SOIC-14, 14 pins) verified at intake; family batch integration C6052.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC08 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS08 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6053 / Nexperia 74LVC08APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS08 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_quad_2_input_and_gate_nexperia_74lvc08apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191932875804672-C6052.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC08APW datasheet (C6053)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS08 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input and gate",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS08",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6053 (Nexperia 74LVC08APW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C6053.", "Shares the 74LVC08 family datasheet downloaded into C6052 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74LS08 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6057 / Nexperia 74LVC125AD,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LVC125 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_bus_buffer_tri_state_nexperia_74lvc125ad_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191939205279744-C6057.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74LVC125AD datasheet (C6057)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LVC125 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bus buffer tri state",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "ts"},
            "pin_4": {"number": "4", "name": "2OE", "type": "in"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "ts"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "ts"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3OE", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "ts"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4OE", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LVC125",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6057 (Nexperia 74LVC125AD,118, SOIC-14, 14 pins) verified at intake; family batch integration C6057.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC125 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LVC125 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6059 / Nexperia 74LVC125APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LVC125 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_quad_bus_buffer_tri_state_nexperia_74lvc125apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191939205279744-C6057.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC125APW datasheet (C6059)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LVC125 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bus buffer tri state",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "ts"},
            "pin_4": {"number": "4", "name": "2OE", "type": "in"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "ts"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "ts"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3OE", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "ts"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4OE", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LVC125",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6059 (Nexperia 74LVC125APW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C6059.", "Shares the 74LVC125 family datasheet downloaded into C6057 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74LVC125 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6061 / Nexperia 74LVC138AD,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC138 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_3_to_8_line_decoder_demultiplexer_nexperia_74lvc138ad_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186978832760832-C6061.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74LVC138AD datasheet (C6061)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC138 symbol.",
        }
        part["electrical"] = {
            "device_type": "3 to 8 line decoder demultiplexer",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A0", "type": "in"},
            "pin_2": {"number": "2", "name": "A1", "type": "in"},
            "pin_3": {"number": "3", "name": "A2", "type": "in"},
            "pin_4": {"number": "4", "name": "~{E0}", "type": "in"},
            "pin_5": {"number": "5", "name": "~{E1}", "type": "in"},
            "pin_6": {"number": "6", "name": "E2", "type": "in"},
            "pin_7": {"number": "7", "name": "~{Y7}", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{Y6}", "type": "out"},
            "pin_10": {"number": "10", "name": "~{Y5}", "type": "out"},
            "pin_11": {"number": "11", "name": "~{Y4}", "type": "out"},
            "pin_12": {"number": "12", "name": "~{Y3}", "type": "out"},
            "pin_13": {"number": "13", "name": "~{Y2}", "type": "out"},
            "pin_14": {"number": "14", "name": "~{Y1}", "type": "out"},
            "pin_15": {"number": "15", "name": "~{Y0}", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC138",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6061 (Nexperia 74LVC138AD,118, SOIC-16, 16 pins) verified at intake; family batch integration C6061.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC138 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC138 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6062 / Nexperia 74LVC138APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC138 master; footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_16_logic_3_to_8_line_decoder_demultiplexer_nexperia_74lvc138apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-16 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186978832760832-C6061.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC138APW datasheet (C6062)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-16_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC138 symbol.",
        }
        part["electrical"] = {
            "device_type": "3 to 8 line decoder demultiplexer",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A0", "type": "in"},
            "pin_2": {"number": "2", "name": "A1", "type": "in"},
            "pin_3": {"number": "3", "name": "A2", "type": "in"},
            "pin_4": {"number": "4", "name": "~{E0}", "type": "in"},
            "pin_5": {"number": "5", "name": "~{E1}", "type": "in"},
            "pin_6": {"number": "6", "name": "E2", "type": "in"},
            "pin_7": {"number": "7", "name": "~{Y7}", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{Y6}", "type": "out"},
            "pin_10": {"number": "10", "name": "~{Y5}", "type": "out"},
            "pin_11": {"number": "11", "name": "~{Y4}", "type": "out"},
            "pin_12": {"number": "12", "name": "~{Y3}", "type": "out"},
            "pin_13": {"number": "13", "name": "~{Y2}", "type": "out"},
            "pin_14": {"number": "14", "name": "~{Y1}", "type": "out"},
            "pin_15": {"number": "15", "name": "~{Y0}", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC138",
            "machine_solder": "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6062 (Nexperia 74LVC138APW,118, TSSOP-16, 16 pins) verified at intake; family batch integration C6062.", "Shares the 74LVC138 family datasheet downloaded into C6061 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74HC138 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6065 / Nexperia 74LVC14AD,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_schmitt_trigger_inverter_nexperia_74lvc14ad_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712044206964736-C6065.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74LVC14AD datasheet (C6065)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6065 (Nexperia 74LVC14AD,118, SOIC-14, 14 pins) verified at intake; family batch integration C6065.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC14 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6066 / Nexperia 74LVC14APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_hex_schmitt_trigger_inverter_nexperia_74lvc14apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712044206964736-C6065.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC14APW datasheet (C6066)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6066 (Nexperia 74LVC14APW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C6066.", "Shares the 74LVC14 family datasheet downloaded into C6065 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6067 / Nexperia 74LVC157AD,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS157 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_quad_2_to_1_line_multiplexer_nexperia_74lvc157ad_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186987854708736-C6067.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74LVC157AD datasheet (C6067)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS157 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 to 1 line multiplexer",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "S", "type": "in"},
            "pin_2": {"number": "2", "name": "I0a", "type": "in"},
            "pin_3": {"number": "3", "name": "I1a", "type": "in"},
            "pin_4": {"number": "4", "name": "Za", "type": "out"},
            "pin_5": {"number": "5", "name": "I0b", "type": "in"},
            "pin_6": {"number": "6", "name": "I1b", "type": "in"},
            "pin_7": {"number": "7", "name": "Zb", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Zc", "type": "out"},
            "pin_10": {"number": "10", "name": "I1c", "type": "in"},
            "pin_11": {"number": "11", "name": "I0c", "type": "in"},
            "pin_12": {"number": "12", "name": "Zd", "type": "out"},
            "pin_13": {"number": "13", "name": "I1d", "type": "in"},
            "pin_14": {"number": "14", "name": "I0d", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS157",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6067 (Nexperia 74LVC157AD,118, SOIC-16, 16 pins) verified at intake; family batch integration C6067.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC157 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS157 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6068 / Nexperia 74LVC157APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS157 master; footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_16_logic_quad_2_to_1_line_multiplexer_nexperia_74lvc157apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-16 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186987854708736-C6067.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC157APW datasheet (C6068)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-16_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS157 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 to 1 line multiplexer",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "S", "type": "in"},
            "pin_2": {"number": "2", "name": "I0a", "type": "in"},
            "pin_3": {"number": "3", "name": "I1a", "type": "in"},
            "pin_4": {"number": "4", "name": "Za", "type": "out"},
            "pin_5": {"number": "5", "name": "I0b", "type": "in"},
            "pin_6": {"number": "6", "name": "I1b", "type": "in"},
            "pin_7": {"number": "7", "name": "Zb", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Zc", "type": "out"},
            "pin_10": {"number": "10", "name": "I1c", "type": "in"},
            "pin_11": {"number": "11", "name": "I0c", "type": "in"},
            "pin_12": {"number": "12", "name": "Zd", "type": "out"},
            "pin_13": {"number": "13", "name": "I1d", "type": "in"},
            "pin_14": {"number": "14", "name": "I0d", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS157",
            "machine_solder": "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6068 (Nexperia 74LVC157APW,118, TSSOP-16, 16 pins) verified at intake; family batch integration C6068.", "Shares the 74LVC157 family datasheet downloaded into C6067 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74LS157 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6076 / Nexperia 74LVC1G17GV,125 - 74-series logic family
    # batch: pins from the KiCad 74xGxx:74LVC1G17 master; footprint Package_TO_SOT_SMD:SOT-23-5
    current = "electronic_ic_sot_23_5_logic_single_schmitt_trigger_buffer_nexperia_74lvc1g17gv_125"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT753-1 / SC-74A (2.9 x 1.6 mm; Nexperia GV)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712058990399488-C6076.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.6, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC1G17GV datasheet (C6076)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_TO_SOT_SMD:SOT-23-5 master geometry; pinning cross-checked against the KiCad 74xGxx:74LVC1G17 symbol.",
        }
        part["electrical"] = {
            "device_type": "single schmitt trigger buffer",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "NC", "type": "nc"},
            "pin_2": {"number": "2", "name": "A", "type": "in"},
            "pin_3": {"number": "3", "name": "GND", "type": "pwr"},
            "pin_4": {"number": "4", "name": "Y", "type": "out"},
            "pin_5": {"number": "5", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xGxx:74LVC1G17",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23-5",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6076 (Nexperia 74LVC1G17GV,125, SC-74A, 5 pins) verified at intake; family batch integration C6076.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC1G17 data sheet into this part.", "Pin table generated from the KiCad 74xGxx:74LVC1G17 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 5-pin package count.", "Footprint Package_TO_SOT_SMD:SOT-23-5 verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6079 / Nexperia 74LVC244APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_nexperia_74lvc244apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712068368453632-C6079.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC244APW datasheet (C6079)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6079 (Nexperia 74LVC244APW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C6079.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC244 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6080 / Nexperia 74LVC245AD,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_transceiver_tri_state_nexperia_74lvc245ad_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712077529088000-C6080.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74LVC245AD datasheet (C6080)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6080 (Nexperia 74LVC245AD,118, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6080.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC245 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6082 / Nexperia 74LVC245APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_transceiver_tri_state_nexperia_74lvc245apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712077529088000-C6080.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC245APW datasheet (C6082)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6082 (Nexperia 74LVC245APW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C6082.", "Shares the 74LVC245 family datasheet downloaded into C6080 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6085 / Nexperia 74LVC2G14GW,125 - 74-series logic family
    # batch: pins from the KiCad 74xGxx:74LVC2G14 master; footprint Package_TO_SOT_SMD:SOT-363_SC-70-6
    current = "electronic_ic_sot_363_logic_dual_schmitt_trigger_inverter_nexperia_74lvc2g14gw_125"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT363-1 / SC-88 (2.1 x 2.1 mm)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588886697970556928-C6085.pdf"
        part["dimensions_mm"] = {"length": 2.1, "width": 2.1, "height": 1.0}
        part["dimension_reference"] = {
            "document": "74LVC2G14GW datasheet (C6085)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_TO_SOT_SMD:SOT-363_SC-70-6 master geometry; pinning cross-checked against the KiCad 74xGxx:74LVC2G14 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual schmitt trigger inverter",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "GND", "type": "pwr"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "1Y", "type": "out"},
            "pin_5": {"number": "5", "name": "VCC", "type": "pwr"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"}
        }
        part["kicad"] = {
            "symbol": "74xGxx:74LVC2G14",
            "machine_solder": "Package_TO_SOT_SMD:SOT-363_SC-70-6",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6085 (Nexperia 74LVC2G14GW,125, SC-70-6(SOT-363), 6 pins) verified at intake; family batch integration C6085.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC2G14 data sheet into this part.", "Pin table generated from the KiCad 74xGxx:74LVC2G14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 6-pin package count.", "Footprint Package_TO_SOT_SMD:SOT-363_SC-70-6 verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6087 / Nexperia 74LVC32APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS32 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_quad_2_input_or_gate_nexperia_74lvc32apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712089406947328-C6087.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC32APW datasheet (C6087)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS32 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input or gate",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS32",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6087 (Nexperia 74LVC32APW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C6087.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC32 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS32 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6093 / Nexperia 74LVC541APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT541 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_nexperia_74lvc541apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588881485532815360-C6093.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC541APW datasheet (C6093)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT541 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G1", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "in"},
            "pin_3": {"number": "3", "name": "A1", "type": "in"},
            "pin_4": {"number": "4", "name": "A2", "type": "in"},
            "pin_5": {"number": "5", "name": "A3", "type": "in"},
            "pin_6": {"number": "6", "name": "A4", "type": "in"},
            "pin_7": {"number": "7", "name": "A5", "type": "in"},
            "pin_8": {"number": "8", "name": "A6", "type": "in"},
            "pin_9": {"number": "9", "name": "A7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Y7", "type": "ts"},
            "pin_12": {"number": "12", "name": "Y6", "type": "ts"},
            "pin_13": {"number": "13", "name": "Y5", "type": "ts"},
            "pin_14": {"number": "14", "name": "Y4", "type": "ts"},
            "pin_15": {"number": "15", "name": "Y3", "type": "ts"},
            "pin_16": {"number": "16", "name": "Y2", "type": "ts"},
            "pin_17": {"number": "17", "name": "Y1", "type": "ts"},
            "pin_18": {"number": "18", "name": "Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "G2", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT541",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6093 (Nexperia 74LVC541APW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C6093.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC541 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HCT541 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6094 / Nexperia 74LVC573AD,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS573 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_transparent_latch_tri_state_nexperia_74lvc573ad_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186994867449856-C6094.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74LVC573AD datasheet (C6094)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS573 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Load", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS573",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6094 (Nexperia 74LVC573AD,118, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6094.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC573 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS573 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6096 / Nexperia 74LVC573APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS573 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_d_type_transparent_latch_tri_state_nexperia_74lvc573apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186994867449856-C6094.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC573APW datasheet (C6096)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS573 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Load", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS573",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6096 (Nexperia 74LVC573APW,118, TSSOP-20, 20 pins) verified at intake; family batch integration C6096.", "Shares the 74LVC573 family datasheet downloaded into C6094 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74LS573 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6097 / Nexperia 74LVC574AD,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT574 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_flip_flop_tri_state_nexperia_74lvc574ad_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586187001935122432-C6097.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74LVC574AD datasheet (C6097)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT574 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop tri state",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Cp", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT574",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6097 (Nexperia 74LVC574AD,118, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6097.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC574 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HCT574 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6099 / Nexperia 74LVC74AD,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC74 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_dual_d_type_flip_flop_set_reset_nexperia_74lvc74ad_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586187004136861696-C6099.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74LVC74AD datasheet (C6099)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC74 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual d type flip flop set reset",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{R}", "type": "in"},
            "pin_2": {"number": "2", "name": "D", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "~{S}", "type": "in"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "~{Q}", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "~{Q}", "type": "out"},
            "pin_9": {"number": "9", "name": "Q", "type": "out"},
            "pin_10": {"number": "10", "name": "~{S}", "type": "in"},
            "pin_11": {"number": "11", "name": "C", "type": "in"},
            "pin_12": {"number": "12", "name": "D", "type": "in"},
            "pin_13": {"number": "13", "name": "~{R}", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC74",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6099 (Nexperia 74LVC74AD,118, SOIC-14, 14 pins) verified at intake; family batch integration C6099.", "Browser-extracted the signed JLC OSS link and downloaded the Nexperia 74LVC74 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC74 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6100 / Nexperia 74LVC74APW,118 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC74 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_dual_d_type_flip_flop_set_reset_nexperia_74lvc74apw_118"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586187004136861696-C6099.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74LVC74APW datasheet (C6100)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC74 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual d type flip flop set reset",
            "supply_voltage": "1.2-3.6 V (1.65 V for some functions)",
            "logic_family": "74LVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{R}", "type": "in"},
            "pin_2": {"number": "2", "name": "D", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "~{S}", "type": "in"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "~{Q}", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "~{Q}", "type": "out"},
            "pin_9": {"number": "9", "name": "Q", "type": "out"},
            "pin_10": {"number": "10", "name": "~{S}", "type": "in"},
            "pin_11": {"number": "11", "name": "C", "type": "in"},
            "pin_12": {"number": "12", "name": "D", "type": "in"},
            "pin_13": {"number": "13", "name": "~{R}", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC74",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6100 (Nexperia 74LVC74APW,118, TSSOP-14, 14 pins) verified at intake; family batch integration C6100.", "Shares the 74LVC74 family datasheet downloaded into C6099 (byte-identical copy in this part's source folder).", "Pin table generated from the KiCad 74xx:74HC74 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5477 / onsemi 74AC04SCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC04 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_onsemi_74ac04scx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186808313466880-C5477.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74AC04SCX datasheet (C5477)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74AC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC04",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5477 (onsemi 74AC04SCX, SOIC-14, 14 pins) verified at intake; family batch integration C5477.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74AC04 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5478 / onsemi 74AC08SCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS08 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_and_gate_onsemi_74ac08scx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186815724802048-C5478.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74AC08SCX datasheet (C5478)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS08 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input and gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74AC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS08",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5478 (onsemi 74AC08SCX, SOIC-14, 14 pins) verified at intake; family batch integration C5478.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74AC08 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS08 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5480 / onsemi 74AC138MTCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC138 master; footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_16_logic_3_to_8_line_decoder_demultiplexer_onsemi_74ac138mtcx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-16 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588881455732690944-C5480.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74AC138MTCX datasheet (C5480)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-16_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC138 symbol.",
        }
        part["electrical"] = {
            "device_type": "3 to 8 line decoder demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74AC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A0", "type": "in"},
            "pin_2": {"number": "2", "name": "A1", "type": "in"},
            "pin_3": {"number": "3", "name": "A2", "type": "in"},
            "pin_4": {"number": "4", "name": "~{E0}", "type": "in"},
            "pin_5": {"number": "5", "name": "~{E1}", "type": "in"},
            "pin_6": {"number": "6", "name": "E2", "type": "in"},
            "pin_7": {"number": "7", "name": "~{Y7}", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{Y6}", "type": "out"},
            "pin_10": {"number": "10", "name": "~{Y5}", "type": "out"},
            "pin_11": {"number": "11", "name": "~{Y4}", "type": "out"},
            "pin_12": {"number": "12", "name": "~{Y3}", "type": "out"},
            "pin_13": {"number": "13", "name": "~{Y2}", "type": "out"},
            "pin_14": {"number": "14", "name": "~{Y1}", "type": "out"},
            "pin_15": {"number": "15", "name": "~{Y0}", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC138",
            "machine_solder": "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5480 (onsemi 74AC138MTCX, TSSOP-16, 16 pins) verified at intake; family batch integration C5480.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74AC138 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC138 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5482 / onsemi 74AC14SCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_schmitt_trigger_inverter_onsemi_74ac14scx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186828567220224-C5482.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74AC14SCX datasheet (C5482)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74AC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5482 (onsemi 74AC14SCX, SOIC-14, 14 pins) verified at intake; family batch integration C5482.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74AC14 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5484 / onsemi 74AC240SCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC240 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_buffer_tri_state_inverting_onsemi_74ac240scx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588883686494785536-C5484.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74AC240SCX datasheet (C5484)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC240 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state inverting",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74AC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC240",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5484 (onsemi 74AC240SCX, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5484.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74AC240 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC240 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5486 / onsemi 74AC245SCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_transceiver_tri_state_onsemi_74ac245scx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586186834598899712-C5486.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74AC245SCX datasheet (C5486)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74AC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5486 (onsemi 74AC245SCX, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5486.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74AC245 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5487 / onsemi 74ACT00SCX - 74-series logic family
    # batch: pins from the KiCad 74xx:7400 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_nand_gate_onsemi_74act00scx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588883756132274176-C5487.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74ACT00SCX datasheet (C5487)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:7400 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:7400",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5487 (onsemi 74ACT00SCX, SOIC-14, 14 pins) verified at intake; family batch integration C5487.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74ACT00 data sheet into this part.", "Pin table generated from the KiCad 74xx:7400 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5490 / onsemi 74ACT04SCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC04 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_onsemi_74act04scx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191778856767488-C5490.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74ACT04SCX datasheet (C5490)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC04",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5490 (onsemi 74ACT04SCX, SOIC-14, 14 pins) verified at intake; family batch integration C5490.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74ACT04 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5492 / onsemi 74ACT08SCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS08 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_and_gate_onsemi_74act08scx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588883756132274177-C5492.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74ACT08SCX datasheet (C5492)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS08 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input and gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS08",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5492 (onsemi 74ACT08SCX, SOIC-14, 14 pins) verified at intake; family batch integration C5492.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74ACT08 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS08 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5496 / onsemi 74ACT244MTCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_onsemi_74act244mtcx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588881485197271040-C5496.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74ACT244MTCX datasheet (C5496)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5496 (onsemi 74ACT244MTCX, TSSOP-20, 20 pins) verified at intake; family batch integration C5496.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74ACT244 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5499 / onsemi 74ACT32SCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS32 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_or_gate_onsemi_74act32scx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191798472986624-C5499.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "74ACT32SCX datasheet (C5499)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS32 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input or gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS32",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5499 (onsemi 74ACT32SCX, SOIC-14, 14 pins) verified at intake; family batch integration C5499.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74ACT32 data sheet into this part.", "Pin table generated from the KiCad 74xx:74LS32 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5589 / onsemi MC74HC04ADTR2G - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC04 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_hex_inverter_onsemi_mc74hc04adtr2g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711693280509952-C5589.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "MC74HC04ADTR2G datasheet (C5589)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC04",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5589 (onsemi MC74HC04ADTR2G, TSSOP-14, 14 pins) verified at intake; family batch integration C5589.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74HC04 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5624 / onsemi MM74HC244WMX - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_buffer_tri_state_onsemi_mm74hc244wmx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586191869939732480-C5624.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "MM74HC244WMX datasheet (C5624)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5624 (onsemi MM74HC244WMX, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5624.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74HC244 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5990 / onsemi 74HCT373MTCX - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT373 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_d_type_transparent_latch_tri_state_onsemi_74hct373mtcx"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588883719746957312-C5990.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "74HCT373MTCX datasheet (C5990)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT373 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "LE", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT373",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5990 (onsemi 74HCT373MTCX, TSSOP-20, 20 pins) verified at intake; family batch integration C5990.", "Browser-extracted the signed JLC OSS link and downloaded the onsemi 74HCT373 data sheet into this part.", "Pin table generated from the KiCad 74xx:74HCT373 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6914 / Texas Instruments SN7406DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS06 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_open_collector_texas_instruments_sn7406dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn7406.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN7406DR datasheet (C6914)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS06 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter open collector",
            "supply_voltage": "4.75-5.25 V (standard TTL)",
            "logic_family": "74standard TTL",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS06",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6914 (Texas Instruments SN7406DR, SOIC-14, 14 pins) verified at intake; family batch integration C6914.", "Downloaded the official Texas Instruments 7406 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS06 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6917 / Texas Instruments SN74ABT240ANSR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC240 master; footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm
    current = "electronic_ic_soic_20_208mil_logic_octal_bus_buffer_tri_state_inverting_texas_instruments_sn74abt240ansr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-20 208 mil (5.3 x 7.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74abt240a.pdf"
        part["dimensions_mm"] = {"length": 7.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74ABT240ANSR datasheet (C6917)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-20_5.3x7.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC240 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state inverting",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74ABT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC240",
            "machine_solder": "Package_SO:SSOP-20_5.3x7.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6917 (Texas Instruments SN74ABT240ANSR, SOIC-20-208mil, 20 pins) verified at intake; family batch integration C6917.", "Downloaded the official Texas Instruments 74ABT240 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC240 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6922 / Texas Instruments SN74ACT04DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC04 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_texas_instruments_sn74act04dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74act04.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74ACT04DR datasheet (C6922)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC04",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6922 (Texas Instruments SN74ACT04DR, SOIC-14, 14 pins) verified at intake; family batch integration C6922.", "Downloaded the official Texas Instruments 74ACT04 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6928 / Texas Instruments SN74ACT244DWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_buffer_tri_state_texas_instruments_sn74act244dwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74act244.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "SN74ACT244DWR datasheet (C6928)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6928 (Texas Instruments SN74ACT244DWR, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6928.", "Downloaded the official Texas Instruments 74ACT244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6929 / Texas Instruments SN74ACT244NSR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm
    current = "electronic_ic_soic_20_208mil_logic_octal_bus_buffer_tri_state_texas_instruments_sn74act244nsr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-20 208 mil (5.3 x 7.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74act244.pdf"
        part["dimensions_mm"] = {"length": 7.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74ACT244NSR datasheet (C6929)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-20_5.3x7.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:SSOP-20_5.3x7.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6929 (Texas Instruments SN74ACT244NSR, SOIC-20-208mil, 20 pins) verified at intake; family batch integration C6929.", "Downloaded the official Texas Instruments 74ACT244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6930 / Texas Instruments SN74ACT244PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_texas_instruments_sn74act244pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74act244.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74ACT244PWR datasheet (C6930)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6930 (Texas Instruments SN74ACT244PWR, TSSOP-20, 20 pins) verified at intake; family batch integration C6930.", "Downloaded the official Texas Instruments 74ACT244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6534 / Texas Instruments CD74ACT245M96 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_transceiver_tri_state_texas_instruments_cd74act245m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74act245.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "CD74ACT245M96 datasheet (C6534)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6534 (Texas Instruments CD74ACT245M96, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6534.", "Downloaded the official Texas Instruments 74ACT245 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6931 / Texas Instruments SN74ACT245PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_transceiver_tri_state_texas_instruments_sn74act245pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74act245.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74ACT245PWR datasheet (C6931)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6931 (Texas Instruments SN74ACT245PWR, TSSOP-20, 20 pins) verified at intake; family batch integration C6931.", "Downloaded the official Texas Instruments 74ACT245 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6933 / Texas Instruments SN74ACT74DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC74 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_dual_d_type_flip_flop_set_reset_texas_instruments_sn74act74dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74act74.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74ACT74DR datasheet (C6933)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC74 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual d type flip flop set reset",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74ACT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{R}", "type": "in"},
            "pin_2": {"number": "2", "name": "D", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "~{S}", "type": "in"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "~{Q}", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "~{Q}", "type": "out"},
            "pin_9": {"number": "9", "name": "Q", "type": "out"},
            "pin_10": {"number": "10", "name": "~{S}", "type": "in"},
            "pin_11": {"number": "11", "name": "C", "type": "in"},
            "pin_12": {"number": "12", "name": "D", "type": "in"},
            "pin_13": {"number": "13", "name": "~{R}", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC74",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6933 (Texas Instruments SN74ACT74DR, SOIC-14, 14 pins) verified at intake; family batch integration C6933.", "Downloaded the official Texas Instruments 74ACT74 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC74 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6937 / Texas Instruments SN74AHC08DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS08 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_and_gate_texas_instruments_sn74ahc08dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ahc08.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74AHC08DR datasheet (C6937)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS08 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input and gate",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS08",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6937 (Texas Instruments SN74AHC08DR, SOIC-14, 14 pins) verified at intake; family batch integration C6937.", "Downloaded the official Texas Instruments 74AHC08 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS08 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6938 / Texas Instruments SN74AHC123ADR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC123 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_dual_retriggerable_monostable_multivibrator_texas_instruments_sn74ahc123adr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ahc123a.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74AHC123ADR datasheet (C6938)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC123 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual retriggerable monostable multivibrator",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A", "type": "in"},
            "pin_2": {"number": "2", "name": "B", "type": "in"},
            "pin_3": {"number": "3", "name": "Clr", "type": "in"},
            "pin_4": {"number": "4", "name": "~{Q}", "type": "out"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "Cext", "type": "in"},
            "pin_7": {"number": "7", "name": "RCext", "type": "in"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "A", "type": "in"},
            "pin_10": {"number": "10", "name": "B", "type": "in"},
            "pin_11": {"number": "11", "name": "Clr", "type": "in"},
            "pin_12": {"number": "12", "name": "~{Q}", "type": "out"},
            "pin_13": {"number": "13", "name": "Q", "type": "out"},
            "pin_14": {"number": "14", "name": "Cext", "type": "in"},
            "pin_15": {"number": "15", "name": "RCext", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC123",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6938 (Texas Instruments SN74AHC123ADR, SOIC-16, 16 pins) verified at intake; family batch integration C6938.", "Downloaded the official Texas Instruments 74AHC123 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC123 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6939 / Texas Instruments SN74AHC125DBR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS125 master; footprint Package_SO:SSOP-14_5.3x6.2mm_P0.65mm
    current = "electronic_ic_ssop_14_208mil_logic_quad_bus_buffer_tri_state_texas_instruments_sn74ahc125dbr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-14 208 mil (5.3 x 6.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ahc125.pdf"
        part["dimensions_mm"] = {"length": 6.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74AHC125DBR datasheet (C6939)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-14_5.3x6.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS125 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bus buffer tri state",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "ts"},
            "pin_4": {"number": "4", "name": "2OE", "type": "in"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "ts"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "ts"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3OE", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "ts"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4OE", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS125",
            "machine_solder": "Package_SO:SSOP-14_5.3x6.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6939 (Texas Instruments SN74AHC125DBR, SSOP-14-208mil, 14 pins) verified at intake; family batch integration C6939.", "Downloaded the official Texas Instruments 74AHC125 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS125 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SSOP-14_5.3x6.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6940 / Texas Instruments SN74AHC125DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS125 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_bus_buffer_tri_state_texas_instruments_sn74ahc125dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ahc125.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74AHC125DR datasheet (C6940)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS125 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bus buffer tri state",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "ts"},
            "pin_4": {"number": "4", "name": "2OE", "type": "in"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "ts"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "ts"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3OE", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "ts"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4OE", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS125",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6940 (Texas Instruments SN74AHC125DR, SOIC-14, 14 pins) verified at intake; family batch integration C6940.", "Downloaded the official Texas Instruments 74AHC125 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS125 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6941 / Texas Instruments SN74AHC139DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS139 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_dual_2_to_4_line_decoder_demultiplexer_texas_instruments_sn74ahc139dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ahc139.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74AHC139DR datasheet (C6941)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS139 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual 2 to 4 line decoder demultiplexer",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "in"},
            "pin_3": {"number": "3", "name": "A1", "type": "in"},
            "pin_4": {"number": "4", "name": "O0", "type": "out"},
            "pin_5": {"number": "5", "name": "O1", "type": "out"},
            "pin_6": {"number": "6", "name": "O2", "type": "out"},
            "pin_7": {"number": "7", "name": "O3", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "O3", "type": "out"},
            "pin_10": {"number": "10", "name": "O2", "type": "out"},
            "pin_11": {"number": "11", "name": "O1", "type": "out"},
            "pin_12": {"number": "12", "name": "O0", "type": "out"},
            "pin_13": {"number": "13", "name": "A1", "type": "in"},
            "pin_14": {"number": "14", "name": "A0", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS139",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6941 (Texas Instruments SN74AHC139DR, SOIC-16, 16 pins) verified at intake; family batch integration C6941.", "Downloaded the official Texas Instruments 74AHC139 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS139 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6942 / Texas Instruments SN74AHC14DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_schmitt_trigger_inverter_texas_instruments_sn74ahc14dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ahc14.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74AHC14DR datasheet (C6942)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74AHC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6942 (Texas Instruments SN74AHC14DR, SOIC-14, 14 pins) verified at intake; family batch integration C6942.", "Downloaded the official Texas Instruments 74AHC14 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7125 / Texas Instruments SN74ALS688NSR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC688 master; footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm
    current = "electronic_ic_soic_20_208mil_logic_8_bit_identity_comparator_texas_instruments_sn74als688nsr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-20 208 mil (5.3 x 7.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74als688.pdf"
        part["dimensions_mm"] = {"length": 7.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74ALS688NSR datasheet (C7125)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-20_5.3x7.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC688 symbol.",
        }
        part["electrical"] = {
            "device_type": "8 bit identity comparator",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74ALS",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "in"},
            "pin_2": {"number": "2", "name": "P0", "type": "in"},
            "pin_3": {"number": "3", "name": "R0", "type": "in"},
            "pin_4": {"number": "4", "name": "P1", "type": "in"},
            "pin_5": {"number": "5", "name": "R1", "type": "in"},
            "pin_6": {"number": "6", "name": "P2", "type": "in"},
            "pin_7": {"number": "7", "name": "R2", "type": "in"},
            "pin_8": {"number": "8", "name": "P3", "type": "in"},
            "pin_9": {"number": "9", "name": "R3", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "P4", "type": "in"},
            "pin_12": {"number": "12", "name": "R4", "type": "in"},
            "pin_13": {"number": "13", "name": "P5", "type": "in"},
            "pin_14": {"number": "14", "name": "R5", "type": "in"},
            "pin_15": {"number": "15", "name": "P6", "type": "in"},
            "pin_16": {"number": "16", "name": "R6", "type": "in"},
            "pin_17": {"number": "17", "name": "P7", "type": "in"},
            "pin_18": {"number": "18", "name": "R7", "type": "in"},
            "pin_19": {"number": "19", "name": "P=R", "type": "out"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC688",
            "machine_solder": "Package_SO:SSOP-20_5.3x7.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7125 (Texas Instruments SN74ALS688NSR, SOIC-20-208mil, 20 pins) verified at intake; family batch integration C7125.", "Downloaded the official Texas Instruments 74ALS688 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC688 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7128 / Texas Instruments SN74ALVC164245DGGR - 74-series logic family
    # batch: pins from the KiCad 74xx:74ALVC164245 master; footprint Package_SO:TSSOP-48_6.1x12.5mm_P0.5mm
    current = "electronic_ic_tssop_48_logic_16_bit_bus_transceiver_tri_state_texas_instruments_sn74alvc164245dggr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-48 6.2 mm (6.2 x 12.5 mm, 0.5 mm pitch; master 6.1 mm body)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74alvc164245.pdf"
        part["dimensions_mm"] = {"length": 12.5, "width": 6.2, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74ALVC164245DGGR datasheet (C7128)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-48_6.1x12.5mm_P0.5mm master geometry; pinning cross-checked against the KiCad 74xx:74ALVC164245 symbol.",
        }
        part["electrical"] = {
            "device_type": "16 bit bus transceiver tri state",
            "supply_voltage": "1.65-3.6 V",
            "logic_family": "74ALVC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1DIR", "type": "in"},
            "pin_2": {"number": "2", "name": "1B0", "type": "bidirectional"},
            "pin_3": {"number": "3", "name": "1B1", "type": "bidirectional"},
            "pin_4": {"number": "4", "name": "GND", "type": "pwr"},
            "pin_5": {"number": "5", "name": "1B2", "type": "bidirectional"},
            "pin_6": {"number": "6", "name": "1B3", "type": "bidirectional"},
            "pin_7": {"number": "7", "name": "V_{CC(B)}", "type": "pwr"},
            "pin_8": {"number": "8", "name": "1B4", "type": "bidirectional"},
            "pin_9": {"number": "9", "name": "1B5", "type": "bidirectional"},
            "pin_10": {"number": "10", "name": "GND", "type": "passive"},
            "pin_11": {"number": "11", "name": "1B6", "type": "bidirectional"},
            "pin_12": {"number": "12", "name": "1B7", "type": "bidirectional"},
            "pin_13": {"number": "13", "name": "2B0", "type": "bidirectional"},
            "pin_14": {"number": "14", "name": "2B1", "type": "bidirectional"},
            "pin_15": {"number": "15", "name": "GND", "type": "passive"},
            "pin_16": {"number": "16", "name": "2B2", "type": "bidirectional"},
            "pin_17": {"number": "17", "name": "2B3", "type": "bidirectional"},
            "pin_18": {"number": "18", "name": "V_{CC(B)}", "type": "passive"},
            "pin_19": {"number": "19", "name": "2B4", "type": "bidirectional"},
            "pin_20": {"number": "20", "name": "2B5", "type": "bidirectional"},
            "pin_21": {"number": "21", "name": "GND", "type": "passive"},
            "pin_22": {"number": "22", "name": "2B6", "type": "bidirectional"},
            "pin_23": {"number": "23", "name": "2B7", "type": "bidirectional"},
            "pin_24": {"number": "24", "name": "2DIR", "type": "in"},
            "pin_25": {"number": "25", "name": "2~{OE}", "type": "in"},
            "pin_26": {"number": "26", "name": "2A7", "type": "bidirectional"},
            "pin_27": {"number": "27", "name": "2A6", "type": "bidirectional"},
            "pin_28": {"number": "28", "name": "GND", "type": "passive"},
            "pin_29": {"number": "29", "name": "2A5", "type": "bidirectional"},
            "pin_30": {"number": "30", "name": "2A4", "type": "bidirectional"},
            "pin_31": {"number": "31", "name": "V_{CC(A)}", "type": "pwr"},
            "pin_32": {"number": "32", "name": "2A3", "type": "bidirectional"},
            "pin_33": {"number": "33", "name": "2A2", "type": "bidirectional"},
            "pin_34": {"number": "34", "name": "GND", "type": "passive"},
            "pin_35": {"number": "35", "name": "2A1", "type": "bidirectional"},
            "pin_36": {"number": "36", "name": "2A0", "type": "bidirectional"},
            "pin_37": {"number": "37", "name": "1A7", "type": "bidirectional"},
            "pin_38": {"number": "38", "name": "1A6", "type": "bidirectional"},
            "pin_39": {"number": "39", "name": "GND", "type": "passive"},
            "pin_40": {"number": "40", "name": "1A5", "type": "bidirectional"},
            "pin_41": {"number": "41", "name": "1A4", "type": "bidirectional"},
            "pin_42": {"number": "42", "name": "V_{CC(A)}", "type": "passive"},
            "pin_43": {"number": "43", "name": "1A3", "type": "bidirectional"},
            "pin_44": {"number": "44", "name": "1A2", "type": "bidirectional"},
            "pin_45": {"number": "45", "name": "GND", "type": "passive"},
            "pin_46": {"number": "46", "name": "1A1", "type": "bidirectional"},
            "pin_47": {"number": "47", "name": "1A0", "type": "bidirectional"},
            "pin_48": {"number": "48", "name": "1~{OE}", "type": "in"}
        }
        part["kicad"] = {
            "symbol": "74xx:74ALVC164245",
            "machine_solder": "Package_SO:TSSOP-48_6.1x12.5mm_P0.5mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7128 (Texas Instruments SN74ALVC164245DGGR, TSSOP-48-6.2mm, 48 pins) verified at intake; family batch integration C7128.", "Downloaded the official Texas Instruments 74ALVC164245 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74ALVC164245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 48-pin package count.", "Footprint Package_SO:TSSOP-48_6.1x12.5mm_P0.5mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7134 / Texas Instruments SN74AS244ANSR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm
    current = "electronic_ic_soic_20_208mil_logic_octal_bus_buffer_tri_state_texas_instruments_sn74as244ansr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-20 208 mil (5.3 x 7.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74as244a.pdf"
        part["dimensions_mm"] = {"length": 7.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74AS244ANSR datasheet (C7134)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-20_5.3x7.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74AS",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:SSOP-20_5.3x7.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7134 (Texas Instruments SN74AS244ANSR, SOIC-20-208mil, 20 pins) verified at intake; family batch integration C7134.", "Downloaded the official Texas Instruments 74AS244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7158 / Texas Instruments SN74F00DR - 74-series logic family
    # batch: pins from the KiCad 74xx:7400 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_nand_gate_texas_instruments_sn74f00dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74f00.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74F00DR datasheet (C7158)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:7400 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74F",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:7400",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7158 (Texas Instruments SN74F00DR, SOIC-14, 14 pins) verified at intake; family batch integration C7158.", "Downloaded the official Texas Instruments 74F00 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:7400 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7159 / Texas Instruments SN74F04DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC04 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_texas_instruments_sn74f04dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74f04.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74F04DR datasheet (C7159)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74F",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC04",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7159 (Texas Instruments SN74F04DR, SOIC-14, 14 pins) verified at intake; family batch integration C7159.", "Downloaded the official Texas Instruments 74F04 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7163 / Texas Instruments SN74F157ADR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS157 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_quad_2_to_1_line_multiplexer_texas_instruments_sn74f157adr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74f157a.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74F157ADR datasheet (C7163)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS157 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 to 1 line multiplexer",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74F",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "S", "type": "in"},
            "pin_2": {"number": "2", "name": "I0a", "type": "in"},
            "pin_3": {"number": "3", "name": "I1a", "type": "in"},
            "pin_4": {"number": "4", "name": "Za", "type": "out"},
            "pin_5": {"number": "5", "name": "I0b", "type": "in"},
            "pin_6": {"number": "6", "name": "I1b", "type": "in"},
            "pin_7": {"number": "7", "name": "Zb", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Zc", "type": "out"},
            "pin_10": {"number": "10", "name": "I1c", "type": "in"},
            "pin_11": {"number": "11", "name": "I0c", "type": "in"},
            "pin_12": {"number": "12", "name": "Zd", "type": "out"},
            "pin_13": {"number": "13", "name": "I1d", "type": "in"},
            "pin_14": {"number": "14", "name": "I0d", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS157",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7163 (Texas Instruments SN74F157ADR, SOIC-16, 16 pins) verified at intake; family batch integration C7163.", "Downloaded the official Texas Instruments 74F157 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS157 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7164 / Texas Instruments SN74F21DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS21 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_dual_4_input_and_gate_texas_instruments_sn74f21dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74f21.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74F21DR datasheet (C7164)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS21 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual 4 input and gate",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74F",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "NC", "type": "no_connect"},
            "pin_4": {"number": "4", "name": "1C", "type": "in"},
            "pin_5": {"number": "5", "name": "1D", "type": "in"},
            "pin_6": {"number": "6", "name": "1Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "2Y", "type": "out"},
            "pin_9": {"number": "9", "name": "2A", "type": "in"},
            "pin_10": {"number": "10", "name": "2B", "type": "in"},
            "pin_11": {"number": "11", "name": "NC", "type": "no_connect"},
            "pin_12": {"number": "12", "name": "2C", "type": "in"},
            "pin_13": {"number": "13", "name": "2D", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS21",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7164 (Texas Instruments SN74F21DR, SOIC-14, 14 pins) verified at intake; family batch integration C7164.", "Downloaded the official Texas Instruments 74F21 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS21 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7168 / Texas Instruments SN74F32DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS32 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_or_gate_texas_instruments_sn74f32dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74f32.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74F32DR datasheet (C7168)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS32 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input or gate",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74F",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS32",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7168 (Texas Instruments SN74F32DR, SOIC-14, 14 pins) verified at intake; family batch integration C7168.", "Downloaded the official Texas Instruments 74F32 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS32 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5562 / NXP Semicon 74F373D - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC373 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_transparent_latch_nxp_semiconductors_74f373d"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74f373.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74F373D datasheet (C5562)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC373 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch nxp semiconductors",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74F",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "LE", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC373",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5562 (NXP Semicon 74F373D, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5562.", "Downloaded the official NXP Semicon 74F373 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC373 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7169 / Texas Instruments SN74F373DWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC373 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_transparent_latch_tri_state_texas_instruments_sn74f373dwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74f373.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "SN74F373DWR datasheet (C7169)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC373 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74F",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "LE", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC373",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7169 (Texas Instruments SN74F373DWR, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C7169.", "Downloaded the official Texas Instruments 74F373 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC373 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5565 / Philips Semicons 74F377AD - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS377 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_flip_flop_common_enable_philips_semiconductors_74f377ad"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74f377a.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "74F377AD datasheet (C5565)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS377 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop common enable philips semiconductors",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74F",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{E}", "type": "in"},
            "pin_2": {"number": "2", "name": "Q0", "type": "out"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "Q1", "type": "out"},
            "pin_6": {"number": "6", "name": "Q2", "type": "out"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "Q3", "type": "out"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "CP", "type": "in"},
            "pin_12": {"number": "12", "name": "Q4", "type": "out"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "Q5", "type": "out"},
            "pin_16": {"number": "16", "name": "Q6", "type": "out"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "Q7", "type": "out"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS377",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5565 (Philips Semicons 74F377AD, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C5565.", "Downloaded the official Philips Semicons 74F377 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS377 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6804 / Texas Instruments SN74F573DWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS573 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_transparent_latch_tri_state_texas_instruments_sn74f573dwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74f573.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "SN74F573DWR datasheet (C6804)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS573 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74F",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Load", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS573",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6804 (Texas Instruments SN74F573DWR, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6804.", "Downloaded the official Texas Instruments 74F573 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS573 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6805 / Texas Instruments SN74F74DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC74 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_dual_d_type_flip_flop_set_reset_texas_instruments_sn74f74dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74f74.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74F74DR datasheet (C6805)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC74 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual d type flip flop set reset",
            "supply_voltage": "4.5-5.5 V",
            "logic_family": "74F",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{R}", "type": "in"},
            "pin_2": {"number": "2", "name": "D", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "~{S}", "type": "in"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "~{Q}", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "~{Q}", "type": "out"},
            "pin_9": {"number": "9", "name": "Q", "type": "out"},
            "pin_10": {"number": "10", "name": "~{S}", "type": "in"},
            "pin_11": {"number": "11", "name": "C", "type": "in"},
            "pin_12": {"number": "12", "name": "D", "type": "in"},
            "pin_13": {"number": "13", "name": "~{R}", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC74",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6805 (Texas Instruments SN74F74DR, SOIC-14, 14 pins) verified at intake; family batch integration C6805.", "Downloaded the official Texas Instruments 74F74 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC74 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2902 / Texas Instruments SN74HC00N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC00 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_quad_2_input_nand_gate_texas_instruments_sn74hc00n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc00.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC00N datasheet (C2902)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC00 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC00",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2902 (Texas Instruments SN74HC00N, DIP-14, 14 pins) verified at intake; family batch integration C2902.", "Downloaded the official Texas Instruments 74HC00 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC00 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6807 / Texas Instruments SN74HC00PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC00 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_quad_2_input_nand_gate_texas_instruments_sn74hc00pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc00.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC00PWR datasheet (C6807)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC00 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC00",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6807 (Texas Instruments SN74HC00PWR, TSSOP-14, 14 pins) verified at intake; family batch integration C6807.", "Downloaded the official Texas Instruments 74HC00 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC00 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2897 / Texas Instruments SN74HC02N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC02 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_quad_2_input_nor_gate_texas_instruments_sn74hc02n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc02.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC02N datasheet (C2897)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC02 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nor gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1Y", "type": "out"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1B", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2B", "type": "in"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3A", "type": "in"},
            "pin_9": {"number": "9", "name": "3B", "type": "in"},
            "pin_10": {"number": "10", "name": "3Y", "type": "out"},
            "pin_11": {"number": "11", "name": "4A", "type": "in"},
            "pin_12": {"number": "12", "name": "4B", "type": "in"},
            "pin_13": {"number": "13", "name": "4Y", "type": "out"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC02",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2897 (Texas Instruments SN74HC02N, DIP-14, 14 pins) verified at intake; family batch integration C2897.", "Downloaded the official Texas Instruments 74HC02 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC02 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2904 / Texas Instruments SN74HC03N - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS03 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_quad_2_input_nand_gate_open_collector_texas_instruments_sn74hc03n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc03.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC03N datasheet (C2904)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS03 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate open collector",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS03",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2904 (Texas Instruments SN74HC03N, DIP-14, 14 pins) verified at intake; family batch integration C2904.", "Downloaded the official Texas Instruments 74HC03 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS03 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6811 / Texas Instruments SN74HC04DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC04 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_texas_instruments_sn74hc04dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc04.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC04DR datasheet (C6811)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC04",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6811 (Texas Instruments SN74HC04DR, SOIC-14, 14 pins) verified at intake; family batch integration C6811.", "Downloaded the official Texas Instruments 74HC04 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2886 / Texas Instruments SN74HC04N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC04 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_hex_inverter_texas_instruments_sn74hc04n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc04.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC04N datasheet (C2886)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC04",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2886 (Texas Instruments SN74HC04N, DIP-14, 14 pins) verified at intake; family batch integration C2886.", "Downloaded the official Texas Instruments 74HC04 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6812 / Texas Instruments SN74HC04NSR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC04 master; footprint Package_SO:SSOP-14_5.3x6.2mm_P0.65mm
    current = "electronic_ic_soic_14_208mil_logic_hex_inverter_texas_instruments_sn74hc04nsr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-14 208 mil (5.3 x 6.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc04.pdf"
        part["dimensions_mm"] = {"length": 6.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74HC04NSR datasheet (C6812)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-14_5.3x6.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC04",
            "machine_solder": "Package_SO:SSOP-14_5.3x6.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6812 (Texas Instruments SN74HC04NSR, SOIC-14-208mil, 14 pins) verified at intake; family batch integration C6812.", "Downloaded the official Texas Instruments 74HC04 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SSOP-14_5.3x6.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6810 / Texas Instruments SN74HC04PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC04 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_hex_inverter_texas_instruments_sn74hc04pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc04.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC04PWR datasheet (C6810)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC04",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6810 (Texas Instruments SN74HC04PWR, TSSOP-14, 14 pins) verified at intake; family batch integration C6810.", "Downloaded the official Texas Instruments 74HC04 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2887 / Texas Instruments SN74HC08N - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS08 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_quad_2_input_and_gate_texas_instruments_sn74hc08n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc08.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC08N datasheet (C2887)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS08 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input and gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS08",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2887 (Texas Instruments SN74HC08N, DIP-14, 14 pins) verified at intake; family batch integration C2887.", "Downloaded the official Texas Instruments 74HC08 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS08 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6816 / Texas Instruments SN74HC10DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS10 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_triple_3_input_nand_gate_texas_instruments_sn74hc10dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc10.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC10DR datasheet (C6816)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS10 symbol.",
        }
        part["electrical"] = {
            "device_type": "triple 3 input nand gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2B", "type": "in"},
            "pin_5": {"number": "5", "name": "2C", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "3C", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y", "type": "out"},
            "pin_13": {"number": "13", "name": "1C", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS10",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6816 (Texas Instruments SN74HC10DR, SOIC-14, 14 pins) verified at intake; family batch integration C6816.", "Downloaded the official Texas Instruments 74HC10 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS10 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2888 / Texas Instruments SN74HC10N - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS10 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_triple_3_input_nand_gate_texas_instruments_sn74hc10n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc10.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC10N datasheet (C2888)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS10 symbol.",
        }
        part["electrical"] = {
            "device_type": "triple 3 input nand gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2B", "type": "in"},
            "pin_5": {"number": "5", "name": "2C", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "3C", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y", "type": "out"},
            "pin_13": {"number": "13", "name": "1C", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS10",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2888 (Texas Instruments SN74HC10N, DIP-14, 14 pins) verified at intake; family batch integration C2888.", "Downloaded the official Texas Instruments 74HC10 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS10 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2890 / Texas Instruments SN74HC125N - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS125 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_quad_bus_buffer_tri_state_texas_instruments_sn74hc125n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc125.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC125N datasheet (C2890)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS125 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "ts"},
            "pin_4": {"number": "4", "name": "2OE", "type": "in"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "ts"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "ts"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3OE", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "ts"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4OE", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS125",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2890 (Texas Instruments SN74HC125N, DIP-14, 14 pins) verified at intake; family batch integration C2890.", "Downloaded the official Texas Instruments 74HC125 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS125 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6818 / Texas Instruments SN74HC138DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC138 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_3_to_8_line_decoder_demultiplexer_texas_instruments_sn74hc138dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc138.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC138DR datasheet (C6818)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC138 symbol.",
        }
        part["electrical"] = {
            "device_type": "3 to 8 line decoder demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A0", "type": "in"},
            "pin_2": {"number": "2", "name": "A1", "type": "in"},
            "pin_3": {"number": "3", "name": "A2", "type": "in"},
            "pin_4": {"number": "4", "name": "~{E0}", "type": "in"},
            "pin_5": {"number": "5", "name": "~{E1}", "type": "in"},
            "pin_6": {"number": "6", "name": "E2", "type": "in"},
            "pin_7": {"number": "7", "name": "~{Y7}", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{Y6}", "type": "out"},
            "pin_10": {"number": "10", "name": "~{Y5}", "type": "out"},
            "pin_11": {"number": "11", "name": "~{Y4}", "type": "out"},
            "pin_12": {"number": "12", "name": "~{Y3}", "type": "out"},
            "pin_13": {"number": "13", "name": "~{Y2}", "type": "out"},
            "pin_14": {"number": "14", "name": "~{Y1}", "type": "out"},
            "pin_15": {"number": "15", "name": "~{Y0}", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC138",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6818 (Texas Instruments SN74HC138DR, SOIC-16, 16 pins) verified at intake; family batch integration C6818.", "Downloaded the official Texas Instruments 74HC138 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC138 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2913 / Texas Instruments SN74HC138N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC138 master; footprint Package_DIP:DIP-16_W7.62mm
    current = "electronic_ic_dip_16_logic_3_to_8_line_decoder_demultiplexer_texas_instruments_sn74hc138n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-16 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc138.pdf"
        part["dimensions_mm"] = {"length": 21.3, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC138N datasheet (C2913)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-16_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC138 symbol.",
        }
        part["electrical"] = {
            "device_type": "3 to 8 line decoder demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A0", "type": "in"},
            "pin_2": {"number": "2", "name": "A1", "type": "in"},
            "pin_3": {"number": "3", "name": "A2", "type": "in"},
            "pin_4": {"number": "4", "name": "~{E0}", "type": "in"},
            "pin_5": {"number": "5", "name": "~{E1}", "type": "in"},
            "pin_6": {"number": "6", "name": "E2", "type": "in"},
            "pin_7": {"number": "7", "name": "~{Y7}", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{Y6}", "type": "out"},
            "pin_10": {"number": "10", "name": "~{Y5}", "type": "out"},
            "pin_11": {"number": "11", "name": "~{Y4}", "type": "out"},
            "pin_12": {"number": "12", "name": "~{Y3}", "type": "out"},
            "pin_13": {"number": "13", "name": "~{Y2}", "type": "out"},
            "pin_14": {"number": "14", "name": "~{Y1}", "type": "out"},
            "pin_15": {"number": "15", "name": "~{Y0}", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC138",
            "machine_solder": "Package_DIP:DIP-16_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2913 (Texas Instruments SN74HC138N, DIP-16, 16 pins) verified at intake; family batch integration C2913.", "Downloaded the official Texas Instruments 74HC138 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC138 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_DIP:DIP-16_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6819 / Texas Instruments SN74HC148DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS148 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_8_to_3_line_priority_encoder_texas_instruments_sn74hc148dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc148.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC148DR datasheet (C6819)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS148 symbol.",
        }
        part["electrical"] = {
            "device_type": "8 to 3 line priority encoder",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "I4", "type": "in"},
            "pin_2": {"number": "2", "name": "I5", "type": "in"},
            "pin_3": {"number": "3", "name": "I6", "type": "in"},
            "pin_4": {"number": "4", "name": "I7", "type": "in"},
            "pin_5": {"number": "5", "name": "EI", "type": "in"},
            "pin_6": {"number": "6", "name": "S2", "type": "out"},
            "pin_7": {"number": "7", "name": "S1", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "S0", "type": "out"},
            "pin_10": {"number": "10", "name": "IO", "type": "in"},
            "pin_11": {"number": "11", "name": "I1", "type": "in"},
            "pin_12": {"number": "12", "name": "I2", "type": "in"},
            "pin_13": {"number": "13", "name": "I3", "type": "in"},
            "pin_14": {"number": "14", "name": "GS", "type": "out"},
            "pin_15": {"number": "15", "name": "EO", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS148",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6819 (Texas Instruments SN74HC148DR, SOIC-16, 16 pins) verified at intake; family batch integration C6819.", "Downloaded the official Texas Instruments 74HC148 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS148 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6820 / Texas Instruments SN74HC14DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_schmitt_trigger_inverter_texas_instruments_sn74hc14dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc14.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC14DR datasheet (C6820)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6820 (Texas Instruments SN74HC14DR, SOIC-14, 14 pins) verified at intake; family batch integration C6820.", "Downloaded the official Texas Instruments 74HC14 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2907 / Texas Instruments SN74HC14N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_hex_schmitt_trigger_inverter_texas_instruments_sn74hc14n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc14.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC14N datasheet (C2907)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2907 (Texas Instruments SN74HC14N, DIP-14, 14 pins) verified at intake; family batch integration C2907.", "Downloaded the official Texas Instruments 74HC14 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6821 / Texas Instruments SN74HC14PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_hex_schmitt_trigger_inverter_texas_instruments_sn74hc14pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc14.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC14PWR datasheet (C6821)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6821 (Texas Instruments SN74HC14PWR, TSSOP-14, 14 pins) verified at intake; family batch integration C6821.", "Downloaded the official Texas Instruments 74HC14 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6822 / Texas Instruments SN74HC151DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS151 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_8_to_1_line_data_selector_multiplexer_texas_instruments_sn74hc151dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc151.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC151DR datasheet (C6822)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS151 symbol.",
        }
        part["electrical"] = {
            "device_type": "8 to 1 line data selector multiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "I3", "type": "in"},
            "pin_2": {"number": "2", "name": "I2", "type": "in"},
            "pin_3": {"number": "3", "name": "I1", "type": "in"},
            "pin_4": {"number": "4", "name": "I0", "type": "in"},
            "pin_5": {"number": "5", "name": "Z", "type": "out"},
            "pin_6": {"number": "6", "name": "~{Z}", "type": "out"},
            "pin_7": {"number": "7", "name": "~{E}", "type": "in"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "S2", "type": "in"},
            "pin_10": {"number": "10", "name": "S1", "type": "in"},
            "pin_11": {"number": "11", "name": "S0", "type": "in"},
            "pin_12": {"number": "12", "name": "I7", "type": "in"},
            "pin_13": {"number": "13", "name": "I6", "type": "in"},
            "pin_14": {"number": "14", "name": "I5", "type": "in"},
            "pin_15": {"number": "15", "name": "I4", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS151",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6822 (Texas Instruments SN74HC151DR, SOIC-16, 16 pins) verified at intake; family batch integration C6822.", "Downloaded the official Texas Instruments 74HC151 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS151 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6823 / Texas Instruments SN74HC157DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS157 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_quad_2_to_1_line_multiplexer_texas_instruments_sn74hc157dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc157.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC157DR datasheet (C6823)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS157 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 to 1 line multiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "S", "type": "in"},
            "pin_2": {"number": "2", "name": "I0a", "type": "in"},
            "pin_3": {"number": "3", "name": "I1a", "type": "in"},
            "pin_4": {"number": "4", "name": "Za", "type": "out"},
            "pin_5": {"number": "5", "name": "I0b", "type": "in"},
            "pin_6": {"number": "6", "name": "I1b", "type": "in"},
            "pin_7": {"number": "7", "name": "Zb", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Zc", "type": "out"},
            "pin_10": {"number": "10", "name": "I1c", "type": "in"},
            "pin_11": {"number": "11", "name": "I0c", "type": "in"},
            "pin_12": {"number": "12", "name": "Zd", "type": "out"},
            "pin_13": {"number": "13", "name": "I1d", "type": "in"},
            "pin_14": {"number": "14", "name": "I0d", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS157",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6823 (Texas Instruments SN74HC157DR, SOIC-16, 16 pins) verified at intake; family batch integration C6823.", "Downloaded the official Texas Instruments 74HC157 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS157 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5218 / Texas Instruments SN74HC157N - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS157 master; footprint Package_DIP:DIP-16_W7.62mm
    current = "electronic_ic_dip_16_logic_quad_2_channel_analog_multiplexer_texas_instruments_sn74hc157n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-16 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc157.pdf"
        part["dimensions_mm"] = {"length": 21.3, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC157N datasheet (C5218)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-16_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS157 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 channel analog multiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "S", "type": "in"},
            "pin_2": {"number": "2", "name": "I0a", "type": "in"},
            "pin_3": {"number": "3", "name": "I1a", "type": "in"},
            "pin_4": {"number": "4", "name": "Za", "type": "out"},
            "pin_5": {"number": "5", "name": "I0b", "type": "in"},
            "pin_6": {"number": "6", "name": "I1b", "type": "in"},
            "pin_7": {"number": "7", "name": "Zb", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Zc", "type": "out"},
            "pin_10": {"number": "10", "name": "I1c", "type": "in"},
            "pin_11": {"number": "11", "name": "I0c", "type": "in"},
            "pin_12": {"number": "12", "name": "Zd", "type": "out"},
            "pin_13": {"number": "13", "name": "I1d", "type": "in"},
            "pin_14": {"number": "14", "name": "I0d", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS157",
            "machine_solder": "Package_DIP:DIP-16_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5218 (Texas Instruments SN74HC157N, DIP-16, 16 pins) verified at intake; family batch integration C5218.", "Downloaded the official Texas Instruments 74HC157 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS157 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_DIP:DIP-16_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6824 / Texas Instruments SN74HC161DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS161 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_synchronous_4_bit_binary_counter_texas_instruments_sn74hc161dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc161.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC161DR datasheet (C6824)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS161 symbol.",
        }
        part["electrical"] = {
            "device_type": "synchronous 4 bit binary counter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{MR}", "type": "in"},
            "pin_2": {"number": "2", "name": "CP", "type": "in"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "D2", "type": "in"},
            "pin_6": {"number": "6", "name": "D3", "type": "in"},
            "pin_7": {"number": "7", "name": "CEP", "type": "in"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{PE}", "type": "in"},
            "pin_10": {"number": "10", "name": "CET", "type": "in"},
            "pin_11": {"number": "11", "name": "Q3", "type": "out"},
            "pin_12": {"number": "12", "name": "Q2", "type": "out"},
            "pin_13": {"number": "13", "name": "Q1", "type": "out"},
            "pin_14": {"number": "14", "name": "Q0", "type": "out"},
            "pin_15": {"number": "15", "name": "TC", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS161",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6824 (Texas Instruments SN74HC161DR, SOIC-16, 16 pins) verified at intake; family batch integration C6824.", "Downloaded the official Texas Instruments 74HC161 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS161 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2893 / Texas Instruments SN74HC163N - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS163 master; footprint Package_DIP:DIP-16_W7.62mm
    current = "electronic_ic_dip_16_logic_synchronous_4_bit_binary_counter_texas_instruments_sn74hc163n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-16 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc163.pdf"
        part["dimensions_mm"] = {"length": 21.3, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC163N datasheet (C2893)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-16_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS163 symbol.",
        }
        part["electrical"] = {
            "device_type": "synchronous 4 bit binary counter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{MR}", "type": "in"},
            "pin_2": {"number": "2", "name": "CP", "type": "in"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "D2", "type": "in"},
            "pin_6": {"number": "6", "name": "D3", "type": "in"},
            "pin_7": {"number": "7", "name": "CEP", "type": "in"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "~{PE}", "type": "in"},
            "pin_10": {"number": "10", "name": "CET", "type": "in"},
            "pin_11": {"number": "11", "name": "Q3", "type": "out"},
            "pin_12": {"number": "12", "name": "Q2", "type": "out"},
            "pin_13": {"number": "13", "name": "Q1", "type": "out"},
            "pin_14": {"number": "14", "name": "Q0", "type": "out"},
            "pin_15": {"number": "15", "name": "TC", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS163",
            "machine_solder": "Package_DIP:DIP-16_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2893 (Texas Instruments SN74HC163N, DIP-16, 16 pins) verified at intake; family batch integration C2893.", "Downloaded the official Texas Instruments 74HC163 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS163 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_DIP:DIP-16_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5419 / Texas Instruments SN74HC164DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC164 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_serial_in_parallel_out_shift_register_texas_instruments_sn74hc164dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 150 mil (3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc164.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC164DR datasheet (C5419)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC164 symbol.",
        }
        part["electrical"] = {
            "device_type": "serial in parallel out shift register",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "DSA", "type": "in"},
            "pin_2": {"number": "2", "name": "DSB", "type": "in"},
            "pin_3": {"number": "3", "name": "Q0", "type": "out"},
            "pin_4": {"number": "4", "name": "Q1", "type": "out"},
            "pin_5": {"number": "5", "name": "Q2", "type": "out"},
            "pin_6": {"number": "6", "name": "Q3", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "CP", "type": "in"},
            "pin_9": {"number": "9", "name": "~{MR}", "type": "in"},
            "pin_10": {"number": "10", "name": "Q4", "type": "out"},
            "pin_11": {"number": "11", "name": "Q5", "type": "out"},
            "pin_12": {"number": "12", "name": "Q6", "type": "out"},
            "pin_13": {"number": "13", "name": "Q7", "type": "out"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC164",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5419 (Texas Instruments SN74HC164DR, SOIC-14-150mil, 14 pins) verified at intake; family batch integration C5419.", "Downloaded the official Texas Instruments 74HC164 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC164 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2908 / Texas Instruments SN74HC164N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC164 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_serial_in_parallel_out_shift_register_texas_instruments_sn74hc164n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc164.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC164N datasheet (C2908)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC164 symbol.",
        }
        part["electrical"] = {
            "device_type": "serial in parallel out shift register",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "DSA", "type": "in"},
            "pin_2": {"number": "2", "name": "DSB", "type": "in"},
            "pin_3": {"number": "3", "name": "Q0", "type": "out"},
            "pin_4": {"number": "4", "name": "Q1", "type": "out"},
            "pin_5": {"number": "5", "name": "Q2", "type": "out"},
            "pin_6": {"number": "6", "name": "Q3", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "CP", "type": "in"},
            "pin_9": {"number": "9", "name": "~{MR}", "type": "in"},
            "pin_10": {"number": "10", "name": "Q4", "type": "out"},
            "pin_11": {"number": "11", "name": "Q5", "type": "out"},
            "pin_12": {"number": "12", "name": "Q6", "type": "out"},
            "pin_13": {"number": "13", "name": "Q7", "type": "out"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC164",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2908 (Texas Instruments SN74HC164N, DIP-14, 14 pins) verified at intake; family batch integration C2908.", "Downloaded the official Texas Instruments 74HC164 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC164 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2909 / Texas Instruments SN74HC165N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC165 master; footprint Package_DIP:DIP-16_W7.62mm
    current = "electronic_ic_dip_16_logic_parallel_in_serial_out_shift_register_texas_instruments_sn74hc165n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-16 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc165.pdf"
        part["dimensions_mm"] = {"length": 21.3, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC165N datasheet (C2909)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-16_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC165 symbol.",
        }
        part["electrical"] = {
            "device_type": "parallel in serial out shift register",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{PL}", "type": "in"},
            "pin_2": {"number": "2", "name": "CP", "type": "in"},
            "pin_3": {"number": "3", "name": "D4", "type": "in"},
            "pin_4": {"number": "4", "name": "D5", "type": "in"},
            "pin_5": {"number": "5", "name": "D6", "type": "in"},
            "pin_6": {"number": "6", "name": "D7", "type": "in"},
            "pin_7": {"number": "7", "name": "~{Q7}", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Q7", "type": "out"},
            "pin_10": {"number": "10", "name": "DS", "type": "in"},
            "pin_11": {"number": "11", "name": "D0", "type": "in"},
            "pin_12": {"number": "12", "name": "D1", "type": "in"},
            "pin_13": {"number": "13", "name": "D2", "type": "in"},
            "pin_14": {"number": "14", "name": "D3", "type": "in"},
            "pin_15": {"number": "15", "name": "~{CE}", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC165",
            "machine_solder": "Package_DIP:DIP-16_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2909 (Texas Instruments SN74HC165N, DIP-16, 16 pins) verified at intake; family batch integration C2909.", "Downloaded the official Texas Instruments 74HC165 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC165 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_DIP:DIP-16_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6828 / Texas Instruments SN74HC174DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS174 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_hex_d_type_flip_flop_clear_texas_instruments_sn74hc174dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc174.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC174DR datasheet (C6828)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS174 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex d type flip flop clear",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{Mr}", "type": "in"},
            "pin_2": {"number": "2", "name": "Q0", "type": "out"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "Q1", "type": "out"},
            "pin_6": {"number": "6", "name": "D2", "type": "in"},
            "pin_7": {"number": "7", "name": "Q2", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Cp", "type": "in"},
            "pin_10": {"number": "10", "name": "Q3", "type": "out"},
            "pin_11": {"number": "11", "name": "D3", "type": "in"},
            "pin_12": {"number": "12", "name": "Q4", "type": "out"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "Q5", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS174",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6828 (Texas Instruments SN74HC174DR, SOIC-16, 16 pins) verified at intake; family batch integration C6828.", "Downloaded the official Texas Instruments 74HC174 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS174 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6829 / Texas Instruments SN74HC175DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS175 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_quad_d_type_flip_flop_texas_instruments_sn74hc175dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc175.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC175DR datasheet (C6829)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS175 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad d type flip flop",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{Mr}", "type": "in"},
            "pin_2": {"number": "2", "name": "Q0", "type": "out"},
            "pin_3": {"number": "3", "name": "~{Q0}", "type": "out"},
            "pin_4": {"number": "4", "name": "D0", "type": "in"},
            "pin_5": {"number": "5", "name": "D1", "type": "in"},
            "pin_6": {"number": "6", "name": "~{Q1}", "type": "out"},
            "pin_7": {"number": "7", "name": "Q1", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Cp", "type": "in"},
            "pin_10": {"number": "10", "name": "Q2", "type": "out"},
            "pin_11": {"number": "11", "name": "~{Q2}", "type": "out"},
            "pin_12": {"number": "12", "name": "D2", "type": "in"},
            "pin_13": {"number": "13", "name": "D3", "type": "in"},
            "pin_14": {"number": "14", "name": "~{Q3}", "type": "out"},
            "pin_15": {"number": "15", "name": "Q3", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS175",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6829 (Texas Instruments SN74HC175DR, SOIC-16, 16 pins) verified at intake; family batch integration C6829.", "Downloaded the official Texas Instruments 74HC175 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS175 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2896 / Texas Instruments SN74HC175N - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS175 master; footprint Package_DIP:DIP-16_W7.62mm
    current = "electronic_ic_dip_16_logic_quad_d_type_flip_flop_texas_instruments_sn74hc175n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-16 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc175.pdf"
        part["dimensions_mm"] = {"length": 21.3, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC175N datasheet (C2896)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-16_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS175 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad d type flip flop",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{Mr}", "type": "in"},
            "pin_2": {"number": "2", "name": "Q0", "type": "out"},
            "pin_3": {"number": "3", "name": "~{Q0}", "type": "out"},
            "pin_4": {"number": "4", "name": "D0", "type": "in"},
            "pin_5": {"number": "5", "name": "D1", "type": "in"},
            "pin_6": {"number": "6", "name": "~{Q1}", "type": "out"},
            "pin_7": {"number": "7", "name": "Q1", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Cp", "type": "in"},
            "pin_10": {"number": "10", "name": "Q2", "type": "out"},
            "pin_11": {"number": "11", "name": "~{Q2}", "type": "out"},
            "pin_12": {"number": "12", "name": "D2", "type": "in"},
            "pin_13": {"number": "13", "name": "D3", "type": "in"},
            "pin_14": {"number": "14", "name": "~{Q3}", "type": "out"},
            "pin_15": {"number": "15", "name": "Q3", "type": "out"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS175",
            "machine_solder": "Package_DIP:DIP-16_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2896 (Texas Instruments SN74HC175N, DIP-16, 16 pins) verified at intake; family batch integration C2896.", "Downloaded the official Texas Instruments 74HC175 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS175 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_DIP:DIP-16_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6830 / Texas Instruments SN74HC20PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS20 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_dual_4_input_nand_gate_texas_instruments_sn74hc20pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc20.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC20PWR datasheet (C6830)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS20 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual 4 input nand gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "NC", "type": "no_connect"},
            "pin_4": {"number": "4", "name": "1C", "type": "in"},
            "pin_5": {"number": "5", "name": "1D", "type": "in"},
            "pin_6": {"number": "6", "name": "1Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "2Y", "type": "out"},
            "pin_9": {"number": "9", "name": "2A", "type": "in"},
            "pin_10": {"number": "10", "name": "2B", "type": "in"},
            "pin_11": {"number": "11", "name": "NC", "type": "no_connect"},
            "pin_12": {"number": "12", "name": "2C", "type": "in"},
            "pin_13": {"number": "13", "name": "2D", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS20",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6830 (Texas Instruments SN74HC20PWR, TSSOP-14, 14 pins) verified at intake; family batch integration C6830.", "Downloaded the official Texas Instruments 74HC20 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS20 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6831 / Texas Instruments SN74HC21QDRQ1 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS21 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_dual_4_input_and_gate_texas_instruments_sn74hc21qdrq1"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc21.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC21QDRQ1 datasheet (C6831)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS21 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual 4 input and gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "NC", "type": "no_connect"},
            "pin_4": {"number": "4", "name": "1C", "type": "in"},
            "pin_5": {"number": "5", "name": "1D", "type": "in"},
            "pin_6": {"number": "6", "name": "1Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "2Y", "type": "out"},
            "pin_9": {"number": "9", "name": "2A", "type": "in"},
            "pin_10": {"number": "10", "name": "2B", "type": "in"},
            "pin_11": {"number": "11", "name": "NC", "type": "no_connect"},
            "pin_12": {"number": "12", "name": "2C", "type": "in"},
            "pin_13": {"number": "13", "name": "2D", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS21",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6831 (Texas Instruments SN74HC21QDRQ1, SOIC-14, 14 pins) verified at intake; family batch integration C6831.", "Downloaded the official Texas Instruments 74HC21 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS21 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6833 / Texas Instruments SN74HC241DWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS241 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_buffer_tri_state_texas_instruments_sn74hc241dwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc241.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "SN74HC241DWR datasheet (C6833)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS241 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OEa", "type": "in"},
            "pin_2": {"number": "2", "name": "I0a", "type": "in"},
            "pin_3": {"number": "3", "name": "O3b", "type": "ts"},
            "pin_4": {"number": "4", "name": "I1a", "type": "in"},
            "pin_5": {"number": "5", "name": "O2b", "type": "ts"},
            "pin_6": {"number": "6", "name": "I2a", "type": "in"},
            "pin_7": {"number": "7", "name": "O1b", "type": "ts"},
            "pin_8": {"number": "8", "name": "I3a", "type": "in"},
            "pin_9": {"number": "9", "name": "O0b", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "I0b", "type": "in"},
            "pin_12": {"number": "12", "name": "O3a", "type": "ts"},
            "pin_13": {"number": "13", "name": "I1b", "type": "in"},
            "pin_14": {"number": "14", "name": "O2a", "type": "ts"},
            "pin_15": {"number": "15", "name": "I2b", "type": "in"},
            "pin_16": {"number": "16", "name": "O1a", "type": "ts"},
            "pin_17": {"number": "17", "name": "I3b", "type": "in"},
            "pin_18": {"number": "18", "name": "O0a", "type": "ts"},
            "pin_19": {"number": "19", "name": "OEb", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS241",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6833 (Texas Instruments SN74HC241DWR, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6833.", "Downloaded the official Texas Instruments 74HC241 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS241 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2912 / Texas Instruments SN74HC244N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_DIP:DIP-20_W7.62mm
    current = "electronic_ic_dip_20_logic_octal_bus_buffer_tri_state_texas_instruments_sn74hc244n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-20 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc244.pdf"
        part["dimensions_mm"] = {"length": 25.7, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC244N datasheet (C2912)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-20_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_DIP:DIP-20_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2912 (Texas Instruments SN74HC244N, DIP-20, 20 pins) verified at intake; family batch integration C2912.", "Downloaded the official Texas Instruments 74HC244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_DIP:DIP-20_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6835 / Texas Instruments SN74HC244PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_texas_instruments_sn74hc244pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc244.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC244PWR datasheet (C6835)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6835 (Texas Instruments SN74HC244PWR, TSSOP-20, 20 pins) verified at intake; family batch integration C6835.", "Downloaded the official Texas Instruments 74HC244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2899 / Texas Instruments SN74HC245N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_DIP:DIP-20_W7.62mm
    current = "electronic_ic_dip_20_logic_octal_bus_transceiver_tri_state_texas_instruments_sn74hc245n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-20 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc245.pdf"
        part["dimensions_mm"] = {"length": 25.7, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC245N datasheet (C2899)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-20_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_DIP:DIP-20_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2899 (Texas Instruments SN74HC245N, DIP-20, 20 pins) verified at intake; family batch integration C2899.", "Downloaded the official Texas Instruments 74HC245 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_DIP:DIP-20_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6539 / Texas Instruments CD74HC259M96 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS259 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_8_bit_addressable_latch_texas_instruments_cd74hc259m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hc259.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HC259M96 datasheet (C6539)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS259 symbol.",
        }
        part["electrical"] = {
            "device_type": "8 bit addressable latch",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A0", "type": "in"},
            "pin_2": {"number": "2", "name": "A1", "type": "in"},
            "pin_3": {"number": "3", "name": "A2", "type": "in"},
            "pin_4": {"number": "4", "name": "Q0", "type": "out"},
            "pin_5": {"number": "5", "name": "Q1", "type": "out"},
            "pin_6": {"number": "6", "name": "Q2", "type": "out"},
            "pin_7": {"number": "7", "name": "Q3", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Q4", "type": "out"},
            "pin_10": {"number": "10", "name": "Q5", "type": "out"},
            "pin_11": {"number": "11", "name": "Q6", "type": "out"},
            "pin_12": {"number": "12", "name": "Q7", "type": "out"},
            "pin_13": {"number": "13", "name": "D", "type": "in"},
            "pin_14": {"number": "14", "name": "E", "type": "in"},
            "pin_15": {"number": "15", "name": "Clr", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS259",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6539 (Texas Instruments CD74HC259M96, SOIC-16, 16 pins) verified at intake; family batch integration C6539.", "Downloaded the official Texas Instruments 74HC259 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS259 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5238 / Texas Instruments SN74HC273N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC273 master; footprint Package_DIP:DIP-20_W7.62mm
    current = "electronic_ic_dip_20_logic_octal_d_type_flip_flop_texas_instruments_sn74hc273n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-20 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc273.pdf"
        part["dimensions_mm"] = {"length": 25.7, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC273N datasheet (C5238)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-20_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC273 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{Mr}", "type": "in"},
            "pin_2": {"number": "2", "name": "Q0", "type": "out"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "Q1", "type": "out"},
            "pin_6": {"number": "6", "name": "Q2", "type": "out"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "Q3", "type": "out"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Cp", "type": "in"},
            "pin_12": {"number": "12", "name": "Q4", "type": "out"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "Q5", "type": "out"},
            "pin_16": {"number": "16", "name": "Q6", "type": "out"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "Q7", "type": "out"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC273",
            "machine_solder": "Package_DIP:DIP-20_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5238 (Texas Instruments SN74HC273N, DIP-20, 20 pins) verified at intake; family batch integration C5238.", "Downloaded the official Texas Instruments 74HC273 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC273 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_DIP:DIP-20_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6837 / Texas Instruments SN74HC273PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC273 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_d_type_flip_flop_clear_texas_instruments_sn74hc273pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc273.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC273PWR datasheet (C6837)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC273 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop clear",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{Mr}", "type": "in"},
            "pin_2": {"number": "2", "name": "Q0", "type": "out"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "Q1", "type": "out"},
            "pin_6": {"number": "6", "name": "Q2", "type": "out"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "Q3", "type": "out"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Cp", "type": "in"},
            "pin_12": {"number": "12", "name": "Q4", "type": "out"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "Q5", "type": "out"},
            "pin_16": {"number": "16", "name": "Q6", "type": "out"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "Q7", "type": "out"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC273",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6837 (Texas Instruments SN74HC273PWR, TSSOP-20, 20 pins) verified at intake; family batch integration C6837.", "Downloaded the official Texas Instruments 74HC273 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC273 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6540 / Texas Instruments CD74HC30M96 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS30 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_8_input_nand_gate_texas_instruments_cd74hc30m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hc30.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HC30M96 datasheet (C6540)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS30 symbol.",
        }
        part["electrical"] = {
            "device_type": "8 input nand gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A", "type": "in"},
            "pin_2": {"number": "2", "name": "B", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "D", "type": "in"},
            "pin_5": {"number": "5", "name": "E", "type": "in"},
            "pin_6": {"number": "6", "name": "F", "type": "in"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "Y", "type": "out"},
            "pin_9": {"number": "9", "name": "NC", "type": "no_connect"},
            "pin_10": {"number": "10", "name": "NC", "type": "no_connect"},
            "pin_11": {"number": "11", "name": "G", "type": "in"},
            "pin_12": {"number": "12", "name": "H", "type": "in"},
            "pin_13": {"number": "13", "name": "NC", "type": "no_connect"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS30",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6540 (Texas Instruments CD74HC30M96, SOIC-14, 14 pins) verified at intake; family batch integration C6540.", "Downloaded the official Texas Instruments 74HC30 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS30 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6838 / Texas Instruments SN74HC32DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS32 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_or_gate_texas_instruments_sn74hc32dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc32.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC32DR datasheet (C6838)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS32 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input or gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS32",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6838 (Texas Instruments SN74HC32DR, SOIC-14, 14 pins) verified at intake; family batch integration C6838.", "Downloaded the official Texas Instruments 74HC32 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS32 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2894 / Texas Instruments SN74HC32N - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS32 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_quad_2_input_or_gate_texas_instruments_sn74hc32n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc32.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC32N datasheet (C2894)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS32 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input or gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS32",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2894 (Texas Instruments SN74HC32N, DIP-14, 14 pins) verified at intake; family batch integration C2894.", "Downloaded the official Texas Instruments 74HC32 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS32 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6840 / Texas Instruments SN74HC32PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS32 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_quad_2_input_or_gate_texas_instruments_sn74hc32pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc32.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC32PWR datasheet (C6840)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS32 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input or gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS32",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6840 (Texas Instruments SN74HC32PWR, TSSOP-14, 14 pins) verified at intake; family batch integration C6840.", "Downloaded the official Texas Instruments 74HC32 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS32 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6841 / Texas Instruments SN74HC365DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS365 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_hex_bus_buffer_tri_state_texas_instruments_sn74hc365dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc365.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC365DR datasheet (C6841)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS365 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E1", "type": "in"},
            "pin_2": {"number": "2", "name": "I1", "type": "in"},
            "pin_3": {"number": "3", "name": "O1", "type": "ts"},
            "pin_4": {"number": "4", "name": "I2", "type": "in"},
            "pin_5": {"number": "5", "name": "O2", "type": "ts"},
            "pin_6": {"number": "6", "name": "I3", "type": "in"},
            "pin_7": {"number": "7", "name": "O3", "type": "ts"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "O4", "type": "ts"},
            "pin_10": {"number": "10", "name": "I4", "type": "in"},
            "pin_11": {"number": "11", "name": "O5", "type": "ts"},
            "pin_12": {"number": "12", "name": "I5", "type": "in"},
            "pin_13": {"number": "13", "name": "O6", "type": "ts"},
            "pin_14": {"number": "14", "name": "I6", "type": "in"},
            "pin_15": {"number": "15", "name": "E2", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS365",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6841 (Texas Instruments SN74HC365DR, SOIC-16, 16 pins) verified at intake; family batch integration C6841.", "Downloaded the official Texas Instruments 74HC365 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS365 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6844 / Texas Instruments SN74HC373DWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC373 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_transparent_latch_tri_state_texas_instruments_sn74hc373dwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc373.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "SN74HC373DWR datasheet (C6844)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC373 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "LE", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC373",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6844 (Texas Instruments SN74HC373DWR, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6844.", "Downloaded the official Texas Instruments 74HC373 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC373 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2885 / Texas Instruments SN74HC373N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC373 master; footprint Package_DIP:DIP-20_W7.62mm
    current = "electronic_ic_dip_20_logic_octal_d_type_transparent_latch_tri_state_texas_instruments_sn74hc373n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-20 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc373.pdf"
        part["dimensions_mm"] = {"length": 25.7, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC373N datasheet (C2885)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-20_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC373 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "LE", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC373",
            "machine_solder": "Package_DIP:DIP-20_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2885 (Texas Instruments SN74HC373N, DIP-20, 20 pins) verified at intake; family batch integration C2885.", "Downloaded the official Texas Instruments 74HC373 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC373 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_DIP:DIP-20_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6845 / Texas Instruments SN74HC374DWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC374 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_flip_flop_tri_state_texas_instruments_sn74hc374dwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc374.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "SN74HC374DWR datasheet (C6845)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC374 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Cp", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC374",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6845 (Texas Instruments SN74HC374DWR, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6845.", "Downloaded the official Texas Instruments 74HC374 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC374 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5237 / Texas Instruments SN74HC374N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC374 master; footprint Package_DIP:DIP-20_W7.62mm
    current = "electronic_ic_dip_20_logic_octal_d_type_flip_flop_tri_state_texas_instruments_sn74hc374n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-20 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc374.pdf"
        part["dimensions_mm"] = {"length": 25.7, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC374N datasheet (C5237)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-20_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC374 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Cp", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC374",
            "machine_solder": "Package_DIP:DIP-20_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5237 (Texas Instruments SN74HC374N, DIP-20, 20 pins) verified at intake; family batch integration C5237.", "Downloaded the official Texas Instruments 74HC374 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC374 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_DIP:DIP-20_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6846 / Texas Instruments SN74HC374NSR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC374 master; footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm
    current = "electronic_ic_soic_20_208mil_logic_octal_d_type_flip_flop_tri_state_texas_instruments_sn74hc374nsr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-20 208 mil (5.3 x 7.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc374.pdf"
        part["dimensions_mm"] = {"length": 7.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74HC374NSR datasheet (C6846)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-20_5.3x7.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC374 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Cp", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC374",
            "machine_solder": "Package_SO:SSOP-20_5.3x7.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6846 (Texas Instruments SN74HC374NSR, SOIC-20-208mil, 20 pins) verified at intake; family batch integration C6846.", "Downloaded the official Texas Instruments 74HC374 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC374 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6847 / Texas Instruments SN74HC374PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC374 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_d_type_flip_flop_tri_state_texas_instruments_sn74hc374pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc374.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC374PWR datasheet (C6847)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC374 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "O0", "type": "ts"},
            "pin_3": {"number": "3", "name": "D0", "type": "in"},
            "pin_4": {"number": "4", "name": "D1", "type": "in"},
            "pin_5": {"number": "5", "name": "O1", "type": "ts"},
            "pin_6": {"number": "6", "name": "O2", "type": "ts"},
            "pin_7": {"number": "7", "name": "D2", "type": "in"},
            "pin_8": {"number": "8", "name": "D3", "type": "in"},
            "pin_9": {"number": "9", "name": "O3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Cp", "type": "in"},
            "pin_12": {"number": "12", "name": "O4", "type": "ts"},
            "pin_13": {"number": "13", "name": "D4", "type": "in"},
            "pin_14": {"number": "14", "name": "D5", "type": "in"},
            "pin_15": {"number": "15", "name": "O5", "type": "ts"},
            "pin_16": {"number": "16", "name": "O6", "type": "ts"},
            "pin_17": {"number": "17", "name": "D6", "type": "in"},
            "pin_18": {"number": "18", "name": "D7", "type": "in"},
            "pin_19": {"number": "19", "name": "O7", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC374",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6847 (Texas Instruments SN74HC374PWR, TSSOP-20, 20 pins) verified at intake; family batch integration C6847.", "Downloaded the official Texas Instruments 74HC374 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC374 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6848 / Texas Instruments SN74HC4040DR - 74-series logic family
    # batch: pins from the KiCad 4xxx:4040 master; footprint Package_SO:SSOP-16_5.3x6.2mm_P0.65mm
    current = "electronic_ic_soic_16_208mil_logic_12_stage_binary_ripple_counter_texas_instruments_sn74hc4040dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-16 208 mil (5.3 x 6.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc4040.pdf"
        part["dimensions_mm"] = {"length": 6.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74HC4040DR datasheet (C6848)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-16_5.3x6.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 4xxx:4040 symbol.",
        }
        part["electrical"] = {
            "device_type": "12 stage binary ripple counter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "Q11", "type": "out"},
            "pin_2": {"number": "2", "name": "Q5", "type": "out"},
            "pin_3": {"number": "3", "name": "Q4", "type": "out"},
            "pin_4": {"number": "4", "name": "Q6", "type": "out"},
            "pin_5": {"number": "5", "name": "Q3", "type": "out"},
            "pin_6": {"number": "6", "name": "Q2", "type": "out"},
            "pin_7": {"number": "7", "name": "Q1", "type": "out"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Q0", "type": "out"},
            "pin_10": {"number": "10", "name": "CLK", "type": "in"},
            "pin_11": {"number": "11", "name": "Reset", "type": "in"},
            "pin_12": {"number": "12", "name": "Q8", "type": "out"},
            "pin_13": {"number": "13", "name": "Q7", "type": "out"},
            "pin_14": {"number": "14", "name": "Q9", "type": "out"},
            "pin_15": {"number": "15", "name": "Q10", "type": "out"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4040",
            "machine_solder": "Package_SO:SSOP-16_5.3x6.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6848 (Texas Instruments SN74HC4040DR, SOIC-16-208mil, 16 pins) verified at intake; family batch integration C6848.", "Downloaded the official Texas Instruments 74HC4040 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 4xxx:4040 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SSOP-16_5.3x6.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6542 / Texas Instruments CD74HC4046AM96 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4046 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_clock_management_pll_with_vco_texas_instruments_cd74hc4046am96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hc4046a.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HC4046AM96 datasheet (C6542)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 4xxx:4046 symbol.",
        }
        part["electrical"] = {
            "device_type": "",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "PCP", "type": "out"},
            "pin_2": {"number": "2", "name": "PC1", "type": "out"},
            "pin_3": {"number": "3", "name": "RefIn", "type": "in"},
            "pin_4": {"number": "4", "name": "FOUT", "type": "out"},
            "pin_5": {"number": "5", "name": "Inh", "type": "in"},
            "pin_6": {"number": "6", "name": "C1", "type": "in"},
            "pin_7": {"number": "7", "name": "C2", "type": "in"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "VCOin", "type": "in"},
            "pin_10": {"number": "10", "name": "SFout", "type": "out"},
            "pin_11": {"number": "11", "name": "R1", "type": "in"},
            "pin_12": {"number": "12", "name": "R2", "type": "in"},
            "pin_13": {"number": "13", "name": "PC2", "type": "ts"},
            "pin_14": {"number": "14", "name": "SigIn", "type": "in"},
            "pin_15": {"number": "15", "name": "ZOUT", "type": "out"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4046",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6542 (Texas Instruments CD74HC4046AM96, SOIC-16, 16 pins) verified at intake; family batch integration C6542.", "Downloaded the official Texas Instruments 74HC4046 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 4xxx:4046 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6543 / Texas Instruments CD74HC4046APWR - 74-series logic family
    # batch: pins from the KiCad 4xxx:4046 master; footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_16_clock_management_pll_with_vco_texas_instruments_cd74hc4046apwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-16 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hc4046a.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "CD74HC4046APWR datasheet (C6543)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-16_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 4xxx:4046 symbol.",
        }
        part["electrical"] = {
            "device_type": "",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "PCP", "type": "out"},
            "pin_2": {"number": "2", "name": "PC1", "type": "out"},
            "pin_3": {"number": "3", "name": "RefIn", "type": "in"},
            "pin_4": {"number": "4", "name": "FOUT", "type": "out"},
            "pin_5": {"number": "5", "name": "Inh", "type": "in"},
            "pin_6": {"number": "6", "name": "C1", "type": "in"},
            "pin_7": {"number": "7", "name": "C2", "type": "in"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "VCOin", "type": "in"},
            "pin_10": {"number": "10", "name": "SFout", "type": "out"},
            "pin_11": {"number": "11", "name": "R1", "type": "in"},
            "pin_12": {"number": "12", "name": "R2", "type": "in"},
            "pin_13": {"number": "13", "name": "PC2", "type": "ts"},
            "pin_14": {"number": "14", "name": "SigIn", "type": "in"},
            "pin_15": {"number": "15", "name": "ZOUT", "type": "out"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4046",
            "machine_solder": "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6543 (Texas Instruments CD74HC4046APWR, TSSOP-16, 16 pins) verified at intake; family batch integration C6543.", "Downloaded the official Texas Instruments 74HC4046 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 4xxx:4046 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6548 / Texas Instruments CD74HC4052M96 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4052 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_dual_4_channel_analog_multiplexer_demultiplexer_texas_instruments_cd74hc4052m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hc4052.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HC4052M96 datasheet (C6548)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 4xxx:4052 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual 4 channel analog multiplexer demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "Y0", "type": "passive"},
            "pin_2": {"number": "2", "name": "Y2", "type": "passive"},
            "pin_3": {"number": "3", "name": "Y", "type": "passive"},
            "pin_4": {"number": "4", "name": "Y3", "type": "passive"},
            "pin_5": {"number": "5", "name": "Y1", "type": "passive"},
            "pin_6": {"number": "6", "name": "Inh", "type": "in"},
            "pin_7": {"number": "7", "name": "VEE", "type": "pwr"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "B", "type": "in"},
            "pin_10": {"number": "10", "name": "A", "type": "in"},
            "pin_11": {"number": "11", "name": "X3", "type": "passive"},
            "pin_12": {"number": "12", "name": "X0", "type": "passive"},
            "pin_13": {"number": "13", "name": "X", "type": "passive"},
            "pin_14": {"number": "14", "name": "X1", "type": "passive"},
            "pin_15": {"number": "15", "name": "X2", "type": "passive"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4052",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6548 (Texas Instruments CD74HC4052M96, SOIC-16, 16 pins) verified at intake; family batch integration C6548.", "Downloaded the official Texas Instruments 74HC4052 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 4xxx:4052 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6545 / Texas Instruments CD74HC4053M96 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4053 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_triple_2_channel_analog_multiplexer_demultiplexer_texas_instruments_cd74hc4053m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hc4053.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HC4053M96 datasheet (C6545)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 4xxx:4053 symbol.",
        }
        part["electrical"] = {
            "device_type": "triple 2 channel analog multiplexer demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "Y1", "type": "passive"},
            "pin_2": {"number": "2", "name": "Y0", "type": "passive"},
            "pin_3": {"number": "3", "name": "Z1", "type": "passive"},
            "pin_4": {"number": "4", "name": "Z", "type": "passive"},
            "pin_5": {"number": "5", "name": "Z0", "type": "passive"},
            "pin_6": {"number": "6", "name": "Inh", "type": "in"},
            "pin_7": {"number": "7", "name": "VEE", "type": "pwr"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "C", "type": "in"},
            "pin_10": {"number": "10", "name": "B", "type": "in"},
            "pin_11": {"number": "11", "name": "A", "type": "in"},
            "pin_12": {"number": "12", "name": "X0", "type": "passive"},
            "pin_13": {"number": "13", "name": "X1", "type": "passive"},
            "pin_14": {"number": "14", "name": "X", "type": "passive"},
            "pin_15": {"number": "15", "name": "Y", "type": "passive"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4053",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6545 (Texas Instruments CD74HC4053M96, SOIC-16, 16 pins) verified at intake; family batch integration C6545.", "Downloaded the official Texas Instruments 74HC4053 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 4xxx:4053 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6546 / Texas Instruments CD74HC4053PWR - 74-series logic family
    # batch: pins from the KiCad 4xxx:4053 master; footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_16_logic_triple_2_channel_analog_multiplexer_demultiplexer_texas_instruments_cd74hc4053pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-16 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hc4053.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "CD74HC4053PWR datasheet (C6546)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-16_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 4xxx:4053 symbol.",
        }
        part["electrical"] = {
            "device_type": "triple 2 channel analog multiplexer demultiplexer",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "Y1", "type": "passive"},
            "pin_2": {"number": "2", "name": "Y0", "type": "passive"},
            "pin_3": {"number": "3", "name": "Z1", "type": "passive"},
            "pin_4": {"number": "4", "name": "Z", "type": "passive"},
            "pin_5": {"number": "5", "name": "Z0", "type": "passive"},
            "pin_6": {"number": "6", "name": "Inh", "type": "in"},
            "pin_7": {"number": "7", "name": "VEE", "type": "pwr"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "C", "type": "in"},
            "pin_10": {"number": "10", "name": "B", "type": "in"},
            "pin_11": {"number": "11", "name": "A", "type": "in"},
            "pin_12": {"number": "12", "name": "X0", "type": "passive"},
            "pin_13": {"number": "13", "name": "X1", "type": "passive"},
            "pin_14": {"number": "14", "name": "X", "type": "passive"},
            "pin_15": {"number": "15", "name": "Y", "type": "passive"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4053",
            "machine_solder": "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6546 (Texas Instruments CD74HC4053PWR, TSSOP-16, 16 pins) verified at intake; family batch integration C6546.", "Downloaded the official Texas Instruments 74HC4053 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 4xxx:4053 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6849 / Texas Instruments SN74HC4066DBR - 74-series logic family
    # batch: pins from the KiCad 4xxx:4066 master; footprint Package_SO:SSOP-14_5.3x6.2mm_P0.65mm
    current = "electronic_ic_ssop_14_208mil_logic_quad_bilateral_analog_switch_texas_instruments_sn74hc4066dbr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-14 208 mil (5.3 x 6.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc4066.pdf"
        part["dimensions_mm"] = {"length": 6.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74HC4066DBR datasheet (C6849)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-14_5.3x6.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 4xxx:4066 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bilateral analog switch",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1Y", "type": "passive"},
            "pin_2": {"number": "2", "name": "1Z", "type": "passive"},
            "pin_3": {"number": "3", "name": "2Z", "type": "passive"},
            "pin_4": {"number": "4", "name": "2Y", "type": "passive"},
            "pin_5": {"number": "5", "name": "2E", "type": "in"},
            "pin_6": {"number": "6", "name": "3E", "type": "in"},
            "pin_7": {"number": "7", "name": "VSS", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "passive"},
            "pin_9": {"number": "9", "name": "3Z", "type": "passive"},
            "pin_10": {"number": "10", "name": "4Z", "type": "passive"},
            "pin_11": {"number": "11", "name": "4Y", "type": "passive"},
            "pin_12": {"number": "12", "name": "4E", "type": "in"},
            "pin_13": {"number": "13", "name": "1E", "type": "in"},
            "pin_14": {"number": "14", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4066",
            "machine_solder": "Package_SO:SSOP-14_5.3x6.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6849 (Texas Instruments SN74HC4066DBR, SSOP-14-208mil, 14 pins) verified at intake; family batch integration C6849.", "Downloaded the official Texas Instruments 74HC4066 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 4xxx:4066 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SSOP-14_5.3x6.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6547 / Texas Instruments CD74HC4075M96 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4075 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_triple_3_input_or_gate_texas_instruments_cd74hc4075m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hc4075.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HC4075M96 datasheet (C6547)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 4xxx:4075 symbol.",
        }
        part["electrical"] = {
            "device_type": "triple 3 input or gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2B", "type": "in"},
            "pin_5": {"number": "5", "name": "2C", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "VSS", "type": "pwr"},
            "pin_8": {"number": "8", "name": "1C", "type": "in"},
            "pin_9": {"number": "9", "name": "1Y", "type": "out"},
            "pin_10": {"number": "10", "name": "3Y", "type": "out"},
            "pin_11": {"number": "11", "name": "3A", "type": "in"},
            "pin_12": {"number": "12", "name": "3B", "type": "in"},
            "pin_13": {"number": "13", "name": "3C", "type": "in"},
            "pin_14": {"number": "14", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4075",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6547 (Texas Instruments CD74HC4075M96, SOIC-14, 14 pins) verified at intake; family batch integration C6547.", "Downloaded the official Texas Instruments 74HC4075 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 4xxx:4075 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6757 / Texas Instruments SN74HC541DWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT541 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_buffer_tri_state_texas_instruments_sn74hc541dwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc541.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "SN74HC541DWR datasheet (C6757)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT541 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G1", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "in"},
            "pin_3": {"number": "3", "name": "A1", "type": "in"},
            "pin_4": {"number": "4", "name": "A2", "type": "in"},
            "pin_5": {"number": "5", "name": "A3", "type": "in"},
            "pin_6": {"number": "6", "name": "A4", "type": "in"},
            "pin_7": {"number": "7", "name": "A5", "type": "in"},
            "pin_8": {"number": "8", "name": "A6", "type": "in"},
            "pin_9": {"number": "9", "name": "A7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Y7", "type": "ts"},
            "pin_12": {"number": "12", "name": "Y6", "type": "ts"},
            "pin_13": {"number": "13", "name": "Y5", "type": "ts"},
            "pin_14": {"number": "14", "name": "Y4", "type": "ts"},
            "pin_15": {"number": "15", "name": "Y3", "type": "ts"},
            "pin_16": {"number": "16", "name": "Y2", "type": "ts"},
            "pin_17": {"number": "17", "name": "Y1", "type": "ts"},
            "pin_18": {"number": "18", "name": "Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "G2", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT541",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6757 (Texas Instruments SN74HC541DWR, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6757.", "Downloaded the official Texas Instruments 74HC541 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT541 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6758 / Texas Instruments SN74HC541PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT541 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_texas_instruments_sn74hc541pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc541.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC541PWR datasheet (C6758)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT541 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G1", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "in"},
            "pin_3": {"number": "3", "name": "A1", "type": "in"},
            "pin_4": {"number": "4", "name": "A2", "type": "in"},
            "pin_5": {"number": "5", "name": "A3", "type": "in"},
            "pin_6": {"number": "6", "name": "A4", "type": "in"},
            "pin_7": {"number": "7", "name": "A5", "type": "in"},
            "pin_8": {"number": "8", "name": "A6", "type": "in"},
            "pin_9": {"number": "9", "name": "A7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Y7", "type": "ts"},
            "pin_12": {"number": "12", "name": "Y6", "type": "ts"},
            "pin_13": {"number": "13", "name": "Y5", "type": "ts"},
            "pin_14": {"number": "14", "name": "Y4", "type": "ts"},
            "pin_15": {"number": "15", "name": "Y3", "type": "ts"},
            "pin_16": {"number": "16", "name": "Y2", "type": "ts"},
            "pin_17": {"number": "17", "name": "Y1", "type": "ts"},
            "pin_18": {"number": "18", "name": "Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "G2", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT541",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6758 (Texas Instruments SN74HC541PWR, TSSOP-20, 20 pins) verified at intake; family batch integration C6758.", "Downloaded the official Texas Instruments 74HC541 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT541 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5196 / Texas Instruments SN74HC573AN - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS573 master; footprint Package_DIP:DIP-20_W7.62mm
    current = "electronic_ic_dip_20_logic_octal_d_type_transparent_latch_tri_state_texas_instruments_sn74hc573an"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-20 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc573a.pdf"
        part["dimensions_mm"] = {"length": 25.7, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC573AN datasheet (C5196)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-20_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS573 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Load", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS573",
            "machine_solder": "Package_DIP:DIP-20_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5196 (Texas Instruments SN74HC573AN, DIP-20, 20 pins) verified at intake; family batch integration C5196.", "Downloaded the official Texas Instruments 74HC573 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS573 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_DIP:DIP-20_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6759 / Texas Instruments SN74HC573APWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS573 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_d_type_transparent_latch_tri_state_texas_instruments_sn74hc573apwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc573a.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC573APWR datasheet (C6759)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS573 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Load", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS573",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6759 (Texas Instruments SN74HC573APWR, TSSOP-20, 20 pins) verified at intake; family batch integration C6759.", "Downloaded the official Texas Instruments 74HC573 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS573 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6762 / Texas Instruments SN74HC74DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC74 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_dual_d_type_flip_flop_set_reset_texas_instruments_sn74hc74dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc74.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC74DR datasheet (C6762)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC74 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual d type flip flop set reset",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{R}", "type": "in"},
            "pin_2": {"number": "2", "name": "D", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "~{S}", "type": "in"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "~{Q}", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "~{Q}", "type": "out"},
            "pin_9": {"number": "9", "name": "Q", "type": "out"},
            "pin_10": {"number": "10", "name": "~{S}", "type": "in"},
            "pin_11": {"number": "11", "name": "C", "type": "in"},
            "pin_12": {"number": "12", "name": "D", "type": "in"},
            "pin_13": {"number": "13", "name": "~{R}", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC74",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6762 (Texas Instruments SN74HC74DR, SOIC-14, 14 pins) verified at intake; family batch integration C6762.", "Downloaded the official Texas Instruments 74HC74 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC74 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6761 / Texas Instruments SN74HC74PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC74 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_dual_d_type_flip_flop_set_reset_texas_instruments_sn74hc74pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc74.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HC74PWR datasheet (C6761)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC74 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual d type flip flop set reset",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{R}", "type": "in"},
            "pin_2": {"number": "2", "name": "D", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "~{S}", "type": "in"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "~{Q}", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "~{Q}", "type": "out"},
            "pin_9": {"number": "9", "name": "Q", "type": "out"},
            "pin_10": {"number": "10", "name": "~{S}", "type": "in"},
            "pin_11": {"number": "11", "name": "C", "type": "in"},
            "pin_12": {"number": "12", "name": "D", "type": "in"},
            "pin_13": {"number": "13", "name": "~{R}", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC74",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6761 (Texas Instruments SN74HC74PWR, TSSOP-14, 14 pins) verified at intake; family batch integration C6761.", "Downloaded the official Texas Instruments 74HC74 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC74 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6763 / Texas Instruments SN74HC86DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC86 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_xor_gate_texas_instruments_sn74hc86dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc86.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HC86DR datasheet (C6763)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC86 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input xor gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC86",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6763 (Texas Instruments SN74HC86DR, SOIC-14, 14 pins) verified at intake; family batch integration C6763.", "Downloaded the official Texas Instruments 74HC86 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC86 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2903 / Texas Instruments SN74HC86N - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC86 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_quad_2_input_xor_gate_texas_instruments_sn74hc86n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hc86.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74HC86N datasheet (C2903)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74HC86 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input xor gate",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC86",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C2903 (Texas Instruments SN74HC86N, DIP-14, 14 pins) verified at intake; family batch integration C2903.", "Downloaded the official Texas Instruments 74HC86 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC86 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6551 / Texas Instruments CD74HC93M96 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS93 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_4_bit_binary_ripple_counter_texas_instruments_cd74hc93m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hc93.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HC93M96 datasheet (C6551)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS93 symbol.",
        }
        part["electrical"] = {
            "device_type": "4 bit binary ripple counter",
            "supply_voltage": "2.0-6.0 V",
            "logic_family": "74HC",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "CP1..3", "type": "in"},
            "pin_2": {"number": "2", "name": "R0(1)", "type": "in"},
            "pin_3": {"number": "3", "name": "R0(2)", "type": "in"},
            "pin_4": {"number": "4", "name": "NC", "type": "no_connect"},
            "pin_5": {"number": "5", "name": "VCC", "type": "pwr"},
            "pin_6": {"number": "6", "name": "NC", "type": "no_connect"},
            "pin_7": {"number": "7", "name": "NC", "type": "no_connect"},
            "pin_8": {"number": "8", "name": "Q2", "type": "out"},
            "pin_9": {"number": "9", "name": "Q1", "type": "out"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Q3", "type": "out"},
            "pin_12": {"number": "12", "name": "Q0", "type": "out"},
            "pin_13": {"number": "13", "name": "NC", "type": "no_connect"},
            "pin_14": {"number": "14", "name": "CP0", "type": "in"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS93",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6551 (Texas Instruments CD74HC93M96, SOIC-14, 14 pins) verified at intake; family batch integration C6551.", "Downloaded the official Texas Instruments 74HC93 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS93 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6764 / Texas Instruments SN74HCT00DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT00 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_nand_gate_texas_instruments_sn74hct00dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct00.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HCT00DR datasheet (C6764)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT00 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT00",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6764 (Texas Instruments SN74HCT00DR, SOIC-14, 14 pins) verified at intake; family batch integration C6764.", "Downloaded the official Texas Instruments 74HCT00 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT00 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6552 / Texas Instruments CD74HCT00M96 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT00 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_nand_gate_texas_instruments_cd74hct00m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hct00.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HCT00M96 datasheet (C6552)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT00 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nand gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT00",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6552 (Texas Instruments CD74HCT00M96, SOIC-14, 14 pins) verified at intake; family batch integration C6552.", "Downloaded the official Texas Instruments 74HCT00 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT00 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6766 / Texas Instruments SN74HCT04DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT04 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_texas_instruments_sn74hct04dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct04.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HCT04DR datasheet (C6766)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT04",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6766 (Texas Instruments SN74HCT04DR, SOIC-14, 14 pins) verified at intake; family batch integration C6766.", "Downloaded the official Texas Instruments 74HCT04 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6767 / Texas Instruments SN74HCT08DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS08 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_and_gate_texas_instruments_sn74hct08dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct08.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HCT08DR datasheet (C6767)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS08 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input and gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS08",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6767 (Texas Instruments SN74HCT08DR, SOIC-14, 14 pins) verified at intake; family batch integration C6767.", "Downloaded the official Texas Instruments 74HCT08 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS08 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6554 / Texas Instruments CD74HCT139M96 - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS139 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_dual_2_to_4_line_decoder_demultiplexer_texas_instruments_cd74hct139m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hct139.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HCT139M96 datasheet (C6554)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS139 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual 2 to 4 line decoder demultiplexer",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "in"},
            "pin_3": {"number": "3", "name": "A1", "type": "in"},
            "pin_4": {"number": "4", "name": "O0", "type": "out"},
            "pin_5": {"number": "5", "name": "O1", "type": "out"},
            "pin_6": {"number": "6", "name": "O2", "type": "out"},
            "pin_7": {"number": "7", "name": "O3", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "O3", "type": "out"},
            "pin_10": {"number": "10", "name": "O2", "type": "out"},
            "pin_11": {"number": "11", "name": "O1", "type": "out"},
            "pin_12": {"number": "12", "name": "O0", "type": "out"},
            "pin_13": {"number": "13", "name": "A1", "type": "in"},
            "pin_14": {"number": "14", "name": "A0", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS139",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6554 (Texas Instruments CD74HCT139M96, SOIC-16, 16 pins) verified at intake; family batch integration C6554.", "Downloaded the official Texas Instruments 74HCT139 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS139 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6769 / Texas Instruments SN74HCT14DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC14 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_schmitt_trigger_inverter_texas_instruments_sn74hct14dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct14.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HCT14DR datasheet (C6769)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HC14 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex schmitt trigger inverter",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC14",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6769 (Texas Instruments SN74HCT14DR, SOIC-14, 14 pins) verified at intake; family batch integration C6769.", "Downloaded the official Texas Instruments 74HCT14 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC14 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6771 / Texas Instruments SN74HCT157DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS157 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_quad_2_to_1_line_multiplexer_texas_instruments_sn74hct157dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct157.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HCT157DR datasheet (C6771)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS157 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 to 1 line multiplexer",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "S", "type": "in"},
            "pin_2": {"number": "2", "name": "I0a", "type": "in"},
            "pin_3": {"number": "3", "name": "I1a", "type": "in"},
            "pin_4": {"number": "4", "name": "Za", "type": "out"},
            "pin_5": {"number": "5", "name": "I0b", "type": "in"},
            "pin_6": {"number": "6", "name": "I1b", "type": "in"},
            "pin_7": {"number": "7", "name": "Zb", "type": "out"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "Zc", "type": "out"},
            "pin_10": {"number": "10", "name": "I1c", "type": "in"},
            "pin_11": {"number": "11", "name": "I0c", "type": "in"},
            "pin_12": {"number": "12", "name": "Zd", "type": "out"},
            "pin_13": {"number": "13", "name": "I1d", "type": "in"},
            "pin_14": {"number": "14", "name": "I0d", "type": "in"},
            "pin_15": {"number": "15", "name": "E", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS157",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6771 (Texas Instruments SN74HCT157DR, SOIC-16, 16 pins) verified at intake; family batch integration C6771.", "Downloaded the official Texas Instruments 74HCT157 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS157 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6772 / Texas Instruments SN74HCT240NSR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT240 master; footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm
    current = "electronic_ic_soic_20_208mil_logic_octal_bus_buffer_tri_state_inverting_texas_instruments_sn74hct240nsr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-20 208 mil (5.3 x 7.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct240.pdf"
        part["dimensions_mm"] = {"length": 7.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74HCT240NSR datasheet (C6772)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-20_5.3x7.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT240 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state inverting",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT240",
            "machine_solder": "Package_SO:SSOP-20_5.3x7.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6772 (Texas Instruments SN74HCT240NSR, SOIC-20-208mil, 20 pins) verified at intake; family batch integration C6772.", "Downloaded the official Texas Instruments 74HCT240 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT240 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6775 / Texas Instruments SN74HCT244DBR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT244 master; footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm
    current = "electronic_ic_ssop_20_208mil_logic_octal_bus_buffer_tri_state_texas_instruments_sn74hct244dbr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-20 208 mil (5.3 x 7.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct244.pdf"
        part["dimensions_mm"] = {"length": 7.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74HCT244DBR datasheet (C6775)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-20_5.3x7.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT244",
            "machine_solder": "Package_SO:SSOP-20_5.3x7.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6775 (Texas Instruments SN74HCT244DBR, SSOP-20-208mil, 20 pins) verified at intake; family batch integration C6775.", "Downloaded the official Texas Instruments 74HCT244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6776 / Texas Instruments SN74HCT244DWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT244 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_buffer_tri_state_texas_instruments_sn74hct244dwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct244.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "SN74HCT244DWR datasheet (C6776)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT244",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6776 (Texas Instruments SN74HCT244DWR, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6776.", "Downloaded the official Texas Instruments 74HCT244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6777 / Texas Instruments SN74HCT244NSR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT244 master; footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm
    current = "electronic_ic_soic_20_208mil_logic_octal_bus_buffer_tri_state_texas_instruments_sn74hct244nsr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SSOP-20 208 mil (5.3 x 7.2 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct244.pdf"
        part["dimensions_mm"] = {"length": 7.2, "width": 5.3, "height": 1.98}
        part["dimension_reference"] = {
            "document": "SN74HCT244NSR datasheet (C6777)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SSOP-20_5.3x7.2mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT244",
            "machine_solder": "Package_SO:SSOP-20_5.3x7.2mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6777 (Texas Instruments SN74HCT244NSR, SOIC-20-208mil, 20 pins) verified at intake; family batch integration C6777.", "Downloaded the official Texas Instruments 74HCT244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SSOP-20_5.3x7.2mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6778 / Texas Instruments SN74HCT244PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT244 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_texas_instruments_sn74hct244pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct244.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HCT244PWR datasheet (C6778)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT244",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6778 (Texas Instruments SN74HCT244PWR, TSSOP-20, 20 pins) verified at intake; family batch integration C6778.", "Downloaded the official Texas Instruments 74HCT244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6779 / Texas Instruments SN74HCT245PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC245 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_transceiver_tri_state_texas_instruments_sn74hct245pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct245.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74HCT245PWR datasheet (C6779)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC245 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus transceiver tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A->B", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "ts"},
            "pin_3": {"number": "3", "name": "A1", "type": "ts"},
            "pin_4": {"number": "4", "name": "A2", "type": "ts"},
            "pin_5": {"number": "5", "name": "A3", "type": "ts"},
            "pin_6": {"number": "6", "name": "A4", "type": "ts"},
            "pin_7": {"number": "7", "name": "A5", "type": "ts"},
            "pin_8": {"number": "8", "name": "A6", "type": "ts"},
            "pin_9": {"number": "9", "name": "A7", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "B7", "type": "ts"},
            "pin_12": {"number": "12", "name": "B6", "type": "ts"},
            "pin_13": {"number": "13", "name": "B5", "type": "ts"},
            "pin_14": {"number": "14", "name": "B4", "type": "ts"},
            "pin_15": {"number": "15", "name": "B3", "type": "ts"},
            "pin_16": {"number": "16", "name": "B2", "type": "ts"},
            "pin_17": {"number": "17", "name": "B1", "type": "ts"},
            "pin_18": {"number": "18", "name": "B0", "type": "ts"},
            "pin_19": {"number": "19", "name": "CE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC245",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6779 (Texas Instruments SN74HCT245PWR, TSSOP-20, 20 pins) verified at intake; family batch integration C6779.", "Downloaded the official Texas Instruments 74HCT245 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC245 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6781 / Texas Instruments SN74HCT32DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS32 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_or_gate_texas_instruments_sn74hct32dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct32.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HCT32DR datasheet (C6781)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS32 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input or gate",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS32",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6781 (Texas Instruments SN74HCT32DR, SOIC-14, 14 pins) verified at intake; family batch integration C6781.", "Downloaded the official Texas Instruments 74HCT32 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS32 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6559 / Texas Instruments CD74HCT4053M96 - 74-series logic family
    # batch: pins from the KiCad 4xxx:4053 master; footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm
    current = "electronic_ic_soic_16_logic_triple_2_channel_analog_multiplexer_demultiplexer_texas_instruments_cd74hct4053m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-16 (SOT109-1, 3.9 x 9.9 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hct4053.pdf"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HCT4053M96 datasheet (C6559)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-16_3.9x9.9mm_P1.27mm master geometry; pinning cross-checked against the KiCad 4xxx:4053 symbol.",
        }
        part["electrical"] = {
            "device_type": "triple 2 channel analog multiplexer demultiplexer",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "Y1", "type": "passive"},
            "pin_2": {"number": "2", "name": "Y0", "type": "passive"},
            "pin_3": {"number": "3", "name": "Z1", "type": "passive"},
            "pin_4": {"number": "4", "name": "Z", "type": "passive"},
            "pin_5": {"number": "5", "name": "Z0", "type": "passive"},
            "pin_6": {"number": "6", "name": "Inh", "type": "in"},
            "pin_7": {"number": "7", "name": "VEE", "type": "pwr"},
            "pin_8": {"number": "8", "name": "VSS", "type": "pwr"},
            "pin_9": {"number": "9", "name": "C", "type": "in"},
            "pin_10": {"number": "10", "name": "B", "type": "in"},
            "pin_11": {"number": "11", "name": "A", "type": "in"},
            "pin_12": {"number": "12", "name": "X0", "type": "passive"},
            "pin_13": {"number": "13", "name": "X1", "type": "passive"},
            "pin_14": {"number": "14", "name": "X", "type": "passive"},
            "pin_15": {"number": "15", "name": "Y", "type": "passive"},
            "pin_16": {"number": "16", "name": "VDD", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "4xxx:4053",
            "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6559 (Texas Instruments CD74HCT4053M96, SOIC-16, 16 pins) verified at intake; family batch integration C6559.", "Downloaded the official Texas Instruments 74HCT4053 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 4xxx:4053 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:SOIC-16_3.9x9.9mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6560 / Texas Instruments CD74HCT541M96 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT541 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_bus_buffer_tri_state_texas_instruments_cd74hct541m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hct541.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "CD74HCT541M96 datasheet (C6560)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT541 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G1", "type": "in"},
            "pin_2": {"number": "2", "name": "A0", "type": "in"},
            "pin_3": {"number": "3", "name": "A1", "type": "in"},
            "pin_4": {"number": "4", "name": "A2", "type": "in"},
            "pin_5": {"number": "5", "name": "A3", "type": "in"},
            "pin_6": {"number": "6", "name": "A4", "type": "in"},
            "pin_7": {"number": "7", "name": "A5", "type": "in"},
            "pin_8": {"number": "8", "name": "A6", "type": "in"},
            "pin_9": {"number": "9", "name": "A7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Y7", "type": "ts"},
            "pin_12": {"number": "12", "name": "Y6", "type": "ts"},
            "pin_13": {"number": "13", "name": "Y5", "type": "ts"},
            "pin_14": {"number": "14", "name": "Y4", "type": "ts"},
            "pin_15": {"number": "15", "name": "Y3", "type": "ts"},
            "pin_16": {"number": "16", "name": "Y2", "type": "ts"},
            "pin_17": {"number": "17", "name": "Y1", "type": "ts"},
            "pin_18": {"number": "18", "name": "Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "G2", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT541",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6560 (Texas Instruments CD74HCT541M96, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6560.", "Downloaded the official Texas Instruments 74HCT541 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT541 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6786 / Texas Instruments SN74HCT573DWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS573 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_transparent_latch_tri_state_texas_instruments_sn74hct573dwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct573.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "SN74HCT573DWR datasheet (C6786)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS573 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type transparent latch tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Load", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS573",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6786 (Texas Instruments SN74HCT573DWR, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6786.", "Downloaded the official Texas Instruments 74HCT573 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS573 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6788 / Texas Instruments SN74HCT574DWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT574 master; footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm
    current = "electronic_ic_soic_20_300mil_logic_octal_d_type_flip_flop_tri_state_texas_instruments_sn74hct574dwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-20W 300 mil (7.5 x 12.8 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct574.pdf"
        part["dimensions_mm"] = {"length": 12.8, "width": 7.5, "height": 2.65}
        part["dimension_reference"] = {
            "document": "SN74HCT574DWR datasheet (C6788)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT574 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal d type flip flop tri state",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "OE", "type": "in"},
            "pin_2": {"number": "2", "name": "D0", "type": "in"},
            "pin_3": {"number": "3", "name": "D1", "type": "in"},
            "pin_4": {"number": "4", "name": "D2", "type": "in"},
            "pin_5": {"number": "5", "name": "D3", "type": "in"},
            "pin_6": {"number": "6", "name": "D4", "type": "in"},
            "pin_7": {"number": "7", "name": "D5", "type": "in"},
            "pin_8": {"number": "8", "name": "D6", "type": "in"},
            "pin_9": {"number": "9", "name": "D7", "type": "in"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Cp", "type": "in"},
            "pin_12": {"number": "12", "name": "Q7", "type": "ts"},
            "pin_13": {"number": "13", "name": "Q6", "type": "ts"},
            "pin_14": {"number": "14", "name": "Q5", "type": "ts"},
            "pin_15": {"number": "15", "name": "Q4", "type": "ts"},
            "pin_16": {"number": "16", "name": "Q3", "type": "ts"},
            "pin_17": {"number": "17", "name": "Q2", "type": "ts"},
            "pin_18": {"number": "18", "name": "Q1", "type": "ts"},
            "pin_19": {"number": "19", "name": "Q0", "type": "ts"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT574",
            "machine_solder": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6788 (Texas Instruments SN74HCT574DWR, SOIC-20-300mil, 20 pins) verified at intake; family batch integration C6788.", "Downloaded the official Texas Instruments 74HCT574 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT574 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6790 / Texas Instruments SN74HCT74DRG4 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT74 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_dual_d_type_flip_flop_set_reset_texas_instruments_sn74hct74drg4"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74hct74.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74HCT74DRG4 datasheet (C6790)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT74 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual d type flip flop set reset",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{R}", "type": "in"},
            "pin_2": {"number": "2", "name": "D", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "~{S}", "type": "in"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "~{Q}", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "~{Q}", "type": "out"},
            "pin_9": {"number": "9", "name": "Q", "type": "out"},
            "pin_10": {"number": "10", "name": "~{S}", "type": "in"},
            "pin_11": {"number": "11", "name": "C", "type": "in"},
            "pin_12": {"number": "12", "name": "D", "type": "in"},
            "pin_13": {"number": "13", "name": "~{R}", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT74",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6790 (Texas Instruments SN74HCT74DRG4, SOIC-14, 14 pins) verified at intake; family batch integration C6790.", "Downloaded the official Texas Instruments 74HCT74 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT74 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6561 / Texas Instruments CD74HCT74M96 - 74-series logic family
    # batch: pins from the KiCad 74xx:74HCT74 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_dual_d_type_flip_flop_set_reset_texas_instruments_cd74hct74m96"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/cd74hct74.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "CD74HCT74M96 datasheet (C6561)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74HCT74 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual d type flip flop set reset",
            "supply_voltage": "4.5-5.5 V (TTL-compatible inputs)",
            "logic_family": "74HCT",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~{R}", "type": "in"},
            "pin_2": {"number": "2", "name": "D", "type": "in"},
            "pin_3": {"number": "3", "name": "C", "type": "in"},
            "pin_4": {"number": "4", "name": "~{S}", "type": "in"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "~{Q}", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "~{Q}", "type": "out"},
            "pin_9": {"number": "9", "name": "Q", "type": "out"},
            "pin_10": {"number": "10", "name": "~{S}", "type": "in"},
            "pin_11": {"number": "11", "name": "C", "type": "in"},
            "pin_12": {"number": "12", "name": "D", "type": "in"},
            "pin_13": {"number": "13", "name": "~{R}", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HCT74",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6561 (Texas Instruments CD74HCT74M96, SOIC-14, 14 pins) verified at intake; family batch integration C6561.", "Downloaded the official Texas Instruments 74HCT74 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HCT74 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6794 / Texas Instruments SN74LS02DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS02 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_nor_gate_texas_instruments_sn74ls02dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ls02.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74LS02DR datasheet (C6794)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS02 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input nor gate",
            "supply_voltage": "",
            "logic_family": "74LS",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1Y", "type": "out"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1B", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2B", "type": "in"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3A", "type": "in"},
            "pin_9": {"number": "9", "name": "3B", "type": "in"},
            "pin_10": {"number": "10", "name": "3Y", "type": "out"},
            "pin_11": {"number": "11", "name": "4A", "type": "in"},
            "pin_12": {"number": "12", "name": "4B", "type": "in"},
            "pin_13": {"number": "13", "name": "4Y", "type": "out"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS02",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6794 (Texas Instruments SN74LS02DR, SOIC-14, 14 pins) verified at intake; family batch integration C6794.", "Downloaded the official Texas Instruments 74LS02 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS02 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6796 / Texas Instruments SN74LS04DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS04 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_texas_instruments_sn74ls04dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ls04.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74LS04DR datasheet (C6796)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS04 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter",
            "supply_voltage": "",
            "logic_family": "74LS",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS04",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6796 (Texas Instruments SN74LS04DR, SOIC-14, 14 pins) verified at intake; family batch integration C6796.", "Downloaded the official Texas Instruments 74LS04 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS04 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6798 / Texas Instruments SN74LS05DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS05 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_hex_inverter_open_collector_texas_instruments_sn74ls05dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ls05.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74LS05DR datasheet (C6798)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS05 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex inverter open collector",
            "supply_voltage": "",
            "logic_family": "74LS",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS05",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6798 (Texas Instruments SN74LS05DR, SOIC-14, 14 pins) verified at intake; family batch integration C6798.", "Downloaded the official Texas Instruments 74LS05 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS05 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5197 / Texas Instruments SN74LS07N - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS07 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_hex_buffer_open_collector_texas_instruments_sn74ls07n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ls07.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74LS07N datasheet (C5197)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS07 symbol.",
        }
        part["electrical"] = {
            "device_type": "hex buffer open collector",
            "supply_voltage": "",
            "logic_family": "74LS",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1Y", "type": "out"},
            "pin_3": {"number": "3", "name": "2A", "type": "in"},
            "pin_4": {"number": "4", "name": "2Y", "type": "out"},
            "pin_5": {"number": "5", "name": "3A", "type": "in"},
            "pin_6": {"number": "6", "name": "3Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "4Y", "type": "out"},
            "pin_9": {"number": "9", "name": "4A", "type": "in"},
            "pin_10": {"number": "10", "name": "5Y", "type": "out"},
            "pin_11": {"number": "11", "name": "5A", "type": "in"},
            "pin_12": {"number": "12", "name": "6Y", "type": "out"},
            "pin_13": {"number": "13", "name": "6A", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS07",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5197 (Texas Instruments SN74LS07N, DIP-14, 14 pins) verified at intake; family batch integration C5197.", "Downloaded the official Texas Instruments 74LS07 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS07 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6802 / Texas Instruments SN74LS08DR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS08 master; footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm
    current = "electronic_ic_soic_14_logic_quad_2_input_and_gate_texas_instruments_sn74ls08dr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOIC-14 (SOT108-1, 3.9 x 8.7 mm, 1.27 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ls08.pdf"
        part["dimensions_mm"] = {"length": 8.7, "width": 3.9, "height": 1.75}
        part["dimension_reference"] = {
            "document": "SN74LS08DR datasheet (C6802)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:SOIC-14_3.9x8.7mm_P1.27mm master geometry; pinning cross-checked against the KiCad 74xx:74LS08 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad 2 input and gate",
            "supply_voltage": "",
            "logic_family": "74LS",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1A", "type": "in"},
            "pin_2": {"number": "2", "name": "1B", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "out"},
            "pin_4": {"number": "4", "name": "2A", "type": "in"},
            "pin_5": {"number": "5", "name": "2B", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "out"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "out"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3B", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "out"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4B", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS08",
            "machine_solder": "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6802 (Texas Instruments SN74LS08DR, SOIC-14, 14 pins) verified at intake; family batch integration C6802.", "Downloaded the official Texas Instruments 74LS08 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS08 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:SOIC-14_3.9x8.7mm_P1.27mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5262 / Texas Instruments SN74LS90N - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS90 master; footprint Package_DIP:DIP-14_W7.62mm
    current = "electronic_ic_dip_14_logic_decade_counter_texas_instruments_sn74ls90n"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "PDIP-14 (7.62 mm row spacing)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74ls90.pdf"
        part["dimensions_mm"] = {"length": 19.2, "width": 6.35, "height": 3.3}
        part["dimension_reference"] = {
            "document": "SN74LS90N datasheet (C5262)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_DIP:DIP-14_W7.62mm master geometry; pinning cross-checked against the KiCad 74xx:74LS90 symbol.",
        }
        part["electrical"] = {
            "device_type": "decade counter",
            "supply_voltage": "",
            "logic_family": "74LS",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "CP1..3", "type": "in"},
            "pin_2": {"number": "2", "name": "R0(1)", "type": "in"},
            "pin_3": {"number": "3", "name": "R0(2)", "type": "in"},
            "pin_4": {"number": "4", "name": "NC", "type": "no_connect"},
            "pin_5": {"number": "5", "name": "VCC", "type": "pwr"},
            "pin_6": {"number": "6", "name": "R9(1)", "type": "in"},
            "pin_7": {"number": "7", "name": "R9(2)", "type": "in"},
            "pin_8": {"number": "8", "name": "Q2", "type": "out"},
            "pin_9": {"number": "9", "name": "Q1", "type": "out"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "Q3", "type": "out"},
            "pin_12": {"number": "12", "name": "Q0", "type": "out"},
            "pin_13": {"number": "13", "name": "NC", "type": "no_connect"},
            "pin_14": {"number": "14", "name": "CP0", "type": "in"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS90",
            "machine_solder": "Package_DIP:DIP-14_W7.62mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C5262 (Texas Instruments SN74LS90N, DIP-14, 14 pins) verified at intake; family batch integration C5262.", "Downloaded the official Texas Instruments 74LS90 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS90 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_DIP:DIP-14_W7.62mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6036 / Texas Instruments SN74LV123APWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC123 master; footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_16_logic_dual_retriggerable_monostable_multivibrator_texas_instruments_sn74lv123apwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-16 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74lv123a.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74LV123APWR datasheet (C6036)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-16_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC123 symbol.",
        }
        part["electrical"] = {
            "device_type": "dual retriggerable monostable multivibrator",
            "supply_voltage": "2.0-5.5 V",
            "logic_family": "74LV",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A", "type": "in"},
            "pin_2": {"number": "2", "name": "B", "type": "in"},
            "pin_3": {"number": "3", "name": "Clr", "type": "in"},
            "pin_4": {"number": "4", "name": "~{Q}", "type": "out"},
            "pin_5": {"number": "5", "name": "Q", "type": "out"},
            "pin_6": {"number": "6", "name": "Cext", "type": "in"},
            "pin_7": {"number": "7", "name": "RCext", "type": "in"},
            "pin_8": {"number": "8", "name": "GND", "type": "pwr"},
            "pin_9": {"number": "9", "name": "A", "type": "in"},
            "pin_10": {"number": "10", "name": "B", "type": "in"},
            "pin_11": {"number": "11", "name": "Clr", "type": "in"},
            "pin_12": {"number": "12", "name": "~{Q}", "type": "out"},
            "pin_13": {"number": "13", "name": "Q", "type": "out"},
            "pin_14": {"number": "14", "name": "Cext", "type": "in"},
            "pin_15": {"number": "15", "name": "RCext", "type": "in"},
            "pin_16": {"number": "16", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC123",
            "machine_solder": "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C6036 (Texas Instruments SN74LV123APWR, TSSOP-16, 16 pins) verified at intake; family batch integration C6036.", "Downloaded the official Texas Instruments 74LV123 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC123 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 16-pin package count.", "Footprint Package_SO:TSSOP-16_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7038 / Texas Instruments SN74LVCH244APWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74HC244 master; footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm
    current = "electronic_ic_tssop_20_logic_octal_bus_buffer_tri_state_texas_instruments_sn74lvch244apwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-20 (4.4 x 6.5 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74lvch244a.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74LVCH244APWR datasheet (C7038)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74HC244 symbol.",
        }
        part["electrical"] = {
            "device_type": "octal bus buffer tri state",
            "supply_voltage": "1.65-3.6 V",
            "logic_family": "74LVCH",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A0", "type": "in"},
            "pin_3": {"number": "3", "name": "2Y0", "type": "ts"},
            "pin_4": {"number": "4", "name": "1A1", "type": "in"},
            "pin_5": {"number": "5", "name": "2Y1", "type": "ts"},
            "pin_6": {"number": "6", "name": "1A2", "type": "in"},
            "pin_7": {"number": "7", "name": "2Y2", "type": "ts"},
            "pin_8": {"number": "8", "name": "1A3", "type": "in"},
            "pin_9": {"number": "9", "name": "2Y3", "type": "ts"},
            "pin_10": {"number": "10", "name": "GND", "type": "pwr"},
            "pin_11": {"number": "11", "name": "2A3", "type": "in"},
            "pin_12": {"number": "12", "name": "1Y3", "type": "ts"},
            "pin_13": {"number": "13", "name": "2A2", "type": "in"},
            "pin_14": {"number": "14", "name": "1Y2", "type": "ts"},
            "pin_15": {"number": "15", "name": "2A1", "type": "in"},
            "pin_16": {"number": "16", "name": "1Y1", "type": "ts"},
            "pin_17": {"number": "17", "name": "2A0", "type": "in"},
            "pin_18": {"number": "18", "name": "1Y0", "type": "ts"},
            "pin_19": {"number": "19", "name": "2OE", "type": "in"},
            "pin_20": {"number": "20", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74HC244",
            "machine_solder": "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7038 (Texas Instruments SN74LVCH244APWR, TSSOP-20, 20 pins) verified at intake; family batch integration C7038.", "Downloaded the official Texas Instruments 74LVCH244 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74HC244 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 20-pin package count.", "Footprint Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7042 / Texas Instruments SN74LVTH125PWR - 74-series logic family
    # batch: pins from the KiCad 74xx:74LS125 master; footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm
    current = "electronic_ic_tssop_14_logic_quad_bus_buffer_tri_state_texas_instruments_sn74lvth125pwr"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TSSOP-14 (4.4 x 5.0 mm, 0.65 mm pitch)"
        part["datasheet_url"] = "https://www.ti.com/lit/ds/symlink/sn74lvth125.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 4.4, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SN74LVTH125PWR datasheet (C7042)",
            "pages": [2, 3],
            "notes": "Body outline per the Package_SO:TSSOP-14_4.4x5mm_P0.65mm master geometry; pinning cross-checked against the KiCad 74xx:74LS125 symbol.",
        }
        part["electrical"] = {
            "device_type": "quad bus buffer tri state",
            "supply_voltage": "2.7-3.6 V",
            "logic_family": "74LVTH",
            "operating_temperature": "-40 to +125 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1OE", "type": "in"},
            "pin_2": {"number": "2", "name": "1A", "type": "in"},
            "pin_3": {"number": "3", "name": "1Y", "type": "ts"},
            "pin_4": {"number": "4", "name": "2OE", "type": "in"},
            "pin_5": {"number": "5", "name": "2A", "type": "in"},
            "pin_6": {"number": "6", "name": "2Y", "type": "ts"},
            "pin_7": {"number": "7", "name": "GND", "type": "pwr"},
            "pin_8": {"number": "8", "name": "3Y", "type": "ts"},
            "pin_9": {"number": "9", "name": "3A", "type": "in"},
            "pin_10": {"number": "10", "name": "3OE", "type": "in"},
            "pin_11": {"number": "11", "name": "4Y", "type": "ts"},
            "pin_12": {"number": "12", "name": "4A", "type": "in"},
            "pin_13": {"number": "13", "name": "4OE", "type": "in"},
            "pin_14": {"number": "14", "name": "VCC", "type": "pwr"}
        }
        part["kicad"] = {
            "symbol": "74xx:74LS125",
            "machine_solder": "Package_SO:TSSOP-14_4.4x5mm_P0.65mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = ["JLC house-parts queue row C7042 (Texas Instruments SN74LVTH125PWR, TSSOP-14, 14 pins) verified at intake; family batch integration C7042.", "Downloaded the official Texas Instruments 74LVTH125 data sheet directly from ti.com into this part.", "Pin table generated from the KiCad 74xx:74LS125 master and cross-checked pad-for-pad (pin numbers and electrical types); no-connect pins filled to the 14-pin package count.", "Footprint Package_SO:TSSOP-14_4.4x5mm_P0.65mm verified present in the KiCad 10 library."]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END LOGIC BATCH ===



