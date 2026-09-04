import oomp
import oomp_helper
import copy
import oomlout_roboclick
import os
import yaml

import working_oomp_metadata


DATA_DIRECTORY = "data"


def as_boolean(value):
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ["1", "true", "yes", "on"]


def add_part_page_details(part):
    """Prepare small, explicit arrays used by the part Markdown template."""
    taxonomy = []
    for taxonomy_number in range(1, 16):
        taxonomy_key = f"taxonomy_{taxonomy_number}"
        taxonomy_value = str(part.get(taxonomy_key, "")).strip()
        if taxonomy_value != "":
            taxonomy.append({"level": taxonomy_number, "value": taxonomy_value})

    pins = []
    pins_dictionary = part.get("pins", {})
    if isinstance(pins_dictionary, dict):
        used_pin_keys = []
        for pin_number in range(0, 100):
            pin_key = f"pin_{pin_number}"
            if pin_key in pins_dictionary:
                pin = pins_dictionary[pin_key]
                pins.append(
                    {
                        "number": str(pin.get("number", pin_number)),
                        "name": str(pin.get("name", f"pin {pin_number}")),
                        "type": str(pin.get("type", "")),
                    }
                )
                used_pin_keys.append(pin_key)
        for pin_key in pins_dictionary:
            if pin_key not in used_pin_keys:
                pin = pins_dictionary[pin_key]
                pins.append(
                    {
                        "number": str(pin.get("number", "")),
                        "name": str(pin.get("name", pin_key)),
                        "type": str(pin.get("type", "")),
                    }
                )

    identifiers = []
    identifier_fields = [
        ["Manufacturer part number", "part_number_manufacturer"],
        ["Generic part number", "part_number_generic"],
        ["MD5 alpha", "md5_6_alpha_upper"],
    ]
    for identifier_field in identifier_fields:
        identifier_value = str(part.get(identifier_field[1], "")).strip()
        if identifier_value != "":
            identifiers.append({"title": identifier_field[0], "value": identifier_value, "url": ""})
    distributors = part.get("distributors", [])
    if isinstance(distributors, list):
        for distributor in distributors:
            if not isinstance(distributor, dict):
                continue
            identifiers.append(
                {
                    "title": distributor.get("title", "Distributor"),
                    "value": distributor.get("part_number", ""),
                    "url": distributor.get("url", ""),
                }
            )

    diagrams = [
        {"title": "Assembly", "svg": f"{DATA_DIRECTORY}/working_svg_assembly.svg", "png": ""},
        {"title": "Outline", "svg": f"{DATA_DIRECTORY}/working_svg_outline.svg", "png": f"{DATA_DIRECTORY}/working_svg_outline.png"},
        {"title": "Part ID", "svg": f"{DATA_DIRECTORY}/working_svg_part_id.svg", "png": f"{DATA_DIRECTORY}/working_svg_part_id.png"},
        {"title": "MD5 alpha", "svg": f"{DATA_DIRECTORY}/working_svg_md5_6_alpha.svg", "png": f"{DATA_DIRECTORY}/working_svg_md5_6_alpha.png"},
        {"title": "BIP 39 words", "svg": f"{DATA_DIRECTORY}/working_svg_bip_39_3_word.svg", "png": f"{DATA_DIRECTORY}/working_svg_bip_39_3_word.png"},
        {"title": "Square summary", "svg": f"{DATA_DIRECTORY}/working_svg_square.svg", "png": f"{DATA_DIRECTORY}/working_svg_square.png"},
        {"title": "Dimensions", "svg": f"{DATA_DIRECTORY}/working_svg_dimensioned.svg", "png": f"{DATA_DIRECTORY}/working_svg_dimensioned.png"},
        {"title": "Dimensions with labels", "svg": f"{DATA_DIRECTORY}/working_svg_dimensioned_titles.svg", "png": f"{DATA_DIRECTORY}/working_svg_dimensioned_titles.png"},
    ]
    is_connector = part.get("taxonomy_2", "") == "connector"
    if is_connector:
        connector_view_diagrams = [
            {"title": "Top view", "svg": f"{DATA_DIRECTORY}/working_svg_top.svg", "png": f"{DATA_DIRECTORY}/working_svg_top.png"},
            {"title": "Bottom view", "svg": f"{DATA_DIRECTORY}/working_svg_bottom.svg", "png": f"{DATA_DIRECTORY}/working_svg_bottom.png"},
            {"title": "Side view", "svg": f"{DATA_DIRECTORY}/working_svg_side.svg", "png": f"{DATA_DIRECTORY}/working_svg_side.png"},
        ]
        for connector_view_diagram in connector_view_diagrams:
            diagrams.append(connector_view_diagram)

    for diagram in diagrams:
        png_filename = diagram.get("png", "")
        if png_filename != "":
            diagram["preview"] = png_filename.replace(".png", "_300.png")
        else:
            diagram["preview"] = diagram["svg"]

    file_previews = [
        {"title": "Pinout drawing", "preview": f"{DATA_DIRECTORY}/working_svg_square_pins_300.png"},
    ]
    for diagram in diagrams:
        preview_filename = diagram.get("preview", "")
        if preview_filename.endswith("_300.png"):
            file_previews.append(
                {
                    "title": diagram["title"],
                    "preview": preview_filename,
                }
            )

    component_type = str(part.get("taxonomy_2", "component")).replace("_", " ")
    package_name = str(part.get("taxonomy_3", "")).replace("_", " ")
    if part.get("taxonomy_2", "") == "diode":
        package_name = str(part.get("taxonomy_4", "")).replace("_", " ")
    dimensions = part.get("dimensions_mm", {})
    dimension_text = ""
    if isinstance(dimensions, dict):
        length = dimensions.get("length", "")
        width = dimensions.get("width", "")
        if length != "" and width != "":
            dimension_text = f"{length} × {width} mm"

    taxonomy_family = str(part.get("taxonomy_1", "electronic")).replace("_", " ")
    summary_sentences = [
        f"{part.get('name_short', part.get('name_proper', 'This part'))} is an OOMP {taxonomy_family} {component_type} definition."
    ]
    if package_name != "":
        summary_sentences.append(f"It uses the {package_name} package or form factor.")
    if dimension_text != "":
        summary_sentences.append(f"Its nominal drawing size is {dimension_text}.")
    if len(pins) > 0:
        summary_sentences.append(f"The definition includes {len(pins)} documented pins.")

    quick_facts = [
        {"title": "OOMP ID", "value": part.get("name", "")},
        {"title": "Type", "value": component_type.title()},
    ]
    if package_name != "":
        quick_facts.append({"title": "Package / style", "value": package_name})
    if dimension_text != "":
        quick_facts.append({"title": "Nominal size", "value": dimension_text})
    if len(pins) > 0:
        quick_facts.append({"title": "Documented pins", "value": len(pins)})

    part_name = part.get("name", "")
    has_datasheet = os.path.isfile(
        os.path.join(os.path.dirname(__file__), "parts", part_name, DATA_DIRECTORY, "datasheet.pdf")
    )
    file_copies = part.get("file_copy", [])
    if isinstance(file_copies, list):
        for file_copy in file_copies:
            if not isinstance(file_copy, dict):
                continue
            file_destination = str(file_copy.get("file_destination", "")).replace("\\", "/")
            if file_destination.lower().endswith("datasheet.pdf"):
                source_file = str(file_copy.get("file_source", ""))
                if not os.path.isabs(source_file):
                    source_file = os.path.join(os.path.dirname(__file__), source_file)
                if os.path.isfile(source_file):
                    has_datasheet = True

    main_image = {
        "title": "Pinout",
        "svg": f"{DATA_DIRECTORY}/working_svg_square_pins.svg",
        "png": f"{DATA_DIRECTORY}/working_svg_square_pins.png",
        "preview": f"{DATA_DIRECTORY}/working_svg_square_pins_300.png",
    }
    if is_connector:
        main_image = {
            "title": "Top view",
            "svg": f"{DATA_DIRECTORY}/working_svg_top.svg",
            "png": f"{DATA_DIRECTORY}/working_svg_top.png",
            "preview": f"{DATA_DIRECTORY}/working_svg_top_300.png",
        }
    if part.get("taxonomy_2", "") == "mounting_hole":
        main_image = {
            "title": "Mounting hole",
            "svg": f"{DATA_DIRECTORY}/working_svg_outline.svg",
            "png": f"{DATA_DIRECTORY}/working_svg_outline.png",
            "preview": f"{DATA_DIRECTORY}/working_svg_outline_300.png",
        }

    part["part_page"] = {
        "oomp_id": part_name,
        "taxonomy": taxonomy,
        "pins": pins,
        "identifiers": identifiers,
        "diagrams": diagrams,
        "file_previews": file_previews,
        "main_image": main_image,
        "summary": " ".join(summary_sentences),
        "quick_facts": quick_facts,
        "has_datasheet": has_datasheet,
        "repository_url": f"https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts/{part_name}",
        "navigation_link": working_oomp_metadata.navigation_link_for_part(part),
        "datasheet_path": f"{DATA_DIRECTORY}/datasheet.pdf",
    }
    return part


