"""Render only the reviewed Nexperia diode recipes with proven SOT-23 passes."""
import argparse
import hashlib
import json
from pathlib import Path

from kicad_agents import display_render_sot23_composite as shared
from kicad_agents import display_render_nexperia_sot23_diodes_queue as queue


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=queue.PARTS)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    root = shared.ROOT
    adapter_hash = shared.renderer.digest(__file__)
    queue_hash = shared.renderer.digest(queue.__file__)
    original_read = shared.read_recipe
    pilot = original_read(queue.REFERENCE)

    def reviewed_read(part_id):
        if part_id not in queue.PARTS:
            raise ValueError('Only reviewed diode candidates may use this adapter')
        recipes = json.loads(shared.renderer.RECIPES.read_text(encoding='utf8'))
        recipe = recipes[part_id]
        if (recipe != queue.candidate(part_id, recipes) or recipe['model'] != pilot['model']
            or recipe['family'] != pilot['family'] or recipe.get('disable_bump_for')
            or recipe['output'] != pilot['output'] or recipe['marking'].get('rotation_degrees') != 90
            or recipe['marking'].get('maximum_width_mm') != 1.5
            or recipe['marking'].get('maximum_height_mm') != .5):
            raise ValueError('Diode recipe or reviewed shared geometry changed')
        return recipe

    shared.read_recipe = reviewed_read
    shared.render(args.part, args.output)
    if shared.renderer.digest(__file__) != adapter_hash or shared.renderer.digest(queue.__file__) != queue_hash:
        raise RuntimeError('Diode adapter or queue changed during rendering')
    path = Path(args.output) / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['composite']['candidate_validator_sha256'] = adapter_hash
    manifest['composite']['candidate_batch_sha256'] = queue_hash
    manifest['input_fingerprint'] = hashlib.sha256(
        (manifest['input_fingerprint'] + adapter_hash + queue_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
