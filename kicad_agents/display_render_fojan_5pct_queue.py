"""Prepare supplier-verified FOJAN 5% FRC recipes after exact identity repair."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE, E24

EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES.json')
TEMPLATES={'0201':('electronic_resistor_0201_2700_ohm','Resistor_SMD:R_0201_0603Metric',None),
 '0603':('electronic_resistor_0603_102000_ohm','Resistor_SMD:R_0603_1608Metric',(.76,.32)),
 '0805':('electronic_resistor_0805_102000_ohm','Resistor_SMD:R_0805_2012Metric',(.95,.48)),
 '1206':('electronic_resistor_1206_1200000_ohm','Resistor_SMD:R_1206_3216Metric',(1.52,.64))}
PART=re.compile(r'electronic_resistor_(0201|0603|0805|1206)_([0-9]+)_ohm')


def reviewed_recipe(part_id,record,recipes,evidence_hash,identities,evidence_path=EVIDENCE):
    match=PART.fullmatch(part_id)
    identity=identities.get(part_id)
    if not match or not identity:raise ValueError('Part lacks a verified supplier identity')
    size,raw=match.groups();value=Decimal(raw);mpn=identity['mpn'];compact=mpn.replace(' ','')
    code=re.fullmatch('FRC'+size+r'J([0-9]{3})TS',compact)
    if not code or record.get('manufacturer')!='FOJAN' or record.get('part_number_manufacturer')!=mpn:raise ValueError('Primary FOJAN MPN does not match supplier evidence')
    digits=code.group(1)
    if Decimal(digits[:2])*Decimal(10)**int(digits[2])!=value or int(digits[:2])*10 not in E24:raise ValueError('Part number value is not the catalogue E24 value')
    if not Decimal(10)<=value<=Decimal(10000000):raise ValueError('Value outside reviewed range')
    template,footprint,box=TEMPLATES[size]
    if record.get('kicad',{}).get('machine_solder')!=footprint:raise ValueError('Footprint mismatch')
    if not any(isinstance(x,dict) and x.get('manufacturer')=='FOJAN' and x.get('part_number')==mpn for x in record.get('manufacturers') or []):raise ValueError('Primary manufacturer entry missing')
    if not any(isinstance(x,dict) and x.get('key')=='lcsc' and x.get('part_number')==identity['lcsc'] and '5%' in str(x.get('product_name','')) for x in record.get('distributors') or []):raise ValueError('Supplier code or 5% rating missing')
    recipe=copy.deepcopy(recipes[template])
    if recipe.get('family')!='chip_resistor' or recipe.get('represented_manufacturer')!='FOJAN':raise ValueError('Unexpected template')
    recipe.update(represented_manufacturer='FOJAN',represented_mpn=mpn)
    evidence={'file':evidence_path.as_posix(),'sha256':evidence_hash,'document':'FOJAN FRC manufacturer specification and individually reviewed identity evidence',
       'source_record':f'parts_source/{part_id}/working.yaml','supplier_url':identity['url'],
       'rule':f'FOJAN 5% E24 marking {digits} represents {value} ohm.'}
    if size=='0201':
        evidence['rule']=f'FOJAN FRC 0201 body is unmarked; supplier code {digits} represents {value} ohm.'
        recipe['marking']['evidence']=evidence
    else:
        recipe['marking']={'policy':'verified_literal','text':digits,'evidence':evidence,
          'maximum_width_mm':box[0],'maximum_height_mm':box[1],'font_file':'arialbd.ttf',
          'appearance_status':'Documented FOJAN value code; ink, typeface and placement are illustrative.'}
    return recipe


def discover(evidence_path=EVIDENCE):
    recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'));ledger=json.loads((ROOT/evidence_path).read_text(encoding='utf8'))
    identities={x['part_id']:x for x in ledger['records']};sha=hashlib.sha256((ROOT/evidence_path).read_bytes()).hexdigest();found={}
    for part in identities:
        if part in recipes:continue
        source=ROOT/'parts_source'/part/'working.yaml'
        if not source.is_file() or not (ROOT/'parts'/part/'working.yaml').is_file():raise ValueError('Missing source or generated part: '+part)
        found[part]=reviewed_recipe(part,yaml.safe_load(source.read_text(encoding='utf8')) or {},recipes,sha,identities,evidence_path)
    return found


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');parser.add_argument('--evidence',type=Path,default=EVIDENCE);args=parser.parse_args();found=discover(args.evidence)
    if args.add:
        recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
        if any(k in recipes for k in found):raise ValueError('Existing recipe preserved')
        recipes.update(found);RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(len(found),'verified FOJAN 5% recipes')
    for k,r in found.items():print(k,r['represented_mpn'],r['marking'].get('text','unmarked'))

if __name__=='__main__':main()
