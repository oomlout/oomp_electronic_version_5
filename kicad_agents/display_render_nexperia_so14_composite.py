"""Experimental shared material passes for the reviewed Nexperia SO14 pilot.

Only use after the independent pilot has been inspected and published. Compare
the pilot composite to that final before using the method for further parts.
The shared pass approximates indirect reflections and does not independently
path trace each marking. Every result needs individual review before publishing.
"""
from __future__ import annotations

import argparse
import json

import yaml

from kicad_agents import display_render_composite as shared
from kicad_agents.display_render_nexperia_so14_pilot_queue import EVIDENCE, MODEL_SHA256, PART
from kicad_agents.display_render_nexperia_so14_batch import FOOTPRINT, ROW

renderer = shared.renderer
_original_master_inputs = shared.master_inputs


def read_recipe(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf-8'))
    if part_id not in recipes or PART not in recipes:
        raise ValueError('No reviewed SO14 recipe for this exact part')
    recipe = recipes[part_id]
    pilot = recipes[PART]
    mark = recipe.get('marking', {})
    mpn = recipe.get('represented_mpn')
    rows = [m.groups() for line in (renderer.ROOT / EVIDENCE).read_text(encoding='utf-8').splitlines()
            if (m := ROW.match(line))]
    matches = [(text, url) for row_mpn, text, url in rows if row_mpn == mpn]
    source = renderer.ROOT / 'parts_source' / part_id / 'working.yaml'
    record = yaml.safe_load(source.read_text(encoding='utf-8')) or {}
    if (recipe.get('family') != 'integrated_circuit'
        or recipe.get('package') != pilot.get('package')
        or recipe.get('model') != pilot.get('model')
        or recipe['model'].get('sha256') != MODEL_SHA256
        or recipe.get('represented_manufacturer') != 'Nexperia'
        or record.get('manufacturer') != 'Nexperia'
        or record.get('part_number_manufacturer') != mpn
        or (record.get('kicad') or {}).get('machine_solder') != FOOTPRINT
        or record.get('dimensions_mm') != {'length': 8.7, 'width': 3.9, 'height': 1.75}
        or len(matches) != 1 or matches[0][0] != mark.get('text')
        or mark.get('evidence', {}).get('file') != EVIDENCE.as_posix()
        or mark.get('evidence', {}).get('source_record') != f'parts_source/{part_id}/working.yaml'
        or mark.get('policy') != 'verified_literal'
        or mark.get('rotation_degrees') != 90
        or not 0 < mark.get('maximum_width_mm', 0) <= 5.5
        or not 0 < mark.get('maximum_height_mm', 0) <= 1.0
        or recipe.get('output') != pilot.get('output')
        or recipe.get('disable_bump_for') != pilot.get('disable_bump_for')):
        raise ValueError('Recipe differs from the reviewed Nexperia SO14 setup')
    manifest = renderer.ROOT / 'parts' / PART / 'data/display_render/manifest.json'
    if not manifest.is_file():
        raise ValueError('Inspect and publish the independent pilot first')
    published = json.loads(manifest.read_text(encoding='utf-8'))
    if published.get('part_id') != PART or published.get('recipe') != pilot:
        raise ValueError('Published pilot differs from the current recipe')
    return recipe


def master_inputs(recipe, studio):
    inputs = _original_master_inputs(recipe, studio)
    inputs['so14_adapter_sha256'] = renderer.digest(__file__)
    return inputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    master = sub.add_parser('make-master')
    master.add_argument('part_id')
    render = sub.add_parser('render')
    render.add_argument('part_id')
    render.add_argument('--output')
    args = parser.parse_args()
    adapter_hash = renderer.digest(__file__)
    shared.read_recipe = read_recipe
    shared.master_inputs = master_inputs
    if args.command == 'make-master':
        shared.make_master(args.part_id)
    else:
        shared.render(args.part_id, args.output)
    if renderer.digest(__file__) != adapter_hash:
        raise RuntimeError('SO14 adapter changed during rendering; do not publish output')


if __name__ == '__main__':
    main()
