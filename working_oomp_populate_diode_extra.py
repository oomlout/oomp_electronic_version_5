def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_diode_tvs_array_sot_23_6_protek_srv054pt7"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "SRV05-4-P-T7"
        extras_dict[current]["part_number_lcsc"] = "C85364"
