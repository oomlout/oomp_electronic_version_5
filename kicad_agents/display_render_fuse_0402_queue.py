"""Stage a generic 0402 resettable fuse display with identity caveats."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_0402_resettable'
MODEL = 'Fuse.3dshapes/Fuse_0402_1005Metric.step'
MODEL_SHA = 'c18cb5f8977e59e7f62917f145c9ee7efeeaf96ed4a69b0ffb965911153f2608'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FUSE_0402_SMD0402_004_12_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'R+O' or record.get('part_number_manufacturer') != 'SMD0402-004-12'
        or record.get('dimensions_mm') != {'length': 1.0, 'width': .5}
        or (record.get('kicad') or {}).get('machine_solder') != 'Fuse:Fuse_0402_1005Metric'):
        raise ValueError('0402 source identity, size or footprint changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='0402_metric_1005', represented_manufacturer='R+O',
                  represented_mpn='SMD0402-004-12')
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination']
    recipe['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        copyright='2020 kicad StepUp', sha256=MODEL_SHA, expected_bounds_mm=[1.0, .52, .35],
        required_roles=['coating', 'ceramic', 'termination'],
        role_by_source_colour={'0.082,0.086,0.094': 'coating', '0.895,0.891,0.813': 'ceramic',
                               '0.824,0.820,0.781': 'termination'})
    recipe['marking'] = {'policy': 'unmarked_illustration', 'text': '', 'font_file': 'arialbd.ttf',
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'LCSC and Hongjiacheng MPN listings; KiCad 0402 model review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Deliberately unmarked: exact production marking, material and colour are not established.'}
    recipe['appearance_status'] = ('Generic KiCad 0402 fuse model with 1.00 x 0.52 x 0.35 mm bounds; '
        'the exact device height is not established. R+O source identity differs from another listing naming Hongjiacheng; '
        'their relationship is unverified. Dark body and metal ends are illustrative, and any marking is omitted. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
