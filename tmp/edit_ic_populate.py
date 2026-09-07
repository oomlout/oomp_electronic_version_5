f = open(r'working_oomp_populate_ic.py')
c = f.read()
f.close()

old = '''    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_223_3",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_3_3_volt",
        "taxonomy_14": "advanced_monolithic_systems", "taxonomy_15": "ams1117_3_3",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "qfn_28_5_mm_x_5_mm",
        "taxonomy_4": "converter", "taxonomy_5": "usb_to_serial_converter",
        "taxonomy_14": "silicon_labs", "taxonomy_15": "cp2102_gmr",
    })'''

new = '''    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_223_3",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_3_3_volt",
        "taxonomy_14": "advanced_monolithic_systems", "taxonomy_15": "ams1117_3_3",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_223_3",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_5_volt",
        "taxonomy_14": "advanced_monolithic_systems", "taxonomy_15": "ams1117_5",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_3_3_volt",
        "taxonomy_14": "torex", "taxonomy_15": "xc6206p332mr",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sot_23",
        "taxonomy_4": "power_management", "taxonomy_5": "linear_voltage_regulator_5_volt",
        "taxonomy_14": "torex", "taxonomy_15": "xc6206p502mr",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "qfn_28_5_mm_x_5_mm",
        "taxonomy_4": "converter", "taxonomy_5": "usb_to_serial_converter",
        "taxonomy_14": "silicon_labs", "taxonomy_15": "cp2102_gmr",
    })'''

if old in c:
    c = c.replace(old, new)
    f = open(r'working_oomp_populate_ic.py', 'w')
    f.write(c)
    f.close()
    print('Done - replaced')
else:
    print('Old string not found')
