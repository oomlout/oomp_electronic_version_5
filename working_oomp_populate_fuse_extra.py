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

    current = "electronic_fuse_0603_resettable_bourns_mf_fsmf"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Bourns"
        part["part_number_manufacturer"] = "MF-FSMF"
        part["name_short"] = "Bourns MF-FSMF 0603 Resettable Fuse"
        part["name_readable"] = "Bourns MF-FSMF Series 0603 Resettable Fuse"
        part["datasheet_url"] = "https://www.bourns.com/docs/product-datasheets/mffsmf.pdf"
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.6}
        part["dimension_reference"] = {
            "document": "Bourns MF-FSMF Series datasheet",
            "notes": "0603 low-profile surface-mount PTC series; electrical suffix is intentionally unspecified because the source schematic only gives the series footprint.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "~", "type": "passive"},
            "pin_2": {"number": "2", "name": "~", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:Polyfuse",
            "machine_solder": "Fuse:Fuse_0603_1608Metric",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["MF-FSMF", "Polyfuse"],
            "symbols": ["Device:Polyfuse"],
            "footprints": ["Fuse:Fuse_0603_1608Metric", "MF-FSMF"],
        }
