content = open('kicad_agents/oomp_matching_agent.py').read()

# Edit 1: Add diode inference to infer_kind
old1 = '''    if reference.startswith("Q") or "transistor" in evidence or "mosfet" in evidence:
        return "transistor"
    # Generic through-hole pin headers: Conn_01xNN value + PinHeader_1xNN_P2.54mm evidence'''

new1 = '''    if reference.startswith("Q") or "transistor" in evidence or "mosfet" in evidence:
        return "transistor"
    # Diodes: D-prefixed references, or schottky/tvs/rectifier/zener in evidence
    if reference.startswith("D") and not reference.startswith("DN"):
        return "diode"
    if any(d in evidence for d in ["d_schottky", "d_tvs", "d_rectifier", "d_zener", "d_zener_sod"]):
        return "diode"
    # Generic through-hole pin headers: Conn_01xNN value + PinHeader_1xNN_P2.54mm evidence'''

assert old1 in content, "old1 not found"
content = content.replace(old1, new1)

# Edit 2: Add diode handling to proposed_oomp_id before the final return ""
old2 = '''    if kind == "crystal":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])

        # Parse frequency
        freq_match = re.search(r"(\d+(?:_\d+)?)[_\s]*(mhz|khz)", value_text)
        if not freq_match:
            return ""
        freq_num = freq_match.group(1).replace("_", ".")
        freq_unit = freq_match.group(2)
        if freq_unit == "mhz":
            freq_taxonomy = freq_num.replace(".", "_") + "_mhz"
        else:
            freq_taxonomy = freq_num.replace(".", "_") + "_khz"

        # Parse package and pin count from footprint
        pkg_match = re.search(r"crystal_smd_(\d+)_(\d)pin", footprint_text)
        if not pkg_match:
            return ""
        package = pkg_match.group(1)
        pin_count = pkg_match.group(2) + "_pin"

        # Default load capacitance by frequency
        if "32_768" in freq_taxonomy:
            load_cap = "12_5_pf"
        else:
            load_cap = "20_pf"

        return f"electronic_crystal_{package}_surface_mount_{pin_count}_{freq_taxonomy}_{load_cap}"

    return ""'''

new2 = '''    if kind == "crystal":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])

        # Parse frequency
        freq_match = re.search(r"(\d+(?:_\d+)?)[_\s]*(mhz|khz)", value_text)
        if not freq_match:
            return ""
        freq_num = freq_match.group(1).replace("_", ".")
        freq_unit = freq_match.group(2)
        if freq_unit == "mhz":
            freq_taxonomy = freq_num.replace(".", "_") + "_mhz"
        else:
            freq_taxonomy = freq_num.replace(".", "_") + "_khz"

        # Parse package and pin count from footprint
        pkg_match = re.search(r"crystal_smd_(\d+)_(\d)pin", footprint_text)
        if not pkg_match:
            return ""
        package = pkg_match.group(1)
        pin_count = pkg_match.group(2) + "_pin"

        # Default load capacitance by frequency
        if "32_768" in freq_taxonomy:
            load_cap = "12_5_pf"
        else:
            load_cap = "20_pf"

        return f"electronic_crystal_{package}_surface_mount_{pin_count}_{freq_taxonomy}_{load_cap}"

    if kind == "diode":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])
        library_text = normalize_text(fields["library_id"])

        # Determine diode type
        diode_type = ""
        if "schottky" in value_text or "schottky" in library_text:
            diode_type = "schottky"
        elif "tvs" in value_text or "tvs" in library_text or "esd" in value_text or "pesd" in value_text:
            diode_type = "tvs"
        elif "zener" in value_text or "zener" in library_text:
            diode_type = "zener"
        elif "switching" in value_text or "switching" in library_text:
            diode_type = "switching"
        elif "rectifier" in value_text or "rectifier" in library_text:
            diode_type = "rectifier"
        else:
            # Default for generic D_Schottky and similar
            diode_type = "schottky"

        # Determine package from footprint
        package = ""
        for pkg_token in ["sod_123", "sod_323", "sod_523f", "sod_523", "sot_23", "sot_143", "sot_523", "d_0402", "d_0603"]:
            if pkg_token in footprint_text or pkg_token in library_text:
                package = pkg_token.replace("d_", "")
                break

        if diode_type and package:
            return f"electronic_diode_{diode_type}_{package}"

    return ""'''

assert old2 in content, "old2 not found"
content = content.replace(old2, new2)

open('kicad_agents/oomp_matching_agent.py', 'w').write(content)
print("done")
