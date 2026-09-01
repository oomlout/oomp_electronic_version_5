def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

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
        pins = [["1", "vdd"], ["2", "data_out"], ["3", "gnd"], ["4", "data_in"]]
        for pin_index in range(len(pins)):
            pin = pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0], "name": pin[1], "type": "signal"
            }
