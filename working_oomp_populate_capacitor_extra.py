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
