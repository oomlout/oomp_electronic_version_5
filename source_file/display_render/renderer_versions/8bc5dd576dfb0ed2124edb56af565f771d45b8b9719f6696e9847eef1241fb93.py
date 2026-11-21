"""Stage two MDD KBP bridge display illustrations."""
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

PREFIX = 'electronic_diode_bridge_rectifier_kbp_mdd_microdiode_semiconductor_'
PARTS = {PREFIX + 'kbp206': 'KBP206', PREFIX + 'kbp210': 'KBP210'}
MODEL = 'kicad_agents/display_model_mdd_kbp.py'
MODEL_SHA = '79432bd656c713146a6bb92ed14da72137db5427a975265371336485e2398e71'
PDF_SHA = '5cd52df2def43b3dda4ed781f9a858671cfb12ee02ca6e402e1a3faa7fc0466f'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_KBP2_RESEARCH.md')


def prepare(recipes):
    if hashlib.sha256((ROOT / MODEL).read_bytes()).hexdigest() != MODEL_SHA:
        raise ValueError('Procedural model changed')
    if hashlib.sha256((ROOT / 'parts_source' / (PREFIX + 'kbp206') / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA:
        raise ValueError('Reviewed family PDF changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(); result = {}
    for part, mpn in PARTS.items():
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
            or (record.get('kicad') or {}).get('machine_solder')):
            raise ValueError(f'{mpn}: source record changed')
        recipe = copy.deepcopy(recipes[PILOT]); recipe.update(family='diode', package='kbp_procedural',
            represented_manufacturer='MDD(Microdiode Semiconductor)', represented_mpn=mpn)
        recipe['disable_bump_for'] = ['coating', 'termination']
        recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
            'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
            'expected_bounds_mm': [14.0, 23.8, 3.2], 'dimension_tolerance_mm': .015,
            'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
        recipe['marking'] = {'policy': 'illustrative_literal', 'text': mpn + '\n+  ~  ~  -', 'font_file': 'arialbd.ttf',
            'maximum_width_mm': 8.0, 'maximum_height_mm': 2.0,
            'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
                'document': 'MDD KBP2 outline, identification and terminal order', 'source_record': f'parts_source/{part}/working.yaml'},
            'appearance_status': 'Part identifier and +, ~, ~, - polarity labels follow the family drawing; typeface, exact placement, finish and production details are illustrative.'}
        recipe['appearance_status'] = ('Procedural KBP body is 14.0 x 10.6 x 3.2 mm with 3.81 mm lead pitch and 13.2 mm projection. '
            'The bevel and lead details are illustrative. Source 10 x 5 mm dimensions appear to be placeholders and no footprint is selected. '
            'Display illustration only; not manufacturing CAD or a PCB footprint.')
        if mpn == 'KBP210': recipe['marking']['appearance_status'] += ' No local PDF is stored for this entry; the KBP206 family PDF is the source.'
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--add', action='store_true'); args = parser.parse_args()
    original = RECIPE_FILE.read_bytes(); recipes = json.loads(original.decode('utf8')); candidates = prepare(recipes)
    for part, recipe in candidates.items():
        if part in recipes and recipes[part] != recipe: raise ValueError(f'{part}: existing recipe differs')
        recipes[part] = recipe
    if args.add:
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name); f.write((json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8')); f.flush(); os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists(): temp.unlink()
    print('Two KBP candidates; geometry, polarity and preview review required')


if __name__ == '__main__': main()
