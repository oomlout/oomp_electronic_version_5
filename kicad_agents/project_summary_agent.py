"""Compile deterministic project-part README files and PCB placement SVGs."""

from __future__ import annotations

import argparse
import html
import json
import math
import re
import shutil
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .sexpr import as_float, child, children, load, tag, value


ROOT_DIRECTORY = Path(__file__).resolve().parents[1]
SUMMARY_TEMPLATE = ROOT_DIRECTORY / "source_file" / "template_jinja" / "project_summary" / "working.md.j2"
STYLE_TEMPLATE = ROOT_DIRECTORY / "styles" / "style_project_summary.yaml"


def _read_yaml(path, default=None):
    if not path.is_file():
        return {} if default is None else default
    with path.open("r", encoding="utf-8") as input_file:
        loaded = yaml.safe_load(input_file)
    if loaded is None:
        return {} if default is None else default
    return loaded


def _write_yaml(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(data, output_file, sort_keys=False, allow_unicode=True)


def _write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as output_file:
        json.dump(data, output_file, indent=2, ensure_ascii=False)
        output_file.write("\n")


def _write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        output_file.write(text)


def _merge_dicts(base, extra):
    merged = {}
    for key in base:
        value = base[key]
        if isinstance(value, dict):
            merged[key] = _merge_dicts(value, {})
        else:
            merged[key] = value
    for key in extra:
        value = extra[key]
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = _merge_dicts(merged[key], value)
        else:
            merged[key] = value
    return merged


def _project_identity(project_directory):
    directory_parts = list(project_directory.parts)
    owner = project_directory.parent.name
    repository = project_directory.name
    for index in range(len(directory_parts) - 2):
        if directory_parts[index].lower() == "project":
            owner = directory_parts[index + 1]
            repository = directory_parts[index + 2]
    return {
        "owner": owner,
        "repository": repository,
        "github_url": f"https://github.com/{owner}/{repository}",
    }


def _natural_reference_key(reference):
    sections = []
    current = ""
    current_is_number = None
    for character in str(reference):
        is_number = character.isdigit()
        if current != "" and is_number != current_is_number:
            sections.append(int(current) if current_is_number else current.lower())
            current = ""
        current += character
        current_is_number = is_number
    if current != "":
        sections.append(int(current) if current_is_number else current.lower())
    return sections


def _available_bbox(record):
    if not isinstance(record, dict) or not record.get("available", False):
        return None
    minimum = record.get("min", {})
    maximum = record.get("max", {})
    required = [minimum.get("x"), minimum.get("y"), maximum.get("x"), maximum.get("y")]
    if any(value_item is None for value_item in required):
        return None
    return {
        "min_x": float(minimum["x"]),
        "min_y": float(minimum["y"]),
        "max_x": float(maximum["x"]),
        "max_y": float(maximum["y"]),
    }


def _component_bbox(component):
    pcb = component.get("pcb")
    if not isinstance(pcb, dict):
        return None
    size = pcb.get("size", {})
    preferred_names = ["overall_placed", "courtyard_placed", "pads_placed"]
    for preferred_name in preferred_names:
        available = _available_bbox(size.get(preferred_name, {}))
        if available is not None:
            available["source"] = preferred_name
            return available
    position = pcb.get("position", {})
    if "x" in position and "y" in position:
        x = float(position["x"])
        y = float(position["y"])
        return {"min_x": x - 0.5, "min_y": y - 0.5, "max_x": x + 0.5, "max_y": y + 0.5, "source": "position"}
    return None


def _point(node, point_name):
    point_node = child(node, point_name)
    if point_node is None or len(point_node) < 3:
        return None
    return [as_float(point_node[1]), as_float(point_node[2])]


def _arc_points(start, middle, end, steps=12):
    x1, y1 = start
    x2, y2 = middle
    x3, y3 = end
    determinant = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if abs(determinant) < 0.000001:
        return [start, middle, end]
    center_x = (
        (x1 * x1 + y1 * y1) * (y2 - y3)
        + (x2 * x2 + y2 * y2) * (y3 - y1)
        + (x3 * x3 + y3 * y3) * (y1 - y2)
    ) / determinant
    center_y = (
        (x1 * x1 + y1 * y1) * (x3 - x2)
        + (x2 * x2 + y2 * y2) * (x1 - x3)
        + (x3 * x3 + y3 * y3) * (x2 - x1)
    ) / determinant
    radius = math.hypot(x1 - center_x, y1 - center_y)
    start_angle = math.atan2(y1 - center_y, x1 - center_x)
    middle_angle = math.atan2(y2 - center_y, x2 - center_x)
    end_angle = math.atan2(y3 - center_y, x3 - center_x)
    full_turn = math.pi * 2
    ccw_span = (end_angle - start_angle) % full_turn
    ccw_middle = (middle_angle - start_angle) % full_turn
    if ccw_middle <= ccw_span:
        angle_span = ccw_span
    else:
        angle_span = -((start_angle - end_angle) % full_turn)
    points = []
    for step in range(steps + 1):
        angle = start_angle + angle_span * step / steps
        points.append([center_x + radius * math.cos(angle), center_y + radius * math.sin(angle)])
    return points


def _edge_cut_shapes(project_directory, pcb_files):
    shapes = []
    all_points = []
    shape_tags = ["gr_line", "gr_arc", "gr_rect", "gr_circle", "gr_poly"]
    for pcb_file in pcb_files:
        pcb_path = project_directory / pcb_file
        if not pcb_path.is_file():
            continue
        root = load(pcb_path)
        for shape_tag in shape_tags:
            for shape_node in children(root, shape_tag):
                if value(shape_node, "layer", "") != "Edge.Cuts":
                    continue
                points = []
                if shape_tag == "gr_line":
                    start = _point(shape_node, "start")
                    end = _point(shape_node, "end")
                    if start and end:
                        points = [start, end]
                elif shape_tag == "gr_arc":
                    start = _point(shape_node, "start")
                    middle = _point(shape_node, "mid")
                    end = _point(shape_node, "end")
                    if start and middle and end:
                        points = _arc_points(start, middle, end)
                elif shape_tag == "gr_rect":
                    start = _point(shape_node, "start")
                    end = _point(shape_node, "end")
                    if start and end:
                        points = [start, [end[0], start[1]], end, [start[0], end[1]], start]
                elif shape_tag == "gr_circle":
                    center = _point(shape_node, "center")
                    end = _point(shape_node, "end")
                    if center and end:
                        radius = math.hypot(end[0] - center[0], end[1] - center[1])
                        for step in range(25):
                            angle = math.pi * 2 * step / 24
                            points.append([center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle)])
                elif shape_tag == "gr_poly":
                    points_node = child(shape_node, "pts")
                    if points_node is not None:
                        for xy_node in children(points_node, "xy"):
                            if len(xy_node) >= 3:
                                points.append([as_float(xy_node[1]), as_float(xy_node[2])])
                        if len(points) > 1:
                            points.append(points[0])
                if points:
                    shapes.append({"type": shape_tag, "points": points})
                    all_points.extend(points)
    return shapes, all_points


