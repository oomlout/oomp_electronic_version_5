"""Stage the individually checked JSCJ D882 TO-126 display recipe."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_jscj_d882_to126 import MODEL, MODEL_SHA, PART

PILOT = 'electronic_transistor_to_220_mosfet_n_channel_enhancement_mode_100_volt_180_amp_infineon_technologies_irfb4110pbf'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_D882_TO126_RESEARCH.md')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != 'Jiangsu Changjing Electronics Technology Co., Ltd.'
        or record.get('part_number_manufacturer') != 'D882(RANGE:160-320)'
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-126-3_Vertical'
        or record.get('dimensions_mm') != {'length': 9.0, 'width': 4.5, 'height': 8.5}
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != '26329a5b3bcdc31a0e72464d65808051b97874c8767099a90f1701f2f6246e29'):
        raise ValueError('D882 identity, footprint, dimensions or source changed')
    result = copy.deepcopy(recipes[PILOT])
    result['package'] = 'to_126_3'
    result['model'].update(relative_path=MODEL, sha256=MODEL_SHA,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[8.0, 3.25, 23.75], required_roles=['coating', 'termination'],
        display_orientation='to220_face_up')
    result['model'].pop('role_by_source_colour', None)
    result['represented_manufacturer'] = record['manufacturer']
    result['represented_mpn'] = record['part_number_manufacturer']
    result['disable_bump_for'] = ['coating']
    result['marking'].update(policy='verified_literal', text='D882', maximum_width_mm=4.0,
        maximum_height_mm=1.0, offset_x_mm=-5.25,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
                  'document': 'JSCJ D882 TO-126 package and marking review',
                  'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='D882 is the manufacturer device code; typeface and placement are illustrative. Optional green dot and variable code are omitted.')
    result['appearance_status'] = ('KiCad TO-126 model has geometry-checked material regions and leads extended to 15.50 mm. '
        'Body is approximately 0.2 mm wider and 0.35 mm thicker than the drawing maxima; '
        'finish and details are approximate. Coating surface bump is omitted for renderer stability. '
        'Not verified manufacturing CAD or a footprint.')
    if PART in recipes and recipes[PART] != result:
        raise ValueError('Existing recipe differs')
    if args.add and PART not in recipes:
        recipes[PART] = result
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
