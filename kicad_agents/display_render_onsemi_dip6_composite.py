"""Shared procedural DIP-6 lighting, gated on the independently reviewed pilot.

Compare the pilot composite with its independent final before using candidates.
The shared-pass method approximates reflections from markings.
"""
import argparse
import hashlib
import json

from kicad_agents import display_model_onsemi_dip6 as model
from kicad_agents import display_render_composite as shared
from kicad_agents import display_render_onsemi_4n25_dip6_queue as pilot_queue
from kicad_agents import display_render_onsemi_4n35_dip6_queue as a
from kicad_agents import display_render_onsemi_moc3021_dip6_queue as b
from kicad_agents import display_render_onsemi_moc3023_dip6_queue as c

renderer = shared.renderer
PART = pilot_queue.PART
MODEL = pilot_queue.MODEL
QUEUES = {q.PART: q for q in (a, b, c)}
original_inputs = shared.master_inputs


def read_recipe(part_id):
    import yaml

    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    published = json.loads((renderer.ROOT / 'parts' / PART / 'data/display_render/manifest.json').read_text(encoding='utf8'))
    if published.get('part_id') != PART or published.get('recipe') != recipes.get(PART):
        raise ValueError('The reviewed independent DIP-6 pilot changed')
    if part_id == PART:
        return recipes[PART]
    q = QUEUES.get(part_id)
    if q is None:
        raise ValueError('Unknown DIP-6 candidate')
    record = yaml.safe_load((renderer.ROOT / 'parts_source' / part_id / 'working.yaml').read_text(encoding='utf8'))
    evidence = renderer.digest(renderer.ROOT / q.EVIDENCE)
    candidate = q.reviewed_recipe(record, recipes, evidence)
    if recipes.get(part_id) != candidate or candidate['model'] != recipes[PART]['model']:
        raise ValueError('DIP-6 candidate or model changed')
    return candidate


def master_inputs(recipe, studio):
    inputs = original_inputs(recipe, studio)
    inputs['dip6_adapter_sha256'] = renderer.digest(__file__)
    inputs['dip6_generator_sha256'] = renderer.digest(model.__file__)
    inputs['dip6_queue_sha256'] = {q.PART: renderer.digest(q.__file__) for q in (pilot_queue, a, b, c)}
    return inputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('make-master', 'render'))
    parser.add_argument('part_id')
    parser.add_argument('--output')
    args = parser.parse_args()
    if args.command == 'render' and not args.output:
        parser.error('render requires --output')
    model_path = renderer.ROOT / MODEL
    adapter_hash = renderer.digest(__file__)
    source_hash = renderer.digest(model_path)
    queue_hashes = [renderer.digest(q.__file__) for q in (pilot_queue, a, b, c)]

    def locate(relative_path, model_root=None):
        if relative_path != MODEL or model_root is not None:
            raise ValueError('Unexpected procedural model path')
        return model_path

    def load(path, specification):
        if path != model_path or specification['sha256'] != source_hash:
            raise ValueError('Procedural model changed')
        return model.build()

    renderer.locate_model = locate
    renderer.load_coloured_step = load
    shared.read_recipe = read_recipe
    shared.master_inputs = master_inputs
    if args.command == 'make-master':
        if args.part_id != PART:
            raise ValueError('Only the independent pilot may build shared passes')
        shared.make_master(PART)
    else:
        shared.render(args.part_id, args.output)
    if (renderer.digest(__file__) != adapter_hash or renderer.digest(model_path) != source_hash
        or [renderer.digest(q.__file__) for q in (pilot_queue, a, b, c)] != queue_hashes):
        raise RuntimeError('Shared render input changed during rendering')


if __name__ == '__main__':
    main()
