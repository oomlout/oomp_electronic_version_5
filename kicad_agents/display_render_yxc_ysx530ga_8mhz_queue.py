"""Stage the reviewed KiCad 3225 crystal with illustrative frequency text."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_crystal_5032_surface_mount_2_pin_8_mhz_20_pf'
MODEL = 'Crystal.3dshapes/Crystal_SMD_5032-2Pin_5.0x3.2mm.step'
MODEL_SHA = '8db55547119e47f2a8f852b629b1df468b0a50286dbb4b62a50e10c6115975cc'
PDF_SHA = '8bf08a3bf19c155396a5113bbd11ab3b6bfdfe78b26c652125f18df11eb0eda2'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YXC_YSX530GA_8MHZ_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'YXC Crystal Oscillators'
            or record.get('part_number_manufacturer') != 'X50328MSB2GI'
            or '8 MHz' not in record.get('name_proper', '')
            or record.get('dimensions_mm') != {'length': 5.0, 'width': 3.2}
            or digest(source / 'datasheet.pdf') != PDF_SHA):
        raise ValueError('Crystal identity, drawing or dimensions changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='crystal', package='5032_two_pad',
                  represented_manufacturer='YXC Crystal Oscillators', represented_mpn='X50328MSB2GI')
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination', 'pin_indicator']
    recipe['model'] = {'relative_path': MODEL,
        'source_url': 'https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        'copyright': 'KiCad library contributors',
        'license': 'CC-BY-SA-4.0 with KiCad library exception; see original STEP header',
        'license_url': 'https://www.kicad.org/libraries/license/',
        'expected_bounds_mm': [5.0, 3.2, 1.13], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'metal_top_marking': True,
        'role_by_source_colour': {'0.372,0.372,0.373': 'termination', '0.824,0.820,0.781': 'termination',
                                  '0.859,0.738,0.496': 'pin_indicator', '0.148,0.145,0.145': 'ceramic'},
        'required_roles': ['coating', 'ceramic', 'termination', 'pin_indicator']}
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': '8 MHz', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 3.0, 'maximum_height_mm': .8, 'offset_x_mm': 0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'YXC YSX530GA family drawing; exact marking not established',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Frequency text and typography are illustrative; exact inscription not established.'}
    recipe['appearance_status'] = ('KiCad 5032 crystal dimensions are within the YXC family drawing tolerances; '
        'the KiCad model includes two underside contacts. Gold-coloured perimeter, dark lid and marking are illustrative; '
        'manufacturer logo and date code omitted. Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
