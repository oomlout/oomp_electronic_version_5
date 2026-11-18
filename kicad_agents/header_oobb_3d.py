"""Regenerate reusable 2.54 mm header STEP and material-separated STL assets.

Run `python -m kicad_agents.header_oobb_3d` from the repository root.
Requires OpenCascade Python bindings (cadquery-ocp).
Coordinates are mm: contacts lie along Y, positions run along X, Z=0 is their axis.
"""

import json
import hashlib
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
STOCK_ID = "electronic_connector_header_long_2_54_mm_pitch_through_hole_6_pin"
BASIC_ID = "electronic_connector_header_oobb_2_54_mm_pitch_basic_6_position_3_contact"
HOUSING_ID = "electronic_connector_header_2_54_mm_pitch_housing_3_pin_black_harwin_m20_1060300"
CONTACT_ID = "electronic_connector_header_2_54_mm_pitch_crimp_1_pin_socket_22_to_30_awg_tin_harwin_m20_1180046"
PITCH = 2.54
LONG_BODY = 2.5
LONG_END = 6.25
LONG_TOTAL = 15.0
LONG_MPN = "1625-1140CNG0S150001"
LONG_LCSC = "C343639"
LONG_PRODUCT_URL = "https://www.lcsc.com/product-detail/C343639.html"
LONG_DATASHEET_URL = "https://atta.szlcsc.com/upload/public/pdf/source/20260917/9F655738B2D4F4FC500A9931BECCBD77.pdf"
LONG_DRAWING = "HYC-1812011115, sheet 1 of 1, dated 2014-02-23"
BASIC_REMOVED = (1, 2, 6)
VARIANTS = {
    "basic": dict(count=6, removed=(1, 2, 6), contacts=3, header_x=0, housing_x=1.27, rear_y=7),
    "power": dict(count=5, removed=(1, 2, 5), contacts=2, header_x=-1.27, housing_x=0, rear_y=7),
    "motor": dict(count=4, removed=(1, 4), contacts=2, header_x=0, housing_x=0, rear_y=7),
    "motor_stepper": dict(count=6, removed=(1, 6), contacts=4, header_x=0, housing_x=0, rear_y=7),
    "i2c": dict(count=7, removed=(1, 2, 7), contacts=4, header_x=0, housing_x=1.27, rear_y=7),
}


for _rows in range(2, 11):
    VARIANTS[f"vertical_{_rows}_row"] = dict(count=_rows+2, removed=(1, _rows+2),
                                             contacts=_rows, vertical=True)


def stock_id(count):
    return f"electronic_connector_header_2_54_mm_pitch_through_hole_{count}_pin"


def long_id(count):
    return f"electronic_connector_header_long_2_54_mm_pitch_through_hole_{count}_pin"


def long_reference(option):
    option.update(
        header_stock_type="header_long", reference_mpn=LONG_MPN, reference_lcsc=LONG_LCSC,
        reference_product_url=LONG_PRODUCT_URL, datasheet_url=LONG_DATASHEET_URL,
        dimension_reference=dict(manufacturer="HOAUC", drawing=LONG_DRAWING, checked_on="2026-11-16"),
        header_dimensions_mm=dict(pitch=PITCH, insulator_depth=LONG_BODY, insulator_height=LONG_BODY,
                                  pin_square=.64, front_pin=LONG_END, rear_pin=LONG_END, overall_pin=LONG_TOTAL),
        procurement_notes="LCSC C343639 is a 40-position strip. Shorter generic lengths represent sections cut from that strip; the family drawing lists 1–40 positions.",
        oomp_datasheet_common_with=long_id(40))
    copies = option.setdefault("file_copy", [])
    record = dict(file_source=f"parts_source/{long_id(40)}/datasheet.pdf", file_destination="datasheet.pdf")
    if record not in copies:
        copies.append(record)
    return option


def long_option(count):
    option = dict(taxonomy_2="connector", taxonomy_3="header_long", taxonomy_4="2_54_mm_pitch",
                  taxonomy_5="through_hole", taxonomy_6=f"{count}_pin",
                  name_short=f"Long equal-pin header, {count} positions, 2.54 mm pitch",
                  dimensions_mm=dict(length=count*PITCH, width=LONG_TOTAL, height=LONG_BODY),
                  connector_details=dict(positions=count, pitch_mm=PITCH, exposed_each_end_mm=LONG_END,
                                         insulator_mm=LONG_BODY, overall_pin_mm=LONG_TOTAL))
    option["name_readable_override"] = option["name_short"]
    long_reference(option)
    if count == 40:
        option["distributors"] = [dict(title="LCSC", part_number=LONG_LCSC, url=LONG_PRODUCT_URL)]
    return attach_assets(option, long_id(count))


