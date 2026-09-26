def main(**kwargs):
    options = kwargs.get("options", [])

    sizes = ["0402"]
    capacitance_values = [
        "8_pico_farad",
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

    # The Basic 0402 1 nF house part C1523 fills this missing generic value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "1_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "220_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "4_7_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "100_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "12_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "20_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "47_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "220_nano_farad",
    })
    # JLC Basic C32949 supplies this previously absent 0402 value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "10_pico_farad",
    })

    # C23733 is +/-20%; retain the existing generic 0402 4.7 uF purchase
    # choice at +/-10% and add this explicit rated/tolerance variant.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "4_7_micro_farad",
        "taxonomy_5": "10_volt",
        "taxonomy_6": "20_percent",
    })

    # Keep the existing 16 V 100 nF generic preference and represent the
    # JLC Basic 50 V choice as a rated purchasing variant.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "100_nano_farad",
        "taxonomy_5": "50_volt",
    })

    sizes = ["0603"]
    capacitance_values = [
        "10_pico_farad",
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

    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "1_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "150_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "220_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "3_3_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "47_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "470_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "6_8_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "15_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "20_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "30_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "330_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "100_pico_farad",
    })
    # Missing generic values supplied by Basic C21117, C21120 and C21122.
    for value in ("33_nano_farad", "220_nano_farad", "22_nano_farad"):
        options.append({
            "taxonomy_2": "capacitor",
            "taxonomy_3": "0603",
            "taxonomy_4": value,
        })
    # Basic C53987 and C1322360 fill these 0603 values.
    for value in ("4_7_nano_farad", "8_2_nano_farad"):
        options.append({
            "taxonomy_2": "capacitor",
            "taxonomy_3": "0603",
            "taxonomy_4": value,
        })
    # JLC Basic C38523 supplies this previously absent 0603 value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "12_pico_farad",
    })

    # C19666 is a 16 V Basic choice. Keep the existing generic 0603 4.7 uF
    # purchase preference at 25 V and represent this lower-rated SKU explicitly.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "4_7_micro_farad",
        "taxonomy_5": "16_volt",
    })

    # C96446 is rated 25 V but has +/-20% tolerance. Keep the generic
    # 0603 10 uF preference at +/-10% and expose this SKU explicitly.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "10_micro_farad",
        "taxonomy_5": "25_volt",
        "taxonomy_6": "20_percent",
    })

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

    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "10_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "22_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "33_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "470_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "4_7_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "100_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "20_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "22_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "220_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "470_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "47_pico_farad",
    })
    # New compatible generic values supplied by Basic C28233, C28260,
    # C28323 and C46653.
    for value in ("100_nano_farad", "2_2_nano_farad", "1_micro_farad", "1_nano_farad"):
        options.append({
            "taxonomy_2": "capacitor",
            "taxonomy_3": "0805",
            "taxonomy_4": value,
        })
    # Basic C53134, C107145 and C377773 fill these 0805 values.
    for value in ("47_nano_farad", "220_pico_farad", "2_2_micro_farad"):
        options.append({
            "taxonomy_2": "capacitor",
            "taxonomy_3": "0805",
            "taxonomy_4": value,
        })
    # Keep the 100 V C28233 generic preference; C49678 is the 50 V variant.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "100_nano_farad",
        "taxonomy_5": "50_volt",
    })

    # C440198 is a 50 V Basic option alongside the generic 25 V preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "10_micro_farad",
        "taxonomy_5": "50_volt",
    })

    sizes = ["1206"]
    capacitance_values = ["10_micro_farad", "47_micro_farad"]
    for size in sizes:
        for capacitance_value in capacitance_values:
            option = {}
            option["taxonomy_2"] = "capacitor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = capacitance_value
            options.append(option)

    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "10_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_micro_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_nano_farad",
        "taxonomy_5": "2000_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "22_micro_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "100_nano_farad",
    })
    # Basic C29823 supplies the new 1206 4.7 uF generic value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "4_7_micro_farad",
    })
    # Basic C50254 supplies the previously absent 1206 2.2 uF generic value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "2_2_micro_farad",
    })
    # The 100 uF 1206 house SKU is only 6.3 V and +/-20%; keep both ratings
    # explicit rather than assigning it to an unrated generic value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "100_micro_farad",
        "taxonomy_5": "6_3_volt",
        "taxonomy_6": "20_percent",
    })

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
