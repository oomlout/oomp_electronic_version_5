import copy
import opsvg
import yaml
import os
from pathlib import Path
import svg_help
import svg_styles


def main(**kwargs):
    make_svg(**kwargs)

def make_svg(**kwargs):
    typ = svg_help.get_typ(**kwargs)
    oomp_mode = "project"
    #oomp_mode = "oobb"
    filt = kwargs.get("filter", "")
    build_variables = svg_help.get_build_variables(typ, filter=filt)
    if True:
        kwargs["filter"] = filt if filt != "" else build_variables["filter"]
        kwargs["save_type"] = build_variables["save_type"]
        kwargs["navigation"] = build_variables["navigation"]
        kwargs["overwrite"] = build_variables["overwrite"]
        kwargs["oomp_mode"] = oomp_mode
    parts = get_parts(kwargs, oomp_mode)

    kwargs["parts"] = parts

    svg_help.make_parts(**kwargs)

    if kwargs["navigation"]:
        oobb_style = False
        sort = svg_help.get_navigation_sort(oobb_style=oobb_style)
        svg_help.generate_navigation(sort=sort)


def get_parts(kwargs, oomp_mode):
    parts = []

    #load parts from parts/folder/working.yaml
    parts_directory = os.path.join(os.path.dirname(__file__), "parts")
    if not os.path.isdir(parts_directory):
        return parts

    for folder in os.listdir(parts_directory):
        folder_path = os.path.join(parts_directory, folder)
        if not os.path.isdir(folder_path):
            continue

        working_yaml_path = os.path.join(folder_path, "working.yaml")
        if not os.path.isfile(working_yaml_path):
            continue

        with open(working_yaml_path, "r", encoding="utf-8") as infile:
            loaded_part = yaml.safe_load(infile)

        if not isinstance(loaded_part, dict):
            continue

        # Apply the shared population definition to existing generated parts.
        # Future population runs write the same values into working.yaml.
        import working_oomp_populate_svg
        working_oomp_populate_svg.add_svg_details(loaded_part)

        svg_details_raw = loaded_part.get("svg_details")
        # Accept either a single dict or a list of dicts.
        if isinstance(svg_details_raw, list):
            # Use the first entry to derive kwargs / oobb_name; the full list
            # is kept intact in part["svg_details"] for make_svg_generic.
            svg_details = svg_details_raw[0] if svg_details_raw else {}
        elif isinstance(svg_details_raw, dict):
            svg_details = svg_details_raw
        else:
            continue  # no recognisable svg_details — skip

        part = loaded_part

        part_kwargs = copy.deepcopy(kwargs)
        part_kwargs.update(copy.deepcopy(loaded_part.get("kwargs", {})))
        _SD_META = {"svg_name", "filename_extra", "width", "height", "depth", "styles",
                    "extra", "radius_name"}
        svg_details_safe = {k: v for k, v in svg_details.items()
                            if k not in _SD_META or (k in ("width", "height", "depth") and isinstance(v, (int, float)))}
        part_kwargs.update(copy.deepcopy(svg_details_safe))

        # stylesheet name override from yaml: svg_details.stylesheet: "jazzy"
        if "stylesheet" in svg_details:
            part_kwargs["stylesheet"] = svg_details["stylesheet"]

        # per-part style overrides from yaml: svg_details.styles: {plate: {color: "#FF0000"}}
        yaml_styles = svg_details.get("styles", {})
        if isinstance(yaml_styles, dict) and yaml_styles:
            existing = part_kwargs.get("part_styles", {})
            part_kwargs["part_styles"] = svg_styles.merge(
                svg_styles.get_stylesheet(part_kwargs.get("stylesheet", "default")),
                {**existing, **yaml_styles}
            ) if not existing else {**existing, **yaml_styles}

        part["kwargs"] = part_kwargs
        part["oobb_name"] = part.get("oobb_name", svg_details.get("svg_name", "default"))

        if oomp_mode == "oobb":
            part["kwargs"]["oomp_size"] = part["oobb_name"]

        parts.append(part)

    return parts


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("depth", 3)
    rot = kwargs.get("rot", [0,0,0])
    pos = kwargs.get("pos", [0,0,0])
    extra = kwargs.get("extra", "")



    #add plate
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["shape"] = f"oobb_plate"
        p3["depth"] = depth
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        p3["pos"] = pos1
        opsvg.se(thing,**p3)

    #add holes
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["shape"] = f"oobb_holes"
        p3["depth"] = depth
        p3["radius_name"] = "m6"
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        p3["pos"] = pos1
        opsvg.se(thing,**p3)

    #add text
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["shape"] = f"text"
        p3["text"] = "Base Plate"
        p3["size"] = 10.0
        p3["font"] = "sans-serif"
        p3["halign"] = "left"
        p3["valign"] = "center"
        p3["color"] = "#000000"
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        p3["pos"] = pos1
        opsvg.se(thing,**p3)

    if prepare_print:
        svg_help.prepare_base_for_print(thing, pos, **kwargs)


def _use_style_oomp(thing, **kwargs):
    """Load the project-local OOMP stylesheet for component diagrams."""
    stylesheet = kwargs.get("stylesheet", "style_oomp")
    styles_directory = Path(__file__).parent / "styles"
    thing["styles"] = svg_styles.get_stylesheet(
        stylesheet,
        styles_dir=styles_directory,
    )

    part_styles = kwargs.get("part_styles", {})
    if isinstance(part_styles, dict) and part_styles:
        thing["styles"] = svg_styles.merge(thing["styles"], part_styles)


def _add_diagram_bounds(thing, width, height):
    """Add the white background and fixed bounds used by every diagram."""
    opsvg.se(
        thing,
        shape="rect",
        style="background",
        size=[width, height, 0],
        pos=[0, 0, 0],
    )


def _add_square_background(thing, size=64):
    """Add the white square required by the square PNG diagrams."""
    opsvg.se(
        thing,
        shape="rect",
        style="background",
        size=[size, size, 0],
        pos=[0, 0, 0],
    )


def _add_resistor_outline(
    thing,
    body_width=22,
    body_height=10,
    pos=None,
    body_style="component.body",
):
    """Draw the resistor body and its two surface-mount end terminals."""
    if pos is None:
        pos = [0, 0, 0]

    opsvg.se(
        thing,
        shape="rounded_rectangle",
        style=body_style,
        size=[body_width, body_height, 0],
        r=1.2,
        pos=copy.deepcopy(pos),
    )

    terminal_width = 3
    # Two explicit sides keep this easy to edit for other two-pin parts.
    sides = [-1, 1]
    for side in sides:
        terminal_pos = copy.deepcopy(pos)
        terminal_pos[0] += side * (body_width / 2 - terminal_width / 2)
        opsvg.se(
            thing,
            shape="rect",
            style="component.terminal",
            size=[terminal_width, body_height, 0],
            pos=terminal_pos,
        )

    return body_width, body_height


def _add_through_hole_resistor_outline(thing, width=32, height=9, pos=None):
    if pos is None:
        pos = [0, 0, 0]

    lead_lines = [
        [[-width / 2, 0], [-width / 2 + 6, 0]],
        [[width / 2 - 6, 0], [width / 2, 0]],
    ]
    for lead_line in lead_lines:
        opsvg.se(
            thing,
            shape="line",
            style="component.pin",
            p1=lead_line[0],
            p2=lead_line[1],
            pos=copy.deepcopy(pos),
        )

    opsvg.se(
        thing,
        shape="rounded_rectangle",
        style="component.body_warm",
        size=[width - 12, height, 0],
        r=height / 2,
        pos=copy.deepcopy(pos),
    )
    return width, height


