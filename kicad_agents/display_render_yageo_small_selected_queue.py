"""Prepare explicit, unmarked Yageo visual references for selected small parts."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_SMALL_SELECTED_REFERENCES.md')
# size, selected manufacturer, selected MPN, LCSC, reference, tolerance, required selected-listing text
PARTS = {
 'electronic_resistor_0201_10000000_ohm': ('0201','FH','RHC-01U106JT','C2991657','RC0201JR-0710ML','5%','10MΩ'),
 'electronic_resistor_0402_10000000_ohm': ('0402','HWA CHN','HRC0402F1005DNTO','C54920615','RC0402FR-0710ML','1%','10MΩ'),
 'electronic_resistor_0402_150000_ohm_5_percent': ('0402','FH (Guangdong Fenghua Advanced Tech)','RS-02K154JT','C1166','RC0402JR-07150KL','5%',None),
}


def reviewed_recipe(part, record, recipes, evidence_hash):
 if part not in PARTS: raise ValueError('No reviewed reference for this part')
 size, manufacturer, selected, lcsc, reference, tolerance, value = PARTS[part]
 if record.get('manufacturer') != manufacturer or record.get('part_number_manufacturer') != selected: raise ValueError('Selected identity changed')
 if not any(x.get('manufacturer') == manufacturer and x.get('part_number') == selected for x in record.get('manufacturers',[]) if isinstance(x,dict)): raise ValueError('Manufacturer entry changed')
 selected_listing = next((x for x in record.get('distributors',[]) if isinstance(x,dict) and x.get('key') == 'lcsc' and x.get('part_number') == lcsc),None)
 if not selected_listing: raise ValueError('Selected listing changed')
 if value and (value not in str(selected_listing.get('product_name','')) or tolerance not in str(selected_listing.get('product_name',''))): raise ValueError('Selected listing value or tolerance changed')
 pattern = r'(?<![0-9.])' + tolerance[0] + r'(?:\.0+)?\s*%'
 ratings = ((record.get('electrical') or {}).get('tolerance'),((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance'))
 if any(r and not re.search(pattern,str(r)) for r in ratings): raise ValueError('Tolerance conflict')
 if value is None and not all(r and re.search(pattern,str(r)) for r in ratings): raise ValueError('Expected independent recorded tolerances')
 if value is None and ('150 kOhm' not in str((record.get('electrical') or {}).get('resistance','')) or '150kΩ' not in str(((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Resistance',''))): raise ValueError('Recorded value changed')
 metric = {'0201':'0603','0402':'1005'}[size]
 if record.get('kicad',{}).get('machine_solder') != f'Resistor_SMD:R_{size}_{metric}Metric': raise ValueError('Footprint mismatch')
 template = {'0201':'electronic_resistor_0201_2700_ohm','0402':'electronic_resistor_0402_1000_ohm'}[size]
 recipe=copy.deepcopy(recipes[template])
 if recipe.get('family') != 'chip_resistor' or recipe.get('package') != size+'_imperial' or recipe.get('marking',{}).get('policy') != 'none': raise ValueError('Unexpected reference geometry')
 recipe.update(represented_manufacturer='YAGEO',represented_mpn=reference)
 recipe['marking']={'policy':'none','evidence':{'file':EVIDENCE.as_posix(),'sha256':evidence_hash,'document':'Yageo RC_L manufacturer specification and exact reference specifications (reviewed online)','source_record':f'parts_source/{part}/working.yaml','rule':f'Yageo {reference} is an unmarked {size} reference of the same nominal value and {tolerance} tolerance.'},'appearance_status':f'Yageo RC{size} bodies are unmarked.'}
 recipe['appearance_status']=(f'Illustrates Yageo {reference}; the selected {manufacturer} {selected} appearance is unverified. Same nominal value and tolerance do not establish full interchangeability. Generic KiCad geometry and materials are illustrative.')
 return recipe


def discover():
 recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
 sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest()
 return {p:reviewed_recipe(p,yaml.safe_load((ROOT/'parts_source'/p/'working.yaml').read_text(encoding='utf8')) or {},recipes,sha) for p in PARTS if p not in recipes and (ROOT/'parts'/p/'working.yaml').is_file()}


def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();found=discover()
 if args.add:
  recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
  if any(p in recipes for p in found):raise ValueError('Existing recipe preserved')
  recipes.update(found);RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 for p,r in found.items():print(p,r['represented_mpn'])
 print(len(found),'reviewed visual references')

if __name__ == '__main__':main()
