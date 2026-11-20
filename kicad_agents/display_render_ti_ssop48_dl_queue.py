"""Stage reviewed TI DL SSOP-48 candidates; preview and verify each separately."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TI_SSOP48_DL_EVIDENCE.md')
MODEL = 'Package_SO.3dshapes/SSOP-48_7.5x15.9mm_P0.635mm.step'
MODEL_SHA = '129539aee05b352d331d67c6ac685318c51f9aa84f66dfd2202e28b646d2eaad'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
CANDIDATES = {
    'electronic_ic_logic_16_bit_bus_buffer_tri_state_ssop_48_300mil_texas_instruments_sn74abt162244dlrg4': ('SN74ABT162244DLRG4', 'ABT162244'),
    'electronic_ic_logic_16_bit_bus_transceiver_tri_state_ssop_48_300mil_texas_instruments_sn74lvch16245adlr': ('SN74LVCH16245ADLR', 'LVCH16245A'),
    'electronic_ic_logic_16_bit_bus_transceiver_tri_state_ssop_48_300mil_texas_instruments_sn74lvth16245adlr': ('SN74LVTH16245ADLR', 'LVTH16245A'),
}


def candidate(part, record, recipes, evidence_sha):
    mpn, text = CANDIDATES[part]
    if (record.get('manufacturer') != 'Texas Instruments' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
            or (record.get('kicad') or {}).get('machine_solder') != ''):
        raise ValueError(f'{part}: source identity, dimensions or footprint changed; review again')
    result = copy.deepcopy(recipes[REFERENCE])
    if (result.get('family') != 'integrated_circuit'
            or result['model'].get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reference model roles changed')
    result['package'] = 'ssop_48_7_5x15_9mm'
    result['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[10.35, 15.9, 2.99], sha256=MODEL_SHA,
        role_by_source_colour={'0.148,0.145,0.145': 'coating', '0.824,0.820,0.781': 'termination', '0.691,0.664,0.598': 'pin_indicator'},
        required_roles=['coating', 'termination', 'pin_indicator'], display_scale_xyz=[1.0, 1.0, 2.7 / 2.99])
    result['represented_manufacturer'] = 'Texas Instruments'
    result['represented_mpn'] = mpn
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': text, 'font_file': 'arialbd.ttf',
        'rotation_degrees': 90, 'maximum_width_mm': 9.0, 'maximum_height_mm': 1.5,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
                     'document': 'Texas Instruments DL SSOP-48 package and marking review',
                     'source_record': f'parts_source/{part}/working.yaml'},
        'appearance_status': f'TI lists {text} as the device marking for {mpn}; typeface, placement, logo and variable manufacturing details are illustrative or omitted.',
    }
    result['appearance_status'] = ('TI identifies the orderable in the DL SSOP-48 package, approximately 15.88 x 10.35 mm overall. '
        'The KiCad model has 15.9 x 10.35 x 2.99 mm source bounds and 0.635 mm pitch. Its height is scaled to 2.70 mm for display because TI lists a 2.79 mm maximum. '
        'The catalogue lists 10 x 5 mm without specifying the measurement; that differs from TI overall package dimensions. '
        'Not a verified mechanical model or footprint.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=sorted(CANDIDATES))
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / args.part / 'working.yaml').read_text(encoding='utf8'))
    recipe = candidate(args.part, record, recipes, hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest())
    if args.part in recipes and recipes[args.part] != recipe:
        raise ValueError('Existing recipe differs; preserve and review it')
    if args.add and args.part not in recipes:
        recipes[args.part] = recipe
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
    print(args.part, 'candidate only; visual review required')


if __name__ == '__main__':
    main()
