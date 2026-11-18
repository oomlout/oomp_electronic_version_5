"""Prepare the exact RALEC RTT051R00FTP legacy-ID display recipe."""
import argparse,hashlib,json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
from kicad_agents.display_render_ralec_rtt_queue import reviewed_recipe as base_recipe
PART='electronic_resistor_0805_1_ohm_uni_royal_uniroyal_elec_rtt051r00ftp'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_RALEC_0805_1R00_EVIDENCE.md')

def reviewed_recipe(record,recipes,sha):
 if record.get('manufacturer')!='RALEC' or record.get('part_number_manufacturer')!='RTT051R00FTP':raise ValueError('Selected identity changed')
 if not any(x.get('key')=='lcsc' and x.get('part_number')=='C4321' for x in record.get('distributors',[]) if isinstance(x,dict)):raise ValueError('Selected supplier changed')
 ratings=(record.get('jlcpcb_selection') or {}).get('ratings') or {};e=record.get('electrical') or {}
 if ratings.get('Resistance')!='1Ω' or not re.search(r'(?<![0-9.])1(?:\.0+)?\s*%',str(ratings.get('Tolerance',''))) or not re.search(r'(?<![0-9.])1(?:\.0+)?\s*%',str(e.get('tolerance',''))):raise ValueError('Value or tolerance changed')
 r=base_recipe('electronic_resistor_0805_1_ohm_ralec_rtt051r00ftp',record,recipes['electronic_resistor_0805_1000_ohm'],sha)
 r['marking']['evidence']={'file':EVIDENCE.as_posix(),'sha256':sha,'document':'Local RALEC IE-SP-007 RTT family specification, pages 4 and 12','source_record':f'parts_source/{PART}/working.yaml','rule':'RALEC RTT05 1% decimal code 1R00 denotes 1 ohm.'}
 r['appearance_status']+=' The legacy catalogue ID contains UNI-ROYAL, but the selected part is RALEC RTT051R00FTP.'
 return r

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
 if PART in recipes:print('Already prepared');return
 record=yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8'));sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest();r=reviewed_recipe(record,recipes,sha)
 if args.add:recipes[PART]=r;RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 print(PART,r['represented_mpn'],r['marking']['text'])
if __name__=='__main__':main()
