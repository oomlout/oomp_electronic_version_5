"""Experimental radial capacitor display renderer with curved sleeve markings.

No CAD/mesh exports are retained. STEP tessellation and textures are temporary.
Use an explicitly staged radial recipe and inspect a low-resolution preview
before enabling publication.
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

import numpy as np


def straight_sleeve_triangles(vertices, triangles, center_xy, radius, lower_z, upper_z, tolerance=.05):
    """Select triangles wholly on the reviewed cylindrical straight sleeve."""
    v = np.asarray(vertices, dtype=float)
    tri = np.asarray(triangles, dtype=int)
    center = np.asarray(center_xy, dtype=float)
    if (v.ndim != 2 or v.shape[1] != 3 or tri.ndim != 2 or tri.shape[1] != 3
        or center.shape != (2,) or not np.isfinite(v).all() or not np.isfinite(center).all()
        or not np.isfinite([radius, lower_z, upper_z, tolerance]).all()
        or radius <= 0 or tolerance <= 0 or upper_z <= lower_z
        or tri.size == 0 or tri.min() < 0 or tri.max() >= len(v)):
        raise ValueError('Invalid reviewed sleeve geometry')
    points = v[tri]
    radii = np.linalg.norm(points[:, :, :2] - center, axis=2)
    on_cylinder = np.all(np.abs(radii - radius) <= tolerance, axis=1)
    in_height = np.all((points[:, :, 2] >= lower_z - 1e-6)
                       & (points[:, :, 2] <= upper_z + 1e-6), axis=1)
    return on_cylinder & in_height


def stretch_sleeve(vertices, normals, triangles, lower_z, upper_z, extra_height):
    """Lengthen the straight sleeve while preserving leads and end details.

    Triangles must not straddle either deformation boundary. This prevents a
    silently bent face; split/re-tessellate geometry where necessary. Normals
    are transformed using the local inverse transpose.
    """
    v = np.asarray(vertices, dtype=float)
    n = np.asarray(normals, dtype=float)
    tri = np.asarray(triangles, dtype=int)
    if (v.ndim != 2 or v.shape[1] != 3 or n.shape != v.shape or tri.ndim != 2
        or tri.shape[1] != 3 or not np.isfinite(v).all() or not np.isfinite(n).all()
        or not np.isfinite([lower_z, upper_z, extra_height]).all()
        or upper_z <= lower_z or extra_height < 0 or tri.size == 0
        or tri.min() < 0 or tri.max() >= len(v)):
        raise ValueError('Invalid reviewed radial mesh or deformation')
    zs = v[tri, 2]
    for boundary in (lower_z, upper_z):
        if np.any((zs.min(axis=1) < boundary - 1e-7) & (zs.max(axis=1) > boundary + 1e-7)):
            raise ValueError('Triangle crosses a sleeve deformation boundary')
    scale = 1 + extra_height / (upper_z - lower_z)
    out = v.copy()
    middle = (v[:, 2] > lower_z) & (v[:, 2] < upper_z)
    above = v[:, 2] >= upper_z
    out[middle, 2] = lower_z + (v[middle, 2] - lower_z) * scale
    out[above, 2] = v[above, 2] + extra_height
    # Boundary vertices can belong to a stretched face even when their
    # position lies exactly on the boundary. Use incident triangles to select
    # the inverse-transpose transform; reject ambiguous sloped shared normals.
    transformed = n.copy()
    centers = zs.mean(axis=1)
    used_middle = np.zeros(len(v), dtype=bool)
    used_outer = np.zeros(len(v), dtype=bool)
    np.logical_or.at(used_middle, tri.ravel(), np.repeat((centers > lower_z) & (centers < upper_z), 3))
    np.logical_or.at(used_outer, tri.ravel(), np.repeat((centers <= lower_z) | (centers >= upper_z), 3))
    if np.any(used_middle & used_outer & (np.abs(n[:, 2]) > 1e-7)):
        raise ValueError('Split shared sloped normals at deformation boundaries')
    transformed[used_middle, 2] /= scale
    lengths = np.linalg.norm(transformed, axis=1)
    if np.any(lengths <= 0) or not np.isfinite(lengths).all():
        raise ValueError('Invalid radial mesh normal')
    transformed /= lengths[:, None]
    return out, transformed


def sleeve_triangle_uv(vertices, triangles, center_xy, bottom_z, top_z, seam_angle=0.0):
    """Return per-corner cylindrical UVs with each triangle unwrapped at seam.

    The caller must assign the UVs only to reviewed sleeve surfaces and use a
    repeating texture. Per-corner UVs permit the same vertex on either side of
    the seam to carry different coordinates.
    """
    v = np.asarray(vertices, dtype=float)
    tri = np.asarray(triangles, dtype=int)
    center = np.asarray(center_xy, dtype=float)
    if (v.ndim != 2 or v.shape[1] != 3 or tri.ndim != 2 or tri.shape[1] != 3
        or center.shape != (2,) or not np.isfinite(v).all() or not np.isfinite(center).all()
        or not np.isfinite([bottom_z, top_z, seam_angle]).all() or top_z <= bottom_z
        or tri.size == 0 or tri.min() < 0 or tri.max() >= len(v)):
        raise ValueError('Invalid cylindrical mapping input')
    points = v[tri]
    radial = points[:, :, :2] - center
    if np.any(np.linalg.norm(radial, axis=2) < 1e-8):
        raise ValueError('Cylindrical mapping is undefined on the axis')
    u = np.mod((np.arctan2(radial[:, :, 1], radial[:, :, 0]) - seam_angle) / (2 * np.pi), 1.0)
    crossing = np.ptp(u, axis=1) > .5
    u[crossing] += (u[crossing] < .5)
    if np.any(np.ptp(u, axis=1) > .5 + 1e-7):
        raise ValueError('Triangle spans too much of the cylinder')
    height = (points[:, :, 2] - bottom_z) / (top_z - bottom_z)
    if np.any(height < -1e-6) or np.any(height > 1 + 1e-6):
        raise ValueError('Sleeve UV extends beyond reviewed height')
    return np.stack((u, height), axis=2)



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
    top_marking_faces = 0
    for face in shape.Faces():
        colour = Quantity_Color()
        if not colours.GetColor(face.wrapped, XCAFDoc_ColorType.XCAFDoc_ColorSurf, colour):
            raise ValueError('Source face has no material colour; review this package adapter')
        # OCCT exposes linear RGB internally; STEP's authored palette is sRGB.
        key = ','.join(f'{v:.3f}' for v in colour.Values(Quantity_TOC_sRGB))
        if key not in model['role_by_source_colour']:
            raise ValueError(f'Unreviewed source face colour {key}')
        role = model['role_by_source_colour'][key]
        # The reviewed polarized can has the same STEP colour on its shell and
        # top. Only the flat, metallic upper face receives the ink projection.
        if model.get('metal_top_marking'):
            face_box = face.BoundingBox()
            if (role == 'termination' and face.geomType() == 'PLANE'
                    and abs(face_box.zmin - upper[2]) < .001
                    and abs(face_box.zmax - upper[2]) < .001
                    and face.Area() > 1):
                role = 'coating'
                top_marking_faces += 1
        colour_counts[key] += 1
        vertices, triangles = face.tessellate(0.003, 0.08)
        group = groups[role]
        offset = len(group['vertices'])
        group['vertices'].extend(v.toTuple() for v in vertices)
        group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
        group['triangles'].extend(tuple(index + offset for index in t) for t in triangles)
    if model.get('metal_top_marking') and top_marking_faces != 1:
        raise ValueError('Expected exactly one reviewed metallic top marking face')
    expected = set(model.get('required_roles', ['coating', 'ceramic', 'termination']))
    supported = {'coating', 'ceramic', 'termination', 'pin_indicator'}
    if not expected or not expected <= supported or set(groups) != expected:
        raise ValueError(f'Material regions {set(groups)} do not match reviewed roles {expected}')
    return groups, lower, upper, dict(colour_counts)


def scale_display_geometry(groups, lower, upper, factors):
    """Scale display-only mesh about its lower bound; transform normals correctly."""
    import numpy as np
    scale = np.asarray(factors, dtype=float)
    if scale.shape != (3,) or not np.all(np.isfinite(scale)) or np.any(scale <= 0):
        raise ValueError('Display scale must contain three finite positive factors')
    lower = np.asarray(lower, dtype=float)
    upper = np.asarray(upper, dtype=float)
    for group in groups.values():
        vertices = np.asarray(group['vertices'], dtype=float)
        normals = np.asarray(group['normals'], dtype=float) / scale
        lengths = np.linalg.norm(normals, axis=1)
        if np.any(~np.isfinite(lengths)) or np.any(lengths <= 0):
            raise ValueError('Cannot transform invalid mesh normals')
        group['vertices'] = (lower + (vertices - lower) * scale).tolist()
        group['normals'] = (normals / lengths[:, None]).tolist()
    return lower, lower + (upper - lower) * scale


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
        character = marking.get('underline_character')
        if character is not None and (type(character) is not int or not 0 <= character < len(text)
                                      or '\n' in text or marking.get('underline', False)):
            raise ValueError('Character underline requires one valid index on a single line')
        underline = marking.get('underline', False) or character is not None
        if underline and '\n' in text:
            raise ValueError('Underlined marking must be a single line')
        gap = max(3, round(text_height * .10)) if underline else 0
        thickness = max(2, round(text_height * .045)) if underline else 0
        glyph = Image.new('L', (glyph_width, text_height + gap + thickness), 0)
        draw = ImageDraw.Draw(glyph)
        draw.multiline_text((-left, -top), text, fill=255, font=font, align='center')
        if underline:
            if character is None:
                x0, x1 = 0, glyph_width - 1
            else:
                offset = draw.textlength(text[:character], font=font)
                bbox = draw.textbbox((offset, 0), text[character], font=font)
                x0 = max(0, math.floor(bbox[0] - left))
                x1 = min(glyph_width - 1, math.ceil(bbox[2] - left) - 1)
                if x0 > x1:
                    raise ValueError('Character underline has no visible width')
            draw.rectangle((x0, text_height + gap, x1, glyph.height - 1), fill=255)
        rotation = marking.get('rotation_degrees', 0)
        if rotation not in (0, 90) or isinstance(rotation, bool):
            raise ValueError('Marking rotation must be 0 or 90 degrees')
        if rotation == 90:
            # Width follows physical Y, height follows X; compensate for the
            # rectangular bitmap and the different physical dimensions.
            along, across = marking['maximum_width_mm'], marking['maximum_height_mm']
            if along > bounds_mm[1] * .75 or across > bounds_mm[0] * .7:
                raise ValueError('Marking exceeds the reviewed central coating area')
            scale_mm = min(along / glyph.width, across / glyph.height)
            pixel_width = round(glyph.height * scale_mm * width / bounds_mm[0])
            pixel_height = round(glyph.width * scale_mm * height / bounds_mm[1])
            glyph = glyph.transpose(Image.Transpose.ROTATE_90).resize(
                (max(1, pixel_width), max(1, pixel_height)), Image.Resampling.LANCZOS)
        else:
            max_width = width * marking['maximum_width_mm'] / bounds_mm[0]
            max_height = height * marking['maximum_height_mm'] / bounds_mm[1]
            if max_width > width * .7 or max_height > height * .75:
                raise ValueError('Marking exceeds the reviewed central coating area')
            scale = min(max_width / glyph.width, max_height / glyph.height)
            glyph = glyph.resize((round(glyph.width * scale), round(glyph.height * scale)), Image.Resampling.LANCZOS)
        offset = marking.get('offset_x_mm', 0)
        if isinstance(offset, bool) or not isinstance(offset, (int, float)) or not math.isfinite(offset):
            raise ValueError('Marking offset must be a finite number of millimetres')
        x = (width - glyph.width) // 2 + round(offset * width / bounds_mm[0])
        y = (height - glyph.height) // 2
        if x < 0 or x + glyph.width > width or y < 0 or y + glyph.height > height:
            raise ValueError('Marking offset places text outside the package')
        mask.paste(glyph, (x, y))
    mask.save(folder / 'marking.png')
    rng = np.random.default_rng(19)
    noise = np.clip(rng.normal(127, 25, (512, 1024)), 0, 255).astype('uint8')
    Image.fromarray(noise).save(folder / 'grain.png')
    return {'file': font_path.name if font_path else None,
            'sha256': digest(font_path) if font_path else None, 'bitmap_size': [width, height]}


def create_axial_band_texture(marking, lower, upper, folder):
    """Paint illustrative axial bands across the cylinder's X-coordinate UV."""
    from PIL import Image, ImageDraw
    palette = {'black': '#111315', 'brown': '#633627', 'red': '#c32827',
               'orange': '#ed791d', 'yellow': '#e9cc35', 'green': '#2a7c49',
               'blue': '#285ba6', 'violet': '#814889', 'grey': '#596163',
               'white': '#e5e4d9', 'gold': '#b89549', 'silver': '#b5b9bc'}
    bands = marking.get('bands')
    if not isinstance(bands, list) or (len(bands) not in (4, 5) and bands != ['black']) or any(c not in palette for c in bands):
        raise ValueError('Axial markings require one black jumper band or four/five reviewed band colours')
    body = marking.get('body_span_mm')
    if (not isinstance(body, list) or len(body) != 2 or not lower[0] < body[0] < body[1] < upper[0]):
        raise ValueError('Axial body span is not within reviewed model bounds')
    width = marking.get('band_width_mm', .21)
    if isinstance(width, bool) or not isinstance(width, (int, float)) or not 0 < width <= (body[1] - body[0]) * .1:
        raise ValueError('Invalid axial band width')
    image = Image.new('RGB', (2048, 32), '#7ca6ab')
    draw = ImageDraw.Draw(image)
    centres = {1: (.50,), 4: (.18, .33, .48, .78), 5: (.18, .30, .42, .54, .78)}[len(bands)]
    for colour, position in zip(bands, centres):
        centre = body[0] + position * (body[1] - body[0])
        half_width = width / 2
        x0 = round((centre - half_width - lower[0]) * image.width / (upper[0] - lower[0]))
        x1 = round((centre + half_width - lower[0]) * image.width / (upper[0] - lower[0]))
        draw.rectangle((x0, 0, x1, image.height - 1), fill=palette[colour])
    image.save(folder / 'axial_bands.png')


