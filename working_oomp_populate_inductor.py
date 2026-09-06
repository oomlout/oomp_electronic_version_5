def main(**kwargs):
    options = kwargs.get("options", [])

    inductors = [
        {"size": "0603", "inductance": "10_micro_henry"},
    ]

    for inductor in inductors:
        option = {}
        option["taxonomy_2"] = "inductor"
        option["taxonomy_3"] = inductor["size"]
        option["taxonomy_4"] = inductor["inductance"]
        options.append(option)
