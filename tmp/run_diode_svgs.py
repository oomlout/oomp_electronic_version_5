import sys
sys.path.insert(0, r'C:\gh\oomlout_svg_version_5')
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import working_svg

for part_id in [
    "electronic_diode_schottky_sod_123_ss14",
    "electronic_diode_schottky_sod_323_bat54w",
    "electronic_diode_schottky_sod_523_1ss400",
]:
    print(f"Generating SVGs for {part_id}...")
    working_svg.main(part_id=part_id, filter="", regenerate_pngs=True)
    print(f"  Done")

print("All SVGs generated")
