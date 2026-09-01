def main(**kwargs):
    options = kwargs.get("options", [])

    # Standard indicator LEDs. Empty values retain the generic legacy entries.
    sizes = ["0201", "0402", "0603", "0805", "1206", "3_mm", "5_mm", "10_mm"]
    colors = ["", "blue", "green", "red", "white", "yellow"]
    lens_styles = ["", "clear", "tint"]
    for size in sizes:
        for color in colors:
            for lens_style in lens_styles:
                option = {}
                option["taxonomy_2"] = "led"
                option["taxonomy_3"] = size
                option["taxonomy_4"] = color
                option["taxonomy_5"] = lens_style
                options.append(option)

    # Addressable RGB LEDs from the old component set.
    addressable_leds = [
        {
            "size": "1010",
            "color": "rgb",
            "controller": "ws2812b",
            "manufacturer": "xinglight",
            "part_number": "1010rgbc",
        },
        {
            "size": "5050",
            "color": "rgb",
            "controller": "ws2812b",
            "manufacturer": "worldsemi",
            "part_number": "ws2812b_b_w",
        },
    ]
    for addressable_led in addressable_leds:
        option = {}
        option["taxonomy_2"] = "led"
        option["taxonomy_3"] = addressable_led["size"]
        option["taxonomy_4"] = addressable_led["color"]
        option["taxonomy_5"] = addressable_led["controller"]
        option["taxonomy_6"] = addressable_led["manufacturer"]
        option["taxonomy_7"] = addressable_led["part_number"]
        options.append(option)

    bus_pirate_leds = [
        {
            "size": "3535",
            "color": "rgb",
            "controller": "sk6812",
            "manufacturer": "opsco_optoelectronics",
            "part_number": "sk6812mini_e",
        },
        {
            "size": "4020_side_view",
            "color": "rgb",
            "controller": "sk6812",
            "manufacturer": "opsco_optoelectronics",
            "part_number": "sk6812side_a",
        },
    ]
    for bus_pirate_led in bus_pirate_leds:
        option = {}
        option["taxonomy_2"] = "led"
        option["taxonomy_3"] = bus_pirate_led["size"]
        option["taxonomy_4"] = bus_pirate_led["color"]
        option["taxonomy_5"] = bus_pirate_led["controller"]
        option["taxonomy_6"] = bus_pirate_led["manufacturer"]
        option["taxonomy_7"] = bus_pirate_led["part_number"]
        options.append(option)

    colors = ["blue", "green", "pink", "red", "warm_white", "yellow"]
    lengths = [
        "38_mm_length",
        "60_mm_length",
        "80_mm_length",
        "95_mm_length",
        "130_mm_length",
        "145_mm_length",
        "185_mm_length",
        "260_mm_length",
        "300_mm_length",
    ]
    for color in colors:
        for length in lengths:
            option = {}
            option["taxonomy_2"] = "led"
            option["taxonomy_3"] = "filament_3_volt"
            option["taxonomy_4"] = color
            option["taxonomy_5"] = length
            options.append(option)

    voltages = [5, 12, 24]
    widths = [3, 5, 8]
    colors = ["blue", "green", "pink", "red", "warm_white", "yellow"]
    lengths = [
        "500_mm_length",
        "1000_mm_length",
        "2000_mm_length",
        "3000_mm_length",
        "5000_mm_length",
    ]
    led_densities = ["", "320_leds_per_meter"]
    for voltage in voltages:
        for width in widths:
            for color in colors:
                for length in lengths:
                    for led_density in led_densities:
                        option = {}
                        option["taxonomy_2"] = "led"
                        option["taxonomy_3"] = f"strip_{voltage}_volt_{width}_mm_width"
                        option["taxonomy_4"] = color
                        option["taxonomy_5"] = length
                        option["taxonomy_6"] = led_density
                        options.append(option)


if __name__ == "__main__":
    main()
