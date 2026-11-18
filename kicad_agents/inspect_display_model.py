"""Inspect a local KiCad STEP model before authoring a display recipe.

Colours are reported as authored sRGB values; assigning their material roles
still requires visual and source review. This command writes no model or image.
"""
import argparse
from collections import Counter
import json

from kicad_agents.display_render import digest, locate_model


def inspect(relative_path, model_root=None):
    import cadquery as cq
    from OCP.IFSelect import IFSelect_RetDone
    from OCP.Quantity import Quantity_Color, Quantity_TOC_sRGB
    from OCP.STEPCAFControl import STEPCAFControl_Reader
    from OCP.TCollection import TCollection_ExtendedString
    from OCP.TDF import TDF_LabelSequence
    from OCP.TDocStd import TDocStd_Document
    from OCP.XCAFDoc import XCAFDoc_ColorType, XCAFDoc_DocumentTool

    path = locate_model(relative_path, model_root)
    doc = TDocStd_Document(TCollection_ExtendedString('display-model-inspection'))
    reader = STEPCAFControl_Reader()
    reader.SetColorMode(True)
    if reader.ReadFile(str(path)) != IFSelect_RetDone or not reader.Transfer(doc):
        raise ValueError(f'Cannot read STEP model: {path}')
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    colours = XCAFDoc_DocumentTool.ColorTool_s(doc.Main())
    labels = TDF_LabelSequence()
    shapes.GetFreeShapes(labels)
    roots = []
    for index in range(1, labels.Length() + 1):
        shape = cq.Shape.cast(shapes.GetShape_s(labels.Value(index)))
        box = shape.BoundingBox()
        counts = Counter()
        for face in shape.Faces():
            colour = Quantity_Color()
            if colours.GetColor(face.wrapped, XCAFDoc_ColorType.XCAFDoc_ColorSurf, colour):
                key = ','.join(f'{v:.3f}' for v in colour.Values(Quantity_TOC_sRGB))
            else:
                key = '(no face colour)'
            counts[key] += 1
        roots.append({'valid': shape.isValid(), 'bounds_mm': [box.xlen, box.ylen, box.zlen],
                      'face_colours': dict(counts)})
    return {'relative_path': relative_path, 'sha256': digest(path), 'roots': roots}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('relative_path')
    parser.add_argument('--model-root')
    args = parser.parse_args()
    print(json.dumps(inspect(args.relative_path, args.model_root), indent=2))


if __name__ == '__main__':
    main()
