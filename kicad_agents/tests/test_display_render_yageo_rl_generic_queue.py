import copy,json
from pathlib import Path
import pytest,yaml
from kicad_agents.display_render_yageo_rl_generic_queue import PARTS,reviewed_recipe

@pytest.mark.parametrize('part',PARTS)
def test_generic_reference_and_review_guards(part):
 d=yaml.safe_load((Path('parts_source')/part/'working.yaml').read_text(encoding='utf8'));recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'));r=reviewed_recipe(part,d,recipes,'hash')
 assert r['marking']['text']==PARTS[part][2] and r['represented_mpn']==PARTS[part][1]
 assert 'no selected manufacturer, tolerance or power rating' in r['appearance_status'] and 'interchangeability' in r['appearance_status']
 for field in ('supplier','tolerance','power','footprint'):
  bad=copy.deepcopy(d)
  if field=='supplier':bad['manufacturer']='other'
  if field=='tolerance':bad['electrical']={'tolerance':'5%'}
  if field=='power':bad['electrical']={'power':'2 W'}
  if field=='footprint':bad['kicad']['machine_solder']='other'
  with pytest.raises(ValueError):reviewed_recipe(part,bad,recipes,'hash')
