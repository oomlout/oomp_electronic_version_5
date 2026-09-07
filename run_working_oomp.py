import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')

import working_oomp

# Generate new parts
filters = [
    "electronic_resistor_0402_2400_ohm",
    "electronic_crystal_3225_surface_mount_4_pin_16_mhz",
    "electronic_crystal_5032_surface_mount_2_pin_8_mhz",
    "electronic_crystal_3215_surface_mount_2_pin_32_768_khz",
    "mechanical_mounting_hole_2_2_mm",
    "electronic_capacitor_0603_33_pico_farad",
    "electronic_capacitor_0603_47_pico_farad",
    "navigation",
]

for f in filters:
    print(f"Generating {f}...")
    working_oomp.main(filter=f, regenerate_pngs=False)
    print(f"  Done")

print("All working_oomp done")
