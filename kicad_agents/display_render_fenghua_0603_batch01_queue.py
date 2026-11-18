"""Prepare individually evidenced Fenghua 0603 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0603_batch01_queue import PILOT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0603_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0603_100_pico_farad_fenghua_adv_tech_0603cg101j500nt': ('0603CG101J500NT', 'C1635', '100 pF'),
    'electronic_capacitor_0603_120_pico_farad': ('0603CG121J500NT', 'C1643', '120 pF'),
    'electronic_capacitor_0603_150_pico_farad_fenghua_adv_tech_0603cg151j500nt': ('0603CG151J500NT', 'C1645', '150 pF'),
}
MAKER = 'FH (Guangdong Fenghua Advanced Tech)'


def reviewed_recipe(part, record, recipes, sha, *, parts=None, evidence=None):
    parts = PARTS if parts is None else parts
    evidence = EVIDENCE if evidence is None else evidence
    if part not in parts:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value = parts[part]
    if record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MAKER and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0603_1608Metric':
        raise ValueError('Footprint changed')
    dims = record.get('dimensions_mm') or {}
    if dims.get('length') != 1.6 or dims.get('width') != .8 or dims.get('height', .8) != .8:
        raise ValueError('Dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', value), ('rated_voltage', '50 V'), ('dielectric', 'C0G'), ('tolerance', '5%')):
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0603_imperial_1608_metric':
        raise ValueError('Unexpected source model')
    r.update(represented_manufacturer=MAKER, represented_mpn=mpn)
    r['marking'].update(policy='unmarked_illustration',
        evidence={'file': evidence.as_posix(), 'sha256': sha, 'document': 'Individual Fenghua product page reviewed online',
                  'source_record': f'parts_source/{part}/working.yaml'},
        appearance_status='Unmarked body is illustrative; the selected part’s no-marking policy has not been verified.')
    r['appearance_status'] = ('Generic KiCad nominal 0603 MLCC geometry with illustrative ceramic colour and metallic terminations; '
                              'represents the selected Fenghua part.')
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
