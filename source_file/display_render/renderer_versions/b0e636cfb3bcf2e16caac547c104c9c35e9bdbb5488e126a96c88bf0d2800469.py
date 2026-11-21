"""Stage five unspecified-lens generic 0603 LED colour variants."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_generic_smd_led_pilots_queue import SPECS

PILOT = 'electronic_led_0603'
MODEL_SHA = SPECS['0603'][2]
PARTS = {f'electronic_led_0603_{colour}': colour for colour in ('blue', 'green', 'red', 'white', 'yellow')}
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_0603_LED_FAMILY.md')


def prepare(recipes):
    pilot = recipes[PILOT]
    if pilot['model']['sha256'] != MODEL_SHA or pilot['marking']['policy'] != 'unmarked_illustration':
        raise ValueError('Reviewed unmarked 0603 pilot changed')
    pilot_manifest = ROOT / 'parts' / PILOT / 'data/display_render/manifest.json'
    if not pilot_manifest.is_file() or json.loads(pilot_manifest.read_text(encoding='utf8')).get('recipe') != pilot:
        raise ValueError('Published independent 0603 pilot is missing or differs')
    evidence_hash = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    result = {}
    for part, colour in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('taxonomy_3') != '0603' or (record.get('taxonomy_4') or '') != colour
            or (record.get('taxonomy_5') or '') != '' or record.get('manufacturer') not in ('', None)
            or record.get('part_number_manufacturer') not in ('', None) or (source / 'datasheet.pdf').exists()
            or record.get('dimensions_mm') != {'length': 1.6, 'width': .8}
            or (record.get('kicad') or {}).get('machine_solder') != 'LED_SMD:LED_0603_1608Metric'):
            raise ValueError(f'{part}: generic identity or package assumptions changed')
        recipe = copy.deepcopy(pilot)
        recipe['represented_mpn'] = f'generic {colour} 0603 LED'
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
            'document': 'Generic unlit 0603 LED family and shared-image review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = ('Deliberately unmarked illustration: no manufacturer or exact part number is specified, '
                                                  'so actual markings are unknown.')
        recipe['appearance_status'] = ('Unlit generic KiCad 0603 LED package; ' + colour.capitalize() +
            ' describes emitted light, not necessarily lens colour. No exact manufacturer, lens appearance or local datasheet is specified. '
            'Model bounds are 1.6 x 0.8 x 1.1 mm; its height is a generic model property, not an exact-part specification. '
            'The green orientation region is underneath. Material finish is illustrative; not manufacturing CAD or a footprint.')
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    for part, recipe in prepare(recipes).items():
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{part}: existing recipe differs')
        recipes[part] = recipe
    if args.add:
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name)
                f.write((json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8'))
                f.flush()
                os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original:
                raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists():
                temp.unlink()
    print('Five generic 0603 LED candidates; verify shared-image provenance before publication')


if __name__ == '__main__':
    main()