def variant_id(kind):
    v = VARIANTS[kind]
    return f"electronic_connector_header_oobb_2_54_mm_pitch_{kind}_{v['count']}_position_{v['contacts']}_contact"


def housing_id(count):
    return f"electronic_connector_header_2_54_mm_pitch_housing_{count}_pin_black_harwin_m20_106{count:02d}00"


def variant_option(kind):
    v = VARIANTS[kind]
    option = dict(taxonomy_2="connector", taxonomy_3="header_oobb", taxonomy_4="2_54_mm_pitch",
                  taxonomy_5=kind, taxonomy_6=f"{v['count']}_position", taxonomy_7=f"{v['contacts']}_contact",
                  name_short=f"OOBB {kind.replace('_', ' ')} header, {v['count']} positions / {v['contacts']} contacts",
                  parent_header_id=long_id(v['count']), removed_pin_positions=list(v['removed']),
                  retained_pin_positions=[i for i in range(1, v['count']+1) if i not in v['removed']])
    vertical = v.get("vertical", False)
    option["name_readable_override"] = option["name_short"]
    option.update(
        pcb_mountable=False,
        dimensions_mm=dict(length=LONG_BODY if vertical else v["count"]*PITCH,
                           width=LONG_TOTAL, height=v["count"]*PITCH if vertical else LONG_BODY),
        connector_details=dict(orientation="vertical, count bottom to top" if vertical else "horizontal, count from negative X",
                               positions=v["count"], contacts=v["contacts"], removed=list(v["removed"])),
        drawing_note="Nominal reference geometry; empty plastic end cells retain the connector in its OOBB plate.",
        kicad=dict(applicability="not_applicable", reason="Prepared cable connector for an OOBB plate."))
    long_reference(option)
    return attach_assets(option, variant_id(kind))


ARRANGEMENT_ASSETS = ("model_3d_3_strip.step", "model_3d_3_strip_body.stl", "model_3d_3_strip_pins.stl", "model_3d_arrangement.png")
MODEL_ASSETS = ("model_3d.step", "model_3d_body.stl", "model_3d_pins.stl", "model_3d_source.json")


def attach_assets(option, part_id):
    option["readme_template_folder"] = "source_file/template_jinja/header_reference"
    relative = Path("parts_source") / part_id
    copies = option.setdefault("file_copy", [])
    for name in (*MODEL_ASSETS, "model_3d_render.png", *(ARRANGEMENT_ASSETS if "vertical_" in part_id else ())):
        file_source = (relative / name).as_posix()
        if (name.endswith(".png") or name in ARRANGEMENT_ASSETS) and not (ROOT / file_source).is_file():
            continue
        if not any(entry.get("file_source") == file_source for entry in copies):
            copies.append({"file_source": file_source, "file_destination": name})
    option["model_3d"] = {"step": "data/model_3d.step", "provenance": "data/model_3d_source.json",
                          "generator": "kicad_agents/header_oobb_3d.py"}
    if (ROOT / relative / "model_3d_render.png").is_file():
        option["model_3d"]["render"] = "data/model_3d_render.png"
    if "vertical_" in part_id:
        option["model_3d"].update(arrangement_step="data/model_3d_3_strip.step",
                                   arrangement_render="data/model_3d_arrangement.png")
    return option


def basic_option():
    return variant_option("basic")


def positions(count=6):
    return {i: (i - (count + 1) / 2) * PITCH for i in range(1, count + 1)}


def build(count, removed=(), long=False):
    from OCP.BRepAlgoAPI import BRepAlgoAPI_Cut
    from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeFace, BRepBuilderAPI_MakePolygon
    from OCP.BRepOffsetAPI import BRepOffsetAPI_ThruSections
    from OCP.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakePrism
    from OCP.gp import gp_Pnt, gp_Vec

    def wire(points):
        p = BRepBuilderAPI_MakePolygon()
        for xyz in points:
            p.Add(gp_Pnt(*xyz))
        p.Close()
        return p.Wire()

    half = (LONG_BODY if long else PITCH) / 2
    front, rear = (LONG_END, LONG_END) if long else (6.1, 3.0)
    axes = positions(count)
    if not set(removed) <= axes.keys():
        raise ValueError("Depopulated positions must be within the strip")
    edges = [(x + dx, y) for x in axes.values() for dx, y in
             ((-1.27, -half+.36), (-.91, -half), (.91, -half), (1.27, -half+.36))]
    # The slight grooves between cells suggest a breakaway strip.
    outline = list(dict.fromkeys(edges + [(x, -y) for x, y in reversed(edges)]))
    body = BRepPrimAPI_MakePrism(BRepBuilderAPI_MakeFace(
        wire([(x, -half, z) for x, z in outline])).Face(), gp_Vec(0, 2*half, 0)).Shape()
    pins = []
    for index, x in axes.items():
        tool = BRepPrimAPI_MakeBox(gp_Pnt(x - .32, -half-.13, -.32), .64, 2*half+.26, .64).Shape()
        body = BRepAlgoAPI_Cut(body, tool).Shape()
        if index in removed:
            continue
        loft = BRepOffsetAPI_ThruSections(True, True)
        for y, a in ((-half-front, .18), (-half-front+.3, .32), (half+rear-.3, .32), (half+rear, .18)):
            loft.AddWire(wire([(x-a, y, -a), (x+a, y, -a), (x+a, y, a), (x-a, y, a)]))
        loft.Build()
        pins.append(loft.Shape())
    return body, pins


