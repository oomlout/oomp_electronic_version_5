import oomp
import oomp_helper
import copy
import oomlout_roboclick
import os


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
        ["LCSC", "part_number_lcsc"],
        ["MD5 alpha", "md5_6_alpha_upper"],
    ]
    for identifier_field in identifier_fields:
        identifier_value = str(part.get(identifier_field[1], "")).strip()
        if identifier_value != "":
            identifiers.append({"title": identifier_field[0], "value": identifier_value})

    diagrams = [
        {"title": "Assembly", "svg": "working_svg_assembly.svg", "png": ""},
        {"title": "Outline", "svg": "working_svg_outline.svg", "png": "working_svg_outline.png"},
        {"title": "Part ID", "svg": "working_svg_part_id.svg", "png": "working_svg_part_id.png"},
        {"title": "MD5 alpha", "svg": "working_svg_md5_6_alpha.svg", "png": "working_svg_md5_6_alpha.png"},
        {"title": "BIP 39 words", "svg": "working_svg_bip_39_3_word.svg", "png": "working_svg_bip_39_3_word.png"},
        {"title": "Square summary", "svg": "working_svg_square.svg", "png": "working_svg_square.png"},
        {"title": "Dimensions", "svg": "working_svg_dimensioned.svg", "png": "working_svg_dimensioned.png"},
        {"title": "Dimensions with labels", "svg": "working_svg_dimensioned_titles.svg", "png": "working_svg_dimensioned_titles.png"},
    ]

    for diagram in diagrams:
        png_filename = diagram.get("png", "")
        if png_filename != "":
            diagram["preview"] = png_filename.replace(".png", "_300.png")
        else:
            diagram["preview"] = diagram["svg"]

    file_previews = [
        {"title": "Pinout drawing", "preview": "working_svg_square_pins_300.png"},
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
    dimensions = part.get("dimensions_mm", {})
    dimension_text = ""
    if isinstance(dimensions, dict):
        length = dimensions.get("length", "")
        width = dimensions.get("width", "")
        if length != "" and width != "":
            dimension_text = f"{length} × {width} mm"

    summary_sentences = [
        f"{part.get('name_short', part.get('name_proper', 'This part'))} is an OOMP electronic {component_type} definition."
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
        os.path.join(os.path.dirname(__file__), "parts", part_name, "datasheet.pdf")
    )
    file_copies = part.get("file_copy", [])
    if isinstance(file_copies, list):
        for file_copy in file_copies:
            if not isinstance(file_copy, dict):
                continue
            file_destination = str(file_copy.get("file_destination", "")).replace("\\", "/")
            if file_destination.lower().endswith("datasheet.pdf"):
                has_datasheet = True

    part["part_page"] = {
        "oomp_id": part_name,
        "taxonomy": taxonomy,
        "pins": pins,
        "identifiers": identifiers,
        "diagrams": diagrams,
        "file_previews": file_previews,
        "main_image": {
            "title": "Pinout",
            "svg": "working_svg_square_pins.svg",
            "png": "working_svg_square_pins.png",
            "preview": "working_svg_square_pins_300.png",
        },
        "summary": " ".join(summary_sentences),
        "quick_facts": quick_facts,
        "has_datasheet": has_datasheet,
        "repository_url": f"https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts/{part_name}",
    }
    return part


def add_part_preview_actions(part, count):
    """Add one always-run block that makes 300-pixel README previews."""
    actions = []
    main_image = part.get("part_page", {}).get("main_image", {})
    main_png = main_image.get("png", "")
    main_preview = main_image.get("preview", "")
    if main_png != "" and main_preview != "":
        actions.append(
            {
                "command": "image_resize",
                "file_source": main_png,
                "file_destination": main_preview,
                "maximum_dimension": 300,
                "allow_upscale": False,
                "resample": "lanczos",
            }
        )

    diagrams = part.get("part_page", {}).get("diagrams", [])
    for diagram in diagrams:
        png_filename = diagram.get("png", "")
        preview_filename = diagram.get("preview", "")
        if png_filename != "" and preview_filename != "":
            actions.append(
                {
                    "command": "image_resize",
                    "file_source": png_filename,
                    "file_destination": preview_filename,
                    "maximum_dimension": 300,
                    "allow_upscale": False,
                    "resample": "lanczos",
                }
            )

    if len(actions) > 0:
        count += 1
        part[f"oomlout_ai_roboclick_{count}"] = {
            "actions": actions,
            "description": "Build proportional 300-pixel previews for the generated part README.",
            "file_test": "",
            "retries_until_complete": 0,
        }
    return count


def add_project_actions(part, count):
    """Add the deterministic, always-run source and diagram project actions."""
    project_action_fields = [
        "project_github_user",
        "project_github_repository",
        "project_github_url",
        "project_git_url",
        "project_git_ref",
        "project_version",
        "project_file_folder",
        "project_file_basename",
        "project_file_path",
        "project_file_extensions",
        "project_match_overrides",
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
        "file_test": "",
        "retries_until_complete": 0,
    }

    project_compile_action = {
        "command": "run_python",
        "file_python": "kicad_agents/project_readme_action.py",
        "file_output": "generated_data/src/board_pins.png",
        "description": "Extract KiCad data and rebuild the project README, board SVGs, and pin-labelled board PNG.",
        "parts_directory": "parts",
        "timeout": "1200",
    }
    for project_action_field in project_action_fields:
        project_compile_action[project_action_field] = copy.deepcopy(part.get(project_action_field, ""))

    count += 1
    part[f"oomlout_ai_roboclick_{count}"] = {
        "actions": [project_compile_action],
        "file_test": "",
        "retries_until_complete": 0,
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

    for thing in things:
        current = things[thing]                
        #name stuff        
        part = copy.deepcopy(current)
        
        part["name"] = thing
        part["name_space"] = thing.replace("_", " ")
        part["name_proper"] = part["name_space"].title()
        name_proper = part["name_proper"]
        part["name_upper"] = part["name_space"].upper()

        is_project_part = (
            part.get("taxonomy_1", "") == "oomp"
            and part.get("taxonomy_2", "") == "project"
        )
        if not is_project_part:
            import working_oomp_populate_svg
            working_oomp_populate_svg.add_svg_details(part)
            add_part_page_details(part)
        else:
            part["name_short"] = f"{part.get('project_github_user', '')}/{part.get('project_github_repository', '')} {part.get('project_version', 'current')}"
        
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

        
        #image chibi
        test_image_chibi = False
        if test_image_chibi:
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
        if not is_project_part:
            count = add_part_preview_actions(part, count)
            templates = []
            templates.append({"template_folder": "default"})
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
    



    oomp.add_parts(parts, **kwargs)

    #dd file copy
    for part in parts:
        file_copies = part.get("file_copy", [])
        if file_copies != []:
            for file_copy in file_copies:
                directory = part.get("directory", "")
                if directory != "":
                    file_source = f'{file_copy["file_source"]}'
                    file_destination = f'{directory}\\{file_copy["file_destination"]}'
                    import shutil
                    print(f"      copying {file_source} to {file_destination}")
                    try:
                        shutil.copyfile(file_source, file_destination)
                    except Exception as e:
                        print(f"      error copying file: {e}") 

    import time
    time.sleep(2)



if __name__ == "__main__":
    # run the function
    load_parts()    
    
