"""Experimentally reuse reviewed TO-220 material passes for ST regulators.

Publish an independently path-traced pilot first. Compare the composited pilot
against it before using other candidates; inspect every output. Ink's effect on
indirect reflections is approximate and is disclosed in each manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents import display_render_composite as shared
from kicad_agents import display_render_st_l78_l79_to220_batch as batch
from kicad_agents.display_render_orientation import orient_to220_face_up

renderer = shared.renderer
original_master_inputs = shared.master_inputs
original_load = renderer.load_coloured_step


def read_recipe(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    pilot = batch.REFERENCE
    pilot_path = renderer.ROOT / 'parts' / pilot / 'data/display_render/manifest.json'
    if not pilot_path.is_file():
        raise ValueError('Publish the independently rendered TO-220 pilot first')
    published = json.loads(pilot_path.read_text(encoding='utf8'))
    if published.get('part_id') != pilot or published.get('recipe') != recipes.get(pilot) or published.get('composite'):
        raise ValueError('TO-220 pilot must match the current independently rendered recipe')
    recipe = recipes.get(part_id)
    if part_id != pilot:
        if part_id not in batch.PARTS:
            raise ValueError('Unreviewed TO-220 candidate')
        record = yaml.safe_load((renderer.ROOT / 'parts_source' / part_id / 'working.yaml').read_text(encoding='utf8'))
        if recipe != batch.candidate(part_id, record, recipes):
            raise ValueError('TO-220 candidate no longer matches its reviewed source')
    if (recipe['model'] != recipes[pilot]['model'] or recipe['family'] != 'integrated_circuit'
            or recipe['marking'].get('offset_x_mm') != -3.52
            or recipe['marking'].get('rotation_degrees') != 90
            or recipe['marking'].get('maximum_width_mm') != 7.0
            or recipe['marking'].get('maximum_height_mm') != 1.8
            or recipe['output']['pixels'] != 1400 or recipe['output']['samples'] != 256):
        raise ValueError('TO-220 geometry, marking layout or output settings changed')
    return recipe


def master_inputs(recipe, studio):
    inputs = original_master_inputs(recipe, studio)
    inputs['to220_adapter_sha256'] = renderer.digest(__file__)
    inputs['orientation_adapter_sha256'] = renderer.digest(Path(__file__).with_name('display_render_orientation.py'))
    inputs['candidate_batch_sha256'] = renderer.digest(batch.__file__)
    return inputs


def load_oriented(path, model):
    if model.get('display_orientation') != 'to220_face_up':
        raise ValueError('Unexpected TO-220 display pose')
    groups, lower, upper, colours = original_load(path, model)
    lower, upper = orient_to220_face_up(groups, lower, upper)
    return groups, lower, upper, colours


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    master = sub.add_parser('make-master')
    master.add_argument('part_id')
    render = sub.add_parser('render')
    render.add_argument('part_id')
    render.add_argument('--output', required=True)
    args = parser.parse_args()
    adapter_hash = renderer.digest(__file__)
    batch_hash = renderer.digest(batch.__file__)
    orientation_hash = renderer.digest(Path(__file__).with_name('display_render_orientation.py'))
    shared.read_recipe = read_recipe
    shared.master_inputs = master_inputs
    renderer.load_coloured_step = load_oriented
    if args.command == 'make-master':
        shared.make_master(args.part_id)
    else:
        if args.part_id != batch.REFERENCE:
            review_path = renderer.ROOT / 'tmp/display_render/st_to220_composite_review.json'
            if not review_path.is_file():
                raise ValueError('Compare and approve the scratch composited pilot first')
            review = json.loads(review_path.read_text(encoding='utf8'))
            pilot_image = renderer.ROOT / 'parts' / batch.REFERENCE / 'data/display_render/render.png'
            master = shared.MASTER_ROOT / shared.json_hash(master_inputs(read_recipe(args.part_id), json.loads(renderer.STUDIO.read_text(encoding='utf8')))) / 'manifest.json'
            if (review.get('status') != 'visually_reviewed'
                    or review.get('adapter_sha256') != adapter_hash
                    or review.get('orientation_adapter_sha256') != orientation_hash
                    or review.get('pilot_render_sha256') != renderer.digest(pilot_image)
                    or not master.is_file() or review.get('master_manifest_sha256') != renderer.digest(master)):
                raise ValueError('TO-220 comparison is missing or stale; review again')
        shared.render(args.part_id, args.output)
        path = Path(args.output) / 'manifest.json'
        manifest = json.loads(path.read_text(encoding='utf8'))
        manifest['model']['source_bounds_mm'] = [10.25, 4.455, 28.525]
        manifest['model']['display_orientation'] = 'to220_face_up'
        manifest['model']['orientation_adapter_sha256'] = orientation_hash
        manifest['composite']['candidate_validator_sha256'] = adapter_hash
        manifest['composite']['candidate_batch_sha256'] = batch_hash
        manifest['input_fingerprint'] = hashlib.sha256(
            (manifest['input_fingerprint'] + adapter_hash + batch_hash + orientation_hash).encode('ascii')).hexdigest()
        path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')
    if (renderer.digest(__file__) != adapter_hash or renderer.digest(batch.__file__) != batch_hash
            or renderer.digest(Path(__file__).with_name('display_render_orientation.py')) != orientation_hash):
        raise RuntimeError('TO-220 adapter changed during rendering; do not publish')


if __name__ == '__main__':
    main()
