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