def _bounds_from_points(points):
    if not points:
        return None
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    return {
        "min_x": min(x_values),
        "min_y": min(y_values),
        "max_x": max(x_values),
        "max_y": max(y_values),
    }


def _bounds_from_components(components):
    component_bounds = []
    for component in components:
        bounds = _component_bbox(component)
        if bounds is not None:
            component_bounds.append(bounds)
    if not component_bounds:
        return None
    return {
        "min_x": min(bounds["min_x"] for bounds in component_bounds),
        "min_y": min(bounds["min_y"] for bounds in component_bounds),
        "max_x": max(bounds["max_x"] for bounds in component_bounds),
        "max_y": max(bounds["max_y"] for bounds in component_bounds),
    }


def _oomp_description(component):
    oomp = component.get("oomp", {})
    if oomp.get("status") == "matched":
        return oomp.get("oomp_id", "")
    return ""


def _bom_rows(components, oomp_link_prefix="../../../../parts"):
    groups = {}
    for component in components:
        pcb = component.get("pcb")
        if not isinstance(pcb, dict):
            continue
        oomp_id = _oomp_description(component)
        value_text = str(pcb.get("value", ""))
        footprint = str(pcb.get("library_id", ""))
        key = (oomp_id, value_text, footprint)
        if key not in groups:
            description = oomp_id.replace("_", " ") if oomp_id else value_text or footprint or "Unmatched component"
            groups[key] = {
                "description": description,
                "value": value_text,
                "footprint": footprint,
                "oomp_id": oomp_id,
                "oomp_link": f"{oomp_link_prefix}/{oomp_id}/README.md" if oomp_id else "",
                "references": [],
            }
        groups[key]["references"].append(component["reference"])
    rows = []
    for key in groups:
        row = groups[key]
        row["references"] = sorted(row["references"], key=_natural_reference_key)
        row["quantity"] = len(row["references"])
        rows.append(row)
    rows.sort(key=lambda row: (_natural_reference_key(row["references"][0]), row["description"]))
    return rows


