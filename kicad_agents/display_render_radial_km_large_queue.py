"""Stage four individually reviewed large Chengx KM radial illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

REFERENCE = 'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_100_micro_farad_50_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_KM_LARGE_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_16_mm_diameter_25_mm_tall_electrolytic_2200_micro_farad_35_volt':
        ('KM228M035K25RR0VH2FP0', 'C2763', '2200 uF', '35 V', 16., 25., '2200uF\n35V\nKM 105C'),
    'electronic_capacitor_16_mm_diameter_25_mm_tall_electrolytic_47_micro_farad_450_volt':
        ('KM476M450K25RR0VH2FP0', 'C2746', '47 uF', '450 V', 16., 25., '47uF\n450V\nKM 105C'),
    'electronic_capacitor_18_mm_diameter_30_mm_tall_electrolytic_100_micro_farad_400_volt':
        ('KM107M400L30RR0VH2FP0', 'C2767', '100 uF', '400 V', 18., 30., '100uF\n400V\nKM 105C'),
    'electronic_capacitor_18_mm_diameter_30_mm_tall_electrolytic_6800_micro_farad_25_volt':
        ('KM688M025L30RR0VH2FP0', 'C2754', '6800 uF', '25 V', 18., 30., '6800uF\n25V\nKM 105C'),
}
MODELS = {
    16.: ('Capacitor_THT.3dshapes/CP_Radial_D16.0mm_P7.50mm.step',
          '6ff24b1ad7161c52fa605740f3e2cf292a57964021404ee4b828c6577e1ba561', 15.8, 9.),
    18.: ('Capacitor_THT.3dshapes/CP_Radial_D18.0mm_P7.50mm.step',
          'ae2d8bf5ddd7b73271c87f1ad63a3849077d694adcf3577672131e4ba0364c02', 17.8, 12.),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed large KM part')
    mpn, supplier, value, voltage, diameter, height, text = PARTS[part]
    e = record.get('electrical') or {}
    footprint = f'Capacitor_THT:CP_Radial_D{diameter:.1f}mm_P7.50mm'
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != mpn or record.get('part_number_lcsc') != supplier
        or e.get('capacitance') != value or e.get('rated_voltage') != voltage
        or e.get('pin_spacing') != '7.5 mm' or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': diameter, 'width': diameter, 'height': height}
        or record.get('kicad', {}).get('machine_solder') != footprint):
        raise ValueError('Identity, rating, dimensions or polarity changed')
    result = copy.deepcopy(recipes[REFERENCE])
    if result.get('family') != 'radial_aluminum_capacitor':
        raise ValueError('Reference family changed')
    model, digest, top, extra = MODELS[diameter]
    result['package'] = f'radial_{int(diameter)}x{int(height)}_pitch7_5'
    result['model'].update(relative_path=model,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + model,
        expected_bounds_mm=[diameter, diameter, diameter+2.], sha256=digest,
        radial_stretch={'lower_z': 2.13502085691, 'upper_z': top, 'extra_height': extra,
                        'center_xy': [3.75, 0.], 'radius': diameter/2, 'tolerance': .05})
    result['represented_mpn'] = mpn
    result['marking'].update(text=text, maximum_width_mm=diameter*.60, maximum_height_mm=height*.30,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha,
                  'document': 'Individual LCSC listing and Chengx KM/code specifications',
                  'source_record': f'parts_source/{part}/working.yaml'},
        appearance_status='Value, voltage and series text are illustrative; exact typography and production artwork are unverified.')
    result['appearance_status'] = (f'Illustrative KiCad radial model with the straight sleeve extended to {height:g} mm, leaving ends and leads unchanged. The black sleeve and white printing follow the manufacturer code; stripe, shades and finish are illustrative. Supplier temperature information conflicts with the source record.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part in PARTS:
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, record, recipes, sha)
        if part in recipes and recipes[part] != recipe:
            raise ValueError('Existing recipe differs; review manually')
        if args.add:
            recipes[part] = recipe
        print(part, recipe['represented_mpn'])
    if args.add:
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
