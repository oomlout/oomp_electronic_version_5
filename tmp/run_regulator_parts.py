import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import working_oomp

for part_id in [
    "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_5_volt_advanced_monolithic_systems_ams1117_5",
    "electronic_ic_sot_23_power_management_linear_voltage_regulator_3_3_volt_torex_xc6206p332mr",
    "electronic_ic_sot_23_power_management_linear_voltage_regulator_5_volt_torex_xc6206p502mr",
]:
    print(f"Generating part {part_id}...")
    working_oomp.main(filter=part_id, regenerate_pngs=False)
    print(f"  Done")

print("All parts generated")
