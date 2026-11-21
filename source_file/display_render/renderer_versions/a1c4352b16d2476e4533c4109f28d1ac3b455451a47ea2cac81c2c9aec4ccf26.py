"""Shared SOD-123 passes for the reviewed JSCJ BZT52 family.

Compare a pilot composite against the independent BZT52C10 render before using
these passes for other parts. Review each output; reflections are approximate.
"""
import argparse
import hashlib
import json

import yaml
from kicad_agents import display_render_composite as shared

renderer = shared.renderer
PILOT = 'electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10'
MODEL_SHA = 'b3dc4065573abc72e3d5b4cca0e908f72a24205a41b6284b1f75ccacbe99adf8'
original_inputs = shared.master_inputs


def read_recipe(part_id):
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    pilot = recipes[PILOT]
    recipe = recipes[part_id]
    mark = recipe['marking']
    source = renderer.ROOT / 'parts_source' / part_id / 'working.yaml'
    record = yaml.safe_load(source.read_text(encoding='utf8')) or {}
    evidence = mark['evidence']
    evidence_path = renderer.ROOT / evidence['file']
    if (not part_id.startswith('electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c')
        or recipe['family'] != 'diode' or recipe['package'] != 'sod_123'
        or recipe['model'] != pilot['model'] or recipe['model']['sha256'] != MODEL_SHA
        or recipe['output'] != pilot['output'] or recipe.get('disable_bump_for') != pilot.get('disable_bump_for')
        or mark.get('policy') != 'verified_literal' or mark.get('maximum_width_mm') != .8
        or mark.get('maximum_height_mm') != .45 or mark.get('offset_x_mm') != .25
        or mark.get('rotation_degrees', 0) != 0
        or record.get('manufacturer') != 'Jiangsu Changjing Electronics Technology Co., Ltd.'
        or record.get('part_number_manufacturer') != recipe['represented_mpn']
        or record.get('dimensions_mm') != {'height': 1.1, 'length': 1.6, 'width': 1.25}
        or (record.get('kicad') or {}).get('machine_solder') != 'Diode_SMD:D_SOD-123'
        or evidence.get('source_record') != f'parts_source/{part_id}/working.yaml'
        or hashlib.sha256(evidence_path.read_bytes()).hexdigest() != evidence.get('sha256')):
        raise ValueError('SOD-123 recipe or source differs from reviewed family setup')
    if part_id != PILOT:
        lines = evidence_path.read_text(encoding='utf8').splitlines()
        if not any(f"| {recipe['represented_mpn']} | {mark['text']} |" in line for line in lines):
            raise ValueError('Family marking evidence missing')
    manifest = renderer.ROOT / 'parts' / PILOT / 'data/display_render/manifest.json'
    if not manifest.is_file() or json.loads(manifest.read_text(encoding='utf8')).get('recipe') != pilot:
        raise ValueError('Published independent pilot differs from recipe')
    return recipe


def master_inputs(recipe, studio):
    inputs = original_inputs(recipe, studio)
    inputs['jscj_sod123_validator_sha256'] = renderer.digest(__file__)
    return inputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    master = sub.add_parser('make-master'); master.add_argument('part_id')
    render = sub.add_parser('render'); render.add_argument('part_id'); render.add_argument('--output', required=True)
    args = parser.parse_args()
    source_hash = renderer.digest(__file__)
    shared.read_recipe = read_recipe
    shared.master_inputs = master_inputs
    if args.command == 'make-master':
        shared.make_master(args.part_id)
    else:
        shared.render(args.part_id, args.output)
    if renderer.digest(__file__) != source_hash:
        raise RuntimeError('Validator changed during rendering; do not publish output')


if __name__ == '__main__':
    main()
