"""Stage the reviewed display-only KiCad SOP-4 candidate for the LTV-217."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_ic_optocoupler_phototransistor_output_sop_4_175mil_lite_on_ltv_217_b_g'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_LITEON_LTV217_RESEARCH.md')
MODEL = 'Package_SO.3dshapes/SOP-4_4.4x2.6mm_P1.27mm.step'
MODEL_SHA = 'cb2b0da8eb9fdb76dbba2de2ff1cc50164623079ee56b75b8eef2c751591bff3'


def candidate(record, recipes):
    if (record.get('manufacturer') != 'Lite-On'
            or record.get('part_number_manufacturer') != 'LTV-217-B-G'
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
            or (record.get('kicad') or {}).get('machine_solder') != ''):
        raise ValueError('Source identity, generic dimensions or footprint changed; review again')
    ref = recipes[REFERENCE]
    if ref.get('family') != 'integrated_circuit' or ref['model'].get('required_roles') != ['coating', 'termination', 'pin_indicator']:
        raise ValueError('Reference material recipe changed')
    result = copy.deepcopy(ref)
    result['package'] = 'sop_4_4_4x2_6mm'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[7.0, 2.6, 2.1], sha256=MODEL_SHA,
        role_by_source_colour={'0.148,0.145,0.145': 'coating', '0.824,0.820,0.781': 'termination', '0.691,0.664,0.598': 'pin_indicator'},
        required_roles=['coating', 'termination', 'pin_indicator'])
    result['represented_manufacturer'] = 'Lite-On'
    result['represented_mpn'] = 'LTV-217-B-G'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'L217', 'font_file': 'arialbd.ttf',
        'rotation_degrees': 0, 'maximum_width_mm': 2.5, 'maximum_height_mm': 0.55,
        'offset_x_mm': 0.6,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                     'document': 'Lite-On LTV-217-G package and marking research',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('L217 is shown in the manufacturer drawing. Typeface, orientation and placement are illustrative; optional rank, date and other production markings are omitted. The KiCad indicator is illustrative and should not be interpreted as the manufacturer halogen-option mark.'),
    }
    result['appearance_status'] = ('KiCad SOP-4 display uses a 4.4 x 2.6 mm nominal body, 7.0 mm lead span and 2.1 mm overall height. Source 10 x 5 mm dimensions are generic. Manufacturer drawing dimensions have only been text-extracted, not visually confirmed; geometry and indicator are approximate and not a verified mechanical model or footprint.')
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
        raise ValueError('Existing recipe differs; preserve and review it')
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
    print(PART, 'candidate only; inspect preview before final')


if __name__ == '__main__':
    main()
