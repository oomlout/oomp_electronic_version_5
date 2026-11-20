"""Prepare individually evidenced Nexperia DIP-14 follow-ons after pilot review."""
import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_ti_dip14_pilot_queue import PART, ROOT, RECIPE_FILE, MODEL_SHA256

EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_INFINEON_IR211X_DIP14_EVIDENCE.md'
FOOTPRINT = 'Package_DIP:DIP-14_W7.62mm'
ROW = re.compile(r'^\| `([^`]+)` \| ([^|]+?) \| `([^`]+)` \| \[[^]]+\]\((https://www\.infineon\.com/[^)]+)\) \|$')


def prepare(recipes):
    pilot = recipes[PART]
    if (pilot.get('represented_mpn') != 'SN74HC10N' or pilot.get('marking', {}).get('text') != 'SN74HC10N'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256
        or pilot.get('model', {}).get('required_roles') != ['coating', 'termination']
        or 'projecting leads' not in pilot.get('appearance_status', '')):
        raise ValueError('DIP-14 pilot changed')
    raw = (ROOT/EVIDENCE).read_bytes()
    rows = [m.groups() for line in raw.decode('utf8').splitlines() if (m := ROW.match(line))]
    if len(rows) != 3 or len({r[0] for r in rows}) != len(rows): raise ValueError('Evidence table changed')
    result = {}
    for part, mpn, text, _ in rows:
        record = yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'Infineon Technologies' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        recipe = copy.deepcopy(pilot); recipe['represented_mpn'] = mpn; recipe['represented_manufacturer'] = 'Infineon Technologies'
        recipe['appearance_status'] = ('Illustrative KiCad DIP-14 model; catalogue records 10 × 5 mm, with unspecified reference, no height or footprint, conflicting with approximately 19 mm length of this representative DIP-14 body. Model total 6.98 mm height includes projecting pins; this is not a verified mechanical model or PCB footprint.')
        mark = recipe['marking']; mark['text'] = text; mark['policy'] = 'illustrative_literal'
        mark['evidence'] = {'file': EVIDENCE, 'sha256': hashlib.sha256(raw).hexdigest(),
            'document': 'Infineon IR211x DIP-14 illustrative marking and package review', 'source_record': f'parts_source/{part}/working.yaml'}
        mark['appearance_status'] = (f'{text} is an illustrative family identifier; the manufacturer uses a generic placeholder and exact complete marking is unconfirmed. Typeface, orientation, '
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
    print(f'Validated {len(additions)} Infineon DIP-14 identities; added={args.add}')


if __name__ == '__main__': main()
