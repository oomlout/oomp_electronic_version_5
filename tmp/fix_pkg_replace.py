content = open('kicad_agents/oomp_matching_agent.py').read()

old = '''        # Determine package from footprint
        package = ""
        for pkg_token in ["sod_123", "sod_323", "sod_523f", "sod_523", "sot_23", "sot_143", "sot_523", "d_0402", "d_0603"]:
            if pkg_token in footprint_text or pkg_token in library_text:
                package = pkg_token.replace("d_", "")
                break'''

new = '''        # Determine package from footprint
        package = ""
        for pkg_token in ["sod_123", "sod_323", "sod_523f", "sod_523", "sot_23", "sot_143", "sot_523", "d_0402", "d_0603"]:
            if pkg_token in footprint_text or pkg_token in library_text:
                if pkg_token.startswith("d_"):
                    package = pkg_token[2:]
                else:
                    package = pkg_token
                break'''

assert old in content, "old not found"
content = content.replace(old, new)
open('kicad_agents/oomp_matching_agent.py', 'w').write(content)
print("done")
