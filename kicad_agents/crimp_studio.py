"""Photographic studio scene for the connector STEP previews."""

from pathlib import Path
from tempfile import TemporaryDirectory

import cv2
import drjit as dr
import mitsuba as mi
import numpy as np
from PIL import Image


def material_for(row):
    if row["role"] == "cable_housing":
        if row["taxonomy"]["taxonomy_7"] == "white":
            polymer = row["details"]["housing_material"]
            return f"Natural white {polymer}", {
                "type": "roughplastic", "alpha": 0.24, "int_ior": 1.52,
                "nonlinear": True, "diffuse_reflectance": rgb(0.74, 0.70, 0.63),
            }
        return "Satin black PPE+PS", {
            "type": "roughplastic", "alpha": 0.18, "int_ior": 1.53,
            "nonlinear": True, "diffuse_reflectance": rgb(0.035, 0.039, 0.047),
        }
    gold = row["taxonomy"]["taxonomy_9"] == "gold"
    color = (0.83, 0.60, 0.30) if gold else (0.34, 0.36, 0.39)
    return ("Satin gold" if gold else "Satin tin plating"), {
        "type": "principled", "base_color": rgb(*color),
        "metallic": 1.0, "roughness": 0.24, "anisotropic": 0.18,
    }


def rgb(red, green, blue):
    return {"type": "rgb", "value": [red, green, blue]}


def write_mesh(shape, path):
    vertices, triangles = shape.tessellate(0.015, 0.10)
    points = np.array([vertex.toTuple() for vertex in vertices])
    lower, upper = points.min(axis=0), points.max(axis=0)
    origin = (lower + upper) / 2
    origin[2] = lower[2]
    # Normalize the scene for consistent lighting and framing at every part size.
    points = (points - origin) / np.max(upper - lower)
    with path.open("w", encoding="ascii") as obj:
        for x, y, z in points:
            obj.write(f"v {x:.8f} {y:.8f} {z+0.001:.8f}\n")
        for a, b, c in triangles:
            obj.write(f"f {a+1} {b+1} {c+1}\n")
    return float(np.max(points[:, 2]))


def area_light(origin, target, extent, radiance):
    transform = mi.ScalarTransform4f().look_at(origin=origin, target=target, up=[0, 0, 1])
    return {
        "type": "rectangle",
        "to_world": transform @ mi.ScalarTransform4f().scale([*extent, 1]),
        "emitter": {"type": "area", "radiance": rgb(*radiance)},
    }


def render_studio(shape, row, destination, samples=96, resolution=1024):
    """Path trace the exported solid with softboxes, floor bounce and contact shadows."""
    if "llvm_ad_rgb" in mi.variants() and dr.has_backend(dr.JitBackend.LLVM):
        mi.set_variant("llvm_ad_rgb")
    else:
        mi.set_variant("scalar_rgb")
    material_name, material = material_for(row)
    housing = row["role"] == "cable_housing"
    white = housing and row["taxonomy"]["taxonomy_7"] == "white"
    camera = [1.55, -2.40, 1.43] if housing else [-1.45, -2.55, 1.20]
    with TemporaryDirectory(prefix="crimp-studio-") as scratch:
        mesh_path = Path(scratch) / "part.obj"
        height = write_mesh(shape, mesh_path)
        target = [0, 0, height * 0.38]
        scene = mi.load_dict({
            "type": "scene",
            "integrator": {"type": "path", "max_depth": 6},
            "camera": {
                "type": "perspective", "fov": 26, "fov_axis": "x",
                "to_world": mi.ScalarTransform4f().look_at(origin=camera, target=target, up=[0, 0, 1]),
                "sampler": {"type": "independent", "sample_count": samples},
                "film": {
                    "type": "hdrfilm", "width": resolution, "height": resolution,
                    "rfilter": {"type": "tent"},
                },
            },
            "part": {"type": "obj", "filename": str(mesh_path), "face_normals": True, "bsdf": material},
            "sweep": {
                "type": "rectangle", "to_world": mi.ScalarTransform4f().scale([30, 30, 1]),
                "bsdf": {"type": "diffuse", "reflectance": (
                    rgb(0.22, 0.26, 0.31) if white else rgb(0.76, 0.77, 0.79)
                )},
            },
            "ambient": {"type": "constant", "radiance": rgb(0.31, 0.33, 0.36)},
            "key": area_light([-1.4, -1.8, 2.0], target, [0.95, 0.62], [4.0, 3.85, 3.6]),
            "fill": area_light([1.9, -0.65, 1.15], target, [0.55, 0.85], [2.0, 2.2, 2.55]),
            "rim": area_light([0.35, 1.55, 1.45], target, [0.95, 0.34], [5.2, 5.5, 6.0]),
        })
        linear = np.asarray(mi.render(scene, seed=19, spp=samples))
    # Filmic highlight rolloff, then display sRGB.
    linear = 1.6 * np.maximum(linear, 0)
    mapped = np.clip(linear * (2.51 * linear + 0.03) /
                     (linear * (2.43 * linear + 0.59) + 0.14), 0, 1)
    srgb = np.where(mapped <= 0.0031308, 12.92 * mapped, 1.055 * mapped**(1 / 2.4) - 0.055)
    pixels = np.rint(srgb * 255).astype(np.uint8)
    # Smooth sample noise while retaining the edges of the small terminals.
    bgr = cv2.cvtColor(pixels, cv2.COLOR_RGB2BGR)
    denoised = cv2.fastNlMeansDenoisingColored(bgr, None, 4 if housing else 6, 4, 7, 15)
    Image.fromarray(cv2.cvtColor(denoised, cv2.COLOR_BGR2RGB)).save(destination, optimize=True)
    return {
        "renderer": "Mitsuba 3 path tracer", "material": material_name,
        "samples_per_pixel": samples, "size_px": [resolution, resolution],
        "studio_reference": "https://github.com/oomlout/oomp_hardware_screw_version_5/blob/main/THREE_D_MODELS.md",
    }
