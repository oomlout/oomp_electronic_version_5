import re

path = r"C:\gh\oomp_electronic_version_5\working_oomp_populate_ic_extra.py"
with open(path, "r") as f:
    text = f.read()

# Fix XC6206P332MR package_drawing
old1 = '''        part["package_drawing"] = {
            "overall": [2.92, 2.8], "body": [2.92, 1.6],
            "pins": [["1", "bottom", -0.95, -1.45, .5, .95],
                     ["2", "bottom", 0, -1.45, .5, .95],
                     ["3", "bottom", 0.95, -1.45, .5, .95]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:XC6206PxxxMR", "machine_solder": "Package_TO_SOT_SMD:SOT-23", "hand_solder": ""}

    current = "electronic_ic_sot_23_power_management_linear_voltage_regulator_5_volt_torex_xc6206p502mr"'''

new1 = '''        part["package_drawing"] = {
            "overall": [2.92, 2.8], "body": [2.92, 1.6],
            "pins": [["1", "bottom", -0.95, -1.45, .5, .95],
                     ["2", "bottom", 0.95, -1.45, .5, .95],
                     ["3", "top", 0, 1.45, .5, .95]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:XC6206PxxxMR", "machine_solder": "Package_TO_SOT_SMD:SOT-23", "hand_solder": ""}

    current = "electronic_ic_sot_23_power_management_linear_voltage_regulator_5_volt_torex_xc6206p502mr"'''

if old1 in text:
    text = text.replace(old1, new1, 1)
    print("Fixed XC6206P332MR package_drawing")
else:
    print("ERROR: XC6206P332MR pattern not found")

# Fix XC6206P502MR package_drawing
old2 = '''    current = "electronic_ic_sot_23_power_management_linear_voltage_regulator_5_volt_torex_xc6206p502mr"
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
        part["kicad"] = {"symbol": "Regulator_Linear:XC6206PxxxMR", "machine_solder": "Package_TO_SOT_SMD:SOT-23", "hand_solder": ""}'''

new2 = '''    current = "electronic_ic_sot_23_power_management_linear_voltage_regulator_5_volt_torex_xc6206p502mr"
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
                     ["2", "bottom", 0.95, -1.45, .5, .95],
                     ["3", "top", 0, 1.45, .5, .95]],
        }
        part["kicad"] = {"symbol": "Regulator_Linear:XC6206PxxxMR", "machine_solder": "Package_TO_SOT_SMD:SOT-23", "hand_solder": ""}'''

if old2 in text:
    text = text.replace(old2, new2, 1)
    print("Fixed XC6206P502MR package_drawing")
else:
    print("ERROR: XC6206P502MR pattern not found")

with open(path, "w") as f:
    f.write(text)
