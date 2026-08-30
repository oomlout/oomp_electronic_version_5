"""Extract modern KiCad projects and call the OOMP matching agent."""

import argparse
import json
import math
import re
import shutil
from collections import defaultdict
from pathlib import Path

import yaml

from kicad_agents.geometry import (
    add_point,
    add_points,
    arc_bbox,
    bbox_record,
    empty_bbox,
    expand_bbox,
    merge_bbox,
    point_on_segment,
    rotated_rectangle_bbox,
    transform_bbox,
    transform_point,
)
from kicad_agents.oomp_matching_agent import (
    OompPartIndex,
    component_fields,
    load_overrides,
    match_component,
)
from kicad_agents.sexpr import (
    as_bool,
    as_float,
    as_int,
    child,
    children,
    load,
    tag,
    value,
    values,
)


OUTPUT_FORMAT_VERSION = 1
GRAPHIC_TAGS = {"arc", "bezier", "circle", "polyline", "rectangle"}
FOOTPRINT_GRAPHIC_TAGS = {"fp_arc", "fp_circle", "fp_curve", "fp_line", "fp_poly", "fp_rect"}


class NoAliasSafeDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def _rounded(value_number):
    return round(float(value_number), 6)


def _point(node, point_tag="at", default=(0.0, 0.0)):
    point_node = child(node, point_tag)
    if point_node is None or len(point_node) < 3:
        return default
    return as_float(point_node[1]), as_float(point_node[2])


def _position(node):
    at_node = child(node, "at")
    if at_node is None:
        return {"x": 0.0, "y": 0.0, "rotation": 0.0}
    return {
        "x": as_float(at_node[1]) if len(at_node) > 1 else 0.0,
        "y": as_float(at_node[2]) if len(at_node) > 2 else 0.0,
        "rotation": as_float(at_node[3]) if len(at_node) > 3 else 0.0,
    }


def _properties(node):
    result = {}
    for property_node in children(node, "property"):
        if len(property_node) >= 3:
            result[str(property_node[1])] = str(property_node[2])
    return result


def _stroke_width(node):
    stroke_node = child(node, "stroke")
    if stroke_node is not None:
        return as_float(value(stroke_node, "width", 0.0))
    return as_float(value(node, "width", 0.0))


def _points_from_pts(node):
    pts_node = child(node, "pts")
    if pts_node is None:
        return []
    points = []
    for point_node in children(pts_node, "xy"):
        if len(point_node) >= 3:
            points.append((as_float(point_node[1]), as_float(point_node[2])))
    return points


def _graphic_bbox(node):
    node_tag = tag(node)
    bbox = empty_bbox()

    if node_tag in {"polyline", "bezier", "fp_poly", "fp_curve"}:
        bbox = add_points(bbox, _points_from_pts(node))
    elif node_tag in {"rectangle", "fp_rect"}:
        bbox = add_points(bbox, [_point(node, "start"), _point(node, "end")])
    elif node_tag in {"circle", "fp_circle"}:
        center = _point(node, "center")
        if node_tag == "circle":
            radius = as_float(value(node, "radius", 0.0))
        else:
            radius_point = _point(node, "end")
            radius = math.hypot(radius_point[0] - center[0], radius_point[1] - center[1])
        bbox = [center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius]
    elif node_tag in {"arc", "fp_arc"}:
        bbox = arc_bbox(_point(node, "start"), _point(node, "mid"), _point(node, "end"))
    elif node_tag == "fp_line":
        bbox = add_points(bbox, [_point(node, "start"), _point(node, "end")])

    return expand_bbox(bbox, _stroke_width(node) / 2)


def _unit_identity(symbol_node):
    if len(symbol_node) < 2 or not isinstance(symbol_node[1], str):
        return None
    match = re.search(r"_(\d+)_(\d+)$", symbol_node[1])
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def _selected_library_nodes(library_symbol, unit_number, body_style):
    selected = [library_symbol]
    for unit_symbol in children(library_symbol, "symbol"):
        identity = _unit_identity(unit_symbol)
        if identity is None:
            continue
        symbol_unit, symbol_style = identity
        unit_matches = symbol_unit in {0, unit_number}
        style_matches = symbol_style in {0, body_style}
        if unit_matches and style_matches:
            selected.append(unit_symbol)
    return selected


def _library_graphic_bbox(library_symbol, unit_number, body_style):
    bbox = empty_bbox()
    for selected_node in _selected_library_nodes(library_symbol, unit_number, body_style):
        for item in selected_node[1:]:
            if isinstance(item, list) and tag(item) in GRAPHIC_TAGS:
                bbox = merge_bbox(bbox, _graphic_bbox(item))
    return bbox