def add_part_build_actions(part, count):
    """Add the deterministic SVG, PNG-preview, and README preparation block."""
    library_actions = [
        {
            "command": "run_python",
            "file_python": "kicad_agents/kicad_library_agent.py",
            "file_output": f"{DATA_DIRECTORY}/kicad/manifest.yaml",
            "description": "Copy official KiCad masters into per-part OOMP symbols and verified soldering footprint variants.",
            "timeout": "600",
        }
    ]
    count += 1
    part[f"oomlout_ai_roboclick_{count}"] = {
        "actions": library_actions,
        "description": "Install KiCad master data for this part.",
        "file_test": f"{DATA_DIRECTORY}/kicad/manifest.yaml",
        "retries_until_complete": 0,
    }
    file_copies = part.get("file_copy", [])
    if len(file_copies) > 0:
        copy_actions = []
        last_copy_destination = ""
        for file_copy in file_copies:
            if not isinstance(file_copy, dict):
                continue
            file_destination = os.path.join(
                DATA_DIRECTORY,
                os.path.basename(str(file_copy.get("file_destination", ""))),
            ).replace("\\", "/")
            copy_actions.append(
                {
                    "command": "file_copy",
                    "file_source": file_copy.get("file_source", ""),
                    "file_destination": file_destination,
                    "exit_on_missing": True,
                    "delete_before_copy": True,
                }
            )
            last_copy_destination = file_destination
        if len(copy_actions) > 0:
            count += 1
            part[f"oomlout_ai_roboclick_{count}"] = {
                "actions": copy_actions,
                "description": "Copy part-specific source files into the working data directory.",
                "file_test": last_copy_destination,
                "retries_until_complete": 0,
            }

    component_actions = [
        {
            "command": "run_python",
            "file_python": "kicad_agents/component_svg_action.py",
            "file_output": f"{DATA_DIRECTORY}/working_svg_assembly.svg",
            "description": "Generate this component's standard SVG and PNG diagrams with working_svg.py.",
            "part_id": part.get("name", ""),
            "regenerate_pngs": as_boolean(part.get("regenerate_pngs", False)),
            "timeout": "600",
        }
    ]
    used_destinations = []
    regenerate_pngs = as_boolean(part.get("regenerate_pngs", False))
    main_image = part.get("part_page", {}).get("main_image", {})
    main_png = main_image.get("png", "")
    main_preview = main_image.get("preview", "")
    if main_png != "" and main_preview != "":
        component_actions.append(
            {
                "command": "image_resize",
                "file_source": main_png,
                "file_destination": main_preview,
                "maximum_dimension": 300,
                "allow_upscale": False,
                "resample": "lanczos",
                "regenerate_pngs": regenerate_pngs,
            }
        )
        used_destinations.append(main_preview)

    diagrams = list(part.get("part_page", {}).get("diagrams", []))
    # The pinout is also offered in Files when a connector top view or a
    # mounting-hole outline is the hero. Always generate that preview too.
    diagrams.append({
        "png": f"{DATA_DIRECTORY}/working_svg_square_pins.png",
        "preview": f"{DATA_DIRECTORY}/working_svg_square_pins_300.png",
    })
    for diagram in diagrams:
        png_filename = diagram.get("png", "")
        preview_filename = diagram.get("preview", "")
        if png_filename != "" and preview_filename != "" and preview_filename not in used_destinations:
            component_actions.append(
                {
                    "command": "image_resize",
                    "file_source": png_filename,
                    "file_destination": preview_filename,
                    "maximum_dimension": 300,
                    "allow_upscale": False,
                    "resample": "lanczos",
                    "regenerate_pngs": regenerate_pngs,
                }
            )
            used_destinations.append(preview_filename)

    if len(component_actions) > 0:
        count += 1
        part[f"oomlout_ai_roboclick_{count}"] = {
            "actions": component_actions,
            "description": "Build component diagrams and proportional 300-pixel README previews with deterministic Python actions.",
            "file_test": f"{DATA_DIRECTORY}/working_svg_square_pins_300.png",
            "retries_until_complete": 0,
        }
    return count


