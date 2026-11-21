"""Stage a reviewed KiCad illustration of the XFCN two-position header."""
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

PART = 'electronic_connector_header_2_54_mm_pitch_through_hole_2_pin'
MODEL = 'Connector_PinHeader_2.54mm.3dshapes/PinHeader_1x02_P2.54mm_Vertical.step'
MODEL_SHA = 'ea4d0799007ebdd3945072bf255d673d2fe87eb05fda85fd8d7993ad9397da41'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_XFCN_HEADER_2P_RESEARCH.md')


def prepare(recipes):
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'XFCN(兴飞)' or record.get('part_number_manufacturer') != 'PZ254V-11-02P'
        or record.get('dimensions_mm') != {'length': 5.08, 'width': 2.48}
        or (record.get('kicad') or {}).get('machine_solder') != 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical'):
        raise ValueError('Header identity, dimensions or footprint changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='connector', package='2_54_mm_pin_header_1x02',
                  represented_manufacturer='XFCN(兴飞)', represented_mpn='PZ254V-11-02P')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        copyright='KiCad 3D Model Libraries contributors', sha256=MODEL_SHA,
        expected_bounds_mm=[2.54, 5.08, 11.54], dimension_tolerance_mm=.015,
        required_roles=['coating', 'termination'],
        role_by_source_colour={'0.148,0.145,0.145': 'coating', '0.859,0.738,0.496': 'termination'})
    recipe['marking'] = {'policy': 'unmarked_illustration', 'text': '', 'font_file': 'arialbd.ttf',
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                     'document': 'XFCN family drawing and generic KiCad model review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Unmarked generic package illustration; no printed markings are established.'}
    recipe['appearance_status'] = ('Generic KiCad two-position header shown with black body and illustrative gold contacts; '
        'the XFCN family drawing permits tin or gold and does not establish the exact unit finish. '
        'The model body is 2.54 mm wide and high versus the drawing 2.50 mm; it has 6.00 mm mating pins and 3.00 mm tails. '
        'Source width is 2.48 mm. Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    recipe = prepare(recipes)
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs')
    recipes[PART] = recipe
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
    print('Two-position header candidate; preview and final review required')


if __name__ == '__main__':
    main()
