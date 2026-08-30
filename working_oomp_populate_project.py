def main(**kwargs):
    options = kwargs.get("options", [])

    # Add projects here.  Each version is a plain dictionary so an older board
    # revision can point at a tag/commit and a different KiCad file stem.
    projects = [
        {
            "github_user": "electrolama",
            "github_repository": "pt1",
            "repository_url": "https://github.com/electrolama/pt1.git",
            "versions": [
                {
                    "version": "current",
                    "git_ref": "main",
                    "project_file_folder": "pcba/Rev A2",
                    "project_file_basename": "pt1-RevA2",
                    "project_file_path": "pcba/Rev A2/pt1-RevA2",
                    "project_file_path_original": "C:\\gh\\oomp_electronic_version_5\\project\\electrolama\\pt1\\git\\pt1\\pcba\\Rev A2\\pt1-RevA2",
                    "match_overrides": {
                        "CON1": "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12",
                        "CON2": "electronic_connector_usb_c_surface_mount_16_pin_korean_hroparts_elec_typec31m12",
                        "CON3": "electronic_connector_usb_a_surface_mount_4_pin_shenzhen_jing_tuo_jin_electronics_912121a2023s10100",
                        "D1": "electronic_diode_tvs_array_sot_23_6_protek_srv054pt7",
                        "D2": "electronic_diode_tvs_array_sot_23_6_protek_srv054pt7",
                        "IC1": "electronic_ic_qfn_16_3_mm_x_3_mm_converter_usb_to_serial_converter_wch_ch343p",
                        "IC2": "electronic_ic_sop_16_controller_usb_hub_controller_4_port_corechips_sl21a",
                        "IC3": "electronic_ic_sot_23_6_logic_configurable_multi_function_gate_texas_instruments_sn74lvc1g57dbvr",
                        "IC4": "electronic_ic_tsot_23_5_power_management_high_side_power_switch_with_flag_richtek_rt9742cgj5",
                        "J1": "electronic_connector_header_2_54_mm_pitch_through_hole_6_pin",
                        "L1": "electronic_ferrite_bead_0805_220_ohm_2_amp_murata_blm21pg221sn1d",
                        "XT1": "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf",
                    },
                }
            ],
        }
    ]

    project_file_extensions = [
        ".kicad_pcb",
        ".kicad_sch",
        ".kicad_pro",
    ]

    for project in projects:
        versions = project.get("versions", [])
        if versions == []:
            versions = [{"version": "current"}]

        for version_details in versions:
            option = {}
            option["taxonomy_1"] = "oomp"
            option["taxonomy_2"] = "project"
            option["taxonomy_3"] = "github"
            option["taxonomy_4"] = project["github_user"]
            option["taxonomy_5"] = project["github_repository"]
            option["taxonomy_6"] = version_details.get("version", "current")

            option["project_github_user"] = project["github_user"]
            option["project_github_repository"] = project["github_repository"]
            option["project_github_url"] = f"https://github.com/{project['github_user']}/{project['github_repository']}"
            option["project_git_url"] = project["repository_url"]
            option["project_git_ref"] = version_details.get("git_ref", "main")
            option["project_version"] = version_details.get("version", "current")
            option["project_file_folder"] = version_details.get("project_file_folder", "")
            option["project_file_basename"] = version_details.get("project_file_basename", "")
            option["project_file_path"] = version_details.get("project_file_path", "")
            option["project_file_path_original"] = version_details.get("project_file_path_original", "")
            option["project_file_extensions"] = list(project_file_extensions)
            option["project_match_overrides"] = dict(version_details.get("match_overrides", {}))
            options.append(option)


if __name__ == "__main__":
    main()
