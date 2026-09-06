"""Read routed copper and draw explorer overlays in KiCad board millimetres.

Format reference: https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/
No routing, zone filling or connectivity inference happens here: the saved PCB
net assignments are authoritative. Unfilled zone outlines are never copper.
"""

import copy
import html
import math

from kicad_agents.geometry import _circle_from_three_points, transform_point
from kicad_agents.sexpr import as_float, child, children, value, values


def point(node, key):
    coordinates = child(node, key) or [key, 0, 0]
    return [as_float(coordinates[1]), as_float(coordinates[2])]


def net_name(node, net_names):
    net = child(node, "net")
    if not net or len(net) < 2:
        return ""
    if len(net) >= 3:
        return str(net[2])
    token = str(net[1])
    # Older boards use integer codes; newer boards store the name directly.
    # Only consult the table when one exists, so a literal modern net "0"
    # remains valid while old net code 0 (the empty net) stays unconnected.
    if net_names:
        return net_names.get(token, "")
    return token


def _layers(node):
    layers = values(node, "layers")
    if not layers:
        layer = value(node, "layer", "")
        if layer:
            layers.append(layer)
    return layers


def _points(node):
    return [point_record[1:3] for point_record in children(child(node, "pts") or ["pts"], "xy")]


def extract_copper(root):
    net_names = {}
    for net in children(root, "net"):
        if len(net) >= 3:
            net_names[str(net[1])] = str(net[2])
    layers = []
    for layer in (child(root, "layers") or ["layers"])[1:]:
        if isinstance(layer, list) and len(layer) > 1 and str(layer[1]).endswith(".Cu"):
            layers.append(str(layer[1]))
    tracks = []
    for kind in ["segment", "arc"]:
        for node in children(root, kind):
            record = {
                "kind": kind, "start": point(node, "start"), "end": point(node, "end"),
                "width": as_float(value(node, "width")), "layers": _layers(node),
                "net": net_name(node, net_names),
                "uuid": value(node, "uuid") or value(node, "tstamp"),
            }
            if kind == "arc":
                record["mid"] = point(node, "mid")
            tracks.append(record)
    vias = []
    for node in children(root, "via"):
        via_layers = _layers(node)
        # A via's layer pair denotes its span, including any internal layers.
        if len(via_layers) == 2 and all(layer in layers for layer in via_layers):
            start = layers.index(via_layers[0])
            end = layers.index(via_layers[1])
            via_layers = layers[min(start, end):max(start, end) + 1]
        vias.append({
            "kind": "via", "position": point(node, "at"),
            "size": as_float(value(node, "size")), "drill": as_float(value(node, "drill")),
            "layers": via_layers, "net": net_name(node, net_names),
            "uuid": value(node, "uuid") or value(node, "tstamp"),
        })
    zones = []
    warnings = []
    for node in children(root, "zone"):
        if child(node, "keepout") is not None:
            continue
        zone_layers = _layers(node)
        filled = children(node, "filled_polygon")
        if not filled and any(layer.endswith(".Cu") for layer in zone_layers):
            warnings.append("A copper zone has no saved fill; refill in KiCad to display it.")
        for polygon in filled:
            polygon_layers = _layers(polygon) or zone_layers
            if not any(layer.endswith(".Cu") for layer in polygon_layers):
                continue
            zones.append({
                "kind": "zone", "points": [[float(x), float(y)] for x, y in _points(polygon)],
                "layers": polygon_layers, "net": net_name(node, net_names),
                "uuid": value(node, "uuid") or value(node, "tstamp"),
            })
    pads = []
    for footprint in children(root, "footprint"):
        reference = ""
        for prop in children(footprint, "property"):
            if len(prop) >= 3 and prop[1] == "Reference":
                reference = prop[2]
        if not reference:
            for text in children(footprint, "fp_text"):
                if len(text) >= 3 and text[1] == "reference":
                    reference = text[2]
        origin = point(footprint, "at")
        at = child(footprint, "at") or []
        rotation = -as_float(at[3]) if len(at) > 3 else 0
        for index, pad in enumerate(children(footprint, "pad")):
            pad_layers = _layers(pad)
            if pad[2] == "np_thru_hole" or not any(layer.endswith(".Cu") for layer in pad_layers):
                continue
            if "*.Cu" in pad_layers:
                pad_layers = list(layers)
            elif "F&B.Cu" in pad_layers:
                pad_layers = ["F.Cu", "B.Cu"]
            else:
                pad_layers = [layer for layer in pad_layers if layer.endswith(".Cu")]
            pad_at = child(pad, "at") or []
            # The centre is footprint-local; the pad angle is already absolute
            # in the PCB file. Do not add the footprint angle a second time.
            pad_rotation = -as_float(pad_at[3]) if len(pad_at) > 3 else 0
            center = transform_point(point(pad, "at"), origin, rotation)
            record = {
                "kind": "pad", "reference": reference, "number": str(pad[1]), "pad_index": index,
                "position": [round(center[0], 6), round(center[1], 6)],
                "rotation": pad_rotation, "size": point(pad, "size"), "shape": str(pad[3]),
                "layers": pad_layers, "net": net_name(pad, net_names),
                "roundrect_rratio": as_float(value(pad, "roundrect_rratio", 0)),
                "anchor": value(child(pad, "options") or ["options"], "anchor", "rect"),
                "primitives": copy.deepcopy((child(pad, "primitives") or ["primitives"])[1:]),
            }
            drill = child(pad, "drill")
            if drill and len(drill) > 1:
                if drill[1] == "oval":
                    drill_size = [as_float(drill[2]), as_float(drill[3])]
                else:
                    drill_size = [as_float(drill[1]), as_float(drill[1])]
                record["drill"] = {"size": drill_size, "offset": point(drill, "offset")}
            supported = ["circle", "rect", "roundrect", "oval", "custom"]
            if record["shape"] not in supported:
                warnings.append(f"{reference} pad {pad[1]}: {pad[3]} shown by a size envelope.")
            for primitive in record["primitives"]:
                if primitive[0] not in ["gr_poly", "gr_line", "gr_arc", "gr_circle", "gr_curve"]:
                    warnings.append(f"{reference} pad {pad[1]}: unsupported primitive {primitive[0]}.")
            pads.append(record)
    return {"units": "mm", "coordinate_system": "KiCad board, Y down; SVG clockwise angles",
            "layers": layers, "tracks": tracks, "vias": vias, "zones": zones, "pads": pads,
            "warnings": sorted(set(warnings))}


