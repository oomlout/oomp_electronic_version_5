import copy


def get_svg_details():
    """Return the standard OOMP component diagram set."""
    svg_details = [
        {
            "svg_name": "oomp_component_assembly",
            "filename_extra": "assembly",
            "stylesheet": "style_oomp_assembly",
            "output_formats": ["svg"],
            "padding": 0,
            "make_a4": False,
            "write_yaml": False,
        },
        {
            "svg_name": "oomp_component_assembly_pins",
            "filename_extra": "assembly_pins",
            "stylesheet": "style_oomp_assembly",
            "output_formats": ["svg"],
            "padding": 0,
            "make_a4": False,
            "write_yaml": False,
        },
        {
            "svg_name": "oomp_component_outline",
            "filename_extra": "outline",
            "stylesheet": "style_oomp",
            "output_formats": ["svg", "png"],
            "padding": 0,
            "make_a4": False,
            "write_yaml": False,
        },
        {
            "svg_name": "oomp_component_part_id",
            "filename_extra": "part_id",
            "stylesheet": "style_oomp",
            "output_formats": ["svg", "png"],
            "padding": 0,
            "make_a4": False,
            "write_yaml": False,
        },
        {
            "svg_name": "oomp_component_md5_6_alpha",
            "filename_extra": "md5_6_alpha",
            "stylesheet": "style_oomp",
            "output_formats": ["svg", "png"],
            "padding": 0,
            "make_a4": False,
            "write_yaml": False,
        },
        {
            "svg_name": "oomp_component_bip_39_3_word",
            "filename_extra": "bip_39_3_word",
            "stylesheet": "style_oomp",
            "output_formats": ["svg", "png"],
            "padding": 0,
            "make_a4": False,
            "write_yaml": False,
        },
        {
            "svg_name": "oomp_component_square",
            "filename_extra": "square",
            "stylesheet": "style_oomp",
            "output_formats": ["svg", "png"],
            "padding": 0,
            "make_a4": False,
            "write_yaml": False,
        },
        {
            "svg_name": "oomp_component_square_pins",
            "filename_extra": "square_pins",
            "stylesheet": "style_oomp",
            "output_formats": ["svg", "png"],
            "padding": 0,
            "make_a4": False,
            "write_yaml": False,
        },
        {
            "svg_name": "oomp_component_dimensioned",
            "filename_extra": "dimensioned",
            "stylesheet": "style_oomp",
            "output_formats": ["svg", "png"],
            "padding": 0,
            "make_a4": False,
            "write_yaml": False,
        },
        {
            "svg_name": "oomp_component_dimensioned_titles",
            "filename_extra": "dimensioned_titles",
            "stylesheet": "style_oomp",
            "output_formats": ["svg", "png"],
            "padding": 0,
            "make_a4": False,
            "write_yaml": False,
        },
    ]
    return copy.deepcopy(svg_details)


def _get_number(text, suffix):
    text = str(text)
    for section in text.split("_"):
        if section.isdigit() and suffix in text:
            return int(section)
    return 0


def get_part_id_default(component_type):
    part_ids = {
        "capacitor": "C1",
        "connector": "J1",
        "crystal": "Y1",
        "diode": "D1",
        "display": "DS1",
        "ferrite_bead": "FB1",
        "ic": "U1",
        "led": "D1",
        "mounting_hole": "MH1",
        "prototyping": "BB1",
        "resistor": "R1",
        "transistor": "Q1",
        "wire": "W1",
    }
    return part_ids.get(component_type, "P1")


def get_name_short(option):
    """Build a display name without the leading electronic taxonomy."""
    name_sections = []
    ic_part_number = ""
    for taxonomy_number in range(2, 9):
        taxonomy_name = f"taxonomy_{taxonomy_number}"
        taxonomy_value = str(option.get(taxonomy_name, "")).strip()
        if taxonomy_value != "":
            taxonomy_value = taxonomy_value.replace("2_54", "2.54")
            taxonomy_value = taxonomy_value.replace("_", " ")
            name_sections.append(taxonomy_value)

    # IC display names need the exact manufacturer part number, but not the
    # manufacturer name from taxonomy_14.  Prefer the populated extra detail
    # because it preserves punctuation such as the dot in SL2.1A.
    if option.get("taxonomy_2", "") == "ic":
        ic_part_number = str(option.get("part_number_manufacturer", "")).strip()
        if ic_part_number == "":
            ic_part_number = str(option.get("taxonomy_15", "")).strip().upper()

    name_short = " ".join(name_sections).title()
    replacements = [
        [" Ic ", " IC "],
        [" Led ", " LED "],
        [" Lcd ", " LCD "],
        [" Usb ", " USB "],
        [" Mm", " mm"],
        [" Mhz", " MHz"],
        [" Pf", " pF"],
    ]
    name_short = f" {name_short} "
    for replacement in replacements:
        name_short = name_short.replace(replacement[0], replacement[1])
    name_short = name_short.strip()
    if ic_part_number != "":
        name_short = f"{name_short} {ic_part_number}"
    return name_short


