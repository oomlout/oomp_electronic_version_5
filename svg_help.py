import copy
import os
import sys
import yaml

import opsvg
import svg_variables as _sv
import svg_styles as _ss
import svg_a4


###### utilities


def get_typ(**kwargs):
    typ = kwargs.get("typ", "")

    if typ == "":
        #setup
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    return typ


def get_build_variables(typ, filter=""):
    if typ == "all":
        return {
            "filter": "",
            "save_type": "all",
            "navigation": True,
            "overwrite": True,
        }

    if typ == "fast":
        return {
            "filter": "",
            "save_type": "all",
            "navigation": False,
            "overwrite": True,
        }

    if typ == "manual":
        return {
            "filter": "",
            #"filter": "label"
            "save_type": "none",
            #"save_type": "all"
            "navigation": True,
            #"navigation": False
            "overwrite": True,
        }

    raise ValueError(f"Unknown typ: {typ}")


def get_navigation_sort(oobb_style=False):
    sort = []
    #sort.append("extra")
    sort.append("oobb_name")
    sort.append("width")
    sort.append("height")
    return sort


def prepare_base_for_print(thing, pos, **kwargs):
    # SVG is a flat 2-D format — there is no Z axis to flip for printing.
    # This stub exists so builder functions that call it remain compatible
    # with the working_scad.py pattern.
    pass


def make_parts(**kwargs):
    parts          = kwargs.get("parts", [])
    filter         = kwargs.get("filter", "")

    #make the parts
    if True:
        for part in parts:
            oobb_name = part.get("oobb_name", "default")
            extra = part["kwargs"].get("extra", "")
            part_id = part.get("id", "")
            if filter in oobb_name or filter in extra or filter in part_id:
                print(f"making {part['oobb_name']}")
                make_svg_generic(part)
            else:
                print(f"skipping {part['oobb_name']}")


