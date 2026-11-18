"""Prepare exact UNI-ROYAL 1% quarter-watt axial display recipes."""
import argparse,copy,hashlib,json
from decimal import Decimal
from pathlib import Path
import re,yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import bands_for
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_UNIROYAL_MFR0W4_EVIDENCE.md')
PARTS={'electronic_resistor_quarter_watt_through_hole_12000_ohm':('MFR0W4F1202A50','C58670',Decimal(12000)),
       'electronic_resistor_quarter_watt_through_hole_82000_ohm':('MFR0W4F8202A50','C58623',Decimal(82000))}

def reviewed_recipe(part,record,recipes,sha):
 if part not in PARTS:raise ValueError('Unreviewed ID')
 mpn,lcsc,value=PARTS[part]
 if record.get('manufacturer')!='UNI-ROYAL' or record.get('part_number_manufacturer')!=mpn:raise ValueError('Selected identity changed')
 if not any(x.get('manufacturer')=='UNI-ROYAL' and x.get('part_number')==mpn for x in record.get('manufacturers',[]) if isinstance(x,dict)):raise ValueError('Manufacturer entry changed')
 if not any(x.get('key')=='lcsc' and x.get('part_number')==lcsc and all(t in str(x.get('product_name','')) for t in ('1%','250mW')) for x in record.get('distributors',[]) if isinstance(x,dict)):raise ValueError('Selected supplier rating changed')
 for t in ((record.get('electrical') or {}).get('tolerance'),((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
  if t and not re.search(r'(?<![0-9.])1(?:\.0+)?\s*%',str(t)):raise ValueError('Tolerance conflict')
 if record.get('kicad',{}).get('machine_solder')!='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':raise ValueError('Footprint changed')
 r=copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_1000_ohm']);bands=bands_for(value)
 if r.get('family')!='axial_resistor' or len(bands)!=5 or bands[-1]!='brown':raise ValueError('Unexpected template or tolerance')
 r.update(represented_manufacturer='UNI-ROYAL',represented_mpn=mpn)
 r['marking'].update(text=' / '.join(bands),bands=bands,evidence={'file':EVIDENCE.as_posix(),'sha256':sha,'document':'UNI-ROYAL precision metal-film and MFR0W4 specifications (reviewed online)','source_record':f'parts_source/{part}/working.yaml','rule':f'UNI-ROYAL 1% five-band code for {value} Ω: '+', '.join(bands)+'.'},appearance_status='Documented 1% value code with brown tolerance band; stripe spacing and shades are illustrative.')
 r['appearance_status']='Generic KiCad axial geometry with bent leads at 7.62 mm pitch. Blue body is illustrative; its 2.5 mm diameter is at the manufacturer upper limit.'
 return r

def discover():
 recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'));sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest()
 return {p:reviewed_recipe(p,yaml.safe_load((ROOT/'parts_source'/p/'working.yaml').read_text(encoding='utf8')) or {},recipes,sha) for p in PARTS if p not in recipes and (ROOT/'parts'/p/'working.yaml').is_file()}

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();found=discover()
 if args.add:
  recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
  if any(p in recipes for p in found):raise ValueError('Existing recipe preserved')
  recipes.update(found);RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 for p,r in found.items():print(p,r['represented_mpn'],r['marking']['text'])
 print(len(found),'reviewed parts')
if __name__=='__main__':main()
