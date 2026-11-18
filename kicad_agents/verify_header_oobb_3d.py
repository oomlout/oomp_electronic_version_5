"""Audit exported headers, including the orientation of their snap grooves."""
import json
import numpy as np
import trimesh
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.TopAbs import TopAbs_IN, TopAbs_OUT
from OCP.gp import gp_Pnt
from kicad_agents.header_oobb_3d import ROOT, VARIANTS, build, positions, stock_id, long_id, variant_id, read_step


def main():
    body, _ = build(2, long=True)
    # Between cells, the front/back surfaces stay solid; top/bottom are notched.
    for point, expected in [((0, 1.2, 0), TopAbs_IN), ((0, -1.2, 0), TopAbs_IN),
                            ((0, 0, 1.2), TopAbs_OUT), ((0, 0, -1.2), TopAbs_OUT)]:
        assert BRepClass3d_SolidClassifier(body, gp_Pnt(*point), 1e-7).State() == expected, point
    models = [(stock_id(n), n, (), False) for n in range(1, 41)]
    models += [(long_id(n), n, (), False) for n in range(1, 41)]
    models += [(variant_id(k), v['count'], v['removed'], v.get('vertical', False)) for k, v in VARIANTS.items()]
    for identity, count, removed, vertical in models:
        data = ROOT / 'parts' / identity / 'data'
        body = trimesh.load_mesh(data / 'model_3d_body.stl')
        pins = trimesh.load_mesh(data / 'model_3d_pins.stl').split()
        assert body.is_watertight and body.volume > 0, identity
        assert len(pins) == count-len(removed), identity
        assert all(p.is_watertight and p.volume > 0 for p in pins), identity
        expected = sorted(x for i, x in positions(count).items() if i not in removed)
        actual = sorted(p.centroid[2 if vertical else 0] for p in pins)
        assert np.allclose(actual, expected, atol=1e-4), identity
        long = "header_long_" in identity or "header_oobb_" in identity
        insulator = 2.5 if long else 2.54
        envelope = [insulator, insulator, count*2.54] if vertical else [count*2.54, insulator, insulator]
        if long:
            # Every individual contact must be centred and extend 6.25 mm from both faces.
            for pin in pins:
                assert np.allclose(pin.bounds[:, 1], [-7.5, 7.5], atol=1e-4), identity
                assert np.allclose([-pin.bounds[0, 1]-insulator/2, pin.bounds[1, 1]-insulator/2], [6.25, 6.25], atol=1e-4), identity
        assert np.allclose(body.extents, envelope, atol=1e-4), identity
        for name in ('model_3d.step', 'model_3d_body.stl', 'model_3d_pins.stl', 'model_3d_source.json'):
            assert (data/name).read_bytes() == (ROOT/'parts_source'/identity/name).read_bytes(), identity
        provenance = json.loads((data/'model_3d_source.json').read_text())
        assert provenance['removed'] == list(removed), identity
        if long:
            import yaml, hashlib
            metadata = yaml.safe_load((data.parent/'working.yaml').read_text(encoding='utf-8'))
            assert metadata['header_stock_type'] == 'header_long', identity
            if 'header_oobb_' in identity:
                assert metadata['parent_header_id'] == long_id(count), identity
            assert provenance['exposed_pin_ends_mm'] == [6.25, 6.25], identity
            assert hashlib.sha256((data/'datasheet.pdf').read_bytes()).hexdigest() == provenance['datasheet_sha256'], identity
        if vertical:
            from OCP.BRepCheck import BRepCheck_Analyzer
            from OCP.TopExp import TopExp_Explorer
            from OCP.TopAbs import TopAbs_SOLID
            assembly = read_step(data/'model_3d_3_strip.step')
            assert BRepCheck_Analyzer(assembly).IsValid(), identity
            iterator, solids = TopExp_Explorer(assembly, TopAbs_SOLID), 0
            while iterator.More():
                solids += 1
                iterator.Next()
            assert solids == 3 + 3*(count-len(removed)), identity
            pins = trimesh.load_mesh(data/'model_3d_3_strip_pins.stl').split()
            assert len(pins) == 3*(count-len(removed)), identity
            assert np.allclose(sorted(set(round(p.centroid[0], 4) for p in pins)), [-2.54, 0, 2.54]), identity
            for name in ('model_3d_3_strip.step', 'model_3d_3_strip_body.stl', 'model_3d_3_strip_pins.stl'):
                assert (data/name).read_bytes() == (ROOT/'parts_source'/identity/name).read_bytes(), identity
    print(f'PASS: {len(models)} headers, retained contact locations, watertight solids, source copies and top/bottom grooves.')


if __name__ == '__main__':
    main()
