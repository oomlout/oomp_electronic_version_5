"""Prepare two individually researched TO-3P display candidates."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

REFERENCE = 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_57_amp_infineon_technologies_irfp3710pbf'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_ONSEMI_TO3P_RESEARCH.md')
MODEL_SHA = '6b9dd6fdfcfb00909b04d9f132623ccee7612f9b4de9ee0bea3ac067713b9b59'
PARTS = {
    'electronic_transistor_to_3p_3_mosfet_n_channel_enhancement_mode_500_volt_28_4_amp_onsemi_fqa28n50':
        ('FQA28N50', 'FQA28N50', '9a86516a93ff64580fd3f4d2e81d7c3f464b752d96e1d5e90ee245f201a72a45', 16.5, -7.75),
    'electronic_transistor_to_3pn_mosfet_n_channel_enhancement_mode_900_volt_9_amp_onsemi_fqa9n90c_f109':
        ('FQA9N90C-F109', 'FQA9N90C', '382ad37b21678d0b1c1c8cfb0eb1f3c2bda741d9dc5562501118d871d36e3b63', 20.0, -9.5),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part, (mpn, marking, pdf_sha, length, offset) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != 'onsemi' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'height': 15.6, 'length': 15.9, 'width': 5.5}
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-3P-3_Vertical'
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source or local drawing changed')
        recipe = copy.deepcopy(recipes[REFERENCE])
        recipe.update(package='to_3p_3', represented_manufacturer='onsemi / Fairchild', represented_mpn=mpn)
        recipe['model'].update(relative_path='Package_TO_SOT_THT.3dshapes/TO-3P-3_Vertical.step',
            source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Package_TO_SOT_THT.3dshapes/TO-3P-3_Vertical.step',
            expected_bounds_mm=[15.51, 4.51, 40.7], sha256=MODEL_SHA, display_lead_length_mm=length)
        recipe['marking'].update(policy='illustrative_literal', text=marking, offset_x_mm=offset,
            evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
                'document': f'{mpn} Fairchild package and lead-length review', 'source_record': f'parts_source/{part}/working.yaml'},
            appearance_status=f'{marking} is an illustrative partial identifier; exact marking, typeface, logo, placement and variable production details are unverified.')
        variant_note = (' The local historical sheet calls this TO-3P, while a later onsemi family sheet says TO-3PN; the catalogue revision is uncertain.' if mpn == 'FQA28N50' else '')
        recipe['appearance_status'] = (f'KiCad TO-3P model is laid face-up with display-only leads adjusted from 20.7 mm to {length:.1f} mm below the body. Body and lead transitions are approximate; catalogue dimensions differ from the drawing.' + variant_note + ' Not a manufacturing model or footprint.')
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{mpn}: existing recipe differs')
        recipes[part] = recipe
        print(mpn, 'candidate; preview and final review required')
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
