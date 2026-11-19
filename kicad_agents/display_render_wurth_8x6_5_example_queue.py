"""Prepare one explicitly disclosed Würth example for an unsourced generic item."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_8_mm_diameter_6_5_mm_tall_electrolytic_220_micro_farad_10_volt'
REFERENCE = 'electronic_capacitor_8_mm_diameter_10_2_mm_tall_electrolytic_100_micro_farad_50_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_WURTH_8X6_5_220UF_10V_EXAMPLE_EVIDENCE.md')
MODEL = 'Capacitor_SMD.3dshapes/CP_Elec_8x6.5.step'
MODEL_SHA = 'b68f9f996cc3c4594872968aacec31af520043f4093f9409e1d753b44d088d13'


def reviewed_recipe(record, recipes, sha):
    if (record.get('name_proper') != 'Capacitor 220 uF 10 V Electrolytic 8 mm diameter x 6.5 mm tall'
        or record.get('dimensions_mm') != {'length': 8., 'width': 8.}
        or record.get('manufacturer') or record.get('part_number_manufacturer')
        or record.get('manufacturers') or record.get('distributors') or record.get('electrical')
        or record.get('kicad', {}).get('machine_solder') or record.get('kicad', {}).get('symbol')):
        raise ValueError('Generic identity or missing package data changed; review again')
    result = copy.deepcopy(recipes[REFERENCE])
    if (result.get('family') != 'aluminum_capacitor'
        or result['model'].get('metal_top_marking') is not True):
        raise ValueError('Reviewed SMD reference changed')
    result['package'] = 'electrolytic_smd_8x6_5_example'
    result['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[9.5, 8.3, 6.5], sha256=MODEL_SHA, display_scale_xyz=[1., 1., 1.])
    result['represented_manufacturer'] = 'Würth Elektronik (illustrative example only)'
    result['represented_mpn'] = '865090249008 (illustrative example only)'
    result['marking'].update(text='221\n10V', evidence={'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Würth 865090249008 manufacturer specification', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Simplified illustrative marking omits the variable production date line; exact artwork is not asserted.')
    result['appearance_status'] = ('Illustrative Würth 865090249008 220 uF / 10 V SMD example, not a selected procurement part. The generic source has no electrical fields, symbol or footprint and omits height from its dimensions; those remain unresolved. KiCad shape, base, polarity sector, ink and finish are illustrative.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest())
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; review manually')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
