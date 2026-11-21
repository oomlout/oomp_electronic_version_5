"""Stage a generic 0805 resettable fuse display."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_0805_resettable'
MODEL = 'Fuse.3dshapes/Fuse_0805_2012Metric.step'
MODEL_SHA = 'bd29ccc62530d3bcfbbe078f12aac2a99ac75d01c043a2723a4bd36540aac146'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_0805_RESETTABLE_FUSE_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') or record.get('part_number_manufacturer')
        or record.get('dimensions_mm') != {'length': 2.0, 'width': 1.25}
        or (record.get('kicad') or {}).get('machine_solder') != ''):
        raise ValueError('0805 source identity, size or footprint changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='0805_metric_2012', represented_manufacturer='',
                  represented_mpn='')
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination']
    recipe['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        copyright='2020 kicad StepUp', sha256=MODEL_SHA, expected_bounds_mm=[2.0, 1.25, .45],
        required_roles=['coating', 'ceramic', 'termination'],
        role_by_source_colour={'0.082,0.086,0.094': 'coating', '0.895,0.891,0.813': 'ceramic',
                               '0.824,0.820,0.781': 'termination'})
    recipe['marking'] = {'policy': 'unmarked_illustration', 'text': '', 'font_file': 'arialbd.ttf',
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Generic source record and KiCad 0805 model review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Deliberately unmarked: exact production marking, material and colour are not established.'}
    recipe['appearance_status'] = ('Generic KiCad 0805 fuse model with 2.00 x 1.25 x 0.45 mm bounds; '
        'the exact device height is not established. The source has no manufacturer, MPN, rating or datasheet; '
        'Dark body and metal ends are illustrative, and any marking is omitted. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
