"""Stage the reviewed Sunlord 0805 inductor as an illustrative unmarked model."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_jscj_bzt52_sod123_composite import PILOT

PART = 'electronic_inductor_0805_10_micro_henry_sunlord_sdfl2012s100ktf'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SUNLORD_SDFL2012S100KTF_RESEARCH.md')
PDF_HASH = '335d6b6b58598ce932424478dbb3ec3c02cd90a4ff171a6c9ec78f79172651ef'
MODEL_HASH = '751a8ae26d20698bfe8303aa2fc7ec986a8b9a7154699b94bf2a13d4ad401425'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Sunlord' or record.get('part_number_manufacturer') != 'SDFL2012S100KTF'
        or record.get('dimensions_mm') != {'length': 2.0, 'width': 1.25, 'height': .85}
        or (record.get('kicad') or {}).get('machine_solder') != 'Inductor_SMD:L_0805_2012Metric'
        or digest(ROOT / 'parts_source/electronic_inductor_0603_10_micro_henry_sunlord_sdfl1608s100ktf/datasheet.pdf') != PDF_HASH):
        raise ValueError('Sunlord part identity, dimensions, footprint or evidence changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='chip_inductor', package='0805_metric_2012',
                  represented_manufacturer='Sunlord', represented_mpn='SDFL2012S100KTF')
    recipe['disable_bump_for'] = ['coating', 'termination']
    name = 'Inductor_SMD.3dshapes/L_0805_2012Metric.step'
    recipe['model'].update(relative_path=name,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + name,
        copyright='2017 kicad StepUp', sha256=MODEL_HASH, expected_bounds_mm=[2.0, 1.25, 1.25], display_scale_xyz=[1.0, 1.0, .68], required_roles=['coating', 'termination'],
        role_by_source_colour={'0.273,0.273,0.273': 'coating', '0.824,0.820,0.781': 'termination'})
    recipe['marking'] = {'policy': 'unmarked_illustration', 'text': '', 'font_file': 'arialbd.ttf',
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Sunlord SDFL 0805 inductor source and model review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Deliberately unmarked illustration; the manufacturer drawing does not establish the production marking.'}
    recipe['appearance_status'] = ('Generic KiCad 0805 inductor model is scaled vertically from 1.25 to 0.85 mm to match nominal drawing height; length and width are unchanged. '
        'Dark body and metal ends follow the family illustration; exact finish and any omitted marking are illustrative. '
        'This is a display model, not manufacturing CAD or a footprint.')
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
    print('Sunlord inductor candidate; independent preview and final review required')


if __name__ == '__main__':
    main()
