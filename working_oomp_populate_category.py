"""Human-editable component categories, shared by population and board import.

Set option['category'] in a family populator, or part['category'] in its extra
block, to override these defaults. Categories do not change OOMP IDs.
"""


# taxonomy_2, category. Arrays stay simple so new families are easy to add.
FAMILY_CATEGORIES = [
    ['resistor', 'resistor'],
    ['resistor_array', 'resistor'],
    ['capacitor', 'capacitor'],
    ['connector', 'connector'],
    ['switch', 'switch'],
    ['led', 'led'],
    ['diode', 'diode'],
    ['transistor', 'transistor'],
    ['crystal', 'crystal'],
    ['ferrite_bead', 'ferrite_bead'],
    ['inductor', 'inductor'],
    ['display', 'display'],
    ['wire', 'wire'],
    ['prototyping', 'prototyping'],
    ['mounting_hole', 'mounting_hole'],
    ['ic', 'ic'],
]

# IC taxonomy_4, category. Function matters more than the physical package.
IC_CATEGORIES = [
    ['microcontroller', 'mcu'],
    ['memory', 'memory'],
    ['logic', 'logic'],
    ['amplifier', 'amplifier'],
    ['comparator', 'comparator'],
    ['power_management', 'power_management'],
    ['converter', 'interface'],
    ['controller', 'controller'],
]

CATEGORY_NAMES = {
    'mcu': 'MCU', 'ic': 'IC', 'led': 'LED', 'code': 'Code',
    'power_management': 'Power management', 'ferrite_bead': 'Ferrite bead',
    'mounting_hole': 'Mounting hole', 'test_point': 'Test point',
}


def category_name(category):
    return CATEGORY_NAMES.get(category, category.replace('_', ' ').capitalize())


def add_category(part):
    if part.get('taxonomy_1', 'electronic') not in ['electronic', 'mechanical']:
        return
    category = str(part.get('category') or '').strip().lower().replace('-', '_').replace(' ', '_')
    if not category:
        category = 'other'
        for family, default in FAMILY_CATEGORIES:
            if part.get('taxonomy_2') == family:
                category = default
        if part.get('taxonomy_2') == 'ic':
            for function, default in IC_CATEGORIES:
                if part.get('taxonomy_4') == function:
                    category = default
    part['category'] = category
    part['category_name'] = category_name(category)


# Coarse categories for unmatched board items only; never an OOMP match.
# Official symbol library prefixes provide stronger evidence than references.
SYMBOL_CATEGORY_PREFIXES = [
    ['mcu_', 'mcu'], ['memory_', 'memory'], ['74', 'logic'], ['4xxx', 'logic'],
    ['connector', 'connector'], ['amplifier_', 'amplifier'],
    ['comparator', 'comparator'], ['regulator_', 'power_management'],
    ['interface_', 'interface'], ['switch', 'switch'],
]
REFERENCE_CATEGORIES = [
    ['LED', 'led'], ['RN', 'resistor'], ['R', 'resistor'],
    ['CON', 'connector'], ['J', 'connector'], ['P', 'connector'],
    ['C', 'capacitor'], ['D', 'diode'], ['Q', 'transistor'],
    ['FB', 'ferrite_bead'], ['L', 'inductor'], ['F', 'fuse'],
    ['SW', 'switch'], ['TP', 'test_point'], ['XT', 'crystal'], ['Y', 'crystal'],
    ['IC', 'ic'], ['U', 'ic'],
]


def unmatched_category(reference, library_id=''):
    library = str(library_id).split(':')[0].lower()
    for prefix, category in SYMBOL_CATEGORY_PREFIXES:
        if library.startswith(prefix):
            return category
    reference_prefix = ''.join(character for character in reference.upper() if character.isalpha())
    for prefix, category in REFERENCE_CATEGORIES:
        if reference_prefix == prefix:
            return category
    return 'other'
