"""Stage a drawing-inspired radial RXEF010 display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_radial_5_08_mm_pitch_resettable_littelfuse_rxef010'
MODEL = 'kicad_agents/display_model_littelfuse_rxef010.py'
MODEL_SHA = '51dc3481a51675c8900dabddbee333be22b1b996db44b46da85c7c44496e4f8f'
PDF_SHA = 'e6ddfc474ba47e8cc9ebaeb418a1082e58612288a7de7ddd0bb97f4446874ee0'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_LITTELFUSE_RXEF010_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Littelfuse' or record.get('part_number_manufacturer') != 'RXEF010'
        or record.get('dimensions_mm') != {'length': 7.4, 'width': 6.6, 'height': 3.0}
        or digest(source / 'datasheet.pdf') != PDF_SHA or digest(ROOT / MODEL) != MODEL_SHA):
        raise ValueError('Radial fuse identity, dimensions, model or source drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='rxef_radial_face_up', represented_manufacturer='Littelfuse',
                  represented_mpn='RXEF010')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [15.6, 7.0, 2.4], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'verified_literal', 'text': 'X10', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 3.2, 'maximum_height_mm': 1.4, 'offset_x_mm': 4.5,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Local Tyco RXEF010 drawing and marking',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Manufacturer code X10; omitted logo and lot code, ink, typeface and placement are illustrative.'}
    recipe['appearance_status'] = ('Drawing-inspired RXEF010 radial fuse displayed lying face-up, with 5.08 mm lead pitch. '
        'Manufacturer drawing provides maximum dimensions, not the exact nominal body size. Body curvature, yellow finish, '
        'lead shape and marking layout are illustrative; manufacturer logo and lot code omitted. '
        'The drawing gives 0.10 A hold while one source note says 1 A. Display illustration only; not manufacturing CAD or a footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
