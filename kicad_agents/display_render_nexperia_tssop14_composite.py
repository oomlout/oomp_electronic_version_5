"""Experimental TSSOP-14 shared-pass adapter for individually evidenced parts.

Compare the pilot composite with the independent published pilot before use on
other components. Indirect reflections are approximate; inspect every result.
"""
from __future__ import annotations

import argparse
import hashlib
import json

import yaml

from kicad_agents import display_render_composite as shared
from kicad_agents import display_render_nexperia_tssop14_batch as batch
from kicad_agents.display_render_nexperia_tssop14_pilot_queue import MODEL_SHA256, PART

renderer = shared.renderer
_original_master_inputs = shared.master_inputs


def read_recipe(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf-8'))
    if part_id not in recipes or PART not in recipes: raise ValueError('No reviewed TSSOP recipe')
    recipe=recipes[part_id]; pilot=recipes[PART]; mark=recipe.get('marking', {}); ev=mark.get('evidence', {})
    evidence_file = batch.PILOT_EVIDENCE if part_id in (PART,batch.FOLLOWUP) else batch.EVIDENCE
    evidence_bytes = (renderer.ROOT/evidence_file).read_bytes()
    record = yaml.safe_load((renderer.ROOT/'parts_source'/part_id/'working.yaml').read_text(encoding='utf-8')) or {}
    mpn=recipe.get('represented_mpn'); text=mark.get('text')
    if (recipe.get('family') != 'integrated_circuit' or recipe.get('package') != pilot.get('package')
        or recipe.get('model') != pilot.get('model') or recipe['model'].get('sha256') != MODEL_SHA256
        or recipe.get('represented_manufacturer') != 'Nexperia' or record.get('manufacturer') != 'Nexperia'
        or record.get('part_number_manufacturer') != mpn
        or (record.get('kicad') or {}).get('machine_solder') != batch.FOOTPRINT
        or record.get('dimensions_mm') != {'length':5.0, 'width':4.4, 'height':1.1}
        or mark.get('policy') != 'verified_literal' or mark.get('rotation_degrees') != 90
        or not 0 < mark.get('maximum_width_mm',0) <= 3.0 or not 0 < mark.get('maximum_height_mm',0) <= .8
        or ev.get('file') != evidence_file or ev.get('sha256') != hashlib.sha256(evidence_bytes).hexdigest()
        or ev.get('source_record') != f'parts_source/{part_id}/working.yaml'
        or not any(part_id in line and mpn in line and f'`{text}`' in line
                   for line in evidence_bytes.decode('utf-8').splitlines())
        or recipe.get('output') != pilot.get('output')
        or recipe.get('disable_bump_for') != pilot.get('disable_bump_for')):
        raise ValueError('Recipe or source differs from reviewed TSSOP setup')
    path=renderer.ROOT/'parts'/PART/'data/display_render/manifest.json'
    if not path.is_file(): raise ValueError('Inspect and publish independent TSSOP pilot first')
    published=json.loads(path.read_text(encoding='utf-8'))
    if published.get('part_id') != PART or published.get('recipe') != pilot:
        raise ValueError('Published TSSOP pilot differs from recipe')
    return recipe


def master_inputs(recipe, studio):
    inputs=_original_master_inputs(recipe,studio)
    inputs['tssop_adapter_sha256']=renderer.digest(__file__)
    inputs['tssop_batch_sha256']=renderer.digest(batch.__file__)
    return inputs


def main():
    parser=argparse.ArgumentParser(description=__doc__); sub=parser.add_subparsers(dest='command',required=True)
    master=sub.add_parser('make-master'); master.add_argument('part_id')
    render=sub.add_parser('render'); render.add_argument('part_id'); render.add_argument('--output')
    args=parser.parse_args(); adapter_hash=renderer.digest(__file__); batch_hash=renderer.digest(batch.__file__)
    shared.read_recipe=read_recipe; shared.master_inputs=master_inputs
    if args.command == 'make-master': shared.make_master(args.part_id)
    else: shared.render(args.part_id,args.output)
    if renderer.digest(__file__) != adapter_hash or renderer.digest(batch.__file__) != batch_hash:
        raise RuntimeError('TSSOP adapter or candidate definition changed; do not publish output')


if __name__ == '__main__': main()
