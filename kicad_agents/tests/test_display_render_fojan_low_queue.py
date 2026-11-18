import json
from pathlib import Path
import pytest
from kicad_agents.display_render_fojan_low_queue import reviewed_decimal_recipe

@pytest.fixture
def recipes():return json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
def record(size,code):
    mpn=f'FRC{size}F{code}TS'
    return {'manufacturer':'FOJAN','part_number_manufacturer':mpn,'manufacturers':[{'manufacturer':'FOJAN','part_number':mpn}],
      'kicad':{'machine_solder':{'0201':'Resistor_SMD:R_0201_0603Metric','0402':'Resistor_SMD:R_0402_1005Metric',
      '0603':'Resistor_SMD:R_0603_1608Metric','0805':'Resistor_SMD:R_0805_2012Metric','1206':'Resistor_SMD:R_1206_3216Metric'}[size]}}

def test_distinct_marking_policies(recipes):
    assert reviewed_decimal_recipe('electronic_resistor_0402_12_ohm',record('0402','12R0'),recipes,'hash')['marking']['policy']=='none'
    m=reviewed_decimal_recipe('electronic_resistor_0603_12_ohm',record('0603','12R0'),recipes,'hash')['marking']
    assert m['text']=='120' and m['underline_character']==1
    m=reviewed_decimal_recipe('electronic_resistor_0603_15_ohm',record('0603','15R0'),recipes,'hash')['marking']
    assert m['text']=='18X' and 'underline_character' not in m
    assert reviewed_decimal_recipe('electronic_resistor_1206_18_ohm',record('1206','18R0'),recipes,'hash')['marking']['text']=='18R0'

def test_rejects_identity_and_footprint_mismatches(recipes):
    r=record('0805','12R0')
    for part,changed in [('electronic_resistor_0805_13_ohm',r),('electronic_resistor_0805_12_ohm',{**r,'manufacturer':'other'}),
      ('electronic_resistor_0805_12_ohm',{**r,'manufacturers':[]}),('electronic_resistor_0805_12_ohm',{**r,'kicad':{}})]:
        with pytest.raises(ValueError):reviewed_decimal_recipe(part,changed,recipes,'hash')
