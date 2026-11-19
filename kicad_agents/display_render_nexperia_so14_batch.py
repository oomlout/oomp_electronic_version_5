"""Prepare individually evidenced Nexperia SO14 candidates after the pilot.

Validation is the default. --add requires a published, matching pilot and never
overwrites a different recipe. Every final still needs individual visual review.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

import yaml

from kicad_agents.display_render_nexperia_so14_pilot_queue import (
    EVIDENCE, MODEL_SHA256, PART, ROOT, RECIPE_FILE,
)

ROW = re.compile(r'^\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*\[[^]]+\]\((https://www\.nexperia\.com/[^)]+)\)\s*\|$')
FOOTPRINT = 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm'


def candidates():
    evidence = (ROOT / EVIDENCE).read_text(encoding='utf-8')
    rows = [m.groups() for line in evidence.splitlines() if (m := ROW.match(line))]
    if len(rows) != 31 or len({mpn for mpn, _, _ in rows}) != len(rows):
        raise ValueError('Evidence table changed; review it before preparing a batch')
    wanted = {mpn: (mark, url) for mpn, mark, url in rows}
    found = {}
    for path in (ROOT / 'parts_source').glob('electronic_ic_*/working.yaml'):
        record = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
        mpn = record.get('part_number_manufacturer')
        if mpn not in wanted or record.get('manufacturer') != 'Nexperia':
            continue
        if mpn in found:
            raise ValueError(f'Duplicate catalogue identity for {mpn}')
        if (record.get('kicad') or {}).get('machine_solder') != FOOTPRINT:
            raise ValueError(f'Footprint changed for {mpn}')
        if record.get('dimensions_mm') != {'length': 8.7, 'width': 3.9, 'height': 1.75}:
            raise ValueError(f'Dimensions need review for {mpn}')
        found[mpn] = (path.parent.name, *wanted[mpn])
    if set(found) != set(wanted):
        raise ValueError(f'Missing or changed identities: {sorted(set(wanted) - set(found))}')
    return found


def prepare(recipes, found):
    pilot = recipes[PART]
    if (pilot.get('family') != 'integrated_circuit'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256
        or pilot.get('marking', {}).get('text') != '74HC00D'):
        raise ValueError('Pilot recipe changed; review before batch preparation')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    if pilot['marking']['evidence']['sha256'] != evidence_sha:
        raise ValueError('Evidence changed since the pilot recipe was prepared')
    result = {}
    for mpn, (part, text, url) in found.items():
        if part == PART:
            continue
        recipe = copy.deepcopy(pilot)
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = text
        recipe['marking']['evidence']['source_record'] = f'parts_source/{part}/working.yaml'
        recipe['marking']['appearance_status'] = (
            f'Nexperia lists {text} as the package marking. Typeface, orientation, '
            'placement and variable lot/date details are illustrative.'
        )
        result[part] = recipe
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'Existing recipe differs for {part}; preserve it')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf-8'))
    found = candidates()
    additions = prepare(recipes, found)
    if args.add:
        manifest_path = ROOT / 'parts' / PART / 'data/display_render/manifest.json'
        if not manifest_path.is_file():
            raise ValueError('Publish and inspect the pilot before staging this batch')
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        if manifest.get('part_id') != PART or manifest.get('recipe') != recipes[PART]:
            raise ValueError('Published pilot does not match the current recipe')
        for part, recipe in additions.items():
            recipes.setdefault(part, recipe)
        updated = (json.dumps(recipes, indent=2, ensure_ascii=False) + '\n').encode('utf-8')
        if RECIPE_FILE.read_bytes() != original:
            raise RuntimeError('Recipes changed during validation; refusing to overwrite')
        if updated != original:
            temp_path = None
            try:
                with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as file:
                    temp_path = Path(file.name)
                    file.write(updated)
                    file.flush()
                    os.fsync(file.fileno())
                if RECIPE_FILE.read_bytes() != original:
                    raise RuntimeError('Recipes changed before replacement; refusing to overwrite')
                os.replace(temp_path, RECIPE_FILE)
            finally:
                if temp_path is not None and temp_path.exists():
                    temp_path.unlink()
    print(f'Validated {len(found)} source identities; {len(additions)} additional candidates; added={args.add}')


if __name__ == '__main__':
    main()
