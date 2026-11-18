"""Reuse reviewed black/white path-traced passes for axial colour bands.

The visible stripe masks are derived from the two calibration images.
Band colours are interpolated in linear light; indirect reflections and colour
interactions are approximate and are disclosed in every output manifest.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

from kicad_agents import display_render as renderer
from kicad_agents.display_render_composite import forward_tone, inverse_tone, json_hash, require_disk_space, runtime_versions
from working_oomp_populate_display_render import renderer_source_available

ROOT = renderer.ROOT
MASTERS = ROOT / 'source_file/display_render/masters'
MODEL_HASH = '46710ac36957e4073ef7e80153823ef7db1ea12932074cb71f43bc4b476a74dc'
PALETTE = {'black': '111315', 'brown': '633627', 'red': 'c32827', 'orange': 'ed791d',
           'yellow': 'e9cc35', 'green': '2a7c49', 'blue': '285ba6', 'violet': '814889',
           'grey': '596163', 'white': 'e5e4d9', 'gold': 'b89549', 'silver': 'b5b9bc'}


def recipe_for(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf-8'))
    recipe = recipes[part_id]
    marking = recipe['marking']
    if (recipe.get('family') != 'axial_resistor' or recipe.get('package') != 'din0207_horizontal_7_62mm'
        or recipe['model'].get('sha256') != MODEL_HASH or marking.get('body_span_mm') != [.66, 6.96]
        or not isinstance(marking.get('bands'), list) or len(marking['bands']) not in (4, 5)
        or marking.get('band_width_mm', .21) != .21
        or any(band not in PALETTE for band in marking['bands'])
        or marking.get('text') != ' / '.join(marking['bands'])
        or recipe.get('disable_bump_for') or recipe.get('output', {}).get('pixels') != 1400
        or recipe['output'].get('samples') != 256):
        raise ValueError('Axial recipe is outside the reviewed material and geometry setup')
    return recipe


def _hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _check_files(folder, artifacts, names):
    return set(artifacts) == set(names) and all(
        (folder/name).is_file() and (folder/name).stat().st_size == item['bytes']
        and _hash(folder/name) == item['sha256'] for name, item in artifacts.items())


def prepare_master(calibration, part_id):
    """Import two independently rendered calibration passes after inspection."""
    require_disk_space()
    calibration = Path(calibration)
    recipe = recipe_for(part_id)
    studio = json.loads(renderer.STUDIO.read_text(encoding='utf-8'))
    references = {}
    for name in ('black', 'white'):
        folder = calibration / name
        m = json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
        base = m.get('recipe', {})
        mark = base.get('marking', {})
        if (m.get('part_id') != part_id or m.get('purpose') != 'display_only'
            or m.get('studio') != studio or m.get('model', {}).get('sha256') != MODEL_HASH
            or m.get('render', {}).get('pixels') != 1400 or m.get('render', {}).get('samples') != 256
            or m.get('render', {}).get('nonfinite_pixels_repaired') != 0
            or not renderer_source_available(m.get('renderer_source_sha256'))
            or mark.get('bands') != [name] * len(recipe['marking']['bands'])
            or mark.get('text') != ' / '.join([name] * len(recipe['marking']['bands']))
            or not _check_files(folder, m.get('artifacts', {}), {'render.png', 'preview.webp'})):
            raise ValueError(f'Unverified {name} calibration pass')
        normalized = json.loads(json.dumps(base))
        normalized['marking']['bands'] = recipe['marking']['bands']
        normalized['marking']['text'] = recipe['marking']['text']
        if normalized != recipe:
            raise ValueError('Calibration recipe differs in an image-affecting input')
        references[name] = m
    if (references['black']['renderer_source_sha256'] != references['white']['renderer_source_sha256']
        or references['black']['runtime'] != references['white']['runtime']):
        raise ValueError('Calibration passes use different renderer or runtime')
    inputs = {'schema_version': 1, 'model': recipe['model'], 'family': recipe['family'],
              'disable_bump_for': recipe.get('disable_bump_for', []), 'studio': studio,
              'pixels': 1400, 'samples': 256, 'renderer_sha256': references['black']['renderer_source_sha256'],
              'builder_sha256': _hash(Path(__file__)), 'runtime': references['black']['runtime'],
              'reference_manifest_sha256': {name: _hash(calibration/name/'manifest.json') for name in references}}
    folder = MASTERS / json_hash(inputs)
    if folder.exists():
        raise FileExistsError('Existing master is preserved; inspect it before reuse')
    folder.mkdir(parents=True)
    for name, target in [('black', 'body.png'), ('white', 'ink.png')]:
        shutil.copyfile(calibration/name/'render.png', folder/target)
    artifacts = {name: {'sha256': _hash(folder/name), 'bytes': (folder/name).stat().st_size}
                 for name in ('body.png', 'ink.png')}
    master = {'inputs': inputs, 'model': references['black']['model'], 'artifacts': artifacts,
              'method': f'black and white synthetic {len(recipe["marking"]["bands"])}-band calibration renders',
              'reference_manifests': references}
    (folder/'manifest.json').write_text(json.dumps(master, indent=2) + '\n', encoding='utf-8')
    print('Saved verified axial material passes:', folder)
    return folder


def band_masks(black, white, expected_count=5):
    import cv2
    import numpy as np
    difference = np.mean(np.abs(white.astype('float32') - black.astype('float32')), axis=2)
    count, labels, stats, centroids = cv2.connectedComponentsWithStats((difference > 10).astype('uint8'), 8)
    selected = sorted(range(1, count), key=lambda i: stats[i, 4], reverse=True)[:expected_count]
    if len(selected) != expected_count or any(stats[i, 4] < 4000 for i in selected):
        raise ValueError('Calibration did not produce the expected substantial band regions')
    selected.sort(key=lambda i: centroids[i, 0])
    if any(centroids[b, 0] - centroids[a, 0] < 30 for a, b in zip(selected, selected[1:])):
        raise ValueError('Band regions are not separated in the reviewed view')
    masks = [cv2.dilate((labels == i).astype('uint8'), np.ones((3, 3), np.uint8), iterations=2).astype(bool)
             for i in selected]
    if np.any(np.sum(np.stack(masks), axis=0) > 1):
        raise ValueError('Dilated band regions overlap')
    return masks


def compose(black, white, colours):
    import numpy as np
    def linear(hex_colour):
        values = np.array([int(hex_colour[i:i+2], 16)/255 for i in (0, 2, 4)], dtype='float32')
        return np.where(values <= .04045, values/12.92, ((values+.055)/1.055)**2.4)
    masks = band_masks(black, white, len(colours))
    lo, hi = linear(PALETTE['black']), linear(PALETTE['white'])
    a, b = inverse_tone(black.astype('float32')/255), inverse_tone(white.astype('float32')/255)
    output = a.copy()
    for mask, colour in zip(masks, colours):
        weight = np.clip((linear(PALETTE[colour]) - lo) / (hi - lo), 0, 1)
        output[mask] = a[mask] + (b[mask] - a[mask]) * weight
    return np.rint(np.clip(forward_tone(output), 0, 1)*255).astype('uint8')


def render(part_id, master, output=None):
    from PIL import Image
    import numpy as np
    require_disk_space()
    recipe = recipe_for(part_id)
    studio = json.loads(renderer.STUDIO.read_text(encoding='utf-8'))
    master_file = (Path(master) / 'manifest.json').resolve()
    master_data = json.loads(master_file.read_text(encoding='utf-8'))
    inputs = master_data['inputs']
    calibrated_bands = master_data.get('reference_manifests', {}).get('black', {}).get('recipe', {}).get('marking', {}).get('bands', [])
    if (not master_file.resolve().is_relative_to(MASTERS.resolve()) or inputs['model'] != recipe['model']
        or inputs['family'] != recipe['family'] or inputs['studio'] != studio
        or calibrated_bands != ['black'] * len(recipe['marking']['bands'])
        or inputs['builder_sha256'] != _hash(Path(__file__)) or inputs['pixels'] != 1400 or inputs['samples'] != 256
        or not renderer_source_available(inputs['renderer_sha256'])
        or not _check_files(master_file.parent, master_data['artifacts'], {'body.png', 'ink.png'})):
        raise ValueError('Master passes are stale, unreviewed or damaged')
    evidence = recipe['marking']['evidence']
    ev = (ROOT / evidence['file']).resolve()
    if not ev.is_relative_to(ROOT.resolve()) or not ev.is_file() or _hash(ev) != evidence['sha256']:
        raise ValueError('Marking evidence is missing or changed')
    dest = Path(output) if output else ROOT / 'parts' / part_id / 'data/display_render'
    if dest.exists() and (not dest.is_dir() or any(dest.iterdir())):
        raise FileExistsError('Existing output is preserved')
    with Image.open(master_file.parent/'body.png') as source:
        black = np.asarray(source.convert('RGB'))
    with Image.open(master_file.parent/'ink.png') as source:
        white = np.asarray(source.convert('RGB'))
    picture = Image.fromarray(compose(black, white, recipe['marking']['bands']))
    dest.mkdir(parents=True, exist_ok=True)
    picture.save(dest/'render.png', optimize=True)
    picture.thumbnail((recipe['output']['thumbnail_pixels'],)*2, Image.Resampling.LANCZOS)
    picture.save(dest/'preview.webp', quality=90, method=6)
    details = {'method': 'linear-light interpolation of shared axial band material passes',
               'limitation': 'Approximate indirect reflections and colour interactions; bands not independently path traced.',
               'compositor_source_sha256': _hash(Path(__file__)),
               'master_manifest': master_file.relative_to(ROOT).as_posix(),
               'master_manifest_sha256': _hash(master_file)}
    composition_runtime = runtime_versions()
    manifest = {'schema_version': 1, 'part_id': part_id, 'purpose': 'display_only',
        'input_fingerprint': json_hash({'recipe': recipe, 'master': details['master_manifest_sha256'],
                                        'compositor': details['compositor_source_sha256'], 'runtime': composition_runtime}),
        'recipe': recipe, 'recipe_sha256': json_hash(recipe), 'studio': studio,
        'runtime': composition_runtime, 'model': master_data['model'],
        'marking': {'text': recipe['marking']['text'], 'font': {'file': None, 'sha256': None},
                    'evidence_sha256': _hash(ev)},
        'renderer_source_sha256': inputs['renderer_sha256'], 'composite': details,
        'render': {'pixels': 1400, 'samples_per_master': 256},
        'artifacts': {name: {'sha256': _hash(dest/name), 'bytes': (dest/name).stat().st_size}
                      for name in ('render.png', 'preview.webp')}}
    (dest/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    print('Composited', part_id, 'to', dest, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    master = sub.add_parser('prepare-master')
    master.add_argument('part_id')
    master.add_argument('calibration', type=Path)
    output = sub.add_parser('render')
    output.add_argument('part_id')
    output.add_argument('master', type=Path)
    output.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.command == 'prepare-master':
        prepare_master(args.calibration, args.part_id)
    else:
        render(args.part_id, args.master, args.output)


if __name__ == '__main__':
    main()
