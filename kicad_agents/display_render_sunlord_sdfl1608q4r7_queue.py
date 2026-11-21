"""Stage the reviewed Sunlord 0603 inductor as an illustrative unmarked model."""
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

PART = 'electronic_inductor_0603_4_7_micro_henry'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SUNLORD_SDFL1608Q4R7KTF_RESEARCH.md')
PDF_HASH = '335d6b6b58598ce932424478dbb3ec3c02cd90a4ff171a6c9ec78f79172651ef'
MODEL_HASH = 'b0136ad7160588d2f5dac8c85da84a35646db656b5bc54bbb873b6b548eedbb3'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Sunlord' or record.get('part_number_manufacturer') != 'SDFL1608Q4R7KTF'
        or record.get('dimensions_mm') != {'length': 1.6, 'width': .8, 'height': .8}
        or (record.get('kicad') or {}).get('machine_solder') != 'Inductor_SMD:L_0603_1608Metric'
        or digest(ROOT / 'parts_source/electronic_inductor_0603_10_micro_henry_sunlord_sdfl1608s100ktf/datasheet.pdf') != PDF_HASH):
        raise ValueError('Sunlord part identity, dimensions, footprint or evidence changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='chip_inductor', package='0603_metric_1608',
                  represented_manufacturer='Sunlord', represented_mpn='SDFL1608Q4R7KTF')
    recipe['disable_bump_for'] = ['coating', 'termination']
    name = 'Inductor_SMD.3dshapes/L_0603_1608Metric.step'
    recipe['model'].update(relative_path=name,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + name,
        copyright='2017 kicad StepUp', sha256=MODEL_HASH, expected_bounds_mm=[1.6, .8, .8], required_roles=['coating', 'termination'],
        role_by_source_colour={'0.273,0.273,0.273': 'coating', '0.824,0.820,0.781': 'termination'})
    recipe['marking'] = {'policy': 'unmarked_illustration', 'text': '', 'font_file': 'arialbd.ttf',
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Sunlord SDFL 0603 inductor source and model review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Deliberately unmarked illustration; the manufacturer drawing does not establish the production marking.'}
    recipe['appearance_status'] = ('Generic KiCad 0603 inductor model matches the nominal 1.6 x 0.8 x 0.8 mm drawing dimensions. '
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
