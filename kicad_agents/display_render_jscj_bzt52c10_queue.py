"""Stage the reviewed JSCJ BZT52C10 SOD-123 display candidate."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10'
REFERENCE = 'electronic_ic_amplifier_operational_amplifier_dual_low_noise_soic_8_texas_instruments_ne5532dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_BZT52C10_RESEARCH.md')
MODEL_SHA = 'b3dc4065573abc72e3d5b4cca0e908f72a24205a41b6284b1f75ccacbe99adf8'
PDF_SHA = 'fd5a910fc58737806f1596a6318cecd1e1264061e3ca7c6c7f13e69667e36ab5'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != 'Jiangsu Changjing Electronics Technology Co., Ltd.'
        or record.get('part_number_manufacturer') != 'BZT52C10'
        or record.get('dimensions_mm') != {'height': 1.1, 'length': 1.6, 'width': 1.25}
        or (record.get('kicad') or {}).get('machine_solder') != 'Diode_SMD:D_SOD-123'
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA):
        raise ValueError('BZT52C10 source record or local datasheet changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if recipe['family'] != 'integrated_circuit':
        raise ValueError('Reviewed material reference changed')
    recipe.update(family='diode', package='sod_123',
        represented_manufacturer='Jiangsu Changjing Electronics Technology Co., Ltd.', represented_mpn='BZT52C10')
    recipe['model'].update(relative_path='Diode_SMD.3dshapes/D_SOD-123.step',
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Diode_SMD.3dshapes/D_SOD-123.step',
        expected_bounds_mm=[3.8, 1.6, 1.26], sha256=MODEL_SHA)
    recipe['marking'] = {'policy': 'verified_literal', 'text': 'WF', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': .8, 'maximum_height_mm': .45, 'offset_x_mm': .25,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
            'document': 'JSCJ BZT52C10 SOD-123 code, cathode band and package review', 'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'JSCJ specifies WF and a cathode bar; the optional green-moulding dot is omitted. Typeface, placement and finish are illustrative.'}
    recipe['appearance_status'] = ('KiCad SOD-123 model is 3.8 x 1.6 x 1.26 mm overall; the cathode band is on the pin-1 side. Its height exceeds the local drawing maximum by about 0.01 mm; source dimensions use a different envelope. Fine details are illustrative; not manufacturing CAD or a footprint.')
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
    print('BZT52C10 candidate; preview and final review required')


if __name__ == '__main__':
    main()
