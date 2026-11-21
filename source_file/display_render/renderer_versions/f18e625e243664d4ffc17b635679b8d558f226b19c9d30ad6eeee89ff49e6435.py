"""Render the reviewed KiCad 3225 crystal with a metallic cap and gold rim."""
import argparse
import hashlib
import json
from pathlib import Path

from kicad_agents import display_render as renderer
from kicad_agents import display_render_yxc_ysx321sl_16mhz_queue as batch


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
        raise ValueError('Recipe differs from reviewed crystal candidate')
    adapter_hash, queue_hash = renderer.digest(__file__), renderer.digest(batch.__file__)
    import mitsuba as mi
    original = mi.load_dict
    seen = []

    def load_scene(scene, *a, **kw):
        if not isinstance(scene, dict) or scene.get('type') != 'scene':
            raise ValueError('Unexpected scene')
        top = scene.get('coating', {}).get('bsdf', {})
        if top.get('type') != 'blendbsdf' or top.get('body', {}).get('type') != 'roughplastic':
            raise ValueError('Unexpected crystal top material')
        top['body'] = {'type': 'principled', 'base_color': {'type': 'rgb', 'value': [.61, .65, .70]},
                       'metallic': 1., 'roughness': .24, 'anisotropic': .22}
        top['ink']['diffuse_reflectance'] = {'type': 'rgb', 'value': [.018, .019, .021]}
        base = scene.get('ceramic', {}).get('bsdf', {})
        rim = scene.get('pin_indicator', {}).get('bsdf', {})
        if base.get('type') != 'roughplastic' or rim.get('type') != 'roughplastic':
            raise ValueError('Unexpected crystal base or rim material')
        base['diffuse_reflectance'] = {'type': 'rgb', 'value': [.035, .035, .04]}
        rim.clear()
        rim.update({'type': 'principled', 'base_color': {'type': 'rgb', 'value': [.80, .57, .22]},
                    'metallic': 1., 'roughness': .28})
        seen.append(True)
        return original(scene, *a, **kw)

    mi.load_dict = load_scene
    try:
        renderer.generate(batch.PART, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    finally:
        mi.load_dict = original
    if len(seen) != 1 or renderer.digest(__file__) != adapter_hash or renderer.digest(batch.__file__) != queue_hash:
        raise RuntimeError('Crystal adapter or queue changed during rendering')
    path = out / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['model']['queue_sha256'] = queue_hash
    manifest['model']['material_note'] = 'Silver cap, gold-coloured rim, dark base and frequency inscription are illustrative.'
    manifest['input_fingerprint'] = hashlib.sha256(
        (manifest['input_fingerprint'] + adapter_hash + queue_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
