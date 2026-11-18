"""Evidence-backed cable contacts and empty housings; no PCB geometry defaults.

Harwin M20 loose contacts and black single-row 2.54 mm housings.
See kicad_agents/CRIMP_CONNECTOR_AGENT.md for the taxonomy and evidence rules.
"""
from copy import deepcopy
from pathlib import Path
from oomp_populate_helper import build_oomp_id

CONTACT_PDF = 'https://content.harwin.com/asset/d742d022-1905-41c8-b996-8feb2ed262c8/DRG-00379-Technical-Drawing-Datasheet-M20-118-pdf.pdf'
HOUSING_PDF = 'https://content.harwin.com/asset/b9496f9a-d89f-420f-aea9-abb4534be02f/DRG-00376-Technical-Drawing-Datasheet-M20-106-pdf.pdf'
PRODUCT_URL = 'https://www.harwin.com/products/'
MODEL_ASSETS = ('model_3d.step', 'model_3d_render.png', 'model_3d_source.yaml')

# Exact MPNs and mating finishes verified on the individual Harwin product pages.
CONTACT_MODELS = (
    ('M20-1180042', 'gold', 'Gold'),
    ('M20-1180046', 'tin', '100% tin over nickel'),
)
# Exact MPN, positions, and published dimension along the contact row (mm).
HOUSING_MODELS = (
    ('M20-1060200', 2, 5.28),
    ('M20-1060100', 1, 2.74),
    ('M20-1060300', 3, 7.82),
    ('M20-1060400', 4, 10.36),
    ('M20-1060500', 5, 12.90),
    ('M20-1060600', 6, 15.44),
    ('M20-1060800', 8, 20.52),
    ('M20-1061000', 10, 25.60),
)


def _taxonomy(mpn, role, positions, style):
    return {
        'taxonomy_2': 'connector', 'taxonomy_3': 'header',
        'taxonomy_4': '2_54_mm_pitch', 'taxonomy_5': role,
        'taxonomy_6': f'{positions}_pin', 'taxonomy_7': style,
        'taxonomy_14': 'harwin', 'taxonomy_15': mpn.lower().replace('-', '_'),
    }


def _id(taxonomy):
    return build_oomp_id({'taxonomy_1': 'electronic', **taxonomy})


def _contact(mpn, finish, plating):
    taxonomy = _taxonomy(mpn, 'crimp', 1, 'socket')
    taxonomy.update(taxonomy_8='22_to_30_awg', taxonomy_9=finish)
    return {
        'id': _id(taxonomy),
        'taxonomy': taxonomy,
        'name': f'Header crimp contact 2.54 mm socket 22-30 AWG {finish} (Harwin {mpn})',
        'mpn': mpn, 'product_url': PRODUCT_URL + mpn, 'datasheet_url': CONTACT_PDF,
        'role': 'cable_crimp_contact',
        'dimensions_mm': {'length': 11.7, 'width': 2.3, 'height': 2.6},
        'pins': {'pin_1': {'number': '1', 'name': 'contact', 'type': 'passive'}},
        'details': {
            'component_role': 'Loose female crimp contact with one conductive terminal',
            'series': 'Harwin M20', 'pitch': '2.54 mm (housing pitch)',
            'contact_finish': plating, 'termination_finish': '100% tin over nickel',
            'contact_material': 'Brass', 'wire_size': '22-30 AWG',
            'mating_pin': '0.64 mm square', 'packaging': 'Loose',
            'catalogue_length': '11.70 mm, with a separate 12.04 mm reference span in the drawing',
        },
        'electrical': {'current_rating': '3 A per contact', 'operating_temperature': '-40 to +105 C'},
        'label': {'primary': 'CRIMP SOCKET', 'details': [
            '2.54 mm header / 22-30 AWG', f'{finish.title()} contact / tin termination', f'Harwin {mpn}',
        ]},
        'related_parts': [],
    }


def _housing(mpn, positions, row_length):
    taxonomy = _taxonomy(mpn, 'housing', positions, 'black')
    contact_noun = 'contact' if positions == 1 else 'contacts'
    return {
        'id': _id(taxonomy),
        'taxonomy': taxonomy,
        'name': f'Header housing 2.54 mm {positions}-position black (Harwin {mpn})',
        'mpn': mpn, 'product_url': PRODUCT_URL + mpn, 'datasheet_url': HOUSING_PDF,
        'role': 'cable_housing',
        'dimensions_mm': {'length': row_length, 'width': 14.0, 'height': 2.5},
        'positions': positions,
        'pins': {},
        'details': {
            'component_role': 'Empty insulating housing with contacts supplied separately',
            'series': 'Harwin M20', 'pitch': '2.54 mm', 'positions': f'{positions}, single row',
            'housing_color': 'Black', 'housing_material': 'PPE+PS',
            'flammability': 'UL94V-1', 'mating_pin': '0.64 mm square',
            'mating_pin_length': '5.50 to 6.30 mm',
            'polarised': 'No', 'contacts_required': f'{positions}, sold separately',
        },
        'electrical': {'operating_temperature': '-25 to +85 C',
                       'assembled_current_rating': '3 A per contact with suitable contacts'},
        'label': {'primary': f'{positions}-POS HOUSING', 'details': [
            '2.54 mm header / BLACK', f'Empty: needs {positions} crimp {contact_noun}', f'Harwin {mpn}',
        ]},
        'related_parts': [],
    }