def get_dimensions_mm(option):
    component_type = option.get("taxonomy_2", "")
    size = option.get("taxonomy_3", "")

    surface_mount_sizes = {
        "0201": [0.6, 0.3],
        "0402": [1.0, 0.5],
        "0603": [1.6, 0.8],
        "0805": [2.0, 1.25],
        "1010": [1.0, 1.0],
        "1206": [3.2, 1.6],
        "2512": [6.3, 3.2],
        "3225": [3.2, 2.5],
        "5050": [5.0, 5.0],
    }
    if size in surface_mount_sizes:
        values = surface_mount_sizes[size]
        return {"length": values[0], "width": values[1]}

    if size == "quarter_watt_through_hole":
        return {"length": 6.5, "width": 2.5}
    if size == "3_mm":
        return {"length": 3.0, "width": 3.0}
    if size == "5_mm":
        return {"length": 5.0, "width": 5.0}
    if size == "10_mm":
        return {"length": 10.0, "width": 10.0}
    if size == "3216_avx_a":
        return {"length": 3.2, "width": 1.6}

    capacitor_dimensions = {
        "6_3_mm_diameter_5_4_mm_tall": [6.3, 6.3],
        "6_3_mm_diameter_7_7_mm_tall": [6.3, 6.3],
        "8_mm_diameter_6_5_mm_tall": [8.0, 8.0],
    }
    if size in capacitor_dimensions:
        values = capacitor_dimensions[size]
        return {"length": values[0], "width": values[1]}

    if component_type == "led" and size == "filament_3_volt":
        length = _get_number(option.get("taxonomy_5", ""), "length")
        return {"length": length if length else 38, "width": 2.0}

    if component_type == "led" and size.startswith("strip_"):
        length = _get_number(option.get("taxonomy_5", ""), "length")
        width_sections = size.split("_")
        width = 0
        for index in range(len(width_sections) - 2):
            if width_sections[index].isdigit() and width_sections[index + 1] == "mm":
                width = int(width_sections[index])
        return {
            "length": length if length else 500,
            "width": width if width else 8,
        }

    if component_type == "connector" and size == "header":
        pin_count = _get_number(option.get("taxonomy_6", ""), "pin")
        return {"length": max(pin_count, 1) * 2.54, "width": 2.48}
    if component_type == "connector" and size == "usb_c":
        return {"length": 8.94, "width": 7.35}
    if component_type == "connector" and size == "usb_a":
        return {"length": 14.3, "width": 10.6}

    package_dimensions = {
        "qfn_16_3_mm_x_3_mm": [3.0, 3.0],
        "sop_16": [10.0, 3.9],
        "sot_23_6": [2.9, 1.6],
        "tsot_23_5": [2.9, 1.6],
        "sot_23_5": [2.9, 1.6],
        "sot_23": [2.9, 2.6],
        "sot_89_3": [4.5, 2.5],
        "sot_363_6": [2.0, 1.25],
        "tssop_14": [5.0, 4.4],
        "tssop_16": [5.0, 4.4],
        "tssop_20": [6.5, 4.4],
        "tssop_24": [7.8, 4.4],
        "sop_8_5_28_mm_x_5_23_mm": [5.28, 5.23],
        "updfn_8": [6.0, 5.0],
        "qfn_56_7_mm_x_7_mm": [7.0, 7.0],
        "sod_523f": [1.6, 0.8],
        "sot_523": [1.6, 0.8],
    }
    package = size
    if component_type == "diode":
        package = option.get("taxonomy_4", "")
    if package in package_dimensions:
        values = package_dimensions[package]
        return {"length": values[0], "width": values[1]}

    if component_type == "resistor_array" and size == "4_x_0402_convex":
        return {"length": 3.2, "width": 1.6}

    if component_type == "display":
        return {"length": 80.0, "width": 36.0}

    breadboard_dimensions = {
        "170_point": [46.0, 35.0],
        "400_point": [82.0, 55.0],
        "800_point": [165.0, 55.0],
    }
    if component_type == "prototyping":
        point_count = option.get("taxonomy_4", "")
        if point_count in breadboard_dimensions:
            values = breadboard_dimensions[point_count]
            return {"length": values[0], "width": values[1]}

    if component_type == "wire":
        length = _get_number(option.get("taxonomy_7", ""), "length")
        return {"length": length if length else 150, "width": 2.0}

    return {"length": 10.0, "width": 5.0}


