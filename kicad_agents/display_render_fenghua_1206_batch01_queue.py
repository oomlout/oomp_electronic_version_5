"""Prepare individually evidenced Fenghua 1206 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_10nf_queue import PART as PILOT, MAKER

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_150_pico_farad_fenghua_adv_tech_1206cg151j500nt': ('1206CG151J500NT', 'C1888', '150 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_18_pico_farad': ('1206CG180J500NT', 'C1889', '18 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_330_nano_farad': ('1206B334K500NT', 'C1865', '330 nF', 'X7R', '10%'),
    'electronic_capacitor_1206_470_pico_farad': ('1206B471K500NT', 'C1868', '470 pF', 'X7R', '10%'),
    'electronic_capacitor_1206_680_pico_farad_fenghua_adv_tech_1206cg681j500nt': ('1206CG681J500NT', 'C1923', '680 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_6_8_nano_farad': ('1206B682K500NT', 'C1879', '6.8 nF', 'X7R', '10%'),
}


def reviewed_recipe(part, record, recipes, sha, *, parts=PARTS, evidence=EVIDENCE):
    if part not in parts:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value, dielectric, tolerance = parts[part]
    if record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MAKER and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1206_3216Metric':
        raise ValueError('Footprint changed')
    if record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6}:
        raise ValueError('Source dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', value), ('rated_voltage', '50 V'), ('dielectric', dielectric), ('tolerance', tolerance)):
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '1206_imperial_3216_metric' or r['model'].get('display_scale_xyz') != [1.0, 1.0, .5]:
        raise ValueError('Unexpected source model')
    r['represented_mpn'] = mpn
    r['marking']['evidence'] = {'file': evidence.as_posix(), 'sha256': sha, 'document': 'Individual Fenghua catalogue entries reviewed online',
                                 'source_record': f'parts_source/{part}/working.yaml'}
    return r


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
