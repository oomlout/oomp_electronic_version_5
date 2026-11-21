"""Prepare an unmarked generic dual MOSFET SOT-363 display illustration."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_transistor_sot_363_6_mosfet_n_channel_dual'
REFERENCE = 'electronic_ic_logic_dual_schmitt_trigger_inverter_sot_363_nexperia_74lvc2g14gw_125'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_SOT363_RESEARCH.md')
MODEL_SHA = '045cc95e18ee7a13d1623c3ce6604fc833049bdb4f952f68c26e3c5767d122e4'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') not in ('', None) or record.get('part_number_manufacturer') not in ('', None)
        or record.get('dimensions_mm') != {'height': .95, 'length': 2.0, 'width': 1.25}
        or (record.get('kicad') or {}).get('machine_solder') != '' or (source / 'datasheet.pdf').exists()):
        raise ValueError('Generic source identity, dimensions or PDF availability changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if recipe['package'] != 'sot_363_sc70_6' or recipe['model']['sha256'] != MODEL_SHA:
        raise ValueError('Reviewed SOT-363 reference changed')
    recipe.update(family='transistor', represented_manufacturer='Unspecified', represented_mpn='generic dual N-channel MOSFET')
    recipe['model']['display_scale_xyz'] = [1.0, 1.0, .95 / 1.1]
    recipe['marking'].update(policy='unmarked_illustration', text='', evidence={'file': EVIDENCE.as_posix(),
        'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
        'document': 'Generic dual MOSFET SOT-363 package review', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Deliberately unmarked illustration: no manufacturer or part number is specified, and actual devices may carry different codes.')
    recipe['appearance_status'] = ('Generic KiCad SOT-363 2.1 x 2.0 x 1.1 mm model is vertically scaled to 0.95 mm. No exact manufacturer or device is specified and there is no separate local PDF. The pin indicator and finish are illustrative; not manufacturing CAD or a footprint.')
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
    print('Generic SOT-363 unmarked candidate; preview and final review required')


if __name__ == '__main__':
    main()
