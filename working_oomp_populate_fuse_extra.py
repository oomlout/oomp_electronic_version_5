def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_fuse_0402_resettable"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Polyfuse 0402"
        part["name_readable"] = "Resettable Fuse 0402"
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~", "type": "passive"},
            "pin_2": {"number": "2", "name": "~", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_0402_1005Metric",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["Polyfuse"],
            "symbols": ["Device:Polyfuse"],
            "footprints": ["Fuse:Fuse_0402_1005Metric"],
        }

    current = "electronic_fuse_1206_resettable"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Polyfuse 1206"
        part["name_readable"] = "Resettable Fuse 1206"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~", "type": "passive"},
            "pin_2": {"number": "2", "name": "~", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_1206_3216Metric",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["Polyfuse"],
            "symbols": ["Device:Polyfuse"],
            "footprints": ["Fuse:Fuse_1206_3216Metric"],
        }
