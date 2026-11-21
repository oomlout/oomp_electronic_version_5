"""Stage a reviewed IRFU220N TO-251 display candidate."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_200_volt_5_amp_infineon_technologies_irfu220npbf'
PILOT = 'electronic_transistor_to_220_mosfet_n_channel_enhancement_mode_100_volt_180_amp_infineon_technologies_irfb4110pbf'
MODEL = 'Package_TO_SOT_THT.3dshapes/TO-251-3_Vertical.step'
MODEL_SHA = '7bb694d087837f077086c278225d603d812ff6a7a8af1db64601db91de627c55'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_IRFU220N_TO251_RESEARCH.md')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != 'Infineon Technologies' or record.get('part_number_manufacturer') != 'IRFU220NPBF'
        or record.get('dimensions_mm') != {'length': 6.6, 'width': 6.2, 'height': 2.5}
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-251-3_Vertical'
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != '7b8b6e32281bb5b9d3dfde103740646d3ca80293b6efbe9e0f637b920e5af154'):
        raise ValueError('IRFU220N source or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe['package'] = 'to_251_3_ipak'
    recipe['model'].update(relative_path=MODEL, sha256=MODEL_SHA,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[6.575, 2.31, 16.26], required_roles=['coating', 'termination'],
        role_by_source_colour={'0.148,0.145,0.145': 'coating', '0.824,0.820,0.781': 'termination'},
        display_orientation='to220_face_up')
    recipe['represented_mpn'] = 'IRFU220NPBF'
    recipe['marking'].update(policy='illustrative_literal', text='IRFU220N', maximum_width_mm=4.0,
        maximum_height_mm=.8, offset_x_mm=-4.78,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                  'document': 'IRFU220N TO-251 package review', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='IRFU220N is an illustrative partial identifier; exact top marking, typeface, logo and production codes are unverified. The drawing example shows another part.')
    recipe['appearance_status'] = ('The KiCad TO-251 model is laid face-up, with three full leads approximately 9.56 mm long. '
        'Its main dimensions fit the reviewed drawing; finish and fine details are approximate. Not verified manufacturing CAD or a footprint.')
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