def make_svg_generic(part):
    # These keys control output routing and do not belong in builder kwargs.
    svg_details_meta = {
        "svg_name",
        "filename_extra",
        "output_formats",
        "png_dpi",
        "padding",
        "make_a4",
        "write_yaml",
    }

    oobb_name = part.get("oobb_name", "default")
    project_name = part.get("project_name", "default")
    kwargs_base = part.get("kwargs", {})
    save_type = kwargs_base.get("save_type", "all")
    overwrite = kwargs_base.get("overwrite", True)
    kwargs_base["type"] = f"{project_name}_{oobb_name}"

    oomp_id = id_from_part(part)
    part["id"] = oomp_id
    folder = f"parts/{oomp_id}"

    raw_svg_details = part.get("svg_details", {})
    if isinstance(raw_svg_details, list):
        svg_details_list = raw_svg_details
    else:
        svg_details_list = [raw_svg_details]

    if save_type != "all":
        print(f"  dry-run — would write to {folder}/")
        return get_default_thing(**kwargs_base)

    if not os.path.isdir(folder):
        os.makedirs(folder)

    import working_svg

    last_thing = None
    for svg_detail in svg_details_list:
        if not isinstance(svg_detail, dict):
            continue

        svg_detail_filter = str(kwargs_base.get("svg_detail_filter", "")).strip()
        if svg_detail_filter != "":
            filename_extra_filter = str(svg_detail.get("filename_extra", ""))
            svg_name_filter = str(svg_detail.get("svg_name", ""))
            if svg_detail_filter not in [filename_extra_filter, svg_name_filter]:
                continue

        kwargs = copy.deepcopy(kwargs_base)
        for key, value in svg_detail.items():
            if key not in svg_details_meta:
                kwargs[key] = copy.deepcopy(value)

        thing = get_default_thing(**kwargs)
        thing.update(part)

        svg_name = svg_detail.get("svg_name", oobb_name)
        func = getattr(working_svg, f"get_{svg_name}", None)
        if callable(func):
            func(thing, **kwargs)
        else:
            working_svg.get_base(thing, **kwargs)

        filename_extra = svg_detail.get("filename_extra", "")
        suffix = f"_{filename_extra}" if filename_extra else ""
        svg_path = os.path.join(folder, f"working_svg{suffix}.svg")
        padding = svg_detail.get("padding", 1.0)
        opsvg.opsvg_make_object(
            svg_path,
            thing["svg_components"],
            overwrite=overwrite,
            padding=padding,
            scale=float(thing.get("svg_output_scale", 1.0)),
        )

        # The line primitive carries an invisible default fill even though
        # only its stroke is rendered.  Normalize that attribute as well so
        # style_oomp SVG source contains black and white values only.
        stylesheet = kwargs.get("stylesheet", "")
        if stylesheet in ["style_oomp", "style_oomp_assembly"]:
            with open(svg_path, "r", encoding="utf-8") as svg_file:
                svg_contents = svg_file.read()
            svg_contents = svg_contents.replace("#333333", "#000000")
            if stylesheet == "style_oomp_assembly":
                svg_contents = svg_contents.replace(
                    " stroke-width=",
                    ' vector-effect="non-scaling-stroke" stroke-width=',
                )
                pin_one_svg = thing.get("assembly_pin_one_svg", {})
                if isinstance(pin_one_svg, dict) and "x" in pin_one_svg and "y" in pin_one_svg:
                    pin_one_attributes = (
                        f'data-pin-one-x="{float(pin_one_svg["x"]):.4f}" '
                        f'data-pin-one-y="{float(pin_one_svg["y"]):.4f}" '
                    )
                    svg_contents = svg_contents.replace("<svg ", f"<svg {pin_one_attributes}", 1)
            with open(svg_path, "w", encoding="utf-8") as svg_file:
                svg_file.write(svg_contents)

        output_formats = svg_detail.get("output_formats", ["svg"])
        if "png" in output_formats:
            png_path = os.path.join(folder, f"working_svg{suffix}.png")
            png_dpi = int(svg_detail.get("png_dpi", 150))
            svg_to_png(svg_path, png_path, dpi=png_dpi)

        if svg_detail.get("make_a4", True):
            svg_a4.make_a4_sheet(
                svg_path,
                folder,
                part,
                thing,
                filename_extra=filename_extra,
            )

        last_thing = thing

    if last_thing is None:
        return None

    # The new diagram definitions originate in working_oomp_populate_*.py.
    # They can opt out of YAML write-back so rendering never changes metadata.
    write_yaml = False
    for svg_detail in svg_details_list:
        if isinstance(svg_detail, dict) and svg_detail.get("write_yaml", True):
            write_yaml = True

    if write_yaml:
        yaml_file = f"{folder}/working.yaml"
        with open(yaml_file, "w", encoding="utf-8") as file:
            part_new = copy.deepcopy(part)
            kwargs_new = part_new.get("kwargs", {})
            kwargs_new.pop("save_type", "")
            part_new["kwargs"] = kwargs_new
            part_new["project_name"] = os.getcwd()
            part_new["id_svg"] = last_thing.get("id", oomp_id)
            part_new["svg_details"] = copy.deepcopy(raw_svg_details)
            part_new.pop("thing", "")
            yaml.dump(part_new, file, allow_unicode=True)

        yaml_file = f"{folder}/thing.yaml"
        with open(yaml_file, "w", encoding="utf-8") as file:
            part_new = copy.deepcopy(part)
            kwargs_new = part_new.get("kwargs", {})
            kwargs_new.pop("save_type", "")
            part_new["kwargs"] = kwargs_new
            part_new["project_name"] = os.getcwd()
            part_new["id_svg"] = last_thing.get("id", oomp_id)
            part_new["thing"] = _serialisable(last_thing)
            yaml.dump(part_new, file, allow_unicode=True)

    print(f"done {oomp_id}")
    return last_thing


def svg_to_png(svg_path, png_path, dpi=150):
    """Render an SVG to PNG using CairoSVG."""
    try:
        import cairosvg
    except ImportError:
        print("[svg_help] PNG export skipped; install cairosvg")
        return

    # OOMP component renders use a deliberate white page.  Setting the Cairo
    # background also removes the transparent padding around cropped SVGs.
    cairosvg.svg2png(
        url=svg_path,
        write_to=png_path,
        dpi=dpi,
        background_color="#FFFFFF",
    )
    # Cairo can use coloured sub-pixel antialiasing around otherwise black
    # text.  Flatten to grayscale so the PNG contains no accidental hues.
    try:
        from PIL import Image

        with Image.open(png_path) as rendered_image:
            monochrome_image = rendered_image.convert("L").convert("RGB")
            monochrome_image.save(png_path)
    except ImportError:
        pass
    print(f"saved png: {png_path}")