def _add_led_outline(thing, width=22, height=12, pos=None):
    if pos is None:
        pos = [0, 0, 0]
    size = str(thing.get("taxonomy_3", ""))

    if size in ["3_mm", "5_mm", "10_mm"]:
        diameter = min(width - 8, height)
        lead_lines = [
            [[-diameter / 2, 0], [-width / 2, 0]],
            [[diameter / 2, 0], [width / 2, 0]],
        ]
        for lead_line in lead_lines:
            opsvg.se(
                thing,
                shape="line",
                style="component.pin",
                p1=lead_line[0],
                p2=lead_line[1],
                pos=copy.deepcopy(pos),
            )
        opsvg.se(
            thing,
            shape="circle",
            style="component.lens",
            r=diameter / 2,
            pos=copy.deepcopy(pos),
        )
        return width, diameter

    if size == "filament_3_volt":
        opsvg.se(
            thing,
            shape="rounded_rectangle",
            style="component.lens",
            size=[width, max(3, height / 3), 0],
            r=1.5,
            pos=copy.deepcopy(pos),
        )
        return width, max(3, height / 3)

    if size.startswith("strip_"):
        opsvg.se(
            thing,
            shape="rounded_rectangle",
            style="component.body",
            size=[width, height, 0],
            r=1,
            pos=copy.deepcopy(pos),
        )
        led_x_positions = [-width * 0.3, -width * 0.1, width * 0.1, width * 0.3]
        for led_x in led_x_positions:
            led_pos = copy.deepcopy(pos)
            led_pos[0] += led_x
            opsvg.se(
                thing,
                shape="circle",
                style="component.lens",
                r=min(2.1, height / 4),
                pos=led_pos,
            )
        return width, height

    _add_resistor_outline(
        thing,
        body_width=width,
        body_height=height,
        pos=pos,
    )
    opsvg.se(
        thing,
        shape="circle",
        style="component.lens",
        r=min(3.2, height / 3),
        pos=copy.deepcopy(pos),
    )
    polarity_pos = copy.deepcopy(pos)
    polarity_pos[0] -= width * 0.23
    opsvg.se(
        thing,
        shape="line",
        style="component.pin",
        p1=[0, -height * 0.3],
        p2=[0, height * 0.3],
        pos=polarity_pos,
    )
    return width, height


def _add_capacitor_outline(thing, width=22, height=10, pos=None):
    if pos is None:
        pos = [0, 0, 0]
    size = str(thing.get("taxonomy_3", ""))
    style = str(thing.get("taxonomy_4", ""))

    if "diameter" in size or style == "electrolytic":
        diameter = min(width, height)
        _add_resistor_outline(
            thing,
            body_width=diameter + 6,
            body_height=diameter,
            pos=pos,
            body_style="component.body_dark",
        )
        opsvg.se(
            thing,
            shape="circle",
            style="component.body_dark",
            r=diameter / 2,
            pos=copy.deepcopy(pos),
        )
        plus_pos = copy.deepcopy(pos)
        plus_pos[0] -= diameter * 0.18
        _add_text(thing, "+", "label", plus_pos, size=max(3, diameter / 3), color="#FFFFFF")
        return diameter + 6, diameter

    body_style = "component.body_warm"
    _add_resistor_outline(
        thing,
        body_width=width,
        body_height=height,
        pos=pos,
        body_style=body_style,
    )
    if style == "tantalum":
        stripe_pos = copy.deepcopy(pos)
        stripe_pos[0] -= width * 0.2
        opsvg.se(
            thing,
            shape="rect",
            style="component.pad",
            size=[1.5, height * 0.75, 0],
            pos=stripe_pos,
        )
    return width, height


def _add_crystal_outline(thing, width=24, height=14, pos=None):
    if pos is None:
        pos = [0, 0, 0]
    opsvg.se(
        thing,
        shape="rounded_rectangle",
        style="component.body",
        size=[width - 4, height - 4, 0],
        r=1.5,
        pos=copy.deepcopy(pos),
    )
    pad_positions = [
        [-width / 2 + 2, -height / 2 + 2],
        [-width / 2 + 2, height / 2 - 2],
        [width / 2 - 2, -height / 2 + 2],
        [width / 2 - 2, height / 2 - 2],
    ]
    for pad_position in pad_positions:
        pad_pos = copy.deepcopy(pos)
        pad_pos[0] += pad_position[0]
        pad_pos[1] += pad_position[1]
        opsvg.se(
            thing,
            shape="rect",
            style="component.pad",
            size=[4, 3, 0],
            pos=pad_pos,
        )
    return width, height


def _get_number_from_taxonomy(thing, taxonomy_names):
    for taxonomy_name in taxonomy_names:
        value = str(thing.get(taxonomy_name, ""))
        sections = value.split("_")
        for section in sections:
            if section.isdigit():
                return int(section)
    return 0


def _add_connector_outline(thing, width=30, height=16, pos=None):
    if pos is None:
        pos = [0, 0, 0]
    connector_type = str(thing.get("taxonomy_3", ""))
    pin_count = _get_number_from_taxonomy(thing, ["taxonomy_5", "taxonomy_6"])

    if connector_type == "header":
        pin_count = max(pin_count, 1)
        header_height = width
        header_width = min(8, max(4, height * 0.35))
        opsvg.se(
            thing,
            shape="rounded_rectangle",
            style="component.body_dark",
            size=[header_width, header_height, 0],
            r=1,
            pos=copy.deepcopy(pos),
        )
        pin_spacing = header_height / pin_count
        diagram_pin_positions = []
        for pin_index in range(pin_count):
            pin_pos = copy.deepcopy(pos)
            pin_pos[1] += header_height / 2 - pin_spacing / 2 - pin_index * pin_spacing
            opsvg.se(
                thing,
                shape="rect",
                style="component.hole",
                size=[min(1.8, pin_spacing * 0.5), min(1.8, pin_spacing * 0.5), 0],
                pos=pin_pos,
            )
            diagram_pin_positions.append(copy.deepcopy(pin_pos))
        thing["diagram_pin_positions"] = diagram_pin_positions
        thing["diagram_outline_width"] = header_width
        return header_width, header_height

    opsvg.se(
        thing,
        shape="rounded_rectangle",
        style="component.body",
        size=[width, height, 0],
        r=2,
        pos=copy.deepcopy(pos),
    )
    opening_width = width - 6
    opening_height = height - 6
    opsvg.se(
        thing,
        shape="rounded_rectangle",
        style="component.body_dark",
        size=[opening_width, opening_height, 0],
        r=1.5,
        pos=copy.deepcopy(pos),
    )
    visible_contacts = min(max(pin_count, 4), 16)
    contact_spacing = opening_width / (visible_contacts + 1)
    for contact_index in range(visible_contacts):
        contact_pos = copy.deepcopy(pos)
        contact_pos[0] += -opening_width / 2 + contact_spacing * (contact_index + 1)
        opsvg.se(
            thing,
            shape="line",
            style="component.terminal",
            p1=[0, -opening_height * 0.28],
            p2=[0, opening_height * 0.28],
            pos=contact_pos,
        )
    return width, height


def _get_package_pin_count(thing):
    pins = thing.get("pins", {})
    if isinstance(pins, dict) and len(pins) > 0:
        return len(pins)
    if isinstance(pins, list) and len(pins) > 0:
        return len(pins)

    component_type = thing.get("taxonomy_2", "")
    if component_type == "connector":
        pin_count = _get_number_from_taxonomy(thing, ["taxonomy_5", "taxonomy_6"])
        if pin_count > 0:
            return pin_count
    if component_type in ["diode", "ic"]:
        pin_count = _get_number_from_taxonomy(thing, ["taxonomy_3", "taxonomy_4"])
        if pin_count > 0:
            return pin_count

    defaults = {
        "capacitor": 2,
        "crystal": 4,
        "diode": 2,
        "display": 16,
        "ferrite_bead": 2,
        "led": 2,
        "resistor": 2,
        "wire": 2,
    }
    return defaults.get(component_type, 0)


