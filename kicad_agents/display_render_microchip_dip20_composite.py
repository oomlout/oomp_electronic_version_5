"""Use compared DIP-20 shared passes for the second individually evidenced batch."""
import argparse
import hashlib
import json
from pathlib import Path
from kicad_agents import display_render_ti_dip20_composite as base
from kicad_agents import display_render_microchip_dip20 as batch

shared = base.shared
renderer = base.renderer


def read_recipe(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    base.read_recipe(base.PART)
    candidates = batch.prepare(recipes)
    if part_id not in candidates or recipes.get(part_id) != candidates[part_id]:
        raise ValueError('No exact reviewed mixed DIP-20 recipe')
    return recipes[part_id]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part_id'); parser.add_argument('--output', required=True)
    args = parser.parse_args(); validator_hash = renderer.digest(__file__); batch_hash = renderer.digest(batch.__file__)
    shared.read_recipe = read_recipe; shared.master_inputs = base.master_inputs
    shared.render(args.part_id, args.output)
    if renderer.digest(__file__) != validator_hash or renderer.digest(batch.__file__) != batch_hash:
        raise RuntimeError('Candidate validator changed during rendering')
    path = Path(args.output)/'manifest.json'; manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['composite']['candidate_validator_sha256'] = validator_hash
    manifest['composite']['candidate_batch_sha256'] = batch_hash
    manifest['input_fingerprint'] = hashlib.sha256(
        (manifest['input_fingerprint'] + validator_hash + batch_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf8')


if __name__ == '__main__': main()
