"""Prepare a source-checked 1206 Y5V illustration from secondary evidence."""
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_1206_2_2_micro_farad_fenghua_adv_tech_1206f225m250nt'
SOURCE = 'electronic_capacitor_1206_10_micro_farad_16_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_2U2_25V_SECONDARY_EVIDENCE.md')
MAKER = 'FH (Guangdong Fenghua Advanced Tech)'
MPN = '1206F225M250NT'

def reviewed_recipe(record, recipes, sha):
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != MPN
        or record.get('part_number_lcsc') != 'C1933' or e.get('capacitance') != '2.2 uF'
        or e.get('rated_voltage') != '25 V' or e.get('dielectric') != 'Y5V'
        or '20%' not in str(e.get('tolerance')) or e.get('polarized') is not False
        or record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1206_3216Metric'):
        raise ValueError('Identity, rating, dielectric or package changed')
    if not any(x.get('manufacturer') == MAKER and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    r = copy.deepcopy(recipes[SOURCE])
    if (r.get('family') != 'chip_capacitor' or r.get('package') != '1206_imperial_3216_metric'
        or r['model'].get('expected_bounds_mm') != [3.2, 1.6, 1.6]
        or r['model'].get('display_scale_xyz') or r['marking'].get('policy') != 'unmarked_illustration'):
        raise ValueError('Reviewed source illustration changed')
    r['represented_manufacturer'] = MAKER
    r['represented_mpn'] = MPN
    r['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'LCSC and secondary product listing', 'source_record': f'parts_source/{PART}/working.yaml'}
    r['appearance_status'] = ('Generic KiCad 1206 geometry is 1.6 mm high, matching a secondary listing. Ceramic colour, terminations and unmarked appearance are illustrative; manufacturer drawing was not independently accessed and the reported height may be generic.')
    return r

def main():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    if PART in recipes: raise ValueError('Existing recipe is preserved')
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipes[PART] = reviewed_recipe(record, recipes, sha)
    RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print('Prepared', PART)

if __name__ == '__main__': main()
