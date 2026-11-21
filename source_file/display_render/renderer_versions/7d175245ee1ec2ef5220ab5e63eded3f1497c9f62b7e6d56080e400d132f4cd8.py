"""Use reviewed SOD-123 passes for the B5819W SL example."""
import argparse
import hashlib
import json
from pathlib import Path
from kicad_agents import display_render_jscj_bzt52_sod123_composite as base
from kicad_agents import display_render_b5819w_sl_queue as batch

shared, renderer = base.shared, base.renderer


def read_recipe(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    base.read_recipe(base.PILOT)
    if part_id != batch.PART or recipes.get(part_id) != batch.prepare(recipes):
        raise ValueError('No reviewed B5819W SL recipe')
    return recipes[part_id]


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('part_id'); parser.add_argument('--output', required=True)
    args = parser.parse_args(); source_hash = renderer.digest(__file__); batch_hash = renderer.digest(batch.__file__)
    shared.read_recipe = read_recipe; shared.master_inputs = base.master_inputs
    shared.render(args.part_id, args.output)
    if renderer.digest(__file__) != source_hash or renderer.digest(batch.__file__) != batch_hash:
        raise RuntimeError('Candidate validator changed; do not publish output')
    path = Path(args.output) / 'manifest.json'; manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['composite']['candidate_validator_sha256'] = source_hash
    manifest['composite']['candidate_batch_sha256'] = batch_hash
    manifest['input_fingerprint'] = hashlib.sha256((manifest['input_fingerprint'] + source_hash + batch_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__': main()