def _library_pins(library_symbol, unit_number, body_style):
    pins = []
    for selected_node in _selected_library_nodes(library_symbol, unit_number, body_style):
        for pin_node in children(selected_node, "pin"):
            position = _position(pin_node)
            name_node = child(pin_node, "name")
            number_node = child(pin_node, "number")
            pins.append(
                {
                    "number": number_node[1] if number_node and len(number_node) > 1 else "",
                    "name": name_node[1] if name_node and len(name_node) > 1 else "",
                    "electrical_type": pin_node[1] if len(pin_node) > 1 else "",
                    "graphic_style": pin_node[2] if len(pin_node) > 2 else "",
                    "local_position": {
                        "x": _rounded(position["x"]),
                        "y": _rounded(position["y"]),
                        "rotation": _rounded(position["rotation"]),
                    },
                    "length": as_float(value(pin_node, "length", 0.0)),
                }
            )
    return pins


def _placed_library_id(symbol_node):
    library_id = value(symbol_node, "lib_id", "")
    if library_id:
        return library_id
    if len(symbol_node) > 1 and isinstance(symbol_node[1], str):
        return symbol_node[1]
    return ""


def _mirror(symbol_node):
    mirror_node = child(symbol_node, "mirror")
    if mirror_node is not None and len(mirror_node) > 1:
        return mirror_node[1]
    return ""


def _reference(symbol_node):
    properties = _properties(symbol_node)
    if properties.get("Reference"):
        return properties["Reference"]
    for instances_node in children(symbol_node, "instances"):
        for project_node in children(instances_node, "project"):
            for path_node in children(project_node, "path"):
                instance_reference = value(path_node, "reference", "")
                if instance_reference:
                    return instance_reference
    return ""


class UnionFind:
    def __init__(self):
        self.parent = {}

    def add(self, item):
        if item not in self.parent:
            self.parent[item] = item

    def find(self, item):
        self.add(item)
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, first, second):
        first_root = self.find(first)
        second_root = self.find(second)
        if first_root != second_root:
            if first_root < second_root:
                self.parent[second_root] = first_root
            else:
                self.parent[first_root] = second_root


def _coordinate_key(point):
    return round(point[0], 4), round(point[1], 4)


def _symbol_record(symbol_node, library_symbols, schematic_path, project_directory):
    reference = _reference(symbol_node)
    library_id = _placed_library_id(symbol_node)
    library_symbol = library_symbols.get(library_id)
    position = _position(symbol_node)
    unit_number = as_int(value(symbol_node, "unit", 1), 1)
    body_style = as_int(value(symbol_node, "body_style", 1), 1)
    mirror = _mirror(symbol_node)
    properties = _properties(symbol_node)
    placed_pin_numbers = {
        pin_node[1] for pin_node in children(symbol_node, "pin") if len(pin_node) > 1
    }

    if library_symbol is None:
        local_bbox = None
        library_pins = []
    else:
        local_bbox = _library_graphic_bbox(library_symbol, unit_number, body_style)
        library_pins = _library_pins(library_symbol, unit_number, body_style)

    pins = []
    for pin in library_pins:
        if placed_pin_numbers and pin["number"] not in placed_pin_numbers:
            continue
        local_point = (pin["local_position"]["x"], pin["local_position"]["y"])
        placed_point = transform_point(
            local_point,
            origin=(position["x"], position["y"]),
            angle_degrees=position["rotation"],
            mirror=mirror,
        )
        placed_pin = dict(pin)
        placed_pin["position"] = {"x": _rounded(placed_point[0]), "y": _rounded(placed_point[1])}
        pins.append(placed_pin)

    relative_source = str(schematic_path.relative_to(project_directory)).replace("\\", "/")
    placed_bbox = transform_bbox(
        local_bbox,
        origin=(position["x"], position["y"]),
        angle_degrees=position["rotation"],
        mirror=mirror,
    )
    return {
        "reference": reference,
        "source_file": relative_source,
        "uuid": value(symbol_node, "uuid", ""),
        "library_id": library_id,
        "unit": unit_number,
        "body_style": body_style,
        "position": {
            "x": _rounded(position["x"]),
            "y": _rounded(position["y"]),
            "rotation": _rounded(position["rotation"]),
            "mirror": mirror or None,
            "units": "mm",
        },
        "properties": properties,
        "in_bom": as_bool(value(symbol_node, "in_bom", "yes"), True),
        "on_board": as_bool(value(symbol_node, "on_board", "yes"), True),
        "in_position_files": as_bool(value(symbol_node, "in_pos_files", "yes"), True),
        "dnp": as_bool(value(symbol_node, "dnp", "no"), False),
        "pins": pins,
        "size": {
            "local_graphics": bbox_record(
                local_bbox,
                "symbol graphics only; excludes pins, properties, and text",
            ),
            "placed_graphics": bbox_record(
                placed_bbox,
                "axis-aligned bounds after schematic placement, rotation, and mirroring",
            ),
        },
        "warnings": [] if library_symbol is not None else ["Embedded library symbol definition was not found."],
    }


