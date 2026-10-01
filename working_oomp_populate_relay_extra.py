def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    # Apply explicitly promoted browser-reviewed JLC identities (manufacturer,
    # MPN, LCSC code) to the relay family, matching the other families'
    # reviewed-choice enrichment.
    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="relay")
