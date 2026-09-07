def main(**kwargs):
    options = kwargs.get("options", [])
    options.append({
        "taxonomy_2": "switch", "taxonomy_3": "slide", "taxonomy_4": "surface_mount",
        "taxonomy_5": "dpdt",
        "taxonomy_14": "ck", "taxonomy_15": "dshp03ts_s",
        "name_short": "Slide Switch DSHP03TS-S",
    })
    options.append({
        "taxonomy_2": "switch", "taxonomy_3": "tactile", "taxonomy_4": "surface_mount",
        "taxonomy_14": "xunpu", "taxonomy_15": "ts_1088_ar02016",
        "name_short": "Push Button TS-1088-AR02016",
    })

    # Unmatched-project population records.  These intentionally contain only
    # the identity visible in the project data; manufacturer evidence and
    # project matching are added in the later research/match pass.
    unmatched_switches = [
        {
            "style": "tactile", "mounting": "surface_mount",
            "manufacturer": "", "part_number": "pts810",
            "name_short": "Tactile Switch PTS810",
        },
        {
            "style": "tactile", "mounting": "through_hole",
            "manufacturer": "", "part_number": "gt_tc026x_hxxx_lx",
            "name_short": "4P Button Switch GT-TC026X-HXXX-LX",
        },
        {
            "style": "tactile", "mounting": "surface_mount",
            "manufacturer": "omron", "part_number": "b3fs_100xp",
            "name_short": "Omron B3FS-100xP Tactile Switch",
        },
        {
            "style": "tactile", "mounting": "surface_mount",
            "manufacturer": "ck", "part_number": "pts636",
            "name_short": "CK PTS636 Tactile Switch",
        },
        {
            "style": "tactile", "mounting": "surface_mount",
            "manufacturer": "alps_alpine", "part_number": "skr_k",
            "name_short": "Alps SKRK Tactile Switch",
        },
        {
            "style": "tactile", "mounting": "surface_mount",
            "manufacturer": "alps_alpine", "part_number": "skrpace010",
            "name_short": "Alps SKRPACE010 Tactile Switch",
        },
        {
            "style": "navigation", "mounting": "surface_mount",
            "size": "7_5_mm", "name_short": "Five-Way Navigation Switch 7.5 mm",
        },
        {
            "style": "navigation", "mounting": "surface_mount",
            "size": "9_9_mm", "name_short": "Five-Way Navigation Switch 9.9 mm",
        },
        {
            "style": "roller_encoder", "mounting": "through_hole",
            "part_number": "roller_encoder_switch",
            "name_short": "Roller Encoder Switch",
        },
    ]
    for switch in unmatched_switches:
        option = {
            "taxonomy_2": "switch",
            "taxonomy_3": switch["style"],
            "taxonomy_4": switch["mounting"],
        }
        if switch.get("size"):
            option["taxonomy_5"] = switch["size"]
        if switch.get("manufacturer"):
            option["taxonomy_14"] = switch["manufacturer"]
        if switch.get("part_number"):
            option["taxonomy_15"] = switch["part_number"]
        option["name_short"] = switch["name_short"]
        options.append(option)
