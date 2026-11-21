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

PARTS = {'electronic_diode_zener_sod_323_jiangsu_changjing_electronics_technology_co_ltd_mmsz5248bs': ('MMSZ5248BS', 'J3'), 'electronic_diode_zener_sod_323_jiangsu_changjing_electronics_technology_co_ltd_mmsz5250bs': ('MMSZ5250BS', 'J5'), 'electronic_diode_schottky_sod_323_jiangsu_changjing_electronics_technology_co_ltd_1ss404': ('1SS404', 'S51')}
MODEL_SHA = 'cd8619b2119cd95683a2c5e660ab4f2d4db674f696cd6f9e9756f221171a214d'
PDF_SHA = 'a39a67bd216e2bb869ae7fb71ee320adf8a0feec7421d7cb9ff0045c8981ed3a'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_OTHER_SOD323_RESEARCH.md')


def prepare(recipes):
    if hashlib.sha256((ROOT / 'parts_source' / 'electronic_diode_zener_sod_323_jiangsu_changjing_electronics_technology_co_ltd_mmsz5248bs' / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA:
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
            'document': 'JSCJ SOD-323 marking and source review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'JSCJ manufacturer evidence specifies {text}; typeface, placement and finish are illustrative. '
            'The available local PDFs are different-manufacturer JCST examples; MMSZ5250BS has no local PDF.')
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
    print('Three SOD-323 candidates; preview and final review required')


if __name__ == '__main__': main()
