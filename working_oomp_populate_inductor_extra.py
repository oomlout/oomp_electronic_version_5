def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_inductor_0603_10_micro_henry"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Inductor 10µH 0603"
        part["name_readable"] = "Inductor 10µH 0603"
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~", "type": "passive"},
            "pin_2": {"number": "2", "name": "~", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:L",
            "machine_solder": "Inductor_SMD:L_0603_1608Metric",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["L"],
            "symbols": ["Device:L"],
            "footprints": ["Inductor_SMD:L_0603_1608Metric"],
        }