def _net_rows(components):
    nets = {}
    for component in components:
        pcb = component.get("pcb")
        if not isinstance(pcb, dict):
            continue
        for pad in pcb.get("pads", []):
            net_name = str(pad.get("net", "")).strip()
            if net_name == "":
                continue
            if net_name not in nets:
                nets[net_name] = {"name": net_name, "pad_count": 0, "references": []}
            nets[net_name]["pad_count"] += 1
            if component["reference"] not in nets[net_name]["references"]:
                nets[net_name]["references"].append(component["reference"])
    rows = list(nets.values())
    for row in rows:
        row["references"] = sorted(row["references"], key=_natural_reference_key)
    rows.sort(key=lambda row: (-row["pad_count"], row["name"].lower()))
    return rows[:20]


def _component_rows(components):
    rows = []
    for component in components:
        pcb = component.get("pcb")
        if not isinstance(pcb, dict):
            continue
        position = pcb.get("position", {})
        rows.append(
            {
                "reference": component["reference"],
                "value": pcb.get("value", ""),
                "footprint": pcb.get("library_id", ""),
                "side": pcb.get("side", "front"),
                "x": float(position.get("x", 0)),
                "y": float(position.get("y", 0)),
                "rotation": float(position.get("rotation", 0)),
                "oomp_id": _oomp_description(component),
                "bounds": _component_bbox(component),
            }
        )
    rows.sort(key=lambda row: _natural_reference_key(row["reference"]))
    return rows


def _svg_polyline(points, css_class):
    points_text = " ".join(f"{point[0]:.4f},{point[1]:.4f}" for point in points)
    return f'<polyline class="{css_class}" points="{points_text}" />'


def _inline_svg(svg_path, x, y, width, height):
    """Place a copied part SVG inline so GitHub and rasterizers need no file fetch."""
    svg_text = svg_path.read_text(encoding="utf-8")
    view_box_match = re.search(r'viewBox\s*=\s*"([^"]+)"', svg_text)
    svg_start = svg_text.find("<svg")
    opening_end = svg_text.find(">", svg_start)
    closing_start = svg_text.rfind("</svg>")
    if view_box_match is None or svg_start < 0 or opening_end < 0 or closing_start < 0:
        return ""
    inner_svg = svg_text[opening_end + 1 : closing_start].strip()
    return (
        f'<svg x="{x:.4f}" y="{y:.4f}" width="{width:.4f}" height="{height:.4f}" '
        f'viewBox="{html.escape(view_box_match.group(1))}" preserveAspectRatio="none">{inner_svg}</svg>'
    )


