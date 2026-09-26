def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    # Apply individually reviewed JLC house choices after other supplier data.
    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="resistor_array")
