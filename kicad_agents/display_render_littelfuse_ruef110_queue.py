"""Stage a drawing-inspired radial RUEF110 display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_radial_5_08_mm_pitch_resettable_littelfuse_ruef110'
MODEL = 'kicad_agents/display_model_littelfuse_ruef110.py'
MODEL_SHA = '8a09dea193332e8d6e24fabd31902bc5192e105d260da6b9460cff3075369b69'
PDF_SHA = 'cf03cd3a63b2f97721f654e5bb97647656a1a658fba845ff3ca898ea6ca2ad6d'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_LITTELFUSE_RUEF110_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Littelfuse' or record.get('part_number_manufacturer') != 'RUEF110'
        or record.get('dimensions_mm') != {'length': 7.4, 'width': 6.6, 'height': 3.0}
        or digest(source / 'datasheet.pdf') != PDF_SHA or digest(ROOT / MODEL) != MODEL_SHA):
        raise ValueError('Radial fuse identity, dimensions, model or source drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='ruef_radial_face_up', represented_manufacturer='Littelfuse',
                  represented_mpn='RUEF110')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [17.0, 7.0, 2.4], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'verified_literal', 'text': 'U110', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 3.2, 'maximum_height_mm': 1.4, 'offset_x_mm': 4.5,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Local Tyco RUEF110 drawing and marking',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Manufacturer code U110; omitted logo and lot code, ink, typeface and placement are illustrative.'}
    recipe['appearance_status'] = ('Drawing-inspired RUEF110 radial fuse displayed lying face-up, with 5.08 mm lead pitch. '
        'Manufacturer drawing provides maximum dimensions, not the exact nominal body size. Rounded rectangular body, yellow finish, '
        'lead shape and marking layout are illustrative; manufacturer logo and lot code omitted. '
        'Display illustration only; not manufacturing CAD or a footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
