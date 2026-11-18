import copy
import json

import pytest
import yaml

from kicad_agents.display_render_huaxing_knp2w_10r_queue import PART, ROOT, RECIPE_FILE, reviewed_recipe


def test_large_package_rating_and_code():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(record, recipes, 'test')
    assert result['marking']['bands'] == ['brown', 'black', 'black', 'gold']
    assert 'DIN0516' in result['model']['relative_path']
    assert '2 W' in result['appearance_status']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace('2W', '250mW')
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')


def test_axial_band_width_validation(tmp_path):
    from kicad_agents.display_render import create_axial_band_texture
    marking = {'bands': ['brown', 'black', 'black', 'gold'],
               'body_span_mm': [2.41, 17.91], 'band_width_mm': .52}
    create_axial_band_texture(marking, [-.4, 0, 0], [20.72, 1, 1], tmp_path)
    assert (tmp_path / 'axial_bands.png').is_file()
    marking['band_width_mm'] = 3
    with pytest.raises(ValueError):
        create_axial_band_texture(marking, [-.4, 0, 0], [20.72, 1, 1], tmp_path)
