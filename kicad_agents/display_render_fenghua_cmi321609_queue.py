"""Stage four drawing-reviewed Fenghua 1206 chip inductors."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_inductor_0805_10_micro_henry_sunlord_sdfl2012s100ktf'
PARTS = {'electronic_inductor_1206_2_2_micro_henry': 'CMI321609U2R2KT',
         'electronic_inductor_1206_4_7_micro_henry': 'CMI321609U4R7KT',
         'electronic_inductor_1206_5_6_micro_henry': 'CMI321609U5R6KT',
         'electronic_inductor_1206_10_micro_henry': 'CMI321609X100KT'}
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_CMI321609_INDUCTORS_RESEARCH.md')
PDF = Path('parts_source/electronic_inductor_1206_10_micro_henry/datasheet.pdf')
PDF_HASH = '56229443c350135b4f895831fa10f9f9e298e6bd53f6699ab9ad2743a3650f00'
MODEL_HASH = '7a76ea34101f04e5f76cf96aa1ead38be0f0b388f5d21e9dafbb3047c495e5dd'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    pilot = recipes[PILOT]
    if pilot['model']['sha256'] != '751a8ae26d20698bfe8303aa2fc7ec986a8b9a7154699b94bf2a13d4ad401425' or digest(ROOT / PDF) != PDF_HASH:
        raise ValueError('Reviewed model or manufacturer family drawing changed')
    result = {}
    for part, mpn in PARTS.items():
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'FH (Guangdong Fenghua Advanced Tech)'
            or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6, 'height': .9}
            or (record.get('kicad') or {}).get('machine_solder') != 'Inductor_SMD:L_1206_3216Metric'):
            raise ValueError(f'{part}: identity, source dimensions or footprint changed')
        recipe = copy.deepcopy(pilot)
        recipe.update(represented_manufacturer='Fenghua', represented_mpn=mpn)
        recipe['package'] = '1206_metric_3216'
        recipe['model'].update(relative_path='Inductor_SMD.3dshapes/L_1206_3216Metric.step',
            source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Inductor_SMD.3dshapes/L_1206_3216Metric.step',
            sha256=MODEL_HASH, expected_bounds_mm=[3.2, 1.6, 1.6], display_scale_xyz=[1.0, 1.0, .5625])
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
            'document': 'Fenghua CMI321609 manufacturer drawing and model review',
            'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = ('Deliberately unmarked illustration; the manufacturer drawing does not establish the production marking.')
        recipe['appearance_status'] = ('Generic KiCad 1206 inductor model scaled vertically from 1.6 to 0.9 mm to match the drawing nominal; length and width are unchanged. '
            'Dark body and metal ends are illustrative; the drawing does not verify body shade or any omitted marking. '
            'This is a display model, not manufacturing CAD or a footprint.')
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
    print('Four Fenghua inductor candidates; independent preview and final review required')


if __name__ == '__main__':
    main()