def _add_ic_pin(thing, pin_number, side, pin_pos, pin_size):
    """Draw one outlined IC pin and retain its exact label position."""
    opsvg.se(
        thing,
        shape="rect",
        style="component.pad",
        size=pin_size,
        pos=copy.deepcopy(pin_pos),
    )
    thing["diagram_pin_positions"].append(
        {
            "number": str(pin_number),
            "side": side,
            "pos": copy.deepcopy(pin_pos),
            "size": copy.deepcopy(pin_size),
        }
    )


def _add_ic_pin_one_marker(thing, package, body_width, body_height, pos):
    """Use the same basic pin-1 cue shown by each source datasheet."""
    marker_x = pos[0] - body_width / 2 + 1.1
    marker_y = pos[1] + body_height / 2 - 1.1

    if package == "tsot_23_5":
        # Richtek uses a triangular corner mark beside pin 1.
        marker_x = pos[0] - body_width / 2 + 0.9
        marker_y = pos[1] - body_height / 2 + 0.9
        triangle_points = [
            [marker_x - 0.8, marker_y - 0.8],
            [marker_x - 0.8, marker_y + 0.8],
            [marker_x + 0.8, marker_y - 0.8],
        ]
        triangle_lines = [
            [triangle_points[0], triangle_points[1]],
            [triangle_points[1], triangle_points[2]],
            [triangle_points[2], triangle_points[0]],
        ]
        for triangle_line in triangle_lines:
            opsvg.se(
                thing,
                shape="line",
                style="component.pin_one_line",
                p1=triangle_line[0],
                p2=triangle_line[1],
                pos=[0, 0, 0],
            )
        return

    # WCH, CoreChips, and TI all use a circular pin-1 index cue.
    if package.startswith("qfn"):
        marker_y = pos[1] - body_height / 2 + 1.1
    opsvg.se(
        thing,
        shape="circle",
        style="component.pin_one",
        r=0.65,
        pos=[marker_x, marker_y, 0],
    )


def _add_ic_outline(thing, width=24, height=16, pos=None):
    """Draw the audited IC package orientation and physical pin numbering."""
    if pos is None:
        pos = [0, 0, 0]
    package = str(thing.get("taxonomy_3", ""))
    thing["diagram_pin_positions"] = []

    if package.startswith("qfn"):
        body_width = min(width - 2, height - 2)
        body_height = body_width
        pad_length = max(1.8, body_width * 0.18)
        pad_width = max(0.75, body_width * 0.09)
        edge_offset = body_width / 2
        offsets = []
        for pin_index in range(4):
            offsets.append(body_width * (-0.30 + pin_index * 0.20))

        pin_sides = [
            {"side": "left", "numbers": [13, 14, 15, 16]},
            {"side": "top", "numbers": [12, 11, 10, 9]},
            {"side": "right", "numbers": [8, 7, 6, 5]},
            {"side": "bottom", "numbers": [1, 2, 3, 4]},
        ]
        for pin_side in pin_sides:
            side = pin_side["side"]
            numbers = pin_side["numbers"]
            for pin_index in range(len(numbers)):
                if side == "left":
                    pin_pos = [pos[0] - edge_offset, pos[1] - offsets[pin_index], 0]
                    pin_size = [pad_length, pad_width, 0]
                elif side == "right":
                    pin_pos = [pos[0] + edge_offset, pos[1] - offsets[pin_index], 0]
                    pin_size = [pad_length, pad_width, 0]
                elif side == "top":
                    pin_pos = [pos[0] + offsets[pin_index], pos[1] + edge_offset, 0]
                    pin_size = [pad_width, pad_length, 0]
                else:
                    pin_pos = [pos[0] + offsets[pin_index], pos[1] - edge_offset, 0]
                    pin_size = [pad_width, pad_length, 0]
                _add_ic_pin(thing, numbers[pin_index], side, pin_pos, pin_size)

        opsvg.se(
            thing,
            shape="rounded_rectangle",
            style="component.body",
            size=[body_width, body_height, 0],
            r=0.7,
            pos=copy.deepcopy(pos),
        )
        # CH343P exposed pad 0 is GND.
        opsvg.se(
            thing,
            shape="rect",
            style="component.exposed_pad",
            size=[body_width * 0.44, body_height * 0.44, 0],
            pos=copy.deepcopy(pos),
        )
        thing["diagram_pin_positions"].append(
            {"number": "0", "side": "center", "pos": copy.deepcopy(pos), "size": [0, 0, 0]}
        )
        _add_ic_pin_one_marker(thing, package, body_width, body_height, pos)
        thing["diagram_outline_width"] = body_width + pad_length
        thing["diagram_outline_height"] = body_height + pad_length
        return body_width, body_height

    if package == "sop_16":
        body_height = max(8, height - 2)
        body_width = body_height * 3.9 / 9.9
        overall_width = body_height * 6.04 / 9.9
        pad_length = (overall_width - body_width) / 2 + 0.5
        pad_width = max(0.45, body_height * 0.406 / 9.9)
        left_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        right_numbers = [16, 15, 14, 13, 12, 11, 10, 9]
        for side_index in range(2):
            side = ["left", "right"][side_index]
            numbers = [left_numbers, right_numbers][side_index]
            side_sign = [-1, 1][side_index]
            for pin_index in range(8):
                pin_y = pos[1] + body_height * (0.4375 - pin_index * 0.125)
                pin_x = pos[0] + side_sign * (body_width / 2 + pad_length / 2 - 0.25)
                _add_ic_pin(thing, numbers[pin_index], side, [pin_x, pin_y, 0], [pad_length, pad_width, 0])

    elif package == "sot_23_6":
        body_height = max(8, height - 2)
        body_width = body_height * 1.6 / 2.9
        overall_width = body_height * 2.8 / 2.9
        pad_length = (overall_width - body_width) / 2 + 0.5
        pad_width = body_height * 0.375 / 2.9
        left_numbers = [1, 2, 3]
        right_numbers = [6, 5, 4]
        for side_index in range(2):
            side = ["left", "right"][side_index]
            numbers = [left_numbers, right_numbers][side_index]
            side_sign = [-1, 1][side_index]
            for pin_index in range(3):
                pin_y = pos[1] + body_height * (0.3275 - pin_index * 0.3275)
                pin_x = pos[0] + side_sign * (body_width / 2 + pad_length / 2 - 0.25)
                _add_ic_pin(thing, numbers[pin_index], side, [pin_x, pin_y, 0], [pad_length, pad_width, 0])

    elif package == "tsot_23_5":
        overall_height = max(9, height - 2)
        body_height = overall_height * 1.6 / 2.7955
        body_width = body_height * 2.8955 / 1.6
        pad_length = (overall_height - body_height) / 2 + 0.5
        pad_width = body_width * 0.4295 / 2.8955
        bottom_numbers = [1, 2, 3]
        top_numbers = [5, 4]
        for pin_index in range(3):
            pin_x = pos[0] + body_width * (-0.3275 + pin_index * 0.3275)
            pin_y = pos[1] - body_height / 2 - pad_length / 2 + 0.25
            _add_ic_pin(thing, bottom_numbers[pin_index], "bottom", [pin_x, pin_y, 0], [pad_width, pad_length, 0])
        for pin_index in range(2):
            pin_x = pos[0] + body_width * [-0.3275, 0.3275][pin_index]
            pin_y = pos[1] + body_height / 2 + pad_length / 2 - 0.25
            _add_ic_pin(thing, top_numbers[pin_index], "top", [pin_x, pin_y, 0], [pad_width, pad_length, 0])

    else:
        body_width = width - 8
        body_height = height
        pin_count = max(_get_package_pin_count(thing), 2)
        left_pin_count = (pin_count + 1) // 2
        right_pin_count = pin_count // 2
        for side_index in range(2):
            side = ["left", "right"][side_index]
            side_sign = [-1, 1][side_index]
            side_count = [left_pin_count, right_pin_count][side_index]
            for pin_index in range(side_count):
                pin_number = pin_index + 1
                if side == "right":
                    pin_number = pin_count - pin_index
                pin_y = pos[1] + body_height * (0.5 - (pin_index + 0.5) / side_count)
                pin_x = pos[0] + side_sign * (body_width / 2 + 1.5)
                _add_ic_pin(thing, pin_number, side, [pin_x, pin_y, 0], [3.5, 1.2, 0])

    opsvg.se(
        thing,
        shape="rounded_rectangle",
        style="component.body",
        size=[body_width, body_height, 0],
        r=0.8,
        pos=copy.deepcopy(pos),
    )
    _add_ic_pin_one_marker(thing, package, body_width, body_height, pos)
    thing["diagram_outline_width"] = body_width + 2 * max(0, (thing["diagram_pin_positions"][0]["size"][0] - 0.5))
    thing["diagram_outline_height"] = body_height
    if package == "tsot_23_5":
        thing["diagram_outline_width"] = body_width
        thing["diagram_outline_height"] = body_height + 2 * pad_length
    return body_width, body_height


