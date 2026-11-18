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
        part["oomp_datasheet_common_with"] = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_2n7002"
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
        part["oomp_datasheet_common_with"] = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_220_milliamp_onsemi_bss138"
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

    # JLC C2145 / Jiangsu Changjing MMBT5551 full-stage technical data,
    # verified against the Changjing MMBT5551 SOT-23 specification (March
    # 2013, browser-downloaded to this part; anchors the high-voltage NPN
    # SOT-23 family): maximum ratings page 1 - VCBO 180 V, VCEO 160 V,
    # VEBO 6 V, IC 600 mA, PC 300 mW, RthJA 416 C/W, Tj 150 C, Tstg -55 to
    # +150 C; electrical characteristics page 1 - ICBO 50 nA (VCB = 120 V),
    # hFE 100-300 at VCE = 5 V, IC = 10 mA (rank H = 200-300 matches the
    # MPN RANGE suffix; rank L = 100-200), VCE(sat) 0.2 V max at IC = 50 mA,
    # VBE(sat) 1 V, fT 100-300 MHz, Cob 6 pF; marking G1. Pinout page 1:
    # SOT-23 1 = BASE, 2 = EMITTER, 3 = COLLECTOR, matching the KiCad
    # Transistor_BJT:Q_NPN_BEC symbol (pins 1 B / 2 E / 3 C) and the
    # Package_TO_SOT_SMD:SOT-23 (JEDEC TO-236 Var AB) pads 1/2/3; the
    # library also carries MMBT5551L (extends Q_NPN_BEC, rank L binning).
    current = "electronic_transistor_sot_23_bipolar_npn_160_volt_jiangsu_changjing_electronics_technology_co_ltd_mmbt5551_range_200_300"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (JEDEC TO-236 Var AB)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707456223559680-C2145.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing MMBT5551 SOT-23 specification, March 2013 (C2145)",
            "pages": [1, 2],
            "notes": "SOT-23 (JEDEC TO-236 Var AB) outline: body ~2.9 x 1.3 mm, height ~1.1 mm per the Package_TO_SOT_SMD:SOT-23 master geometry; the 2-page datasheet carries the pinout and ratings but no dimension table.",
        }
        part["electrical"] = {
            "transistor_polarity": "NPN",
            "collector_emitter_breakdown_voltage": "160 V (VCEO); VCBO 180 V, VEBO 6 V",
            "collector_current": "600 mA continuous",
            "power_dissipation": "300 mW (collector, RthJA 416 C/W)",
            "dc_current_gain": "hFE 100-300 at VCE = 5 V, IC = 10 mA (rank H 200-300)",
            "collector_emitter_saturation_voltage": "0.2 V max at IC = 50 mA, IB = 5 mA",
            "transition_frequency": "100-300 MHz (VCE = 10 V, IC = 10 mA)",
            "collector_cutoff_current": "50 nA max (VCB = 120 V)",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["pins"] = {}
        transistor_pins = [
            ["1", "base", "input"],
            ["2", "emitter", "passive"],
            ["3", "collector", "passive"],
        ]
        for pin_index in range(len(transistor_pins)):
            pin = transistor_pins[pin_index]
            part["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing MMBT5551(RANGE:200-300) (C2145): 160 V NPN, 600 mA, 300 mW, hFE rank 200-300 in SOT-23; reconfirmed live 2026-10-01 (stock 2,259,646).",
            "Browser-downloaded the Changjing MMBT5551 datasheet (2 pages, March 2013) into this part; it anchors the MMBT5551/high-voltage NPN SOT-23 family.",
            "Datasheet pinout page 1: 1 = BASE, 2 = EMITTER, 3 = COLLECTOR; the KiCad Transistor_BJT:Q_NPN_BEC symbol numbers its pins B = 1, E = 2, C = 3, matching pad-for-pad.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2146 / Jiangsu Changjing S8050 J3Y full-stage technical data,
    # verified against the Changjing S8050 SOT-23 specification (Rev 2.0,
    # browser-downloaded to this part; anchors the S8050 NPN SOT-23 family):
    # maximum ratings - VCBO 40 V, VCEO 25 V, VEBO 5 V, IC 500 mA, PC 300 mW,
    # RthJA 417 C/W, Tj/Tstg -55 to +150 C; electrical characteristics -
    # V(BR)CBO 40 V, V(BR)CEO 25 V, V(BR)EBO 5 V, ICBO/ICEO/IEBO 0.1 uA,
    # hFE 120-400 at VCE = 1 V, IC = 50 mA (ranks L 120-200 / H 200-350 /
    # J 300-400; the MPN RANGE 200-350 = rank H), VCE(sat) 0.6 V max at
    # IC = 500 mA, VBE(sat) 1.2 V, fT 150 MHz; marking J3Y. Pinout page 1:
    # SOT-23 1 = BASE, 2 = EMITTER, 3 = COLLECTOR, matching the KiCad
    # Transistor_BJT:Q_NPN_BEC symbol (pins 1 B / 2 E / 3 C) and the
    # Package_TO_SOT_SMD:SOT-23 pads. Known library discrepancy recorded:
    # Transistor_BJT:S8050 extends Q_NPN_EBC (1 E / 2 B / 3 C), a different
    # vendor's pinout convention; the Changjing datasheet is authoritative
    # for this part, so Q_NPN_BEC is used.
    current = "electronic_transistor_sot_23_bipolar_npn_25_volt_500_milliamp_jiangsu_changjing_electronics_technology_co_ltd_s8050_j3y_range_200_350"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (JEDEC TO-236 Var AB, J3Y)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710511031631872-C2146.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing S8050 SOT-23 specification, Rev 2.0 (C2146)",
            "pages": [1],
            "notes": "SOT-23 (JEDEC TO-236 Var AB) outline: body ~2.9 x 1.3 mm, height ~1.1 mm per the Package_TO_SOT_SMD:SOT-23 master geometry; the datasheet carries the pinout and ratings but no dimension table.",
        }
        part["electrical"] = {
            "transistor_polarity": "NPN",
            "collector_emitter_breakdown_voltage": "25 V (VCEO); VCBO 40 V, VEBO 5 V",
            "collector_current": "500 mA continuous",
            "power_dissipation": "300 mW (collector, RthJA 417 C/W)",
            "dc_current_gain": "hFE 120-400 at VCE = 1 V, IC = 50 mA (rank H 200-350)",
            "collector_emitter_saturation_voltage": "0.6 V max at IC = 500 mA, IB = 50 mA",
            "transition_frequency": "150 MHz (VCE = 6 V, IC = 20 mA)",
            "collector_cutoff_current": "0.1 uA max (VCB = 40 V)",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["pins"] = {}
        transistor_pins = [
            ["1", "base", "input"],
            ["2", "emitter", "passive"],
            ["3", "collector", "passive"],
        ]
        for pin_index in range(len(transistor_pins)):
            pin = transistor_pins[pin_index]
            part["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing S8050 J3Y(RANGE:200-350) (C2146): 25 V NPN, 500 mA, 300 mW, hFE rank 200-350 in SOT-23; reconfirmed live 2026-10-02 (stock 1,341,936).",
            "Browser-downloaded the Changjing S8050 datasheet (4 pages, Rev 2.0) into this part; it anchors the Changjing S8050 SOT-23 family.",
            "Datasheet pinout page 1: 1 = BASE, 2 = EMITTER, 3 = COLLECTOR; Transistor_BJT:Q_NPN_BEC matches pad-for-pad. The library's Transistor_BJT:S8050 symbol extends Q_NPN_EBC (1 E / 2 B / 3 C), another vendor's convention - deliberately not used; the Changjing datasheet is authoritative.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C2150 / Jiangsu Changjing SS8050 full-stage technical data,
    # verified against the Changjing SS8050 SOT-23 specification (Rev 2.1,
    # browser-downloaded to this part; anchors the SS8050 NPN SOT-23
    # family): maximum ratings - VCBO 40 V, VCEO 25 V, VEBO 5 V, IC 1.5 A,
    # PC 300 mW, RthJA 417 C/W, Tj/Tstg -55 to +150 C; electrical
    # characteristics - V(BR)CBO 40 V, V(BR)CEO 25 V, V(BR)EBO 5 V,
    # ICBO/ICEO/IEBO 0.1 uA, hFE 120-400 at VCE = 1 V, IC = 100 mA (ranks
    # L 120-200 / H 200-350 / J 300-400; the MPN RANGE 200-350 = rank H),
    # VCE(sat) 0.5 V max at IC = 800 mA, VBE(sat) 1.2 V, fT 100 MHz;
    # marking Y1. Pinout page 1: SOT-23 1 = BASE, 2 = EMITTER, 3 =
    # COLLECTOR, matching the KiCad Transistor_BJT:Q_NPN_BEC symbol (pins
    # 1 B / 2 E / 3 C) and the Package_TO_SOT_SMD:SOT-23 pads. The separate
    # jsmsemi SS8050 part (different maker, own datasheet) is not this
    # part's evidence.
    current = "electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jiangsu_changjing_electronics_technology_co_ltd_ss8050_range_200_350"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (JEDEC TO-236 Var AB)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707466581327872-C2150.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing SS8050 SOT-23 specification, Rev 2.1 (C2150)",
            "pages": [1],
            "notes": "SOT-23 (JEDEC TO-236 Var AB) outline: body ~2.9 x 1.3 mm, height ~1.1 mm per the Package_TO_SOT_SMD:SOT-23 master geometry; the datasheet carries the pinout and ratings but no dimension table.",
        }
        part["electrical"] = {
            "transistor_polarity": "NPN",
            "collector_emitter_breakdown_voltage": "25 V (VCEO); VCBO 40 V, VEBO 5 V",
            "collector_current": "1.5 A continuous",
            "power_dissipation": "300 mW (collector, RthJA 417 C/W)",
            "dc_current_gain": "hFE 120-400 at VCE = 1 V, IC = 100 mA (rank H 200-350)",
            "collector_emitter_saturation_voltage": "0.5 V max at IC = 800 mA, IB = 80 mA",
            "transition_frequency": "100 MHz (VCE = 10 V, IC = 50 mA)",
            "collector_cutoff_current": "0.1 uA max (VCB = 40 V)",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["pins"] = {}
        transistor_pins = [
            ["1", "base", "input"],
            ["2", "emitter", "passive"],
            ["3", "collector", "passive"],
        ]
        for pin_index in range(len(transistor_pins)):
            pin = transistor_pins[pin_index]
            part["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing SS8050(RANGE:200-350) (C2150): 25 V NPN, 1.5 A, 300 mW, hFE rank 200-350 in SOT-23; reconfirmed live 2026-10-02 (stock 1,853,286).",
            "Browser-downloaded the Changjing SS8050 datasheet (4 pages, Rev 2.1) into this part; it anchors the Changjing SS8050 SOT-23 family (separate from the jsmsemi SS8050 part, which has its own datasheet and masters).",
            "Datasheet pinout page 1: 1 = BASE, 2 = EMITTER, 3 = COLLECTOR; Transistor_BJT:Q_NPN_BEC matches pad-for-pad, same convention as the C2145/C2146 Changjing SOT-23 NPN integrations.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C6749 / Jiangsu Changjing S9013 J3 full-stage technical data,
    # verified against the Changjing S9013 SOT-23 specification (B.Nov 2011,
    # browser-downloaded to this part; anchors the S9013 NPN SOT-23 family):
    # maximum ratings - VCBO 40 V, VCEO 25 V, VEBO 5 V, IC 500 mA, PC 300 mW,
    # RthJA 416 C/W, Tj 150 C, Tstg -55 to +150 C; electrical
    # characteristics - ICBO/ICEO/IEBO 0.1 uA, hFE 120-400 at VCE = 1 V,
    # IC = 50 mA (ranks L 120-200 / H 200-350 / J 300-400; the MPN RANGE
    # 200-350 = rank H), VCE(sat) 0.6 V max at IC = 500 mA, VBE(sat) 1.2 V,
    # fT 150 MHz, Cob 8 pF; marking J3. Pinout page 1: SOT-23 1 = BASE,
    # 2 = EMITTER, 3 = COLLECTOR, matching the KiCad
    # Transistor_BJT:Q_NPN_BEC symbol and the Package_TO_SOT_SMD:SOT-23
    # pads (same convention as the C2145/C2146/C2150 Changjing integrations).
    current = "electronic_transistor_sot_23_bipolar_npn_25_volt_500_milliamp_jiangsu_changjing_electronics_technology_co_ltd_s9013_j3_range_200_350"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (JEDEC TO-236 Var AB, J3)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579712682339336192-C6749.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing S9013 SOT-23 specification, B.Nov 2011 (C6749)",
            "pages": [1],
            "notes": "SOT-23 (JEDEC TO-236 Var AB) outline: body ~2.9 x 1.3 mm, height ~1.1 mm per the Package_TO_SOT_SMD:SOT-23 master geometry; the datasheet carries the pinout and ratings but no dimension table.",
        }
        part["electrical"] = {
            "transistor_polarity": "NPN",
            "collector_emitter_breakdown_voltage": "25 V (VCEO); VCBO 40 V, VEBO 5 V",
            "collector_current": "500 mA continuous",
            "power_dissipation": "300 mW (collector, RthJA 416 C/W)",
            "dc_current_gain": "hFE 120-400 at VCE = 1 V, IC = 50 mA (rank H 200-350)",
            "collector_emitter_saturation_voltage": "0.6 V max at IC = 500 mA, IB = 50 mA",
            "transition_frequency": "150 MHz (VCE = 6 V, IC = 20 mA)",
            "collector_cutoff_current": "0.1 uA max (VCB = 40 V)",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["pins"] = {}
        transistor_pins = [
            ["1", "base", "input"],
            ["2", "emitter", "passive"],
            ["3", "collector", "passive"],
        ]
        for pin_index in range(len(transistor_pins)):
            pin = transistor_pins[pin_index]
            part["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing S9013 J3(RANGE:200-350) (C6749): 25 V NPN, 500 mA, 300 mW, hFE rank 200-350 in SOT-23; reconfirmed live 2026-10-02 (stock 873,977).",
            "Browser-downloaded the Changjing S9013 datasheet (2 pages, B.Nov 2011) into this part; it anchors the S9013 SOT-23 family.",
            "Datasheet pinout page 1: 1 = BASE, 2 = EMITTER, 3 = COLLECTOR; Transistor_BJT:Q_NPN_BEC matches pad-for-pad, same convention as the C2145/C2146/C2150 Changjing SOT-23 NPN integrations.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C8326 / Jiangsu Changjing MMBT5401 full-stage technical data,
    # verified against the Changjing MMBT5401 SOT-23 specification (C.Nov
    # 2012, browser-downloaded to this part; anchors the high-voltage PNP
    # SOT-23 family): complementary PNP to the MMBT5551. Maximum ratings
    # page 1 - VCBO -160 V, VCEO -150 V, VEBO -5 V, IC -0.6 A, PC 0.3 W,
    # RthJA 416 C/W, Tj 150 C, Tstg -55 to +150 C; electrical
    # characteristics page 1 - ICBO/IEBO -0.1 uA, hFE 100-300 at VCE = -5
    # V, IC = -10 mA (ranks L 100-200 / H 200-300; the MPN RANGE 200-300 =
    # rank H), VCE(sat) -0.5 V max at IC = -50 mA, VBE(sat) -1 V,
    # fT 100 MHz, marking 2L. Pinout page 1: SOT-23 1 = BASE, 2 = EMITTER,
    # 3 = COLLECTOR, matching the KiCad Transistor_BJT:Q_PNP_BEC symbol
    # (pins 1 B / 2 E / 3 C) and the Package_TO_SOT_SMD:SOT-23 pads (same
    # numbering convention as the Changjing NPN integrations).
    current = "electronic_transistor_sot_23_bipolar_pnp_150_volt_jiangsu_changjing_electronics_technology_co_ltd_mmbt5401_range_200_300"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (JEDEC TO-236 Var AB)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707445083758592-C8326.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing MMBT5401 SOT-23 specification, C.Nov 2012 (C8326)",
            "pages": [1],
            "notes": "SOT-23 (JEDEC TO-236 Var AB) outline: body ~2.9 x 1.3 mm, height ~1.1 mm per the Package_TO_SOT_SMD:SOT-23 master geometry; the datasheet carries the pinout and ratings but no dimension table.",
        }
        part["electrical"] = {
            "transistor_polarity": "PNP",
            "collector_emitter_breakdown_voltage": "-150 V (VCEO); VCBO -160 V, VEBO -5 V",
            "collector_current": "-600 mA continuous",
            "power_dissipation": "300 mW (collector, RthJA 416 C/W)",
            "dc_current_gain": "hFE 100-300 at VCE = -5 V, IC = -10 mA (rank H 200-300)",
            "collector_emitter_saturation_voltage": "-0.5 V max at IC = -50 mA, IB = -5 mA",
            "transition_frequency": "100 MHz (VCE = -5 V, IC = -10 mA)",
            "collector_cutoff_current": "-0.1 uA max (VCB = -120 V)",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["pins"] = {}
        transistor_pins = [
            ["1", "base", "input"],
            ["2", "emitter", "passive"],
            ["3", "collector", "passive"],
        ]
        for pin_index in range(len(transistor_pins)):
            pin = transistor_pins[pin_index]
            part["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing MMBT5401(RANGE:200-300) (C8326): -150 V PNP, 600 mA, 300 mW, hFE rank 200-300 in SOT-23; reconfirmed live 2026-10-02 (stock 777,528).",
            "Browser-downloaded the Changjing MMBT5401 datasheet (2 pages, C.Nov 2012) into this part; it anchors the MMBT5401/high-voltage PNP SOT-23 family.",
            "Datasheet pinout page 1: 1 = BASE, 2 = EMITTER, 3 = COLLECTOR; Transistor_BJT:Q_PNP_BEC matches pad-for-pad, same numbering as the Changjing NPN integrations.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # JLC C8512 / Jiangsu Changjing MMBT2222A 1P full-stage technical data,
    # verified against the Changjing MMBT2222A SOT-23 specification (C.Jan
    # 2014, browser-downloaded to this part; anchors the MMBT2222A SOT-23
    # family): maximum ratings - VCBO 75 V, VCEO 40 V, VEBO 6 V, IC 600 mA,
    # PC 300 mW, RthJA 417 C/W, Tj 150 C, Tstg -55 to +150 C; electrical
    # characteristics - ICBO 0.01 uA, hFE 100-300 at VCE = 10 V, IC = 150
    # mA (ranks L 100-200 / H 200-300), VCE(sat) 1 V max at IC = 500 mA /
    # 0.3 V at 150 mA, VBE(sat) 2.0/1.2 V, fT 300 MHz, switching times
    # td 10 ns / tr 25 ns / ts 225 ns / tf 60 ns; marking 1P. Pinout
    # page 1: SOT-23 1 = BASE, 2 = EMITTER, 3 = COLLECTOR, matching the
    # KiCad Transistor_BJT:MMBT2222A symbol (extends Q_NPN_BEC, pins
    # 1 B / 2 E / 3 C) and the Package_TO_SOT_SMD:SOT-23 pads.
    current = "electronic_transistor_sot_23_bipolar_npn_40_volt_600_milliamp_jiangsu_changjing_electronics_technology_co_ltd_mmbt2222a_1p"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (JEDEC TO-236 Var AB, 1P)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586172569242648576-C8512.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "Changjing MMBT2222A SOT-23 specification, C.Jan 2014 (C8512)",
            "pages": [1],
            "notes": "SOT-23 (JEDEC TO-236 Var AB) outline: body ~2.9 x 1.3 mm, height ~1.1 mm per the Package_TO_SOT_SMD:SOT-23 master geometry; the datasheet carries the pinout and ratings but no dimension table.",
        }
        part["electrical"] = {
            "transistor_polarity": "NPN",
            "collector_emitter_breakdown_voltage": "40 V (VCEO); VCBO 75 V, VEBO 6 V",
            "collector_current": "600 mA continuous",
            "power_dissipation": "300 mW (collector, RthJA 417 C/W)",
            "dc_current_gain": "hFE 100-300 at VCE = 10 V, IC = 150 mA (rank H 200-300)",
            "collector_emitter_saturation_voltage": "1 V max at IC = 500 mA (0.3 V at 150 mA)",
            "transition_frequency": "300 MHz (VCE = 20 V, IC = 20 mA)",
            "collector_cutoff_current": "0.01 uA max (VCB = 60 V)",
            "operating_temperature": "-55 to +150 C",
            "polarized": True,
        }
        part["pins"] = {}
        transistor_pins = [
            ["1", "base", "input"],
            ["2", "emitter", "passive"],
            ["3", "collector", "passive"],
        ]
        for pin_index in range(len(transistor_pins)):
            pin = transistor_pins[pin_index]
            part["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": pin[2],
            }
        part["kicad"] = {
            "symbol": "Transistor_BJT:MMBT2222A",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "Package_TO_SOT_SMD:SOT-23_Handsoldering",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Basic Jiangsu Changjing MMBT2222A 1P (C8512): 40 V NPN, 600 mA, 300 mW, hFE rank 200-300 in SOT-23; reconfirmed live 2026-10-02 (stock 597,781).",
            "Browser-downloaded the Changjing MMBT2222A datasheet (2 pages, C.Jan 2014) into this part; it anchors the MMBT2222A SOT-23 family.",
            "Datasheet pinout page 1: 1 = BASE, 2 = EMITTER, 3 = COLLECTOR; Transistor_BJT:MMBT2222A (extends Q_NPN_BEC) matches pad-for-pad, same convention as the other Changjing SOT-23 NPN integrations.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]

    # Apply individually reviewed JLC house choices after other supplier data.
    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="transistor")

    # === BEGIN generated transistor batch (tmp/transistor_batch.py) — regenerated, do not hand-edit ===
    # JLC C10487 / Vishay Intertech SI2301CDS-T1-GE3 - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_p_channel_enhancement_mode_20_volt_vishay_si2301cds_t1_ge3"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-p, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707746209619968-C10487.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SI2301CDS-T1-GE3 datasheet (C10487 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech SI2301CDS-T1-GE3 (C10487); identity and ratings observed live at intake 2026-09-25.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C105432 / Jiangsu Changjing Electronics Technology Co., Ltd. S8550(RANGE:120-200) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_pnp_25_volt_500_milliamp_jiangsu_changjing_electronics_technology_co_ltd_s8550_range_120_200"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586180363135279104-C105432.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "S8550(RANGE:120-200) datasheet (C105432 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. S8550(RANGE:120-200) (C105432); identity and ratings observed live at intake 2026-09-25.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C15127 / Alpha & Omega Semicon AO3401A - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_p_channel_enhancement_mode_30_volt_alpha_omega_semicon_ao3401a"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-p, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8776572966194683904-C15127.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "AO3401A datasheet (C15127 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 to +150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Alpha & Omega Semicon AO3401A (C15127); identity and ratings observed live at intake 2026-09-25.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C20526 / Jiangsu Changjing Electronics Technology Co., Ltd. MMBT3904(RANGE:100-300) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_npn_40_volt_200_milliamp_jiangsu_changjing_electronics_technology_co_ltd_mmbt3904_range_100_300"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-npn, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8552894390264741888-C20526.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "MMBT3904(RANGE:100-300) datasheet (C20526 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. MMBT3904(RANGE:100-300) (C20526); identity and ratings observed live at intake 2026-09-25.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2078 / Jiangsu Changjing Electronics Technology Co., Ltd. 2SA1213(RANGE:120-240) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_89_3_bipolar_pnp_50_volt_2_amp_jiangsu_changjing_electronics_technology_co_ltd_2sa1213_range_120_240"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-89-3 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710228297928704-C2078.pdf"
        part["dimensions_mm"] = {"length": 4.5, "width": 2.5, "height": 1.5}
        part["dimension_reference"] = {
            "document": "2SA1213(RANGE:120-240) datasheet (C2078 provenance)",
            "pages": [1],
            "notes": "SOT-89-3 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-89-3",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. 2SA1213(RANGE:120-240) (C2078); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:SOT-89-3 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2081 / Jiangsu Changjing Electronics Technology Co., Ltd. 2N3904-TA(RANGE:200-300) - transistor family batch 2026-10-06
    current = "electronic_transistor_to_92_bipolar_npn_40_volt_200_milliamp_jiangsu_changjing_electronics_technology_co_ltd_2n3904_ta_range_200_300"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-92_Inline (bjt-npn, pins EBC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895760235057152-C2081.pdf"
        part["dimensions_mm"] = {"length": 5.2, "width": 4.2, "height": 5.2}
        part["dimension_reference"] = {
            "document": "2N3904-TA(RANGE:200-300) datasheet (C2081 provenance)",
            "pages": [1],
            "notes": "TO-92_Inline master geometry; pin order EBC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "passive"},
            "pin_2": {"number": "2", "name": "B", "type": "input"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_EBC",
            "machine_solder": "Package_TO_SOT_THT:TO-92_Inline",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. 2N3904-TA(RANGE:200-300) (C2081); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_EBC master and the Package_TO_SOT_THT:TO-92_Inline footprint master in the 2026-10-06 family batch; pin order EBC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2082 / Jiangsu Changjing Electronics Technology Co., Ltd. 2N5401-TA(RANGE:150-200) - transistor family batch 2026-10-06
    current = "electronic_transistor_to_92_bipolar_pnp_150_volt_600_milliamp_jiangsu_changjing_electronics_technology_co_ltd_2n5401_ta_range_150_200"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-92_Inline (bjt-pnp, pins EBC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895794473025537-C2082.pdf"
        part["dimensions_mm"] = {"length": 5.2, "width": 4.2, "height": 5.2}
        part["dimension_reference"] = {
            "document": "2N5401-TA(RANGE:150-200) datasheet (C2082 provenance)",
            "pages": [1],
            "notes": "TO-92_Inline master geometry; pin order EBC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "passive"},
            "pin_2": {"number": "2", "name": "B", "type": "input"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_EBC",
            "machine_solder": "Package_TO_SOT_THT:TO-92_Inline",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. 2N5401-TA(RANGE:150-200) (C2082); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_EBC master and the Package_TO_SOT_THT:TO-92_Inline footprint master in the 2026-10-06 family batch; pin order EBC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2083 / Jiangsu Changjing Electronics Technology Co., Ltd. 2N5551-TA(RANGE:200-300) - transistor family batch 2026-10-06
    current = "electronic_transistor_to_92_bipolar_npn_160_volt_600_milliamp_jiangsu_changjing_electronics_technology_co_ltd_2n5551_ta_range_200_300"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-92_Inline (bjt-npn, pins EBC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896012308398080-C2083.pdf"
        part["dimensions_mm"] = {"length": 5.2, "width": 4.2, "height": 5.2}
        part["dimension_reference"] = {
            "document": "2N5551-TA(RANGE:200-300) datasheet (C2083 provenance)",
            "pages": [1],
            "notes": "TO-92_Inline master geometry; pin order EBC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "passive"},
            "pin_2": {"number": "2", "name": "B", "type": "input"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_EBC",
            "machine_solder": "Package_TO_SOT_THT:TO-92_Inline",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. 2N5551-TA(RANGE:200-300) (C2083); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_EBC master and the Package_TO_SOT_THT:TO-92_Inline footprint master in the 2026-10-06 family batch; pin order EBC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2089 / Jiangsu Changjing Electronics Technology Co., Ltd. 8550SS-TA(RANGE:160-300) - transistor family batch 2026-10-06
    current = "electronic_transistor_to_92_bipolar_pnp_25_volt_1_5_amp_jiangsu_changjing_electronics_technology_co_ltd_8550ss_ta_range_160_300"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-92_Inline (bjt-pnp, pins EBC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895097085153280-C2089.pdf"
        part["dimensions_mm"] = {"length": 5.2, "width": 4.2, "height": 5.2}
        part["dimension_reference"] = {
            "document": "8550SS-TA(RANGE:160-300) datasheet (C2089 provenance)",
            "pages": [1],
            "notes": "TO-92_Inline master geometry; pin order EBC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "passive"},
            "pin_2": {"number": "2", "name": "B", "type": "input"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_EBC",
            "machine_solder": "Package_TO_SOT_THT:TO-92_Inline",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. 8550SS-TA(RANGE:160-300) (C2089); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_EBC master and the Package_TO_SOT_THT:TO-92_Inline footprint master in the 2026-10-06 family batch; pin order EBC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2090 / Jiangsu Changjing Electronics Technology Co., Ltd. A733-TA(RANGE:200-400) - transistor family batch 2026-10-06
    current = "electronic_transistor_to_92_bipolar_pnp_50_volt_100_milliamp_jiangsu_changjing_electronics_technology_co_ltd_a733_ta_range_200_400"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-92_Inline (bjt-pnp, pins ECB)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895097135620096-C2090.pdf"
        part["dimensions_mm"] = {"length": 5.2, "width": 4.2, "height": 5.2}
        part["dimension_reference"] = {
            "document": "A733-TA(RANGE:200-400) datasheet (C2090 provenance)",
            "pages": [1],
            "notes": "TO-92_Inline master geometry; pin order ECB per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "passive"},
            "pin_2": {"number": "2", "name": "C", "type": "passive"},
            "pin_3": {"number": "3", "name": "B", "type": "input"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_ECB",
            "machine_solder": "Package_TO_SOT_THT:TO-92_Inline",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. A733-TA(RANGE:200-400) (C2090); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_ECB master and the Package_TO_SOT_THT:TO-92_Inline footprint master in the 2026-10-06 family batch; pin order ECB verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2091 / Jiangsu Changjing Electronics Technology Co., Ltd. A94-TA - transistor family batch 2026-10-06
    current = "electronic_transistor_to_92_bipolar_pnp_400_volt_200_milliamp_jiangsu_changjing_electronics_technology_co_ltd_a94_ta"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-92_Inline (bjt-pnp, pins EBC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895097350340608-C2091.pdf"
        part["dimensions_mm"] = {"length": 5.2, "width": 4.2, "height": 5.2}
        part["dimension_reference"] = {
            "document": "A94-TA datasheet (C2091 provenance)",
            "pages": [1],
            "notes": "TO-92_Inline master geometry; pin order EBC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "passive"},
            "pin_2": {"number": "2", "name": "B", "type": "input"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_EBC",
            "machine_solder": "Package_TO_SOT_THT:TO-92_Inline",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. A94-TA (C2091); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_EBC master and the Package_TO_SOT_THT:TO-92_Inline footprint master in the 2026-10-06 family batch; pin order EBC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C20917 / Alpha & Omega Semicon AO3400A - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_30_volt_alpha_omega_semicon_ao3400a"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-n, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8550723985349361664-C20917.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "AO3400A datasheet (C20917 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Alpha & Omega Semicon AO3400A (C20917); identity and ratings observed live at intake 2026-09-25.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2092 / Jiangsu Changjing Electronics Technology Co., Ltd. BC547-TA(RANGE:200-450) - transistor family batch 2026-10-06
    current = "electronic_transistor_to_92_bipolar_npn_45_volt_100_milliamp_jiangsu_changjing_electronics_technology_co_ltd_bc547_ta_range_200_450"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-92_Inline (bjt-npn, pins CBE)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895794468425729-C2092.pdf"
        part["dimensions_mm"] = {"length": 5.2, "width": 4.2, "height": 5.2}
        part["dimension_reference"] = {
            "document": "BC547-TA(RANGE:200-450) datasheet (C2092 provenance)",
            "pages": [1],
            "notes": "TO-92_Inline master geometry; pin order CBE per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "C", "type": "passive"},
            "pin_2": {"number": "2", "name": "B", "type": "input"},
            "pin_3": {"number": "3", "name": "E", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_CBE",
            "machine_solder": "Package_TO_SOT_THT:TO-92_Inline",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. BC547-TA(RANGE:200-450) (C2092); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_CBE master and the Package_TO_SOT_THT:TO-92_Inline footprint master in the 2026-10-06 family batch; pin order CBE verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2095 / Jiangsu Changjing Electronics Technology Co., Ltd. C945-TA(RANGE:200-400) - transistor family batch 2026-10-06
    current = "electronic_transistor_to_92_bipolar_npn_50_volt_150_milliamp_jiangsu_changjing_electronics_technology_co_ltd_c945_ta_range_200_400"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-92_Inline (bjt-npn, pins ECB)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895097128042496-C2095.pdf"
        part["dimensions_mm"] = {"length": 5.2, "width": 4.2, "height": 5.2}
        part["dimension_reference"] = {
            "document": "C945-TA(RANGE:200-400) datasheet (C2095 provenance)",
            "pages": [1],
            "notes": "TO-92_Inline master geometry; pin order ECB per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+125 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "passive"},
            "pin_2": {"number": "2", "name": "C", "type": "passive"},
            "pin_3": {"number": "3", "name": "B", "type": "input"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_ECB",
            "machine_solder": "Package_TO_SOT_THT:TO-92_Inline",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. C945-TA(RANGE:200-400) (C2095); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_ECB master and the Package_TO_SOT_THT:TO-92_Inline footprint master in the 2026-10-06 family batch; pin order ECB verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2097 / Jiangsu Changjing Electronics Technology Co., Ltd. S9014-TA(RANGE:200-600) - transistor family batch 2026-10-06
    current = "electronic_transistor_to_92_bipolar_npn_45_volt_100_milliamp_jiangsu_changjing_electronics_technology_co_ltd_s9014_ta_range_200_600"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-92_Inline (bjt-npn, pins EBC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895826689339392-C2097.pdf"
        part["dimensions_mm"] = {"length": 5.2, "width": 4.2, "height": 5.2}
        part["dimension_reference"] = {
            "document": "S9014-TA(RANGE:200-600) datasheet (C2097 provenance)",
            "pages": [1],
            "notes": "TO-92_Inline master geometry; pin order EBC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "passive"},
            "pin_2": {"number": "2", "name": "B", "type": "input"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_EBC",
            "machine_solder": "Package_TO_SOT_THT:TO-92_Inline",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. S9014-TA(RANGE:200-600) (C2097); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_EBC master and the Package_TO_SOT_THT:TO-92_Inline footprint master in the 2026-10-06 family batch; pin order EBC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2132 / Jiangsu Changjing Electronics Technology Co., Ltd. 2SA812(RANGE:300-400) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_pnp_50_volt_100_milliamp_jiangsu_changjing_electronics_technology_co_ltd_2sa812_range_300_400"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710422603120640-C2132.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "2SA812(RANGE:300-400) datasheet (C2132 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. 2SA812(RANGE:300-400) (C2132); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2133 / Jiangsu Changjing Electronics Technology Co., Ltd. 2SC1623(RANGE:300-400) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_npn_50_volt_100_milliamp_jiangsu_changjing_electronics_technology_co_ltd_2sc1623_range_300_400"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-npn, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710434938978304-C2133.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "2SC1623(RANGE:300-400) datasheet (C2133 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. 2SC1623(RANGE:300-400) (C2133); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2134 / Jiangsu Changjing Electronics Technology Co., Ltd. A1015(RANGE:120-240) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_pnp_50_volt_150_milliamp_jiangsu_changjing_electronics_technology_co_ltd_a1015_range_120_240"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710442853765120-C2134.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "A1015(RANGE:120-240) datasheet (C2134 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. A1015(RANGE:120-240) (C2134); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2137 / Jiangsu Changjing Electronics Technology Co., Ltd. BC817(RANGE:100-250) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_npn_45_volt_500_milliamp_jiangsu_changjing_electronics_technology_co_ltd_bc817_range_100_250"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-npn, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710464588103680-C2137.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "BC817(RANGE:100-250) datasheet (C2137 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. BC817(RANGE:100-250) (C2137); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2138 / Jiangsu Changjing Electronics Technology Co., Ltd. BC847 1G(RANGE:420-800) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_npn_45_volt_100_milliamp_jiangsu_changjing_electronics_technology_co_ltd_bc847_1g_range_420_800"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-npn, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710474255974400-C2138.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "BC847 1G(RANGE:420-800) datasheet (C2138 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. BC847 1G(RANGE:420-800) (C2138); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2139 / Jiangsu Changjing Electronics Technology Co., Ltd. BC857(RANGE:420-800) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_pnp_45_volt_100_milliamp_jiangsu_changjing_electronics_technology_co_ltd_bc857_range_420_800"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178037360967680-C2139.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "BC857(RANGE:420-800) datasheet (C2139 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 to +150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. BC857(RANGE:420-800) (C2139); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2143 / Jiangsu Changjing Electronics Technology Co., Ltd. MMBT3906 2A(RANGE:100-300) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_pnp_40_volt_200_milliamp_jiangsu_changjing_electronics_technology_co_ltd_mmbt3906_2a_range_100_300"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710496003575808-C2143.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "MMBT3906 2A(RANGE:100-300) datasheet (C2143 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. MMBT3906 2A(RANGE:100-300) (C2143); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2144 / Jiangsu Changjing Electronics Technology Co., Ltd. MMBT4401(RANGE:100-300) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_npn_40_volt_600_milliamp_jiangsu_changjing_electronics_technology_co_ltd_mmbt4401_range_100_300"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-npn, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710506862493696-C2144.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "MMBT4401(RANGE:100-300) datasheet (C2144 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. MMBT4401(RANGE:100-300) (C2144); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2147 / Jiangsu Changjing Electronics Technology Co., Ltd. S8550 2TY(RANGE:200-350) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_pnp_25_volt_500_milliamp_jiangsu_changjing_electronics_technology_co_ltd_s8550_2ty_range_200_350"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710520724938752-C2147.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "S8550 2TY(RANGE:200-350) datasheet (C2147 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. S8550 2TY(RANGE:200-350) (C2147); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2148 / Jiangsu Changjing Electronics Technology Co., Ltd. S9014 - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_npn_45_volt_100_milliamp_jiangsu_changjing_electronics_technology_co_ltd_s9014"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-npn, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710530543804416-C2148.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "S9014 datasheet (C2148 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. S9014 (C2148); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2149 / Jiangsu Changjing Electronics Technology Co., Ltd. S9015(RANGE:300-400) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_pnp_45_volt_100_milliamp_jiangsu_changjing_electronics_technology_co_ltd_s9015_range_300_400"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710539880189952-C2149.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "S9015(RANGE:300-400) datasheet (C2149 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. S9015(RANGE:300-400) (C2149); identity and ratings observed live at intake 2026-09-28.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2152 / Jiangsu Changjing Electronics Technology Co., Ltd. D882(RANGE:160-320) - transistor family batch 2026-10-06
    current = "electronic_transistor_to_126_bipolar_npn_30_volt_3_amp_jiangsu_changjing_electronics_technology_co_ltd_d882_range_160_320"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-126-3_Vertical (bjt-npn, pins ECB)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895794468966400-C2152.pdf"
        part["dimensions_mm"] = {"length": 9.0, "width": 4.5, "height": 8.5}
        part["dimension_reference"] = {
            "document": "D882(RANGE:160-320) datasheet (C2152 provenance)",
            "pages": [1],
            "notes": "TO-126-3_Vertical master geometry; pin order ECB per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "E", "type": "passive"},
            "pin_2": {"number": "2", "name": "C", "type": "passive"},
            "pin_3": {"number": "3", "name": "B", "type": "input"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_ECB",
            "machine_solder": "Package_TO_SOT_THT:TO-126-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. D882(RANGE:160-320) (C2152); identity and ratings observed live at intake 2026-09-27.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_ECB master and the Package_TO_SOT_THT:TO-126-3_Vertical footprint master in the 2026-10-06 family batch; pin order ECB verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2557 / Infineon Technologies IRF1010EPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_60_volt_83_amp_infineon_technologies_irf1010epbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159579553792-C2557.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF1010EPBF datasheet (C2557 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF1010EPBF (C2557); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2559 / Infineon Technologies IRF1405PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_55_volt_169_amp_infineon_technologies_irf1405pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159718100992-C2559.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF1405PBF datasheet (C2559 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF1405PBF (C2559); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2560 / Infineon Technologies IRF2807PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_75_amp_infineon_technologies_irf2807pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159545323520-C2560.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF2807PBF datasheet (C2560 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF2807PBF (C2560); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2561 / Infineon Technologies IRF3205PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_55_volt_110_amp_infineon_technologies_irf3205pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588886901999226880-C2561.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF3205PBF datasheet (C2561 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF3205PBF (C2561); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2562 / Infineon Technologies IRF3710PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_100_volt_57_amp_infineon_technologies_irf3710pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896295759056896-C2562.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF3710PBF datasheet (C2562 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF3710PBF (C2562); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2564 / Infineon Technologies IRF4905PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_p_channel_enhancement_mode_55_volt_74_amp_infineon_technologies_irf4905pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896295813042176-C2564.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF4905PBF datasheet (C2564 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF4905PBF (C2564); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2565 / Infineon Technologies IRF530NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_100_volt_17_amp_infineon_technologies_irf530npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887091846008832-C2565.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF530NPBF datasheet (C2565 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF530NPBF (C2565); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2566 / Infineon Technologies IRF540NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_100_volt_33_amp_infineon_technologies_irf540npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159701188608-C2566.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF540NPBF datasheet (C2566 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF540NPBF (C2566); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2567 / Infineon Technologies IRF630NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_200_volt_9_3_amp_infineon_technologies_irf630npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159554523136-C2567.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF630NPBF datasheet (C2567 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF630NPBF (C2567); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2568 / Infineon Technologies IRF640NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_200_volt_18_amp_infineon_technologies_irf640npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887122061504512-C2568.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF640NPBF datasheet (C2568 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF640NPBF (C2568); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2570 / Vishay Intertech IRF740PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_400_volt_10_amp_vishay_intertech_irf740pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887122090053632-C2570.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF740PBF datasheet (C2570 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF740PBF (C2570); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2573 / Vishay Intertech IRF830PbF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_500_volt_4_5_amp_vishay_intertech_irf830pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159507980288-C2573.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF830PbF datasheet (C2573 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF830PbF (C2573); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2574 / Infineon Technologies IRF9530NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_p_channel_enhancement_mode_100_volt_14_amp_infineon_technologies_irf9530npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159540994048-C2574.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF9530NPBF datasheet (C2574 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF9530NPBF (C2574); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2575 / Infineon Technologies IRF9540NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220_mosfet_p_channel_enhancement_mode_100_volt_23_amp_infineon_technologies_irf9540npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887122090864640-C2575.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF9540NPBF datasheet (C2575 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF9540NPBF (C2575); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2576 / Infineon Technologies IRF9Z24NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_p_channel_enhancement_mode_55_volt_12_amp_infineon_technologies_irf9z24npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159562506240-C2576.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF9Z24NPBF datasheet (C2576 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF9Z24NPBF (C2576); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2578 / Infineon Technologies IRFB3207PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_180_amp_infineon_technologies_irfb3207pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896295763251200-C2578.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB3207PBF datasheet (C2578 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB3207PBF (C2578); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2580 / Infineon Technologies IRFP250NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_30_amp_infineon_technologies_irfp250npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159537881088-C2580.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP250NPBF datasheet (C2580 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP250NPBF (C2580); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2582 / Vishay Intertech IRFP460APBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_500_volt_20_amp_vishay_intertech_irfp460apbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159536799744-C2582.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP460APBF datasheet (C2582 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFP460APBF (C2582); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2583 / Infineon Technologies IRFR024NTRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_55_volt_17_amp_infineon_technologies_irfr024ntrpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710818142900224-C2583.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR024NTRPBF datasheet (C2583 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFR024NTRPBF (C2583); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2584 / Infineon Technologies IRFR220NTRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_200_volt_5_amp_infineon_technologies_irfr220ntrpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710828792238080-C2584.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR220NTRPBF datasheet (C2584 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFR220NTRPBF (C2584); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2585 / Infineon Technologies IRFR9024NTRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_p_channel_enhancement_mode_55_volt_11_amp_infineon_technologies_irfr9024ntrpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710840192765952-C2585.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR9024NTRPBF datasheet (C2585 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFR9024NTRPBF (C2585); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2586 / Infineon Technologies IRFZ44NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_55_volt_49_amp_infineon_technologies_irfz44npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887122070163456-C2586.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFZ44NPBF datasheet (C2586 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFZ44NPBF (C2586); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2588 / Infineon Technologies IRLML2402TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_20_volt_1_2_amp_infineon_technologies_irlml2402trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-n, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710850024214528-C2588.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "IRLML2402TRPBF datasheet (C2588 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLML2402TRPBF (C2588); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2589 / Infineon Technologies IRLML2502TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_20_volt_4_2_amp_infineon_technologies_irlml2502trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-n, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710858408628224-C2589.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "IRLML2502TRPBF datasheet (C2589 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLML2502TRPBF (C2589); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2590 / Infineon Technologies IRLML2803TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_30_volt_1_2_amp_infineon_technologies_irlml2803trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-n, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710867971231744-C2590.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "IRLML2803TRPBF datasheet (C2590 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLML2803TRPBF (C2590); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2591 / Infineon Technologies IRLML5103TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_p_channel_enhancement_mode_30_volt_760_milliamp_infineon_technologies_irlml5103trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-p, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710876957327360-C2591.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "IRLML5103TRPBF datasheet (C2591 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLML5103TRPBF (C2591); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2592 / Infineon Technologies IRLML5203TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_p_channel_enhancement_mode_30_volt_3_amp_infineon_technologies_irlml5203trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-p, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8578898135135014912-C2592.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "IRLML5203TRPBF datasheet (C2592 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLML5203TRPBF (C2592); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2593 / Infineon Technologies IRLML6402TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_p_channel_enhancement_mode_20_volt_3_7_amp_infineon_technologies_irlml6402trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-p, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710937009340416-C2593.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "IRLML6402TRPBF datasheet (C2593 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLML6402TRPBF (C2593); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2594 / Infineon Technologies IRLR120NTRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_100_volt_10_amp_infineon_technologies_irlr120ntrpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710946452750336-C2594.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRLR120NTRPBF datasheet (C2594 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLR120NTRPBF (C2594); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2595 / Vishay Intertech IRFP460PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_500_volt_20_amp_vishay_intertech_irfp460pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887159558852608-C2595.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP460PBF datasheet (C2595 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFP460PBF (C2595); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2597 / Vishay Intertech IRF520PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_100_volt_9_2_amp_vishay_intertech_irf520pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896295755132928-C2597.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF520PBF datasheet (C2597 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF520PBF (C2597); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2598 / Infineon Technologies IRF520NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_100_volt_9_7_amp_infineon_technologies_irf520npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896295599673344-C2598.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF520NPBF datasheet (C2598 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF520NPBF (C2598); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2600 / Vishay Intertech IRF710PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_400_volt_2_amp_vishay_intertech_irf710pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896295763791872-C2600.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF710PBF datasheet (C2600 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF710PBF (C2600); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2605 / Vishay Intertech IRF840APBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_500_volt_8_amp_vishay_intertech_irf840apbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887122065833984-C2605.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF840APBF datasheet (C2605 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF840APBF (C2605); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2606 / Vishay Intertech IRF840ASTRLPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_263_mosfet_n_channel_enhancement_mode_500_volt_8_amp_vishay_intertech_irf840astrlpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-263-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586202410838052864-C2606.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 9.2, "height": 4.6}
        part["dimension_reference"] = {
            "document": "IRF840ASTRLPBF datasheet (C2606 provenance)",
            "pages": [1],
            "notes": "TO-263-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-263-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF840ASTRLPBF (C2606); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-263-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2608 / Infineon Technologies IRF1404ZPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_40_volt_120_amp_infineon_technologies_irf1404zpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887122069217280-C2608.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF1404ZPBF datasheet (C2608 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF1404ZPBF (C2608); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2609 / Infineon Technologies IRF1407PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_130_amp_infineon_technologies_irf1407pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887160631648256-C2609.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF1407PBF datasheet (C2609 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF1407PBF (C2609); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2610 / Infineon Technologies IRF2804PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_40_volt_270_amp_infineon_technologies_irf2804pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887254378942464-C2610.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF2804PBF datasheet (C2610 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF2804PBF (C2610); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2611 / Infineon Technologies IRF2805PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_55_volt_175_amp_infineon_technologies_irf2805pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896296983793664-C2611.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF2805PBF datasheet (C2611 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF2805PBF (C2611); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2612 / Infineon Technologies IRF3205ZPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_55_volt_110_amp_infineon_technologies_irf3205zpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896296988528640-C2612.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF3205ZPBF datasheet (C2612 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF3205ZPBF (C2612); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2613 / Infineon Technologies IRF3205STRLPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_263_mosfet_n_channel_enhancement_mode_55_volt_110_amp_infineon_technologies_irf3205strlpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-263-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710955192057856-C2613.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 9.2, "height": 4.6}
        part["dimension_reference"] = {
            "document": "IRF3205STRLPBF datasheet (C2613 provenance)",
            "pages": [1],
            "notes": "TO-263-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-263-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF3205STRLPBF (C2613); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-263-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2614 / Infineon Technologies IRF3415PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_150_volt_43_amp_infineon_technologies_irf3415pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887122115760128-C2614.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF3415PBF datasheet (C2614 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF3415PBF (C2614); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2615 / Infineon Technologies IRFP3415PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_150_volt_43_amp_infineon_technologies_irfp3415pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588902628273369088-C2615.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP3415PBF datasheet (C2615 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP3415PBF (C2615); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2616 / Infineon Technologies IRF3710STRLPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_263_mosfet_n_channel_enhancement_mode_100_volt_57_amp_infineon_technologies_irf3710strlpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-263-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710964190461952-C2616.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 9.2, "height": 4.6}
        part["dimension_reference"] = {
            "document": "IRF3710STRLPBF datasheet (C2616 provenance)",
            "pages": [1],
            "notes": "TO-263-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-263-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF3710STRLPBF (C2616); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-263-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2618 / Infineon Technologies IRF3808PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_140_amp_infineon_technologies_irf3808pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896296983793665-C2618.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF3808PBF datasheet (C2618 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF3808PBF (C2618); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2620 / Infineon Technologies IRF4905STRLPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_263_mosfet_p_channel_enhancement_mode_55_volt_70_amp_infineon_technologies_irf4905strlpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-263-3_TabPin2 (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710973634138112-C2620.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 9.2, "height": 4.6}
        part["dimension_reference"] = {
            "document": "IRF4905STRLPBF datasheet (C2620 provenance)",
            "pages": [1],
            "notes": "TO-263-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-263-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF4905STRLPBF (C2620); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_SMD:TO-263-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2621 / Infineon Technologies IRF5210PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_p_channel_enhancement_mode_100_volt_40_amp_infineon_technologies_irf5210pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887160656678912-C2621.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF5210PBF datasheet (C2621 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF5210PBF (C2621); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2622 / Infineon Technologies IRF5210STRLPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_263_mosfet_p_channel_enhancement_mode_100_volt_38_amp_infineon_technologies_irf5210strlpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-263-3_TabPin2 (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710982522142720-C2622.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 9.2, "height": 4.6}
        part["dimension_reference"] = {
            "document": "IRF5210STRLPBF datasheet (C2622 provenance)",
            "pages": [1],
            "notes": "TO-263-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-263-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF5210STRLPBF (C2622); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_SMD:TO-263-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2623 / Infineon Technologies IRF5305PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_p_channel_enhancement_mode_55_volt_31_amp_infineon_technologies_irf5305pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896296992587776-C2623.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF5305PBF datasheet (C2623 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRF5305PBF (C2623); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2624 / Infineon Technologies IRFR5305TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_p_channel_enhancement_mode_55_volt_31_amp_infineon_technologies_irfr5305trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579710991099355136-C2624.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR5305TRPBF datasheet (C2624 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFR5305TRPBF (C2624); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2627 / Vishay Intertech IRF9630PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_p_channel_enhancement_mode_200_volt_6_5_amp_vishay_intertech_irf9630pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887160632459264-C2627.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF9630PBF datasheet (C2627 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF9630PBF (C2627); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2628 / Vishay Intertech IRF9640PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_p_channel_enhancement_mode_200_volt_11_amp_vishay_intertech_irf9640pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887122060693504-C2628.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF9640PBF datasheet (C2628 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF9640PBF (C2628); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2629 / Vishay Intertech IRF9640STRLPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_263_mosfet_p_channel_enhancement_mode_200_volt_6_8_amp_vishay_intertech_irf9640strlpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-263-3_TabPin2 (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586202370527408128-C2629.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 9.2, "height": 4.6}
        part["dimension_reference"] = {
            "document": "IRF9640STRLPBF datasheet (C2629 provenance)",
            "pages": [1],
            "notes": "TO-263-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-263-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF9640STRLPBF (C2629); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_SMD:TO-263-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2631 / Infineon Technologies IRFB4410PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_100_volt_96_amp_infineon_technologies_irfb4410pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896296995835904-C2631.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4410PBF datasheet (C2631 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4410PBF (C2631); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2634 / Vishay Intertech IRFBE20PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_800_volt_1_8_amp_vishay_intertech_irfbe20pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896296979869696-C2634.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFBE20PBF datasheet (C2634 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFBE20PBF (C2634); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2637 / Vishay Intertech IRFBG30PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220_mosfet_n_channel_enhancement_mode_1000_volt_3_1_amp_vishay_intertech_irfbg30pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896298317987840-C2637.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFBG30PBF datasheet (C2637 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFBG30PBF (C2637); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2641 / Infineon Technologies IRFB3077PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_210_amp_infineon_technologies_irfb3077pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887122220077057-C2641.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB3077PBF datasheet (C2641 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB3077PBF (C2641); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2642 / Infineon Technologies IRFB3206PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_60_volt_210_amp_infineon_technologies_irfb3206pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887160665878528-C2642.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB3206PBF datasheet (C2642 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB3206PBF (C2642); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2643 / Infineon Technologies IRFB3306PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_60_volt_160_amp_infineon_technologies_irfb3306pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896298287681536-C2643.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB3306PBF datasheet (C2643 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB3306PBF (C2643); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2644 / Infineon Technologies IRFB3307ZPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_128_amp_infineon_technologies_irfb3307zpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896298041163776-C2644.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB3307ZPBF datasheet (C2644 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB3307ZPBF (C2644); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2646 / Vishay Intertech IRF840STRLPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_263_mosfet_n_channel_enhancement_mode_500_volt_8_amp_vishay_intertech_irf840strlpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-263-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586202419772866560-C2646.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 9.2, "height": 4.6}
        part["dimension_reference"] = {
            "document": "IRF840STRLPBF datasheet (C2646 provenance)",
            "pages": [1],
            "notes": "TO-263-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-263-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF840STRLPBF (C2646); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-263-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2647 / Infineon Technologies IRFB3607PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_80_amp_infineon_technologies_irfb3607pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887160657219584-C2647.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB3607PBF datasheet (C2647 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB3607PBF (C2647); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2649 / Infineon Technologies IRFB4020PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_200_volt_18_amp_infineon_technologies_irfb4020pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896298082701312-C2649.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4020PBF datasheet (C2649 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4020PBF (C2649); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2650 / Infineon Technologies IRFB4110PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220_mosfet_n_channel_enhancement_mode_100_volt_180_amp_infineon_technologies_irfb4110pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887122074222592-C2650.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4110PBF datasheet (C2650 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4110PBF (C2650); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2651 / Infineon Technologies IRFB4115PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220_mosfet_n_channel_enhancement_mode_150_volt_104_amp_infineon_technologies_irfb4115pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887160808620032-C2651.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4115PBF datasheet (C2651 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4115PBF (C2651); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2652 / Infineon Technologies IRFB4227PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_200_volt_65_amp_infineon_technologies_irfb4227pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887123147964416-C2652.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4227PBF datasheet (C2652 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-40 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4227PBF (C2652); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2653 / Infineon Technologies IRFB4229PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_250_volt_46_amp_infineon_technologies_irfb4229pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887160820391936-C2653.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4229PBF datasheet (C2653 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-40 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4229PBF (C2653); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2655 / Infineon Technologies IRFB4310ZPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220_3_mosfet_n_channel_enhancement_mode_100_volt_127_amp_infineon_technologies_irfb4310zpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887161910775808-C2655.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4310ZPBF datasheet (C2655 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4310ZPBF (C2655); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2656 / Infineon Technologies IRFB4321PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_150_volt_85_amp_infineon_technologies_irfb4321pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896298304593920-C2656.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4321PBF datasheet (C2656 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4321PBF (C2656); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2657 / Infineon Technologies IRFB4410ZPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_100_volt_97_amp_infineon_technologies_irfb4410zpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887161903333376-C2657.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4410ZPBF datasheet (C2657 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4410ZPBF (C2657); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2658 / Infineon Technologies IRFB4610PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_100_volt_73_amp_infineon_technologies_irfb4610pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887162082877440-C2658.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4610PBF datasheet (C2658 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4610PBF (C2658); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2660 / Infineon Technologies IRFB4710PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_100_volt_75_amp_infineon_technologies_irfb4710pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896298296205312-C2660.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB4710PBF datasheet (C2660 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB4710PBF (C2660); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2662 / Infineon Technologies IRFB260NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_200_volt_56_amp_infineon_technologies_irfb260npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896298291875840-C2662.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRFB260NPBF datasheet (C2662 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFB260NPBF (C2662); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2671 / Infineon Technologies IRFP054NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_55_volt_81_amp_infineon_technologies_irfp054npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588902826944696320-C2671.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP054NPBF datasheet (C2671 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP054NPBF (C2671); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2672 / Infineon Technologies IRFP140NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_33_amp_infineon_technologies_irfp140npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887285673185280-C2672.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP140NPBF datasheet (C2672 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP140NPBF (C2672); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2673 / Infineon Technologies IRFP150MPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_42_amp_infineon_technologies_irfp150mpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887285630160896-C2673.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP150MPBF datasheet (C2673 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP150MPBF (C2673); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2674 / Vishay Intertech IRFP240PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_20_amp_vishay_intertech_irfp240pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887629866160128-C2674.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP240PBF datasheet (C2674 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFP240PBF (C2674); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2676 / Infineon Technologies IRFP250MPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_30_amp_infineon_technologies_irfp250mpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887161956913152-C2676.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP250MPBF datasheet (C2676 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP250MPBF (C2676); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2678 / Infineon Technologies IRFP260NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_50_amp_infineon_technologies_irfp260npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887161889939456-C2678.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP260NPBF datasheet (C2678 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP260NPBF (C2678); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2679 / Infineon Technologies IRFP260MPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_50_amp_infineon_technologies_irfp260mpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887162087071744-C2679.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP260MPBF datasheet (C2679 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP260MPBF (C2679); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2680 / Vishay Intertech IRFP350PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_400_volt_16_amp_vishay_intertech_irfp350pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588911081536700416-C2680.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP350PBF datasheet (C2680 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFP350PBF (C2680); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2683 / Vishay Intertech IRFP450PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_500_volt_8_7_amp_vishay_intertech_irfp450pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887123910381568-C2683.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP450PBF datasheet (C2683 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFP450PBF (C2683); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2684 / Infineon Technologies IRFP450LCPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_500_volt_14_amp_infineon_technologies_irfp450lcpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588911426848608256-C2684.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP450LCPBF datasheet (C2684 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP450LCPBF (C2684); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2685 / Infineon Technologies IRFP9140NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_p_channel_enhancement_mode_100_volt_23_amp_infineon_technologies_irfp9140npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887253528039424-C2685.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP9140NPBF datasheet (C2685 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP9140NPBF (C2685); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2686 / Vishay Intertech IRFP9240PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_p_channel_enhancement_mode_200_volt_12_amp_vishay_intertech_irfp9240pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887254638448640-C2686.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP9240PBF datasheet (C2686 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFP9240PBF (C2686); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2687 / Infineon Technologies IRFP3206PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_60_volt_200_amp_infineon_technologies_irfp3206pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887629726801920-C2687.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP3206PBF datasheet (C2687 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP3206PBF (C2687); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2688 / Infineon Technologies IRFP3710PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_57_amp_infineon_technologies_irfp3710pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887124070846464-C2688.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP3710PBF datasheet (C2688 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP3710PBF (C2688); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2689 / Infineon Technologies IRFP4110PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_180_amp_infineon_technologies_irfp4110pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887162079088640-C2689.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP4110PBF datasheet (C2689 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP4110PBF (C2689); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2690 / Infineon Technologies IRFP4227PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_65_amp_infineon_technologies_irfp4227pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887162096271360-C2690.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP4227PBF datasheet (C2690 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-40 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP4227PBF (C2690); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2711 / onsemi FQA9N90C-F109 - transistor family batch 2026-10-06
    current = "electronic_transistor_to_3pn_mosfet_n_channel_enhancement_mode_900_volt_9_amp_onsemi_fqa9n90c_f109"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-3P-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887123428036608-C2711.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "FQA9N90C-F109 datasheet (C2711 provenance)",
            "pages": [1],
            "notes": "TO-3P-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-3P-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi FQA9N90C-F109 (C2711); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-3P-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2720 / onsemi FQA28N50 - transistor family batch 2026-10-06
    current = "electronic_transistor_to_3p_3_mosfet_n_channel_enhancement_mode_500_volt_28_4_amp_onsemi_fqa28n50"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-3P-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896257892339712-C2720.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "FQA28N50 datasheet (C2720 provenance)",
            "pages": [1],
            "notes": "TO-3P-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-3P-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi FQA28N50 (C2720); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-3P-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2728 / onsemi MJ15025G - transistor family batch 2026-10-06
    current = "electronic_transistor_to_204_bipolar_pnp_250_volt_16_amp_onsemi_mj15025g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-3 (bjt-pnp, pins BCE)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887285567246336-C2728.pdf"
        part["dimensions_mm"] = {"length": 26.0, "width": 20.0, "height": 10.5}
        part["dimension_reference"] = {
            "document": "MJ15025G datasheet (C2728 provenance)",
            "pages": [1],
            "notes": "TO-3 master geometry; pin order BCE per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-65 C~+200 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "C", "type": "passive"},
            "pin_3": {"number": "3", "name": "E", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BCE",
            "machine_solder": "Package_TO_SOT_THT:TO-3",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi MJ15025G (C2728); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BCE master and the Package_TO_SOT_THT:TO-3 footprint master in the 2026-10-06 family batch; pin order BCE verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2729 / onsemi MJ15004G - transistor family batch 2026-10-06
    current = "electronic_transistor_to_204_bipolar_pnp_140_volt_20_amp_onsemi_mj15004g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-3 (bjt-pnp, pins BCE)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588895189692272640-C2729.pdf"
        part["dimensions_mm"] = {"length": 26.0, "width": 20.0, "height": 10.5}
        part["dimension_reference"] = {
            "document": "MJ15004G datasheet (C2729 provenance)",
            "pages": [1],
            "notes": "TO-3 master geometry; pin order BCE per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-65 C~+200 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "C", "type": "passive"},
            "pin_3": {"number": "3", "name": "E", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BCE",
            "machine_solder": "Package_TO_SOT_THT:TO-3",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi MJ15004G (C2729); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BCE master and the Package_TO_SOT_THT:TO-3 footprint master in the 2026-10-06 family batch; pin order BCE verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2730 / onsemi MJ15024G - transistor family batch 2026-10-06
    current = "electronic_transistor_to_204_bipolar_npn_250_volt_16_amp_onsemi_mj15024g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-3 (bjt-npn, pins BCE)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887629853306880-C2730.pdf"
        part["dimensions_mm"] = {"length": 26.0, "width": 20.0, "height": 10.5}
        part["dimension_reference"] = {
            "document": "MJ15024G datasheet (C2730 provenance)",
            "pages": [1],
            "notes": "TO-3 master geometry; pin order BCE per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-65 C~+200 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "C", "type": "passive"},
            "pin_3": {"number": "3", "name": "E", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BCE",
            "machine_solder": "Package_TO_SOT_THT:TO-3",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi MJ15024G (C2730); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_BCE master and the Package_TO_SOT_THT:TO-3 footprint master in the 2026-10-06 family batch; pin order BCE verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2732 / onsemi MJ11032G - transistor family batch 2026-10-06
    current = "electronic_transistor_to_204_bipolar_npn_darlington_120_volt_50_amp_onsemi_mj11032g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-3 (bjt-npn, pins BCE)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588886940732678144-C2732.pdf"
        part["dimensions_mm"] = {"length": 26.0, "width": 20.0, "height": 10.5}
        part["dimension_reference"] = {
            "document": "MJ11032G datasheet (C2732 provenance)",
            "pages": [1],
            "notes": "TO-3 master geometry; pin order BCE per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+200 C@(Tj)"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "C", "type": "passive"},
            "pin_3": {"number": "3", "name": "E", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BCE",
            "machine_solder": "Package_TO_SOT_THT:TO-3",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi MJ11032G (C2732); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_BCE master and the Package_TO_SOT_THT:TO-3 footprint master in the 2026-10-06 family batch; pin order BCE verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2916 / Infineon Technologies IRFP4310ZPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_134_amp_infineon_technologies_irfp4310zpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887285928091648-C2916.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP4310ZPBF datasheet (C2916 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP4310ZPBF (C2916); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2917 / Infineon Technologies IRFP4321PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_150_volt_78_amp_infineon_technologies_irfp4321pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887629685264384-C2917.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP4321PBF datasheet (C2917 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP4321PBF (C2917); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2918 / Infineon Technologies IRFP4368PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_75_volt_195_amp_infineon_technologies_irfp4368pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887629861965824-C2918.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP4368PBF datasheet (C2918 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP4368PBF (C2918); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2919 / Infineon Technologies IRFP4468PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_290_amp_infineon_technologies_irfp4468pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887162938380288-C2919.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP4468PBF datasheet (C2919 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP4468PBF (C2919); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2920 / Infineon Technologies IRFP4568PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_150_volt_171_amp_infineon_technologies_irfp4568pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887164113731584-C2920.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP4568PBF datasheet (C2920 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP4568PBF (C2920); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2921 / Infineon Technologies IRFP4668PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_130_amp_infineon_technologies_irfp4668pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887164113866752-C2921.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP4668PBF datasheet (C2921 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP4668PBF (C2921); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2923 / Infineon Technologies IRFP4768PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_250_volt_93_amp_infineon_technologies_irfp4768pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887286805377024-C2923.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP4768PBF datasheet (C2923 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP4768PBF (C2923); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2924 / Infineon Technologies IRFP90N20DPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_94_amp_infineon_technologies_irfp90n20dpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887629856825344-C2924.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFP90N20DPBF datasheet (C2924 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFP90N20DPBF (C2924); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2929 / Vishay Intertech IRFPC60LCPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_600_volt_16_amp_vishay_intertech_irfpc60lcpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887286818230272-C2929.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFPC60LCPBF datasheet (C2929 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFPC60LCPBF (C2929); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2934 / Infineon Technologies IRFPF50PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_900_volt_6_7_amp_infineon_technologies_irfpf50pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588904358684086272-C2934.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFPF50PBF datasheet (C2934 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFPF50PBF (C2934); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C2936 / Vishay Intertech IRFPG50PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_1000_volt_6_1_amp_vishay_intertech_irfpg50pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-247-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887164125503488-C2936.pdf"
        part["dimensions_mm"] = {"length": 15.9, "width": 5.5, "height": 15.6}
        part["dimension_reference"] = {
            "document": "IRFPG50PBF datasheet (C2936 provenance)",
            "pages": [1],
            "notes": "TO-247-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-247-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFPG50PBF (C2936); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-247-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3007 / Infineon Technologies IRLR024NTRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_55_volt_17_amp_infineon_technologies_irlr024ntrpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711209257689088-C3007.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRLR024NTRPBF datasheet (C3007 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLR024NTRPBF (C3007); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3008 / Infineon Technologies IRFR120NTRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_100_volt_9_4_amp_infineon_technologies_irfr120ntrpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711221681356800-C3008.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR120NTRPBF datasheet (C3008 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFR120NTRPBF (C3008); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3009 / Vishay Intertech IRFR320TRPbF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_400_volt_3_1_amp_vishay_intertech_irfr320trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586202374762979328-C3009.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR320TRPbF datasheet (C3009 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFR320TRPbF (C3009); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3010 / Infineon Technologies IRLR2905TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_55_volt_42_amp_infineon_technologies_irlr2905trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711230912745472-C3010.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRLR2905TRPBF datasheet (C3010 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLR2905TRPBF (C3010); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3015 / Infineon Technologies IRFR430ATRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_500_volt_5_amp_infineon_technologies_irfr430atrpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711247216414720-C3015.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR430ATRPBF datasheet (C3015 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFR430ATRPBF (C3015); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3016 / Infineon Technologies IRFR3410TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_100_volt_31_amp_infineon_technologies_irfr3410trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711302300209152-C3016.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR3410TRPBF datasheet (C3016 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFR3410TRPBF (C3016); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3017 / Infineon Technologies IRLR3410TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_100_volt_17_amp_infineon_technologies_irlr3410trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711355689369600-C3017.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRLR3410TRPBF datasheet (C3017 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLR3410TRPBF (C3017); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3018 / Infineon Technologies IRFR5410TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_p_channel_enhancement_mode_100_volt_13_amp_infineon_technologies_irfr5410trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711364759076864-C3018.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR5410TRPBF datasheet (C3018 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFR5410TRPBF (C3018); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3019 / Infineon Technologies IRFR9120NTRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_p_channel_enhancement_mode_100_volt_6_6_amp_infineon_technologies_irfr9120ntrpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711373630029824-C3019.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR9120NTRPBF datasheet (C3019 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFR9120NTRPBF (C3019); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3020 / Vishay Intertech IRFR9220TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_p_channel_enhancement_mode_200_volt_3_6_amp_vishay_intertech_irfr9220trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586202389569818624-C3020.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFR9220TRPBF datasheet (C3020 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFR9220TRPBF (C3020); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3022 / Vishay Intertech IRFRC20TRLPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_600_volt_2_amp_vishay_intertech_irfrc20trlpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586202398017011712-C3022.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "IRFRC20TRLPBF datasheet (C3022 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFRC20TRLPBF (C3022); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3024 / Infineon Technologies IRLU024NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_55_volt_17_amp_infineon_technologies_irlu024npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-251-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887286696460288-C3024.pdf"
        part["dimensions_mm"] = {"length": 6.6, "width": 6.2, "height": 2.5}
        part["dimension_reference"] = {
            "document": "IRLU024NPBF datasheet (C3024 provenance)",
            "pages": [1],
            "notes": "TO-251-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-251-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLU024NPBF (C3024); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-251-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3025 / Infineon Technologies IRFU120NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_100_volt_9_4_amp_infineon_technologies_irfu120npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-251-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887163946094592-C3025.pdf"
        part["dimensions_mm"] = {"length": 6.6, "width": 6.2, "height": 2.5}
        part["dimension_reference"] = {
            "document": "IRFU120NPBF datasheet (C3025 provenance)",
            "pages": [1],
            "notes": "TO-251-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-251-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFU120NPBF (C3025); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-251-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3027 / Infineon Technologies IRFU220NPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_200_volt_5_amp_infineon_technologies_irfu220npbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-251-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887091577438208-C3027.pdf"
        part["dimensions_mm"] = {"length": 6.6, "width": 6.2, "height": 2.5}
        part["dimension_reference"] = {
            "document": "IRFU220NPBF datasheet (C3027 provenance)",
            "pages": [1],
            "notes": "TO-251-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-251-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFU220NPBF (C3027); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-251-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3031 / Infineon Technologies IRFU3910PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_100_volt_16_amp_infineon_technologies_irfu3910pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-251-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887286779400192-C3031.pdf"
        part["dimensions_mm"] = {"length": 6.6, "width": 6.2, "height": 2.5}
        part["dimension_reference"] = {
            "document": "IRFU3910PBF datasheet (C3031 provenance)",
            "pages": [1],
            "notes": "TO-251-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+175 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-251-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFU3910PBF (C3031); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-251-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3032 / Infineon Technologies IRFU5410PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_251_mosfet_p_channel_enhancement_mode_100_volt_13_amp_infineon_technologies_irfu5410pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-251-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887163983708160-C3032.pdf"
        part["dimensions_mm"] = {"length": 6.6, "width": 6.2, "height": 2.5}
        part["dimension_reference"] = {
            "document": "IRFU5410PBF datasheet (C3032 provenance)",
            "pages": [1],
            "notes": "TO-251-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-251-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRFU5410PBF (C3032); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-251-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3033 / Vishay Intertech IRFU9024PBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_251_mosfet_p_channel_enhancement_mode_60_volt_8_8_amp_vishay_intertech_irfu9024pbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-251-3_Vertical (mosfet-p, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588891881971863552-C3033.pdf"
        part["dimensions_mm"] = {"length": 6.6, "width": 6.2, "height": 2.5}
        part["dimension_reference"] = {
            "document": "IRFU9024PBF datasheet (C3033 provenance)",
            "pages": [1],
            "notes": "TO-251-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-251-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRFU9024PBF (C3033); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GDS master and the Package_TO_SOT_THT:TO-251-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3034 / Infineon Technologies IRLML6401TRPBF - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_p_channel_enhancement_mode_12_volt_4_3_amp_infineon_technologies_irlml6401trpbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-p, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711393148289024-C3034.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "IRLML6401TRPBF datasheet (C3034 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Infineon Technologies IRLML6401TRPBF (C3034); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3055 / Vishay Intertech IRF830APBF - transistor family batch 2026-10-06
    current = "electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_500_volt_5_amp_vishay_intertech_irf830apbf"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-220-3_Vertical (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588896300788568064-C3055.pdf"
        part["dimensions_mm"] = {"length": 10.0, "width": 4.4, "height": 9.2}
        part["dimension_reference"] = {
            "document": "IRF830APBF datasheet (C3055 provenance)",
            "pages": [1],
            "notes": "TO-220-3_Vertical master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_THT:TO-220-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech IRF830APBF (C3055); identity and ratings observed live at intake 2026-09-29.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_THT:TO-220-3_Vertical footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5386 / onsemi FQD2N60CTM - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_600_volt_1_9_amp_onsemi_fqd2n60ctm"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (mosfet-n, pins GDS)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579711516146253824-C5386.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "FQD2N60CTM datasheet (C5386 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order GDS per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "D", "type": "passive"},
            "pin_3": {"number": "3", "name": "S", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GDS",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi FQD2N60CTM (C5386); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GDS master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order GDS verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5424 / onsemi MJD45H11G - transistor family batch 2026-10-06
    current = "electronic_transistor_to_252_bipolar_pnp_80_volt_8_amp_onsemi_mjd45h11g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-252-3_TabPin2 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588905629607989248-C5424.pdf"
        part["dimensions_mm"] = {"length": 6.5, "width": 6.1, "height": 2.3}
        part["dimension_reference"] = {
            "document": "MJD45H11G datasheet (C5424 provenance)",
            "pages": [1],
            "notes": "TO-252-3_TabPin2 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:TO-252-3_TabPin2",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi MJD45H11G (C5424); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:TO-252-3_TabPin2 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5439 / onsemi MJD44H11-1G - transistor family batch 2026-10-06
    current = "electronic_transistor_to_251_bipolar_npn_80_volt_8_amp_onsemi_mjd44h11_1g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-251-3_Vertical (bjt-npn, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887286737592320-C5439.pdf"
        part["dimensions_mm"] = {"length": 6.6, "width": 6.2, "height": 2.5}
        part["dimension_reference"] = {
            "document": "MJD44H11-1G datasheet (C5439 provenance)",
            "pages": [1],
            "notes": "TO-251-3_Vertical master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_THT:TO-251-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi MJD44H11-1G (C5439); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_BEC master and the Package_TO_SOT_THT:TO-251-3_Vertical footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C5440 / onsemi MJD45H11-1G - transistor family batch 2026-10-06
    current = "electronic_transistor_to_251_bipolar_pnp_80_volt_8_amp_onsemi_mjd45h11_1g"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "TO-251-3_Vertical (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588887286737592321-C5440.pdf"
        part["dimensions_mm"] = {"length": 6.6, "width": 6.2, "height": 2.5}
        part["dimension_reference"] = {
            "document": "MJD45H11-1G datasheet (C5440 provenance)",
            "pages": [1],
            "notes": "TO-251-3_Vertical master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_THT:TO-251-3_Vertical",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists onsemi MJD45H11-1G (C5440); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_THT:TO-251-3_Vertical footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C6903 / Vishay Intertech SI2343CDS-T1-GE3 - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_p_channel_enhancement_mode_30_volt_4_amp_vishay_intertech_si2343cds_t1_ge3"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-p, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586178050111651840-C6903.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SI2343CDS-T1-GE3 datasheet (C6903 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "P-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_PMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Vishay Intertech SI2343CDS-T1-GE3 (C6903); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Transistor_FET:Q_PMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C8542 / Jiangsu Changjing Electronics Technology Co., Ltd. SS8550 Y2(RANGE:200-350) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_pnp_25_volt_1_5_amp_jiangsu_changjing_electronics_technology_co_ltd_ss8550_y2_range_200_350"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707479441063936-C8542.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "SS8550 Y2(RANGE:200-350) datasheet (C8542 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. SS8550 Y2(RANGE:200-350) (C8542); identity and ratings observed live at intake 2026-09-25.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C8543 / Jiangsu Changjing Electronics Technology Co., Ltd. S9012 2T1(RANGE:200-350) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_bipolar_pnp_25_volt_500_milliamp_jiangsu_changjing_electronics_technology_co_ltd_s9012_2t1_range_200_350"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (bjt-pnp, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8586172953784963072-C8543.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "S9012 2T1(RANGE:200-350) datasheet (C8543 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "PNP",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_PNP_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. S9012 2T1(RANGE:200-350) (C8543); identity and ratings observed live at intake 2026-09-25.",
            "Mapped to the KiCad Transistor_BJT:Q_PNP_BEC master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C8545 / Jiangsu Changjing Electronics Technology Co., Ltd. 2N7002 - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_jiangsu_changjing_electronics_technology_co_ltd_2n7002"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-23 (mosfet-n, pins GSD)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8550724090240786432-C8545.pdf"
        part["dimensions_mm"] = {"length": 2.9, "width": 1.3, "height": 1.1}
        part["dimension_reference"] = {
            "document": "2N7002 datasheet (C8545 provenance)",
            "pages": [1],
            "notes": "SOT-23 master geometry; pin order GSD per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "N-channel",
            "device_type": "power MOSFET (enhancement mode)",
            "operating_temperature": "-55 to +150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "G", "type": "input"},
            "pin_2": {"number": "2", "name": "S", "type": "passive"},
            "pin_3": {"number": "3", "name": "D", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_FET:Q_NMOS_GSD",
            "machine_solder": "Package_TO_SOT_SMD:SOT-23",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. 2N7002 (C8545); identity and ratings observed live at intake 2026-09-25.",
            "Mapped to the KiCad Transistor_FET:Q_NMOS_GSD master and the Package_TO_SOT_SMD:SOT-23 footprint master in the 2026-10-06 family batch; pin order GSD verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C9634 / Jiangsu Changjing Electronics Technology Co., Ltd. D882(RANGE:160-320) - transistor family batch 2026-10-06
    current = "electronic_transistor_sot_89_3_bipolar_npn_30_volt_3_amp_jiangsu_changjing_electronics_technology_co_ltd_d882_range_160_320"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "SOT-89-3 (bjt-npn, pins BEC)"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579707511542370304-C9634.pdf"
        part["dimensions_mm"] = {"length": 4.5, "width": 2.5, "height": 1.5}
        part["dimension_reference"] = {
            "document": "D882(RANGE:160-320) datasheet (C9634 provenance)",
            "pages": [1],
            "notes": "SOT-89-3 master geometry; pin order BEC per the part datasheet.",
        }
        part["electrical"] = {
            "polarity": "NPN",
            "device_type": "bipolar junction transistor",
            "operating_temperature": "-55 C~+150 C"
        }
        part["pins"] = {
            "pin_1": {"number": "1", "name": "B", "type": "input"},
            "pin_2": {"number": "2", "name": "E", "type": "passive"},
            "pin_3": {"number": "3", "name": "C", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Transistor_BJT:Q_NPN_BEC",
            "machine_solder": "Package_TO_SOT_SMD:SOT-89-3",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists Jiangsu Changjing Electronics Technology Co., Ltd. D882(RANGE:160-320) (C9634); identity and ratings observed live at intake 2026-09-25.",
            "Mapped to the KiCad Transistor_BJT:Q_NPN_BEC master and the Package_TO_SOT_SMD:SOT-89-3 footprint master in the 2026-10-06 family batch; pin order BEC verified against the part datasheet.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated transistor batch (tmp/transistor_batch.py) ===