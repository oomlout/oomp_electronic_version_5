"""Experimental TI SOIC-8 shared-pass adapter, gated on a published pilot.

Compare the independent pilot with its composite before using this method for
other parts. The method approximates indirect reflections and every image and
marking needs individual review before publication.
"""
from __future__ import annotations

import argparse
import hashlib
import json

import yaml

from kicad_agents import display_render_composite as shared
from kicad_agents import display_render_ti_soic8_batch as batch
from kicad_agents.display_render_ti_soic8_batch import CANDIDATES, FOOTPRINT
from kicad_agents.display_render_ti_soic8_pilot_queue import MODEL_SHA256, PART

renderer = shared.renderer
_original_master_inputs = shared.master_inputs


def read_recipe(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf-8'))
    if part_id not in recipes or PART not in recipes:
        raise ValueError('No reviewed TI SOIC-8 recipe for this exact part')
    recipe = recipes[part_id]; pilot = recipes[PART]; mark = recipe.get('marking', {})
    entry = next((x for x in CANDIDATES if x[0] == part_id), None)
    if part_id == PART:
        entry = (PART, 'NE5532DR', 'N5532', pilot['marking']['evidence']['file'])
    if entry is None:
        raise ValueError('Part is outside the individually researched TI candidates')
    _, mpn, text, evidence_file = entry
    record = yaml.safe_load((renderer.ROOT/'parts_source'/part_id/'working.yaml').read_text(encoding='utf-8')) or {}
    dims = record.get('dimensions_mm') or {}
    evidence = mark.get('evidence', {})
    evidence_path = renderer.ROOT/evidence_file
    evidence_bytes = evidence_path.read_bytes()
    if (recipe.get('family') != 'integrated_circuit' or recipe.get('package') != pilot.get('package')
        or recipe.get('model') != pilot.get('model') or recipe['model'].get('sha256') != MODEL_SHA256
        or recipe.get('represented_manufacturer') != 'Texas Instruments' or recipe.get('represented_mpn') != mpn
        or record.get('manufacturer') != 'Texas Instruments' or record.get('part_number_manufacturer') != mpn
        or (record.get('kicad') or {}).get('machine_solder') != FOOTPRINT
        or dims.get('length') != 4.9 or dims.get('width') != 3.9 or dims.get('height') not in (None, 1.75)
        or mark.get('policy') != 'verified_literal' or mark.get('text') != text
        or mark.get('rotation_degrees', 0) != 0
        or not 0 < mark.get('maximum_width_mm', 0) <= 2.6
        or not 0 < mark.get('maximum_height_mm', 0) <= 1.0
        or evidence.get('file') != evidence_file or evidence.get('sha256') != hashlib.sha256(evidence_bytes).hexdigest()
        or evidence.get('source_record') != f'parts_source/{part_id}/working.yaml'
        or not any(part_id in line and mpn in line and f'`{text}`' in line
                   for line in evidence_bytes.decode('utf-8').splitlines())
        or recipe.get('output') != pilot.get('output')
        or recipe.get('disable_bump_for') != pilot.get('disable_bump_for')):
        raise ValueError('Recipe or source differs from the researched TI SOIC-8 setup')
    manifest = renderer.ROOT/'parts'/PART/'data/display_render/manifest.json'
    if not manifest.is_file():
        raise ValueError('Inspect and publish the independent TI pilot first')
    published = json.loads(manifest.read_text(encoding='utf-8'))
    if published.get('part_id') != PART or published.get('recipe') != pilot:
        raise ValueError('Published TI pilot differs from the current recipe')
    return recipe


def master_inputs(recipe, studio):
    inputs = _original_master_inputs(recipe, studio)
    inputs['ti_soic8_adapter_sha256'] = renderer.digest(__file__)
    inputs['ti_soic8_batch_sha256'] = renderer.digest(batch.__file__)
    return inputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    master = sub.add_parser('make-master'); master.add_argument('part_id')
    render = sub.add_parser('render'); render.add_argument('part_id'); render.add_argument('--output')
    args = parser.parse_args()
    source_hash = renderer.digest(__file__)
    batch_hash = renderer.digest(batch.__file__)
    shared.read_recipe = read_recipe; shared.master_inputs = master_inputs
    if args.command == 'make-master': shared.make_master(args.part_id)
    else: shared.render(args.part_id, args.output)
    if renderer.digest(__file__) != source_hash or renderer.digest(batch.__file__) != batch_hash:
        raise RuntimeError('TI adapter changed during rendering; do not publish output')


if __name__ == '__main__':
    main()
