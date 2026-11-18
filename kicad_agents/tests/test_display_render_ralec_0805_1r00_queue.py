import copy,json
from pathlib import Path
import pytest,yaml
from kicad_agents.display_render_ralec_0805_1r00_queue import PART,reviewed_recipe

def test_legacy_id_is_explicit_and_selected_identity_guarded():
 record=yaml.safe_load((Path('parts_source')/PART/'working.yaml').read_text(encoding='utf8'));recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
 r=reviewed_recipe(record,recipes,'hash');assert r['marking']['text']=='1R00' and r['represented_mpn']=='RTT051R00FTP'
 assert 'legacy catalogue ID' in r['appearance_status'] and 'selected part is RALEC' in r['appearance_status']
 for field in ('identity','listing','tolerance','footprint'):
  bad=copy.deepcopy(record)
  if field=='identity':bad['part_number_manufacturer']='other'
  if field=='listing':bad['distributors']=[]
  if field=='tolerance':bad['electrical']['tolerance']='5%'
  if field=='footprint':bad['kicad']['machine_solder']='other'
  with pytest.raises(ValueError):reviewed_recipe(bad,recipes,'hash')
