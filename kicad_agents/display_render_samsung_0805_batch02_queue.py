"""Prepare more individually evidenced Samsung 0805 illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0805_BATCH02_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0805_100_nano_farad': ('CL21B104KCFNNNE', 'C28233', '100 nF', '100 V', '10%', 'X7R'),
    'electronic_capacitor_0805_10_micro_farad': ('CL21A106KAYNNNE', 'C15850', '10 uF', '25 V', '10%', 'X5R'),
    'electronic_capacitor_0805_47_micro_farad': ('CL21A476MQYNNNE', 'C16780', '47 uF', '6.3 V', '20%', 'X5R'),
    'electronic_capacitor_0805_1_micro_farad': ('CL21B105KBFNNNE', 'C28323', '1 uF', '50 V', '10%', 'X7R'),
    'electronic_capacitor_0805_1_micro_farad_25_volt': ('CL21B105KAFNFNE', 'C1712', '1 uF', '25 V', '10%', 'X7R'),
    'electronic_capacitor_0805_1_micro_farad_samsung_electro_mechanics_cl21f105zbfnnne': ('CL21F105ZBFNNNE', 'C5422', '1 uF', '50 V', '-20%~+80%', 'Y5V'),
    'electronic_capacitor_0805_220_nano_farad': ('CL21B224KBFNNNE', 'C5378', '220 nF', '50 V', '10%', 'X7R'),
    'electronic_capacitor_0805_220_nano_farad_samsung_electro_mechanics_cl21b224kafnnne': ('CL21B224KAFNNNE', 'C5153', '220 nF', '25 V', '10%', 'X7R'),
    'electronic_capacitor_0805_470_nano_farad': ('CL21B474KBFNNNE', 'C13967', '470 nF', '50 V', '10%', 'X7R'),
    'electronic_capacitor_0805_2_2_nano_farad': ('CL21C222JBFNNNE', 'C28260', '2.2 nF', '50 V', '5%', 'C0G'),
    'electronic_capacitor_0805_2_2_micro_farad_16_volt': ('CL21A225KOFNNNE', 'C1731', '2.2 uF', '16 V', '10%', 'X5R'),
    'electronic_capacitor_0805_4_7_micro_farad_16_volt': ('CL21A475KOFNNNE', 'C1746', '4.7 uF', '16 V', '10%', 'X5R'),
}
NO_ELECTRICAL = frozenset(list(PARTS)[i] for i in (0, 1, 2, 3, 5, 7, 8, 9))


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    return base_recipe(part, record, recipes, sha,
                       parts={p: data[:5] for p, data in PARTS.items()},
                       no_electrical=NO_ELECTRICAL, evidence=EVIDENCE,
                       dielectric=PARTS[part][5])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {p: reviewed_recipe(p, yaml.safe_load((ROOT / 'parts_source' / p / 'working.yaml').read_text(encoding='utf8')), recipes, sha)
             for p in PARTS if p not in recipes}
    if args.add:
        recipes.update(found)
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    for part, recipe in found.items():
        print(part, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
