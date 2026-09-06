"""Render KiCad schematics as interactive, OOMP-styled SVG for the board explorer.

The goal is fidelity to the original sheet: every wire, junction, label, note
rectangle, free text and symbol stays exactly where the schematic file placed
it, so the drawing an engineer recognises from KiCad is what the explorer
shows.  Symbol graphics come from the file's embedded ``lib_symbols`` using the
same unit/body-style selection (and the same Y-up to Y-down conversion, mirror
order and rotation sign) as ``kicad_processing_agent``, so placed pins land on
the coordinates the connectivity extractor already reports.

Each placed symbol becomes a ``<g class="sch-symbol" data-reference ...>``
group so the explorer can reuse its component hover/select machinery, and
wires and labels carry ``data-net`` so net selections can light up the sheet
without a second netlist.  Colours are CSS variables with light-theme
fallbacks, so the same SVG renders standalone (README/GitHub) and picks up the
explorer's light/dark/rainbow themes automatically.

Hierarchical designs are supported: every referenced ``Sheetfile`` becomes an
additional page laid out beside its parent, and the sheet symbol in the parent
keeps its name and file text so the split stays legible.
"""

import math
import re
from pathlib import Path

from kicad_agents.geometry import point_on_segment, transform_point
from kicad_agents.sexpr import as_float, as_int, child, children, load, tag, value

DEFAULT_WIRE_WIDTH = 0.1524
WIRE_VISUAL_WIDTH = 0.3
DEFAULT_BUS_WIDTH = 0.5
DEFAULT_GRAPHIC_WIDTH = 0.1524
DEFAULT_FONT_HEIGHT = 1.27
JUNCTION_RADIUS = 0.45
TEXT_WIDTH_FACTOR = 0.63
LINE_HEIGHT_FACTOR = 1.3
PAGE_GAP_MM = 40.0
PIN_LABEL_FONT = 1.4
PIN_NAME_FONT = 1.5
NON_DRAWN_TAGS = {
    "property",
    "pin",
    "instances",
    "exclude_from_sim",
    "in_bom",
    "on_board",
    "in_pos_files",
    "dnp",
    "body_style",
    "unit",
    "uuid",
    "pin_numbers",
    "pin_names",
    "embedded_fonts",
}

_SVG_EXTRA_STYLE = (
    ".sch-page { fill: var(--sch-page, #ffffff); }"
    ".sch-wire { fill: none; stroke: var(--net-color, var(--sch-ink, #171717)); stroke-linecap: round; }"
    ".sch-wire-hit { stroke: #000000; stroke-opacity: 0; stroke-width: 1.0; pointer-events: stroke; cursor: pointer; }"
    ".sch-pin-hit { fill: none; stroke: #000000; stroke-opacity: 0; stroke-width: 0.9; pointer-events: stroke; cursor: pointer; }"
    ".sch-junction { fill: var(--sch-ink, #171717); stroke: none; }"
    ".sch-no-connect { stroke: var(--sch-note, #b0543f); fill: none; stroke-width: 0.25; stroke-linecap: round; }"
    ".sch-pin { fill: none; stroke: var(--sch-ink, #171717); stroke-width: 0.3048; stroke-linecap: round; }"
    ".sch-pin-number { fill: var(--sch-ink, #171717); }"
    ".sch-pin-name { fill: var(--sch-ink, #171717); font-weight: 700; }"
    ".sch-ref { fill: var(--sch-ink, #171717); font-weight: 800; }"
    ".sch-value { fill: var(--sch-ink, #171717); }"
    ".sch-label { fill: var(--net-color, var(--sch-ink, #171717)); }"
    ".sch-label-pill { fill: var(--accent-soft, #ffe4db); stroke: var(--accent, #ff5c35); stroke-width: 0.2; }"
    ".sch-label-pill-text { fill: var(--accent, #ff5c35); font-weight: 600; }"
    ".sch-note { fill: none; stroke: var(--sch-note, #8a7f6a); }"
    ".sch-note-text { fill: var(--sch-note, #8a7f6a); }"
    ".sch-sheet-box { fill: var(--sch-page, #ffffff); stroke: var(--sch-ink, #171717); stroke-width: 0.254; }"
    ".sch-sheet-text { fill: var(--sch-ink, #171717); }"
    ".sch-missing { fill: none; stroke: var(--sch-note, #b0543f); stroke-width: 0.2; stroke-dasharray: 0.8 0.5; }"
    ".sch-filled-body { fill: var(--sch-body, #f0ede4); stroke: var(--sch-ink, #171717); }"
    ".sch-filled-page { fill: var(--sch-page, #ffffff); stroke: var(--sch-ink, #171717); }"
    ".sch-graphic { fill: none; stroke: var(--sch-ink, #171717); }"
    # Class-scoped so the rule stays safe when the SVG is inlined into the
    # explorer page next to the board artwork (inline <style> is global).
    ".sch-ref, .sch-value, .sch-pin-number, .sch-pin-name, .sch-label,"
    " .sch-label-pill-text, .sch-note-text, .sch-sheet-text"
    " { font-family: 'Segoe UI', Arial, sans-serif; }"
)


