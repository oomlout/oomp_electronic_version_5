def main(**kwargs):
    options = kwargs.get("options", [])

    inductors = [
        {"size": "0603", "inductance": "10_micro_henry"},
        {"size": "0806", "inductance": "2_2_micro_henry"},
        {"size": "0603", "inductance": "33_nano_henry"},
        {"size": "0603", "inductance": "470_ohm"},
        {"size": "0603", "inductance": "30_ohm"},
    ]

    for inductor in inductors:
        option = {}
        option["taxonomy_2"] = "inductor"
        option["taxonomy_3"] = inductor["size"]
        option["taxonomy_4"] = inductor["inductance"]
        options.append(option)
