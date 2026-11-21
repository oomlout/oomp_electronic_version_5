"""Prepare evidence-backed SOT-363 transistor display candidates."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

REFERENCE = 'electronic_ic_logic_dual_schmitt_trigger_inverter_sot_363_nexperia_74lvc2g14gw_125'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SOT363_TRANSISTOR_RESEARCH.md')
MODEL_SHA = '045cc95e18ee7a13d1623c3ce6604fc833049bdb4f952f68c26e3c5767d122e4'
PARTS = {
    'electronic_transistor_sot_363_6_bipolar_pnp_dual_general_purpose_40_volt_200_milliamp_cbi_mmdt3906dw':
        ('CBI', 'MMDT3906DW', 'K3N', {'length': 2.1, 'width': 2.3}, '5304f7811d556f0192aaa78ec6d05a6de53b68ca7aab2131d1af46b2cec56693'),
    'electronic_transistor_sot_363_6_bipolar_pnp_dual_matched_pair_45_volt_100_milliamp_diodes_incorporated_bcm857bs_7_f':
        ('Diodes Incorporated', 'BCM857BS-7-F', 'M3W', {'length': 2.15, 'width': 2.1}, 'cb26f2ade2c320dae17ed6ea22b4ca7bee8550c04b490324150289c00c3336ff'),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    reference = recipes[REFERENCE]
    if reference['package'] != 'sot_363_sc70_6' or reference['model']['sha256'] != MODEL_SHA:
        raise ValueError('Reviewed SOT-363 reference changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part, (manufacturer, mpn, marking, dimensions, pdf_sha) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != manufacturer or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != dimensions or (record.get('kicad') or {}).get('machine_solder') != ''
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source or local datasheet changed')
        recipe = copy.deepcopy(reference)
        recipe.update(family='transistor', represented_manufacturer=manufacturer, represented_mpn=mpn)
        recipe['marking'].update(policy='verified_literal', text=marking, evidence={'file': EVIDENCE.as_posix(),
            'sha256': evidence_sha, 'document': f'{mpn} SOT-363 package and marking review',
            'source_record': f'parts_source/{part}/working.yaml'},
            appearance_status=f'The manufacturer specifies {marking}; typeface, placement and omitted variable production markings are illustrative.')
        if manufacturer == 'CBI':
            recipe['appearance_status'] = ('KiCad SOT-363 model has 2.1 x 2.0 x 1.1 mm overall bounds; its lead span is about 0.05 mm narrower than the drawing minimum. Finish and fine details are illustrative; not a manufacturing model or footprint.')
        else:
            recipe['model']['display_scale_xyz'] = [1.0, 1.0, 1.0 / 1.1]
            recipe['appearance_status'] = ('KiCad SOT-363 2.1 x 2.0 x 1.1 mm model is vertically scaled to 1.0 mm to match the manufacturer drawing. Finish and fine details are illustrative; not a manufacturing model or footprint.')
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
