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
        ["1206", 20],
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


if __name__ == "__main__":
    main()
