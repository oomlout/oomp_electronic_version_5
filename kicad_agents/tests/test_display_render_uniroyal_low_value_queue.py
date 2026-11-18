import copy
import pytest
from kicad_agents.display_render_uniroyal_low_value_queue import four_digit_mark, reviewed_recipe

@pytest.mark.parametrize(('digits','exponent','expected'), [('100','J','10R0'),('499','J','49R9'),('220','K','2R20'),('100','L','R100')])
def test_exact_decimal_marking(digits,exponent,expected):
    assert four_digit_mark(digits,exponent)==expected

def test_identity_footprint_value_and_e96_rules():
    mpn='0805W8F220KT5E';record={'manufacturer':'UNI-ROYAL','part_number_manufacturer':mpn,
        'manufacturers':[{'manufacturer':'UNI-ROYAL','part_number':mpn}],
        'kicad':{'machine_solder':'Resistor_SMD:R_0805_2012Metric'}}
    evidence={'file':'evidence','sha256':'hash'}
    recipes={'electronic_resistor_0603_10000_ohm':{'marking':{'evidence':evidence}},
             'electronic_resistor_0805_1000_ohm':{'family':'chip_resistor','package':'0805_imperial','marking':{}}}
    recipe,text=reviewed_recipe('electronic_resistor_0805_2_2_ohm',record,recipes)
    assert text=='2R20' and recipe['marking']['text']=='2R20'
    for changed in ({**record,'manufacturer':'other'}, {**record,'manufacturers':[]},
                    {**record,'kicad':{'machine_solder':'wrong'}},
                    {**record,'part_number_manufacturer':'0805W8F200KT5E'}):
        with pytest.raises(ValueError):reviewed_recipe('electronic_resistor_0805_2_2_ohm',changed,recipes)
    with pytest.raises(ValueError):four_digit_mark('000','J')

def test_0603_uses_e96_and_reviewed_underlined_e24():
    pilot={'family':'chip_resistor','package':'0603_imperial_1608_metric','marking':{'policy':'uniroyal_0603_e96','evidence':{'file':'evidence','sha256':'hash'}}}
    recipes={'electronic_resistor_0603_10000_ohm':pilot}
    def rec(mpn):return {'manufacturer':'UNI-ROYAL','part_number_manufacturer':mpn,
        'manufacturers':[{'manufacturer':'UNI-ROYAL','part_number':mpn}],
        'kicad':{'machine_solder':'Resistor_SMD:R_0603_1608Metric'}}
    assert reviewed_recipe('electronic_resistor_0603_49_9_ohm',rec('0603WAF499JT5E'),recipes)[1]=='68X'
    recipe,text=reviewed_recipe('electronic_resistor_0603_2_2_ohm',rec('0603WAF220KT5E'),recipes)
    assert text=='2R2' and recipe['marking']['underline'] is True
    with pytest.raises(ValueError):reviewed_recipe('electronic_resistor_0603_2_3_ohm',rec('0603WAF230KT5E'),recipes)
    with pytest.raises(ValueError,match='tolerance'):
        reviewed_recipe('electronic_resistor_0603_2_2_ohm',{**rec('0603WAF220KT5E'),'electrical':{'tolerance':'±5%'}},recipes)