def _parse_schematic(schematic_path, project_directory):
    root = load(schematic_path)
    if tag(root) != "kicad_sch":
        raise ValueError(f"Not a modern .kicad_sch file: {schematic_path}")

    library_symbols = {}
    library_container = child(root, "lib_symbols")
    if library_container is not None:
        for library_symbol in children(library_container, "symbol"):
            if len(library_symbol) > 1 and isinstance(library_symbol[1], str):
                library_symbols[library_symbol[1]] = library_symbol

    symbols = [
        _symbol_record(symbol_node, library_symbols, schematic_path, project_directory)
        for symbol_node in children(root, "symbol")
    ]

    union_find = UnionFind()
    wire_segments = []
    connection_points = set()
    for wire_node in children(root, "wire"):
        wire_points = [_coordinate_key(point) for point in _points_from_pts(wire_node)]
        for start, end in zip(wire_points, wire_points[1:]):
            union_find.union(start, end)
            connection_points.add(start)
            connection_points.add(end)
            wire_segments.append((start, end))

    junction_points = set()
    for junction_node in children(root, "junction"):
        junction_point = _coordinate_key(_point(junction_node))
        junction_points.add(junction_point)
        connection_points.add(junction_point)
        union_find.add(junction_point)

    no_connect_points = {
        _coordinate_key(_point(no_connect_node)) for no_connect_node in children(root, "no_connect")
    }
    connection_points.update(no_connect_points)

    label_records = []
    local_label_points = defaultdict(list)
    global_label_points = defaultdict(list)
    for label_tag, scope in [
        ("label", "local"),
        ("global_label", "global"),
        ("hierarchical_label", "hierarchical"),
    ]:
        for label_node in children(root, label_tag):
            if len(label_node) < 2:
                continue
            label_name = label_node[1]
            label_point = _coordinate_key(_point(label_node))
            label_records.append({"name": label_name, "scope": scope, "point": label_point})
            connection_points.add(label_point)
            union_find.add(label_point)
            if scope == "local":
                local_label_points[label_name].append(label_point)
            elif scope == "global":
                global_label_points[label_name].append(label_point)

    pin_records = []
    for symbol in symbols:
        for pin in symbol["pins"]:
            pin_point = _coordinate_key((pin["position"]["x"], pin["position"]["y"]))
            pin_record = {"symbol": symbol, "pin": pin, "point": pin_point}
            pin_records.append(pin_record)
            connection_points.add(pin_point)
            union_find.add(pin_point)
            if symbol["reference"].startswith("#") and symbol["properties"].get("Value"):
                label_records.append(
                    {"name": symbol["properties"]["Value"], "scope": "power", "point": pin_point}
                )

    for label_points in list(local_label_points.values()) + list(global_label_points.values()):
        for label_point in label_points[1:]:
            union_find.union(label_points[0], label_point)

    for connection_point in connection_points:
        for segment_start, segment_end in wire_segments:
            if point_on_segment(connection_point, segment_start, segment_end):
                union_find.union(connection_point, segment_start)

    labels_by_root = defaultdict(list)
    for label_record in label_records:
        labels_by_root[union_find.find(label_record["point"])].append(label_record)

    pins_by_root = defaultdict(list)
    for pin_record in pin_records:
        pins_by_root[union_find.find(pin_record["point"])].append(pin_record)

    relative_source = str(schematic_path.relative_to(project_directory)).replace("\\", "/")
    for root_point, root_pins in pins_by_root.items():
        labels = labels_by_root[root_point]
        global_names = sorted({item["name"] for item in labels if item["scope"] in {"global", "power"}})
        local_names = sorted({item["name"] for item in labels if item["scope"] == "local"})
        hierarchical_names = sorted({item["name"] for item in labels if item["scope"] == "hierarchical"})
        all_names = global_names + local_names + hierarchical_names
        net_name = all_names[0] if all_names else None
        if global_names:
            connection_key = f"global:{global_names[0]}"
            net_scope = "global"
        else:
            connection_key = f"sheet:{relative_source}:{root_point[0]:.4f},{root_point[1]:.4f}"
            net_scope = "sheet"

        for pin_record in root_pins:
            pin = pin_record["pin"]
            pin["net"] = net_name
            pin["net_aliases"] = all_names
            pin["net_scope"] = net_scope
            pin["no_connect"] = pin_record["point"] in no_connect_points
            pin["_connection_key"] = connection_key

    for pin_record in pin_records:
        pin = pin_record["pin"]
        if "_connection_key" not in pin:
            point_key = pin_record["point"]
            pin["net"] = None
            pin["net_aliases"] = []
            pin["net_scope"] = "sheet"
            pin["no_connect"] = point_key in no_connect_points
            pin["_connection_key"] = f"sheet:{relative_source}:{point_key[0]:.4f},{point_key[1]:.4f}"

    return {
        "source_file": relative_source,
        "format": "kicad_sch",
        "format_version": value(root, "version", ""),
        "generator": value(root, "generator", ""),
        "generator_version": value(root, "generator_version", ""),
        "uuid": value(root, "uuid", ""),
        "symbols": symbols,
        "wire_count": len(children(root, "wire")),
        "junction_count": len(children(root, "junction")),
        "labels": [
            {"name": record["name"], "scope": record["scope"], "position": {"x": record["point"][0], "y": record["point"][1]}}
            for record in label_records
            if record["scope"] != "power"
        ],
        "hierarchical_sheet_count": len(children(root, "sheet")),
    }


