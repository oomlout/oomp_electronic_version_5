def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_ferrite_bead_0805_220_ohm_2_amp_murata_blm21pg221sn1d"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "BLM21PG221SN1D"
        extras_dict[current]["part_number_lcsc"] = "C85840"

    current = "electronic_ferrite_bead_0805_15_ohm_1_5_amp_tdk_mmz2012r150at000"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "MMZ2012R150AT000"
        extras_dict[current]["part_number_manufacturer_tdk"] = "MMZ2012R150AT000"
        extras_dict[current]["part_number_lcsc"] = "C275464"
        extras_dict[current]["manufacturer"] = "TDK"
        extras_dict[current]["product_url"] = "https://www.lcsc.com/product-detail/C275464.html"
        extras_dict[current]["product_url_manufacturer"] = "https://product.tdk.com/en/search/emc/emc/beads/info?part_no=MMZ2012R150AT000"
        extras_dict[current]["datasheet_url"] = "https://product.tdk.com/en/system/files/dam/doc/product/emc/emc/beads/catalog/beads_commercial_signal_mmz2012_en.pdf"
        extras_dict[current]["datasheet_url_lcsc"] = "https://www.lcsc.com/datasheet/C275464.pdf"
        extras_dict[current]["package_name_manufacturer"] = "MMZ2012"
        extras_dict[current]["electrical"] = {
            "impedance_at_100_mhz": "15 ohm",
            "impedance_tolerance": "+/-25%",
            "maximum_dc_resistance": "0.05 ohm",
            "maximum_rated_current": "1.5 A",
            "operating_temperature": "-55 to +125 C",
        }
        extras_dict[current]["ferrite_bead_dimensions_mm"] = {
            "body_length": 2.0,
            "body_length_tolerance": 0.2,
            "body_width": 1.25,
            "body_width_tolerance": 0.2,
            "body_height": 0.85,
            "body_height_tolerance": 0.2,
            "terminal_length": 0.5,
            "terminal_length_tolerance": 0.3,
            "recommended_pad_length": 0.8,
            "recommended_pad_width": 1.2,
            "recommended_pad_gap": 1.0,
        }
        extras_dict[current]["pins"] = {}
        ferrite_bead_pins = [
            ["1", "terminal_1"],
            ["2", "terminal_2"],
        ]
        for pin_index in range(len(ferrite_bead_pins)):
            pin = ferrite_bead_pins[pin_index]
            extras_dict[current]["pins"][f"pin_{pin_index + 1}"] = {
                "number": pin[0],
                "name": pin[1],
                "type": "passive",
            }
        extras_dict[current]["research_notes"] = [
            "The Bus Pirate historical supplier URL resolves to TDK MMZ2012R150AT000, LCSC C275464.",
            "The schematic value 1.5A is the rated current; the component is a 15 ohm at 100 MHz ferrite bead.",
        ]
        extras_dict[current]["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
