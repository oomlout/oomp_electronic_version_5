"""Prepare the exact FOJAN FRP1206F15R0TSN display recipe."""
import argparse,copy,hashlib,json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
PART='electronic_resistor_1206_15_ohm'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_FOJAN_FRP1206_15R0_EVIDENCE.md')

def reviewed_recipe(record,recipes,sha):
 mpn='FRP1206F15R0TSN'
 if record.get('manufacturer')!='FOJAN' or record.get('part_number_manufacturer')!=mpn:raise ValueError('Selected identity changed')
 if not any(x.get('manufacturer')=='FOJAN' and x.get('part_number')==mpn for x in record.get('manufacturers',[]) if isinstance(x,dict)):raise ValueError('Manufacturer entry changed')
 if not any(x.get('key')=='lcsc' and x.get('part_number')=='C2934388' and all(t in str(x.get('product_name','')) for t in ('15Ω','1%','1206')) for x in record.get('distributors',[]) if isinstance(x,dict)):raise ValueError('Supplier rating changed')
 for v in ((record.get('electrical') or {}).get('tolerance'),((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
  if v and not re.search(r'(?<![0-9.])1(?:\.0+)?\s*%',str(v)):raise ValueError('Tolerance conflict')
 if record.get('kicad',{}).get('machine_solder')!='Resistor_SMD:R_1206_3216Metric':raise ValueError('Footprint changed')
 r=copy.deepcopy(recipes['electronic_resistor_1206_1000_ohm'])
 if r.get('family')!='chip_resistor' or r.get('package')!='1206_imperial':raise ValueError('Unexpected package')
 r.update(represented_manufacturer='FOJAN',represented_mpn=mpn)
 r['marking']={'policy':'verified_literal','text':'15R0','evidence':{'file':EVIDENCE.as_posix(),'sha256':sha,'document':'FOJAN FRP high-power series specification and selected supplier listing (reviewed online)','source_record':f'parts_source/{PART}/working.yaml','rule':'FOJAN FRP1206 1% decimal marking 15R0 denotes 15 Ω.'},'maximum_width_mm':1.52,'maximum_height_mm':.64,'font_file':'arialbd.ttf','appearance_status':'Documented value code; ink, typeface and placement are illustrative.'}
 r['appearance_status']='Generic KiCad 1206 package with illustrative ceramic, coating and terminations; represents the selected FOJAN FRP high-power series choice; generic 3.20 mm body length is at the manufacturer maximum.'
 return r

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
 if PART in recipes:print('Already prepared');return
 record=yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8'));sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest();r=reviewed_recipe(record,recipes,sha)
 if args.add:recipes[PART]=r;RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 print(PART,r['represented_mpn'],r['marking']['text'])
if __name__=='__main__':main()
