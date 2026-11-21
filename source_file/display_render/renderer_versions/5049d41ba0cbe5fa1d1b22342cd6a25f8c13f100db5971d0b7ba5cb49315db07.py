"""Stage four MDD SMA Schottky illustrations from the reviewed family sheet."""
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

PREFIX = 'electronic_diode_schottky_sma_mdd_microdiode_semiconductor_'
PARTS = {PREFIX + x.lower(): x for x in ('SS210', 'SS34', 'SS54')}
MODEL_SHA = '1cfddd4e3b1bf22b8fc6ee3258c2aade882ed7b85b528e23b9db42437775a1db'
PDFS = {'SS210':'a456a883171824a32cec75ed39dae86d8a54b9a2c1774a4bc99262d3b05d3bae', 'SS34':'fb4970875779696914d235bcf954240569302fb325399838f2861d474cbf9760', 'SS54':'d90558a8db9d6ea0e8712c740ffea6d9c106544653faf724af75f1ab276dee66'}
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_SS235_SMA_RESEARCH.md')


def prepare(recipes):
    for mpn, expected in PDFS.items():
        if hashlib.sha256((ROOT / 'parts_source' / (PREFIX + mpn.lower()) / 'datasheet.pdf').read_bytes()).hexdigest() != expected:
            raise ValueError(f'{mpn}: reviewed PDF changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    result = {}
    for part, mpn in PARTS.items():
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'height': 2.3, 'length': 4.5, 'width': 2.8}
            or (record.get('kicad') or {}).get('machine_solder') != 'Diode_SMD:D_SMA'):
            raise ValueError(f'{mpn}: source record changed')
        recipe = copy.deepcopy(recipes[PILOT]); recipe['package'] = 'sma'; recipe['represented_manufacturer'] = 'MDD(Microdiode Semiconductor)'; recipe['represented_mpn'] = mpn
        recipe['model'].update(relative_path='Diode_SMD.3dshapes/D_SMA.step',
            source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Diode_SMD.3dshapes/D_SMA.step',
            sha256=MODEL_SHA, expected_bounds_mm=[5.0, 2.7, 2.22])
        recipe['marking'].update(text=mpn, maximum_width_mm=1.45, maximum_height_mm=.5, offset_x_mm=.45)
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': 'MDD SMA page 1 marking and outline', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{mpn} is the family table identifier with the MDD logo omitted; '
            'actual typeface, placement and production details are illustrative. Each part retains its own local PDF.')
        recipe['appearance_status'] = ('KiCad SMA model is 5.0 x 2.7 x 2.22 mm overall, with the cathode band on the pin-1 side. '
            'Its body is approximately 0.06 mm longer than the drawing maximum. Fine details are illustrative; not manufacturing CAD or a footprint.')
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
    print('Three SMA candidates; preview and independent pilot required')


if __name__ == '__main__': main()
