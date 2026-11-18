"""Prepare the reviewed Murata GRM21BR61H106KE43L illustration."""
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_0805_10_micro_farad_50_volt'
PILOT = 'electronic_capacitor_0805_10_micro_farad_16_volt'
EVIDENCE = Path('parts_source') / PART / 'datasheet.pdf'

def reviewed_recipe(part, record, recipes, sha):
    if part != PART or record.get('manufacturer') != 'Murata Electronics' or record.get('part_number_manufacturer') != 'GRM21BR61H106KE43L':
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == 'Murata Electronics' and x.get('part_number') == 'GRM21BR61H106KE43L' for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C440198' for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0805_2012Metric':
        raise ValueError('Footprint changed')
    dims = record.get('dimensions_mm') or {}
    if (dims.get('length'), dims.get('width'), dims.get('height')) != (2.0, 1.25, 1.25):
        raise ValueError('Dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', '10 uF'), ('rated_voltage', '50 V'), ('dielectric', 'X5R'), ('tolerance', '10%')):
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0805_imperial_2012_metric' or r.get('model', {}).get('expected_bounds_mm') != [2.0, 1.25, 1.25]:
        raise ValueError('Unexpected source model')
    r.update(represented_manufacturer='Murata Electronics', represented_mpn='GRM21BR61H106KE43L')
    r['marking'].update(policy='unmarked_illustration', evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Murata GRM21BR61H106KE43-01A, page 1', 'source_record': f'parts_source/{part}/working.yaml'}, appearance_status='Unmarked body is illustrative; the selected part’s no-marking policy has not been verified.')
    r['appearance_status'] = 'Generic KiCad 0805 MLCC geometry matches the dimensions in the Murata specification; ceramic colour and metallic terminations are illustrative.'
    return r

def main():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    if PART in recipes: raise ValueError('Recipe already exists')
    recipes[PART] = reviewed_recipe(PART, record, recipes, sha)
    RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART)

if __name__ == '__main__': main()
