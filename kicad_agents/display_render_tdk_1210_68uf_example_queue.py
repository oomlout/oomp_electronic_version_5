"""Stage one clearly disclosed TDK visual example for a conflicting generic item."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_1210_68_micro_farad'
REFERENCE = 'electronic_capacitor_1210_2_2_micro_farad'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TDK_1210_68UF_EXAMPLE_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if (record.get('name_proper') != 'Capacitor 68 uF 1210'
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1210_3225Metric'
        or record.get('manufacturer') or record.get('part_number_manufacturer')
        or record.get('manufacturers') or record.get('distributors') or record.get('electrical')):
        raise ValueError('Generic identity or dimension conflict changed; review again')
    result = copy.deepcopy(recipes[REFERENCE])
    if (result.get('family') != 'chip_capacitor'
        or result.get('marking', {}).get('policy') != 'unmarked_illustration'
        or result['model'].get('expected_bounds_mm') != [3.2, 2.5, 2.5]):
        raise ValueError('Reviewed 1210 model changed')
    result['model']['display_scale_xyz'] = [1., 1., .8]
    result['represented_manufacturer'] = 'TDK (illustrative example only)'
    result['represented_mpn'] = 'C3225X5R0J686M200AC (illustrative example only)'
    result['marking'].update(evidence={'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'TDK example and C-series dimensions', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='The unmarked ceramic appearance is illustrative; the generic item has no selected part or confirmed voltage rating.')
    result['appearance_status'] = ('Illustrative TDK 68 uF 1210 example, 3.2 x 2.5 x 2.0 mm. The generic source record instead lists 10 x 5 mm: this dimension conflict needs correction. The example is not a selected procurement part, and its 6.3 V rating is not an asserted rating of the generic item. Colour and terminal finish are illustrative.')
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
