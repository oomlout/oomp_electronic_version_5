import hashlib
import json

import working_oomp_populate_display_render as metadata


def digest(data):
    return hashlib.sha256(data).hexdigest()


def test_reuse_requires_identical_visual_inputs_and_undamaged_source(tmp_path, monkeypatch):
    monkeypatch.setattr(metadata, 'ROOT', tmp_path)
    monkeypatch.setattr(metadata, 'renderer_source_available', lambda value: value == 'renderer')
    recipe = {'family': 'chip_resistor', 'model': {'sha256': 'model'}, 'output': {'pixels': 1400},
              'marking': {'policy': 'none', 'evidence': {'file': 'one'}}, 'represented_mpn': 'one'}
    target_recipe = {**recipe, 'represented_mpn': 'two', 'marking': {'policy': 'none', 'evidence': {'file': 'two'}}}
    folder = tmp_path / 'parts/electronic_source/data/display_render'
    folder.mkdir(parents=True)
    artifacts = {}
    for name in ('render.png', 'preview.webp'):
        data = name.encode()
        (folder / name).write_bytes(data)
        artifacts[name] = {'sha256': digest(data), 'bytes': len(data)}
    source = {'part_id': 'electronic_source', 'recipe': recipe, 'studio': {'light': 1},
              'renderer_source_sha256': 'renderer', 'marking': {'text': ''}, 'artifacts': artifacts}
    raw = json.dumps(source).encode()
    (folder / 'manifest.json').write_bytes(raw)
    manifest = {'reused_image': {'source_part': 'electronic_source', 'source_manifest_sha256': digest(raw)},
                'renderer_source_sha256': 'renderer', 'artifacts': artifacts}
    assert metadata.reused_image_valid(manifest, target_recipe, {'light': 1})
    assert not metadata.reused_image_valid(manifest, {**target_recipe, 'output': {'pixels': 700}}, {'light': 1})
    assert not metadata.reused_image_valid(manifest, {**target_recipe, 'marking': {'policy': 'literal'}}, {'light': 1})
    (folder / 'render.png').write_bytes(b'damaged')
    assert not metadata.reused_image_valid(manifest, target_recipe, {'light': 1})
