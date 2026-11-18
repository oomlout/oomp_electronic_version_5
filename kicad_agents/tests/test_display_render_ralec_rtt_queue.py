from decimal import Decimal
import pytest
from kicad_agents.display_render_ralec_rtt_queue import marking_value, reviewed_recipe

@pytest.mark.parametrize(('code','tolerance','value'), [
    ('1102','F','11000'), ('11R0','F','11'), ('4R99','F','4.99'),
    ('182','J','1800'), ('3R9','J','3.9'), ('6800','F','680')])
def test_documented_codes(code, tolerance, value):
    assert marking_value(code, tolerance) == Decimal(value)

def test_guarded_primary_identity_footprint_and_tolerance():
    part='electronic_resistor_1206_11_ohm_ralec_rtt0611r0ftp'
    mpn='RTT0611R0FTP'
    record={'manufacturer':'RALEC','part_number_manufacturer':mpn,
            'manufacturers':[{'manufacturer':'RALEC','part_number':mpn}],
            'kicad':{'machine_solder':'Resistor_SMD:R_1206_3216Metric'}}
    pilot={'family':'chip_resistor','package':'1206_imperial','marking':{}}
    result=reviewed_recipe(part,record,pilot,'evidence')
    assert result['marking']['text']=='11R0'
    assert '0.05 mm longer' in result['appearance_status']
    for changed in ({**record,'manufacturer':'other'}, {**record,'manufacturers':[]},
                    {**record,'part_number_manufacturer':'RTT0610R0FTP'},
                    {**record,'kicad':{'machine_solder':'wrong'}}):
        with pytest.raises(ValueError):reviewed_recipe(part,changed,pilot,'evidence')
    with pytest.raises(ValueError):
        reviewed_recipe('electronic_resistor_1206_11_ohm_5_percent',record,pilot,'evidence')
    with pytest.raises(ValueError):marking_value('110','F')


def test_rejects_value_equivalent_but_wrong_marking_form():
    mpn = 'RTT060100FTP'
    record = {'manufacturer':'RALEC','part_number_manufacturer':mpn,
              'manufacturers':[{'manufacturer':'RALEC','part_number':mpn}],
              'kicad':{'machine_solder':'Resistor_SMD:R_1206_3216Metric'}}
    with pytest.raises(ValueError, match='documented decimal'):
        reviewed_recipe('electronic_resistor_1206_10_ohm', record,
                        {'family':'chip_resistor','package':'1206_imperial','marking':{}}, 'hash')