def _add_display_outline(thing, width=30, height=16, pos=None):
    if pos is None:
        pos = [0, 0, 0]
    opsvg.se(thing, shape="rounded_rectangle", style="component.body", size=[width, height, 0], r=1.5, pos=copy.deepcopy(pos))
    opsvg.se(thing, shape="rounded_rectangle", style="component.screen", size=[width - 6, height - 6, 0], r=1, pos=copy.deepcopy(pos))
    return width, height


def _add_breadboard_outline(thing, width=32, height=16, pos=None):
    if pos is None:
        pos = [0, 0, 0]
    opsvg.se(thing, shape="rounded_rectangle", style="component.body", size=[width, height, 0], r=1.5, pos=copy.deepcopy(pos))
    columns = 12
    rows = 4
    for column in range(columns):
        for row in range(rows):
            hole_pos = copy.deepcopy(pos)
            hole_pos[0] += -width * 0.42 + column * width * 0.84 / (columns - 1)
            hole_pos[1] += -height * 0.3 + row * height * 0.6 / (rows - 1)
            opsvg.se(thing, shape="circle", style="component.hole", r=0.45, pos=hole_pos)
    return width, height


def _add_wire_outline(thing, width=32, height=10, pos=None):
    if pos is None:
        pos = [0, 0, 0]
    wire_points = [
        [-width / 2 + 3, 0],
        [-width / 6, height / 4],
        [width / 6, -height / 4],
        [width / 2 - 3, 0],
    ]
    for index in range(len(wire_points) - 1):
        opsvg.se(
            thing,
            shape="line",
            style="component.pin",
            p1=wire_points[index],
            p2=wire_points[index + 1],
            pos=copy.deepcopy(pos),
        )
    for side in [-1, 1]:
        end_pos = copy.deepcopy(pos)
        end_pos[0] += side * (width / 2 - 1.5)
        opsvg.se(thing, shape="circle", style="component.pad", r=1.5, pos=end_pos)
    return width, height


def _add_component_outline(thing, width=22, height=10, pos=None):
    """Dispatch to a simple physical outline for each populated component type."""
    component_type = str(thing.get("taxonomy_2", ""))
    size = str(thing.get("taxonomy_3", ""))

    if component_type == "resistor":
        if size == "quarter_watt_through_hole":
            return _add_through_hole_resistor_outline(thing, width=width, height=height, pos=pos)
        return _add_resistor_outline(thing, body_width=width, body_height=height, pos=pos)
    if component_type == "capacitor":
        return _add_capacitor_outline(thing, width=width, height=height, pos=pos)
    if component_type == "led":
        return _add_led_outline(thing, width=width, height=height, pos=pos)
    if component_type == "crystal":
        return _add_crystal_outline(thing, width=width, height=height, pos=pos)
    if component_type == "ferrite_bead":
        return _add_resistor_outline(thing, body_width=width, body_height=height, pos=pos, body_style="component.body_dark")
    if component_type == "connector":
        return _add_connector_outline(thing, width=width, height=height, pos=pos)
    if component_type in ["diode", "ic"]:
        return _add_ic_outline(thing, width=width, height=height, pos=pos)
    if component_type == "display":
        return _add_display_outline(thing, width=width, height=height, pos=pos)
    if component_type == "prototyping":
        return _add_breadboard_outline(thing, width=width, height=height, pos=pos)
    if component_type == "wire":
        return _add_wire_outline(thing, width=width, height=height, pos=pos)

    opsvg.se(thing, shape="rounded_rectangle", style="component.body", size=[width, height, 0], r=1, pos=pos or [0, 0, 0])
    return width, height


def _add_text(thing, text, style, pos, size=None, **kwargs):
    text_details = {
        "shape": "text",
        "style": style,
        "text": str(text),
        "pos": copy.deepcopy(pos),
    }
    if size is not None:
        text_details["size"] = size
    text_details.update(kwargs)
    opsvg.se(thing, **text_details)


def _get_bip_39_words(thing):
    words = thing.get("bip_39_3_word_array", [])
    if not isinstance(words, list) or len(words) == 0:
        words = str(thing.get("bip_39_3_word_space", "")).split()

    words_three = []
    for index in range(3):
        if index < len(words):
            words_three.append(str(words[index]))
        else:
            words_three.append("")
    return words_three


def _get_pin_labels(thing):
    pins = thing.get("pins", [])
    labels = []
    used_pin_keys = []

    if isinstance(pins, dict):
        # Numeric traversal keeps pin order predictable and easy to inspect.
        for pin_number in range(0, 100):
            pin_key = f"pin_{pin_number}"
            if pin_key in pins:
                pin = pins[pin_key]
                pin_name = str(pin.get("name", "")).strip()
                if pin_name == "":
                    pin_name = f"pin {pin.get('number', pin_number)}"
                labels.append(pin_name)
                used_pin_keys.append(pin_key)

        for pin_key in pins:
            if pin_key not in used_pin_keys:
                pin = pins[pin_key]
                pin_number = str(pin.get("number", len(labels) + 1))
                pin_name = str(pin.get("name", "")).strip()
                labels.append(pin_name if pin_name != "" else f"pin {pin_number}")

    if isinstance(pins, list):
        for index in range(len(pins)):
            pin = pins[index]
            if isinstance(pin, dict):
                pin_number = str(pin.get("number", index + 1))
                pin_name = str(pin.get("name", "")).strip()
                labels.append(pin_name if pin_name != "" else f"pin {pin_number}")

    pin_count = _get_package_pin_count(thing)
    while len(labels) < pin_count:
        labels.append(f"pin {len(labels) + 1}")

    return labels


def _get_pin_label_map(thing):
    """Return pin names by their explicit datasheet pin number."""
    pin_label_map = {}
    pins = thing.get("pins", {})
    if isinstance(pins, dict):
        for pin_key in pins:
            pin = pins[pin_key]
            pin_number = str(pin.get("number", pin_key.replace("pin_", "")))
            pin_name = str(pin.get("name", "")).strip()
            if pin_name == "":
                pin_name = f"pin {pin_number}"
            pin_label_map[pin_number] = pin_name
    if isinstance(pins, list):
        for pin_index in range(len(pins)):
            pin = pins[pin_index]
            if isinstance(pin, dict):
                pin_number = str(pin.get("number", pin_index + 1))
                pin_name = str(pin.get("name", "")).strip()
                if pin_name == "":
                    pin_name = f"pin {pin_number}"
                pin_label_map[pin_number] = pin_name
    return pin_label_map


