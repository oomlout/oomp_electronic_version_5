"""Stage two SOT-23 family examples with uncertainty made explicit."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

REFERENCE = 'electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050'
SIBLING = 'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_220_milliamp_onsemi_bss138'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_SOT23_TRANSISTORS_RESEARCH.md')
PARTS = {
    'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_bss138':
        ('Generic (manufacturer unspecified)', 'BSS138 family', 'SS', 'Generic', {'length': 2.9, 'width': 2.4}, 'Package_TO_SOT_SMD:SOT-23'),
    'electronic_transistor_sot_23_bipolar_pnp_40_volt_600_milliamp_onsemi_mmbt4403':
        ('onsemi (inferred from ID)', 'MMBT4403 family', '2T', None, {'length': 2.9, 'width': 2.6}, ''),
}
SIBLING_SHA = 'd7ef8509e41f2def9147c14a68a0578155f7400c58e3b9514aad07524d6dd4dd'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    if hashlib.sha256((ROOT / 'parts_source' / SIBLING / 'datasheet.pdf').read_bytes()).hexdigest() != SIBLING_SHA:
        raise ValueError('Sibling onsemi BSS138 datasheet changed')
    for part, (represented, mpn, marking, manufacturer, dimensions, footprint) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != manufacturer or record.get('part_number_manufacturer') not in ('', None)
            or record.get('dimensions_mm') != dimensions or (record.get('kicad') or {}).get('machine_solder') != footprint
            or (source / 'datasheet.pdf').exists()):
            raise ValueError(f'{mpn}: source record or PDF availability changed')
        recipe = copy.deepcopy(recipes[REFERENCE])
        if (recipe['model']['sha256'] != 'dd5d1711204e1d8d26cd11490923bd84340820baa69538c385a4300ec2539bc0'
            or recipe['model'].get('display_scale_xyz') != [1., 1., .9166666666666666]):
            raise ValueError('Reviewed SOT-23 model changed')
        recipe.update(represented_manufacturer=represented, represented_mpn=mpn)
        note = ('SS is an illustrative onsemi BSS138 example; the generic part manufacturer and exact marking are unspecified.'
                if marking == 'SS' else '2T is an illustrative onsemi MMBT4403 family code; the exact orderable is unspecified and manufacturer is inferred from the ID.')
        recipe['marking'].update(policy='illustrative_literal', text=marking, evidence={'file': EVIDENCE.as_posix(),
            'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
            'document': f'{mpn} SOT-23 family package and illustrative marking review', 'source_record': f'parts_source/{part}/working.yaml'},
            appearance_status=note + ' Typeface, placement and variable production details are illustrative or omitted.')
        recipe['appearance_status'] = ('KiCad SOT-23 2.5 x 3.0 x 1.2 mm model is scaled vertically to 1.1 mm for display. This part has no separate local PDF. Manufacturer/orderable and marking limitations are stated above. Finish and fine details are illustrative; not manufacturing CAD or a footprint.')
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{mpn}: existing recipe differs')
        recipes[part] = recipe
        print(mpn, 'illustrative candidate; final review required')
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
