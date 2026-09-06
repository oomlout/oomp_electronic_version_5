content = open('working_oomp_populate_diode_extra.py').read()

old = '''    current = "electronic_diode_schottky_0402_generic_1ss400"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Schottky Diode 0402 (generic)"
        part["name_readable"] = "Schottky Diode 0402 (generic)"
        part["name_proper"] = "Schottky Diode 0402 (generic)"
        part["dimensions_mm"] = {"length": 1.0, "width": 0.5}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_0402_1005Metric",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky"],
            "symbols": ["Device:D_Schottky"],
            "footprints": ["Diode_SMD:D_0402_1005Metric"],
        }'''

new = '''    current = "electronic_diode_schottky_sod_523_generic_1ss400"
    if current in extras_dict:
        part = extras_dict[current]
        part["name_short"] = "Schottky Diode SOD-523 (generic)"
        part["name_readable"] = "Schottky Diode SOD-523 (generic)"
        part["name_proper"] = "Schottky Diode SOD-523 (generic)"
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SOD-523",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky"],
            "symbols": ["Device:D_Schottky"],
            "footprints": ["Diode_SMD:D_0402_1005Metric", "Diode_SMD:D_SOD-523"],
        }'''

assert old in content, "old not found"
content = content.replace(old, new)
open('working_oomp_populate_diode_extra.py', 'w').write(content)
print("done")