def write_meshes(groups, lower, upper, folder):
    scale = float(max(upper - lower))
    origin = (lower + upper) / 2
    origin[2] = lower[2]
    for role, group in groups.items():
        world = np.asarray(group['vertices'], dtype=float)
        points = (world - origin) / scale
        triangles = np.asarray(group['triangles'], dtype=int)
        radial = group.get('radial_uv')
        if radial:
            triangle_uv = sleeve_triangle_uv(world, triangles, radial['center_xy'],
                radial['bottom_z'], radial['top_z'], radial['seam_angle'])
        else:
            uvs = (world[:, :2] - lower[:2]) / (upper[:2] - lower[:2])
        with (folder / f'{role}.obj').open('w', encoding='ascii') as file:
            for v in points:
                file.write('v ' + ' '.join(f'{x:.8f}' for x in v) + '\n')
            if radial:
                for uv in triangle_uv.reshape(-1, 2):
                    file.write(f'vt {uv[0]:.8f} {uv[1]:.8f}\n')
            else:
                for uv in uvs:
                    file.write(f'vt {uv[0]:.8f} {uv[1]:.8f}\n')
            for normal in group['normals']:
                file.write('vn ' + ' '.join(f'{x:.8f}' for x in normal) + '\n')
            for index, triangle in enumerate(triangles):
                if radial:
                    file.write('f ' + ' '.join(f'{v+1}/{index*3+j+1}/{v+1}' for j, v in enumerate(triangle)) + '\n')
                else:
                    file.write('f ' + ' '.join(f'{v+1}/{v+1}/{v+1}' for v in triangle) + '\n')
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
    backend = os.environ.get('OOMP_RENDER_BACKEND', 'auto')
    if backend not in ('auto', 'scalar'):
        raise ValueError('OOMP_RENDER_BACKEND must be auto or scalar')
    variant = 'llvm_ad_rgb' if backend == 'auto' and dr.has_backend(dr.JitBackend.LLVM) else 'scalar_rgb'
    mi.set_variant(variant)
    T = mi.ScalarTransform4f
    rgb = lambda value: {'type': 'rgb', 'value': value}
    bitmap = lambda name: {'type': 'bitmap', 'filename': str(scratch / name), 'raw': True, 'wrap_mode': 'repeat' if name == 'marking.png' else 'clamp'}
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
    if recipe.get('family') == 'axial_resistor':
        materials['coating'] = {'type': 'roughplastic',
            'diffuse_reflectance': {'type': 'bitmap', 'filename': str(scratch / 'axial_bands.png'),
                                    'raw': False, 'wrap_mode': 'clamp'},
            'alpha': .25, 'int_ior': 1.52}
    if recipe.get('family') == 'cement_power_resistor':
        materials['coating'] = {'type': 'blendbsdf', 'weight': bitmap('marking.png'),
            'body': {'type': 'roughplastic', 'diffuse_reflectance': rgb([.72, .71, .67]),
                     'alpha': .40, 'int_ior': 1.48},
            'ink': {'type': 'roughplastic', 'diffuse_reflectance': rgb([.025, .025, .022]),
                    'alpha': .45, 'int_ior': 1.48}}
    if recipe.get('family') == 'tantalum_capacitor':
        materials['coating'] = {'type': 'blendbsdf', 'weight': bitmap('marking.png'),
            'body': {'type': 'roughplastic', 'diffuse_reflectance': rgb([.72, .45, .055]),
                     'alpha': .30, 'int_ior': 1.48},
            'ink': {'type': 'roughplastic', 'diffuse_reflectance': rgb([.055, .037, .025]),
                    'alpha': .40, 'int_ior': 1.48}}
        materials['pin_indicator'] = {'type': 'roughplastic',
            'diffuse_reflectance': rgb([.53, .14, .055]), 'alpha': .35, 'int_ior': 1.48}
    if recipe.get('family') == 'aluminum_capacitor':
        materials['ceramic'] = {'type': 'roughplastic',
            'diffuse_reflectance': rgb([.018, .019, .021]), 'alpha': .34, 'int_ior': 1.48}
        materials['coating'] = {'type': 'blendbsdf', 'weight': bitmap('marking.png'),
            'body': {'type': 'principled', 'base_color': rgb([.61, .65, .70]),
                     'metallic': 1., 'roughness': .24, 'anisotropic': .22},
            'ink': {'type': 'roughplastic', 'diffuse_reflectance': rgb([.018, .019, .021]),
                    'alpha': .4, 'int_ior': 1.48}}
    if recipe.get('family') == 'radial_aluminum_capacitor':
        black = {'type': 'roughplastic', 'diffuse_reflectance': rgb([.016, .018, .022]),
                 'alpha': .28, 'int_ior': 1.48}
        materials['sleeve_background'] = black
        materials['ceramic'] = black
        materials['pin_indicator'] = {'type': 'roughplastic',
            'diffuse_reflectance': rgb([.56, .57, .55]), 'alpha': .35, 'int_ior': 1.48}
        materials['coating'] = {'type': 'blendbsdf', 'weight': bitmap('marking.png'),
            'body': black, 'ink': {'type': 'roughplastic',
            'diffuse_reflectance': rgb([.78, .79, .76]), 'alpha': .4, 'int_ior': 1.48}}
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


