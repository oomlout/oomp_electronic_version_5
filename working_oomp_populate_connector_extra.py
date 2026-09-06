def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_connector_usb_c_surface_mount_16_pin_shou_han_type_c_16pin_2md_073"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "SHOU HAN"
        part["part_number_manufacturer"] = "TYPE-C 16PIN 2MD(073)"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["part_number_lcsc"] = "C2765186"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2765186.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C2765186.pdf"
        part["dimensions_mm"] = {"length": 8.94, "width": 7.35, "height": 3.16}
        part["dimension_reference"] = {"document": "SHOU HAN TYPE-C 16PIN 2MD(073)", "pages": [6], "notes": "Top view with solder tails visible; shell 8.94x7.35mm, rear tails extend 0.3mm. Not a fabrication land pattern."}
        contacts = [
            ["A1", "gnd", -3.325], ["B12", "gnd", -3.075],
            ["A4", "vbus", -2.525], ["B9", "vbus", -2.275],
            ["B8", "sbu2", -1.75], ["A5", "cc1", -1.25],
            ["B7", "usb_d_minus", -.75], ["A6", "usb_d_plus", -.25],
            ["A7", "usb_d_minus", .25], ["B6", "usb_d_plus", .75],
            ["A8", "sbu1", 1.25], ["B5", "cc2", 1.75],
            ["B4", "vbus", 2.275], ["A9", "vbus", 2.525],
            ["B1", "gnd", 3.075], ["A12", "gnd", 3.325],
        ]
        part["pins"] = {}
        pads = []
        for number, name, x in contacts:
            part["pins"]["pin_" + number] = {"number": number, "name": name, "type": "power" if name in ["gnd", "vbus"] else "signal"}
            pads.append([number, "top", x, 3.825, .25, .3])
        part["pins"]["pin_S1"] = {"number": "S1", "name": "shield", "type": "passive"}
        for x in [-4.32, 4.32]:
            pads.append(["S1", "left" if x < 0 else "right", x, 3.025, .3, 1.1])
            pads.append(["S1", "left" if x < 0 else "right", x, -1.475, .3, .8])
        part["package_drawing"] = {
            "overall": [8.94, 7.95], "body": [8.94, 7.35], "pins": pads,
            "boxes": [[-1.7, 1.4, 1.0, .5], [1.7, 1.4, 1.0, .5]],
            "side": {"overall": [7.35, 3.16], "body": [7.35, 3.16], "pins": []},
        }
        part["kicad"] = {"symbol": "Connector:USB_C_Receptacle_USB2.0_16P", "machine_solder": "", "hand_solder": "", "allow_project_fallback": False}
        part["research_notes"] = ["LCSC C2765186 and the upstream USBC.pdf identify SHOU HAN, not G-Switch GT-USB-7010ASV. The original footprint is preserved; exact master/land-pattern equivalence has not been established."]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_3_pin_socket_kinghelm_kh_2_54fh_1x3p_h8_5"
    if current in extras_dict:
        extras_dict[current]["name_short"] = "Female Socket 3 Pin"
        extras_dict[current]["part_number_manufacturer"] = "KH-2.54FH-1X3P-H8.5"
        extras_dict[current]["part_number_manufacturer_kinghelm"] = "KH-2.54FH-1X3P-H8.5"
        extras_dict[current]["part_number_lcsc"] = "C2932670"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C2932670.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C2932670.pdf"
        extras_dict[current]["manufacturer"] = "Kinghelm"
        extras_dict[current]["connector_dimensions_mm"] = {
            "body_length": 7.62,
            "body_width": 2.5,
            "insulation_height": 8.5,
            "pin_pitch": 2.54,
            "pin_width": 0.64,
            "pin_thickness": 0.4,
            "recommended_hole_diameter": 1.02,
        }
        extras_dict[current]["electrical"] = {
            "current_rating": "3 A",
            "withstand_voltage": "1000 V AC",
            "contact_resistance_maximum": "20 milliohm",
            "operating_temperature": "-40 to +105 C",
        }
        extras_dict[current]["pins"] = {}
        connector_pins = [
            ["1", "pin_1"],
            ["2", "pin_2"],
            ["3", "pin_3"],
        ]
        for pin_index in range(len(connector_pins)):
            pin = connector_pins[pin_index]
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

    current = "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "TYPE-C-31-M-12"
        extras_dict[current]["part_number_lcsc"] = "C165948"
        extras_dict[current]["pins"] = {}
        usb_c_pins = [
            ["A1", "gnd", "power"],
            ["B12", "gnd", "power"],
            ["A4", "vbus", "power"],
            ["B9", "vbus", "power"],
            ["A5", "cc1", "signal"],
            ["B8", "sbu2", "signal"],
            ["A6", "dp1", "signal"],
            ["B7", "dn2", "signal"],
            ["A7", "dn1", "signal"],
            ["B6", "dp2", "signal"],
            ["A8", "sbu1", "signal"],
            ["B5", "cc2", "signal"],
            ["A9", "vbus", "power"],
            ["B4", "vbus", "power"],
            ["A12", "gnd", "power"],
            ["B1", "gnd", "power"],
        ]
        for pin_index in range(len(usb_c_pins)):
            pin = usb_c_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_connector_usb_a_surface_mount_4_pin_shenzhen_jing_tuo_jin_electronics_912121a2023s10100"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "912-121A2023S10100"
        extras_dict[current]["part_number_lcsc"] = "C42428"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "vbus",
            "number": "1",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "usb_negative",
            "number": "2",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "usb_positive",
            "number": "3",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "gnd",
            "number": "4",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "shield",
            "number": "5",
            "type": "shield",
        }
        extras_dict[current]["pins"]["pin_6"] = {
            "name": "shield",
            "number": "6",
            "type": "shield",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JST header families (SH/PH/XH and the SparkFun black Qwiic connectors):
    # shared extras come from the editable data table so pin counts, drawings
    # and KiCad masters stay in one place.
    import working_oomp_populate
    import working_oomp_populate_connector_jst_data

    datasheet_urls = {
        "eSH": "https://www.jst-mfg.com/product/pdf/eng/eSH.pdf",
        "ePH": "https://www.jst-mfg.com/product/pdf/eng/ePH.pdf",
        "eXH": "https://www.jst-mfg.com/product/pdf/eng/eXH.pdf",
    }
    for jst_part in working_oomp_populate_connector_jst_data.JST_HEADERS:
        current = working_oomp_populate.build_oomp_id(
            {"taxonomy_1": "electronic", "taxonomy_2": "connector", **jst_part["taxonomy"]}
        )
        if current not in extras_dict:
            continue
        part = extras_dict[current]
        part["manufacturer"] = "JST"
        part["part_number_manufacturer"] = jst_part["part_number_manufacturer"]
        part["part_numbers_manufacturer"] = jst_part["part_numbers_manufacturer"]
        part["name_short"] = jst_part["name_short"]
        part["part_numbers_lcsc"] = jst_part["part_numbers_lcsc"]
        if jst_part["part_number_lcsc"]:
            part["part_number_lcsc"] = jst_part["part_number_lcsc"]
            part["product_url"] = f"https://www.lcsc.com/product-detail/{jst_part['part_number_lcsc']}.html"
        elif jst_part["product_url"]:
            part["product_url"] = jst_part["product_url"]
        part["datasheet_url"] = datasheet_urls[jst_part["datasheet"]]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
        pins = {}
        for index in range(1, jst_part["pin_count"] + 1):
            pins[f"pin_{index}"] = {"number": str(index), "name": f"pin_{index}", "type": "signal"}
        part["pins"] = pins
        drawing = jst_part["package_drawing"]
        part["package_drawing"] = drawing
        part["dimensions_mm"] = {"length": drawing["body"][0], "width": drawing["body"][1]}
        footprint_name = jst_part["kicad_footprint"].split(":")[-1] or "BM15B master (BM16B extrapolated)"
        part["dimension_reference"] = {
            "document": f"KiCad Connector_JST {footprint_name} F.Fab outline",
            "pages": [],
            "notes": jst_part["note"],
        }
        part["kicad"] = {
            "symbol": jst_part["kicad_symbol"],
            "machine_solder": jst_part["kicad_footprint"],
            "hand_solder": "",
        }
        notes = [jst_part["note"]]
        if jst_part["part_number_lcsc"]:
            notes.append(
                f"LCSC {jst_part['part_number_lcsc']} lists the JST {jst_part['part_number_manufacturer']}(LF)(SN)."
            )
        if jst_part["generic_match"]:
            part["generic_match"] = jst_part["generic_match"]
            notes.append(
                "Generic match targets the SparkFun Qwiic symbols and footprints; "
                "SparkFun's Qwiic connectors are custom black-insulator JST SH headers."
            )
        part["research_notes"] = notes

    # Generic match for USB-C receptacle used in Easyduino projects
    current = "electronic_connector_usb_c_surface_mount_16_pin_shou_han_type_c_16pin_2md_073"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_match"] = {
            "values": ["USB_C_Receptacle_USB2.0", "USB_C_Receptacle"],
            "symbols": [
                "Connector:USB_C_Receptacle_USB2.0",
                "Connector:USB_C_Receptacle_USB2.0_16P",
                "SparkFun-Connector:USB_C_Receptacle",
            ],
            "footprints": [
                "Connector_USB:USB_C_Receptacle_G-Switch_GT-USB-7010ASV",
                "SparkFun-Connector:USB-C_16",
            ],
        }

    # --- LCSC stock research 2026-09: 2.54mm single-row straight pin headers, 1-40P.
    # Every pick was verified on its LCSC product page as a JLCPCB-assemblable
    # part ("JLCPCB Part Class: Extended Part") with 2.54mm pitch; preference
    # order was assembly availability, then stock. Probes and product-page
    # captures live in temp captures (kicad_agents/lcsc_capture_parser.py).

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_1_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Megastar(兆星)"
        part["part_number_manufacturer"] = "ZX-PZ2.54-1-1PZZ"
        part["part_number_lcsc"] = "C7501259"
        part["product_url"] = "https://www.lcsc.com/product-detail/C7501259.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C7501259", "product_name": "1P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C7501259.html"},
            {"part_number": "C54950614", "product_name": "3A 1x1P Black 250V 2.5mm 2.54mm 1 -25℃~+80℃ Gold Square pin 3mm 1P Thr", "url": "https://www.lcsc.com/product-detail/C54950614.html"},
            {"part_number": "C27985186", "product_name": "50+ $0.0113 $0.0118 500+ $0.0089 $0.0093 More 24,000+ $0.0061 $0.0064", "url": "https://www.lcsc.com/product-detail/C27985186.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 105740 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_2_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XFCN(兴飞)"
        part["part_number_manufacturer"] = "PZ254V-11-02P"
        part["part_number_lcsc"] = "C492401"
        part["product_url"] = "https://www.lcsc.com/product-detail/C492401.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C492401", "product_name": "2P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C492401.html"},
            {"part_number": "C7429632", "product_name": "50+ $0.0113 $0.0118 500+ $0.0094 $0.0098 More 24,000+ $0.0070 $0.0073", "url": "https://www.lcsc.com/product-detail/C7429632.html"},
            {"part_number": "C7501273", "product_name": "10+ $0.0302 $0.0317 100+ $0.0276 $0.029 More 4,000+ $0.0246 $0.0258 10", "url": "https://www.lcsc.com/product-detail/C7501273.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 1280400 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_3_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "BOOMELE(博穆精密)"
        part["part_number_manufacturer"] = "2.54-1*3P针"
        part["part_number_lcsc"] = "C49257"
        part["product_url"] = "https://www.lcsc.com/product-detail/C49257.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C49257", "product_name": "3P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C49257.html"},
            {"part_number": "C7429633", "product_name": "20+ $0.0114 $0.0119 200+ $0.0105 $0.011 More 10,000+ $0.0092 $0.0096 2", "url": "https://www.lcsc.com/product-detail/C7429633.html"},
            {"part_number": "C7429672", "product_name": "5+ $0.0663 $0.0697 50+ $0.0559 $0.0588 More 2,800+ $0.0419 $0.0441 4,9", "url": "https://www.lcsc.com/product-detail/C7429672.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 323480 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_4_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "JXTCONN(聚兴泰)"
        part["part_number_manufacturer"] = "PZ2.54-S04P-A60"
        part["part_number_lcsc"] = "C42431795"
        part["product_url"] = "https://www.lcsc.com/product-detail/C42431795.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C42431795", "product_name": "4P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C42431795.html"},
            {"part_number": "C7429634", "product_name": "Connector Header 4 position 2.5mm Pitch 3A Through Hole -25℃~+85℃", "url": "https://www.lcsc.com/product-detail/C7429634.html"},
            {"part_number": "C7429682", "product_name": "5+ $0.0838 $0.0882 50+ $0.0705 $0.0742 More 2,500+ $0.0539 $0.0567 5,0", "url": "https://www.lcsc.com/product-detail/C7429682.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 50800 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_5_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "JXTCONN(聚兴泰)"
        part["part_number_manufacturer"] = "PH2.54-1X5P-H25"
        part["part_number_lcsc"] = "C42431835"
        part["product_url"] = "https://www.lcsc.com/product-detail/C42431835.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C42431835", "product_name": "5P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C42431835.html"},
            {"part_number": "C7429635", "product_name": "20+ $0.0241 $0.0253 200+ $0.0201 $0.0211 More 10,000+ $0.0147 $0.0154", "url": "https://www.lcsc.com/product-detail/C7429635.html"},
            {"part_number": "C42391663", "product_name": "50+ $0.0167 $0.0175 500+ $0.0129 $0.0135 More 25,000+ $0.0086 $0.009 5", "url": "https://www.lcsc.com/product-detail/C42391663.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 18800 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_6_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "BOOMELE(博穆精密)"
        part["part_number_manufacturer"] = "2.54-1x6P直针"
        part["part_number_lcsc"] = "C37208"
        part["product_url"] = "https://www.lcsc.com/product-detail/C37208.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C37208", "product_name": "6P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C37208.html"},
            {"part_number": "C7429636", "product_name": "20+ $0.0269 $0.0283 200+ $0.0222 $0.0233 More 10,000+ $0.0166 $0.0174", "url": "https://www.lcsc.com/product-detail/C7429636.html"},
            {"part_number": "C3294461", "product_name": "Pin Header 6 Position 2.54mm Pitch Dual Row Surface Mount -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C3294461.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 319980 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_7_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XUNPU(讯普)"
        part["part_number_manufacturer"] = "PH2.54-01-07PZD"
        part["part_number_lcsc"] = "C7501585"
        part["product_url"] = "https://www.lcsc.com/product-detail/C7501585.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C7501585", "product_name": "7P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C7501585.html"},
            {"part_number": "C7429676", "product_name": "5+ $0.0976 $0.1027 50+ $0.0819 $0.0862 More 2,800+ $0.0635 $0.0668 4,9", "url": "https://www.lcsc.com/product-detail/C7429676.html"},
            {"part_number": "C7429637", "product_name": "10+ $0.0311 $0.0327 100+ $0.0262 $0.0275 More 5,000+ $0.0200 $0.021 10", "url": "https://www.lcsc.com/product-detail/C7429637.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 6540 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_8_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XFCN(兴飞)"
        part["part_number_manufacturer"] = "PZ254V-12-8P"
        part["part_number_lcsc"] = "C492421"
        part["product_url"] = "https://www.lcsc.com/product-detail/C492421.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C492421", "product_name": "8P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C492421.html"},
            {"part_number": "C7429638", "product_name": "10+ $0.0356 $0.0374 100+ $0.0300 $0.0315 More 5,000+ $0.0229 $0.0241 1", "url": "https://www.lcsc.com/product-detail/C7429638.html"},
            {"part_number": "C54950595", "product_name": "3A 8P 1x8P Black 250V 2.5mm 2.54mm 1 -25℃~+80℃ Gold Square pin Through", "url": "https://www.lcsc.com/product-detail/C54950595.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 141800 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_9_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "kinghelm(金航标)"
        part["part_number_manufacturer"] = "KH-2.54PH180-1X9P-L11.5"
        part["part_number_lcsc"] = "C2932701"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2932701.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2932701", "product_name": "9P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2932701.html"},
            {"part_number": "C7429639", "product_name": "10+ $0.0399 $0.0419 100+ $0.0336 $0.0353 More 5,000+ $0.0257 $0.027 10", "url": "https://www.lcsc.com/product-detail/C7429639.html"},
            {"part_number": "C7429612", "product_name": "5+ $0.1252 $0.1317 50+ $0.1038 $0.1092 More 2,800+ $0.0780 $0.0821 4,9", "url": "https://www.lcsc.com/product-detail/C7429612.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 0 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_10_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "BOOMELE(博穆精密)"
        part["part_number_manufacturer"] = "2.54-1*10P针"
        part["part_number_lcsc"] = "C57369"
        part["product_url"] = "https://www.lcsc.com/product-detail/C57369.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C57369", "product_name": "10P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C57369.html"},
            {"part_number": "C3294463", "product_name": "Pin Header 10 Position 2.54mm Pitch Dual Row Surface Mount -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C3294463.html"},
            {"part_number": "C7501596", "product_name": "Pin Header 10 Position 2.54mm Pitch Dual Row Through Hole -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C7501596.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 25400 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_11_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "HCTL(华灿天禄)"
        part["part_number_manufacturer"] = "PZ254-1-11-Z-8.5"
        part["part_number_lcsc"] = "C2894934"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2894934.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2894934", "product_name": "11P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2894934.html"},
            {"part_number": "C18197918", "product_name": "Pin Header 11 Position 2.54mm Pitch Single Row Through Hole -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C18197918.html"},
            {"part_number": "C2894953", "product_name": "Pin Header 11 Position 2.54mm Pitch Single Row Through Hole, Right Ang", "url": "https://www.lcsc.com/product-detail/C2894953.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 8925 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_12_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XUNPU(讯普)"
        part["part_number_manufacturer"] = "PH2.54-01-12PZD"
        part["part_number_lcsc"] = "C7501588"
        part["product_url"] = "https://www.lcsc.com/product-detail/C7501588.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C7501588", "product_name": "12P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C7501588.html"},
            {"part_number": "C725243", "product_name": "Pin Header 12 Position 2.54mm Pitch Single Row Through Hole, Right Ang", "url": "https://www.lcsc.com/product-detail/C725243.html"},
            {"part_number": "C7501597", "product_name": "Pin Header 12 Position 2.54mm Pitch Dual Row Through Hole -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C7501597.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 2200 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_13_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "HCTL(��灿天禄)"
        part["part_number_manufacturer"] = "PZ254-1-13-Z-8.5"
        part["part_number_lcsc"] = "C2894936"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2894936.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2894936", "product_name": "13P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2894936.html"},
            {"part_number": "C2894955", "product_name": "Pin Header 13 Position 2.54mm Pitch Single Row Through Hole, Right Ang", "url": "https://www.lcsc.com/product-detail/C2894955.html"},
            {"part_number": "C52928", "product_name": "Pin Header 13 Position 2.54mm Pitch Single Row Through Hole, Right Ang", "url": "https://www.lcsc.com/product-detail/C52928.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 3015 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_14_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "kinghelm(金航标)"
        part["part_number_manufacturer"] = "KH-2.54PH180-1X14P-L11.5"
        part["part_number_lcsc"] = "C2905490"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2905490.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2905490", "product_name": "14P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2905490.html"},
            {"part_number": "C3294465", "product_name": "Pin Header 14 Position 2.54mm Pitch Dual Row Surface Mount -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C3294465.html"},
            {"part_number": "C54803357", "product_name": "Through Hole 1kV 1 2.54mm Square pin 3A 2.5mm 6mm 3mm Gold 14P -40℃~+1", "url": "https://www.lcsc.com/product-detail/C54803357.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 3970 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_15_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XUNPU(讯普)"
        part["part_number_manufacturer"] = "PH2.54-01-15PZD"
        part["part_number_lcsc"] = "C7501589"
        part["product_url"] = "https://www.lcsc.com/product-detail/C7501589.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C7501589", "product_name": "15P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C7501589.html"},
            {"part_number": "C42372507", "product_name": "Through Hole 1kV 1 2.54mm Square pin 3A 2.5mm 6mm -40℃~+105℃ 3mm Gold", "url": "https://www.lcsc.com/product-detail/C42372507.html"},
            {"part_number": "C247916", "product_name": "Pin Header 15 Position 2.54mm Pitch Single Row Through Hole, Right Ang", "url": "https://www.lcsc.com/product-detail/C247916.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 465 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_16_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Megastar(兆星)"
        part["part_number_manufacturer"] = "ZX-PZ2.54-1-16PZZ"
        part["part_number_lcsc"] = "C7501270"
        part["product_url"] = "https://www.lcsc.com/product-detail/C7501270.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C7501270", "product_name": "16P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C7501270.html"},
            {"part_number": "C54950622", "product_name": "16P 3A 1x16P Black 250V 2.5mm 2.54mm 1 -25℃~+80℃ Gold Square pin 3mm T", "url": "https://www.lcsc.com/product-detail/C54950622.html"},
            {"part_number": "C22465876", "product_name": "6.1mm 1 16P Black 3A Square pin 3mm -40℃~+105℃ Through Hole 1x16P 2.5m", "url": "https://www.lcsc.com/product-detail/C22465876.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 392275 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_17_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Ckmtw(灿科盟)"
        part["part_number_manufacturer"] = "B-2100S17P-A110"
        part["part_number_lcsc"] = "C49423291"
        part["product_url"] = "https://www.lcsc.com/product-detail/C49423291.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C49423291", "product_name": "17P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C49423291.html"},
            {"part_number": "C22465877", "product_name": "6.1mm 1 Black 17P 3A Square pin 3mm 1x17P -40℃~+105℃ Through Hole 2.5m", "url": "https://www.lcsc.com/product-detail/C22465877.html"},
            {"part_number": "C55130795", "product_name": "1x17P 17P 6mm Right Angle 2.5mm 2.54mm 1 Gold Square pin Through Hole,", "url": "https://www.lcsc.com/product-detail/C55130795.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 705 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_18_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XFCN(兴飞)"
        part["part_number_manufacturer"] = "PZ254R-11-18P"
        part["part_number_lcsc"] = "C41413627"
        part["product_url"] = "https://www.lcsc.com/product-detail/C41413627.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C41413627", "product_name": "18P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C41413627.html"},
            {"part_number": "C3294467", "product_name": "Pin Header 18 Position 2.54mm Pitch Dual Row Surface Mount -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C3294467.html"},
            {"part_number": "C22465878", "product_name": "6.1mm 1 Black 3A 18P Square pin 3mm -40℃~+105℃ Through Hole 1x18P 2.5m", "url": "https://www.lcsc.com/product-detail/C22465878.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 1390 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_19_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "HCTL(华灿天禄)"
        part["part_number_manufacturer"] = "PZ254-1-19-Z-8.5"
        part["part_number_lcsc"] = "C2894942"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2894942.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2894942", "product_name": "19P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2894942.html"},
            {"part_number": "C247840", "product_name": "Pin Header 19 Position 2.54mm Pitch Single Row Through Hole, Right Ang", "url": "https://www.lcsc.com/product-detail/C247840.html"},
            {"part_number": "C55130799", "product_name": "1x19P 6mm Right Angle 2.5mm 2.54mm 1 19P Gold Square pin Through Hole,", "url": "https://www.lcsc.com/product-detail/C55130799.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 520 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_20_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "BOOMELE(博穆精密)"
        part["part_number_manufacturer"] = "2.54-1*20P直针"
        part["part_number_lcsc"] = "C50981"
        part["product_url"] = "https://www.lcsc.com/product-detail/C50981.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C50981", "product_name": "20P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C50981.html"},
            {"part_number": "C3294468", "product_name": "Pin Header 20 Position 2.54mm Pitch Dual Row Surface Mount -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C3294468.html"},
            {"part_number": "C7501591", "product_name": "Pin Header 20 Position 2.54mm Pitch Single Row Through Hole -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C7501591.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 50820 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_21_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "HDGC(华德共创)"
        part["part_number_manufacturer"] = "HDGCPH-PZ01-21"
        part["part_number_lcsc"] = "C19190987"
        part["product_url"] = "https://www.lcsc.com/product-detail/C19190987.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C19190987", "product_name": "21P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C19190987.html"},
            {"part_number": "C2883446", "product_name": "Pin Header 21 Position 2.54mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C2883446.html"},
            {"part_number": "C2883859", "product_name": "250V 3A 2.54mm 1x21P Square pin -40℃~+105℃ 2.5mm 2.54mm Gold Black 1 2", "url": "https://www.lcsc.com/product-detail/C2883859.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 1015 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_22_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Ckmtw(灿科盟)"
        part["part_number_manufacturer"] = "B-2100S22P-A110"
        part["part_number_lcsc"] = "C49423294"
        part["product_url"] = "https://www.lcsc.com/product-detail/C49423294.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C49423294", "product_name": "22P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C49423294.html"},
            {"part_number": "C725954", "product_name": "Pin Header 22 Position 2.54 mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C725954.html"},
            {"part_number": "C2883860", "product_name": "Pin Header 22 Position 2.54 mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C2883860.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 1940 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_23_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WR-23H-C60D30R2"
        part["part_number_lcsc"] = "C725915"
        part["product_url"] = "https://www.lcsc.com/product-detail/C725915.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C725915", "product_name": "23P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C725915.html"},
            {"part_number": "C49423295", "product_name": "1 250V 1x23P 3A 6mm Square pin 3mm -40℃~+105℃ Through Hole 23P 2.5mm 2", "url": "https://www.lcsc.com/product-detail/C49423295.html"},
            {"part_number": "C19154736", "product_name": "2.54mm 3A Through Hole Tin 23P Black 250V 1x23P 16.46mm 2.54mm 1 -35℃~", "url": "https://www.lcsc.com/product-detail/C19154736.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 952 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_24_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WR-24H-C60D30R1"
        part["part_number_lcsc"] = "C2883862"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2883862.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2883862", "product_name": "24P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2883862.html"},
            {"part_number": "C3294470", "product_name": "Pin Header 24 Position 2.54mm Pitch Dual Row Surface Mount -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C3294470.html"},
            {"part_number": "C725956", "product_name": "Pin Header 24 Position 2.54 mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C725956.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 654 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_25_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WR-25H-C60D30R2"
        part["part_number_lcsc"] = "C2883713"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2883713.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2883713", "product_name": "25P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2883713.html"},
            {"part_number": "C725957", "product_name": "Square pin 3A 250V 2.5mm 1x25P -40℃~+105℃ 2.54 mm 2.54 mm Black Gold 1", "url": "https://www.lcsc.com/product-detail/C725957.html"},
            {"part_number": "C22465883", "product_name": "25P 6.1mm 1 Black 3A Square pin 3mm -40℃~+105℃ Through Hole 2.5mm 1x25", "url": "https://www.lcsc.com/product-detail/C22465883.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 1460 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_26_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WR-26H-C60D30R2"
        part["part_number_lcsc"] = "C725918"
        part["product_url"] = "https://www.lcsc.com/product-detail/C725918.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C725918", "product_name": "26P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C725918.html"},
            {"part_number": "C49569610", "product_name": "1 Black 3A 6mm Square pin Gold 3mm Right Angle -40℃~+105℃ 600V 2.5mm 1", "url": "https://www.lcsc.com/product-detail/C49569610.html"},
            {"part_number": "C19190992", "product_name": "1 2.54 mm Black 3A 6mm Square pin Gold 3mm -40℃~+105℃ Through Hole 1x2", "url": "https://www.lcsc.com/product-detail/C19190992.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 1930 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_27_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WR-27H-C60D30R1"
        part["part_number_lcsc"] = "C2883865"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2883865.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2883865", "product_name": "27P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2883865.html"},
            {"part_number": "C725919", "product_name": "Pin Header 27 Position 2.54mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C725919.html"},
            {"part_number": "C49569573", "product_name": "1 Black 27P 3A 6mm Square pin Gold 3mm Right Angle -40℃~+105℃ 1x27P 60", "url": "https://www.lcsc.com/product-detail/C49569573.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 1118 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_28_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "WingTAT(格林柏)"
        part["part_number_manufacturer"] = "2011-1X28G00SB"
        part["part_number_lcsc"] = "C49569651"
        part["product_url"] = "https://www.lcsc.com/product-detail/C49569651.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C49569651", "product_name": "28P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C49569651.html"},
            {"part_number": "C3294472", "product_name": "Pin Header 28 Position 2.54mm Pitch Dual Row Surface Mount -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C3294472.html"},
            {"part_number": "C49569574", "product_name": "Pin Header 28 Position 2.54 mm Pitch Single Row Through Hole, Right An", "url": "https://www.lcsc.com/product-detail/C49569574.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 740 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_29_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "HDGC(华德共创)"
        part["part_number_manufacturer"] = "HDGCPH-PZ01-29"
        part["part_number_lcsc"] = "C19190995"
        part["product_url"] = "https://www.lcsc.com/product-detail/C19190995.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C19190995", "product_name": "29P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C19190995.html"},
            {"part_number": "C49569613", "product_name": "Pin Header 29 Position 2.54mm Pitch Single Row Through Hole, Right Ang", "url": "https://www.lcsc.com/product-detail/C49569613.html"},
            {"part_number": "C49569575", "product_name": "Pin Header 29 Position 2.54mm Pitch Single Row Through Hole, Right Ang", "url": "https://www.lcsc.com/product-detail/C49569575.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 490 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_30_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Amphenol"
        part["part_number_manufacturer"] = "54101-T30-00LF"
        part["part_number_lcsc"] = "C5156075"
        part["product_url"] = "https://www.lcsc.com/product-detail/C5156075.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C5156075", "product_name": "30P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C5156075.html"},
            {"part_number": "C49569576", "product_name": "Pin Header 30 Position 2.54 mm Pitch Single Row Through Hole, Right An", "url": "https://www.lcsc.com/product-detail/C49569576.html"},
            {"part_number": "C2883718", "product_name": "Pin Header 30 Position 2.54 mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C2883718.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 112560 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_31_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "WingTAT(格林柏)"
        part["part_number_manufacturer"] = "2011-1X31G00SB"
        part["part_number_lcsc"] = "C49569654"
        part["product_url"] = "https://www.lcsc.com/product-detail/C49569654.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C49569654", "product_name": "31P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C49569654.html"},
            {"part_number": "C7430387", "product_name": "1 31P -40℃~+105℃ Through Hole Black 1x31P 250V 3A 2.54mm Square pin Go", "url": "https://www.lcsc.com/product-detail/C7430387.html"},
            {"part_number": "C2883869", "product_name": "Pin Header 31 Position 2.54mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C2883869.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 195 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_32_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WV-32H-C60D30"
        part["part_number_lcsc"] = "C2883691"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2883691.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2883691", "product_name": "32P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2883691.html"},
            {"part_number": "C7501602", "product_name": "Pin Header 32 Position 2.54mm Pitch Dual Row Through Hole -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C7501602.html"},
            {"part_number": "C49569655", "product_name": "1 Black 32P 3A 6mm Square pin Gold 3mm -40℃~+105℃ Through Hole 600V 2.", "url": "https://www.lcsc.com/product-detail/C49569655.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 976 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_33_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WR-33H-C60D30R2"
        part["part_number_lcsc"] = "C2883721"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2883721.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2883721", "product_name": "33P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2883721.html"},
            {"part_number": "C7430389", "product_name": "1x33P 1 -40℃~+105℃ Through Hole Black 250V 33P 3A 2.54mm Square pin Go", "url": "https://www.lcsc.com/product-detail/C7430389.html"},
            {"part_number": "C2883790", "product_name": "1x33P -40℃~+105℃ 250V 2.5mm 3A 2.54mm 2.54mm Square pin Gold Black 1 3", "url": "https://www.lcsc.com/product-detail/C2883790.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 950 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_34_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WR-34H-C60D30R2"
        part["part_number_lcsc"] = "C2883722"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2883722.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2883722", "product_name": "34P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2883722.html"},
            {"part_number": "C2883693", "product_name": "Pin Header 34 Position 2.54 mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C2883693.html"},
            {"part_number": "C7430390", "product_name": "1 34P -40℃~+105℃ Through Hole Black 250V 3A 1x34P 2.54 mm Square pin G", "url": "https://www.lcsc.com/product-detail/C7430390.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 956 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_35_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WR-35H-C60D30R2"
        part["part_number_lcsc"] = "C2883723"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2883723.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2883723", "product_name": "35P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2883723.html"},
            {"part_number": "C2883694", "product_name": "Pin Header 35 Position 2.54mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C2883694.html"},
            {"part_number": "C2883831", "product_name": "Pin Header 35 Position 2.54mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C2883831.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 774 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_36_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WV-36H-C60D30"
        part["part_number_lcsc"] = "C2883695"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2883695.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2883695", "product_name": "36P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2883695.html"},
            {"part_number": "C2883874", "product_name": "Pin Header 36 Position 2.54 mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C2883874.html"},
            {"part_number": "C7430392", "product_name": "Pin Header 36 Position 2.54 mm Pitch Single Row Through Hole", "url": "https://www.lcsc.com/product-detail/C7430392.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 1320 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_37_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WV-37H-C60D30"
        part["part_number_lcsc"] = "C2883696"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2883696.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2883696", "product_name": "37P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2883696.html"},
            {"part_number": "C7430393", "product_name": "1x37P 1 -40℃~+105℃ Through Hole Black 250V 3A 37P 2.54mm Square pin Go", "url": "https://www.lcsc.com/product-detail/C7430393.html"},
            {"part_number": "C2883875", "product_name": "Pin Header 37 Position 2.54mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C2883875.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 928 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_38_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XKB Connection(中国星坤)"
        part["part_number_manufacturer"] = "X6511WV-38H-C60D30"
        part["part_number_lcsc"] = "C2883697"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2883697.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2883697", "product_name": "38P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2883697.html"},
            {"part_number": "C7430394", "product_name": "1 -40℃~+105℃ Through Hole Black 250V 38P 3A 2.54 mm 1x38P Square pin G", "url": "https://www.lcsc.com/product-detail/C7430394.html"},
            {"part_number": "C2883876", "product_name": "Pin Header 38 Position 2.54 mm Pitch Single Row -40℃~+105℃", "url": "https://www.lcsc.com/product-detail/C2883876.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 681 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_39_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "HDGC(华德共创)"
        part["part_number_manufacturer"] = "HDGCPH-PZ01-39"
        part["part_number_lcsc"] = "C19191005"
        part["product_url"] = "https://www.lcsc.com/product-detail/C19191005.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C19191005", "product_name": "39P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C19191005.html"},
            {"part_number": "C2883698", "product_name": "250V 3A 2.54mm Square pin 1x39P -40℃~+105℃ 2.5mm 2.54mm Gold Black 1 3", "url": "https://www.lcsc.com/product-detail/C2883698.html"},
            {"part_number": "C7430395", "product_name": "1x39P 1 -40℃~+105℃ Through Hole Black 250V 3A 2.54mm Square pin 39P Go", "url": "https://www.lcsc.com/product-detail/C7430395.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 935 in stock at capture."
        ]

    current = "electronic_connector_header_2_54_mm_pitch_through_hole_40_pin"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "BOOMELE(博穆精密)"
        part["part_number_manufacturer"] = "2.54-1*40P直针"
        part["part_number_lcsc"] = "C2337"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2337.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2337", "product_name": "40P 2.54mm single-row straight pin header (JLC assembly verified)", "url": "https://www.lcsc.com/product-detail/C2337.html"},
            {"part_number": "C2334", "product_name": "Pin Header 40 Position 2.54mm Pitch Single Row Through Hole, Right Ang", "url": "https://www.lcsc.com/product-detail/C2334.html"},
            {"part_number": "C9742", "product_name": "Pin Header 40 Position 2.54mm Pitch Single Row Through Hole -55℃~+105℃", "url": "https://www.lcsc.com/product-detail/C9742.html"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: JLCPCB-assembly verified (Extended Part), 2.54mm single-row straight, 84990 in stock at capture."
        ]
