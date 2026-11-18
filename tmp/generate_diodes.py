import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')

import working_oomp

parts = [
    "electronic_diode_schottky_sod_123_ss14",
    "electronic_diode_schottky_sod_323_bat54w",
    "electronic_diode_schottky_sod_523_1ss400",
]

for part in parts:
    print(f"Generating {part}...")
    working_oomp.main(filter=part, regenerate_pngs=False)
    print(f"Done {part}")
