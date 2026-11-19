"""Prepare four individually researched TAJ E-case display recipes."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_taj_e_pilot_queue import PILOT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TAJ_E_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_7343_avx_e_tantalum_100_micro_farad_25_volt_avx_taje107m025rnej': ('TAJE107M025RNJ', 'C7230', '100 uF', '25 V', '107 E'),
    'electronic_capacitor_7343_avx_e_tantalum_330_micro_farad_10_volt_avx_taje337k010rnej': ('TAJE337K010RNJ', 'C7232', '330 uF', '10 V', '337 A'),
    'electronic_capacitor_7343_avx_e_tantalum_470_micro_farad_10_volt_avx_taje477k010rnej': ('TAJE477K010RNJ', 'C7234', '470 uF', '10 V', '477 A'),
    'electronic_capacitor_7343_avx_e_tantalum_47_micro_farad_35_volt_avx_taje476k035rnej': ('TAJE476K035RNJ', 'C7233', '47 uF', '35 V', '476 V'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed TAJ E part')
    mpn, supplier, value, voltage, text = PARTS[part]
    e = record.get('electrical') or {}
    if (record.get('part_number_manufacturer') != mpn or record.get('part_number_lcsc') != supplier
        or e.get('capacitance') != value or e.get('rated_voltage') != voltage
        or e.get('case_size') != 'CASE-E-7343-43' or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 7.3, 'width': 4.3, 'height': 4.3}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X'):
        raise ValueError('Selected identity, rating, polarity or E-case geometry changed')
    recipe = copy.deepcopy(recipes[PILOT])
    if (recipe.get('family') != 'tantalum_capacitor' or recipe.get('package') != 'tantalum_7343_avx_e'
        or recipe['model'].get('display_scale_xyz') != [73/76, 43/46, 41/43]):
        raise ValueError('Pilot changed')
    recipe['represented_mpn'] = mpn
    recipe['marking']['text'] = text
    recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'KYOCERA AVX TAJ series and individual supplier listing',
        'source_record': f'parts_source/{part}/working.yaml'}
    recipe['appearance_status'] += ' Marking is composited from shared material passes; indirect reflections are approximate.'
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part in PARTS:
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, record, recipes, sha)
        if part in recipes and recipes[part] != recipe:
            raise ValueError('Existing recipe differs; review manually')
        if args.add:
            recipes[part] = recipe
        print(part, recipe['represented_mpn'])
    if args.add:
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
