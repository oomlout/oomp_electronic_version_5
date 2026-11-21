"""Stage a source-backed PTTC SMD1812P110TF resettable fuse display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_1812_resettable_pttc_polytronics_tech_smd1812p110tf'
MODEL = 'kicad_agents/display_model_littelfuse_minismdc.py'
MODEL_SHA = 'd66c0fb6a77d89c60317f8c1ebb0ee00e38d759757afd72d9f4cc982d979abbb'
PDF_SHA = 'a069663b6cacca56713e2c319c9de96d8a5fc1f15f39e7a480fbd2f6d8f875d0'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_PTTC_SMD1812P110TF_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'PTTC(Polytronics Tech)' or record.get('part_number_manufacturer') != 'SMD1812P110TF'
        or record.get('dimensions_mm') != {'length': 4.5, 'width': 3.2, 'height': 2.4}
        or digest(source / 'datasheet.pdf') != PDF_SHA):
        raise ValueError('Fuse identity, source dimensions or local drawing changed')
    if digest(ROOT / MODEL) != MODEL_SHA:
        raise ValueError('Procedural fuse model changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='pttc_1812_procedural', represented_manufacturer='PTTC(Polytronics Tech)',
                  represented_mpn='SMD1812P110TF')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [4.55, 3.24, .76], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'display_scale_xyz': [1.0, 1.0, .5/.76], 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'verified_literal', 'text': '110', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 2.0, 'maximum_height_mm': 1.0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Local Polytronics manufacturer family datasheet pages 10 and 12',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Manufacturer code 110; omitted logo, ink, typeface and placement are illustrative.'}
    recipe['appearance_status'] = ('Drawing-based concave-end display geometry adjusted from 0.76 to 0.50 mm high, with 4.55 x 3.24 x 0.50 mm bounds '
        'within manufacturer limits. The source height 2.4 mm exceeds the drawing maximum 0.71 mm. '
        'The code 110 is documented; body colour, ink, omitted logo, exact notch shape and finish are illustrative. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
