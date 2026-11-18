import json
from pathlib import Path
import pytest
from kicad_agents.display_render_fenghua_rs_queue import resistance, reviewed_recipe

@pytest.fixture
def recipes():return json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
def source():
    mpn='RS-05L1R8JT';return {'manufacturer':'FH (Guangdong Fenghua Advanced Tech)', 'part_number_manufacturer':mpn,
       'manufacturers':[{'manufacturer':'FH (Guangdong Fenghua Advanced Tech)','part_number':mpn}],
       'kicad':{'machine_solder':'Resistor_SMD:R_0805_2012Metric'},'electrical':{'tolerance':'±5%'},
       'jlcpcb_selection':{'ratings':{'Tolerance':'±5%'}}}

def test_decimal_and_exponent_codes(recipes):
    r=reviewed_recipe('electronic_resistor_0805_1_8_ohm',source(),recipes,'hash')
    assert r['marking']['text']=='1R8' and str(resistance('390'))=='39'

def test_rejects_conflicting_tolerance_and_identity(recipes):
    r=source()
    for changed in ({**r,'electrical':{'tolerance':'+-1% (F)'}},
                    {**r,'jlcpcb_selection':{'ratings':{'Tolerance':'±1%'}}},
                    {**r,'manufacturer':'other'}, {**r,'manufacturers':[]},
                    {**r,'kicad':{'machine_solder':'wrong'}}):
        with pytest.raises(ValueError):reviewed_recipe('electronic_resistor_0805_1_8_ohm',changed,recipes,'hash')
    with pytest.raises(ValueError):reviewed_recipe('electronic_resistor_0805_3_9_ohm',r,recipes,'hash')