def explorer_copper(project_data):
    """Build small net/pad indices; keep huge routing arrays out of UI JSON."""
    nets = []
    features = []
    layers = []
    warnings = []
    for board_index, board in enumerate(project_data.get("pcb_files", [])):
        copper = board.get("copper") or {}
        source = board.get("source_file", "")
        for layer in copper.get("layers", []):
            if layer not in layers:
                layers.append(layer)
        warnings.extend(copper.get("warnings", []))
        board_features = []
        for key in ["zones", "tracks", "vias", "pads"]:
            board_features.extend(copper.get(key, []))
        names = sorted(set(str(feature["net"]) for feature in board_features if feature.get("net")))
        by_name = {}
        for index, name in enumerate(names):
            record = {"id": f"net_{board_index}_{index}", "name": name, "source_file": source,
                      "pins": [], "track_count": 0, "via_count": 0, "fill_count": 0, "layers": []}
            by_name[name] = record
            nets.append(record)
        for feature in board_features:
            record = dict(feature)
            net = by_name.get(feature.get("net"))
            record["net_id"] = net["id"] if net else ""
            record["source_file"] = source
            features.append(record)
            if net is None:
                continue
            for layer in feature["layers"]:
                if layer not in net["layers"]:
                    net["layers"].append(layer)
            kind = feature["kind"]
            if kind == "pad":
                pin = {"reference": feature["reference"], "number": feature["number"],
                       "layers": feature["layers"]}
                if pin not in net["pins"]:
                    net["pins"].append(pin)
            elif kind in ["arc", "segment"]:
                net["track_count"] += 1
            elif kind == "via":
                net["via_count"] += 1
            elif kind == "zone":
                net["fill_count"] += 1
    return {"nets": nets, "layers": layers, "features": features, "warnings": sorted(set(warnings))}


def arc_path(start, middle, end):
    circle = _circle_from_three_points(start, middle, end)
    if circle is None:
        return f'M {start[0]} {start[1]} L {middle[0]} {middle[1]} L {end[0]} {end[1]}'
    center, radius = circle
    angles = []
    for p in [start, middle, end]:
        angles.append(math.atan2(p[1] - center[1], p[0] - center[0]))
    span = (angles[2] - angles[0]) % math.tau
    sweep = int((angles[1] - angles[0]) % math.tau <= span)
    if not sweep:
        span = math.tau - span
    return f'M {start[0]} {start[1]} A {radius:.6f} {radius:.6f} 0 {int(span > math.pi)} {sweep} {end[0]} {end[1]}'


def _polygon(points):
    return " ".join(f"{float(x):.6f},{float(y):.6f}" for x, y in points)


