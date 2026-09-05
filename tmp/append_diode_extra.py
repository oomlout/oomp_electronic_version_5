append_text = '''
    # Generic Schottky diodes
    current = "electronic_diode_schottky_sod_123_generic_ss14"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Generic"
        part["name_short"] = "Schottky Diode SOD-123 (generic)"
        part["name_readable"] = "Schottky Diode SOD-123 (generic)"
        part["name_proper"] = "Schottky Diode SOD-123 (generic)"
        part["dimensions_mm"] = {"length": 3.5, "width": 1.6}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SOD-123",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky"],
            "symbols": ["Device:D_Schottky"],
            "footprints": ["Diode_SMD:D_SOD-123"],
        }

    current = "electronic_diode_schottky_sod_323_generic_bat54w"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Generic"
        part["name_short"] = "Schottky Diode SOD-323 (generic)"
        part["name_readable"] = "Schottky Diode SOD-323 (generic)"
        part["name_proper"] = "Schottky Diode SOD-323 (generic)"
        part["dimensions_mm"] = {"length": 2.1, "width": 1.25}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "cathode", "type": "passive"},
            "pin_2": {"number": "2", "name": "anode", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:D_Schottky",
            "machine_solder": "Diode_SMD:D_SOD-323",
            "hand_solder": "",
        }
        part["generic_match"] = {
            "values": ["D_Schottky", "BAT60A", "PMEG4005EJ"],
            "symbols": ["Device:D_Schottky", "SparkFun-DiscreteSemi:D_Schottky_3A_10V_0.28V", "SparkFun-DiscreteSemi:D_Schottky_0.5A_40V_0.42V"],
            "footprints": ["Diode_SMD:D_SOD-323", "SparkFun-Semiconductor-Standard:SOD-323"],
        }

    current = "electronic_diode_schottky_0402_generic_1ss400"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Generic"
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
        }
'''

with open('working_oomp_populate_diode_extra.py', 'a') as f:
    f.write(append_text)

print("done")
