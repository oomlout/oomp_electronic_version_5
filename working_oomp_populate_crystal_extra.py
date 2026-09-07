def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer_yxc"] = "X322512MSB4SI"
        extras_dict[current]["part_number_lcsc_yxc"] = "C9002"
