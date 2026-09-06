f = open(r'working_oomp_populate_ic_extra.py')
c = f.read()
f.close()

# Find the end of the file (before if __name__ block if present, or just append)
insert_marker = '''    current = "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102_gmr"'''

new_entries = '''
    current = "electronic_ic_tqfp_32_7_mm_x_7_mm_microcontroller_8_bit_avr_microchip_atmega328p_au"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Microchip"
        part["part_number_manufacturer"] = "ATmega328P-AU"
        part["part_number_lcsc"] = "C14877"
        part["product_url"] = "https://www.lcsc.com/product-detail/C14877.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C14877.pdf"
        part["name_readable_override"] = "MCU ATmega328P-AU 8-bit AVR TQFP-32"
        part["name_short"] = "ATmega328P-AU"
        part["category"] = "mcu"
        part["dimensions_mm"] = {"length": 7.0, "width": 7.0}
        part["dimension_reference"] = {"document": "ATmega328P datasheet", "pages": [2, 12], "notes": "TQFP-32 7x7mm, 0.8mm pitch"}
        part["kicad"] = {"symbol": "MCU_Microchip_ATmega:ATmega328P-A", "machine_solder": "Package_QFP:TQFP-32_7x7mm_P0.8mm", "hand_solder": ""}

    current = "electronic_ic_sop_16_converter_usb_to_serial_converter_wch_ch340c"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "WCH"
        part["part_number_manufacturer"] = "CH340C"
        part["part_number_lcsc"] = "C84681"
        part["product_url"] = "https://www.lcsc.com/product-detail/C84681.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C84681.pdf"
        part["name_readable_override"] = "USB-Serial CH340C SOP-16"
        part["name_short"] = "CH340C"
        part["category"] = "interface"
        part["dimensions_mm"] = {"length": 9.9, "width": 3.9}
        part["dimension_reference"] = {"document": "CH340 datasheet", "pages": [1], "notes": "SOP-16, 1.27mm pitch, built-in clock"}
        part["kicad"] = {"symbol": "Interface_USB:CH340C", "machine_solder": "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm", "hand_solder": ""}

    current = "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102n_a01_gqfn28r"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Silicon Labs"
        part["part_number_manufacturer"] = "CP2102N-A01-GQFN28R"
        part["part_number_lcsc"] = "C105167"
        part["product_url"] = "https://www.lcsc.com/product-detail/C105167.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C105167.pdf"
        part["name_readable_override"] = "USB-Serial CP2102N-A01-GQFN28R"
        part["name_short"] = "CP2102N-A01"
        part["category"] = "interface"
        part["dimensions_mm"] = {"length": 5.0, "width": 5.0}
        part["dimension_reference"] = {"document": "CP2102N datasheet", "pages": [22, 23], "notes": "QFN-28 5x5mm, 0.5mm pitch, EP 3.35x3.35mm"}
        part["kicad"] = {"symbol": "Interface_USB:CP2102N-Axx-xQFN28", "machine_solder": "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm", "hand_solder": ""}

    current = "electronic_ic_esp32_s3_wroom_1_microcontroller_wifi_bluetooth_8_mb_flash_espressif_esp32_s3_wroom_1_n8"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Espressif"
        part["part_number_manufacturer"] = "ESP32-S3-WROOM-1-N8"
        part["part_number_lcsc"] = "C2913198"
        part["product_url"] = "https://www.lcsc.com/product-detail/C2913198.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C2913198.pdf"
        part["name_readable_override"] = "WiFi/BLE Module ESP32-S3-WROOM-1-N8 8MB"
        part["name_short"] = "ESP32-S3-WROOM-1-N8"
        part["category"] = "mcu"
        part["dimensions_mm"] = {"length": 18.0, "width": 25.5, "height": 3.1}
        part["dimension_reference"] = {"document": "ESP32-S3-WROOM-1 datasheet", "pages": [3, 4], "notes": "Module with PCB antenna, 39 castellated pins on 1.27mm pitch"}
        part["kicad"] = {"symbol": "RF_Module:ESP32-S3-WROOM-1", "machine_solder": "RF_Module:ESP32-S3-WROOM-1", "hand_solder": ""}

    current = "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102_gmr"'''

if insert_marker in c:
    c = c.replace(insert_marker, new_entries)
    f = open(r'working_oomp_populate_ic_extra.py', 'w')
    f.write(c)
    f.close()
    print('Done - added extra metadata for 4 new ICs')
else:
    print('Insert marker not found')