def add_project_actions(part, count):
    """Add the deterministic, always-run source and diagram project actions."""
    regenerate_pngs = as_boolean(part.get("regenerate_pngs", False))
    project_action_fields = [
        "project_github_user",
        "project_github_repository",
        "project_github_url",
        "project_git_url",
        "project_git_ref",
        "project_sparse_checkout",
        "project_version",
        "project_board",
        "project_board_name",
        "project_board_url",
        "project_file_folder",
        "project_file_basename",
        "project_file_path",
        "project_file_extensions",
        "project_match_overrides",
        "project_match_blocked",
        "project_review_notes",
    ]

    git_action = {
        "command": "run_python",
        "file_python": "kicad_agents/project_git_action.py",
        "description": "Clone or update the Git project and copy its selected KiCad files into the project part.",
        "timeout": "600",
    }
    for project_action_field in project_action_fields:
        git_action[project_action_field] = copy.deepcopy(part.get(project_action_field, ""))

    count += 1
    part[f"oomlout_ai_roboclick_{count}"] = {
        "actions": [git_action],
        "file_test": f"{DATA_DIRECTORY}/original/manifest.yaml",
        "retries_until_complete": 0,
    }

    project_compile_action = {
        "command": "run_python",
        "file_python": "kicad_agents/project_readme_action.py",
        "file_output": f"{DATA_DIRECTORY}/generated_data/src/board_pins.png",
        "description": "Extract KiCad data and rebuild the project README, board SVGs, pin-labelled PNG, and mechanical layer.",
        "parts_directory": "parts",
        "regenerate_pngs": regenerate_pngs,
        "timeout": "1200",
    }
    for project_action_field in project_action_fields:
        project_compile_action[project_action_field] = copy.deepcopy(part.get(project_action_field, ""))

    board_preview_actions = []
    board_png_names = [
        "board",
        "board_pins",
        "board_bottom",
        "board_pins_bottom",
        "board_mechanical",
    ]
    for board_png_name in board_png_names:
        board_preview_actions.append(
            {
                "command": "image_resize",
                "file_source": f"{DATA_DIRECTORY}/generated_data/src/{board_png_name}.png",
                "file_destination": f"{DATA_DIRECTORY}/generated_data/src/{board_png_name}_300.png",
                "maximum_dimension": 300,
                "allow_upscale": False,
                "resample": "lanczos",
                "regenerate_pngs": regenerate_pngs,
            }
        )

    count += 1
    part[f"oomlout_ai_roboclick_{count}"] = {
        "actions": [
            {
                "command": "run_python",
                "file_python": "kicad_agents/interactive_html_bom_action.py",
                "file_output": f"{DATA_DIRECTORY}/interactivehtmlbom/generation_status.yaml",
                "description": "Generate a self-contained InteractiveHtmlBom page without opening a browser.",
                "timeout": "1200",
            }
        ],
        "file_test": f"{DATA_DIRECTORY}/interactivehtmlbom/generation_status.yaml",
        "retries_until_complete": 0,
    }
    count += 1
    part[f"oomlout_ai_roboclick_{count}"] = {
        "actions": [project_compile_action] + board_preview_actions,
        "file_test": f"{DATA_DIRECTORY}/generated_data/src/board_mechanical_300.png",
        "retries_until_complete": 0,
    }
    count += 1
    part[f"oomlout_ai_roboclick_{count}"] = {
        "actions": [{
            "command": "run_python",
            "file_python": "kicad_agents/project_usage_action.py",
            "description": "Refresh Used in projects metadata and part README links from all confirmed project matches.",
            "parts_directory": "parts",
            "timeout": "600",
        }],
        "file_test": "",
        "retries_until_complete": 0,
    }
    count += 1
    conversion_action = {
        "command": "run_python",
        "file_python": "kicad_agents/kicad_project_action.py",
        "file_output": f"{DATA_DIRECTORY}/oomp_design/conversion_report.yaml",
        "description": "Preserve original KiCad files, package local libraries, and replace only verified unchanged defaults in an OOMP design copy.",
        "parts_directory": "parts",
        "project_match_overrides": copy.deepcopy(part.get("project_match_overrides", {})),
        "project_file_basename": part.get("project_file_basename", ""),
        "timeout": "1200",
    }
    part[f"oomlout_ai_roboclick_{count}"] = {
        "actions": [conversion_action], "file_test": "", "retries_until_complete": 0,
    }
    return count

