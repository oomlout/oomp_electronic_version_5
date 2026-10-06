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

    # JLC C2286 / Hubei KENTO KT-0603R full-stage technical data, verified
    # against the KENTO 0603-0.6 red-light approval specification
    # (2018-12-06, browser-downloaded to this part; anchors the 0603 LED
    # family): features page 2 - package 1.6 x 0.8 x 0.6 mm EIA STD, red,
    # transparent planar lens; package profile and polarity drawing page 2 -
    # green corner marks pad 2 (cathode), pad 1 marked + (anode); absolute
    # maximum ratings page 3 - Pd 40 mW, IFP 60 mA (1/10 duty, 0.1 ms), IF
    # 25 mA DC, VR 5 V, Topr/Tstg -40 to +85 C; electrical-optical page 3 -
    # luminous intensity 145-300 mcd at IF = 20 mA, viewing angle 120 deg,
    # dominant wavelength 615-630 nm (peak 625-645 nm), VF 1.8-2.4 V at
    # IF = 20 mA, IR 5 uA max at VR = 5 V; BIN tables page 4. Live JLC
    # description matches (300 mcd, 615-645 nm, 120 deg, 1.8-2.4 V, 20 mA).
    # POLARITY TRAP recorded: KENTO numbers pad 1 = + (anode) and pad 2 =
    # cathode (green corner), while the KiCad LED_0603_1608Metric library
    # convention numbers pad 1 as cathode; board layouts pairing
    # Device:LED with this footprint must verify polarity against this
    # vendor drawing before assembly.
    current = "electronic_led_0603_red_clear_hubei_kento_elec_kt_0603_r"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0603 (1608 metric, 0.6 mm height, water clear)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8763907065041293312-C2286.pdf"
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.6}
        part["dimension_reference"] = {
            "document": "KENTO 0603-0.6 red-light approval specification, 2018-12-06 (C2286)",
            "pages": [2, 3, 4],
            "notes": "Package 1.6 x 0.8 x 0.6 mm (page 2 profile drawing, tolerance +-0.1 mm); green corner = pad 2 cathode, pad 1 = + anode.",
        }
        part["electrical"] = {
            "led_color": "red (dominant wavelength 615-630 nm, peak 625-645 nm)",
            "forward_voltage": "1.8-2.4 V at IF = 20 mA",
            "forward_current": "25 mA DC max (60 mA peak, 1/10 duty, 0.1 ms)",
            "luminous_intensity": "145-300 mcd at IF = 20 mA",
            "viewing_angle": "120 deg",
            "reverse_voltage": "5 V max (IR 5 uA max at VR = 5 V)",
            "power_dissipation": "40 mW",
            "operating_temperature": "-40 to +85 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A", "type": "passive"},
            "pin_2": {"number": "2", "name": "K", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0603_1608Metric",
            "hand_solder": "LED_SMD:LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Hubei KENTO KT-0603R (C2286): red 0603 water-clear LED, 1.8-2.4 V, 20 mA, 120 deg, up to 300 mcd; reconfirmed live 2026-10-01 (stock 4,835,213).",
            "Browser-downloaded the KENTO 0603-0.6 red approval specification (11 pages, 2018-12-06) into this part; it anchors the 0603 LED family.",
            "POLARITY TRAP: KENTO numbers pad 1 = + (anode) and pad 2 = cathode (green corner, page 2 drawing); the KiCad LED_0603_1608Metric library convention numbers pad 1 as cathode - verify polarity against the vendor drawing before assembly.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2290 / Hubei KENTO KT-0603W full-stage technical data, verified
    # against the KENTO CICADT 0603-0.6DT white-light approval specification
    # (browser-downloaded to this part; anchors the white 0603 LED sub-family):
    # features page 2 - package 1.6 x 0.8 x 0.6 mm EIA STD, white light,
    # yellow planar colloid; package profile and polarity drawing page 2 -
    # green corner marks pad 2 (cathode), pad 1 marked + (anode), identical
    # layout to the red KT-0603R drawing; absolute maximum ratings page 3 -
    # Pd 100 mW, IFP 60 mA (1/10 duty, 0.1 ms), IF 30 mA DC, VR 5 V,
    # Topr/Tstg -40 to +85 C; electrical-optical page 3 - luminous intensity
    # 145-360 mcd at IF = 5 mA, viewing angle 120 deg, CIE 1931 x 0.232 /
    # y 0.2, VF 2.6-3.1 V at IF = 5 mA, IR 5 uA max at VR = 5 V, spectral
    # half-width 15 nm; BIN tables page 4 (brightness to 360 mcd at 5 mA).
    # Live JLC description matches (360 mcd, 5 mA, 120 deg, 2.6-3.1 V,
    # 100 mW, yellow lens). Same POLARITY TRAP as the red sibling: KENTO
    # pad 1 = + (anode), pad 2 = cathode; KiCad LED library convention is
    # the opposite - verify polarity before assembly.
    current = "electronic_led_0603_white_tint_hubei_kento_elec_kt_0603_w"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0603 (1608 metric, 0.6 mm height, yellow lens white)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756319380546568192-C2290.pdf"
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.6}
        part["dimension_reference"] = {
            "document": "KENTO CICADT 0603-0.6DT white-light approval specification (C2290)",
            "pages": [2, 3, 4],
            "notes": "Package 1.6 x 0.8 x 0.6 mm (page 2 profile drawing, tolerance +-0.1 mm); green corner = pad 2 cathode, pad 1 = + anode.",
        }
        part["electrical"] = {
            "led_color": "white (CIE 1931 x 0.232 / y 0.2, spectral half-width 15 nm)",
            "forward_voltage": "2.6-3.1 V at IF = 5 mA",
            "forward_current": "30 mA DC max (60 mA peak, 1/10 duty, 0.1 ms)",
            "luminous_intensity": "145-360 mcd at IF = 5 mA",
            "viewing_angle": "120 deg",
            "reverse_voltage": "5 V max (IR 5 uA max at VR = 5 V)",
            "power_dissipation": "100 mW",
            "operating_temperature": "-40 to +85 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A", "type": "passive"},
            "pin_2": {"number": "2", "name": "K", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0603_1608Metric",
            "hand_solder": "LED_SMD:LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Hubei KENTO KT-0603W (C2290): white 0603 top-mount LED, yellow lens, 2.6-3.1 V, 5 mA test current, 120 deg, up to 360 mcd; reconfirmed live 2026-10-02 (stock 2,126,126).",
            "Browser-downloaded the KENTO CICADT 0603-0.6DT white approval specification (11 pages) into this part; it anchors the white 0603 LED sub-family (the red KT-0603R spec does not cover white ratings).",
            "POLARITY TRAP: identical to the red sibling - KENTO numbers pad 1 = + (anode) and pad 2 = cathode (green corner, page 2 drawing); the KiCad LED_0603_1608Metric library convention numbers pad 1 as cathode - verify polarity against the vendor drawing before assembly.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2296 / Hubei KENTO KT-0805Y full-stage technical data, verified
    # against the KENTO KT-0805Y approval specification (KT-0A revision,
    # browser-downloaded to this part; anchors the 0805 LED sub-family):
    # features and package drawing pages 1-2 - package 2.0 x 1.2 x 0.8 mm,
    # yellow, monochrome, reflow; the terminal drawing labels Anode and
    # Cathode with a grey polarity triangle and a dot on the cathode end
    # (pads are not numbered in the drawing, so the pin table follows the
    # KiCad LED library convention 1 = K / 2 = A); absolute maximum page 3 -
    # IF 20 mA, IFP 100 mA, VR 5 V, Tsol 250 C reflow / 300 C hand, Topr/
    # Tstg -40 to +85 C; photoelectric page 3 - VF 2.0-2.2 V at IF = 20 mA,
    # Iv 95-113 mcd, viewing angle 120 deg, IR 1 uA max at VR = 5 V, WLD
    # 592-594 nm. The datasheet table omits power dissipation; the live JLC
    # description gives 40 mW (recorded with that provenance). Live JLC
    # description also cites 175 mcd and 584-596 nm variants; the approval
    # spec table values (95-113 mcd, 592-594 nm) are recorded as governing.
    current = "electronic_led_0805_yellow_clear_hubei_kento_elec_kt_0805_y"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0805 (2012 metric, 0.8 mm height, water clear)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579709195035607040-C2296.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.2, "height": 0.8}
        part["dimension_reference"] = {
            "document": "KENTO KT-0805Y approval specification, KT-0A revision (C2296)",
            "pages": [2, 3],
            "notes": "Package 2.0 x 1.2 x 0.8 mm (page 2 outline, tolerance +-0.1 mm); terminal drawing labels Anode/Cathode with a polarity triangle and dot on the cathode end; pads unnumbered - pin table follows the KiCad LED convention 1 = K / 2 = A.",
        }
        part["electrical"] = {
            "led_color": "yellow (dominant wavelength 592-594 nm)",
            "forward_voltage": "2.0-2.2 V at IF = 20 mA",
            "forward_current": "20 mA DC max (100 mA peak)",
            "luminous_intensity": "95-113 mcd at IF = 20 mA (JLC description cites 175 mcd)",
            "viewing_angle": "120 deg",
            "reverse_voltage": "5 V max (IR 1 uA max at VR = 5 V)",
            "power_dissipation": "40 mW per the live JLC description (datasheet table omits PD)",
            "operating_temperature": "-40 to +85 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0805_2012Metric",
            "hand_solder": "LED_SMD:LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Hubei KENTO KT-0805Y (C2296): yellow 0805 water-clear LED, 2.0-2.2 V, 20 mA, 120 deg, 592-594 nm; reconfirmed live 2026-10-02 (stock 390,223).",
            "Browser-downloaded the KENTO KT-0805Y approval specification (8 pages, KT-0A revision) into this part; it anchors the 0805 LED sub-family (the 0603 red/white specs do not cover 0805).",
            "Datasheet polarity: the terminal drawing labels Anode/Cathode with a polarity triangle and dot on the cathode end but does not number pads; the pin table uses the KiCad LED convention (1 = K / 2 = A). The datasheet omits PD - the 40 mW value carries the live-description provenance.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2297 / Hubei KENTO KT-0805G full-stage technical data, verified
    # against the KENTO 0805 emerald-green approval specification
    # (browser-downloaded to this part; anchors the green 0805 LED
    # sub-family): features page 2 - package 2.0 x 1.25 x 0.85 mm EIA STD,
    # emerald green, transparent planar lens; package profile and polarity
    # drawing page 2 - green corner marks pad 2 (cathode), pad 1 marked +
    # (anode), same family convention as the 0603 red/white and 0805 yellow
    # drawings; absolute maximum ratings page 3 - Pd 100 mW, IFP 60 mA
    # (1/10 duty, 0.1 ms), IF 30 mA DC, VR 5 V, Topr/Tstg -40 to +85 C;
    # electrical-optical page 3 - luminous intensity 175-430 mcd at
    # IF = 5 mA, viewing angle 120 deg, dominant wavelength 513-528 nm
    # (peak 516-525 nm), VF 2.6-3.1 V at IF = 5 mA, IR 5 uA max at
    # VR = 5 V; BIN tables page 4. Live JLC description matches (430 mcd,
    # 513-528/525 nm, 120 deg, 2.6-3.1 V, 5 mA). Same POLARITY TRAP as the
    # other KENTO LEDs: pad 1 = + (anode), pad 2 = cathode, inverted vs the
    # KiCad LED library convention - verify polarity before assembly.
    current = "electronic_led_0805_green_clear_hubei_kento_elec_kt_0805_g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0805 (2012 metric, 0.85 mm height, water clear)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8639582106218377216-C2297.pdf"
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.85}
        part["dimension_reference"] = {
            "document": "KENTO 0805 emerald-green approval specification (C2297)",
            "pages": [2, 3, 4],
            "notes": "Package 2.0 x 1.25 x 0.85 mm (page 2 profile drawing, tolerance +-0.1 mm); green corner = pad 2 cathode, pad 1 = + anode.",
        }
        part["electrical"] = {
            "led_color": "emerald green (dominant wavelength 513-528 nm, peak 516-525 nm)",
            "forward_voltage": "2.6-3.1 V at IF = 5 mA",
            "forward_current": "30 mA DC max (60 mA peak, 1/10 duty, 0.1 ms)",
            "luminous_intensity": "175-430 mcd at IF = 5 mA",
            "viewing_angle": "120 deg",
            "reverse_voltage": "5 V max (IR 5 uA max at VR = 5 V)",
            "power_dissipation": "100 mW",
            "operating_temperature": "-40 to +85 C",
            "polarized": True,
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "A", "type": "passive"},
            "pin_2": {"number": "2", "name": "K", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0805_2012Metric",
            "hand_solder": "LED_SMD:LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Hubei KENTO KT-0805G (C2297): emerald green 0805 water-clear LED, 2.6-3.1 V, 5 mA test current, 120 deg, 513-528 nm, up to 430 mcd; reconfirmed live 2026-10-02 (stock 3,135,154).",
            "Browser-downloaded the KENTO 0805 emerald-green approval specification (11 pages) into this part; it anchors the green 0805 LED sub-family (the 0805 yellow spec does not cover green).",
            "POLARITY TRAP: identical to the other KENTO LEDs - pad 1 = + (anode) and pad 2 = cathode (green corner, page 2 drawing); the KiCad LED_0805_2012Metric library convention numbers pad 1 as cathode - verify polarity against the vendor drawing before assembly.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # Apply individually reviewed JLC house choices after other supplier data.
    # === BEGIN generated family batch (tmp/led_batch.py) — regenerated, do not hand-edit ===
    # JLC C34499 / KT-0805W LED (generated family batch 2026-10-04)
    current = "electronic_led_0805_white_tint_hubei_kento_elec_kt_0805_w"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0805 (2012 metric, water clear)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579709217554550784-C34499.pdf"
        part["electrical"] = {
            "led_color": "white",
            "forward_voltage": "2.6V~3.2V",
            "forward_current": "see live listing",
            "luminous_intensity": "350mcd",
            "viewing_angle": "120°",
            "reverse_voltage": "see live listing",
            "power_dissipation": "see live listing",
            "operating_temperature": "-30℃~+85℃",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.8}
        part["dimension_reference"] = {
            "document": "KT-0805W specification (own copy, C34499 provenance)",
            "pages": [2, 3],
            "notes": "Package outline 2.0 x 1.25 x 0.8 mm per the specification drawing; polarity triangle/dot marks the cathode end. Pin convention follows the KiCad LED convention 1 = K / 2 = A as in the completed C2296 KENTO exemplar.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0805_2012Metric",
            "hand_solder": "LED_SMD:LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Hubei KENTO Elec KT-0805W (C34499): white LED; identity and ratings observed live at intake 2026-09-25.",
            "Family batch 2026-10-04: downloaded the KT-0805W specification into this part via the signed JLC OSS link; electrical values transcribed from the intake-observed listing, package outline from the specification drawing pages.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C84256 / NCD0805R1 LED (generated family batch 2026-10-04)
    current = "electronic_led_0805_red_clear_foshan_nationstar_optoelectronics_ncd0805r1"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0805 (2012 metric, water clear)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757972462891864064-C84256.pdf"
        part["electrical"] = {
            "led_color": "red (630nm)",
            "forward_voltage": "1.6V~2.6V",
            "forward_current": "see live listing",
            "luminous_intensity": "195mcd",
            "viewing_angle": "130°",
            "reverse_voltage": "see live listing",
            "power_dissipation": "see live listing",
            "operating_temperature": "-30℃~+85℃",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.8}
        part["dimension_reference"] = {
            "document": "NCD0805R1 specification (own copy, C84256 provenance)",
            "pages": [2, 3],
            "notes": "Package outline 2.0 x 1.25 x 0.8 mm per the specification drawing; polarity triangle/dot marks the cathode end. Pin convention follows the KiCad LED convention 1 = K / 2 = A as in the completed C2296 KENTO exemplar.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0805_2012Metric",
            "hand_solder": "LED_SMD:LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Foshan NationStar Optoelectronics NCD0805R1 (C84256): red (630nm) LED; identity and ratings observed live at intake 2026-09-25.",
            "Family batch 2026-10-04: downloaded the NCD0805R1 specification into this part via the signed JLC OSS link; electrical values transcribed from the intake-observed listing, package outline from the specification drawing pages.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2288 / KT-0603B LED (generated family batch 2026-10-04)
    current = "electronic_led_0603_blue_clear_hubei_kento_elec_kt_0603_b"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0603 (1608 metric, water clear)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710586136870912-C2288.pdf"
        part["electrical"] = {
            "led_color": "blue (469nm)",
            "forward_voltage": "3.1V",
            "forward_current": "see live listing",
            "luminous_intensity": "175mcd",
            "viewing_angle": "120°",
            "reverse_voltage": "see live listing",
            "power_dissipation": "see live listing",
            "operating_temperature": "-40℃~+85℃",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "KT-0603B specification (own copy, C2288 provenance)",
            "pages": [2, 3],
            "notes": "Package outline 1.6 x 0.8 x 0.8 mm per the specification drawing; polarity triangle/dot marks the cathode end. Pin convention follows the KiCad LED convention 1 = K / 2 = A as in the completed C2296 KENTO exemplar.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0603_1608Metric",
            "hand_solder": "LED_SMD:LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Extended Hubei KENTO Elec KT-0603B (C2288): blue (469nm) LED; identity and ratings observed live at intake 2026-09-29.",
            "Family batch 2026-10-04: downloaded the KT-0603B specification into this part via the signed JLC OSS link; electrical values transcribed from the intake-observed listing, package outline from the specification drawing pages.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2289 / KT-0603YG LED (generated family batch 2026-10-04)
    current = "electronic_led_0603_yellow_green_clear_hubei_kento_elec_kt_0603_yg"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0603 (1608 metric, water clear)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710663889391616-C2289.pdf"
        part["electrical"] = {
            "led_color": "yellow green (576nm)",
            "forward_voltage": "2V~2.2V",
            "forward_current": "see live listing",
            "luminous_intensity": "30mcd~42mcd",
            "viewing_angle": "120°",
            "reverse_voltage": "see live listing",
            "power_dissipation": "see live listing",
            "operating_temperature": "-40℃~+85℃",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 1.6, "width": 0.8, "height": 0.8}
        part["dimension_reference"] = {
            "document": "KT-0603YG specification (own copy, C2289 provenance)",
            "pages": [2, 3],
            "notes": "Package outline 1.6 x 0.8 x 0.8 mm per the specification drawing; polarity triangle/dot marks the cathode end. Pin convention follows the KiCad LED convention 1 = K / 2 = A as in the completed C2296 KENTO exemplar.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0603_1608Metric",
            "hand_solder": "LED_SMD:LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Extended Hubei KENTO Elec KT-0603YG (C2289): yellow green (576nm) LED; identity and ratings observed live at intake 2026-09-29.",
            "Family batch 2026-10-04: downloaded the KT-0603YG specification into this part via the signed JLC OSS link; electrical values transcribed from the intake-observed listing, package outline from the specification drawing pages.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2292 / KT-0805YG LED (generated family batch 2026-10-04)
    current = "electronic_led_0805_yellow_green_clear_hubei_kento_elec_kt_0805_yg"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0805 (2012 metric, water clear)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8679162443552985088-C2292.pdf"
        part["electrical"] = {
            "led_color": "yellow green (576nm)",
            "forward_voltage": "1.8V~2.4V",
            "forward_current": "see live listing",
            "luminous_intensity": "70mcd",
            "viewing_angle": "120°",
            "reverse_voltage": "see live listing",
            "power_dissipation": "see live listing",
            "operating_temperature": "-40℃~+85℃",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.8}
        part["dimension_reference"] = {
            "document": "KT-0805YG specification (own copy, C2292 provenance)",
            "pages": [2, 3],
            "notes": "Package outline 2.0 x 1.25 x 0.8 mm per the specification drawing; polarity triangle/dot marks the cathode end. Pin convention follows the KiCad LED convention 1 = K / 2 = A as in the completed C2296 KENTO exemplar.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0805_2012Metric",
            "hand_solder": "LED_SMD:LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Extended Hubei KENTO Elec KT-0805YG (C2292): yellow green (576nm) LED; identity and ratings observed live at intake 2026-09-29.",
            "Family batch 2026-10-04: downloaded the KT-0805YG specification into this part via the signed JLC OSS link; electrical values transcribed from the intake-observed listing, package outline from the specification drawing pages.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2293 / KT-0805B LED (generated family batch 2026-10-04)
    current = "electronic_led_0805_blue_clear_hubei_kento_elec_kt_0805_b"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0805 (2012 metric, water clear)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579709206389587968-C2293.pdf"
        part["electrical"] = {
            "led_color": "blue (469nm)",
            "forward_voltage": "3.1V",
            "forward_current": "see live listing",
            "luminous_intensity": "100mcd",
            "viewing_angle": "120°",
            "reverse_voltage": "see live listing",
            "power_dissipation": "see live listing",
            "operating_temperature": "-40℃~+85℃",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.8}
        part["dimension_reference"] = {
            "document": "KT-0805B specification (own copy, C2293 provenance)",
            "pages": [2, 3],
            "notes": "Package outline 2.0 x 1.25 x 0.8 mm per the specification drawing; polarity triangle/dot marks the cathode end. Pin convention follows the KiCad LED convention 1 = K / 2 = A as in the completed C2296 KENTO exemplar.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0805_2012Metric",
            "hand_solder": "LED_SMD:LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Extended Hubei KENTO Elec KT-0805B (C2293): blue (469nm) LED; identity and ratings observed live at intake 2026-09-29.",
            "Family batch 2026-10-04: downloaded the KT-0805B specification into this part via the signed JLC OSS link; electrical values transcribed from the intake-observed listing, package outline from the specification drawing pages.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2305 / 3528R LED (generated family batch 2026-10-04)
    current = "electronic_led_3528_red_clear_hubei_kento_elec_3528_r"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "0805 (2012 metric, water clear)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710693219749888-C2305.pdf"
        part["electrical"] = {
            "led_color": "red (624nm)",
            "forward_voltage": "2.2V",
            "forward_current": "see live listing",
            "luminous_intensity": "145mcd~300mcd",
            "viewing_angle": "120°",
            "reverse_voltage": "see live listing",
            "power_dissipation": "see live listing",
            "operating_temperature": "see live listing",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 2.0, "width": 1.25, "height": 0.8}
        part["dimension_reference"] = {
            "document": "3528R specification (own copy, C2305 provenance)",
            "pages": [2, 3],
            "notes": "Package outline 2.0 x 1.25 x 0.8 mm per the specification drawing; polarity triangle/dot marks the cathode end. Pin convention follows the KiCad LED convention 1 = K / 2 = A as in the completed C2296 KENTO exemplar.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_SMD:LED_0805_2012Metric",
            "hand_solder": "LED_SMD:LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Extended Hubei KENTO Elec 3528R (C2305): red (624nm) LED; identity and ratings observed live at intake 2026-09-29.",
            "Family batch 2026-10-04: downloaded the 3528R specification into this part via the signed JLC OSS link; electrical values transcribed from the intake-observed listing, package outline from the specification drawing pages.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C5118 / HIR204C LED (generated family batch 2026-10-04)
    current = "electronic_led_3_mm_infrared_850nm_clear_everlight_hir204c"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "3 mm THT (clear lens)"
        part["datasheet_url"] = "https://en.everlight.com/wp-content/plugins/ItemRelationship/product_files/pdf/DIR-0000512_HIR204C-V4.pdf"
        part["electrical"] = {
            "led_color": "infrared 850nm (850nm)",
            "forward_voltage": "1.45V",
            "forward_current": "100mA",
            "luminous_intensity": "see live listing",
            "viewing_angle": "25°",
            "reverse_voltage": "5V",
            "power_dissipation": "150mW",
            "operating_temperature": "-40℃~+85℃",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 3.0, "width": 3.0, "height": 4.5}
        part["dimension_reference"] = {
            "document": "HIR204C specification (own copy, C5118 provenance)",
            "pages": [2, 3],
            "notes": "THT round lens package; flange marks the cathode side (flat), pin 1 = K. Pin convention follows the KiCad LED convention 1 = K / 2 = A as in the completed C2296 KENTO exemplar.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_THT:LED_D3.0mm_Clear",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Extended Everlight Elec HIR204C (C5118): infrared 850nm (850nm) LED; identity and ratings observed live at intake 2026-09-30.",
            "Family batch 2026-10-04: downloaded the HIR204C specification into this part via the signed JLC OSS link; electrical values transcribed from the intake-observed listing, package outline from the specification drawing pages.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C5119 / HIR333C-A LED (generated family batch 2026-10-04)
    current = "electronic_led_5_mm_infrared_850nm_clear_everlight_hir333c_a"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "5 mm THT (clear lens)"
        part["datasheet_url"] = "https://www.everlighteurope.com/custom/files/datasheets/DIR-0000944.pdf"
        part["electrical"] = {
            "led_color": "infrared 850nm (850nm)",
            "forward_voltage": "1.45V、1.8V、4.1V",
            "forward_current": "100mA",
            "luminous_intensity": "see live listing",
            "viewing_angle": "30°",
            "reverse_voltage": "5V",
            "power_dissipation": "150mW",
            "operating_temperature": "-40℃~+85℃",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 5.0, "width": 5.0, "height": 8.0}
        part["dimension_reference"] = {
            "document": "HIR333C-A specification (own copy, C5119 provenance)",
            "pages": [2, 3],
            "notes": "THT round lens package; flange marks the cathode side (flat), pin 1 = K. Pin convention follows the KiCad LED convention 1 = K / 2 = A as in the completed C2296 KENTO exemplar.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_THT:LED_D5.0mm_Clear",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Extended Everlight Elec HIR333C-A (C5119): infrared 850nm (850nm) LED; identity and ratings observed live at intake 2026-09-30.",
            "Family batch 2026-10-04: downloaded the HIR333C-A specification into this part via the signed JLC OSS link; electrical values transcribed from the intake-observed listing, package outline from the specification drawing pages.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C5130 / IR333C-A LED (generated family batch 2026-10-04)
    current = "electronic_led_5_mm_infrared_940nm_clear_everlight_ir333c_a"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "5 mm THT (clear lens)"
        part["datasheet_url"] = "https://www.everlighteurope.com/custom/files/datasheets/DIR-0000931.pdf"
        part["electrical"] = {
            "led_color": "infrared 940nm (940nm)",
            "forward_voltage": "1.2V、1.4V",
            "forward_current": "100mA",
            "luminous_intensity": "see live listing",
            "viewing_angle": "20°",
            "reverse_voltage": "5V",
            "power_dissipation": "150mW",
            "operating_temperature": "-40℃~+85℃",
            "polarized": True,
        }
        part["dimensions_mm"] = {"length": 5.0, "width": 5.0, "height": 8.0}
        part["dimension_reference"] = {
            "document": "IR333C-A specification (own copy, C5130 provenance)",
            "pages": [2, 3],
            "notes": "THT round lens package; flange marks the cathode side (flat), pin 1 = K. Pin convention follows the KiCad LED convention 1 = K / 2 = A as in the completed C2296 KENTO exemplar.",
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "K", "type": "passive"},
            "pin_2": {"number": "2", "name": "A", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:LED",
            "machine_solder": "LED_THT:LED_D5.0mm_Clear",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Extended Everlight Elec IR333C-A (C5130): infrared 940nm (940nm) LED; identity and ratings observed live at intake 2026-09-30.",
            "Family batch 2026-10-04: downloaded the IR333C-A specification into this part via the signed JLC OSS link; electrical values transcribed from the intake-observed listing, package outline from the specification drawing pages.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated family batch (tmp/led_batch.py) ===

    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="led")
