content = open('kicad_agents/oomp_matching_agent.py').read()

old = '        for pkg_token in ["sod_123", "sod_323", "sod_523f", "sod_523", "sot_23", "sot_143", "sot_523", "d_0402", "d_0603"]:'
new = '        for pkg_token in ["sod_123", "sod_323", "sod_523f", "sod_523", "sot_23", "sot_143", "sot_523", "d_0402", "d_0603"]:'

# sod_523 is already there! Let me verify
if old in content:
    print("sod_523 already in matcher")
else:
    print("NOT FOUND - checking current tokens")
    # Find the line
    for i, line in enumerate(content.split('\n')):
        if 'pkg_token' in line and 'sod_' in line:
            print(f"Line {i}: {line}")