def _get_component_text_color(thing):
    # style_oomp is intentionally monochrome: white parts, black outlines/text.
    return "#000000"


def _add_square_pin_labels(thing):
    pin_labels = _get_pin_labels(thing)
    if len(pin_labels) == 0:
        return

    component_type = str(thing.get("taxonomy_2", ""))
    component_size = str(thing.get("taxonomy_3", ""))
    diagram_pin_positions = thing.get("diagram_pin_positions", [])
    if component_type == "connector" and component_size == "header" and diagram_pin_positions:
        label_size = min(2.2, max(0.7, 16.0 / len(pin_labels)))
        label_x = float(thing.get("diagram_outline_width", 4)) / 2 + 2
        for index in range(min(len(pin_labels), len(diagram_pin_positions))):
            pin_position = diagram_pin_positions[index]
            _add_text(
                thing,
                pin_labels[index],
                "label.pin",
                [label_x, pin_position[1], 0],
                size=label_size,
                halign="left",
            )
        return

    if component_type == "ic" and diagram_pin_positions:
        pin_label_map = _get_pin_label_map(thing)

        # SOP16 has eight pins on each long edge.  Directly adjacent text would
        # overlap, so keep its two readable banks as the requested exception.
        if component_size == "sop_16":
            side_details = [
                {"side": "left", "x": -12.5, "halign": "right"},
                {"side": "right", "x": 12.5, "halign": "left"},
            ]
            for side_detail in side_details:
                side_records = []
                for pin_record in diagram_pin_positions:
                    if pin_record.get("side", "") == side_detail["side"]:
                        side_records.append(pin_record)
                for pin_index in range(len(side_records)):
                    pin_record = side_records[pin_index]
                    pin_number = pin_record.get("number", "")
                    pin_name = pin_label_map.get(pin_number, f"pin {pin_number}")
                    label_y = 12 - pin_index * 18 / max(1, len(side_records) - 1)
                    _add_text(
                        thing,
                        pin_name,
                        "label.pin",
                        [side_detail["x"], label_y, 0],
                        size=1.8,
                        halign=side_detail["halign"],
                    )
            return

        # All other audited packages keep every title directly beside its pin.
        for pin_record in diagram_pin_positions:
            pin_number = pin_record.get("number", "")
            pin_name = pin_label_map.get(pin_number, f"pin {pin_number}")
            side = pin_record.get("side", "")
            pin_pos = pin_record.get("pos", [0, 0, 0])
            pin_size = pin_record.get("size", [0, 0, 0])
            label_size = 2.2
            if component_size.startswith("qfn"):
                label_size = 1.45
            if component_size == "tsot_23_5":
                label_size = 1.9

            if side == "left":
                label_pos = [pin_pos[0] - pin_size[0] / 2 - 0.6, pin_pos[1], 0]
                _add_text(thing, pin_name, "label.pin", label_pos, size=label_size, halign="right")
            elif side == "right":
                label_pos = [pin_pos[0] + pin_size[0] / 2 + 0.6, pin_pos[1], 0]
                _add_text(thing, pin_name, "label.pin", label_pos, size=label_size, halign="left")
            elif side == "top":
                label_pos = [pin_pos[0], pin_pos[1] + pin_size[1] / 2 + 0.7, 0]
                _add_text(
                    thing,
                    pin_name,
                    "label.pin",
                    label_pos,
                    size=label_size,
                    halign="left",
                    rot=[0, 0, 90],
                )
            elif side == "bottom":
                label_pos = [pin_pos[0], pin_pos[1] - pin_size[1] / 2 - 0.7, 0]
                _add_text(
                    thing,
                    pin_name,
                    "label.pin",
                    label_pos,
                    size=label_size,
                    halign="right",
                    rot=[0, 0, 90],
                )
            elif side == "center":
                _add_text(
                    thing,
                    pin_name,
                    "label.pin",
                    [pin_pos[0], pin_pos[1], 0],
                    size=label_size,
                )
        return

    left_labels = []
    right_labels = []
    for index in range(len(pin_labels)):
        if index < (len(pin_labels) + 1) // 2:
            left_labels.append(pin_labels[index])
        else:
            right_labels.append(pin_labels[index])

    maximum_side_count = max(len(left_labels), len(right_labels))
    label_size = 2.8
    if maximum_side_count > 8:
        label_size = max(0.9, 18.0 / maximum_side_count)

    side_details = [
        {"labels": left_labels, "x": -13, "halign": "right"},
        {"labels": right_labels, "x": 13, "halign": "left"},
    ]
    for side_detail in side_details:
        labels = side_detail["labels"]
        if len(labels) == 1:
            y_positions = [3]
        else:
            y_positions = []
            for index in range(len(labels)):
                y_positions.append(12 - index * 18 / (len(labels) - 1))

        for index in range(len(labels)):
            _add_text(
                thing,
                labels[index],
                "label.pin",
                [side_detail["x"], y_positions[index], 0],
                size=label_size,
                halign=side_detail["halign"],
            )


def _get_name_lines(thing, maximum_characters=29):
    """Split a long part name into short, manually predictable lines."""
    display_name = thing.get("name_short", "")
    if display_name == "":
        display_name = thing.get("name", thing.get("id", "component"))
    words = str(display_name).split()
    lines = []
    current_line = ""

    for word in words:
        proposed_line = word if current_line == "" else f"{current_line} {word}"
        if len(proposed_line) <= maximum_characters:
            current_line = proposed_line
        else:
            if current_line != "":
                lines.append(current_line)
            current_line = word

    if current_line != "":
        lines.append(current_line)

    return lines[:3]


def _add_square_name(thing):
    name_lines = _get_name_lines(thing)
    y_positions = [27, 23, 19]
    for index in range(len(name_lines)):
        _add_text(
            thing,
            name_lines[index],
            "label.name",
            [0, y_positions[index], 0],
        )


def _add_square_codes(thing):
    md5_6_alpha_upper = thing.get("md5_6_alpha_upper", "")
    if md5_6_alpha_upper == "":
        md5_6_alpha_upper = str(thing.get("md5_6_alpha", "")).upper()
    words = _get_bip_39_words(thing)
    bip_39_3_word = " ".join(words)
    _add_text(thing, md5_6_alpha_upper, "label.summary_code", [0, -14, 0])
    _add_text(thing, bip_39_3_word, "label.summary_words", [0, -21, 0])


def _format_dimension_mm(value):
    if isinstance(value, (int, float)):
        return f"{value:g} mm"
    return f"{value} mm"


def _format_dimension_range_mm(minimum, maximum, nominal):
    if minimum is not None and maximum is not None:
        if minimum == maximum:
            return _format_dimension_mm(minimum)
        return f"{minimum:g}-{maximum:g} mm"
    return _format_dimension_mm(nominal)


def _add_dimension_line(thing, p1, p2):
    opsvg.se(
        thing,
        shape="line",
        style="dimension.line",
        p1=copy.deepcopy(p1),
        p2=copy.deepcopy(p2),
        pos=[0, 0, 0],
    )


