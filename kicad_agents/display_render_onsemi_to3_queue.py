"""Prepare reviewed onsemi TO-3 metal-can display candidates."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_ONSEMI_TO3_RESEARCH.md')
REFERENCE = 'electronic_capacitor_8_mm_diameter_10_2_mm_tall_electrolytic_100_micro_farad_50_volt'
MODEL_SHA = '10d36da80a7f328482e27916f3044cc4bfec83922e402c41ed3552aa777116bb'
PARTS = {
    'electronic_transistor_to_204_bipolar_npn_250_volt_16_amp_onsemi_mj15024g': ('MJ15024G', '7b46afbdd8de68c25d2bca66cb5009a9396c5e460d5037da246b58605b51d1f6'),
    'electronic_transistor_to_204_bipolar_pnp_250_volt_16_amp_onsemi_mj15025g': ('MJ15025G', 'b7045e15a4b295363b37f0b3eaa01802ceac322d6c70a52c74c0a5f31baab46f'),
    'electronic_transistor_to_204_bipolar_pnp_140_volt_20_amp_onsemi_mj15004g': ('MJ15004G', '2139768db1f29730d031c4aa29eb942345c0c7c97fc85990a49dd40ac5d20f38'),
    'electronic_transistor_to_204_bipolar_npn_darlington_120_volt_50_amp_onsemi_mj11032g': ('MJ11032G', '3ae0782cde581a2000e515ec20b033c4c3da00a8d4ca725b071f6e327da1b6ff'),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    reference = recipes[REFERENCE]
    if reference.get('family') != 'aluminum_capacitor' or not reference.get('model', {}).get('metal_top_marking'):
        raise ValueError('Metal-top reference changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part, (mpn, pdf_sha) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != 'onsemi' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'height': 10.5, 'length': 26.0, 'width': 20.0}
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-3'
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source or datasheet changed')
        recipe = copy.deepcopy(reference)
        recipe.update(family='transistor_metal_can', package='to_204_to_3', represented_manufacturer='onsemi', represented_mpn=mpn)
        recipe['model'] = {'relative_path': 'Package_TO_SOT_THT.3dshapes/TO-3.step',
            'source_url': 'https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Package_TO_SOT_THT.3dshapes/TO-3.step',
            'copyright': 'KiCad library contributors', 'license': 'CC-BY-SA-4.0 with KiCad library exception; see original STEP header',
            'license_url': 'https://www.kicad.org/libraries/license/', 'expected_bounds_mm': [40.2, 27.2, 19.0],
            'dimension_tolerance_mm': .015, 'sha256': MODEL_SHA,
            'role_by_source_colour': {'0.506,0.506,0.506': 'termination', '0.859,0.738,0.496': 'termination'},
            'required_roles': ['termination', 'coating'], 'metal_top_marking': True}
        recipe['marking'] = {'policy': 'verified_literal', 'text': mpn, 'font_file': 'arialbd.ttf',
            'maximum_width_mm': 11.0, 'maximum_height_mm': 3.0,
            'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
                'document': f'{mpn} onsemi metal-can package and marking review', 'source_record': f'parts_source/{part}/working.yaml'},
            'appearance_status': 'The fixed device code and G suffix follow the manufacturer marking diagram; variable production details are omitted. Typeface, ink and placement are illustrative.'}
        recipe['appearance_status'] = ('KiCad TO-3 metal can has a 40.2 x 27.2 mm flange and 9.0 mm height above the seating plane, slightly oversized compared with the manufacturer drawing. The catalogue 26 x 20 x 10.5 mm dimensions use a different envelope. Finish and fine details are illustrative; not a manufacturing model or footprint.')
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{mpn}: existing recipe differs')
        recipes[part] = recipe
        print(mpn, 'candidate; preview and final image review required')
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


if __name__ == '__main__':
    main()
