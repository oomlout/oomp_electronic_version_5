def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    current = "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf"
    if current in extras_dict:
        extras_dict[current]["part_number_manufacturer_yxc"] = "X322512MSB4SI"
        extras_dict[current]["part_number_lcsc_yxc"] = "C9002"

    current = "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf_80_ohm_esr"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_oomp_id"] = "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf"
        part["category"] = "crystal"
        part["electrical"] = {
            "frequency": "12 MHz",
            "load_capacitance": "20 pF",
            "equivalent_series_resistance": "80 ohm",
            "frequency_tolerance": "+/-10 ppm",
            "frequency_stability": "+/-20 ppm",
            "operating_temperature": "-40 to +85 C",
        }
        part["research_notes"] = [
            "80 ohm ESR purchasing variant. The generic 12 MHz 20 pF choice retains its 50 ohm C133334 preference.",
            "Pad orientation and crystal pin mapping remain for the full pass.",
        ]

    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="crystal")
