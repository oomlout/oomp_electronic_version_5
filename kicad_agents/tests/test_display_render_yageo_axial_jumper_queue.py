import copy,json
from pathlib import Path
import pytest,yaml
from PIL import Image
from kicad_agents.display_render import create_axial_band_texture
from kicad_agents.display_render_yageo_axial_jumper_queue import PART,reviewed_recipe

def test_centered_black_jumper_on_blue_body(tmp_path):
 create_axial_band_texture({'bands':['black'],'body_span_mm':[.66,6.96]},[-.3,-1.25,-3],[7.92,1.25,2.5],tmp_path)
 image=Image.open(tmp_path/'axial_bands.png').convert('RGB')
 def pixel(f):return image.getpixel((round((.66+f*6.3+.3)*image.width/8.22),0))
 assert pixel(.5)==(17,19,21) and pixel(.3)==pixel(.7)==(124,166,171)
 with pytest.raises(ValueError):create_axial_band_texture({'bands':['red'],'body_span_mm':[.66,6.96]},[-.3,-1.25,-3],[7.92,1.25,2.5],tmp_path)

def test_jumper_identity_and_disclosure():
 record=yaml.safe_load((Path('parts_source')/PART/'working.yaml').read_text(encoding='utf8'));recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
 r=reviewed_recipe(record,recipes,'hash');assert r['marking']['bands']==['black'] and 'unverified' in r['appearance_status']
 for field in ('identity','listing','footprint'):
  changed=copy.deepcopy(record)
  if field=='identity':changed['part_number_manufacturer']='other'
  if field=='listing':changed['distributors']=[]
  if field=='footprint':changed['kicad']['machine_solder']='other'
  with pytest.raises(ValueError):reviewed_recipe(changed,recipes,'hash')
