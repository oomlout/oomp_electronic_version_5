f = open(r'working_oomp_populate_ic.py')
c = f.read()
f.close()

old = '''    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "qfn_28_5_mm_x_5_mm",
        "taxonomy_4": "converter", "taxonomy_5": "usb_to_serial_converter",
        "taxonomy_14": "silicon_labs", "taxonomy_15": "cp2102_gmr",
    })'''

new = '''    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "tqfp_32_7_mm_x_7_mm",
        "taxonomy_4": "microcontroller", "taxonomy_5": "8_bit_avr",
        "taxonomy_14": "microchip", "taxonomy_15": "atmega328p_au",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "sop_16",
        "taxonomy_4": "converter", "taxonomy_5": "usb_to_serial_converter",
        "taxonomy_14": "wch", "taxonomy_15": "ch340c",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "qfn_28_5_mm_x_5_mm",
        "taxonomy_4": "converter", "taxonomy_5": "usb_to_serial_converter",
        "taxonomy_14": "silicon_labs", "taxonomy_15": "cp2102n_a01_gqfn28r",
    })
    options.append({
        "taxonomy_2": "ic", "taxonomy_3": "esp32_s3_wroom_1",
        "taxonomy_4": "microcontroller", "taxonomy_5": "wifi_bluetooth_8_mb_flash",
        "taxonomy_14": "espressif", "taxonomy_15": "esp32_s3_wroom_1_n8",
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
    print('Done - added ATmega328P, CH340C, CP2102N, ESP32-S3-WROOM-1')
else:
    print('Old string not found')
