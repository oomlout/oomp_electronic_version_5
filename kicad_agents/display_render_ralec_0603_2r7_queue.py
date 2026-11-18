"""Prepare the reviewed RALEC RTT032R70FTP display recipe."""
import argparse,copy,hashlib,json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
PART='electronic_resistor_0603_2_7_ohm_ralec_rtt032r70ftp'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_RALEC_0603_2R7_EVIDENCE.md')

def reviewed_recipe(record,recipes,sha):
 mpn='RTT032R70FTP';manufacturer='RALEC'
 if record.get('manufacturer')!=manufacturer or record.get('part_number_manufacturer')!=mpn:raise ValueError('Selected identity changed')
 if not any(x.get('manufacturer')==manufacturer and x.get('part_number')==mpn for x in record.get('manufacturers',[]) if isinstance(x,dict)):raise ValueError('Manufacturer entry changed')
 if not any(x.get('key')=='lcsc' and x.get('part_number')=='C4209' for x in record.get('distributors',[]) if isinstance(x,dict)):raise ValueError('Selected listing changed')
 ratings=(record.get('jlcpcb_selection') or {}).get('ratings') or {}
 if ratings.get('Resistance')!='2.7Ω':raise ValueError('Value changed')
 if not re.search(r'(?<![0-9.])1(?:\.0+)?\s*%',str(ratings.get('Tolerance') or '')):raise ValueError('Tolerance changed')
 if record.get('kicad',{}).get('machine_solder')!='Resistor_SMD:R_0603_1608Metric':raise ValueError('Footprint changed')
 r=copy.deepcopy(recipes['electronic_resistor_0603_102000_ohm'])
 if r.get('family')!='chip_resistor' or r.get('package')!='0603_imperial':raise ValueError('Unexpected template')
 r.update(represented_manufacturer='RALEC',represented_mpn=mpn)
 r['marking']={'policy':'verified_literal','text':'2R7','underline':True,'evidence':{'file':EVIDENCE.as_posix(),'sha256':sha,'document':'Local RALEC IE-SP-007 specification, pages 12–13','source_record':f'parts_source/{PART}/working.yaml','rule':'Inferred underlined 2R7 from RALEC 1% E24 and low-value decimal rules; no exact 2.7-ohm example shown.'},'maximum_width_mm':.76,'maximum_height_mm':.32,'font_file':'arialbd.ttf','appearance_status':'Underlined 2R7 inferred from RALEC rules; exact 2.7-ohm marking not pictured. Ink, typeface and placement are illustrative.'}
 r['appearance_status']='Generic KiCad package with illustrative ceramic, coating and terminations; represents one supplier choice.'
 return r

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
 if PART in recipes:print('Already prepared');return
 record=yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8'));sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest();r=reviewed_recipe(record,recipes,sha)
 if args.add:recipes[PART]=r;RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 print(PART,r['represented_mpn'],r['marking']['text'])
if __name__=='__main__':main()

