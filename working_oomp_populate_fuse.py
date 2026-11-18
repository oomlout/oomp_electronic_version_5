def main(**kwargs):
    options = kwargs.get("options", [])

    fuses = [
        {"size": "0402", "fuse_type": "resettable"},
        {"size": "0805", "fuse_type": "resettable"},
        {"size": "1206", "fuse_type": "resettable"},
        {"size": "1210", "fuse_type": "resettable"},
        {"size": "0805", "fuse_type": "resettable_6_volt_0_5_amp_1_amp"},
        {"size": "1210", "fuse_type": "resettable_6_volt_2_amp_4_amp"},
    ]

    for fuse in fuses:
        option = {}
        option["taxonomy_2"] = "fuse"
        option["taxonomy_3"] = fuse["size"]
        option["taxonomy_4"] = fuse["fuse_type"]
        options.append(option)

    # Tiny Reflow Controller uses the Bourns MF-FSMF low-profile PTC family.
    # The source project does not specify the electrical suffix, so keep the
    # series identity and 0603 package without inventing a hold current.
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "0603", "taxonomy_4": "resettable",
        "taxonomy_14": "bourns", "taxonomy_15": "mf_fsmf",
        "name_short": "Bourns MF-FSMF 0603 Resettable Fuse",
    })

    # Disposable and resettable fuses from the JLC house-parts queue.  Size
    # tokens follow the page labels; plugin bodies name their glass/square
    # outlines explicitly.
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "5_mm_square_plugin", "taxonomy_4": "disposable",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "5te_10002r1bt",
        "name_short": "Square Fuse 5TE.10002R1BT (5 mm, 1A 250V)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "2410", "taxonomy_4": "disposable",
        "taxonomy_14": "littelfuse", "taxonomy_15": "0451001_mrl",
        "name_short": "Surface Mount Fuse 0451001.MRL (2410, 1A 125V)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "3_6_x_10_mm_glass_plugin", "taxonomy_4": "disposable",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "3f_1000212000r1n",
        "name_short": "Glass Tube Fuse 3F.1000212000R1N (3.6x10 mm, 1A)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "1812", "taxonomy_4": "resettable",
        "taxonomy_14": "pttc_polytronics_tech", "taxonomy_15": "smd1812p110tf",
        "name_short": "Resettable Fuse SMD1812P110TF (1812, 1.1A hold)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "1206", "taxonomy_4": "disposable",
        "taxonomy_14": "littelfuse", "taxonomy_15": "0466002_nrhf",
        "name_short": "Surface Mount Fuse 0466002.NRHF (1206, 2A 63V)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "1812", "taxonomy_4": "resettable",
        "taxonomy_14": "littelfuse", "taxonomy_15": "rf1404_000",
        "name_short": "Resettable Fuse RF1404-000 (1812, 750mA hold)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "2_8_x_7_1_mm_glass_plugin", "taxonomy_4": "disposable",
        "taxonomy_14": "littelfuse", "taxonomy_15": "0251_500nrt1l",
        "name_short": "Glass Tube Fuse 0251.500NRT1L (2.8x7.1 mm, 500mA 125V)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "5_2_x_20_mm_glass_plugin", "taxonomy_4": "disposable",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "5f_2000210000r1",
        "name_short": "Glass Tube Fuse 5F.2000210000R1 (5.2x20 mm, 2A 250V)",
    })

    # More 5.2x20 mm glass fuses from the JLC house-parts queue.
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "5_2_x_20_mm_glass_plugin", "taxonomy_4": "disposable",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "5g_3000210000s1",
        "name_short": "Glass Tube Fuse 5G.3000210000S1 (5.2x20 mm, 3A 250V)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "5_2_x_20_mm_glass_plugin", "taxonomy_4": "disposable",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "7a_250vacglass_tube_fuse",
        "name_short": "Glass Tube Fuse 7A 250VAC (5.2x20 mm)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "5_2_x_20_mm_glass_plugin", "taxonomy_4": "disposable",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "5f_0010220000r1",
        "name_short": "Glass Tube Fuse 5F.0010220000R1 (5.2x20 mm, 10A 250V)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "5_2_x_20_mm_glass_plugin", "taxonomy_4": "disposable",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "5f_0500210000r1",
        "name_short": "Glass Tube Fuse 5F.0500210000R1 (5.2x20 mm, 500mA 250V)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "5_2_x_20_mm_glass_plugin", "taxonomy_4": "disposable",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "5f_1600210000r1",
        "name_short": "Glass Tube Fuse 5F.1600210000R1 (5.2x20 mm, 1.6A 250V)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "5_2_x_20_mm_glass_plugin", "taxonomy_4": "disposable",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "0_2a_250vacglass_tube_fuse",
        "name_short": "Glass Tube Fuse 200mA 250VAC (5.2x20 mm)",
    })

    # Radial through-hole and SMD resettable fuses (PTCs) from the JLC
    # house-parts queue: Littelfuse RXEF/RUEF radial bodies and the 1812
    # miniSMD.
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "radial_5_08_mm_pitch", "taxonomy_4": "resettable",
        "taxonomy_14": "littelfuse", "taxonomy_15": "rxef010",
        "name_short": "Resettable Fuse RXEF010 (radial, 100mA hold)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "radial_5_08_mm_pitch", "taxonomy_4": "resettable",
        "taxonomy_14": "littelfuse", "taxonomy_15": "ruef110",
        "name_short": "Resettable Fuse RUEF110 (radial, 1.1A hold)",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "1812", "taxonomy_4": "resettable",
        "taxonomy_14": "littelfuse", "taxonomy_15": "minismdc020f_2",
        "name_short": "Resettable Fuse MINISMDC020F-2 (1812, 200mA hold)",
    })

    # First fuseholders in the family: 5x20 mm clip and bracket-type holders.
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "5_x_20_mm", "taxonomy_4": "clip_fuseholder",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "5x20_environmentally_friendly_fuse_clip_socket",
        "name_short": "5x20 Clip Fuse Holder/Socket",
    })
    options.append({
        "taxonomy_2": "fuse", "taxonomy_3": "5_x_20_mm", "taxonomy_4": "bracket_fuseholder",
        "taxonomy_14": "xucheng_elec", "taxonomy_15": "5x20_blx_atype_fuse_holder_xc_7",
        "name_short": "5x20 BLX-A Bracket Fuse Holder XC-7 (6.3A 250V)",
    })


if __name__ == "__main__":
    main()
