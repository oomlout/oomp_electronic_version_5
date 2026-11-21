"""Prepare a drawing-reviewed IRLR120N display candidate; preview required."""
import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_st_l78m05_dpak_queue import reviewed_recipe

PART = 'electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_100_volt_10_amp_infineon_technologies_irlr120ntrpbf'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_IRLR120N_DPAK_RESEARCH.md')
PDF_SHA = '2677b70bc4ac977f2470ab2c036362530ff0051ac5ca631b6dbf2efcaaf3e0ac'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != 'Infineon Technologies'
        or record.get('part_number_manufacturer') != 'IRLR120NTRPBF'
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_SMD:TO-252-3_TabPin2'
        or record.get('dimensions_mm') != {'length': 6.5, 'width': 6.1, 'height': 2.3}):
        raise ValueError('Part identity or dimensions changed; review again')
    if hashlib.sha256((ROOT / 'parts_source' / PART / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA:
        raise ValueError('Drawing changed; review again')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    reference_record = {'manufacturer': 'STMicroelectronics', 'part_number_manufacturer': 'L78M05ABDT-TR',
                        'kicad': {'machine_solder': ''}, 'dimensions_mm': {'length': 10.0, 'width': 5.0}}
    recipe = reviewed_recipe(reference_record, recipes, evidence_sha)
    recipe['family'] = 'transistor'
    recipe['represented_manufacturer'] = 'Infineon Technologies'
    recipe['represented_mpn'] = 'IRLR120NTRPBF'
    recipe['marking']['text'] = 'IRLR120N'
    recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
        'document': 'IRLR120N DPAK drawing and display review', 'source_record': f'parts_source/{PART}/working.yaml'}
    recipe['marking']['appearance_status'] = ('IRLR120N is an illustrative partial identifier; exact top marking, '
        'typeface, placement and variable production details are unverified. The drawing example is a different device.')
    recipe['appearance_status'] = ('The KiCad TO-252-2 display model approximates the drawing with two full leads, '
        'a short centre stub and a metal tab; its overall bounds are 9.9 x 6.5 x 2.32 mm. The catalogue footprint '
        'remains TO-252-3_TabPin2. Stub dimensions, finish and marking are approximate; not a manufacturing model.')
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; preserve it and review manually')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        updated = (json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8')
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name)
                f.write(updated)
                f.flush()
                os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original:
                raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists():
                temp.unlink()
    print(PART, recipe['represented_mpn'], 'candidate only; preview review required')


if __name__ == '__main__':
    main()
