import copy,json
from pathlib import Path
import pytest,yaml
from kicad_agents.display_render_yageo_rt1206_133k_queue import PART,reviewed_recipe

def test_rt_identity_tolerance_and_marking():
 d=yaml.safe_load((Path('parts_source')/PART/'working.yaml').read_text(encoding='utf8'));recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'));r=reviewed_recipe(d,recipes,'hash')
 assert r['marking']['text']=='1333' and r['represented_mpn']=='RT1206DRE07133KL'
 for field in ('identity','listing','tolerance','footprint'):
  bad=copy.deepcopy(d)
  if field=='identity':bad['part_number_manufacturer']='other'
  if field=='listing':bad['distributors']=[]
  if field=='tolerance':bad['electrical']={'tolerance':'1%'}
  if field=='footprint':bad['kicad']['machine_solder']='other'
  with pytest.raises(ValueError):reviewed_recipe(bad,recipes,'hash')
