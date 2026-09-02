def main(**kwargs):
    options = kwargs.get("options", [])

    # Keep exact stocked parts in one editable array.  A cross-product would
    # invent manufacturer/package/value combinations that do not exist.
    ferrite_beads = [
        {
            "package": "0805",
            "impedance": "220_ohm",
            "current_rating": "2_amp",
            "manufacturer": "murata",
            "part_number": "blm21pg221sn1d",
        },
        {
            "package": "0805",
            "impedance": "15_ohm",
            "current_rating": "1_5_amp",
            "manufacturer": "tdk",
            "part_number": "mmz2012r150at000",
            "name_short": "Ferrite Bead 15 Ohm 1.5 A",
        },
    ]

    for ferrite_bead in ferrite_beads:
        option = {}
        option["taxonomy_2"] = "ferrite_bead"
        option["taxonomy_3"] = ferrite_bead["package"]
        option["taxonomy_4"] = ferrite_bead["impedance"]
        option["taxonomy_5"] = ferrite_bead["current_rating"]
        option["taxonomy_14"] = ferrite_bead["manufacturer"]
        option["taxonomy_15"] = ferrite_bead["part_number"]
        if "name_short" in ferrite_bead:
            option["name_short"] = ferrite_bead["name_short"]
        options.append(option)


if __name__ == "__main__":
    main()
