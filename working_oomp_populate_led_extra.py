def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})
    current = "electronic_led_0402_blue"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Yongyu Photoelectric"
        part["part_number_manufacturer"] = "SZYY0402B"
        part["part_number_manufacturer_yongyu_photoelectric"] = "SZYY0402B"
        part["part_number_lcsc"] = "C434447"
        part["product_url"] = "https://www.lcsc.com/product-detail/C434447.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C434447.pdf"

    # WS2812B parts carry four functional pins on their PLCC4-style bodies
    # (Worldsemi datasheet: 1 VDD, 2 DOUT, 3 VSS, 4 DIN); the 5050 body's
    # sixth-pad corners are not connected.
    ws2812b_parts = [
        "electronic_led_5050_rgb_ws2812b_worldsemi_ws2812b_b_w",
        "electronic_led_1010_rgb_ws2812b_xinglight_1010rgbc",
    ]
    for current in ws2812b_parts:
        if current not in extras_dict:
            continue
        extras_dict[current]["pins"] = {}
        if current == "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a":
            # SK6812SIDE-A datasheet: 1 DIN, 2 VDD, 3 DOUT, 4 GND.
            pins = [["1", "data_in"], ["2", "vdd"], ["3", "data_out"], ["4", "gnd"]]
        else:
            # SK6812MINI-E datasheet: 1 VDD, 2 DOUT, 3 GND, 4 DIN.
            pins = [["1", "vdd"], ["2", "data_out"], ["3", "gnd"], ["4", "data_in"]]
        for pin_index in range(len(pins)):
            pin = pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0], "name": pin[1], "type": "signal"
            }

    led_parts = [
        [
            "electronic_led_3535_rgb_sk6812_opsco_optoelectronics_sk6812mini_e",
            "SK6812MINI-E",
            "C5149201",
        ],
        [
            "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a",
            "SK6812SIDE-A",
            "C5378721",
        ],
    ]
    for led_part in led_parts:
        current = led_part[0]
        if current not in extras_dict:
            continue
        extras_dict[current]["part_number_manufacturer"] = led_part[1]
        extras_dict[current]["part_number_lcsc"] = led_part[2]
        extras_dict[current]["pins"] = {}
        if current == "electronic_led_4020_side_view_rgb_sk6812_opsco_optoelectronics_sk6812side_a":
            # SK6812SIDE-A datasheet: 1 DIN, 2 VDD, 3 DOUT, 4 GND.
            pins = [["1", "data_in"], ["2", "vdd"], ["3", "data_out"], ["4", "gnd"]]
        else:
            # SK6812MINI-E datasheet: 1 VDD, 2 DOUT, 3 GND, 4 DIN.
            pins = [["1", "vdd"], ["2", "data_out"], ["3", "gnd"], ["4", "data_in"]]
        for pin_index in range(len(pins)):
            pin = pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0], "name": pin[1], "type": "signal"
            }

    # The SparkFun 1205 RGB indicator is a four-pad 1205 metric package, not
    # the two-terminal generic LED fallback.  Keep the common-anode/cathode
    # identity explicit so assembly and pinout diagrams show all four pads.
    current = "electronic_led_1205_rgb"
    if current in extras_dict:
        part = extras_dict[current]
        part["dimensions_mm"] = {"length": 3.2, "width": 1.6}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "R", "type": "signal"},
            "pin_2": {"number": "2", "name": "G", "type": "signal"},
            "pin_3": {"number": "3", "name": "B", "type": "signal"},
            "pin_4": {"number": "4", "name": "COM", "type": "signal"},
        }
        part["package_drawing"] = {
            "overall": [3.2, 1.6],
            "body": [2.4, 1.2],
            "pins": [
                ["1", "bottom", -1.05, -0.7, 0.45, 0.4],
                ["2", "bottom", -0.35, -0.7, 0.45, 0.4],
                ["3", "bottom", 0.35, -0.7, 0.45, 0.4],
                ["4", "bottom", 1.05, -0.7, 0.45, 0.4],
            ],
            "pin_one": [-1.05, -0.7],
        }

    # SparkFun LED_1206_Bottom_Green is the board-facing version of the
    # standard 1206 green LED footprint.  It is a two-terminal device; the
    # bottom-facing footprint name must not turn it into the unrelated four
    # pad 1205 RGB entry above.
    current = "electronic_led_1206_bottom_green"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Inolux"
        part["part_number_manufacturer"] = "IN-S126ATG"
        part["product_url"] = "https://www.sparkfun.com/bright-green-led-surface-mount-1206.html"
        part["dimensions_mm"] = {"length": 3.2, "width": 1.5, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SparkFun Bright Green LED Surface Mount 1206 / IN-S126ATG",
            "notes": "3.20 x 1.50 x 1.10 mm LED; bottom-view Eagle footprint with two contacts.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "signal"},
            "pin_2": {"number": "2", "name": "A", "type": "signal"},
        }
        part["package_drawing"] = {
            "overall": [3.2, 1.5],
            "body": [2.35, 1.10],
            "pins": [
                ["1", "left", -1.35, 0.0, 0.50, 1.05],
                ["2", "right", 1.35, 0.0, 0.50, 1.05],
            ],
            "pin_one": [-1.35, 0.0],
        }
