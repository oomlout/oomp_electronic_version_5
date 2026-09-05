def main(**kwargs):
    options = kwargs.get("options", [])

    # 3225 4-pin crystals
    packages = ["3225"]
    mounting_types = ["surface_mount"]
    pin_counts = ["4_pin"]
    frequencies = ["12_mhz", "16_mhz"]
    load_capacitances = ["20_pf"]

    for package in packages:
        for mounting_type in mounting_types:
            for pin_count in pin_counts:
                for frequency in frequencies:
                    for load_capacitance in load_capacitances:
                        option = {}
                        option["taxonomy_2"] = "crystal"
                        option["taxonomy_3"] = package
                        option["taxonomy_4"] = mounting_type
                        option["taxonomy_5"] = pin_count
                        option["taxonomy_6"] = frequency
                        option["taxonomy_7"] = load_capacitance
                        options.append(option)

    # 5032 2-pin crystals
    packages = ["5032"]
    mounting_types = ["surface_mount"]
    pin_counts = ["2_pin"]
    frequencies = ["8_mhz"]
    load_capacitances = ["20_pf"]

    for package in packages:
        for mounting_type in mounting_types:
            for pin_count in pin_counts:
                for frequency in frequencies:
                    for load_capacitance in load_capacitances:
                        option = {}
                        option["taxonomy_2"] = "crystal"
                        option["taxonomy_3"] = package
                        option["taxonomy_4"] = mounting_type
                        option["taxonomy_5"] = pin_count
                        option["taxonomy_6"] = frequency
                        option["taxonomy_7"] = load_capacitance
                        options.append(option)

    # 3215 2-pin watch crystals
    packages = ["3215"]
    mounting_types = ["surface_mount"]
    pin_counts = ["2_pin"]
    frequencies = ["32_768_khz"]
    load_capacitances = ["12_5_pf"]

    for package in packages:
        for mounting_type in mounting_types:
            for pin_count in pin_counts:
                for frequency in frequencies:
                    for load_capacitance in load_capacitances:
                        option = {}
                        option["taxonomy_2"] = "crystal"
                        option["taxonomy_3"] = package
                        option["taxonomy_4"] = mounting_type
                        option["taxonomy_5"] = pin_count
                        option["taxonomy_6"] = frequency
                        option["taxonomy_7"] = load_capacitance
                        options.append(option)


if __name__ == "__main__":
    main()
