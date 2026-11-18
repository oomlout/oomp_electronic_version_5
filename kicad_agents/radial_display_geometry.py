"""Geometry helpers for reviewed display-only radial capacitor models.

This module is not yet wired into the renderer. Select body regions and
thresholds from inspected source geometry; never infer them from a footprint.
"""
import numpy as np


def straight_sleeve_triangles(vertices, triangles, center_xy, radius, lower_z, upper_z, tolerance=.05):
    """Select triangles wholly on the reviewed cylindrical straight sleeve."""
    v = np.asarray(vertices, dtype=float)
    tri = np.asarray(triangles, dtype=int)
    center = np.asarray(center_xy, dtype=float)
    if (v.ndim != 2 or v.shape[1] != 3 or tri.ndim != 2 or tri.shape[1] != 3
        or center.shape != (2,) or not np.isfinite(v).all() or not np.isfinite(center).all()
        or not np.isfinite([radius, lower_z, upper_z, tolerance]).all()
        or radius <= 0 or tolerance <= 0 or upper_z <= lower_z
        or tri.size == 0 or tri.min() < 0 or tri.max() >= len(v)):
        raise ValueError('Invalid reviewed sleeve geometry')
    points = v[tri]
    radii = np.linalg.norm(points[:, :, :2] - center, axis=2)
    on_cylinder = np.all(np.abs(radii - radius) <= tolerance, axis=1)
    in_height = np.all((points[:, :, 2] >= lower_z - 1e-6)
                       & (points[:, :, 2] <= upper_z + 1e-6), axis=1)
    return on_cylinder & in_height


def stretch_sleeve(vertices, normals, triangles, lower_z, upper_z, extra_height):
    """Lengthen the straight sleeve while preserving leads and end details.

    Triangles must not straddle either deformation boundary. This prevents a
    silently bent face; split/re-tessellate geometry where necessary. Normals
    are transformed using the local inverse transpose.
    """
    v = np.asarray(vertices, dtype=float)
    n = np.asarray(normals, dtype=float)
    tri = np.asarray(triangles, dtype=int)
    if (v.ndim != 2 or v.shape[1] != 3 or n.shape != v.shape or tri.ndim != 2
        or tri.shape[1] != 3 or not np.isfinite(v).all() or not np.isfinite(n).all()
        or not np.isfinite([lower_z, upper_z, extra_height]).all()
        or upper_z <= lower_z or extra_height < 0 or tri.size == 0
        or tri.min() < 0 or tri.max() >= len(v)):
        raise ValueError('Invalid reviewed radial mesh or deformation')
    zs = v[tri, 2]
    for boundary in (lower_z, upper_z):
        if np.any((zs.min(axis=1) < boundary - 1e-7) & (zs.max(axis=1) > boundary + 1e-7)):
            raise ValueError('Triangle crosses a sleeve deformation boundary')
    scale = 1 + extra_height / (upper_z - lower_z)
    out = v.copy()
    middle = (v[:, 2] > lower_z) & (v[:, 2] < upper_z)
    above = v[:, 2] >= upper_z
    out[middle, 2] = lower_z + (v[middle, 2] - lower_z) * scale
    out[above, 2] = v[above, 2] + extra_height
    # Boundary vertices can belong to a stretched face even when their
    # position lies exactly on the boundary. Use incident triangles to select
    # the inverse-transpose transform; reject ambiguous sloped shared normals.
    transformed = n.copy()
    centers = zs.mean(axis=1)
    used_middle = np.zeros(len(v), dtype=bool)
    used_outer = np.zeros(len(v), dtype=bool)
    np.logical_or.at(used_middle, tri.ravel(), np.repeat((centers > lower_z) & (centers < upper_z), 3))
    np.logical_or.at(used_outer, tri.ravel(), np.repeat((centers <= lower_z) | (centers >= upper_z), 3))
    if np.any(used_middle & used_outer & (np.abs(n[:, 2]) > 1e-7)):
        raise ValueError('Split shared sloped normals at deformation boundaries')
    transformed[used_middle, 2] /= scale
    lengths = np.linalg.norm(transformed, axis=1)
    if np.any(lengths <= 0) or not np.isfinite(lengths).all():
        raise ValueError('Invalid radial mesh normal')
    transformed /= lengths[:, None]
    return out, transformed


def sleeve_triangle_uv(vertices, triangles, center_xy, bottom_z, top_z, seam_angle=0.0):
    """Return per-corner cylindrical UVs with each triangle unwrapped at seam.

    The caller must assign the UVs only to reviewed sleeve surfaces and use a
    repeating texture. Per-corner UVs permit the same vertex on either side of
    the seam to carry different coordinates.
    """
    v = np.asarray(vertices, dtype=float)
    tri = np.asarray(triangles, dtype=int)
    center = np.asarray(center_xy, dtype=float)
    if (v.ndim != 2 or v.shape[1] != 3 or tri.ndim != 2 or tri.shape[1] != 3
        or center.shape != (2,) or not np.isfinite(v).all() or not np.isfinite(center).all()
        or not np.isfinite([bottom_z, top_z, seam_angle]).all() or top_z <= bottom_z
        or tri.size == 0 or tri.min() < 0 or tri.max() >= len(v)):
        raise ValueError('Invalid cylindrical mapping input')
    points = v[tri]
    radial = points[:, :, :2] - center
    if np.any(np.linalg.norm(radial, axis=2) < 1e-8):
        raise ValueError('Cylindrical mapping is undefined on the axis')
    u = np.mod((np.arctan2(radial[:, :, 1], radial[:, :, 0]) - seam_angle) / (2 * np.pi), 1.0)
    crossing = np.ptp(u, axis=1) > .5
    u[crossing] += (u[crossing] < .5)
    if np.any(np.ptp(u, axis=1) > .5 + 1e-7):
        raise ValueError('Triangle spans too much of the cylinder')
    height = (points[:, :, 2] - bottom_z) / (top_z - bottom_z)
    if np.any(height < -1e-6) or np.any(height > 1 + 1e-6):
        raise ValueError('Sleeve UV extends beyond reviewed height')
    return np.stack((u, height), axis=2)
