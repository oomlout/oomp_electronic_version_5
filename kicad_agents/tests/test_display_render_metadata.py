import hashlib
import json

import pytest
import working_oomp_populate_display_render as metadata


@pytest.fixture
def published(tmp_path, monkeypatch):
    monkeypatch.setattr(metadata, 'ROOT', tmp_path)
    root = tmp_path / 'source_file/display_render'
    root.mkdir(parents=True)
    evidence = tmp_path / 'evidence.md'
    evidence.write_text('Reviewed marking evidence')
    evidence_hash = hashlib.sha256(evidence.read_bytes()).hexdigest()
    recipe = {'appearance_status': 'Display approximation.',
              'marking': {'appearance_status': 'Verified code, approximate font.',
                          'evidence': {'file': 'evidence.md', 'sha256': evidence_hash}},
              'model': {'copyright': 'Test model author', 'source_url': 'https://example.com/model', 'license': 'Test'}}
    (root / 'recipes.json').write_text(json.dumps({'part': recipe}))
    (root / 'studio.json').write_text('{}')
    code = tmp_path / 'kicad_agents/display_render.py'
    code.parent.mkdir()
    code.write_text('test renderer')
    output = tmp_path / 'parts/part/data/display_render'
    output.mkdir(parents=True)
    artifacts = {}
    for name in ('render.png', 'preview.webp'):
        (output / name).write_bytes(b'test image bytes')
        artifacts[name] = {'sha256': hashlib.sha256((output/name).read_bytes()).hexdigest()}
    manifest = {'part_id': 'part', 'recipe_sha256': hashlib.sha256(json.dumps(recipe, sort_keys=True).encode()).hexdigest(),
                'studio': {}, 'renderer_source_sha256': hashlib.sha256(code.read_bytes()).hexdigest(),
                'artifacts': artifacts, 'marking': {'text': '01C', 'evidence_sha256': evidence_hash}}
    (output / 'manifest.json').write_text(json.dumps(manifest))
    return tmp_path, output


def test_current_render_is_advertised_without_renderer_dependencies(published):
    parts = {'part': {}, 'unrelated': {}}
    metadata.apply_extras(parts)
    assert parts['part']['display_render']['marking'] == '01C'
    assert parts['unrelated'] == {}


def test_older_render_remains_valid_only_with_matching_archived_renderer(published):
    root, output = published
    renderer = root / 'kicad_agents/display_render.py'
    old = renderer.read_bytes()
    old_hash = hashlib.sha256(old).hexdigest()
    archive = root / 'source_file/display_render/renderer_versions' / (old_hash + '.py')
    archive.parent.mkdir(parents=True)
    archive.write_bytes(old)
    renderer.write_text('new renderer')
    parts = {'part': {}}
    metadata.apply_extras(parts)
    assert parts['part']['display_render']['marking'] == '01C'
    archive.write_text('tampered archive')
    metadata.apply_extras(parts)
    assert not parts['part'].get('display_render')


def test_composite_requires_current_compositor_and_intact_shared_passes(published):
    root, output = published
    manifest_path = output / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    recipe = json.loads((root / 'source_file/display_render/recipes.json').read_text())['part']
    code = root / 'kicad_agents/display_render_composite.py'
    code.write_text('reviewed compositor')
    code_hash = hashlib.sha256(code.read_bytes()).hexdigest()
    folder = root / 'source_file/display_render/masters/test'
    folder.mkdir(parents=True)
    artifacts = {}
    for name in ('body.png', 'ink.png'):
        (folder/name).write_bytes(name.encode())
        artifacts[name] = {'sha256': hashlib.sha256((folder/name).read_bytes()).hexdigest(),
                           'bytes': (folder/name).stat().st_size}
    master = {'inputs': {'model': recipe['model'], 'family': recipe.get('family'),
                         'disable_bump_for': [], 'studio': {}, 'pixels': 1400, 'samples': 256,
                         'renderer_sha256': manifest['renderer_source_sha256'], 'builder_sha256': code_hash},
              'artifacts': artifacts}
    master_path = folder/'manifest.json'
    master_path.write_text(json.dumps(master))
    manifest['composite'] = {'compositor_source_sha256': code_hash,
                             'master_manifest': master_path.relative_to(root).as_posix(),
                             'master_manifest_sha256': hashlib.sha256(master_path.read_bytes()).hexdigest()}
    manifest_path.write_text(json.dumps(manifest))
    parts = {'part': {}}
    metadata.apply_extras(parts)
    assert 'composited' in parts['part']['display_render']['description']
    (folder/'ink.png').write_bytes(b'changed')
    metadata.apply_extras(parts)
    assert not parts['part'].get('display_render')


