content = open('kicad_agents/oomp_matching_agent.py').read()

# Add switch inference
old = '''    if reference.startswith("Y") and "crystal" in evidence:
        return "crystal"
    # USB-C and other connectors
    if "usb_c_receptacle" in evidence or "usb_c" in evidence:
        return "connector"
    if reference.startswith("J") and ("conn_" in evidence or "header" in evidence or "receptacle" in evidence):
        return "connector"
    return ""'''

new = '''    if reference.startswith("Y") and "crystal" in evidence:
        return "crystal"
    # USB-C and other connectors
    if "usb_c_receptacle" in evidence or "usb_c" in evidence:
        return "connector"
    if reference.startswith("J") and ("conn_" in evidence or "header" in evidence or "receptacle" in evidence):
        return "connector"
    # Switches: SW-prefixed references, or sw_push/sw_spst in evidence
    if reference.startswith("SW") or "sw_push" in evidence or "sw_spst" in evidence or "sw_tactile" in evidence:
        return "switch"
    return ""'''

assert old in content, "old not found"
content = content.replace(old, new)

open('kicad_agents/oomp_matching_agent.py', 'w').write(content)
print("done")
