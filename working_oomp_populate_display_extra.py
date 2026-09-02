def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_display_tft_2_inch_240_x_320_pixel_ips_spi_12_pin_szhtc_qt200h1201"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "QT200H1201"
        extras_dict[current]["part_number_manufacturer_szhtc"] = "QT200H1201"
        extras_dict[current]["manufacturer"] = "SZHTC"
        extras_dict[current]["controller"] = "ST7789V"
        extras_dict[current]["supplier_url"] = "https://item.taobao.com/item.htm?id=581793017604"
        extras_dict[current]["project_bom_url"] = "https://hardware.buspirate.com/bom"
        extras_dict[current]["datasheet_url"] = "https://device.report/m/07680e0977a46bb493db9b7bf791be435de59b37345e7119556ab12e3b367f61.pdf"
        extras_dict[current]["datasheet_publisher"] = "Shenzhen Surenoo Technology Co., Ltd."
        extras_dict[current]["display_dimensions_mm"] = {
            "body_width": 34.6,
            "body_height": 47.8,
            "body_thickness": 1.9,
            "active_width": 30.6,
            "active_height": 40.8,
            "pixel_pitch_x": 0.1275,
            "pixel_pitch_y": 0.1275,
            "fpc_pin_pitch": 0.8,
            "fpc_pad_width": 0.6,
            "fpc_pad_length": 2.55,
        }
        extras_dict[current]["electrical"] = {
            "logic_supply_typical": "2.8 V",
            "logic_supply_range": "2.5 to 3.3 V",
            "io_supply_typical": "1.8 or 2.8 V",
            "backlight_forward_voltage": "3.0 to 3.3 V",
            "backlight_current_typical": "60 mA",
        }
        extras_dict[current]["display"] = {
            "diagonal_size": "2.0 inch",
            "technology": "IPS TFT LCD",
            "resolution": "240 x 320 RGB pixels",
            "interface": "4-wire SPI",
            "viewing_direction": "all",
            "color_depth": "262K",
        }
        extras_dict[current]["pins"] = {}
        display_pins = [
            ["1", "gnd", "power_in"],
            ["2", "led_k", "power_in"],
            ["3", "led_a", "power_in"],
            ["4", "vci", "power_in"],
            ["5", "gnd", "power_in"],
            ["6", "gnd", "power_in"],
            ["7", "wr_a0", "input"],
            ["8", "chip_select", "input"],
            ["9", "rs_scl", "input"],
            ["10", "serial_data", "input"],
            ["11", "reset", "input"],
            ["12", "gnd", "power_in"],
        ]
        for pin_index in range(len(display_pins)):
            pin = display_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate fitted BOM identifies the brand as SZHTC and the part as QT200H1201.",
            "The browser-downloaded Surenoo manual explicitly labels its mechanical drawing PRODUCT NO: QT200H1201.",
            "LCSC search returned zero exact QT200H1201 results, so no LCSC number is recorded.",
            "The product is a 2.0 inch module with 12 flex contacts; TFT_20 means 2.0 inch, not 20 pins.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
