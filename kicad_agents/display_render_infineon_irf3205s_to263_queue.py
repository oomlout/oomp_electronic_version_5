"""Prepare the individually researched IRF3205S D2PAK display candidate."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_infineon_irf3205s_to263 import PART, MODEL, MODEL_SHA

PILOT = 'electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_55_volt_42_amp_infineon_technologies_irlr2905trpbf'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TO263_MODEL_RESEARCH.md')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != 'Infineon Technologies'
        or record.get('part_number_manufacturer') != 'IRF3205STRLPBF'
        or record.get('dimensions_mm') != {'height': 4.6, 'length': 10.0, 'width': 9.2}
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_SMD:TO-263-3_TabPin2'
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != '65ae69363cbeb25c807523218c9667ddda9657b3692fdb9c1661d17a470ae7b5'):
        raise ValueError('IRF3205S source identity or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe['package'] = 'to_263_3_d2pak'
    recipe['model'].update(relative_path=MODEL, sha256=MODEL_SHA,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[15.0, 10.0, 4.42], required_roles=['coating', 'termination'])
    recipe['represented_mpn'] = 'IRF3205STRLPBF'
    recipe['marking'].update(text='IRF3205S', maximum_width_mm=6.5, maximum_height_mm=1.25,
        offset_x_mm=3.75,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                  'document': 'IRF3205S D2PAK package and display research',
                  'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='IRF3205S is an illustrative partial identifier; exact top marking, typeface, placement and production codes are unverified. The drawing example shows another part.')
    recipe['appearance_status'] = ('The KiCad TO-263 model is adapted for display by trimming its centre lead to an approximate 0.5 mm external stub. '
        'Its body and overall dimensions fit the reviewed drawing; stub shape, finish and details are approximate. Not verified manufacturing CAD or a footprint.')
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
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
    print(PART, 'candidate only; preview and final image review required')


if __name__ == '__main__':
    main()
