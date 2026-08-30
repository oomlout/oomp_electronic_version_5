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
    additional_resistance_values = [5100, 510000]
    for additional_resistance_value in additional_resistance_values:
        resistance_values.append(additional_resistance_value)

    for size in sizes:
        for resistance_value in resistance_values:
            option = {}
            option["taxonomy_2"] = "resistor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = f"{resistance_value}_ohm"

            options.append(option)


if __name__ == "__main__":
    main()
