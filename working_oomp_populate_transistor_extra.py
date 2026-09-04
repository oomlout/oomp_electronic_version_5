def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "JSMSEMI"
        part["part_number_manufacturer"] = "SS8050"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["part_number_lcsc"] = "C916392"
        part["product_url"] = "https://www.lcsc.com/product-detail/C916392.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C916392.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 2.4}
        part["dimension_reference"] = {"document": "JSMICRO SS8050", "pages": [1, 4]}
        part["pins"] = {}
        for number, name in [["1", "base"], ["2", "emitter"], ["3", "collector"]]:
            part["pins"]["pin_" + number] = {"number": number, "name": name, "type": "signal"}
        part["package_drawing"] = {
            "overall": [2.9, 2.4], "body": [2.9, 1.3],
            "pins": [["1", "bottom", -.95, -.925, .4, .55],
                     ["2", "bottom", .95, -.925, .4, .55],
                     ["3", "top", 0, .925, .4, .55]],
        }
        part["kicad"] = {"symbol": "Transistor_BJT:SS8050", "machine_solder": "Package_TO_SOT_SMD:SOT-23W", "hand_solder": "Package_TO_SOT_SMD:SOT-23W_Handsoldering"}

    current = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_2n7002"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Generic"
        part["part_number"] = "2N7002"
        part["part_number_generic"] = "2N7002"
        part["generic_match"] = {
            "values": ["2N7002"],
            "symbols": ["Transistor_FET:2N7002"],
            "footprints": [
                "Package_TO_SOT_SMD:SOT-23",
                "Package_TO_SOT_SMD:SOT-23_Handsoldering",
                "SOT-23",
                "SOT-23_Handsoldering",
            ],
        }
        part["product_url"] = "https://www.nexperia.com/product/2N7002"
        part["datasheet_url"] = "https://assets.nexperia.com/documents/data-sheet/2N7002.pdf"
        part["datasheet_note"] = "Representative Nexperia datasheet for this generic family. Check the exact manufacturer variant before relying on electrical or thermal limits."
        part["package_name"] = "SOT-23 / TO-236AB"
        part["electrical"] = {
            "device_type": "N-channel enhancement-mode MOSFET",
            "maximum_drain_source_voltage": "60 V",
            "representative_maximum_drain_current": "300 mA",
            "representative_maximum_gate_source_voltage": "+/-30 V",
            "representative_maximum_power_dissipation": "830 mW",
            "representative_gate_threshold_voltage": "1.0 to 2.5 V",
            "reference_device": "Nexperia 2N7002 Rev. 7",
        }
        part["transistor_dimensions_mm"] = {
            "body_length_nominal": 2.9,
            "body_length_minimum": 2.8,
            "body_length_maximum": 3.0,
            "body_width_nominal": 1.3,
            "body_width_minimum": 1.2,
            "body_width_maximum": 1.4,
            "overall_width_nominal": 2.3,
            "overall_width_minimum": 2.1,
            "overall_width_maximum": 2.5,
            "body_height_nominal": 1.0,
            "body_height_minimum": 0.9,
            "body_height_maximum": 1.1,
            "lead_width_nominal": 0.43,
            "lead_width_minimum": 0.38,
            "lead_width_maximum": 0.48,
            "lead_length_nominal": 0.3,
            "lead_length_minimum": 0.15,
            "lead_length_maximum": 0.45,
            "terminal_projection_nominal": 0.5,
            "pin_pitch": 0.95,
            "outer_pin_pitch": 1.9,
        }
        part["dimensions_mm"] = {"length": 2.9, "width": 2.3}
        part["pins"] = {}
        transistor_pins = [
            ["1", "gate", "input"],
            ["2", "source", "passive"],
            ["3", "drain", "passive"],
        ]
        for pin in transistor_pins:
            part["pins"]["pin_" + pin[0]] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        part["package_drawing"] = {
            "overall": [2.9, 2.3],
            "body": [2.9, 1.3],
            "pins": [
                ["1", "bottom", -0.95, -0.9, 0.43, 0.5],
                ["2", "bottom", 0.95, -0.9, 0.43, 0.5],
                ["3", "top", 0, 0.9, 0.43, 0.5],
            ],
            "pin_one": [-1.1, -0.42],
        }
        part["dimension_reference"] = {
            "document": "Nexperia 2N7002 Rev. 7",
            "pages": [1, 2, 8, 9],
        }
        part["research_notes"] = [
            "This is a generic 2N7002 family entry, not an exact orderable manufacturer variant.",
            "The Nexperia sheet is retained as the representative browser-verified source for the standard SOT-23 outline and pins 1 gate, 2 source and 3 drain.",
            "Current, gate-voltage, resistance and thermal limits vary between manufacturers; representative Nexperia values are labelled as such and must not replace an exact design choice.",
            "No LCSC number is attached because an LCSC code identifies one exact manufacturer variant; the following ledger item selects one separately.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
        part["kicad"] = {
            "symbol": "Transistor_FET:2N7002",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
        }

    current = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_300_milliamp_nexperia_2n7002_215"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Nexperia"
        part["part_number_manufacturer"] = "2N7002,215"
        part["part_number_manufacturer_nexperia"] = "2N7002,215"
        part["part_number_lcsc"] = "C65189"
        part["product_url"] = "https://www.lcsc.com/product-detail/C65189.html"
        part["manufacturer_product_url"] = "https://www.nexperia.com/product/2N7002"
        part["datasheet_url"] = "https://assets.nexperia.com/documents/data-sheet/2N7002.pdf"
        part["package_name_manufacturer"] = "SOT23 / TO-236AB"
        part["marking_code"] = "12%"
        part["marking_note"] = "% is the manufacturing-site code, not a literal package marking."
        part["electrical"] = {
            "device_type": "N-channel enhancement-mode Trench MOSFET",
            "maximum_drain_source_voltage": "60 V at Tj 25 to 150 C",
            "maximum_continuous_drain_current": "300 mA at VGS 10 V, solder point 25 C",
            "maximum_gate_source_voltage": "+/-30 V",
            "maximum_power_dissipation": "830 mW at solder point 25 C; derate with temperature",
            "gate_threshold_voltage": "1.0 to 2.5 V at ID 250 uA, Tj 25 C",
            "maximum_on_resistance_at_10_v": "5 ohm at ID 500 mA, Tj 25 C",
            "maximum_on_resistance_at_4_5_v": "5.3 ohm at ID 75 mA, Tj 25 C",
            "operating_junction_temperature": "-65 to +150 C",
        }
        part["transistor_dimensions_mm"] = {
            "body_length_nominal": 2.9,
            "body_length_minimum": 2.8,
            "body_length_maximum": 3.0,
            "body_width_nominal": 1.3,
            "body_width_minimum": 1.2,
            "body_width_maximum": 1.4,
            "overall_width_nominal": 2.3,
            "overall_width_minimum": 2.1,
            "overall_width_maximum": 2.5,
            "body_height_nominal": 1.0,
            "body_height_minimum": 0.9,
            "body_height_maximum": 1.1,
            "lead_width_nominal": 0.43,
            "lead_width_minimum": 0.38,
            "lead_width_maximum": 0.48,
            "lead_length_nominal": 0.3,
            "lead_length_minimum": 0.15,
            "lead_length_maximum": 0.45,
            "terminal_projection_nominal": 0.5,
            "pin_pitch": 0.95,
            "outer_pin_pitch": 1.9,
        }
        part["dimensions_mm"] = {"length": 2.9, "width": 2.3}
        part["pins"] = {}
        transistor_pins = [
            ["1", "gate", "input"],
            ["2", "source", "passive"],
            ["3", "drain", "passive"],
        ]
        for pin in transistor_pins:
            part["pins"]["pin_" + pin[0]] = {
                "number": pin[0], "name": pin[1], "type": pin[2],
            }
        part["package_drawing"] = {
            "overall": [2.9, 2.3],
            "body": [2.9, 1.3],
            "pins": [
                ["1", "bottom", -0.95, -0.9, 0.43, 0.5],
                ["2", "bottom", 0.95, -0.9, 0.43, 0.5],
                ["3", "top", 0, 0.9, 0.43, 0.5],
            ],
            "pin_one": [-1.1, -0.42],
        }
        part["dimension_reference"] = {
            "document": "Nexperia 2N7002 Rev. 7",
            "pages": [1, 2, 5, 8],
        }
        part["research_notes"] = [
            "LCSC C65189 explicitly identifies Nexperia 2N7002,215 in SOT-23; 560,000 pieces were in stock at browser verification on 2026-09-03, not a permanent availability guarantee.",
            "Nexperia lists 2N7002,215 as an active orderable part, 12NC 934003470215, supplied on a 3,000-piece reel.",
            "C551410 is the different 2N7002,235 packing suffix and was out of stock at verification; it is not assigned to this part.",
            "The datasheet confirms pins 1 gate, 2 source, 3 drain and the SOT23 outline. Solder-point ratings must not be interpreted as ambient-temperature ratings.",
        ]
        part["file_copy"] = [{
            "file_source": f"parts_source/{current}/datasheet.pdf",
            "file_destination": "datasheet.pdf",
        }]
        part["kicad"] = {
            "symbol": "Transistor_FET:2N7002",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
        }

    current = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_bss138"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "Generic"
        part["part_number"] = "BSS138"
        part["part_number_generic"] = "BSS138"
        part["generic_match"] = {
            "values": ["BSS138"],
            "symbols": ["Transistor_FET:BSS138"],
            "footprints": [
                "Package_TO_SOT_SMD:SOT-23",
                "Package_TO_SOT_SMD:SOT-23_Handsoldering",
                "SOT-23",
                "SOT-23_Handsoldering",
            ],
        }
        part["datasheet_url"] = "https://www.onsemi.com/pdf/datasheet/bss138-d.pdf"
        part["datasheet_note"] = "Representative onsemi datasheet for this generic family. Check the exact manufacturer variant before relying on electrical, thermal or package tolerance limits."
        part["package_name"] = "SOT-23 / TO-236"
        part["electrical"] = {
            "device_type": "N-channel enhancement-mode MOSFET",
            "maximum_drain_source_voltage": "50 V",
            "representative_maximum_drain_current": "220 mA at ambient 25 C; subject to PCB thermal conditions",
            "representative_maximum_gate_source_voltage": "+/-20 V",
            "representative_maximum_power_dissipation": "360 mW at ambient 25 C; subject to PCB thermal conditions",
            "representative_gate_threshold_voltage": "0.8 to 1.5 V at ID 1 mA",
            "reference_device": "onsemi BSS138 Rev. 7, April 2024",
        }
        part["transistor_dimensions_mm"] = {
            "body_length_nominal": 2.9,
            "body_length_minimum": 2.8,
            "body_length_maximum": 3.04,
            "body_width_nominal": 1.3,
            "body_width_minimum": 1.2,
            "body_width_maximum": 1.4,
            "overall_width_nominal": 2.4,
            "overall_width_minimum": 2.1,
            "overall_width_maximum": 2.64,
            "body_height_nominal": 1.0,
            "body_height_minimum": 0.89,
            "body_height_maximum": 1.11,
            "lead_width_nominal": 0.44,
            "lead_width_minimum": 0.37,
            "lead_width_maximum": 0.50,
            "lead_length_nominal": 0.43,
            "lead_length_minimum": 0.30,
            "lead_length_maximum": 0.55,
            "terminal_projection_nominal": 0.55,
            "pin_pitch": 0.95,
            "outer_pin_pitch": 1.9,
        }
        part["dimensions_mm"] = {"length": 2.9, "width": 2.4}
        part["pins"] = {}
        transistor_pins = [
            ["1", "gate", "input"],
            ["2", "source", "passive"],
            ["3", "drain", "passive"],
        ]
        for pin in transistor_pins:
            part["pins"]["pin_" + pin[0]] = {
                "number": pin[0], "name": pin[1], "type": pin[2],
            }
        part["package_drawing"] = {
            "overall": [2.9, 2.4],
            "body": [2.9, 1.3],
            "pins": [
                ["1", "bottom", -0.95, -0.925, 0.44, 0.55],
                ["2", "bottom", 0.95, -0.925, 0.44, 0.55],
                ["3", "top", 0, 0.925, 0.44, 0.55],
            ],
            "pin_one": [-1.1, -0.42],
        }
        part["dimension_reference"] = {
            "document": "onsemi BSS138 Rev. 7; CASE 318 Issue AU, 14 August 2024",
            "pages": [1, 2, 6],
        }
        part["research_notes"] = [
            "Generic BSS138 family identity; no manufacturer or supplier code is implied.",
            "The onsemi datasheet linked by KiCad's official BSS138 symbol is the representative reference, with pins 1 gate, 2 source and 3 drain.",
            "The actual CASE 318 drawing gives 2.90 by 1.30 mm body, 2.40 mm overall width and 0.44 mm nominal lead width; these are not copied from a different manufacturer's SOT-23 outline.",
            "No LCSC number is attached to the generic family; the following ledger row selects an exact manufacturer and ordering suffix separately.",
        ]
        part["file_copy"] = [{
            "file_source": f"parts_source/{current}/datasheet.pdf",
            "file_destination": "datasheet.pdf",
        }]
        part["kicad"] = {
            "symbol": "Transistor_FET:BSS138",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
        }

    current = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_220_milliamp_onsemi_bss138"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "onsemi"
        part["part_number_manufacturer"] = "BSS138"
        part["part_number_manufacturer_onsemi"] = "BSS138"
        part["part_number_lcsc"] = "C52895"
        part["product_url"] = "https://www.lcsc.com/product-detail/C52895.html"
        part["datasheet_url"] = "https://www.onsemi.com/pdf/datasheet/bss138-d.pdf"
        part["package_name_manufacturer"] = "SOT-23-3 / CASE 318"
        part["marking_code"] = "SS"
        part["marking_note"] = "SS is the device code; the additional M denotes a date code and the microdot denotes the Pb-free package."
        part["electrical"] = {
            "device_type": "N-channel enhancement-mode MOSFET",
            "maximum_drain_source_voltage": "50 V",
            "maximum_continuous_drain_current": "220 mA at ambient 25 C; subject to PCB thermal conditions",
            "maximum_gate_source_voltage": "+/-20 V",
            "maximum_power_dissipation": "360 mW at ambient 25 C; derate 2.8 mW/C above 25 C",
            "thermal_resistance_junction_to_ambient": "350 C/W on a minimum pad",
            "gate_threshold_voltage": "0.8 to 1.5 V at ID 1 mA, ambient 25 C",
            "maximum_on_resistance_at_10_v": "3.5 ohm at ID 220 mA, ambient 25 C",
            "maximum_on_resistance_at_4_5_v": "6.0 ohm at ID 220 mA, ambient 25 C",
            "operating_junction_temperature": "-55 to +150 C",
        }
        part["transistor_dimensions_mm"] = {
            "body_length_nominal": 2.9,
            "body_length_minimum": 2.8,
            "body_length_maximum": 3.04,
            "body_width_nominal": 1.3,
            "body_width_minimum": 1.2,
            "body_width_maximum": 1.4,
            "overall_width_nominal": 2.4,
            "overall_width_minimum": 2.1,
            "overall_width_maximum": 2.64,
            "body_height_nominal": 1.0,
            "body_height_minimum": 0.89,
            "body_height_maximum": 1.11,
            "lead_width_nominal": 0.44,
            "lead_width_minimum": 0.37,
            "lead_width_maximum": 0.50,
            "lead_length_nominal": 0.43,
            "lead_length_minimum": 0.30,
            "lead_length_maximum": 0.55,
            "terminal_projection_nominal": 0.55,
            "pin_pitch": 0.95,
            "outer_pin_pitch": 1.9,
        }
        part["dimensions_mm"] = {"length": 2.9, "width": 2.4}
        part["pins"] = {}
        transistor_pins = [
            ["1", "gate", "input"],
            ["2", "source", "passive"],
            ["3", "drain", "passive"],
        ]
        for pin in transistor_pins:
            part["pins"]["pin_" + pin[0]] = {
                "number": pin[0], "name": pin[1], "type": pin[2],
            }
        part["package_drawing"] = {
            "overall": [2.9, 2.4],
            "body": [2.9, 1.3],
            "pins": [
                ["1", "bottom", -0.95, -0.925, 0.44, 0.55],
                ["2", "bottom", 0.95, -0.925, 0.44, 0.55],
                ["3", "top", 0, 0.925, 0.44, 0.55],
            ],
            "pin_one": [-1.1, -0.42],
        }
        part["dimension_reference"] = {
            "document": "onsemi BSS138 Rev. 7; CASE 318 Issue AU, 14 August 2024",
            "pages": [1, 2, 3, 6],
        }
        part["research_notes"] = [
            "LCSC C52895 identifies onsemi BSS138 in SOT-23, with 42,980 pieces in stock at browser verification on 2026-09-03; stock is not a permanent guarantee.",
            "The manufacturer ordering table explicitly lists BSS138 as well as BSS138-G. This part is the bare BSS138 orderable device from the supplier listing, not an assumed suffix variant.",
            "The manufacturer sheet confirms 50 V, 220 mA and pins 1 gate, 2 source, 3 drain; its minimum-pad thermal conditions qualify the current and power limits.",
            "The downloaded CASE 318 outline is the same verified manufacturer drawing used as the reference for the separate generic BSS138 entry.",
        ]
        part["file_copy"] = [{
            "file_source": f"parts_source/{current}/datasheet.pdf",
            "file_destination": "datasheet.pdf",
        }]
        part["kicad"] = {
            "symbol": "Transistor_FET:BSS138",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
        }

    current = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_300_milliamp_cbi_mmbt7002k"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "MMBT7002K"
        extras_dict[current]["part_number_manufacturer_cbi"] = "MMBT7002K"
        extras_dict[current]["part_number_lcsc"] = "C2879714"
        extras_dict[current]["manufacturer"] = "CBI"
        extras_dict[current]["manufacturer_full"] = "China Base International"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C2879714.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C2879714.pdf"
        extras_dict[current]["package_name_manufacturer"] = "SOT-23"
        extras_dict[current]["electrical"] = {
            "maximum_drain_source_voltage": "60 V",
            "maximum_gate_source_voltage": "+/-20 V",
            "maximum_continuous_drain_current": "300 mA",
            "maximum_pulsed_drain_current": "800 mA",
            "maximum_power_dissipation": "350 mW",
            "gate_threshold_voltage": "1 to 2.5 V",
            "maximum_on_resistance_at_10_v": "3 ohm",
            "maximum_on_resistance_at_4_5_v": "4 ohm",
            "minimum_forward_transconductance": "80 mS",
            "input_capacitance": "50 pF",
            "output_capacitance": "25 pF",
            "reverse_transfer_capacitance": "5 pF",
            "operating_temperature": "-55 to +150 C",
            "electrostatic_discharge_protection": "2 kV",
        }
        extras_dict[current]["transistor_dimensions_mm"] = {
            "body_length_nominal": 2.9,
            "body_length_minimum": 2.7,
            "body_length_maximum": 3.1,
            "body_width_nominal": 1.425,
            "body_width_minimum": 1.2,
            "body_width_maximum": 1.65,
            "overall_width_nominal": 2.6,
            "overall_width_minimum": 2.2,
            "overall_width_maximum": 3.0,
            "body_height_minimum": 0.95,
            "body_height_maximum": 1.4,
            "lead_width_minimum": 0.35,
            "lead_width_maximum": 0.5,
            "lead_length_minimum": 0.2,
            "lead_length_maximum": 0.5,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 2.9,
            "width": 2.6,
        }
        extras_dict[current]["pins"] = {}
        transistor_pins = [
            ["1", "gate", "input"],
            ["2", "source", "passive"],
            ["3", "drain", "passive"],
        ]
        for pin_index in range(len(transistor_pins)):
            pin = transistor_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The current Bus Pirate fitted BOM identifies CBI (China Base International) MMBT7002K.",
            "The exact LCSC listing is C2879714 and specifies an N-channel 60 V, 300 mA SOT-23 MOSFET.",
            "The CBI datasheet assigns pin 1 gate, pin 2 source, and pin 3 drain.",
            "The historical project supplier URL now resolves to Diodes Incorporated BSS138-13-F, C526482, so it is not used as identity evidence.",
            "The KiCad 50 V and 0.22 A description belongs to the old BSS138 metadata and is superseded by the fitted MMBT7002K datasheet.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_transistor_sot_363_6_bipolar_pnp_dual_general_purpose_40_volt_200_milliamp_cbi_mmdt3906dw"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "MMDT3906DW"
        extras_dict[current]["part_number_manufacturer_cbi"] = "MMDT3906DW"
        extras_dict[current]["part_number_lcsc"] = "C2836075"
        extras_dict[current]["manufacturer"] = "CBI"
        extras_dict[current]["manufacturer_full"] = "China Base International"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C2836075.html"
        extras_dict[current]["datasheet_url"] = "https://www.lcsc.com/datasheet/C2836075.pdf"
        extras_dict[current]["package_name_manufacturer"] = "SOT-363"
        extras_dict[current]["marking_code"] = "K3N"
        extras_dict[current]["electrical"] = {
            "transistor_configuration": "two internally isolated PNP transistors",
            "maximum_collector_base_voltage": "-40 V",
            "maximum_collector_emitter_voltage": "-40 V",
            "maximum_emitter_base_voltage": "-5 V",
            "maximum_continuous_collector_current": "-200 mA",
            "maximum_collector_power_dissipation": "200 mW",
            "thermal_resistance_junction_to_ambient": "625 C/W",
            "maximum_junction_temperature": "150 C",
            "storage_temperature": "-55 to +150 C",
            "dc_current_gain_at_10_ma": "100 to 300",
            "minimum_transition_frequency": "250 MHz",
            "maximum_collector_output_capacitance": "4.5 pF",
            "maximum_noise_figure": "4 dB",
        }
        extras_dict[current]["transistor_dimensions_mm"] = {
            "body_length_nominal": 2.1,
            "body_length_minimum": 2.0,
            "body_length_maximum": 2.2,
            "body_width_nominal": 1.25,
            "body_width_minimum": 1.15,
            "body_width_maximum": 1.35,
            "overall_width_nominal": 2.3,
            "overall_width_minimum": 2.15,
            "overall_width_maximum": 2.45,
            "body_height_nominal": 1.0,
            "body_height_minimum": 0.9,
            "body_height_maximum": 1.1,
            "lead_width_nominal": 0.25,
            "lead_width_minimum": 0.15,
            "lead_width_maximum": 0.35,
            "lead_length_nominal": 0.36,
            "lead_length_minimum": 0.26,
            "lead_length_maximum": 0.46,
            "pin_pitch": 0.65,
        }
        extras_dict[current]["package_dimensions_manufacturer_mm"] = {
            "A_minimum": 0.9,
            "A_maximum": 1.1,
            "A1_minimum": 0.0,
            "A1_maximum": 0.1,
            "A2_minimum": 0.9,
            "A2_maximum": 1.0,
            "b_minimum": 0.15,
            "b_maximum": 0.35,
            "c_minimum": 0.08,
            "c_maximum": 0.15,
            "D_minimum": 2.0,
            "D_maximum": 2.2,
            "E_minimum": 1.15,
            "E_maximum": 1.35,
            "E1_minimum": 2.15,
            "E1_maximum": 2.45,
            "e_typical": 0.65,
            "e1_minimum": 1.2,
            "e1_maximum": 1.4,
            "L_reference": 0.525,
            "L1_minimum": 0.26,
            "L1_maximum": 0.46,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 2.1,
            "width": 2.3,
        }
        extras_dict[current]["pins"] = {}
        transistor_pins = [
            ["1", "emitter_1", "passive"],
            ["2", "base_1", "input"],
            ["3", "collector_2", "passive"],
            ["4", "emitter_2", "passive"],
            ["5", "base_2", "input"],
            ["6", "collector_1", "passive"],
        ]
        for pin_index in range(len(transistor_pins)):
            pin = transistor_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate fitted BOM names CBI MMDT3906 in SOT-363 as the general-purpose dual PNP device.",
            "The project CBI supplier link resolves to exact MPN MMDT3906DW, LCSC C2836075, with K3N marking.",
            "The other supplier links on the project page are alternate manufacturers and are not mixed into this exact identity.",
            "The CBI datasheet confirms two isolated PNP transistors, 40 V, 200 mA and the EBCEBC top-view pinout.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_transistor_sot_363_6_bipolar_pnp_dual_matched_pair_45_volt_100_milliamp_diodes_incorporated_bcm857bs_7_f"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "BCM857BS-7-F"
        extras_dict[current]["part_number_manufacturer_diodes_incorporated"] = "BCM857BS-7-F"
        extras_dict[current]["part_number_lcsc"] = "C105896"
        extras_dict[current]["manufacturer"] = "Diodes Incorporated"
        extras_dict[current]["manufacturer_full"] = "Diodes Incorporated"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C105896.html"
        extras_dict[current]["manufacturer_product_url"] = "https://www.diodes.com/part/view/BCM857BS"
        extras_dict[current]["datasheet_url"] = "https://www.mouser.com/datasheet/2/115/BCM857BS-959446.pdf"
        extras_dict[current]["package_name_manufacturer"] = "SOT363"
        extras_dict[current]["marking_code"] = "M3W"
        extras_dict[current]["electrical"] = {
            "transistor_configuration": "two internally isolated intrinsically matched PNP transistors",
            "maximum_collector_base_voltage": "-50 V",
            "maximum_collector_emitter_voltage": "-45 V",
            "maximum_emitter_base_voltage": "-5 V",
            "maximum_continuous_collector_current": "-100 mA",
            "maximum_peak_collector_current": "-200 mA",
            "maximum_peak_base_current": "-200 mA",
            "maximum_total_power_dissipation": "200 mW",
            "thermal_resistance_junction_to_ambient": "625 C/W",
            "operating_and_storage_temperature": "-65 to +150 C",
            "dc_current_gain": "220 to 475 at VCE -5 V and IC -2 mA",
            "minimum_current_gain_matching_ratio": "0.9",
            "maximum_base_emitter_voltage_difference": "2 mV",
            "minimum_gain_bandwidth_product": "100 MHz",
            "human_body_model_esd": "4 kV",
            "machine_model_esd": "400 V",
        }
        extras_dict[current]["transistor_dimensions_mm"] = {
            "body_length_nominal": 2.15,
            "body_length_minimum": 1.8,
            "body_length_maximum": 2.2,
            "body_width_nominal": 1.3,
            "body_width_minimum": 1.15,
            "body_width_maximum": 1.35,
            "overall_width_nominal": 2.1,
            "overall_width_minimum": 2.0,
            "overall_width_maximum": 2.2,
            "body_height_nominal": 1.0,
            "body_height_minimum": 0.9,
            "body_height_maximum": 1.0,
            "lead_width_nominal": 0.25,
            "lead_width_minimum": 0.1,
            "lead_width_maximum": 0.3,
            "lead_length_nominal": 0.3,
            "lead_length_minimum": 0.25,
            "lead_length_maximum": 0.4,
            "pin_pitch": 0.65,
        }
        extras_dict[current]["package_dimensions_manufacturer_mm"] = {
            "A_minimum": 0.1,
            "A_maximum": 0.3,
            "A_typical": 0.25,
            "B_minimum": 1.15,
            "B_maximum": 1.35,
            "B_typical": 1.3,
            "C_minimum": 2.0,
            "C_maximum": 2.2,
            "C_typical": 2.1,
            "D_typical": 0.65,
            "F_minimum": 0.4,
            "F_maximum": 0.45,
            "F_typical": 0.425,
            "H_minimum": 1.8,
            "H_maximum": 2.2,
            "H_typical": 2.15,
            "J_minimum": 0.0,
            "J_maximum": 0.1,
            "J_typical": 0.05,
            "K_minimum": 0.9,
            "K_maximum": 1.0,
            "K_typical": 1.0,
            "L_minimum": 0.25,
            "L_maximum": 0.4,
            "L_typical": 0.3,
            "M_minimum": 0.1,
            "M_maximum": 0.22,
            "M_typical": 0.11,
        }
        extras_dict[current]["recommended_pad_layout_mm"] = {
            "overall_height_z": 2.5,
            "inner_gap_g": 1.3,
            "pad_width_x": 0.42,
            "pad_height_y": 0.6,
            "row_pitch_c1": 1.9,
            "pin_pitch_c2": 0.65,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 2.15,
            "width": 2.1,
        }
        extras_dict[current]["pins"] = {}
        transistor_pins = [
            ["1", "emitter_1", "passive"],
            ["2", "base_1", "input"],
            ["3", "collector_2", "passive"],
            ["4", "emitter_2", "passive"],
            ["5", "base_2", "input"],
            ["6", "collector_1", "passive"],
        ]
        for pin_index in range(len(transistor_pins)):
            pin = transistor_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The current Bus Pirate fitted BOM specifies DIODES BCM857 in SOT-363 as the dual PNP matched pair.",
            "The Bus Pirate transistor notes identify BCM857BS-7-F as the Diodes Incorporated ordering option for Q401.",
            "The exact LCSC listing is C105896 and confirms BCM857BS-7-F, SOT-363, 45 V, 100 mA and 200 mW.",
            "The manufacturer datasheet guarantees 10 percent hFE matching and a maximum 2 mV VBE difference.",
            "The manufacturer top-view pinout is 1 emitter 1, 2 base 1, 3 collector 2, 4 emitter 2, 5 base 2, 6 collector 1.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    current = "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "BC2301T-2.8A"
        extras_dict[current]["part_number_manufacturer_cbi"] = "BC2301T-2.8A"
        extras_dict[current]["manufacturer"] = "CBI"
        extras_dict[current]["manufacturer_full"] = "Heyuan China Base Electronics Technology Co., Ltd."
        extras_dict[current]["project_bom_name"] = "BC2301(2.8A)"
        extras_dict[current]["product_url"] = "https://docs.buspirate.com/docs/hardware/bp5rev10/components/transistors-fets/"
        extras_dict[current]["datasheet_url"] = "https://alltransistors.com/adv/pdfview.php?doc=bc2301t-2.8a.pdf&dire=_cn_cbi"
        extras_dict[current]["package_name_manufacturer"] = "SOT-523"
        extras_dict[current]["electrical"] = {
            "maximum_drain_source_voltage": "-20 V",
            "maximum_gate_source_voltage": "+/-8 V",
            "maximum_continuous_drain_current": "-2.8 A",
            "maximum_pulsed_drain_current": "-4.8 A",
            "maximum_continuous_source_drain_diode_current": "-0.72 A",
            "maximum_power_dissipation": "350 mW",
            "thermal_resistance_junction_to_ambient": "357 C/W",
            "gate_threshold_voltage": "-0.4 to -1 V",
            "maximum_on_resistance_at_4_5_v": "120 milliohm",
            "maximum_on_resistance_at_2_5_v": "170 milliohm",
            "forward_transconductance": "6.5 S",
            "input_capacitance": "405 pF",
            "output_capacitance": "75 pF",
            "reverse_transfer_capacitance": "55 pF",
            "typical_total_gate_charge_at_4_5_v": "5.5 nC",
            "operating_temperature": "-55 to +150 C",
        }
        extras_dict[current]["transistor_dimensions_mm"] = {
            "body_length_nominal": 1.6,
            "body_length_minimum": 1.5,
            "body_length_maximum": 1.7,
            "body_width_nominal": 0.775,
            "body_width_minimum": 0.7,
            "body_width_maximum": 0.85,
            "overall_width_nominal": 1.6,
            "overall_width_minimum": 1.45,
            "overall_width_maximum": 1.75,
            "body_height_minimum": 0.6,
            "body_height_maximum": 0.8,
            "lead_width_minimum": 0.16,
            "lead_width_maximum": 0.4,
            "lead_length_minimum": 0.16,
            "lead_length_maximum": 0.36,
        }
        extras_dict[current]["dimensions_mm"] = {
            "length": 1.6,
            "width": 1.6,
        }
        extras_dict[current]["pins"] = {}
        transistor_pins = [
            ["1", "gate", "input"],
            ["2", "source", "passive"],
            ["3", "drain", "passive"],
        ]
        for pin_index in range(len(transistor_pins)):
            pin = transistor_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        extras_dict[current]["research_notes"] = [
            "The current Bus Pirate fitted BOM calls the part CBI BC2301(2.8A); the exact special-order CBI datasheet identifies it as BC2301T-2.8A in SOT-523.",
            "The Bus Pirate component notes explicitly say the SOT-523 SI2301-family device may be a special-order package and name CBI BC2301 as the example.",
            "The public LCSC C2928245 BC2301(2.8A) listing and PDF are the physically larger SOT-23 package, so that LCSC number is deliberately not attached to this SOT-523 part.",
            "The historical project supplier URL resolves to Nexperia PMV65XP,215 in SOT-23 and is not used as identity evidence.",
            "The CBI SOT-523 datasheet assigns pin 1 gate, pin 2 source, and pin 3 drain.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
