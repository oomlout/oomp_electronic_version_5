"""Source data for the Switch Electronics DC-022B panel socket."""
from pathlib import Path

TAXONOMY = {
    "taxonomy_2": "connector", "taxonomy_3": "dc_power_jack",
    "taxonomy_4": "2_1_mm_x_5_5_mm", "taxonomy_5": "panel_mount",
    "taxonomy_6": "solder_lug", "taxonomy_14": "switch_electronics",
    "taxonomy_15": "dc_022b",
}
PART = "electronic_" + "_".join(TAXONOMY.values())
NAME = "2.1 × 5.5 mm Panel Mount DC Power Socket DC-022B"
PRODUCT_URL = (
    "https://www.switchelectronics.co.uk/products/"
    "2-1mm-x-5-5mm-panel-mount-dc-power-socket-dc-022b?variant=45365909750069"
)
DATASHEET_URL = "https://cdn.shopify.com/s/files/1/0695/1347/8453/files/210011.pdf"
SOURCE = Path("parts_source") / PART
SHAFT_DIAMETER_MM = 8.0
SHAFT_ACROSS_FLATS_MM = 6.8


def apply_extras(extras):
    if PART not in extras:
        return
    part = extras[PART]
    part.update({
        "name_short": NAME, "name_readable_override": NAME,
        "diagram_name": "DC-022B panel socket",
        "manufacturer": "Switch Electronics", "part_number_manufacturer": "DC-022B",
        "product_url": PRODUCT_URL, "datasheet_url": DATASHEET_URL,
        "part_number_switch_electronics": "210011",
        "part_number_switch_electronics_url": PRODUCT_URL,
        "component_role": "panel_mount_socket", "pcb_mountable": False,
        "dimensions_mm": {"length": 17.8, "width": 10.0, "height": 10.0},
        "connector_details": {
            "mating_plug": "2.1 mm ID × 5.5 mm OD",
            "panel_cutout_mm": SHAFT_DIAMETER_MM, "panel_thickness_max_mm": 4.0,
            "shaft_across_flats_mm": SHAFT_ACROSS_FLATS_MM,
            "anti_rotation_cutout": "Double-D, nominal Ø8 mm arcs × 6.8 mm across flats",
            "mounting_thread": "M8 × 1", "fixing_nut_included": True,
            "termination": "Solder lug", "housing_material": "PBT",
        },
        "electrical": {"voltage_dc_max_v": 30, "current_max_a": 0.5},
        "pins": {
            "pin_4": {"number": "4", "name": "Centre contact", "type": "passive"},
            "pin_5": {"number": "5", "name": "Sleeve contact", "type": "passive"},
        },
        "dimension_reference": {
            "product_url": PRODUCT_URL, "datasheet_url": DATASHEET_URL, "pdf_page": 1,
            "drawing": "Switch Electronics 210011, 2019-03-01",
            "notes": (
                "Listing envelope 18.2 × Ø10.2 mm. Drawing nominal 17.8 × Ø10.0 mm, excluding nut. "
                "The anti-rotation opening is derived from the drawing's M8 thread and 6.8 mm shaft width."
            ),
        },
        "drawing_note": (
            "Panel opening Ø8 mm, maximum panel thickness 4 mm, M8 × 1 thread. "
            "For anti-rotation, use a double-D opening based on Ø8 mm arcs and 6.8 mm across flats. "
            "These are nominal shaft dimensions. Check the actual socket and allow clearance before cutting. "
            "Rated 30 V DC / 0.5 A. The supplier lists 18.2 × Ø10.2 mm (length × body diameter). "
            "The mechanical drawing and model use the datasheet nominal 17.8 × Ø10.0 mm, excluding nut. "
            "Lug 4 is centre and lug 5 is sleeve. Circuit polarity is set by the wiring."
        ),
        "kicad": {
            "applicability": "not_applicable", "symbol": "", "machine_solder": "",
            "hand_solder": "", "allow_project_fallback": False,
            "reason": "Panel-mounted, wire-terminated socket.",
        },
    })
    part["package_drawing"] = {
        "overall": [17.8, 10.0], "body": [12.0, 10.0], "body_offset": [-2.9, 0],
        "pins": [["4", "right", 5.35, 2.65, 4.5, 0.8], ["5", "right", 6.0, -2.65, 5.8, 0.8]],
        "side": {"overall": [10, 10], "body": [10, 10], "pins": [],
                 "circles": [[0, 0, 4.45], [0, 0, 2.8], [0, 0, 1.05]]},
    }
    asset_names = ["datasheet.pdf", "datasheet_source.yaml", "supplier_page.jpg",
                   "mechanical_drawing.svg", "mechanical_drawing.png"]
    model_names = ["model_3d_render.png", "model_3d_rear.png", "model_3d_source.json"]
    if all((SOURCE / name).is_file() for name in model_names):
        asset_names.extend(model_names)
        part["model_3d"] = {
            "render": "data/model_3d_render.png",
            "rear_render": "data/model_3d_rear.png",
            "provenance": "data/model_3d_source.json",
        }
    if all((SOURCE / name).is_file() for name in ("mechanical_drawing.svg", "mechanical_drawing.png")):
        part["mechanical_drawing"] = {"svg": "data/mechanical_drawing.svg", "png": "data/mechanical_drawing.png"}
    if (SOURCE / "supplier_page.jpg").is_file():
        part["supplier_page_capture"] = "data/supplier_page.jpg"
    part["file_copy"] = [
        {"file_source": (SOURCE / name).as_posix(), "file_destination": name}
        for name in asset_names if (SOURCE / name).is_file()
    ]
