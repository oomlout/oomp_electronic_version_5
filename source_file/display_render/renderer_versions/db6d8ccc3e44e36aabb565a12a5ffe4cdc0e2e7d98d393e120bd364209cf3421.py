"""Render the reviewed Kangnex terminal model with green housing materials."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from kicad_agents import display_model_kangnex_wj127_2p as model
from kicad_agents import display_render as renderer
from kicad_agents import display_render_kangnex_wj127_2p_queue as batch


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
        raise ValueError('Recipe differs from reviewed terminal candidate')
    model_file = renderer.ROOT / batch.MODEL
    model_hash = renderer.digest(model_file)
    adapter_hash = renderer.digest(__file__)
    queue_hash = renderer.digest(batch.__file__)

    def locate(relative_path, model_root=None):
        if relative_path != batch.MODEL or model_root is not None:
            raise ValueError('Unexpected model')
        return model_file

    def load(path, specification):
        if path != model_file or specification.get('sha256') != model_hash:
            raise ValueError('Model changed')
        groups, lower, upper, counts = model.build()
        vertices = np.asarray([v for group in groups.values() for v in group['vertices']])
        if (set(groups) != {'coating', 'termination'} or not np.allclose(vertices.min(axis=0), lower, atol=.001)
            or not np.allclose(vertices.max(axis=0), upper, atol=.001)
            or not np.allclose(upper-lower, specification['expected_bounds_mm'], atol=.001)):
            raise ValueError('Procedural terminal model bounds or material roles changed')
        return groups, lower, upper, counts

    renderer.locate_model = locate
    renderer.load_coloured_step = load
    import mitsuba as mi
    original_load = mi.load_dict
    original_scene = renderer.render_scene
    seen = []
    camera = [1.3, -2.4, 2.1]

    def render_scene(groups, lower, upper, recipe, studio, scratch, pixels, samples):
        return original_scene(groups, lower, upper, recipe, dict(studio, camera_direction=camera), scratch, pixels, samples)

    def load_scene(scene, *positional, **keyword):
        if not isinstance(scene, dict) or scene.get('type') != 'scene':
            raise ValueError('Unexpected Mitsuba scene')
        material = scene.get('coating', {}).get('bsdf', {})
        if material.get('type') != 'blendbsdf' or material.get('body', {}).get('type') != 'roughplastic':
            raise ValueError('Unexpected terminal housing material')
        material['body']['diffuse_reflectance'] = {'type': 'rgb', 'value': [.025, .22, .085]}
        metal = scene.get('termination', {}).get('bsdf', {})
        if metal.get('type') != 'principled' or metal.get('metallic') != 1.0:
            raise ValueError('Unexpected terminal metal material')
        metal['base_color'] = {'type': 'rgb', 'value': [.32, .36, .40]}
        seen.append(True)
        return original_load(scene, *positional, **keyword)

    mi.load_dict = load_scene
    renderer.render_scene = render_scene
    try:
        renderer.generate(batch.PART, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    finally:
        mi.load_dict = original_load
        renderer.render_scene = original_scene
    if len(seen) != 1 or renderer.digest(model_file) != model_hash or renderer.digest(__file__) != adapter_hash or renderer.digest(batch.__file__) != queue_hash:
        raise RuntimeError('Model, adapter, queue or material adjustment changed during rendering')
    path = out / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['source_header'] = 'Procedural display-only geometry; see ' + batch.MODEL
    manifest['model']['generator_sha256'] = model_hash
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['model']['queue_sha256'] = queue_hash
    manifest['model']['material_note'] = 'Green housing shade and metallic finishes are illustrative.'
    manifest['render']['camera_direction_override'] = camera
    manifest['input_fingerprint'] = hashlib.sha256((manifest['input_fingerprint'] + model_hash + adapter_hash + queue_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
