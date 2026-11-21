"""Stage CBI MMBT7002K with an explicitly illustrative family marking."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_300_milliamp_cbi_mmbt7002k'
REFERENCE = 'electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_CBI_MMBT7002K_RESEARCH.md')
PDF_SHA = 'fba5368f324b0423d16ee03fbfdebacab2af893e000ce73ec74b5887f396fab8'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != 'CBI' or record.get('part_number_manufacturer') != 'MMBT7002K'
        or record.get('dimensions_mm') != {'length': 2.9, 'width': 2.6}
        or (record.get('kicad') or {}).get('machine_solder') != ''
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA):
        raise ValueError('CBI source record or datasheet changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if (recipe['model']['sha256'] != 'dd5d1711204e1d8d26cd11490923bd84340820baa69538c385a4300ec2539bc0'
        or recipe['model'].get('display_scale_xyz') != [1., 1., .9166666666666666]):
        raise ValueError('Reviewed SOT-23 model changed')
    recipe.update(represented_manufacturer='CBI', represented_mpn='MMBT7002K')
    recipe['marking'].update(policy='illustrative_literal', text='K72', evidence={'file': EVIDENCE.as_posix(),
        'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
        'document': 'CBI MMBT7002K outline and illustrative Diotec family marking', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='K72 is an illustrative Diotec family marking; the CBI datasheet does not establish the actual CBI marking. Typeface, placement and production details are illustrative.')
    recipe['appearance_status'] = ('KiCad SOT-23 2.5 x 3.0 x 1.2 mm model is scaled vertically to 1.1 mm and approximates the CBI outline. The K72 marking comes from a different manufacturer and is illustrative. Finish and fine details are approximate; not a manufacturing model or footprint.')
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
    print('CBI MMBT7002K illustrative candidate; final review required')


if __name__ == '__main__':
    main()
