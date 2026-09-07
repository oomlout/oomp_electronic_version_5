def main(**kwargs):
    options = kwargs.get("options", [])

    sizes = ["0402"]
    capacitance_values = [
        "15_pico_farad",
        "18_pico_farad",
        "22_pico_farad",
        "27_pico_farad",
        "33_pico_farad",
        "120_pico_farad",
        "10_nano_farad",
        "22_nano_farad",
        "100_nano_farad",
        "1_micro_farad",
        "2_2_micro_farad",
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

    sizes = ["0603"]
    capacitance_values = [
        "18_pico_farad",
        "22_pico_farad",
        "27_pico_farad",
        "33_pico_farad",
        "47_pico_farad",
        "470_pico_farad",
        "2_2_nano_farad",
        "10_nano_farad",
        "100_nano_farad",
        "1_micro_farad",
        "2_2_micro_farad",
        "4_7_micro_farad",
        "10_micro_farad",
        "22_micro_farad",
    ]
    for size in sizes:
        for capacitance_value in capacitance_values:
            option = {}
            option["taxonomy_2"] = "capacitor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = capacitance_value
            options.append(option)

    sizes = ["0805"]
    capacitance_values = [
        "4_7_micro_farad",
        "10_micro_farad",
        "22_micro_farad",
        "47_micro_farad",
    ]
    for size in sizes:
        for capacitance_value in capacitance_values:
            option = {}
            option["taxonomy_2"] = "capacitor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = capacitance_value
            options.append(option)

    sizes = ["1206"]
    capacitance_values = ["10_micro_farad", "47_micro_farad"]
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

    # Easyduino ESP32: keep the value/voltage pair explicit, not a cross-product.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "3216_avx_a",
        "taxonomy_4": "tantalum",
        "taxonomy_5": "22_micro_farad",
        "taxonomy_6": "10_volt",
    })

    # Soldered 1210C_tantal 68uF and the 8 mm radial electrolytic (the fitted
    # MPN's "681" code is 68x10 = 680 uF at 16 V).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1210",
        "taxonomy_4": "68_micro_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_14_5_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "680_micro_farad",
        "taxonomy_6": "16_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "2200_pico_farad",
    })


if __name__ == "__main__":
    main()
