"""Prepare a reviewed, explicitly illustrative axial zero-ohm jumper."""
import argparse,copy,hashlib,json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
PART='electronic_resistor_quarter_watt_through_hole_0_ohm'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_AXIAL_JUMPER_EVIDENCE.md')

def reviewed_recipe(record,recipes,sha):
 mpn='MFR-25-T-52-0R'
 if record.get('manufacturer')!='YAGEO' or record.get('part_number_manufacturer')!=mpn:raise ValueError('Selected identity changed')
 if not any(x.get('manufacturer')=='YAGEO' and x.get('part_number')==mpn for x in record.get('manufacturers',[]) if isinstance(x,dict)):raise ValueError('Manufacturer entry changed')
 if not any(x.get('key')=='lcsc' and x.get('part_number')=='C173063' and '0Ω' in str(x.get('product_name','')) for x in record.get('distributors',[]) if isinstance(x,dict)):raise ValueError('Supplier listing changed')
 if record.get('kicad',{}).get('machine_solder')!='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':raise ValueError('Footprint changed')
 r=copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_1000_ohm'])
 if r.get('family')!='axial_resistor' or r.get('package')!='din0207_horizontal_7_62mm':raise ValueError('Unexpected template')
 r.update(represented_manufacturer='YAGEO',represented_mpn=mpn)
 r['marking']={'policy':'verified_literal','text':'black','bands':['black'],'body_span_mm':[.66,6.96],
  'evidence':{'file':EVIDENCE.as_posix(),'sha256':sha,'document':'Yageo selected identity and Vishay cylindrical jumper convention (reviewed online)','source_record':f'parts_source/{PART}/working.yaml','rule':'One centered black band illustrates a zero-ohm jumper; selected Yageo marking is unverified.'},
  'appearance_status':'Illustrative centered black jumper band; actual selected Yageo marking is unverified.'}
 r['appearance_status']='Generic KiCad axial geometry with bent leads at 7.62 mm pitch. Beige coating and black jumper band are illustrative; the selected Yageo appearance is unverified.'
 return r

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
 if PART in recipes:print('Already prepared');return
 record=yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8'));sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest();r=reviewed_recipe(record,recipes,sha)
 if args.add:recipes[PART]=r;RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 print(PART,r['represented_mpn'],r['marking']['text'])
if __name__=='__main__':main()