def _footprint_layer_bbox(footprint_node, layer_filter=None):
    bbox = empty_bbox()
    for item in footprint_node[1:]:
        if not isinstance(item, list) or tag(item) not in FOOTPRINT_GRAPHIC_TAGS:
            continue
        item_layer = value(item, "layer", "")
        if layer_filter is not None and item_layer not in layer_filter:
            continue
        bbox = merge_bbox(bbox, _graphic_bbox(item))
    return bbox


def _pad_record(pad_node, footprint_position):
    pad_position = _position(pad_node)
    size_node = child(pad_node, "size")
    pad_size = (
        as_float(size_node[1]) if size_node is not None and len(size_node) > 1 else 0.0,
        as_float(size_node[2]) if size_node is not None and len(size_node) > 2 else 0.0,
    )
    local_bbox = rotated_rectangle_bbox(
        (pad_position["x"], pad_position["y"]),
        pad_size,
        pad_position["rotation"],
    )
    placed_bbox = transform_bbox(
        local_bbox,
        origin=(footprint_position["x"], footprint_position["y"]),
        angle_degrees=footprint_position["rotation"],
    )
    placed_center = transform_point(
        (pad_position["x"], pad_position["y"]),
        origin=(footprint_position["x"], footprint_position["y"]),
        angle_degrees=footprint_position["rotation"],
    )
    net_node = child(pad_node, "net")
    net_name = None
    net_number = None
    if net_node is not None:
        if len(net_node) == 2:
            net_name = net_node[1]
        elif len(net_node) >= 3:
            net_number = as_int(net_node[1], None)
            net_name = net_node[2]
    return {
        "number": pad_node[1] if len(pad_node) > 1 else "",
        "type": pad_node[2] if len(pad_node) > 2 else "",
        "shape": pad_node[3] if len(pad_node) > 3 else "",
        "local_position": {
            "x": _rounded(pad_position["x"]),
            "y": _rounded(pad_position["y"]),
            "rotation": _rounded(pad_position["rotation"]),
        },
        "position": {"x": _rounded(placed_center[0]), "y": _rounded(placed_center[1])},
        "size": {"x": _rounded(pad_size[0]), "y": _rounded(pad_size[1]), "units": "mm"},
        "layers": values(pad_node, "layers"),
        "net": net_name,
        "net_number": net_number,
        "pin_function": value(pad_node, "pinfunction", "") or None,
        "pin_type": value(pad_node, "pintype", "") or None,
        "bounds": {
            "local": bbox_record(local_bbox, "pad bounds in footprint-local coordinates"),
            "placed": bbox_record(placed_bbox, "pad bounds after footprint placement and rotation"),
        },
        "_local_bbox": local_bbox,
        "_placed_bbox": placed_bbox,
    }


