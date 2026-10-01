def main(**kwargs):
    options = kwargs.get("options", [])

    sizes = [
        "0201",
        "0402",
        "0603",
        "0805",
        "1206",
        "quarter_watt_through_hole",
    ]

    # E12 values used by the old OOMP component set.
    base_values = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 75, 82]
    multipliers = [1, 10, 100, 1000, 10000, 100000]

    resistance_values = [0]
    for multiplier in multipliers:
        for base_value in base_values:
            resistance_values.append(base_value * multiplier)
    resistance_values.append(10000000)

    # Additional project values can be added directly to this simple list.
    additional_resistance_values = [200, 300, 510, 1600, 2400, 5100, 20000, 53600, 102000, 133000, 200000, 510000]
    for additional_resistance_value in additional_resistance_values:
        resistance_values.append(additional_resistance_value)

    for size in sizes:
        for resistance_value in resistance_values:
            option = {}
            option["taxonomy_2"] = "resistor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = f"{resistance_value}_ohm"

            options.append(option)

    # Project-specific 2512 resistors (the Bus Pirate current shunt, the GNSS
    # DAN F10N 13.3 ohm termination).  Keep this separate from the broad value
    # grid so we do not create hundreds of unlikely 2512 variants.
    low_value_resistors = [
        ["2512", "0_2_ohm"],
        ["2512", "13_3_ohm"],
        ["2512", "0_015_ohm"],
        ["1210", "0_1_ohm"],
        ["0805", "1_8_ohm"],
        ["0805", "3_9_ohm"],
        ["0805", "2_2_ohm"],
        ["0805", "4_7_ohm"],
        ["0805", "5_1_ohm"],
        ["1206", "1_ohm"],
        # C1419 supplies the missing 1206 3.9 ohm generic value (RALEC
        # RTT063R9JTP, the first reviewed 1206 3.9 ohm house part).
        ["1206", "3_9_ohm"],
        # C1424 supplies the missing 1206 8.2 ohm generic value (FH
        # RS-06L8R2JT, the first reviewed 1206 8.2 ohm house part).
        ["1206", "8_2_ohm"],
        # C2884 supplies the missing 1206 6.8 ohm generic value (UNI-ROYAL
        # 1206W4J068JT5E, the first reviewed 1206 6.8 ohm house part).
        ["1206", "6_8_ohm"],
        # C3109 supplies the missing 0805 1.6 megaohm generic value (RALEC
        # RTT051604FTP, the first reviewed 0805 1.6M ohm house part; 16 is
        # not in this project's E12 base list).
        ["0805", "1600000_ohm"],
        # C4125 supplies the missing 0402 499 ohm generic value (UNI-ROYAL
        # 0402WGF4990TCE, the first reviewed 0402 499 ohm house part; 499 is
        # an E96 value outside the E12 grid).
        ["0402", "499_ohm"],
        # C4144 supplies the missing 0402 8.2 ohm generic value (RALEC
        # RTT028R20FTH, the first reviewed 0402 8.2 ohm house part).
        ["0402", "8_2_ohm"],
        # C4148 supplies the missing 0402 9.1 ohm generic value (RALEC
        # RTT029R10FTH; 91 is an E96 value outside the E12 grid).
        ["0402", "9_1_ohm"],
        # C5301 supplies the missing 0805 78.7k ohm generic value (RALEC
        # RTT057872FTP; 78.7 is an E96 value outside the E12 grid).
        ["0805", "78700_ohm"],
        # C4376/C4403/C4407 supply the missing 0805 4.99/8.2/91 ohm values
        # (4.99 and 91 are E96 values outside the E12 grid; the earlier 8.2
        # row was 0402/1206 only).
        ["0805", "4_99_ohm"],
        ["0805", "8_2_ohm"],
        ["0805", "91_ohm"],
        # C4417/C4428/C4429/C4436/C4437/C4454/C4463 supply the missing 1206
        # 11k/140/1.4k/16k/160k/21.5k/24k values (11, 14, 16, 21.5 and 24
        # are not in this project's E12 base list).
        ["1206", "11000_ohm"],
        ["1206", "140_ohm"],
        ["1206", "1400_ohm"],
        ["1206", "16000_ohm"],
        ["1206", "160000_ohm"],
        ["1206", "21500_ohm"],
        ["1206", "24000_ohm"],
        # C4516/C4538 supply the missing 1206 5.6 and 910 ohm values (5.6
        # is E96-below-grid; 91 is not in the base list).
        ["1206", "5_6_ohm"],
        ["1206", "910_ohm"],
        # C4906/C4940/C4961/C4962/C5099/C5101 supply the missing 0402
        # 1.3k/3.4k/620/62/24.9/442k values.
        ["0402", "1300_ohm"],
        ["0402", "3400_ohm"],
        ["0402", "620_ohm"],
        ["0402", "62_ohm"],
        ["0402", "24_9_ohm"],
        ["0402", "442000_ohm"],
        # C4197/C4198 supply the missing 0603 240k and 24 ohm generic values
        # (24 is not in this project's E12 base list).
        ["0603", "240000_ohm"],
        ["0603", "24_ohm"],
        # C4210/C4257 supply the missing 0603 16k and 59 ohm generic values
        # (16 and 59 are not in this project's E12 base list).
        ["0603", "16000_ohm"],
        ["0603", "59_ohm"],
        # C4360/C4368 supply the missing 0805 36k and 43 ohm generic values
        # (36 is not in the base list; the earlier 43 ohm row was 1206 only).
        ["0805", "36000_ohm"],
        ["0805", "43_ohm"],
        # C1426 supplies the missing 1206 11 ohm generic value (FH
        # RS-06K110JT); 11 ohm is not in this project's E12 base list.
        ["1206", "11_ohm"],
        # C1440 supplies the missing 1206 43 ohm generic value (FH
        # RS-06K430JT); 43 ohm is not in this project's E12 base list.
        ["1206", "43_ohm"],
        # C1448 supplies the missing 1206 91 ohm generic value (FH
        # RS-06K910JT); 91 ohm is not in this project's E12 base list.
        ["1206", "91_ohm"],
        ["0603", "1_ohm"],
        ["0603", "2_2_ohm"],
        ["0603", "2_ohm"],
        ["0603", "4_7_ohm"],
        ["0603", "5_1_ohm"],
        ["0805", "1_ohm"],
        ["1206", "0_1_ohm"],
    ]
    for low_value_resistor in low_value_resistors:
        option = {}
        option["taxonomy_2"] = "resistor"
        option["taxonomy_3"] = low_value_resistor[0]
        option["taxonomy_4"] = low_value_resistor[1]
        options.append(option)

    # Exact second-source rows for generics whose preferred JLC code is
    # already taken by an earlier research wave (C1161/C1186/C25271): the
    # new queue part gets its own maker-stamped identity.
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "0402", "taxonomy_4": "91000_ohm",
        "taxonomy_14": "uni_royal_uniroyal_elec", "taxonomy_15": "0402wgf9102tce",
        "name_short": "91k ohm 0402 Resistor (UNI-ROYAL 0402WGF9102TCE)",
    })
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "0603", "taxonomy_4": "2_7_ohm",
        "taxonomy_14": "ralec", "taxonomy_15": "rtt032r70ftp",
        "name_short": "2.7 ohm 0603 Resistor (RALEC RTT032R70FTP)",
    })
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "0805", "taxonomy_4": "1_ohm",
        "taxonomy_14": "uni_royal_uniroyal_elec", "taxonomy_15": "rtt051r00ftp",
        "name_short": "1 ohm 0805 Resistor (RALEC RTT051R00FTP)",
    })
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "1206", "taxonomy_4": "11_ohm",
        "taxonomy_14": "ralec", "taxonomy_15": "rtt0611r0ftp",
        "name_short": "11 ohm 1206 Resistor (RALEC RTT0611R0FTP)",
    })
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "1206", "taxonomy_4": "1300_ohm",
        "taxonomy_14": "ralec", "taxonomy_15": "rtt061301ftp",
        "name_short": "1.3k ohm 1206 Resistor (RALEC RTT061301FTP)",
    })
    # C4466/C4502/C4513/C4521/C4535: exact second-source rows for 1206
    # generics whose parts_source pages pre-date the queue (earlier research
    # waves), so scaffold cannot reuse the shared page.
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "1206", "taxonomy_4": "270_ohm",
        "taxonomy_14": "uni_royal_uniroyal_elec", "taxonomy_15": "1206w4f2700t5e",
        "name_short": "270 ohm 1206 Resistor (UNI-ROYAL 1206W4F2700T5E)",
    })
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "1206", "taxonomy_4": "470_ohm",
        "taxonomy_14": "uni_royal_uniroyal_elec", "taxonomy_15": "1206w4f4700t5e",
        "name_short": "470 ohm 1206 Resistor (UNI-ROYAL 1206W4F4700T5E)",
    })
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "1206", "taxonomy_4": "56000_ohm",
        "taxonomy_14": "ralec", "taxonomy_15": "rtt065602ftp",
        "name_short": "56k ohm 1206 Resistor (RALEC RTT065602FTP)",
    })
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "1206", "taxonomy_4": "680_ohm",
        "taxonomy_14": "ralec", "taxonomy_15": "rtt066800ftp",
        "name_short": "680 ohm 1206 Resistor (RALEC RTT066800FTP)",
    })
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "1206", "taxonomy_4": "820000_ohm",
        "taxonomy_14": "ralec", "taxonomy_15": "rtt068203ftp",
        "name_short": "820k ohm 1206 Resistor (RALEC RTT068203FTP)",
    })
    # C4908: the 0402 1.6k generic's parts_source page pre-dates the queue,
    # so the new UNI-ROYAL part gets its own maker-stamped exact row.
    options.append({
        "taxonomy_2": "resistor", "taxonomy_3": "0402", "taxonomy_4": "1600_ohm",
        "taxonomy_14": "uni_royal_uniroyal_elec", "taxonomy_15": "0402wgf1601tce",
        "name_short": "1.6k ohm 0402 Resistor (UNI-ROYAL 0402WGF1601TCE)",
    })

    # Board values outside the E12 grid: the Soldered 0603 pull-ups and the
    # SparkFun USB current-limiting resistors.
    extra_values = [
        # C1186 supplies the missing 0603 2.7 ohm generic value.
        ["0603", 2.7],
        ["0603", 5.6],
        ["0603", 30],
        ["0402", 2000],
        ["0603", 3000],
        ["0603", 6200],
        ["0805", 20],
        ["0805", 24000],
        ["0805", 2000],
        ["0805", 30000],
        ["0805", 3000],
        # C1365 adds a separate 0805 3.6 kOhm value; C22980 is 0603.
        ["0805", 3600],
        ["0805", 49.9],
        ["0805", 51000],
        ["0805", 51],
        ["1206", 2000],
        # C1453 supplies the missing 1206 160 ohm generic value (FH
        # RS-06K161JT); 160 ohm is not in this project's E12 base list.
        ["1206", 160],
        ["1206", 20],
        # C1480 supplies the missing 1206 3.6 kOhm value (FH RS-06K362JT);
        # 36 ohm is not in this project's E12 base list, so before this row
        # only the 0805 (C1365) and 0603 (C22980) 3600 ohm values existed.
        ["1206", 3600],
        ["0603", 13000],
        ["0603", 20],
        ["0603", 2000],
        ["0603", 2000000],
        ["0603", 3600],
        ["0603", 30000],
        ["0603", 300000],
        ["0603", 4990],
        ["0603", 49900],
        ["0603", 49.9],
        ["0603", 51000],
        ["0603", 51],
        ["0603", 9100],
        ["0603", 24000],
        ["0402", 36],
        ["0402", 24000],
        ["0402", 49.9],
        ["0402", 51000],
    ]
    for size, resistance_value in extra_values:
        # Integer values must stay exact; :g alone would render 2000000 as 2e+06.
        value_token = f"{resistance_value:d}" if isinstance(resistance_value, int) else f"{resistance_value:g}".replace(".", "_")
        option = {
            "taxonomy_2": "resistor",
            "taxonomy_3": size,
            "taxonomy_4": f"{value_token}_ohm",
        }
        options.append(option)

    # C1335 is the first reviewed 0805 110 ohm value; it is outside the E12 grid.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0805",
        "taxonomy_4": "110_ohm",
    })

    # C1450 is the first reviewed 1206 110 ohm value; it is outside the E12 grid.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "1206",
        "taxonomy_4": "110_ohm",
    })

    # C1471 is the first reviewed 1206 1.3 kOhm value; 1300 ohm is not in the
    # E12 grid or the extra-value list.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1300_ohm",
    })

    # C1339 is ±5%; preserve the existing ±1% 0805 180 ohm generic choice.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0805",
        "taxonomy_4": "180_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1358 is ±5%; preserve the existing ±1% 0805 1.8 kΩ generic choice.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1800_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1359 is ±5%; keep the existing ±1% 0805 2 kΩ generic choice intact.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0805",
        "taxonomy_4": "2000_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1382 is the ±5% option; keep the existing Basic ±1% 24 kΩ choice.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0805",
        "taxonomy_4": "24000_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1160 is 5%; keep the existing generic 0402 82 kOhm 1% choice and
    # represent this looser-tolerance purchasing option as a separate variant.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0402",
        "taxonomy_4": "82000_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1161 is the first reviewed 0402 91 kOhm value; it is not in the
    # project's standard E12 value set, so keep one explicit generic row.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0402",
        "taxonomy_4": "91000_ohm",
    })

    # C1166 is 5%; keep the existing YAGEO 150 kOhm ±1% generic choice intact.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0402",
        "taxonomy_4": "150000_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1203 is a 5% version of the existing 0603 22 ohm generic resistor.
    # Keep the tighter-tolerance generic choice and represent this rating as a variant.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0603",
        "taxonomy_4": "22_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1211 is the ±5% UNI-ROYAL version of the existing 0603 47 ohm generic.
    # Preserve its reviewed ±1% generic preference as a separate tolerance variant.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0603",
        "taxonomy_4": "47_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1226 is the ±5% UNI-ROYAL version of the existing 0603 220 ohm generic.
    # Preserve its reviewed ±1% generic preference as a separate tolerance variant.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0603",
        "taxonomy_4": "220_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1275 is the ±5% UNI-ROYAL version of the existing 0603 82 kΩ generic.
    # Preserve its reviewed ±1% generic preference as a separate tolerance variant.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "0603",
        "taxonomy_4": "82000_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1409 is the ±5% UNI-ROYAL version of the existing 1206 1 ohm generic.
    # Preserve its reviewed ±1% Basic preference as a separate tolerance variant.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1469 is the ±5% UNI-ROYAL version of the existing 1206 1 kohm generic.
    # Preserve its reviewed ±1% Basic preference (C4410) as a tolerance variant.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1000_ohm",
        "taxonomy_5": "5_percent",
    })

    # C1489 is the ±5% UNI-ROYAL version of the existing 1206 10 kohm generic.
    # Preserve its reviewed ±1% Basic preference (C17902) as a tolerance variant.
    options.append({
        "taxonomy_2": "resistor",
        "taxonomy_3": "1206",
        "taxonomy_4": "10000_ohm",
        "taxonomy_5": "5_percent",
    })


if __name__ == "__main__":
    main()
