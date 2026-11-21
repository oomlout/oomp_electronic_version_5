"""Stage only generic 0201 LEDs with unspecified unlit lens appearance."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_generic_led_0201_queue import PART as PILOT, MODEL_SHA

PARTS = {f'electronic_led_0201{("_" + color) if color else ""}': color
         for color in ('', 'green', 'red', 'white', 'yellow')}
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_0201_LED_FAMILY.md')


def prepare(recipes):
    pilot = recipes[PILOT]
    if pilot['model']['sha256'] != MODEL_SHA or pilot['marking']['policy'] != 'unmarked_illustration':
        raise ValueError('The reviewed unmarked 0201 pilot changed')
    evidence_hash = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    result = {}
    for part, color in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('taxonomy_3') != '0201' or (record.get('taxonomy_4') or '') != color
            or (record.get('taxonomy_5') or '') != '' or record.get('manufacturer') not in ('', None)
            or record.get('part_number_manufacturer') not in ('', None) or (source / 'datasheet.pdf').exists()
            or record.get('dimensions_mm') != {'length': .6, 'width': .3}
            or (record.get('kicad') or {}).get('machine_solder') != 'LED_SMD:LED_0201_0603Metric'):
            raise ValueError(f'{part}: generic identity or package assumptions changed')
        recipe = copy.deepcopy(pilot)
        label = f'generic {color} 0201 LED' if color else 'generic 0201 LED, emission colour unspecified'
        recipe['represented_mpn'] = label
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
            'document': 'Generic unlit 0201 LED family and shared-image review',
            'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = ('Deliberately unmarked illustration: no manufacturer or exact part number is specified, '
                                                  'so actual markings are unknown.')
        emission = f'{color.capitalize()} describes emitted light, not necessarily lens colour.' if color else 'The emitted colour is unspecified.'
        recipe['appearance_status'] = ('Unlit generic KiCad 0201 LED package; ' + emission +
            ' No exact manufacturer, lens appearance or local datasheet is specified. The 0.65 x 0.35 x 0.20 mm model is larger '
            'than the 0.60 x 0.30 mm nominal catalogue dimensions. Material finish is illustrative; not manufacturing CAD or a footprint.')
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
    print('Five generic 0201 LED candidates; verify shared-image provenance before publishing')


if __name__ == '__main__':
    main()