def _add_horizontal_dimension(thing, x1, x2, y, text, text_y=None):
    if text_y is None:
        text_y = y - 3.5
    dimension_lines = [
        [[x1, y], [x2, y]],
        [[x1 - 0.8, y - 0.8], [x1 + 0.8, y + 0.8]],
        [[x2 - 0.8, y - 0.8], [x2 + 0.8, y + 0.8]],
    ]
    for dimension_line in dimension_lines:
        _add_dimension_line(thing, dimension_line[0], dimension_line[1])
    _add_text(thing, text, "label.dimension", [(x1 + x2) / 2, text_y, 0], size=2.5)


def _add_vertical_dimension(thing, x, y1, y2, text, text_x=None):
    if text_x is None:
        text_x = x - 3.5
    dimension_lines = [
        [[x, y1], [x, y2]],
        [[x - 0.8, y1 - 0.8], [x + 0.8, y1 + 0.8]],
        [[x - 0.8, y2 - 0.8], [x + 0.8, y2 + 0.8]],
    ]
    for dimension_line in dimension_lines:
        _add_dimension_line(thing, dimension_line[0], dimension_line[1])
    _add_text(
        thing,
        text,
        "label.dimension",
        [text_x, (y1 + y2) / 2, 0],
        size=2.5,
        rot=[0, 0, 90],
    )


def _get_dimension_label(title, value, show_titles):
    value_text = _format_dimension_mm(value)
    if show_titles:
        return f"{title} {value_text}"
    return value_text


def _add_header_dimensions(thing, show_titles=False):
    """Dimension the vertical header in top and side views."""
    dimensions = thing.get("header_dimensions_mm", {})
    plastic_length = dimensions.get("plastic_length", 25.4)
    plastic_width = dimensions.get("plastic_width", 2.48)
    plastic_height = dimensions.get("plastic_height", 2.54)
    pin_pitch = dimensions.get("pin_pitch", 2.54)
    pin_square = dimensions.get("pin_square", 0.64)
    pin_length_total = dimensions.get("pin_length_total", 10.92)
    pin_length_post = dimensions.get("pin_length_post", 5.84)
    pin_length_tail = dimensions.get("pin_length_tail", 2.54)

    opsvg.se(
        thing,
        shape="rect",
        style="background",
        size=[82, 72, 0],
        pos=[0, 0, 0],
    )

    # Top view: black plastic body and all pins, oriented vertically.
    top_view_pos = [-15, 2, 0]
    top_view_width, top_view_height = _add_connector_outline(
        thing,
        width=36,
        height=14,
        pos=top_view_pos,
    )
    top_view_left = top_view_pos[0] - top_view_width / 2
    top_view_right = top_view_pos[0] + top_view_width / 2
    top_view_bottom = top_view_pos[1] - top_view_height / 2
    top_view_top = top_view_pos[1] + top_view_height / 2

    _add_dimension_line(thing, [top_view_left, top_view_bottom], [-24, top_view_bottom])
    _add_dimension_line(thing, [top_view_left, top_view_top], [-24, top_view_top])
    _add_vertical_dimension(
        thing,
        -24,
        top_view_bottom,
        top_view_top,
        _get_dimension_label("plastic length", plastic_length, show_titles),
        text_x=-28,
    )

    _add_dimension_line(thing, [top_view_left, top_view_bottom], [top_view_left, -21])
    _add_dimension_line(thing, [top_view_right, top_view_bottom], [top_view_right, -21])
    _add_horizontal_dimension(
        thing,
        top_view_left,
        top_view_right,
        -21,
        _get_dimension_label("plastic width", plastic_width, show_titles),
        text_y=-25,
    )

    pin_positions = thing.get("diagram_pin_positions", [])
    if len(pin_positions) >= 2:
        pitch_x = top_view_right + 5
        first_pin_y = pin_positions[0][1]
        second_pin_y = pin_positions[1][1]
        _add_dimension_line(thing, [top_view_right, first_pin_y], [pitch_x, first_pin_y])
        _add_dimension_line(thing, [top_view_right, second_pin_y], [pitch_x, second_pin_y])
        _add_vertical_dimension(
            thing,
            pitch_x,
            second_pin_y,
            first_pin_y,
            _get_dimension_label("pitch", pin_pitch, show_titles),
            text_x=pitch_x + 3,
        )

    # Enlarged square pin detail.
    pin_detail_pos = [12, 21, 0]
    opsvg.se(
        thing,
        shape="rect",
        style="component.pad",
        size=[5, 5, 0],
        pos=pin_detail_pos,
    )
    _add_horizontal_dimension(
        thing,
        pin_detail_pos[0] - 2.5,
        pin_detail_pos[0] + 2.5,
        16.5,
        _get_dimension_label("pin square", pin_square, show_titles),
        text_y=13,
    )

    # Side view: full pin, plastic body, post, and PCB tail.
    side_view_x = 20
    side_bottom = -24
    side_top = 8
    side_scale = (side_top - side_bottom) / pin_length_total
    tail_height = pin_length_tail * side_scale
    plastic_body_height = plastic_height * side_scale
    plastic_bottom = side_bottom + tail_height
    plastic_top = plastic_bottom + plastic_body_height
    plastic_center = (plastic_bottom + plastic_top) / 2

    opsvg.se(
        thing,
        shape="rect",
        style="component.pad",
        size=[1.8, side_top - side_bottom, 0],
        pos=[side_view_x, (side_top + side_bottom) / 2, 0],
    )
    opsvg.se(
        thing,
        shape="rect",
        style="component.body_dark",
        size=[12, plastic_body_height, 0],
        pos=[side_view_x, plastic_center, 0],
    )

    _add_vertical_dimension(
        thing,
        31,
        side_bottom,
        side_top,
        _get_dimension_label("pin total", pin_length_total, show_titles),
        text_x=35,
    )
    _add_vertical_dimension(
        thing,
        11,
        plastic_top,
        side_top,
        _get_dimension_label("post", pin_length_post, show_titles),
        text_x=8,
    )
    _add_vertical_dimension(
        thing,
        11,
        side_bottom,
        plastic_bottom,
        _get_dimension_label("tail", pin_length_tail, show_titles),
        text_x=8,
    )
    _add_text(
        thing,
        _get_dimension_label("plastic height", plastic_height, show_titles),
        "label.dimension",
        [side_view_x, -30, 0],
        size=2.3,
    )