def _make_board_svg(output_path, project_directory, project_data, components, style, component_asset_directory):
    pcb_files = project_data.get("project", {}).get("pcb_files", [])
    edge_shapes, edge_points = _edge_cut_shapes(project_directory, pcb_files)
    bounds = _bounds_from_points(edge_points)
    bounds_source = "KiCad Edge.Cuts"
    if bounds is None:
        bounds = _bounds_from_components(components)
        bounds_source = "placed component extents"
    if bounds is None:
        _write_text(output_path, '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="320"><rect width="100%" height="100%" fill="#FFFFFF"/><text x="20" y="40">No PCB placement data available</text></svg>\n')
        return {"available": False, "image_file": "generated_data/src/board.svg", "bounds_source": "none"}

    svg_style = style["board_svg"]
    colors = style["colors"]
    typography = style["typography"]
    margin = float(svg_style["margin_mm"])
    board_width = bounds["max_x"] - bounds["min_x"]
    board_height = bounds["max_y"] - bounds["min_y"]
    view_min_x = bounds["min_x"] - margin
    view_min_y = bounds["min_y"] - margin
    view_width = board_width + margin * 2
    view_height = board_height + margin * 2
    component_rows = _component_rows(components)

    lines = [
        '<?xml version="1.0" encoding="utf-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="{view_min_x:.4f} {view_min_y:.4f} {view_width:.4f} {view_height:.4f}">',
        "<defs>",
        "<style>",
        f'.page {{ fill: {colors["background"]}; }}',
        f'.board {{ fill: {colors["board_fill"]}; stroke: {colors["board_outline"]}; stroke-width: {svg_style["board_stroke_width_mm"]}; }}',
        f'.edge-cut {{ fill: none; stroke: {colors["board_outline"]}; stroke-width: {svg_style["edge_cut_stroke_width_mm"]}; }}',
        f'.component {{ fill: {colors["component_fill"]}; stroke: {colors["component_outline"]}; stroke-width: {svg_style["component_stroke_width_mm"]}; }}',
        f'.reference {{ fill: {colors["text"]}; font-family: {typography["family"]}; font-size: {typography["reference_size_mm"]}px; text-anchor: middle; paint-order: stroke; stroke: {colors["background"]}; stroke-width: 0.35px; }}',
        "</style>",
        "</defs>",
        f'<rect class="page" x="{view_min_x:.4f}" y="{view_min_y:.4f}" width="{view_width:.4f}" height="{view_height:.4f}" />',
        f'<rect class="board" x="{bounds["min_x"]:.4f}" y="{bounds["min_y"]:.4f}" width="{board_width:.4f}" height="{board_height:.4f}" rx="{svg_style["board_corner_radius_mm"]}" />',
    ]
    for edge_shape in edge_shapes:
        lines.append(_svg_polyline(edge_shape["points"], "edge-cut"))

    rows_by_area = []
    for row in component_rows:
        bounds_record = row.get("bounds")
        if bounds_record is None:
            area = 1
        else:
            area = max(0.01, (bounds_record["max_x"] - bounds_record["min_x"]) * (bounds_record["max_y"] - bounds_record["min_y"]))
        rows_by_area.append([area, row])
    rows_by_area.sort(key=lambda item: -item[0])

    reference_lines = []
    for area, row in rows_by_area:
        bounds_record = row.get("bounds")
        if bounds_record is None:
            width = float(svg_style["minimum_component_width_mm"])
            height = float(svg_style["minimum_component_height_mm"])
        else:
            width = bounds_record["max_x"] - bounds_record["min_x"]
            height = bounds_record["max_y"] - bounds_record["min_y"]
            width = max(width, float(svg_style["minimum_component_width_mm"]))
            height = max(height, float(svg_style["minimum_component_height_mm"]))
        x = row["x"]
        y = row["y"]
        rotation = row["rotation"]
        mirror = " scale(-1 1)" if row["side"] == "back" else ""
        lines.append(f'<g transform="translate({x:.4f} {y:.4f}) rotate({rotation:.4f}){mirror}">')
        oomp_id = row["oomp_id"]
        svg_part_path = component_asset_directory / oomp_id / "working_svg_outline.svg" if oomp_id else None
        if svg_part_path is not None and svg_part_path.is_file():
            inline_svg = _inline_svg(svg_part_path, -width / 2, -height / 2, width, height)
            if inline_svg != "":
                lines.append(inline_svg)
            else:
                lines.append(f'<rect class="component" x="{-width / 2:.4f}" y="{-height / 2:.4f}" width="{width:.4f}" height="{height:.4f}" rx="0.2" />')
        else:
            lines.append(f'<rect class="component" x="{-width / 2:.4f}" y="{-height / 2:.4f}" width="{width:.4f}" height="{height:.4f}" rx="0.2" />')
        lines.append("</g>")
        label_y = y - height / 2 - 0.45
        reference_lines.append(
            f'<text x="{x:.4f}" y="{label_y:.4f}" fill="#000000" font-family="Arial, sans-serif" '
            f'font-size="{typography["reference_size_mm"]}" font-weight="bold" text-anchor="middle">{html.escape(row["reference"])}</text>'
        )
    for reference_line in reference_lines:
        lines.append(reference_line)
    lines.append("</svg>")
    _write_text(output_path, "\n".join(lines) + "\n")
    return {
        "available": True,
        "image_file": "generated_data/src/board.svg",
        "bounds_source": bounds_source,
        "min_x": round(bounds["min_x"], 4),
        "min_y": round(bounds["min_y"], 4),
        "max_x": round(bounds["max_x"], 4),
        "max_y": round(bounds["max_y"], 4),
        "width_mm": round(board_width, 4),
        "height_mm": round(board_height, 4),
        "edge_shape_count": len(edge_shapes),
    }


