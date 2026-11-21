"""Stage two source-reviewed Nexperia SOT-23 diode display candidates."""
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
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_NEXPERIA_SOT23_DIODES_RESEARCH.md')
PARTS = {
    'electronic_diode_switching_dual_common_cathode_sot_23_nexperia_bav70_215':
        ('BAV70,215', 'A4', '8af3a1214cc19d081bd8604ed1cdb98dc83dbb5a91bbdfba3663484a78450108', {'length': 2.9, 'width': 2.6}),
    'electronic_diode_switching_dual_series_sot_23_nexperia_bav99_215':
        ('BAV99,215', 'A7', '826c982f4f2bbefcc047abea7ed2be517c09cf46bf61c10c25e4b7c378369b2f', {'height': 1.0, 'length': 2.9, 'width': 1.3}),
}
MANUFACTURER = 'Nexperia'


def candidate(part, recipes):
    mpn, marking, pdf_sha, dimensions = PARTS[part]
    source = ROOT / 'parts_source' / part
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != MANUFACTURER or record.get('part_number_manufacturer') != mpn
        or record.get('dimensions_mm') != dimensions
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
        'document': f'Nexperia {mpn} SOT-23 package and marking review', 'source_record': f'parts_source/{part}/working.yaml'},
        appearance_status=f'Nexperia specifies {marking} followed by a variable manufacturing-site code, which is omitted. Typeface and placement are illustrative.')
    recipe['appearance_status'] = ('KiCad SOT-23 2.5 x 3.0 x 1.2 mm overall model is vertically scaled to 1.1 mm for display; the Nexperia sheet lists a nominal 1.0 mm body height. Finish and fine details are illustrative; not a manufacturing model or footprint.')
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
