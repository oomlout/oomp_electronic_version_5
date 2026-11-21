"""Stage independently rendered, unmarked generic SMD LED package pilots."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_generic_led_0201_queue import PART as PILOT

SPECS = {
    '0402': ('1005Metric', [1.0, .5, .5], '401a17c0a337a26edbde24f58dabfc1560d6cb1bfb8c8fc5c31b8692e321eb12'),
    '0603': ('1608Metric', [1.6, .8, 1.1], '98343205ec260ec165026ba2d44329a23096779ac36c553ea84aa7b370242e6d'),
    '0805': ('2012Metric', [2.0, 1.25, 1.1], '0aa8b791804f5d72a2fc7d1bf231dd9959207d83df8ad801176fbc459f575b98'),
    '1206': ('3216Metric', [3.2, 1.6, 1.1], '9de47a5de5d40bcdc5dcc40d5b9d41fc41af90bbd37d25c17d211285e1c63a6e'),
}
PARTS = {'electronic_led_' + size: size for size in SPECS}
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_LED_OTHER_PACKAGE_INVENTORY.md')


def prepare(recipes):
    pilot = recipes[PILOT]
    evidence_hash = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    result = {}
    for part, size in PARTS.items():
        suffix, bounds, model_hash = SPECS[size]
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
        name = f'LED_{size}_{suffix}'
        if (record.get('taxonomy_3') != size or (record.get('taxonomy_4') or '') != ''
            or (record.get('taxonomy_5') or '') != '' or record.get('manufacturer') not in ('', None)
            or record.get('part_number_manufacturer') not in ('', None) or (source / 'datasheet.pdf').exists()
            or record.get('dimensions_mm') != {'length': bounds[0], 'width': bounds[1]}
            or (record.get('kicad') or {}).get('machine_solder') != 'LED_SMD:' + name):
            raise ValueError(f'{part}: generic identity or footprint changed')
        recipe = copy.deepcopy(pilot)
        recipe['package'] = size + '_metric_' + suffix
        recipe['represented_mpn'] = f'generic {size} LED, emission colour unspecified'
        recipe['model'].update(relative_path='LED_SMD.3dshapes/' + name + '.step',
            source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/LED_SMD.3dshapes/' + name + '.step',
            sha256=model_hash, expected_bounds_mm=bounds)
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
            'document': 'KiCad generic SMD LED geometry and source review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['appearance_status'] = (f'Unlit generic KiCad {size} LED package; the emitted colour is unspecified. '
            f'No exact manufacturer, lens appearance or local datasheet is specified. Model bounds are {bounds[0]:g} x {bounds[1]:g} x {bounds[2]:g} mm; '
            'its height is a generic model property, not an exact-part specification. The green orientation region is underneath. '
            'Material finish is illustrative; not manufacturing CAD or a footprint.')
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
    print('Four generic SMD LED pilots; independent preview and final review required')


if __name__ == '__main__':
    main()
