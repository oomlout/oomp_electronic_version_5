"""Component taxonomy semantics shared by ingestion, displays and generators.

ICs: electronic / ic / function / subtype / package / manufacturer / MPN.
The last two fields retain their reserved taxonomy levels 14 and 15.
"""

IC_FUNCTIONS = frozenset({
    'amplifier', 'audio', 'capacitive_touch_controller', 'clock_management',
    'comparator', 'controller', 'converter', 'cpld', 'driver', 'interface',
    'logic', 'memory', 'microcontroller', 'optocoupler', 'pld',
    'power_management', 'power_meter', 'power_monitor', 'rf', 'sensor',
    'timer', 'trusted_platform_module',
})


def package_token(part):
    """Return a family's package/style field; IC packages belong at level 5."""
    return str(part.get('taxonomy_5' if part.get('taxonomy_2') == 'ic' else 'taxonomy_3', '') or '')


def validate_ic_taxonomy(part):
    """Reject package-first IC definitions before they can create old IDs."""
    if part.get('taxonomy_2') != 'ic':
        return
    if part.get('taxonomy_3') not in IC_FUNCTIONS:
        raise ValueError('IC taxonomy_3 must be its function, not its package. '
                         'Add a justified new function to component_taxonomy.IC_FUNCTIONS when needed.')
    if not part.get('taxonomy_4') or not part.get('taxonomy_5'):
        raise ValueError('IC taxonomy requires subtype at level 4 and package at level 5.')
    if any(part.get(f'taxonomy_{n}') for n in range(6, 14)):
        raise ValueError('IC package at taxonomy_5 must be the last regular taxonomy field; '
                         'put functional qualifiers in taxonomy_4, manufacturer at 14 and MPN at 15.')


def is_function_first_ic_id(part_id):
    return any(str(part_id).startswith('electronic_ic_'+function+'_') for function in IC_FUNCTIONS)

