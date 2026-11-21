"""Render reviewed W06 geometry with illustrative, lead-aligned top markings."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from kicad_agents import display_model_mdd_w06 as model
from kicad_agents import display_render as renderer
from kicad_agents import display_render_mdd_w06_queue as batch


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
        raise ValueError('Recipe differs from reviewed W06 candidate')
    model_file = renderer.ROOT / batch.MODEL
    model_hash = renderer.digest(model_file)
    adapter_hash = renderer.digest(__file__)
    queue_hash = renderer.digest(batch.__file__)
    original_textures = renderer.create_textures

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
            raise ValueError('Procedural model bounds or roles changed')
        return groups, lower, upper, counts

    def textures(marking, text, bounds, folder):
        if text != 'W06\n+  ~  ~  -':
            raise ValueError('Unexpected marking')
        original_textures(marking, '', bounds, folder)
        font_path = renderer.find_font(marking['font_file'])
        font = ImageFont.truetype(str(font_path), 180)
        image = Image.new('L', (1024, 512), 0)
        draw = ImageDraw.Draw(image)

        def put(label, x_mm, y_mm, max_width, max_height):
            box = draw.textbbox((0, 0), label, font=font)
            glyph = Image.new('L', (box[2]-box[0]+4, box[3]-box[1]+4), 0)
            ImageDraw.Draw(glyph).text((2-box[0], 2-box[1]), label, fill=255, font=font)
            scale = min(max_width/glyph.width, max_height/glyph.height)
            glyph = glyph.resize((max(1, round(glyph.width*scale*1024/8.8)),
                                  max(1, round(glyph.height*scale*512/8.8))), Image.Resampling.LANCZOS)
            x = round((x_mm+4.4)/8.8*1024)
            y = round((4.4-y_mm)/8.8*512)
            image.paste(glyph, (x-glyph.width//2, y-glyph.height//2))

        put('W06', 0, 0, 3.0, 1.1)
        for symbol, x, y in [('+', -2.55, 2.55), ('~', 2.55, 2.55),
                              ('~', -2.55, -2.55), ('-', 2.55, -2.55)]:
            put(symbol, x, y, .9, .9)
        image.save(Path(folder) / 'marking.png')
        return {'file': font_path.name, 'sha256': renderer.digest(font_path), 'bitmap_size': [1024, 512]}

    renderer.locate_model = locate
    renderer.load_coloured_step = load
    renderer.create_textures = textures
    # Darker neutral silver keeps the long narrow leads legible on the light
    # studio floor; this display-only finish remains illustrative.
    import mitsuba as mi
    original_load = mi.load_dict
    seen = []

    def load_scene(scene, *positional, **keyword):
        if not isinstance(scene, dict) or scene.get('type') != 'scene':
            raise ValueError('Unexpected Mitsuba scene')
        material = scene.get('termination', {}).get('bsdf', {})
        if material.get('type') != 'principled' or material.get('metallic') != 1.0:
            raise ValueError('Unexpected W06 lead material')
        material['base_color'] = {'type': 'rgb', 'value': [.32, .36, .40]}
        seen.append(True)
        return original_load(scene, *positional, **keyword)

    mi.load_dict = load_scene
    try:
        renderer.generate(batch.PART, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    finally:
        mi.load_dict = original_load
    if len(seen) != 1:
        raise RuntimeError('Expected exactly one W06 scene material adjustment')
    if renderer.digest(model_file) != model_hash or renderer.digest(__file__) != adapter_hash or renderer.digest(batch.__file__) != queue_hash:
        raise RuntimeError('Model, adapter or queue changed during rendering')
    path = out / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['source_header'] = 'Procedural display-only geometry; see ' + batch.MODEL
    manifest['model']['generator_sha256'] = model_hash
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['model']['queue_sha256'] = queue_hash
    manifest['model']['material_note'] = 'Darker neutral silver leads are an illustrative display finish.'
    manifest['input_fingerprint'] = hashlib.sha256((manifest['input_fingerprint'] + model_hash + adapter_hash + queue_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
