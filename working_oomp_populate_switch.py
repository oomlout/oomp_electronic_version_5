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

    # First DIP switches: Cixi Tonver slide DIP switches (SPST per position,
    # 2.54 mm pitch, 24V 25mA) from the JLC house-parts queue.  taxonomy_5
    # carries circuit + positions, taxonomy_6 the actuator style (the two
    # 8-position SMD parts differ only by raised vs recessed actuators).
    options.append({
        "taxonomy_2": "switch", "taxonomy_3": "dip_switch", "taxonomy_4": "through_hole",
        "taxonomy_5": "spst_5_position", "taxonomy_6": "raised_actuator",
        "taxonomy_14": "cixi_tonver", "taxonomy_15": "ham_05hwa_r",
        "name_short": "DIP Switch HAM-05HWA-R (5-pos SPST slide)",
    })
    options.append({
        "taxonomy_2": "switch", "taxonomy_3": "dip_switch", "taxonomy_4": "through_hole",
        "taxonomy_5": "spst_9_position", "taxonomy_6": "raised_actuator",
        "taxonomy_14": "cixi_tonver", "taxonomy_15": "yam_09hwag",
        "name_short": "DIP Switch YAM-09HWAG (9-pos SPST slide)",
    })
    options.append({
        "taxonomy_2": "switch", "taxonomy_3": "dip_switch", "taxonomy_4": "surface_mount",
        "taxonomy_5": "spst_8_position", "taxonomy_6": "raised_actuator",
        "taxonomy_14": "cixi_tonver", "taxonomy_15": "had_08hwag_r",
        "name_short": "DIP Switch HAD-08HWAG-R (8-pos SPST slide, raised)",
    })
    options.append({
        "taxonomy_2": "switch", "taxonomy_3": "dip_switch", "taxonomy_4": "surface_mount",
        "taxonomy_5": "spst_8_position", "taxonomy_6": "recessed_actuator",
        "taxonomy_14": "cixi_tonver", "taxonomy_15": "had_08lwag_2",
        "name_short": "DIP Switch HAD-08LWAG-2 (8-pos SPST slide, recessed)",
    })
    options.append({
        "taxonomy_2": "switch", "taxonomy_3": "dip_switch", "taxonomy_4": "through_hole",
        "taxonomy_5": "spst_10_position", "taxonomy_6": "recessed_actuator",
        "taxonomy_14": "cixi_tonver", "taxonomy_15": "ham_10lwa_r",
        "name_short": "DIP Switch HAM-10LWA-R (10-pos SPST slide, recessed)",
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
            "manufacturer": "switronic", "part_number": "it_1109s",
            "name_short": "Switronic IT-1109S Tactile Switch",
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
            "style": "tactile", "mounting": "surface_mount",
            "manufacturer": "xkb_connection", "part_number": "ts_1187a_b_a_b",
            "name_short": "XKB TS-1187A-B-A-B Tactile Switch",
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
