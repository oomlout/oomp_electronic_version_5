"""Generate working_oomp_populate_connector_families_data.py.

Extracts true-scale top-view package drawings from the official KiCad
footprint masters (same approach as the JST data module) for:
  - JST PH 2.0 mm THT vertical (B2B-PH-K-S) and right angle (S2B-PH-K-S)
  - JST PH 2.0 mm SMD right angle (S..B-PH-SM4-TB)
  - JST XH 2.5 mm THT right angle (S..B-XH-A)
  - 2.54 mm right angle pin headers, short-pin and long-pin plastic variants
  - 2.54 mm dual-row header (2x03 ICSP)
"""
import os, sys

sys.path.insert(0, r"C:\gh\oomp_electronic_version_5")
from kicad_agents import kicad_sexpr as sx

KICAD_FP = r"C:\Program Files\KiCad\10.0\share\kicad\footprints"

def _points(node):
    pts = []
    for name in ["start", "end", "center", "mid"]:
        child = sx.child(node, name)
        if child is not None and len(child) >= 3:
            pts.append((float(child[1]), float(child[2])))
    if sx.tag(node) == "fp_rect":
        for sub in node:
            if sx.tag(sub) == "pts":
                for xy in sub:
                    if sx.tag(xy) == "xy" and len(xy) >= 3:
                        pts.append((float(xy[1]), float(xy[2])))
    return pts

def extract_raw(footprint_name):
    path = os.path.join(KICAD_FP, footprint_name.replace(":", ".pretty/") + ".kicad_mod")
    assert os.path.isfile(path), path
    doc = sx.parse(open(path, encoding="utf-8").read())
    fab_pts, pads = [], []
    for node in doc:
        tag = sx.tag(node)
        if tag.startswith("fp_") and sx.value(node, "layer") == "F.Fab":
            fab_pts.extend(_points(node))
        elif tag == "pad":
            at = sx.child(node, "at")
            size = sx.child(node, "size")
            pads.append({
                "number": str(node[1]),
                "x": float(at[1]), "y": float(at[2]),
                "w": float(size[1]), "h": float(size[2]),
            })
    assert fab_pts, footprint_name
    body = (min(p[0] for p in fab_pts), min(p[1] for p in fab_pts),
            max(p[0] for p in fab_pts), max(p[1] for p in fab_pts))
    return body, pads

def finish_drawing(body, pads, mirror_body=False):
    numbered = sorted((p for p in pads if p["number"].isdigit()),
                      key=lambda p: int(p["number"]))
    mounting = [p for p in pads if not p["number"].isdigit()]

    def pad_box(p):
        return (p["x"] - p["w"] / 2, p["y"] - p["h"] / 2, p["x"] + p["w"] / 2, p["y"] + p["h"] / 2)

    overall = [body] + [pad_box(p) for p in numbered] + [pad_box(p) for p in mounting]
    over = (min(b[0] for b in overall), min(b[1] for b in overall),
            max(b[2] for b in overall), max(b[3] for b in overall))
    if mirror_body:
        # Long-pin variant: the plastic block moves to the other side of the
        # pin row (the long legs enter the board).
        pin_y = numbered[0]["y"]
        body = (body[0], 2 * pin_y - body[3], body[2], 2 * pin_y - body[1])
    cx = (body[0] + body[2]) / 2
    cy = (body[1] + body[3]) / 2

    def r4(v):
        return round(v, 4)

    pins = [[p["number"], "top", r4(p["x"] - cx), r4(p["y"] - cy), r4(p["w"]), r4(p["h"])]
            for p in numbered]
    boxes = [[r4(p["x"] - cx), r4(p["y"] - cy), r4(p["w"]), r4(p["h"])] for p in mounting]
    first = numbered[0]
    pin_one = [r4(first["x"] - cx), r4(first["y"] - cy)]
    return {
        "overall": [r4(over[2] - over[0]), r4(over[3] - over[1])],
        "body": [r4(body[2] - body[0]), r4(body[3] - body[1])],
        "pins": pins,
        "boxes": boxes,
        "pin_one": pin_one,
    }

