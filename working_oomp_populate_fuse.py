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


if __name__ == "__main__":
    main()
