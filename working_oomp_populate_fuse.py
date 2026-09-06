def main(**kwargs):
    options = kwargs.get("options", [])

    fuses = [
        {"size": "0402", "fuse_type": "resettable"},
        {"size": "1206", "fuse_type": "resettable"},
    ]

    for fuse in fuses:
        option = {}
        option["taxonomy_2"] = "fuse"
        option["taxonomy_3"] = fuse["size"]
        option["taxonomy_4"] = fuse["fuse_type"]
        options.append(option)
