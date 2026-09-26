def main(**kwargs):
    options = kwargs.get("options", [])

    packages = ["4_x_0402_convex", "4_x_0603_convex"]
    resistance_values = [330, 510, 10000, 100000, 1000000]
    for package in packages:
        for resistance_value in resistance_values:
            option = {}
            option["taxonomy_2"] = "resistor_array"
            option["taxonomy_3"] = package
            option["taxonomy_4"] = f"{resistance_value}_ohm"
            option["taxonomy_5"] = "8_pin"
            options.append(option)

    # JLC house-part array: UNI-ROYAL 4D03 convex 0603x4 network, 4.7 kohm.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "4700_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # JLC house-part array: UNI-ROYAL 4D03 convex 0603x4 network, 1 kohm.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "1000_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)


if __name__ == "__main__":
    main()
