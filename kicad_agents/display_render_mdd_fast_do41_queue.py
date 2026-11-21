"""Stage four reviewed MDD fast-recovery DO-41 display illustrations."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_mdd_1n400x_axial_queue import MODEL_SHA

PREFIX = 'electronic_diode_fast_recovery_do_41_mdd_microdiode_semiconductor_'
PARTS = {PREFIX + x.lower(): x for x in ('FR104', 'FR107', 'HER107', 'SF18')}
PILOT = 'electronic_diode_rectifier_do_41_mdd_microdiode_semiconductor_1n4001'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_FAST_DO41_RESEARCH.md')
PDFS = {'fr104': 'ee69054205d45685a9b9c0aff48ba221d23499be8c81ff60bc02894907a783c4',
        'her107': 'a0dbd27d727387ce3b9fed56bef875c70675d97ad63b835aa27103a3c8027b8a',
        'sf18': '837813e9b7d38bfd0343c3f543ab1de74d4499525d588bcfe9e3a5cf610b8991'}


def prepare(recipes):
    for name, expected in PDFS.items():
        if hashlib.sha256((ROOT / 'parts_source' / (PREFIX + name) / 'datasheet.pdf').read_bytes()).hexdigest() != expected:
            raise ValueError(f'{name}: reviewed PDF changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    result = {}
    for part, mpn in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
        expected_dims = {'height': 4.0, 'length': 5.2, 'width': 2.7} if mpn == 'SF18' else {'length': 10.0, 'width': 5.0}
        expected_footprint = 'Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal' if mpn == 'SF18' else ''
        if (record.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != expected_dims or (record.get('kicad') or {}).get('machine_solder') != expected_footprint):
            raise ValueError(f'{mpn}: source identity, dimensions or footprint changed')
        if mpn == 'FR107' and (source / 'datasheet.pdf').exists():
            raise ValueError('FR107 gained a local PDF; review it')
        recipe = copy.deepcopy(recipes[PILOT])
        if recipe['model']['sha256'] != MODEL_SHA:
            raise ValueError('Unexpected reviewed KiCad DO-41 model')
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = mpn
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': 'MDD fast-recovery DO-41 family drawings and markings', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{mpn} is an illustrative partial identifier from the MDD family marking; '
            'the MDD logo is omitted. Typeface, placement and stripe width are illustrative.')
        if mpn == 'FR107':
            recipe['marking']['appearance_status'] += ' No local FR107 PDF is stored; the FR104 family PDF covers it.'
        recipe['appearance_status'] = ('KiCad DO-41 model has bent leads at 10.16 mm pitch; the manufacturer drawing shows '
            'straight leads at least 25.4 mm long. Display illustration only; not manufacturing CAD or a PCB footprint.')
        if mpn == 'SF18':
            recipe['appearance_status'] += ' The approximately 0.80 mm lead diameter exceeds the 0.64 mm drawing maximum by 0.16 mm.'
        else:
            recipe['appearance_status'] += ' The source 10 x 5 mm dimensions are placeholders and no KiCad footprint is selected.'
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    for part, recipe in prepare(recipes).items():
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{part}: existing recipe differs')
        recipes[part] = recipe
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
    print('Four fast-recovery DO-41 candidates; marked previews and final review required')


if __name__ == '__main__':
    main()