def test_composite_orientation_source_must_match_or_be_archived(published):
    root, output = published
    recipe = json.loads((root / 'source_file/display_render/recipes.json').read_text())['part']
    manifest = json.loads((output / 'manifest.json').read_text())
    compositor = root / 'kicad_agents/display_render_composite.py'
    compositor.write_text('reviewed compositor')
    compositor_hash = hashlib.sha256(compositor.read_bytes()).hexdigest()
    orientation = root / 'kicad_agents/display_render_orientation.py'
    orientation.write_text('reviewed orientation')
    orientation_hash = hashlib.sha256(orientation.read_bytes()).hexdigest()
    folder = root / 'source_file/display_render/masters/oriented'
    folder.mkdir(parents=True)
    artifacts = {}
    for name in ('body.png', 'ink.png'):
        (folder / name).write_bytes(name.encode())
        artifacts[name] = {'bytes': (folder / name).stat().st_size,
                           'sha256': hashlib.sha256((folder / name).read_bytes()).hexdigest()}
    master = {'inputs': {'model': recipe['model'], 'family': recipe.get('family'), 'studio': {},
                         'pixels': 1400, 'samples': 256,
                         'renderer_sha256': manifest['renderer_source_sha256'],
                         'builder_sha256': compositor_hash,
                         'orientation_adapter_sha256': orientation_hash}, 'artifacts': artifacts}
    master_path = folder / 'manifest.json'
    master_path.write_text(json.dumps(master))
    manifest['composite'] = {'compositor_source_sha256': compositor_hash,
                             'master_manifest': master_path.relative_to(root).as_posix(),
                             'master_manifest_sha256': hashlib.sha256(master_path.read_bytes()).hexdigest()}
    assert metadata.composite_sources_valid(manifest, recipe, {})
    orientation.write_text('changed orientation')
    assert not metadata.composite_sources_valid(manifest, recipe, {})
    archive = root / 'source_file/display_render/renderer_versions' / (orientation_hash + '.py')
    archive.parent.mkdir(parents=True)
    archive.write_text('reviewed orientation')
    assert metadata.composite_sources_valid(manifest, recipe, {})
    model_adapter = root / 'kicad_agents/display_render_infineon_irfp4310z.py'
    model_adapter.write_text('reviewed model adapter')
    model_hash = hashlib.sha256(model_adapter.read_bytes()).hexdigest()
    master['inputs']['model_adapter_sha256'] = model_hash
    master_path.write_text(json.dumps(master))
    manifest['composite']['master_manifest_sha256'] = hashlib.sha256(master_path.read_bytes()).hexdigest()
    manifest['model'] = {'adapter_sha256': model_hash}
    assert metadata.composite_sources_valid(manifest, recipe, {})
    model_adapter.write_text('changed model adapter')
    assert not metadata.composite_sources_valid(manifest, recipe, {})
    (archive.parent / (model_hash + '.py')).write_text('reviewed model adapter')
    assert metadata.composite_sources_valid(manifest, recipe, {})
    manifest['model']['adapter_sha256'] = '0' * 64
    assert not metadata.composite_sources_valid(manifest, recipe, {})


@pytest.mark.parametrize('change', ['image', 'recipe', 'renderer', 'evidence'])
def test_stale_or_corrupt_render_is_not_advertised(published, change):
    root, output = published
    if change == 'image':
        (output / 'render.png').write_bytes(b'corrupted')
    elif change == 'recipe':
        path = root / 'source_file/display_render/recipes.json'
        recipe = json.loads(path.read_text())
        recipe['part']['appearance_status'] = 'New recipe'
        path.write_text(json.dumps(recipe))
    elif change == 'renderer':
        (root / 'kicad_agents/display_render.py').write_text('changed renderer')
    else:
        (root / 'evidence.md').write_text('Changed evidence')
    parts = {'part': {}}
    metadata.apply_extras(parts)
    assert not parts['part'].get('display_render')


def test_character_underline_requires_renderer_support(published):
    root, output = published
    recipe_path = root / 'source_file/display_render/recipes.json'
    recipes = json.loads(recipe_path.read_text())
    recipes['part']['marking']['underline_character'] = 1
    recipe_path.write_text(json.dumps(recipes))
    manifest_path = output / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    manifest['recipe_sha256'] = hashlib.sha256(json.dumps(recipes['part'], sort_keys=True).encode()).hexdigest()
    manifest_path.write_text(json.dumps(manifest))
    parts = {'part': {}}
    metadata.apply_extras(parts)
    assert not parts['part'].get('display_render')
    renderer = root / 'kicad_agents/display_render.py'
    renderer.write_text("character = marking.get('underline_character')")
    manifest['renderer_source_sha256'] = hashlib.sha256(renderer.read_bytes()).hexdigest()
    manifest_path.write_text(json.dumps(manifest))
    metadata.apply_extras(parts)
    assert parts['part']['display_render']
