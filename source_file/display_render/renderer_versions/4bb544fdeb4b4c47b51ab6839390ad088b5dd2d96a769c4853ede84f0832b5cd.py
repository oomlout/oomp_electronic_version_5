"""Stage the drawing-inspired YXC HC-49SMD 24 MHz display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_crystal_hc_49s_smd_surface_mount_2_pin_24_mhz_20_pf_35_ohm_esr'
MODEL = 'kicad_agents/display_model_yxc_hc49smd.py'
MODEL_SHA = '3f3e766f0e7e4df3ed6a2e953502b0c4d39a0b4b2822bdc2019c6924665f30fd'
PDF_SHA = '6e7d2d4116b38ecf854eb09bc31dda421ca7d8ab91492b81df9b5c4792783b41'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YXC_HC49SMD_24_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'YXC Crystal Oscillators'
            or record.get('part_number_manufacturer') != 'X49SM24MSD2SC'
            or '24 MHz' not in record.get('name_proper', '')
            or record.get('dimensions_mm') != {'length': 11.4, 'width': 4.8, 'height': 3.8}
            or digest(ROOT / 'parts_source/electronic_crystal_hc_49s_smd_surface_mount_2_pin_10_mhz_20_pf_60_ohm_esr/datasheet.pdf') != PDF_SHA or digest(ROOT / MODEL) != MODEL_SHA):
        raise ValueError('Crystal source identity, dimensions, model or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='crystal', package='hc49smd_surface_mount',
                  represented_manufacturer='YXC Crystal Oscillators', represented_mpn='X49SM24MSD2SC')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL,
        'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [11.4, 4.8, 3.8], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': '24 MHz', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 5.5, 'maximum_height_mm': 1.0, 'offset_x_mm': 0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'YXC HC-49SMD sibling family drawing and source frequency; exact marking not specified',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Frequency inscription, ink and placement are illustrative; exact production marking is unknown.'}
    recipe['appearance_status'] = ('Low-profile oval metal HC-49SMD can with two underside terminals based on the YXC family drawing. '
        'Can curvature, carrier and finish are illustrative; frequency marking is illustrative and logo omitted. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
