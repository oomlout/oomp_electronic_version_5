"""Lay the KiCad KBL model face up and align illustrative markings to pads."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from kicad_agents import display_render as renderer
from kicad_agents import display_render_mdd_kbl_queue as batch


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=batch.PARTS)
    parser.add_argument('--output', required=True)
    parser.add_argument('--pixels', type=int)
    parser.add_argument('--samples', type=int)
    args = parser.parse_args()
    out = Path(args.output)
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise FileExistsError('Existing output preserved')
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    if recipes.get(args.part) != batch.prepare(recipes)[args.part]:
        raise ValueError('Recipe differs from reviewed KBL candidate')
    adapter_hash = renderer.digest(__file__)
    queue_hash = renderer.digest(batch.__file__)
    original_loader = renderer.load_coloured_step
    original_textures = renderer.create_textures

    def load(path, specification):
        groups, lower, upper, counts = original_loader(path, specification)
        if set(groups) != {'coating', 'termination'}:
            raise ValueError('Unexpected KBL material roles')
        # Proper rotation (x,y,z) -> (x,z,-y) puts the wide -Y face up,
        # while retaining pad 1 to the left of pad 4.
        matrix = np.array([[1., 0., 0.], [0., 0., 1.], [0., -1., 0.]])
        for group in groups.values():
            vertices = np.asarray(group['vertices'], dtype=float)
            normals = np.asarray(group['normals'], dtype=float)
            if vertices.shape != normals.shape or not np.isfinite(vertices).all() or not np.isfinite(normals).all():
                raise ValueError('Invalid KBL mesh or normals')
            group['vertices'] = (vertices @ matrix.T).tolist()
            group['normals'] = (normals @ matrix.T).tolist()
        corners = np.array([[x, y, z] for x in (lower[0], upper[0]) for y in (lower[1], upper[1])
                            for z in (lower[2], upper[2])]) @ matrix.T
        return groups, corners.min(axis=0), corners.max(axis=0), counts

    def textures(marking, text, bounds, folder):
        if text != batch.PARTS[args.part] + '\n+  ~  ~  -':
            raise ValueError('Unexpected marking')
        if not np.allclose(bounds, [19.5, 29.05, 6.5], atol=.03):
            raise ValueError('Unexpected rotated KBL bounds')
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
            glyph = glyph.resize((max(1, round(glyph.width*scale*1024/19.5)),
                                  max(1, round(glyph.height*scale*512/29.05))), Image.Resampling.LANCZOS)
            x = round((x_mm+2.13)/19.5*1024)
            y = round((15.05-y_mm)/29.05*512)
            image.paste(glyph, (x-glyph.width//2, y-glyph.height//2))

        put(batch.PARTS[args.part], 7.62, 8.5, 10.0, 2.0)
        for symbol, x in zip(('+', '~', '~', '-'), (0., 5.08, 10.16, 15.24)):
            put(symbol, x, 1.7, 1.4, 1.4)
        image.save(Path(folder) / 'marking.png')
        return {'file': font_path.name, 'sha256': renderer.digest(font_path), 'bitmap_size': [1024, 512]}

    renderer.load_coloured_step = load
    renderer.create_textures = textures
    renderer.generate(args.part, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    if renderer.digest(__file__) != adapter_hash or renderer.digest(batch.__file__) != queue_hash:
        raise RuntimeError('Adapter or queue changed during rendering')
    path = out / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['source_bounds_mm'] = [19.5, 6.5, 29.05]
    manifest['model']['display_orientation'] = '(x,y,z) -> (x,z,-y); wide -Y face up'
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['model']['queue_sha256'] = queue_hash
    manifest['input_fingerprint'] = hashlib.sha256((manifest['input_fingerprint'] + adapter_hash + queue_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
