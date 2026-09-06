def main(**kwargs):
    """Apply the browser-researched LCSC/manufacturer picks to parts.

    The literal rows live in working_oomp_populate_lcsc_research_data.py.
    Merge semantics: existing manufacturer identity (e.g. the JST data
    table) is kept; missing LCSC numbers and listing details are added.
    """
    extras_dict = kwargs.get("extras_dict", {})
    import working_oomp_populate_lcsc_research_data

    for part_id, research in working_oomp_populate_lcsc_research_data.LCSC_RESEARCH.items():
        part = extras_dict.get(part_id)
        if part is None:
            continue
        notes = list(part.get("research_notes", []))
        lcsc_code = research.get("part_number_lcsc", "")
        manufacturer = research.get("manufacturer", "")
        mpn = research.get("part_number_manufacturer", "")
        if not part.get("part_number_lcsc") and lcsc_code:
            part["part_number_lcsc"] = lcsc_code
            part["product_url"] = f"https://www.lcsc.com/product-detail/{lcsc_code}.html"
            part["part_numbers_lcsc"] = [
                {
                    "part_number": lcsc_code,
                    "product_name": research.get("lcsc_description", ""),
                }
            ]
            notes.append(
                "LCSC stock research 2026-09 (batch): highest-stock in-stock listing "
                f"for query \"{research.get('lcsc_query', '')}\" ({research.get('lcsc_stock', 0):,} in stock at capture)."
            )
        if not part.get("part_number_manufacturer") and mpn:
            if manufacturer:
                part["manufacturer"] = manufacturer
            part["part_number_manufacturer"] = mpn
            part["part_numbers_manufacturer"] = (
                [{"manufacturer": manufacturer, "part_number": mpn}] if manufacturer else []
            )
        if notes and notes != part.get("research_notes", []):
            part["research_notes"] = notes


if __name__ == "__main__":
    main()
