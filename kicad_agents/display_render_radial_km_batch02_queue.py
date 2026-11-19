"""Prepare two exact KM radial capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_radial_km_220uf_queue import PILOT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_KM_BATCH02_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_100_micro_farad_63_volt': ('KM107M063F12RR0VH2FP0', 'C2772', '100 uF', '63 V', '100uF\n63V\nKM 105C'),
    'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_330_micro_farad_25_volt': ('KM337M025F12RR0VH2FP0', 'C2051', '330 uF', '25 V', '330uF\n25V\nKM 105C'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    mpn, supplier, value, voltage, text = PARTS[part]
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != mpn or record.get('part_number_lcsc') != supplier
        or e.get('capacitance') != value or e.get('rated_voltage') != voltage
        or e.get('pin_spacing') != '3.5 mm' or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'height': 12.0, 'length': 8.0, 'width': 8.0}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_THT:CP_Radial_D8.0mm_P3.50mm'
        or record.get('kicad', {}).get('symbol') != 'Device:C_Polarized'):
        raise ValueError('Identity, ratings, polarity or package changed')
    result = copy.deepcopy(recipes[PILOT])
    if (result.get('family') != 'radial_aluminum_capacitor'
        or result.get('represented_mpn') != 'KM107M050F12RR0VH2FP0'
        or result['model'].get('radial_stretch', {}).get('extra_height') != 4.0):
        raise ValueError('Pilot changed')
    result['represented_mpn'] = mpn
    result['marking']['text'] = text
    result['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'CX KM series and individual supplier listings',
        'source_record': f'parts_source/{part}/working.yaml'}
    return result


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
