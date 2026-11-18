"""Prepare one sourced illustration without changing a generic part's procurement."""
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_220_micro_farad_10_volt'
PILOT = 'electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_100_micro_farad_25_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RVT_6_3MM_GENERIC_220UF_EVIDENCE.md')

def reviewed_recipe(record, recipes, sha):
    if (record.get('name_proper') != 'Capacitor 220 uF 10 V Electrolytic 6.3 mm diameter x 7.7 mm tall'
        or record.get('dimensions_mm') != {'length': 6.3, 'width': 6.3}
        or record.get('lcsc_research_status') != 'rejected'
        or record.get('manufacturers') != [] or record.get('distributors') != []
        or record.get('kicad', {}).get('machine_solder') != ''):
        raise ValueError('Generic part identity or procurement state changed; review again')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('package') != 'electrolytic_smd_6_3x7_7' or not r['model'].get('metal_top_marking'):
        raise ValueError('Reviewed example geometry changed')
    r['represented_mpn'] = 'RVT1A221M0607'
    r['marking']['text'] = '220\n10V'
    r['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Honor RVT specification and individual LCSC/JLCPCB listings',
        'source_record': f'parts_source/{PART}/working.yaml'}
    r['appearance_status'] = ('Illustrative Honor example for a generic record without a selected supplier; this does not alter procurement status. KiCad polarized can, negative sector, finish and marking layout are illustrative. Marking is composited from shared material passes; indirect reflections are approximate.')
    return r

def main():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    if PART in recipes: raise ValueError('Existing recipe is preserved')
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipes[PART] = reviewed_recipe(record, recipes, sha)
    RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print('Prepared illustrative recipe; procurement record unchanged')

if __name__ == '__main__':
    main()
