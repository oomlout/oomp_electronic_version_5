import re


def _identity_token(value):
    return re.sub(r"[^a-z0-9]", "", str(value or "").lower())


def rejection_reason(part, research):
    """A search result cannot override an established purchasing identity."""
    if research.get("research_status") == "rejected":
        return research["rejection_reason"]
    if part.get("taxonomy_2") == "connector" and re.search(
        r"\b(diode|transistor|capacitor|resistor)\b",
        research.get("lcsc_description", ""), re.IGNORECASE,
    ):
        return "Supplier listing describes a different component category from this connector."
    for field in ("manufacturer", "part_number_manufacturer"):
        established = _identity_token(part.get(field))
        candidate = _identity_token(research.get(field))
        if established and established != candidate:
            return f"Supplier research {field} does not match the established component identity."
    if part.get("procurement_variant") and research.get("procurement_variant") != part["procurement_variant"]:
        return "Supplier research does not establish the required custom colour/finish variant."
    return ""


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
        reason = rejection_reason(part, research)
        if reason:
            # Keep the rejected evidence in the research table, never in the
            # active purchasing fields or manufacturer/distributor lists.
            if not part.get("part_number_lcsc"):
                part["lcsc_research_status"] = "rejected"
                part["procurement_notes"] = reason + " No verified LCSC replacement is assigned."
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
