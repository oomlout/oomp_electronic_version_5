"""Render an explicitly selected KiCad package with evidence-backed display markings.

No CAD/mesh exports are retained. STEP tessellation and textures are temporary.
Run: python -m kicad_agents.display_render electronic_resistor_0603_10000_ohm
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import math
import os
from pathlib import Path
import tempfile
import time
from importlib.metadata import version

from kicad_agents.package_markings import marking_text

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / 'source_file/display_render/recipes.json'
STUDIO = ROOT / 'source_file/display_render/studio.json'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def locate_model(relative_path, model_root=None):
    from kicad_agents.kicad_cli import installation_directories
    roots = []
    override = model_root or os.environ.get('OOMP_KICAD_3DMODEL_DIR')
    if override:
        roots.append(Path(override))
    else:
        for installation in installation_directories():
            roots.extend([installation / 'share/kicad/3dmodels', installation / 'share/3dmodels'])
        roots.extend([Path('/usr/share/kicad/3dmodels'),
                      Path('/Applications/KiCad/KiCad.app/Contents/SharedSupport/3dmodels')])
    for root in roots:
        path = (root / relative_path).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError('Model path must remain within the selected KiCad model root')
        if path.is_file():
            return path
    raise FileNotFoundError('KiCad package model missing. Set OOMP_KICAD_3DMODEL_DIR or --model-root. No silent geometry fallback.')


def load_coloured_step(path, model):
    """Preserve STEP face colours as explicit material regions, and validate scale."""
    import cadquery as cq
    import numpy as np
    from OCP.STEPCAFControl import STEPCAFControl_Reader
    from OCP.TDocStd import TDocStd_Document
    from OCP.TCollection import TCollection_ExtendedString
    from OCP.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_ColorType
    from OCP.TDF import TDF_LabelSequence
    from OCP.Quantity import Quantity_Color, Quantity_TOC_sRGB
    from OCP.IFSelect import IFSelect_RetDone

    doc = TDocStd_Document(TCollection_ExtendedString('display-model'))
    reader = STEPCAFControl_Reader()
    reader.SetColorMode(True)
    if reader.ReadFile(str(path)) != IFSelect_RetDone or not reader.Transfer(doc):
        raise ValueError(f'Cannot read STEP model: {path}')
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    colours = XCAFDoc_DocumentTool.ColorTool_s(doc.Main())
    labels = TDF_LabelSequence()
    shapes.GetFreeShapes(labels)
    if labels.Length() != 1:
        raise ValueError('This pilot adapter expects one root shape. Assembly transforms need a separate reviewed adapter.')
    shape = cq.Shape.cast(shapes.GetShape_s(labels.Value(1)))
    if not shape.isValid():
        raise ValueError('Invalid KiCad source shape')
    box = shape.BoundingBox()
    lower = np.array([box.xmin, box.ymin, box.zmin])
    upper = np.array([box.xmax, box.ymax, box.zmax])
    actual = upper - lower
    if not np.allclose(actual, model['expected_bounds_mm'], atol=model['dimension_tolerance_mm'], rtol=0):
        raise ValueError(f'Unexpected package dimensions {actual.tolist()}; check units/model selection before rendering')
    groups = defaultdict(lambda: dict(vertices=[], normals=[], triangles=[]))
    colour_counts = defaultdict(int)
    for face in shape.Faces():
        colour = Quantity_Color()
        if not colours.GetColor(face.wrapped, XCAFDoc_ColorType.XCAFDoc_ColorSurf, colour):
            raise ValueError('Source face has no material colour; review this package adapter')
        # OCCT exposes linear RGB internally; STEP's authored palette is sRGB.
        key = ','.join(f'{v:.3f}' for v in colour.Values(Quantity_TOC_sRGB))
        if key not in model['role_by_source_colour']:
            raise ValueError(f'Unreviewed source face colour {key}')
        role = model['role_by_source_colour'][key]
        colour_counts[key] += 1
        vertices, triangles = face.tessellate(0.003, 0.08)
        group = groups[role]
        offset = len(group['vertices'])
        group['vertices'].extend(v.toTuple() for v in vertices)
        group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
        group['triangles'].extend(tuple(index + offset for index in t) for t in triangles)
    expected = set(model.get('required_roles', ['coating', 'ceramic', 'termination']))
    supported = {'coating', 'ceramic', 'termination', 'pin_indicator'}
    if not expected or not expected <= supported or set(groups) != expected:
        raise ValueError(f'Material regions {set(groups)} do not match reviewed roles {expected}')
    return groups, lower, upper, dict(colour_counts)


def find_font(filename):
    configured = os.environ.get('OOMP_MARKING_FONT')
    candidates = [Path(configured)] if configured else [
        Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts' / filename,
        Path(os.environ.get('LOCALAPPDATA', '')) / 'Microsoft/Windows/Fonts' / filename,
    ]
    for path in candidates:
        if path.is_file():
            return path
    raise FileNotFoundError('Marking font not found. Set OOMP_MARKING_FONT explicitly; do not silently substitute.')


def create_textures(marking, text, bounds_mm, folder):
    """Planar top projection with a separately shaded ink mask and subtle microtexture."""
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    width, height = 1024, 512
    mask = Image.new('L', (width, height), 0)
    font_path = None
    if text:
        font_path = find_font(marking['font_file'])
        font = ImageFont.truetype(str(font_path), 350)
        box = ImageDraw.Draw(mask).multiline_textbbox((0, 0), text, font=font, align='center')
        left, top = math.floor(box[0]), math.floor(box[1])
        right, bottom = math.ceil(box[2]), math.ceil(box[3])
        glyph_width, text_height = right - left, bottom - top
        if glyph_width <= 0 or text_height <= 0:
            raise ValueError('Marking has no visible glyphs')
        underline = marking.get('underline', False)
        if underline and '\n' in text:
            raise ValueError('Underlined marking must be a single line')
        gap = max(3, round(text_height * .10)) if underline else 0
        thickness = max(2, round(text_height * .045)) if underline else 0
        glyph = Image.new('L', (glyph_width, text_height + gap + thickness), 0)
        draw = ImageDraw.Draw(glyph)
        draw.multiline_text((-left, -top), text, fill=255, font=font, align='center')
        if underline:
            draw.rectangle((0, text_height + gap, glyph_width - 1, glyph.height - 1), fill=255)
        max_width = width * marking['maximum_width_mm'] / bounds_mm[0]
        max_height = height * marking['maximum_height_mm'] / bounds_mm[1]
        if max_width > width * .7 or max_height > height * .75:
            raise ValueError('Marking exceeds the reviewed central coating area')
        scale = min(max_width / glyph.width, max_height / glyph.height)
        glyph = glyph.resize((round(glyph.width * scale), round(glyph.height * scale)), Image.Resampling.LANCZOS)
        mask.paste(glyph, ((width - glyph.width) // 2, (height - glyph.height) // 2))
    mask.save(folder / 'marking.png')
    rng = np.random.default_rng(19)
    noise = np.clip(rng.normal(127, 25, (512, 1024)), 0, 255).astype('uint8')
    Image.fromarray(noise).save(folder / 'grain.png')
    return {'file': font_path.name if font_path else None,
            'sha256': digest(font_path) if font_path else None, 'bitmap_size': [width, height]}


def write_meshes(groups, lower, upper, folder):
    import numpy as np
    scale = float(max(upper - lower))
    origin = (lower + upper) / 2
    origin[2] = lower[2]
    for role, group in groups.items():
        points = np.array(group['vertices'])
        uvs = (points[:, :2] - lower[:2]) / (upper[:2] - lower[:2])
        points = (points - origin) / scale
        with (folder / f'{role}.obj').open('w', encoding='ascii') as file:
            for v in points:
                file.write('v ' + ' '.join(f'{x:.8f}' for x in v) + '\n')
            for uv in uvs:
                file.write(f'vt {uv[0]:.8f} {uv[1]:.8f}\n')
            for normal in group['normals']:
                file.write('vn ' + ' '.join(f'{x:.8f}' for x in normal) + '\n')
            for triangle in group['triangles']:
                file.write('f ' + ' '.join(f'{i+1}/{i+1}/{i+1}' for i in triangle) + '\n')
    return scale


def repair_nonfinite_pixels(linear):
    """Repair isolated invalid path-tracer samples; reject widespread failures."""
    import numpy as np
    invalid = ~np.isfinite(linear).all(axis=2)
    count = int(invalid.sum())
    if not count:
        return linear, 0
    if count > max(4, int(invalid.size * .0001)):
        raise ValueError(f'Render contains {count} non-finite pixels; inspect the scene/backend')
    repaired = linear.copy()
    height, width = invalid.shape
    for y, x in np.argwhere(invalid):
        for radius in (2, 4, 8, 16):
            ys, ye = max(0, y-radius), min(height, y+radius+1)
            xs, xe = max(0, x-radius), min(width, x+radius+1)
            neighbours = linear[ys:ye, xs:xe][~invalid[ys:ye, xs:xe]]
            if len(neighbours):
                repaired[y, x] = np.median(neighbours, axis=0)
                break
        else:
            raise ValueError('Non-finite render sample has no nearby valid pixels')
    return repaired, count


def render_scene(groups, lower, upper, recipe, studio, scratch, pixels, samples):
    import numpy as np
    import mitsuba as mi
    import drjit as dr
    # The scalar backend is a portable multithreaded fallback when LLVM is absent.
    variant = 'llvm_ad_rgb' if dr.has_backend(dr.JitBackend.LLVM) else 'scalar_rgb'
    mi.set_variant(variant)
    T = mi.ScalarTransform4f
    rgb = lambda value: {'type': 'rgb', 'value': value}
    bitmap = lambda name: {'type': 'bitmap', 'filename': str(scratch / name), 'raw': True, 'wrap_mode': 'clamp'}
    materials = {
        'termination': {'type': 'principled', 'base_color': rgb([.61, .65, .70]),
                        'metallic': 1., 'roughness': .24, 'anisotropic': .22},
        'ceramic': {'type': 'roughplastic', 'diffuse_reflectance': rgb([.53, .50, .43]),
                    'alpha': .30, 'int_ior': 1.52},
        'pin_indicator': {'type': 'roughplastic', 'diffuse_reflectance': rgb([.48, .47, .44]),
                          'alpha': .4, 'int_ior': 1.48},
        'coating': {'type': 'blendbsdf', 'weight': bitmap('marking.png'),
                    'body': {'type': 'roughplastic', 'diffuse_reflectance': rgb([.016, .019, .024]),
                             'alpha': .30, 'int_ior': 1.48},
                    'ink': {'type': 'roughplastic', 'diffuse_reflectance': rgb([.65, .64, .59]),
                            'alpha': .38, 'int_ior': 1.45}},
    }
    scale = write_meshes(groups, lower, upper, scratch)
    height = float((upper[2] - lower[2]) / scale)
    target = np.array([0., 0., height * .48])
    direction = np.array(studio['camera_direction'], dtype=float)
    direction /= np.linalg.norm(direction)
    transform = T().look_at(origin=target + direction * 5, target=target, up=[0, 0, 1])
    # Fit the projected model envelope, preserving room for its contact shadow.
    extent = (upper - lower) / scale
    bounds = np.array([[x, y, z] for x in [-extent[0]/2, extent[0]/2]
                       for y in [-extent[1]/2, extent[1]/2] for z in [0, height]])
    basis = np.asarray(transform.matrix)[:3, :3]
    span = np.ptp(bounds @ basis, axis=0)[:2].max()
    half = float(span / (2 * (1 - 2 * studio['framing_margin'])))
    scene = {
        'type': 'scene', 'integrator': {'type': 'path', 'max_depth': 8, 'hide_emitters': True},
        'sensor': {'type': 'orthographic', 'to_world': transform @ T().scale([half, half, 1]),
                   'sampler': {'type': 'independent', 'sample_count': samples},
                   'film': {'type': 'hdrfilm', 'width': pixels, 'height': pixels,
                            'pixel_format': 'rgb', 'rfilter': {'type': 'tent'}}},
        'floor': {'type': 'rectangle', 'to_world': T().translate([0, 0, -.0001]) @ T().scale([100, 100, 1]),
                  'bsdf': {'type': 'diffuse', 'reflectance': rgb(studio['floor_reflectance'])}},
        'environment': {'type': 'constant', 'radiance': rgb(studio['world_radiance'])},
    }
    disabled_bump = recipe.get('disable_bump_for', [])
    if not isinstance(disabled_bump, list) or set(disabled_bump) - set(groups):
        raise ValueError('Bump exclusions must name reviewed material roles in this model')
    for role in groups:
        material = materials[role]
        if role not in disabled_bump:
            material = {'type': 'bumpmap', 'texture': bitmap('grain.png'),
                        'scale': .00035 if role == 'termination' else .00018,
                        'material': material}
        scene[role] = {'type': 'obj', 'filename': str(scratch / f'{role}.obj'),
                       'face_normals': False, 'bsdf': material}
    for light in studio['lights']:
        scene[light['name']] = {
            'type': 'rectangle',
            'to_world': T().look_at(origin=light['position'], target=target, up=[0, 0, 1]) @ T().scale([*light['half_size'], 1]),
            'emitter': {'type': 'area', 'radiance': rgb(light['radiance'])}}
    started = time.perf_counter()
    linear = np.asarray(mi.render(mi.load_dict(scene), seed=studio['seed'], spp=samples))
    linear, repaired_pixels = repair_nonfinite_pixels(linear)
    linear = np.maximum(linear, 0) * studio['exposure']
    mapped = np.clip(linear * (2.51 * linear + .03) / (linear * (2.43 * linear + .59) + .14), 0, 1)
    srgb = np.where(mapped <= .0031308, 12.92 * mapped, 1.055 * mapped ** (1 / 2.4) - .055)
    import cv2
    pixels_rgb = np.rint(srgb * 255).astype('uint8')
    denoised = cv2.fastNlMeansDenoisingColored(
        cv2.cvtColor(pixels_rgb, cv2.COLOR_RGB2BGR), None,
        studio['denoise_strength'], studio['denoise_strength'], 7, 15)
    pixels_rgb = cv2.cvtColor(denoised, cv2.COLOR_BGR2RGB)
    def portable(value):
        if isinstance(value, dict):
            return {k: Path(v).name if k == 'filename' else portable(v) for k, v in value.items()}
        return value
    return pixels_rgb, {'variant': variant, 'seconds': round(time.perf_counter() - started, 2),
        'samples': samples, 'pixels': pixels, 'materials': portable(materials), 'normalized_unit_mm': scale,
        'tone_mapping': 'ACES fitted curve then sRGB; not Blender AgX',
        'nonfinite_pixels_repaired': repaired_pixels,
        'bump_disabled_roles': disabled_bump,
        'denoising': {'method': 'OpenCV non-local means', 'strength': studio['denoise_strength']}}


def generate(part_id, *, model_root=None, output=None, pixels=None, samples=None, check=False, force=False):
    from PIL import Image
    recipes = json.loads(RECIPES.read_text(encoding='utf-8'))
    if part_id not in recipes:
        raise ValueError('No reviewed display recipe for this exact component. Add evidence before rendering.')
    recipe = recipes[part_id]
    studio = json.loads(STUDIO.read_text(encoding='utf-8'))
    model_path = locate_model(recipe['model']['relative_path'], model_root)
    if digest(model_path) != recipe['model']['sha256']:
        raise ValueError('KiCad model changed. Review geometry/colours and update its pinned hash explicitly.')
    text = marking_text(recipe['marking'])
    evidence = ROOT / recipe['marking']['evidence']['file']
    if not evidence.is_file():
        raise FileNotFoundError(f'Marking evidence missing: {evidence}')
    if digest(evidence) != recipe['marking']['evidence']['sha256']:
        raise ValueError('Marking evidence changed. Recheck the page and policy before updating its hash.')
    destination = Path(output) if output else ROOT / 'parts' / part_id / 'data/display_render'
    pixels = pixels or recipe['output']['pixels']
    samples = samples or recipe['output']['samples']
    if not 128 <= pixels <= 4096 or not 1 <= samples <= 4096:
        raise ValueError('Pixels must be 128–4096 and samples 1–4096')
    runtime = {name: version(name) for name in ('cadquery', 'cadquery-ocp', 'mitsuba', 'drjit', 'numpy', 'Pillow', 'opencv-python-headless')}
    inputs = {'recipe': recipe, 'studio': studio, 'pixels': pixels, 'samples': samples,
              'renderer_sha256': digest(__file__), 'marking_code_sha256': digest(Path(__file__).with_name('package_markings.py')),
              'font_sha256': digest(find_font(recipe['marking']['font_file'])) if text else None,
              'runtime': runtime}
    fingerprint = hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest()
    manifest_file = destination / 'manifest.json'
    if not check and not force and manifest_file.is_file():
        existing = json.loads(manifest_file.read_text(encoding='utf-8'))
        if (existing.get('input_fingerprint') == fingerprint
            and all((destination / name).is_file() and digest(destination/name) == item['sha256']
                    for name, item in existing.get('artifacts', {}).items())
            and set(existing.get('artifacts', {})) == {'render.png', 'preview.webp'}):
            print(f'Reused verified render cache: {destination}', flush=True)
            return
    groups, lower, upper, colour_counts = load_coloured_step(model_path, recipe['model'])
    print(f'{part_id}: {text!r}; bounds {(upper-lower).tolist()} mm; {sum(len(g["triangles"]) for g in groups.values())} triangles', flush=True)
    if check:
        return
    destination.mkdir(parents=True, exist_ok=True)
    # Temporary directory owns all intermediate geometry. No STL, STEP, GLB or
    # Blender scene is written into the catalogue by this pipeline.
    with tempfile.TemporaryDirectory(prefix='oomp-display-') as temporary:
        scratch = Path(temporary)
        font = create_textures(recipe['marking'], text, upper - lower, scratch)
        pixels_rgb, settings = render_scene(groups, lower, upper, recipe, studio, scratch, pixels, samples)
        picture = Image.fromarray(pixels_rgb)
        picture.save(destination / 'render.png', optimize=True)
        picture.thumbnail((recipe['output']['thumbnail_pixels'], recipe['output']['thumbnail_pixels']), Image.Resampling.LANCZOS)
        picture.save(destination / 'preview.webp', quality=90, method=6)
    manifest = {
        'schema_version': 1, 'part_id': part_id, 'purpose': 'display_only', 'recipe': recipe,
        'input_fingerprint': fingerprint, 'runtime': runtime,
        'recipe_sha256': hashlib.sha256(json.dumps(recipe, sort_keys=True).encode()).hexdigest(),
        'model': {'relative_path': recipe['model']['relative_path'], 'sha256': digest(model_path),
                  'actual_bounds_mm': (upper-lower).tolist(), 'source_face_colours': colour_counts,
                  'triangle_count': sum(len(g['triangles']) for g in groups.values()),
                  'source_header': model_path.read_text(encoding='utf-8').split('FILE_DESCRIPTION')[0]},
        'marking': {'text': text, 'font': font, 'evidence_sha256': digest(evidence)},
        'studio': studio, 'render': settings,
        'renderer_source_sha256': digest(__file__),
        'artifacts': {name: {'sha256': digest(destination/name), 'bytes': (destination/name).stat().st_size}
                      for name in ['render.png', 'preview.webp']},
    }
    (destination / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(f'Rendered {destination} ({settings["seconds"]} seconds)', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part_id')
    parser.add_argument('--model-root')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--pixels', type=int)
    parser.add_argument('--samples', type=int)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--force', action='store_true', help='Re-render even when all cached input/artifact hashes match')
    args = parser.parse_args()
    generate(**vars(args))


if __name__ == '__main__':
    main()
