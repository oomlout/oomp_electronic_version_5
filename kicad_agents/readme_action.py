"""Run only deterministic README/navigation Jinja actions for generated parts."""

import argparse
from functools import lru_cache
from pathlib import Path

import oomlout_roboclick
import yaml
from jinja2 import Environment, FileSystemLoader
from robo_roboclick import fix_search_replace_special_characters

if __package__:
    from .part_file_table import file_table, local_files
else:
    from part_file_table import file_table, local_files


TEMPLATES = Path(__file__).resolve().parents[1] / "source_file/template_jinja"
COMPONENT_TEMPLATE = "oomp_category/template_jinja_markdown/working.md.j2"
HEADER_TEMPLATE = "header_reference/working.md.j2"


@lru_cache(maxsize=2)
def _template(name):
    header = name == HEADER_TEMPLATE
    return Environment(loader=FileSystemLoader(TEMPLATES), trim_blocks=header,
                       lstrip_blocks=header).get_template(name)


def render_component(directory, working, template_name):
    paths = local_files(directory)
    part = {key: value for key, value in working.items() if not key.startswith("oomlout_")}
    if template_name == COMPONENT_TEMPLATE:
        # Match Roboclick's text encoding for generated component descriptions.
        part = fix_search_replace_special_characters(part)
        page = part["part_page"]
        if page["main_image"]["svg"] not in paths:
            page["main_image"]["svg"] = ""
        page["has_datasheet"] = page["datasheet_path"] in paths
        if not (directory / page["navigation_link"]).is_file():
            page["navigation_link"] = ""
    content = _template(template_name).render(p=part, file_table=file_table(paths))
    (directory / "README.md").write_text(content, encoding="utf-8")


def regenerate_readmes(parts_directory="parts", filter_text="", part_ids=None, output_names=None):
    parts_directory = Path(parts_directory).resolve()
    discovered_actions = None
    rendered = 0
    for part_directory in sorted(parts_directory.iterdir(), key=lambda path: path.name.lower()):
        if not part_directory.is_dir() or filter_text not in part_directory.name:
            continue
        if part_ids is not None and part_directory.name not in part_ids:
            continue
        working_file = part_directory / "working.yaml"
        if not working_file.is_file():
            continue
        workings = yaml.load(working_file.read_bytes(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader)) or {}
        for mode_name, mode_details in workings.items():
            if not str(mode_name).startswith("oomlout_") or not isinstance(mode_details, dict):
                continue
            for action in mode_details.get("actions", []):
                if not isinstance(action, dict) or action.get("command") != "text_jinja_template":
                    continue
                if output_names is not None and action.get("file_output") not in output_names:
                    continue
                template_path = action.get("file_template", "").replace("\\", "/")
                template_name = template_path.split("source_file/template_jinja/")[-1]
                if action.get("file_output") == "README.md" and template_name in (HEADER_TEMPLATE, COMPONENT_TEMPLATE):
                    render_component(part_directory, workings, template_name)
                    rendered += 1
                    continue
                if discovered_actions is None:
                    discovered_actions = oomlout_roboclick.build_action_lookup()
                result = oomlout_roboclick.run_single_action(
                    action=action,
                    directory=str(part_directory),
                    directory_absolute=str(part_directory),
                    file_action=str(working_file),
                    _discovered_actions=discovered_actions,
                )
                if result in ["exit", "exit_no_tab"]:
                    raise RuntimeError(f"README action failed for {part_directory.name}: {result}")
                rendered += 1
    print(f"rendered {rendered} README/navigation files")
    return rendered


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parts-dir", default="parts")
    parser.add_argument("--filter", default="")
    parser.add_argument("--parts-only", action="store_true", help="Render only the part README.md files.")
    arguments = parser.parse_args()
    regenerate_readmes(arguments.parts_dir, filter_text=arguments.filter,
                       output_names={"README.md"} if arguments.parts_only else None)


if __name__ == "__main__":
    main()