def _escape(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _font_height(node, default=DEFAULT_FONT_HEIGHT):
    effects = child(node, "effects")
    if effects is None:
        return default
    font = child(effects, "font")
    if font is None:
        return default
    size = child(font, "size")
    if size is None or len(size) < 2:
        return default
    return as_float(size[1], default)


def _justify(node):
    """Horizontal anchor ('start'|'middle'|'end') and vertical ('hanging'|'central'|'auto')."""
    effects = child(node, "effects")
    horizontal, vertical = "middle", "central"
    if effects is not None:
        justify = child(effects, "justify")
        if justify is not None:
            for atom in justify[1:]:
                atom_text = str(atom)
                if atom_text in ("left", "right"):
                    horizontal = "start" if atom_text == "left" else "end"
                elif atom_text in ("top", "bottom"):
                    vertical = "hanging" if atom_text == "top" else "auto"
    return horizontal, vertical


def _rotate_attr(angle_degrees, x, y):
    # KiCad angles are counter-clockwise on a Y-down sheet; SVG rotate() is
    # clockwise, so the sign flips to keep text and pills lying as in KiCad.
    if abs(angle_degrees % 360) < 0.001:
        return ""
    return f' transform="rotate({-angle_degrees:.4f} {x:.4f} {y:.4f})"'


def _text_lines(text):
    return str(text).split("\n")


def _split_value_lines(text):
    """Spread a long value across two lines at the boundary nearest the middle."""
    text = str(text)
    if len(text) <= 8 or len(_text_lines(text)) > 1:
        return _text_lines(text)
    middle = len(text) / 2
    best_index, best_distance = None, math.inf
    for index, character in enumerate(text):
        if character in (" ", "-", "_", "/"):
            distance = abs(index + 1 - middle)
            if distance < best_distance:
                best_index, best_distance = index + 1, distance
    if best_index is None:
        best_index = int(round(middle))
    return [text[:best_index].rstrip(), text[best_index:].lstrip()]


SYMBOL_OVERLAP_WEIGHT = 4
WIRE_OVERLAP_WEIGHT = 1
OVERLAP_PAD = 0.2


def _rects_overlap(first, second, pad=OVERLAP_PAD):
    return not (
        first[2] < second[0] - pad
        or second[2] < first[0] - pad
        or first[3] < second[1] - pad
        or second[3] < first[1] - pad
    )


def _segment_hits_rect(segment, rect, samples=16):
    (start_x, start_y), (end_x, end_y) = segment
    for index in range(samples + 1):
        fraction = index / samples
        x = start_x + (end_x - start_x) * fraction
        y = start_y + (end_y - start_y) * fraction
        if (
            rect[0] - OVERLAP_PAD <= x <= rect[2] + OVERLAP_PAD
            and rect[1] - OVERLAP_PAD <= y <= rect[3] + OVERLAP_PAD
        ):
            return True
    return False


def _overlap_score(rect, obstacles):
    """How badly a label block rectangle collides with the sheet around it.

    Obstacles are ("rect", (x0, y0, x1, y1)) for other symbols' bodies —
    weighted heavily, since covering another part is the worst outcome — and
    ("seg", ((x0, y0), (x1, y1))) for wire segments.
    """
    score = 0
    for kind, geometry in obstacles:
        if kind == "rect":
            if _rects_overlap(rect, geometry):
                score += SYMBOL_OVERLAP_WEIGHT
        elif _segment_hits_rect(geometry, rect):
            score += WIRE_OVERLAP_WEIGHT
    return score


def _text_extent(text, height):
    lines = _text_lines(text)
    width = max((len(line) for line in lines), default=0) * height * TEXT_WIDTH_FACTOR
    return width, len(lines) * height * LINE_HEIGHT_FACTOR


def _node_point(node, point_tag, default=(0.0, 0.0)):
    point_node = child(node, point_tag)
    if point_node is None or len(point_node) < 3:
        return default
    return as_float(point_node[1]), as_float(point_node[2])


def _node_at(node, point_tag="at"):
    """(x, y, angle) with a zero angle when the node omits it."""
    point_node = child(node, point_tag)
    if point_node is None or len(point_node) < 3:
        return 0.0, 0.0, 0.0
    return as_float(point_node[1]), as_float(point_node[2]), as_float(point_node[3]) if len(point_node) > 3 else 0.0


def _node_points(node):
    pts = child(node, "pts")
    if pts is None:
        return []
    return [
        (as_float(point[1]), as_float(point[2]))
        for point in children(pts, "xy")
        if len(point) >= 3
    ]


def _stroke_width_of(node, default=DEFAULT_GRAPHIC_WIDTH):
    stroke = child(node, "stroke")
    if stroke is not None:
        width = as_float(value(stroke, "width", 0.0))
        if width > 0:
            return width
    return default


def _fill_class(node):
    fill = child(node, "fill")
    if fill is None:
        return ""
    fill_type = str(value(fill, "type", "none"))
    if fill_type == "outline":
        return " sch-filled-body"
    if fill_type == "background":
        return " sch-filled-page"
    return ""


def _polyline_path(points):
    return " ".join(
        f"{'M' if index == 0 else 'L'}{x:.4f} {y:.4f}" for index, (x, y) in enumerate(points)
    )


def _arc_flags(start, middle, end):
    """(radius, large_arc, sweep) for an arc through three fitted points."""
    ax, ay = start
    bx, by = middle
    cx, cy = end
    determinant = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if abs(determinant) < 1e-9:
        return None
    ux = (
        (ax * ax + ay * ay) * (by - cy)
        + (bx * bx + by * by) * (cy - ay)
        + (cx * cx + cy * cy) * (ay - by)
    ) / determinant
    uy = (
        (ax * ax + ay * ay) * (cx - bx)
        + (bx * bx + by * by) * (ax - cx)
        + (cx * cx + cy * cy) * (bx - ax)
    ) / determinant
    radius = math.hypot(ax - ux, ay - uy)
    cross = (bx - ax) * (cy - by) - (by - ay) * (cx - bx)
    sweep = 0 if cross > 0 else 1
    sweep_sign = 1 if sweep == 1 else -1

    def sweep_to(angle_from, angle_to):
        delta = (angle_to - angle_from) * sweep_sign
        while delta < 0:
            delta += 2 * math.pi
        while delta >= 2 * math.pi:
            delta -= 2 * math.pi
        return delta

    start_angle = math.atan2(ay - uy, ax - ux)
    mid_angle = math.atan2(by - uy, bx - ux)
    end_angle = math.atan2(cy - uy, cx - ux)
    large_arc = 1 if sweep_to(start_angle, mid_angle) + sweep_to(mid_angle, end_angle) > math.pi else 0
    return radius, large_arc, sweep


class _Bounds:
    def __init__(self):
        self.min_x = math.inf
        self.min_y = math.inf
        self.max_x = -math.inf
        self.max_y = -math.inf

    def add(self, x, y):
        self.min_x = min(self.min_x, x)
        self.min_y = min(self.min_y, y)
        self.max_x = max(self.max_x, x)
        self.max_y = max(self.max_y, y)

    def add_point(self, point):
        self.add(point[0], point[1])

    def add_text(self, x, y, text, height, horizontal, vertical):
        width, height_total = _text_extent(text, height)
        if horizontal == "start":
            x0, x1 = x, x + width
        elif horizontal == "end":
            x0, x1 = x - width, x
        else:
            x0, x1 = x - width / 2, x + width / 2
        if vertical == "hanging":
            y0, y1 = y, y + height_total
        elif vertical == "auto":
            y0, y1 = y - height_total, y
        else:
            y0, y1 = y - height_total / 2, y + height_total / 2
        self.add(x0, y0)
        self.add(x1, y1)

    @property
    def valid(self):
        return self.min_x != math.inf

    def merged(self, other):
        result = _Bounds()
        for bounds in (self, other):
            if bounds.valid:
                result.add(bounds.min_x, bounds.min_y)
                result.add(bounds.max_x, bounds.max_y)
        return result


def _unit_identity(name):
    """Unit and body style encoded in a lib sub-symbol name like BASE_1_0."""
    parts = str(name).rsplit("_", 2)
    if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
        return int(parts[1]), int(parts[2])
    return None


class SymbolInstance:
    def __init__(self, node, library_symbols):
        self.node = node
        self.library_id = value(node, "lib_id", "")
        at = child(node, "at")
        self.x = as_float(at[1]) if at is not None and len(at) > 1 else 0.0
        self.y = as_float(at[2]) if at is not None and len(at) > 2 else 0.0
        self.rotation = as_float(at[3]) if at is not None and len(at) > 3 else 0.0
        mirror_node = child(node, "mirror")
        self.mirror = str(mirror_node[1]) if mirror_node is not None and len(mirror_node) > 1 else ""
        self.unit = as_int(value(node, "unit", 1), 1)
        self.body_style = as_int(value(node, "body_style", 1), 1)
        self.library_symbol = library_symbols.get(self.library_id)
        self.properties = {}
        for property_node in children(node, "property"):
            if len(property_node) < 3:
                continue
            x, y, angle = _node_at(property_node)
            self.properties[str(property_node[1])] = {
                "value": str(property_node[2]),
                "hidden": child(property_node, "hide") is not None,
                "x": x,
                "y": y,
                "angle": angle,
                "height": _font_height(property_node),
                "justify": _justify(property_node),
            }
        self.reference = self.properties.get("Reference", {}).get("value", "")
        self.value = self.properties.get("Value", {}).get("value", "")

    def group_transform(self):
        """Transform applied to library points already converted to Y-down.

        Matches kicad_processing_agent: mirror flips the Y-down local point,
        then the symbol rotates by the negative of the stored angle.
        """
        scale_x, scale_y = 1.0, 1.0
        if self.mirror == "x":
            scale_y = -1.0
        elif self.mirror == "y":
            scale_x = -1.0
        transform = f"translate({self.x:.4f} {self.y:.4f})"
        if abs(self.rotation % 360) > 0.001:
            transform += f" rotate({-self.rotation:.4f})"
        if scale_x != 1.0 or scale_y != 1.0:
            transform += f" scale({scale_x:.4f} {scale_y:.4f})"
        return transform

    def place(self, lib_x, lib_y):
        """Absolute sheet coordinate of a library point (Y-up input)."""
        return transform_point(
            (lib_x, -lib_y),
            origin=(self.x, self.y),
            angle_degrees=-self.rotation,
            mirror=self.mirror,
        )

    def unit_nodes(self):
        """The library symbol plus every unit/body-style sub-symbol drawn."""
        if self.library_symbol is None:
            return []
        selected = [self.library_symbol]
        for unit_symbol in children(self.library_symbol, "symbol"):
            if len(unit_symbol) < 2 or isinstance(unit_symbol[1], list):
                continue
            identity = _unit_identity(unit_symbol[1])
            if identity is None:
                continue
            symbol_unit, symbol_style = identity
            if symbol_unit in (0, self.unit) and symbol_style in (0, self.body_style):
                selected.append(unit_symbol)
        return selected

    def graphic_nodes(self):
        for node in self.unit_nodes():
            items = node[2:] if node is self.library_symbol else node[1:]
            for item in items:
                if isinstance(item, list) and tag(item) in ("polyline", "rectangle", "circle", "arc", "text"):
                    yield item

    @staticmethod
    def _pin_endpoints(pin_node):
        """(connection, body_end) library coordinates for a pin node."""
        at = child(pin_node, "at")
        if at is None or len(at) < 4:
            return None
        pin_x, pin_y = as_float(at[1]), as_float(at[2])
        pin_angle = as_float(at[3])
        length = as_float(value(pin_node, "length", 0.0))
        radians = math.radians(pin_angle)
        # Library pins extend along +x at angle 0 (Y-up coordinates).
        body = (pin_x + length * math.cos(radians), pin_y + length * math.sin(radians))
        return (pin_x, pin_y), body

    def pins(self):
        pins = []
        for node in self.unit_nodes():
            for pin_node in children(node, "pin"):
                endpoints = self._pin_endpoints(pin_node)
                if endpoints is None:
                    continue
                connection, body = endpoints
                name_node = child(pin_node, "name")
                number_node = child(pin_node, "number")
                pins.append(
                    {
                        "connection": self.place(*connection),
                        "body_end": self.place(*body),
                        "number": str(number_node[1]) if number_node is not None and len(number_node) > 1 else "",
                        "name": str(name_node[1]) if name_node is not None and len(name_node) > 1 else "",
                    }
                )
        return pins

    def visible_texts(self):
        return {
            name: text
            for name, text in self.properties.items()
            if name in ("Reference", "Value") and not text["hidden"] and text["value"]
        }

    def placed_shape_bounds(self):
        """Placed bounds of the body shapes only (no pins, no property text)."""
        bounds = _Bounds()
        for item in self.graphic_nodes():
            item_tag = tag(item)
            if item_tag == "polyline":
                for point in _node_points(item):
                    bounds.add_point(self.place(*point))
            elif item_tag == "rectangle":
                bounds.add_point(self.place(*_node_point(item, "start")))
                bounds.add_point(self.place(*_node_point(item, "end")))
            elif item_tag == "circle":
                center = self.place(*_node_point(item, "center"))
                radius = as_float(value(item, "radius", 0.0))
                bounds.add(center[0] - radius, center[1] - radius)
                bounds.add(center[0] + radius, center[1] + radius)
            elif item_tag == "arc":
                for point_tag in ("start", "mid", "end"):
                    bounds.add_point(self.place(*_node_point(item, point_tag)))
        return bounds

    def label_layout(self, obstacles):
        """Choose and lay out the identifier/value block for this symbol.

        Four candidates are generated — above, below, left and right of the
        body — and each is scored against the sheet obstacles (other symbols'
        bodies and the wires) using placed-coordinate overlap tests; the
        candidate overlapping least wins, with the classic above-first tie
        break.  Everything runs here in Python so the emitted SVG needs no
        layout logic in the page.  The stack itself keeps the bold identifier
        closest to the body with the value above it, on tighter line spacing,
        and the whole block rotates (and mirrors) with the part.
        """
        local_bounds = _Bounds()
        for item in self.graphic_nodes():
            item_tag = tag(item)
            if item_tag == "polyline":
                for point in _node_points(item):
                    local_bounds.add(point[0], -point[1])
            elif item_tag == "rectangle":
                for point in (_node_point(item, "start"), _node_point(item, "end")):
                    local_bounds.add(point[0], -point[1])
            elif item_tag == "circle":
                center = _node_point(item, "center")
                radius = as_float(value(item, "radius", 0.0))
                local_bounds.add(center[0] - radius, -center[1] - radius)
                local_bounds.add(center[0] + radius, -center[1] + radius)
            elif item_tag == "arc":
                for point_tag in ("start", "mid", "end"):
                    point = _node_point(item, point_tag)
                    local_bounds.add(point[0], -point[1])
        if not local_bounds.valid or not self.reference or self.reference.startswith("#"):
            return None
        placed_bounds = self.placed_shape_bounds()
        width = local_bounds.max_x - local_bounds.min_x
        height = local_bounds.max_y - local_bounds.min_y
        package = width >= 6.0 and height >= 6.0 and max(width, height) / min(width, height) <= 2.5
        center_x = (local_bounds.min_x + local_bounds.max_x) / 2
        center_y = (local_bounds.min_y + local_bounds.max_y) / 2

        def fit(font, text, factor=TEXT_WIDTH_FACTOR):
            return min(font, (width * 0.9) / max(1, len(text)) / factor)

        # Sized to read when the whole sheet is zoomed out; bold reference,
        # regular value, both in the ink colour (never grey).
        reference_font = fit(min(3.6, max(2.2, width * 0.4)), self.reference, 0.68)
        value_lines = _split_value_lines(self.value)
        value_font = fit(min(reference_font * 0.8, max(1.6, width * 0.28)), self.value)
        if len(value_lines) == 2:
            longest = max(len(line) for line in value_lines)
            value_font = min(value_font, (width * 0.9) / max(1, longest) / TEXT_WIDTH_FACTOR)
        # The "above" candidate in local coordinates: reference hugging the
        # body, value line(s) above it, tight line spacing.  Value lines are
        # appended bottom-up so a wrapped value reads top-down.
        lines = [("reference", self.reference, reference_font)]
        for value_line in reversed(value_lines):
            lines.append(("value", value_line, value_font))
        gap = value_font * 1.15
        cursor = local_bounds.min_y - 0.3
        local_lines = []
        for kind, text, font in lines:
            cursor -= font * 0.5
            local_lines.append((kind, text, center_x, cursor, font))
            cursor -= font * (0.55 if kind == "reference" else 0.5) + gap * (0.35 if kind == "reference" else 0.5)
        text_width = max(
            len(text) * font * TEXT_WIDTH_FACTOR for _, text, _, _, font in local_lines
        ) + reference_font * 0.4
        block_top = min(row[3] for row in local_lines) - reference_font * 0.55
        block_bottom = max(row[3] for row in local_lines) + value_font * 0.55
        local_rect = (
            center_x - text_width / 2,
            block_top,
            center_x + text_width / 2,
            block_bottom,
        )

        def rotated_rect(angle_degrees):
            radians = math.radians(angle_degrees)
            cosine, sine = math.cos(radians), math.sin(radians)
            corners = []
            for rect_x in (local_rect[0], local_rect[2]):
                for rect_y in (local_rect[1], local_rect[3]):
                    dx, dy = rect_x - center_x, rect_y - center_y
                    corners.append((center_x + dx * cosine - dy * sine, center_y + dx * sine + dy * cosine))
            placed = _Bounds()
            for corner in corners:
                placed.add_point(self.place(corner[0], -corner[1]))
            return (placed.min_x, placed.min_y, placed.max_x, placed.max_y)

        best = None
        for side, side_angle in (("above", 0), ("below", 180), ("left", -90), ("right", 90)):
            rect = rotated_rect(side_angle)
            score = _overlap_score(rect, obstacles)
            if best is None or score < best[0]:
                best = (score, side, side_angle, rect)
        _, side, side_angle, _ = best
        radians = math.radians(side_angle)
        cosine, sine = math.cos(radians), math.sin(radians)
        placed_lines = []
        for kind, text, line_x, line_y, font in local_lines:
            dx, dy = line_x - center_x, line_y - center_y
            moved_x = center_x + dx * cosine - dy * sine
            moved_y = center_y + dx * sine + dy * cosine
            placed_x, placed_y = self.place(moved_x, -moved_y)
            placed_lines.append((kind, text, placed_x, placed_y, font))
        return {
            "min_x": placed_bounds.min_x,
            "min_y": placed_bounds.min_y,
            "max_x": placed_bounds.max_x,
            "max_y": placed_bounds.max_y,
            "width": width,
            "height": height,
            "package": package,
            "side": side,
            "text_angle": -self.rotation + side_angle,
            "lines": placed_lines,
        }

    def placed_graphics_bounds(self):
        bounds = _Bounds()
        for item in self.graphic_nodes():
            item_tag = tag(item)
            if item_tag == "polyline":
                for point in _node_points(item):
                    bounds.add_point(self.place(*point))
            elif item_tag == "rectangle":
                bounds.add_point(self.place(*_node_point(item, "start")))
                bounds.add_point(self.place(*_node_point(item, "end")))
            elif item_tag == "circle":
                center = self.place(*_node_point(item, "center"))
                radius = as_float(value(item, "radius", 0.0))
                bounds.add(center[0] - radius, center[1] - radius)
                bounds.add(center[0] + radius, center[1] + radius)
            elif item_tag == "arc":
                for point_tag in ("start", "mid", "end"):
                    bounds.add_point(self.place(*_node_point(item, point_tag)))
            elif item_tag == "text":
                x, y, angle = _node_at(item)
                placed = self.place(x, y)
                bounds.add_text(placed[0], placed[1], str(item[1]) if len(item) > 1 else "", _font_height(item), *(_justify(item)))
        for pin in self.pins():
            bounds.add_point(pin["connection"])
            bounds.add_point(pin["body_end"])
        for text in self.visible_texts().values():
            bounds.add_text(text["x"], text["y"], text["value"], text["height"], *text["justify"])
        return bounds


class SchematicPage:
    """One sheet of the hierarchy with its placed symbols and drawn items."""

    def __init__(self, path, root, name=""):
        self.path = Path(path)
        self.root = root
        self.name = name
        library_symbols = {}
        container = child(root, "lib_symbols")
        if container is not None:
            for library_symbol in children(container, "symbol"):
                if len(library_symbol) > 1 and isinstance(library_symbol[1], str):
                    library_symbols[library_symbol[1]] = library_symbol
        self.instances = [SymbolInstance(node, library_symbols) for node in children(root, "symbol")]
        self.bounds = _Bounds()
        self.offset = (0.0, 0.0)

    def connectivity(self):
        """Net name per coordinate, using the extractor's union-find rules.

        Wires, junctions, label anchors, no-connects, pin points and power
        symbol pins are unioned (including ends landing mid-segment); global
        labels and power symbol values name the run, local labels fall back.
        """
        parent = {}

        def find(item):
            parent.setdefault(item, item)
            while parent[item] != item:
                parent[item] = parent[parent[item]]
                item = parent[item]
            return item

        def union(first, second):
            parent.setdefault(first, first)
            parent.setdefault(second, second)
            first_root, second_root = find(first), find(second)
            if first_root != second_root:
                parent[max(first_root, second_root)] = min(first_root, second_root)

        def key(point):
            return round(point[0], 4), round(point[1], 4)

        segments = []
        registered = []

        def register(point):
            point_key = key(point)
            find(point_key)
            registered.append(point_key)
            return point_key

        for wire_node in children(self.root, "wire"):
            points = _node_points(wire_node)
            for start, end in zip(points, points[1:]):
                segments.append((key(start), key(end)))
                union(register(start), register(end))
        for node_tag in ("junction", "no_connect", "label", "global_label", "hierarchical_label"):
            for node in children(self.root, node_tag):
                at = child(node, "at")
                if at is not None and len(at) >= 3:
                    register((as_float(at[1]), as_float(at[2])))
        names_by_root = {}
        for node_tag, scope in (("label", "local"), ("global_label", "global"), ("hierarchical_label", "local")):
            for node in children(self.root, node_tag):
                if len(node) < 2:
                    continue
                at = child(node, "at")
                if at is None or len(at) < 3:
                    continue
                names_by_root.setdefault(find(key((as_float(at[1]), as_float(at[2])))), []).append(
                    (scope, str(node[1]))
                )
        for instance in self.instances:
            for pin in instance.pins():
                pin_key = register(pin["connection"])
                if instance.reference.startswith("#") and instance.value:
                    names_by_root.setdefault(find(pin_key), []).append(("power", instance.value))
        # Every connection point joins the wire run it touches — including
        # points that coincide with a segment endpoint, which is how two wire
        # polylines, a pin, a power symbol or a label merge into one net.
        # Without this each polyline stays its own run and following a net
        # would only light one segment.
        for point_key in set(registered):
            for start, end in segments:
                if point_on_segment(point_key, start, end):
                    union(point_key, start)
                    break

        def net_for(point_key):
            entry = names_by_root.get(find(point_key))
            if not entry:
                return ""
            global_names = sorted({name for scope, name in entry if scope in ("global", "power")})
            if global_names:
                return global_names[0]
            local_names = sorted({name for scope, name in entry if scope == "local"})
            return local_names[0] if local_names else ""

        names = {}
        runs = {}
        for point_key in set(registered):
            names[point_key] = net_for(point_key)
            # Run id: which electrical run root this point belongs to.  Runs
            # without a label still get a stable id so the explorer can group
            # (and resolve through their pins) every wire drawn on them.
            root = find(point_key)
            runs[point_key] = f"{self.path.name}:{root[0]:.4f},{root[1]:.4f}"
        return names, runs


class SchematicModel:
    """Parsed hierarchy of one project, ready to emit the full sheet or previews."""

    def __init__(self, project_directory, schematic_files):
        self.project_directory = Path(project_directory)
        self.pages = []
        self.sheet_boxes = []
        self._visited = set()
        self._load_pages(schematic_files, name="")
        self._arrange_pages()

    def _resolve(self, base_path, schematic_file):
        path = Path(schematic_file)
        if not path.is_absolute():
            path = base_path / path
        return path.resolve()

    def _load_pages(self, schematic_files, name):
        for schematic_file in schematic_files:
            path = self._resolve(self.project_directory, schematic_file)
            if str(path) in self._visited or not path.is_file():
                continue
            self._visited.add(str(path))
            root = load(path)
            if tag(root) != "kicad_sch":
                continue
            page = SchematicPage(path, root, name=name)
            self.pages.append(page)
            for sheet_node in children(root, "sheet"):
                sheet_name = ""
                sheet_file = ""
                for property_node in children(sheet_node, "property"):
                    if len(property_node) >= 3:
                        if str(property_node[1]) == "Sheetname":
                            sheet_name = str(property_node[2])
                        elif str(property_node[1]) == "Sheetfile":
                            sheet_file = str(property_node[2])
                if not sheet_file:
                    continue
                try:
                    relative = path.parent.joinpath(sheet_file).resolve().relative_to(self.project_directory).as_posix()
                except ValueError:
                    relative = str(path.parent.joinpath(sheet_file).resolve())
                self.sheet_boxes.append({"page": page, "node": sheet_node, "file": relative, "name": sheet_name})
                self._load_pages([relative], name=sheet_name or sheet_file)

    def _arrange_pages(self):
        x_cursor = 0.0
        for index, page in enumerate(self.pages):
            page.bounds = self._page_bounds(page)
            if index == 0:
                page.offset = (0.0, 0.0)
                x_cursor = page.bounds.max_x - page.bounds.min_x
            else:
                page.offset = (x_cursor + PAGE_GAP_MM - page.bounds.min_x, -page.bounds.min_y)
                x_cursor = page.offset[0] + (page.bounds.max_x - page.bounds.min_x)

    def _page_bounds(self, page):
        bounds = _Bounds()
        for instance in page.instances:
            instance_bounds = instance.placed_graphics_bounds()
            if instance_bounds.valid:
                bounds = bounds.merged(instance_bounds)
        for wire_node in children(page.root, "wire"):
            for point in _node_points(wire_node):
                bounds.add_point(point)
        for bus_node in children(page.root, "bus"):
            for point in _node_points(bus_node):
                bounds.add_point(point)
        for node_tag in ("junction", "no_connect"):
            for node in children(page.root, node_tag):
                at = child(node, "at")
                if at is not None and len(at) >= 3:
                    bounds.add(as_float(at[1]), as_float(at[2]))
        for node_tag in ("label", "global_label", "hierarchical_label"):
            for node in children(page.root, node_tag):
                at = child(node, "at")
                if at is None or len(at) < 3:
                    continue
                bounds.add_text(
                    as_float(at[1]), as_float(at[2]), str(node[1]) if len(node) > 1 else "",
                    _font_height(node), "start", "central",
                )
        for node in children(page.root, "rectangle"):
            for point_tag in ("start", "end"):
                point = _node_point(node, point_tag)
                bounds.add_point(point)
        for node in children(page.root, "polyline"):
            for point in _node_points(node):
                bounds.add_point(point)
        for node in children(page.root, "text"):
            at = child(node, "at")
            if at is not None and len(at) >= 3:
                bounds.add_text(
                    as_float(at[1]), as_float(at[2]), str(node[1]) if len(node) > 1 else "",
                    _font_height(node), *(_justify(node)),
                )
        for node in children(page.root, "text_box"):
            at = child(node, "at")
            size = child(node, "size")
            if at is not None and len(at) >= 3 and size is not None and len(size) >= 3:
                x, y = as_float(at[1]), as_float(at[2])
                bounds.add(x, y)
                bounds.add(x + as_float(size[1]), y + as_float(size[2]))
        for box in self.sheet_boxes:
            if box["page"] is page:
                bounds = bounds.merged(self._sheet_box_bounds(box["node"]))
        if not bounds.valid:
            bounds.add(0, 0)
            bounds.add(100, 60)
        return bounds

    @staticmethod
    def _sheet_box_bounds(sheet_node):
        bounds = _Bounds()
        at = child(sheet_node, "at")
        size = child(sheet_node, "size")
        if at is not None and len(at) >= 3 and size is not None and len(size) >= 3:
            x, y = as_float(at[1]), as_float(at[2])
            width, height = as_float(size[1]), as_float(size[2])
            bounds.add(x, y)
            bounds.add(x + width, y + height)
        return bounds

    def _symbol_svg(self, instance, names=None, runs=None, plan=None):
        names = names or {}
        runs = runs or {}
        plan = plan if plan is not None else instance.label_layout([])
        lines = [
            f'<g class="sch-symbol" data-reference="{_escape(instance.reference)}" '
            f'data-value="{_escape(instance.value)}" tabindex="0"'
        ]
        if plan is not None:
            # Tight body bounds for the explorer's selection rectangle; the
            # group's own bbox would include pin stubs and the label block.
            pad = 0.35
            lines.append(
                f' data-bounds="{plan["min_x"] - pad:.4f},{plan["min_y"] - pad:.4f},'
                f'{plan["max_x"] - plan["min_x"] + pad * 2:.4f},{plan["max_y"] - plan["min_y"] + pad * 2:.4f}"'
            )
        lines.append(">")
        if instance.library_symbol is None:
            lines.append(
                f'<g transform="{instance.group_transform()}">'
                f'<rect class="sch-missing" x="-4" y="-2.5" width="8" height="5" rx="0.4" /></g>'
            )
        else:
            lines.append(f'<g transform="{instance.group_transform()}">')
            for item in instance.graphic_nodes():
                item_tag = tag(item)
                # Symbol artwork shares the wire weight so two-pin parts don't
                # look fainter than the nets around them.
                width = WIRE_VISUAL_WIDTH
                if item_tag == "polyline":
                    points = [(x, -y) for x, y in _node_points(item)]
                    if len(points) >= 2:
                        lines.append(
                            f'<path class="sch-graphic{_fill_class(item)}" stroke-width="{width:.4f}" '
                            f'd="{_polyline_path(points)}" />'
                        )
                elif item_tag == "rectangle":
                    start = _node_point(item, "start")
                    end = _node_point(item, "end")
                    lines.append(
                        f'<rect class="sch-graphic{_fill_class(item)}" stroke-width="{width:.4f}" '
                        f'x="{min(start[0], end[0]):.4f}" y="{-max(start[1], end[1]):.4f}" '
                        f'width="{abs(end[0] - start[0]):.4f}" height="{abs(end[1] - start[1]):.4f}" />'
                    )
                elif item_tag == "circle":
                    center = _node_point(item, "center")
                    lines.append(
                        f'<circle class="sch-graphic{_fill_class(item)}" stroke-width="{width:.4f}" '
                        f'cx="{center[0]:.4f}" cy="{-center[1]:.4f}" r="{as_float(value(item, "radius", 0.0)):.4f}" />'
                    )
                elif item_tag == "arc":
                    start = _node_point(item, "start")
                    middle = _node_point(item, "mid")
                    end = _node_point(item, "end")
                    flags = _arc_flags((start[0], -start[1]), (middle[0], -middle[1]), (end[0], -end[1]))
                    if flags is None:
                        lines.append(
                            f'<path class="sch-graphic{_fill_class(item)}" stroke-width="{width:.4f}" '
                            f'd="M{start[0]:.4f} {-start[1]:.4f} L{end[0]:.4f} {-end[1]:.4f}" />'
                        )
                    else:
                        radius, large_arc, sweep = flags
                        lines.append(
                            f'<path class="sch-graphic{_fill_class(item)}" stroke-width="{width:.4f}" '
                            f'd="M{start[0]:.4f} {-start[1]:.4f} A{radius:.4f} {radius:.4f} 0 {large_arc} {sweep} '
                            f'{end[0]:.4f} {-end[1]:.4f}" />'
                        )
                elif item_tag == "text":
                    x, y, angle = _node_at(item)
                    placed = instance.place(x, y)
                    horizontal, vertical = _justify(item)
                    lines.append(
                        f'<text class="sch-value" x="{placed[0]:.4f}" y="{placed[1]:.4f}" '
                        f'font-size="{_font_height(item):.4f}" text-anchor="{horizontal}" '
                        f'dominant-baseline="{vertical}"{_rotate_attr(angle, placed[0], placed[1])}'
                        f'>{_escape(str(item[1]) if len(item) > 1 else "")}</text>'
                    )
            for node in instance.unit_nodes():
                for pin_node in children(node, "pin"):
                    endpoints = SymbolInstance._pin_endpoints(pin_node)
                    if endpoints is None:
                        continue
                    connection, body = endpoints
                    lines.append(
                        f'<line class="sch-pin" x1="{connection[0]:.4f}" y1="{-connection[1]:.4f}" '
                        f'x2="{body[0]:.4f}" y2="{-body[1]:.4f}" />'
                    )
            lines.append("</g>")
        used_inside_labels = []
        for pin in instance.pins():
            connection, body_end = pin["connection"], pin["body_end"]
            dx = body_end[0] - connection[0]
            dy = body_end[1] - connection[1]
            length = math.hypot(dx, dy)
            if length < 0.01:
                continue
            ux, uy = dx / length, dy / length
            perpendicular = (-uy, ux)
            point_key = (round(connection[0], 4), round(connection[1], 4))
            pin_net = names.get(point_key, "")
            pin_run = runs.get(point_key, "")
            pin_net_attribute = f' data-net="{_escape(pin_net)}"' if pin_net else ""
            pin_run_attribute = f' data-run="{_escape(pin_run)}"' if pin_run else ""
            # A fat invisible twin of the pin stub gives the click target some
            # width; the explorer listens on these to select pin + net.
            lines.append(
                f'<line class="sch-pin-hit" data-reference="{_escape(instance.reference)}" '
                f'data-pin="{_escape(pin["number"])}"{pin_net_attribute}{pin_run_attribute} '
                f'x1="{connection[0]:.4f}" y1="{connection[1]:.4f}" '
                f'x2="{body_end[0]:.4f}" y2="{body_end[1]:.4f}" />'
            )
            # Eagle-imported libraries often carry the meaningful pin function
            # ("VBUS", "SHIELD1") in the number field and a placeholder in the
            # name field — display whichever is the real identifier.
            number, name = pin["number"], pin["name"]
            packaged = plan is not None and plan["package"]
            number_is_placeholder = bool(re.fullmatch(r"P\$\d+", number or ""))
            if packaged:
                if number and not number.isdigit() and not number_is_placeholder:
                    inside_label, inside_is_number = number, True
                elif name and name != number:
                    inside_label, inside_is_number = name, False
                else:
                    inside_label, inside_is_number = "", False
            else:
                inside_label, inside_is_number = (name if name and name != number and length > 1.2 else ""), False
            if number and number != name and not (packaged and inside_is_number):
                number_x = connection[0] + dx * 0.3 + perpendicular[0] * 0.85
                number_y = connection[1] + dy * 0.3 + perpendicular[1] * 0.85
                lines.append(
                    f'<text class="sch-pin-number" x="{number_x:.4f}" y="{number_y:.4f}" '
                    f'font-size="{PIN_LABEL_FONT:.4f}" text-anchor="middle" dominant-baseline="central">'
                    f'{_escape(number)}</text>'
                )
            if inside_label:
                if packaged:
                    # Packaged parts carry their pin names inside the outline,
                    # hugging the edge the pin enters through, large and bold.
                    # A label is dropped when it would sit on one already
                    # drawn (Eagle shield pins often share a corner).
                    name_font = min(
                        PIN_NAME_FONT,
                        (plan["width"] * 0.5) / max(1, len(inside_label)) / TEXT_WIDTH_FACTOR,
                    )
                    edge_distances = {
                        "left": body_end[0] - plan["min_x"],
                        "right": plan["max_x"] - body_end[0],
                        "top": body_end[1] - plan["min_y"],
                        "bottom": plan["max_y"] - body_end[1],
                    }
                    edge = min(edge_distances, key=edge_distances.get)
                    inset = name_font * 0.45
                    if edge == "left":
                        name_x = plan["min_x"] + inset
                        name_y = body_end[1]
                        anchor = "start"
                    elif edge == "right":
                        name_x = plan["max_x"] - inset
                        name_y = body_end[1]
                        anchor = "end"
                    elif edge == "top":
                        name_x = body_end[0]
                        name_y = plan["min_y"] + name_font * 0.8
                        anchor = "middle"
                    else:
                        name_x = body_end[0]
                        name_y = plan["max_y"] - name_font * 0.25
                        anchor = "middle"
                    label_width = len(inside_label) * name_font * TEXT_WIDTH_FACTOR
                    if anchor == "start":
                        label_rect = (name_x, name_x + label_width)
                    elif anchor == "end":
                        label_rect = (name_x - label_width, name_x)
                    else:
                        label_rect = (name_x - label_width / 2, name_x + label_width / 2)
                    label_rect = (
                        label_rect[0],
                        name_y - name_font * 0.7,
                        label_rect[1],
                        name_y + name_font * 0.7,
                    )
                    if any(_rects_overlap(label_rect, used, pad=0.05) for used in used_inside_labels):
                        continue
                    used_inside_labels.append(label_rect)
                    lines.append(
                        f'<text class="sch-pin-name" x="{name_x:.4f}" y="{name_y:.4f}" '
                        f'font-size="{name_font:.4f}" text-anchor="{anchor}" dominant-baseline="central">'
                        f'{_escape(inside_label)}</text>'
                    )
                    continue
                name_x = connection[0] + dx * 0.7 - perpendicular[0] * 0.9
                name_y = connection[1] + dy * 0.7 - perpendicular[1] * 0.9
                lines.append(
                    f'<text class="sch-pin-name" x="{name_x:.4f}" y="{name_y:.4f}" '
                    f'font-size="{PIN_LABEL_FONT:.4f}" text-anchor="middle" dominant-baseline="central">'
                    f'{_escape(inside_label)}</text>'
                )
        texts = instance.visible_texts()
        if plan is not None:
            # The bold identifier and its value sit beside the body on every
            # part (side chosen by the overlap test in label_layout), rotated
            # with the part and always reading in the block's own direction.
            texts = {name: text for name, text in texts.items() if name not in ("Reference", "Value")}
            for kind, line_text, placed_x, placed_y, font in plan["lines"]:
                css_class = "sch-ref" if kind == "reference" else "sch-value"
                lines.append(
                    f'<text class="{css_class}" x="{placed_x:.4f}" y="{placed_y:.4f}" '
                    f'font-size="{font:.4f}" text-anchor="middle" dominant-baseline="central"'
                    f'{_rotate_attr(plan["text_angle"], placed_x, placed_y)}>{_escape(line_text)}</text>'
                )
        for name, text in texts.items():
            css_class = "sch-ref" if name == "Reference" else "sch-value"
            horizontal, vertical = text["justify"]
            offset = 0.2 if horizontal == "start" else (-0.2 if horizontal == "end" else 0.0)
            lines.append(
                f'<text class="{css_class}" x="{text["x"] + offset:.4f}" y="{text["y"]:.4f}" '
                f'font-size="{text["height"]:.4f}" text-anchor="{horizontal}" '
                f'dominant-baseline="{vertical}"{_rotate_attr(text["angle"], text["x"], text["y"])}>'
                f'{_escape(text["value"])}</text>'
            )
        lines.append("</g>")
        return lines

    def _wire_svg(self, wire_node, names, runs):
        points = _node_points(wire_node)
        if len(points) < 2:
            return []
        start_key = (round(points[0][0], 4), round(points[0][1], 4))
        end_key = (round(points[-1][0], 4), round(points[-1][1], 4))
        net = names.get(start_key, "") or names.get(end_key, "")
        run = runs.get(start_key) or runs.get(end_key) or ""
        net_attribute = f' data-net="{_escape(net)}"' if net else ""
        run_attribute = f' data-run="{_escape(run)}"' if run else ""
        wire_path = _polyline_path(points)
        return [
            # Drawn bolder than KiCad's hairline so the sheet reads at explorer
            # zoom levels; the invisible fat twin underneath is what clicks hit.
            f'<path class="sch-wire"{net_attribute}{run_attribute} '
            f'stroke-width="{WIRE_VISUAL_WIDTH:.4f}" d="{wire_path}" />',
            f'<path class="sch-wire sch-wire-hit"{net_attribute}{run_attribute} d="{wire_path}" />',
        ]

    def _label_svg(self, node, kind, names, runs):
        at = child(node, "at")
        if at is None or len(at) < 3:
            return []
        x, y = as_float(at[1]), as_float(at[2])
        angle = as_float(at[3]) if len(at) > 3 else 0.0
        text_value = str(node[1]) if len(node) > 1 else ""
        height = _font_height(node)
        point_key = (round(x, 4), round(y, 4))
        net = names.get(point_key, "")
        run = runs.get(point_key, "")
        net_attribute = (
            f' data-net="{_escape(net or text_value)}" data-run="{_escape(run)}"' if net
            else f' data-run="{_escape(run)}"'
        )
        if kind == "label":
            # Wire labels become banners floating above the wire: same idea as
            # the arrow-ended net tags but beveled/pointed on both ends.
            tag_font = max(height, 1.4)
            text_width, _ = _text_extent(text_value, tag_font)
            banner_height = tag_font * 1.6
            tip = banner_height * 0.45
            half = text_width / 2 + tag_font * 0.55
            bottom = y - 0.45
            top = bottom - banner_height
            middle = (top + bottom) / 2
            left, right = x - half, x + half
            return [
                f'<g class="sch-label-tag"{net_attribute}>',
                f'<path class="sch-label-pill" d="M{left + tip:.4f} {top:.4f} L{right - tip:.4f} {top:.4f} '
                f'L{right:.4f} {middle:.4f} L{right - tip:.4f} {bottom:.4f} L{left + tip:.4f} {bottom:.4f} '
                f'L{left:.4f} {middle:.4f} Z" />',
                f'<text class="sch-label-pill-text" x="{x:.4f}" y="{middle:.4f}" '
                f'font-size="{tag_font:.4f}" text-anchor="middle" dominant-baseline="central">'
                f'{_escape(text_value)}</text>',
                "</g>",
            ]
        if kind == "global_label":
            # Net tags are the sheet's wayfinding: generously sized around a
            # larger font than KiCad's default.  The arrow side follows the
            # attachment angle but the text never rotates — KiCad keeps
            # global label text upright too, and a 180° sheet label used to
            # flip this one upside down.
            tag_font = max(height, 1.7)
            width, _ = _text_extent(text_value, tag_font)
            pill_height = tag_font * 1.9
            pill_length = width + tag_font * 1.2
            arrow = pill_height * 0.4
            half = pill_height / 2
            label_angle = angle % 360
            horizontal = label_angle < 45 or label_angle > 315 or 135 <= label_angle <= 225
            flipped = 135 < label_angle < 225
            if horizontal and flipped:
                return [
                    f'<g class="sch-global"{net_attribute}>',
                    f'<path class="sch-label-pill" d="M{x:.4f} {y - half:.4f} L{x - pill_length:.4f} '
                    f'{y - half:.4f} L{x - pill_length - arrow:.4f} {y:.4f} L{x - pill_length:.4f} '
                    f'{y + half:.4f} L{x:.4f} {y + half:.4f} Z" />',
                    f'<text class="sch-label-pill-text" x="{x - tag_font * 0.6:.4f}" y="{y:.4f}" '
                    f'font-size="{tag_font:.4f}" text-anchor="end" dominant-baseline="central">'
                    f'{_escape(text_value)}</text>',
                    "</g>",
                ]
            if horizontal:
                return [
                    f'<g class="sch-global"{net_attribute}>',
                    f'<path class="sch-label-pill" d="M{x:.4f} {y - half:.4f} L{x + pill_length:.4f} '
                    f'{y - half:.4f} L{x + pill_length + arrow:.4f} {y:.4f} L{x + pill_length:.4f} '
                    f'{y + half:.4f} L{x:.4f} {y + half:.4f} Z" />',
                    f'<text class="sch-label-pill-text" x="{x + tag_font * 0.6:.4f}" y="{y:.4f}" '
                    f'font-size="{tag_font:.4f}" text-anchor="start" dominant-baseline="central">'
                    f'{_escape(text_value)}</text>',
                    "</g>",
                ]
            # Vertical attachments keep the rotated pill; these are rare.
            return [
                f'<g class="sch-global"{net_attribute}{_rotate_attr(angle, x, y)}>',
                f'<path class="sch-label-pill" d="M{x:.4f} {y - half:.4f} L{x + pill_length:.4f} '
                f'{y - half:.4f} L{x + pill_length + arrow:.4f} {y:.4f} L{x + pill_length:.4f} '
                f'{y + half:.4f} L{x:.4f} {y + half:.4f} Z" />',
                f'<text class="sch-label-pill-text" x="{x + tag_font * 0.6:.4f}" y="{y:.4f}" '
                f'font-size="{tag_font:.4f}" text-anchor="start" dominant-baseline="central">{_escape(text_value)}</text>',
                "</g>",
            ]
        return [
            f'<text class="sch-label"{net_attribute} x="{x + height * 0.3:.4f}" '
            f'y="{y:.4f}" font-size="{height:.4f}" text-anchor="start" dominant-baseline="central"'
            f'{_rotate_attr(angle, x, y)}>{_escape(text_value)}</text>'
        ]

    def _sheet_box_svg(self, box):
        at = child(box["node"], "at")
        size = child(box["node"], "size")
        if at is None or len(at) < 3 or size is None or len(size) < 3:
            return []
        x, y = as_float(at[1]), as_float(at[2])
        width, height = as_float(size[1]), as_float(size[2])
        lines = [
            "<g>",
            f'<rect class="sch-sheet-box" data-sheet="{_escape(box["file"])}" '
            f'x="{x:.4f}" y="{y:.4f}" width="{width:.4f}" height="{height:.4f}" />',
        ]
        if box["name"]:
            lines.append(
                f'<text class="sch-sheet-text" x="{x + 0.6:.4f}" y="{y + 1.8:.4f}" font-size="1.27" '
                f'text-anchor="start" dominant-baseline="auto">{_escape(box["name"])}</text>'
            )
        lines.append(
            f'<text class="sch-sheet-text" x="{x + 0.6:.4f}" y="{y + height - 0.4:.4f}" font-size="1.0" '
            f'text-anchor="start" dominant-baseline="auto">{_escape(box["file"])}</text>'
        )
        lines.append("</g>")
        return lines

    def _page_obstacles(self, page):
        """Placed-coordinate obstacles for label placement on one sheet."""
        obstacles = []
        for instance in page.instances:
            bounds = instance.placed_shape_bounds()
            if bounds.valid:
                obstacles.append(("rect", (bounds.min_x, bounds.min_y, bounds.max_x, bounds.max_y)))
        for wire_node in children(page.root, "wire"):
            points = _node_points(wire_node)
            for start, end in zip(points, points[1:]):
                obstacles.append(("seg", (start, end)))
        return obstacles

    def page_svg(self, page):
        names, runs = page.connectivity()
        obstacles = self._page_obstacles(page)
        lines = [
            f'<g class="sch-page" data-page="{_escape(page.name or page.path.name)}" '
            f'transform="translate({page.offset[0]:.4f} {page.offset[1]:.4f})">'
        ]
        for wire_node in children(page.root, "wire"):
            lines.extend(self._wire_svg(wire_node, names, runs))
        for bus_node in children(page.root, "bus"):
            points = _node_points(bus_node)
            if len(points) >= 2:
                lines.append(
                    f'<path class="sch-wire" stroke-width="{DEFAULT_BUS_WIDTH:.4f}" d="{_polyline_path(points)}" />'
                )
        for node in children(page.root, "rectangle"):
            start = _node_point(node, "start")
            end = _node_point(node, "end")
            lines.append(
                f'<rect class="sch-note{_fill_class(node)}" stroke-width="{_stroke_width_of(node):.4f}" '
                f'x="{min(start[0], end[0]):.4f}" y="{min(start[1], end[1]):.4f}" '
                f'width="{abs(end[0] - start[0]):.4f}" height="{abs(end[1] - start[1]):.4f}" />'
            )
        for node in children(page.root, "polyline"):
            points = _node_points(node)
            if len(points) >= 2:
                lines.append(
                    f'<path class="sch-note{_fill_class(node)}" stroke-width="{_stroke_width_of(node):.4f}" '
                    f'd="{_polyline_path(points)}" />'
                )
        for node in children(page.root, "text_box"):
            at = child(node, "at")
            size = child(node, "size")
            if at is None or len(at) < 3 or size is None or len(size) < 3:
                continue
            x, y = as_float(at[1]), as_float(at[2])
            width, height = as_float(size[1]), as_float(size[2])
            text_value = str(node[1]) if len(node) > 1 else ""
            lines.append(
                f'<rect class="sch-note" stroke-width="0.2" x="{x:.4f}" y="{y:.4f}" '
                f'width="{width:.4f}" height="{height:.4f}" rx="0.3" />'
            )
            font_height = _font_height(node)
            horizontal, _ = _justify(node)
            for line_index, line in enumerate(_text_lines(text_value)):
                lines.append(
                    f'<text class="sch-note-text" x="{x + 0.6:.4f}" y="{y + font_height * 1.2 + line_index * font_height * LINE_HEIGHT_FACTOR:.4f}" '
                    f'font-size="{font_height:.4f}" text-anchor="{"start" if horizontal == "middle" else horizontal}">'
                    f'{_escape(line)}</text>'
                )
        for node in children(page.root, "text"):
            at = child(node, "at")
            if at is None or len(at) < 3:
                continue
            x, y = as_float(at[1]), as_float(at[2])
            angle = as_float(at[3]) if len(at) > 3 else 0.0
            horizontal, vertical = _justify(node)
            lines.append(
                f'<text class="sch-note-text" x="{x:.4f}" y="{y:.4f}" font-size="{_font_height(node):.4f}" '
                f'text-anchor="{horizontal}" dominant-baseline="{vertical}"{_rotate_attr(angle, x, y)}>'
                f'{_escape(str(node[1]) if len(node) > 1 else "")}</text>'
            )
        for node in children(page.root, "no_connect"):
            at = child(node, "at")
            if at is not None and len(at) >= 3:
                x, y = as_float(at[1]), as_float(at[2])
                radius = 0.6
                lines.append(
                    f'<path class="sch-no-connect" d="M{x - radius:.4f} {y - radius:.4f} '
                    f'L{x + radius:.4f} {y + radius:.4f} M{x - radius:.4f} {y + radius:.4f} '
                    f'L{x + radius:.4f} {y - radius:.4f}" />'
                )
        for node in children(page.root, "junction"):
            at = child(node, "at")
            if at is not None and len(at) >= 3:
                lines.append(
                    f'<circle class="sch-junction" cx="{as_float(at[1]):.4f}" cy="{as_float(at[2]):.4f}" '
                    f'r="{JUNCTION_RADIUS:.4f}" />'
                )
        for box in self.sheet_boxes:
            if box["page"] is page:
                lines.extend(self._sheet_box_svg(box))
        for instance in page.instances:
            lines.extend(self._symbol_svg(instance, names, runs, instance.label_layout(obstacles)))
        for node in children(page.root, "label"):
            lines.extend(self._label_svg(node, "label", names, runs))
        for node in children(page.root, "hierarchical_label"):
            lines.extend(self._label_svg(node, "hierarchical_label", names, runs))
        for node in children(page.root, "global_label"):
            lines.extend(self._label_svg(node, "global_label", names, runs))
        lines.append("</g>")
        return lines

    def combined_bounds(self, margin=3.0):
        combined = _Bounds()
        for page in self.pages:
            offset_x, offset_y = page.offset
            combined.add(page.bounds.min_x + offset_x, page.bounds.min_y + offset_y)
            combined.add(page.bounds.max_x + offset_x, page.bounds.max_y + offset_y)
        if not combined.valid:
            combined.add(0, 0)
            combined.add(100, 60)
        combined.add(combined.min_x - margin, combined.min_y - margin)
        combined.add(combined.max_x + margin, combined.max_y + margin)
        return combined

    def svg_document(self, title=""):
        margin = 2.0
        bounds = self.combined_bounds()
        min_x = bounds.min_x - margin
        min_y = bounds.min_y - margin
        width = bounds.max_x - bounds.min_x
        height = bounds.max_y - bounds.min_y
        lines = [
            '<?xml version="1.0" encoding="utf-8"?>',
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{min_x:.4f} {min_y:.4f} {width:.4f} {height:.4f}">',
            f"<style>{_SVG_EXTRA_STYLE}</style>",
            f'<rect class="sch-page" x="{min_x:.4f}" y="{min_y:.4f}" width="{width:.4f}" height="{height:.4f}" />',
        ]
        if title:
            lines.append(f"<title>{_escape(title)}</title>")
        for page in self.pages:
            lines.extend(self.page_svg(page))
        lines.append("</svg>")
        return "\n".join(lines) + "\n"

    def symbol_preview_svg(self, reference, margin=2.5):
        """Standalone SVG of every unit placed for one reference (detail pane)."""
        fragments = []
        bounds = _Bounds()
        for page in self.pages:
            page_conn = None
            for instance in page.instances:
                if instance.reference != reference:
                    continue
                if page_conn is None:
                    page_conn = page.connectivity()
                instance_bounds = instance.placed_graphics_bounds()
                if not instance_bounds.valid:
                    continue
                bounds = bounds.merged(instance_bounds)
                fragments.append(self._symbol_svg(instance, *page_conn))
        if not fragments or not bounds.valid:
            return ""
        min_x = bounds.min_x - margin
        min_y = bounds.min_y - margin
        width = bounds.max_x - bounds.min_x
        height = bounds.max_y - bounds.min_y
        lines = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{min_x:.4f} {min_y:.4f} {width:.4f} {height:.4f}">',
            f"<style>{_SVG_EXTRA_STYLE}</style>",
        ]
        for fragment in fragments:
            lines.extend(fragment)
        lines.append("</svg>")
        return "\n".join(lines) + "\n"


_MODEL_CACHE = {}


def load_model(project_directory, schematic_files):
    project_directory = Path(project_directory).resolve()
    key = (str(project_directory), tuple(schematic_files))
    model = _MODEL_CACHE.get(key)
    if model is None:
        if len(_MODEL_CACHE) > 8:
            _MODEL_CACHE.clear()
        model = SchematicModel(project_directory, schematic_files)
        _MODEL_CACHE[key] = model
    return model


def build_schematic_svg(project_directory, schematic_files, title=""):
    """Return {"svg", "width", "height", "symbol_count", "page_count"} for a project."""
    model = load_model(project_directory, schematic_files)
    return {
        "svg": model.svg_document(title=title),
        "symbol_count": sum(len(page.instances) for page in model.pages),
        "page_count": len(model.pages),
    }


def build_symbol_preview_svg(project_directory, schematic_files, reference):
    return load_model(project_directory, schematic_files).symbol_preview_svg(reference)