def _footprint_record(footprint_node, pcb_path, project_directory):
    properties = _properties(footprint_node)
    footprint_position = _position(footprint_node)
    layer = value(footprint_node, "layer", "")
    pads = [_pad_record(pad_node, footprint_position) for pad_node in children(footprint_node, "pad")]

    pads_bbox = empty_bbox()
    for pad in pads:
        pads_bbox = merge_bbox(pads_bbox, pad["_local_bbox"])

    courtyard_layers = {"F.CrtYd", "B.CrtYd"}
    fabrication_layers = {"F.Fab", "B.Fab"}
    silkscreen_layers = {"F.SilkS", "B.SilkS"}
    courtyard_bbox = _footprint_layer_bbox(footprint_node, courtyard_layers)
    fabrication_bbox = _footprint_layer_bbox(footprint_node, fabrication_layers)
    silkscreen_bbox = _footprint_layer_bbox(footprint_node, silkscreen_layers)
    graphics_bbox = _footprint_layer_bbox(footprint_node)
    overall_bbox = merge_bbox(graphics_bbox, pads_bbox)

    def placed(local_bbox):
        return transform_bbox(
            local_bbox,
            origin=(footprint_position["x"], footprint_position["y"]),
            angle_degrees=footprint_position["rotation"],
        )

    relative_source = str(pcb_path.relative_to(project_directory)).replace("\\", "/")
    attributes_node = child(footprint_node, "attr")
    attributes = [item for item in attributes_node[1:] if isinstance(item, str)] if attributes_node else []
    library_id = footprint_node[1] if len(footprint_node) > 1 and isinstance(footprint_node[1], str) else ""
    for pad in pads:
        pad.pop("_local_bbox", None)
        pad.pop("_placed_bbox", None)
    return {
        "reference": properties.get("Reference", ""),
        "value": properties.get("Value", ""),
        "source_file": relative_source,
        "uuid": value(footprint_node, "uuid", "") or value(footprint_node, "tstamp", ""),
        "library_id": library_id,
        "layer": layer,
        "side": "back" if layer.startswith("B.") else "front",
        "position": {
            "x": _rounded(footprint_position["x"]),
            "y": _rounded(footprint_position["y"]),
            "rotation": _rounded(footprint_position["rotation"]),
            "units": "mm",
        },
        "properties": properties,
        "attributes": attributes,
        "exclude_from_bom": "exclude_from_bom" in attributes,
        "exclude_from_position_files": "exclude_from_pos_files" in attributes,
        "pads": pads,
        "size": {
            "pads_local": bbox_record(pads_bbox, "all footprint pads in footprint-local coordinates"),
            "pads_placed": bbox_record(placed(pads_bbox), "all pads after PCB placement and rotation"),
            "courtyard_local": bbox_record(courtyard_bbox, "F.CrtYd and B.CrtYd graphics; text excluded"),
            "courtyard_placed": bbox_record(placed(courtyard_bbox), "courtyard after PCB placement and rotation"),
            "fabrication_local": bbox_record(fabrication_bbox, "F.Fab and B.Fab graphics; text excluded"),
            "fabrication_placed": bbox_record(placed(fabrication_bbox), "fabrication graphics after placement"),
            "silkscreen_local": bbox_record(silkscreen_bbox, "F.SilkS and B.SilkS graphics; text excluded"),
            "silkscreen_placed": bbox_record(placed(silkscreen_bbox), "silkscreen graphics after placement"),
            "overall_local": bbox_record(overall_bbox, "all non-text footprint graphics and pads"),
            "overall_placed": bbox_record(placed(overall_bbox), "all non-text footprint graphics and pads after placement"),
        },
    }


def _parse_pcb(pcb_path, project_directory):
    root = load(pcb_path)
    if tag(root) != "kicad_pcb":
        raise ValueError(f"Not a modern .kicad_pcb file: {pcb_path}")
    relative_source = str(pcb_path.relative_to(project_directory)).replace("\\", "/")
    return {
        "source_file": relative_source,
        "format": "kicad_pcb",
        "format_version": value(root, "version", ""),
        "generator": value(root, "generator", ""),
        "generator_version": value(root, "generator_version", ""),
        "footprints": [
            _footprint_record(footprint_node, pcb_path, project_directory)
            for footprint_node in children(root, "footprint")
        ],
    }


def _natural_reference_key(reference):
    pieces = re.split(r"(\d+)", reference)
    return [int(piece) if piece.isdigit() else piece.lower() for piece in pieces]


def _component_directory_name(reference):
    directory_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", reference).strip(".")
    return directory_name or "unnamed_component"