def replace_grooved_top(group, *, center_xy, radius, cutoff_z, disk_z, segments=128):
    """Replace only disconnected, entirely-above-cutoff metal triangles.

    Other metal geometry, including both leads, is preserved. A crossing
    triangle rejects the operation instead of silently cutting an unknown part.
    The resulting group keeps unreferenced original vertices, which do not
    appear in the render and avoid altering preserved triangle indices.
    """
    vertices = np.asarray(group['vertices'], dtype=float)
    normals = np.asarray(group['normals'], dtype=float)
    triangles = np.asarray(group['triangles'], dtype=int)
    center = np.asarray(center_xy, dtype=float)
    if (vertices.ndim != 2 or vertices.shape[1] != 3 or normals.shape != vertices.shape
        or triangles.ndim != 2 or triangles.shape[1] != 3 or triangles.size == 0
        or triangles.min() < 0 or triangles.max() >= len(vertices)
        or center.shape != (2,) or not np.isfinite(vertices).all()
        or not np.isfinite(normals).all() or not np.isfinite(center).all()
        or not np.isfinite([radius, cutoff_z, disk_z]).all()
        or radius <= 0 or disk_z <= cutoff_z or not isinstance(segments, int) or segments < 16):
        raise ValueError('Invalid reviewed flat top geometry')
    z = vertices[triangles, 2]
    below, above = z.min(axis=1), z.max(axis=1)
    if np.any((below < cutoff_z) & (above >= cutoff_z)):
        raise ValueError('A metal triangle crosses the top cutoff')
    removed = below >= cutoff_z
    if not removed.any() or removed.all():
        raise ValueError('Expected separate top and lead geometry')
    top_points = vertices[triangles[removed].ravel()]
    if np.any(np.linalg.norm(top_points[:, :2] - center, axis=1) > radius + 0.002):
        raise ValueError('Metal above cutoff exceeds reviewed top radius')
    angle = np.arange(segments) * (2 * np.pi / segments)
    ring = np.column_stack((center[0] + radius*np.cos(angle),
                            center[1] + radius*np.sin(angle),
                            np.full(segments, disk_z)))
    start = len(vertices)
    vertices = np.vstack((vertices, [[center[0], center[1], disk_z]], ring))
    normals = np.vstack((normals, np.tile([0., 0., 1.], (segments + 1, 1))))
    fan = np.array([(start, start+1+i, start+1+(i+1)%segments)
                    for i in range(segments)], dtype=int)
    return {'vertices': vertices.tolist(), 'normals': normals.tolist(),
            'triangles': np.vstack((triangles[~removed], fan)).tolist()}


