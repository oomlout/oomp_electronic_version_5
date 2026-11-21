"""Stage a display-only SLB9665 family QFN candidate after source checks."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_ic_trusted_platform_module_trusted_platform_module_qfn_32_5_mm_x_5_mm_infineon_slb9665'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_SLB9665_QFN_RESEARCH.md')
MODEL = 'Package_DFN_QFN.3dshapes/QFN-32-1EP_5x5mm_P0.5mm_EP3.7x3.7mm.step'
MODEL_SHA = '7e77a52b3e261a45529e0df739376ea7cd79204fb1afad81332a50f4f1607000'


def candidate(record, recipes):
    drawing = record.get('package_drawing') or {}
    if (record.get('manufacturer') not in (None, '') or record.get('part_number_manufacturer') not in (None, '')
            or record.get('dimensions_mm') != {'length': 5.0, 'width': 5.0, 'height': 0.9}
            or len(drawing.get('pins', [])) != 32 or drawing.get('boxes') != [[0, 0, 2.1, 2.1]]
            or (record.get('kicad') or {}).get('machine_solder') != ''):
        raise ValueError('Source identity, dimensions, drawing or footprint changed; review again')
    ref = recipes[REFERENCE]
    if ref.get('family') != 'integrated_circuit' or ref['model'].get('required_roles') != ['coating', 'termination', 'pin_indicator']:
        raise ValueError('Reference material recipe changed')
    result = copy.deepcopy(ref)
    result['package'] = 'qfn_32_5x5mm_1ep'
    result['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[5.0, 5.0, 0.85], sha256=MODEL_SHA,
        role_by_source_colour={'0.148,0.145,0.145': 'coating', '0.824,0.820,0.781': 'termination', '0.691,0.664,0.598': 'pin_indicator'},
        required_roles=['coating', 'termination', 'pin_indicator'])
    result['represented_manufacturer'] = 'Infineon (inferred from catalogue ID)'
    result['represented_mpn'] = 'SLB9665 family (exact variant unspecified; inferred from catalogue ID)'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'SLB9665', 'font_file': 'arialbd.ttf',
        'rotation_degrees': 0, 'maximum_width_mm': 3.1, 'maximum_height_mm': 0.7,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                     'document': 'Infineon SLB9665 family package and marking review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('SLB9665 is an illustrative family marking. Exact variant, firmware, production codes and logo are omitted; typeface, layout and orientation are illustrative.'),
    }
    result['appearance_status'] = ('Infineon SLB9665 family identity is inferred from the catalogue ID; exact variant is unspecified. KiCad display has 5 x 5 mm body, 0.85 mm height, 0.5 mm pitch and 3.7 mm exposed pad. The source drawing uses 0.625 mm pitch and a 2.1 mm centre box; the manufacturer recommends a 3.6 mm PCB land. Manufacturer drawing was not visually confirmed. Display is not a verified footprint or mechanical model.')
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
