"""Prepare the specifically evidenced Fenghua RC-MT08W000JT jumper."""
import copy
from pathlib import Path

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_ARRAY_JUMPER_EVIDENCE.md')
PART = 'electronic_resistor_array_4_x_0402_convex_0_ohm_8_pin'
MPN = 'RC-MT08W000JT'


def reviewed_recipe(part, record, recipes, evidence_hash):
    if part != PART or record.get('manufacturer') != 'FH (Guangdong Fenghua Advanced Tech)' or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Exact reviewed jumper identity required')
    if not any(x.get('manufacturer') == record['manufacturer'] and x.get('part_number') == MPN
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry missing')
    kicad = record.get('kicad') or {}
    if kicad.get('machine_solder') != 'Resistor_SMD:R_Array_Convex_4x0402' or kicad.get('symbol') != 'Device:R_Pack04':
        raise ValueError('Footprint or symbol mismatch')
    electrical = record.get('electrical') or {}
    if electrical.get('elements') != 4 or electrical.get('terminals') != 8 or electrical.get('resistance') != '0Ω':
        raise ValueError('Jumper configuration mismatch')
    recipe = copy.deepcopy(recipes['electronic_resistor_array_4_x_0402_convex_3300_ohm_8_pin'])
    if recipe.get('family') != 'chip_resistor_array' or recipe.get('package') != '4x0402_convex_8_pin':
        raise ValueError('Unexpected array template')
    recipe.update(represented_manufacturer='FH', represented_mpn=MPN)
    recipe['marking'].update(text='0', evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
        'document': 'Fenghua network approval sheet N-5.10, page 7 (reviewed online)',
        'source_record': f'parts_source/{part}/working.yaml',
        'rule': 'RCMT08 zero-ohm jumper arrays are marked with a single 0.'},
        appearance_status='Manufacturer documents the zero mark; ink, typeface and placement are illustrative.')
    recipe['appearance_status'] = ('Generic KiCad four-jumper array with illustrative materials; '
                                   'model height is at the manufacturer tolerance limit.')
    return recipe
