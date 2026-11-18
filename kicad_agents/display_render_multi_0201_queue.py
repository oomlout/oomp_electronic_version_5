"""Prepare five manufacturer-verified, unmarked 0201 display recipes."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_MULTI_0201_EVIDENCE.md')
TEMPLATE='electronic_resistor_0201_2700_ohm'
FOOTPRINT='Resistor_SMD:R_0201_0603Metric'
# Exact source identifiers and nominal values were separately reviewed.
PARTS={
 'electronic_resistor_0201_1500000_ohm':('Walsin','WR02X155JAL','WR02X'),
 'electronic_resistor_0201_560000_ohm':('YAGEO','AF0201FR-07560KL','AF0201'),
 'electronic_resistor_0201_2700000_ohm':('KOA','RK73B1HTTC275J','RK73B 1H'),
 'electronic_resistor_0201_3900000_ohm':('KOA','RK73B1HTTC395J','RK73B 1H'),
 'electronic_resistor_0201_7500_ohm':('KOA','RK73H1HTTC7501F','RK73H 1H'),
}


def reviewed_recipe(part_id,record,recipes,evidence_hash):
    if part_id not in PARTS:raise ValueError('Not an exact reviewed part')
    manufacturer,mpn,series=PARTS[part_id]
    if record.get('manufacturer')!=manufacturer or record.get('part_number_manufacturer')!=mpn:
        raise ValueError('Primary identity changed')
    if not any(isinstance(x,dict) and x.get('manufacturer')==manufacturer and x.get('part_number')==mpn for x in record.get('manufacturers') or []):
        raise ValueError('Primary manufacturer entry missing')
    if record.get('kicad',{}).get('machine_solder')!=FOOTPRINT:raise ValueError('Footprint mismatch')
    recipe=copy.deepcopy(recipes[TEMPLATE])
    if recipe.get('family')!='chip_resistor' or recipe.get('package')!='0201_imperial' or recipe.get('marking',{}).get('policy')!='none':raise ValueError('Unexpected reviewed 0201 template')
    recipe.update(represented_manufacturer=manufacturer,represented_mpn=mpn)
    recipe['marking']={'policy':'none','evidence':{'file':EVIDENCE.as_posix(),'sha256':evidence_hash,
        'document':f'{manufacturer} {series} manufacturer marking specification (reviewed online)',
        'rule':f'{manufacturer} specifies {series} 0201 bodies as unmarked.',
        'source_record':f'parts_source/{part_id}/working.yaml'},
        'appearance_status':f'{manufacturer} documents {series} bodies as unmarked.'}
    return recipe


def discover():
    recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'));sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest();found={}
    for part in PARTS:
        if part in recipes:continue
        source=ROOT/'parts_source'/part/'working.yaml'
        if not source.is_file() or not (ROOT/'parts'/part/'working.yaml').is_file():continue
        found[part]=reviewed_recipe(part,yaml.safe_load(source.read_text(encoding='utf8')) or {},recipes,sha)
    return found


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();found=discover()
    if args.add:
        recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
        if any(k in recipes for k in found):raise ValueError('Existing recipe preserved')
        recipes.update(found);RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(len(found),'exact reviewed unmarked 0201 parts')
    for k,r in found.items():print(k,r['represented_mpn'])

if __name__=='__main__':main()