def _copy_project_sources(components, parts_directory, project_source_directory, component_asset_directory):
    # These short arrays are intentionally explicit.  Add another filename
    # here when the project compiler begins consuming another part asset.
    source_filenames = [
        "working.yaml",
        "working_svg_outline.svg",
    ]
    image_filenames = [
        "working_svg_outline.svg",
    ]

    oomp_ids = []
    for component in components:
        oomp_id = _oomp_description(component)
        if oomp_id != "" and oomp_id not in oomp_ids:
            oomp_ids.append(oomp_id)
    oomp_ids.sort()

    manifest_parts = []
    for oomp_id in oomp_ids:
        source_part_directory = parts_directory / oomp_id
        copied_source_files = []
        copied_image_files = []

        for source_filename in source_filenames:
            source_file = source_part_directory / source_filename
            if source_file.is_file():
                destination_file = project_source_directory / oomp_id / source_filename
                destination_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_file, destination_file)
                copied_source_files.append(source_filename)

        for image_filename in image_filenames:
            source_file = source_part_directory / image_filename
            if source_file.is_file():
                destination_file = component_asset_directory / oomp_id / image_filename
                destination_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_file, destination_file)
                # Component sheets use a white page rectangle.  That is right
                # for standalone diagrams but would hide neighboring items on
                # a board composite, so remove only that page-background line
                # from the local project image copy.
                source_lines = destination_file.read_text(encoding="utf-8").splitlines()
                board_lines = []
                removed_background = False
                for source_line in source_lines:
                    is_page_rectangle = (
                        not removed_background
                        and "<rect" in source_line
                        and 'stroke="none"' in source_line
                        and 'fill="#FFFFFF"' in source_line
                    )
                    if is_page_rectangle:
                        removed_background = True
                    else:
                        board_lines.append(source_line)
                destination_file.write_text("\n".join(board_lines) + "\n", encoding="utf-8")
                copied_image_files.append(image_filename)

        manifest_parts.append(
            {
                "oomp_id": oomp_id,
                "project_source_files": copied_source_files,
                "generated_image_files": copied_image_files,
            }
        )

    manifest = {
        "format_version": 1,
        "source_filenames": source_filenames,
        "image_filenames": image_filenames,
        "parts": manifest_parts,
    }
    _write_yaml(project_source_directory / "manifest.yaml", manifest)
    _write_yaml(component_asset_directory / "manifest.yaml", manifest)
    return manifest


def _deterministic_text(display_name, summary, board, placement):
    component_count = int(summary.get("component_count", 0))
    matched_count = int(summary.get("matched_component_count", 0))
    unmatched_count = int(summary.get("unmatched_physical_component_count", 0))
    front_count = int(placement.get("front_count", 0))
    back_count = int(placement.get("back_count", 0))
    disagreement_count = int(summary.get("connectivity_named_net_disagreement_count", 0))

    overview = (
        f"{display_name} is a KiCad project containing {component_count} extracted component records. "
        f"The catalogue matcher linked {matched_count} physical placements to OOMP parts."
    )

    design_notes = []
    if board.get("available", False):
        design_notes.append(
            f"The extracted board outline is approximately {board['width_mm']} mm by {board['height_mm']} mm."
        )
    design_notes.append(f"Placement data contains {front_count} front-side and {back_count} back-side components.")

    review_notes = []
    if unmatched_count > 0:
        review_notes.append(f"{unmatched_count} physical component records are not yet matched to an OOMP part.")
    if disagreement_count > 0:
        review_notes.append(
            f"The extractor reports {disagreement_count} named-net comparisons that differ between schematic and PCB data."
        )
    if review_notes == []:
        review_notes.append("No unmatched physical components or named-net disagreements were reported by the extractor.")

    return {
        "overview": overview,
        "design_notes": design_notes,
        "review_notes": review_notes,
    }


