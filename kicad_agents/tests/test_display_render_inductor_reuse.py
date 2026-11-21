"""Restrict shared inductor illustrations to the reviewed exact family."""
import copy

import pytest
import working_oomp_populate_display_render as populate


def test_fenghua_inductor_reuse_scope():
    base = {'family': 'chip_inductor', 'package': '1206_metric_3216',
            'represented_manufacturer': 'Fenghua', 'represented_mpn': 'CMI321609X100KT',
            'model': {'sha256': 'same-model', 'display_scale_xyz': [1, 1, .5625]},
            'marking': {'policy': 'unmarked_illustration', 'text': '', 'evidence': {'file': 'one'}}}
    variant = copy.deepcopy(base)
    variant['represented_mpn'] = 'CMI321609U2R2KT'
    variant['marking']['evidence'] = {'file': 'two'}
    assert populate.unmarked_visual_recipe(base) == populate.unmarked_visual_recipe(variant)
    for key, value in [('represented_manufacturer', 'Sunlord'), ('represented_mpn', 'other'),
                       ('package', '0805_metric_2012')]:
        invalid = copy.deepcopy(variant)
        invalid[key] = value
        with pytest.raises(ValueError):
            populate.unmarked_visual_recipe(invalid)
    changed = copy.deepcopy(variant)
    changed['model']['display_scale_xyz'] = [1, 1, .72]
    assert populate.unmarked_visual_recipe(base) != populate.unmarked_visual_recipe(changed)
    generic = copy.deepcopy(base)
    generic.update(package='0603_metric_1608', represented_manufacturer='Unspecified', represented_mpn='generic 0603 30 ohm')
    populate.unmarked_visual_recipe(generic)
    generic['represented_mpn'] = 'generic 0603 unknown'
    with pytest.raises(ValueError):
        populate.unmarked_visual_recipe(generic)
