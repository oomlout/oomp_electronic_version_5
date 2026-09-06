f = open(r'working_oomp_populate_ic_extra.py')
c = f.read()
f.close()

# Insert after the AMS1117-3.3 block and before the CP2102 block
old = '''    current = "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102_gmr"'''

new = '''    current = "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_5_volt_advanced_monolithic_systems_ams1117_5"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Advanced Monolithic Systems"
        part["part_number_manufacturer"] = "AMS1117-5.0"
        part["part_number_lcsc"] = "C6187"
        part["product_url"] = "https://www.lcsc.com/product-detail/C6187.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C6187.pdf"
        part["name_readable_override"] = "Regulator AMS1117-5.0 5V SOT-223"
        part["name_short"] = "Regulator AMS1117-5.0"
        part["category"] = "power_management"
        part["dimensions_mm"] = {"length": 6.5, "width": 7.0}
        part["dimension_reference"] = {"document": "AMS1117 datasheet", "pages": [1, 7], "notes": "Nominal SOT-223 dimensions; tab is VOUT, pin 2."}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "gnd", "type": "gnd"},
            "pin_2": {"number": "2", "name": "vout", "type": "power"},
            "pin_3": {"number": "3", "name": "vin", "type": "power"},
        }
        part["package_drawing"] = {
            "overall": [6.5, 7.0], "body": [6.5, 3.5],
            "pins": [["1", "bottom", -2.29, -2.625, .74, 1.75],
                     ["2", "bottom", 0, -2.625, .74, 1.75],
                     ["3", "bottom", 2.29, -2.625, .74, 1.75],
                     ["2", "top", 0, 2.625, 3.05, 1.75]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:AMS1117-5.0", "machine_solder": "Package_TO_SOT_SMD:SOT-223-3_TabPin2", "hand_solder": ""}

    current = "electronic_ic_sot_23_power_management_linear_voltage_regulator_3_3_volt_torex_xc6206p332mr"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Torex"
        part["part_number_manufacturer"] = "XC6206P332MR"
        part["part_number_lcsc"] = "C51489"
        part["product_url"] = "https://www.lcsc.com/product-detail/C51489.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C51489.pdf"
        part["name_readable_override"] = "Regulator XC6206P332MR 3.3V SOT-23"
        part["name_short"] = "Regulator XC6206P332MR"
        part["category"] = "power_management"
        part["dimensions_mm"] = {"length": 2.92, "width": 2.8}
        part["dimension_reference"] = {"document": "XC6206 datasheet", "pages": [10], "notes": "SOT-23 package outline."}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "vss", "type": "gnd"},
            "pin_2": {"number": "2", "name": "vout", "type": "power"},
            "pin_3": {"number": "3", "name": "vin", "type": "power"},
        }
        part["package_drawing"] = {
            "overall": [2.92, 2.8], "body": [2.92, 1.6],
            "pins": [["1", "bottom", -0.95, -1.45, .5, .95],
                     ["2", "bottom", 0, -1.45, .5, .95],
                     ["3", "bottom", 0.95, -1.45, .5, .95]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:XC6206PxxxMR", "machine_solder": "Package_TO_SOT_SMD:SOT-23", "hand_solder": ""}

    current = "electronic_ic_sot_23_power_management_linear_voltage_regulator_5_volt_torex_xc6206p502mr"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Torex"
        part["part_number_manufacturer"] = "XC6206P502MR"
        part["part_number_lcsc"] = "C51490"
        part["product_url"] = "https://www.lcsc.com/product-detail/C51490.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C51490.pdf"
        part["name_readable_override"] = "Regulator XC6206P502MR 5V SOT-23"
        part["name_short"] = "Regulator XC6206P502MR"
        part["category"] = "power_management"
        part["dimensions_mm"] = {"length": 2.92, "width": 2.8}
        part["dimension_reference"] = {"document": "XC6206 datasheet", "pages": [10], "notes": "SOT-23 package outline."}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "vss", "type": "gnd"},
            "pin_2": {"number": "2", "name": "vout", "type": "power"},
            "pin_3": {"number": "3", "name": "vin", "type": "power"},
        }
        part["package_drawing"] = {
            "overall": [2.92, 2.8], "body": [2.92, 1.6],
            "pins": [["1", "bottom", -0.95, -1.45, .5, .95],
                     ["2", "bottom", 0, -1.45, .5, .95],
                     ["3", "bottom", 0.95, -1.45, .5, .95]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:XC6206PxxxMR", "machine_solder": "Package_TO_SOT_SMD:SOT-23", "hand_solder": ""}

    current = "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102_gmr"'''

if old in c:
    c = c.replace(old, new)
    f = open(r'working_oomp_populate_ic_extra.py', 'w')
    f.write(c)
    f.close()
    print('Done - replaced')
else:
    print('Old string not found')
