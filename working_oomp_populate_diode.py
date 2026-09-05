def main(**kwargs):
    options = kwargs.get("options", [])

    # Keep exact diode definitions as a plain array.  Diode families do not
    # share every package/manufacturer combination, so a cross-product of four
    # separate lists would create invalid parts that do not exist.
    diodes = [
        {"diode_type": "tvs_array", "package": "sot_143", "manufacturer": "littelfuse",
         "part_number": "sp0503bahtg", "name_short": "ESD Array SP0503BAHTG"},
        {
            "diode_type": "tvs_array",
            "package": "sot_23_6",
            "manufacturer": "protek",
            "part_number": "srv054pt7",
        },
        {
            "diode_type": "switching",
            "package": "sod_523f",
            "manufacturer": "onsemi",
            "part_number": "1n4148wt",
            "name_short": "Switching Diode 1N4148WT",
        },
        {
            "diode_type": "schottky_dual_common_cathode",
            "package": "sot_523",
            "manufacturer": "diodes_incorporated",
            "part_number": "bas40t_05",
            "name_short": "Dual Schottky Diode BAS40T-05",
        },
        {
            "diode_type": "schottky",
            "package": "sod_123",
            "manufacturer": "generic",
            "part_number": "ss14",
            "name_short": "Schottky Diode SOD-123",
        },
        {
            "diode_type": "schottky",
            "package": "sod_323",
            "manufacturer": "generic",
            "part_number": "bat54w",
            "name_short": "Schottky Diode SOD-323",
        },
        {
            "diode_type": "schottky",
            "package": "0402",
            "manufacturer": "generic",
            "part_number": "1ss400",
            "name_short": "Schottky Diode 0402",
        },
    ]

    for diode in diodes:
        option = {}
        option["taxonomy_2"] = "diode"
        option["taxonomy_3"] = diode["diode_type"]
        option["taxonomy_4"] = diode["package"]
        option["taxonomy_14"] = diode["manufacturer"]
        option["taxonomy_15"] = diode["part_number"]
        if "name_short" in diode:
            option["name_short"] = diode["name_short"]
        options.append(option)


if __name__ == "__main__":
    main()
