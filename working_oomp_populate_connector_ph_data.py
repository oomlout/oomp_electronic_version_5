"""The five existing BOOMELE PH-style headers under their exact catalogue IDs."""
from oomp_populate_helper import build_oomp_id


PARTS = []
for positions, mount, mpn, code, width, height in (
    (2, "through_hole", "PH-2A", "C2319", 4.8, 6.0),
    (3, "through_hole", "PH-3A", "C2320", 5.0, 6.0),
    (4, "through_hole", "PH-4A", "C2321", 4.7, 6.05),
    (5, "through_hole", "PH-5A", "C2322", 5.0, 6.0),
    (6, "through_hole_right_angle", "PH-6AW", "C5662", 6.0, 5.0),
):
    taxonomy = {
        "taxonomy_2": "connector", "taxonomy_3": "jst_ph", "taxonomy_4": "2_mm_pitch",
        "taxonomy_5": mount, "taxonomy_6": f"{positions}_pin",
        "taxonomy_14": "boomele_boom_precision_elec", "taxonomy_15": mpn.lower().replace("-", "_"),
    }
    PARTS.append({
        "id": build_oomp_id({"taxonomy_1": "electronic", **taxonomy}),
        "old": f"electronic_connector_ph_2_mm_pitch_{mount}_{positions}_pin",
        "taxonomy": taxonomy, "mpn": mpn, "code": code,
        "dimensions": {"length": 2.0 * (positions + 1), "width": width, "height": height},
        "positions": positions, "shared_drawing": positions in (5, 6),
    })

# Original distributor documents. The PH-3A download covers PH-5A and PH-6AW.
DRAWINGS = ("8757121760939008000", "8588905910421106688", "8757245273171345408",
            "8588886973348261888", "8588887093955203072")


def apply_extras(extras):
    for row, drawing in zip(PARTS, DRAWINGS):
        if row["id"] not in extras:
            continue
        part = extras[row["id"]]
        count = row["positions"]
        length, width, height = row["dimensions"].values()
        mount = "right-angle" if count == 6 else "vertical"
        datasheet_url = ("https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/"
                         f"{drawing}-{row['code']}.pdf")
        part.update(
            name_readable_override=f"BOOMELE PH 2 mm {count}-position {mount} header ({row['mpn']})",
            dimensions_mm=dict(row["dimensions"]),
            datasheet_url=datasheet_url,
            pins={f"pin_{i}": {"number": str(i), "name": f"pin_{i}", "type": "passive"}
                  for i in range(1, count + 1)},
            package_drawing={
                "overall": [length, width], "body": [length, width], "pins": [],
                "side": {"overall": [width, height], "body": [width, height], "pins": []},
            },
            diagram_name=f"BOOMELE {row['mpn']}",
            drawing_note="Housing envelope from the distributor drawing. Refer to the drawing for PCB drilling and fit.",
            dimension_reference={
                "document": f"BOOMELE {row['mpn']} distributor drawing",
                "pdf_page": 1, "datasheet_url": datasheet_url,
                "notes": "Nominal body dimensions. Board tails are excluded from the envelope.",
            },
            file_copy=[{
                "file_source": f"parts_source/{row['id']}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }],
        )
        if row["shared_drawing"]:
            part["oomp_datasheet_common_with"] = PARTS[1]["id"]
