"""Stage a drawing-based Xucheng 3 A glass fuse display candidate."""
import copy
import hashlib
from pathlib import Path

import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_5_2_x_20_mm_glass_plugin_disposable_xucheng_elec_5g_3000210000s1'
MODEL = 'kicad_agents/display_model_xucheng_5f_2a.py'
MODEL_SHA = 'dac41281c8d7891772b4e67951c55d31460d86fd996550c67078f2850dd775db'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_XUCHENG_5G_3A_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('part_number_manufacturer') != '5G.3000210000S1'
        or record.get('dimensions_mm') != {'length': 20.0, 'width': 5.2, 'height': 6.5}
        or digest(ROOT / MODEL) != MODEL_SHA):
        raise ValueError('Glass fuse identity, dimensions, model or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='5x20_glass_procedural', represented_manufacturer='Xucheng Electronics',
                  represented_mpn='5G.3000210000S1')
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination', 'pin_indicator']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [20., 5.2, 5.2], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'ceramic', 'termination', 'pin_indicator']}
    recipe['marking'] = {'policy': 'verified_literal', 'text': '5G3A 250V', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 3.5, 'maximum_height_mm': .8,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Xucheng exact 5G 3 A specification viewed online, pages 1 and 5',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Manufacturer cap marking 5G3A 250V; typeface and placement illustrative; logo and approval marks omitted.'}
    recipe['appearance_status'] = ('Transparent hollow glass fuse with visible alloy element and nickel-coloured caps, '
        'nominal 20 x 5.2 mm distributor dimensions. Source height 6.5 mm conflicts with the cylindrical diameter. '
        'Cap lengths, glass wall, wire size, finish and cap-mark placement are illustrative; logo and approval marks omitted. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe


def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()


if __name__ == '__main__':
    main()
