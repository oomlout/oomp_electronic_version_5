"""Stage the drawing-inspired YXC HC-49US 11.0592 MHz display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_crystal_hc_49s_through_hole_2_pin_11_0592_mhz_20_pf_50_ohm_esr'
MODEL = 'kicad_agents/display_model_yxc_hc49us.py'
MODEL_SHA = '8b44495b27b1e3c1972897149faeec4a101709897e0a1f050ce6247cbbf00147'
PDF_SHA = '8d9dbc91b68d398acdebaf93a00d8b21ceca8cb94e6b12e62b564e2194ada5c0'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YXC_HC49US_110592_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'YXC Crystal Oscillators'
            or record.get('part_number_manufacturer') != 'X49SD110592MSD2SC'
            or '11.0592 MHz' not in record.get('name_proper', '')
            or record.get('dimensions_mm') != {'length': 11.5, 'width': 4.5, 'height': 3.6}
            or digest(ROOT / 'parts_source/electronic_crystal_hc_49s_through_hole_2_pin_10_mhz_20_pf_60_ohm_esr/datasheet.pdf') != PDF_SHA or digest(ROOT / MODEL) != MODEL_SHA):
        raise ValueError('Crystal source identity, dimensions, model or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='crystal', package='hc49us_through_hole',
                  represented_manufacturer='YXC Crystal Oscillators', represented_mpn='X49SD110592MSD2SC')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL,
        'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [11.4, 4.5, 9.6], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': '11.0592 MHz', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 5.5, 'maximum_height_mm': 1.0, 'offset_x_mm': 0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'YXC HC-49US sibling family drawing and source frequency; exact marking not specified',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Frequency inscription, ink and placement are illustrative; exact production marking is unknown.'}
    recipe['appearance_status'] = ('Low-profile oval metal HC-49US can with two leads based on the YXC family drawing. '
        'Can curvature, flange and finish are illustrative; frequency marking is illustrative and logo omitted. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
