"""Prepare reviewed FOJAN 1% FRC decimal-value recipes without rendering."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE, E24
from kicad_agents.package_markings import marking_text

EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_FOJAN_LOW_EVIDENCE.md')
PART=re.compile(r'electronic_resistor_(0201|0402|0603|0805|1206)_([0-9]+(?:_[0-9]+)?)_ohm')
TEMPLATES={
 '0201':('electronic_resistor_0201_2700_ohm','Resistor_SMD:R_0201_0603Metric'),
 '0402':('electronic_resistor_0402_102000_ohm','Resistor_SMD:R_0402_1005Metric'),
 '0603':('electronic_resistor_0603_102000_ohm','Resistor_SMD:R_0603_1608Metric'),
 '0805':('electronic_resistor_0805_102000_ohm','Resistor_SMD:R_0805_2012Metric'),
 '1206':('electronic_resistor_1206_1200000_ohm','Resistor_SMD:R_1206_3216Metric')}


def reviewed_decimal_recipe(part_id,record,recipes,evidence_hash):
    ident=PART.fullmatch(part_id)
    if not ident:raise ValueError('Unsupported ID')
    size,raw=ident.groups();value=Decimal(raw.replace('_','.'));mpn=str(record.get('part_number_manufacturer','')).replace(' ','')
    code=re.fullmatch('FRC'+size+r'F([1-9][0-9]R[0-9])TS',mpn)
    if not code or 'FOJAN' not in str(record.get('manufacturer','')).upper():raise ValueError('Unreviewed primary manufacturer or MPN')
    literal=code.group(1)
    if not Decimal(10)<=value<100 or Decimal(literal.replace('R','.'))!=value:raise ValueError('Value does not match supported decimal MPN')
    template,footprint=TEMPLATES[size]
    if record.get('kicad',{}).get('machine_solder')!=footprint:raise ValueError('Footprint mismatch')
    if not any(isinstance(x,dict) and 'FOJAN' in str(x.get('manufacturer','')).upper() and str(x.get('part_number','')).replace(' ','')==mpn for x in record.get('manufacturers') or []):raise ValueError('Primary manufacturer entry missing')
    recipe=copy.deepcopy(recipes[template])
    if recipe.get('family')!='chip_resistor' or recipe.get('represented_manufacturer')!='FOJAN':raise ValueError('Unexpected source recipe')
    recipe.update(represented_manufacturer='FOJAN',represented_mpn=mpn)
    evidence={'file':EVIDENCE.as_posix(),'sha256':evidence_hash,'document':'FOJAN FRC specification FJ-JS-3001 V1.0, 2023 (reviewed online)',
              'source_record':f'parts_source/{part_id}/working.yaml'}
    if size in ('0201','0402'):
        evidence.update(page=2,rule=f'FOJAN specifies {size} FRC bodies as unmarked.')
        recipe['marking']['evidence']=evidence
    elif size=='0603':
        try:
            text=marking_text({'policy':'uniroyal_0603_e96','resistance_ohm':str(value),'evidence':evidence})
            if text[-1] not in 'YXABCDEF':raise ValueError('Multiplier outside FOJAN table')
            evidence.update(page=2,rule=f'FOJAN E96 table: {value} ohm is marked {text}.')
            marking={'policy':'verified_literal','text':text,'evidence':evidence}
        except ValueError:
            if value!=value.to_integral_value() or int(value)*10 not in E24:raise ValueError('Not a reviewed E24 exception')
            text=f'{int(value):02d}0';evidence.update(page=3,rule=f'FOJAN 0603 E24 exception: {value} ohm uses {text} with an underline below the middle character.')
            marking={'policy':'verified_literal','text':text,'underline_character':1,'evidence':evidence}
        marking.update(maximum_width_mm=.76,maximum_height_mm=.32,font_file='arialbd.ttf',
            appearance_status='Documented FOJAN code; ink, typeface and placement are illustrative.')
        recipe['marking']=marking
    else:
        evidence.update(page=2,rule=f'FOJAN 1% marking {literal} denotes {value} ohm; R is the decimal point.')
        box={'0805':(.95,.48),'1206':(1.52,.64)}[size]
        recipe['marking']={'policy':'verified_literal','text':literal,'evidence':evidence,'maximum_width_mm':box[0],
          'maximum_height_mm':box[1],'font_file':'arialbd.ttf','appearance_status':'Documented FOJAN code; ink, typeface and placement are illustrative.'}
    return recipe


def discover():
    recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'));evidence_hash=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest();found={};skipped={}
    for d in sorted((ROOT/'parts_source').glob('electronic_resistor_*')):
        source=d/'working.yaml'
        if d.name in recipes or not source.is_file() or not (ROOT/'parts'/d.name/'working.yaml').is_file():continue
        try:found[d.name]=reviewed_decimal_recipe(d.name,yaml.safe_load(source.read_text(encoding='utf8')) or {},recipes,evidence_hash)
        except (ValueError,TypeError,KeyError) as exc:skipped[d.name]=str(exc)
    return found,skipped


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();found,skipped=discover()
    if args.add:
        recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
        if any(k in recipes for k in found):raise ValueError('Selected recipe already exists')
        recipes.update(found);RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(len(found),'FOJAN candidates;',len(skipped),'other records require review')
    for k,r in found.items():print(k,r['represented_mpn'],r['marking'].get('text','(unmarked)'), 'middle underline' if r['marking'].get('underline_character')==1 else '')

if __name__=='__main__':main()
