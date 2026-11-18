append_text = '''
    # Generic match for USB-C receptacle used in Easyduino projects
    current = "electronic_connector_usb_c_surface_mount_16_pin_shou_han_type_c_16pin_2md_073"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_match"] = {
            "values": ["USB_C_Receptacle_USB2.0", "USB_C_Receptacle"],
            "symbols": ["Connector:USB_C_Receptacle_USB2.0", "Connector:USB_C_Receptacle_USB2.0_16P"],
            "footprints": [
                "Connector_USB:USB_C_Receptacle_G-Switch_GT-USB-7010ASV",
                "SparkFun-Connector:USB-C_16",
            ],
        }
'''

with open('working_oomp_populate_connector_extra.py', 'a') as f:
    f.write(append_text)

print("done")
