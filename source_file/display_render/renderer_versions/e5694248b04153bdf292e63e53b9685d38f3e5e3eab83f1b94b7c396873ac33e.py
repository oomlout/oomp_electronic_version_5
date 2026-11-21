"""Reuse the verified unlit 0201 pilot for equivalent generic display records."""
import argparse
import copy
import hashlib
import json
import shutil
from pathlib import Path

from kicad_agents import display_render as renderer
from kicad_agents import display_render_generic_0201_led_family_queue as batch


def json_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=batch.PARTS)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = Path(args.output)
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise FileExistsError('Existing output preserved')
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    expected = batch.prepare(recipes)
    if recipes.get(args.part) != expected[args.part]:
        raise ValueError('Candidate recipe changed')
    recipe, pilot_recipe = recipes[args.part], recipes[batch.PILOT]
    left, right = copy.deepcopy(recipe), copy.deepcopy(pilot_recipe)
    for value in (left, right):
        value.pop('represented_mpn')
        value.pop('appearance_status')
        value['marking'].pop('evidence')
        value['marking'].pop('appearance_status')
    if left != right or recipe['marking'].get('text') != '' or recipe['marking'].get('policy') != 'unmarked_illustration':
        raise ValueError('Candidate does not share the exact unmarked pilot rendering inputs')
    pilot_dir = renderer.ROOT / 'parts' / batch.PILOT / 'data/display_render'
    pilot_path = pilot_dir / 'manifest.json'
    original = json.loads(pilot_path.read_text(encoding='utf8'))
    studio = json.loads(renderer.STUDIO.read_text(encoding='utf8'))
    if (original['part_id'] != batch.PILOT or original['recipe'] != pilot_recipe or original['studio'] != studio
        or original['renderer_source_sha256'] != renderer.digest(renderer.__file__)
        or original['model']['sha256'] != batch.MODEL_SHA or original['marking']['text'] != ''
        or original['render']['pixels'] != 1400 or original['render']['samples'] != 256
        or original['render']['nonfinite_pixels_repaired'] != 0):
        raise ValueError('Published pilot no longer matches reviewed render')
    if renderer.digest(renderer.locate_model(recipe['model']['relative_path'])) != batch.MODEL_SHA:
        raise ValueError('KiCad source model changed')
    if set(original['artifacts']) != {'render.png', 'preview.webp'}:
        raise ValueError('Unexpected pilot artifacts')
    for name, info in original['artifacts'].items():
        path = pilot_dir / name
        if not path.is_file() or path.stat().st_size != info['bytes'] or renderer.digest(path) != info['sha256']:
            raise ValueError(f'Pilot artifact changed: {name}')
    marking_code = renderer.digest(Path(renderer.__file__).with_name('package_markings.py'))
    def inputs(r):
        return {'recipe': r, 'studio': studio, 'pixels': 1400, 'samples': 256,
                'renderer_sha256': original['renderer_source_sha256'], 'marking_code_sha256': marking_code,
                'font_sha256': None, 'runtime': original['runtime']}
    if json_hash(inputs(pilot_recipe)) != original['input_fingerprint']:
        raise ValueError('Pilot fingerprint no longer matches the current marking code')
    evidence = recipe['marking']['evidence']
    if renderer.digest(renderer.ROOT / evidence['file']) != evidence['sha256']:
        raise ValueError('Family evidence changed')
    manifest = copy.deepcopy(original)
    manifest['part_id'] = args.part
    manifest['recipe'] = recipe
    manifest['recipe_sha256'] = json_hash(recipe)
    manifest['input_fingerprint'] = json_hash(inputs(recipe))
    manifest['marking']['evidence_sha256'] = evidence['sha256']
    manifest['render']['reused_image'] = {'pilot_part_id': batch.PILOT, 'pilot_manifest_sha256': renderer.digest(pilot_path),
        'reason': 'Same reviewed unlit model, material, studio, output and empty marking; no independent path trace.'}
    manifest['render']['reuse_adapter_sha256'] = renderer.digest(__file__)
    manifest['render']['reuse_queue_sha256'] = renderer.digest(batch.__file__)
    out.mkdir(parents=True, exist_ok=True)
    for name in original['artifacts']:
        shutil.copy2(pilot_dir / name, out / name)
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf8')
    print(f'Prepared verified shared unlit image for {args.part}', flush=True)


if __name__ == '__main__':
    main()
