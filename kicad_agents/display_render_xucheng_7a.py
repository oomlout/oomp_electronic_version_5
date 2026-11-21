"""Render the Xucheng display model with a dielectric glass tube."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from kicad_agents import display_model_xucheng_5f_2a as model
from kicad_agents import display_render as renderer
from kicad_agents import display_render_xucheng_7a_queue as batch


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
        raise ValueError('Recipe differs from reviewed glass fuse candidate')
    model_file = renderer.ROOT / batch.MODEL
    model_hash, adapter_hash, queue_hash = (renderer.digest(p) for p in (model_file, Path(__file__), Path(batch.__file__)))

    def locate(relative_path, model_root=None):
        if relative_path != batch.MODEL or model_root is not None:
            raise ValueError('Unexpected model')
        return model_file

    def load(path, specification):
        if path != model_file or specification.get('sha256') != model_hash:
            raise ValueError('Model changed')
        groups, lower, upper, counts = model.build()
        vertices = np.asarray([v for group in groups.values() for v in group['vertices']])
        if (set(groups) != {'coating', 'ceramic', 'termination', 'pin_indicator'} or not np.allclose(vertices.min(axis=0), lower, atol=.002)
            or not np.allclose(vertices.max(axis=0), upper, atol=.002)
            or not np.allclose(upper-lower, specification['expected_bounds_mm'], atol=.001)):
            raise ValueError('Glass fuse bounds or material roles changed')
        return groups, lower, upper, counts

    renderer.locate_model = locate
    renderer.load_coloured_step = load
    original_write = renderer.write_meshes
    original_textures = renderer.create_textures

    def end_face_textures(marking, text, bounds_mm, folder):
        return original_textures(marking, text, [5.2, 5.2, 5.2], folder)

    def end_face_mesh(groups, lower, upper, folder):
        scale = original_write(groups, lower, upper, folder)
        path = folder / 'pin_indicator.obj'
        lines = path.read_text(encoding='ascii').splitlines()
        coordinates = iter(groups['pin_indicator']['vertices'])
        for i, line in enumerate(lines):
            if line.startswith('vt '):
                _, y, z = next(coordinates)
                lines[i] = f'vt {(y + 2.6) / 5.2:.8f} {z / 5.2:.8f}'
        path.write_text('\n'.join(lines) + '\n', encoding='ascii')
        return scale

    renderer.create_textures = end_face_textures
    renderer.write_meshes = end_face_mesh
    import mitsuba as mi
    original_load = mi.load_dict
    seen = []

    def load_scene(scene, *positional, **keyword):
        if not isinstance(scene, dict) or scene.get('type') != 'scene':
            raise ValueError('Unexpected Mitsuba scene')
        glass = scene.get('coating', {}).get('bsdf', {})
        wire = scene.get('ceramic', {}).get('bsdf', {})
        metal = scene.get('termination', {}).get('bsdf', {})
        end = scene.get('pin_indicator', {}).get('bsdf', {})
        if (glass.get('type') != 'blendbsdf' or wire.get('type') != 'roughplastic'
            or metal.get('type') != 'principled' or end.get('type') != 'roughplastic'):
            raise ValueError('Unexpected glass fuse materials')
        marking_bitmap = glass['weight']
        # Mutate the shared dictionaries so the manifest captures actual materials.
        glass.clear()
        glass.update({'type': 'dielectric', 'int_ior': 1.52, 'ext_ior': 1.0})
        wire.clear()
        wire.update({'type': 'principled', 'base_color': {'type': 'rgb', 'value': [.55, .49, .40]},
                     'metallic': 1.0, 'roughness': .32})
        metal['base_color'] = {'type': 'rgb', 'value': [.61, .65, .70]}
        end.clear()
        end.update({'type': 'blendbsdf', 'weight': marking_bitmap,
                    'body': {'type': 'principled', 'base_color': {'type': 'rgb', 'value': [.61, .65, .70]},
                             'metallic': 1.0, 'roughness': .24},
                    'ink': {'type': 'roughplastic', 'diffuse_reflectance': {'type': 'rgb', 'value': [.025, .025, .022]},
                            'alpha': .4, 'int_ior': 1.48}})
        seen.append(True)
        return original_load(scene, *positional, **keyword)

    mi.load_dict = load_scene
    try:
        renderer.generate(batch.PART, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    finally:
        mi.load_dict = original_load
        renderer.create_textures = original_textures
        renderer.write_meshes = original_write
    if len(seen) != 1 or any(renderer.digest(p) != h for p, h in
        ((model_file, model_hash), (Path(__file__), adapter_hash), (Path(batch.__file__), queue_hash))):
        raise RuntimeError('Model, adapter, queue or material adjustment changed during rendering')
    path = out / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['source_header'] = 'Procedural display-only geometry; see ' + batch.MODEL
    manifest['model']['generator_sha256'] = model_hash
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['model']['queue_sha256'] = queue_hash
    manifest['model']['material_note'] = 'Glass, wire, cap finishes and marking layout are illustrative; logo and approval marks omitted.'
    manifest['input_fingerprint'] = hashlib.sha256((manifest['input_fingerprint'] + model_hash + adapter_hash + queue_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