def prepare_radial(groups, lower, upper, recipe, studio):
    """Stretch a reviewed sleeve and isolate its cylindrical printing face."""
    params = recipe['model']['radial_stretch']
    if 'flat_top' in recipe['model']:
        groups['termination'] = replace_grooved_top(groups['termination'], **recipe['model']['flat_top'])
    center, radius = params['center_xy'], params['radius']
    start, end, extra = params['lower_z'], params['upper_z'], params['extra_height']
    original = groups['coating']
    selected = straight_sleeve_triangles(original['vertices'], original['triangles'],
        center, radius, start, end, params['tolerance'])
    if not selected.any() or selected.all():
        raise ValueError('Expected distinct straight sleeve and end geometry')
    for group in groups.values():
        vertices, normals = stretch_sleeve(group['vertices'], group['normals'],
            group['triangles'], start, end, extra)
        group['vertices'], group['normals'] = vertices.tolist(), normals.tolist()
    original = groups['coating']
    triangles = np.asarray(original['triangles'], dtype=int)
    groups['sleeve_background'] = {'vertices': original['vertices'],
        'normals': original['normals'], 'triangles': triangles[~selected].tolist()}
    original['triangles'] = triangles[selected].tolist()
    direction = studio['camera_direction']
    original['radial_uv'] = {'center_xy': center, 'bottom_z': start,
        'top_z': end + extra, 'seam_angle': math.atan2(direction[1], direction[0]) - math.pi}
    return groups, np.asarray(lower, dtype=float), np.asarray(upper, dtype=float) + [0, 0, extra]


