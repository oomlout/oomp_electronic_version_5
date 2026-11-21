"""Stage individually mapped JSCJ BZT52 family display recipes."""
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

PREFIX = 'electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_BZT52_SOD123_FAMILY_RESEARCH.md')
PDF_SHA = 'fd5a910fc58737806f1596a6318cecd1e1264061e3ca7c6c7f13e69667e36ab5'
PARTS = {
    'BZT52C3V3': 'W3', 'BZT52C3V6': 'W4', 'BZT52C3V9': 'W5',
    'BZT52C4V3': 'W6', 'BZT52C4V7': 'W7', 'BZT52C5V1': 'W8',
    'BZT52C5V6': 'W9', 'BZT52C6V8': 'WB', 'BZT52C7V5': 'WC',
    'BZT52C8V2 WD': 'WD', 'BZT52C9V1': 'WE', 'BZT52C15': 'WJ',
    'BZT52C16': 'WK', 'BZT52C20': 'WM', 'BZT52C22': 'WN',
    'BZT52C24': 'WO', 'BZT52C33': 'WR', 'BZT52C39': 'WT',
}


def part_id(mpn):
    return PREFIX + mpn.lower().replace(' ', '_')


def prepare(recipes):
    pilot = recipes[PILOT]
    if pilot['model']['sha256'] != MODEL_SHA or pilot['marking']['text'] != 'WF':
        raise ValueError('Pilot changed')
    pdf = ROOT / 'parts_source' / PILOT / 'datasheet.pdf'
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != PDF_SHA:
        raise ValueError('Reviewed family PDF changed')
    evidence_bytes = (ROOT / EVIDENCE).read_bytes()
    evidence_sha = hashlib.sha256(evidence_bytes).hexdigest()
    result = {}
    for mpn, code in PARTS.items():
        part = part_id(mpn)
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'Jiangsu Changjing Electronics Technology Co., Ltd.'
            or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'height': 1.1, 'length': 1.6, 'width': 1.25}
            or (record.get('kicad') or {}).get('machine_solder') != 'Diode_SMD:D_SOD-123'
            or f'| {mpn} | {code} |' not in evidence_bytes.decode('utf8')):
            raise ValueError(f'{mpn} source or marking evidence changed')
        recipe = copy.deepcopy(pilot)
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = code
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': 'JSCJ BZT52 family page 2 type-code table and SOD-123 review',
            'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'JSCJ family table specifies {code} and a cathode bar; '
            'the optional green-moulding dot is omitted. Typeface, placement and finish are illustrative. '
            'The family PDF is stored with BZT52C10; exact orderable and production marking variation are not independently confirmed.')
        if mpn == 'BZT52C8V2 WD':
            recipe['marking']['appearance_status'] += ' WD matches the type code; whether it is an orderable suffix is unverified.'
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    candidates = prepare(recipes)
    for part, recipe in candidates.items():
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{part}: existing recipe differs')
        recipes[part] = recipe
    if args.add:
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name)
                f.write((json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8'))
                f.flush(); os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original:
                raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists():
                temp.unlink()
    print(f'{len(candidates)} candidates; pilot comparison and individual image review required')


if __name__ == '__main__':
    main()
