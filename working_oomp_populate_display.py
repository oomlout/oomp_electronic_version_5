def main(**kwargs):
    options = kwargs.get("options", [])

    # Displays vary too much for a cross-product.  Keep each real module in
    # this plain array so dimensions, interface and exact identity stay tied.
    displays = [
        {
            "display_type": "lcd",
            "format": "character",
            "resolution": "16_by_2",
            "feature": "backlight_yellow",
        },
        {
            "display_type": "tft",
            "format": "2_inch",
            "resolution": "240_x_320_pixel",
            "feature": "ips",
            "interface": "spi",
            "pin_count": "12_pin",
            "manufacturer": "szhtc",
            "part_number": "qt200h1201",
            "name_short": "2 Inch IPS TFT 240 x 320",
            "dimensions_mm": {"length": 34.6, "width": 47.8},
        },
    ]

    for display in displays:
        option = {}
        option["taxonomy_2"] = "display"
        option["taxonomy_3"] = display["display_type"]
        option["taxonomy_4"] = display["format"]
        option["taxonomy_5"] = display["resolution"]
        option["taxonomy_6"] = display["feature"]
        if "interface" in display:
            option["taxonomy_7"] = display["interface"]
        if "pin_count" in display:
            option["taxonomy_8"] = display["pin_count"]
        if "manufacturer" in display:
            option["taxonomy_14"] = display["manufacturer"]
        if "part_number" in display:
            option["taxonomy_15"] = display["part_number"]
        if "name_short" in display:
            option["name_short"] = display["name_short"]
        if "dimensions_mm" in display:
            option["dimensions_mm"] = dict(display["dimensions_mm"])
        options.append(option)


if __name__ == "__main__":
    main()
