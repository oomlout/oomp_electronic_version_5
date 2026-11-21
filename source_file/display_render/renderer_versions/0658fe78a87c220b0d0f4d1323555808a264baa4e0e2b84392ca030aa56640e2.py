"""Stage the source-backed Littelfuse 466-series 2 A display candidate."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_fuse_1206_disposable_littelfuse_0466002_nrhf'
PILOT = 'electronic_resistor_0603_10000_ohm'
MODEL = 'Fuse.3dshapes/Fuse_1206_3216Metric.step'
MODEL_HASH = '5e6dcbe286696143d35a8ea37d91eef4b54ff3d1bd7c2c2b4dedda83d3f8e203'
PDF_HASH = '33f71340c39d8991607a0be589732a29bb11fbfcae8565bc52f849703dfb0276'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_LITTELFUSE_0466002_RESEARCH.md')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Littelfuse' or record.get('part_number_manufacturer') != '0466002.NRHF'
        or record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6, 'height': 1.1}
        or (record.get('kicad') or {}).get('machine_solder') != 'Fuse:Fuse_1206_3216Metric'
        or digest(source / 'datasheet.pdf') != PDF_HASH):
        raise ValueError('Fuse identity, source dimensions, footprint or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='1206_metric_3216',
                  represented_manufacturer='Littelfuse', represented_mpn='0466002.NRHF')
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination']
    recipe['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        copyright='2020 kicad StepUp', sha256=MODEL_HASH, expected_bounds_mm=[3.2, 1.6, .55],
        required_roles=['coating', 'ceramic', 'termination'],
        role_by_source_colour={'0.082,0.086,0.094': 'coating', '0.895,0.891,0.813': 'ceramic',
                               '0.824,0.820,0.781': 'termination'})
    recipe['marking'] = {'policy': 'verified_literal', 'text': 'N', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 1.05, 'maximum_height_mm': .8,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Littelfuse 466 series local drawing and 2 A marking review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Manufacturer 2 A marking N; approximate ink, typeface and placement.'}
    recipe['appearance_status'] = ('Generic KiCad 1206 fuse model measures 3.2 x 1.6 x 0.55 mm within drawing tolerances; '
        'the source 1.1 mm height exceeds the drawing 0.66 mm maximum. The model omits the drawing end notches. '
        'Green coating and light ink follow the drawing artwork but exact finish is illustrative; not manufacturer CAD or a footprint.')
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
    print('Littelfuse 466 2 A candidate; preview and final review required')


if __name__ == '__main__':
    main()
