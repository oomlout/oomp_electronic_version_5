"""Prepare the reviewed CBI BC2301T-2.8A procedural display candidate."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a'
REFERENCE = 'electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050'
MODEL = 'kicad_agents/display_model_cbi_sot523.py'
MODEL_SHA = '697336e8fc26d059868948dfedb951c37e413b06bf3a8495ea4223f99ab82581'
PDF_SHA = '1163554d7e6b7dd9726fffd70229da61541ba21ef30fc341bdc743d1cbf7a119'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_CBI_BC2301T_SOT523_RESEARCH.md')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != 'CBI' or record.get('part_number_manufacturer') != 'BC2301T-2.8A'
        or record.get('dimensions_mm') != {'length': 1.6, 'width': 1.6}
        or (record.get('kicad') or {}).get('machine_solder') != ''
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA
        or hashlib.sha256((ROOT / MODEL).read_bytes()).hexdigest() != MODEL_SHA):
        raise ValueError('Source record, evidence or procedural model changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if recipe['package'] != 'sot_23_3':
        raise ValueError('Reviewed transistor material reference changed')
    recipe.update(family='transistor', package='sot_523', represented_manufacturer='CBI', represented_mpn='BC2301T-2.8A')
    recipe['model'] = {'relative_path': MODEL,
        'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [1.6, 1.6, .7], 'dimension_tolerance_mm': .015,
        'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination']}
    recipe['marking'].update(policy='verified_literal', text='2301', maximum_width_mm=.8, maximum_height_mm=.3,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
            'document': 'CBI BC2301T-2.8A SOT-523 drawing and marking review', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='CBI specifies 2301; exact typeface, size, position and additional production markings are illustrative.')
    recipe['appearance_status'] = ('Procedural SOT-523 display geometry follows nominal dimensions from the manufacturer drawing: 1.6 mm body length, 1.6 mm overall width and 0.7 mm height. Lead bends, bevels and finish are illustrative; not manufacturing CAD or a PCB footprint.')
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs')
    recipes[PART] = recipe
    if args.add:
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name)
                f.write((json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8'))
                f.flush()
                os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original:
                raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists():
                temp.unlink()
    print('BC2301T-2.8A candidate; preview and final review required')


if __name__ == '__main__':
    main()
