"""Prepare exact, non-conflicting Fenghua RS 5% display recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE, E24

EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_RS_EVIDENCE.md')
PART=re.compile(r'electronic_resistor_(0805|1206)_([0-9]+(?:_[0-9]+)?)_ohm')
SPECS={'0805':('05','electronic_resistor_0805_1000_ohm','Resistor_SMD:R_0805_2012Metric',(.95,.48)),
       '1206':('06','electronic_resistor_1206_1000_ohm','Resistor_SMD:R_1206_3216Metric',(1.52,.64))}


def resistance(code):
    if re.fullmatch(r'[1-9][0-9]{2}',code):return Decimal(code[:2])*Decimal(10)**int(code[2])
    if re.fullmatch(r'[1-9]R[0-9]',code):return Decimal(code.replace('R','.'))
    raise ValueError('Unsupported three-character E24 code')


def reviewed_recipe(part_id,record,recipes,evidence_hash):
    match=PART.fullmatch(part_id)
    if not match:raise ValueError('Unsupported ID')
    size,raw=match.groups();value=Decimal(raw.replace('_','.'));prefix,pilot_id,footprint,box=SPECS[size]
    mpn=str(record.get('part_number_manufacturer',''))
    found=re.fullmatch('RS-'+prefix+r'[KL]([0-9R]{3})JT',mpn)
    if not found or 'FENGHUA' not in str(record.get('manufacturer','')).upper():raise ValueError('Unreviewed primary manufacturer or MPN')
    code=found.group(1)
    if resistance(code)!=value or not Decimal(1)<=value<=Decimal(10000000):raise ValueError('Value or supported range does not match MPN')
    normalized=value
    while normalized<100:normalized*=10
    while normalized>=1000:normalized/=10
    if normalized!=normalized.to_integral_value() or int(normalized) not in E24:raise ValueError('Not a reviewed E24 value')
    if record.get('kicad',{}).get('machine_solder')!=footprint:raise ValueError('Footprint mismatch')
    if not any(isinstance(x,dict) and 'FENGHUA' in str(x.get('manufacturer','')).upper() and x.get('part_number')==mpn for x in record.get('manufacturers') or []):raise ValueError('Matching primary manufacturer entry missing')
    electrical=record.get('electrical') or {};selection=record.get('jlcpcb_selection') or {};ratings=selection.get('ratings') or {}
    tolerances=[v for v in (electrical.get('tolerance'),ratings.get('Tolerance')) if v is not None and str(v).strip()]
    if not tolerances:raise ValueError('No explicit catalogue tolerance')
    for t in tolerances:
        found_tolerance=re.search(r'(?<![0-9.])([0-9]+(?:\.[0-9]+)?)\s*%',str(t))
        if not found_tolerance or Decimal(found_tolerance.group(1))!=5:raise ValueError('Catalogue tolerance conflicts with 5% MPN')
    recipe=copy.deepcopy(recipes[pilot_id])
    if recipe.get('family')!='chip_resistor' or recipe.get('package')!=size+'_imperial':raise ValueError('Unexpected package pilot')
    recipe.update(represented_manufacturer='FH',represented_mpn=mpn)
    evidence={'file':EVIDENCE.as_posix(),'sha256':evidence_hash,'document':'Fenghua RC/RS approval sheet R-6.1 (reviewed online)',
              'page':7,'rule':f'Fenghua RS {size} E24 5% marking {code} represents {value} ohm.',
              'source_record':f'parts_source/{part_id}/working.yaml'}
    recipe['marking']={'policy':'verified_literal','text':code,'evidence':evidence,'maximum_width_mm':box[0],
       'maximum_height_mm':box[1],'font_file':'arialbd.ttf','appearance_status':'Documented 5% value code; ink, typeface and placement are illustrative.'}
    recipe['appearance_status']='Generic KiCad package with illustrative ceramic, coating and terminations; represents one supplier choice.'
    return recipe


def discover():
    recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'));evidence_hash=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest();found={};skipped={}
    for size in SPECS:
        for d in sorted((ROOT/'parts_source').glob('electronic_resistor_'+size+'_*')):
            source=d/'working.yaml'
            if d.name in recipes or not source.is_file() or not (ROOT/'parts'/d.name/'working.yaml').is_file():continue
            try:found[d.name]=reviewed_recipe(d.name,yaml.safe_load(source.read_text(encoding='utf8')) or {},recipes,evidence_hash)
            except (ValueError,TypeError,KeyError) as exc:skipped[d.name]=str(exc)
    return found,skipped


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();found,skipped=discover()
    if args.add:
        recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
        if any(k in recipes for k in found):raise ValueError('Recipe already exists')
        recipes.update(found);RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(len(found),'reviewed Fenghua candidates;',sum(v=='Catalogue tolerance conflicts with 5% MPN' for v in skipped.values()),'tolerance conflicts')
    for k,r in found.items():print(k,r['represented_mpn'],r['marking']['text'])
    for k,v in skipped.items():
        if v=='Catalogue tolerance conflicts with 5% MPN':print('CONFLICT',k)

if __name__=='__main__':main()