def main(**kwargs):
    load_parts(**kwargs)

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    create_generic(**kwargs)

def create_generic(**kwargs):
    print(f"  loading parts from part_source")
    make_files = kwargs.get("make_files", True)
    things = {}    
    
    #load parts from parts_source directory
    directory_source = "parts_source"
    import os
    if not os.path.exists(directory_source):
        print(f"      directory {directory_source} does not exist, creating it")
        #create it
        os.makedirs(directory_source)
    directories = os.listdir(directory_source)
    for directory  in directories:
        directory_full = f"{directory_source}/{directory}"
        filenames = os.listdir(f"{directory_full}")
        for filename in filenames:
            import yaml
            #go through directories and load working.yaml files
            # only load .yaml files
            if "working.yaml" in filename:
                file_path = os.path.join(directory_full, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = yaml.safe_load(file)
                    thing_details = {}
                    for deet in data:
                        thing_details[deet] = data[deet]
                    things[directory] = thing_details
    
    
    parts = []
    from kicad_agents.project_usage_action import build_usage_index, usage_for_part, apply_usage
    usage_parts_directory = "parts" if make_files is True or make_files is False else str(make_files)
    usage_index, unavailable_projects = build_usage_index(usage_parts_directory)

    for thing in things:
        current = things[thing]                
        #name stuff        
        part = copy.deepcopy(current)
        part["regenerate_pngs"] = as_boolean(kwargs.get("regenerate_pngs", False))
        
        part["name"] = thing
        part["name_space"] = thing.replace("_", " ")
        part["name_proper"] = part["name_space"].title()
        name_proper = part["name_proper"]
        part["name_upper"] = part["name_space"].upper()
        working_oomp_metadata.add_readable_metadata([part])

        is_project_part = (
            part.get("taxonomy_1", "") == "oomp"
            and part.get("taxonomy_2", "") == "project"
        )
        is_navigation_part = part.get("taxonomy_1", "") == "navigation"
        if not is_project_part and not is_navigation_part:
            previous_usage = {}
            previous_file = os.path.join(usage_parts_directory, thing, "working.yaml")
            if unavailable_projects and os.path.isfile(previous_file):
                with open(previous_file, encoding="utf-8") as previous_input:
                    previous_usage = yaml.safe_load(previous_input) or {}
            apply_usage(part, usage_for_part(thing, previous_usage, usage_index, unavailable_projects))
            import working_oomp_populate_svg
            working_oomp_populate_svg.add_svg_details(part)
            import working_oomp_populate_kicad
            working_oomp_populate_kicad.add_kicad_details(part)
            add_part_page_details(part)
        else:
            part["name_short"] = part.get("name_readable", part.get("name_proper", thing))
        
        folder = oomlout_roboclick.get_directory(part)   
        part["directory"] = folder  
        url_chat = oomlout_roboclick.get_url(part)   
        part["url_chat"] = url_chat
        files_to_trace = []
        count = 0

        #mode_ai_wait = "fast"
        mode_ai_wait = "slow"

        #load working_manual and add it to surrent if availabe
        if True:
            directory_manual = f"{part['directory']}/working_manual.yaml"
            if os.path.exists(directory_manual):
                with open(directory_manual, 'r', encoding='utf-8') as file:
                    data = yaml.safe_load(file)
                    for deet in data:
                        part[deet] = data[deet]

        #working with variables
        if True:
            if "content" in part:
                content_string = ", ".join(part["content"])
                print(f"      content: {content_string}")
                part["content_string"] = content_string

        #icon
        if False:
            count += 1     
            icon_detail = f"make {name_proper} cute"
            oomp_helper.add_icon(part=part, count=count, mode_ai_wait=mode_ai_wait, icon_detail=icon_detail)

        
        # Optional illustrative artwork is deliberately opt-in.  Core OOMP
        # records, diagrams, previews, and documentation never require an LLM.
        test_image_chibi = as_boolean(kwargs.get("enable_ai_assets", False))
        if test_image_chibi and not is_navigation_part:
            content_string = part.get("content_string", "")    
            count += 1
            chibi_detail = f"make {name_proper} cute"
            oomp_helper.add_image_chibi(part=part, count=count, mode_ai_wait=mode_ai_wait, chibi_detail=chibi_detail)       

        #image_from_directory
        if False:
            count += 1
            directory_prompt = f"roboclick\\prompt_1"
            file_name_image = "image_main.png"
            oomp_helper.add_image_from_prompt_directory(part=part, count=count, prompt_folder=directory_prompt, file_name=file_name_image, generate_prompt="", mode_ai_wait=mode_ai_wait)


        # all images
        test_image_all = False
        if test_image_all:
            content_string = part.get("content_string", "")    
            count += 1
            image_detail = f"make {name_proper} cute"
            oomp_helper.add_all_default_prompt_images(part=part, count=count, mode_ai_wait=mode_ai_wait, image_detail=image_detail)

        #folder_project = "helen_personal_chart_bribe_bank"

        #jinja_template replace
        if not is_project_part and not is_navigation_part:
            count = add_part_build_actions(part, count)
            templates = []
            templates.append(
                {
                    "template_folder": "source_file\\template_jinja\\oomp_category\\template_jinja_markdown",
                    "template_file": "working.md.j2",
                    "output_filename": "README.md",
                    "file_test": "",
                    "convert_to_pdf": False,
                    "convert_to_png": False,
                }
            )
            #templates.append({"template_folder": "source_file\\template_jinja\\template_jinja_postcard_image_main_oomlout_152_4_mm_101_6_mm", "output_filename": "postcard_oomp.svg"})
            convert_to_pdf = False
            convert_to_png = False
            count = oomp_helper.add_jinja_template(part=part, templates=templates, mode_ai_wait=mode_ai_wait, count=count, convert_to_pdf=convert_to_pdf, convert_to_png=convert_to_png)

        if is_navigation_part:
            navigation_templates = [
                {
                    "template_folder": "source_file\\template_jinja\\navigation",
                    "template_file": "part.md.j2",
                    "output_filename": "README.md",
                    "file_test": "",
                    "convert_to_pdf": False,
                    "convert_to_png": False,
                },
                {
                    "template_folder": "source_file\\template_jinja\\navigation",
                    "template_file": "canonical.md.j2",
                    "output_filename": part.get("navigation", {}).get(
                        "canonical_output_from_part", "../../navigation/README.md"
                    ),
                    "file_test": "",
                    "convert_to_pdf": False,
                    "convert_to_png": False,
                },
            ]
            count = oomp_helper.add_jinja_template(
                part=part,
                templates=navigation_templates,
                mode_ai_wait=mode_ai_wait,
                count=count,
                convert_to_pdf=False,
                convert_to_png=False,
            )

        if is_project_part:
            count = add_project_actions(part, count)
        #prompt bubble letter        
        if False:
            count = oomp_helper.add_image(
                part=part,
                folder_project=folder_project,
                files_to_trace=files_to_trace,
                mode_ai_wait=mode_ai_wait,
                count=count,
            )

        #prompt image theme
        if False:
            count = oomp_helper.add_prompt_image(
                part=part,
                folder_project=folder_project,
                prompt_folder="prompt_image_main_1",
                file_name="image_main_1.png",
                files_to_trace=files_to_trace,
                mode_ai_wait=mode_ai_wait,
                count=count,
            )
        #value
        if False:
            count = oomp_helper.add_value_images(
                part=part,
                folder_project=folder_project,
                files_to_trace=files_to_trace,
                mode_ai_wait=mode_ai_wait,
                count=count,
            )
            

        #cover_background
        #prompt image
        if False:
            count = oomp_helper.add_cover_background(
                part=part,
                folder_project=folder_project,
                files_to_trace=files_to_trace,
                mode_ai_wait=mode_ai_wait,
                count=count,
            )
       
        #internal border
        #prompt image
        if False:
            count = oomp_helper.add_prompt_image(
                part=part,
                folder_project=folder_project,
                prompt_folder="prompt_inside_border_1",
                file_name="image_inside_border.png",
                files_to_trace=files_to_trace,
                mode_ai_wait=mode_ai_wait,
                count=count,
            )

        #logo back
        #prompt image
        if False:
            count = oomp_helper.add_prompt_image(
                part=part,
                folder_project=folder_project,
                prompt_folder="prompt_logo_back_1",
                file_name="image_logo_back.png",
                files_to_trace=files_to_trace,
                mode_ai_wait=mode_ai_wait,
                count=count,
            )

        #trace
        if False:  
            count = oomp_helper.trace_files(
                part=part,
                files_to_trace=files_to_trace,
                mode_ai_wait=mode_ai_wait,
                count=count,
            )

        #make_card
        if False:
            count = oomp_helper.make_card(part=part, folder_project=folder_project, count=count)

        #research
        if False:
            count = oomp_helper.add_research(
                part=part,
                folder_project=folder_project,
                mode_ai_wait=mode_ai_wait,
                count=count,
            )


        parts.append(part)
    



    # Keep filtered population runs small enough for one component family.
    # The shared OOMP helper reads this simple string before writing files.
    oomp.add_part_filter = kwargs.get("filter", "")
    add_parts_kwargs = copy.deepcopy(kwargs)
    # filter controls which records are written; it is not component data.
    # Removing it here prevents the shared helper from copying it into YAML.
    add_parts_kwargs.pop("filter", None)
    # Keep generation linear and deterministic.  The upstream helper starts a
    # thread per item and returns before all working.yaml files are complete,
    # which made full-regeneration actions race their own output.
    for part in parts:
        part_filters = kwargs.get("filter", "")
        if not isinstance(part_filters, list):
            part_filters = [part_filters]
        include_part = False
        for part_filter in part_filters:
            if part_filter in part["name"]:
                include_part = True
        if not include_part:
            continue
        part_details = copy.deepcopy(part)
        part_details.update(copy.deepcopy(add_parts_kwargs))
        # The shared helper still supplies IDs and hashes, but its repository
        # links are from v1. Normalize the returned record before writing once.
        part_details["make_files"] = False
        oomp.add_part_filter = ""  # Filtering is handled explicitly above.
        generated_part = oomp.add_part(**part_details)
        if generated_part is None:
            continue
        generated_id = generated_part.get("id", "")
        if generated_id == "":
            continue
        repository_url = (
            "https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts/"
            + generated_id
        )
        generated_part["link_github"] = repository_url
        generated_part["link_main"] = repository_url
        generated_part["link_redirect"] = repository_url
        if make_files:
            generated_parts_directory = "parts" if make_files is True else str(make_files)
            generated_working_file = os.path.join(
                generated_parts_directory, generated_id, "working.yaml"
            )
            generated_working = copy.deepcopy(generated_part)
            generated_working.pop("make_files", None)
            generated_working.pop("counter", None)
            os.makedirs(os.path.dirname(generated_working_file), exist_ok=True)
            with open(generated_working_file, "w", encoding="utf-8") as working_file:
                yaml.safe_dump(
                    generated_working,
                    working_file,
                    sort_keys=True,
                    allow_unicode=True,
                )



if __name__ == "__main__":
    # run the function
    load_parts()    
    
