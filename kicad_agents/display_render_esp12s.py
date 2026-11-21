"""Adapt a reviewed KiCad ESP-12E display model to an ESP-12S illustration.

Six extra ESP-12E end contacts are recoloured as substrate; notch contours,
antenna and components remain approximate. The one flat
shield top alone receives illustrative family text; no logos or approval
marks are inferred. Source hashes and face counts bind geometry assignment.
"""
import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import time
from kicad_agents import display_render as renderer

write_meshes = renderer.write_meshes
repair_nonfinite_pixels = renderer.repair_nonfinite_pixels
MODELS = {'984f7bce88206d1f9efd21f272d5cc12f0cb9556f6b2b29385b0d2f2f2011079': {'0.160,0.160,0.160':74, '0.508,0.508,0.508':18, '0.859,0.738,0.496':384, '0.895,0.891,0.813':8, '0.340,0.680,0.445':4}}

def load(path, specification):
    import cadquery as cq
    import numpy as np
    from OCP.STEPCAFControl import STEPCAFControl_Reader
    from OCP.TDocStd import TDocStd_Document
    from OCP.TCollection import TCollection_ExtendedString
    from OCP.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_ColorType
    from OCP.TDF import TDF_LabelSequence
    from OCP.Quantity import Quantity_Color, Quantity_TOC_sRGB
    from OCP.IFSelect import IFSelect_RetDone
    digest = renderer.digest(path)
    if digest not in MODELS or specification.get('sha256') != digest:
        raise ValueError('Unreviewed WROOM model')
    doc = TDocStd_Document(TCollection_ExtendedString('wroom-display'))
    reader = STEPCAFControl_Reader()
    reader.SetColorMode(True)
    if reader.ReadFile(str(path)) != IFSelect_RetDone or not reader.Transfer(doc):
        raise ValueError('Cannot read WROOM STEP')
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    colours = XCAFDoc_DocumentTool.ColorTool_s(doc.Main())
    labels = TDF_LabelSequence()
    shapes.GetFreeShapes(labels)
    if labels.Length() != 1:
        raise ValueError('Unexpected WROOM assembly root count')
    shape = cq.Shape.cast(shapes.GetShape_s(labels.Value(1)))
    if not shape.isValid():
        raise ValueError('Invalid WROOM model')
    box = shape.BoundingBox()
    lower = np.array([box.xmin,box.ymin,box.zmin])
    upper = np.array([box.xmax,box.ymax,box.zmax])
    if not np.allclose(upper-lower, [16.,24.,3.2], atol=.005, rtol=0):
        raise ValueError('Unexpected WROOM dimensions')
    groups = defaultdict(lambda: dict(vertices=[], normals=[], triangles=[]))
    counts = defaultdict(int)
    tops = 0
    hidden_end_faces = 0
    for face in shape.Faces():
        colour = Quantity_Color()
        found = colours.GetColor(face.wrapped, XCAFDoc_ColorType.XCAFDoc_ColorSurf, colour)
        key = ','.join(f'{v:.3f}' for v in colour.Values(Quantity_TOC_sRGB)) if found else 'none'
        if key not in MODELS[digest]:
            raise ValueError(f'Unreviewed WROOM colour: {key}')
        role = {'0.160,0.160,0.160':'ceramic', '0.859,0.738,0.496':'termination', '0.508,0.508,0.508':'pin_indicator', '0.895,0.891,0.813':'ceramic', '0.340,0.680,0.445':'ceramic'}[key]
        face_box = face.BoundingBox()
        # ESP-12E has six additional end contacts; the ESP-12S has only
        # two rows of eight. Recolour the end-contact faces as PCB. This
        # preserves the E model's notch contours as a documented approximation.
        if role == 'termination' and face_box.ymax <= -10.8 and face_box.xmin >= -6.01 and face_box.xmax <= 6.01:
            role = 'ceramic'
            hidden_end_faces += 1
        if role == 'pin_indicator' and face.geomType() == 'PLANE' and abs(face_box.zmin-upper[2]) < .001 and abs(face_box.zmax-upper[2]) < .001 and face.Area() > 100:
            role = 'coating'
            tops += 1
        counts[key] += 1
        vertices, triangles = face.tessellate(.003,.08)
        group = groups[role]
        offset = len(group['vertices'])
        group['vertices'].extend(v.toTuple() for v in vertices)
        group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
        group['triangles'].extend(tuple(offset+i for i in t) for t in triangles)
    if dict(counts) != MODELS[digest] or tops != 1 or hidden_end_faces != 84 or set(groups) != {'ceramic','termination','pin_indicator','coating'}:
        raise ValueError(f'Unexpected WROOM face regions: {dict(counts)}, shield tops {tops}, groups {set(groups)}')
    return dict(groups), lower, upper, dict(counts, suppressed_end_contact_faces=hidden_end_faces)

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
    # Module-specific surfaces: dark laminate, gold pads, brushed metal shield,
    # and black illustrative text on the shield top only.
    materials['ceramic'] = {'type': 'roughplastic', 'diffuse_reflectance': rgb([.012, .025, .023]), 'alpha': .28, 'int_ior': 1.5}
    materials['termination'] = {'type': 'principled', 'base_color': rgb([.69, .49, .18]), 'metallic': 1., 'roughness': .29}
    materials['pin_indicator'] = {'type': 'principled', 'base_color': rgb([.53, .56, .58]), 'metallic': 1., 'roughness': .30, 'anisotropic': .25}
    materials['coating'] = {'type': 'blendbsdf', 'weight': bitmap('marking.png'),
        'body': {'type': 'principled', 'base_color': rgb([.53, .56, .58]), 'metallic': 1., 'roughness': .30, 'anisotropic': .25},
        'ink': {'type': 'roughplastic', 'diffuse_reflectance': rgb([.025, .027, .028]), 'alpha': .35, 'int_ior': 1.48}}
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part')
    parser.add_argument('--output',required=True)
    parser.add_argument('--pixels',type=int)
    parser.add_argument('--samples',type=int)
    args=parser.parse_args()
    adapter_hash=renderer.digest(__file__)
    renderer.load_coloured_step=load
    renderer.render_scene=render_scene
    renderer.generate(args.part,output=args.output,pixels=args.pixels,samples=args.samples,force=True)
    if renderer.digest(__file__) != adapter_hash:
        raise RuntimeError('Adapter changed during render')
    path=Path(args.output)/'manifest.json'
    manifest=json.loads(path.read_text(encoding='utf8'))
    manifest['model']['adapter_sha256']=adapter_hash
    manifest['input_fingerprint']=hashlib.sha256((manifest['input_fingerprint']+adapter_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf8')

if __name__ == '__main__':
    main()
