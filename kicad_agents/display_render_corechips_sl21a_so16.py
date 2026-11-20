"""Prepare individually evidenced Texas Instruments SO16 follow-ons after pilot review."""
import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_nexperia_so16_pilot_queue import PART, ROOT, RECIPE_FILE, MODEL_SHA256

EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_CORECHIPS_SL21A_SO16_EVIDENCE.md'
FOOTPRINT = 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm'
ROW = re.compile(r'^\| `([^`]+)` \| ([^|]+?) \| `([^`]+)` \| \[[^]]+\]\((https://datasheet\.lcsc\.com/[^)]+)\) \|$')


def prepare(recipes):
    pilot = recipes[PART]
    if (pilot.get('represented_mpn') != '74HC138D,653' or pilot.get('marking', {}).get('text') != '74HC138D'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256):
        raise ValueError('SO16 pilot changed')
    raw = (ROOT/EVIDENCE).read_bytes()
    rows = [m.groups() for line in raw.decode('utf8').splitlines() if (m := ROW.match(line))]
    if len(rows) != 1 or len({r[0] for r in rows}) != len(rows): raise ValueError('Evidence table changed')
    result = {}
    for part, mpn, text, _ in rows:
        record = yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') not in ('', None) or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
            or record.get('dimensions_mm') != {'length': 9.9, 'width': 3.9}):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        recipe = copy.deepcopy(pilot); recipe['represented_mpn'] = mpn; recipe['represented_manufacturer'] = 'CoreChips'
        recipe['appearance_status'] = ('Illustrative KiCad SOIC-16 model is 1.75 mm high. Catalogue lists 9.9 x 3.9 mm without height or footprint; manufacturer field is absent and CoreChips identity is inferred. Model height is unverified; not a verified mechanical model or PCB footprint.')
        mark = recipe['marking']; mark['text'] = text; mark['policy'] = 'illustrative_literal'
        mark['evidence'] = {'file': EVIDENCE, 'sha256': hashlib.sha256(raw).hexdigest(),
            'document': 'CoreChips SL2.1A SOP16 illustrative identifier and package review', 'source_record': f'parts_source/{part}/working.yaml'}
        mark['appearance_status'] = (f'{text} is an illustrative family identifier; the exact physical marking is not confirmed. Typeface, orientation, '
                                     'placement and variable lot/date details are illustrative.')
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
    print(f'Validated {len(additions)} CoreChips SO16 identities; added={args.add}')


if __name__ == '__main__': main()