def generate_project_summary(
    project_directory,
    parts_directory=None,
    output_directory=None,
    project_data=None,
    part_metadata=None,
    readme_output=None,
):
    project_directory = Path(project_directory).resolve()
    if parts_directory is None:
        parts_directory = ROOT_DIRECTORY / "parts"
    else:
        parts_directory = Path(parts_directory).resolve()
    if output_directory is None:
        output_directory = project_directory / "generated_data"
    else:
        output_directory = Path(output_directory).resolve()
    output_directory.mkdir(parents=True, exist_ok=True)
    asset_directory = output_directory / "src"
    component_asset_directory = asset_directory / "components"
    project_source_directory = project_directory / "project_source"
    asset_directory.mkdir(parents=True, exist_ok=True)
    component_asset_directory.mkdir(parents=True, exist_ok=True)
    project_source_directory.mkdir(parents=True, exist_ok=True)

    if project_data is None:
        project_data = _read_yaml(output_directory / "project.yaml")
    components = project_data.get("components", [])

    base_style = _read_yaml(STYLE_TEMPLATE)
    style_override = _read_yaml(output_directory / "project_style_override.yaml")
    style = _merge_dicts(base_style, style_override)
    _write_yaml(output_directory / "project_style.yaml", style)

    if part_metadata is None:
        part_metadata = _read_yaml(project_directory / "working.yaml")
    identity = _project_identity(project_directory)
    if part_metadata.get("project_github_user", "") != "":
        identity["owner"] = part_metadata["project_github_user"]
    if part_metadata.get("project_github_repository", "") != "":
        identity["repository"] = part_metadata["project_github_repository"]
    if part_metadata.get("project_github_url", "") != "":
        identity["github_url"] = part_metadata["project_github_url"]
    else:
        identity["github_url"] = f"https://github.com/{identity['owner']}/{identity['repository']}"

    raw_project = project_data.get("project", {})
    display_name = raw_project.get("name", identity["repository"])
    source_manifest = _copy_project_sources(
        components,
        parts_directory,
        project_source_directory,
        component_asset_directory,
    )
    board = _make_board_svg(
        asset_directory / "board.svg",
        project_directory,
        project_data,
        components,
        style,
        component_asset_directory,
    )
    component_rows = _component_rows(components)
    placement = {
        "component_count": len(component_rows),
        "front_count": sum(1 for row in component_rows if row["side"] == "front"),
        "back_count": sum(1 for row in component_rows if row["side"] == "back"),
        "components": component_rows,
    }
    summary = project_data.get("summary", {})
    generated_text = _deterministic_text(display_name, summary, board, placement)
    summary_data = {
        "format_version": 1,
        "generated_by": "kicad_agents.project_summary_agent",
        "project": {
            "name": raw_project.get("name", identity["repository"]),
            "display_name": display_name,
            "owner": identity["owner"],
            "repository": identity["repository"],
            "github_url": identity["github_url"],
            "version": part_metadata.get("project_version", "current"),
            "git_ref": part_metadata.get("project_git_ref", ""),
            "directory": str(project_directory),
            "schematic_files": raw_project.get("schematic_files", []),
            "pcb_files": raw_project.get("pcb_files", []),
        },
        "summary": summary,
        "placement": placement,
        "board": board,
        "bom": _bom_rows(components, oomp_link_prefix=".."),
        "nets": _net_rows(components),
        "generated_text": generated_text,
        "style": style,
        "source_manifest": source_manifest,
    }
    _write_json(output_directory / "project_summary_data.json", summary_data)
    _write_yaml(output_directory / "project_summary_data.yaml", summary_data)

    environment = Environment(
        loader=FileSystemLoader(str(SUMMARY_TEMPLATE.parent)),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = environment.get_template(SUMMARY_TEMPLATE.name)
    markdown = template.render(**summary_data)
    if readme_output is None:
        readme_output = project_directory / "README.md"
    else:
        readme_output = Path(readme_output).resolve()
    _write_text(readme_output, markdown)
    return summary_data


def main():
    parser = argparse.ArgumentParser(description="Build a styled project summary and PCB placement SVG.")
    parser.add_argument("project_directory", help="Project part directory containing copied kicad_file.* files")
    parser.add_argument("--parts-dir", default="parts", help="OOMP parts directory")
    parser.add_argument("--output-dir", help="Output directory; defaults to PROJECT/generated_data")
    arguments = parser.parse_args()
    summary_data = generate_project_summary(
        arguments.project_directory,
        parts_directory=arguments.parts_dir,
        output_directory=arguments.output_dir,
    )
    print(f"Generated: {Path(arguments.output_dir).resolve() if arguments.output_dir else Path(arguments.project_directory).resolve() / 'generated_data'}")
    print(f"GitHub: {summary_data['project']['github_url']}")
    print(f"Board: {summary_data['board'].get('width_mm', 0)} mm x {summary_data['board'].get('height_mm', 0)} mm")


if __name__ == "__main__":
    main()
