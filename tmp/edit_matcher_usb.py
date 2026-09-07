content = open('kicad_agents/oomp_matching_agent.py').read()

# Edit 1: Add USB-C connector inference to infer_kind
old1 = '''    if reference.startswith("Y") and "crystal" in evidence:
        return "crystal"
    return ""'''

new1 = '''    if reference.startswith("Y") and "crystal" in evidence:
        return "crystal"
    # USB-C and other connectors
    if "usb_c_receptacle" in evidence or "usb_c" in evidence:
        return "connector"
    if reference.startswith("J") and ("conn_" in evidence or "header" in evidence or "receptacle" in evidence):
        return "connector"
    return ""'''

assert old1 in content, "old1 not found"
content = content.replace(old1, new1)

# Edit 2: Add connector handling to proposed_oomp_id for USB-C
old2 = '''    if kind == "diode":
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
                if pkg_token.startswith("d_"):
                    package = pkg_token[2:]
                else:
                    package = pkg_token
                break

        if diode_type and package:
            return f"electronic_diode_{diode_type}_{package}"

    return ""'''

new2 = '''    if kind == "diode":
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
                if pkg_token.startswith("d_"):
                    package = pkg_token[2:]
                else:
                    package = pkg_token
                break

        if diode_type and package:
            return f"electronic_diode_{diode_type}_{package}"

    if kind == "connector":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])
        library_text = normalize_text(fields["library_id"])

        # USB-C receptacle
        if "usb_c" in value_text or "usb_c" in library_text or "usb_c" in footprint_text:
            return "electronic_connector_usb_c_surface_mount_16_pin"

    return ""'''

assert old2 in content, "old2 not found"
content = content.replace(old2, new2)

open('kicad_agents/oomp_matching_agent.py', 'w').write(content)
print("done")