def extract(footprint_name, mirror_body=False):
    body, pads = extract_raw(footprint_name)
    return finish_drawing(body, pads, mirror_body=mirror_body)

FAMILIES = [
    # (kind, taxonomy_3/4/5, mpn template, kicad footprint template, pin range)
    ("jst_ph", "2_mm_pitch", "through_hole_vertical", "B{n}B-PH-K-S", "JST_PH_B{n}B-PH-K_1x{nn}_P2.00mm_Vertical", range(2, 17), "top"),
    ("jst_ph", "2_mm_pitch", "through_hole_right_angle", "S{n}B-PH-K-S", "JST_PH_S{n}B-PH-K_1x{nn}_P2.00mm_Horizontal", range(2, 17), "side"),
    ("jst_ph", "2_mm_pitch", "surface_mount_right_angle", "S{n}B-PH-SM4-TB", "JST_PH_S{n}B-PH-SM4-TB_1x{nn}-1MP_P2.00mm_Horizontal", range(2, 15), "side"),
    ("jst_xh", "2_5_mm_pitch", "through_hole_right_angle", "S{n}B-XH-A", "JST_XH_S{n}B-XH-A_1x{nn}_P2.50mm_Horizontal", range(2, 17), "side"),
]

def main():
    rows = []
    for family, pitch, mounting, mpn_template, fp_template, pin_range, entry in FAMILIES:
        for n in pin_range:
            mpn = mpn_template.format(nn=f"{n:02d}", n=n)
            footprint = fp_template.format(n=n, nn=f"{n:02d}")
            try:
                drawing = extract(f"Connector_JST:{footprint}")
            except AssertionError:
                print("missing master:", footprint)
                continue
            rows.append({
                "family": family,
                "pitch": pitch,
                "mounting": mounting,
                "pin_count": f"{n}_pin",
                "mpn": mpn,
                "kicad_footprint": f"Connector_JST:{footprint}",
                "entry": entry,
                "pin_count_int": n,
                "package_drawing": drawing,
            })
    # 2.54 mm right-angle pin headers: KiCad's horizontal master is the common
    # type with the plastic moulded at the short (board-entry) leg. The
    # long-pin variant mirrors the plastic block across the pin row.
    for n in range(1, 41):
        footprint = f"PinHeader_1x{n:02d}_P2.54mm_Horizontal"
        try:
            short = extract(f"Connector_PinHeader_2.54mm:{footprint}")
            long_pin = extract(f"Connector_PinHeader_2.54mm:{footprint}", mirror_body=True)
        except AssertionError:
            print("missing master:", footprint)
            continue
        rows.append({
            "family": "header", "pitch": "2_54_mm_pitch",
            "mounting": "through_hole_right_angle_short_pin",
            "pin_count": f"{n}_pin", "mpn": "",
            "kicad_footprint": f"Connector_PinHeader_2.54mm:{footprint}",
            "entry": "side", "pin_count_int": n, "package_drawing": short,
        })
        rows.append({
            "family": "header", "pitch": "2_54_mm_pitch",
            "mounting": "through_hole_right_angle_long_pin",
            "pin_count": f"{n}_pin", "mpn": "",
            "kicad_footprint": f"Connector_PinHeader_2.54mm:{footprint}",
            "entry": "side", "pin_count_int": n, "package_drawing": long_pin,
        })
    # Dual-row 2.54 mm header (ICSP 2x03).
    try:
        drawing = extract("Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical")
        rows.append({
            "family": "header", "pitch": "2_54_mm_pitch",
            "mounting": "through_hole", "pin_count": "dual_row_6_pin", "mpn": "",
            "kicad_footprint": "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical",
            "entry": "top", "pin_count_int": 6, "package_drawing": drawing,
        })
    except AssertionError as error:
        print(error)
    import json
    out = r"C:/gh/oomp_electronic_version_5/tmp/connector_families_rows.json"
    json.dump(rows, open(out, "w", encoding="utf-8"), indent=1)
    print("rows:", len(rows))

if __name__ == "__main__":
    main()
