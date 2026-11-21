"""Render the reviewed KiCad header with illustrative gold-coloured contacts."""
import argparse
import hashlib
import json
from pathlib import Path

from kicad_agents import display_render as renderer
from kicad_agents import display_render_hctl_header_13p_queue as batch


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--pixels', type=int)
    parser.add_argument('--samples', type=int)
    args = parser.parse_args()
    out = Path(args.output)
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise FileExistsError('Existing output preserved')
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    if recipes.get(batch.PART) != batch.prepare(recipes):
        raise ValueError('Recipe differs from reviewed header candidate')
    adapter_hash = renderer.digest(__file__)
    queue_hash = renderer.digest(batch.__file__)

    import mitsuba as mi
    original_load = mi.load_dict
    seen = []

    def load_with_gold(scene, *a, **kw):
        if not isinstance(scene, dict) or scene.get('type') != 'scene':
            raise ValueError('Unexpected Mitsuba input')
        material = scene.get('termination', {}).get('bsdf', {})
        if (material.get('type') != 'principled' or material.get('metallic') != 1.0
            or material.get('base_color') != {'type': 'rgb', 'value': [.61, .65, .70]}):
            raise ValueError('Unexpected termination material; review gold adapter')
        material['base_color'] = {'type': 'rgb', 'value': [.80, .57, .22]}
        seen.append(True)
        return original_load(scene, *a, **kw)

    mi.load_dict = load_with_gold
    try:
        renderer.generate(batch.PART, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    finally:
        mi.load_dict = original_load
    if len(seen) != 1 or renderer.digest(__file__) != adapter_hash or renderer.digest(batch.__file__) != queue_hash:
        raise RuntimeError('Gold adapter or queue changed during rendering')
    path = out / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['model']['queue_sha256'] = queue_hash
    manifest['model']['material_note'] = 'Gold-coloured contacts are illustrative; exact BOOMELE finish is unverified.'
    manifest['input_fingerprint'] = hashlib.sha256(
        (manifest['input_fingerprint'] + adapter_hash + queue_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
