def main(**kwargs):
    options = kwargs.get("options", [])

    # Keep transistor definitions in a plain array. Adding another generic or
    # exact device should only require copying and editing one dictionary.
    transistors = [
        {
            "taxonomy": ["transistor", "sot_363_6", "mosfet", "n_channel", "dual"],
            "manufacturer": "",
            "part_number": "",
            "name_short": "Dual N-channel MOSFET SOT-363 (generic)",
        },
        {
            "taxonomy": ["transistor", "sot_23", "bipolar", "npn"],
            "manufacturer": "",
            "part_number": "",
            "name_short": "NPN Transistor SOT-23 (generic)",
        },
        {
            # Soldered boards draw bare "PNP" symbols on SOT-23-3 footprints
            # (PIR movement sensor Q2); mirror the generic NPN entry.
            "taxonomy": ["transistor", "sot_23", "bipolar", "pnp"],
            "manufacturer": "",
            "part_number": "",
            "name_short": "PNP Transistor SOT-23 (generic)",
        },
        {
            # Soldered boards draw bare "NMOS" symbols on SOT-23-3 footprints
            # (PIR movement sensor Q1); a value-less generic keeps them matchable
            # until a fitted BOM names the exact part.
            "taxonomy": ["transistor", "sot_23", "mosfet", "n_channel", "enhancement_mode"],
            "manufacturer": "",
            "part_number": "",
            "name_short": "N-channel MOSFET SOT-23 (generic)",
        },
        {
            "taxonomy": ["transistor", "sot_23", "bipolar", "pnp", "40_volt", "600_milliamp"],
            "manufacturer": "onsemi",
            "part_number": "mmbt4403",
            "name_short": "PNP Transistor MMBT4403",
        },
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
            ],
            "manufacturer": "",
            "part_number": "2n7002",
            "name_short": "N-channel MOSFET 2N7002",
            "name_readable_override": "N-channel MOSFET 2N7002 SOT-23 (generic)",
        },
        {
            "taxonomy": [
                "transistor", "sot_23", "mosfet", "n_channel",
                "enhancement_mode", "60_volt", "300_milliamp",
            ],
            "manufacturer": "nexperia",
            "part_number": "2n7002_215",
            "name_short": "N-channel MOSFET 2N7002,215",
            "name_readable_override": "N-channel MOSFET 2N7002,215 SOT-23",
        },
        {
            "taxonomy": [
                "transistor", "sot_23", "mosfet", "n_channel",
                "enhancement_mode", "50_volt",
            ],
            "manufacturer": "",
            "part_number": "bss138",
            "name_short": "N-channel MOSFET BSS138",
            "name_readable_override": "N-channel MOSFET BSS138 SOT-23 (generic)",
        },
        {
            "taxonomy": [
                "transistor", "sot_23", "mosfet", "n_channel",
                "enhancement_mode", "50_volt", "220_milliamp",
            ],
            "manufacturer": "onsemi",
            "part_number": "bss138",
            "name_short": "N-channel MOSFET BSS138",
            "name_readable_override": "N-channel MOSFET BSS138 SOT-23",
        },
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
                "sot_23",
                "bipolar",
                "npn",
                "160_volt",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "mmbt5551_range_200_300",
            "name_short": "NPN Transistor MMBT5551 (200-300)",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "bipolar",
                "npn",
                "25_volt",
                "500_milliamp",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "s8050_j3y_range_200_350",
            "name_short": "NPN Transistor S8050 J3Y (200-350)",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "bipolar",
                "npn",
                "25_volt",
                "1_5_amp",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "ss8050_range_200_350",
            "name_short": "NPN Transistor SS8050 (200-350)",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "bipolar",
                "npn",
                "25_volt",
                "500_milliamp",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "s9013_j3_range_200_350",
            "name_short": "NPN Transistor S9013 J3 (200-350)",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "bipolar",
                "pnp",
                "150_volt",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "mmbt5401_range_200_300",
            "name_short": "PNP Transistor MMBT5401 (200-300)",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "bipolar",
                "npn",
                "40_volt",
                "600_milliamp",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "mmbt2222a_1p",
            "name_short": "NPN Transistor MMBT2222A 1P",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "bipolar",
                "pnp",
                "25_volt",
                "1_5_amp",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "ss8550_y2_range_200_350",
            "name_short": "PNP Transistor SS8550 Y2 (200-350)",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "bipolar",
                "pnp",
                "25_volt",
                "500_milliamp",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "s9012_2t1_range_200_350",
            "name_short": "PNP Transistor S9012 2T1 (200-350)",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_89_3",
                "bipolar",
                "npn",
                "30_volt",
                "3_amp",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "d882_range_160_320",
            "name_short": "NPN Transistor D882 (160-320)",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "bipolar",
                "npn",
                "40_volt",
                "200_milliamp",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "mmbt3904_range_100_300",
            "name_short": "NPN Transistor MMBT3904 (100-300)",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "bipolar",
                "pnp",
                "25_volt",
                "500_milliamp",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "s8550_range_120_200",
            "name_short": "PNP Transistor S8550 (120-200)",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "mosfet",
                "n_channel",
                "enhancement_mode",
                "60_volt",
            ],
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "2n7002",
            "name_short": "N-channel MOSFET 2N7002",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "mosfet",
                "p_channel",
                "enhancement_mode",
                "20_volt",
            ],
            "manufacturer": "vishay",
            "part_number": "si2301cds_t1_ge3",
            "name_short": "P-channel MOSFET SI2301CDS-T1-GE3",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "mosfet",
                "p_channel",
                "enhancement_mode",
                "30_volt",
            ],
            "manufacturer": "alpha_omega_semicon",
            "part_number": "ao3401a",
            "name_short": "P-channel MOSFET AO3401A",
        },
        {
            "taxonomy": [
                "transistor",
                "sot_23",
                "mosfet",
                "n_channel",
                "enhancement_mode",
                "30_volt",
            ],
            "manufacturer": "alpha_omega_semicon",
            "part_number": "ao3400a",
            "name_short": "N-channel MOSFET AO3400A",
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
        if "name_readable_override" in transistor:
            option["name_readable_override"] = transistor["name_readable_override"]
        options.append(option)


if __name__ == "__main__":
    main()