def _build_components(schematic_files, pcb_files):
    components = {}

    for schematic_file in schematic_files:
        for symbol in schematic_file["symbols"]:
            reference = symbol["reference"] or f"unannotated_{symbol['uuid'][:8]}"
            component = components.setdefault(
                reference,
                {"reference": reference, "schematic": {"available": True, "units": []}, "pcb": None},
            )
            component["schematic"]["units"].append(symbol)

    for pcb_file in pcb_files:
        for footprint in pcb_file["footprints"]:
            reference = footprint["reference"] or f"board_only_{footprint['uuid'][:8]}"
            component = components.setdefault(
                reference,
                {"reference": reference, "schematic": {"available": False, "units": []}, "pcb": None},
            )
            if component["pcb"] is None:
                component["pcb"] = footprint
            else:
                component.setdefault("additional_pcb_footprints", []).append(footprint)

    return [components[reference] for reference in sorted(components, key=_natural_reference_key)]


def _enrich_schematic_connections(components):
    pins_by_connection = defaultdict(list)
    for component in components:
        for unit in component["schematic"]["units"]:
            for pin in unit["pins"]:
                pins_by_connection[pin["_connection_key"]].append(
                    {"component": component, "unit": unit, "pin": pin}
                )

    for connection_items in pins_by_connection.values():
        for item in connection_items:
            item["pin"]["connected_to"] = [
                {
                    "reference": other["component"]["reference"],
                    "pin_number": other["pin"]["number"],
                    "pin_name": other["pin"]["name"],
                }
                for other in connection_items
                if other["component"]["reference"] != item["component"]["reference"]
                or other["pin"]["number"] != item["pin"]["number"]
            ]
            item["pin"].pop("_connection_key", None)

    for component in components:
        connection_map = {}
        for unit in component["schematic"]["units"]:
            for pin in unit["pins"]:
                for connected in pin.get("connected_to", []):
                    key = (connected["reference"], connected["pin_number"])
                    connection_map[key] = connected
        component["schematic"]["connected_components"] = sorted(
            connection_map.values(),
            key=lambda item: (_natural_reference_key(item["reference"]), item["pin_number"]),
        )


def _enrich_pcb_connections(components):
    pads_by_net = defaultdict(list)
    for component in components:
        if component.get("pcb"):
            for pad in component["pcb"]["pads"]:
                if pad.get("net"):
                    pads_by_net[pad["net"]].append({"component": component, "pad": pad})

    for net_items in pads_by_net.values():
        for item in net_items:
            item["pad"]["connected_to"] = [
                {
                    "reference": other["component"]["reference"],
                    "pad_number": other["pad"]["number"],
                }
                for other in net_items
                if other["component"]["reference"] != item["component"]["reference"]
                or other["pad"]["number"] != item["pad"]["number"]
            ]

    for component in components:
        if not component.get("pcb"):
            continue
        connected_references = set()
        for pad in component["pcb"]["pads"]:
            for connected in pad.get("connected_to", []):
                connected_references.add(connected["reference"])
        component["pcb"]["connected_components"] = sorted(
            connected_references,
            key=_natural_reference_key,
        )


def _add_connectivity_cross_checks(components):
    for component in components:
        schematic_pins = {}
        for unit in component["schematic"]["units"]:
            for pin in unit["pins"]:
                schematic_pins.setdefault(pin["number"], []).append(pin)

        pcb_pads = defaultdict(list)
        if component.get("pcb"):
            for pad in component["pcb"]["pads"]:
                pcb_pads[pad["number"]].append(pad)

        comparisons = []
        for pin_number in sorted(set(schematic_pins) | set(pcb_pads)):
            schematic_nets = sorted(
                {pin.get("net") for pin in schematic_pins.get(pin_number, []) if pin.get("net")}
            )
            pcb_nets = sorted({pad.get("net") for pad in pcb_pads.get(pin_number, []) if pad.get("net")})
            if schematic_nets and pcb_nets:
                status = "agree" if set(schematic_nets) & set(pcb_nets) else "disagree"
            elif schematic_nets or pcb_nets:
                status = "incomplete"
            else:
                status = "no_named_net"
            comparisons.append(
                {
                    "pin_or_pad_number": pin_number,
                    "schematic_nets": schematic_nets,
                    "pcb_nets": pcb_nets,
                    "status": status,
                }
            )
        component["connectivity_cross_check"] = {
            "available": bool(schematic_pins and pcb_pads),
            "policy": "Named schematic nets are compared with PCB pad nets using matching pin/pad numbers.",
            "comparisons": comparisons,
            "agree_count": sum(item["status"] == "agree" for item in comparisons),
            "disagree_count": sum(item["status"] == "disagree" for item in comparisons),
            "incomplete_count": sum(item["status"] == "incomplete" for item in comparisons),
        }


def _write_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_yaml(path, data):
    path.write_text(
        yaml.dump(
            data,
            Dumper=NoAliasSafeDumper,
            sort_keys=False,
            allow_unicode=True,
            width=120,
        ),
        encoding="utf-8",
    )


