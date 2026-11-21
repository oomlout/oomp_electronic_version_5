"""Stage a display-only EPM1270 TQFP candidate after source checks."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_ic_cpld_cpld_1270_macrocells_tqfp_144_intel_altera_epm1270t144c5n'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INTEL_EPM1270_TQFP144_RESEARCH.md')
MODEL = 'Package_QFP.3dshapes/TQFP-144_20x20mm_P0.5mm.step'
MODEL_SHA = '04375074474c94e835558669f44d0989e234e983d3964161956a27bc675357d1'


def candidate(record, recipes):
    if (record.get('manufacturer') != 'Intel/Altera' or record.get('part_number_manufacturer') != 'EPM1270T144C5N'
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
            or (record.get('kicad') or {}).get('machine_solder') != ''):
        raise ValueError('Source identity, dimensions, drawing or footprint changed; review again')
    ref = recipes[REFERENCE]
    if ref.get('family') != 'integrated_circuit' or ref['model'].get('required_roles') != ['coating', 'termination', 'pin_indicator']:
        raise ValueError('Reference material recipe changed')
    result = copy.deepcopy(ref)
    result['package'] = 'tqfp_144_20x20mm'
    result['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[22.0, 22.0, 1.1], sha256=MODEL_SHA, display_scale_xyz=[1.0, 1.0, 1.4],
        role_by_source_colour={'0.148,0.145,0.145': 'coating', '0.824,0.820,0.781': 'termination', '0.691,0.664,0.598': 'pin_indicator'},
        required_roles=['coating', 'termination', 'pin_indicator'])
    result['represented_manufacturer'] = 'Intel/Altera'
    result['represented_mpn'] = 'EPM1270T144C5N'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'EPM1270T144C5N', 'font_file': 'arialbd.ttf',
        'rotation_degrees': 0, 'maximum_width_mm': 13.0, 'maximum_height_mm': 1.6,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                     'document': 'Altera MAX II TQFP-144 package research',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('EPM1270T144C5N is an illustrative identifier; exact physical marking is unverified. Typeface, orientation, placement and omitted logo and production codes are illustrative.'),
    }
    result['appearance_status'] = ('KiCad TQFP-144 display has 22 x 22 mm overall span. Its 1.10 mm source height is vertically scaled to 1.54 mm, giving 1.40 mm body thickness and 0.14 mm clearance; the catalogue 10 x 5 mm dimensions are generic. Altera drawing was not visually confirmed. Display is not a verified footprint or mechanical model.')
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
