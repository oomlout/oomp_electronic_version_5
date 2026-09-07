"""Datasheet-shaped geometry for the second unmatched-component population pass.

This module deliberately stays in the populate/extra-detail layer.  It adds
the physical information needed for useful drawings without asserting a later
project match or inventing a KiCad library identity.
"""


def _pin_map(names):
    pins = {}
    for index, name in enumerate(names, 1):
        lowered = str(name).lower()
        pin_type = "signal"
        if lowered in {"gnd", "vss", "vssa", "dgnd", "agnd", "vssd"}:
            pin_type = "gnd"
        elif lowered in {"vcc", "vdd", "vdda", "avdd", "dvdd", "vin", "vcc_io", "v_bckp", "vcc_rf", "vddl", "vddd"}:
            pin_type = "power"
        elif lowered in {"nc", "reserved"}:
            pin_type = "no_connect"
        pins[f"pin_{index}"] = {"number": str(index), "name": str(name), "type": pin_type}
    return pins


def _gullwing(names, body=(4.9, 3.9), overall=(6.0, 5.0), pad_width=0.7):
    """Create a top-view two-row package drawing for SO/MSOP/VSSOP/SOT parts."""
    count = len(names)
    left_count = (count + 1) // 2
    right_count = count - left_count
    body_w, body_h = body
    overall_w, overall_h = overall
    pin_length = max(0.55, (overall_w - body_w) / 2)
    pins = []
    for index in range(left_count):
        y = body_h / 2 - (index + 0.5) * body_h / max(left_count, 1)
        pins.append([str(index + 1), "left", -(body_w + pin_length) / 2, y, pin_length, pad_width])
    for index in range(right_count):
        y = body_h / 2 - (index + 0.5) * body_h / max(right_count, 1)
        pins.append([str(count - index), "right", (body_w + pin_length) / 2, y, pin_length, pad_width])
    return {
        "overall": list(overall),
        "body": list(body),
        "pins": pins,
        "pin_one": [-(body_w / 2) + 0.35, (body_h / 2) - 0.35],
    }


def _qfp(names, body=(7.0, 7.0), overall=(9.7, 9.7), pad_width=0.32):
    """Create a square gull-wing package with clockwise pin numbering."""
    count = len(names)
    per_side = count // 4
    body_w, body_h = body
    overall_w, overall_h = overall
    pin_x = (body_w + overall_w) / 4
    pin_y = (body_h + overall_h) / 4
    pins = []
    for index in range(per_side):
        offset = body_h / 2 - (index + 0.5) * body_h / per_side
        pins.append([str(index + 1), "bottom", -body_w / 2 + (index + 0.5) * body_w / per_side, -pin_y, pad_width, pin_y - body_h / 2])
    for index in range(per_side):
        number = per_side + index + 1
        offset = body_w / 2 - (index + 0.5) * body_w / per_side
        pins.append([str(number), "right", pin_x, offset, pin_y - body_h / 2, pad_width])
    for index in range(per_side):
        number = per_side * 2 + index + 1
        pins.append([str(number), "top", body_w / 2 - (index + 0.5) * body_w / per_side, pin_y, pad_width, pin_y - body_h / 2])
    for index in range(per_side):
        number = per_side * 3 + index + 1
        pins.append([str(number), "left", -pin_x, -body_h / 2 + (index + 0.5) * body_h / per_side, pin_y - body_h / 2, pad_width])
    return {
        "overall": list(overall),
        "body": list(body),
        "pins": pins,
        "pin_one": [-body_w / 2 + 0.45, -body_h / 2 + 0.45],
    }


