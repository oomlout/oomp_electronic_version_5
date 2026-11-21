"""Use the reviewed SOT-23 body pass for exact generic unmarked entries."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import time

from PIL import Image
import yaml
from kicad_agents import display_render_sot23_composite as shared
from kicad_agents import display_render_generic_transistor_packages_queue as queue


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=queue.PARTS)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    renderer = shared.renderer
    adapter_sha = renderer.digest(__file__)
    queue_sha = renderer.digest(queue.__file__)
    recipe = shared.read_recipe(args.part)
    source = renderer.ROOT / 'parts_source' / args.part
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    evidence = recipe['marking']['evidence']
    if (record.get('manufacturer') not in ('', None) or record.get('part_number_manufacturer') not in ('', None)
        or record.get('dimensions_mm') != {'length': 2.9, 'width': 2.6}
        or (record.get('kicad') or {}).get('machine_solder') != '' or (source / 'datasheet.pdf').exists()
        or recipe['represented_manufacturer'] != 'Unspecified' or recipe['represented_mpn'] != queue.PARTS[args.part]
        or recipe['marking'].get('policy') != 'unmarked_illustration' or recipe['marking'].get('text') != ''
        or evidence['file'] != queue.EVIDENCE.as_posix()
        or evidence['sha256'] != renderer.digest(renderer.ROOT / queue.EVIDENCE)):
        raise ValueError('Generic entry, recipe or evidence changed')
    studio = json.loads(renderer.STUDIO.read_text(encoding='utf8'))
    inputs = shared.master_inputs(recipe, studio)
    master_dir = shared.MASTER_ROOT / shared.json_hash(inputs)
    master_file = master_dir / 'manifest.json'
    master = json.loads(master_file.read_text(encoding='utf8'))
    if (master.get('inputs') != inputs or not shared.check_files(master_dir, master.get('artifacts', {}), {'body.png', 'ink.png'})
        or any(item.get('nonfinite_pixels_repaired') != 0 for item in master['render'].values())):
        raise ValueError('Shared SOT-23 master changed or contains invalid pixels')
    if args.output.exists() and (not args.output.is_dir() or any(args.output.iterdir())):
        raise FileExistsError('Existing output is preserved')
    args.output.mkdir(parents=True, exist_ok=True)
    shutil.copy2(master_dir / 'body.png', args.output / 'render.png')
    with Image.open(args.output / 'render.png') as picture:
        picture = picture.convert('RGB')
        picture.thumbnail((recipe['output']['thumbnail_pixels'], recipe['output']['thumbnail_pixels']), Image.Resampling.LANCZOS)
        picture.save(args.output / 'preview.webp', quality=90, method=6)
    if renderer.digest(__file__) != adapter_sha or renderer.digest(queue.__file__) != queue_sha:
        raise RuntimeError('Generic adapter or queue changed while rendering')
    fingerprint = shared.json_hash({'recipe': recipe, 'master_manifest_sha256': renderer.digest(master_file),
                                    'adapter_sha256': adapter_sha, 'queue_sha256': queue_sha})
    manifest = {'schema_version': 1, 'part_id': args.part, 'purpose': 'display_only',
        'input_fingerprint': fingerprint, 'recipe': recipe, 'recipe_sha256': shared.json_hash(recipe),
        'studio': studio, 'runtime': shared.runtime_versions(), 'model': master['model'],
        'marking': {'text': '', 'font': None, 'evidence_sha256': renderer.digest(renderer.ROOT / queue.EVIDENCE)},
        'renderer_source_sha256': inputs['renderer_sha256'],
        'composite': {'method': 'unmarked shared path-traced body pass',
            'limitation': 'Generic unmarked package illustration; actual part markings are unknown.',
            'compositor_source_sha256': renderer.digest(shared.__file__),
            'candidate_validator_sha256': adapter_sha, 'candidate_batch_sha256': queue_sha,
            'master_manifest': master_file.relative_to(renderer.ROOT).as_posix(),
            'master_manifest_sha256': renderer.digest(master_file)},
        'render': {'pixels': 1400, 'samples_per_master': 256, 'seconds': round(time.perf_counter()-started, 2)},
        'artifacts': {name: {'sha256': renderer.digest(args.output / name), 'bytes': (args.output / name).stat().st_size}
                      for name in ('render.png', 'preview.webp')}}
    (args.output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')
    print('Unmarked display', args.part, 'written to', args.output, flush=True)


if __name__ == '__main__':
    main()
