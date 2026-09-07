def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_resistor_0402_510000_ohm"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer_uni_royal"] = "0402WGF5103TCE"
        extras_dict[current]["part_number_lcsc_uni_royal"] = "C11616"

    # --- LCSC stock research (browser captures parsed by kicad_agents/lcsc_capture_parser.py) ---

    current = "electronic_resistor_0402_100000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGJ0104TCE"
        part["part_number_lcsc"] = "C25530"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25530.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25530", "product_name": "100kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25741", "product_name": "100kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C60491", "product_name": "62.5mW 100kΩ 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surface Mount RoHS"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "UNI-ROYAL", "part_number": "0402WGJ0104TCE"},
            {"manufacturer": "UNI-ROYAL", "part_number": "0402WGF1003TCE"},
            {"manufacturer": "YAGEO", "part_number": "RC0402FR-07100KL"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C25530, 9,536,600 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0402_10000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1002TS"
        part["part_number_lcsc"] = "C2906861"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2906861.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2906861", "product_name": "10kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25744", "product_name": "10kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C60490", "product_name": "50V 10kΩ Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surface Mount RoHS"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "FOJAN", "part_number": "FRC0402F1002TS"},
            {"manufacturer": "UNI-ROYAL", "part_number": "0402WGF1002TCE"},
            {"manufacturer": "YAGEO", "part_number": "RC0402FR-0710KL"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C2906861, 18,322,800 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0402_1000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1001TS"
        part["part_number_lcsc"] = "C2906864"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2906864.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2906864", "product_name": "1kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C105637", "product_name": "1kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C106235", "product_name": "50V Thick Film Resistor 62.5mW 1kΩ ±1% ±100ppm/℃ 0402 Chip Resistor - Surface Mount RoHS"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "FOJAN", "part_number": "FRC0402F1001TS"},
            {"manufacturer": "YAGEO", "part_number": "RC0402JR-071KL"},
            {"manufacturer": "YAGEO", "part_number": "RC0402FR-071KL"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C2906864, 15,276,400 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0402_2000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF2001TCE"
        part["part_number_lcsc"] = "C4109"
        part["product_url"] = "https://www.lcsc.com/product-detail/C4109.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C4109", "product_name": "2kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909344", "product_name": "2kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C137887", "product_name": "2kΩ 62.5mW 50V ±5% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surface Mount RoHS"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "UNI-ROYAL", "part_number": "0402WGF2001TCE"},
            {"manufacturer": "FOJAN", "part_number": "FRC0402F2001TS"},
            {"manufacturer": "YAGEO", "part_number": "RC0402JR-072KL"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C4109, 6,285,400 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0402_200_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF2000TCE"
        part["part_number_lcsc"] = "C25087"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25087.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25087", "product_name": "200Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909333", "product_name": "200Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920644", "product_name": "200Ω ±100ppm/℃ ±1% 50V 62.5mW Thick Film Resistor 0402 Chip Resistor - Surface Mount"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "UNI-ROYAL", "part_number": "0402WGF2000TCE"},
            {"manufacturer": "FOJAN", "part_number": "FRC0402F2000TS"},
            {"manufacturer": "HWA CHN", "part_number": "HRC0402F2000DNTO"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C25087, 2,584,400 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0402_22_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0722RL"
        part["part_number_lcsc"] = "C114765"
        part["product_url"] = "https://www.lcsc.com/product-detail/C114765.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C114765", "product_name": "50V Thick Film Resistor 62.5mW 22Ω ±1% ±100ppm/℃ 0402 Chip Resistor - Surface Mount RoHS"},
            {"part_number": "C25092", "product_name": "22Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2929994", "product_name": "22Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "RC0402FR-0722RL"},
            {"manufacturer": "UNI-ROYAL", "part_number": "0402WGF220JTCE"},
            {"manufacturer": "FOJAN", "part_number": "FRC0402F22R0TS"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C114765, 4,357,300 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0402_33000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F3302TS"
        part["part_number_lcsc"] = "C2909350"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909350.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909350", "product_name": "33kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C138003", "product_name": "33kΩ 50V Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surface Mount RoHS"},
            {"part_number": "C25779", "product_name": "33kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "FOJAN", "part_number": "FRC0402F3302TS"},
            {"manufacturer": "YAGEO", "part_number": "RC0402FR-0733KL"},
            {"manufacturer": "UNI-ROYAL", "part_number": "0402WGF3302TCE"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C2909350, 1,501,000 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0402_5100_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF5101TCE"
        part["part_number_lcsc"] = "C25905"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25905.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25905", "product_name": "5.1kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906874", "product_name": "5.1kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C105872", "product_name": "62.5mW 5.1kΩ 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surface Mount RoHS"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "UNI-ROYAL", "part_number": "0402WGF5101TCE"},
            {"manufacturer": "FOJAN", "part_number": "FRC0402F5101TS"},
            {"manufacturer": "YAGEO", "part_number": "RC0402FR-075K1L"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C25905, 5,618,500 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0603_100000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0603WAF1003T5E"
        part["part_number_lcsc"] = "C25803"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25803.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25803", "product_name": "100kΩ ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C2906980", "product_name": "100kΩ ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C14675", "product_name": "100kΩ 100mW 75V ±1% ±100ppm/℃ Thick Film Resistor 0603 Chip Resistor - Surface Mount RoHS"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAF1003T5E"},
            {"manufacturer": "FOJAN", "part_number": "FRC0603F1003TS"},
            {"manufacturer": "YAGEO", "part_number": "RC0603FR-07100KL"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C25803, 17,818,900 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0603_10000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0603FR-0710KL"
        part["part_number_lcsc"] = "C98220"
        part["product_url"] = "https://www.lcsc.com/product-detail/C98220.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C98220", "product_name": "10kΩ 100mW 75V ±1% ±100ppm/℃ Thick Film Resistor 0603 Chip Resistor - Surface Mount RoHS"},
            {"part_number": "C2906982", "product_name": "10kΩ ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C99198", "product_name": "75V 10kΩ Thick Film Resistor 100mW ±5% ±100ppm/℃ 0603 Chip Resistor - Surface Mount RoHS"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "YAGEO", "part_number": "RC0603FR-0710KL"},
            {"manufacturer": "FOJAN", "part_number": "FRC0603F1002TS"},
            {"manufacturer": "YAGEO", "part_number": "RC0603JR-0710KL"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C98220, 11,903,000 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0603_1000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0603F1001TS"
        part["part_number_lcsc"] = "C2907002"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2907002.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2907002", "product_name": "1kΩ ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C21190", "product_name": "1kΩ ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C22548", "product_name": "1kΩ 100mW 75V ±1% ±100ppm/℃ Thick Film Resistor 0603 Chip Resistor - Surface Mount RoHS"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "FOJAN", "part_number": "FRC0603F1001TS"},
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAF1001T5E"},
            {"manufacturer": "YAGEO", "part_number": "RC0603FR-071KL"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C2907002, 13,177,800 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0603_2200_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0603WAF2201T5E"
        part["part_number_lcsc"] = "C4190"
        part["product_url"] = "https://www.lcsc.com/product-detail/C4190.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C4190", "product_name": "2.2kΩ ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C2907005", "product_name": "2.2kΩ ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C25992", "product_name": "2.2kΩ ±5% 100mW 0603 Thick Film Resistor"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAF2201T5E"},
            {"manufacturer": "FOJAN", "part_number": "FRC0603F2201TS"},
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAJ0222T5E"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C4190, 5,071,800 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0603_33_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0603WAF330JT5E"
        part["part_number_lcsc"] = "C23140"
        part["product_url"] = "https://www.lcsc.com/product-detail/C23140.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C23140", "product_name": "33Ω ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C2909394", "product_name": "33Ω ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C25232", "product_name": "33Ω ±5% 100mW 0603 Thick Film Resistor"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAF330JT5E"},
            {"manufacturer": "FOJAN", "part_number": "FRC0603F33R0TS"},
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAJ0330T5E"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C23140, 4,105,300 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0603_4700_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0603WAF4701T5E"
        part["part_number_lcsc"] = "C23162"
        part["product_url"] = "https://www.lcsc.com/product-detail/C23162.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C23162", "product_name": "4.7kΩ ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C99782", "product_name": "4.7kΩ 100mW 75V ±1% ±100ppm/℃ Thick Film Resistor 0603 Chip Resistor - Surface Mount RoHS"},
            {"part_number": "C2907034", "product_name": "4.7kΩ ±1% 100mW 0603 Thick Film Resistor"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAF4701T5E"},
            {"manufacturer": "YAGEO", "part_number": "RC0603FR-074K7L"},
            {"manufacturer": "FOJAN", "part_number": "FRC0603F4701TS"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C23162, 17,752,300 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0603_470_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0603WAF4700T5E"
        part["part_number_lcsc"] = "C23179"
        part["product_url"] = "https://www.lcsc.com/product-detail/C23179.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C23179", "product_name": "470Ω ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C25241", "product_name": "470Ω ±5% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C2907041", "product_name": "470Ω ±1% 100mW 0603 Thick Film Resistor"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAF4700T5E"},
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAJ0471T5E"},
            {"manufacturer": "FOJAN", "part_number": "FRC0603F4700TS"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C23179, 5,689,600 in stock at capture); runners-up follow."
        ]

    current = "electronic_resistor_0603_5100_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0603WAF5101T5E"
        part["part_number_lcsc"] = "C23186"
        part["product_url"] = "https://www.lcsc.com/product-detail/C23186.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C23186", "product_name": "5.1kΩ ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C2907044", "product_name": "5.1kΩ ±1% 100mW 0603 Thick Film Resistor"},
            {"part_number": "C26000", "product_name": "5.1kΩ ±5% 100mW 0603 Thick Film Resistor"},
        ]
        part["part_numbers_manufacturer"] = [
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAF5101T5E"},
            {"manufacturer": "FOJAN", "part_number": "FRC0603F5101TS"},
            {"manufacturer": "UNI-ROYAL", "part_number": "0603WAJ0512T5E"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock listing first (C23186, 20,435,000 in stock at capture); runners-up follow."
        ]

    # --- LCSC stock research 2026-09 batch: 0402 values (browser captures parsed by kicad_agents/lcsc_capture_parser.py, JLCPCB Part Class verified on every product page) ---

    current = "electronic_resistor_0402_0_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402P000 TS"
        part["part_number_lcsc"] = "C2906877"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2906877.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2906877", "product_name": "0Ω 62.5mW 50V Thick Film Resistor ±5% 0402 Chip Resistor - Surface Mount"},
            {"part_number": "C17168", "product_name": "0Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906858", "product_name": "0Ω 62.5mW 50V Thick Film Resistor ±1% ±400ppm/℃ 0402 Chip Resistor - Surface ..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2906877 with 15,744,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_10_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0710RL"
        part["part_number_lcsc"] = "C138066"
        part["product_url"] = "https://www.lcsc.com/product-detail/C138066.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C138066", "product_name": "62.5mW 10Ω 50V ±200ppm/℃ ±1% Thick Film Resistor 0402 Chip Resistor - Surface..."},
            {"part_number": "C2906886", "product_name": "10Ω ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C137925", "product_name": "62.5mW 10Ω 50V ±200ppm/℃ ±5% Thick Film Resistor 0402 Chip Resistor - Surface..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C138066 with 1,704,700 in stock at capture.",
        ]

    current = "electronic_resistor_0402_12_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F12R0TS"
        part["part_number_lcsc"] = "C2909317"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909317.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909317", "product_name": "12Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C274886", "product_name": "50V Thick Film Resistor 62.5mW 12Ω ±1% ±100ppm/℃ 0402 Chip Resistor - Surface..."},
            {"part_number": "C911955", "product_name": "12Ω ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909317 with 157,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_15_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0715RL"
        part["part_number_lcsc"] = "C138052"
        part["product_url"] = "https://www.lcsc.com/product-detail/C138052.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C138052", "product_name": "15Ω 62.5mW 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surface..."},
            {"part_number": "C2909323", "product_name": "15Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25083", "product_name": "15Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C138052 with 616,800 in stock at capture.",
        ]

    current = "electronic_resistor_0402_18_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F18R0TS"
        part["part_number_lcsc"] = "C2929991"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2929991.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2929991", "product_name": "18Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C138043", "product_name": "50V 18Ω Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surface..."},
            {"part_number": "C53064389", "product_name": "18Ω 50V 62.5mW ±5% Thick Film Resistor 0402 Chip Resistor - Surface Mount"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2929991 with 548,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_27_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF270JTCE"
        part["part_number_lcsc"] = "C25100"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25100.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25100", "product_name": "27Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25156", "product_name": "27Ω ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C138021", "product_name": "27Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C25100 with 121,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_33_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0733RL"
        part["part_number_lcsc"] = "C138002"
        part["product_url"] = "https://www.lcsc.com/product-detail/C138002.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C138002", "product_name": "33Ω 62.5mW 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surface..."},
            {"part_number": "C2906868", "product_name": "33Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C324773", "product_name": "33Ω 62.5mW ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surface Mount"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C138002 with 5,275,500 in stock at capture.",
        ]

    current = "electronic_resistor_0402_39_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0739RL"
        part["part_number_lcsc"] = "C185420"
        part["product_url"] = "https://www.lcsc.com/product-detail/C185420.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C185420", "product_name": "39Ω 62.5mW 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surface..."},
            {"part_number": "C2906939", "product_name": "39Ω ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25110", "product_name": "39Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C185420 with 160,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_47_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0747RL"
        part["part_number_lcsc"] = "C137973"
        part["product_url"] = "https://www.lcsc.com/product-detail/C137973.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C137973", "product_name": "50V Thick Film Resistor 62.5mW 47Ω ±1% ±100ppm/℃ 0402 Chip Resistor - Surface..."},
            {"part_number": "C2909362", "product_name": "47Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25118", "product_name": "47Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C137973 with 1,810,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_56_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F56R0TS"
        part["part_number_lcsc"] = "C3013179"
        part["product_url"] = "https://www.lcsc.com/product-detail/C3013179.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C3013179", "product_name": "56Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920812", "product_name": "56Ω 50V 62.5mW Thick Film Resistor ±200ppm/℃ ±5% 0402 Chip Resistor - Surface..."},
            {"part_number": "C137957", "product_name": "56Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C3013179 with 833,500 in stock at capture.",
        ]

    current = "electronic_resistor_0402_68_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F68R0TS"
        part["part_number_lcsc"] = "C2909380"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909380.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909380", "product_name": "68Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920697", "product_name": "68Ω ±1% 50V 62.5mW Thick Film Resistor ±200ppm/℃ 0402 Chip Resistor - Surface..."},
            {"part_number": "C2906961", "product_name": "68Ω ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909380 with 1,175,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_75_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0775RL"
        part["part_number_lcsc"] = "C114757"
        part["product_url"] = "https://www.lcsc.com/product-detail/C114757.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C114757", "product_name": "75Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906966", "product_name": "75Ω ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25133", "product_name": "75Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C114757 with 899,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_82_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F82R0TS"
        part["part_number_lcsc"] = "C2909389"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909389.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909389", "product_name": "82Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C163453", "product_name": "50V 82Ω Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surface..."},
            {"part_number": "C4143", "product_name": "82Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909389 with 1,132,900 in stock at capture.",
        ]

    current = "electronic_resistor_0402_100_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1000TS"
        part["part_number_lcsc"] = "C2906860"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2906860.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2906860", "product_name": "100Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C106232", "product_name": "50V Thick Film Resistor 62.5mW 100Ω ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C2906884", "product_name": "100Ω ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2906860 with 7,382,900 in stock at capture.",
        ]

    current = "electronic_resistor_0402_120_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1200TS"
        part["part_number_lcsc"] = "C2909315"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909315.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909315", "product_name": "120Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C114758", "product_name": "50V Thick Film Resistor 62.5mW 120Ω ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C25079", "product_name": "120Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909315 with 3,255,500 in stock at capture.",
        ]

    current = "electronic_resistor_0402_150_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FH"
        part["part_number_manufacturer"] = "RC-02K1500FT"
        part["part_number_lcsc"] = "C140202"
        part["product_url"] = "https://www.lcsc.com/product-detail/C140202.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C140202", "product_name": "150Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909321", "product_name": "150Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25143", "product_name": "150Ω ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C140202 with 208,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_180_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-07180RL"
        part["part_number_lcsc"] = "C138045"
        part["product_url"] = "https://www.lcsc.com/product-detail/C138045.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C138045", "product_name": "50V Thick Film Resistor 62.5mW 180Ω ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C38941", "product_name": "180Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909326", "product_name": "180Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C138045 with 384,400 in stock at capture.",
        ]

    current = "electronic_resistor_0402_220_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-07220RL"
        part["part_number_lcsc"] = "C112291"
        part["product_url"] = "https://www.lcsc.com/product-detail/C112291.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C112291", "product_name": "50V Thick Film Resistor 62.5mW 220Ω ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C2909336", "product_name": "220Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25091", "product_name": "220Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C112291 with 1,524,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_270_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F2700TS"
        part["part_number_lcsc"] = "C2909342"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909342.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909342", "product_name": "270Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906919", "product_name": "270Ω ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C163474", "product_name": "270Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909342 with 877,600 in stock at capture.",
        ]

    current = "electronic_resistor_0402_330_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402J331 TS"
        part["part_number_lcsc"] = "C2906929"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2906929.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2906929", "product_name": "330Ω ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2930002", "product_name": "330Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C105875", "product_name": "50V Thick Film Resistor 62.5mW 330Ω ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2906929 with 3,385,200 in stock at capture.",
        ]

    current = "electronic_resistor_0402_390_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-07390RL"
        part["part_number_lcsc"] = "C137997"
        part["product_url"] = "https://www.lcsc.com/product-detail/C137997.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C137997", "product_name": "50V 390Ω Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C2909353", "product_name": "390Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906937", "product_name": "390Ω ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C137997 with 1,956,500 in stock at capture.",
        ]

    current = "electronic_resistor_0402_470_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402J471 TS"
        part["part_number_lcsc"] = "C2906945"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2906945.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2906945", "product_name": "470Ω ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909361", "product_name": "470Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25117", "product_name": "470Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2906945 with 3,427,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_510_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-07510RL"
        part["part_number_lcsc"] = "C276273"
        part["product_url"] = "https://www.lcsc.com/product-detail/C276273.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C276273", "product_name": "50V 510Ω Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C25123", "product_name": "510Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909366", "product_name": "510Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C276273 with 1,996,900 in stock at capture.",
        ]

    current = "electronic_resistor_0402_560_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF5600TCE"
        part["part_number_lcsc"] = "C25126"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25126.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25126", "product_name": "560Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25172", "product_name": "560Ω ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C324803", "product_name": "560Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C25126 with 312,700 in stock at capture.",
        ]

    current = "electronic_resistor_0402_680_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-07680RL"
        part["part_number_lcsc"] = "C137948"
        part["product_url"] = "https://www.lcsc.com/product-detail/C137948.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C137948", "product_name": "62.5mW 680Ω 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfac..."},
            {"part_number": "C2906959", "product_name": "680Ω ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25177", "product_name": "680Ω ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C137948 with 624,200 in stock at capture.",
        ]

    current = "electronic_resistor_0402_750_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-07750RL"
        part["part_number_lcsc"] = "C137936"
        part["product_url"] = "https://www.lcsc.com/product-detail/C137936.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C137936", "product_name": "50V 750Ω Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C25132", "product_name": "750Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909382", "product_name": "750Ω ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C137936 with 414,200 in stock at capture.",
        ]

    current = "electronic_resistor_0402_820_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F8200TS"
        part["part_number_lcsc"] = "C2909387"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909387.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909387", "product_name": "820Ω ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920831", "product_name": "820Ω ±100ppm/℃ 50V 62.5mW Thick Film Resistor ±5% 0402 Chip Resistor - Surfac..."},
            {"part_number": "C2933122", "product_name": "820Ω ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909387 with 384,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_1200_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1201TS"
        part["part_number_lcsc"] = "C2909307"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909307.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909307", "product_name": "1.2kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920635", "product_name": "1.2kΩ ±100ppm/℃ ±1% 50V Thick Film Resistor 62.5mW 0402 Chip Resistor - Surfa..."},
            {"part_number": "C138040", "product_name": "1.2kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909307 with 608,400 in stock at capture.",
        ]

    current = "electronic_resistor_0402_1500_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF1501TCE"
        part["part_number_lcsc"] = "C25867"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25867.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25867", "product_name": "1.5kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2933074", "product_name": "1.5kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C114759", "product_name": "50V 1.5kΩ Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C25867 with 1,841,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_1800_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1801TS"
        part["part_number_lcsc"] = "C2909310"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909310.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909310", "product_name": "1.8kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C163481", "product_name": "1.8kΩ 62.5mW 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfa..."},
            {"part_number": "C2906882", "product_name": "1.8kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909310 with 478,300 in stock at capture.",
        ]

    current = "electronic_resistor_0402_2200_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402J222 TS"
        part["part_number_lcsc"] = "C2906920"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2906920.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2906920", "product_name": "2.2kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906865", "product_name": "2.2kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C163447", "product_name": "2.2kΩ 62.5mW 50V ±5% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2906920 with 3,096,800 in stock at capture.",
        ]

    current = "electronic_resistor_0402_2400_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402J242TS"
        part["part_number_lcsc"] = "C2929911"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2929911.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2929911", "product_name": "2.4kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C112296", "product_name": "50V 2.4kΩ Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C25882", "product_name": "2.4kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2929911 with 545,700 in stock at capture.",
        ]

    current = "electronic_resistor_0402_2700_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-072K7L"
        part["part_number_lcsc"] = "C138017"
        part["product_url"] = "https://www.lcsc.com/product-detail/C138017.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909332", "product_name": "2.7kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C138017", "product_name": "62.5mW 2.7kΩ 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfa..."},
            {"part_number": "C25885", "product_name": "2.7kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C138017 with 356,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_3300_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF3301TCE"
        part["part_number_lcsc"] = "C25890"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25890.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25890", "product_name": "3.3kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906923", "product_name": "3.3kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C137992", "product_name": "3.3kΩ 62.5mW 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C25890 with 1,667,600 in stock at capture.",
        ]

    current = "electronic_resistor_0402_3900_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-073K9L"
        part["part_number_lcsc"] = "C131467"
        part["product_url"] = "https://www.lcsc.com/product-detail/C131467.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C131467", "product_name": "50V Thick Film Resistor 62.5mW 3.9kΩ ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C2909346", "product_name": "3.9kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906925", "product_name": "3.9kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C131467 with 1,759,900 in stock at capture.",
        ]

    current = "electronic_resistor_0402_4700_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF4701TCE"
        part["part_number_lcsc"] = "C25900"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25900.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25900", "product_name": "4.7kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906941", "product_name": "4.7kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C105871", "product_name": "4.7kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C25900 with 13,820,600 in stock at capture.",
        ]

    current = "electronic_resistor_0402_5600_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F5601TS"
        part["part_number_lcsc"] = "C2909364"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909364.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909364", "product_name": "5.6kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25908", "product_name": "5.6kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C137856", "product_name": "5.6kΩ 62.5mW 50V ±5% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909364 with 228,700 in stock at capture.",
        ]

    current = "electronic_resistor_0402_6800_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-076K8L"
        part["part_number_lcsc"] = "C93940"
        part["product_url"] = "https://www.lcsc.com/product-detail/C93940.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C93940", "product_name": "50V Thick Film Resistor 6.8kΩ 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C2906876", "product_name": "6.8kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920698", "product_name": "±100ppm/℃ ±1% 50V 6.8kΩ Thick Film Resistor 62.5mW 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C93940 with 2,463,400 in stock at capture.",
        ]

    current = "electronic_resistor_0402_7500_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF7501TCE"
        part["part_number_lcsc"] = "C25918"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25918.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25918", "product_name": "7.5kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C137934", "product_name": "62.5mW 7.5kΩ 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfa..."},
            {"part_number": "C2960875", "product_name": "7.5kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C25918 with 1,180,900 in stock at capture.",
        ]

    current = "electronic_resistor_0402_8200_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF8201TCE"
        part["part_number_lcsc"] = "C25924"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25924.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25924", "product_name": "8.2kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909385", "product_name": "8.2kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C19267412", "product_name": "8.2kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C25924 with 184,600 in stock at capture.",
        ]

    current = "electronic_resistor_0402_12000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1202TS"
        part["part_number_lcsc"] = "C2909316"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909316.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909316", "product_name": "12kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C114760", "product_name": "50V Thick Film Resistor 62.5mW 12kΩ ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C25752", "product_name": "12kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909316 with 1,861,200 in stock at capture.",
        ]

    current = "electronic_resistor_0402_15000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402J153 TS"
        part["part_number_lcsc"] = "C2906893"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2906893.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2906893", "product_name": "15kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C114761", "product_name": "50V Thick Film Resistor 62.5mW 15kΩ ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C137917", "product_name": "50V Thick Film Resistor 62.5mW 15kΩ ±5% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2906893 with 1,119,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_18000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0718KL"
        part["part_number_lcsc"] = "C138044"
        part["product_url"] = "https://www.lcsc.com/product-detail/C138044.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C138044", "product_name": "50V 18kΩ Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C25762", "product_name": "18kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909327", "product_name": "18kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C138044 with 1,022,900 in stock at capture.",
        ]

    current = "electronic_resistor_0402_22000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0722KL"
        part["part_number_lcsc"] = "C82868"
        part["product_url"] = "https://www.lcsc.com/product-detail/C82868.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C82868", "product_name": "22kΩ 50V Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C25768", "product_name": "22kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906913", "product_name": "22kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C82868 with 1,025,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_27000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F2702TS"
        part["part_number_lcsc"] = "C2933084"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2933084.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2933084", "product_name": "27kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25771", "product_name": "27kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2929913", "product_name": "27kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2933084 with 668,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_39000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0739KL"
        part["part_number_lcsc"] = "C137995"
        part["product_url"] = "https://www.lcsc.com/product-detail/C137995.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C137995", "product_name": "39kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C844109", "product_name": "50V 62.5mW 39kΩ Thick Film Resistor ±100ppm/℃ ±1% 0402 Chip Resistor - Surfac..."},
            {"part_number": "C2930006", "product_name": "39kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C137995 with 1,484,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_47000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF4702TCE"
        part["part_number_lcsc"] = "C25792"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25792.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25792", "product_name": "47kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C93943", "product_name": "50V 47kΩ Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C2906946", "product_name": "47kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C25792 with 4,787,300 in stock at capture.",
        ]

    current = "electronic_resistor_0402_56000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-0756KL"
        part["part_number_lcsc"] = "C114756"
        part["product_url"] = "https://www.lcsc.com/product-detail/C114756.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C114756", "product_name": "50V Thick Film Resistor 62.5mW 56kΩ ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C2906875", "product_name": "56kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906955", "product_name": "56kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C114756 with 1,584,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_68000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F6802TS"
        part["part_number_lcsc"] = "C2909379"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909379.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909379", "product_name": "68kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C137947", "product_name": "50V Thick Film Resistor 62.5mW 68kΩ ±1% ±100ppm/℃ 0402 Chip Resistor - Surfac..."},
            {"part_number": "C36871", "product_name": "68kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909379 with 2,128,800 in stock at capture.",
        ]

    current = "electronic_resistor_0402_75000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F7502TS"
        part["part_number_lcsc"] = "C2909383"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909383.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909383", "product_name": "75kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C140129", "product_name": "75kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920828", "product_name": "±100ppm/℃ 75kΩ 50V Thick Film Resistor 62.5mW ±5% 0402 Chip Resistor - Surfac..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909383 with 251,400 in stock at capture.",
        ]

    current = "electronic_resistor_0402_82000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F8202TS"
        part["part_number_lcsc"] = "C2909388"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909388.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909388", "product_name": "82kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C4142", "product_name": "82kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906969", "product_name": "82kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909388 with 533,300 in stock at capture.",
        ]

    current = "electronic_resistor_0402_102000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1023TS"
        part["part_number_lcsc"] = "C2933066"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2933066.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2933066", "product_name": "102kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54863930", "product_name": "±1% 50V 62.5mW 102kΩ Thick Film Resistor ±200ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C852473", "product_name": "Thin Film Resistor 62.5mW 102kΩ ±0.1% ±25ppm/℃ 50V 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2933066 with 236,900 in stock at capture.",
        ]

    current = "electronic_resistor_0402_120000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1203TS"
        part["part_number_lcsc"] = "C2909314"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909314.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909314", "product_name": "120kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920620", "product_name": "120kΩ ±100ppm/℃ ±1% 50V Thick Film Resistor 62.5mW 0402 Chip Resistor - Surfa..."},
            {"part_number": "C25750", "product_name": "120kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909314 with 1,463,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_133000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1333TS"
        part["part_number_lcsc"] = "C2998045"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2998045.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2998045", "product_name": "133kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25753", "product_name": "133kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C49654184", "product_name": "62.5mW 133kΩ ±1% 50V Thick Film Resistor 0402 Chip Resistor - Surface Mount"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2998045 with 146,200 in stock at capture.",
        ]

    current = "electronic_resistor_0402_150000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-07150KL"
        part["part_number_lcsc"] = "C93947"
        part["product_url"] = "https://www.lcsc.com/product-detail/C93947.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C93947", "product_name": "150kΩ 50V Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C2909320", "product_name": "150kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906891", "product_name": "150kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C93947 with 825,800 in stock at capture.",
        ]

    current = "electronic_resistor_0402_180000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-07180KL"
        part["part_number_lcsc"] = "C138046"
        part["product_url"] = "https://www.lcsc.com/product-detail/C138046.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C138046", "product_name": "50V 180kΩ Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C25760", "product_name": "180kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909325", "product_name": "180kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C138046 with 530,800 in stock at capture.",
        ]

    current = "electronic_resistor_0402_220000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F2203TS"
        part["part_number_lcsc"] = "C2909335"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909335.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909335", "product_name": "220kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C138030", "product_name": "62.5mW 220kΩ 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfa..."},
            {"part_number": "C54920755", "product_name": "±100ppm/℃ 50V Thick Film Resistor 220kΩ 62.5mW ±5% 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909335 with 797,700 in stock at capture.",
        ]

    current = "electronic_resistor_0402_270000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF2703TCE"
        part["part_number_lcsc"] = "C25770"
        part["product_url"] = "https://www.lcsc.com/product-detail/C25770.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C25770", "product_name": "270kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2909341", "product_name": "270kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25550", "product_name": "270kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C25770 with 129,300 in stock at capture.",
        ]

    current = "electronic_resistor_0402_330000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F3303TS"
        part["part_number_lcsc"] = "C2909349"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909349.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909349", "product_name": "330kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C138006", "product_name": "50V 330kΩ Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C324777", "product_name": "330kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909349 with 426,200 in stock at capture.",
        ]

    current = "electronic_resistor_0402_390000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F3903TS"
        part["part_number_lcsc"] = "C2909352"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909352.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909352", "product_name": "390kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920788", "product_name": "390kΩ ±100ppm/℃ 50V Thick Film Resistor 62.5mW ±5% 0402 Chip Resistor - Surfa..."},
            {"part_number": "C54920667", "product_name": "390kΩ ±100ppm/℃ ±1% 50V Thick Film Resistor 62.5mW 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909352 with 530,400 in stock at capture.",
        ]

    current = "electronic_resistor_0402_470000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F4703TS"
        part["part_number_lcsc"] = "C2906871"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2906871.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2906871", "product_name": "470kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C25790", "product_name": "470kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906944", "product_name": "470kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2906871 with 457,700 in stock at capture.",
        ]

    current = "electronic_resistor_0402_560000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F5603TS"
        part["part_number_lcsc"] = "C2909369"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909369.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909369", "product_name": "560kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C1883578", "product_name": "560kΩ 62.5mW Thick Film Resistor 50V ±0.1% ±50ppm/℃ 0402 Chip Resistor - Surf..."},
            {"part_number": "C137958", "product_name": "62.5mW 560kΩ 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909369 with 35,600 in stock at capture.",
        ]

    current = "electronic_resistor_0402_680000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-07680KL"
        part["part_number_lcsc"] = "C163456"
        part["product_url"] = "https://www.lcsc.com/product-detail/C163456.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C163456", "product_name": "50V 680kΩ Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C2909377", "product_name": "680kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C144741", "product_name": "680kΩ 50V Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C163456 with 679,400 in stock at capture.",
        ]

    current = "electronic_resistor_0402_750000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F7503TS"
        part["part_number_lcsc"] = "C2909381"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909381.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909381", "product_name": "750kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920826", "product_name": "±100ppm/℃ 50V Thick Film Resistor 750kΩ 62.5mW ±5% 0402 Chip Resistor - Surfa..."},
            {"part_number": "C122545", "product_name": "750kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909381 with 102,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_820000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F8203TS"
        part["part_number_lcsc"] = "C2909386"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2909386.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2909386", "product_name": "820kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C67558", "product_name": "820kΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2906968", "product_name": "820kΩ ±5% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2909386 with 64,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_1000000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402J105 TS"
        part["part_number_lcsc"] = "C2906900"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2906900.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2906900", "product_name": "1MΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C138033", "product_name": "1MΩ 62.5mW 50V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surface..."},
            {"part_number": "C26083", "product_name": "1MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2906900 with 2,595,600 in stock at capture.",
        ]

    current = "electronic_resistor_0402_1200000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F1204TS"
        part["part_number_lcsc"] = "C2960795"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2960795.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2960795", "product_name": "1.2MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C43675", "product_name": "1.2MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C226867", "product_name": "1.2MΩ 50V Thick Film Resistor 62.5mW ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2960795 with 434,400 in stock at capture.",
        ]

    current = "electronic_resistor_0402_1500000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF1504TCE"
        part["part_number_lcsc"] = "C22276"
        part["product_url"] = "https://www.lcsc.com/product-detail/C22276.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C22276", "product_name": "1.5MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C138034", "product_name": "1.5MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C159956", "product_name": "1.5MΩ 100mW 75V ±1% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfac..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C22276 with 74,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_1800000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF1804TCE"
        part["part_number_lcsc"] = "C38587"
        part["product_url"] = "https://www.lcsc.com/product-detail/C38587.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C38587", "product_name": "1.8MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2933079", "product_name": "1.8MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2481599", "product_name": "1.8MΩ 62.5mW Thick Film Resistor 50V ±1% ±200ppm/℃ 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C38587 with 81,400 in stock at capture.",
        ]

    current = "electronic_resistor_0402_2200000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F2204TS"
        part["part_number_lcsc"] = "C2998080"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2998080.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2998080", "product_name": "2.2MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C11490", "product_name": "2.2MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C172168", "product_name": "62.5mW 2.2MΩ 50V ±5% ±100ppm/℃ Thick Film Resistor 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C2998080 with 392,800 in stock at capture.",
        ]

    current = "electronic_resistor_0402_2700000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF2704TCE"
        part["part_number_lcsc"] = "C270621"
        part["product_url"] = "https://www.lcsc.com/product-detail/C270621.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C54920773", "product_name": "2.7MΩ ±100ppm/℃ 50V 62.5mW Thick Film Resistor ±5% 0402 Chip Resistor - Surfa..."},
            {"part_number": "C270621", "product_name": "2.7MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C3013160", "product_name": "2.7MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C270621 with 14,200 in stock at capture.",
        ]

    current = "electronic_resistor_0402_3300000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402FR-073M3L"
        part["part_number_lcsc"] = "C470023"
        part["product_url"] = "https://www.lcsc.com/product-detail/C470023.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C470023", "product_name": "50V Thick Film Resistor 62.5mW 3.3MΩ ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C482174", "product_name": "50V 63mW 3.3MΩ Thick Film Resistor ±100ppm/℃ ±1% 0402 Chip Resistor - Surface..."},
            {"part_number": "C2998179", "product_name": "62.5mW 50V 3.3MΩ Thick Film Resistor ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C470023 with 80,700 in stock at capture.",
        ]

    current = "electronic_resistor_0402_3900000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F3904TS"
        part["part_number_lcsc"] = "C3013167"
        part["product_url"] = "https://www.lcsc.com/product-detail/C3013167.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C3013167", "product_name": "3.9MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920796", "product_name": "3.9MΩ ±100ppm/℃ 50V 62.5mW Thick Film Resistor ±5% 0402 Chip Resistor - Surfa..."},
            {"part_number": "C54531090", "product_name": "3.9MΩ 50V 62.5mW ±5% Thick Film Resistor ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C3013167 with 23,000 in stock at capture.",
        ]

    current = "electronic_resistor_0402_4700000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F4704TS"
        part["part_number_lcsc"] = "C3013173"
        part["product_url"] = "https://www.lcsc.com/product-detail/C3013173.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C3013173", "product_name": "4.7MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C482196", "product_name": "50V 62.5mW 4.7MΩ Thick Film Resistor ±100ppm/℃ ±1% 0402 Chip Resistor - Surfa..."},
            {"part_number": "C227116", "product_name": "50V Thick Film Resistor 62.5mW 4.7MΩ ±1% ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C3013173 with 228,300 in stock at capture.",
        ]

    current = "electronic_resistor_0402_5600000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "FOJAN"
        part["part_number_manufacturer"] = "FRC0402F5604TS"
        part["part_number_lcsc"] = "C3013178"
        part["product_url"] = "https://www.lcsc.com/product-detail/C3013178.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C3013178", "product_name": "5.6MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C2929925", "product_name": "5.6MΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54530929", "product_name": "5.6MΩ ±1% 50V 62.5mW Thick Film Resistor ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C3013178 with 35,400 in stock at capture.",
        ]

    current = "electronic_resistor_0402_6800000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "AC0402JR-076M8L"
        part["part_number_lcsc"] = "C227411"
        part["product_url"] = "https://www.lcsc.com/product-detail/C227411.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C49254148", "product_name": "6.8MΩ ±5% 62.5mW 50V Thick Film Resistor 0402 Chip Resistor - Surface Mount RoHS"},
            {"part_number": "C3017535", "product_name": "6.8MΩ ±5% 50V 62.5mW Thick Film Resistor ±200ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C2906463", "product_name": "6.8MΩ 50V 62.5mW Thick Film Resistor ±200ppm/℃ ±5% 0402 Chip Resistor - Surfa..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C227411 with 6,600 in stock at capture.",
        ]

    current = "electronic_resistor_0402_7500000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "YAGEO"
        part["part_number_manufacturer"] = "RC0402JR-077M5L"
        part["part_number_lcsc"] = "C137839"
        part["product_url"] = "https://www.lcsc.com/product-detail/C137839.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2933121", "product_name": "7.5MΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C137839", "product_name": "7.5MΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C131625", "product_name": "7.5MΩ 100mW 75V ±200ppm/℃ ±5% Thick Film Resistor 0402 Chip Resistor - Surfac..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C137839 with 8,800 in stock at capture.",
        ]

    current = "electronic_resistor_0402_8200000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "UNI-ROYAL"
        part["part_number_manufacturer"] = "0402WGF8204TCE"
        part["part_number_lcsc"] = "C423132"
        part["product_url"] = "https://www.lcsc.com/product-detail/C423132.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C2933123", "product_name": "8.2MΩ ±5% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54531134", "product_name": "8.2MΩ 50V 62.5mW ±5% Thick Film Resistor ±100ppm/℃ 0402 Chip Resistor - Surfa..."},
            {"part_number": "C423132", "product_name": "8.2MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C423132 with 9,100 in stock at capture.",
        ]

    current = "electronic_resistor_0402_10000000_ohm"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "HWA CHN"
        part["part_number_manufacturer"] = "HRC0402F1005DNTO"
        part["part_number_lcsc"] = "C54920615"
        part["product_url"] = "https://www.lcsc.com/product-detail/C54920615.html"
        part["part_numbers_lcsc"] = [
            {"part_number": "C54920615", "product_name": "10MΩ ±100ppm/℃ ±1% 50V 62.5mW Thick Film Resistor 0402 Chip Resistor - Surfac..."},
            {"part_number": "C2933065", "product_name": "10MΩ ±1% 62.5mW 0402 Thick Film Resistor"},
            {"part_number": "C54920718", "product_name": "10MΩ ±100ppm/℃ 50V 62.5mW Thick Film Resistor ±5% 0402 Chip Resistor - Surfac..."},
        ]
        part["research_notes"] = [
            "LCSC stock research 2026-09: highest-stock JLC-assembly listing (verified JLCPCB Part Class on the product page); best C54920615 with 512,000 in stock at capture.",
        ]
