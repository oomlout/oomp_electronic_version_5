"""Validate unmarked LED reuse without trusting a different image or lens."""
import copy
import hashlib
import json

import working_oomp_populate_display_render as populate


def test_unmarked_led_reuse_checks_source_and_excludes_tinted(monkeypatch, tmp_path):
    monkeypatch.setattr(populate, 'ROOT', tmp_path)
    monkeypatch.setattr(populate, 'renderer_source_available', lambda value: value == 'reviewed-renderer')
    source_part = 'electronic_led_0201_blue'
    source_dir = tmp_path / 'parts' / source_part / 'data/display_render'
    source_dir.mkdir(parents=True)
    artifacts = {}
    for name, content in [('render.png', b'full image'), ('preview.webp', b'preview image')]:
        (source_dir / name).write_bytes(content)
        artifacts[name] = {'sha256': hashlib.sha256(content).hexdigest(), 'bytes': len(content)}
    recipe = {'family': 'led', 'package': '0201_metric_0603', 'represented_manufacturer': 'Unspecified',
              'represented_mpn': 'generic blue 0201 LED', 'model': {'sha256': 'reviewed-model'},
              'marking': {'policy': 'unmarked_illustration', 'text': '', 'evidence': {'file': 'blue'}}}
    studio = {'camera': 'reviewed'}
    source = {'part_id': source_part, 'recipe': recipe, 'studio': studio, 'renderer_source_sha256': 'reviewed-renderer',
              'marking': {'text': ''}, 'artifacts': artifacts}
    source_path = source_dir / 'manifest.json'
    source_path.write_text(json.dumps(source), encoding='utf8')
    candidate = copy.deepcopy(recipe)
    candidate['represented_mpn'] = 'generic green 0201 LED'
    candidate['marking']['evidence'] = {'file': 'green'}
    manifest = {'renderer_source_sha256': 'reviewed-renderer', 'artifacts': artifacts,
                'reused_image': {'source_part': source_part,
                                 'source_manifest_sha256': hashlib.sha256(source_path.read_bytes()).hexdigest()}}
    assert populate.reused_image_valid(manifest, candidate, studio)
    changed_model = copy.deepcopy(candidate)
    changed_model['model']['sha256'] = 'different-model'
    assert not populate.reused_image_valid(manifest, changed_model, studio)
    tinted = copy.deepcopy(candidate)
    tinted['represented_mpn'] = 'generic green tint 0201 LED'
    assert not populate.reused_image_valid(manifest, tinted, studio)
    generic_0402 = copy.deepcopy(candidate)
    generic_0402['package'] = '0402_metric_1005Metric'
    generic_0402['represented_mpn'] = 'generic 0402 LED, emission colour unspecified'
    populate.unmarked_visual_recipe(generic_0402)
    named_blue = copy.deepcopy(generic_0402)
    named_blue['represented_mpn'] = 'generic blue 0402 LED'
    try:
        populate.unmarked_visual_recipe(named_blue)
    except ValueError:
        pass
    else:
        raise AssertionError('The named 0402 blue entry must not use generic image reuse')
    generic_0603 = copy.deepcopy(candidate)
    generic_0603['package'] = '0603_metric_1608Metric'
    generic_0603['represented_mpn'] = 'generic blue 0603 LED'
    populate.unmarked_visual_recipe(generic_0603)
    named_0603 = copy.deepcopy(generic_0603)
    named_0603['represented_mpn'] = 'KT-0603B'
    try:
        populate.unmarked_visual_recipe(named_0603)
    except ValueError:
        pass
    else:
        raise AssertionError('A manufacturer-specific 0603 LED must not use generic image reuse')
    generic_0805 = copy.deepcopy(candidate)
    generic_0805['package'] = '0805_metric_2012Metric'
    generic_0805['represented_mpn'] = 'generic blue 0805 LED'
    populate.unmarked_visual_recipe(generic_0805)
    generic_0805['represented_mpn'] = 'generic blue tint 0805 LED'
    try:
        populate.unmarked_visual_recipe(generic_0805)
    except ValueError:
        pass
    else:
        raise AssertionError('A tinted 0805 LED must not use generic image reuse')
    generic_1206 = copy.deepcopy(candidate)
    generic_1206['package'] = '1206_metric_3216Metric'
    generic_1206['represented_mpn'] = 'generic green 1206 LED'
    populate.unmarked_visual_recipe(generic_1206)
    generic_1206['represented_manufacturer'] = 'Named manufacturer'
    try:
        populate.unmarked_visual_recipe(generic_1206)
    except ValueError:
        pass
    else:
        raise AssertionError('A manufacturer-specific 1206 LED must not use generic image reuse')
    (source_dir / 'render.png').write_bytes(b'changed image')
    assert not populate.reused_image_valid(manifest, candidate, studio)
