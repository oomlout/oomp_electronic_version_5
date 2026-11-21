"""Stage three explicitly illustrative, unspecified 0603 magnetic components."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_inductor_0603_10_micro_henry_sunlord_sdfl1608s100ktf'
PARTS = {'electronic_inductor_0603_30_ohm': '30_ohm',
         'electronic_inductor_0603_470_ohm': '470_ohm',
         'electronic_inductor_0603_33_nano_henry': '33_nano_henry'}
MODEL_HASH = 'b0136ad7160588d2f5dac8c85da84a35646db656b5bc54bbb873b6b548eedbb3'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_0603_INDUCTORS_RESEARCH.md')


def prepare(recipes):
    pilot = recipes[PILOT]
    if pilot['model']['sha256'] != MODEL_HASH:
        raise ValueError('Reviewed model changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    result = {}
    for part, value in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('taxonomy_2') != 'inductor' or record.get('taxonomy_3') != '0603'
            or record.get('taxonomy_4') != value or (record.get('taxonomy_5') or '') != ''
            or record.get('manufacturer') not in ('', None) or record.get('part_number_manufacturer') not in ('', None)
            or record.get('dimensions_mm') != {'length': 1.6, 'width': .8}
            or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
            or (source / 'datasheet.pdf').exists()):
            raise ValueError(f'{part}: unspecified identity or package assumptions changed')
        recipe = copy.deepcopy(pilot)
        recipe.update(represented_manufacturer='Unspecified', represented_mpn='generic 0603 ' + value.replace('_', ' '))
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': 'Unspecified generic 0603 magnetic component model review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = 'Deliberately unmarked illustration; no manufacturer or exact part is specified.'
        recipe['appearance_status'] = ('Generic KiCad 0603 chip illustration; manufacturer, MPN, footprint and height are unspecified. '
            'The 1.6 x 0.8 x 0.8 mm model height is an example, not a verified source dimension. '
            'The source value is retained as named; measurement frequency and construction are unspecified. '
            'Dark body, metallic ends and any omitted markings are illustrative; not manufacturing CAD or a footprint.')
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
    print('Three generic 0603 chip candidates; independent preview and final review required')


if __name__ == '__main__':
    main()
