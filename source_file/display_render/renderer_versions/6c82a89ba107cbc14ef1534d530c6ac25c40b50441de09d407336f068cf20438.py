"""Stage a drawing-inspired square Xucheng 5TE 1 A display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_5_mm_square_plugin_disposable_xucheng_elec_5te_10002r1bt'
MODEL = 'kicad_agents/display_model_xucheng_5te_1a.py'
MODEL_SHA = '579f0c921ae20af8d7570c83802addfafd3af7e15f3763c12483bb2edc9cefc0'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_XUCHENG_5TE_1A_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Xucheng Elec' or record.get('part_number_manufacturer') != '5TE.10002R1BT'
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
        or digest(ROOT / MODEL) != MODEL_SHA):
        raise ValueError('Radial fuse identity, dimensions, model or source drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='xucheng_5te_face_up', represented_manufacturer='Xucheng Electronics',
                  represented_mpn='5TE.10002R1BT')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [16.2, 8.4, 4.0], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': '1A 250V', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 3.2, 'maximum_height_mm': 1.4, 'offset_x_mm': 4.5,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Distributor 5TE dimensions and rating; no exact manufacturer drawing',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Illustrative 1A 250V marking; exact production inscription, ink and layout are unknown.'}
    recipe['appearance_status'] = ('Distributor-sized 5TE square fuse displayed lying face-up, with 5 mm lead pitch. '
        'No exact manufacturer drawing is available. Body curvature, dark finish, '
        'lead shape and marking are illustrative; manufacturer logo and approval marks omitted. '
        'Display illustration only; not manufacturing CAD or a footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
