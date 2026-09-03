"""Run only deterministic README/navigation Jinja actions for generated parts."""

import argparse
from pathlib import Path

import oomlout_roboclick
import yaml


def regenerate_readmes(parts_directory="parts", filter_text=""):
    parts_directory = Path(parts_directory).resolve()
    discovered_actions = oomlout_roboclick.build_action_lookup()
    rendered = 0
    for part_directory in sorted(parts_directory.iterdir(), key=lambda path: path.name.lower()):
        if not part_directory.is_dir() or filter_text not in part_directory.name:
            continue
        working_file = part_directory / "working.yaml"
        if not working_file.is_file():
            continue
        workings = yaml.safe_load(working_file.read_text(encoding="utf-8")) or {}
        for mode_name, mode_details in workings.items():
            if not str(mode_name).startswith("oomlout_") or not isinstance(mode_details, dict):
                continue
            for action in mode_details.get("actions", []):
                if not isinstance(action, dict) or action.get("command") != "text_jinja_template":
                    continue
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
    arguments = parser.parse_args()
    regenerate_readmes(arguments.parts_dir, filter_text=arguments.filter)


if __name__ == "__main__":
    main()
