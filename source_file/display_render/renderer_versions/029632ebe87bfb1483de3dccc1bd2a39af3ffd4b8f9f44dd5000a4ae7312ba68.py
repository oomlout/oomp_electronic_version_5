"""Reviewed rigid orientations for display-only KiCad package meshes.

These transforms change the presentation pose, never the source STEP or a PCB
footprint. Apply them after validating the untransformed model and its colours.
"""
from __future__ import annotations


def orient_to220_face_up(groups, lower, upper):
    """Lay the KiCad TO-220-3 vertical package with its front (-Y) face up.

    The proper rotation maps (x, y, z) to (-z, x, -y). Normals receive the
    same rotation. Return bounds for the entire transformed source envelope.
    """
    import numpy as np

    matrix = np.array([[0., 0., -1.], [1., 0., 0.], [0., -1., 0.]])
    low, high = np.asarray(lower, dtype=float), np.asarray(upper, dtype=float)
    if (low.shape != (3,) or high.shape != (3,) or not np.isfinite(low).all()
            or not np.isfinite(high).all() or np.any(high <= low)):
        raise ValueError('Orientation requires finite, nonempty 3D bounds')
    for group in groups.values():
        vertices = np.asarray(group['vertices'], dtype=float)
        normals = np.asarray(group['normals'], dtype=float)
        if (vertices.ndim != 2 or vertices.shape[1] != 3 or normals.shape != vertices.shape
                or not np.isfinite(vertices).all() or not np.isfinite(normals).all()):
            raise ValueError('Orientation requires finite 3D vertices and matching normals')
        group['vertices'] = (vertices @ matrix.T).tolist()
        group['normals'] = (normals @ matrix.T).tolist()
    corners = np.array([[x, y, z] for x in (low[0], high[0])
                        for y in (low[1], high[1]) for z in (low[2], high[2])]) @ matrix.T
    return corners.min(axis=0), corners.max(axis=0)
