import copy,json
from pathlib import Path
import pytest,yaml
from kicad_agents.display_render_fojan_frp1206_15r0_queue import PART,reviewed_recipe

def test_frp_marking_and_selected_identity():
 d=yaml.safe_load((Path('parts_source')/PART/'working.yaml').read_text(encoding='utf8'));recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'));r=reviewed_recipe(d,recipes,'hash')
 assert r['marking']['text']=='15R0' and r['represented_mpn']=='FRP1206F15R0TSN'
 for field in ('identity','listing','tolerance','footprint'):
  bad=copy.deepcopy(d)
  if field=='identity':bad['part_number_manufacturer']='other'
  if field=='listing':bad['distributors']=[]
  if field=='tolerance':bad['electrical']={'tolerance':'5%'}
  if field=='footprint':bad['kicad']['machine_solder']='other'
  with pytest.raises(ValueError):reviewed_recipe(bad,recipes,'hash')
