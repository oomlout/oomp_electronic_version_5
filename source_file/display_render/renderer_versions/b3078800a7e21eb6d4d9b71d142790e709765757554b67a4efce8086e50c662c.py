"""Reuse two path-traced resistor material passes for display-only markings.

This is an explicitly labelled approximation: ink is composited in linear light
onto shared studio renders, so the effect of ink on indirect reflections is not
recomputed. It is restricted to the reviewed resistor geometries and studio.
No CAD or mesh export is retained. Run ``--help`` for the two explicit stages.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import time
from importlib.metadata import version

from kicad_agents import display_render as renderer
from kicad_agents.package_markings import marking_text

ROOT = renderer.ROOT
MASTER_ROOT = ROOT / 'source_file/display_render/masters'
MODEL_SHA256 = '1875571c326d0d9e96f36b4efeb8094068ef7619f0a449c781caf0b49c2e5861'
MODELS = {
    '0603_imperial_1608_metric': ('electronic_resistor_0603_10000_ohm', MODEL_SHA256, .76, .32),
    '0603_imperial': ('electronic_resistor_0603_10000_ohm', MODEL_SHA256, .76, .32),
    '0805_imperial': ('electronic_resistor_0805_1000_ohm', 'ded342cdb394fb45395227beaaa75cc390613cf2581b29cd6d22c12abd6103b2', .95, .48),
    '1206_imperial': ('electronic_resistor_1206_1000_ohm', 'f5d1ea5c47935091292bd1c6c698e0df88d3d4bbf92bf66b4c97e49df5be9ebc', 1.52, .64),
    '4x0402_convex_8_pin': ('electronic_resistor_array_4_x_0402_convex_3300_ohm_8_pin',
                            '36ded1f7b7c9e9dcddde3eb3200acdf1c0e0b60046893660e6f043afc2ec7fad', 1.1, .32),
}
MINIMUM_FREE_BYTES = 512 * 1024 * 1024


def require_disk_space():
    if shutil.disk_usage(ROOT).free < MINIMUM_FREE_BYTES:
        raise OSError('Less than 512 MiB is free on the repository drive; stop the render batch')


def json_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def runtime_versions():
    return {name: version(name) for name in ('cadquery', 'cadquery-ocp', 'mitsuba',
            'drjit', 'numpy', 'Pillow', 'opencv-python-headless')}


def read_recipe(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf-8'))
    if part_id not in recipes:
        raise ValueError('No reviewed recipe for this exact component')
    recipe = recipes[part_id]
    model = recipe['model']
    spec = MODELS.get(recipe.get('package'))
    if not spec:
        raise ValueError('Shared passes are reviewed only for selected resistor packages')
    pilot, expected_hash, max_width, max_height = spec
    is_array = recipe.get('package') == '4x0402_convex_8_pin'
    if (recipe['family'] != ('chip_resistor_array' if is_array else 'chip_resistor')
        or recipe['marking'].get('rotation_degrees', 0) != (90 if is_array else 0)
        or model['sha256'] != expected_hash
        or model != recipes[pilot]['model']
        or recipe.get('disable_bump_for')
        or recipe['marking'].get('maximum_width_mm', 0) > max_width
        or recipe['marking'].get('maximum_height_mm', 0) > max_height
        or recipe['marking'].get('maximum_width_mm', 0) <= 0
        or recipe['marking'].get('maximum_height_mm', 0) <= 0
        or recipe['output']['pixels'] != 1400 or recipe['output']['samples'] != 256):
        raise ValueError('Shared passes are reviewed only for selected resistor packages')
    return recipe


def master_inputs(recipe, studio):
    return {'schema_version': 1, 'model': recipe['model'], 'family': recipe['family'],
            'disable_bump_for': recipe.get('disable_bump_for', []), 'studio': studio,
            'pixels': 1400, 'samples': 256, 'renderer_sha256': renderer.digest(renderer.__file__),
            'builder_sha256': renderer.digest(__file__),
            'runtime': runtime_versions()}


def check_files(folder, artifacts, expected_names):
    if set(artifacts) != set(expected_names):
        return False
    return all((folder / name).is_file() and (folder / name).stat().st_size == info['bytes']
               and renderer.digest(folder / name) == info['sha256'] for name, info in artifacts.items())


def make_master(part_id):
    from PIL import Image
    require_disk_space()
    recipe = read_recipe(part_id)
    studio = json.loads(renderer.STUDIO.read_text(encoding='utf-8'))
    model = renderer.locate_model(recipe['model']['relative_path'])
    if renderer.digest(model) != recipe['model']['sha256']:
        raise ValueError('KiCad model hash changed; review before rendering')
    inputs = master_inputs(recipe, studio)
    folder = MASTER_ROOT / json_hash(inputs)
    manifest_file = folder / 'manifest.json'
    if manifest_file.is_file():
        manifest = json.loads(manifest_file.read_text(encoding='utf-8'))
        if manifest.get('inputs') == inputs and check_files(folder, manifest.get('artifacts', {}),
                                                             {'body.png', 'ink.png'}):
            print('Reused verified shared material passes:', folder, flush=True)
            return folder
        raise ValueError('Existing master is damaged or inconsistent; do not overwrite it silently')
    groups, lower, upper, colour_counts = renderer.load_coloured_step(model, recipe['model'])
    MASTER_ROOT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='oomp-master-', dir=MASTER_ROOT) as temp:
        scratch = Path(temp)
        renderer.create_textures({}, '', upper - lower, scratch)
        render_details = {}
        for name, weight in [('body.png', 0), ('ink.png', 255)]:
            Image.new('L', (1024, 512), weight).save(scratch / 'marking.png')
            pixels, settings = renderer.render_scene(groups, lower, upper, recipe, studio,
                                                       scratch, 1400, 256)
            Image.fromarray(pixels).save(scratch / name, optimize=True)
            render_details[name] = settings
            print('Rendered shared pass', name, settings['seconds'], 'seconds', flush=True)
        if (renderer.digest(__file__) != inputs['builder_sha256']
            or renderer.digest(renderer.__file__) != inputs['renderer_sha256']):
            raise RuntimeError('Render source changed while the shared passes were being generated')
        artifacts = {name: {'sha256': renderer.digest(scratch / name),
                            'bytes': (scratch / name).stat().st_size} for name in ('body.png', 'ink.png')}
        manifest = {'inputs': inputs, 'lower_mm': lower.tolist(), 'upper_mm': upper.tolist(),
                    'model': {'relative_path': recipe['model']['relative_path'], 'sha256': renderer.digest(model),
                              'actual_bounds_mm': (upper-lower).tolist(), 'source_face_colours': colour_counts,
                              'triangle_count': sum(len(group['triangles']) for group in groups.values()),
                              'source_header': model.read_text(encoding='utf-8').split('FILE_DESCRIPTION')[0]},
                    'render': render_details, 'artifacts': artifacts}
        (scratch / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
        folder.mkdir()
        for name in ('body.png', 'ink.png', 'manifest.json'):
            (scratch / name).replace(folder / name)
    print('Saved shared material passes:', folder, flush=True)
    return folder


def project_mask(mask, lower, upper, studio, pixels):
    """Project the planar top UV mask through the reviewed orthographic camera."""
    import cv2
    import mitsuba as mi
    import drjit as dr
    import numpy as np
    mi.set_variant('llvm_ad_rgb' if dr.has_backend(dr.JitBackend.LLVM) else 'scalar_rgb')
    transform_type = mi.ScalarTransform4f
    extent = (upper-lower) / max(upper-lower)
    height = float(extent[2])
    target = np.array([0., 0., height * .48])
    direction = np.array(studio['camera_direction'], dtype=float)
    direction /= np.linalg.norm(direction)
    transform = transform_type().look_at(origin=target + direction * 5, target=target, up=[0, 0, 1])
    basis = np.asarray(transform.matrix)[:3, :3]
    bounds = np.array([[x, y, z] for x in [-extent[0]/2, extent[0]/2]
                       for y in [-extent[1]/2, extent[1]/2] for z in [0, height]])
    half = float(np.ptp(bounds @ basis, axis=0)[:2].max() / (2 * (1 - 2 * studio['framing_margin'])))
    world = np.array([[-extent[0]/2, -extent[1]/2, height, 1],
                      [extent[0]/2, -extent[1]/2, height, 1],
                      [extent[0]/2, extent[1]/2, height, 1],
                      [-extent[0]/2, extent[1]/2, height, 1]])
    camera = (np.linalg.inv(np.asarray(transform.matrix)) @ world.T).T
    dest = np.column_stack(((1-camera[:, 0]/half)*pixels/2-.5,
                            (1-camera[:, 1]/half)*pixels/2-.5)).astype('float32')
    h, w = mask.shape
    source = np.array([[0, h-1], [w-1, h-1], [w-1, 0], [0, 0]], dtype='float32')
    matrix = cv2.getPerspectiveTransform(source, dest)
    alpha = cv2.warpPerspective(mask, matrix, (pixels, pixels), flags=cv2.INTER_LINEAR).astype('float32') / 255
    return cv2.GaussianBlur(alpha, (0, 0), .5)


def inverse_tone(srgb):
    import numpy as np
    y = np.where(srgb <= .04045, srgb/12.92, ((srgb+.055)/1.055)**2.4)
    a, b, c = 2.51-2.43*y, .03-.59*y, -.14*y
    return (-b + np.sqrt(np.maximum(0, b*b-4*a*c))) / (2*a)


def forward_tone(linear):
    import numpy as np
    y = np.clip(linear*(2.51*linear+.03)/(linear*(2.43*linear+.59)+.14), 0, 1)
    return np.where(y <= .0031308, 12.92*y, 1.055*y**(1/2.4)-.055)


def composite(body, ink, alpha):
    import numpy as np
    a = alpha[..., None]
    return np.rint(np.clip(forward_tone(inverse_tone(body/255.)*(1-a)
                                      + inverse_tone(ink/255.)*a), 0, 1)*255).astype('uint8')


def render(part_id, output=None):
    import numpy as np
    from PIL import Image
    started = time.perf_counter()
    require_disk_space()
    compositor_hash = renderer.digest(__file__)
    recipe = read_recipe(part_id)
    studio = json.loads(renderer.STUDIO.read_text(encoding='utf-8'))
    model = renderer.locate_model(recipe['model']['relative_path'])
    if renderer.digest(model) != recipe['model']['sha256']:
        raise ValueError('KiCad model hash changed; review before rendering')
    evidence = recipe['marking']['evidence']
    evidence_path = (ROOT / evidence['file']).resolve()
    if (not evidence_path.is_relative_to(ROOT.resolve()) or not evidence_path.is_file()
        or renderer.digest(evidence_path) != evidence['sha256']):
        raise ValueError('Marking evidence is missing or changed')
    text = marking_text(recipe['marking'])
    if not text:
        raise ValueError('This shared-marking path expects an evidenced, nonempty marking')
    inputs = master_inputs(recipe, studio)
    master = MASTER_ROOT / json_hash(inputs)
    master_file = master / 'manifest.json'
    if not master_file.is_file():
        raise FileNotFoundError('No current shared passes: run make-master first')
    master_data = json.loads(master_file.read_text(encoding='utf-8'))
    if master_data.get('inputs') != inputs or not check_files(master, master_data.get('artifacts', {}),
                                                              {'body.png', 'ink.png'}):
        raise ValueError('Shared passes are stale or damaged')
    destination = Path(output) if output else ROOT / 'parts' / part_id / 'data/display_render'
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise FileExistsError('Existing output is preserved; select an empty scratch output or an unrendered part')
    lower, upper = np.array(master_data['lower_mm']), np.array(master_data['upper_mm'])
    with tempfile.TemporaryDirectory(prefix='oomp-marking-') as folder:
        scratch = Path(folder)
        font = renderer.create_textures(recipe['marking'], text, upper-lower, scratch)
        with Image.open(scratch / 'marking.png') as mask:
            alpha = project_mask(np.asarray(mask.convert('L')), lower, upper, studio, 1400)
        with Image.open(master/'body.png') as image:
            body = np.asarray(image.convert('RGB'), dtype='float32')
        with Image.open(master/'ink.png') as image:
            ink = np.asarray(image.convert('RGB'), dtype='float32')
        picture = Image.fromarray(composite(body, ink, alpha))
        destination.mkdir(parents=True, exist_ok=True)
        picture.save(destination/'render.png', optimize=True)
        picture.thumbnail((recipe['output']['thumbnail_pixels'], recipe['output']['thumbnail_pixels']), Image.Resampling.LANCZOS)
        picture.save(destination/'preview.webp', quality=90, method=6)
    if renderer.digest(__file__) != compositor_hash or renderer.digest(renderer.__file__) != inputs['renderer_sha256']:
        raise RuntimeError('Render source changed during composition; do not publish this output')
    fingerprint = json_hash({'recipe': recipe, 'master_manifest_sha256': renderer.digest(master_file),
                             'compositor_sha256': compositor_hash, 'font_sha256': font['sha256'],
                             'runtime': runtime_versions()})
    manifest = {'schema_version': 1, 'part_id': part_id, 'purpose': 'display_only',
        'input_fingerprint': fingerprint,
        'recipe': recipe, 'recipe_sha256': json_hash(recipe), 'studio': studio,
        'runtime': runtime_versions(), 'model': master_data['model'],
        'marking': {'text': text, 'font': font, 'evidence_sha256': renderer.digest(evidence_path)},
        'renderer_source_sha256': inputs['renderer_sha256'],
        'composite': {'method': 'linear-light blend of shared path-traced body and ink passes',
            'limitation': 'Approximate indirect reflections; marking not independently path traced.',
            'compositor_source_sha256': compositor_hash,
            'master_manifest': master_file.relative_to(ROOT).as_posix(),
            'master_manifest_sha256': renderer.digest(master_file)},
        'render': {'pixels': 1400, 'samples_per_master': 256, 'seconds': round(time.perf_counter()-started, 2)},
        'artifacts': {name: {'sha256': renderer.digest(destination/name), 'bytes': (destination/name).stat().st_size}
                      for name in ('render.png', 'preview.webp')}}
    (destination/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    print('Composited', part_id, 'in', manifest['render']['seconds'], 'seconds:', destination, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    master = sub.add_parser('make-master')
    master.add_argument('part_id')
    selected = sub.add_parser('render')
    selected.add_argument('part_id')
    selected.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.command == 'make-master':
        make_master(args.part_id)
    else:
        render(args.part_id, args.output)


if __name__ == '__main__':
    main()
