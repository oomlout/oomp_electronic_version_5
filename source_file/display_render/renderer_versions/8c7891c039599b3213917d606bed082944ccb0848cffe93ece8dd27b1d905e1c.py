"""Stage the reviewed KiCad 3225 crystal with illustrative frequency text."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf_80_ohm_esr'
MODEL = 'Crystal.3dshapes/Crystal_SMD_3225-4Pin_3.2x2.5mm.step'
MODEL_SHA = 'd2a89df82ee5f0f56ef23ee59c8161b8d4e92af2b21959d72778316dde3f9f22'
PDF_SHA = '7bc18549e407d8e381075b0f5fc696e48cf0fa060aeee67971925f43cfdfbb8b'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YXC_YSX321SL_12MHZ_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'YXC Crystal Oscillators'
            or record.get('part_number_manufacturer') != 'X322512MSB4SI'
            or '12 MHz' not in record.get('name_proper', '')
            or record.get('dimensions_mm') != {'length': 3.2, 'width': 2.5, 'height': .7}
            or digest(source / 'datasheet.pdf') != PDF_SHA):
        raise ValueError('Crystal identity, drawing or dimensions changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='crystal', package='3225_four_pad',
                  represented_manufacturer='YXC Crystal Oscillators', represented_mpn='X322512MSB4SI')
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination', 'pin_indicator']
    recipe['model'] = {'relative_path': MODEL,
        'source_url': 'https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        'copyright': 'KiCad library contributors',
        'license': 'CC-BY-SA-4.0 with KiCad library exception; see original STEP header',
        'license_url': 'https://www.kicad.org/libraries/license/',
        'expected_bounds_mm': [3.20043, 2.50084, .64], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'metal_top_marking': True,
        'role_by_source_colour': {'0.824,0.820,0.781': 'termination', '0.859,0.738,0.496': 'pin_indicator',
                                  '0.160,0.160,0.160': 'ceramic'},
        'required_roles': ['coating', 'ceramic', 'termination', 'pin_indicator']}
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': '12 MHz', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 2.1, 'maximum_height_mm': .55, 'offset_x_mm': 0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'YXC YSX321SL family drawing; exact marking not specified',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Frequency inscription, typography and placement are illustrative; exact marking unknown.'}
    recipe['appearance_status'] = ('KiCad 3225 metal-capped crystal is within family drawing tolerances; '
        'the KiCad underside omits the four separate pads. Gold-coloured perimeter, dark base and marking are illustrative; '
        'manufacturer logo and date code omitted. Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
