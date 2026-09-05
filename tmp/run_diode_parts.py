import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import working_oomp

for part_id in [
    "electronic_diode_schottky_sod_123_generic_ss14",
    "electronic_diode_schottky_sod_323_generic_bat54w",
    "electronic_diode_schottky_0402_generic_1ss400",
]:
    print(f"Generating {part_id}...")
    working_oomp.main(filter=part_id, regenerate_pngs=False)
    print(f"  Done")

print("All diode parts generated")
