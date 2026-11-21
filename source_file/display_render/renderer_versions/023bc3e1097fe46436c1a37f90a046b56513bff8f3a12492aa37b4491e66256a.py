"""Stage the drawing-based Kangnex WJ127 two-position display model."""
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

PART = 'electronic_connector_terminal_block_5_mm_pitch_through_hole_2_pin'
MODEL = 'kicad_agents/display_model_kangnex_wj127_2p.py'
MODEL_SHA = 'c1b82f7582c0cbf32e2ef5f24dc12fcd2483a7787640c9532e7e1920ac282c7c'
PDF_SHA = '54798969ee12c5fec7b3f874007ed3c89da7ab43a9a6d2ab365a2d625402d139'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_KANGNEX_WJ127_RESEARCH.md')


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Ningbo Kangnex Elec' or record.get('part_number_manufacturer') != 'WJ127-5.0-02P-14-00A'
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
        or (record.get('kicad') or {}).get('machine_solder') != 'TerminalBlock_Phoenix:TerminalBlock_Phoenix_PT-1,5-2-5.0-H_1x02_P5.00mm_Horizontal'):
        raise ValueError('Terminal block source identity, dimensions or footprint changed')
    if hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA:
        raise ValueError('Kangnex drawing changed')
    if hashlib.sha256((ROOT / MODEL).read_bytes()).hexdigest() != MODEL_SHA:
        raise ValueError('Terminal block procedural model changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='connector', package='wj127_2p_procedural', represented_manufacturer='Ningbo Kangnex Elec',
                  represented_mpn='WJ127-5.0-02P-14-00A')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [10.0, 8.12, 14.34], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'unmarked_illustration', 'text': '', 'font_file': 'arialbd.ttf',
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                     'document': 'Kangnex WJ127 drawing and KiCad Phoenix model comparison', 'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Deliberately unmarked illustration; no logo or contact numbering is established by the drawing.'}
    recipe['appearance_status'] = ('Drawing-based green WJ127 terminal illustration: nominal 10 x 8.12 x 10.14 mm body, '
        '5 mm pitch and 4.2 mm pin projection. Recesses, wire openings, screw slots, cages, green shade and finish are illustrative. '
        'Source width 5 mm differs from the drawing depth 8.12 mm; the selected KiCad Phoenix model is a different manufacturer and size. '
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
    print('Kangnex terminal candidate; preview and geometry review required')


if __name__ == '__main__':
    main()