CONTACTS = [_contact(*model) for model in CONTACT_MODELS]
HOUSINGS = [_housing(*model) for model in HOUSING_MODELS]
CONTACT_ID = CONTACTS[0]['id']
HOUSING_ID = HOUSINGS[0]['id']
PARTS = [CONTACTS[0], HOUSINGS[0], *CONTACTS[1:], *HOUSINGS[1:]]

# Every listed housing product page explicitly names both loose M20-118 contacts.
for housing in HOUSINGS:
    for contact in CONTACTS:
        contact['related_parts'].append({
            'relationship': 'Fits housing', 'oomp_id': housing['id'],
            'name': housing['name'], 'evidence_url': housing['product_url'],
            'notes': f"Order {housing['positions']} contacts separately to fill this housing.",
        })
        housing['related_parts'].append({
            'relationship': 'Contact option', 'oomp_id': contact['id'],
            'name': contact['name'], 'quantity': housing['positions'],
            'evidence_url': housing['product_url'],
            'notes': 'Select the finish for the mating header. Quantity is for filling all positions with this option.',
        })


def apply_extras(extras_dict):
    """Apply at the end of connector extras so PCB-header defaults cannot leak in."""
    for row in PARTS:
        part = extras_dict.get(row['id'])
        if part is None:
            continue
        for field in ('header_dimensions_mm', 'generic_match'):
            part.pop(field, None)
        if row['role'] == 'cable_crimp_contact':
            drawing_id = 'M20-11800XX issue 13'
            dimension_note = ('The nominal diagram uses the published 11.70 mm length. '
                              'The drawing also gives a 12.04 mm reference span. '
                              'Use the manufacturer drawing for feature-level dimensions.')
        else:
            drawing_id = 'M20-106XX00 issue 8'
            dimension_note = ('The row length follows 2.54 mm × positions + 0.20 mm with a ±0.30 mm tolerance. '
                              'The diagram shows nominal outer dimensions.')
        part.update({
            'name_short': row['name'], 'name_readable_override': row['name'],
            'manufacturer': 'Harwin', 'part_number_manufacturer': row['mpn'],
            'product_url': row['product_url'], 'datasheet_url': row['datasheet_url'],
            'component_role': row['role'], 'pcb_mountable': False,
            'diagram_name': ('Crimp socket 2.54 mm ' if row['role'] == 'cable_crimp_contact' else 'Black housing 2.54 mm ') + row['mpn'],
            'dimensions_mm': deepcopy(row['dimensions_mm']), 'pins': deepcopy(row['pins']),
            'connector_details': deepcopy(row['details']), 'electrical': deepcopy(row['electrical']),
            'related_parts': deepcopy(row['related_parts']),
            'label_drawer_overrides': deepcopy(row['label']),
            'research_notes': [
                'Manufacturer product page checked 2026-11-16. Exact Harwin identity, finish/colour and pair compatibility recorded.',
                'No LCSC/JLCPCB code or assembly classification has been verified; none is assigned.',
                'Pitch alone does not establish compatibility with another header or crimp system.',
            ],
            'dimension_reference': {'manufacturer': 'Harwin', 'product_url': row['product_url'],
                'datasheet_url': row['datasheet_url'], 'checked_on': '2026-11-16',
                'drawing': drawing_id, 'pdf_page': 1, 'notes': dimension_note},
            'drawing_note': 'Dimensioned envelope only: contact spring, crimp wings and housing cavities are not detailed. Not a PCB footprint or crimp-tool drawing.',
            'kicad': {'applicability': 'not_applicable', 'symbol': '', 'machine_solder': '',
                'hand_solder': '', 'allow_project_fallback': False,
                'reason': 'Separate cable-assembly component, not a PCB-mounted connector. No standalone PCB symbol or solder footprint is assigned.'},
        })
        length, width, height = (row['dimensions_mm'][k] for k in ('length', 'width', 'height'))
        part['package_drawing'] = {
            'overall': [length, width], 'body': [length, width], 'pins': [],
            'side': {'overall': [width, height], 'body': [width, height], 'pins': []},
        }
        # A document link is not a downloaded PDF. Copy only an actual source asset.
        relative_source = Path('parts_source') / row['id']
        source = Path(__file__).resolve().parent / relative_source
        assets = ['datasheet.pdf'] if (source / 'datasheet.pdf').is_file() else []
        if all((source / name).is_file() for name in MODEL_ASSETS):
            assets.extend(MODEL_ASSETS)
            part['model_3d'] = dict(zip(('step', 'render', 'provenance'),
                                       (f'data/{name}' for name in MODEL_ASSETS)))
        part['file_copy'] = [
            {'file_source': (relative_source / name).as_posix(), 'file_destination': name}
            for name in assets
        ]
