def main(**kwargs):
    options = kwargs.get("options", [])

    diode_types = ["tvs_array"]
    packages = ["sot_23_6"]
    manufacturers = ["protek"]
    part_numbers = ["srv054pt7"]

    for diode_type in diode_types:
        for package in packages:
            for manufacturer in manufacturers:
                for part_number in part_numbers:
                    option = {}
                    option["taxonomy_2"] = "diode"
                    option["taxonomy_3"] = diode_type
                    option["taxonomy_4"] = package
                    option["taxonomy_14"] = manufacturer
                    option["taxonomy_15"] = part_number
                    options.append(option)


if __name__ == "__main__":
    main()
