"""Prepare verified low-value UNI-ROYAL resistor display recipes."""
import argparse
import copy
import hashlib
from decimal import Decimal
import json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE, E24
from kicad_agents.package_markings import marking_text

SPECS = {'0603': ('0603WAF','electronic_resistor_0603_10000_ohm','Resistor_SMD:R_0603_1608Metric'),
         '0805': ('0805W8F','electronic_resistor_0805_1000_ohm','Resistor_SMD:R_0805_2012Metric'),
         '1206': ('1206W4F','electronic_resistor_1206_1000_ohm','Resistor_SMD:R_1206_3216Metric')}
PART = re.compile(r'electronic_resistor_(0603|0805|1206)_([0-9]+(?:_[0-9]+)?)_ohm')
LOW_0603_EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_UNIROYAL_0603_LOW_EVIDENCE.md')


def four_digit_mark(digits, exponent):
    if not re.fullmatch(r'[1-9][0-9]{2}', digits) or exponent not in ('J', 'K', 'L'):
        raise ValueError('Unsupported low-value MPN code')
    return {'J': digits[:2]+'R'+digits[2:], 'K': digits[0]+'R'+digits[1:], 'L': 'R'+digits}[exponent]


def reviewed_recipe(part_id, record, recipes):
    match = PART.fullmatch(part_id)
    if not match: raise ValueError('Unsupported ID')
    size, raw = match.groups()
    prefix,pilot_id,footprint=SPECS[size]
    value=Decimal(raw.replace('_','.'))
    mpn=str(record.get('part_number_manufacturer',''))
    code=re.fullmatch(re.escape(prefix)+r'([0-9]{3})([JKL0])T5E',mpn)
    if not code or 'UNI-ROYAL' not in str(record.get('manufacturer','')).upper():
        raise ValueError('Unreviewed manufacturer or MPN')
    digits,exponent=code.groups()
    jumper=(digits=='000' and exponent=='0' and value==0 and size=='0603')
    if not jumper:
        if exponent not in 'JKL' or digits[0]=='0' or Decimal(digits)*Decimal(10)**{'J':-1,'K':-2,'L':-3}[exponent]!=value:
            raise ValueError('Exact MPN value mismatch')
        if not Decimal('0.1') <= value < 100:
            raise ValueError('Outside reviewed low-value range')
    if record.get('kicad',{}).get('machine_solder') != footprint:
        raise ValueError('Footprint mismatch')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance is not None and str(tolerance).strip():
            found = re.search(r'(?<![0-9.])([0-9]+(?:\.[0-9]+)?)\s*%', str(tolerance))
            if not found or Decimal(found.group(1)) != 1:
                raise ValueError('Catalogue tolerance conflicts with 1% MPN')
    if not any(isinstance(x,dict) and 'UNI-ROYAL' in str(x.get('manufacturer','')).upper() and x.get('part_number')==mpn for x in record.get('manufacturers') or []):
        raise ValueError('Matching primary manufacturer entry missing')
    recipe=copy.deepcopy(recipes[pilot_id])
    expected_package={'0603':'0603_imperial_1608_metric','0805':'0805_imperial','1206':'1206_imperial'}[size]
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != expected_package:
        raise ValueError('Unexpected package pilot')
    recipe.update(represented_manufacturer='UNI-ROYAL',represented_mpn=mpn)
    evidence=copy.deepcopy(recipes['electronic_resistor_0603_10000_ohm']['marking']['evidence'])
    evidence.update(page=3,source_record=f'parts_source/{part_id}/working.yaml')
    if size=='0603' and not jumper:
        marking=recipe['marking'];marking.update(policy='uniroyal_0603_e96',resistance_ohm=str(value),tolerance_percent=1,evidence=evidence)
        try:
            text=marking_text(marking)
        except ValueError:
            if exponent != 'K' or int(digits) not in E24 or digits[-1] != '0' or not Decimal(1) <= value < 10:
                raise ValueError('Not a reviewed 0603 low-value E24 exception')
            text=digits[0]+'R'+digits[1]
            path=ROOT/LOW_0603_EVIDENCE
            evidence={'file':LOW_0603_EVIDENCE.as_posix(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                'document':'UNI-ROYAL thick-film specification 2017 V2 (reviewed online)', 'page':6,
                'source_record':f'parts_source/{part_id}/working.yaml',
                'rule':f'Sections 4(3) and 4(5): 0603 1% E24 {value} ohm uses underlined {text}.'}
            recipe['marking']={'policy':'verified_literal','text':text,'underline':True,'evidence':evidence,
                'maximum_width_mm':.76,'maximum_height_mm':.32,'font_file':'arialbd.ttf',
                'appearance_status':'Documented underlined code; ink, typeface and placement are illustrative.'}
        else:
            evidence['rule']=f'Section 4(6): {value} ohm uses the exact E96 code {text}.'
    else:
        text='0' if jumper else four_digit_mark(digits,exponent)
        evidence['rule']=(f'Section 4(2): 0603 zero-ohm jumpers normally carry 0.' if jumper else
                          f'Sections 4(4)-(5): {value} ohm at 1% is marked {text}; R is the decimal point.')
        box={'0603':(.76,.32),'0805':(.95,.48),'1206':(1.52,.64)}[size]
        recipe['marking']={'policy':'verified_literal','text':text,'evidence':evidence,
            'maximum_width_mm':box[0],'maximum_height_mm':box[1],'font_file':'arialbd.ttf',
            'appearance_status':'Documented value code; ink, typeface and placement are illustrative.'}
    return recipe,text


def discover():
    recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'));found={};skipped={}
    for size in SPECS:
        for d in sorted((ROOT/'parts_source').glob('electronic_resistor_'+size+'_*')):
            source=d/'working.yaml'
            if d.name in recipes or not source.is_file() or not (ROOT/'parts'/d.name/'working.yaml').is_file():continue
            try:
                record=yaml.safe_load(source.read_text(encoding='utf8')) or {}
                found[d.name]=reviewed_recipe(d.name,record,recipes)
            except (ValueError,KeyError,TypeError) as exc:skipped[d.name]=str(exc)
    return found,skipped


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args()
    found,skipped=discover()
    if args.add:
        recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
        if any(k in recipes for k in found):raise ValueError('A selected recipe already exists')
        recipes.update({k:v[0] for k,v in found.items()})
        RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(len(found),'reviewed candidates;',len(skipped),'need other review')
    for key,(recipe,text) in found.items():print(key,recipe['represented_mpn'],text)

if __name__=='__main__':main()