def generate_navigation(folder="parts", sort=["oobb_name", "width", "height"]):
    #crawl through all directories in parts/ and load all working.yaml files
    parts = {}
    for root, dirs, files in os.walk(folder):
        if "working.yaml" in files:
            yaml_file = os.path.join(root, "working.yaml")
            if root != folder:
                with open(yaml_file, "r", encoding="utf-8") as file:
                    part = yaml.safe_load(file)
                    part["folder"] = root
                    part_name = root.replace(f"{folder}", "")
                    part_name = part_name.replace("/", "").replace("\\", "")
                    parts[part_name] = part
                    print(f"Loaded {yaml_file}")

    for part_id in parts:
        if part_id != "":
            part = parts[part_id]

            if "kwargs" in part:
                kwarg_copy = copy.deepcopy(part["kwargs"])
                folder_navigation = "navigation_svg"
                folder_source = part["folder"]
                folder_extra = ""
                for s in sort:
                    if s == "oobb_name":
                        ex = part.get("oobb_name", "default")
                    else:
                        ex = kwarg_copy.get(s, "default")
                        if isinstance(ex, list):
                            ex_string = ""
                            for e in ex:
                                ex_string += f"{e}_"
                            ex = ex_string[:-1]
                            ex = ex.replace(".", "d")
                    folder_extra += f"{s}_{ex}/"

                folder_extra = folder_extra.replace(".", "d")
                folder_destination = f"{folder_navigation}/{folder_extra}"
                if not os.path.exists(folder_destination):
                    os.makedirs(folder_destination)
                if os.name == "nt":
                    command = f'xcopy "{folder_source}" "{folder_destination}" /E /I /Y'
                    print(command)
                    os.system(command)
                else:
                    os.system(f"cp -r {folder_source}/. {folder_destination}")


def get_default_thing(**kwargs):
    # Resolve stylesheet: kwargs may carry "stylesheet" name or a full "styles" dict
    sheet_name = kwargs.get("stylesheet", "default")
    styles     = kwargs.get("styles", None)
    if styles is None:
        styles = _ss.get_stylesheet(sheet_name)
    else:
        styles = copy.deepcopy(styles)

    # Apply any per-part style overrides passed as part_styles
    part_styles = kwargs.get("part_styles", {})
    if part_styles:
        styles = _ss.merge(styles, part_styles)

    thing = {
        "oobb_name":         kwargs.get("oobb_name",         ""),
        "type":              kwargs.get("type",              ""),
        "description":       kwargs.get("description",       ""),
        "classification":    kwargs.get("classification",    "svg"),
        "size":              kwargs.get("size",              ""),
        "color":             kwargs.get("color",             ""),
        "description_main":  kwargs.get("description_main",  ""),
        "description_extra": kwargs.get("description_extra", ""),
        "width":             kwargs.get("width",  1),
        "height":            kwargs.get("height", 1),
        "depth":             kwargs.get("depth",  3),
        "extra":             kwargs.get("extra",  ""),
        "width_mm":          (kwargs.get("width",  1) if isinstance(kwargs.get("width",  1), (int, float)) else 1) * _sv.OSP - _sv.OSP_MINUS,
        "height_mm":         (kwargs.get("height", 1) if isinstance(kwargs.get("height", 1), (int, float)) else 1) * _sv.OSP - _sv.OSP_MINUS,
        "depth_mm":          kwargs.get("depth",  3),
        "svg_components":    [],
        "styles":            styles,
    }
    return thing


def id_from_part(part):
    oomp_keys = ["classification", "type", "size", "color", "description_main", "description_extra"]
    oomp_id = part.get("id", "")
    if not oomp_id:
        for key in oomp_keys:
            val = str(part.get(key, "")).replace(".", "_").strip()
            if val:
                oomp_id += f"{val}_"
        oomp_id = oomp_id.rstrip("_")
    if not oomp_id:
        oomp_id = part.get("oobb_name", "unnamed")
    return oomp_id


def _serialisable(obj, _depth=0):
    if _depth > 10:
        return str(obj)
    if isinstance(obj, dict):
        return {k: _serialisable(v, _depth + 1) for k, v in obj.items()
                if not callable(v)}
    if isinstance(obj, (list, tuple)):
        return [_serialisable(i, _depth + 1) for i in obj]
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    return str(obj)