def add_svg_details(option):
    # Family defaults may be applied twice (populate and working_oomp). Keep
    # explicit datasheet dimensions from the populate-extra definition.
    explicit_geometry = {}
    for key in ["ic_dimensions_mm", "connector_dimensions_mm", "header_dimensions_mm", "dimension_reference"]:
        if isinstance(option.get(key), dict):
            explicit_geometry[key] = copy.deepcopy(option[key])
    component_type = option.get("taxonomy_2", "")
    option["name_short"] = option.get("name_short", get_name_short(option))
    option["part_id"] = option.get(
        "part_id",
        get_part_id_default(component_type),
    )
    option["dimensions_mm"] = option.get(
        "dimensions_mm",
        get_dimensions_mm(option),
    )

    if component_type == "mounting_hole":
        option["hole_style"] = option.get("hole_style", option.get("taxonomy_4", "round"))
        option["hole_plating"] = option.get("hole_plating", option.get("taxonomy_5", "unplated"))

    if component_type == "connector" and option.get("taxonomy_3", "") == "header":
        pin_count = _get_number(option.get("taxonomy_6", ""), "pin")
        if option.get("taxonomy_7", "") == "socket":
            option["dimension_reference"] = {
                "manufacturer": "kinghelm",
                "part_number": "kh_2_54fh_1x3p_h8_5",
                "lcsc": "C2932670",
                "datasheet_url": "https://www.lcsc.com/datasheet/C2932670.pdf",
            }
            option["header_dimensions_mm"] = {
                # Kinghelm KH-2.54FH-1X3P-H8.5 drawing, three positions.
                "plastic_length": 7.62,
                "plastic_width": 2.5,
                "plastic_height": 8.5,
                "pin_pitch": 2.54,
                "pin_square": 0.64,
                "pin_thickness": 0.4,
                "recommended_hole_diameter": 1.02,
                # The drawing's code table identifies the 30 terminal option
                # as 3.0 mm.  No mating post protrudes above a female socket.
                "pin_length_total": 11.5,
                "pin_length_post": 0.0,
                "pin_length_tail": 3.0,
            }
        else:
            option["dimension_reference"] = {
                "manufacturer": "samtec",
                "series": "tsw",
                "sample_part_number": "tsw_110_07_t_s",
                "datasheet_url": "https://suddendocs.samtec.com/catalog_english/a-tsw-htsw.pdf",
                "product_url": "https://www.samtec.com/products/tsw-110-07-t-s",
            }
            option["header_dimensions_mm"] = {
                # Samtec TSW-1XX-07 single-row vertical header dimensions.
                "plastic_length": max(pin_count, 1) * 2.54,
                "plastic_width": 2.48,
                "plastic_height": 2.54,
                "pin_pitch": 2.54,
                "pin_square": 0.64,
                "pin_length_total": 10.92,
                "pin_length_post": 5.84,
                "pin_length_tail": 2.54,
            }

    if component_type == "connector" and option.get("taxonomy_3", "") == "usb_a":
        option["connector_dimensions_mm"] = {
            # Shenzhen Jing Tuo Jin 912-121A2023S10100 mechanical drawing.
            "overall_width": 14.3,
            "shell_width": 13.1,
            "body_depth": 10.6,
            "port_height": 5.7,
            "contact_count": 4,
            "contact_pitch": 2.0,
            "contact_width": 1.0,
            "contact_span": 7.0,
            "shell_mount_count": 2,
            "shell_mount_width": 1.45,
            "overall_height": 6.9,
            "shell_height": 5.7,
            "mounting_tail_length": 1.0,
        }

    if component_type == "connector" and option.get("taxonomy_3", "") == "usb_c":
        option["connector_dimensions_mm"] = {
            # Korean Hroparts TYPE-C-31-M-12 mechanical drawing.
            "shell_width": 8.94,
            "body_depth": 7.35,
            "receptacle_width": 8.34,
            "receptacle_height": 2.56,
            "contact_count": 16,
            "contact_pitch": 0.5,
            "contact_width": 0.2,
            "pcb_pad_count": 12,
            "pcb_signal_pad_count": 8,
            "pcb_signal_pad_width": 0.3,
            "pcb_power_pad_count": 4,
            "pcb_power_pad_width": 0.6,
            "pcb_pad_length": 1.5,
            "shell_mount_count": 4,
            "shell_mount_width": 0.6,
            "overall_height": 3.26,
            "side_depth": 6.77,
            "bottom_body_depth": 6.28,
        }

    if component_type == "ic":
        package = option.get("taxonomy_3", "")
        ic_dimensions = {
            "qfn_16_3_mm_x_3_mm": {
                # WCH CH343: QFN16_3X3 package table.
                "body_length": 3.0,
                "body_width": 3.0,
                "pin_pitch": 0.5,
            },
            "sop_16": {
                # CoreChips SL2.1A package drawing, nominal values from ranges.
                "body_length": 9.9,
                "body_width": 3.9,
                "body_length_min": 9.8,
                "body_length_max": 10.0,
                "body_width_min": 3.85,
                "body_width_max": 3.95,
                "overall_width": 6.04,
                "overall_width_min": 5.84,
                "overall_width_max": 6.24,
                "pin_pitch": 1.27,
                "pin_width": 0.406,
                "pin_length": 1.07,
            },
            "sot_23_6": {
                # TI DBV0006A package outline, nominal values from ranges.
                "body_length": 2.9,
                "body_width": 1.6,
                "body_length_min": 2.75,
                "body_length_max": 3.05,
                "body_width_min": 1.45,
                "body_width_max": 1.75,
                "overall_width": 2.8,
                "overall_width_min": 2.6,
                "overall_width_max": 3.0,
                "pin_pitch": 0.95,
                "pin_width": 0.375,
                "pin_length": 0.45,
            },
            "sot_23_5": {
                # Gainsil LMV321 SOT23-5 package table, nominal values from ranges.
                "body_length": 2.92,
                "body_width": 1.6,
                "body_length_min": 2.82,
                "body_length_max": 3.02,
                "body_width_min": 1.5,
                "body_width_max": 1.7,
                "overall_width": 2.8,
                "overall_width_min": 2.65,
                "overall_width_max": 2.95,
                "pin_pitch": 0.95,
                "pin_width": 0.4,
                "pin_length": 0.45,
            },
            "tssop_14": {
                # TI PW0014A TSSOP-14 outline, nominal values from ranges.
                "body_length": 5.0,
                "body_width": 4.4,
                "body_length_min": 4.9,
                "body_length_max": 5.1,
                "body_width_min": 4.3,
                "body_width_max": 4.5,
                "overall_width": 6.4,
                "overall_width_min": 6.2,
                "overall_width_max": 6.6,
                "pin_pitch": 0.65,
                "pin_width": 0.235,
                "pin_length": 0.625,
            },
            "tsot_23_5": {
                # Richtek TSOT-23-5 outline, midpoints of published limits.
                "body_length": 2.8955,
                "body_width": 1.6,
                "body_length_min": 2.692,
                "body_length_max": 3.099,
                "body_width_min": 1.397,
                "body_width_max": 1.803,
                "overall_width": 2.7955,
                "overall_width_min": 2.591,
                "overall_width_max": 3.0,
                "pin_pitch": 0.9395,
                "pin_width": 0.4295,
                "pin_length": 0.455,
            },
        }
        if package in ic_dimensions:
            option["ic_dimensions_mm"] = copy.deepcopy(ic_dimensions[package])
    svg_details = get_svg_details()
    if component_type == "connector":
        connector_views = [
            ["oomp_component_top", "top"],
            ["oomp_component_bottom", "bottom"],
            ["oomp_component_side", "side"],
        ]
        for connector_view in connector_views:
            svg_details.append(
                {
                    "svg_name": connector_view[0],
                    "filename_extra": connector_view[1],
                    "stylesheet": "style_oomp",
                    "output_formats": ["svg", "png"],
                    "padding": 0,
                    "make_a4": False,
                    "write_yaml": False,
                }
            )
    for key, details in explicit_geometry.items():
        option.setdefault(key, {}).update(details)
    option["svg_details"] = svg_details
    return option