def create_radial_textures(marking, text, params, folder):
    """Fit illustrative text in physical units onto the curved sleeve mask."""
    from PIL import Image, ImageDraw, ImageFont
    width, height = 2048, 1024
    font_path = find_font(marking['font_file'])
    font = ImageFont.truetype(str(font_path), 350)
    probe = Image.new('L', (1, 1), 0)
    box = ImageDraw.Draw(probe).multiline_textbbox((0, 0), text, font=font, align='center')
    glyph = Image.new('L', (math.ceil(box[2] - box[0]), math.ceil(box[3] - box[1])), 0)
    if not text or glyph.width <= 0 or glyph.height <= 0:
        raise ValueError('Radial marking has no visible glyphs')
    ImageDraw.Draw(glyph).multiline_text((-box[0], -box[1]), text, fill=255, font=font, align='center')
    circumference = 2 * math.pi * params['radius']
    sleeve_height = params['upper_z'] - params['lower_z'] + params['extra_height']
    max_w, max_h = marking['maximum_width_mm'], marking['maximum_height_mm']
    if max_w <= 0 or max_h <= 0 or max_w > circumference * .4 or max_h > sleeve_height * .7:
        raise ValueError('Radial marking exceeds reviewed sleeve area')
    physical_scale = min(max_w / glyph.width, max_h / glyph.height)
    glyph = glyph.resize((max(1, round(glyph.width * physical_scale / circumference * width)),
                          max(1, round(glyph.height * physical_scale / sleeve_height * height))),
                         Image.Resampling.LANCZOS)
    mask = Image.new('L', (width, height), 0)
    mask.paste(glyph, ((width - glyph.width) // 2, (height - glyph.height) // 2))
    mask.save(folder / 'marking.png')
    rng = np.random.default_rng(19)
    noise = np.clip(rng.normal(127, 25, (512, 1024)), 0, 255).astype('uint8')
    Image.fromarray(noise).save(folder / 'grain.png')
    return {'file': font_path.name, 'sha256': digest(font_path), 'bitmap_size': [width, height]}


def generate(part_id, *, model_root=None, output=None, pixels=None, samples=None, check=False, force=False):
    from PIL import Image
    recipes = json.loads(RECIPES.read_text(encoding='utf-8'))
    if part_id not in recipes:
        raise ValueError('No reviewed display recipe for this exact component. Add evidence before rendering.')
    recipe = recipes[part_id]
    if recipe.get('family') != 'radial_aluminum_capacitor':
        raise ValueError('This experimental renderer only accepts reviewed radial capacitors')
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
    axial = recipe.get('family') == 'axial_resistor'
    inputs = {'recipe': recipe, 'studio': studio, 'pixels': pixels, 'samples': samples,
              'renderer_sha256': digest(__file__), 'marking_code_sha256': digest(Path(__file__).with_name('package_markings.py')),
              'font_sha256': digest(find_font(recipe['marking']['font_file'])) if text and not axial else None,
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
    source_bounds = (upper - lower).tolist()
    groups, lower, upper = prepare_radial(groups, lower, upper, recipe, studio)
    if 'display_scale_xyz' in recipe['model']:
        lower, upper = scale_display_geometry(groups, lower, upper, recipe['model']['display_scale_xyz'])
    print(f'{part_id}: {text!r}; bounds {(upper-lower).tolist()} mm; {sum(len(g["triangles"]) for g in groups.values())} triangles', flush=True)
    if check:
        return
    destination.mkdir(parents=True, exist_ok=True)
    # Temporary directory owns all intermediate geometry. No STL, STEP, GLB or
    # Blender scene is written into the catalogue by this pipeline.
    with tempfile.TemporaryDirectory(prefix='oomp-display-') as temporary:
        scratch = Path(temporary)
        font = create_radial_textures(recipe['marking'], text, recipe['model']['radial_stretch'], scratch)
        if axial:
            create_axial_band_texture(recipe['marking'], lower, upper, scratch)
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
    manifest['model']['source_bounds_mm'] = source_bounds
    manifest['model']['radial_stretch'] = recipe['model']['radial_stretch']
    if 'display_scale_xyz' in recipe['model']:
        manifest['model']['source_bounds_mm'] = source_bounds
        manifest['model']['display_scale_xyz'] = recipe['model']['display_scale_xyz']
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
