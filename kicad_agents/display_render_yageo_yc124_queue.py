"""Prepare the exact documented YC124-JR-0710KL array display recipe."""
import copy
from pathlib import Path
import re

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_YC124_EVIDENCE.md')
PART = 'electronic_resistor_array_4_x_0402_convex_10000_ohm_8_pin'
MPN = 'YC124-JR-0710KL'


def reviewed_recipe(part, record, recipes, evidence_hash):
    if part != PART or record.get('manufacturer') != 'YAGEO' or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Exact reviewed Yageo identity required')
    if not any(x.get('manufacturer') == 'YAGEO' and x.get('part_number') == MPN
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry missing')
    if not any(x.get('part_number') == 'C326872' and '5%' in str(x.get('product_name', ''))
               for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier identity and tolerance need review')
    tolerance = (record.get('electrical') or {}).get('tolerance')
    if tolerance and not re.search(r'(?<![0-9.])5(?:\.0+)?\s*%', str(tolerance)):
        raise ValueError('Catalogue tolerance conflicts with selected part')
    kicad = record.get('kicad') or {}
    if kicad.get('machine_solder') not in ('', None, 'Resistor_SMD:R_Array_Convex_4x0402'):
        raise ValueError('Footprint conflicts with model')
    if record.get('dimensions_mm') != {'length': 2.0, 'width': 1.0}:
        raise ValueError('Dimensions changed; review again')
    recipe = copy.deepcopy(recipes['electronic_resistor_array_4_x_0402_convex_3300_ohm_8_pin'])
    if recipe.get('family') != 'chip_resistor_array' or recipe.get('package') != '4x0402_convex_8_pin':
        raise ValueError('Unexpected array template')
    recipe.update(represented_manufacturer='YAGEO', represented_mpn=MPN)
    recipe['marking'].update(text='103', evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
        'document': 'Yageo YC/TC specification V.11, pages 3 and 6 (reviewed online)',
        'source_record': f'parts_source/{part}/working.yaml',
        'rule': 'YC124 5% E24 marking 103 represents 10 kΩ per resistor.'},
        appearance_status='Documented value code; ink, typeface and placement are illustrative.')
    recipe['appearance_status'] = ('Generic KiCad four-resistor array with illustrative materials; '
                                   'model height is at the manufacturer tolerance limit.')
    return recipe
