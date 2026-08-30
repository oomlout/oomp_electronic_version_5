def main(**kwargs):
    options = kwargs.get("options", [])

    packages = ["0805"]
    impedances = ["220_ohm"]
    current_ratings = ["2_amp"]
    manufacturers = ["murata"]
    part_numbers = ["blm21pg221sn1d"]

    for package in packages:
        for impedance in impedances:
            for current_rating in current_ratings:
                for manufacturer in manufacturers:
                    for part_number in part_numbers:
                        option = {}
                        option["taxonomy_2"] = "ferrite_bead"
                        option["taxonomy_3"] = package
                        option["taxonomy_4"] = impedance
                        option["taxonomy_5"] = current_rating
                        option["taxonomy_14"] = manufacturer
                        option["taxonomy_15"] = part_number
                        options.append(option)


if __name__ == "__main__":
    main()
