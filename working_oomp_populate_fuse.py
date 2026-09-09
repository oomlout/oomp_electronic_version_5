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


if __name__ == "__main__":
    main()
