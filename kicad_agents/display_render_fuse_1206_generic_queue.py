"""Stage a generic 1206 resettable fuse display."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_1206_resettable'
MODEL = 'Fuse.3dshapes/Fuse_1206_3216Metric.step'
MODEL_SHA = '5e6dcbe286696143d35a8ea37d91eef4b54ff3d1bd7c2c2b4dedda83d3f8e203'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_1206_RESETTABLE_FUSE_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') or record.get('part_number_manufacturer')
        or record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6}
        or (record.get('kicad') or {}).get('machine_solder') != 'Fuse:Fuse_1206_3216Metric'):
        raise ValueError('1206 source identity, size or footprint changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='1206_metric_3216', represented_manufacturer='',
                  represented_mpn='')
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination']
    recipe['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        copyright='2020 kicad StepUp', sha256=MODEL_SHA, expected_bounds_mm=[3.2, 1.6, .55],
        required_roles=['coating', 'ceramic', 'termination'],
        role_by_source_colour={'0.082,0.086,0.094': 'coating', '0.895,0.891,0.813': 'ceramic',
                               '0.824,0.820,0.781': 'termination'})
    recipe['marking'] = {'policy': 'unmarked_illustration', 'text': '', 'font_file': 'arialbd.ttf',
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Generic source record and KiCad 1206 model review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Deliberately unmarked: exact production marking, material and colour are not established.'}
    recipe['appearance_status'] = ('Generic KiCad 1206 fuse model with 3.20 x 1.60 x 0.55 mm bounds; '
        'the exact device height is not established. The source has no manufacturer, MPN, rating or datasheet; '
        'Dark body and metal ends are illustrative, and any marking is omitted. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
