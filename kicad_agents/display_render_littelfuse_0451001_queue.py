"""Stage the drawing-based Littelfuse 451-series 1 A display model."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_2410_disposable_littelfuse_0451001_mrl'
MODEL = 'kicad_agents/display_model_littelfuse_451.py'
MODEL_SHA = '0384fe3d5c043026aed99b7abd32c34b165f9d1a8530d6d1eba439d6bd709435'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_LITTELFUSE_0451001_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Littelfuse' or record.get('part_number_manufacturer') != '0451001.MRL'
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
        or (record.get('kicad') or {}).get('machine_solder') != ''):
        raise ValueError('Fuse identity, source dimensions or footprint changed')
    if hashlib.sha256((ROOT / MODEL).read_bytes()).hexdigest() != MODEL_SHA:
        raise ValueError('Procedural fuse model changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='451_2410_procedural', represented_manufacturer='Littelfuse',
                  represented_mpn='0451001.MRL')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [6.10, 2.69, 2.69], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': 'LF 1A', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 2.7, 'maximum_height_mm': .8,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                     'document': 'Littelfuse 451/453 manufacturer family datasheet, viewed online',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Illustrative brand and 1 A marking; exact layout, ink and typeface are not established.'}
    recipe['appearance_status'] = ('Drawing-based 451-series nominal 6.10 x 2.69 x 2.69 mm ceramic body with 1.45 mm end caps. '
        'The source dimensions 10 x 5 mm conflict with the drawing and the source has no KiCad footprint. '
        'LF 1A marking, layout, colour, cap finish and small edge rounding are illustrative. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    # Reuse the existing atomic staging entry point while applying this exact recipe.
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
