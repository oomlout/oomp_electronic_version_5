"""Stage two drawing- and marking-reviewed JSCJ SOT-23 diodes."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

REFERENCE = 'electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_SOT23_DIODES_RESEARCH.md')
PARTS = {
    'electronic_diode_switching_dual_common_anode_sot_23_jiangsu_changjing_electronics_technology_co_ltd_baw56':
        ('BAW56', 'A1', '7ea39b2c8229c3bffebb55dd96f0a07d99b18caf316f92293f4287e31e1d7737'),
    'electronic_diode_switching_dual_common_cathode_sot_23_jiangsu_changjing_electronics_technology_co_ltd_bav70':
        ('BAV70', 'A4', '2688a2ac8f7576e7ffa8b58c76f9ff025cd61a80053774b2a07b9cbee540b07d'),
}
MANUFACTURER = 'Jiangsu Changjing Electronics Technology Co., Ltd.'


def candidate(part, recipes):
    mpn, marking, pdf_sha = PARTS[part]
    source = ROOT / 'parts_source' / part
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != MANUFACTURER or record.get('part_number_manufacturer') != mpn
        or record.get('dimensions_mm') != {'length': 2.9, 'width': 2.6}
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_SMD:SOT-23'
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
        raise ValueError(f'{mpn}: source identity, dimensions, footprint or PDF changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if (recipe['model']['sha256'] != 'dd5d1711204e1d8d26cd11490923bd84340820baa69538c385a4300ec2539bc0'
        or recipe['model'].get('display_scale_xyz') != [1., 1., .9166666666666666]):
        raise ValueError('Reviewed SOT-23 model changed')
    recipe.update(represented_manufacturer=MANUFACTURER, represented_mpn=mpn)
    recipe['marking'].update(policy='verified_literal', text=marking, evidence={'file': EVIDENCE.as_posix(),
        'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
        'document': f'JSCJ {mpn} SOT-23 package and marking review', 'source_record': f'parts_source/{part}/working.yaml'},
        appearance_status=f'JSCJ specifies {marking}; optional green-moulding dot is omitted. Typeface, placement and production details are illustrative.')
    note = ' The BAV70 PDF drawing did not render reliably; the related BAW56 family drawing provides package evidence.' if mpn == 'BAV70' else ''
    recipe['appearance_status'] = ('KiCad SOT-23 2.5 x 3.0 x 1.2 mm model is vertically scaled to 1.1 mm for display. Finish and fine details are illustrative; not a verified manufacturing model or footprint.' + note)
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    for part in PARTS:
        recipe = candidate(part, recipes)
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{part}: existing recipe differs')
        recipes[part] = recipe
        print(PARTS[part][0], 'candidate; final visual review required')
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


if __name__ == '__main__':
    main()