def compound(shapes):
    from OCP.BRep import BRep_Builder
    from OCP.TopoDS import TopoDS_Compound
    result = TopoDS_Compound()
    builder = BRep_Builder()
    builder.MakeCompound(result)
    for shape in shapes:
        builder.Add(result, shape)
    return result


def read_step(path):
    from OCP.IFSelect import IFSelect_RetDone
    from OCP.STEPControl import STEPControl_Reader
    reader = STEPControl_Reader()
    if reader.ReadFile(str(path)) != IFSelect_RetDone or not reader.TransferRoots():
        raise ValueError(f"Could not import {path}")
    return reader.OneShape()


def write_stl(shape, path):
    from OCP.BRepMesh import BRepMesh_IncrementalMesh
    from OCP.StlAPI import StlAPI_Writer
    BRepMesh_IncrementalMesh(shape, .025, False, .15, False).Perform()
    writer = StlAPI_Writer()
    writer.ASCIIMode = False
    if not writer.Write(shape, str(path)):
        raise RuntimeError(f"Failed to write {path}")


def generate(part_id, removed=(), count=6, vertical=False, long=None):
    from OCP.BRepCheck import BRepCheck_Analyzer
    from OCP.IFSelect import IFSelect_RetDone
    from OCP.STEPControl import STEPControl_AsIs, STEPControl_Writer
    needs_long = "header_long_" in part_id or "header_oobb_" in part_id
    if long is None:
        long = needs_long
    if needs_long and not long:
        raise ValueError("header_long and header_oobb records require equal-ended long pins")
    source = ROOT / "parts_source" / part_id
    data = ROOT / "parts" / part_id / "data"
    source.mkdir(parents=True, exist_ok=True)
    data.mkdir(parents=True, exist_ok=True)
    body, pins = build(count, removed, long=long)
    if vertical:
        from math import pi
        from OCP.gp import gp_Trsf, gp_Ax1, gp_Pnt, gp_Dir
        from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
        transform = gp_Trsf()
        transform.SetRotation(gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 1, 0)), -pi/2)
        body = BRepBuilderAPI_Transform(body, transform, True).Shape()
        pins = [BRepBuilderAPI_Transform(pin, transform, True).Shape() for pin in pins]
    if len(pins) != count - len(removed) or not all(BRepCheck_Analyzer(s).IsValid() for s in (body, *pins)):
        raise ValueError(f"Invalid header geometry: {part_id}")
    writer = STEPControl_Writer()
    writer.Transfer(compound([body, *pins]), STEPControl_AsIs)
    if writer.Write(str(source / "model_3d.step")) != IFSelect_RetDone:
        raise RuntimeError(f"Failed to write header STEP: {part_id}")
    write_stl(body, source / "model_3d_body.stl")
    write_stl(compound(pins), source / "model_3d_pins.stl")
    record = dict(pitch_mm=PITCH, positions=count, removed=list(removed),
                  retained=[i for i in positions(count) if i not in removed],
                  orientation=("Vertical strip: positions run bottom to top along Z; contacts lie along Y." if vertical else
                               "Contacts lie along Y; count from negative X. Snap grooves are on the top/bottom Z faces."),
                  vertical=vertical,
                  header_type="header_long" if long else "header",
                  insulator_mm=LONG_BODY if long else PITCH,
                  exposed_pin_ends_mm=[LONG_END, LONG_END] if long else [6.1, 3.0],
                  total_pin_mm=LONG_TOTAL if long else 11.64,
                  dimensions_reference=LONG_DATASHEET_URL if long else "https://www.harwin.com/products/M20-9990645",
                  limits="Nominal straight-header geometry extrapolated at 2.54 mm pitch; existing KiCad STEP is unchanged.")
    if long:
        datasheet = ROOT / "parts_source" / long_id(40) / "datasheet.pdf"
        record.update(drawing=LONG_DRAWING, reference_mpn=LONG_MPN, lcsc=LONG_LCSC,
                      datasheet_sha256=hashlib.sha256(datasheet.read_bytes()).hexdigest(),
                      limits="Nominal manufacturer envelope and pitch for 1–40 positions; grooves and tip bevels are illustrative. C343639 is the 40-position stock strip.")
        shutil.copyfile(datasheet, data / "datasheet.pdf")
    (source / "model_3d_source.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    for name in MODEL_ASSETS:
        shutil.copyfile(source / name, data / name)
    if vertical:
        generate_arrangement(part_id)


def generate_arrangement(part_id):
    """Place three copies of a vertical strip on the standard pitch."""
    from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
    from OCP.gp import gp_Trsf, gp_Vec
    from OCP.STEPControl import STEPControl_AsIs, STEPControl_Writer
    from OCP.IFSelect import IFSelect_RetDone
    from OCP.BRepCheck import BRepCheck_Analyzer
    # Read back the verified STEP and separate body/pin solids by their volume.
    from OCP.TopExp import TopExp_Explorer
    from OCP.TopAbs import TopAbs_SOLID
    source = ROOT / "parts_source" / part_id
    data = ROOT / "parts" / part_id / "data"
    step = read_step(source / "model_3d.step")
    explorer = TopExp_Explorer(step, TopAbs_SOLID)
    solids = []
    while explorer.More():
        solids.append(explorer.Current())
        explorer.Next()
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    def volume(solid):
        properties = GProp_GProps()
        BRepGProp.VolumeProperties_s(solid, properties)
        return properties.Mass()
    solids.sort(key=volume, reverse=True)
    bodies, pins = [], []
    for x in (-2.54, 0, 2.54):
        move = gp_Trsf()
        move.SetTranslation(gp_Vec(x, 0, 0))
        bodies.append(BRepBuilderAPI_Transform(solids[0], move, True).Shape())
        pins.extend(BRepBuilderAPI_Transform(pin, move, True).Shape() for pin in solids[1:])
    result = compound([*bodies, *pins])
    if not BRepCheck_Analyzer(result).IsValid():
        raise ValueError(part_id)
    writer = STEPControl_Writer()
    writer.Transfer(result, STEPControl_AsIs)
    if writer.Write(str(source / "model_3d_3_strip.step")) != IFSelect_RetDone:
        raise RuntimeError(part_id)
    write_stl(compound(bodies), source / "model_3d_3_strip_body.stl")
    write_stl(compound(pins), source / "model_3d_3_strip_pins.stl")
    for name in ARRANGEMENT_ASSETS[:-1]:
        shutil.copyfile(source / name, data / name)


def main(only_vertical=False, metadata_only=False, long_only=False):
    from oomp_populate_helper import write_extras
    from os import chdir
    import working_oomp
    import working_oomp_populate_category as categories
    import working_oomp_populate_svg as svg
    import yaml
    from jinja2 import Environment, FileSystemLoader
    from kicad_agents.part_file_table import file_table, local_files

    chdir(ROOT)
    options, identities = [], []
    if not only_vertical:
        if not long_only:
            for count in range(1, 41):
                identity = stock_id(count)
                option = yaml.safe_load((ROOT / "parts_source" / identity / "working.yaml").read_text(encoding="utf-8"))
                attach_assets(option, identity)
                options.append(option)
                identities.append(identity)
                if not metadata_only:
                    generate(identity, count=count)
        for count in range(1, 41):
            option = dict(long_option(count), taxonomy_1="electronic")
            svg.add_svg_details(option)
            categories.add_category(option)
            options.append(option)
            identities.append(long_id(count))
            if not metadata_only:
                generate(long_id(count), count=count, long=True)
    for kind, variant in VARIANTS.items():
        if only_vertical and not variant.get("vertical"):
            continue
        option = dict(variant_option(kind), taxonomy_1="electronic")
        svg.add_svg_details(option)
        categories.add_category(option)
        options.append(option)
        identities.append(variant_id(kind))
        if not metadata_only:
            generate(variant_id(kind), variant["removed"], variant["count"], variant.get("vertical", False), long=True)
    write_extras(options)
    working_oomp.main(filter=identities)
    template = Environment(loader=FileSystemLoader(ROOT / "source_file/template_jinja/header_reference"), trim_blocks=True, lstrip_blocks=True).get_template("working.md.j2")
    for identity in identities:
        canonical = ROOT / "parts" / identity
        part = yaml.safe_load((canonical / "working.yaml").read_text(encoding="utf-8"))
        (canonical / "README.md").write_text(
            template.render(p=part, file_table=file_table(local_files(canonical))), encoding="utf-8")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only-vertical", action="store_true")
    parser.add_argument("--metadata-only", action="store_true")
    parser.add_argument("--long-only", action="store_true", help="Build long stock and OOBB variants, retaining PCB-header assets")
    args = parser.parse_args()
    main(args.only_vertical, args.metadata_only, args.long_only)
