"""Experimental TSSOP24 shared passes, gated on the independent published pilot.

Compare a scratch pilot with its independent final before rendering candidates;
each marking needs inspection. Indirect reflections are approximate.
"""
import argparse
import json
from kicad_agents import display_render_composite as shared
from kicad_agents import display_render_tssop24_batch01 as batch
from kicad_agents.display_render_nexperia_tssop24_pilot_queue import PART

renderer = shared.renderer
_original_master_inputs = shared.master_inputs


def read_recipe(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    published_path = renderer.ROOT/'parts'/PART/'data/display_render/manifest.json'
    if not published_path.is_file(): raise ValueError('Inspect and publish the independent TSSOP24 pilot first')
    published = json.loads(published_path.read_text(encoding='utf8'))
    if published.get('part_id') != PART or published.get('recipe') != recipes.get(PART):
        raise ValueError('Published TSSOP24 pilot differs from the recipe')
    candidates = batch.prepare(recipes)
    if part_id == PART: return recipes[PART]
    if part_id not in candidates or recipes.get(part_id) != candidates[part_id]:
        raise ValueError('No exact reviewed TSSOP24 candidate recipe')
    return recipes[part_id]


def master_inputs(recipe, studio):
    inputs = _original_master_inputs(recipe, studio)
    inputs['tssop24_adapter_sha256'] = renderer.digest(__file__)
    inputs['tssop24_batch_sha256'] = renderer.digest(batch.__file__)
    return inputs


def main():
    parser = argparse.ArgumentParser(description=__doc__); sub = parser.add_subparsers(dest='command', required=True)
    master = sub.add_parser('make-master'); master.add_argument('part_id')
    render = sub.add_parser('render'); render.add_argument('part_id'); render.add_argument('--output', required=True)
    args = parser.parse_args(); adapter_hash = renderer.digest(__file__); batch_hash = renderer.digest(batch.__file__)
    shared.read_recipe = read_recipe; shared.master_inputs = master_inputs
    if args.command == 'make-master': shared.make_master(args.part_id)
    else: shared.render(args.part_id, args.output)
    if renderer.digest(__file__) != adapter_hash or renderer.digest(batch.__file__) != batch_hash:
        raise RuntimeError('TSSOP24 adapter or batch changed during rendering; do not publish')


if __name__ == '__main__': main()
