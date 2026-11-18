"""Prepare evidenced 1.25 mm 1206 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_470nf_queue import PART as PILOT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_1206_125_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_680_nano_farad': ('FH (Guangdong Fenghua Advanced Tech)', '1206B684K500NT', 'C1881', '680 nF', '50 V'),
    'electronic_capacitor_1206_100_nano_farad_100_volt': ('Samsung Electro-Mechanics', 'CL31B104KCFNNNE', 'C1945', '100 nF', '100 V'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    maker, mpn, lcsc, value, voltage = PARTS[part]
    if record.get('manufacturer') != maker or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == maker and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1206_3216Metric':
        raise ValueError('Footprint changed')
    if record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6}:
        raise ValueError('Source dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', value), ('rated_voltage', voltage), ('dielectric', 'X7R'), ('tolerance', '10%')):
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '1206_imperial_3216_metric' or r['model'].get('display_scale_xyz') != [1.0, 1.0, .78125]:
        raise ValueError('Unexpected source model')
    r.update(represented_manufacturer=maker, represented_mpn=mpn)
    r['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Individual manufacturer pages reviewed online',
                                'source_record': f'parts_source/{part}/working.yaml'}
    r['appearance_status'] = ('Generic KiCad 1206 model scaled to the selected part’s 1.25 mm nominal height; '
                              'shape details, ceramic colour and metallic terminations are illustrative.')
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
