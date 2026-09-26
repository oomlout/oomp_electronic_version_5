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
            "LCSC stock research 2026-09: highest-stock listing first (C106997, 2,467,600 in stock at capture); runners-up follow."
        ]
        from working_oomp_populate_jlc import set_preferred_jlc
        set_preferred_jlc(
            part,
            code="C1548",
            manufacturer="FH (Guangdong Fenghua Advanced Tech)",
            mpn="0402CG150J500NT",
            selection={
                "verified_on": "2026-09-24",
                "official_url": "https://jlcpcb.com/partdetail/1900-0402CG150J500NT/C1548",
                "tier": "basic",
                "tier_label_observed": "Basic",
                "stock_observed": 1465932,
                "purchase_moq_observed": 1,
                "pcba_min_qty_observed": None,
                "compatibility_notes": "Existing generic 0402 15 pF capacitor. FH C1548 is 50 V C0G +/-5%; prior YAGEO C106997 is recorded as 50 V NP0 +/-5%. C0G/NP0 are the same Class I temperature characteristic. Preserve C106997 and other alternatives; project RF/Q requirements need full review.",
                "ratings": {
                    "capacitance": "15 pF",
                    "rated_voltage": "50 V",
                    "dielectric": "C0G",
                    "tolerance": "+/-5%",
                },
                "datasheet_pages": [],
                "pinout_checked": False,
                "footprint_checked": False,
                "visual_review": "pending",
            },
        )

    current = "electronic_capacitor_0402_18_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
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
            "LCSC stock research 2026-09: highest-stock listing first (C106202, 2,093,000 in stock at capture); runners-up follow."
        ]
        from working_oomp_populate_jlc import set_preferred_jlc
        set_preferred_jlc(
            part,
            code="C1549",
            manufacturer="FH (Guangdong Fenghua Advanced Tech)",
            mpn="0402CG180J500NT",
            selection={
                "verified_on": "2026-09-24",
                "official_url": "https://jlcpcb.com/partdetail/1901-0402CG180J500NT/C1549",
                "tier": "basic",
                "tier_label_observed": "Basic",
                "stock_observed": 727917,
                "purchase_moq_observed": 1,
                "pcba_min_qty_observed": None,
                "compatibility_notes": "Existing generic 0402 18 pF capacitor. FH C1549 is 50 V C0G +/-5%; previous YAGEO C106202 is 50 V NP0 +/-5%. C0G/NP0 are the same Class I temperature characteristic. Preserve C106202 and other alternatives; project-specific RF/Q requirements need full review.",
                "ratings": {
                    "capacitance": "18 pF",
                    "rated_voltage": "50 V",
                    "dielectric": "C0G",
                    "tolerance": "+/-5%",
                },
                "datasheet_pages": [],
                "pinout_checked": False,
                "footprint_checked": False,
                "visual_review": "pending",
            },
        )

    current = "electronic_capacitor_0402_1_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
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
            "LCSC stock research 2026-09: highest-stock listing first (C106203, 2,991,500 in stock at capture); runners-up follow."
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
            {"part_number": "C1591", "product_name": "100nF ±10% 25V X7R 0603 Ceramic Capacitor"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "CC0603KRX7R9BB104"},
            {"manufacturer": "FH", "part_number": "0603B104K500NT"},
            {"manufacturer": "Samsung Electro-Mechanics", "part_number": "CL10B104KB8NNNC"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C14663, 10,855,500 in stock at capture); runners-up follow."
        ]

    current = "electronic_capacitor_0603_10_micro_farad"
    if current in extras_dict:
        part = extras_dict[current]
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

    current = "electronic_capacitor_0603_22_pico_farad"
    if current in extras_dict:
        part = extras_dict[current]
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

    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="capacitor")
