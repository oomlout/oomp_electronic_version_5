def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_resistor_0402_510000_ohm"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer_uni_royal"] = "0402WGF5103TCE"
        extras_dict[current]["part_number_lcsc_uni_royal"] = "C11616"
