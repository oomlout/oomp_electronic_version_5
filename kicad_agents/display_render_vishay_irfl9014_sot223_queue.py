"""Prepare the evidence-backed Vishay IRFL9014 SOT-223 display render."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_ams1117_sot223_batch import REFERENCE

PART = 'electronic_transistor_sot_223_mosfet_p_channel_enhancement_mode_60_volt_1_8_amp_vishay_intertech_irfl9014trpbf'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_VISHAY_IRFL9014_SOT223_RESEARCH.md')
PDF_SHA = '0e2847953fed483654671ca47aa940332e5eee0763051df08d3d0b784b98b46f'
MODEL_SHA = '77ad6dbacc493cb619c728f26d2ddcf461eb0feb6b977b47d01d51e67016f654'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != 'Vishay Intertech' or record.get('part_number_manufacturer') != 'IRFL9014TRPBF'
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
        or (record.get('kicad') or {}).get('machine_solder') != ''
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA):
        raise ValueError('Source record or local drawing changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if recipe['package'] != 'sot_223_3' or recipe['model']['sha256'] != MODEL_SHA:
        raise ValueError('Reviewed SOT-223 reference changed')
    recipe.update(family='transistor', represented_manufacturer='Vishay Intertech', represented_mpn='IRFL9014TRPBF')
    recipe['marking'].update(policy='verified_literal', text='FE', maximum_width_mm=2.5, maximum_height_mm=0.9, evidence={
        'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
        'document': 'Vishay IRFL9014 SOT-223 marking and package review',
        'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='FE is the manufacturer-documented marking code. Typeface, location, variable production codes and the model pin indicator are illustrative.')
    recipe['appearance_status'] = ('The KiCad SOT-223 model has 7.0 x 6.5 x 1.7 mm overall bounds and three leads plus tab, matching the drawing arrangement. The catalogue 10 x 5 mm dimensions differ from the manufacturer drawing. Finish and pin indicator are illustrative; not a verified manufacturing model or footprint.')
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
    print('IRFL9014TRPBF candidate; final image review required')


if __name__ == '__main__':
    main()
