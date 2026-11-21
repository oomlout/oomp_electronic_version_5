"""Stage SOD-123 illustrations using explicitly disclosed related examples."""
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

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_JCST_SOD123_RESEARCH.md')
BASE = 'jiangsu_changjing_electronics_technology_co_ltd_'
PARTS = {
    'electronic_diode_zener_sod_123_' + BASE + 'mmsz5235b': ('MMSZ5235B', 'E5'),
    'electronic_diode_zener_sod_123_' + BASE + 'mmsz5238b': ('MMSZ5238B', 'F3'),
    'electronic_diode_zener_sod_123_' + BASE + 'mmsz5245b': ('MMSZ5245B', 'H5'),
    'electronic_diode_zener_sod_123_' + BASE + 'mmsz5248b': ('MMSZ5248B', 'J3'),
    'electronic_diode_schottky_sod_123_' + BASE + 'b0530w': ('B0530W', 'SE'),
    'electronic_diode_switching_sod_123_' + BASE + '1n4148w': ('1N4148W', 'T4'),
}
PDFS = {
    'electronic_diode_zener_sod_123_' + BASE + 'mmsz5235b': 'f0ca04b4c091d9d68a770423b0d44c5d87e4cd92028903d95211a7aa446d6323',
    'electronic_diode_schottky_sod_123_' + BASE + 'b0530w': 'cbe9ff977af6cd8a640d6113893247e60a7c55a69beec9caf2664908e3209af0',
    'electronic_diode_switching_sod_123_' + BASE + '1n4148w': '358627a9f88dd139c2f0c88662aa8af98992a2bfb47266b79e05e07b29385cfa',
}


def prepare(recipes):
    pilot = recipes[PILOT]
    if pilot['model']['sha256'] != MODEL_SHA or pilot['marking']['text'] != 'WF':
        raise ValueError('SOD-123 pilot changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part, expected in PDFS.items():
        if hashlib.sha256((ROOT / 'parts_source' / part / 'datasheet.pdf').read_bytes()).hexdigest() != expected:
            raise ValueError(f'{part}: local example PDF changed')
    result = {}
    for part, (mpn, text) in PARTS.items():
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'Jiangsu Changjing Electronics Technology Co., Ltd.'
            or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
            or (record.get('kicad') or {}).get('machine_solder')):
            raise ValueError(f'{mpn}: source identity, dimensions or footprint changed')
        recipe = copy.deepcopy(pilot)
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = text
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': 'SOD-123 marking examples and source limitations', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{text} is an illustrative different-manufacturer JCST example; '
            'the JSCJ factory marking is not confirmed. Typeface, placement and finish are illustrative.')
        if mpn == '1N4148W':
            recipe['marking']['appearance_status'] = ('T4 is an illustrative related JSCJ automotive-variant code; '
                'the overbar over T is omitted, and the unsuffixed JSCJ factory marking is unconfirmed. '
                'The local PDF is a different-manufacturer JCST example. Typeface and placement are illustrative.')
        recipe['appearance_status'] = ('KiCad SOD-123 model is 3.8 x 1.6 x 1.26 mm overall; cathode band is on the pin-1 side. '
            'No local dimensioned drawing is available. The source dimensions 10 x 5 mm appear to be placeholders and no footprint is selected. '
            'Fine details are approximate; not manufacturing CAD or a footprint.')
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--add', action='store_true'); args = parser.parse_args()
    original = RECIPE_FILE.read_bytes(); recipes = json.loads(original.decode('utf8')); candidates = prepare(recipes)
    for part, recipe in candidates.items():
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{part}: existing recipe differs')
        recipes[part] = recipe
    if args.add:
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name); f.write((json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8')); f.flush(); os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original:
                raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists(): temp.unlink()
    print(f'{len(candidates)} candidates; pilot comparison and individual review required')


if __name__ == '__main__': main()
