import re

# Fix the extra populate file - remove manufacturer = "Generic" lines
content = open('working_oomp_populate_diode_extra.py').read()

# Remove the three manufacturer = "Generic" lines for generic diodes
content = re.sub(
    r'(current = "electronic_diode_schottky_sod_\d+_generic_\w+"\r?\n    if current in extras_dict:\r?\n        part = extras_dict\[current\]\r?\n)        part\["manufacturer"\] = "Generic"\r?\n',
    r'\1',
    content
)
content = re.sub(
    r'(current = "electronic_diode_schottky_0402_generic_\w+"\r?\n    if current in extras_dict:\r?\n        part = extras_dict\[current\]\r?\n)        part\["manufacturer"\] = "Generic"\r?\n',
    r'\1',
    content
)

open('working_oomp_populate_diode_extra.py', 'w').write(content)
print("Fixed extra populate file")

# Fix parts_source working.yaml files
import yaml
for part_id in [
    "electronic_diode_schottky_sod_123_generic_ss14",
    "electronic_diode_schottky_sod_323_generic_bat54w",
    "electronic_diode_schottky_0402_generic_1ss400",
]:
    path = f"parts_source/{part_id}/working.yaml"
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if data.get("manufacturer") == "Generic":
        del data["manufacturer"]
    if data.get("taxonomy_14") == "generic":
        del data["taxonomy_14"]
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)
    print(f"  Fixed parts_source/{part_id}/working.yaml")

    # Fix parts working.yaml
    path2 = f"parts/{part_id}/working.yaml"
    with open(path2, "r", encoding="utf-8") as f:
        data2 = yaml.safe_load(f)
    if data2.get("manufacturer") == "Generic":
        del data2["manufacturer"]
    if data2.get("taxonomy_14") == "generic":
        del data2["taxonomy_14"]
    with open(path2, "w", encoding="utf-8") as f:
        yaml.dump(data2, f, sort_keys=False, allow_unicode=True)
    print(f"  Fixed parts/{part_id}/working.yaml")

print("Done")
