"""Stage a source-backed miniSMDC020F resettable fuse display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_1812_resettable_littelfuse_minismdc020f_2'
MODEL = 'kicad_agents/display_model_littelfuse_minismdc.py'
MODEL_SHA = 'd66c0fb6a77d89c60317f8c1ebb0ee00e38d759757afd72d9f4cc982d979abbb'
PDF_SHA = '7b7cb3a9edb8103455448bae8a77bc64c72082e6b90006a8698635a2ebeaac2c'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_LITTELFUSE_MINISMDC020F_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Littelfuse' or record.get('part_number_manufacturer') != 'MINISMDC020F-2'
        or record.get('dimensions_mm') != {'length': 4.5, 'width': 3.2, 'height': 2.4}
        or digest(source / 'datasheet.pdf') != PDF_SHA):
        raise ValueError('Fuse identity, source dimensions or local drawing changed')
    if digest(ROOT / MODEL) != MODEL_SHA:
        raise ValueError('Procedural fuse model changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='minismdc_1812_procedural', represented_manufacturer='Littelfuse',
                  represented_mpn='MINISMDC020F-2')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [4.55, 3.24, .76], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'verified_literal', 'text': '2', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 1.0, 'maximum_height_mm': 1.2,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Local Tyco family datasheet pp. 7, 9, 15 and Littelfuse part drawing',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Manufacturer code 2; omitted logo, ink, typeface and placement are illustrative.'}
    recipe['appearance_status'] = ('Drawing-based miniSMDC display geometry with concave ends and 4.55 x 3.24 x 0.76 mm bounds '
        'within manufacturer limits. The source height 2.4 mm exceeds the drawing maximum 0.89 mm. '
        'The code 2 is documented; body colour, ink, omitted logo, exact notch shape and finish are illustrative. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
