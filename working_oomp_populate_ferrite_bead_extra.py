def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_ferrite_bead_0805_220_ohm_2_amp_murata_blm21pg221sn1d"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer"] = "BLM21PG221SN1D"
        extras_dict[current]["part_number_lcsc"] = "C85840"