def _add_component_dimensions(thing, body_width, body_height, show_titles=False):
    """Draw editable horizontal and vertical dimensions around a component."""
    body_left = -body_width / 2
    body_right = body_width / 2
    body_top = body_height / 2
    body_bottom = -body_height / 2

    horizontal_dimension_y = -body_height / 2 - 6
    vertical_dimension_x = body_width / 2 + 6

    # Extension lines, dimension lines, and diagonal end ticks.
    dimension_lines = [
        [[body_left, body_bottom], [body_left, horizontal_dimension_y - 1]],
        [[body_right, body_bottom], [body_right, horizontal_dimension_y - 1]],
        [[body_left, horizontal_dimension_y], [body_right, horizontal_dimension_y]],
        [[body_left - 1, horizontal_dimension_y - 1], [body_left + 1, horizontal_dimension_y + 1]],
        [[body_right - 1, horizontal_dimension_y - 1], [body_right + 1, horizontal_dimension_y + 1]],
        [[body_right, body_bottom], [vertical_dimension_x + 1, body_bottom]],
        [[body_right, body_top], [vertical_dimension_x + 1, body_top]],
        [[vertical_dimension_x, body_bottom], [vertical_dimension_x, body_top]],
        [[vertical_dimension_x - 1, body_bottom - 1], [vertical_dimension_x + 1, body_bottom + 1]],
        [[vertical_dimension_x - 1, body_top - 1], [vertical_dimension_x + 1, body_top + 1]],
    ]
    for dimension_line in dimension_lines:
        _add_dimension_line(thing, dimension_line[0], dimension_line[1])

    dimensions_mm = thing.get("dimensions_mm", {})
    length_text = _format_dimension_mm(dimensions_mm.get("length", 1.6))
    width_text = _format_dimension_mm(dimensions_mm.get("width", 0.8))

    component_type = thing.get("taxonomy_2", "")
    package = thing.get("taxonomy_3", "")
    if component_type == "ic":
        ic_dimensions = thing.get("ic_dimensions_mm", {})
        length_text = _format_dimension_range_mm(
            ic_dimensions.get("body_length_min"),
            ic_dimensions.get("body_length_max"),
            ic_dimensions.get("body_length", dimensions_mm.get("length", 1.6)),
        )
        width_text = _format_dimension_range_mm(
            ic_dimensions.get("body_width_min"),
            ic_dimensions.get("body_width_max"),
            ic_dimensions.get("body_width", dimensions_mm.get("width", 0.8)),
        )

        # SOP and TI SOT are displayed in the datasheet's portrait top view.
        if package in ["sop_16", "sot_23_6"]:
            length_text, width_text = width_text, length_text
    if show_titles:
        if component_type == "ic" and package in ["sop_16", "sot_23_6"]:
            length_text = f"body width {length_text}"
            width_text = f"body length {width_text}"
        elif component_type == "ic":
            length_text = f"body length {length_text}"
            width_text = f"body width {width_text}"
        else:
            length_text = f"length {length_text}"
            width_text = f"width {width_text}"

    dimension_text_size = None
    if component_type == "ic":
        dimension_text_size = 2.3

    _add_text(
        thing,
        length_text,
        "label.dimension",
        [0, horizontal_dimension_y - 4.5, 0],
        size=dimension_text_size,
    )
    _add_text(
        thing,
        width_text,
        "label.dimension",
        [vertical_dimension_x + 5, 0, 0],
        size=dimension_text_size,
        rot=[0, 0, 90],
    )


def get_oomp_component_outline(thing, **kwargs):
    _use_style_oomp(thing, **kwargs)
    _add_diagram_bounds(thing, 34, 20)
    _add_component_outline(thing, width=30, height=16)


def get_oomp_component_part_id(thing, **kwargs):
    _use_style_oomp(thing, **kwargs)
    _add_diagram_bounds(thing, 34, 20)
    _add_component_outline(thing, width=30, height=16)

    part_id = str(thing.get("part_id", "R1"))
    part_id_size = 6.0
    if len(part_id) > 3:
        part_id_size = max(2.4, 18.0 / len(part_id))
    _add_text(
        thing,
        part_id,
        "label.part_id",
        [0, 0, 0],
        size=part_id_size,
        color=_get_component_text_color(thing),
    )


def get_oomp_component_md5_6_alpha(thing, **kwargs):
    _use_style_oomp(thing, **kwargs)
    _add_diagram_bounds(thing, 34, 20)
    _add_component_outline(thing, width=30, height=16)
    _add_text(
        thing,
        thing.get(
            "md5_6_alpha_upper",
            str(thing.get("md5_6_alpha", "")).upper(),
        ),
        "label.code",
        [0, 0, 0],
        color=_get_component_text_color(thing),
    )


def get_oomp_component_bip_39_3_word(thing, **kwargs):
    _use_style_oomp(thing, **kwargs)
    _add_diagram_bounds(thing, 38, 24)
    _add_component_outline(thing, width=34, height=20)

    words = _get_bip_39_words(thing)
    word_y_positions = [5, 0, -5]
    for index in range(3):
        _add_text(
            thing,
            words[index],
            "label.word",
            [0, word_y_positions[index], 0],
            color=_get_component_text_color(thing),
        )


def get_oomp_component_square(thing, **kwargs):
    _use_style_oomp(thing, **kwargs)
    _add_square_background(thing)
    _add_square_name(thing)
    _add_component_outline(
        thing,
        width=22,
        height=10,
        pos=[0, 3, 0],
    )
    _add_square_codes(thing)


def get_oomp_component_square_pins(thing, **kwargs):
    _use_style_oomp(thing, **kwargs)
    _add_square_background(thing)
    _add_square_name(thing)
    component_width = 18
    component_height = 9
    if thing.get("taxonomy_2", "") == "connector" and thing.get("taxonomy_3", "") == "header":
        component_width = 22
        component_height = 10
    if thing.get("taxonomy_2", "") == "ic":
        package = thing.get("taxonomy_3", "")
        package_sizes = {
            "qfn_16_3_mm_x_3_mm": [16, 14],
            "sop_16": [18, 18],
            "sot_23_6": [18, 16],
            "tsot_23_5": [20, 16],
        }
        if package in package_sizes:
            component_width = package_sizes[package][0]
            component_height = package_sizes[package][1]
    _add_component_outline(
        thing,
        width=component_width,
        height=component_height,
        pos=[0, 3, 0],
    )

    _add_square_pin_labels(thing)

    _add_square_codes(thing)


def get_oomp_component_dimensioned(thing, **kwargs):
    _use_style_oomp(thing, **kwargs)
    if thing.get("taxonomy_2", "") == "connector" and thing.get("taxonomy_3", "") == "header":
        _add_header_dimensions(thing, show_titles=False)
        return
    if thing.get("taxonomy_2", "") == "ic":
        _add_diagram_bounds(thing, 72, 58)
    else:
        _add_diagram_bounds(thing, 58, 44)
    body_width, body_height = _add_component_outline(thing, width=32, height=16)
    _add_component_dimensions(thing, body_width, body_height, show_titles=False)


def get_oomp_component_dimensioned_titles(thing, **kwargs):
    _use_style_oomp(thing, **kwargs)
    if thing.get("taxonomy_2", "") == "connector" and thing.get("taxonomy_3", "") == "header":
        _add_header_dimensions(thing, show_titles=True)
        return
    if thing.get("taxonomy_2", "") == "ic":
        _add_diagram_bounds(thing, 72, 58)
    else:
        _add_diagram_bounds(thing, 58, 44)
    body_width, body_height = _add_component_outline(thing, width=32, height=16)
    _add_component_dimensions(thing, body_width, body_height, show_titles=True)


def get_fill_in_the_blanks(thing, **kwargs):
    svg_help.get_fill_in_the_blanks(thing, **kwargs)


def get_a4_sheet(thing, **kwargs):
    svg_help.get_a4_sheet(thing, **kwargs)


def get_label_76x50(thing, **kwargs):
    svg_help.get_label_76x50(thing, **kwargs)


def _default_label_boxes():
    """Default 3 × 4 grid matching the Project Bolt tin insert photo.

    Top row is 0.5 units tall (narrow label strip);
    the three lower rows are each 1.0 units tall.
    Total: 3 wide × 3.5 high = 12 boxes.
    """
    boxes = []
    n = 1
    layout = [
        (0.0, 0.5),   # top narrow row
        (0.5, 1.0),
        (1.5, 1.0),
        (2.5, 1.0),
    ]
    for (row_y, row_h) in layout:
        for col in range(3):
            boxes.append({
                "x": float(col),
                "y": row_y,
                "w": 1.0,
                "h": row_h,
                "name": f"box_{n}",
            })
            n += 1
    return boxes


