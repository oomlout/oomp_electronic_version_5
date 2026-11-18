import json
from pathlib import Path

import pytest

from kicad_agents.display_render_yageo_large_queue import reviewed_recipe


def test_exact_yageo_identity_value_and_tolerance():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    part = 'electronic_resistor_1206_47000_ohm'
    mpn = 'RC1206FR-0747KL'
    record = {'manufacturer': 'YAGEO', 'part_number_manufacturer': mpn,
              'manufacturers': [{'manufacturer': 'YAGEO', 'part_number': mpn}],
              'distributors': [{'product_name': '47kΩ ±1%'}],
              'kicad': {'machine_solder': 'Resistor_SMD:R_1206_3216Metric'}}
    assert reviewed_recipe(part, record, recipes, 'hash')['marking']['text'] == '4702'
    for changed in ({**record, 'part_number_manufacturer': 'RC1206JR-0747KL'},
                    {**record, 'electrical': {'tolerance': '5%'}},
                    {**record, 'distributors': [{'product_name': '47kΩ'}]},
                    {**record, 'kicad': {'machine_solder': 'wrong'}}):
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'hash')
    with pytest.raises(ValueError):
        reviewed_recipe('electronic_resistor_1206_470000_ohm', record, recipes, 'hash')
