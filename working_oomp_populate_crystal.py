def main(**kwargs):
    options = kwargs.get("options", [])

    # 3225 4-pin crystals
    packages = ["3225"]
    mounting_types = ["surface_mount"]
    pin_counts = ["4_pin"]
    frequencies = ["12_mhz", "16_mhz", "3_579545_mhz"]
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

    # C9002 has 80 ohm ESR. The generic 12 MHz / 20 pF choice currently
    # prefers a 50 ohm part, so keep this Basic SKU as an explicit variant.
    options.append({
        "taxonomy_2": "crystal",
        "taxonomy_3": "3225",
        "taxonomy_4": "surface_mount",
        "taxonomy_5": "4_pin",
        "taxonomy_6": "12_mhz",
        "taxonomy_7": "20_pf",
        "taxonomy_8": "80_ohm_esr",
    })

    # C9006 is a 25 MHz, 12 pF, 50 ohm 3225 crystal.  Keep its electrical
    # constraints explicit rather than allowing it to stand in for a different
    # load-capacitance or ESR oscillator.
    options.append({
        "taxonomy_2": "crystal",
        "taxonomy_3": "3225",
        "taxonomy_4": "surface_mount",
        "taxonomy_5": "4_pin",
        "taxonomy_6": "25_mhz",
        "taxonomy_7": "12_pf",
        "taxonomy_8": "50_ohm_esr",
    })

    # C12674 uses the much larger two-terminal HC-49S-SMD outline.  It is not
    # interchangeable with the existing 5032 8 MHz crystal despite sharing
    # frequency and load capacitance.
    options.append({
        "taxonomy_2": "crystal",
        "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount",
        "taxonomy_5": "2_pin",
        "taxonomy_6": "8_mhz",
        "taxonomy_7": "20_pf",
        "taxonomy_8": "70_ohm_esr",
    })

    # C13738 is a 16 MHz 3225 part, but its 9 pF load differs from the
    # existing 16 MHz / 20 pF definition.
    options.append({
        "taxonomy_2": "crystal",
        "taxonomy_3": "3225",
        "taxonomy_4": "surface_mount",
        "taxonomy_5": "4_pin",
        "taxonomy_6": "16_mhz",
        "taxonomy_7": "9_pf",
        "taxonomy_8": "50_ohm_esr",
    })

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

    # OSHCamp badge: 4-pad 2.0 x 1.6 mm ceramic crystal.
    options.append({
        "taxonomy_2": "crystal",
        "taxonomy_3": "2016",
        "taxonomy_4": "surface_mount",
        "taxonomy_5": "4_pin",
        "taxonomy_6": "26_mhz",
        "taxonomy_7": "20_pf",
        "taxonomy_14": "txc",
        "taxonomy_15": "nx3225gd",
    })

    # YXC HC-49S through-hole crystals (2-pin radial, 20 pF load), the first
    # through-hole HC-49S entries in the grid; ESR varies by frequency.
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "3_579545_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "160_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "3_6864_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "160_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "5_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "80_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "7_3728_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "70_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "10_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "60_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "11_0592_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "50_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "14_31818_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "50_ohm_esr",
    })

    # More YXC HC-49S through-hole crystals (2-pin radial, 20 pF load).
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "18_432_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "45_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "22_1184_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "45_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "24_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "35_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "24_576_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "35_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "27_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "35_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "30_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "35_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "4_9152_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "120_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "4_096_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "120_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "26_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "35_ohm_esr",
    })
    # C2228 page lists no ESR; keep the value/load pair explicit without an
    # ESR token rather than guessing.
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "19_0699_mhz", "taxonomy_7": "20_pf",
    })

    # YXC DT-26 through-hole tuning-fork watch crystal (2-pin, 12.5 pF).
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "dt_26",
        "taxonomy_4": "through_hole", "taxonomy_5": "2_pin",
        "taxonomy_6": "32_768_khz", "taxonomy_7": "12_5_pf",
        "taxonomy_8": "50000_ohm_esr",
    })

    # YXC HC-49S-SMD (surface-mount HC-49S, 2-pin, 20 pF load).
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "3_579545_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "160_ohm_esr",
    })

    # More YXC HC-49S-SMD crystals (2-pin, 20 pF load).
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "3_6864_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "160_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "5_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "80_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "7_3728_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "70_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "10_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "60_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "11_0592_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "50_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "13_56_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "50_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "18_432_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "45_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "22_1184_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "45_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "24_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "35_ohm_esr",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "hc_49s_smd",
        "taxonomy_4": "surface_mount", "taxonomy_5": "2_pin",
        "taxonomy_6": "24_576_mhz", "taxonomy_7": "20_pf",
        "taxonomy_8": "35_ohm_esr",
    })

    # YXC SMD5050-8P SAW resonator (C2275) and Murata SIP-3 ceramic
    # resonator (C2284) land here as well; the crystal family hosts
    # mechanical resonators generally.
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "smd_5050_8p",
        "taxonomy_4": "surface_mount", "taxonomy_5": "saw_resonator",
        "taxonomy_14": "made_in_china", "taxonomy_15": "ndr_420_315_8p",
    })
    options.append({
        "taxonomy_2": "crystal", "taxonomy_3": "sip_3_2_5mm",
        "taxonomy_4": "through_hole", "taxonomy_5": "ceramic_resonator",
        "taxonomy_6": "4_mhz", "taxonomy_7": "15_pf",
        "taxonomy_8": "30_ohm_esr",
        "taxonomy_14": "murata_electronics", "taxonomy_15": "cstls4m00g53_b0",
    })


if __name__ == "__main__":
    main()
