"""Prepare individually evidenced TI TSSOP-48 follow-ons after pilot review."""
import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_ti_tssop48_pilot_queue import PART, ROOT, RECIPE_FILE, MODEL_SHA256

EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_TI_ALVC16244_TSSOP48_EVIDENCE.md'
FOOTPRINT = 'Package_DIP:DIP-16_W7.62mm'
ROW = re.compile(r'^\| `([^`]+)` \| ([^|]+?) \| `([^`]+)` \| \[[^]]+\]\((https://www\.ti\.com/[^)]+)\) \|$')


def prepare(recipes):
    pilot = recipes[PART]
    if (pilot.get('represented_mpn') != 'SN74ALVC164245DGGR' or pilot.get('marking', {}).get('text') != 'ALVC164245' or pilot.get('model', {}).get('sha256') != MODEL_SHA256):
        raise ValueError('TSSOP-48 pilot changed')
    raw = (ROOT/EVIDENCE).read_bytes()
    rows = [m.groups() for line in raw.decode('utf8').splitlines() if (m := ROW.match(line))]
    if len(rows) != 1 or len({r[0] for r in rows}) != len(rows): raise ValueError('Evidence table changed')
    result = {}
    for part, mpn, text, _ in rows:
        record = yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'Texas Instruments' or record.get('part_number_manufacturer') != 'SN74ALVC16244ADGGRG4'
            or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        recipe = copy.deepcopy(pilot); recipe['represented_mpn'] = mpn
        recipe['appearance_status'] = ('Illustrative KiCad TSSOP-48 model is 1.0 mm high; TI DGG0048A body is 12.4-12.6 x 6.0-6.2 mm and maximum height 1.2 mm. Catalogue lists 10 x 5 mm without width reference, height or footprint, conflicting with this example. Catalogue MPN SN74ALVC16244ADGGRG4 differs from TI-listed 74ALVC16244ADGGRG4; exact equivalence unverified. Not a verified mechanical model.')
        mark = recipe['marking']; mark['text'] = text
        mark['evidence'] = {'file': EVIDENCE, 'sha256': hashlib.sha256(raw).hexdigest(),
            'document': 'TI TSSOP-48 representative example and orderable discrepancy', 'source_record': f'parts_source/{part}/working.yaml'}
        mark['appearance_status'] = (f'Texas Instruments lists {text} as the package marking for represented example 74ALVC16244ADGGRG4; exact catalogue MPN equivalence is unverified. Typeface, orientation, '
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
    print(f'Validated {len(additions)} TI TSSOP-48 identities; added={args.add}')


if __name__ == '__main__': main()

