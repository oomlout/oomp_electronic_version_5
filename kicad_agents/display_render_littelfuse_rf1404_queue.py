"""Stage a source-backed Littelfuse RF1404-000 resettable fuse display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_1812_resettable_littelfuse_rf1404_000'
MODEL = 'kicad_agents/display_model_littelfuse_minismdc.py'
MODEL_SHA = 'd66c0fb6a77d89c60317f8c1ebb0ee00e38d759757afd72d9f4cc982d979abbb'
PDF_SHA = '7b7cb3a9edb8103455448bae8a77bc64c72082e6b90006a8698635a2ebeaac2c'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_LITTELFUSE_RF1404_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Littelfuse' or record.get('part_number_manufacturer') != 'RF1404-000'
        or record.get('dimensions_mm') != {'length': 4.5, 'width': 3.2, 'height': 2.4}
        or (record.get('jlcpcb_selection', {}).get('ratings', {}).get('Length') != '5.4mm')
        or digest(ROOT / 'parts_source/electronic_fuse_1812_resettable_littelfuse_minismdc020f_2/datasheet.pdf') != PDF_SHA):
        raise ValueError('Fuse identity, source dimensions or local drawing changed')
    if digest(ROOT / MODEL) != MODEL_SHA:
        raise ValueError('Procedural fuse model changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='rf1404_1812_procedural', represented_manufacturer='Littelfuse',
                  represented_mpn='RF1404-000')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [4.55, 3.24, .76], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'display_scale_xyz': [1.0, 1.0, .5/.76], 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'verified_literal', 'text': '7', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 2.0, 'maximum_height_mm': 1.0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Local Tyco family datasheet pages 7, 9 and 15; Littelfuse RF1404 certificate online',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Manufacturer code 7; omitted logo, ink, typeface and placement are illustrative.'}
    recipe['appearance_status'] = ('Drawing-based concave-end display geometry adjusted from 0.76 to 0.50 mm high, with 4.55 x 3.24 x 0.50 mm bounds '
        'within manufacturer limits. The source height 2.4 mm exceeds the drawing maximum 0.62 mm, and the distributor field 5.4 mm length exceeds the drawing maximum 4.73 mm. '
        'The code 7 is documented; body colour, ink, omitted logo, exact notch shape and finish are illustrative. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
