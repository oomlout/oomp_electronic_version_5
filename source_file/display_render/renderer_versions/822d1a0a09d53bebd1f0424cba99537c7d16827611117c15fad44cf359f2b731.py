"""Stage a drawing-based Xucheng 2 A glass fuse display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_5_2_x_20_mm_glass_plugin_disposable_xucheng_elec_5f_2000210000r1'
MODEL = 'kicad_agents/display_model_xucheng_5f_2a.py'
MODEL_SHA = '3b41ebca6cd1f16749cad1e74af89d5bd4833812213e64243e1bedbe4279e65e'
PDF_SHA = 'eed9cc6991947ce18ab00afc8f4fb6e2f727c69e5cc3a9125ea6945fc8681681'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_XUCHENG_5F_2A_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('part_number_manufacturer') != '5F.2000210000R1'
        or record.get('dimensions_mm') != {'length': 20.0, 'width': 5.2, 'height': 6.5}
        or digest(source / 'datasheet.pdf') != PDF_SHA or digest(ROOT / MODEL) != MODEL_SHA):
        raise ValueError('Glass fuse identity, dimensions, model or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='5x20_glass_procedural', represented_manufacturer='Xucheng Electronics',
                  represented_mpn='5F.2000210000R1')
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [20., 5.2, 5.2], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'ceramic', 'termination']}
    recipe['marking'] = {'policy': 'unmarked_illustration', 'text': '', 'font_file': 'arialbd.ttf',
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Local Xucheng 5F 2 A manufacturer drawing, pages 1, 2 and 9',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Cap marking F2L250V and manufacturer/approval marks are documented but omitted in this display.'}
    recipe['appearance_status'] = ('Transparent hollow glass fuse with visible alloy element and nickel-coloured caps, '
        'nominal 20 x 5.2 mm drawing dimensions. Source height 6.5 mm exceeds drawing diameter maximum 5.4 mm. '
        'Cap lengths, glass wall, wire size and finish are illustrative; documented cap marking F2L250V is omitted. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
