def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})
    current = "electronic_capacitor_3216_avx_a_tantalum_22_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["part_number_manufacturer"] = "TAJA226K010RNJ"
        part["part_number_manufacturer_kyocera_avx"] = "TAJA226K010RNJ"
        part["manufacturer"] = "Kyocera AVX"
        part["part_number_lcsc"] = "C11366"
        part["product_url"] = "https://www.lcsc.com/product-detail/C11366.html"
        part["category"] = "capacitor"
        part["electrical"] = {"capacitance": "22 uF", "voltage": "10 V", "tolerance": "10%"}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "",
        }
        part["research_notes"] = [
            "LCSC verifies AVX A case 3.2 x 1.6 x 1.8 mm. The project uses a Kemet-I height-1.0 footprint; review physical height clearance.",
        ]
        part["generic_match"] = {
            "values": ["22u", "22uF", "22µF"],
            "symbols": ["Device:C_Polarized"],
            "footprints": [
                "Capacitor_Tantalum_SMD:CP_EIA-3216-10_Kemet-I",
                "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            ],
        }

    # --- LCSC stock research (browser captures parsed by kicad_agents/lcsc_capture_parser.py) ---

    current = "electronic_capacitor_0402_100_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "CC0402KRX7R7BB104"
        part["part_number_lcsc"] = "C60474"
        part["product_url"] = "https://www.lcsc.com/product-detail/C60474.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C60474", "product_name": "100nF ±10% 16V Ceramic Capacitor X7R 0402"},
            {"part_number": "C1525", "product_name": "100nF ±10% 16V X7R 0402 Ceramic Capacitor"},
            {"part_number": "C131394", "product_name": "100nF ±10% 50V Ceramic Capacitor X7R 0402"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "CC0402KRX7R7BB104"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL05B104KO5NNNC"},
            {"manufacturer": "YAGEO", "part_number": "CC0402KRX7R9BB104"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C60474, 14,596,000 in stock at capture); runners-up follow."
        ]
        from working_oomp_populate_jlc import set_preferred_jlc
        set_preferred_jlc(
            part,
            code="C1525",
            manufacturer="Samsung Electro-Mechanics",
            mpn="CL05B104KO5NNNC",
            selection={'verified_on': '2026-09-24',
         'official_url': 'https://jlcpcb.com/partdetail/1877-CL05B104KO5NNNC/C1525',
         'tier': 'basic',
         'tier_label_observed': 'Basic',
         'stock_observed': 24770247,
         'purchase_moq_observed': 1,
         'pcba_min_qty_observed': None,
         'compatibility_notes': 'Existing generic 0402 100 nF capacitor. Samsung C1525 is a 16 V X7R '
                                '+/-10% 0402 MLCC, matching the recorded value/package and the former '
                                'YAGEO C60474 option. Preference is a purchasing choice; preserve '
                                'C60474 and other alternatives. DC-bias performance and '
                                'project-specific voltage margin remain for the full pass.',
         'ratings': {'Capacitance': '100 nF (code 104)',
                     'Tolerance': '+-10% (code K)',
                     'Rated voltage': '16 Vdc (code O)',
                     'Dielectric': 'X7R (Class II)',
                     'Temperature range': '-55 C to +125 C',
                     'Temperature characteristic': '+-15% over the operating range',
                     'Thickness maximum': '0.55 mm',
                     'Polarization': 'none',
                     'DC bias note': 'Class II capacitance derates with applied DC voltage; no DC-bias '
                                     'curve in the catalogue'},
         'datasheet_pages': {'document': 'Samsung MLCC catalogue (C1525 import)',
                             'ordering_coverage': [65],
                             'product_dimensions': [65],
                             'packaging_specification': [74, 78]},
         'pinout_checked': True,
         'footprint_checked': True,
         'visual_review': 'Inspected 2026-09-26 after the build. data/working_svg_square_pins.png '
                          'hero: Capacitor 100 nF 0402 with terminals labelled pin 1 / pin 2, '
                          'silkscreen code and bip-39 words legible; assembly and pin views use the '
                          'standard 0402 chip renderer with end metallization, no overlap or cropping. '
                          'data/kicad manifest complete: Device:C_Small symbol, C_0402_1005Metric '
                          'machine master, C_0402_1005Metric_Pad0.74x0.62mm_HandSolder hand master. '
                          'README.md: 100 nF value, C1525 links, pin table, datasheet link to '
                          'data/datasheet.pdf. Limitation: KiCad assets checked as s-expression text '
                          'rather than rendered in a KiCad GUI.'},
        )

    # JLC C1525 / Samsung CL05B104KO5NNNC full-stage technical data, verified
    # against the Samsung MLCC catalogue saved for this part: X7R 0402 lineup
    # row CL05B104KO5NNN (page 65) = 0402, 100 nF, 16 Vdc, +-10%, 0.55 mm max
    # thickness; the NNC packaging variant is the datasheet's own packaging
    # code section applied to that electrical row. Dimensions page 65
    # (1.00 x 0.50 mm) and the part numbering/packaging sections.
    current = "electronic_capacitor_0402_100_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0402 (1005 metric), 0.55 mm max thickness"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707269992677376-C1525.pdf"
        part["electrical"] = {
            "capacitance": "100 nF (104)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "16 Vdc (code O)",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "thickness_maximum": "0.55 mm",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.55}
        part["dimension_reference"] = {
            "document": "Samsung MLCC catalogue, Product Lineup Standard & High Capacitors X7R",
            "pages": [65],
            "notes": "0402 size 1.00 x 0.50 mm with 0.55 mm maximum thickness for the CL05B104KO5 row; the NNC packaging suffix is a packing variant of that electrical row.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = part.get("research_notes", []) + [
            "Full pass 2026-09-26: the saved Samsung catalogue X7R 0402 lineup covers the CL05B104KO5 electrical row exactly (100 nF, 16 Vdc, +-10%, 0.55 mm max); NNC is a packaging variant per the catalogue's packaging specification.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1530 / Fenghua 0402B221K500NT. The shared Fenghua family PDF
    # decodes the ordering code (0402 / X7R / 221 = 220 pF / K / 500 = 50 V)
    # and gives the 0402 dimensions, but its X7R 0402 table starts at 330 pF,
    # so the 221 row is NOT covered by this document revision. The full-stage
    # ordering-coverage check therefore defers; the physical data below is the
    # verified series-generic information. See the record for the remaining
    # task (current Fenghua 0402 X7R datasheet with the 221 row).
    current = "electronic_capacitor_0402_220_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987688294137856-C1530.pdf"
        part["electrical"] = {
            "capacitance": "220 pF (221)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II) per the ordering code and the JLC listing",
            "temperature_range": "-55 to +125 C (X7R class definition)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (shared Fenghua 0402 family PDF)",
            "pages": [5],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0402B221K500NT (C1530): 220 pF, 50 V, X7R, +-10% in 0402.",
            "The ordering code decodes exactly, but the saved Fenghua family PDF's X7R 0402 table starts at 330 pF, so the 221 row is not covered by that document revision.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_capacitor_0402_22_nano_farad"
    if current in extras_dict:
        from working_oomp_populate_jlc import set_preferred_jlc
        set_preferred_jlc(
            extras_dict[current],
            code="C1532",
            manufacturer="FH (Guangdong Fenghua Advanced Tech)",
            mpn="0402B223K500NT",
            selection={'verified_on': '2026-09-24',
         'official_url': 'https://jlcpcb.com/partdetail/1884-0402B223K500NT/C1532',
         'tier': 'basic',
         'tier_label_observed': 'Basic',
         'stock_observed': 631889,
         'purchase_moq_observed': 1,
         'pcba_min_qty_observed': None,
         'compatibility_notes': 'Existing generic 0402 22 nF capacitor. FH C1532 is 50 V X7R +/-10%, '
                                'while previous YAGEO C107017 is listed as 16 V X7R +/-10%; C1532 '
                                'meets the prior voltage rating. Preserve C107017. DC-bias behavior '
                                'and project-specific margins remain for full review.',
         'ratings': {'Capacitance': '22 nF (code 223)',
                     'Tolerance': '+-10% (code K)',
                     'Rated voltage': '50 V (code 500)',
                     'Dielectric': 'X7R (Class II)',
                     'Temperature range': '-55 C to +125 C',
                     'Temperature characteristic': '+-15% over the operating range',
                     'Thickness': '0.50 +-0.05 mm (CA code)',
                     'Polarization': 'none'},
         'datasheet_pages': {'document': 'Fenghua General Series MLCC specification (shared Fenghua '
                                         'family PDF)',
                             'ordering_coverage': [4],
                             'capacitance_voltage_coverage': [9],
                             'product_dimensions': [5],
                             'temperature_characteristics': [5]},
         'pinout_checked': True,
         'footprint_checked': True,
         'visual_review': 'Inspected 2026-09-26 after the build. data/working_svg_square_pins.png '
                          'hero: Capacitor 22 nF 0402 with terminals labelled pin 1 / pin 2, '
                          'silkscreen code and bip-39 words legible; assembly and pin views use the '
                          'standard 0402 chip renderer, no overlap or cropping. data/kicad manifest '
                          'complete: Device:C_Small symbol, C_0402_1005Metric machine master, '
                          'C_0402_1005Metric_Pad0.74x0.62mm_HandSolder hand master. README.md: 22 nF '
                          'value, C1532 links, pin table, datasheet link to data/datasheet.pdf. '
                          'Limitation: KiCad assets checked as s-expression text rather than rendered '
                          'in a KiCad GUI.'},
        )

    # JLC C1532 / Fenghua 0402B223K500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification: ordering
    # code page 4 decodes 0402 / X7R / 223 = 22 nF / K = +-10% / 500 = 50 V;
    # the X7R 0402 table (page 9) lists 22 nF with the CA thickness code at
    # every voltage including 50 V. Dimensions page 5 (0402 CA).
    part = extras_dict.get("electronic_capacitor_0402_22_nano_farad")
    if part is not None:
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987688294137856-C1530.pdf"
        part["electrical"] = {
            "capacitance": "22 nF (223)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (shared Fenghua 0402 family PDF)",
            "pages": [5, 9],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm. X7R 0402 table lists 22 nF at 50 V (page 9).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0402B223K500NT (C1532): 22 nF, 50 V, X7R, +-10% in 0402.",
            "The shared Fenghua family PDF's X7R 0402 table (page 9) covers 22 nF at 50 V with the CA thickness code.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": "parts_source/electronic_capacitor_0402_22_nano_farad/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1538 / Fenghua 0402B472K500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # ordering code page 4 decodes 0402 / X7R / 472 = 4.7 nF / K = +-10% /
    # 500 = 50 V; the X7R 0402 table (page 9) lists 4.7 nF with the CA
    # thickness code at every voltage including 50 V. Dimensions page 5.
    current = "electronic_capacitor_0402_4_7_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987717859651584-C1538.pdf"
        part["electrical"] = {
            "capacitance": "4.7 nF (472)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (shared Fenghua 0402 family PDF)",
            "pages": [5, 9],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm. X7R 0402 table lists 4.7 nF at 50 V (page 9).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0402B472K500NT (C1538): 4.7 nF, 50 V, X7R, +-10% in 0402.",
            "The shared Fenghua family PDF's X7R 0402 table (page 9) covers 4.7 nF at 50 V with the CA thickness code.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": "parts_source/electronic_capacitor_0402_100_pico_farad/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_capacitor_0402_10_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Samsung Electro-Mechanics"
        part["part_number_manufacturer"] = "CL05A106MQ5NUNC"
        part["part_number_lcsc"] = "C15525"
        part["product_url"] = "https://www.lcsc.com/product-detail/C15525.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C15525", "product_name": "10uF ±20% 6.3V Ceramic Capacitor X5R 0402"},
            {"part_number": "C7472949", "product_name": "10uF ±20% 10V Ceramic Capacitor X5R 0402"},
            {"part_number": "C48543727", "product_name": "10uF X5R ±20% 6.3V 0402 Ceramic Capacitors"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL05A106MQ5NUNC"},
            {"manufacturer": "Chinocera", "part_number": "HGC0402R5106M100NTEJ"},
            {"manufacturer": "CCTC", "part_number": "TCC0402X5R106M6R3ATR"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C15525, 6,000,000 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0402_15_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "CC0402JRNPO9BN150"
        part["part_number_lcsc"] = "C106997"
        part["product_url"] = "https://www.lcsc.com/product-detail/C106997.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C106997", "product_name": "15pF ±5% 50V Ceramic Capacitor NP0 0402"},
            {"part_number": "C1548", "product_name": "15pF ±5% 50V Ceramic Capacitor C0G 0402"},
            {"part_number": "C326803", "product_name": "15pF ±1% 50V Ceramic Capacitor NP0 0402"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "CC0402JRNPO9BN150"},
            {"manufacturer": "FH", "part_number": "0402CG150J500NT"},
            {"manufacturer": "YAGEO", "part_number": "CC0402FRNPO9BN150"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C106997, 2,467,600 in stock at capture); runners-up follow.",
            "The official JLC page lists Basic Fenghua 0402CG150J500NT (C1548): 15 pF, 50 V, C0G, +-5% in 0402; reconfirmed live 2026-10-01.",
            "The Fenghua ordering code decodes exactly to that suffix (CG = C0G, 150 = 15 pF, J = +-5%, 500 = 50 V), and the C0G 0402 table covers 15 pF at 50 V (page 6).",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987753502846976-C1548.pdf"
        part["electrical"] = {
            "capacitance": "15 pF (150)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0+-30 ppm/C referenced to 25 C (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1548)",
            "pages": [4, 5, 6],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm. C0G 0402 table lists 15 pF at 50 V with the CA thickness code (page 6).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
        from working_oomp_populate_jlc import set_preferred_jlc
        set_preferred_jlc(
            part,
            code="C1548",
            manufacturer="FH (Guangdong Fenghua Advanced Tech)",
            mpn="0402CG150J500NT",
            selection={
                "verified_on": "2026-10-01",
                "official_url": "https://jlcpcb.com/partdetail/1900-0402CG150J500NT/C1548",
                "tier": "basic",
                "tier_label_observed": "Basic",
                "stock_observed": 1465932,
                "purchase_moq_observed": 1,
                "pcba_min_qty_observed": None,
                "compatibility_notes": "Existing generic 0402 15 pF capacitor. FH C1548 is 50 V C0G +/-5%; prior YAGEO C106997 is recorded as 50 V NP0 +/-5%. C0G/NP0 are the same Class I temperature characteristic. Preserve C106997 and other alternatives; project RF/Q requirements need full review. Full-pass datasheet evidence confirms the identity and ratings.",
                "ratings": {
                    "capacitance": "15 pF",
                    "rated_voltage": "50 V",
                    "dielectric": "C0G",
                    "tolerance": "+/-5%",
                },
                "datasheet_pages": {
                    "document": "Fenghua General Series MLCC specification (shared, C1548 provenance)",
                    "ordering_coverage": [4],
                    "dimensions": [5, 6],
                    "electrical_characteristics": [6],
                },
                "pinout_checked": True,
                "footprint_checked": True,
                "visual_review": "Inspected 2026-10-01 after the build and a forced diagram refresh. data/working_svg_square_pins.png hero titled Capacitor 15 pF 0402 with terminals 1 left and 2 right, non-polarized symmetric body, no mirroring, no label overlap, no cropping. working_svg_dimensioned.png: 1.0 x 0.5 mm body with arrows, matching the Fenghua 0402/1005 CA nominals. data/kicad manifest complete with Device:C_Small symbol and Capacitor_SMD:C_0402_1005Metric machine + Pad0.74x0.62mm_HandSolder hand footprints. README.md: 0402CG150J500NT part number, LCSC/JLC C1548 links, pin table, datasheet link resolving to data/datasheet.pdf (the shared Fenghua General Series MLCC specification, 3.2 MB). Limitation: KiCad symbol/footprint checked as rendered SVG/PNG plus s-expression text rather than in a KiCad GUI.",
            },
        )

    current = "electronic_capacitor_0402_18_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "CC0402JRNPO9BN180"
        part["part_number_lcsc"] = "C106202"
        part["product_url"] = "https://www.lcsc.com/product-detail/C106202.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C106202", "product_name": "18pF ±5% 50V Ceramic Capacitor NP0 0402"},
            {"part_number": "C7393840", "product_name": "18pF ±10% 50V Ceramic Capacitor C0G 0402"},
            {"part_number": "C1549", "product_name": "18pF ±5% 50V Ceramic Capacitor C0G 0402"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "CC0402JRNPO9BN180"},
            {"manufacturer": "CCTC", "part_number": "TCC0402COG180K500AT"},
            {"manufacturer": "FH", "part_number": "0402CG180J500NT"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C106202, 2,093,000 in stock at capture); runners-up follow.",
            "The official JLC page lists Basic Fenghua 0402CG180J500NT (C1549): 18 pF, 50 V, C0G, +-5% in 0402; reconfirmed live 2026-10-01.",
            "The Fenghua ordering code decodes exactly to that suffix (CG = C0G, 180 = 18 pF, J = +-5%, 500 = 50 V), and the C0G 0402 table covers 18 pF at 50 V (page 6).",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987757659807744-C1549.pdf"
        part["electrical"] = {
            "capacitance": "18 pF (180)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0+-30 ppm/C referenced to 25 C (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1549)",
            "pages": [4, 5, 6],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm. C0G 0402 table lists 18 pF at 50 V with the CA thickness code (page 6).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
        from working_oomp_populate_jlc import set_preferred_jlc
        set_preferred_jlc(
            part,
            code="C1549",
            manufacturer="FH (Guangdong Fenghua Advanced Tech)",
            mpn="0402CG180J500NT",
            selection={
                "verified_on": "2026-10-01",
                "official_url": "https://jlcpcb.com/partdetail/1901-0402CG180J500NT/C1549",
                "tier": "basic",
                "tier_label_observed": "Basic",
                "stock_observed": 727917,
                "purchase_moq_observed": 1,
                "pcba_min_qty_observed": None,
                "compatibility_notes": "Existing generic 0402 18 pF capacitor. FH C1549 is 50 V C0G +/-5%; previous YAGEO C106202 is 50 V NP0 +/-5%. C0G/NP0 are the same Class I temperature characteristic. Preserve C106202 and other alternatives; project-specific RF/Q requirements need full review. Full-pass datasheet evidence confirms the identity and ratings.",
                "ratings": {
                    "capacitance": "18 pF",
                    "rated_voltage": "50 V",
                    "dielectric": "C0G",
                    "tolerance": "+/-5%",
                },
                "datasheet_pages": {
                    "document": "Fenghua General Series MLCC specification (shared, C1549 provenance)",
                    "ordering_coverage": [4],
                    "dimensions": [5, 6],
                    "electrical_characteristics": [6],
                },
                "pinout_checked": True,
                "footprint_checked": True,
                "visual_review": "Inspected 2026-10-01 after the build and a forced diagram refresh. data/working_svg_square_pins.png hero titled Capacitor 18 pF 0402 with terminals 1 left and 2 right, non-polarized symmetric body, no mirroring, no label overlap, no cropping. working_svg_dimensioned.png: 1.0 x 0.5 mm body with arrows, matching the Fenghua 0402/1005 CA nominals. data/kicad manifest complete with Device:C_Small symbol and Capacitor_SMD:C_0402_1005Metric machine + Pad0.74x0.62mm_HandSolder hand footprints. README.md: 0402CG180J500NT part number, LCSC/JLC C1549 links, pin table, datasheet link resolving to data/datasheet.pdf (the shared Fenghua General Series MLCC specification, 3.2 MB). Limitation: KiCad symbol/footprint checked as rendered SVG/PNG plus s-expression text rather than in a KiCad GUI.",
            },
        )

    current = "electronic_capacitor_0402_1_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["manufacturer"] = "CCTC"
        part["part_number_manufacturer"] = "TCC0402X5R105M6R3AT"
        part["part_number_lcsc"] = "C2887021"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2887021.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2887021", "product_name": "1uF ±20% 6.3V Ceramic Capacitor X5R 0402"},
            {"part_number": "C52923", "product_name": "1uF ±10% 25V Ceramic Capacitor X5R 0402"},
            {"part_number": "C29266", "product_name": "1uF ±10% 16V Ceramic Capacitor X5R 0402"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "CCTC", "part_number": "TCC0402X5R105M6R3AT"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL05A105KA5NQNC"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL05A105KO5NNNC"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C2887021, 5,124,350 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0402_22_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "CC0402JRNPO9BN220"
        part["part_number_lcsc"] = "C106203"
        part["product_url"] = "https://www.lcsc.com/product-detail/C106203.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C106203", "product_name": "22pF ±5% 50V Ceramic Capacitor NP0 0402"},
            {"part_number": "C1555", "product_name": "22pF ±5% 50V Ceramic Capacitor C0G 0402"},
            {"part_number": "C696857", "product_name": "22pF ±5% 50V Ceramic Capacitor C0G 0402"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "CC0402JRNPO9BN220"},
            {"manufacturer": "FH", "part_number": "0402CG220J500NT"},
            {"manufacturer": "CCTC", "part_number": "TCC0402COG220J500AT"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C106203, 2,991,500 in stock at capture); runners-up follow.",
            "The official JLC page lists Basic Fenghua 0402CG220J500NT (C1555): 22 pF, 50 V, C0G, +-5% in 0402; reconfirmed live 2026-10-01.",
            "The Fenghua ordering code decodes exactly to that suffix (CG = C0G, 220 = 22 pF, J = +-5%, 500 = 50 V), and the C0G 0402 table covers 22 pF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
            "The official JLC page lists Basic Fenghua 0402CG220J500NT (C1555): 22 pF, 50 V, C0G, +-5% in 0402; reconfirmed live 2026-10-01.",
            "The Fenghua ordering code decodes exactly to that suffix (CG = C0G, 220 = 22 pF, J = +-5%, 500 = 50 V), and the C0G 0402 table covers 22 pF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]

        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987777901113344-C1555.pdf"
        part["electrical"] = {
            "capacitance": "22 pF (220)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0+-30 ppm/C referenced to 25 C (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1555)",
            "pages": [4, 5, 6],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm. C0G 0402 table lists 22 pF at 50 V with the CA thickness code (page 6).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_capacitor_0402_27_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "CC0402JRNPO9BN270"
        part["part_number_lcsc"] = "C107002"
        part["product_url"] = "https://www.lcsc.com/product-detail/C107002.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C107002", "product_name": "27pF ±5% 50V Ceramic Capacitor NP0 0402"},
            {"part_number": "C466227", "product_name": "27pF ±5% 50V Ceramic Capacitor C0G 0402"},
            {"part_number": "C1557", "product_name": "27pF ±5% 50V Ceramic Capacitor C0G 0402"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "CC0402JRNPO9BN270"},
            {"manufacturer": "CCTC", "part_number": "TCC0402C0G270J500AT"},
            {"manufacturer": "FH", "part_number": "0402CG270J500NT"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C107002, 1,683,800 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0402_2_2_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["manufacturer"] = "Samsung Electro-Mechanics"
        part["part_number_manufacturer"] = "CL05A225MQ5NSNC"
        part["part_number_lcsc"] = "C12530"
        part["product_url"] = "https://www.lcsc.com/product-detail/C12530.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C12530", "product_name": "2.2uF ±20% 6.3V Ceramic Capacitor X5R 0402"},
            {"part_number": "C20539421", "product_name": "2.2uF ±10% 10V Ceramic Capacitor X5R 0402"},
            {"part_number": "C326606", "product_name": "2.2uF ±10% 10V Ceramic Capacitor X5R 0402"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL05A225MQ5NSNC"},
            {"manufacturer": "CCTC", "part_number": "TCC0402X5R225K100AT"},
            {"manufacturer": "YAGEO", "part_number": "CC0402KRX5R6BB225"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C12530, 5,163,000 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0402_4_7_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Samsung Electro-Mechanics"
        part["part_number_manufacturer"] = "CL05A475KP5NRNC"
        part["part_number_lcsc"] = "C368809"
        part["product_url"] = "https://www.lcsc.com/product-detail/C368809.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C368809", "product_name": "4.7uF ±10% 10V Ceramic Capacitor X5R 0402"},
            {"part_number": "C318563", "product_name": "4.7uF ±20% 16V Ceramic Capacitor X5R 0402"},
            {"part_number": "C23733", "product_name": "4.7uF ±20% 10V Ceramic Capacitor X5R 0402"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL05A475KP5NRNC"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL05A475MO5NUNC"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL05A475MP5NRNC"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C368809, 1,616,950 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0603_100_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "CC0603KRX7R9BB104"
        part["part_number_lcsc"] = "C14663"
        part["product_url"] = "https://www.lcsc.com/product-detail/C14663.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C14663", "product_name": "100nF ±10% 50V X7R 0603 Ceramic Capacitor"},
            {"part_number": "C30926", "product_name": "100nF ±10% 50V Ceramic Capacitor X7R 0603"},
            {"part_number": "C1591", "product_name": "100nF ±10% 50V X7R 0603 Ceramic Capacitor"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "CC0603KRX7R9BB104"},
            {"manufacturer": "FH", "part_number": "0603B104K500NT"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10B104KB8NNNC"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C14663, 10,855,500 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0603_100_nano_farad_samsung_electro_mechanics_cl10b104kb8nnnc"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["generic_oomp_id"] = "electronic_capacitor_0603_100_nano_farad"
        part["category"] = "capacitor"
        part["manufacturer"] = "Samsung Electro-Mechanics"
        part["part_number_manufacturer"] = "CL10B104KB8NNNC"
        part["part_number_lcsc"] = "C1591"
        part["part_number_lcsc_url"] = "https://www.lcsc.com/product-detail/C1591.html"
        part["part_number_jlcpcb"] = "C1591"
        part["part_number_jlcpcb_url"] = "https://jlcpcb.com/partdetail/1943-CL10B104KB8NNNC/C1591"
        part["electrical"] = {
            "capacitance": "100 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "+/-10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung C1591 / CL10B104KB8NNNC purchasing variant; 0603, 100 nF, 50 V, X7R, +/-10% verified against the live JLC listing and Samsung MLCC catalog page 26.",
            "Linked to the generic 0603 100 nF definition. The previously reviewed generic preference C14663 remains unchanged.",
            "The supplier catalogue shows the corresponding CL10B104KB8NNN base family code; the final C suffix is the JLC/LCSC orderable identity.",
        ]

    current = "electronic_capacitor_0603_10_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["manufacturer"] = "Samsung Electro-Mechanics"
        part["part_number_manufacturer"] = "CL10A106KP8NNNC"
        part["part_number_lcsc"] = "C19702"
        part["product_url"] = "https://www.lcsc.com/product-detail/C19702.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C19702", "product_name": "10uF ±10% 10V Ceramic Capacitor X5R 0603"},
            {"part_number": "C96446", "product_name": "10uF ±20% 25V Ceramic Capacitor X5R 0603"},
            {"part_number": "C92487", "product_name": "10uF ±20% 16V Ceramic Capacitor X5R 0603"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10A106KP8NNNC"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10A106MA8NRNC"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10A106MO8NQNC"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C19702, 7,061,560 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0603_1_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["manufacturer"] = "Samsung Electro-Mechanics"
        part["part_number_manufacturer"] = "CL10A105KA8NNNC"
        part["part_number_lcsc"] = "C5673"
        part["product_url"] = "https://www.lcsc.com/product-detail/C5673.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C5673", "product_name": "1uF ±10% 25V Ceramic Capacitor X5R 0603"},
            {"part_number": "C1592", "product_name": "1uF ±10% 16V Ceramic Capacitor X5R 0603"},
            {"part_number": "C5199872", "product_name": "1uF ±10% 50V Ceramic Capacitor X7R 0603"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10A105KA8NNNC"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10A105KO8NNNC"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10B105KB8NQNC"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C5673, 4,609,150 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0603_1_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_1_micro_farad"
        part["category"] = "capacitor"
        part["manufacturer"] = "Samsung Electro-Mechanics"
        part["part_number_manufacturer"] = "CL10A105KO8NNNC"
        part["part_number_lcsc"] = "C1592"
        part["part_number_lcsc_url"] = "https://www.lcsc.com/product-detail/C1592.html"
        part["part_number_jlcpcb"] = "C1592"
        part["part_number_jlcpcb_url"] = "https://jlcpcb.com/partdetail/1944-CL10A105KO8NNNC/C1592"
        part["electrical"] = {
            "capacitance": "1 uF",
            "rated_voltage": "16 V",
            "dielectric": "X5R",
            "tolerance": "+/-10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "C1592 is Samsung CL10A105KO8NNNC, 0603 1 uF 16 V X5R +/-10%, verified against the live JLC and LCSC listings and the linked Samsung reference sheet page 1.",
            "Linked to the generic 0603 1 uF definition as a lower-voltage purchasing variant; the reviewed Basic 50 V C15849 generic preference remains unchanged.",
        ]

    current = "electronic_capacitor_0603_22_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "CC0603JRNPO9BN220"
        part["part_number_lcsc"] = "C105620"
        part["product_url"] = "https://www.lcsc.com/product-detail/C105620.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C105620", "product_name": "22pF ±5% 50V Ceramic Capacitor NP0 0603"},
            {"part_number": "C1653", "product_name": "22pF ±5% 50V Ceramic Capacitor C0G 0603"},
            {"part_number": "C7419421", "product_name": "22pF ±5% 50V Ceramic Capacitor C0G 0603"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "CC0603JRNPO9BN220"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10C220JB8NNNC"},
            {"manufacturer": "FOJAN", "part_number": "FCC0603N220J500CT"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C105620, 3,445,550 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0603_2_2_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["manufacturer"] = "Samsung Electro-Mechanics"
        part["part_number_manufacturer"] = "CL10A225KO8NNNC"
        part["part_number_lcsc"] = "C23630"
        part["product_url"] = "https://www.lcsc.com/product-detail/C23630.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C23630", "product_name": "2.2uF ±10% 16V Ceramic Capacitor X5R 0603"},
            {"part_number": "C57895", "product_name": "2.2uF ±10% 25V Ceramic Capacitor X5R 0603"},
            {"part_number": "C913904", "product_name": "2.2uF ±10% 50V Ceramic Capacitor X5R 0603"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10A225KO8NNNC"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10A225KA8NNNC"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10A225KB8NNNC"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C23630, 2,092,650 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0603_47_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "CC0603JRNPO9BN470"
        part["part_number_lcsc"] = "C105622"
        part["product_url"] = "https://www.lcsc.com/product-detail/C105622.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C105622", "product_name": "47pF ±5% 50V Ceramic Capacitor NP0 0603"},
            {"part_number": "C1671", "product_name": "47pF ±5% 50V Ceramic Capacitor C0G 0603"},
            {"part_number": "C94904", "product_name": "47pF ±5% 50V Ceramic Capacitor C0G 0603"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "CC0603JRNPO9BN470"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10C470JB8NNNC"},
            {"manufacturer": "FH", "part_number": "0603CG470J500NT"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C105622, 1,590,800 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_1206_47_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["manufacturer"] = "Samsung Electro-Mechanics"
        part["part_number_manufacturer"] = "CL31A476MQHNNNE"
        part["part_number_lcsc"] = "C68361"
        part["product_url"] = "https://www.lcsc.com/product-detail/C68361.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C68361", "product_name": "47uF ±20% 6.3V Ceramic Capacitor X5R 1206"},
            {"part_number": "C96123", "product_name": "47uF ±20% 10V Ceramic Capacitor X5R 1206"},
            {"part_number": "C5448950", "product_name": "47uF ±20% 10V Ceramic Capacitor X5R 1206"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL31A476MQHNNNE"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL31A476MPHNNNE"},
            {"manufacturer": "CCTC", "part_number": "TCC1206X5R476M100HT"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C68361, 921,810 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0402_100_nano_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["generic_oomp_id"] = "electronic_capacitor_0402_100_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "100 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "+/-10%",
        }
        part["research_notes"] = [
            "Rated 50 V purchasing variant. The generic 0402 100 nF choice retains its 16 V Samsung C1525 preference.",
            "DC-bias performance and project-specific voltage margin remain for the full pass.",
        ]

    current = "electronic_capacitor_0402_4_7_micro_farad_10_volt_20_percent"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["generic_oomp_id"] = "electronic_capacitor_0402_4_7_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "10 V",
            "dielectric": "X5R",
            "tolerance": "+/-20%",
        }
        part["research_notes"] = [
            "Rated/tolerance variant. The generic 0402 4.7 uF choice retains its +/-10% Samsung C368809 preference.",
            "Effective capacitance under DC bias must be verified for each project in the full pass.",
        ]

    current = "electronic_capacitor_0603_4_7_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["generic_oomp_id"] = "electronic_capacitor_0603_4_7_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "16 V",
            "dielectric": "X5R",
            "tolerance": "+/-10%",
        }
        part["research_notes"] = [
            "Rated 16 V purchasing variant. The generic 0603 4.7 uF choice retains its 25 V Samsung C69335 preference.",
            "Effective capacitance under DC bias must be verified for each project in the full pass.",
        ]

    current = "electronic_capacitor_0603_10_micro_farad_25_volt_20_percent"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["generic_oomp_id"] = "electronic_capacitor_0603_10_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "25 V",
            "dielectric": "X5R",
            "tolerance": "+/-20%",
        }
        part["research_notes"] = [
            "Rated/tolerance variant. The generic 0603 10 uF choice retains its +/-10% Samsung C19702 preference.",
            "Effective capacitance under DC bias must be verified for each project in the full pass.",
        ]

    current = "electronic_capacitor_0805_10_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_10_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "50 V",
            "dielectric": "X5R",
            "tolerance": "+/-10%",
        }
        part["research_notes"] = [
            "Rated 50 V purchasing variant. The generic 0805 10 uF choice retains its 25 V Samsung C15850 preference.",
            "Effective capacitance under DC bias needs project-specific full review.",
        ]

    # JLC C1523 / Fenghua 0402B102K500NT, verified against the Fenghua General
    # Series MLCC specification (shared datasheet with the 0402 10 pF entry):
    # ordering code page 4 decodes 0402 / X7R / 102 = 1 nF / K = +-10% / 500 =
    # 50 V; the X7R 0402 table lists 1 nF at 50 V; dimensions page 5 give the
    # 0402 (1005 metric, CA) body 1.00+-0.05 x 0.50+-0.05, T 0.50+-0.05,
    # terminal WB 0.25+-0.05; X7R temperature characteristic -55 to +125 C
    # (page 5). Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0402_1_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987669373767680-C1523.pdf"
        part["electrical"] = {
            "capacitance": "1 nF (102)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
            "capacitance_measurement": "1 kHz +-10% at 1.0 +-0.2 Vrms for C <= 10 uF (Class II)",
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (shared Fenghua 0402 family PDF)",
            "pages": [5, 9],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal width WB 0.25+-0.05 mm. X7R 0402 table lists 1 nF at 50 V (page 9).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0402B102K500NT (C1523): 1 nF, 50 V, X7R, +-10% in 0402.",
            "The Fenghua ordering code decodes exactly to that suffix, and the X7R 0402 capacitance/voltage table covers 1 nF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions above.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_capacitor_0402_100_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987747089891328-C1546.pdf"
        part["electrical"] = {
            "capacitance": "100 pF (101)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0+-30 ppm/C referenced to 25 C (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1546)",
            "pages": [4, 5, 6],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm. C0G 0402 table lists 100 pF at 50 V with the CA thickness code (page 6).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0402CG101J500NT (C1546): 100 pF, 50 V, C0G, +-5% in 0402.",
            "The Fenghua ordering code decodes exactly to that suffix (CG = C0G, 101 = 100 pF, J = +-5%, 500 = 50 V), and the C0G 0402 table covers 100 pF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1547 / Fenghua 0402CG120J500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # ordering code page 4 decodes 0402 / CG = C0G / 120 = 12 pF /
    # J = +-5% / 500 = 50 V / N nickel barrier / T 7-inch reel; the C0G 0402
    # capacitance table (page 6) lists 12 pF at 25 V and 50 V with
    # the CA thickness code 0.50 +-0.05. Dimensions page 5.
    current = "electronic_capacitor_0402_12_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987750369431552-C1547.pdf"
        part["electrical"] = {
            "capacitance": "12 pF (120)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0+-30 ppm/C referenced to 25 C (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1547)",
            "pages": [4, 5, 6],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm. C0G 0402 table lists 12 pF at 50 V with the CA thickness code (page 6).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0402CG120J500NT (C1547): 12 pF, 50 V, C0G, +-5% in 0402; reconfirmed live 2026-10-01.",
            "The Fenghua ordering code decodes exactly to that suffix (CG = C0G, 120 = 12 pF, J = +-5%, 500 = 50 V), and the C0G 0402 table covers 12 pF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1554 / Fenghua 0402CG200J500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # ordering code page 4 decodes 0402 / CG = C0G / 200 = 20 pF / J = +-5% /
    # 500 = 50 V / N nickel barrier / T 7-inch reel; the C0G 0402
    # capacitance table (page 6) lists 20 pF at 25 V and 50 V with the CA
    # thickness code 0.50 +-0.05. Dimensions page 5.
    current = "electronic_capacitor_0402_20_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987774575165440-C1554.pdf"
        part["electrical"] = {
            "capacitance": "20 pF (200)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0+-30 ppm/C referenced to 25 C (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1554)",
            "pages": [4, 5, 6],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm. C0G 0402 table lists 20 pF at 50 V with the CA thickness code (page 6).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0402CG200J500NT (C1554): 20 pF, 50 V, C0G, +-5% in 0402; reconfirmed live 2026-10-01.",
            "The Fenghua ordering code decodes exactly to that suffix (CG = C0G, 200 = 20 pF, J = +-5%, 500 = 50 V), and the C0G 0402 table covers 20 pF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1562 / Fenghua 0402CG330J500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # ordering code page 4 decodes 0402 / CG = C0G / 330 = 33 pF / J = +-5% /
    # 500 = 50 V / N nickel barrier / T 7-inch reel; the C0G 0402
    # capacitance table (page 6) lists 33 pF at 25 V and 50 V with the CA
    # thickness code 0.50 +-0.05. Dimensions page 5.
    current = "electronic_capacitor_0402_33_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987803381915648-C1562.pdf"
        part["electrical"] = {
            "capacitance": "33 pF (330)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0+-30 ppm/C referenced to 25 C (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1562)",
            "pages": [4, 5, 6],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm. C0G 0402 table lists 33 pF at 50 V with the CA thickness code (page 6).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0402CG330J500NT (C1562): 33 pF, 50 V, C0G, +-5% in 0402; reconfirmed live 2026-10-01.",
            "The Fenghua ordering code decodes exactly to that suffix (CG = C0G, 330 = 33 pF, J = +-5%, 500 = 50 V), and the C0G 0402 table covers 33 pF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1567 / Fenghua 0402CG470J500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # ordering code page 4 decodes 0402 / CG = C0G / 470 = 47 pF / J = +-5% /
    # 500 = 50 V / N nickel barrier / T 7-inch reel; the C0G 0402
    # capacitance table (page 6) lists 47 pF at 25 V and 50 V with the CA
    # thickness code 0.50 +-0.05. Dimensions page 5.
    current = "electronic_capacitor_0402_47_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0402 (1005 metric, CA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987818976067584-C1567.pdf"
        part["electrical"] = {
            "capacitance": "47 pF (470)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0+-30 ppm/C referenced to 25 C (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1567)",
            "pages": [4, 5, 6],
            "notes": "0402/1005 metric CA: L 1.00+-0.05 mm, W 0.50+-0.05 mm, T 0.50+-0.05 mm, terminal WB 0.25+-0.05 mm. C0G 0402 table lists 47 pF at 50 V with the CA thickness code (page 6).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0402CG470J500NT (C1567): 47 pF, 50 V, C0G, +-5% in 0402; reconfirmed live 2026-10-01.",
            "The Fenghua ordering code decodes exactly to that suffix (CG = C0G, 470 = 47 pF, J = +-5%, 500 = 50 V), and the C0G 0402 table covers 47 pF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0402 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1588 / Samsung CL10B102KB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 (1608 metric) / B = X7R /
    # 102 = 1 nF / K = +-10% / B = 50 V / 8 = 0.80 mm thickness / N
    # Ni-barrier termination / C = 7-inch reel; the X7R Product Lineup table
    # page 25 row 51 lists CL10B102KB8NNN + packaging code = 1 nF, 50 V,
    # +-10%, thickness max 0.90 mm (the page 11 range chart only reaches
    # 0.1 uF, so the lineup table is the nF-range ordering evidence). X7R
    # class -55 to +125 C, +-15% (page 5). Purchasing identity fields come
    # from the registry.
    current = "electronic_capacitor_0603_1_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579706978444034048-C1588.pdf"
        part["electrical"] = {
            "capacitance": "1 nF (102)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1588)",
            "pages": [4, 5, 25],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (lineup table T max 0.90 mm, page 25 row 51 lists CL10B102KB8NNN at 1 nF, 50 V, +-10%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10B102KB8NNNC (C1588): 1 nF, 50 V, X7R, +-10% in 0602..0603; reconfirmed live 2026-10-01.",
            "The Samsung ordering decode covers the exact suffix, and the X7R Product Lineup table (page 25 row 51) lists CL10B102KB8NNN + packaging code C.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1594 / Fenghua 0603B151K500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # ordering code page 4 decodes 0603 / B = X7R / 151 = 150 pF / K = +-10% /
    # 500 = 50 V / N nickel barrier / T 7-inch reel; the X7R 0603 table
    # (page 10) lists 150 pF at 6.3-50 V with the DA thickness code 0.80
    # +-0.10 mm. X7R temperature characteristic -55 to +125 C, +-15% (page 5).
    current = "electronic_capacitor_0603_150_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, DA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987892963590144-C1594.pdf"
        part["electrical"] = {
            "capacitance": "150 pF (151)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
            "capacitance_measurement": "1 kHz +-10% at 1.0 +-0.2 Vrms (Class II)",
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1594)",
            "pages": [4, 5, 10],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness DA code 0.80+-0.10 mm. X7R 0603 table lists 150 pF at 50 V (page 10).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0603B151K500NT (C1594): 150 pF, 50 V, X7R, +-10% in 0603; reconfirmed live 2026-10-01.",
            "The Fenghua ordering code decodes exactly to that suffix (B = X7R, 151 = 150 pF, K = +-10%, 500 = 50 V), and the X7R 0603 table covers 150 pF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1603 / Samsung CL10B221KB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / B = X7R / 221 = 220 pF /
    # K = +-10% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C
    # 7-inch reel; the X7R Product Lineup table page 25 row 53 lists
    # CL10B221KB8NNN + packaging code = 220 pF, 50 V, +-10%, thickness max
    # 0.90 mm. X7R class -55 to +125 C, +-15% (page 5). Purchasing identity
    # fields come from the registry.
    current = "electronic_capacitor_0603_220_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579706990813036544-C1603.pdf"
        part["electrical"] = {
            "capacitance": "220 pF (221)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1603)",
            "pages": [4, 5, 25],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (lineup table T max 0.90 mm, page 25 row 53 lists CL10B221KB8NNN at 220 pF, 50 V, +-10%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10B221KB8NNNC (C1603): 220 pF, 50 V, X7R, +-10% in 0603; reconfirmed live 2026-10-01.",
            "The Samsung ordering decode covers the exact suffix, and the X7R Product Lineup table (page 25 row 53) lists CL10B221KB8NNN + packaging code C.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1604 / Fenghua 0603B222K500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # How-To-Order page 4 decodes 0603 / B = X7R / 222 = 2.2 nF / K = +-10% /
    # 500 = 50 V / T 7-inch reel; product dimensions page 5 give the 0603
    # 1608 metric body 1.60 +-0.10 x 0.80 +-0.10 mm, DA thickness 0.80
    # +-0.10 mm; the X7R 0603 capacity/voltage table (page 10) lists 2.2 nF
    # available at 6.3-50 V. Class II tests page 18. Purchasing identity
    # fields come from the registry.
    current = "electronic_capacitor_0603_2_2_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, DA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987928631816192-C1604.pdf"
        part["electrical"] = {
            "capacitance": "2.2 nF (222)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
            "capacitance_measurement": "1 kHz +-10% at 1.0 +-0.2 Vrms (Class II)",
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1604)",
            "pages": [4, 5, 10],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness DA code 0.80+-0.10 mm. X7R 0603 table lists 2.2 nF at 50 V (page 10).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0603B222K500NT (C1604): 2.2 nF, 50 V, X7R, +-10% in 0603; reconfirmed live 2026-10-01 (stock 1,147,702).",
            "The Fenghua ordering code decodes exactly to that suffix (B = X7R, 222 = 2.2 nF, K = +-10%, 500 = 50 V), and the X7R 0603 table covers 2.2 nF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1613 / Samsung CL10B332KB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / B = X7R / 332 = 3.3 nF /
    # K = +-10% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the X7R Product Lineup table page 26 lists CL10B332KB8NNN at
    # 3.3 nF, 50 V, +-10%, 1.60 x 0.80 mm. X7R class -55 to +125 C, +-15%
    # (page 5). Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_3_3_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707001003163648-C1613.pdf"
        part["electrical"] = {
            "capacitance": "3.3 nF (332)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1613)",
            "pages": [4, 5, 26],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (lineup table T max 0.90 mm, page 26 lists CL10B332KB8NNN at 3.3 nF, 50 V, +-10%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10B332KB8NNNC (C1613): 3.3 nF, 50 V, X7R, +-10% in 0603; reconfirmed live 2026-10-01 (stock 222,204).",
            "The Samsung ordering decode covers the exact suffix, and the X7R Product Lineup table (page 26) lists CL10B332KB8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1620 / Fenghua 0603B471K500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # How-To-Order page 4 decodes 0603 / B = X7R / 471 = 470 pF / K = +-10% /
    # 500 = 50 V / T 7-inch reel; product dimensions page 5 give the 0603
    # 1608 metric body 1.60 +-0.10 x 0.80 +-0.10 mm, DA thickness 0.80
    # +-0.10 mm; the X7R 0603 capacity/voltage table (page 10) lists 470 pF
    # available at 6.3-50 V. Class II tests page 18. Purchasing identity
    # fields come from the registry.
    current = "electronic_capacitor_0603_470_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, DA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987977059115008-C1620.pdf"
        part["electrical"] = {
            "capacitance": "470 pF (471)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
            "capacitance_measurement": "1 kHz +-10% at 1.0 +-0.2 Vrms (Class II)",
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1620)",
            "pages": [4, 5, 10],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness DA code 0.80+-0.10 mm. X7R 0603 table lists 470 pF at 50 V (page 10).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0603B471K500NT (C1620): 470 pF, 50 V, X7R, +-10% in 0603; reconfirmed live 2026-10-01 (stock 909,094).",
            "The Fenghua ordering code decodes exactly to that suffix (B = X7R, 471 = 470 pF, K = +-10%, 500 = 50 V), and the X7R 0603 table covers 470 pF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1622 / Samsung CL10B473KB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / B = X7R / 473 = 47 nF /
    # K = +-10% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the X7R Product Lineup table page 26 lists CL10B473KB8NNN at
    # 47 nF, 50 V, +-10%, 1.60 x 0.80 mm. X7R class -55 to +125 C, +-15%
    # (page 5). Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_47_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707009119551488-C1622.pdf"
        part["electrical"] = {
            "capacitance": "47 nF (473)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1622)",
            "pages": [4, 5, 26],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (lineup table T max 0.90 mm, page 26 lists CL10B473KB8NNN at 47 nF, 50 V, +-10%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10B473KB8NNNC (C1622): 47 nF, 50 V, X7R, +-10% in 0603; reconfirmed live 2026-10-01 (stock 829,693).",
            "The Samsung ordering decode covers the exact suffix, and the X7R Product Lineup table (page 26) lists CL10B473KB8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1623 / Samsung CL10B474KA8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / B = X7R / 474 = 470 nF /
    # K = +-10% / A = 25 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the X7R Product Lineup table page 26 lists CL10B474KA8NNN at
    # 470 nF, 25 V, +-10%, 1.60 x 0.80 mm. X7R class -55 to +125 C, +-15%
    # (page 5). Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_470_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707013296939008-C1623.pdf"
        part["electrical"] = {
            "capacitance": "470 nF (474)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "25 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1623)",
            "pages": [4, 5, 26],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (lineup table T max 0.90 mm, page 26 lists CL10B474KA8NNN at 470 nF, 25 V, +-10%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10B474KA8NNNC (C1623): 470 nF, 25 V, X7R, +-10% in 0603; reconfirmed live 2026-10-01 (stock 933,612).",
            "The Samsung ordering decode covers the exact suffix (A = 25 V), and the X7R Product Lineup table (page 26) lists CL10B474KA8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1631 / Fenghua 0603B682K500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # How-To-Order page 4 decodes 0603 / B = X7R / 682 = 6.8 nF / K = +-10% /
    # 500 = 50 V / T 7-inch reel; product dimensions page 5 give the 0603
    # 1608 metric body 1.60 +-0.10 x 0.80 +-0.10 mm, DA thickness 0.80
    # +-0.10 mm; the X7R 0603 capacity/voltage table (page 10) lists 6.8 nF
    # available at 6.3-50 V. Class II tests page 18. Purchasing identity
    # fields come from the registry.
    current = "electronic_capacitor_0603_6_8_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, DA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988003076653056-C1631.pdf"
        part["electrical"] = {
            "capacitance": "6.8 nF (682)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
            "capacitance_measurement": "1 kHz +-10% at 1.0 +-0.2 Vrms (Class II)",
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1631)",
            "pages": [4, 5, 10],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness DA code 0.80+-0.10 mm. X7R 0603 table lists 6.8 nF at 50 V (page 10).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0603B682K500NT (C1631): 6.8 nF, 50 V, X7R, +-10% in 0603; reconfirmed live 2026-10-01 (stock 255,120).",
            "The Fenghua ordering code decodes exactly to that suffix (B = X7R, 682 = 6.8 nF, K = +-10%, 500 = 50 V), and the X7R 0603 table covers 6.8 nF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1634 / Samsung CL10C100JB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / C = C0G / 100 = 10 pF /
    # J = +-5% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the C0G Product Lineup table page 15 lists CL10C100JB8NNN at
    # 10 pF, 50 V, +-5%, 1.60 x 0.80 mm; Class I (C0G) characteristics
    # pages 5-7. Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_10_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707028643897344-C1634.pdf"
        part["electrical"] = {
            "capacitance": "10 pF (100)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1634)",
            "pages": [4, 5, 15],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (C0G lineup table page 15 lists CL10C100JB8NNN at 10 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10C100JB8NNNC (C1634): 10 pF, 50 V, C0G, +-5% in 0603; reconfirmed live 2026-10-01 (stock 1,267,842).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%), and the C0G Product Lineup table (page 15) lists CL10C100JB8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1644 / Samsung CL10C150JB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / C = C0G / 150 = 15 pF /
    # J = +-5% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the C0G Product Lineup table page 15 lists CL10C150JB8NNN at
    # 15 pF, 50 V, +-5%, 1.60 x 0.80 mm; Class I (C0G) characteristics
    # pages 5-7. Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_15_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707088031322112-C1644.pdf"
        part["electrical"] = {
            "capacitance": "15 pF (150)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1644)",
            "pages": [4, 5, 15],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (C0G lineup table page 15 lists CL10C150JB8NNN at 15 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10C150JB8NNNC (C1644): 15 pF, 50 V, C0G, +-5% in 0603; reconfirmed live 2026-10-01 (stock 1,044,036).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%), and the C0G Product Lineup table (page 15) lists CL10C150JB8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1647 / Samsung CL10C180JB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / C = C0G / 180 = 18 pF /
    # J = +-5% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the C0G Product Lineup table page 15 lists CL10C180JB8NNN at
    # 18 pF, 50 V, +-5%, 1.60 x 0.80 mm; Class I (C0G) characteristics
    # pages 5-7. Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_18_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707035342200832-C1647.pdf"
        part["electrical"] = {
            "capacitance": "18 pF (180)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1647)",
            "pages": [4, 5, 15],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (C0G lineup table page 15 lists CL10C180JB8NNN at 18 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10C180JB8NNNC (C1647): 18 pF, 50 V, C0G, +-5% in 0603; reconfirmed live 2026-10-01 (stock 422,542).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%), and the C0G Product Lineup table (page 15) lists CL10C180JB8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1648 / Samsung CL10C200JB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / C = C0G / 200 = 20 pF /
    # J = +-5% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the C0G Product Lineup table page 15 lists CL10C200JB8NNN at
    # 20 pF, 50 V, +-5%, 1.60 x 0.80 mm; Class I (C0G) characteristics
    # pages 5-7. Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_20_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707039381590016-C1648.pdf"
        part["electrical"] = {
            "capacitance": "20 pF (200)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1648)",
            "pages": [4, 5, 15],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (C0G lineup table page 15 lists CL10C200JB8NNN at 20 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10C200JB8NNNC (C1648): 20 pF, 50 V, C0G, +-5% in 0603; reconfirmed live 2026-10-01 (stock 2,285,606).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%), and the C0G Product Lineup table (page 15) lists CL10C200JB8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1653 / Samsung CL10C220JB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / C = C0G / 220 = 22 pF /
    # J = +-5% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the C0G Product Lineup table page 15 lists CL10C220JB8NNN at
    # 22 pF, 50 V, +-5%, 1.60 x 0.80 mm; Class I (C0G) characteristics
    # pages 5-7. Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_22_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707043273629696-C1653.pdf"
        part["electrical"] = {
            "capacitance": "22 pF (220)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1653)",
            "pages": [4, 5, 15],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (C0G lineup table page 15 lists CL10C220JB8NNN at 22 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10C220JB8NNNC (C1653): 22 pF, 50 V, C0G, +-5% in 0603; reconfirmed live 2026-10-01 (stock 2,978,606).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%), and the C0G Product Lineup table (page 15) lists CL10C220JB8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1658 / Fenghua 0603CG300J500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # How-To-Order page 4 decodes 0603 / CG = C0G / 300 = 30 pF / J = +-5% /
    # 500 = 50 V / T 7-inch reel; product dimensions page 5 give the 0603
    # 1608 metric body 1.60 +-0.10 x 0.80 +-0.10 mm; the C0G 0603
    # capacity/voltage table (page 6) lists 30 pF at 10-50 V. Class I tests
    # follow the catalogue Class I sections. Purchasing identity fields come
    # from the registry.
    current = "electronic_capacitor_0603_30_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988069187543040-C1658.pdf"
        part["electrical"] = {
            "capacitance": "30 pF (300)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1658)",
            "pages": [4, 5, 6],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm. C0G 0603 capacity/voltage table lists 30 pF at 50 V (page 6).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0603CG300J500NT (C1658): 30 pF, 50 V, C0G, +-5% in 0603; reconfirmed live 2026-10-01 (stock 379,491).",
            "The Fenghua ordering code decodes exactly to that suffix (CG = C0G, 300 = 30 pF, J = +-5%, 500 = 50 V), and the C0G 0603 table covers 30 pF at 50 V.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1663 / Samsung CL10C330JB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / C = C0G / 330 = 33 pF /
    # J = +-5% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the C0G Product Lineup table page 15 lists CL10C330JB8NNN at
    # 33 pF, 50 V, +-5%, 1.60 x 0.80 mm; Class I (C0G) characteristics
    # pages 5-7. Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_33_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707052081807360-C1663.pdf"
        part["electrical"] = {
            "capacitance": "33 pF (330)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1663)",
            "pages": [4, 5, 15],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (C0G lineup table page 15 lists CL10C330JB8NNN at 33 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10C330JB8NNNC (C1663): 33 pF, 50 V, C0G, +-5% in 0603; reconfirmed live 2026-10-01 (stock 1,035,691).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%), and the C0G Product Lineup table (page 15) lists CL10C330JB8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1664 / Samsung CL10C331JB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / C = C0G / 331 = 330 pF /
    # J = +-5% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the C0G Product Lineup table page 15 lists CL10C331JB8NNN at
    # 330 pF, 50 V, +-5%, 1.60 x 0.80 mm; Class I (C0G) characteristics
    # pages 5-7. Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_330_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707056565379072-C1664.pdf"
        part["electrical"] = {
            "capacitance": "330 pF (331)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1664)",
            "pages": [4, 5, 15],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (C0G lineup table page 15 lists CL10C331JB8NNN at 330 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10C331JB8NNNC (C1664): 330 pF, 50 V, C0G, +-5% in 0603; reconfirmed live 2026-10-01 (stock 915,152).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%), and the C0G Product Lineup table (page 15) lists CL10C331JB8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1671 / Samsung CL10C470JB8NNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 10 = 0603 / C = C0G / 470 = 47 pF /
    # J = +-5% / B = 50 V / 8 = 0.80 mm thickness / N Ni-barrier / C 7-inch
    # reel; the C0G Product Lineup table page 15 lists CL10C470JB8NNN at
    # 47 pF, 50 V, +-5%, 1.60 x 0.80 mm; Class I (C0G) characteristics
    # pages 5-7. Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0603_47_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0603 (1608 metric, thickness code 8)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707064693805056-C1671.pdf"
        part["electrical"] = {
            "capacitance": "47 pF (470)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1671)",
            "pages": [4, 5, 15],
            "notes": "0603/1608 metric: L 1.60 mm, W 0.80 mm, thickness code 8 = 0.80 mm (C0G lineup table page 15 lists CL10C470JB8NNN at 47 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL10C470JB8NNNC (C1671): 47 pF, 50 V, C0G, +-5% in 0603; reconfirmed live 2026-10-01 (stock 677,714).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%), and the C0G Product Lineup table (page 15) lists CL10C470JB8NNN.",
            "Non-polarized two-terminal chip; the standard built-in 0603 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1710 / Samsung CL21B103KBANNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 21 = 0805 / B = X7R / 103 = 10 nF /
    # K = +-10% / B = 50 V / A = 1.25 mm thickness / N Ni-barrier / C 7-inch
    # reel; the X7R Product Lineup table page 27 lists CL21B103KBANNN at
    # 10 nF, 50 V, +-10%, 2.00 x 1.25 mm; X7R class -55 to +125 C, +-15%
    # (page 5). Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0805_10_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0805 (2012 metric, thickness code A)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579706770727755776-C1710.pdf"
        part["electrical"] = {
            "capacitance": "10 nF (103)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.25}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1710)",
            "pages": [4, 5, 27],
            "notes": "0805/2012 metric: L 2.00 mm, W 1.25 mm, thickness code A = 1.25 mm (X7R lineup table page 27 lists CL21B103KBANNN at 10 nF, 50 V, +-10%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL21B103KBANNNC (C1710): 10 nF, 50 V, X7R, +-10% in 0805; reconfirmed live 2026-10-01 (stock 2,273,417).",
            "The Samsung ordering decode covers the exact suffix (21 = 0805, A = 1.25 mm thickness), and the X7R Product Lineup table (page 27) lists CL21B103KBANNN.",
            "Non-polarized two-terminal chip; the standard built-in 0805 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1729 / Samsung CL21B223KBANNNC full-stage technical data. The JLC
    # datasheet link serves the same Samsung MLCC general catalogue
    # (November 2015) already captured for the family - the downloaded PDF
    # is byte-identical (sha256 96baebe4...) and is kept via
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad
    # after a browser download confirmed it. Ordering decode page 4 covers
    # the full suffix: CL / 21 = 0805 / B = X7R / 223 = 22 nF / K = +-10% /
    # B = 50 V / A = 1.25 mm thickness / N Ni-barrier / C 7-inch reel.
    # Gap recorded honestly: the X7R 0805 lineup table (page 27) lists the
    # neighbouring KBA rows (10 nF, 12 nF, 15 nF, 33 nF, 39 nF, 47 nF at
    # 50 V, 2.00 x 1.25 mm) but not 22 nF - this catalogue revision predates
    # the variant. Identity rests on the suffix decode, the adjacent KBA
    # 0805 rows, the X7R class spec (page 5), and the live JLC description.
    # Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0805_22_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0805 (2012 metric, thickness code A)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579706774496002048-C1729.pdf"
        part["electrical"] = {
            "capacitance": "22 nF (223)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.25}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1729)",
            "pages": [4, 5, 27],
            "notes": "0805/2012 metric: L 2.00 mm, W 1.25 mm, thickness code A = 1.25 mm (decode page 4; neighbouring KBA 0805 rows on lineup page 27 share the 2.00 x 1.25 mm body).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL21B223KBANNNC (C1729): 22 nF, 50 V, X7R, +-10% in 0805; reconfirmed live 2026-10-01 (stock 234,075).",
            "Browser-downloaded the JLC datasheet and verified it is byte-identical to the family catalogue (sha256 96baebe4...); no second copy kept (oomp_datasheet_common_with).",
            "Known gap: the catalogue's X7R 0805 lineup table does not list 22 nF (this 2015 revision predates the variant); identity rests on the page 4 suffix decode, the adjacent KBA 0805 rows, and the live JLC description.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1739 / Fenghua 0805B333K500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # How-To-Order page 4 decodes 0805 / B = X7R / 333 = 33 nF / K = +-10% /
    # 500 = 50 V / T 7-inch reel; the X7R 0805 capacity/voltage table
    # (page 11) lists 33 nF at 6.3-50 V with thickness code EA = 0.80
    # +-0.20 mm (body 2.00 x 1.25 mm, page 5). Class II tests page 16.
    # Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0805_33_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0805 (2012 metric, EA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988558687850496-C1739.pdf"
        part["electrical"] = {
            "capacitance": "33 nF (333)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
            "capacitance_measurement": "1 kHz +-10% at 1.0 +-0.2 Vrms (Class II)",
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1739)",
            "pages": [4, 5, 11],
            "notes": "0805/2012 metric: L 2.00 mm, W 1.25 mm, thickness code EA = 0.80+-0.20 mm (X7R 0805 table page 11 lists 33 nF at 50 V).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0805B333K500NT (C1739): 33 nF, 50 V, X7R, +-10% in 0805; reconfirmed live 2026-10-01 (stock 61,921).",
            "The Fenghua ordering code decodes exactly to that suffix (B = X7R, 333 = 33 nF, K = +-10%, 500 = 50 V), and the X7R 0805 table covers 33 nF at 50 V (thickness code EA).",
            "Non-polarized two-terminal chip; the standard built-in 0805 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1743 / Fenghua 0805B471K500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # How-To-Order page 4 decodes 0805 / B = X7R / 471 = 470 pF / K = +-10% /
    # 500 = 50 V / T 7-inch reel; the X7R 0805 capacity/voltage table
    # (page 11) lists 470 pF at 6.3-50 V with thickness code EA = 0.80
    # +-0.20 mm (body 2.00 x 1.25 mm, page 5). Class II tests page 16.
    # Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0805_470_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0805 (2012 metric, EA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988574495776768-C1743.pdf"
        part["electrical"] = {
            "capacitance": "470 pF (471)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
            "capacitance_measurement": "1 kHz +-10% at 1.0 +-0.2 Vrms (Class II)",
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1743)",
            "pages": [4, 5, 11],
            "notes": "0805/2012 metric: L 2.00 mm, W 1.25 mm, thickness code EA = 0.80+-0.20 mm (X7R 0805 table page 11 lists 470 pF at 50 V).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0805B471K500NT (C1743): 470 pF, 50 V, X7R, +-10% in 0805; reconfirmed live 2026-10-01 (stock 296,120).",
            "The Fenghua ordering code decodes exactly to that suffix (B = X7R, 471 = 470 pF, K = +-10%, 500 = 50 V), and the X7R 0805 table covers 470 pF at 50 V (thickness code EA).",
            "Non-polarized two-terminal chip; the standard built-in 0805 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1744 / Fenghua 0805B472K500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # How-To-Order page 4 decodes 0805 / B = X7R / 472 = 4.7 nF / K = +-10% /
    # 500 = 50 V / T 7-inch reel; the X7R 0805 capacity/voltage table
    # (page 11) lists 4.7 nF at 6.3-50 V with thickness code EA = 0.80
    # +-0.20 mm (body 2.00 x 1.25 mm, page 5). Class II tests page 16.
    # Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0805_4_7_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "0805 (2012 metric, EA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988577683853312-C1744.pdf"
        part["electrical"] = {
            "capacitance": "4.7 nF (472)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
            "capacitance_measurement": "1 kHz +-10% at 1.0 +-0.2 Vrms (Class II)",
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1744)",
            "pages": [4, 5, 11],
            "notes": "0805/2012 metric: L 2.00 mm, W 1.25 mm, thickness code EA = 0.80+-0.20 mm (X7R 0805 table page 11 lists 4.7 nF at 50 V).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 0805B472K500NT (C1744): 4.7 nF, 50 V, X7R, +-10% in 0805; reconfirmed live 2026-10-01 (stock 424,648).",
            "The Fenghua ordering code decodes exactly to that suffix (B = X7R, 472 = 4.7 nF, K = +-10%, 500 = 50 V), and the X7R 0805 table covers 4.7 nF at 50 V (thickness code EA).",
            "Non-polarized two-terminal chip; the standard built-in 0805 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1779 / Samsung CL21A475KAQNNNE full-stage technical data. The JLC
    # datasheet link serves the same Samsung MLCC general catalogue
    # (November 2015) already captured for the family - downloaded in the
    # browser and verified byte-identical (sha256 96baebe4...), kept via
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad.
    # Ordering decode page 4 covers the full suffix: CL / 21 = 0805 /
    # A = X5R / 475 = 4.7 uF / K = +-10% / A = 25 V (rated voltage code
    # table) / Q = 1.25 mm thickness (thickness code table) / N / N /
    # E embossed 7-inch reel. Gap recorded honestly: the X5R 0805 lineup
    # (page 20) lists the KB 50 V variant CL21A475KBQNNN with the same Q
    # body but not the KA 25 V variant - this revision predates it.
    # Identity rests on the decode, the adjacent KB row, the X5R class spec
    # (page 5: -55 to +85 C, +-15%), and the live JLC description.
    # Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0805_4_7_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0805 (2012 metric, Q thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8556213325551206400-C1779.pdf"
        part["electrical"] = {
            "capacitance": "4.7 uF (475)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "25 V",
            "dielectric": "X5R (Class II)",
            "temperature_range": "-55 to +85 C",
            "temperature_characteristic": "+-15% over the operating range (X5R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.25}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1779)",
            "pages": [4, 5, 20],
            "notes": "0805/2012 metric: L 2.00 mm, W 1.25 mm, thickness code Q = 1.25 mm (page 4 thickness code table). X5R 0805 lineup page 20 lists the KB 50 V variant with the same Q body.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL21A475KAQNNNE (C1779): 4.7 uF, 25 V, X5R, +-10% in 0805; reconfirmed live 2026-10-01 (stock 3,052,932).",
            "Browser-downloaded the JLC datasheet and verified it is byte-identical to the family catalogue (sha256 96baebe4...); no second copy kept (oomp_datasheet_common_with).",
            "Known gap: the catalogue's X5R 0805 lineup lists the 50 V KB variant but not the 25 V KA variant (this 2015 revision predates it); identity rests on the page 4 decode (A = 25 V, Q = 1.25 mm), the adjacent KB row, and the live JLC description.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1790 / Samsung CL21C101JBANNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 21 = 0805 / C = C0G / 101 = 100 pF /
    # J = +-5% / B = 50 V / A = 1.25 mm thickness / N / N / C 7-inch reel;
    # the C0G Product Lineup table page 17 lists CL21C101JBANNN at 100 pF,
    # 50 V, +-5%, 2.00 x 1.25 mm; Class I (C0G) characteristics pages 5-7.
    # Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0805_100_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0805 (2012 metric, A thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579706805749923840-C1790.pdf"
        part["electrical"] = {
            "capacitance": "100 pF (101)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.25}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1790)",
            "pages": [4, 5, 17],
            "notes": "0805/2012 metric: L 2.00 mm, W 1.25 mm, thickness code A = 1.25 mm (C0G lineup table page 17 lists CL21C101JBANNN at 100 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL21C101JBANNNC (C1790): 100 pF, 50 V, C0G, +-5% in 0805; reconfirmed live 2026-10-01 (stock 587,299).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%, A = 1.25 mm thickness), and the C0G Product Lineup table (page 17) lists CL21C101JBANNN.",
            "Non-polarized two-terminal chip; the standard built-in 0805 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1798 / Samsung CL21C200JBANNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 21 = 0805 / C = C0G / 200 = 20 pF /
    # J = +-5% / B = 50 V / A = 1.25 mm thickness / N / N / C 7-inch reel;
    # the C0G Product Lineup table page 16 lists CL21C200JBANNN at 20 pF,
    # 50 V, +-5%, 2.00 x 1.25 mm; Class I (C0G) characteristics pages 5-7.
    # Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0805_20_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0805 (2012 metric, A thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579706817288998912-C1798.pdf"
        part["electrical"] = {
            "capacitance": "20 pF (200)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.25}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1798)",
            "pages": [4, 5, 16],
            "notes": "0805/2012 metric: L 2.00 mm, W 1.25 mm, thickness code A = 1.25 mm (C0G lineup table page 16 lists CL21C200JBANNN at 20 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL21C200JBANNNC (C1798): 20 pF, 50 V, C0G, +-5% in 0805; reconfirmed live 2026-10-01 (stock 218,875).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%, A = 1.25 mm thickness), and the C0G Product Lineup table (page 16) lists CL21C200JBANNN.",
            "Non-polarized two-terminal chip; the standard built-in 0805 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1804 / Samsung CL21C220JBANNNC full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 21 = 0805 / C = C0G / 220 = 22 pF /
    # J = +-5% / B = 50 V / A = 1.25 mm thickness / N / N / C 7-inch reel;
    # the C0G Product Lineup table page 16 lists CL21C220JBANNN at 22 pF,
    # 50 V, +-5%, 2.00 x 1.25 mm; Class I (C0G) characteristics pages 5-7.
    # Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0805_22_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0805 (2012 metric, A thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579706825203105792-C1804.pdf"
        part["electrical"] = {
            "capacitance": "22 pF (220)",
            "tolerance": "+-5% (J)",
            "rated_voltage": "50 V",
            "dielectric": "C0G (Class I)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "0 +-30 ppm/C over the operating range (C0G)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.25}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1804)",
            "pages": [4, 5, 16],
            "notes": "0805/2012 metric: L 2.00 mm, W 1.25 mm, thickness code A = 1.25 mm (C0G lineup table page 16 lists CL21C220JBANNN at 22 pF, 50 V, +-5%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL21C220JBANNNC (C1804): 22 pF, 50 V, C0G, +-5% in 0805; reconfirmed live 2026-10-01 (stock 799,152).",
            "The Samsung ordering decode covers the exact suffix (C = C0G, J = +-5%, A = 1.25 mm thickness), and the C0G Product Lineup table (page 16) lists CL21C220JBANNN.",
            "Non-polarized two-terminal chip; the standard built-in 0805 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1846 / Fenghua 1206B103K500NT full-stage technical data, verified
    # against the shared Fenghua General Series MLCC specification
    # (oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad):
    # How-To-Order page 4 decodes 1206 / B = X7R / 103 = 10 nF / K = +-10% /
    # 500 = 50 V / T 7-inch reel; the X7R 1206 capacity/voltage table
    # (page 12) lists 10 nF at 6.3-50 V with thickness code FA = 0.80
    # +-0.20 mm (body 3.20 x 1.60 mm, page 5). Class II tests page 16.
    # Purchasing identity fields come from the registry.
    current = "electronic_capacitor_1206_10_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_pico_farad"
        part["package_name_manufacturer"] = "1206 (3216 metric, FA thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991316979736576-C1846.pdf"
        part["electrical"] = {
            "capacitance": "10 nF (103)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
            "capacitance_measurement": "1 kHz +-10% at 1.0 +-0.2 Vrms (Class II)",
        }
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 0.8}
        part["dimension_reference"] = {
            "document": "Fenghua General Series MLCC specification (C1846)",
            "pages": [4, 5, 12],
            "notes": "1206/3216 metric: L 3.20 mm, W 1.60 mm, thickness code FA = 0.80+-0.20 mm (X7R 1206 table page 12 lists 10 nF at 50 V).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_1206_3216Metric",
            "hand_solder": "Capacitor_SMD:C_1206_3216Metric_Pad1.33x1.80mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Fenghua 1206B103K500NT (C1846): 10 nF, 50 V, X7R, +-10% in 1206; reconfirmed live 2026-10-01 (stock 230,801).",
            "The Fenghua ordering code decodes exactly to that suffix (B = X7R, 103 = 10 nF, K = +-10%, 500 = 50 V), and the X7R 1206 table covers 10 nF at 50 V (thickness code FA).",
            "Non-polarized two-terminal chip; the standard built-in 1206 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C1848 / Samsung CL31B105KBHNNNE full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 31 = 1206 / B = X7R / 105 = 1 uF /
    # K = +-10% / B = 50 V / H = 1.60 mm thickness / N / N / E embossed
    # 7-inch reel; the X7R Product Lineup table page 28 lists CL31B105KBHNNN
    # at 1 uF, 50 V, +-10%, 3.20 x 1.60 mm; X7R class -55 to +125 C, +-15%
    # (page 5). Purchasing identity fields come from the registry.
    current = "electronic_capacitor_1206_1_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "1206 (3216 metric, H thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707343589855232-C1848.pdf"
        part["electrical"] = {
            "capacitance": "1 uF (105)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.6}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C1848)",
            "pages": [4, 5, 28],
            "notes": "1206/3216 metric: L 3.20 mm, W 1.60 mm, thickness code H = 1.60 mm (X7R lineup table page 28 lists CL31B105KBHNNN at 1 uF, 50 V, +-10%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_1206_3216Metric",
            "hand_solder": "Capacitor_SMD:C_1206_3216Metric_Pad1.33x1.80mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL31B105KBHNNNE (C1848): 1 uF, 50 V, X7R, +-10% in 1206; reconfirmed live 2026-10-01 (stock 517,314).",
            "The Samsung ordering decode covers the exact suffix (31 = 1206, H = 1.60 mm thickness), and the X7R Product Lineup table (page 28) lists CL31B105KBHNNN.",
            "Non-polarized two-terminal chip; the standard built-in 1206 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C5378 / Samsung CL21B224KBFNNNE full-stage technical data, verified
    # against the shared Samsung MLCC general catalogue (November 2015,
    # oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad):
    # part numbering page 4 decodes CL / 21 = 0805 / B = X7R / 224 = 220 nF /
    # K = +-10% / B = 50 V / F = 1.25 mm thickness / N / N / E embossed
    # 7-inch reel; the X7R 0805 lineup page 27 lists CL21B224KBFNNN at
    # 220 nF, 50 V, +-10%; X7R class -55 to +125 C, +-15% (page 5).
    # Purchasing identity fields come from the registry.
    current = "electronic_capacitor_0805_220_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0805 (2012 metric, F thickness code)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579706836171481088-C5378.pdf"
        part["electrical"] = {
            "capacitance": "220 nF (224)",
            "tolerance": "+-10% (K)",
            "rated_voltage": "50 V",
            "dielectric": "X7R (Class II)",
            "temperature_range": "-55 to +125 C",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.25}
        part["dimension_reference"] = {
            "document": "Samsung Electro-Mechanics MLCC general catalogue, November 2015 (C5378)",
            "pages": [4, 5, 27],
            "notes": "0805/2012 metric: L 2.00 mm, W 1.25 mm, thickness code F = 1.25 mm (X7R lineup page 27 lists CL21B224KBFNNN at 220 nF, 50 V, +-10%).",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung CL21B224KBFNNNE (C5378): 220 nF, 50 V, X7R, +-10% in 0805; reconfirmed live 2026-10-02 (stock 611,888).",
            "The Samsung ordering decode covers the exact suffix (F = 1.25 mm thickness), and the X7R 0805 lineup table (page 27) lists CL21B224KBFNNN.",
            "Non-polarized two-terminal chip; the standard built-in 0805 chip renderer draws the package from the verified dimensions.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_capacitor_0402_150_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "150 pF",
            "tolerance": "±10%",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1527 / Fenghua 0402B151K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 150 pF value; the populate row was added by this intake.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 150 pF, 50 V, X7R, ±10%, stock 153,090, minimum 1, full reel 10,000, available order qty 107,920, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987679179509760-C1527.pdf).",
        ]

    current = "electronic_capacitor_0402_160_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "160 pF",
            "tolerance": "±10%",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1528 / Fenghua 0402B161K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 160 pF value; the populate row was added by this intake. The Fenghua ordering code (161 = 16 x 10^1 pF) decodes consistently with the listed 160 pF.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 160 pF, 50 V, X7R, ±10%, stock 9,924, minimum 1, full reel 10,000, available order qty 9,923, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987682262458368-C1528.pdf).",
        ]

    current = "electronic_capacitor_0402_270_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "270 pF",
            "tolerance": "±10%",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1533 / Fenghua 0402B271K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 270 pF value; the populate row was added by this intake. The Fenghua ordering code (271 = 27 x 10^1 pF) decodes consistently with the listed 270 pF.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 270 pF, 50 V, X7R, ±10%, stock 21,545, minimum 1, full reel 10,000, available order qty 21,487, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987699094200320-C1533.pdf).",
        ]

    current = "electronic_capacitor_0402_560_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "560 pF",
            "tolerance": "±10%",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1539 / Fenghua 0402B561K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 560 pF value; the populate row was added by this intake. The Fenghua ordering code (561 = 56 x 10^1 pF) decodes consistently with the listed 560 pF.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 560 pF, 50 V, X7R, ±10%, stock 59,757, minimum 1, full reel 10,000, available order qty 59,682, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987721080606720-C1539.pdf).",
        ]

    current = "electronic_capacitor_0402_680_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "680 pF",
            "tolerance": "±10%",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1541 / Fenghua 0402B681K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 680 pF value; the populate row was added by this intake. The Fenghua ordering code (681 = 68 x 10^1 pF) decodes consistently with the listed 680 pF.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 680 pF, 50 V, X7R, ±10%, stock 188,329, minimum 1, full reel 10,000, available order qty 183,458, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987727242174464-C1541.pdf).",
        ]

    current = "electronic_capacitor_0402_6_8_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "6.8 nF",
            "tolerance": "±10%",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1542 / Fenghua 0402B682K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 6.8 nF value; the populate row was added by this intake. The Fenghua ordering code (682 = 68 x 10^2 pF) decodes consistently with the listed 6.8 nF.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 6.8 nF, 50 V, X7R, ±10%, stock 119,235, minimum 1, full reel 10,000, available order qty 95,575, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987734380879872-C1542.pdf).",
        ]

    current = "electronic_capacitor_0402_0_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "0.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1544 / Fenghua 0402CG0R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 0.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 0R5 = 0.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 0.5 pF, 50 V, C0G, stock 47,649, minimum 1, full reel 10,000, available order qty 47,296, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987740676395008-C1544.pdf).",
            "A SparkFun Artemis project reference (parts/oomp_project_github_sparkfun_spark_fun_artemis_spark_fun_artemis_current, component C18) already proposed this exact oomp_id as unmatched; this generic row resolves that proposal. Full stage should re-run project matching.",
        ]

    current = "electronic_capacitor_0402_1_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1550 / Fenghua 0402CG1R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 1 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R0 = 1.0 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 1 pF, 50 V, C0G, stock 922,332, minimum 1, full reel 10,000, available order qty 878,566, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987761564164096-C1550.pdf).",
        ]

    current = "electronic_capacitor_0402_1_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1551 / Fenghua 0402CG1R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 1.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R2 = 1.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 1.2 pF, 50 V, C0G, stock 159,402, minimum 1, full reel 10,000, available order qty 154,597, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987764881858560-C1551.pdf).",
        ]

    current = "electronic_capacitor_0402_10_nano_farad_fenghua_adv_tech_0402b103k500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0402_10_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "10 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1524 / 0402B103K500NT purchasing variant; 0402, 10 nF, 50 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0402 10 nF definition. The reviewed Basic Samsung preference C15195 / CL05B103KB5NNNC on the generic ID remains unchanged; the registry allows one preferred code per ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987672766554112-C1524.pdf).",
        ]

    current = "electronic_capacitor_0402_10_pico_farad_fenghua_adv_tech_0402cg100j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0402_10_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "10 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1545 / 0402CG100J500NT purchasing variant; 0402, 10 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0402 10 pF definition. The reviewed Basic Samsung preference C32949 / CL05C100JB5NNNC on the generic ID remains unchanged; the registry allows one preferred code per ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987744002883584-C1545.pdf).",
        ]

    current = "electronic_capacitor_0402_1_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1552 / Fenghua 0402CG1R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 1.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R5 = 1.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 1.5 pF, 50 V, C0G, stock 242,999, minimum 1, full reel 10,000, available order qty 209,310, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987768027586560-C1552.pdf).",
        ]

    current = "electronic_capacitor_0402_1_8_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.8 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1553 / Fenghua 0402CG1R8C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 1.8 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R8 = 1.8 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 1.8 pF, 50 V, C0G, stock 132,499, minimum 1, full reel 10,000, available order qty 128,489, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987771446349824-C1553.pdf).",
        ]

    current = "electronic_capacitor_0402_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1558 / Fenghua 0402CG2R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R0 = 2.0 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 2 pF, 50 V, C0G, stock 218,871, minimum 1, full reel 10,000, available order qty 215,793, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987787350609920-C1558.pdf).",
        ]

    current = "electronic_capacitor_0402_2_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1559 / Fenghua 0402CG2R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 2.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R2 = 2.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 2.2 pF, 50 V, C0G, stock 196,977, minimum 1, full reel 10,000, available order qty 173,077, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987790685216768-C1559.pdf).",
        ]

    current = "electronic_capacitor_0402_2_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1560 / Fenghua 0402CG2R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 2.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R5 = 2.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 2.5 pF, 50 V, C0G, stock 7,527, minimum 1, full reel 10,000, available order qty 7,477, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987793722163200-C1560.pdf).",
        ]

    current = "electronic_capacitor_0402_2_7_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.7 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1561 / Fenghua 0402CG2R7C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 2.7 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R7 = 2.7 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 2.7 pF, 50 V, C0G, stock 77,631, minimum 1, full reel 10,000, available order qty 55,038, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987796775886848-C1561.pdf).",
        ]

    current = "electronic_capacitor_0402_25_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "25 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1556 / Fenghua 0402CG250J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 25 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 250 = 25 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 25 pF, 50 V, C0G, +/-5%, stock 95, minimum 10000 (equal to the 10,000 full reel; listed as Pre-order with estimated unit price $0.0008), MSL 1. Low stock and reel-only purchasing do not change the verified identity. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987780963090432-C1556.pdf).",
        ]

    current = "electronic_capacitor_0402_39_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "39 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1563 / Fenghua 0402CG390J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 39 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 390 = 39 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 39 pF, 50 V, C0G, +/-5%, stock 88,946, minimum 1, full reel 10,000, available order qty 87,267, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987806712193024-C1563.pdf).",
        ]

    current = "electronic_capacitor_0402_56_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "56 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1572 / Fenghua 0402CG560J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 56 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 560 = 56 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 56 pF, 50 V, C0G, +/-5%, stock 15,509, minimum 1, full reel 10,000, available order qty 9,083, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987834956365824-C1572.pdf).",
        ]

    current = "electronic_capacitor_0603_82_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "82 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1708 / Fenghua 0603F823M500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 82 nF value; the populate row was added by this intake. The Fenghua ordering code (F = Y5V, 823 = 82 x 10^3 pF, M = +/-20%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 82 nF generic is distinct from the separate 0603 820 pF X7R generic supplied by C1632.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 82 nF, 50 V, Y5V, +/-20%, stock 20,949, minimum 1, full reel 4,000, available order qty 20,832, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988203677224960-C1708.pdf).",
        ]

    current = "electronic_capacitor_0603_56_nano_farad_fenghua_adv_tech_0603f563m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_56_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "56 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1706 / 0603F563M500NT purchasing variant; 0603, 56 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 56 nF definition. IMPORTANT dielectric difference: the reviewed preference C1629 / 0603B563K500NT on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1706 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988197532569600-C1706.pdf).",
        ]

    current = "electronic_capacitor_0603_4_7_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_4_7_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "10 V",
            "dielectric": "X5R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1705 / Samsung CL10A475KP8NNNC as the first reviewed preferred extended purchasing choice for this rated variant; 0603, 4.7 uF, 10 V, X5R, ±10% verified against the staged live JLC capture 2026-09-28. The Samsung ordering code (CL10 = 0603, A = X5R, 475 = 4.7 uF, K = ±10%, P8 = 10 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Linked to the generic 0603 4.7 uF definition as a lower-voltage purchasing variant (following the established 16_volt taxonomy of C78); the 16 V rated variant keeps its ID. Projects needing 16 V margin must not substitute this 10 V SKU.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178155313184768-C1705.pdf).",
        ]

    current = "electronic_capacitor_0805_8_2_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "8.2 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1758 / Fenghua 0805B822K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 8.2 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 822 = 8.2 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 8.2 nF generic supplied by C1634.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 8.2 nF, 50 V, X7R, +/-10%, stock 12,263, minimum 1, full reel 4,000, available order qty 12,173, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988621820649472-C1758.pdf).",
        ]

    current = "electronic_capacitor_0805_820_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "820 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1757 / Fenghua 0805B821K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 820 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 821 = 82 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 820 pF generic supplied by C1632.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 820 pF, 50 V, X7R, +/-10%, stock 6,409, minimum 1, full reel 4,000, available order qty 6,370, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988618456682496-C1757.pdf).",
        ]

    current = "electronic_capacitor_0805_68_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "68 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1756 / Fenghua 0805B683K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 68 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 683 = 68 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 68 nF, 50 V, X7R, +/-10%, stock 10,712, minimum 1, full reel 4,000, available order qty 10,617, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988615230722048-C1756.pdf).",
        ]

    current = "electronic_capacitor_0805_6_8_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "6.8 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1755 / Fenghua 0805B682K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 6.8 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 682 = 6.8 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 6.8 nF generic supplied by C1633.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 6.8 nF, 50 V, X7R, +/-10%, stock 56,942, minimum 1, full reel 4,000, available order qty 43,646, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988612143849472-C1755.pdf).",
        ]

    current = "electronic_capacitor_0805_680_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "680 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1754 / Fenghua 0805B681K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 680 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 681 = 68 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 680 pF generic supplied by C1630.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 680 pF, 50 V, X7R, +/-10%, stock 67,133, minimum 1, full reel 4,000, available order qty 59,199, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988607072800768-C1754.pdf).",
        ]

    current = "electronic_capacitor_0805_56_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "56 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1753 / Fenghua 0805B563K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 56 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 563 = 56 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 56 nF generic supplied by C1629.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 56 nF, 50 V, X7R, +/-10%, stock 60, minimum 1, full reel 4,000, available order qty 53, MSL 1. Stock is very low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988603981733888-C1753.pdf).",
        ]

    current = "electronic_capacitor_0805_560_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "560 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1751 / Fenghua 0805B561K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 560 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 561 = 56 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 560 pF generic supplied by C1627.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 560 pF, 50 V, X7R, +/-10%, stock 8,137, minimum 1, full reel 4,000, available order qty 8,091, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988597451337728-C1751.pdf).",
        ]

    current = "electronic_capacitor_0805_5_1_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5.1 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1750 / Fenghua 0805B512K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 5.1 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 512 = 5.1 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 5.1 nF generic supplied by C1587.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 5.1 nF, 50 V, X7R, +/-10%, stock 13,544, minimum 1, full reel 4,000, available order qty 13,499, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988594175315968-C1750.pdf).",
        ]

    current = "electronic_capacitor_0805_510_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "510 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1749 / Fenghua 0805B511K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 510 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 511 = 51 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 510 pF generic supplied by C1626.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 510 pF, 50 V, X7R, +/-10%, stock 470, minimum 1, full reel 4,000, available order qty 441, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988591037976576-C1749.pdf).",
        ]

    current = "electronic_capacitor_0805_5_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1748 / Fenghua 0805B502K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 5 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 502 = 5 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 5 nF generic supplied by C1625.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 5 nF, 50 V, X7R, +/-10%, stock 8,285, minimum 1, full reel 4,000, available order qty 8,241, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988587611770880-C1748.pdf).",
        ]

    current = "electronic_capacitor_0805_500_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "500 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1747 / Fenghua 0805B501K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 500 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 501 = 50 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 500 pF generic supplied by C1624.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 500 pF, 50 V, X7R, +/-10%, stock 4,507, minimum 1, full reel 4,000, available order qty 4,489, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988584302600192-C1747.pdf).",
        ]

    current = "electronic_capacitor_0805_4_7_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_4_7_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "16 V",
            "dielectric": "X5R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1746 / Samsung CL21A475KOFNNNE as the first reviewed preferred extended purchasing choice for this rated variant; 0805, 4.7 uF, 16 V, X5R, ±10% verified against the staged live JLC capture 2026-09-28. The Samsung ordering code (CL21 = 0805, A = X5R, 475 = 4.7 uF, K = ±10%, OF = 16 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Linked to the generic 0805 4.7 uF definition as a lower-voltage purchasing variant (following the 0603 16_volt C78 precedent); the reviewed Basic 25 V preference C1779 / CL21A475KAQNNNE on the generic ID remains unchanged. Projects needing 25 V margin must not substitute this 16 V SKU.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178171934400512-C1746.pdf).",
        ]

    current = "electronic_capacitor_0805_47_nano_farad_fenghua_adv_tech_0805b473k500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_47_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "47 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1745 / 0805B473K500NT purchasing variant; 0805, 47 nF, 50 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 47 nF definition. The reviewed Basic preference C53134 / CL21B473KBCNNNC (Samsung, same 47 nF 50 V X7R ±10% spec) keeps the plain generic ID; the registry allows one preferred code per ID, so this equivalent-spec FH SKU is recorded as its own exact variant ID following the established maker/mpn variant taxonomy.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988580967993344-C1745.pdf).",
        ]

    current = "electronic_capacitor_0603_47_nano_farad_fenghua_adv_tech_0603f473m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_47_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "47 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1703 / 0603F473M500NT purchasing variant; 0603, 47 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 47 nF definition. IMPORTANT dielectric difference: the reviewed preference on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1703 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988190515499008-C1703.pdf).",
        ]

    current = "electronic_capacitor_0603_330_nano_farad_fenghua_adv_tech_0603f334m250nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_330_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "330 nF",
            "rated_voltage": "25 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1702 / 0603F334M250NT purchasing variant; 0603, 330 nF, 25 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 330 nF definition. IMPORTANT dielectric difference: the reviewed preference C1615 / 0603B334K250NT on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1702 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988187407654912-C1702.pdf).",
        ]

    current = "electronic_capacitor_0805_39_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "39 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1776 / Fenghua 0805F393M500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 39 nF value; the populate row was added by this intake. The Fenghua ordering code (F = Y5V, 393 = 39 nF, M = +/-20%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 39 nF, 50 V, Y5V, +/-20%, stock 5, minimum 1, full reel 4,000, available order qty 5, MSL 1. Stock is very low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990665372962816-C1776.pdf).",
        ]

    current = "electronic_capacitor_0805_82_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "82 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1782 / Fenghua 0805F823M500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 82 nF value; the populate row was added by this intake. The Fenghua ordering code (F = Y5V, 823 = 82 x 10^3 pF = 82 nF, M = +/-20%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0805 820 pF X7R generic supplied by C1757.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 82 nF, 50 V, Y5V, +/-20%, stock 83, minimum 1, full reel 4,000, available order qty 83. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990697418121216-C1782.pdf).",
        ]

    current = "electronic_capacitor_0805_680_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "680 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1783 / Fenghua 0805F684M500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 680 nF value; the populate row was added by this intake. The Fenghua ordering code (F = Y5V, 684 = 68 x 10^4 pF = 680 nF, M = +/-20%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 680 nF, 50 V, Y5V, +/-20%, stock 5, minimum 1, full reel 4,000, available order qty 4, MSL 1. Stock is very low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990703721889792-C1783.pdf).",
        ]

    current = "electronic_capacitor_0805_0_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "0.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1784 / Fenghua 0805CG0R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 0.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 0R5 = 0.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 0.5 pF generics supplied by C1544 and C1633.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 0.5 pF, 50 V, C0G, stock 7,460, minimum 1, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990710151757824-C1784.pdf).",
        ]

    current = "electronic_capacitor_0805_1_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1786 / Fenghua 0805CG1R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 1 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R0 = 1 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 1 pF generic supplied by C1550.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 1 pF, 50 V, C0G, stock 65,574, minimum 1, full reel 4,000, available order qty 65,385, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990716489351168-C1786.pdf).",
        ]

    current = "electronic_capacitor_0805_1_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1787 / Fenghua 0805CG1R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 1.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R2 = 1.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 1.2 pF generics supplied by C1551 and C1638.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 1.2 pF, 50 V, C0G, stock 995, minimum 1, full reel 4,000, available order qty 977, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990722822479872-C1787.pdf).",
        ]

    current = "electronic_capacitor_0805_1_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1788 / Fenghua 0805CG1R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 1.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R5 = 1.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 1.5 pF generics supplied by C1552 and C1639.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 1.5 pF, 50 V, C0G, stock 3,939, minimum 1, full reel 4,000, available order qty 3,879, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990729428914176-C1788.pdf).",
        ]

    current = "electronic_capacitor_0805_1_8_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.8 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1789 / Fenghua 0805CG1R8C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 1.8 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R8 = 1.8 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 1.8 pF generics supplied by C1553 and C1640.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 1.8 pF, 50 V, C0G, stock 1,711, minimum 1, full reel 4,000, available order qty 1,710, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990735971893248-C1789.pdf).",
        ]

    current = "electronic_capacitor_0805_1_nano_farad_samsung_electro_mechanics_cl21c102jbcnnnc"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_1_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 nF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1791 / CL21C102JBCNNNC purchasing variant; 0805, 1 nF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 113,668, minimum 1, full reel 4,000, available order qty 105,362, MSL 1).",
            "Linked to the generic 0805 1 nF definition. Dielectric difference: the reviewed Basic preference C46653 / CL21B102KBCNNNC (Samsung, X7R ±10%) on the generic ID keeps the preference slot, while this C1791 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 1 nF/0805 should pick this variant explicitly; the X7R Basic preference is not downgraded. The registry allows one preferred code per ID; C1791 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178187076243456-C1791.pdf).",
        ]

    current = "electronic_capacitor_0805_12_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "12 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1792 / Fenghua 0805CG120J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 12 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 120 = 12 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 12 pF generics supplied by C1547 and C38523.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 12 pF, 50 V, C0G, +/-5%, stock 113,778, minimum 1, full reel 4,000, available order qty 94,617, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990742267813888-C1792.pdf).",
        ]

    current = "electronic_capacitor_0805_120_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "120 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1793 / Fenghua 0805CG121J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 120 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 121 = 120 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the in-grid 0402 120 pF generic and the 0603 120 pF generic supplied by C1643.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 120 pF, 50 V, C0G, +/-5%, stock 5,462, minimum 1, full reel 4,000, available order qty 5,235, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991037391220736-C1793.pdf).",
        ]

    current = "electronic_capacitor_0805_33_nano_farad_fenghua_adv_tech_0805f333m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_33_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "33 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1774 / 0805F333M500NT purchasing variant; 0805, 33 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 33 nF definition. IMPORTANT dielectric difference: the reviewed Basic preference C1739 / 0805B333K500NT (same maker, X7R ±10%) on the generic ID is far more stable than this Y5V ±20% SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1774 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990647203778560-C1774.pdf).",
        ]

    current = "electronic_capacitor_0805_27_nano_farad_fenghua_adv_tech_0805f273m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_27_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "27 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1773 / 0805F273M500NT purchasing variant; 0805, 27 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 27 nF definition. IMPORTANT dielectric difference: the reviewed preference C1734 / 0805B273K500NT on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1773 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990640631304192-C1773.pdf).",
        ]

    current = "electronic_capacitor_0805_220_nano_farad_fenghua_adv_tech_0805f224m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_220_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "220 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1770 / 0805F224M500NT purchasing variant; 0805, 220 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 220 nF definition. IMPORTANT dielectric difference: the reviewed Basic preference C5378 / CL21B224KBFNNNE (Samsung, X7R ±10%) on the generic ID is far more stable than this Y5V ±20% SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1770 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990634163417088-C1770.pdf).",
        ]

    current = "electronic_capacitor_0805_20_nano_farad_fenghua_adv_tech_0805f203m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_20_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "20 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1768 / 0805F203M500NT purchasing variant; 0805, 20 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 20 nF definition. IMPORTANT dielectric difference: the reviewed preference C1726 / 0805B203K500NT on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1768 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988644578402304-C1768.pdf).",
        ]

    current = "electronic_capacitor_0805_18_nano_farad_fenghua_adv_tech_0805f183m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_18_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "18 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1767 / 0805F183M500NT purchasing variant; 0805, 18 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 18 nF definition. IMPORTANT dielectric difference: the reviewed preference C1723 / 0805B183K500NT on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1767 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988641038274560-C1767.pdf).",
        ]

    current = "electronic_capacitor_0805_120_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "120 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1764 / Fenghua 0805F124M500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 120 nF value; the populate row was added by this intake. The Fenghua ordering code (F = Y5V, 124 = 120 nF, M = +/-20%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 120 nF, 50 V, Y5V, +/-20%, stock 17, minimum 1, full reel 4,000, available order qty 17, MSL 1. Stock is very low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988627964628992-C1764.pdf).",
        ]

    current = "electronic_capacitor_0805_12_nano_farad_fenghua_adv_tech_0805f123m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_12_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "12 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1763 / 0805F123M500NT purchasing variant; 0805, 12 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 12 nF definition. IMPORTANT dielectric difference: the reviewed preference C1715 / 0805B123K500NT on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1763 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988624890339328-C1763.pdf).",
        ]

    current = "electronic_capacitor_0805_1_micro_farad_samsung_electro_mechanics_cl21f105zafnnne"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_1_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 uF",
            "rated_voltage": "25 V",
            "dielectric": "Y5V",
            "tolerance": "-20%~+80%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1761 / CL21F105ZAFNNNE purchasing variant; 0805, 1 uF, 25 V, Y5V, -20%~+80% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 1 uF definition. IMPORTANT dielectric difference: the reviewed Basic preference C28323 / CL21B105KBFNNNE (X7R ±10% 50 V) and the X7R 25 V rated variant C1712 on the generic family are far more stable than this Y5V -20/+80% SKU. It must never replace the X7R choices, and projects requiring X7R stability or tight tolerance must not substitute this SKU. The registry allows one preferred code per ID; C1761 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178179509719040-C1761.pdf).",
        ]

    current = "electronic_capacitor_0805_470_nano_farad_fenghua_adv_tech_0805f474m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_470_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "470 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1778 / 0805F474M500NT purchasing variant; 0805, 470 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28 (stock 3,831, minimum 1, full reel 4,000, available order qty 3,798).",
            "Linked to the generic 0805 470 nF definition. IMPORTANT dielectric difference: the reviewed Basic preference C13967 / CL21B474KBFNNNE (Samsung, X7R ±10% 50 V) on the generic ID is far more stable than this Y5V ±20% SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1778 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990678056808448-C1778.pdf).",
        ]

    current = "electronic_capacitor_0805_68_nano_farad_fenghua_adv_tech_0805f683m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_68_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "68 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1781 / 0805F683M500NT purchasing variant; 0805, 68 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28 (stock 92, minimum 1, full reel 4,000, available order qty 91).",
            "Linked to the generic 0805 68 nF definition. IMPORTANT dielectric difference: the reviewed preference C1756 / 0805B683K500NT on the generic ID is from the same maker (FH) but X7R ±10%, far more stable than this Y5V ±20% SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1781 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770990691084181504-C1781.pdf).",
        ]

    current = "electronic_capacitor_0603_33_nano_farad_fenghua_adv_tech_0603f333m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_33_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "33 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1701 / 0603F333M500NT purchasing variant; 0603, 33 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 33 nF definition. IMPORTANT dielectric difference: the reviewed Basic preference C21117 (Samsung, X7R ±10%) and the FH X7R variant C1614 (0603B333K500NT) on the generic family are far more stable than this Y5V ±20% SKU. It must never replace the X7R choices, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1701 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988184316993536-C1701.pdf).",
        ]

    current = "electronic_capacitor_0603_27_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "27 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1700 / Fenghua 0603F273M500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 27 nF value; the populate row was added by this intake. The Fenghua ordering code (F = Y5V, 273 = 27 x 10^3 pF, M = +/-20%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 27 nF, 50 V, Y5V, +/-20%, stock 8, minimum 1, full reel 4,000, available order qty 7, MSL 1. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988180763877376-C1700.pdf).",
        ]

    current = "electronic_capacitor_0603_220_nano_farad_samsung_electro_mechanics_cl10f224zb8nnnc"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_220_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "220 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "-20%~+80%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1698 / CL10F224ZB8NNNC purchasing variant; 0603, 220 nF, 50 V, Y5V, -20%~+80% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 220 nF definition. IMPORTANT dielectric difference: the reviewed Basic preference C21120 / CL10B224KA8NNNC (Samsung, X7R ±10% 25 V) and the FH X7R variant C1606 on the generic ID are far more stable than this Y5V -20/+80% SKU. It must never replace the X7R preferences, and projects requiring X7R stability or tight tolerance must not substitute this SKU. The registry allows one preferred code per ID; C1698 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178154017280000-C1698.pdf). Stock was 11 at capture (recorded as observed; low stock does not change identity).",
        ]

    current = "electronic_capacitor_0603_22_nano_farad_fenghua_adv_tech_0603f223m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_22_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "22 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1697 / 0603F223M500NT purchasing variant; 0603, 22 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 22 nF definition. IMPORTANT dielectric difference: the reviewed preference C1532 / 0603B223K500NT on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1697 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988177693917184-C1697.pdf).",
        ]

    current = "electronic_capacitor_0603_20_nano_farad_fenghua_adv_tech_0603f203m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_20_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "20 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1696 / 0603F203M500NT purchasing variant; 0603, 20 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 20 nF definition. IMPORTANT dielectric difference: the reviewed preference C1602 / 0603B203K500NT on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1696 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988174413971456-C1696.pdf).",
        ]

    current = "electronic_capacitor_0603_150_nano_farad_fenghua_adv_tech_0603f154m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_150_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "150 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1694 / 0603F154M500NT purchasing variant; 0603, 150 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 150 nF definition. IMPORTANT dielectric difference: the reviewed preference C1597 / 0603B154K500NT on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1694 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988167875186688-C1694.pdf).",
        ]

    current = "electronic_capacitor_0603_12_nano_farad_fenghua_adv_tech_0603f123m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_12_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "12 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1692 / 0603F123M500NT purchasing variant; 0603, 12 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 12 nF definition. IMPORTANT dielectric difference: the reviewed preference C1593 / 0603B123K500NT on the generic ID is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1692 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988161411358720-C1692.pdf).",
        ]

    current = "electronic_capacitor_0603_10_micro_farad_6_3_volt_20_percent"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_10_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "6.3 V",
            "dielectric": "X5R",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1691 / Samsung CL10A106MQ8NNNC as the first reviewed preferred extended purchasing choice for this rated variant; 0603, 10 uF, 6.3 V, X5R, ±20% verified against the staged live JLC capture 2026-09-28. The Samsung ordering code (CL10 = 0603, A = X5R, 106 = 10 uF, M = ±20%, Q8 = 6.3 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Linked to the generic 0603 10 uF definition as a lower-voltage, wider-tolerance purchasing variant (following the established 25_volt_20_percent taxonomy); the reviewed Basic 10 V ±10% preference C19702 and the 25 V ±20% rated variant C96446 remain unchanged. Projects needing 10 V margin or ±10% tolerance must not substitute this SKU.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178152725164032-C1691.pdf).",
        ]

    current = "electronic_capacitor_0805_3_9_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.9 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1742 / Fenghua 0805B392K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 3.9 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 392 = 3.9 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 3.9 nF generic supplied by C1618.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 3.9 nF, 50 V, X7R, +/-10%, stock 8,961, minimum 1, full reel 4,000, available order qty 8,804, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988571316629504-C1742.pdf).",
        ]

    current = "electronic_capacitor_0805_390_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "390 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1741 / Fenghua 0805B391K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 390 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 391 = 39 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 390 pF generic supplied by C1617.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 390 pF, 50 V, X7R, +/-10%, stock 23,500, minimum 1, full reel 4,000, available order qty 22,960, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988568221233152-C1741.pdf).",
        ]

    current = "electronic_capacitor_0805_330_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "330 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1740 / Fenghua 0805B334K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 330 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 334 = 330 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 330 nF generic supplied by C1615.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 330 nF, 50 V, X7R, +/-10%, stock 36,393, minimum 1, full reel 4,000, available order qty 19,041, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988564983095296-C1740.pdf).",
        ]

    current = "electronic_capacitor_0805_3_3_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.3 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1738 / Fenghua 0805B332K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 3.3 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 332 = 3.3 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 3.3 nF generic supplied by C1576.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 3.3 nF, 50 V, X7R, +/-10%, stock 53,456, minimum 1, full reel 4,000, available order qty 47,565, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988555491926016-C1738.pdf).",
        ]

    current = "electronic_capacitor_0805_330_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "330 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1737 / Fenghua 0805B331K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 330 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 331 = 33 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 330 pF generic supplied by C1612.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 330 pF, 50 V, X7R, +/-10%, stock 76,097, minimum 1, full reel 4,000, available order qty 71,892, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988552186273792-C1737.pdf).",
        ]

    current = "electronic_capacitor_0805_3_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1736 / Fenghua 0805B302K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 3 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 302 = 3 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 3 nF generic supplied by C1611.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 3 nF, 50 V, X7R, +/-10%, stock 21,752, minimum 1, full reel 4,000, available order qty 21,658, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988548852342784-C1736.pdf).",
        ]

    current = "electronic_capacitor_0805_300_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "300 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1735 / Fenghua 0805B301K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 300 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 301 = 30 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 300 pF generic supplied by C1610.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 300 pF, 50 V, X7R, +/-10%, stock 6,787, minimum 1, full reel 4,000, available order qty 6,746, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988543763976192-C1735.pdf).",
        ]

    current = "electronic_capacitor_0805_27_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "27 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1734 / Fenghua 0805B273K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 27 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 273 = 27 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 27 nF generic supplied by C1700.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 27 nF, 50 V, X7R, +/-10%, stock 15, minimum 1, full reel 4,000, available order qty 10, MSL 1. Stock is very low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988540492959744-C1734.pdf).",
        ]

    current = "electronic_capacitor_0805_2_7_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.7 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1733 / Fenghua 0805B272K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 2.7 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 272 = 2.7 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 2.7 nF generic supplied by C1609.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 2.7 nF, 50 V, X7R, +/-10%, stock 10,087, minimum 1, full reel 4,000, available order qty 10,023, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988537414475776-C1733.pdf).",
        ]

    current = "electronic_capacitor_0805_270_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "270 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1732 / Fenghua 0805B271K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 270 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 271 = 27 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 270 pF generic supplied by C1608.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 270 pF, 50 V, X7R, +/-10%, stock 1,985, minimum 1, full reel 4,000, available order qty 1,946, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988534004371456-C1732.pdf).",
        ]

    current = "electronic_capacitor_0805_2_2_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_2_2_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 uF",
            "rated_voltage": "16 V",
            "dielectric": "X5R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1731 / Samsung CL21A225KOFNNNE as the first reviewed preferred extended purchasing choice for this rated variant; 0805, 2.2 uF, 16 V, X5R, ±10% verified against the staged live JLC capture 2026-09-28. The Samsung ordering code (CL21 = 0805, A = X5R, 225 = 2.2 uF, K = ±10%, OF = 16 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Linked to the generic 0805 2.2 uF definition as a lower-voltage purchasing variant; the reviewed Basic 50 V preference C377773 / CL21A225KBQNNNE on the generic ID remains unchanged. Projects needing 50 V margin must not substitute this 16 V SKU.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178168222846976-C1731.pdf).",
        ]

    current = "electronic_capacitor_0805_2_2_nano_farad_samsung_electro_mechanics_cl21b222kbannnc"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_2_2_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1728 / CL21B222KBANNNC purchasing variant; 0805, 2.2 nF, 50 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 2.2 nF definition. IMPORTANT dielectric difference: the reviewed Basic preference C28260 / CL21C222JBFNNNE (same maker, C0G ±5%) on the generic ID is more stable than this X7R ±10% SKU. Either may be selected deliberately per project stability requirements, but C1728 must not silently replace the C0G preference. The registry allows one preferred code per ID; C1728 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178164071026688-C1728.pdf).",
        ]

    current = "electronic_capacitor_0805_220_pico_farad_fenghua_adv_tech_0805b221k500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_220_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "220 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1727 / 0805B221K500NT purchasing variant; 0805, 220 pF, 50 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 220 pF definition. The reviewed Basic preference C107145 / CC0805KRX7R9BB221 (YAGEO, same 220 pF 50 V X7R ±10% spec) keeps the plain generic ID; the registry allows one preferred code per ID, so this equivalent-spec FH SKU is recorded as its own exact variant ID following the established maker/mpn variant taxonomy.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988530842001408-C1727.pdf).",
        ]

    current = "electronic_capacitor_0805_20_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "20 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1726 / Fenghua 0805B203K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 20 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 203 = 20 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 20 nF generic supplied by C1602.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 20 nF, 50 V, X7R, +/-10%, stock 3,612, minimum 1, full reel 4,000, available order qty 3,601, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988527448539136-C1726.pdf).",
        ]

    current = "electronic_capacitor_0805_2_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1725 / Fenghua 0805B202K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 2 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 202 = 2 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0402 2 nF generic supplied by C1601.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 2 nF, 50 V, X7R, +/-10%, stock 6,746, minimum 1, full reel 4,000, available order qty 6,662, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988524361801728-C1725.pdf).",
        ]

    current = "electronic_capacitor_0805_200_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "200 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1724 / Fenghua 0805B201K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 200 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 201 = 20 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0402 200 pF generic supplied by C1529 and 0603 200 pF generic supplied by C1600.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 200 pF, 50 V, X7R, +/-10%, stock 3,371, minimum 1, full reel 4,000, available order qty 1,605, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988521140035584-C1724.pdf).",
        ]

    current = "electronic_capacitor_0805_18_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "18 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1723 / Fenghua 0805B183K500NT as the first reviewed preferred extended purchasing choice for this in-grid generic 0805 18 nF value (the generic already exists in the 0805 capacitance_values grid, so no populate row was needed). The Fenghua ordering code (B = X7R, 183 = 18 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 18 nF, 50 V, X7R, +/-10%, stock 3,763, minimum 1, full reel 4,000, available order qty 3,754, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770997455402225664-C1723.pdf).",
        ]

    current = "electronic_capacitor_0805_1_8_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.8 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1722 / Fenghua 0805B182K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 1.8 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 182 = 1.8 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 1.8 nF generic supplied by C1599.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 1.8 nF, 50 V, X7R, +/-10%, stock 5,862, minimum 1, full reel 4,000, available order qty 5,635, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988239954165760-C1722.pdf).",
        ]

    current = "electronic_capacitor_0805_180_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "180 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1721 / Fenghua 0805B181K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 180 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 181 = 18 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 180 pF generic supplied by C1598.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 180 pF, 50 V, X7R, +/-10%, stock 34,995, minimum 1, full reel 4,000, available order qty 34,747, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988236569092096-C1721.pdf).",
        ]

    current = "electronic_capacitor_0805_160_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "160 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1720 / Fenghua 0805B161K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 160 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 161 = 16 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 160 pF, 50 V, X7R, +/-10%, stock 3,713, minimum 1, full reel 4,000, available order qty 3,713, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988233179959296-C1720.pdf).",
        ]

    current = "electronic_capacitor_0805_150_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "150 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1719 / Fenghua 0805B154K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 150 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 154 = 150 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 150 nF generic supplied by C1597.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 150 nF, 50 V, X7R, +/-10%, stock 4,475, minimum 1, full reel 4,000, available order qty 3,872, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988229820321792-C1719.pdf).",
        ]

    current = "electronic_capacitor_0805_15_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "15 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1718 / Fenghua 0805B153K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 15 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 153 = 15 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 15 nF generic supplied by C1596.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 15 nF, 50 V, X7R, +/-10%, stock 866, minimum 1, full reel 4,000, available order qty 784, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988226121621504-C1718.pdf).",
        ]

    current = "electronic_capacitor_0805_1_5_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.5 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1717 / Fenghua 0805B152K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 1.5 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 152 = 1.5 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0402 1.5 nF generic supplied by C1552 and 0603 1.5 nF generic supplied by C1595.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 1.5 nF, 50 V, X7R, +/-10%, stock 52,913, minimum 1, full reel 4,000, available order qty 40,184, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988222879289344-C1717.pdf).",
        ]

    current = "electronic_capacitor_0805_150_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "150 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1716 / Fenghua 0805B151K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 150 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 151 = 15 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 150 pF, 50 V, X7R, +/-10%, stock 83,419, minimum 1, full reel 4,000, available order qty 77,998, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988216164073472-C1716.pdf).",
        ]

    current = "electronic_capacitor_0805_150_pico_farad_fenghua_adv_tech_0805cg151j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_150_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "150 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1795 / 0805CG151J500NT purchasing variant; 0805, 150 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 2,917, minimum 1, full reel 4,000, available order qty 2,910, MSL 1).",
            "Linked to the generic 0805 150 pF definition. Dielectric difference: the reviewed preference C1716 / 0805B151K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1795 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 150 pF/0805 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1795 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991044034863104-C1795.pdf).",
        ]

    current = "electronic_capacitor_0805_16_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "16 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1796 / Fenghua 0805CG160J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 16 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 160 = 16 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 16 pF generic supplied by C1646.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 16 pF, 50 V, C0G, +/-5%, stock 1,412, minimum 1, full reel 4,000, available order qty 1,260, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991047226728448-C1796.pdf).",
        ]

    current = "electronic_capacitor_0805_18_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "18 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1797 / Fenghua 0805CG180J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 18 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 180 = 18 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the in-grid 0402 18 pF generic and the 0603 18 pF generic supplied by C1647.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 18 pF, 50 V, C0G, +/-5%, stock 153,087, minimum 1, full reel 4,000, available order qty 142,930, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991054005264384-C1797.pdf).",
        ]

    current = "electronic_capacitor_0805_200_pico_farad_fenghua_adv_tech_0805cg201j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_200_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "200 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1799 / 0805CG201J500NT purchasing variant; 0805, 200 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 6,903, minimum 1, full reel 4,000, available order qty 6,857, MSL 1).",
            "Linked to the generic 0805 200 pF definition. Dielectric difference: the reviewed preference C1724 / 0805B201K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1799 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 200 pF/0805 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1799 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991060758093824-C1799.pdf).",
        ]

    current = "electronic_capacitor_0805_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1800 / Fenghua 0805CG2R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R0 = 2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 2 pF generics supplied by C1558 and C1650.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 2 pF, 50 V, C0G, stock 0, minimum 950, full reel 4,000 (listed as pre-order/reel purchasing with no available order quantity), MSL 1; the live page lists no tolerance row. The zero stock and 950-piece minimum are purchasing conditions recorded as observed and do not change the verified identity. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991067456126976-C1800.pdf).",
        ]

    current = "electronic_capacitor_0805_2_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1801 / Fenghua 0805CG2R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 2.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R2 = 2.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 2.2 pF generics supplied by C1559 and C1651.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 2.2 pF, 50 V, C0G, stock 28,355, minimum 1, full reel 4,000, available order qty 28,245, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991073961627648-C1801.pdf).",
        ]

    current = "electronic_capacitor_0805_2_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1802 / Fenghua 0805CG2R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 2.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R5 = 2.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 2.5 pF generics supplied by C1560 and C1652.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 2.5 pF, 50 V, C0G, stock 3,312, minimum 1, full reel 4,000, available order qty 3,312, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991080474841088-C1802.pdf).",
        ]

    current = "electronic_capacitor_0805_2_7_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.7 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1803 / Fenghua 0805CG2R7C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 2.7 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R7 = 2.7 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 2.7 pF generic supplied by C1561.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 2.7 pF, 50 V, C0G, stock 24,381, minimum 1, full reel 4,000, available order qty 24,198, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991087395442688-C1803.pdf).",
        ]

    current = "electronic_capacitor_0805_220_pico_farad_fenghua_adv_tech_0805cg221j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_220_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "220 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1805 / 0805CG221J500NT purchasing variant; 0805, 220 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 3,293, minimum 1, full reel 4,000, available order qty 3,249, MSL 1).",
            "Linked to the generic 0805 220 pF definition. The reviewed preference C107145 / CC0805KRX7R9BB221 (Yageo, X7R ±10%) keeps the generic preference slot and the sibling FH X7R variant C1727 / 0805B221K500NT already exists; this C1805 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the family. Projects needing C0G stability at 220 pF/0805 should pick this variant explicitly; neither X7R choice is downgraded. The registry allows one preferred code per ID; C1805 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991093494501376-C1805.pdf).",
        ]

    current = "electronic_capacitor_0805_24_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "24 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1806 / Fenghua 0805CG240J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 24 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 240 = 24 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 24 pF generic supplied by C1654.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 24 pF, 50 V, C0G, +/-5%, stock 3,683, minimum 1, full reel 4,000, available order qty 3,055, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991099827630080-C1806.pdf).",
        ]

    current = "electronic_capacitor_0805_25_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "25 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1807 / Fenghua 0805CG250J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 25 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 250 = 25 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 25 pF generics supplied by C1556 and C1655.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 25 pF, 50 V, C0G, +/-5%, stock 4,365, minimum 1, full reel 4,000, available order qty 4,320, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991106265616385-C1807.pdf).",
        ]

    current = "electronic_capacitor_0805_27_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "27 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1808 / Fenghua 0805CG270J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 27 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 270 = 27 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the in-grid 0402 27 pF generic and the 0603 27 pF generic supplied by C1656.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 27 pF, 50 V, C0G, +/-5%, stock 64,409, minimum 1, full reel 4,000, available order qty 62,858, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991112624586752-C1808.pdf).",
        ]

    current = "electronic_capacitor_0805_3_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1810 / Fenghua 0805CG3R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 3 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R0 = 3 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 3 pF generic supplied by C1564.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 3 pF, 50 V, C0G, stock 4,129, minimum 1, full reel 4,000, available order qty 4,115, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991119108710400-C1810.pdf).",
        ]

    current = "electronic_capacitor_0805_3_3_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.3 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1811 / Fenghua 0805CG3R3C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 3.3 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R3 = 3.3 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 3.3 pF generics supplied by C1565 and C1660.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 3.3 pF, 50 V, C0G, stock 2,364, minimum 1, full reel 4,000, available order qty 2,328, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991125391777792-C1811.pdf).",
        ]

    current = "electronic_capacitor_0805_3_6_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.6 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1812 / Fenghua 0805CG3R6C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 3.6 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R6 = 3.6 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 3.6 pF generic supplied by C1661.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 3.6 pF, 50 V, C0G, stock 583, minimum 1, full reel 4,000, available order qty 573, MSL 1; the live page lists no tolerance row. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991131838558208-C1812.pdf).",
        ]

    current = "electronic_capacitor_0805_3_9_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.9 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1813 / Fenghua 0805CG3R9C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 3.9 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R9 = 3.9 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 3.9 pF generics supplied by C1566 and C1662.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 3.9 pF, 50 V, C0G, stock 2,903, minimum 1, full reel 4,000, available order qty 2,887, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991135127298048-C1813.pdf).",
        ]

    current = "electronic_capacitor_0805_330_pico_farad_fenghua_adv_tech_0805cg331j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_330_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "330 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1815 / 0805CG331J500NT purchasing variant; 0805, 330 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 24,045, minimum 1, full reel 4,000, available order qty 23,803, MSL 1).",
            "Linked to the generic 0805 330 pF definition. Dielectric difference: the reviewed preference C1737 / 0805B331K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1815 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 330 pF/0805 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1815 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991141460561920-C1815.pdf).",
        ]

    current = "electronic_capacitor_0805_36_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "36 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1816 / Fenghua 0805CG360J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 36 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 360 = 36 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 36 pF generic supplied by C1665.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 36 pF, 50 V, C0G, +/-5%, stock 1,729, minimum 1, full reel 4,000, available order qty 1,709, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991147877711872-C1816.pdf).",
        ]

    current = "electronic_capacitor_0805_39_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "39 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1817 / Fenghua 0805CG390J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 39 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 390 = 39 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 39 pF generics supplied by C1563 and C1666.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 39 pF, 50 V, C0G, +/-5%, stock 16,265, minimum 1, full reel 4,000, available order qty 16,150, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991154160914432-C1817.pdf).",
        ]

    current = "electronic_capacitor_0805_390_pico_farad_fenghua_adv_tech_0805cg391j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_390_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "390 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1818 / 0805CG391J500NT purchasing variant; 0805, 390 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 3,782, minimum 1, full reel 4,000, available order qty 3,782, MSL 1).",
            "Linked to the generic 0805 390 pF definition. Dielectric difference: the reviewed preference C1741 / 0805B391K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1818 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 390 pF/0805 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1818 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991160514879488-C1818.pdf).",
        ]

    current = "electronic_capacitor_0805_4_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1819 / Fenghua 0805CG4R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 4 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 4R0 = 4 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 4 pF generics supplied by C1568 and C1668.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 4 pF, 50 V, C0G, stock 6,689, minimum 1, full reel 4,000, available order qty 6,667, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991167078830080-C1819.pdf).",
        ]

    current = "electronic_capacitor_0805_4_7_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1820 / Fenghua 0805CG4R7C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 4.7 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 4R7 = 4.7 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 4.7 pF generics supplied by C1569 and C1669.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 4.7 pF, 50 V, C0G, stock 14,023, minimum 1, full reel 4,000, available order qty 13,881, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991173429141504-C1820.pdf).",
        ]

    current = "electronic_capacitor_0805_470_pico_farad_fenghua_adv_tech_0805cg471j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_470_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "470 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1822 / 0805CG471J500NT purchasing variant; 0805, 470 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 39,102, minimum 1, full reel 4,000, available order qty 38,943, MSL 1).",
            "Linked to the generic 0805 470 pF definition. Dielectric difference: the reviewed preference C1743 / 0805B471K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1822 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 470 pF/0805 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1822 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991179624398848-C1822.pdf).",
        ]

    current = "electronic_capacitor_0805_50_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "50 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1823 / Fenghua 0805CG500J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 50 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 500 = 50 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 50 pF generic supplied by C1672.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 50 pF, 50 V, C0G, +/-5%, stock 20,176, minimum 1, full reel 4,000, available order qty 19,984, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991186151006208-C1823.pdf).",
        ]

    current = "electronic_capacitor_0805_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1824 / Fenghua 0805CG5R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 5R0 = 5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 5 pF generics supplied by C1573 and C1673.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 5 pF, 50 V, C0G, stock 27,853, minimum 1, full reel 4,000, available order qty 27,686, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991192488329216-C1824.pdf).",
        ]

    current = "electronic_capacitor_0805_5_1_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5.1 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1825 / Fenghua 0805CG5R1C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 5.1 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 5R1 = 5.1 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. No 5.1 pF generic exists in any other package.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 5.1 pF, 50 V, C0G, stock 3,093, minimum 1, full reel 4,000, available order qty 3,055, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991198544633857-C1825.pdf).",
        ]

    current = "electronic_capacitor_0805_5_6_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5.6 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1826 / Fenghua 0805CG5R6C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 5.6 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 5R6 = 5.6 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 5.6 pF generics supplied by C1574 and C1674.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 5.6 pF, 50 V, C0G, stock 7,614, minimum 1, full reel 4,000, available order qty 7,570, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991205939732480-C1826.pdf).",
        ]

    current = "electronic_capacitor_0805_51_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "51 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1827 / Fenghua 0805CG510J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 51 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 510 = 51 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 51 pF generics supplied by C1571 and C1675.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 51 pF, 50 V, C0G, +/-5%, stock 3,481, minimum 1, full reel 4,000, available order qty 3,437, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991212088582144-C1827.pdf).",
        ]

    current = "electronic_capacitor_0805_56_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "56 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1828 / Fenghua 0805CG560J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 56 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 560 = 56 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 56 pF generics supplied by C1572 and C1676.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 56 pF, 50 V, C0G, +/-5%, stock 19,293, minimum 1, full reel 4,000, available order qty 17,657, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991218249609216-C1828.pdf).",
        ]

    current = "electronic_capacitor_0805_560_pico_farad_fenghua_adv_tech_0805cg561j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_560_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "560 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1829 / 0805CG561J500NT purchasing variant; 0805, 560 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 7,544, minimum 1, full reel 4,000, available order qty 7,452, MSL 1).",
            "Linked to the generic 0805 560 pF definition. Dielectric difference: the reviewed preference C1751 / 0805B561K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1829 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 560 pF/0805 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1829 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991224310378496-C1829.pdf).",
        ]

    current = "electronic_capacitor_0805_6_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "6.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1831 / Fenghua 0805CG6R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 6.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 6R2 = 6.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 6.2 pF generic supplied by C1678.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 6.2 pF, 50 V, C0G, stock 3,868, minimum 1, full reel 4,000, available order qty 3,861, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991227598848000-C1831.pdf).",
        ]

    current = "electronic_capacitor_0805_6_8_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "6.8 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1832 / Fenghua 0805CG6R8C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 6.8 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 6R8 = 6.8 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 6.8 pF generics supplied by C1576 and C1679.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 6.8 pF, 50 V, C0G, stock 37,969, minimum 1, full reel 4,000, available order qty 37,817, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991234293092352-C1832.pdf).",
        ]

    current = "electronic_capacitor_0805_62_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "62 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1833 / Fenghua 0805CG620J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 62 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 620 = 62 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. No 62 pF generic exists in any other package.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 62 pF, 50 V, C0G, +/-5%, stock 3,370, minimum 1, full reel 4,000, available order qty 3,370, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991240576159744-C1833.pdf).",
        ]

    current = "electronic_capacitor_0805_68_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "68 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1834 / Fenghua 0805CG680J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 68 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 680 = 68 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 68 pF generic supplied by C1680.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 68 pF, 50 V, C0G, +/-5%, stock 19,989, minimum 1, full reel 4,000, available order qty 19,603, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991246896975872-C1834.pdf).",
        ]

    current = "electronic_capacitor_0805_680_pico_farad_fenghua_adv_tech_0805cg681j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_680_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "680 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1835 / 0805CG681J500NT purchasing variant; 0805, 680 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 4,717, minimum 1, full reel 4,000, available order qty 4,685, MSL 1).",
            "Linked to the generic 0805 680 pF definition. Dielectric difference: the reviewed preference C1754 / 0805B681K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1835 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 680 pF/0805 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1835 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991251875479552-C1835.pdf).",
        ]

    current = "electronic_capacitor_0805_7_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "7 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1836 / Fenghua 0805CG7R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 7 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 7R0 = 7 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 7 pF generics supplied by C1577 and C1682.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 7 pF, 50 V, C0G, stock 3,258, minimum 1, full reel 4,000, available order qty 3,255, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991256681746432-C1836.pdf).",
        ]

    current = "electronic_capacitor_0805_7_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "7.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1837 / Fenghua 0805CG7R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 7.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 7R5 = 7.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. No 7.5 pF generic exists in any other package.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 7.5 pF, 50 V, C0G, stock 496, minimum 1, full reel 4,000, available order qty 481, MSL 1; the live page lists no tolerance row. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991263019339776-C1837.pdf).",
        ]

    current = "electronic_capacitor_0805_75_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "75 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1838 / Fenghua 0805CG750J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 75 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 750 = 75 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 75 pF generic supplied by C1681.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 75 pF, 50 V, C0G, +/-5%, stock 2,426, minimum 1, full reel 4,000, available order qty 2,339, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991269151952896-C1838.pdf).",
        ]

    current = "electronic_capacitor_0805_8_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "8 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1839 / Fenghua 0805CG8R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 8 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 8R0 = 8 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the in-grid 0402 8 pF generic supplied by C1578.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 8 pF, 50 V, C0G, stock 2,658, minimum 1, full reel 4,000, available order qty 2,594, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991275808313344-C1839.pdf).",
        ]

    current = "electronic_capacitor_0805_8_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "8.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1840 / Fenghua 0805CG8R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 8.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 8R2 = 8.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 8.2 pF generics supplied by C1579 and C1685.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 8.2 pF, 50 V, C0G, stock 34,547, minimum 1, full reel 4,000, available order qty 34,116, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991282019942400-C1840.pdf).",
        ]

    current = "electronic_capacitor_0805_82_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "82 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1841 / Fenghua 0805CG820J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 82 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 820 = 82 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 82 pF generic supplied by C1683.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 82 pF, 50 V, C0G, +/-5%, stock 23,455, minimum 1, full reel 4,000, available order qty 23,228, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991288257142784-C1841.pdf).",
        ]

    current = "electronic_capacitor_0805_820_pico_farad_fenghua_adv_tech_0805cg821j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_820_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "820 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1842 / 0805CG821J500NT purchasing variant; 0805, 820 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 7,198, minimum 1, full reel 4,000, available order qty 6,998, MSL 1).",
            "Linked to the generic 0805 820 pF definition. Dielectric difference: the reviewed preference C1757 / 0805B821K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1842 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 820 pF/0805 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1842 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991294472560640-C1842.pdf).",
        ]

    current = "electronic_capacitor_0805_91_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "91 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1843 / Fenghua 0805CG910J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 91 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 910 = 91 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 91 pF generic supplied by C1686.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 91 pF, 50 V, C0G, +/-5%, stock 3,648, minimum 1, full reel 4,000, available order qty 3,630, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991301275721728-C1843.pdf).",
        ]

    current = "electronic_capacitor_0805_9_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "9 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1844 / Fenghua 0805CG9R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 9 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 9R0 = 9 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 9 pF generic supplied by C1580.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 9 pF, 50 V, C0G, stock 4,793, minimum 1, full reel 4,000, available order qty 4,731, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991307424436224-C1844.pdf).",
        ]

    current = "electronic_capacitor_1206_1_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1845 / Fenghua 1206B102K500NT as the first reviewed preferred extended purchasing choice for this previously absent plain 1206 1 nF generic; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 102 = 1 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 1206 1 nF 2000 V rated variant supplied by C9196.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 1 nF, 50 V, X7R, +/-10%, stock 118,007, minimum 1, full reel 4,000, available order qty 116,350, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991310558257152-C1845.pdf).",
        ]

    current = "electronic_capacitor_1206_10_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_10_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "16 V",
            "dielectric": "X5R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1849 / CL31A106KOHNNNE rated purchasing variant; 1206, 10 uF, 16 V, X5R, ±10% verified against the staged live JLC capture 2026-09-28 (stock 235,191, minimum 1, full reel 2,000, available order qty 209,883, MSL 1). The Samsung ordering code (KO = X5R 16 V) decodes consistently with the listed specifications.",
            "Linked to the generic 1206 10 uF definition. IMPORTANT rating difference: the reviewed preference C13585 / CL31A106KBHNNNE on the generic ID is the 50 V rated part; this C1849 SKU is the 16 V part and must never silently replace it in circuits that need the higher rating. It exists so projects that only need 16 V at 1206/10 uF can pick the cheaper exact SKU explicitly. The registry allows one preferred code per ID; C1849 is recorded as its own exact rated-variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178189756674048-C1849.pdf).",
        ]

    current = "electronic_capacitor_1206_150_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "150 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1850 / Fenghua 1206B151K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 150 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 151 = 15 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 150 pF generics supplied by C1552 and C1639.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 150 pF, 50 V, X7R, +/-10%, stock 9, minimum 1, full reel 4,000, available order qty 5, MSL 1. Stock is very low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991323648544768-C1850.pdf).",
        ]

    current = "electronic_capacitor_1206_1_5_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.5 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1851 / Fenghua 1206B152K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 1.5 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 152 = 1.5 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 1.5 nF generics supplied by C1552 and C1595 and the 0805 1.5 nF generic supplied by C1717.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 1.5 nF, 50 V, X7R, +/-10%, stock 2,091, minimum 1, full reel 4,000, available order qty 2,040, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991330132533248-C1851.pdf).",
        ]

    current = "electronic_capacitor_1206_20_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "20 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1853 / Fenghua 1206B203K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 20 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 203 = 20 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0805 20 nF generic supplied by C1726.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 20 nF, 50 V, X7R, +/-10%, stock 3,853, minimum 1, full reel 4,000, available order qty 3,845, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991343998902272-C1853.pdf).",
        ]

    current = "electronic_capacitor_1206_220_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "220 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1854 / Fenghua 1206B221K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 220 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 221 = 22 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 220 pF generics supplied by C1530 and C1603 and the 0805 220 pF generic supplied by C107145.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 220 pF, 50 V, X7R, +/-10%, stock 18,561, minimum 1, full reel 4,000, available order qty 18,503, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991350555140096-C1854.pdf).",
        ]

    current = "electronic_capacitor_1206_2_2_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1855 / Fenghua 1206B222K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 2.2 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 222 = 2.2 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 2.2 nF generics supplied by C1531, C1604 and C28260.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 2.2 nF, 50 V, X7R, +/-10%, stock 66,653, minimum 1, full reel 4,000, available order qty 65,626, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991356603191296-C1855.pdf).",
        ]

    current = "electronic_capacitor_1206_22_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "22 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1856 / Fenghua 1206B223K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 22 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 223 = 22 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 22 nF generics supplied by C1532, C21122 and C1729.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 22 nF, 50 V, X7R, +/-10%, stock 15,398, minimum 1, full reel 4,000, available order qty 15,112, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991362919542784-C1856.pdf).",
        ]

    current = "electronic_capacitor_1206_220_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "220 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1857 / Fenghua 1206B224K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 220 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 224 = 220 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 220 nF generics supplied by C16772, C21120 and C5378.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 220 nF, 50 V, X7R, +/-10%, stock 68,569, minimum 1, full reel 4,000, available order qty 36,394, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991369147949056-C1857.pdf).",
        ]

    current = "electronic_capacitor_1206_22_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_22_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "22 uF",
            "rated_voltage": "10 V",
            "dielectric": "X5R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1859 / 1206X226K100NT rated purchasing variant; 1206, 22 uF, 10 V, X5R, ±10% verified against the staged live JLC capture 2026-09-28 (stock 76,002, minimum 1, full reel 2,000, available order qty 75,945, MSL 1). The Fenghua ordering code (X = X5R, 226 = 22 uF, K = +/-10%, 100 = 10 V) decodes consistently with the listed specifications.",
            "Linked to the generic 1206 22 uF definition. IMPORTANT rating difference: the reviewed preference C12891 / CL31A226KAHNNNE on the generic ID is the 25 V rated part; this C1859 SKU is the 10 V part and must never silently replace it in circuits that need the higher rating. It exists so projects that only need 10 V at 1206/22 uF can pick the exact SKU explicitly. The registry allows one preferred code per ID; C1859 is recorded as its own exact rated-variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991381764550656-C1859.pdf).",
        ]

    current = "electronic_capacitor_1206_2_7_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.7 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1860 / Fenghua 1206B272K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 2.7 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 272 = 2.7 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 2.7 nF generics supplied by C1609 and C1733.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 2.7 nF, 50 V, X7R, +/-10%, stock 3,025, minimum 1, full reel 4,000, available order qty 3,015, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991387984568320-C1860.pdf).",
        ]

    current = "electronic_capacitor_1206_330_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "330 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1862 / Fenghua 1206B331K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 330 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 331 = 33 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 330 pF generics supplied by C1535, C1664 and C1737.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 330 pF, 50 V, X7R, +/-10%, stock 3,020, minimum 1, full reel 4,000, available order qty 3,006, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991397107585024-C1862.pdf).",
        ]

    current = "electronic_capacitor_1206_3_3_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.3 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1863 / Fenghua 1206B332K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 3.3 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 332 = 3.3 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 3.3 nF generics supplied by C1536, C1613 and C1738.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 3.3 nF, 50 V, X7R, +/-10%, stock 8,477, minimum 1, full reel 4,000, available order qty 8,439, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991403604426752-C1863.pdf).",
        ]

    current = "electronic_capacitor_1206_33_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "33 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1864 / Fenghua 1206B333K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 33 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 333 = 33 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 33 nF generics supplied by C21117 and C1739.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 33 nF, 50 V, X7R, +/-10%, stock 3,294, minimum 1, full reel 4,000, available order qty 3,278, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991410004529152-C1864.pdf).",
        ]

    current = "electronic_capacitor_1206_330_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "330 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1865 / Fenghua 1206B334K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 330 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 334 = 330 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 330 nF generics supplied by C1615 and C1740.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 330 nF, 50 V, X7R, +/-10%, stock 8,848, minimum 1, full reel 4,000, available order qty 8,830, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991416459563008-C1865.pdf).",
        ]

    current = "electronic_capacitor_1206_390_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "390 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1866 / Fenghua 1206B391K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 390 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 391 = 39 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 390 pF generics supplied by C1617 and C1741.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 390 pF, 50 V, X7R, +/-10%, stock 995, minimum 1, full reel 4,000, available order qty 935, MSL 1. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991422973452288-C1866.pdf).",
        ]

    current = "electronic_capacitor_1206_3_9_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.9 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1867 / Fenghua 1206B392K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 3.9 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 392 = 3.9 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 3.9 nF generics supplied by C1618 and C1742.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 3.9 nF, 50 V, X7R, +/-10%, stock 2,588, minimum 1, full reel 4,000, available order qty 2,579, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991429361242112-C1867.pdf).",
        ]

    current = "electronic_capacitor_1206_470_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "470 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1868 / Fenghua 1206B471K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 470 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 471 = 47 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 470 pF generics supplied by C1537, C1620 and C1743.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 470 pF, 50 V, X7R, +/-10%, stock 8,757, minimum 1, full reel 4,000, available order qty 8,704, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991436664066048-C1868.pdf).",
        ]

    current = "electronic_capacitor_1206_4_7_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1869 / Fenghua 1206B472K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 4.7 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 472 = 4.7 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 4.7 nF generics supplied by C1538, C53987 and C1744.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 4.7 nF, 50 V, X7R, +/-10%, stock 16,227, minimum 1, full reel 4,000, available order qty 15,933, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991442955522048-C1869.pdf).",
        ]

    current = "electronic_capacitor_1206_47_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "47 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1870 / Fenghua 1206B473K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 47 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 473 = 47 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 47 nF generics supplied by C1622 and C53134.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 47 nF, 50 V, X7R, +/-10%, stock 8,191, minimum 1, full reel 4,000, available order qty 8,148, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991449964204032-C1870.pdf).",
        ]

    current = "electronic_capacitor_1206_470_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "470 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1871 / Fenghua 1206B474K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 470 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 474 = 470 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 470 nF generics supplied by C1623 and C13967.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 470 nF, 50 V, X7R, +/-10%, stock 6,753, minimum 1, full reel 3,000, available order qty 6,664, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991456909701120-C1871.pdf).",
        ]

    current = "electronic_capacitor_1206_4_7_micro_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_4_7_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "25 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1872 / CL31B475KAHNNNE rated purchasing variant; 1206, 4.7 uF, 25 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28 (stock 33,006, minimum 1, full reel 2,000, available order qty 22,228, MSL 1). The Samsung ordering code (KA = X7R 25 V) decodes consistently with the listed specifications.",
            "Linked to the generic 1206 4.7 uF definition. IMPORTANT rating difference: the reviewed preference C29823 / 1206B475K500NT on the generic ID is the 50 V rated part; this C1872 SKU is the 25 V part and must never silently replace it in circuits that need the higher rating. It exists so projects that only need 25 V at 1206/4.7 uF can pick the exact SKU explicitly. The registry allows one preferred code per ID; C1872 is recorded as its own exact rated-variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178191673741312-C1872.pdf).",
        ]

    current = "electronic_capacitor_1206_500_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "500 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1873 / Fenghua 1206B501K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 500 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 501 = 50 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 500 pF generics supplied by C1624 and C1747.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 500 pF, 50 V, X7R, +/-10%, stock 5,984, minimum 1, full reel 4,000, available order qty 5,951, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991463016878080-C1873.pdf).",
        ]

    current = "electronic_capacitor_1206_510_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "510 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1874 / Fenghua 1206B511K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 510 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 511 = 51 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 510 pF generics supplied by C1626 and C1749.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 510 pF, 50 V, X7R, +/-10%, stock 9, minimum 1, full reel 4,000, available order qty 9, MSL 1. Stock is very low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991469576634368-C1874.pdf).",
        ]

    current = "electronic_capacitor_1206_560_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "560 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1875 / Fenghua 1206B561K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 560 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 561 = 56 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 560 pF generics supplied by C1539, C1627 and C1751.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 560 pF, 50 V, X7R, +/-10%, stock 12, minimum 1, full reel 4,000, available order qty 12, MSL 1. Stock is very low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991475960229888-C1875.pdf).",
        ]

    current = "electronic_capacitor_1206_5_6_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5.6 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1876 / Fenghua 1206B562K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 5.6 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 562 = 5.6 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 5.6 nF generics supplied by C1540 and C1628.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 5.6 nF, 50 V, X7R, +/-10%, stock 4, minimum 1, full reel 4,000, available order qty 4, MSL 1. Stock is very low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991479143706624-C1876.pdf).",
        ]

    current = "electronic_capacitor_1206_56_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "56 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1877 / Fenghua 1206B563K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 56 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 563 = 56 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 56 nF generics supplied by C1629 and C1753.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 56 nF, 50 V, X7R, +/-10%, stock 131, minimum 1, full reel 4,000, available order qty 130, MSL 1. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991485325840384-C1877.pdf).",
        ]

    current = "electronic_capacitor_1206_680_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "680 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1878 / Fenghua 1206B681K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 680 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 681 = 68 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 680 pF generics supplied by C1541, C1630 and C1754.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 680 pF, 50 V, X7R, +/-10%, stock 258, minimum 1, full reel 4,000, available order qty 251, MSL 1. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991491504320512-C1878.pdf).",
        ]

    current = "electronic_capacitor_1206_6_8_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "6.8 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1879 / Fenghua 1206B682K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 6.8 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 682 = 6.8 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 6.8 nF generics supplied by C1542, C1631 and C1755.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 6.8 nF, 50 V, X7R, +/-10%, stock 3,643, minimum 1, full reel 4,000, available order qty 3,633, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991498026598400-C1879.pdf).",
        ]

    current = "electronic_capacitor_1206_68_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "68 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1880 / Fenghua 1206B683K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 68 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 683 = 68 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0805 68 nF generic supplied by C1756.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 68 nF, 50 V, X7R, +/-10%, stock 3,952, minimum 1, full reel 4,000, available order qty 3,947, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991504871972864-C1880.pdf).",
        ]

    current = "electronic_capacitor_1206_680_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "680 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1881 / Fenghua 1206B684K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 680 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 684 = 680 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0805 680 nF generic supplied by C1783.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 680 nF, 50 V, X7R, +/-10%, stock 32,897, minimum 1, full reel 3,000, available order qty 32,392, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991511678652416-C1881.pdf).",
        ]

    current = "electronic_capacitor_1206_0_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "0.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1882 / Fenghua 1206CG0R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 0.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 0R5 = 0.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 0.5 pF generics supplied by C1544, C1633 and C1784.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 0.5 pF, 50 V, C0G, stock 3,230, minimum 1, full reel 4,000, available order qty 3,230, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991517941018624-C1882.pdf).",
        ]

    current = "electronic_capacitor_1206_10_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "10 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1883 / Fenghua 1206CG100J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 10 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 100 = 10 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 10 pF generics supplied by C32949 and C1634.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 10 pF, 50 V, C0G, +/-5%, stock 8,016, minimum 1, full reel 4,000, available order qty 7,944, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991524199055360-C1883.pdf).",
        ]

    current = "electronic_capacitor_1206_100_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "100 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1884 / Fenghua 1206CG101J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 100 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 101 = 10 x 10^1 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 100 pF generics supplied by C1546, C14858 and C1790.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 100 pF, 50 V, C0G, +/-5%, stock 16,638, minimum 1, full reel 4,000, available order qty 14,143, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991530439909376-C1884.pdf).",
        ]

    current = "electronic_capacitor_1206_1_nano_farad_fenghua_adv_tech_1206cg102j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_1_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 nF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1885 / 1206CG102J500NT purchasing variant; 1206, 1 nF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 5,855, minimum 1, full reel 4,000, available order qty 5,798, MSL 1).",
            "Linked to the generic 1206 1 nF definition. Dielectric difference: the reviewed preference C1845 / 1206B102K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1885 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 1 nF/1206 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1885 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991537285013504-C1885.pdf).",
        ]

    current = "electronic_capacitor_1206_12_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "12 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1886 / Fenghua 1206CG120J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 12 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 120 = 12 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 12 pF generics supplied by C1547, C38523 and C1792.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 12 pF, 50 V, C0G, +/-5%, stock 36, minimum 1, full reel 4,000, available order qty 25, MSL 1. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991543962615808-C1886.pdf).",
        ]

    current = "electronic_capacitor_1206_15_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "15 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1887 / Fenghua 1206CG150J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 15 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 150 = 15 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the in-grid 0402 15 pF generic and the 0603 15 pF generic supplied by C1644.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 15 pF, 50 V, C0G, +/-5%, stock 17,397, minimum 1, full reel 4,000, available order qty 17,242, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991547238096896-C1887.pdf).",
        ]

    current = "electronic_capacitor_1206_150_pico_farad_fenghua_adv_tech_1206cg151j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_150_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "150 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1888 / 1206CG151J500NT purchasing variant; 1206, 150 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 1, minimum 1, full reel 4,000, available order qty 1, MSL 1). Stock is extremely low at capture time; low stock does not change the verified identity and the part is retained as a candidate.",
            "Linked to the generic 1206 150 pF definition. Dielectric difference: the reviewed preference C1850 / 1206B151K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1888 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 150 pF/1206 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1888 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991553890668544-C1888.pdf).",
        ]

    current = "electronic_capacitor_1206_18_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "18 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1889 / Fenghua 1206CG180J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 18 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 180 = 18 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 18 pF generics supplied by C1647 and C1797.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 18 pF, 50 V, C0G, +/-5%, stock 4,247, minimum 1, full reel 4,000, available order qty 4,231, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991560328790016-C1889.pdf).",
        ]

    current = "electronic_capacitor_1206_180_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "180 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1890 / Fenghua 1206B181K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 180 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 181 = 18 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 180 pF generics supplied by C1598 and C1721.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 180 pF, 50 V, X7R, +/-10%, stock 2, minimum 1, full reel 4,000, available order qty 2, MSL 1. Stock is extremely low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991567106379776-C1890.pdf).",
        ]

    current = "electronic_capacitor_1206_1_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1891 / Fenghua 1206CG1R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 1 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R0 = 1 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0805 1 pF generics supplied by C1550 and C1786.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 1 pF, 50 V, C0G, stock 7, minimum 499, full reel 4,000 (reel/pre-order purchasing with no available order quantity), MSL 1; the live page lists no tolerance row. The zero-scale stock and 499-piece minimum are purchasing conditions recorded as observed and do not change the verified identity. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991573511352320-C1891.pdf).",
        ]

    current = "electronic_capacitor_1206_1_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1892 / Fenghua 1206CG1R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 1.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R5 = 1.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 1.5 pF generics supplied by C1552, C1639 and C1788.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 1.5 pF, 50 V, C0G, stock 817, minimum 1, full reel 4,000, available order qty 816, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991579887099904-C1892.pdf).",
        ]

    current = "electronic_capacitor_1206_1_8_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.8 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1893 / Fenghua 1206CG1R8C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 1.8 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R8 = 1.8 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 1.8 pF generics supplied by C1553, C1640 and C1789.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 1.8 pF, 50 V, C0G, stock 5, minimum 1, full reel 4,000, available order qty 5, MSL 1; the live page lists no tolerance row. Stock is very low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991583216971776-C1893.pdf).",
        ]

    current = "electronic_capacitor_1206_20_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "20 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1894 / Fenghua 1206CG200J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 20 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 200 = 20 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 20 pF generics supplied by C1554, C1648 and C1798.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 20 pF, 50 V, C0G, +/-5%, stock 10,043, minimum 1, full reel 4,000, available order qty 9,855, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991589634121728-C1894.pdf).",
        ]

    current = "electronic_capacitor_1206_200_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "200 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1895 / Fenghua 1206CG201J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 200 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 201 = 20 x 10^1 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 200 pF generics supplied by C1529, C1600 and C1724.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 200 pF, 50 V, C0G, +/-5%, stock 3,042, minimum 1, full reel 4,000, available order qty 3,040, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991596294946816-C1895.pdf).",
        ]

    current = "electronic_capacitor_1206_22_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "22 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1896 / Fenghua 1206CG220J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 22 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 220 = 22 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 22 pF generics supplied by C1555, C1653 and C1804.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 22 pF, 50 V, C0G, +/-5%, stock 5,535, minimum 1, full reel 4,000, available order qty 5,435, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991602510499840-C1896.pdf).",
        ]

    current = "electronic_capacitor_1206_220_pico_farad_fenghua_adv_tech_1206cg221j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_220_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "220 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1897 / 1206CG221J500NT purchasing variant; 1206, 220 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 2,110, minimum 1, full reel 4,000, available order qty 2,051, MSL 1).",
            "Linked to the generic 1206 220 pF definition. Dielectric difference: the reviewed preference C1854 / 1206B221K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1897 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 220 pF/1206 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1897 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991608693579776-C1897.pdf).",
        ]

    current = "electronic_capacitor_1206_25_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "25 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1898 / Fenghua 1206CG250J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 25 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 250 = 25 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 25 pF generics supplied by C1556, C1655 and C1807.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 25 pF, 50 V, C0G, +/-5%, stock 3,267, minimum 1, full reel 4,000, available order qty 3,263, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991615173103616-C1898.pdf).",
        ]

    current = "electronic_capacitor_1206_27_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "27 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1899 / Fenghua 1206CG270J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 27 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 270 = 27 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 27 pF generics supplied by C1557, C1656 and C1808.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 27 pF, 50 V, C0G, +/-5%, stock 1,909, minimum 1, full reel 4,000, available order qty 1,909, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991621809033217-C1899.pdf).",
        ]

    current = "electronic_capacitor_1206_270_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "270 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1900 / Fenghua 1206CG271J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 270 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 271 = 27 x 10^1 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 270 pF generics supplied by C1533, C1608 and C1732.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 270 pF, 50 V, C0G, +/-5%, stock 4,000, minimum 1, full reel 4,000, available order qty 4,000, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991628075188224-C1900.pdf).",
        ]

    current = "electronic_capacitor_1206_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1901 / Fenghua 1206CG2R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R0 = 2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 2 pF generics supplied by C1558, C1650 and C1800.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 2 pF, 50 V, C0G, stock 532, minimum 1, full reel 4,000, available order qty 521, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991634299129856-C1901.pdf).",
        ]

    current = "electronic_capacitor_1206_2_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1902 / Fenghua 1206CG2R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 2.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R2 = 2.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 2.2 pF generics supplied by C1559, C1651 and C1801.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 2.2 pF, 50 V, C0G, stock 4,584, minimum 1, full reel 4,000, available order qty 4,577, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991640502910976-C1902.pdf).",
        ]

    current = "electronic_capacitor_1206_2_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1903 / Fenghua 1206CG2R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 2.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R5 = 2.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 2.5 pF generics supplied by C1560, C1652 and C1802.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 2.5 pF, 50 V, C0G, stock 2,835, minimum 1, full reel 4,000, available order qty 2,835, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991646664208384-C1903.pdf).",
        ]

    current = "electronic_capacitor_1206_2_7_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.7 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1904 / Fenghua 1206CG2R7C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 2.7 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R7 = 2.7 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0805 2.7 pF generics supplied by C1561 and C1803.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 2.7 pF, 50 V, C0G, stock 32, minimum 1, full reel 4,000, available order qty 32, MSL 1; the live page lists no tolerance row. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991652905197568-C1904.pdf).",
        ]

    current = "electronic_capacitor_1206_30_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "30 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1905 / Fenghua 1206CG300J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 30 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 300 = 30 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 30 pF generics supplied by C1570 and C1658.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 30 pF, 50 V, C0G, +/-5%, stock 21, minimum 434, full reel 4,000 (reel/pre-order purchasing with no available order quantity), MSL 1. Stock is low at capture time; low stock and the 434-piece minimum are purchasing conditions recorded as observed and do not change the verified identity. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991656122634240-C1905.pdf).",
        ]

    current = "electronic_capacitor_1206_33_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "33 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1906 / Fenghua 1206CG330J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 33 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 330 = 33 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 33 pF generics supplied by C1562 and C1663.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 33 pF, 50 V, C0G, +/-5%, stock 8,433, minimum 1, full reel 4,000, available order qty 8,377, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991662225211392-C1906.pdf).",
        ]

    current = "electronic_capacitor_1206_330_pico_farad_fenghua_adv_tech_1206cg331j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_330_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "330 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1907 / 1206CG331J500NT purchasing variant; 1206, 330 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 4,002, minimum 1, full reel 4,000, available order qty 3,998, MSL 1).",
            "Linked to the generic 1206 330 pF definition. Dielectric difference: the reviewed preference C1862 / 1206B331K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1907 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 330 pF/1206 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1907 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991668856135680-C1907.pdf).",
        ]

    current = "electronic_capacitor_1206_36_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "36 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1908 / Fenghua 1206CG360J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 36 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 360 = 36 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 36 pF generic supplied by C1665.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 36 pF, 50 V, C0G, +/-5%, stock 4,000, minimum 1, full reel 4,000, available order qty 4,000, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991675181551616-C1908.pdf).",
        ]

    current = "electronic_capacitor_1206_39_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "39 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1909 / Fenghua 1206CG390J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 39 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 390 = 39 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0603 39 pF generics supplied by C1563 and C1666.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 39 pF, 50 V, C0G, +/-5%, stock 16, minimum 1, full reel 4,000, available order qty 5, MSL 1. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991681846030336-C1909.pdf).",
        ]

    current = "electronic_capacitor_1206_3_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1911 / Fenghua 1206CG3R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 3 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R0 = 3 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 and 0805 3 pF generics supplied by C1564 and C1810.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 3 pF, 50 V, C0G, stock 11, minimum 1, full reel 4,000, available order qty 11, MSL 1; the live page lists no tolerance row. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991694592249856-C1911.pdf).",
        ]

    current = "electronic_capacitor_1206_3_3_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.3 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1912 / Fenghua 1206CG3R3C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 3.3 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R3 = 3.3 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 3.3 pF generics supplied by C1565, C1660 and C1811.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 3.3 pF, 50 V, C0G, stock 1,585, minimum 1, full reel 4,000, available order qty 1,580, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991697855418368-C1912.pdf).",
        ]

    current = "electronic_capacitor_1206_3_9_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.9 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1913 / Fenghua 1206CG3R9C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 3.9 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R9 = 3.9 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 3.9 pF generics supplied by C1566, C1662 and C1813.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 3.9 pF, 50 V, C0G, stock 954, minimum 1, full reel 4,000, available order qty 954, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991704046886912-C1913.pdf).",
        ]

    current = "electronic_capacitor_1206_4_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1914 / Fenghua 1206CG4R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 4 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 4R0 = 4 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 4 pF generics supplied by C1568, C1668 and C1819.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 4 pF, 50 V, C0G, stock 2,342, minimum 1, full reel 4,000, available order qty 2,338, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991710631268352-C1914.pdf).",
        ]

    current = "electronic_capacitor_1206_47_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "47 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1916 / Fenghua 1206CG470J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 47 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 470 = 47 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 47 pF generics supplied by C1567, C1671 and C14857.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 47 pF, 50 V, C0G, +/-5%, stock 8,862, minimum 1, full reel 4,000, available order qty 8,815, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991723583414272-C1916.pdf).",
        ]

    current = "electronic_capacitor_1206_470_pico_farad_fenghua_adv_tech_1206cg471j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_470_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "470 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1917 / 1206CG471J500NT purchasing variant; 1206, 470 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 3,932, minimum 1, full reel 4,000, available order qty 3,932, MSL 1).",
            "Linked to the generic 1206 470 pF definition. Dielectric difference: the reviewed preference C1868 / 1206B471K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1917 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 470 pF/1206 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1917 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991730143305728-C1917.pdf).",
        ]

    current = "electronic_capacitor_1206_51_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "51 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1918 / Fenghua 1206CG510J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 51 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 510 = 51 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 51 pF generics supplied by C1571, C1675 and C1827.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 51 pF, 50 V, C0G, +/-5%, stock 11, minimum 1, full reel 4,000, available order qty 8, MSL 1. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991736313532416-C1918.pdf).",
        ]

    current = "electronic_capacitor_1206_56_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "56 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1919 / Fenghua 1206CG560J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 56 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 560 = 56 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 56 pF generics supplied by C1572, C1676 and C1828.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 56 pF, 50 V, C0G, +/-5%, stock 2,022, minimum 1, full reel 4,000, available order qty 2,017, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991743016030208-C1919.pdf).",
        ]

    current = "electronic_capacitor_1206_6_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "6 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1920 / Fenghua 1206CG6R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 6 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 6R0 = 6 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402 6 pF generic supplied by C1575.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 6 pF, 50 V, C0G, stock 472, minimum 1, full reel 4,000, available order qty 440, MSL 1; the live page lists no tolerance row. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991749571862528-C1920.pdf).",
        ]

    current = "electronic_capacitor_1206_62_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "62 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1921 / Fenghua 1206CG620J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 62 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 620 = 62 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0805 62 pF generic supplied by C1833.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 62 pF, 50 V, C0G, +/-5%, stock 438, minimum 1, full reel 4,000, available order qty 432, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991753182887936-C1921.pdf).",
        ]

    current = "electronic_capacitor_1206_68_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "68 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1922 / Fenghua 1206CG680J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 68 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 680 = 68 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 68 pF generics supplied by C1680 and C1834.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 68 pF, 50 V, C0G, +/-5%, stock 2,491, minimum 1, full reel 4,000, available order qty 2,485, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991759348785152-C1922.pdf).",
        ]

    current = "electronic_capacitor_1206_680_pico_farad_fenghua_adv_tech_1206cg681j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_680_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "680 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1923 / 1206CG681J500NT purchasing variant; 1206, 680 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28 (stock 1, minimum 1, full reel 4,000, available order qty 1, MSL 1). Stock is extremely low at capture time; low stock does not change the verified identity and the part is retained as a candidate.",
            "Linked to the generic 1206 680 pF definition. Dielectric difference: the reviewed preference C1878 / 1206B681K500NT on the generic ID is from the same maker (FH) but X7R ±10%, and it keeps the preference slot; this C1923 SKU is C0G ±5% - the more stable, tighter-tolerance dielectric of the two. Projects needing C0G stability at 680 pF/1206 should pick this variant explicitly; the X7R preference is not downgraded. The registry allows one preferred code per ID; C1923 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991765656342528-C1923.pdf).",
        ]

    current = "electronic_capacitor_1206_82_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "82 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1924 / Fenghua 1206CG820J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 82 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 820 = 82 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 82 pF generics supplied by C1683 and C1841.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 82 pF, 50 V, C0G, +/-5%, stock 798, minimum 1, full reel 4,000, available order qty 791, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991772044943360-C1924.pdf).",
        ]

    current = "electronic_capacitor_1206_1_micro_farad_fenghua_adv_tech_1206f105m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_1_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 uF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1926 / 1206F105M500NT purchasing variant; 1206, 1 uF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28 (stock 2,919, minimum 1, full reel 4,000, available order qty 2,850, MSL 1).",
            "Linked to the generic 1206 1 uF definition. IMPORTANT dielectric difference: the reviewed preference C1848 / CL31B105KBHNNNE (Samsung, X7R ±10% 50 V) on the generic ID is far more stable than this Y5V ±20% SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1926 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991778323275776-C1926.pdf).",
        ]

    current = "electronic_capacitor_1206_15_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "15 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1928 / Fenghua 1206F153M500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 15 nF value; the populate row was added by this intake. The Fenghua ordering code (F = Y5V, 153 = 15 nF, M = +/-20%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0402, 0603 and 0805 15 nF generics supplied by C1583, C1596 and C1718.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 15 nF, 50 V, Y5V, +/-20%, stock 4, minimum 1, full reel 4,000, available order qty 4, MSL 1. Stock is extremely low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991784136986624-C1928.pdf).",
        ]

    current = "electronic_capacitor_1206_150_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "150 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1929 / Fenghua 1206F154M500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1206 150 nF value; the populate row was added by this intake. The Fenghua ordering code (F = Y5V, 154 = 150 nF, M = +/-20%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 0603 and 0805 150 nF generics supplied by C1597 and C1719.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1206, 150 nF, 50 V, Y5V, +/-20%, stock 1,006, minimum 1, full reel 4,000, available order qty 953, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991789115490304-C1929.pdf).",
        ]

    current = "electronic_capacitor_1206_20_nano_farad_fenghua_adv_tech_1206f203m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_20_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "20 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1930 / 1206F203M500NT purchasing variant; 1206, 20 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28 (stock 419, minimum 1, full reel 4,000, available order qty 419, MSL 1).",
            "Linked to the generic 1206 20 nF definition. IMPORTANT dielectric difference: the reviewed preference C1853 / 1206B203K500NT on the generic ID is from the same maker (FH) but X7R ±10%, far more stable than this Y5V ±20% SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1930 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991795318865920-C1930.pdf).",
        ]

    current = "electronic_capacitor_1206_22_nano_farad_fenghua_adv_tech_1206f223m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_22_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "22 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1931 / 1206F223M500NT purchasing variant; 1206, 22 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28 (stock 543, minimum 1, full reel 4,000, available order qty 503, MSL 1).",
            "Linked to the generic 1206 22 nF definition. IMPORTANT dielectric difference: the reviewed preference C1856 / 1206B223K500NT on the generic ID is from the same maker (FH) but X7R ±10%, far more stable than this Y5V ±20% SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1931 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991801715044352-C1931.pdf).",
        ]

    current = "electronic_capacitor_1206_2_2_micro_farad_fenghua_adv_tech_1206f225m250nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_2_2_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 uF",
            "rated_voltage": "25 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1933 / 1206F225M250NT purchasing variant; 1206, 2.2 uF, 25 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28 (stock 3,681, minimum 1, full reel 4,000, available order qty 3,665, MSL 1).",
            "Linked to the generic 1206 2.2 uF definition. IMPORTANT dielectric difference: the reviewed preference C1855 / 1206B222K500NT on the generic ID is from the same maker (FH) but X7R ±10% at 50 V, far more stable (and higher rated) than this Y5V ±20% 25 V SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1933 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991814671249408-C1933.pdf).",
        ]

    current = "electronic_capacitor_1206_33_nano_farad_fenghua_adv_tech_1206f333m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_33_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "33 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1935 / 1206F333M500NT purchasing variant; 1206, 33 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28 (stock 3, minimum 1, full reel 4,000, available order qty 3, MSL 1). Stock is extremely low at capture time; low stock does not change the verified identity and the part is retained as a candidate.",
            "Linked to the generic 1206 33 nF definition. IMPORTANT dielectric difference: the reviewed preference C1864 / 1206B333K500NT on the generic ID is from the same maker (FH) but X7R ±10%, far more stable than this Y5V ±20% SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1935 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991821260771328-C1935.pdf).",
        ]

    current = "electronic_capacitor_1206_4_7_micro_farad_fenghua_adv_tech_1206f475m250nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_4_7_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "25 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1939 / 1206F475M250NT purchasing variant; 1206, 4.7 uF, 25 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28 (stock 2,902, minimum 1, full reel 2,000, available order qty 2,880, MSL 1).",
            "Linked to the generic 1206 4.7 uF definition. IMPORTANT dielectric difference: the reviewed preference C29823 / 1206B475K500NT on the generic ID is from the same maker (FH) but X7R ±10% at 50 V, far more stable (and higher rated) than this Y5V ±20% 25 V SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1939 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991843310362624-C1939.pdf).",
        ]

    current = "electronic_capacitor_1206_68_nano_farad_fenghua_adv_tech_1206f683m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_68_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "68 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1940 / 1206F683M500NT purchasing variant; 1206, 68 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28 (stock 3, minimum 1, full reel 4,000, available order qty 3, MSL 1). Stock is extremely low at capture time; low stock does not change the verified identity and the part is retained as a candidate.",
            "Linked to the generic 1206 68 nF definition. IMPORTANT dielectric difference: the reviewed preference C1880 / 1206B683K500NT on the generic ID is from the same maker (FH) but X7R ±10%, far more stable than this Y5V ±20% SKU. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1940 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991849874042880-C1940.pdf).",
        ]

    current = "electronic_capacitor_1206_1_nano_farad_1000_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_1_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 nF",
            "rated_voltage": "1 kV",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1941 / 1206B102K102NT rated purchasing variant; 1206, 1 nF, 1 kV, X7R, ±10% verified against the staged live JLC capture 2026-09-28 (stock 238,478, minimum 1, full reel 3,000, available order qty 222,800, MSL 1). The Fenghua ordering code (102 = 1 nF, K = +/-10%, 102 = 10 x 10^2 V = 1 kV) decodes consistently with the listed specifications.",
            "Linked to the generic 1206 1 nF definition. Rating difference: the reviewed preference C1845 / 1206B102K500NT on the generic ID is the 50 V part; this C1941 SKU is the 1 kV part and must be chosen explicitly for high-voltage circuits. It sits between the plain 50 V generic and the existing 2 kV rated variant C9196. The registry allows one preferred code per ID; C1941 is recorded as its own exact rated-variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991855854985216-C1941.pdf).",
        ]

    current = "electronic_capacitor_1206_1_nano_farad_500_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_1_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 nF",
            "rated_voltage": "500 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1942 / 1206B102K501NT rated purchasing variant; 1206, 1 nF, 500 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28 (stock 25,395, minimum 1, full reel 4,000, available order qty 24,779, MSL 1). The Fenghua ordering code (102 = 1 nF, K = +/-10%, 501 = 50 x 10^1 V = 500 V) decodes consistently with the listed specifications.",
            "Linked to the generic 1206 1 nF definition. Rating difference: the reviewed preference C1845 / 1206B102K500NT on the generic ID is the 50 V part; this C1942 SKU is the 500 V part and must be chosen explicitly for high-voltage circuits. It sits between the plain 50 V generic and the 1 kV (C1941) and 2 kV (C9196) rated variants. The registry allows one preferred code per ID; C1942 is recorded as its own exact rated-variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991862843101184-C1942.pdf).",
        ]

    current = "electronic_capacitor_1206_100_nano_farad_100_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_1206_100_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "100 nF",
            "rated_voltage": "100 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1945 / CL31B104KCFNNNE rated purchasing variant; 1206, 100 nF, 100 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28 (stock 411,314, minimum 1, full reel 2,000, available order qty 374,557, MSL 1). The Samsung ordering code (KC = X7R 100 V) decodes consistently with the listed specifications.",
            "Linked to the generic 1206 100 nF definition. Rating difference: the reviewed preference C24497 / CL31B104KBCNNNE on the generic ID is the 50 V part; this C1945 SKU is the 100 V part and must be chosen explicitly for higher-voltage circuits. The registry allows one preferred code per ID; C1945 is recorded as its own exact rated-variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178200505999360-C1945.pdf).",
        ]

    current = "electronic_capacitor_1210_2_2_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 uF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1950 / Fenghua 1210B225K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 1210 2.2 uF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 225 = 2.2 uF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the 1210 68 uF tantal generic already in the grid.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 1210, 2.2 uF, 50 V, X7R, +/-10%, stock 762, minimum 1, full reel 2,000, available order qty 676, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991875584856064-C1950.pdf).",
        ]

    current = "electronic_capacitor_0603_82_nano_farad_fenghua_adv_tech_0603b823k500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_82_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "82 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1951 / 0603B823K500NT purchasing variant; 0603, 82 nF, 50 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28 (stock 29, minimum 1, full reel 4,000, available order qty 12, MSL 1). Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate.",
            "Linked to the generic 0603 82 nF definition. Dielectric difference: the reviewed preference C1708 / 0603F823M500NT on the generic ID is from the same maker (FH) but Y5V ±20%; this C1951 SKU is X7R ±10% - the more stable, tighter-tolerance dielectric of the two. Projects requiring X7R stability at 82 nF/0603 should pick this variant explicitly; the Y5V preference is not downgraded. The registry allows one preferred code per ID; C1951 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991881960738816-C1951.pdf).",
        ]

    current = "electronic_capacitor_6_3_mm_diameter_11_mm_tall_electrolytic_10_micro_farad_100_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "100 V",
            "dielectric": "aluminum electrolytic",
            "tolerance": "±20%",
            "polarized": True,
        }
        part["research_notes"] = [
            "Verified JLC C2029 / CX (Dongguan Chengxing Elec) KM106M100E11RR0VH2FP0 as the first reviewed preferred extended purchasing choice for this previously absent leaded electrolytic value; the populate row was added by this intake. The KM ordering code (106 = 10 uF, M = +/-20%, 100 = 100 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Leaded (radial through-hole) aluminum electrolytic, D6.3 x L11 mm, 2.5 mm pin spacing, 1000 hrs at 105 C lifetime, ripple current 61 mA at 120 Hz; polarized, observe the marked negative stripe. Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), stock 15,090, minimum 1, full reel 1,000, available order qty 14,627. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8564798012716040192-C2029.pdf).",
        ]

    current = "electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_470_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "10 V",
            "dielectric": "aluminum electrolytic",
            "tolerance": "±20%",
            "polarized": True,
        }
        part["research_notes"] = [
            "Verified JLC C2033 / CX (Dongguan Chengxing Elec) GR477M010F12RR0VL4FP0 as the first reviewed preferred extended purchasing choice for this previously absent leaded electrolytic value; the populate row was added by this intake. The GR ordering code (477 = 470 uF, M = +/-20%, 010 = 10 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Leaded (radial through-hole) aluminum electrolytic, D8 x L12 mm, 3.5 mm pin spacing, 3000 hrs at 105 C lifetime, -40 C to +105 C; polarized, observe the marked negative stripe. Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), stock 2, minimum 1, full reel 500, available order qty 2. Stock is extremely low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588901546444926976-C2033.pdf).",
        ]

    current = "electronic_capacitor_6_3_mm_diameter_11_mm_tall_electrolytic_220_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "10 V",
            "dielectric": "aluminum electrolytic",
            "tolerance": "±20%",
            "polarized": True,
        }
        part["research_notes"] = [
            "Verified JLC C2036 / CX (Dongguan Chengxing Elec) GR227M010E11RR0VH4FP0 as the first reviewed preferred extended purchasing choice for this previously absent leaded electrolytic value; the populate row was added by this intake. The GR ordering code (227 = 220 uF, M = +/-20%, 010 = 10 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Same can size as the C2029 10 uF 100 V part (D6.3 x L11 mm).",
            "Leaded (radial through-hole) aluminum electrolytic, D6.3 x L11 mm, 2.5 mm pin spacing, 2000 hrs at 105 C lifetime, -40 C to +105 C; polarized, observe the marked negative stripe. Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), stock 1,738, minimum 1, full reel 1,000, available order qty 1,668. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887000555900928-C2036.pdf).",
        ]

    current = "electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_330_micro_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "330 uF",
            "rated_voltage": "25 V",
            "dielectric": "aluminum electrolytic",
            "tolerance": "±20%",
            "polarized": True,
        }
        part["research_notes"] = [
            "Verified JLC C2051 / CX (Dongguan Chengxing Elec) KM337M025F12RR0VH2FP0 as the first reviewed preferred extended purchasing choice for this previously absent leaded electrolytic value; the populate row was added by this intake. The KM ordering code (337 = 330 uF, M = +/-20%, 025 = 25 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Same can size as the C2033 470 uF 10 V part (D8 x L12 mm).",
            "Leaded (radial through-hole) aluminum electrolytic, D8 x L12 mm, 3.5 mm pin spacing, 2000 hrs at 105 C lifetime, ripple current 340 mA at 120 Hz; polarized, observe the marked negative stripe. Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), stock 36,836, minimum 1, full reel 500, available order qty 36,600. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588901580645281792-C2051.pdf).",
        ]

    current = "electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_220_micro_farad_35_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "35 V",
            "dielectric": "aluminum electrolytic",
            "tolerance": "±20%",
            "polarized": True,
        }
        part["research_notes"] = [
            "Verified JLC C2063 / CX (Dongguan Chengxing Elec) KM227M035F12RR0VH2FP0 as the first reviewed preferred extended purchasing choice for this previously absent leaded electrolytic value; the populate row was added by this intake. The KM ordering code (227 = 220 uF, M = +/-20%, 035 = 35 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Same can size as the C2033 470 uF 10 V and C2051 330 uF 25 V parts (D8 x L12 mm).",
            "Leaded (radial through-hole) aluminum electrolytic, D8 x L12 mm, 3.5 mm pin spacing, 2000 hrs at 105 C lifetime; polarized, observe the marked negative stripe. Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), stock 234,668, minimum 1, full reel 500, available order qty 225,906. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588894275962875904-C2063.pdf).",
        ]

    current = "electronic_capacitor_10_mm_diameter_17_mm_tall_electrolytic_470_micro_farad_35_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "35 V",
            "dielectric": "aluminum electrolytic",
            "tolerance": "±20%",
            "polarized": True,
        }
        part["research_notes"] = [
            "Verified JLC C2064 / CX (Dongguan Chengxing Elec) KM477M035G17RR0VH2FP0 as the first reviewed preferred extended purchasing choice for this previously absent leaded electrolytic value; the populate row was added by this intake. The KM ordering code (477 = 470 uF, M = +/-20%, 035 = 35 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. Distinct from the C2033 470 uF 10 V part (D8 x L12 mm): same capacitance, higher voltage, larger can.",
            "Leaded (radial through-hole) aluminum electrolytic, D10 x L17 mm, 5 mm pin spacing, 2000 hrs at 105 C lifetime; polarized, observe the marked negative stripe. Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), stock 38,410, minimum 1, full reel 200, available order qty 36,502. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887028632571904-C2064.pdf).",
        ]

    current = "electronic_capacitor_4_mm_diameter_7_mm_tall_electrolytic_2_2_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 uF",
            "rated_voltage": "50 V",
            "dielectric": "aluminum electrolytic",
            "tolerance": "±20%",
            "polarized": True,
        }
        part["research_notes"] = [
            "Verified JLC C2065 / CX (Dongguan Chengxing Elec) KS225M050C07RR0VH2FP0 as the first reviewed preferred extended purchasing choice for this previously absent leaded electrolytic value; the populate row was added by this intake. The KS ordering code (225 = 2.2 uF, M = +/-20%, 050 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Leaded (radial through-hole) aluminum electrolytic, D4 x L7 mm, 1.5 mm pin spacing, 1000 hrs at 105 C lifetime, -40 C to +105 C, ripple current 19 mA at 120 Hz; polarized, observe the marked negative stripe. Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), stock 21,917, minimum 1, full reel 1,000, available order qty 21,843. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895826516561920-C2065.pdf).",
        ]

    current = "electronic_capacitor_0805_12_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "12 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1715 / Fenghua 0805B123K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 12 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 123 = 12 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0603 12 nF generic supplied by C1593.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 12 nF, 50 V, X7R, +/-10%, stock 3,447, minimum 1, full reel 4,000, available order qty 3,442, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988213098037248-C1715.pdf).",
        ]

    current = "electronic_capacitor_0805_1_2_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.2 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1714 / Fenghua 0805B122K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0805 1.2 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 122 = 1.2 nF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0805 generic is distinct from the separate 0402 1.2 nF generic supplied by C1551.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0805, 1.2 nF, 50 V, X7R, +/-10%, stock 17,069, minimum 1, full reel 4,000, available order qty 16,699, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988209931067392-C1714.pdf).",
        ]

    current = "electronic_capacitor_0805_10_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_10_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "16 V",
            "dielectric": "X5R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1713 / Samsung CL21A106KOQNNNE as the first reviewed preferred extended purchasing choice for this rated variant; 0805, 10 uF, 16 V, X5R, ±10% verified against the staged live JLC capture 2026-09-28. The Samsung ordering code (CL21 = 0805, A = X5R, 106 = 10 uF, K = ±10%, OQ = 16 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Linked to the generic 0805 10 uF definition as a lower-voltage purchasing variant; the reviewed Basic 25 V preference C15850 / CL21A106KAYNNNE and the 50 V rated variant on the generic ID remain unchanged. Projects needing 25 V margin must not substitute this 16 V SKU.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178161242984448-C1713.pdf).",
        ]

    current = "electronic_capacitor_0805_1_micro_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_1_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 uF",
            "rated_voltage": "25 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1712 / Samsung CL21B105KAFNFNE as the first reviewed preferred extended purchasing choice for this rated variant; 0805, 1 uF, 25 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28. The Samsung ordering code (CL21 = 0805, B = X7R, 105 = 1 uF, K = ±10%, A = 25 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Linked to the generic 0805 1 uF definition as a lower-voltage purchasing variant; the reviewed Basic 50 V preference C28323 / CL21B105KBFNNNE on the generic ID remains unchanged. Projects needing 50 V margin must not substitute this 25 V SKU.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178156810686464-C1712.pdf).",
        ]

    current = "electronic_capacitor_0805_100_nano_farad_samsung_electro_mechanics_cl21b104kbcnnnc"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0805_100_nano_farad_50_volt"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "100 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1711 / CL21B104KBCNNNC purchasing variant; 0805, 100 nF, 50 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0805 100 nF 50 V definition. The reviewed Basic preference C49678 / CC0805KRX7R9BB104 (YAGEO, same 100 nF 50 V X7R ±10% spec) keeps the plain 50_volt generic ID; the 100 V C28233 preference on the plain 100 nF generic is also unchanged. The registry allows one preferred code per ID, so this equivalent-spec Samsung SKU is recorded as its own exact variant ID following the established maker/mpn variant taxonomy (as with the Samsung C1591 row on 0603).",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586177282230652928-C1711.pdf).",
        ]

    current = "electronic_capacitor_0603_100_nano_farad_samsung_electro_mechanics_cl10f104zb8nnnc"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_100_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "100 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "-20%~+80%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1688 / CL10F104ZB8NNNC purchasing variant; 0603, 100 nF, 50 V, Y5V, -20%~+80% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 100 nF definition. IMPORTANT dielectric difference: the reviewed 50 V X7R +/-10% preference C14663 (YAGEO) and the Samsung X7R variant C1591 on the generic ID are far more stable than this Y5V -20/+80% SKU. It must never replace the X7R preferences, and projects requiring X7R stability or tight tolerance must not substitute this SKU. The registry allows one preferred code per ID; C1688 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178151437647872-C1688.pdf).",
        ]

    current = "electronic_capacitor_0603_91_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "91 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1686 / Fenghua 0603CG910J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 91 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 910 = 91 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 91 pF, 50 V, C0G, +/-5%, stock 8,545, minimum 1, full reel 4,000, available order qty 8,536, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988152229892096-C1686.pdf).",
        ]

    current = "electronic_capacitor_0603_8_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "8.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1685 / Fenghua 0603CG8R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 8.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 8R2 = 8.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 8.2 pF generic supplied by C1579.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 8.2 pF, 50 V, C0G, stock 93,998, minimum 1, full reel 4,000, available order qty 68,609, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988148912873472-C1685.pdf).",
        ]

    current = "electronic_capacitor_0603_82_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "82 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1683 / Fenghua 0603CG820J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 82 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 820 = 82 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. The live page reads 82 pF, which is a distinct value from the 0603 820 pF X7R generic supplied by C1632.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 82 pF, 50 V, C0G, +/-5%, stock 67,898, minimum 1, full reel 4,000, available order qty 63,202, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988140737634304-C1683.pdf).",
        ]

    current = "electronic_capacitor_0603_7_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "7 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1682 / Fenghua 0603CG7R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 7 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 7R0 = 7.0 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 7 pF generic supplied by C1577.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 7 pF, 50 V, C0G, stock 88,449, minimum 1, full reel 4,000, available order qty 84,971, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988137558351872-C1682.pdf).",
        ]

    current = "electronic_capacitor_0603_75_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "75 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1681 / Fenghua 0603CG750J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 75 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 750 = 75 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 75 pF, 50 V, C0G, +/-5%, stock 4,442, minimum 1, full reel 4,000, available order qty 931, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988134228480000-C1681.pdf).",
        ]

    current = "electronic_capacitor_0603_68_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "68 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1680 / Fenghua 0603CG680J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 68 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 680 = 68 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. The live page reads 68 pF, which is a distinct value from the 0603 680 pF X7R generic supplied by C1630.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 68 pF, 50 V, C0G, +/-5%, stock 98,929, minimum 1, full reel 4,000, available order qty 92,459, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988127311532032-C1680.pdf).",
        ]

    current = "electronic_capacitor_0603_6_8_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "6.8 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1679 / Fenghua 0603CG6R8C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 6.8 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 6R8 = 6.8 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 6.8 pF C0G generic supplied by C1576.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 6.8 pF, 50 V, C0G, stock 197,695, minimum 1, full reel 4,000, available order qty 172,129, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988127311532032-C1679.pdf).",
        ]

    current = "electronic_capacitor_0603_6_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "6.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1678 / Fenghua 0603CG6R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 6.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 6R2 = 6.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 6.2 pF, 50 V, C0G, stock 30,973, minimum 1, full reel 4,000, available order qty 30,739, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988123872473088-C1678.pdf).",
        ]

    current = "electronic_capacitor_0603_56_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "56 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1676 / Fenghua 0603CG560J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 56 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 560 = 56 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 56 pF generic supplied by C1572.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 56 pF, 50 V, C0G, +/-5%, stock 48,310, minimum 1, full reel 4,000, available order qty 41,796, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988120789659648-C1676.pdf).",
        ]

    current = "electronic_capacitor_0603_51_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "51 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1675 / Fenghua 0603CG510J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 51 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 510 = 51 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 51 pF generic supplied by C1571.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 51 pF, 50 V, C0G, +/-5%, stock 5,229, minimum 1, full reel 4,000, available order qty 5,180, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988117706981376-C1675.pdf).",
        ]

    current = "electronic_capacitor_0603_5_6_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5.6 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1674 / Fenghua 0603CG5R6C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 5.6 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 5R6 = 5.6 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 5.6 pF generic supplied by C1574.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 5.6 pF, 50 V, C0G, stock 38,885, minimum 1, full reel 4,000, available order qty 34,656, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988114330836992-C1674.pdf).",
        ]

    current = "electronic_capacitor_0603_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1673 / Fenghua 0603CG5R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 5R0 = 5.0 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 5 pF generic supplied by C1573.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 5 pF, 50 V, C0G, stock 161,013, minimum 1, full reel 4,000, available order qty 150,008, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988111109070848-C1673.pdf).",
        ]

    current = "electronic_capacitor_0603_50_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "50 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1672 / Fenghua 0603CG500J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 50 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 500 = 50 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 50 pF, 50 V, C0G, +/-5%, stock 94,413, minimum 1, full reel 4,000, available order qty 86,632, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988107892580352-C1672.pdf).",
        ]

    current = "electronic_capacitor_0603_43_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "43 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1670 / Fenghua 0603CG430J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 43 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 430 = 43 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 43 pF, 50 V, C0G, +/-5%, stock 8,736, minimum 1, full reel 4,000, available order qty 8,661, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988104809361408-C1670.pdf).",
        ]

    current = "electronic_capacitor_0603_4_7_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1669 / Fenghua 0603CG4R7C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 4.7 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 4R7 = 4.7 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 4.7 pF generic supplied by C1569.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 4.7 pF, 50 V, C0G, stock 364,595, minimum 1, full reel 4,000, available order qty 334,310, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988101495590912-C1669.pdf).",
        ]

    current = "electronic_capacitor_0603_4_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1668 / Fenghua 0603CG4R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 4 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 4R0 = 4.0 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 4 pF generic supplied by C1568.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 4 pF, 50 V, C0G, stock 64,988, minimum 1, full reel 4,000, available order qty 63,456, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988098178572288-C1668.pdf).",
        ]

    current = "electronic_capacitor_0603_390_pico_farad_fenghua_adv_tech_0603cg391j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_390_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "390 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1667 / 0603CG391J500NT purchasing variant; 0603, 390 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 390 pF definition. The X7R ±10% preference C1617 / 0603B391K500NT on the generic ID remains unchanged; the registry allows one preferred code per ID, so this C0G ±5% SKU is recorded as its own exact variant ID. Dielectric differs from the preference (C0G vs X7R): either may be selected deliberately per project stability requirements, never substituted silently.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988095200616448-C1667.pdf).",
        ]

    current = "electronic_capacitor_0603_39_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "39 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1666 / Fenghua 0603CG390J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 39 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 390 = 39 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This is a picoFarad value, distinct from the separate 0603 39 nF generic supplied by C1619.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 39 pF, 50 V, C0G, +/-5%, stock 60,417, minimum 1, full reel 4,000, available order qty 57,650, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988091890634752-C1666.pdf).",
        ]

    current = "electronic_capacitor_0603_36_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "36 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1665 / Fenghua 0603CG360J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 36 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 360 = 36 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 36 pF, 50 V, C0G, +/-5%, stock 8,274, minimum 1, full reel 4,000, available order qty 8,225, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988088736653312-C1665.pdf).",
        ]

    current = "electronic_capacitor_0603_3_9_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.9 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1662 / Fenghua 0603CG3R9C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 3.9 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R9 = 3.9 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This is a picoFarad value, distinct from the separate 0603 3.9 nF generic supplied by C1618 and the 0402 3.9 pF generic supplied by C1566.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 3.9 pF, 50 V, C0G, stock 49,106, minimum 1, full reel 4,000, available order qty 47,582, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988081942286336-C1662.pdf).",
        ]

    current = "electronic_capacitor_0603_3_6_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.6 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1661 / Fenghua 0603CG3R6C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 3.6 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R6 = 3.6 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 3.6 pF, 50 V, C0G, stock 25,232, minimum 1, full reel 4,000, available order qty 25,184, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988078670594048-C1661.pdf).",
        ]

    current = "electronic_capacitor_0603_3_3_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.3 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1660 / Fenghua 0603CG3R3C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 3.3 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R3 = 3.3 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This is a picoFarad value, distinct from the separate 0603 3.3 nF generic supplied by C1576 and the 0402 3.3 pF generic supplied by C1565.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 3.3 pF, 50 V, C0G, stock 80,228, minimum 1, full reel 4,000, available order qty 77,535, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988072437723136-C1660.pdf).",
        ]

    current = "electronic_capacitor_0603_270_pico_farad_samsung_electro_mechanics_cl10c271jb8nnnc"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_270_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "270 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1657 / CL10C271JB8NNNC purchasing variant; 0603, 270 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 270 pF definition. The X7R ±10% preference C1608 / 0603B271K500NT on the generic ID remains unchanged; the registry allows one preferred code per ID, so this C0G ±5% Samsung SKU is recorded as its own exact variant ID. Dielectric differs from the preference (C0G vs X7R): either may be selected deliberately per project stability requirements, never substituted silently.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178149990612992-C1657.pdf).",
        ]

    current = "electronic_capacitor_0603_27_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "27 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1656 / Samsung CL10C270JB8NNNC as the first reviewed preferred extended purchasing choice for this in-grid generic 0603 27 pF value (the generic already exists in the 0603 capacitance_values grid, so no populate row was needed). The Samsung ordering code (CL10 = 0603, C = C0G, 270 = 27 pF, J = ±5%, B8 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. The pre-existing YAGEO CC0603JRNPO9BN270 (C107045) LCSC-only supply is preserved as a prior alternative.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 27 pF, 50 V, C0G, +/-5%, stock 37,373, minimum 1, full reel 4,000, available order qty 36,016, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707047652622336-C1656.pdf).",
        ]

    current = "electronic_capacitor_0603_25_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "25 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1655 / Fenghua 0603CG250J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 25 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 250 = 25 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 25 pF generic supplied by C1556.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 25 pF, 50 V, C0G, +/-5%, stock 4,249, minimum 1, full reel 4,000, available order qty 4,241, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988066062651392-C1655.pdf).",
        ]

    current = "electronic_capacitor_0603_24_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "24 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1654 / Fenghua 0603CG240J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 24 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 240 = 24 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 24 pF, 50 V, C0G, +/-5%, stock 110,340, minimum 1, full reel 4,000, available order qty 107,235, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988062648082432-C1654.pdf).",
        ]

    current = "electronic_capacitor_0603_2_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1652 / Fenghua 0603CG2R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 2.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R5 = 2.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 2.5 pF generic supplied by C1560.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 2.5 pF, 50 V, C0G, stock 3,129, minimum 1, full reel 4,000, available order qty 3,127, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988059368677376-C1652.pdf).",
        ]

    current = "electronic_capacitor_0603_2_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1651 / Fenghua 0603CG2R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 2.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R2 = 2.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 2.2 pF generic supplied by C1559.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 2.2 pF, 50 V, C0G, stock 77,088, minimum 1, full reel 4,000, available order qty 71,601, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988055891599360-C1651.pdf).",
        ]

    current = "electronic_capacitor_0603_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1650 / Fenghua 0603CG2R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 2R0 = 2.0 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 2 pF generic supplied by C1558.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 2 pF, 50 V, C0G, stock 219,138, minimum 1, full reel 4,000, available order qty 213,046, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988052745601024-C1650.pdf).",
        ]

    current = "electronic_capacitor_0603_200_pico_farad_fenghua_adv_tech_0603cg201j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_200_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "200 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1649 / 0603CG201J500NT purchasing variant; 0603, 200 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 200 pF definition. The X7R ±10% preference C1600 / 0603B201K500NT on the generic ID remains unchanged; the registry allows one preferred code per ID, so this C0G ±5% SKU is recorded as its own exact variant ID. Dielectric differs from the preference (C0G vs X7R): either may be selected deliberately per project stability requirements, never substituted silently.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988049352409088-C1649.pdf).",
        ]

    current = "electronic_capacitor_0603_16_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "16 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1646 / Fenghua 0603CG160J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 16 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 160 = 16 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 16 pF, 50 V, C0G, +/-5%, stock 23,036, minimum 1, full reel 4,000, available order qty 22,931, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988046244429824-C1646.pdf).",
        ]

    current = "electronic_capacitor_0603_150_pico_farad_fenghua_adv_tech_0603cg151j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_150_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "150 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1645 / 0603CG151J500NT purchasing variant; 0603, 150 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 150 pF definition. The reviewed Basic preference C1594 / 0603B151K500NT (same maker, X7R ±10%) on the generic ID remains unchanged; the registry allows one preferred code per ID, so this C0G ±5% SKU is recorded as its own exact variant ID. Dielectric differs from the preference (C0G vs X7R): either may be selected deliberately per project stability requirements, never substituted silently.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988042943107072-C1645.pdf).",
        ]

    current = "electronic_capacitor_0603_120_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "120 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1643 / Fenghua 0603CG121J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 120 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 121 = 12 x 10^1 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 120 pF, 50 V, C0G, +/-5%, stock 61,632, minimum 1, full reel 4,000, available order qty 61,351, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988039793319936-C1643.pdf).",
        ]

    current = "electronic_capacitor_0603_12_pico_farad_fenghua_adv_tech_0603cg120j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_12_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "12 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1642 / 0603CG120J500NT purchasing variant; 0603, 12 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 12 pF definition. The reviewed Basic preference C38523 / CL10C120JB8NNNC (Samsung, same 12 pF 50 V C0G ±5% spec) on the generic ID remains unchanged; the registry allows one preferred code per ID, so this equivalent-spec FH SKU is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988036518109184-C1642.pdf).",
        ]

    current = "electronic_capacitor_0603_11_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "11 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1641 / Fenghua 0603CG110J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 11 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 110 = 11 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. The live page reads 11 pF, which is a distinct value from the in-grid 10 pF generic.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 11 pF, 50 V, C0G, +/-5%, stock 17,987, minimum 1, full reel 4,000, available order qty 17,805, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988033523376128-C1641.pdf).",
        ]

    current = "electronic_capacitor_0603_1_8_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.8 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1640 / Fenghua 0603CG1R8C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 1.8 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R8 = 1.8 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 1.8 pF generic supplied by C1553.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 1.8 pF, 50 V, C0G, stock 70,251, minimum 1, full reel 4,000, available order qty 62,750, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988030314733568-C1640.pdf).",
        ]

    current = "electronic_capacitor_0603_1_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1639 / Fenghua 0603CG1R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 1.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R5 = 1.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 1.5 pF generic supplied by C1552.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 1.5 pF, 50 V, C0G, stock 48,945, minimum 1, full reel 4,000, available order qty 39,988, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988027022069760-C1639.pdf).",
        ]

    current = "electronic_capacitor_0603_1_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1638 / Fenghua 0603CG1R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 1.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 1R2 = 1.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 1.2 pF generic supplied by C1551.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 1.2 pF, 50 V, C0G, stock 25,094, minimum 1, full reel 4,000, available order qty 25,068, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988022110674944-C1638.pdf).",
        ]

    current = "electronic_capacitor_0603_1_nano_farad_fenghua_adv_tech_0603cg102j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_1_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1 nF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1636 / 0603CG102J500NT purchasing variant; 0603, 1 nF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 1 nF definition. The reviewed Basic preference C1588 / CL10B102KB8NNNC (Samsung, X7R ±10%) on the generic ID remains unchanged; the registry allows one preferred code per ID, so this C0G ±5% FH SKU is recorded as its own exact variant ID. Dielectric differs from the preference (C0G vs X7R): either may be selected deliberately per project stability requirements, never substituted silently.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988018943569920-C1636.pdf).",
        ]

    current = "electronic_capacitor_0603_100_pico_farad_fenghua_adv_tech_0603cg101j500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_100_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "100 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1635 / 0603CG101J500NT purchasing variant; 0603, 100 pF, 50 V, C0G, ±5% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 100 pF definition. The reviewed Basic preference C14858 / CL10C101JB8NNNC (Samsung, same 100 pF 50 V C0G ±5% spec) on the generic ID remains unchanged; the registry allows one preferred code per ID, so this equivalent-spec FH SKU is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988015856967680-C1635.pdf).",
        ]

    current = "electronic_capacitor_0603_0_5_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "0.5 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1633 / Fenghua 0603CG0R5C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 0.5 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 0R5 = 0.5 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 0.5 pF generic supplied by C1544.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 0.5 pF, 50 V, C0G, stock 100,814, minimum 1, full reel 4,000, available order qty 99,206, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988012631547904-C1633.pdf).",
        ]

    current = "electronic_capacitor_0603_820_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "820 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1632 / Fenghua 0603B821K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 820 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 821 = 82 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 820 pF X7R generic is distinct from the separate 0402 820 pF C0G generic supplied by C1543.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 820 pF, 50 V, X7R, +/-10%, stock 57,615, minimum 1, full reel 4,000, available order qty 57,444, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770988009439682560-C1632.pdf).",
        ]

    current = "electronic_capacitor_0603_680_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "680 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1630 / Fenghua 0603B681K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 680 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 681 = 68 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 680 pF X7R generic is distinct from the separate 0402 680 pF C0G generic supplied by C1541.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 680 pF, 50 V, X7R, +/-10%, stock 119,409, minimum 1, full reel 4,000, available order qty 75,483, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987999905488896-C1630.pdf).",
        ]

    current = "electronic_capacitor_0603_56_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "56 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1629 / Fenghua 0603B563K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 56 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 563 = 56 x 10^3 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 56 nF, 50 V, X7R, +/-10%, stock 3,747, minimum 1, full reel 4,000, available order qty 3,714, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987996604436480-C1629.pdf).",
        ]

    current = "electronic_capacitor_0603_5_6_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5.6 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1628 / Fenghua 0603B562K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 5.6 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 562 = 56 x 10^2 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 5.6 nF generic supplied by C1542.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 5.6 nF, 50 V, X7R, +/-10%, stock 63,422, minimum 1, full reel 4,000, available order qty 62,960, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987993475891200-C1628.pdf).",
        ]

    current = "electronic_capacitor_0603_560_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "560 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1627 / Fenghua 0603B561K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 560 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 561 = 56 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 560 pF X7R generic is distinct from the separate 0402 560 pF C0G generic supplied by C1539.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 560 pF, 50 V, X7R, +/-10%, stock 18,966, minimum 1, full reel 4,000, available order qty 18,889, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987990237483008-C1627.pdf).",
        ]

    current = "electronic_capacitor_0603_510_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "510 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1626 / Fenghua 0603B511K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 510 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 511 = 51 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 510 pF, 50 V, X7R, +/-10%, stock 22,770, minimum 1, full reel 4,000, available order qty 21,527, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987987079307264-C1626.pdf).",
        ]

    current = "electronic_capacitor_0603_5_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1625 / Fenghua 0603B502K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 5 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 502 = 50 x 10^2 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 5 nF X7R generic is distinct from the separate 0402 5 pF C0G generic supplied by C1573.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 5 nF, 50 V, X7R, +/-10%, stock 6,489, minimum 1, full reel 4,000, available order qty 6,435, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987983636054016-C1625.pdf).",
        ]

    current = "electronic_capacitor_0603_500_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "500 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1624 / Fenghua 0603B501K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 500 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 501 = 50 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 500 pF, 50 V, X7R, +/-10%, stock 4,195, minimum 1, full reel 4,000, available order qty 4,137, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987980410363904-C1624.pdf).",
        ]

    current = "electronic_capacitor_0603_4_7_nano_farad_samsung_electro_mechanics_cl10b472kb8nnnc"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_4_7_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1621 / CL10B472KB8NNNC purchasing variant; 0603, 4.7 nF, 50 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 4.7 nF definition. The reviewed Basic preference C53987 / 0603B472K500NT (FH) on the generic ID remains unchanged; the registry allows one preferred code per ID, so this equivalent-spec Samsung SKU is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586177280414924801-C1621.pdf).",
        ]

    current = "electronic_capacitor_0603_39_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "39 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1619 / Fenghua 0603B393K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 39 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 393 = 39 x 10^3 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 39 nF, 50 V, X7R, +/-10%, stock 321, minimum 1, full reel 4,000, available order qty 191, MSL 1. Stock is low at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987973926105088-C1619.pdf).",
        ]

    current = "electronic_capacitor_0603_3_9_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.9 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1618 / Fenghua 0603B392K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 3.9 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 392 = 39 x 10^2 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 3.9 nF X7R generic is distinct from the separate 0402 3.9 pF C0G generic supplied by C1566.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 3.9 nF, 50 V, X7R, +/-10%, stock 20,770, minimum 1, full reel 4,000, available order qty 18,505, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987970684043264-C1618.pdf).",
        ]

    current = "electronic_capacitor_0603_390_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "390 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1617 / Fenghua 0603B391K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 390 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 391 = 39 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 390 pF, 50 V, X7R, +/-10%, stock 63,326, minimum 1, full reel 4,000, available order qty 62,330, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987967303299072-C1617.pdf).",
        ]

    current = "electronic_capacitor_0603_360_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "360 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1616 / Fenghua 0603B361K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 360 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 361 = 36 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 360 pF, 50 V, X7R, +/-10%, stock 7,130, minimum 1, full reel 4,000, available order qty 7,091, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987961104117760-C1616.pdf).",
        ]

    current = "electronic_capacitor_0603_330_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "330 nF",
            "rated_voltage": "25 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1615 / Fenghua 0603B334K250NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 330 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 334 = 33 x 10^4 pF, K = +/-10%, 250 = 25 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. The generic ID stays plain because no higher-voltage 0603 330 nF sibling exists yet; if a 50 V sibling is added later it should become an explicit rated variant per the C1590/C1592 precedents.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 330 nF, 25 V, X7R, +/-10%, stock 93,455, minimum 1, full reel 4,000, available order qty 55,710, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987957987479552-C1615.pdf).",
        ]

    current = "electronic_capacitor_0603_33_nano_farad_fenghua_adv_tech_0603b333k500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_33_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "33 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1614 / 0603B333K500NT purchasing variant; 0603, 33 nF, 50 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 33 nF definition. The reviewed Basic preference C21117 / CL10B333KB8NNNC (Samsung, same 33 nF 50 V X7R ±10% spec) on the generic ID remains unchanged; the registry allows one preferred code per ID, so this equivalent-spec FH SKU is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987954732699648-C1614.pdf).",
        ]

    current = "electronic_capacitor_0603_330_pico_farad_fenghua_adv_tech_0603b331k500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_330_pico_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "330 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1612 / 0603B331K500NT purchasing variant; 0603, 330 pF, 50 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 330 pF definition. IMPORTANT dielectric difference: the reviewed Basic preference C1664 / CL10C331JB8NNNC (Samsung) on the generic ID is C0G ±5%; this FH SKU is X7R ±10%, a materially broader-tolerance, worse-stability dielectric. It must never replace the C0G preference, and projects requiring C0G stability must not substitute this SKU. The registry allows one preferred code per ID; C1612 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987951558152192-C1612.pdf).",
        ]

    current = "electronic_capacitor_0603_3_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1611 / Fenghua 0603B302K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 3 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 302 = 30 x 10^2 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 X7R generic is distinct from the separate 0402 3 nF generic supplied by C1564.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 3 nF, 50 V, X7R, +/-10%, stock 16,427, minimum 1, full reel 4,000, available order qty 16,342, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987948433125376-C1611.pdf).",
        ]

    current = "electronic_capacitor_0603_300_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "300 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1610 / Fenghua 0603B301K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 300 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 301 = 30 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 300 pF, 50 V, X7R, +/-10%, stock 7,628, minimum 1, full reel 4,000, available order qty 7,133, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987945321086976-C1610.pdf).",
        ]

    current = "electronic_capacitor_0603_2_7_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.7 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1609 / Fenghua 0603B272K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 2.7 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 272 = 27 x 10^2 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 2.7 nF X7R generic is distinct from the separate 0402 2.7 pF C0G generic supplied by C1561.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 2.7 nF, 50 V, X7R, +/-10%, stock 84,028, minimum 1, full reel 4,000, available order qty 69,377, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987942011375616-C1609.pdf).",
        ]

    current = "electronic_capacitor_0603_270_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "270 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1608 / Fenghua 0603B271K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 270 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 271 = 27 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 270 pF, 50 V, X7R, +/-10%, stock 29,378, minimum 1, full reel 4,000, available order qty 26,306, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987935091314688-C1608.pdf).",
        ]

    current = "electronic_capacitor_0603_2_2_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_2_2_micro_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2.2 uF",
            "rated_voltage": "10 V",
            "dielectric": "X5R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1607 / Samsung CL10A225KP8NNNC as the first reviewed preferred extended purchasing choice for this rated variant; 0603, 2.2 uF, 10 V, X5R, ±10% verified against the staged live JLC capture 2026-09-28. The Samsung ordering code (CL10 = 0603, A = X5R, 225 = 2.2 uF, P = ±10%, P8 = 10 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Linked to the generic 0603 2.2 uF definition as a lower-voltage purchasing variant (C1592 16 V and C1590 25 V precedents); the reviewed Basic 16 V C23630 generic preference remains unchanged. Projects needing 16 V margin must not substitute this 10 V SKU.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178148606492672-C1607.pdf).",
        ]

    current = "electronic_capacitor_0603_220_nano_farad_fenghua_adv_tech_0603b224k250nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_220_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "220 nF",
            "rated_voltage": "25 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1606 / 0603B224K250NT purchasing variant; 0603, 220 nF, 25 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 220 nF definition. The reviewed Basic preference C21120 / CL10B224KA8NNNC (Samsung, same 220 nF 25 V X7R ±10% spec) on the generic ID remains unchanged; the registry allows one preferred code per ID, so this equivalent-spec FH SKU is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987931899449344-C1606.pdf).",
        ]

    current = "electronic_capacitor_0603_20_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "20 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1602 / Fenghua 0603B203K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 20 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 203 = 20 x 10^3 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 20 nF, 50 V, X7R, +/-10%, stock 23,403, minimum 1, full reel 4,000, available order qty 23,011, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987925502595072-C1602.pdf).",
        ]

    current = "electronic_capacitor_0603_2_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "2 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1601 / Fenghua 0603B202K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 2 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 202 = 20 x 10^2 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 2 nF generic is distinct from the separate 0402 2.2 nF generic supplied by C1531.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 2 nF, 50 V, X7R, +/-10%, stock 1,992, minimum 1, full reel 4,000, available order qty 1,907, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987920351989760-C1601.pdf).",
        ]

    current = "electronic_capacitor_0603_200_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "200 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1600 / Fenghua 0603B201K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 200 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 201 = 20 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 generic is distinct from the separate 0402 200 pF generic supplied by C1529.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 200 pF, 50 V, X7R, +/-10%, stock 52,258, minimum 1, full reel 4,000, available order qty 31,886, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987916326133760-C1600.pdf).",
        ]

    current = "electronic_capacitor_0603_1_8_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.8 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1599 / Fenghua 0603B182K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 1.8 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 182 = 18 x 10^2 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 1.8 nF, 50 V, X7R, +/-10%, stock 6,493, minimum 1, full reel 4,000, available order qty 5,970, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987913075142656-C1599.pdf).",
        ]

    current = "electronic_capacitor_0603_180_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "180 pF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1598 / Fenghua 0603B181K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 180 pF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 181 = 18 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 180 pF, 50 V, X7R, +/-10%, stock 17,754, minimum 1, full reel 4,000, available order qty 17,671, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987910084739072-C1598.pdf).",
        ]

    current = "electronic_capacitor_0603_150_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "150 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1597 / Fenghua 0603B154K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 150 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 154 = 15 x 10^4 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 150 nF, 50 V, X7R, +/-10%, stock 2,148, minimum 1, full reel 4,000, available order qty 2,075, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987906842677248-C1597.pdf).",
        ]

    current = "electronic_capacitor_0603_15_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "15 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1596 / Fenghua 0603B153K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 15 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 153 = 15 x 10^3 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This 0603 X7R generic is distinct from the separate 0402 15 nF Y5V generic supplied by C1583.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 15 nF, 50 V, X7R, +/-10%, stock 46,700, minimum 1, full reel 4,000, available order qty 27,591, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987903747416064-C1596.pdf).",
        ]

    current = "electronic_capacitor_0603_1_5_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "1.5 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1595 / Fenghua 0603B152K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 1.5 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 152 = 15 x 10^2 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 1.5 nF, 50 V, X7R, +/-10%, stock 126,504, minimum 1, full reel 4,000, available order qty 102,328, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987896222429184-C1595.pdf).",
        ]

    current = "electronic_capacitor_0603_12_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "12 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1593 / Fenghua 0603B123K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 12 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 123 = 12 x 10^3 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 12 nF, 50 V, X7R, +/-10%, stock 2,357, minimum 1, full reel 4,000, available order qty 2,341, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987889767395328-C1593.pdf).",
        ]

    current = "electronic_capacitor_0603_100_nano_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_100_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "100 nF",
            "rated_voltage": "25 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1590 / Samsung CL10B104KA8NNNC as the first reviewed preferred extended purchasing choice for this rated variant; 0603, 100 nF, 25 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28. The Samsung ordering code (CL10 = 0603, B = X7R, 104 = 100 nF, K = ±10%, A8 = 25 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Linked to the generic 0603 100 nF definition as a lower-voltage purchasing variant (C1592 16 V precedent); the reviewed 50 V C14663 generic preference and the Samsung 50 V C1591 maker/MPN variant remain unchanged. Projects needing 50 V margin must not substitute this 25 V SKU.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987890767724672-C1590.pdf).",
        ]

    current = "electronic_capacitor_0603_10_nano_farad_samsung_electro_mechanics_cl10b103kb8nnnc"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0603_10_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "10 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact Samsung Electro-Mechanics C1589 / CL10B103KB8NNNC purchasing variant; 0603, 10 nF, 50 V, X7R, ±10% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0603 10 nF definition. The reviewed Basic preference C57112 / 0603B103K500NT (FH) on the generic ID remains unchanged; the registry allows one preferred code per ID, so this equivalent-spec Samsung SKU is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987890357215232-C1589.pdf).",
        ]

    current = "electronic_capacitor_0603_5_1_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5.1 nF",
            "rated_voltage": "50 V",
            "dielectric": "X7R",
            "tolerance": "±10%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1587 / Fenghua 0603B512K500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0603 5.1 nF value; the populate row was added by this intake. The Fenghua ordering code (B = X7R, 512 = 51 x 10^1 pF, K = +/-10%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0603, 5.1 nF, 50 V, X7R, +/-10%, stock 16,236, minimum 1, full reel 4,000, available order qty 16,078, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987886487719936-C1587.pdf).",
        ]

    current = "electronic_capacitor_0402_22_nano_farad_fenghua_adv_tech_0402f223m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0402_22_nano_farad"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "22 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1584 / 0402F223M500NT purchasing variant; 0402, 22 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0402 22 nF definition. IMPORTANT dielectric difference: the existing verified Basic preference C1532 / 0402B223K500NT on electronic_capacitor_0402_22_nano_farad is X7R ±10% with full-stage evidence (datasheet sha256-verified, pinout and footprint checked); this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The scaffold guard refused an earlier attempt to scaffold C1584 onto the plain generic ID because C1532's page capture already exists there; C1584 is therefore recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987876916047872-C1584.pdf).",
        ]

    current = "electronic_capacitor_0402_15_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "15 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1583 / Fenghua 0402F153M500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 15 nF value; the populate row was added by this intake. The Fenghua ordering code (F = Y5V, 153 = 15 x 10^3 pF, M = +/-20%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 15 nF, 50 V, Y5V, +/-20%, stock 2, minimum 1, full reel 10,000, available order qty 2, MSL 1. Stock is nearly depleted at capture time; low stock does not change the verified identity and the part is retained as a candidate. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987873841893376-C1583.pdf).",
        ]

    current = "electronic_capacitor_0402_100_nano_farad_fenghua_adv_tech_0402f104m500nt"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_capacitor_0402_100_nano_farad_50_volt"
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "100 nF",
            "rated_voltage": "50 V",
            "dielectric": "Y5V",
            "tolerance": "±20%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Exact FH (Guangdong Fenghua Advanced Tech) C1581 / 0402F104M500NT purchasing variant; 0402, 100 nF, 50 V, Y5V, ±20% verified against the staged live JLC capture 2026-09-28.",
            "Linked to the generic 0402 100 nF 50 V definition. IMPORTANT dielectric difference: the reviewed Samsung Basic preference C307331 / CL05B104KB54PNC on electronic_capacitor_0402_100_nano_farad_50_volt is X7R ±10%; this FH SKU is Y5V ±20%, a materially broader-tolerance, worse-stability dielectric. It must never replace the X7R preference, and projects requiring X7R stability must not substitute this SKU. The registry allows one preferred code per ID; C1581 is recorded as its own exact variant ID.",
            "No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987863876227072-C1581.pdf).",
        ]

    current = "electronic_capacitor_0402_9_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "9 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1580 / Fenghua 0402CG9R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 9 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 9R0 = 9.0 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 9 pF, 50 V, C0G, stock 127,617, minimum 1, full reel 10,000, available order qty 121,306, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987860482764800-C1580.pdf).",
        ]

    current = "electronic_capacitor_0402_8_2_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "8.2 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1579 / Fenghua 0402CG8R2C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 8.2 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 8R2 = 8.2 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 8.2 pF, 50 V, C0G, stock 309,271, minimum 1, full reel 10,000, available order qty 304,577, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987857396162560-C1579.pdf).",
        ]

    current = "electronic_capacitor_0402_8_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "8 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1578 / Fenghua 0402CG8R0C500NT as the first reviewed preferred extended purchasing choice for this in-grid generic 0402 8 pF value (the generic already exists in the 0402 capacitance_values grid, so no populate row was needed). The Fenghua ordering code (CG = C0G, 8R0 = 8.0 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 8 pF, 50 V, C0G, stock 118,321, minimum 1, full reel 10,000, available order qty 110,156, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987854028001280-C1578.pdf).",
        ]

    current = "electronic_capacitor_0402_7_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "7 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1577 / Fenghua 0402CG7R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 7 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 7R0 = 7.0 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 7 pF, 50 V, C0G, stock 119,166, minimum 1, full reel 10,000, available order qty 119,010, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987838464042496-C1577.pdf).",
        ]

    current = "electronic_capacitor_0402_6_8_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "6.8 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1576 / Fenghua 0402CG6R8C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 6.8 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 6R8 = 6.8 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This is a picoFarad value, distinct from the separate 0402 6.8 nF generic supplied by C1542.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 6.8 pF, 50 V, C0G, stock 149,966, minimum 1, full reel 10,000, available order qty 102,998, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987838053537792-C1576.pdf).",
        ]

    current = "electronic_capacitor_0402_6_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "6 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1575 / Fenghua 0402CG6R0C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 6 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 6R0 = 6.0 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 6 pF, 50 V, C0G, stock 381,295, minimum 1, full reel 10,000, available order qty 376,696, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987837643055104-C1575.pdf).",
        ]

    current = "electronic_capacitor_0402_5_6_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "5.6 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1574 / Fenghua 0402CG5R6C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 5.6 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 5R6 = 5.6 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 5.6 pF, 50 V, C0G, stock 113,713, minimum 1, full reel 10,000, available order qty 106,970, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987837230632960-C1574.pdf).",
        ]

    current = "electronic_capacitor_0402_51_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "51 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "tolerance": "±5%",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1571 / Fenghua 0402CG510J500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 51 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 510 = 51 x 10^0 pF, J = +/-5%, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 51 pF, 50 V, C0G, +/-5%, stock 14,223, minimum 1, full reel 10,000, available order qty 13,820, MSL 1. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987831437479936-C1571.pdf).",
        ]

    current = "electronic_capacitor_0402_3_3_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.3 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1565 / Fenghua 0402CG3R3C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 3.3 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R3 = 3.3 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence. This is a picoFarad value, distinct from the separate 0402 3.3 nF generic supplied by C1536.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 3.3 pF, 50 V, C0G, stock 157,223, minimum 1, full reel 10,000, available order qty 140,453, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987812642668544-C1565.pdf).",
        ]

    current = "electronic_capacitor_0402_3_9_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "3.9 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1566 / Fenghua 0402CG3R9C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 3.9 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 3R9 = 3.9 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 3.9 pF, 50 V, C0G, stock 95,438, minimum 1, full reel 10,000, available order qty 89,612, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987815750782976-C1566.pdf).",
        ]

    current = "electronic_capacitor_0402_4_7_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["category"] = "capacitor"
        part["electrical"] = {
            "capacitance": "4.7 pF",
            "rated_voltage": "50 V",
            "dielectric": "C0G",
            "polarized": False,
        }
        part["research_notes"] = [
            "Verified JLC C1569 / Fenghua 0402CG4R7C500NT as the first reviewed preferred extended purchasing choice for this previously absent generic 0402 4.7 pF value; the populate row was added by this intake. The Fenghua ordering code (CG = C0G, 4R7 = 4.7 pF, 500 = 50 V) decodes consistently with the listed specifications; the live page specification table is the primary evidence.",
            "Live JLC detail page (staged capture 2026-09-28) shows Extended (Promotional Extended), 0402, 4.7 pF, 50 V, C0G, stock 627,647, minimum 1, full reel 10,000, available order qty 549,340, MSL 1. The page lists no tolerance row; full stage should extract the tolerance from the datasheet rather than decoding the MPN. No datasheet PDF imported at intake; download is an integration-stage task (JLC lists https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987825213267968-C1569.pdf).",
        ]

    # === BEGIN generated family batch (tmp/family_batch.py) — regenerated, do not hand-edit ===
    # JLC C23733 / 0402 4.7 μF (generated family batch 2026-10-04)
    current = "electronic_capacitor_0402_4_7_micro_farad_10_volt_20_percent"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0402_100_nano_farad"
        part["package_name_manufacturer"] = "0402 (1005 metric)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707315710726144-C23733.pdf"
        part["electrical"] = {
            "capacitance": "4.7 μF (475)",
            "dielectric": "X5R",
            "tolerance": "+-20% (M)",
            "rated_voltage": "10 V",
            "temperature_characteristic": "+-15% over the operating range (X5R)",
            "temperature_range": "0402 to +4 C",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5, "height": 0.5}
        part["dimension_reference"] = {
            "document": "Samsung MLCC data sheet, November 2015 (shared family copy) (C23733 provenance)",
            "pages": {"part_number_system": [4], "class_characteristics": [5], "dimensions": [6]},
            "notes": "part-numbering page 4 decodes the exact suffix; the class-characteristic page and the size tables cover the 0402 family; package dimensions: 0402 L 1.00+-0.05, W 0.50+-0.05, T 0.5+-0.05 mm.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0402_1005Metric",
            "hand_solder": "Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Samsung Electro-Mechanics CL05A475MP5NRNC (C23733): 4.7 μF 10 V X5R +-20% (M) in 0402; identity and ratings observed live at intake 2026-09-24.",
            "Family batch 2026-10-04 over the shared Samsung Electro-Mechanics MLCC datasheet (oomp_datasheet_common_with = electronic_capacitor_0402_100_nano_farad): ordering code decodes 475 = 4.7 μF.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated family batch (tmp/family_batch.py) ===

    # === BEGIN generated family batch (tmp/stragglers.py capacitors) — regenerated, do not hand-edit ===
    # JLC C14663 / YAGEO CC0603KRX7R9BB104 (straggler close-out 2026-10-05)
    current = "electronic_capacitor_0603_100_nano_farad"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "0603_1608Metric"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8667086713656442880-C14663.pdf"
        part["electrical"] = {
            "capacitance": "100 nF (104)",
            "dielectric": "X7R",
            "tolerance": "+-10%",
            "rated_voltage": "50 V",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "temperature_range": "-55 to +125 C",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "YAGEO YAGEO CC0603 series MLCC specification (own copy) (C14663 provenance)",
            "pages": [2, 3],
            "notes": "{pkg_name} outline per the specification drawing Ordering code CC0603KRX7R9BB104 decodes the 100 nF 50 V X7R +-10% rating.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0603_1608Metric",
            "hand_solder": "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists YAGEO CC0603KRX7R9BB104 (C14663): 100 nF 50 V X7R +-10%; identity and ratings observed live at intake 2026-09-24.",
            "Straggler close-out 2026-10-05: downloaded the YAGEO specification into this part via the signed JLC OSS link (the YAGEO/Murata ordering-code systems are per-size series, so this part anchors its own sub-family).",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C49678 / YAGEO CC0805KRX7R9BB104 (straggler close-out 2026-10-05)
    current = "electronic_capacitor_0805_100_nano_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["oomp_datasheet_common_with"] = "electronic_capacitor_0603_100_nano_farad"
        part["package_name_manufacturer"] = "0805_2012Metric"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8785639247575089152-C49678.pdf"
        part["electrical"] = {
            "capacitance": "100 nF (104)",
            "dielectric": "X7R",
            "tolerance": "+-10%",
            "rated_voltage": "50 V",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "temperature_range": "-55 to +125 C",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.25}
        part["dimension_reference"] = {
            "document": "YAGEO CC series MLCC specification (shared with C14663) (C49678 provenance)",
            "pages": [2, 3],
            "notes": "{pkg_name} outline per the shared CC-series specification drawing; the CC-series PDF is byte-identical across sizes Ordering code CC0805KRX7R9BB104 decodes the 100 nF 50 V X7R +-10% rating.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists YAGEO CC0805KRX7R9BB104 (C49678): 100 nF 50 V X7R +-10%; identity and ratings observed live at intake 2026-09-24.",
            "Straggler close-out 2026-10-05: downloaded the YAGEO specification into this part via the signed JLC OSS link (the YAGEO/Murata ordering-code systems are per-size series, so this part anchors its own sub-family).",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C107145 / YAGEO CC0805KRX7R9BB221 (straggler close-out 2026-10-05)
    current = "electronic_capacitor_0805_220_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "0805_2012Metric"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588898764141056001-C107145.pdf"
        part["electrical"] = {
            "capacitance": "220 pF (221)",
            "dielectric": "X7R",
            "tolerance": "+-10%",
            "rated_voltage": "50 V",
            "temperature_characteristic": "+-15% over the operating range (X7R)",
            "temperature_range": "-55 to +125 C",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.25}
        part["dimension_reference"] = {
            "document": "YAGEO YAGEO CC0805 series MLCC specification (own copy) (C107145 provenance)",
            "pages": [2, 3],
            "notes": "{pkg_name} outline per the specification drawing Ordering code CC0805KRX7R9BB221 decodes the 220 pF 50 V X7R +-10% rating.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists YAGEO CC0805KRX7R9BB221 (C107145): 220 pF 50 V X7R +-10%; identity and ratings observed live at intake 2026-09-24.",
            "Straggler close-out 2026-10-05: downloaded the YAGEO specification into this part via the signed JLC OSS link (the YAGEO/Murata ordering-code systems are per-size series, so this part anchors its own sub-family).",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C440198 / Murata Electronics GRM21BR61H106KE43L (straggler close-out 2026-10-05)
    current = "electronic_capacitor_0805_10_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        
        part["package_name_manufacturer"] = "0805_2012Metric"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588884955174330368-C440198.pdf"
        part["electrical"] = {
            "capacitance": "10 uF (106)",
            "dielectric": "X5R",
            "tolerance": "+-10%",
            "rated_voltage": "50 V",
            "temperature_characteristic": "+-15% over the operating range (X5R)",
            "temperature_range": "-55 to +125 C",
            "polarized": False,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.25}
        part["dimension_reference"] = {
            "document": "Murata Electronics Murata GRM21 series MLCC specification (own copy) (C440198 provenance)",
            "pages": [2, 3],
            "notes": "{pkg_name} outline per the specification drawing Ordering code GRM21BR61H106KE43L decodes the 10 uF 50 V X5R +-10% rating.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_0805_2012Metric",
            "hand_solder": "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Murata Electronics GRM21BR61H106KE43L (C440198): 10 uF 50 V X5R +-10%; identity and ratings observed live at intake 2026-09-24.",
            "Straggler close-out 2026-10-05: downloaded the Murata Electronics specification into this part via the signed JLC OSS link (the YAGEO/Murata ordering-code systems are per-size series, so this part anchors its own sub-family).",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated family batch (tmp/stragglers.py capacitors) ===

    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="capacitor")

    # === BEGIN generated polarized cap batch (tmp/cap_batch.py) — regenerated, do not hand-edit ===
    # JLC C1950 / FH (Guangdong Fenghua Advanced Tech) 1210B225K500NT - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_1210_2_2_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "1210 (3225 metric), 3.2 x 2.5 x 1.6 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770991875584856064-C1950.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 2.5, "height": 1.6}
        part["dimension_reference"] = {
            "document": "1210B225K500NT datasheet (C1950 provenance)",
            "pages": [1, 2],
            "notes": "1210 (3225 metric), 3.2 x 2.5 x 1.6 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "2.2 uF",
            "rated_voltage": "50 V",
            "tolerance": "+-10%",
            "dielectric": "class 2 ceramic (X7R per the Fenghua ordering code)",
            "polarized": False,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "1", "type": "passive"},
            "pin_2": {"number": "2", "name": "2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Small",
            "machine_solder": "Capacitor_SMD:C_1210_3225Metric",
            "hand_solder": "Capacitor_SMD:C_1210_3225Metric",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists 1210 FH (Guangdong Fenghua Advanced Tech) 1210B225K500NT (C1950); identity and ratings observed live at intake 2026-09-28.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Small master and the Capacitor_SMD:C_1210_3225Metric footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2029 / CX(Dongguan Chengxing Elec) KM106M100E11RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6_3_mm_diameter_11_mm_tall_electrolytic_10_micro_farad_100_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D6.3 x 11.0 mm, 2.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8564798012716040192-C2029.pdf"
        part["dimensions_mm"] = {"length": 6.3, "width": 6.3, "height": 11.0}
        part["dimension_reference"] = {
            "document": "KM106M100E11RR0VH2FP0 datasheet (C2029 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D6.3 x 11.0 mm, 2.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "100 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "1000hrs@105 C",
            "ripple_current": "61mA@120Hz",
            "pin_spacing": "2.5 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D6.3mm_P2.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D6.3xL11mm CX(Dongguan Chengxing Elec) KM106M100E11RR0VH2FP0 (C2029); identity and ratings observed live at intake 2026-09-28.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D6.3mm_P2.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2033 / CX(Dongguan Chengxing Elec) GR477M010F12RR0VL4FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_470_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588901546444926976-C2033.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 12.0}
        part["dimension_reference"] = {
            "document": "GR477M010F12RR0VL4FP0 datasheet (C2033 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "10 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "3000hrs@105 C",
            "pin_spacing": "3.5 mm",
            "polarized": True,
            "operating_temperature": "-40 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D8xL12mm CX(Dongguan Chengxing Elec) GR477M010F12RR0VL4FP0 (C2033); identity and ratings observed live at intake 2026-09-28.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D8.0mm_P3.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2036 / CX(Dongguan Chengxing Elec) GR227M010E11RR0VH4FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6_3_mm_diameter_11_mm_tall_electrolytic_220_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D6.3 x 11.0 mm, 2.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887000555900928-C2036.pdf"
        part["dimensions_mm"] = {"length": 6.3, "width": 6.3, "height": 11.0}
        part["dimension_reference"] = {
            "document": "GR227M010E11RR0VH4FP0 datasheet (C2036 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D6.3 x 11.0 mm, 2.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "10 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "2.5 mm",
            "polarized": True,
            "operating_temperature": "-40 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D6.3mm_P2.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D6.3xL11mm CX(Dongguan Chengxing Elec) GR227M010E11RR0VH4FP0 (C2036); identity and ratings observed live at intake 2026-09-28.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D6.3mm_P2.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2051 / CX(Dongguan Chengxing Elec) KM337M025F12RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_330_micro_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588901580645281792-C2051.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 12.0}
        part["dimension_reference"] = {
            "document": "KM337M025F12RR0VH2FP0 datasheet (C2051 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "330 uF",
            "rated_voltage": "25 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "ripple_current": "340mA@120Hz",
            "pin_spacing": "3.5 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D8xL12mm CX(Dongguan Chengxing Elec) KM337M025F12RR0VH2FP0 (C2051); identity and ratings observed live at intake 2026-09-28.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D8.0mm_P3.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2063 / CX(Dongguan Chengxing Elec) KM227M035F12RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_220_micro_farad_35_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588894275962875904-C2063.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 12.0}
        part["dimension_reference"] = {
            "document": "KM227M035F12RR0VH2FP0 datasheet (C2063 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "35 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "3.5 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D8xL12mm CX(Dongguan Chengxing Elec) KM227M035F12RR0VH2FP0 (C2063); identity and ratings observed live at intake 2026-09-28.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D8.0mm_P3.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2064 / CX(Dongguan Chengxing Elec) KM477M035G17RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_10_mm_diameter_17_mm_tall_electrolytic_470_micro_farad_35_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D10.0 x 17.0 mm, 5.0 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887028632571904-C2064.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 10.0, "height": 17.0}
        part["dimension_reference"] = {
            "document": "KM477M035G17RR0VH2FP0 datasheet (C2064 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D10.0 x 17.0 mm, 5.0 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "35 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "5.0 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D10xL17mm CX(Dongguan Chengxing Elec) KM477M035G17RR0VH2FP0 (C2064); identity and ratings observed live at intake 2026-09-28.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D10.0mm_P5.00mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2065 / CX(Dongguan Chengxing Elec) KS225M050C07RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_4_mm_diameter_7_mm_tall_electrolytic_2_2_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D4.0 x 7.0 mm, 1.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895826516561920-C2065.pdf"
        part["dimensions_mm"] = {"length": 4.0, "width": 4.0, "height": 7.0}
        part["dimension_reference"] = {
            "document": "KS225M050C07RR0VH2FP0 datasheet (C2065 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D4.0 x 7.0 mm, 1.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "2.2 uF",
            "rated_voltage": "50 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "1000hrs@105 C",
            "ripple_current": "19mA@120Hz",
            "pin_spacing": "1.5 mm",
            "polarized": True,
            "operating_temperature": "-40 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D4.0mm_P1.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D4xL7mm CX(Dongguan Chengxing Elec) KS225M050C07RR0VH2FP0 (C2065); identity and ratings observed live at intake 2026-09-28.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D4.0mm_P1.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2746 / CX(Dongguan Chengxing Elec) KM476M450K25RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_16_mm_diameter_25_mm_tall_electrolytic_47_micro_farad_450_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D16.0 x 25.0 mm, 7.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588936268264165376-C2746.pdf"
        part["dimensions_mm"] = {"length": 16.0, "width": 16.0, "height": 25.0}
        part["dimension_reference"] = {
            "document": "KM476M450K25RR0VH2FP0 datasheet (C2746 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D16.0 x 25.0 mm, 7.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "450 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "7.5 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D16.0mm_P7.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D16xL25mm CX(Dongguan Chengxing Elec) KM476M450K25RR0VH2FP0 (C2746); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D16.0mm_P7.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2749 / CX(Dongguan Chengxing Elec) KM107M050F12RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_100_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588902862562185216-C2749.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 12.0}
        part["dimension_reference"] = {
            "document": "KM107M050F12RR0VH2FP0 datasheet (C2749 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "50 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "3.5 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D8xL12mm CX(Dongguan Chengxing Elec) KM107M050F12RR0VH2FP0 (C2749); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D8.0mm_P3.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2754 / CX(Dongguan Chengxing Elec) KM688M025L30RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_18_mm_diameter_30_mm_tall_electrolytic_6800_micro_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D18.0 x 30.0 mm, 7.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588935545355440128-C2754.pdf"
        part["dimensions_mm"] = {"length": 18.0, "width": 18.0, "height": 30.0}
        part["dimension_reference"] = {
            "document": "KM688M025L30RR0VH2FP0 datasheet (C2754 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D18.0 x 30.0 mm, 7.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "6800 uF",
            "rated_voltage": "25 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "7.5 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D18.0mm_P7.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D18xL30mm CX(Dongguan Chengxing Elec) KM688M025L30RR0VH2FP0 (C2754); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D18.0mm_P7.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2760 / CX(Dongguan Chengxing Elec) KS105M050C07RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_4_mm_diameter_7_mm_tall_electrolytic_1_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D4.0 x 7.0 mm, 1.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895826541862912-C2760.pdf"
        part["dimensions_mm"] = {"length": 4.0, "width": 4.0, "height": 7.0}
        part["dimension_reference"] = {
            "document": "KS105M050C07RR0VH2FP0 datasheet (C2760 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D4.0 x 7.0 mm, 1.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "1 uF",
            "rated_voltage": "50 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "1000hrs@105 C",
            "pin_spacing": "1.5 mm",
            "polarized": True,
            "operating_temperature": "-40 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D4.0mm_P1.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D4xL7mm CX(Dongguan Chengxing Elec) KS105M050C07RR0VH2FP0 (C2760); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D4.0mm_P1.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2763 / CX(Dongguan Chengxing Elec) KM228M035K25RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_16_mm_diameter_25_mm_tall_electrolytic_2200_micro_farad_35_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D16.0 x 25.0 mm, 7.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588936303270907904-C2763.pdf"
        part["dimensions_mm"] = {"length": 16.0, "width": 16.0, "height": 25.0}
        part["dimension_reference"] = {
            "document": "KM228M035K25RR0VH2FP0 datasheet (C2763 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D16.0 x 25.0 mm, 7.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "2200 uF",
            "rated_voltage": "35 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "7.5 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D16.0mm_P7.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D16xL25mm CX(Dongguan Chengxing Elec) KM228M035K25RR0VH2FP0 (C2763); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D16.0mm_P7.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2767 / CX(Dongguan Chengxing Elec) KM107M400L30RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_18_mm_diameter_30_mm_tall_electrolytic_100_micro_farad_400_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D18.0 x 30.0 mm, 7.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588937452328902656-C2767.pdf"
        part["dimensions_mm"] = {"length": 18.0, "width": 18.0, "height": 30.0}
        part["dimension_reference"] = {
            "document": "KM107M400L30RR0VH2FP0 datasheet (C2767 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D18.0 x 30.0 mm, 7.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "400 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "7.5 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D18.0mm_P7.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D18xL30mm CX(Dongguan Chengxing Elec) KM107M400L30RR0VH2FP0 (C2767); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D18.0mm_P7.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2772 / CX(Dongguan Chengxing Elec) KM107M063F12RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_100_micro_farad_63_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588934582430781440-C2772.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 12.0}
        part["dimension_reference"] = {
            "document": "KM107M063F12RR0VH2FP0 datasheet (C2772 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "63 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "3.5 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D8xL12mm CX(Dongguan Chengxing Elec) KM107M063F12RR0VH2FP0 (C2772); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D8.0mm_P3.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2775 / CX(Dongguan Chengxing Elec) KM475M250F12RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_4_7_micro_farad_250_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588936839927775232-C2775.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 12.0}
        part["dimension_reference"] = {
            "document": "KM475M250F12RR0VH2FP0 datasheet (C2775 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "250 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "3.5 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D8xL12mm CX(Dongguan Chengxing Elec) KM475M250F12RR0VH2FP0 (C2775); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D8.0mm_P3.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3299 / CX(Dongguan Chengxing Elec) GR108M010F12RR0VL4FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_1000_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588919922475220992-C3299.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 12.0}
        part["dimension_reference"] = {
            "document": "GR108M010F12RR0VL4FP0 datasheet (C3299 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D8.0 x 12.0 mm, 3.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "1000 uF",
            "rated_voltage": "10 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "3000hrs@105 C",
            "ripple_current": "640mA@100kHz",
            "pin_spacing": "3.5 mm",
            "polarized": True,
            "operating_temperature": "-40 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D8xL12mm CX(Dongguan Chengxing Elec) GR108M010F12RR0VL4FP0 (C3299); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D8.0mm_P3.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3311 / CX(Dongguan Chengxing Elec) GR158M016G20RR0VL4FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_10_mm_diameter_20_mm_tall_electrolytic_1500_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D10.0 x 20.0 mm, 5.0 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887028616605696-C3311.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 10.0, "height": 20.0}
        part["dimension_reference"] = {
            "document": "GR158M016G20RR0VL4FP0 datasheet (C3311 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D10.0 x 20.0 mm, 5.0 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "1500 uF",
            "rated_voltage": "16 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "3000hrs@105 C",
            "ripple_current": "1.4A@100kHz",
            "pin_spacing": "5.0 mm",
            "polarized": True,
            "operating_temperature": "-40 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D10xL20mm CX(Dongguan Chengxing Elec) GR158M016G20RR0VL4FP0 (C3311); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D10.0mm_P5.00mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3312 / CX(Dongguan Chengxing Elec) GR477V050G20RR0VH4FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_10_mm_diameter_20_mm_tall_electrolytic_470_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D10.0 x 20.0 mm, 5.0 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887029707124736-C3312.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 10.0, "height": 20.0}
        part["dimension_reference"] = {
            "document": "GR477V050G20RR0VH4FP0 datasheet (C3312 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D10.0 x 20.0 mm, 5.0 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "50 V",
            "tolerance": "-10%~+20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "1000hrs@105 C",
            "pin_spacing": "5.0 mm",
            "polarized": True,
            "operating_temperature": "-40 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D10xL20mm CX(Dongguan Chengxing Elec) GR477V050G20RR0VH4FP0 (C3312); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D10.0mm_P5.00mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3314 / CX(Dongguan Chengxing Elec) KS336M016C07RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_4_mm_diameter_7_mm_tall_electrolytic_33_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D4.0 x 7.0 mm, 1.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895826684874752-C3314.pdf"
        part["dimensions_mm"] = {"length": 4.0, "width": 4.0, "height": 7.0}
        part["dimension_reference"] = {
            "document": "KS336M016C07RR0VH2FP0 datasheet (C3314 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D4.0 x 7.0 mm, 1.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "33 uF",
            "rated_voltage": "16 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "1000hrs@105 C",
            "pin_spacing": "1.5 mm",
            "polarized": True,
            "operating_temperature": "-40 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D4.0mm_P1.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D4xL7mm CX(Dongguan Chengxing Elec) KS336M016C07RR0VH2FP0 (C3314); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D4.0mm_P1.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3328 / CX(Dongguan Chengxing Elec) KM228M016G20RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_10_mm_diameter_20_mm_tall_electrolytic_2200_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D10.0 x 20.0 mm, 5.0 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887029724172288-C3328.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 10.0, "height": 20.0}
        part["dimension_reference"] = {
            "document": "KM228M016G20RR0VH2FP0 datasheet (C3328 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D10.0 x 20.0 mm, 5.0 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "2200 uF",
            "rated_voltage": "16 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "5.0 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D10xL20mm CX(Dongguan Chengxing Elec) KM228M016G20RR0VH2FP0 (C3328); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D10.0mm_P5.00mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3336 / CX(Dongguan Chengxing Elec) KM107M100G17RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_10_mm_diameter_17_mm_tall_electrolytic_100_micro_farad_100_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D10.0 x 17.0 mm, 5.0 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887000619626496-C3336.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 10.0, "height": 17.0}
        part["dimension_reference"] = {
            "document": "KM107M100G17RR0VH2FP0 datasheet (C3336 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D10.0 x 17.0 mm, 5.0 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "100 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "5.0 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D10xL17mm CX(Dongguan Chengxing Elec) KM107M100G17RR0VH2FP0 (C3336); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D10.0mm_P5.00mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3337 / Honor Elec RVT1C470M0505 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_5_mm_diameter_5_4_mm_tall_electrolytic_47_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D5.0 x 5.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291419281170432-C3337.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 5.0, "height": 5.4}
        part["dimension_reference"] = {
            "document": "RVT1C470M0505 datasheet (C3337 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D5.0 x 5.4 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "16 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_5x5.4",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D5xL5.4mm Honor Elec RVT1C470M0505 (C3337); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_5x5.4 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3338 / Honor Elec RVT1E101M0607 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_100_micro_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D6.3 x 7.7 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291514529890304-C3338.pdf"
        part["dimensions_mm"] = {"length": 6.3, "width": 6.3, "height": 7.7}
        part["dimension_reference"] = {
            "document": "RVT1E101M0607 datasheet (C3338 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D6.3 x 7.7 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "25 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_6.3x7.7",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D6.3xL7.7mm Honor Elec RVT1E101M0607 (C3338); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_6.3x7.7 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3339 / Honor Elec RVT1V101M0607 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_100_micro_farad_35_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D6.3 x 7.7 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757300898349625344-C3339.pdf"
        part["dimensions_mm"] = {"length": 6.3, "width": 6.3, "height": 7.7}
        part["dimension_reference"] = {
            "document": "RVT1V101M0607 datasheet (C3339 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D6.3 x 7.7 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "35 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_6.3x7.7",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D6.3xL7.7mm Honor Elec RVT1V101M0607 (C3339); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_6.3x7.7 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3340 / Honor Elec RVT1V221M0810 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_10_2_mm_tall_electrolytic_220_micro_farad_35_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D8.0 x 10.2 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291444862500864-C3340.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 10.2}
        part["dimension_reference"] = {
            "document": "RVT1V221M0810 datasheet (C3340 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D8.0 x 10.2 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "35 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_8x10",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D8xL10.2mm Honor Elec RVT1V221M0810 (C3340); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_8x10 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3341 / Honor Elec RVT1C471M0810 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_10_2_mm_tall_electrolytic_470_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D8.0 x 10.2 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291431684132864-C3341.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 10.2}
        part["dimension_reference"] = {
            "document": "RVT1C471M0810 datasheet (C3341 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D8.0 x 10.2 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "16 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_8x10",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D8xL10.2mm Honor Elec RVT1C471M0810 (C3341); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_8x10 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3342 / Honor Elec RVT1C221M0607 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_220_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D6.3 x 7.7 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291454182514688-C3342.pdf"
        part["dimensions_mm"] = {"length": 6.3, "width": 6.3, "height": 7.7}
        part["dimension_reference"] = {
            "document": "RVT1C221M0607 datasheet (C3342 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D6.3 x 7.7 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "16 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_6.3x7.7",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D6.3xL7.7mm Honor Elec RVT1C221M0607 (C3342); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_6.3x7.7 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3343 / Honor Elec RVT1E100M0405 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_4_mm_diameter_5_4_mm_tall_electrolytic_10_micro_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D4.0 x 5.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291427606999040-C3343.pdf"
        part["dimensions_mm"] = {"length": 4.0, "width": 4.0, "height": 5.4}
        part["dimension_reference"] = {
            "document": "RVT1E100M0405 datasheet (C3343 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D4.0 x 5.4 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "25 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_4x5.4",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D4xL5.4mm Honor Elec RVT1E100M0405 (C3343); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_4x5.4 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3344 / Honor Elec RVT1V470M0605 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6_3_mm_diameter_5_4_mm_tall_electrolytic_47_micro_farad_35_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D6.3 x 5.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291509765296128-C3344.pdf"
        part["dimensions_mm"] = {"length": 6.3, "width": 6.3, "height": 5.4}
        part["dimension_reference"] = {
            "document": "RVT1V470M0605 datasheet (C3344 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D6.3 x 5.4 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "35 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_6.3x5.4",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D6.3xL5.4mm Honor Elec RVT1V470M0605 (C3344); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_6.3x5.4 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3345 / Honor Elec RVT1A221M0605 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6_3_mm_diameter_5_4_mm_tall_electrolytic_220_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D6.3 x 5.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291449727623168-C3345.pdf"
        part["dimensions_mm"] = {"length": 6.3, "width": 6.3, "height": 5.4}
        part["dimension_reference"] = {
            "document": "RVT1A221M0605 datasheet (C3345 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D6.3 x 5.4 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "10 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_6.3x5.4",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D6.3xL5.4mm Honor Elec RVT1A221M0605 (C3345); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_6.3x5.4 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3347 / Honor Elec RVT1A101M0505 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_5_mm_diameter_5_4_mm_tall_electrolytic_100_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D5.0 x 5.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291440899018752-C3347.pdf"
        part["dimensions_mm"] = {"length": 5.0, "width": 5.0, "height": 5.4}
        part["dimension_reference"] = {
            "document": "RVT1A101M0505 datasheet (C3347 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D5.0 x 5.4 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "10 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_5x5.4",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D5xL5.4mm Honor Elec RVT1A101M0505 (C3347); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_5x5.4 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3348 / Honor Elec RVT1H1R0M0405 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_4_mm_diameter_5_4_mm_tall_electrolytic_1_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D4.0 x 5.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8719585583770370048-C3348.pdf"
        part["dimensions_mm"] = {"length": 4.0, "width": 4.0, "height": 5.4}
        part["dimension_reference"] = {
            "document": "RVT1H1R0M0405 datasheet (C3348 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D4.0 x 5.4 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "1 uF",
            "rated_voltage": "50 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_4x5.4",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D4xL5.4mm Honor Elec RVT1H1R0M0405 (C3348); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_4x5.4 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3349 / Honor Elec RVT1H470M0607 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_47_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D6.3 x 7.7 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291499908546560-C3349.pdf"
        part["dimensions_mm"] = {"length": 6.3, "width": 6.3, "height": 7.7}
        part["dimension_reference"] = {
            "document": "RVT1H470M0607 datasheet (C3349 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D6.3 x 7.7 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "50 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_6.3x7.7",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D6.3xL7.7mm Honor Elec RVT1H470M0607 (C3349); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_6.3x7.7 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3350 / Honor Elec RVT1V471M1010 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_470_micro_farad_35_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D10.0 x 10.2 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291518375931904-C3350.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 10.0, "height": 10.2}
        part["dimension_reference"] = {
            "document": "RVT1V471M1010 datasheet (C3350 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D10.0 x 10.2 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "35 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_10x10",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D10xL10.2mm Honor Elec RVT1V471M1010 (C3350); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_10x10 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3351 / Honor Elec RVT1E471M1010 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_470_micro_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D10.0 x 10.2 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757301218002132992-C3351.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 10.0, "height": 10.2}
        part["dimension_reference"] = {
            "document": "RVT1E471M1010 datasheet (C3351 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D10.0 x 10.2 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "25 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_10x10",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D10xL10.2mm Honor Elec RVT1E471M1010 (C3351); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_10x10 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3352 / Honor Elec RVT1H101M0810 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_10_2_mm_tall_electrolytic_100_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D8.0 x 10.2 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291464793563136-C3352.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 10.2}
        part["dimension_reference"] = {
            "document": "RVT1H101M0810 datasheet (C3352 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D8.0 x 10.2 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "50 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_8x10",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D8xL10.2mm Honor Elec RVT1H101M0810 (C3352); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_8x10 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3353 / Honor Elec RVT1E221M0810 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_10_5_mm_tall_electrolytic_220_micro_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D8.0 x 10.5 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291495722901504-C3353.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 10.5}
        part["dimension_reference"] = {
            "document": "RVT1E221M0810 datasheet (C3353 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D8.0 x 10.5 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "25 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_8x10.5",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D8xL10.5mm Honor Elec RVT1E221M0810 (C3353); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_8x10.5 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3354 / Honor Elec RVT0J471M0607 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_470_micro_farad_6_3_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D6.3 x 7.7 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291503796260864-C3354.pdf"
        part["dimensions_mm"] = {"length": 6.3, "width": 6.3, "height": 7.7}
        part["dimension_reference"] = {
            "document": "RVT0J471M0607 datasheet (C3354 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D6.3 x 7.7 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "6.3 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_6.3x7.7",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D6.3xL7.7mm Honor Elec RVT0J471M0607 (C3354); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_6.3x7.7 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3355 / Honor Elec RVT1V4R7M0405 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_4_mm_diameter_5_4_mm_tall_electrolytic_4_7_micro_farad_35_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D4.0 x 5.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291555902234624-C3355.pdf"
        part["dimensions_mm"] = {"length": 4.0, "width": 4.0, "height": 5.4}
        part["dimension_reference"] = {
            "document": "RVT1V4R7M0405 datasheet (C3355 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D4.0 x 5.4 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "35 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_4x5.4",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D4xL5.4mm Honor Elec RVT1V4R7M0405 (C3355); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_4x5.4 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3356 / Honor Elec RVT1C220M0405 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_4_mm_diameter_5_4_mm_tall_electrolytic_22_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D4.0 x 5.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291559756935168-C3356.pdf"
        part["dimensions_mm"] = {"length": 4.0, "width": 4.0, "height": 5.4}
        part["dimension_reference"] = {
            "document": "RVT1C220M0405 datasheet (C3356 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D4.0 x 5.4 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "22 uF",
            "rated_voltage": "16 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_4x5.4",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D4xL5.4mm Honor Elec RVT1C220M0405 (C3356); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_4x5.4 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3357 / Honor Elec RVT1C100M0405 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_4_mm_diameter_5_4_mm_tall_electrolytic_10_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D4.0 x 5.4 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291564563337216-C3357.pdf"
        part["dimensions_mm"] = {"length": 4.0, "width": 4.0, "height": 5.4}
        part["dimension_reference"] = {
            "document": "RVT1C100M0405 datasheet (C3357 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D4.0 x 5.4 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "16 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_4x5.4",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D4xL5.4mm Honor Elec RVT1C100M0405 (C3357); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_4x5.4 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3358 / Honor Elec RVT1H221M1010 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_220_micro_farad_50_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D10.0 x 10.2 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757302535411372032-C3358.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 10.0, "height": 10.2}
        part["dimension_reference"] = {
            "document": "RVT1H221M1010 datasheet (C3358 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D10.0 x 10.2 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "50 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_10x10",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D10xL10.2mm Honor Elec RVT1H221M1010 (C3358); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_10x10 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3359 / Honor Elec RVT1C102M1010 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_1000_micro_farad_16_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SMD V-chip aluminum electrolytic, D10.0 x 10.2 mm"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757291574172487680-C3359.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 10.0, "height": 10.2}
        part["dimension_reference"] = {
            "document": "RVT1C102M1010 datasheet (C3359 provenance)",
            "pages": [1, 2],
            "notes": "SMD V-chip aluminum electrolytic, D10.0 x 10.2 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "1000 uF",
            "rated_voltage": "16 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "ripple_current": "347mA",
            "polarized": True,
            "operating_temperature": "-55 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_SMD:CP_Elec_10x10",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists SMD,D10xL10.2mm Honor Elec RVT1C102M1010 (C3359); identity and ratings observed live at intake 2026-09-29.",
            "Two-terminal polarized V-chip SMD capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_SMD:CP_Elec_10x10 footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5154 / CX(Dongguan Chengxing Elec) GR477M025F14RR0VL4FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_8_mm_diameter_14_mm_tall_electrolytic_470_micro_farad_25_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D8.0 x 14.0 mm, 3.5 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588919191097790464-C5154.pdf"
        part["dimensions_mm"] = {"length": 8.0, "width": 8.0, "height": 14.0}
        part["dimension_reference"] = {
            "document": "GR477M025F14RR0VL4FP0 datasheet (C5154 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D8.0 x 14.0 mm, 3.5 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "25 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "3000hrs@105 C",
            "pin_spacing": "3.5 mm",
            "polarized": True,
            "operating_temperature": "-40 to +105 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D8xL14mm CX(Dongguan Chengxing Elec) GR477M025F14RR0VL4FP0 (C5154); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D8.0mm_P3.50mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5300 / CX(Dongguan Chengxing Elec) KM156M400G17RR0VH2FP0 - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_10_mm_diameter_17_mm_tall_electrolytic_15_micro_farad_400_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Radial leaded aluminum electrolytic, D10.0 x 17.0 mm, 5.0 mm pin spacing"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887030889242625-C5300.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 10.0, "height": 17.0}
        part["dimension_reference"] = {
            "document": "KM156M400G17RR0VH2FP0 datasheet (C5300 provenance)",
            "pages": [1, 2],
            "notes": "Radial leaded aluminum electrolytic, D10.0 x 17.0 mm, 5.0 mm pin spacing; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "15 uF",
            "rated_voltage": "400 V",
            "tolerance": "+-20%",
            "dielectric": "aluminum electrolytic",
            "lifetime": "2000hrs@105 C",
            "pin_spacing": "5.0 mm",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Plugin,D10xL17mm CX(Dongguan Chengxing Elec) KM156M400G17RR0VH2FP0 (C5300); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized radial leaded capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_THT:CP_Radial_D10.0mm_P5.00mm footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7173 / -- TAJA104K035RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_100_nano_farad_35_volt_avx_taja104k035rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7173 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 nF",
            "rated_voltage": "35 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA104K035RNJ (C7173); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7174 / -- TAJA105K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_1_micro_farad_16_volt_avx_taja105k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7174 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "1 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA105K016RNJ (C7174); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7175 / -- TAJA105K025RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_1_micro_farad_25_volt_avx_taja105k025rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7175 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "1 uF",
            "rated_voltage": "25 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA105K025RNJ (C7175); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7176 / -- TAJA105K035RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_1_micro_farad_35_volt_avx_taja105k035rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7176 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "1 uF",
            "rated_voltage": "35 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA105K035RNJ (C7176); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7177 / -- TAJA106K010RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_10_micro_farad_10_volt_avx_taja106k010rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7177 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "10 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA106K010RNJ (C7177); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7179 / -- TAJA155K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_1_5_micro_farad_16_volt_avx_taja155k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7179 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "1.5 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA155K016RNJ (C7179); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7180 / -- TAJA225K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_2_2_micro_farad_16_volt_avx_taja225k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7180 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "2.2 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA225K016RNJ (C7180); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7181 / -- TAJA225K025RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_2_2_micro_farad_25_volt_avx_taja225k025rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7181 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "2.2 uF",
            "rated_voltage": "25 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA225K025RNJ (C7181); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7182 / -- TAJA226K006RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_22_micro_farad_6_3_volt_avx_taja226k006rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7182 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "22 uF",
            "rated_voltage": "6.3 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA226K006RNJ (C7182); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7183 / -- TAJA226M010RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_22_micro_farad_10_volt_avx_taja226m010rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7183 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "22 uF",
            "rated_voltage": "10 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA226M010RNJ (C7183); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7184 / -- TAJA335K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_3_3_micro_farad_16_volt_avx_taja335k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7184 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "3.3 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA335K016RNJ (C7184); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7185 / -- TAJA336K006RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_33_micro_farad_6_3_volt_avx_taja336k006rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7185 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "33 uF",
            "rated_voltage": "6.3 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA336K006RNJ (C7185); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7186 / -- TAJA336K010RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_33_micro_farad_10_volt_avx_taja336k010rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7186 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "33 uF",
            "rated_voltage": "10 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA336K010RNJ (C7186); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7187 / -- TAJA475K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_16_volt_avx_taja475k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7187 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA475K016RNJ (C7187); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7188 / -- TAJA475K020RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_20_volt_avx_taja475k020rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7188 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "20 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA475K020RNJ (C7188); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7189 / -- TAJA475K025RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_25_volt_avx_taja475k025rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7189 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "25 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA475K025RNJ (C7189); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7190 / -- TAJA476K006RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_47_micro_farad_6_3_volt_avx_taja476k006rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7190 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "6.3 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA476K006RNJ (C7190); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7191 / -- TAJA685K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3216_avx_a_tantalum_6_8_micro_farad_16_volt_avx_taja685k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6, "height": 1.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7191 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case A (3216-18), 3.2 x 1.6 x 1.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "6.8 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-A-3216-18",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-A-3216-18(mm) -- TAJA685K016RNJ (C7191); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7192 / -- TAJB105K035RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_1_micro_farad_35_volt_avx_tajb105k035rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7192 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "1 uF",
            "rated_voltage": "35 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB105K035RNJ (C7192); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7193 / -- TAJB106K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_10_micro_farad_16_volt_avx_tajb106k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7193 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB106K016RNJ (C7193); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7194 / -- TAJB106K025RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_10_micro_farad_25_volt_avx_tajb106k025rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7194 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "25 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB106K025RNJ (C7194); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7195 / -- TAJB107M006RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_100_micro_farad_6_3_volt_avx_tajb107m006rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7195 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "6.3 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB107M006RNJ (C7195); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7196 / -- TAJB107M010RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_100_micro_farad_10_volt_avx_tajb107m010rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7196 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "10 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB107M010RNJ (C7196); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7198 / -- TAJB226K010RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_22_micro_farad_10_volt_avx_tajb226k010rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7198 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "22 uF",
            "rated_voltage": "10 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB226K010RNJ (C7198); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7199 / -- TAJB226K020RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_22_micro_farad_20_volt_avx_tajb226k020rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7199 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "22 uF",
            "rated_voltage": "20 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB226K020RNJ (C7199); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7200 / -- TAJB227M004RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_220_micro_farad_4_volt_avx_tajb227m004rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7200 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "4 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB227M004RNJ (C7200); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7201 / -- TAJB335K035RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_3_3_micro_farad_35_volt_avx_tajb335k035rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7201 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "3.3 uF",
            "rated_voltage": "35 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB335K035RNJ (C7201); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7202 / -- TAJB336K010RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_33_micro_farad_10_volt_avx_tajb336k010rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7202 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "33 uF",
            "rated_voltage": "10 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB336K010RNJ (C7202); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7203 / -- TAJB336K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_33_micro_farad_16_volt_avx_tajb336k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7203 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "33 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB336K016RNJ (C7203); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7204 / -- TAJB475K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_4_7_micro_farad_16_volt_avx_tajb475k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7204 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB475K016RNJ (C7204); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7205 / -- TAJB475K025RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_4_7_micro_farad_25_volt_avx_tajb475k025rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7205 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "25 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB475K025RNJ (C7205); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7206 / -- TAJB475K035RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_4_7_micro_farad_35_volt_avx_tajb475k035rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7206 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "4.7 uF",
            "rated_voltage": "35 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB475K035RNJ (C7206); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7207 / -- TAJB476K006RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_47_micro_farad_6_3_volt_avx_tajb476k006rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7207 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "6.3 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB476K006RNJ (C7207); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7208 / -- TAJB476M006RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_3528_avx_b_tantalum_47_micro_farad_6_3_volt_avx_tajb476m006rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 3.5, "width": 2.8, "height": 2.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7208 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case B (3528-21), 3.5 x 2.8 x 2.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "6.3 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-B-3528-21",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-B-3528-21(mm) -- TAJB476M006RNJ (C7208); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7209 / -- TAJC106K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6032_avx_c_tantalum_10_micro_farad_16_volt_avx_tajc106k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 6.0, "width": 3.2, "height": 2.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7209 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-C-6032-28",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-C-6032-28(mm) -- TAJC106K016RNJ (C7209); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7210 / -- TAJC106K025RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6032_avx_c_tantalum_10_micro_farad_25_volt_avx_tajc106k025rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 6.0, "width": 3.2, "height": 2.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7210 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "25 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-C-6032-28",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-C-6032-28(mm) -- TAJC106K025RNJ (C7210); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7211 / -- TAJC106K035RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6032_avx_c_tantalum_10_micro_farad_35_volt_avx_tajc106k035rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 6.0, "width": 3.2, "height": 2.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7211 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "35 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-C-6032-28",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-C-6032-28(mm) -- TAJC106K035RNJ (C7211); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7214 / -- TAJC226K025RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6032_avx_c_tantalum_22_micro_farad_25_volt_avx_tajc226k025rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 6.0, "width": 3.2, "height": 2.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7214 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "22 uF",
            "rated_voltage": "25 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-C-6032-28",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-C-6032-28(mm) -- TAJC226K025RNJ (C7214); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7216 / -- TAJC227K006RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6032_avx_c_tantalum_220_micro_farad_6_3_volt_avx_tajc227k006rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 6.0, "width": 3.2, "height": 2.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7216 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "6.3 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-C-6032-28",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-C-6032-28(mm) -- TAJC227K006RNJ (C7216); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7217 / -- TAJC336K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6032_avx_c_tantalum_33_micro_farad_16_volt_avx_tajc336k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 6.0, "width": 3.2, "height": 2.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7217 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "33 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-C-6032-28",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-C-6032-28(mm) -- TAJC336K016RNJ (C7217); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7219 / -- TAJC476K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6032_avx_c_tantalum_47_micro_farad_16_volt_avx_tajc476k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 6.0, "width": 3.2, "height": 2.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7219 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-C-6032-28",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-C-6032-28(mm) -- TAJC476K016RNJ (C7219); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7220 / -- TAJC686K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_6032_avx_c_tantalum_68_micro_farad_16_volt_avx_tajc686k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 6.0, "width": 3.2, "height": 2.8}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7220 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case C (6032-28), 6.0 x 3.2 x 2.8 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "68 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-C-6032-28",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-C-6032-28(mm) -- TAJC686K016RNJ (C7220); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7221 / -- TAJD106K035RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_d_tantalum_10_micro_farad_35_volt_avx_tajd106k035rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 3.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7221 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "35 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-D-7343-31",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-D-7343-31(mm) -- TAJD106K035RNJ (C7221); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7222 / -- TAJD107K010RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_d_tantalum_100_micro_farad_10_volt_avx_tajd107k010rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 3.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7222 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "10 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-D-7343-31",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-D-7343-31(mm) -- TAJD107K010RNJ (C7222); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7223 / -- TAJD107K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_d_tantalum_100_micro_farad_16_volt_avx_tajd107k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 3.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7223 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-D-7343-31",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-D-7343-31(mm) -- TAJD107K016RNJ (C7223); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7224 / -- TAJD107K020RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_d_tantalum_100_micro_farad_20_volt_avx_tajd107k020rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 3.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7224 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "20 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-D-7343-31",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-D-7343-31(mm) -- TAJD107K020RNJ (C7224); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7225 / -- TAJD226K035RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_d_tantalum_22_micro_farad_35_volt_avx_tajd226k035rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 3.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7225 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "22 uF",
            "rated_voltage": "35 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-D-7343-31",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-D-7343-31(mm) -- TAJD226K035RNJ (C7225); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7226 / -- TAJD337K010RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_d_tantalum_330_micro_farad_10_volt_avx_tajd337k010rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 3.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7226 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "330 uF",
            "rated_voltage": "10 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-D-7343-31",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-D-7343-31(mm) -- TAJD337K010RNJ (C7226); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7227 / -- TAJD476K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_d_tantalum_47_micro_farad_16_volt_avx_tajd476k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 3.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7227 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-D-7343-31",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-D-7343-31(mm) -- TAJD476K016RNJ (C7227); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7228 / -- TAJD476K025RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_d_tantalum_47_micro_farad_25_volt_avx_tajd476k025rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 3.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7228 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "25 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-D-7343-31",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-D-7343-31(mm) -- TAJD476K025RNJ (C7228); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7229 / -- TAJD477K006RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_d_tantalum_470_micro_farad_6_3_volt_avx_tajd477k006rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 3.1}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7229 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case D (7343-31), 7.3 x 4.3 x 3.1 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "6.3 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-D-7343-31",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-D-7343-31(mm) -- TAJD477K006RNJ (C7229); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7230 / -- TAJE107M025RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_e_tantalum_100_micro_farad_25_volt_avx_taje107m025rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case E (7343-43), 7.3 x 4.3 x 4.3 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 4.3}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7230 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case E (7343-43), 7.3 x 4.3 x 4.3 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "100 uF",
            "rated_voltage": "25 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-E-7343-43",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-E-7343-43(mm) -- TAJE107M025RNJ (C7230); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7231 / -- TAJE227K016RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_e_tantalum_220_micro_farad_16_volt_avx_taje227k016rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case E (7343-43), 7.3 x 4.3 x 4.3 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 4.3}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7231 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case E (7343-43), 7.3 x 4.3 x 4.3 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "220 uF",
            "rated_voltage": "16 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-E-7343-43",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-E-7343-43(mm) -- TAJE227K016RNJ (C7231); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7232 / -- TAJE337K010RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_e_tantalum_330_micro_farad_10_volt_avx_taje337k010rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case E (7343-43), 7.3 x 4.3 x 4.3 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 4.3}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7232 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case E (7343-43), 7.3 x 4.3 x 4.3 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "330 uF",
            "rated_voltage": "10 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-E-7343-43",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-E-7343-43(mm) -- TAJE337K010RNJ (C7232); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7233 / -- TAJE476K035RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_e_tantalum_47_micro_farad_35_volt_avx_taje476k035rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case E (7343-43), 7.3 x 4.3 x 4.3 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 4.3}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7233 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case E (7343-43), 7.3 x 4.3 x 4.3 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "47 uF",
            "rated_voltage": "35 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-E-7343-43",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-E-7343-43(mm) -- TAJE476K035RNJ (C7233); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7234 / -- TAJE477K010RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_7343_avx_e_tantalum_470_micro_farad_10_volt_avx_taje477k010rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case E (7343-43), 7.3 x 4.3 x 4.3 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 7.3, "width": 4.3, "height": 4.3}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7234 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case E (7343-43), 7.3 x 4.3 x 4.3 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "470 uF",
            "rated_voltage": "10 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-E-7343-43",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-E-7343-43(mm) -- TAJE477K010RNJ (C7234); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C7235 / -- TAJR106M006RNJ - polarized capacitor family batch 2026-10-05
    current = "electronic_capacitor_2012_avx_r_tantalum_10_micro_farad_6_3_volt_avx_tajr106m006rnej"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Kyocera AVX TAJ case R (2012-12), 2.0 x 1.25 x 1.2 mm"
        part["datasheet_url"] = "https://datasheets.kyocera-avx.com/TAJ.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 1.2}
        part["dimension_reference"] = {
            "document": "KYOCERA AVX TAJ series datasheet (C7235 provenance)",
            "pages": [1, 2],
            "notes": "Kyocera AVX TAJ case R (2012-12), 2.0 x 1.25 x 1.2 mm; polarity stripe/minus band marks the negative terminal per the datasheet outline drawing.",
        }
        part["electrical"] = {
            "capacitance": "10 uF",
            "rated_voltage": "6.3 V",
            "dielectric": "solid manganese dioxide tantalum",
            "case_size": "CASE-R-2012-12",
            "polarized": True,
            "operating_temperature": "-55 to +125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-2012-12_Kemet-R",
            "hand_solder": "Capacitor_Tantalum_SMD:CP_EIA-2012-12_Kemet-R_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists CASE-R-2012-12(mm) -- TAJR106M006RNJ (C7235); identity and ratings observed live at intake 2026-09-30.",
            "Two-terminal polarized SMD chip capacitor mapped to the KiCad Device:C_Polarized master and the Capacitor_Tantalum_SMD:CP_EIA-2012-12_Kemet-R footprint master in the 2026-10-05 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated polarized cap batch (tmp/cap_batch.py) ===