"""Reuse an inspected render only for visually identical unmarked chip resistors.

This does not publish pages. Each target retains its own evidence and recipe;
the manifest explicitly records the source image rather than claiming a render.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil

import yaml

from working_oomp_populate_display_render import ROOT, reused_image_valid
from kicad_agents.display_render_resistor_queue import PILOT
from kicad_agents.display_render_small_resistor_queue import reviewed_recipe as uniroyal_recipe
from kicad_agents.display_render_fojan_queue import reviewed_recipe as fojan_recipe
from kicad_agents.display_render_fojan_low_queue import reviewed_decimal_recipe as fojan_low_recipe, EVIDENCE as FOJAN_LOW_EVIDENCE
from kicad_agents.display_render_fojan_5pct_queue import reviewed_recipe as fojan_5pct_recipe, EVIDENCE as FOJAN_5PCT_EVIDENCE
from kicad_agents.display_render_multi_0201_queue import reviewed_recipe as multi_0201_recipe, EVIDENCE as MULTI_0201_EVIDENCE
from kicad_agents.display_render_yageo_small_queue import reviewed_recipe as yageo_recipe
from kicad_agents.display_render_yageo_ac0402_queue import reviewed_recipe as yageo_ac_recipe, EVIDENCE as YAGEO_AC_EVIDENCE
from kicad_agents.display_render_yageo_visual_0201_queue import reviewed_recipe as yageo_visual_recipe, EVIDENCE as YAGEO_VISUAL_EVIDENCE
from kicad_agents.display_render_yageo_selected_0201_queue import reviewed_recipe as yageo_selected_recipe, EVIDENCE as YAGEO_SELECTED_EVIDENCE
from kicad_agents.display_render_yageo_selected_0402_queue import reviewed_recipe as yageo_selected_0402_recipe, EVIDENCE as YAGEO_SELECTED_0402_EVIDENCE
from kicad_agents.display_render_yageo_small_selected_queue import reviewed_recipe as yageo_small_selected_recipe, EVIDENCE as YAGEO_SMALL_SELECTED_EVIDENCE
from kicad_agents.display_render_yageo_generic_0201_queue import reviewed_recipe as yageo_generic_recipe, EVIDENCE as YAGEO_GENERIC_EVIDENCE
from kicad_agents.display_render_yageo_generic_0402_queue import reviewed_recipe as yageo_generic_0402_recipe, EVIDENCE as YAGEO_GENERIC_0402_EVIDENCE
from kicad_agents.display_render_fenghua_small_queue import reviewed_recipe as fenghua_recipe
from kicad_agents.display_render_fenghua_0402_5pct_queue import reviewed_recipe as fenghua_5pct_recipe, EVIDENCE as FENGHUA_5PCT_EVIDENCE
from kicad_agents.display_render_ralec_small_queue import reviewed_recipe as ralec_small_recipe, EVIDENCE as RALEC_SMALL_EVIDENCE


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(part_id, source_id):
    if not all(re.fullmatch(r'electronic_[a-z0-9_]+', x) for x in (part_id, source_id)):
        raise ValueError('Use exact component IDs')
    recipes = json.loads((ROOT / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    studio = json.loads((ROOT / 'source_file/display_render/studio.json').read_text(encoding='utf-8'))
    recipe = recipes[part_id]
    source_folder = ROOT / 'parts' / source_id / 'data/display_render'
    source_file = source_folder / 'manifest.json'
    source = json.loads(source_file.read_text(encoding='utf-8'))
    evidence = recipe['marking']['evidence']
    path = (ROOT / evidence['file']).resolve()
    if not path.is_relative_to(ROOT.resolve()) or not path.is_file() or digest(path) != evidence['sha256']:
        raise ValueError('Target evidence is missing or has changed')
    record_path = ROOT / 'parts_source' / part_id / 'working.yaml'
    record = yaml.safe_load(record_path.read_text(encoding='utf-8')) or {}
    if evidence.get('file') == FOJAN_5PCT_EVIDENCE.as_posix():
        ledger = json.loads((ROOT / FOJAN_5PCT_EVIDENCE).read_text(encoding='utf-8'))
        identities = {item['part_id']: item for item in ledger['records']}
        checked_recipe = fojan_5pct_recipe(part_id, record, recipes, evidence['sha256'], identities)
    elif evidence.get('file') == MULTI_0201_EVIDENCE.as_posix():
        checked_recipe = multi_0201_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_GENERIC_0402_EVIDENCE.as_posix():
        checked_recipe = yageo_generic_0402_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_GENERIC_EVIDENCE.as_posix():
        checked_recipe = yageo_generic_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_SMALL_SELECTED_EVIDENCE.as_posix():
        checked_recipe = yageo_small_selected_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_SELECTED_0402_EVIDENCE.as_posix():
        checked_recipe = yageo_selected_0402_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_SELECTED_EVIDENCE.as_posix():
        checked_recipe = yageo_selected_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_VISUAL_EVIDENCE.as_posix():
        checked_recipe = yageo_visual_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_AC_EVIDENCE.as_posix():
        checked_recipe = yageo_ac_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_5PCT_EVIDENCE.as_posix():
        checked_recipe = fenghua_5pct_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == RALEC_SMALL_EVIDENCE.as_posix():
        checked_recipe = ralec_small_recipe(part_id, record, recipes, evidence['sha256'])
    elif recipe.get('represented_manufacturer') == 'UNI-ROYAL':
        checked_recipe = uniroyal_recipe(part_id, record, recipes[PILOT])
    elif recipe.get('represented_manufacturer') == 'FOJAN':
        if evidence.get('file') == FOJAN_LOW_EVIDENCE.as_posix():
            checked_recipe = fojan_low_recipe(part_id, record, recipes, evidence['sha256'])
        else:
            checked_recipe = fojan_recipe(part_id, record, recipes[PILOT], evidence['sha256'])
    elif recipe.get('represented_manufacturer') == 'YAGEO':
        checked_recipe = yageo_recipe(part_id, record, recipes[PILOT], evidence['sha256'])
    elif recipe.get('represented_manufacturer') == 'FH':
        checked_recipe = fenghua_recipe(part_id, record, recipes[PILOT], evidence['sha256'])
    else:
        raise ValueError('This supplier needs a reviewed source-record adapter')
    if recipe != checked_recipe:
        raise ValueError('Current part record does not match the reviewed recipe')
    target = copy.deepcopy(source)
    target.update(part_id=part_id, recipe=recipe,
                  recipe_sha256=hashlib.sha256(json.dumps(recipe, sort_keys=True).encode()).hexdigest())
    target['marking']['evidence_sha256'] = evidence['sha256']
    target['reused_image'] = {'source_part': source_id, 'source_manifest_sha256': digest(source_file),
                              'method': 'identical unmarked package, materials, studio and output'}
    target['input_fingerprint'] = hashlib.sha256(json.dumps(
        {'recipe': recipe, 'reuse': target['reused_image']}, sort_keys=True).encode()).hexdigest()
    if not reused_image_valid(target, recipe, studio):
        raise ValueError('Source image is damaged or does not match this visual recipe')
    destination = ROOT / 'parts' / part_id / 'data/display_render'
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise FileExistsError(f'Existing output preserved: {destination}')
    destination.mkdir(parents=True, exist_ok=True)
    for name in ('render.png', 'preview.webp'):
        shutil.copyfile(source_folder / name, destination / name)
    (destination / 'manifest.json').write_text(json.dumps(target, indent=2) + '\n', encoding='utf-8')
    print(f'Reused inspected {source_id} image for {part_id}; review and publish separately.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part_id')
    parser.add_argument('source_id')
    args = parser.parse_args()
    prepare(args.part_id, args.source_id)


if __name__ == '__main__':
    main()