def _schematic_size_data(component):
    return {
        "reference": component["reference"],
        "measurement_policy": "Only embedded symbol graphics are measured; pins, properties, and text are excluded.",
        "units": [
            {
                "unit": unit["unit"],
                "body_style": unit["body_style"],
                "source_file": unit["source_file"],
                "local_graphics": unit["size"]["local_graphics"],
                "placed_graphics": unit["size"]["placed_graphics"],
            }
            for unit in component["schematic"]["units"]
        ],
    }


def _pcb_size_data(component):
    if not component.get("pcb"):
        return {"reference": component["reference"], "available": False, "measurements": {}}
    return {
        "reference": component["reference"],
        "available": True,
        "measurement_policy": "Footprint text is excluded. Separate pad, courtyard, fabrication, silkscreen, and overall bounds are retained.",
        "measurements": component["pcb"]["size"],
    }


def _write_component_tree(output_directory, components, part_index):
    components_directory = output_directory / "components"
    components_directory.mkdir(parents=True, exist_ok=True)
    used_directory_names = set()
    manifest_path = output_directory / "generated_manifest.json"
    previous_directories = set()
    if manifest_path.is_file():
        try:
            previous_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            previous_directories = set(previous_manifest.get("component_directories", []))
        except (json.JSONDecodeError, OSError):
            previous_directories = set()

    for component in components:
        directory_name = _component_directory_name(component["reference"])
        if directory_name in used_directory_names:
            suffix = (component.get("pcb") or {}).get("uuid", "")[:8] or "duplicate"
            directory_name = f"{directory_name}_{suffix}"
        used_directory_names.add(directory_name)
        component["generated_directory"] = f"components/{directory_name}"

        component_directory = components_directory / directory_name
        schematic_directory = component_directory / "schematic"
        pcb_directory = component_directory / "pcb"
        oomp_directory = component_directory / "oomp"
        schematic_directory.mkdir(parents=True, exist_ok=True)
        pcb_directory.mkdir(parents=True, exist_ok=True)
        oomp_directory.mkdir(parents=True, exist_ok=True)

        schematic_data = component["schematic"]
        pcb_data = component["pcb"] or {"available": False, "reference": component["reference"]}
        _write_yaml(schematic_directory / "working.yaml", schematic_data)
        _write_yaml(schematic_directory / "size.yaml", _schematic_size_data(component))
        _write_yaml(pcb_directory / "working.yaml", pcb_data)
        _write_yaml(pcb_directory / "size.yaml", _pcb_size_data(component))
        _write_yaml(oomp_directory / "match.yaml", component["oomp"])

        matched_id = component["oomp"].get("oomp_id")
        copied_working = oomp_directory / "working.yaml"
        if matched_id and matched_id in part_index.by_id:
            source_working = Path(part_index.by_id[matched_id]["working_yaml"])
            shutil.copyfile(source_working, copied_working)
        elif copied_working.exists():
            copied_working.unlink()

        _write_json(component_directory / "component.json", component)
        _write_yaml(component_directory / "component.yaml", component)

    stale_directories = previous_directories - used_directory_names
    resolved_components_directory = components_directory.resolve()
    for stale_directory_name in sorted(stale_directories):
        stale_directory = (components_directory / stale_directory_name).resolve()
        is_direct_child = stale_directory.parent == resolved_components_directory
        has_generated_component_file = (stale_directory / "component.json").is_file()
        if is_direct_child and has_generated_component_file:
            shutil.rmtree(stale_directory)

    _write_json(
        manifest_path,
        {
            "generated_by": "kicad_agents.kicad_processing_agent",
            "component_directories": sorted(used_directory_names),
        },
    )


