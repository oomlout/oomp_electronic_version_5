"""Stage MDD 1N400x bent-lead display candidates from reviewed sources."""
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

PREFIX = 'electronic_diode_rectifier_do_41_mdd_microdiode_semiconductor_'
PARTS = {PREFIX + x.lower(): x for x in ('1N4001', '1N4004', '1N4007G')}
MODEL_SHA = 'c3e23d4b276811b74eecb329bd4480209ad3dbc8cf6e6e3f2a5b542c5ca343c1'
PDF_SHA = 'ffae0d09201187997d60c8ad051b739b5ebc3db20a46b13fbceb860d1db8e22a'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_1N400X_AXIAL_RESEARCH.md')


def prepare(recipes):
    if hashlib.sha256((ROOT / 'parts_source' / (PREFIX + '1n4001') / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA:
        raise ValueError('Local MDD 1N400x PDF changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(); result = {}
    for part, mpn in PARTS.items():
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'height': 4.0, 'length': 5.2, 'width': 2.7}
            or (record.get('kicad') or {}).get('machine_solder') != 'Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal'):
            raise ValueError(f'{mpn}: source record changed')
        recipe = copy.deepcopy(recipes[PILOT]); recipe['package'] = 'do_41_bent'; recipe['represented_manufacturer'] = 'MDD(Microdiode Semiconductor)'; recipe['represented_mpn'] = mpn
        recipe['model'].update(relative_path='Diode_THT.3dshapes/D_DO-41_SOD81_P10.16mm_Horizontal.step',
            source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Diode_THT.3dshapes/D_DO-41_SOD81_P10.16mm_Horizontal.step',
            copyright='2017 kicad StepUp', sha256=MODEL_SHA, expected_bounds_mm=[10.96, 2.72, 5.71],
            role_by_source_colour={'0.895,0.891,0.813': 'pin_indicator', '0.148,0.145,0.145': 'coating', '0.824,0.820,0.781': 'termination'})
        recipe['marking'].update(text=mpn, maximum_width_mm=2.1, maximum_height_mm=.6, offset_x_mm=.85)
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': 'MDD 1N400x family marking and axial package review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{mpn} is an illustrative partial identifier from MDD family markings; '
            'the MDD logo and production details are omitted. Typeface, placement and stripe width are illustrative.')
        recipe['appearance_status'] = ('KiCad DO-41 model has bent leads at 10.16 mm pitch; the manufacturer drawing shows straight leads. '
            'Its approximately 0.80 mm lead diameter exceeds the 0.65 mm drawing maximum by 0.15 mm. '
            'The source drawing for non-G versions calls the package A-405. Display illustration only; not manufacturing CAD or a footprint.')
        if mpn != '1N4001': recipe['marking']['appearance_status'] += ' No local PDF is stored for this entry; see family evidence.'
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
    print('Three 1N400x candidates; marked preview and geometry review required')


if __name__ == '__main__': main()