def get_internal_label_sheet(thing, **kwargs):
    """Proportional grid label sheet for tin inserts.

    No dark background — boxes sit directly on the card, separated by the
    card's own fill showing through the gap.  Corner radii are computed per
    corner so junctions and card edges look geometrically correct:

      r_inner  = gap_mm / 2   — inner corners: arc exactly fills the gap void
      r_outer  = card_r - card_margin_mm  — outer corners: parallel to card edge

    Parameters
    ----------
    unit_mm        : float  — physical size of one grid unit in mm   (default 42.0)
    grid_w         : float  — grid width in units                    (default 3.0)
    grid_h         : float  — grid height in units                   (default 3.5)
    card_margin_mm : float  — card fill visible around the grid      (default 2.0)
                              unit_mm=42, grid_w=3, margin=2 → card_w=130 mm
    card_r         : float  — card corner radius in mm               (default 8.0)
    gap_frac       : float  — gap between boxes as fraction of unit_mm (default 0.07)
    boxes          : list   — list of box dicts.  Each dict may contain:
                               x, y        — top-left position in units (required)
                               w, h        — size in units              (required)
                               name        — identifier string          (default "box_N")
                               text        — display text               (defaults to name)
                               style       — box fill style             (default "plate.cell")
                               text_style      — text style             (default "label")
                               text_size       — font size override mm  (default from style)
                               halign          — text alignment         (default "center";
                                                 auto "left" when lined)
                               valign          — vertical alignment     (default "center";
                                                 auto "top" when lined)
                               lined           — fill box with ruled    (default False)
                                                 lines for handwriting
                               line_spacing_mm — spacing between lines  (default 6.0 mm)
                               (any extra keys are preserved and ignored)
    stylesheet     : str    — stylesheet name                        (default "project_bolt")
    """
    prepare_print  = kwargs.get("prepare_print", False)
    pos            = kwargs.get("pos", [0, 0, 0])
    unit_mm        = float(kwargs.get("unit_mm",         42.0))
    grid_w         = float(kwargs.get("grid_w",           3.0))
    grid_h         = float(kwargs.get("grid_h",           3.5))
    card_margin_mm = float(kwargs.get("card_margin_mm",   2.0))
    card_r         = float(kwargs.get("card_r",           8.0))
    gap_frac       = float(kwargs.get("gap_frac",         0.07))
    boxes          = kwargs.get("boxes", _default_label_boxes())

    # ── Derived dimensions ────────────────────────────────────────────────────
    sheet_w  = grid_w * unit_mm                       # 126.0 mm
    sheet_h  = grid_h * unit_mm                       # 147.0 mm
    card_w   = sheet_w + 2 * card_margin_mm           # 130.0 mm
    card_h   = sheet_h + 2 * card_margin_mm           # 151.0 mm
    gap_mm   = gap_frac * unit_mm                     #   2.94 mm

    # Corner radius rules:
    #   inner: arc radius = gap/2 → arc exactly reaches the gap centreline,
    #          filling the void where four box corners meet
    #   outer: parallel to the card's own rounded corner
    r_inner  = gap_mm / 2
    r_outer  = max(card_r - card_margin_mm, 0.0)

    _EPS = 1e-3   # tolerance for edge-touching checks

    def _radii(bx, by, bw, bh):
        """Return (r_tl, r_tr, r_br, r_bl) for a box at grid position (bx,by)."""
        at_left   = bx              < _EPS
        at_top    = by              < _EPS
        at_right  = (bx + bw - grid_w) > -_EPS
        at_bottom = (by + bh - grid_h) > -_EPS
        tl = r_outer if (at_left  and at_top)    else r_inner
        tr = r_outer if (at_right and at_top)    else r_inner
        br = r_outer if (at_right and at_bottom) else r_inner
        bl = r_outer if (at_left  and at_bottom) else r_inner
        return tl, tr, br, bl

    # ── Stylesheet ────────────────────────────────────────────────────────────
    if "styles" not in thing or not thing.get("styles"):
        sheet_name = kwargs.get("stylesheet", "project_bolt")
        thing["styles"] = svg_styles.get_stylesheet(sheet_name)

    # ── Card fill (drawn first — border comes last) ───────────────────────────
    pos1 = copy.deepcopy(pos)
    opsvg.se(thing, shape="rounded_rectangle", style="plate",
             size=[card_w, card_h, 0], r=card_r, pos=pos1,
             stroke="none", stroke_width=0)

    # ── Boxes ─────────────────────────────────────────────────────────────────
    # Box centre in Y-up coords (origin = card centre = sheet centre):
    #   cx = -sheet_w/2 + unit_mm*(bx + bw/2)
    #   cy =  sheet_h/2 - unit_mm*(by + bh/2)
    # gap_mm cancels in the centre calculation; only affects w_mm / h_mm.
    for i, box in enumerate(boxes):
        bx         = float(box.get("x", 0))
        by         = float(box.get("y", 0))
        bw         = float(box.get("w", 1))
        bh         = float(box.get("h", 1))
        name       = box.get("name",       f"box_{i + 1}")
        text       = box.get("text",       name)
        box_style  = box.get("style",      "plate.cell")
        txt_style  = box.get("text_style", "label")
        txt_size   = box.get("text_size",  None)
        lined      = bool(box.get("lined", False))
        line_spc   = float(box.get("line_spacing_mm", 6.0))

        # lined boxes default to top-left anchored text; explicit values win
        halign = box.get("halign", "left"   if lined else "center")
        valign = box.get("valign", "top"    if lined else "center")

        w_mm = bw * unit_mm - gap_mm
        h_mm = bh * unit_mm - gap_mm
        cx   = -sheet_w / 2 + unit_mm * (bx + bw / 2)
        cy   =  sheet_h / 2 - unit_mm * (by + bh / 2)

        tl, tr, br, bl = _radii(bx, by, bw, bh)

        pos1    = copy.deepcopy(pos)
        pos1[0] += cx
        pos1[1] += cy

        # 1. Box fill
        opsvg.se(thing, shape="rrect_corners", style=box_style,
                 size=[w_mm, h_mm, 0],
                 r_tl=tl, r_tr=tr, r_br=br, r_bl=bl,
                 pos=pos1)

        # 2. Ruled lines (drawn before text so text sits on top)
        if lined:
            pad_x      = gap_mm * 1.5          # horizontal inset
            pad_y      = gap_mm                # top / bottom inset
            rule_w     = w_mm - 2 * pad_x
            rule_thick = 0.35
            y_from_top = pad_y + line_spc * 0.65   # first line
            while y_from_top + rule_thick / 2 < h_mm - pad_y:
                # Y-up offset from box centre: positive = up
                line_dy = h_mm / 2 - y_from_top
                lpos    = copy.deepcopy(pos)
                lpos[0] += cx
                lpos[1] += cy + line_dy
                opsvg.se(thing, shape="rect", style="rule",
                         size=[rule_w, rule_thick, 0], pos=lpos)
                y_from_top += line_spc

        # 3. Text — anchor point offset so halign/valign align to box edge
        padding = gap_mm
        off_x = {"left":  -(w_mm / 2 - padding),
                 "right":  (w_mm / 2 - padding),
                 "center": 0.0}.get(halign, 0.0)
        off_y = {"top":    (h_mm / 2 - padding),    # Y-up: positive = up
                 "bottom": -(h_mm / 2 - padding),
                 "center": 0.0}.get(valign, 0.0)

        txt_pos    = copy.deepcopy(pos)
        txt_pos[0] += cx + off_x
        txt_pos[1] += cy + off_y

        txt_kwargs = dict(halign=halign, valign=valign)
        if txt_size is not None:
            txt_kwargs["size"] = txt_size
        opsvg.se(thing, shape="text", style=txt_style,
                 text=text, pos=txt_pos, **txt_kwargs)

    # ── Card border (drawn last — on top of everything) ───────────────────────
    pos1 = copy.deepcopy(pos)
    opsvg.se(thing, shape="rounded_rectangle", style="plate.outline",
             size=[card_w, card_h, 0], r=card_r, pos=pos1)

    if prepare_print:
        svg_help.prepare_base_for_print(thing, pos, **kwargs)


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)
