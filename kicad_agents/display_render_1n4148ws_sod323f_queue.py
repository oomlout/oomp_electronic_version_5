"""Stage a different-manufacturer onsemi SOD-323FL illustration."""
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

PART = 'electronic_diode_switching_sod_323_onsemi_1n4148ws'
MODEL_SHA = 'be5930ed2efe5eca953bd400465c68e8d6fe18bbed65f5a40cb96114f48e8ca0'
PDF_SHA = '59e951bd3155eb4a94e958d10edc3b7d17325f38cf06784cac07fbcc9fcabf2e'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_1N4148WS_SOD323F_RESEARCH.md')


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Jiangsu Changjing Electronics Technology Co., Ltd.'
        or record.get('part_number_manufacturer') != '1N4148WS'
        or record.get('dimensions_mm') != {'length': 1.7, 'width': 1.25}
        or (record.get('kicad') or {}).get('machine_solder') != 'Diode_SMD:D_SOD-323'
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA):
        raise ValueError('Source identity or local JCST PDF changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe['package'] = 'sod_323f'
    recipe['represented_mpn'] = '1N4148WS'
    recipe['model'].update(relative_path='Diode_SMD.3dshapes/D_SOD-323F.step',
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Diode_SMD.3dshapes/D_SOD-323F.step',
        sha256=MODEL_SHA, expected_bounds_mm=[2.5, 1.25, .73])
    recipe['marking'].update(text='S1', maximum_width_mm=.55, maximum_height_mm=.3, offset_x_mm=.16)
    recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(),
        'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
        'document': 'Onsemi 1N4148WS flat-lead example, marking and drawing review',
        'source_record': f'parts_source/{PART}/working.yaml'}
    recipe['marking']['appearance_status'] = ('S1 is an illustrative different-manufacturer onsemi example; '
        'the JSCJ factory marking and exact package variant are unconfirmed. Production codes are omitted; typeface and placement are illustrative.')
    recipe['appearance_status'] = ('KiCad SOD-323F flat-lead display model approximates the different-manufacturer onsemi SOD-323FL drawing, '
        'with a cathode stripe on the pin-1 side. The source record instead selects a SOD-323 footprint; '
        'this difference is unverified. The local PDF is a JCST example. Not manufacturing CAD or a footprint.')
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--add', action='store_true'); args = parser.parse_args()
    original = RECIPE_FILE.read_bytes(); recipes = json.loads(original.decode('utf8')); recipe = prepare(recipes)
    if PART in recipes and recipes[PART] != recipe: raise ValueError('Existing recipe differs')
    recipes[PART] = recipe
    if args.add:
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name); f.write((json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8')); f.flush(); os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists(): temp.unlink()
    print('1N4148WS SOD-323F candidate; preview and final review required')


if __name__ == '__main__': main()
