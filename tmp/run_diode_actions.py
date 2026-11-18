import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import yaml
import oomlout_roboclick

part_ids = [
    "electronic_diode_schottky_sod_123_ss14",
    "electronic_diode_schottky_sod_323_bat54w",
    "electronic_diode_schottky_sod_523_1ss400",
]

for part_id in part_ids:
    part_dir = f"parts/{part_id}"
    
    # Load working.yaml to find action modes
    with open(f"{part_dir}/working.yaml", "r", encoding="utf-8") as f:
        working = yaml.safe_load(f)

    modes = []
    for key, value in working.items():
        if str(key).startswith("oomlout_ai_roboclick_") and isinstance(value, dict):
            if isinstance(value.get("actions"), list):
                modes.append(str(key))

    print(f"Running actions for {part_id}: {modes}")

    # Run each mode
    for mode in sorted(modes):
        print(f"  Running {mode}...")
        try:
            oomlout_roboclick.run_folder(folder=part_dir, mode=[mode])
            print(f"    Done")
        except Exception as e:
            print(f"    Error: {e}")

print("All actions complete")
