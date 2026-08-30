def main(**kwargs):
    options = kwargs.get("options", [])

    sizes = ["0402"]
    capacitance_values = [
        "22_pico_farad",
        "10_nano_farad",
        "22_nano_farad",
        "100_nano_farad",
        "1_micro_farad",
        "10_micro_farad",
    ]
    for size in sizes:
        for capacitance_value in capacitance_values:
            option = {}
            option["taxonomy_2"] = "capacitor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = capacitance_value
            options.append(option)

    sizes = ["0603"]
    capacitance_values = [
        "22_pico_farad",
        "10_nano_farad",
        "100_nano_farad",
        "1_micro_farad",
        "4_7_micro_farad",
        "10_micro_farad",
    ]
    for size in sizes:
        for capacitance_value in capacitance_values:
            option = {}
            option["taxonomy_2"] = "capacitor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = capacitance_value
            options.append(option)

    sizes = ["1206"]
    capacitance_values = ["47_micro_farad"]
    for size in sizes:
        for capacitance_value in capacitance_values:
            option = {}
            option["taxonomy_2"] = "capacitor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = capacitance_value
            options.append(option)

    sizes = ["3216_avx_a"]
    capacitor_styles = ["tantalum"]
    capacitance_values = ["4_7_micro_farad"]
    voltages = ["16_volt"]
    for size in sizes:
        for capacitor_style in capacitor_styles:
            for capacitance_value in capacitance_values:
                for voltage in voltages:
                    option = {}
                    option["taxonomy_2"] = "capacitor"
                    option["taxonomy_3"] = size
                    option["taxonomy_4"] = capacitor_style
                    option["taxonomy_5"] = capacitance_value
                    option["taxonomy_6"] = voltage
                    options.append(option)

    sizes = [
        "6_3_mm_diameter_5_4_mm_tall",
        "6_3_mm_diameter_7_7_mm_tall",
        "8_mm_diameter_6_5_mm_tall",
    ]
    capacitor_styles = ["electrolytic"]
    capacitance_values = ["220_micro_farad"]
    voltages = ["10_volt"]
    for size in sizes:
        for capacitor_style in capacitor_styles:
            for capacitance_value in capacitance_values:
                for voltage in voltages:
                    option = {}
                    option["taxonomy_2"] = "capacitor"
                    option["taxonomy_3"] = size
                    option["taxonomy_4"] = capacitor_style
                    option["taxonomy_5"] = capacitance_value
                    option["taxonomy_6"] = voltage
                    options.append(option)


if __name__ == "__main__":
    main()
