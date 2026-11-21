"""Render reviewed procedural KBP geometry and spatially aligned markings."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from kicad_agents import display_model_mdd_kbp as model
from kicad_agents import display_render as renderer
from kicad_agents import display_render_mdd_kbp_queue as batch


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=batch.PARTS); parser.add_argument('--output', required=True)
    parser.add_argument('--pixels', type=int); parser.add_argument('--samples', type=int)
    args = parser.parse_args(); out = Path(args.output)
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise FileExistsError('Existing output preserved')
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    if recipes.get(args.part) != batch.prepare(recipes)[args.part]:
        raise ValueError('Recipe differs from reviewed KBP candidate')
    model_file = renderer.ROOT / batch.MODEL; model_hash = renderer.digest(model_file)
    adapter_hash = renderer.digest(__file__); queue_hash = renderer.digest(batch.__file__)
    if model_hash != batch.MODEL_SHA: raise ValueError('Procedural model changed')
    original_textures = renderer.create_textures

    def locate(relative_path, model_root=None):
        if relative_path != batch.MODEL or model_root is not None: raise ValueError('Unexpected model')
        return model_file

    def load(path, specification):
        if path != model_file or specification.get('sha256') != model_hash: raise ValueError('Model changed')
        groups, lower, upper, counts = model.build()
        vertices = np.asarray([v for group in groups.values() for v in group['vertices']])
        if (set(groups) != {'coating', 'termination'} or not np.allclose(vertices.min(axis=0), lower, atol=1e-6)
            or not np.allclose(vertices.max(axis=0), upper, atol=1e-6)
            or not np.allclose(upper-lower, specification['expected_bounds_mm'], atol=.001)):
            raise ValueError('Procedural model bounds or roles changed')
        return groups, lower, upper, counts

    def textures(marking, text, bounds, folder):
        if text != batch.PARTS[args.part] + '\n+  ~  ~  -': raise ValueError('Unexpected marking')
        metadata = original_textures(marking, '', bounds, folder)
        font_path = renderer.find_font(marking['font_file'])
        font = ImageFont.truetype(str(font_path), 180)
        image = Image.new('L', (1024, 512), 0)
        draw = ImageDraw.Draw(image)

        def put(label, x_mm, y_mm, width_mm, height_mm):
            box = draw.textbbox((0, 0), label, font=font)
            glyph = Image.new('L', (box[2]-box[0]+4, box[3]-box[1]+4), 0)
            ImageDraw.Draw(glyph).text((2-box[0], 2-box[1]), label, fill=255, font=font)
            w = width_mm / 14.0 * 1024; h = height_mm / 23.8 * 512
            scale = min(w/glyph.width, h/glyph.height)
            glyph = glyph.resize((max(1, round(glyph.width*scale)), max(1, round(glyph.height*scale))), Image.Resampling.LANCZOS)
            px = round((x_mm + 7.0) / 14.0 * 1024)
            py = round((5.3 - y_mm) / 23.8 * 512)
            image.paste(glyph, (px-glyph.width//2, py-glyph.height//2))

        put(batch.PARTS[args.part], 0.0, 1.2, 8.0, 2.0)
        for symbol, x in zip(('+', '~', '~', '-'), (-5.715, -1.905, 1.905, 5.715)):
            put(symbol, x, -4.15, 1.0, 1.0)
        image.save(Path(folder) / 'marking.png')
        return {'file': font_path.name, 'sha256': renderer.digest(font_path), 'bitmap_size': [1024, 512]}

    renderer.locate_model = locate; renderer.load_coloured_step = load; renderer.create_textures = textures
    renderer.generate(args.part, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    if renderer.digest(model_file) != model_hash or renderer.digest(__file__) != adapter_hash or renderer.digest(batch.__file__) != queue_hash:
        raise RuntimeError('Model, adapter or queue changed during rendering')
    path = out / 'manifest.json'; manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['source_header'] = 'Procedural display-only geometry; see ' + batch.MODEL
    manifest['model']['generator_sha256'] = model_hash; manifest['model']['adapter_sha256'] = adapter_hash
    manifest['model']['queue_sha256'] = queue_hash
    manifest['input_fingerprint'] = hashlib.sha256((manifest['input_fingerprint'] + model_hash + adapter_hash + queue_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__': main()