def _qfn(names, body=(4.0, 4.0), overall=(5.3, 5.3), exposed_pad=False):
    """Create a leadless square package with contacts on four edges."""
    count = len(names)
    side_counts = [count // 4] * 4
    for index in range(count % 4):
        side_counts[index] += 1
    body_w, body_h = body
    pin_x = overall[0] / 2 - 0.35
    pin_y = overall[1] / 2 - 0.35
    pins = []
    current = 1
    for side, side_count in zip(["bottom", "right", "top", "left"], side_counts):
        for index in range(side_count):
            fraction = (index + 0.5) / side_count
            if side in {"bottom", "top"}:
                x = -body_w / 2 + body_w * fraction
                y = -pin_y if side == "bottom" else pin_y
                pins.append([str(current), side, x, y, 0.42, 0.7])
            else:
                y = -body_h / 2 + body_h * fraction
                x = pin_x if side == "right" else -pin_x
                pins.append([str(current), side, x, y, 0.7, 0.42])
            current += 1
    drawing = {
        "overall": list(overall),
        "body": list(body),
        "pins": pins,
        "pin_one": [-body_w / 2 + 0.45, -body_h / 2 + 0.45],
    }
    if exposed_pad:
        drawing["boxes"] = [[0, 0, body_w * 0.42, body_h * 0.42]]
    return drawing


def _module(width, height, names, antenna=False, body=None):
    """Create a module/LGA outline with evenly distributed edge contacts."""
    body = body or (width * 0.82, height * 0.82)
    count = len(names)
    side_counts = [count // 4] * 4
    for index in range(count % 4):
        side_counts[index] += 1
    pins = []
    number = 1
    for side, side_count in zip(["left", "bottom", "right", "top"], side_counts):
        for index in range(side_count):
            fraction = (index + 0.5) / side_count
            if side in {"left", "right"}:
                x = -width / 2 + 0.25 if side == "left" else width / 2 - 0.25
                y = -height / 2 + height * fraction
                pins.append([str(number), side, x, y, 0.5, max(0.25, height / side_count * 0.45)])
            else:
                x = -width / 2 + width * fraction
                y = -height / 2 + 0.25 if side == "bottom" else height / 2 - 0.25
                pins.append([str(number), side, x, y, max(0.25, width / side_count * 0.45), 0.5])
            number += 1
    drawing = {"overall": [width, height], "body": list(body), "pins": pins,
               "pin_one": [-width / 2 + 0.6, -height / 2 + 0.6]}
    if antenna:
        drawing["boxes"] = [[0, height * 0.08, width * 0.62, height * 0.45]]
    return drawing


def _button(width, depth, pin_count=4, body=None):
    body = body or (width * 0.72, depth * 0.72)
    pins = []
    if pin_count == 2:
        pins = [["1", "left", -width / 2 + 0.35, 0, 0.7, 0.7],
                ["2", "right", width / 2 - 0.35, 0, 0.7, 0.7]]
    else:
        pins = [["1", "left", -width / 2 + 0.35, -depth * 0.28, 0.7, 0.7],
                ["2", "left", -width / 2 + 0.35, depth * 0.28, 0.7, 0.7],
                ["3", "right", width / 2 - 0.35, depth * 0.28, 0.7, 0.7],
                ["4", "right", width / 2 - 0.35, -depth * 0.28, 0.7, 0.7]]
    return {"overall": [width, depth], "body": list(body), "pins": pins,
            "circles": [[0, 0, min(width, depth) * 0.16]],
            "pin_one": [-width / 2 + 0.35, -depth * 0.28]}


def _set(part, *, dimensions, pins, drawing, reference=None, url=None):
    part["dimensions_mm"] = dict(dimensions)
    part["pins"] = _pin_map(pins)
    part["package_drawing"] = drawing
    if reference:
        part["dimension_reference"] = reference
    if url:
        part["datasheet_url"] = url


def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    # Exact packages with manufacturer drawings.
    exact = {
        "electronic_ic_lqfp_48_microcontroller_stm32_st_stm32f103c8tx": {
            "dimensions": {"length": 9.7, "width": 9.7, "height": 1.6},
            "pins": ["VBAT", "PC13", "PC14", "PC15", "PD0", "PD1", "NRST", "VSSA", "VDDA", "PA0", "PA1", "PA2", "PA3", "PA4", "PA5", "PA6", "PA7", "PB0", "PB1", "PB2", "PB10", "PB11", "VSS", "VDD", "PB12", "PB13", "PB14", "PB15", "PA8", "PA9", "PA10", "PA11", "PA12", "PA13", "VSS", "VDD", "PA14", "PA15", "PB3", "PB4", "PB5", "PB6", "PB7", "BOOT0", "PB8", "PB9", "VSS", "VDD"],
            "drawing": _qfp([str(index) for index in range(1, 49)], body=(7.0, 7.0), overall=(9.7, 9.7)),
            "reference": {"document": "STM32F103x8/xB datasheet, LQFP48 package", "notes": "7 x 7 mm body, 0.5 mm pitch, 9.7 mm maximum lead span."},
            "url": "https://www.st.com/resource/en/datasheet/stm32f103c8.pdf",
        },
        "electronic_ic_uson_8_memory_spi_nor_flash_winbond_w25q16jvuxiq": {
            "dimensions": {"length": 3.0, "width": 2.0, "height": 0.55},
            "pins": ["CS", "DO_IO1", "WP_IO2", "GND", "DI_IO0", "CLK", "HOLD_RESET_IO3", "VCC"],
            "drawing": _qfn([str(index) for index in range(1, 9)], body=(2.4, 1.4), overall=(3.0, 2.0), exposed_pad=False),
            "reference": {"document": "Winbond W25Q16JV product selection guide", "notes": "USON-8 2 x 3 mm option; the local taxonomy uses the rotated 3 x 2 mm drawing convention."},
            "url": "https://www.winbond.com/export/sites/winbond/product-selection-guide/file/2025-Product-Selection-Guide-Winbond-Code-Storage-Flash-Memory.pdf",
        },
        "electronic_ic_dfn_8_power_management_linear_voltage_regulator_diodes_ap7361c_3_3v": {
            "dimensions": {"length": 3.0, "width": 3.0, "height": 0.8},
            "pins": ["OUT", "NC", "ADJ_NC", "GND", "EN", "NC", "NC", "IN"],
            "drawing": _qfn([str(index) for index in range(1, 9)], body=(3.0, 3.0), overall=(4.2, 4.2), exposed_pad=True),
            "reference": {"document": "Diodes AP7361C datasheet, U-DFN3030-8 Type E", "notes": "Eight top-view contacts and centre GND pad; package body 3 x 3 mm."},
            "url": "https://www.diodes.com/datasheet/download/AP7361C.pdf",
        },
        "electronic_ic_qfn_14_logic_analog_switch_nexperia_74hc4066bq": {"dimensions": {"length": 3.0, "width": 3.0, "height": 0.9}, "pins": [str(index) for index in range(1, 15)], "drawing": _qfn([str(index) for index in range(1, 15)], body=(3.0, 3.0), overall=(4.2, 4.2), exposed_pad=False)},
        "electronic_ic_qfn_24_converter_usb_to_serial_converter_wch_ch342f": {"dimensions": {"length": 4.0, "width": 4.0, "height": 0.8}, "pins": [str(index) for index in range(1, 25)], "drawing": _qfn([str(index) for index in range(1, 25)], body=(4.0, 4.0), overall=(5.2, 5.2), exposed_pad=False)},
        "electronic_ic_qfn_28_power_meter_energy_metering_analog_devices_ade7953acpz": {"dimensions": {"length": 5.0, "width": 5.0, "height": 0.9}, "pins": [str(index) for index in range(1, 29)], "drawing": _qfn([str(index) for index in range(1, 29)], body=(5.0, 5.0), overall=(6.2, 6.2), exposed_pad=True)},
        "electronic_ic_soic_14_microcontroller_8_bit_avr_microchip_attiny1604_ssnr": {"dimensions": {"length": 8.65, "width": 3.9, "height": 1.75}, "pins": ["VDD", "PA4", "PA5", "PA6", "PA7", "PB5", "PB4", "PB3", "PB2", "PB1", "PB0", "PA3", "PA2", "GND"], "drawing": _gullwing([str(index) for index in range(1, 15)], body=(8.65, 3.9), overall=(10.3, 6.0))},
        "electronic_ic_soic_8_timer_555_timer_texas_instruments_tlc555cd": {"dimensions": {"length": 4.9, "width": 3.9, "height": 1.75}, "pins": ["GND", "TRIG", "OUT", "RESET", "CTRL", "THRESH", "DISCH", "VCC"], "drawing": _gullwing([str(index) for index in range(1, 9)])},
        "electronic_ic_soic_8_timer_555_timer_texas_instruments_ne555dr": {"dimensions": {"length": 4.9, "width": 3.9, "height": 1.75}, "pins": ["GND", "TRIG", "OUT", "RESET", "CTRL", "THRESH", "DISCH", "VCC"], "drawing": _gullwing([str(index) for index in range(1, 9)])},
        "electronic_ic_soic_8_logic_comparator_lm393": {"dimensions": {"length": 4.9, "width": 3.9, "height": 1.75}, "pins": ["OUT1", "IN1_MINUS", "IN1_PLUS", "GND", "IN2_PLUS", "IN2_MINUS", "OUT2", "VCC"], "drawing": _gullwing([str(index) for index in range(1, 9)])},
        "electronic_ic_soic_8_sensor_hall_effect_current_sensor_allegro_acs712": {"dimensions": {"length": 4.9, "width": 3.9, "height": 1.75}, "pins": ["IP_PLUS", "IP_PLUS", "IP_MINUS", "IP_MINUS", "GND", "FILTER", "VIOUT", "VCC"], "drawing": _gullwing([str(index) for index in range(1, 9)])},
        "electronic_ic_soic_8_capacitive_touch_controller_controller_infineon_cy8cmbr3102": {"dimensions": {"length": 4.9, "width": 3.9, "height": 1.75}, "pins": [str(index) for index in range(1, 9)], "drawing": _gullwing([str(index) for index in range(1, 9)])},
        "electronic_ic_so_16_audio_audio_player_my_semi_my1690x_16s": {"dimensions": {"length": 10.0, "width": 4.0, "height": 1.75}, "pins": [str(index) for index in range(1, 17)], "drawing": _gullwing([str(index) for index in range(1, 17)], body=(10.0, 4.0), overall=(12.0, 6.0))},
        "electronic_ic_msop_8_amplifier_operational_amplifier_sg_micro_sgm358yms_tr": {"dimensions": {"length": 3.0, "width": 3.0, "height": 1.1}, "pins": ["OUTA", "INA_MINUS", "INA_PLUS", "V_MINUS", "INB_PLUS", "INB_MINUS", "OUTB", "V_PLUS"], "drawing": _gullwing([str(index) for index in range(1, 9)], body=(3.0, 3.0), overall=(4.8, 3.2), pad_width=0.42)},
        "electronic_ic_msop_8_amplifier_thermocouple_amplifier_texas_instruments_ad8495armz": {"dimensions": {"length": 3.0, "width": 3.0, "height": 1.1}, "pins": [str(index) for index in range(1, 9)], "drawing": _gullwing([str(index) for index in range(1, 9)], body=(3.0, 3.0), overall=(4.8, 3.2), pad_width=0.42)},
        "electronic_ic_msop_10_converter_usb_to_serial_converter_wch_ch340e": {"dimensions": {"length": 3.0, "width": 3.0, "height": 1.1}, "pins": [str(index) for index in range(1, 11)], "drawing": _gullwing([str(index) for index in range(1, 11)], body=(3.0, 3.0), overall=(4.8, 3.2), pad_width=0.42)},
        "electronic_ic_tssop_16_converter_analog_to_digital_converter_texas_instruments_ads1219ipw": {"dimensions": {"length": 5.0, "width": 4.4, "height": 1.2}, "pins": ["AIN0", "AIN1", "AIN2", "AIN3", "AVDD", "DVDD", "DGND", "AGND", "SDA", "SCL", "ADDR0", "ADDR1", "DRDY", "START", "REFOUT", "REFIN"], "drawing": _gullwing([str(index) for index in range(1, 17)], body=(5.0, 4.4), overall=(6.4, 6.4), pad_width=0.28)},
        "electronic_ic_tssop_16_logic_io_expander_texas_instruments_pca9554pw": {"dimensions": {"length": 5.0, "width": 4.4, "height": 1.2}, "pins": ["A0", "A1", "A2", "P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "INT", "SCL", "SDA", "VSS", "VDD"], "drawing": _gullwing([str(index) for index in range(1, 17)], body=(5.0, 4.4), overall=(6.4, 6.4), pad_width=0.28)},
        "electronic_ic_vssop_10_power_monitor_current_monitor_texas_instruments_ina228": {"dimensions": {"length": 4.9, "width": 3.0, "height": 1.1}, "pins": ["IN_PLUS", "IN_MINUS", "VBUS", "GND", "VCC", "SCL", "SDA", "ALERT", "A0", "A1"], "drawing": _gullwing([str(index) for index in range(1, 11)], body=(4.9, 3.0), overall=(6.2, 4.0), pad_width=0.3)},
        "electronic_ic_sot_23_8_power_monitor_current_monitor_texas_instruments_ina219": {"dimensions": {"length": 2.9, "width": 1.6, "height": 1.1}, "pins": ["IN_PLUS", "IN_MINUS", "VCC", "GND", "SCL", "SDA", "A0", "A1"], "drawing": _gullwing([str(index) for index in range(1, 9)], body=(2.9, 1.6), overall=(4.2, 3.2), pad_width=0.42)},
        "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_diodes_ap2112k_3_3": {"dimensions": {"length": 2.9, "width": 1.6, "height": 1.1}, "pins": ["VIN", "GND", "EN", "NC", "VOUT"], "drawing": _gullwing([str(index) for index in range(1, 6)], body=(2.9, 1.6), overall=(4.2, 3.2), pad_width=0.42)},
        "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_se5218": {"dimensions": {"length": 2.9, "width": 1.6, "height": 1.1}, "pins": [str(index) for index in range(1, 6)], "drawing": _gullwing([str(index) for index in range(1, 6)], body=(2.9, 1.6), overall=(4.2, 3.2), pad_width=0.42)},
        "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_se5218alg": {"dimensions": {"length": 2.9, "width": 1.6, "height": 1.1}, "pins": [str(index) for index in range(1, 6)], "drawing": _gullwing([str(index) for index in range(1, 6)], body=(2.9, 1.6), overall=(4.2, 3.2), pad_width=0.42)},
        "electronic_ic_sot_23_3_power_management_shunt_regulator_texas_instruments_tl431acdbz": {"dimensions": {"length": 2.9, "width": 1.6, "height": 1.1}, "pins": ["REF", "ANODE", "CATHODE"], "drawing": _gullwing([str(index) for index in range(1, 4)], body=(2.9, 1.6), overall=(4.2, 3.2), pad_width=0.42)},
    }
    for current, data in exact.items():
        if current in extras_dict:
            _set(extras_dict[current], dimensions=data["dimensions"], pins=data["pins"], drawing=data["drawing"], reference=data.get("reference"), url=data.get("url"))

    # Package-accurate sensor bodies and the small sensor/module families.
    sensors = {
        "electronic_sensor_imu_lga_24_st_lsm9ds1tr": (3.5, 3.0, ["VDD", "GND"] * 12, _module(3.5, 3.0, [str(i) for i in range(1, 25)])),
        "electronic_sensor_air_quality_lga_20_ams_ccs811b_jopr": (3.0, 3.0, [str(i) for i in range(1, 21)], _module(3.0, 3.0, [str(i) for i in range(1, 21)])),
        "electronic_sensor_light_proximity_ch_6_liteon_ltr_507als_01": (2.65, 2.0, [str(i) for i in range(1, 9)], _module(2.65, 2.0, [str(i) for i in range(1, 9)], body=(1.8, 1.3))),
        "electronic_sensor_pressure_temperature_lga_10_bosch_bmp388": (2.0, 2.0, [str(i) for i in range(1, 11)], _module(2.0, 2.0, [str(i) for i in range(1, 11)], body=(1.8, 1.8))),
        "electronic_sensor_accelerometer_lga_14_analog_devices_adxl345": (5.0, 3.0, ["VDD", "GND", "ST1", "GND", "VDDIO", "NC", "NC", "INT2", "INT1", "GND", "RES", "SCL_SCLK", "SDA_SDI", "SDO"], _module(5.0, 3.0, [str(i) for i in range(1, 15)])),
        "electronic_sensor_accelerometer_lga_16_st_lis3dhtr": (3.0, 3.0, [str(i) for i in range(1, 17)], _module(3.0, 3.0, [str(i) for i in range(1, 17)])),
        "electronic_sensor_accelerometer_lga_16_st_lis3dhtr": (3.0, 3.0, [str(i) for i in range(1, 17)], _module(3.0, 3.0, [str(i) for i in range(1, 17)])),
        "electronic_sensor_particulate_matter_module_bosch_bmv080": (20.0, 5.5, ["VDDL", "VSSA", "VDDA", "VSSD", "PS", "SCK", "MOSI", "MISO", "CS", "VDDD"], _module(20.0, 5.5, [str(i) for i in range(1, 11)], body=(4.4, 3.0))),
    }
    for current, (length, width, pins, drawing) in sensors.items():
        if current in extras_dict:
            _set(extras_dict[current], dimensions={"length": length, "width": width}, pins=pins, drawing=drawing)
    modules = {
        "electronic_sensor_gnss_module_quectel_l86_m33": (18.4, 18.4, 18, True),
        "electronic_sensor_gnss_module_u_blox_sam_m8q": (15.5, 15.5, 20, True),
        "electronic_sensor_gnss_module_u_blox_dan_f10n": (20.0, 20.0, 56, True),
        "electronic_sensor_gnss_module_u_blox_neo_f10n": (12.2, 16.0, 24, False),
    }
    for current, (length, width, count, antenna) in modules.items():
        if current in extras_dict:
            _set(extras_dict[current], dimensions={"length": length, "width": width}, pins=[str(i) for i in range(1, count + 1)], drawing=_module(length, width, [str(i) for i in range(1, count + 1)], antenna=antenna))

    # Simple, physically legible two-terminal and protection parts.
    simple = {
        "electronic_diode_schottky_sod_323_infineon_bat20j": ({"length": 1.7, "width": 1.25}, ["K", "A"], _gullwing(["1", "2"], body=(1.7, 1.25), overall=(2.8, 1.8), pad_width=0.55)),
        "electronic_diode_switching_sod_323_onsemi_1n4148ws": ({"length": 1.7, "width": 1.25}, ["K", "A"], _gullwing(["1", "2"], body=(1.7, 1.25), overall=(2.8, 1.8), pad_width=0.55)),
        "electronic_diode_tvs_array_sot_143_nxp_prtr5v0u2x": ({"length": 3.0, "width": 1.3}, ["GND", "IO1", "IO2", "VCC"], _qfn(["1", "2", "3", "4"], body=(2.9, 1.3), overall=(3.8, 2.5))),
        "electronic_capacitor_0603_2200_pico_farad": ({"length": 1.6, "width": 0.8}, ["1", "2"], _gullwing(["1", "2"], body=(1.0, 0.8), overall=(1.8, 1.3), pad_width=0.5)),
        "electronic_inductor_0603_30_ohm": ({"length": 1.6, "width": 0.8}, ["1", "2"], _gullwing(["1", "2"], body=(1.0, 0.8), overall=(1.8, 1.3), pad_width=0.5)),
        "electronic_inductor_0603_470_ohm": ({"length": 1.6, "width": 0.8}, ["1", "2"], _gullwing(["1", "2"], body=(1.0, 0.8), overall=(1.8, 1.3), pad_width=0.5)),
        "electronic_fuse_0805_resettable_6_volt_0_5_amp_1_amp": ({"length": 2.0, "width": 1.25}, ["1", "2"], _gullwing(["1", "2"], body=(1.6, 1.0), overall=(2.3, 1.5), pad_width=0.55)),
        "electronic_fuse_1210_resettable_6_volt_2_amp_4_amp": ({"length": 3.2, "width": 2.5}, ["1", "2"], _gullwing(["1", "2"], body=(2.6, 1.9), overall=(3.6, 2.8), pad_width=0.75)),
        "electronic_battery_coin_cell_6_8_mm_maxell_ml414h": ({"length": 6.8, "width": 6.8}, ["+", "-"], {"overall": [6.8, 6.8], "body": [6.8, 6.8], "pins": [["+", "left", -2.5, 0, 1.2, 1.2], ["-", "right", 2.5, 0, 1.2, 1.2]], "circles": [[0, 0, 2.6]], "pin_one": [-2.5, 0]}),
        "electronic_transformer_surface_mount_usb_coilcraft_rfcmf1220100m4t": ({"length": 12.0, "width": 10.0}, [str(i) for i in range(1, 5)], _gullwing([str(i) for i in range(1, 5)], body=(8.0, 8.0), overall=(12.0, 10.0), pad_width=0.8)),
    }
    for current, (dimensions, pins, drawing) in simple.items():
        if current in extras_dict:
            _set(extras_dict[current], dimensions=dimensions, pins=pins, drawing=drawing)

    # Switches: body, actuator and real terminal count are more informative
    # than the former blank rectangle, even where the exact fitted suffix is
    # intentionally still unresolved.
    switches = {
        "electronic_switch_tactile_surface_mount_pts810": (6.0, 6.0, 4),
        "electronic_switch_tactile_through_hole_gt_tc026x_hxxx_lx": (6.0, 6.0, 4),
        "electronic_switch_tactile_surface_mount_omron_b3fs_100xp": (8.0, 8.0, 4),
        "electronic_switch_tactile_surface_mount_ck_pts636": (6.0, 6.0, 4),
        "electronic_switch_tactile_surface_mount_alps_alpine_skr_k": (3.9, 2.9, 4),
        "electronic_switch_tactile_surface_mount_alps_alpine_skrpace010": (4.2, 3.2, 4),
        "electronic_switch_navigation_surface_mount_7_5_mm": (7.5, 7.5, 5),
        "electronic_switch_navigation_surface_mount_9_9_mm": (9.9, 9.9, 5),
        "electronic_switch_roller_encoder_through_hole_roller_encoder_switch": (12.0, 10.0, 5),
    }
    for current, (length, width, count) in switches.items():
        if current not in extras_dict:
            continue
        if count == 5:
            drawing = {"overall": [length, width], "body": [length * .72, width * .72], "pins": [["1", "left", -length / 2 + .35, -width * .25, .7, .7], ["2", "left", -length / 2 + .35, width * .25, .7, .7], ["3", "right", length / 2 - .35, width * .25, .7, .7], ["4", "right", length / 2 - .35, -width * .25, .7, .7], ["5", "bottom", 0, -width / 2 + .35, .7, .7]], "circles": [[0, 0, min(length, width) * .18]]}
        else:
            drawing = _button(length, width, count)
        _set(extras_dict[current], dimensions={"length": length, "width": width}, pins=[str(i) for i in range(1, count + 1)], drawing=drawing)

    # Connectors are intentionally top-view oriented so their contact pattern
    # is visible in the main part image.
    connectors = {
        "electronic_connector_header_1_27_mm_pitch_surface_mount_10_pin_socket_header_female_5x2_1_27_mm_smd": (7.0, 5.5, 10),
        "electronic_connector_micro_sd_push_push_micro_sd_external_pin": (15.0, 11.0, 10),
        "electronic_connector_micro_sd_friction_fit_micro_sd_friction_fit": (15.0, 11.0, 10),
        "electronic_connector_jst_1_25_mm_pitch_surface_mount_6_pin_locking_jst_smd_1_25_mm_6_locking": (9.5, 4.5, 6),
        "electronic_connector_audio_jack_surface_mount_right_angle_trrs_3_5_mm_audio_jack_3_5_mm_trrs": (13.5, 6.5, 5),
        "electronic_connector_terminal_block_3_5_mm_pitch_through_hole_3_pin_screw_terminal_1x03_p3_5_mm": (11.0, 8.0, 3),
        "electronic_connector_gnss_header_2_mm_pitch_surface_mount_20_pin_plug_in_conn_02x10_gnss_plug_in_header": (20.0, 5.0, 20),
        "electronic_connector_rf_cable_assembly_ipx_to_sma_ipx_connector_with_sma": (30.0, 5.0, 2),
    }
    for current, (length, width, count) in connectors.items():
        if current not in extras_dict:
            continue
        if current.endswith("header_female_5x2_1_27_mm_smd"):
            pins = []
            for row, y in enumerate((-1.1, 1.1)):
                for column in range(5):
                    pins.append([str(row * 5 + column + 1), "bottom", -2.54 + column * 1.27, y, .7, .7])
            drawing = {"overall": [length, width], "body": [6.6, 4.4], "pins": pins, "pin_one": [-2.54, -1.1]}
        elif current.startswith("electronic_connector_micro_sd"):
            pins = [[str(index + 1), "bottom", -4.5 + index * 1.0, -width / 2 + .35, .55, .7] for index in range(count)]
            drawing = {"overall": [length, width], "body": [length - 1.0, width - 1.0], "pins": pins, "boxes": [[0, 0.7, length * .72, width * .36]], "pin_one": [-4.5, -width / 2 + .35]}
        elif current.startswith("electronic_connector_terminal_block"):
            pins = [[str(index + 1), "bottom", -3.5 + index * 3.5, -width / 2 + .45, 1.2, .8] for index in range(count)]
            drawing = {"overall": [length, width], "body": [length - .6, width - .6], "pins": pins, "circles": [[-3.5 + index * 3.5, 0, 1.0] for index in range(count)]}
        elif current.startswith("electronic_connector_audio_jack"):
            drawing = {"overall": [length, width], "body": [length, width], "pins": [[str(index + 1), "bottom", -4.0 + index * 2.0, -width / 2 + .35, .8, .7] for index in range(count)], "circles": [[length * .25, 0, width * .28]]}
        elif current.startswith("electronic_connector_rf_cable"):
            drawing = {"overall": [length, width], "body": [length * .45, width], "pins": [["1", "left", -length / 2 + .5, 0, 1.0, 1.0], ["2", "right", length / 2 - .5, 0, 1.0, 1.0]], "circles": [[length * .28, 0, width * .48]]}
        else:
            drawing = {"overall": [length, width], "body": [length - .5, width - .5], "pins": [[str(index + 1), "bottom", -length / 2 + 1.0 + index * (length - 2.0) / max(count - 1, 1), -width / 2 + .35, .6, .7] for index in range(count)]}
        _set(extras_dict[current], dimensions={"length": length, "width": width}, pins=[str(i) for i in range(1, count + 1)], drawing=drawing)