def _pad_shape(pad):
    width, height = pad["size"]
    shape = pad["shape"]
    if shape == "custom":
        shape = pad["anchor"]
    if shape == "circle":
        drawing = f'<circle class="pad-anchor" r="{width / 2}"/>'
    else:
        radius = 0
        if shape == "oval":
            radius = min(width, height) / 2
        elif shape == "roundrect":
            radius = min(width, height) * pad["roundrect_rratio"]
        drawing = f'<rect class="pad-anchor" x="{-width / 2}" y="{-height / 2}" width="{width}" height="{height}" rx="{radius}"/>'
    for primitive in pad.get("primitives", []):
        kind = primitive[0]
        stroke = as_float(value(primitive, "width"))
        filled = value(primitive, "fill") == "yes"
        style = f'fill="{"currentColor" if filled else "none"}" stroke="currentColor" stroke-width="{stroke}"'
        if kind == "gr_poly":
            drawing += f'<polygon points="{_polygon(_points(primitive))}" {style}/>'
        elif kind == "gr_line":
            start, end = point(primitive, "start"), point(primitive, "end")
            drawing += f'<path d="M {start[0]} {start[1]} L {end[0]} {end[1]}" {style}/>'
        elif kind == "gr_arc":
            drawing += f'<path d="{arc_path(point(primitive, "start"), point(primitive, "mid"), point(primitive, "end"))}" {style}/>'
        elif kind == "gr_circle":
            center, end = point(primitive, "center"), point(primitive, "end")
            drawing += f'<circle cx="{center[0]}" cy="{center[1]}" r="{math.dist(center, end)}" {style}/>'
        elif kind == "gr_curve":
            pts = _points(primitive)
            if len(pts) == 4:
                drawing += f'<path d="M {pts[0][0]} {pts[0][1]} C {_polygon(pts[1:])}" {style}/>'
    # Keep drilled holes clear in both the base and selected copper layers.
    if pad.get("drill"):
        drill_width, drill_height = pad["drill"]["size"]
        offset_x, offset_y = pad["drill"]["offset"]
        drawing += (f'<rect class="pad-drill" x="{offset_x - drill_width / 2}" '
                    f'y="{offset_y - drill_height / 2}" width="{drill_width}" '
                    f'height="{drill_height}" rx="{min(drill_width, drill_height) / 2}" '
                    'style="fill: white; stroke: none"/>')
    return drawing


def copper_svg(features):
    lines = []
    for feature in features:
        kind = feature["kind"]
        reference = html.escape(str(feature.get("reference", "")), quote=True)
        number = html.escape(str(feature.get("number", "")), quote=True)
        layer_text = html.escape(" ".join(feature["layers"]), quote=True)
        attrs = (f'class="copper-feature copper-{kind}" data-net-id="{feature["net_id"]}" '
                 f'data-layers="{layer_text}" data-reference="{reference}" data-pin="{number}"')
        title = html.escape(" · ".join(filter(None, [feature.get("reference"), feature.get("number"), feature.get("net")])))
        drawing = ""
        if kind == "segment":
            start, end = feature["start"], feature["end"]
            drawing = f'<path d="M {start[0]} {start[1]} L {end[0]} {end[1]}" stroke-width="{feature["width"]}"/>'
        elif kind == "arc":
            drawing = f'<path d="{arc_path(feature["start"], feature["mid"], feature["end"])}" stroke-width="{feature["width"]}"/>'
        elif kind == "zone":
            drawing = f'<polygon points="{_polygon(feature["points"])}" fill-rule="evenodd"/>'
        elif kind == "via":
            x, y = feature["position"]
            outer, inner = feature["size"] / 2, feature["drill"] / 2
            # Ring, not a filled disc: drill remains visible in the overlay.
            drawing = f'<circle cx="{x}" cy="{y}" r="{(outer + inner) / 2}" stroke-width="{outer - inner}"/>'
        elif kind == "pad":
            x, y = feature["position"]
            drawing = f'<g transform="translate({x} {y}) rotate({feature["rotation"]})">{_pad_shape(feature)}</g>'
        lines.append(f'<g {attrs}><title>{title}</title>{drawing}</g>')
    return "\n".join(lines)


def add_copper_svg(board_svg, drawing, mirror=False):
    """Insert base and selected copper below the component artwork and labels.

    The assembly viewBox is in PCB mm with symmetric margins. Reflect about
    its centre for the bottom view, exactly as the existing board generator.
    """
    import re
    viewbox = re.search(r'viewBox="([^"]+)"', board_svg)
    if not viewbox:
        return board_svg
    x, y, width, height = [float(item) for item in viewbox.group(1).split()]
    transform = f'translate({2*x + width:.6f} 0) scale(-1 1)' if mirror else ""
    base = f'<g class="copper-base" transform="{transform}">{drawing}</g>'
    overlay = f'<g class="copper-overlay" transform="{transform}"></g>'
    highlights = '<g class="component-highlights" pointer-events="none"></g>'
    first_part = board_svg.find('<g class="board-component"')
    if first_part < 0:
        first_part = board_svg.rfind("</svg>")
    return board_svg[:first_part] + base + overlay + highlights + board_svg[first_part:]
