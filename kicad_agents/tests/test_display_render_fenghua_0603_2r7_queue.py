import copy,json
from pathlib import Path
import pytest,yaml
from kicad_agents.display_render_fenghua_0603_2r7_queue import PART,reviewed_recipe

def test_selected_fenghua_code_and_source_guards():
 record=yaml.safe_load((Path('parts_source')/PART/'working.yaml').read_text(encoding='utf8'))
 recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
 recipe=reviewed_recipe(record,recipes,'hash')
 assert recipe['marking']['text']=='2R7' and recipe['represented_mpn']=='RS-03L2R7JT'
 for field in ('identity','listing','value','tolerance','footprint'):
  bad=copy.deepcopy(record)
  if field=='identity':bad['part_number_manufacturer']='other'
  if field=='listing':bad['distributors']=[]
  if field=='value':bad['electrical']['resistance']='different'
  if field=='tolerance':bad['electrical']['tolerance']='1%'
  if field=='footprint':bad['kicad']['machine_solder']='other'
  with pytest.raises(ValueError):reviewed_recipe(bad,recipes,'hash')
