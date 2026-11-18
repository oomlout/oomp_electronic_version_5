"""Prepare the specifically reviewed Yageo AC0402 6.8 MΩ recipe."""
import copy
from pathlib import Path
import re

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_AC0402_EVIDENCE.md')
PART = 'electronic_resistor_0402_6800000_ohm'
MPN = 'AC0402JR-076M8L'


def reviewed_recipe(part, record, recipes, evidence_hash):
    if part != PART or record.get('manufacturer') != 'YAGEO' or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Exact reviewed Yageo AC part required')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_SMD:R_0402_1005Metric':
        raise ValueError('Footprint mismatch')
    if not any(x.get('manufacturer') == 'YAGEO' and x.get('part_number') == MPN
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry missing')
    for rating in ((record.get('electrical') or {}).get('tolerance'),
                   ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if rating and not re.search(r'(?<![0-9.])5(?:\.0+)?\s*%', str(rating)):
            raise ValueError('Tolerance conflicts with selected part')
    recipe = copy.deepcopy(recipes['electronic_resistor_0402_1000_ohm'])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != '0402_imperial' or recipe.get('marking', {}).get('policy') != 'none':
        raise ValueError('Unexpected unmarked template')
    recipe.update(represented_manufacturer='YAGEO', represented_mpn=MPN)
    recipe['marking'] = {'policy': 'none', 'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
        'document': 'Yageo AC-series product specification (reviewed online)',
        'rule': 'Yageo AC0402 bodies have no marking.', 'source_record': f'parts_source/{part}/working.yaml'},
        'appearance_status': 'Yageo documents AC0402 bodies as unmarked.'}
    recipe['appearance_status'] = ('Generic KiCad nominal package geometry with illustrative materials; '
                                   'represents one supplier choice.')
    return recipe
