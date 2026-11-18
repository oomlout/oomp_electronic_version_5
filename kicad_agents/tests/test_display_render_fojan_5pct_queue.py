import json
from pathlib import Path
import pytest
from kicad_agents.display_render_fojan_5pct_queue import reviewed_recipe

@pytest.fixture
def recipes():return json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))

def test_verified_5_percent_identity_and_mark(recipes):
    part='electronic_resistor_1206_120000_ohm';mpn='FRC1206J124 TS';entry={'mpn':mpn,'lcsc':'C2907425','url':'https://www.lcsc.com/product-detail/C2907425.html'}
    record={'manufacturer':'FOJAN','part_number_manufacturer':mpn,'manufacturers':[{'manufacturer':'FOJAN','part_number':mpn}],
            'kicad':{'machine_solder':'Resistor_SMD:R_1206_3216Metric'},'distributors':[{'key':'lcsc','part_number':'C2907425','product_name':'120kΩ ±5% 1206'}]}
    assert reviewed_recipe(part,record,recipes,'hash',{part:entry})['marking']['text']=='124'
    for changed in ({**record,'part_number_manufacturer':'TS'}, {**record,'manufacturers':[]},
                    {**record,'kicad':{'machine_solder':'wrong'}}, {**record,'distributors':[]}):
        with pytest.raises(ValueError):reviewed_recipe(part,changed,recipes,'hash',{part:entry})
    with pytest.raises(ValueError):reviewed_recipe('electronic_resistor_1206_1000_ohm',record,recipes,'hash',{part:entry})

def test_0201_remains_unmarked(recipes):
    part='electronic_resistor_0201_15_ohm';mpn='FRC0201J150 TS';entry={'mpn':mpn,'lcsc':'C18164323','url':'https://www.lcsc.com/product-detail/C18164323.html'}
    record={'manufacturer':'FOJAN','part_number_manufacturer':mpn,'manufacturers':[{'manufacturer':'FOJAN','part_number':mpn}],
            'kicad':{'machine_solder':'Resistor_SMD:R_0201_0603Metric'},'distributors':[{'key':'lcsc','part_number':'C18164323','product_name':'15Ω ±5%'}]}
    assert reviewed_recipe(part,record,recipes,'hash',{part:entry})['marking']['policy']=='none'


def test_verified_research_rows_keep_full_supplier_identities():
    from working_oomp_populate_lcsc_research_data import LCSC_RESEARCH
    for name in ('DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES.json','DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES_02.json','DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES_03.json','DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES_05.json'):
        ledger=json.loads((Path('kicad_agents/component_records')/name).read_text(encoding='utf8'))
        for identity in ledger['records']:
            row=LCSC_RESEARCH[identity['part_id']]
            assert row['manufacturer']=='FOJAN'
            assert row['part_number_lcsc']==identity['lcsc']
            assert row['part_number_manufacturer']==identity['mpn']
