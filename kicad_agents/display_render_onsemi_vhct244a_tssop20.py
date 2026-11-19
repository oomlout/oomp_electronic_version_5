"""Prepare individually evidenced Nexperia TSSOP20 follow-ons after pilot review."""
import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_nexperia_tssop20_pilot_queue import PART, ROOT, RECIPE_FILE, MODEL_SHA256

EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_ONSEMI_VHCT244A_TSSOP20_EVIDENCE.md'
FOOTPRINT = 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm'
ROW = re.compile(r'^\| `([^`]+)` \| ([^|]+?) \| `([^`]+)` \| \[[^]]+\]\((https://www\.onsemi\.com/[^)]+)\) \|$')


def prepare(recipes):
    pilot = recipes[PART]
    if (pilot.get('represented_mpn') != '74HC244PW,118' or pilot.get('marking', {}).get('text') != 'HC244'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256):
        raise ValueError('TSSOP20 pilot changed')
    raw = (ROOT/EVIDENCE).read_bytes()
    rows = [m.groups() for line in raw.decode('utf8').splitlines() if (m := ROW.match(line))]
    if len(rows) != 1 or len({r[0] for r in rows}) != len(rows): raise ValueError('Evidence table changed')
    result = {}
    for part, mpn, text, _ in rows:
        record = yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'onsemi' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
            or record.get('dimensions_mm') != {'length': 6.5, 'width': 4.4}):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        recipe = copy.deepcopy(pilot); recipe['represented_mpn'] = mpn; recipe['represented_manufacturer'] = 'onsemi'
        recipe['appearance_status'] = ('Illustrative KiCad TSSOP-20 model is 1.2 mm high, matching onsemi case 948AQ maximum. Catalogue source omits height and machine-solder footprint; this is not a verified PCB footprint.')
        mark = recipe['marking']; mark['text'] = text.replace('/', '\n'); mark['policy'] = 'illustrative_literal'; mark['maximum_height_mm'] = 2.0
        mark['evidence'] = {'file': EVIDENCE, 'sha256': hashlib.sha256(raw).hexdigest(),
            'document': 'onsemi TSSOP20 two-line marking and package review', 'source_record': f'parts_source/{part}/working.yaml'}
        mark['appearance_status'] = (f'onsemi lists {text.replace(chr(47), chr(32) + chr(47) + chr(32))} as a two-line package marking. Typeface, orientation, '
                                     'placement and variable lot/date details are illustrative.')
        if mpn == 'SN74ACT245PWR':
            mark['appearance_status'] += ' TI also lists ACT245 as an alternative marking.'
        if part in recipes and recipes[part] != recipe: raise ValueError(f'Conflicting recipe for {part}')
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--add', action='store_true')
    args = parser.parse_args(); original = RECIPE_FILE.read_bytes(); recipes = json.loads(original.decode('utf8'))
    additions = prepare(recipes)
    if args.add:
        m = json.loads((ROOT/'parts'/PART/'data/display_render/manifest.json').read_text(encoding='utf8'))
        if m.get('part_id') != PART or m.get('recipe') != recipes[PART]: raise ValueError('Published pilot changed')
        for part, recipe in additions.items(): recipes.setdefault(part, recipe)
        updated = (json.dumps(recipes, indent=2, ensure_ascii=False)+'\n').encode('utf8')
        if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed during validation')
        if updated != original:
            temp = None
            try:
                with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                    temp = Path(f.name); f.write(updated); f.flush(); os.fsync(f.fileno())
                if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed before replacement')
                os.replace(temp, RECIPE_FILE)
            finally:
                if temp is not None and temp.exists(): temp.unlink()
    print(f'Validated {len(additions)} onsemi TSSOP20 identities; added={args.add}')


if __name__ == '__main__': main()
