"""Stage a source-backed axial Littelfuse 251 500 mA display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_2_8_x_7_1_mm_glass_plugin_disposable_littelfuse_0251_500nrt1l'
MODEL = 'kicad_agents/display_model_littelfuse_251_500.py'
MODEL_SHA = '6fc6a30f2f6134e01a326c6b7419f71a16702ec013c526aea6230ec908dedcf8'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_LITTELFUSE_251_500_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Littelfuse' or record.get('part_number_manufacturer') != '0251.500NRT1L'
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0} or digest(ROOT / MODEL) != MODEL_SHA):
        raise ValueError('PICO fuse source or model changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='pico_251_axial', represented_manufacturer='Littelfuse',
                  represented_mpn='0251.500NRT1L')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [16.11, 2.8, 2.8], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': 'LF 0.5A', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 5.2, 'maximum_height_mm': .9,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Littelfuse 251 series datasheet viewed online',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Illustrative LF 0.5A inscription; exact production marking and placement are not verified.'}
    recipe['appearance_status'] = ('Molded axial PICO II body, 7.11 x 2.8 mm with 0.64 mm leads shortened for display. '
        'The source 10 x 5 mm dimensions and glass-plugin taxonomy differ from the manufacturer axial drawing. '
        'Green body, yellow ink, inscription, lead length and fine contours are illustrative. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
