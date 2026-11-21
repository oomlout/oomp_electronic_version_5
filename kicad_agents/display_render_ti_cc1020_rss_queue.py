"""Stage a display-only CC1020 QFN candidate after source checks."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_ic_rf_sub_ghz_rf_transceiver_qfn_32_ep_texas_instruments_cc1020rssr'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TI_CC1020_RSS_RESEARCH.md')
MODEL = 'Package_DFN_QFN.3dshapes/QFN-32-1EP_7x7mm_P0.65mm_EP5.46x5.46mm.step'
MODEL_SHA = 'f8cb3647a783167910c468bc09d5de74223779876388b796a66718dc82b11a1a'


def candidate(record, recipes):
    if (record.get('manufacturer') != 'Texas Instruments' or record.get('part_number_manufacturer') != 'CC1020RSSR'
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
            or (record.get('kicad') or {}).get('machine_solder') != ''):
        raise ValueError('Source identity, dimensions, drawing or footprint changed; review again')
    ref = recipes[REFERENCE]
    if ref.get('family') != 'integrated_circuit' or ref['model'].get('required_roles') != ['coating', 'termination', 'pin_indicator']:
        raise ValueError('Reference material recipe changed')
    result = copy.deepcopy(ref)
    result['package'] = 'qfn_32_7x7mm_1ep'
    result['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[7.0, 7.0, 0.87], sha256=MODEL_SHA,
        role_by_source_colour={'0.148,0.145,0.145': 'coating', '0.824,0.820,0.781': 'termination', '0.691,0.664,0.598': 'pin_indicator'},
        required_roles=['coating', 'termination', 'pin_indicator'])
    result['represented_manufacturer'] = 'Texas Instruments'
    result['represented_mpn'] = 'CC1020RSSR'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'CC1020', 'font_file': 'arialbd.ttf',
        'rotation_degrees': 0, 'maximum_width_mm': 3.1, 'maximum_height_mm': 0.9,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                     'document': 'TI CC1020 RSS package research',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('TI lists CC1020 as the device marking. Typeface, orientation, placement and omitted logo and production codes are illustrative.'),
    }
    result['appearance_status'] = ('KiCad QFN-32 display has 7 x 7 x 0.87 mm bounds; source 10 x 5 mm dimensions are generic. Its measured 4.70 mm thermal pad is resized to 4.28 mm by a guarded display adapter; the scaled chamfer is approximate. The TI drawing was not visually confirmed. Display is not a verified footprint or mechanical model.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipe = candidate(record, recipes)
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; preserve and review')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as handle:
                temp = Path(handle.name)
                handle.write((json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8'))
                handle.flush()
                os.fsync(handle.fileno())
            if RECIPE_FILE.read_bytes() != original:
                raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists():
                temp.unlink()
    print(PART, 'candidate only; preview review required')


if __name__ == '__main__':
    main()
