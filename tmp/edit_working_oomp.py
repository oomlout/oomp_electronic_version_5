content = open('run_working_oomp.py').read()

old = '''filters = [
    "electronic_resistor_0402_2400_ohm",
    "electronic_crystal_3225_surface_mount_4_pin_16_mhz",
    "electronic_crystal_5032_surface_mount_2_pin_8_mhz",
    "electronic_crystal_3215_surface_mount_2_pin_32_768_khz",
    "mechanical_mounting_hole_2_2_mm",
    "navigation",
]'''

new = '''filters = [
    "electronic_resistor_0402_2400_ohm",
    "electronic_crystal_3225_surface_mount_4_pin_16_mhz",
    "electronic_crystal_5032_surface_mount_2_pin_8_mhz",
    "electronic_crystal_3215_surface_mount_2_pin_32_768_khz",
    "mechanical_mounting_hole_2_2_mm",
    "electronic_capacitor_0603_33_pico_farad",
    "electronic_capacitor_0603_47_pico_farad",
    "navigation",
]'''

if old not in content:
    print("OLD NOT FOUND")
    print(repr(old))
else:
    content = content.replace(old, new)
    open('run_working_oomp.py', 'w').write(content)
    print("done")
