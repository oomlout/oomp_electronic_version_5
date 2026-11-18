append_text = '''
    # Generic match for SW_Push tactile switches used in Easyduino and SparkFun projects
    current = "electronic_switch_tactile_surface_mount_xunpu_ts_1088_ar02016"
    if current in extras_dict:
        part = extras_dict[current]
        part["generic_match"] = {
            "values": ["SW_Push", "SW_SPST", "SW_Tactile"],
            "symbols": ["Switch:SW_Push", "Switch:SW_SPST"],
            "footprints": [
                "Button_Switch_SMD:SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS",
                "Button_Switch_SMD:SW_Push_SPST_NO_Alps_SKRK",
                "Bluepill_Library:ALPSALPINE_SKRPACE010",
                "RP2040:ALPSALPINE_SKRPACE010",
            ],
        }
'''

with open('working_oomp_populate_switch_extra.py', 'a') as f:
    f.write(append_text)

print("done")
