import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')
sys.path.insert(0, r'C:\gh\oomlout_svg_version_5')
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import yaml
import oomlout_roboclick
import working_svg

part_ids = [
    "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_5_volt_advanced_monolithic_systems_ams1117_5",
    "electronic_ic_sot_23_power_management_linear_voltage_regulator_3_3_volt_torex_xc6206p332mr",
    "electronic_ic_sot_23_power_management_linear_voltage_regulator_5_volt_torex_xc6206p502mr",
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

print("\nAll regulators complete")
