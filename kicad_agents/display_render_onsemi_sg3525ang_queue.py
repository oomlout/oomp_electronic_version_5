"""Stage a reviewed display-only onsemi SG3525ANG PDIP-16 candidate."""
import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_ti_dip16_pilot_queue import reviewed_recipe

PART = 'electronic_ic_power_management_pwm_controller_dip_16_onsemi_sg3525ang'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_ONSEMI_SG3525ANG_PDIP16_RESEARCH.md')


def candidate(record, recipes):
    if (record.get('manufacturer') != 'onsemi' or record.get('part_number_manufacturer') != 'SG3525ANG'
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
            or (record.get('kicad') or {}).get('machine_solder') != ''):
        raise ValueError('Source identity, dimensions or footprint changed; review again')
    # Reuse the already reviewed DIP model and material configuration; this
    # synthetic reference is solely an input to the TI recipe's own guards.
    reference_record = {'manufacturer': 'Texas Instruments', 'part_number_manufacturer': 'SN74HC138N',
                        'kicad': {'machine_solder': 'Package_DIP:DIP-16_W7.62mm'},
                        'dimensions_mm': {'height': 3.3, 'length': 21.3, 'width': 6.35}}
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    result = reviewed_recipe(reference_record, recipes, sha)
    result['represented_manufacturer'] = 'onsemi'
    result['represented_mpn'] = 'SG3525ANG'
    result['marking'] = {'policy': 'illustrative_literal', 'text': 'SG3525AN', 'font_file': 'arialbd.ttf',
        'rotation_degrees': 90, 'maximum_width_mm': 10.0, 'maximum_height_mm': 2.0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'onsemi SG3525A PDIP-16 review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('SG3525AN is the fixed marking shown in the manufacturer diagram. Typeface, orientation and placement are illustrative; variable assembly, lot and date codes are omitted. The diagram has not been visually confirmed.')}
    result['appearance_status'] = ('Generic KiCad DIP-16 model has 19.177 mm overall length and 6.98 mm overall height including projecting pins. Source 10 x 5 mm dimensions are generic and conflict with onsemi body range 18.80-19.55 x 6.35-6.85 mm. The manufacturer drawing was text-extracted but not visually confirmed. Display only, not a verified footprint or mechanical model.')
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
        raise ValueError('Existing recipe differs; preserve it and review')
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
