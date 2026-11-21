"""Stage the reviewed KiCad 3225 crystal with illustrative frequency text."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_crystal_3215_surface_mount_2_pin_32_768_khz_12_5_pf'
MODEL = 'Crystal.3dshapes/Crystal_SMD_3215-2Pin_3.2x1.5mm.step'
MODEL_SHA = '70191ff5204d0ce50e154f75b1186923e3123cfdb58d647b5cce319de5485701'
PDF_SHA = '6473c2f06c482eb2c3f1eaeaad37af139de02669d641de4e6a5cdb2bc703210d'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_EPSON_FC135_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Seiko Epson'
            or record.get('part_number_manufacturer') != 'Q13FC13500004'
            or '32.768 kHz' not in record.get('name_proper', '')
            or record.get('dimensions_mm') != {'length': 3.2, 'width': 1.5}
            or digest(source / 'datasheet.pdf') != PDF_SHA):
        raise ValueError('Crystal identity, drawing or dimensions changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='crystal', package='3215_two_pad',
                  represented_manufacturer='Seiko Epson', represented_mpn='Q13FC13500004')
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination', 'pin_indicator']
    recipe['model'] = {'relative_path': MODEL,
        'source_url': 'https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        'copyright': 'KiCad library contributors',
        'license': 'CC-BY-SA-4.0 with KiCad library exception; see original STEP header',
        'license_url': 'https://www.kicad.org/libraries/license/',
        'expected_bounds_mm': [3.2, 1.5, .93], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'metal_top_marking': True,
        'role_by_source_colour': {'0.372,0.372,0.373': 'termination', '0.824,0.820,0.781': 'termination',
                                  '0.859,0.738,0.496': 'pin_indicator', '0.148,0.145,0.145': 'ceramic'},
        'required_roles': ['coating', 'ceramic', 'termination', 'pin_indicator']}
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': 'C622J', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 1.8, 'maximum_height_mm': .42, 'offset_x_mm': 0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Epson FC-135 drawing example C622J; fixed production marking not established',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'C622J is an illustrative drawing example; exact production inscription and typography are not established.'}
    recipe['appearance_status'] = ('KiCad 3215 crystal is 0.93 mm tall, 0.03 mm above the Epson drawing maximum; '
        'the KiCad model includes two underside contacts. Gold-coloured perimeter, dark lid and marking are illustrative; '
        'manufacturer logo and date code omitted. Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
