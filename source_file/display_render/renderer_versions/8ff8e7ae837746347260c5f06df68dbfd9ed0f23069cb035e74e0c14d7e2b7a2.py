"""Stage two independently evidenced JSCJ SOD-323 zener illustrations."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_jscj_bzt52_sod123_composite import PILOT

PREFIX = 'electronic_diode_zener_sod_323_jiangsu_changjing_electronics_technology_co_ltd_'
PARTS = {PREFIX + 'bzt52c18s': ('BZT52C18S', 'WL'), PREFIX + 'bzt52c5v1s_w8': ('BZT52C5V1S W8', 'W8')}
MODEL_SHA = 'cd8619b2119cd95683a2c5e660ab4f2d4db674f696cd6f9e9756f221171a214d'
PDF_SHA = 'b2de1300cc5939db2acde3f2de8e768cf7dd853d179d60e14bf4bf44781c7817'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_BZT52_SOD323_RESEARCH.md')


def prepare(recipes):
    if hashlib.sha256((ROOT / 'parts_source' / (PREFIX + 'bzt52c18s') / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA:
        raise ValueError('Local JCST example changed')
    digest = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    result = {}
    for part, (mpn, text) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'Jiangsu Changjing Electronics Technology Co., Ltd.'
            or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
            or (record.get('kicad') or {}).get('machine_solder') != 'Diode_SMD:D_SOD-323'):
            raise ValueError(f'{mpn}: source identity or footprint changed')
        recipe = copy.deepcopy(recipes[PILOT]); recipe['package'] = 'sod_323'; recipe['represented_mpn'] = mpn
        recipe['model'].update(relative_path='Diode_SMD.3dshapes/D_SOD-323.step',
            source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Diode_SMD.3dshapes/D_SOD-323.step',
            sha256=MODEL_SHA, expected_bounds_mm=[2.5, 1.25, 1.11])
        recipe['marking'].update(text=text, maximum_width_mm=.55, maximum_height_mm=.3, offset_x_mm=.20)
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': digest,
            'document': 'JSCJ BZT52 SOD-323 family marking and source review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'JSCJ family table specifies {text}; typeface, placement and finish are illustrative. '
            'The local PDF is a different-manufacturer JCST example; the second entry has no local PDF.')
        if mpn.endswith(' W8'):
            recipe['marking']['appearance_status'] += ' W8 matches the marking; whether it is an orderable suffix is unverified.'
        recipe['appearance_status'] = ('KiCad SOD-323 display model is 2.5 x 1.25 x 1.11 mm overall with cathode stripe on the pin-1 side. '
            'Its dimensions have not been verified against the manufacturer drawing. Source 10 x 5 mm dimensions appear to be placeholders. '
            'Fine details are illustrative; not manufacturing CAD or a footprint.')
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--add', action='store_true'); args = parser.parse_args()
    original = RECIPE_FILE.read_bytes(); recipes = json.loads(original.decode('utf8')); candidates = prepare(recipes)
    for part, recipe in candidates.items():
        if part in recipes and recipes[part] != recipe: raise ValueError(f'{part}: existing recipe differs')
        recipes[part] = recipe
    if args.add:
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name); f.write((json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8')); f.flush(); os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists(): temp.unlink()
    print('Two SOD-323 candidates; preview and final review required')


if __name__ == '__main__': main()
