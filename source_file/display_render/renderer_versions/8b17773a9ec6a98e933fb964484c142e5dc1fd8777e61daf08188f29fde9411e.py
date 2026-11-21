"""Shared SMA passes for individually evidenced MDD Schottky diodes.

Compare the independently rendered SS14 pilot before using these passes for
other parts. Every output and its provenance must be individually reviewed.
"""
import argparse
import json
from kicad_agents import display_render_composite as shared
from kicad_agents import display_render_mdd_ss1_sma_queue as first
from kicad_agents import display_render_mdd_ss235_sma_queue as other

renderer = shared.renderer
PILOT = first.PREFIX + 'ss14'
original_inputs = shared.master_inputs


def read_recipe(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    candidates = {**first.prepare(recipes), **other.prepare(recipes)}
    if part_id not in candidates or recipes.get(part_id) != candidates[part_id]:
        raise ValueError('No individually reviewed MDD SMA recipe')
    pilot = recipes[PILOT]
    if (recipes[part_id]['model'] != pilot['model'] or recipes[part_id]['output'] != pilot['output']
        or recipes[part_id]['marking'].get('maximum_width_mm') != 1.45
        or recipes[part_id]['marking'].get('maximum_height_mm') != .5
        or recipes[part_id]['marking'].get('offset_x_mm') != .45):
        raise ValueError('SMA geometry or marking layout differs from pilot')
    path = renderer.ROOT / 'parts' / PILOT / 'data/display_render/manifest.json'
    if not path.is_file() or json.loads(path.read_text(encoding='utf8')).get('recipe') != pilot:
        raise ValueError('Published independent SMA pilot is absent or differs')
    return recipes[part_id]


def master_inputs(recipe, studio):
    inputs = original_inputs(recipe, studio)
    inputs['mdd_sma_adapter_sha256'] = renderer.digest(__file__)
    inputs['mdd_sma_first_queue_sha256'] = renderer.digest(first.__file__)
    inputs['mdd_sma_other_queue_sha256'] = renderer.digest(other.__file__)
    return inputs


def main():
    parser = argparse.ArgumentParser(description=__doc__); sub = parser.add_subparsers(dest='command', required=True)
    master = sub.add_parser('make-master'); master.add_argument('part_id')
    render = sub.add_parser('render'); render.add_argument('part_id'); render.add_argument('--output', required=True)
    args = parser.parse_args(); before = [renderer.digest(p) for p in (__file__, first.__file__, other.__file__)]
    shared.read_recipe = read_recipe; shared.master_inputs = master_inputs
    if args.command == 'make-master': shared.make_master(args.part_id)
    else: shared.render(args.part_id, args.output)
    if [renderer.digest(p) for p in (__file__, first.__file__, other.__file__)] != before:
        raise RuntimeError('SMA source changed during render')


if __name__ == '__main__': main()
