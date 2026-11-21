"""Stage a drawing-based W06 bridge display with an explicit footprint caveat."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_mdd_kbp_queue import PARTS as KBP_PARTS

PART = 'electronic_diode_bridge_rectifier_dip_4_mdd_microdiode_semiconductor_w06'
PILOT = next(part for part, mpn in KBP_PARTS.items() if mpn == 'KBP206')
MODEL = 'kicad_agents/display_model_mdd_w06.py'
MODEL_SHA = 'a8908043325df29ac8fdd6caeff3a9c8998b887fc9bedec1a629fc211e328927'
PDF_SHA = '39c486b3432cda04fabd04d8c68438b23d83355137e09b9e2d9c464c72dc05ec'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_BRIDGE_FAMILY_REVIEW.md')


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or record.get('part_number_manufacturer') != 'W06'
        or record.get('dimensions_mm') != {'height': 3.6, 'length': 8.6, 'width': 6.5}
        or (record.get('kicad') or {}).get('machine_solder') != 'Diode_THT:Diode_Bridge_DIP-4_W7.62mm_P5.08mm'):
        raise ValueError('W06 source identity, dimensions or footprint changed')
    if hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA:
        raise ValueError('W06 family PDF changed')
    if hashlib.sha256((ROOT / MODEL).read_bytes()).hexdigest() != MODEL_SHA:
        raise ValueError('W06 procedural model changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(package='wom_procedural', represented_mpn='W06')
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [8.8, 8.8, 26.5], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': 'W06\n+  ~  ~  -', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 3.0, 'maximum_height_mm': 1.0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                     'document': 'MDD W06 WOM family drawing and source footprint conflict', 'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('W06 is a partial manufacturer family identifier; the MDD logo is omitted. The +, ~, ~, - positions '
            'follow the drawing connection arrangement, but their placement on the top face, typeface and production artwork are illustrative.')}
    recipe['appearance_status'] = ('Procedural round WOM body 8.8 mm diameter x 5.5 mm tall with 0.75 mm leads on 5.1 mm centres; '
        'the positive lead is longer. The source record specifies a rectangular DIP footprint and 8.6 x 6.5 x 3.6 mm dimensions, '
        'which conflict with the manufacturer round-body drawing. This image follows the drawing; verify the source footprint before use. '
        'Display illustration only; not manufacturing CAD or a PCB footprint.')
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
    print('W06 round-body candidate; preview and polarity review required')


if __name__ == '__main__':
    main()
