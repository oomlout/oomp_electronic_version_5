"""Advertise existing, current display images without importing any CAD/render engine."""
import hashlib
import json
from pathlib import Path
import re
import copy

ROOT = Path(__file__).resolve().parent


def unmarked_visual_recipe(recipe):
    """Keep every image-affecting field; remove only part identity/evidence."""
    if recipe.get('family') != 'chip_resistor' or recipe.get('marking', {}).get('policy') != 'none':
        raise ValueError('Only unmarked chip resistors can share this image')
    result = copy.deepcopy(recipe)
    for key in ('represented_manufacturer', 'represented_mpn', 'appearance_status'):
        result.pop(key, None)
    marking = result['marking']
    marking.pop('evidence', None)
    marking.pop('appearance_status', None)
    return result


def reused_image_valid(manifest, recipe, studio):
    reuse = manifest.get('reused_image')
    if reuse is None:
        return True
    if not isinstance(reuse, dict) or not re.fullmatch(r'electronic_[a-z0-9_]+', str(reuse.get('source_part', ''))):
        return False
    path = ROOT / 'parts' / reuse['source_part'] / 'data/display_render/manifest.json'
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != reuse.get('source_manifest_sha256'):
        return False
    try:
        source = json.loads(path.read_text(encoding='utf-8'))
        if (source.get('part_id') != reuse['source_part'] or source.get('reused_image') or source.get('composite')
            or source.get('studio') != studio or not renderer_source_available(source.get('renderer_source_sha256'))
            or source.get('renderer_source_sha256') != manifest.get('renderer_source_sha256')
            or unmarked_visual_recipe(source['recipe']) != unmarked_visual_recipe(recipe)
            or source.get('marking', {}).get('text') != ''
            or set(source.get('artifacts', {})) != {'render.png', 'preview.webp'}
            or source.get('artifacts') != manifest.get('artifacts')):
            return False
        return all((path.parent / name).is_file() and hashlib.sha256((path.parent / name).read_bytes()).hexdigest() == details['sha256']
                   for name, details in source['artifacts'].items())
    except (KeyError, TypeError, ValueError, OSError):
        return False


def source_available(expected_hash, live_file):
    """Verify a source against the live file or an exact archive."""
    if not isinstance(expected_hash, str) or not re.fullmatch(r'[0-9a-f]{64}', expected_hash):
        return False
    candidates = [ROOT / live_file,
                  ROOT / 'source_file/display_render/renderer_versions' / (expected_hash + '.py')]
    return any(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash
               for path in candidates)


def renderer_source_available(expected_hash):
    return source_available(expected_hash, 'kicad_agents/display_render.py')


def renderer_supports_marking(expected_hash, marking):
    """Do not advertise a character underline with a renderer that ignores it."""
    if marking.get('underline_character') is None:
        return True
    if not isinstance(expected_hash, str) or not re.fullmatch(r'[0-9a-f]{64}', expected_hash):
        return False
    candidates = [ROOT / 'kicad_agents/display_render.py',
                  ROOT / 'source_file/display_render/renderer_versions' / (expected_hash + '.py')]
    for path in candidates:
        if path.is_file():
            source = path.read_bytes()
            if hashlib.sha256(source).hexdigest() == expected_hash:
                return (b"marking.get('underline_character')" in source or
                        b'marking.get("underline_character")' in source)
    return False


def composite_sources_valid(manifest, recipe, studio):
    details = manifest.get('composite')
    if details is None:
        return True
    if not isinstance(details, dict) or not source_available(
        details.get('compositor_source_sha256'), 'kicad_agents/display_render_composite.py'):
        return False
    if not isinstance(details.get('master_manifest'), str):
        return False
    path = (ROOT / details.get('master_manifest', '')).resolve()
    if (not path.is_relative_to((ROOT / 'source_file/display_render/masters').resolve())
        or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != details.get('master_manifest_sha256')):
        return False
    master = json.loads(path.read_text(encoding='utf-8'))
    inputs = master.get('inputs', {})
    if (inputs.get('model') != recipe.get('model') or inputs.get('family') != recipe.get('family')
        or inputs.get('disable_bump_for', []) != recipe.get('disable_bump_for', [])
        or inputs.get('studio') != studio or inputs.get('pixels') != 1400 or inputs.get('samples') != 256
        or inputs.get('renderer_sha256') != manifest.get('renderer_source_sha256')
        or not source_available(inputs.get('builder_sha256'), 'kicad_agents/display_render_composite.py')):
        return False
    artifacts = master.get('artifacts', {})
    return set(artifacts) == {'body.png', 'ink.png'} and all(
        (path.parent/name).is_file() and (path.parent/name).stat().st_size == info.get('bytes')
        and hashlib.sha256((path.parent/name).read_bytes()).hexdigest() == info.get('sha256')
        for name, info in artifacts.items())


def apply_extras(extras_dict):
    recipes = json.loads((ROOT / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    studio = json.loads((ROOT / 'source_file/display_render/studio.json').read_text(encoding='utf-8'))
    for part_id, recipe in recipes.items():
        if part_id not in extras_dict:
            continue
        extras_dict[part_id].pop('display_render', None)
        folder = ROOT / 'parts' / part_id / 'data/display_render'
        path = folder / 'manifest.json'
        if not path.is_file():
            continue
        manifest = json.loads(path.read_text(encoding='utf-8'))
        recipe_hash = hashlib.sha256(json.dumps(recipe, sort_keys=True).encode()).hexdigest()
        if (manifest.get('part_id') != part_id or manifest.get('recipe_sha256') != recipe_hash
            or manifest.get('studio') != studio
            or not renderer_source_available(manifest.get('renderer_source_sha256'))
            or not renderer_supports_marking(manifest.get('renderer_source_sha256'), recipe.get('marking', {}))
            or not composite_sources_valid(manifest, recipe, studio)
            or not reused_image_valid(manifest, recipe, studio)):
            continue
        evidence = recipe.get('marking', {}).get('evidence', {})
        evidence_file = (ROOT / evidence.get('file', '')).resolve()
        if (not evidence_file.is_relative_to(ROOT.resolve()) or not evidence_file.is_file()
            or hashlib.sha256(evidence_file.read_bytes()).hexdigest() != evidence.get('sha256')
            or manifest.get('marking', {}).get('evidence_sha256') != evidence.get('sha256')):
            continue
        files = manifest.get('artifacts', {})
        if set(files) != {'render.png', 'preview.webp'} or any(
            not (folder/name).is_file() or hashlib.sha256((folder/name).read_bytes()).hexdigest() != item['sha256']
            for name, item in files.items()
        ):
            continue
        description = recipe['appearance_status'] + ' ' + recipe['marking']['appearance_status']
        if manifest.get('composite'):
            description += (' Marking composited in linear light from shared path-traced material passes; '
                            'indirect reflections are approximate.')
        if manifest.get('reused_image'):
            description += ' Image reused from an identical unmarked package and material setup.'
        extras_dict[part_id]['display_render'] = {
            'image': 'data/display_render/render.png',
            'preview': 'data/display_render/preview.webp',
            'provenance': 'data/display_render/manifest.json',
            'marking': manifest['marking']['text'],
            'description': description,
            'model_credit': recipe['model']['copyright'],
            'model_source': recipe['model']['source_url'],
            'license': recipe['model']['license'],
        }
