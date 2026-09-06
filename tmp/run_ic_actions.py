import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')
sys.path.insert(0, r'C:\gh\oomlout_svg_version_5')
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import yaml
import oomlout_roboclick
import working_svg

part_ids = [
    "electronic_ic_tqfp_32_7_mm_x_7_mm_microcontroller_8_bit_avr_microchip_atmega328p_au",
    "electronic_ic_sop_16_converter_usb_to_serial_converter_wch_ch340c",
    "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102n_a01_gqfn28r",
    "electronic_ic_esp32_s3_wroom_1_microcontroller_wifi_bluetooth_8_mb_flash_espressif_esp32_s3_wroom_1_n8",
]

for part_id in part_ids:
    part_dir = f"parts/{part_id}"
    print(f"\n=== {part_id} ===")
    
    # Run roboclick actions
    with open(f"{part_dir}/working.yaml", "r", encoding="utf-8") as f:
        working = yaml.safe_load(f)
    modes = []
    for key, value in working.items():
        if str(key).startswith("oomlout_ai_roboclick_") and isinstance(value, dict):
            if isinstance(value.get("actions"), list):
                modes.append(str(key))
    for mode in sorted(modes):
        print(f"  Running {mode}...")
        try:
            oomlout_roboclick.run_folder(folder=part_dir, mode=[mode])
            print(f"    Done")
        except Exception as e:
            print(f"    Error: {e}")
    
    # Generate SVGs (no PNG - Cairo not available)
    print(f"  Generating SVGs...")
    working_svg.main(part_id=part_id, filter="", regenerate_pngs=False)
    print(f"    Done")

print("\nAll ICs complete")
