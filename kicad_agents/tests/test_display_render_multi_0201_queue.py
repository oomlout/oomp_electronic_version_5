import json
from pathlib import Path
import pytest
from kicad_agents.display_render_multi_0201_queue import reviewed_recipe,PARTS

@pytest.fixture
def recipes():return json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))

def test_all_five_have_matching_verified_sources(recipes):
    for part,(manufacturer,mpn,_) in PARTS.items():
        record={'manufacturer':manufacturer,'part_number_manufacturer':mpn,
                'manufacturers':[{'manufacturer':manufacturer,'part_number':mpn}],
                'kicad':{'machine_solder':'Resistor_SMD:R_0201_0603Metric'}}
        r=reviewed_recipe(part,record,recipes,'hash')
        assert r['marking']['policy']=='none' and r['represented_mpn']==mpn
        for changed in ({**record,'manufacturer':'other'}, {**record,'manufacturers':[]},
                        {**record,'kicad':{'machine_solder':'wrong'}}, {**record,'part_number_manufacturer':'wrong'}):
            with pytest.raises(ValueError):reviewed_recipe(part,changed,recipes,'hash')
