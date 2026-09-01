def main(**kwargs):
    options = kwargs.get("options", [])

    packages = ["4_x_0402_convex"]
    resistance_values = [330, 510, 10000, 100000, 1000000]
    for package in packages:
        for resistance_value in resistance_values:
            option = {}
            option["taxonomy_2"] = "resistor_array"
            option["taxonomy_3"] = package
            option["taxonomy_4"] = f"{resistance_value}_ohm"
            option["taxonomy_5"] = "8_pin"
            options.append(option)


if __name__ == "__main__":
    main()
