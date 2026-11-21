"""Stage Semtech 1N4148W using its local drawing."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_jscj_bzt52_sod123_composite import PILOT, MODEL_SHA

PART = 'electronic_diode_switching_sod_123_st_semtech_1n4148w'
PDF_SHA = '54de8e4089bb8221cf6cf191ee3acc2bdb20c9933cf59e7b5de3ef4ee291ce3f'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SEMTECH_1N4148W_RESEARCH.md')


def prepare(recipes):
    pilot = recipes[PILOT]; source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (pilot['model']['sha256'] != MODEL_SHA or pilot['marking']['text'] != 'WF'
        or record.get('manufacturer') != 'ST(Semtech)'
        or record.get('part_number_manufacturer') != '1N4148W'
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
        or (record.get('kicad') or {}).get('machine_solder')
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA):
        raise ValueError('Pilot or source differs from reviewed B5819W setup')
    recipe = copy.deepcopy(pilot)
    recipe['represented_manufacturer'] = 'ST(Semtech)'
    recipe['represented_mpn'] = '1N4148W'
    recipe['marking']['text'] = 'W1'
    recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(),
        'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
        'document': 'Semtech 1N4148W marking and SOD-123 drawing review',
        'source_record': f'parts_source/{PART}/working.yaml'}
    recipe['marking']['appearance_status'] = ('W1 is the code shown in the Semtech datasheet; typeface, placement and finish are illustrative.')
    recipe['appearance_status'] = ('KiCad SOD-123 model is 3.8 x 1.6 x 1.26 mm overall, with a cathode stripe on the pin-1 side. '
        'Its height exceeds the Semtech drawing maximum by 0.11 mm. The source 10 x 5 mm dimensions appear '
        'to be placeholders and no footprint is selected. Fine details are approximate; not manufacturing CAD.')
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
    print('Semtech 1N4148W candidate; pilot comparison and individual review required')


if __name__ == '__main__': main()
