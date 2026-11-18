"""Prepare the reviewed Fenghua RS-03L2R7JT display recipe."""
import argparse,copy,hashlib,json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
PART='electronic_resistor_0603_2_7_ohm'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0603_2R7_EVIDENCE.md')

def reviewed_recipe(record,recipes,sha):
 mpn='RS-03L2R7JT';manufacturer='FH (Guangdong Fenghua Advanced Tech)'
 if record.get('manufacturer')!=manufacturer or record.get('part_number_manufacturer')!=mpn:raise ValueError('Selected identity changed')
 if not any(x.get('manufacturer')==manufacturer and x.get('part_number')==mpn for x in record.get('manufacturers',[]) if isinstance(x,dict)):raise ValueError('Manufacturer entry changed')
 if not any(x.get('key')=='lcsc' and x.get('part_number')=='C1186' for x in record.get('distributors',[]) if isinstance(x,dict)):raise ValueError('Selected listing changed')
 electrical=record.get('electrical') or {};ratings=(record.get('jlcpcb_selection') or {}).get('ratings') or {}
 if electrical.get('resistance')!='2.7 Ω' or ratings.get('Resistance')!='2.7Ω':raise ValueError('Value changed')
 if any(not re.search(r'(?<![0-9.])5(?:\.0+)?\s*%',str(v or '')) for v in (electrical.get('tolerance'),ratings.get('Tolerance'))):raise ValueError('Tolerance changed')
 if record.get('kicad',{}).get('machine_solder')!='Resistor_SMD:R_0603_1608Metric':raise ValueError('Footprint changed')
 r=copy.deepcopy(recipes['electronic_resistor_0603_102000_ohm'])
 if r.get('family')!='chip_resistor' or r.get('package')!='0603_imperial':raise ValueError('Unexpected template')
 r.update(represented_manufacturer='FH',represented_mpn=mpn)
 r['marking']={'policy':'verified_literal','text':'2R7','evidence':{'file':EVIDENCE.as_posix(),'sha256':sha,'document':'Local Fenghua RS general thick-film specification, pages 1, 11–12','source_record':f'parts_source/{PART}/working.yaml','rule':'Fenghua 0603 5% E24 2R7 code denotes 2.7 ohms.'},'maximum_width_mm':.76,'maximum_height_mm':.32,'font_file':'arialbd.ttf','appearance_status':'Documented 5% code; ink, typeface and placement are illustrative.'}
 r['appearance_status']='Generic KiCad package with illustrative ceramic, coating and terminations; represents one supplier choice.'
 return r

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
 if PART in recipes:print('Already prepared');return
 record=yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8'));sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest();r=reviewed_recipe(record,recipes,sha)
 if args.add:recipes[PART]=r;RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 print(PART,r['represented_mpn'],r['marking']['text'])
if __name__=='__main__':main()

