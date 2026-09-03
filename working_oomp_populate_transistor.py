def main(**kwargs):
    options = kwargs.get("options", [])

    # Keep exact transistor definitions in a plain array.  Adding another
    # fitted device should only require copying and editing one dictionary.
    transistors = [
        {"taxonomy": ["transistor", "sot_23", "bipolar", "npn", "25_volt", "1_5_amp"],
         "manufacturer": "jsmsemi", "part_number": "ss8050", "name_short": "NPN Transistor SS8050"},
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "mosfet",
                "n_channel",
                "enhancement_mode",
                "60_volt",
                "300_milliamp",
            ],
            "manufacturer": "cbi",
            "part_number": "mmbt7002k",
            "name_short": "N-channel MOSFET MMBT7002K",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_523",
                "mosfet",
                "p_channel",
                "enhancement_mode",
                "20_volt",
                "2_8_amp",
            ],
            "manufacturer": "cbi",
            "part_number": "bc2301t_2_8a",
            "name_short": "P-channel MOSFET BC2301T-2.8A",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_363_6",
                "bipolar",
                "pnp",
                "dual_matched_pair",
                "45_volt",
                "100_milliamp",
            ],
            "manufacturer": "diodes_incorporated",
            "part_number": "bcm857bs_7_f",
            "name_short": "Dual matched PNP BCM857BS-7-F",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_363_6",
                "bipolar",
                "pnp",
                "dual_general_purpose",
                "40_volt",
                "200_milliamp",
            ],
            "manufacturer": "cbi",
            "part_number": "mmdt3906dw",
            "name_short": "Dual PNP MMDT3906DW",
        },
    ]

    for transistor in transistors:
        option = {}
        taxonomy = transistor["taxonomy"]
        for taxonomy_index in range(len(taxonomy)):
            option[f"taxonomy_{taxonomy_index + 2}"] = taxonomy[taxonomy_index]
        option["taxonomy_14"] = transistor["manufacturer"]
        option["taxonomy_15"] = transistor["part_number"]
        option["name_short"] = transistor["name_short"]
        options.append(option)


if __name__ == "__main__":
    main()