def process_project(project_directory, parts_directory, output_directory=None):
    project_directory = Path(project_directory).resolve()
    parts_directory = Path(parts_directory).resolve()
    if output_directory is None:
        output_directory = project_directory / "generated_data"
    else:
        output_directory = Path(output_directory).resolve()
    output_directory.mkdir(parents=True, exist_ok=True)

    canonical_schematic_path = project_directory / "kicad_file.kicad_sch"
    canonical_pcb_path = project_directory / "kicad_file.kicad_pcb"
    if canonical_schematic_path.is_file():
        schematic_paths = [canonical_schematic_path]
    else:
        schematic_paths = sorted(
            path for path in project_directory.rglob("*.kicad_sch") if output_directory not in path.parents
        )
    if canonical_pcb_path.is_file():
        pcb_paths = [canonical_pcb_path]
    else:
        pcb_paths = sorted(
            path for path in project_directory.rglob("*.kicad_pcb") if output_directory not in path.parents
        )
    if not schematic_paths:
        raise FileNotFoundError(f"No modern .kicad_sch files found under {project_directory}")
    if not pcb_paths:
        raise FileNotFoundError(f"No modern .kicad_pcb files found under {project_directory}")

    parsed_schematics = [_parse_schematic(path, project_directory) for path in schematic_paths]
    parsed_pcbs = [_parse_pcb(path, project_directory) for path in pcb_paths]
    components = _build_components(parsed_schematics, parsed_pcbs)
    _enrich_schematic_connections(components)
    _enrich_pcb_connections(components)
    _add_connectivity_cross_checks(components)

    overrides_path = output_directory / "match_overrides.yaml"
    if not overrides_path.exists():
        _write_yaml(
            overrides_path,
            {
                "matches": {},
                "help": "An AI or human reviewer may map a reference to an existing OOMP ID here, then rerun the processing agent.",
            },
        )
    overrides = load_overrides(overrides_path)
    part_index = OompPartIndex(parts_directory)
    for component in components:
        component["oomp"] = match_component(part_index, component, overrides=overrides)

    unmatched = [component for component in components if component["oomp"]["status"] in {"unmatched", "ambiguous"}]
    not_applicable = [component for component in components if component["oomp"]["status"] == "not_applicable"]
    matched = [component for component in components if component["oomp"]["status"] == "matched"]

    project_files = sorted(project_directory.rglob("*.kicad_pro"))
    project_name = project_files[0].stem if project_files else project_directory.name
    project_data = {
        "format_version": OUTPUT_FORMAT_VERSION,
        "generated_by": "kicad_agents.kicad_processing_agent",
        "project": {
            "name": project_name,
            "directory": str(project_directory),
            "schematic_files": [file_data["source_file"] for file_data in parsed_schematics],
            "pcb_files": [file_data["source_file"] for file_data in parsed_pcbs],
            "modern_kicad_only": True,
        },
        "summary": {
            "component_count": len(components),
            "schematic_symbol_count": sum(len(file_data["symbols"]) for file_data in parsed_schematics),
            "pcb_footprint_count": sum(len(file_data["footprints"]) for file_data in parsed_pcbs),
            "matched_component_count": len(matched),
            "unmatched_physical_component_count": len(unmatched),
            "non_physical_symbol_count": len(not_applicable),
            "connectivity_named_net_agreement_count": sum(
                component["connectivity_cross_check"]["agree_count"] for component in components
            ),
            "connectivity_named_net_disagreement_count": sum(
                component["connectivity_cross_check"]["disagree_count"] for component in components
            ),
        },
        "schematic_files": [
            {key: file_data[key] for key in file_data if key != "symbols"}
            for file_data in parsed_schematics
        ],
        "pcb_files": [
            {key: file_data[key] for key in file_data if key != "footprints"}
            for file_data in parsed_pcbs
        ],
        "components": components,
    }

    _write_component_tree(output_directory, components, part_index)
    unmatched_data = {
        "count": len(unmatched),
        "components": [
            {
                "reference": component["reference"],
                "fields": component_fields(component),
                "match": component["oomp"],
                "generated_directory": component["generated_directory"],
            }
            for component in unmatched
        ],
    }
    _write_json(output_directory / "unmatched_parts.json", unmatched_data)
    _write_yaml(output_directory / "unmatched_parts.yaml", unmatched_data)
    _write_json(output_directory / "project.json", project_data)
    _write_yaml(output_directory / "project.yaml", project_data)
    _write_yaml(output_directory / "summary.yaml", project_data["summary"])

    return project_data, output_directory


def main():
    parser = argparse.ArgumentParser(
        description="Extract modern KiCad schematic/PCB data and match physical components to OOMP parts."
    )
    parser.add_argument("project_directory", help="Project directory to scan recursively")
    parser.add_argument("--parts-dir", default="parts", help="OOMP parts directory")
    parser.add_argument("--output-dir", help="Output directory; defaults to PROJECT/generated_data")
    arguments = parser.parse_args()

    project_data, output_directory = process_project(
        arguments.project_directory,
        arguments.parts_dir,
        output_directory=arguments.output_dir,
    )
    summary = project_data["summary"]
    print(f"Generated: {output_directory}")
    print(f"Components: {summary['component_count']}")
    print(f"Matched: {summary['matched_component_count']}")
    print(f"Unmatched physical: {summary['unmatched_physical_component_count']}")
    print(f"Non-physical symbols: {summary['non_physical_symbol_count']}")


if __name__ == "__main__":
    main()
