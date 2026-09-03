def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})
    current = "electronic_switch_tactile_surface_mount_xunpu_ts_1088_ar02016"
    if current in extras_dict:
        part = extras_dict[current]
        part["manufacturer"] = "XUNPU"
        part["part_number_manufacturer"] = "TS-1088-AR02016"
        part["file_copy"] = [{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}]
        part["part_number_lcsc"] = "C720477"
        part["product_url"] = "https://www.lcsc.com/product-detail/C720477.html"
        part["datasheet_url"] = "https://www.lcsc.com/datasheet/C720477.pdf"
        part["category"] = "switch"
        part["dimensions_mm"] = {"length": 4.8, "width": 3.0, "height": 2.0}
        part["dimension_reference"] = {"document": "XUNPU TS-1088", "pages": [1], "notes": "4x3 body, 4.8mm terminal span, 1.3mm terminal width; AR02016 is 2mm high, 1.6N."}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "contact_1", "type": "passive"},
            "pin_2": {"number": "2", "name": "contact_2", "type": "passive"},
        }
        part["package_drawing"] = {
            "overall": [4.8, 3], "body": [4, 3],
            "pins": [["1", "left", -2.2, 0, .4, 1.3], ["2", "right", 2.2, 0, .4, 1.3]],
            "circles": [[0, 0, .85]],
        }
        part["kicad"] = {"symbol": "Switch:SW_Push", "machine_solder": "", "hand_solder": "", "allow_project_fallback": False}
        part["research_notes"] = ["Nonpolar contacts numbered 1/2 using schematic convention. No exact XUNPU master footprint verified; the upstream Alps_SKRK footprint is retained, not certified interchangeable."]
