"""Stage a generic 1210 resettable fuse display."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_1210_resettable_6_volt_2_amp_4_amp'
MODEL = 'Fuse.3dshapes/Fuse_1210_3225Metric.step'
MODEL_SHA = 'a2f37cb6e4b6f7a8f2d2ebbbf7feddc654cfba27f38f8a8a35d303017fabf2ba'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_1210_RESETTABLE_FUSE_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') or record.get('part_number_manufacturer')
        or record.get('dimensions_mm') != {'length': 3.2, 'width': 2.5}
        or (record.get('kicad') or {}).get('machine_solder') != ''):
        raise ValueError('1210 source identity, size or footprint changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='1210_metric_3225', represented_manufacturer='',
                  represented_mpn='')
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination']
    recipe['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        copyright='2020 kicad StepUp', sha256=MODEL_SHA, expected_bounds_mm=[3.2, 2.5, 1.6],
        required_roles=['coating', 'ceramic', 'termination'],
        role_by_source_colour={'0.082,0.086,0.094': 'coating', '0.895,0.891,0.813': 'ceramic',
                               '0.824,0.820,0.781': 'termination'})
    recipe['marking'] = {'policy': 'unmarked_illustration', 'text': '', 'font_file': 'arialbd.ttf',
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Generic source record and KiCad 1210 model review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Deliberately unmarked: exact production marking, material and colour are not established.'}
    recipe['appearance_status'] = ('Generic KiCad 1210 fuse model with 3.20 x 2.50 x 1.60 mm bounds; '
        'the exact device height is not established. The source has no manufacturer, MPN or datasheet; the source name lists 6 V, 2 A and 4 A without further detail; '
        'Dark body and metal ends are illustrative, and any marking is omitted. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
