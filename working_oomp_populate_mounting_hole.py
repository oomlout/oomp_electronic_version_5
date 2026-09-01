def _measurement_token(value):
    """Return the plain taxonomy spelling used for a millimetre value."""
    value_text = f"{float(value):g}"
    return value_text.replace(".", "_")


def main(**kwargs):
    options = kwargs.get("options", [])

    # Keep these as simple editable arrays.  Add a diameter or a plating style
    # here and the normal working_oomp population route will make the parts.
    round_hole_diameters_mm = [
        0.65,
        0.7,
        0.8,
        1.0,
        1.5,
        2.0,
        2.5,
        3.0,
        3.2,
        4.0,
        5.0,
        6.0,
    ]
    plating_styles = [
        "unplated",
        "plated",
    ]

    for hole_diameter_mm in round_hole_diameters_mm:
        for plating_style in plating_styles:
            diameter_token = _measurement_token(hole_diameter_mm)
            option = {}
            option["taxonomy_1"] = "mechanical"
            option["taxonomy_2"] = "mounting_hole"
            option["taxonomy_3"] = f"{diameter_token}_mm"
            option["taxonomy_4"] = "round"
            option["taxonomy_5"] = plating_style
            option["hole_style"] = "round"
            option["hole_plating"] = plating_style
            option["hole_diameter_mm"] = float(hole_diameter_mm)
            option["name_short"] = f"Mounting Hole {hole_diameter_mm:g} mm Round {plating_style.title()}"
            option["hole_size_mm"] = {
                "x": float(hole_diameter_mm),
                "y": float(hole_diameter_mm),
            }
            option["dimensions_mm"] = {
                "length": float(hole_diameter_mm),
                "width": float(hole_diameter_mm),
            }
            options.append(option)

    # Slots use explicit width/length pairs so adding a new standard is a
    # one-line edit.  Width is the smaller drill dimension.
    slot_hole_sizes_mm = [
        [0.8, 1.6],
        [1.0, 2.0],
        [1.2, 2.4],
        [2.0, 4.0],
        [3.0, 5.0],
    ]

    for slot_hole_size_mm in slot_hole_sizes_mm:
        for plating_style in plating_styles:
            hole_width_mm = float(slot_hole_size_mm[0])
            hole_length_mm = float(slot_hole_size_mm[1])
            width_token = _measurement_token(hole_width_mm)
            length_token = _measurement_token(hole_length_mm)
            option = {}
            option["taxonomy_1"] = "mechanical"
            option["taxonomy_2"] = "mounting_hole"
            option["taxonomy_3"] = f"{width_token}_mm_x_{length_token}_mm"
            option["taxonomy_4"] = "slot"
            option["taxonomy_5"] = plating_style
            option["hole_style"] = "slot"
            option["hole_plating"] = plating_style
            option["name_short"] = (
                f"Mounting Hole {hole_width_mm:g} mm x {hole_length_mm:g} mm "
                f"Slot {plating_style.title()}"
            )
            option["hole_size_mm"] = {
                "x": hole_width_mm,
                "y": hole_length_mm,
            }
            option["dimensions_mm"] = {
                "length": hole_width_mm,
                "width": hole_length_mm,
            }
            options.append(option)


if __name__ == "__main__":
    main()
