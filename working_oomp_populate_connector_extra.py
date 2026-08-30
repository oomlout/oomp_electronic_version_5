def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "TYPE-C-31-M-12"
        extras_dict[current]["part_number_lcsc"] = "C165948"
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_connector_usb_a_surface_mount_4_pin_shenzhen_jing_tuo_jin_electronics_912121a2023s10100"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "912-121A2023S10100"
        extras_dict[current]["part_number_lcsc"] = "C42428"
        extras_dict[current]["pins"] = {}
        extras_dict[current]["pins"]["pin_1"] = {
            "name": "vbus",
            "number": "1",
            "type": "power",
        }
        extras_dict[current]["pins"]["pin_2"] = {
            "name": "usb_negative",
            "number": "2",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_3"] = {
            "name": "usb_positive",
            "number": "3",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_4"] = {
            "name": "gnd",
            "number": "4",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_5"] = {
            "name": "shield",
            "number": "5",
            "type": "signal",
        }
        extras_dict[current]["pins"]["pin_6"] = {
            "name": "shield",
            "number": "6",
            "type": "signal",
        }
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
