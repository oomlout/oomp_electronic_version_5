"""Rebuild reverse project references in part YAML and their Jinja READMEs.

Uses only saved, confirmed project matches. No browser, LLM or image generation.
"""

import argparse
import copy
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

import yaml

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

REPOSITORY_PARTS_URL = "https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts"
PAGES_PARTS_URL = "https://oomlout.github.io/oomp_electronic_version_5/parts"


def reference_sort_key(reference):
    return [int(piece) if piece.isdigit() else piece.lower() for piece in re.split(r"(\d+)", reference)]


def build_usage_index(parts_directory="parts"):
    """Return one entry per part/project, plus projects not extracted yet."""
    parts_directory = Path(parts_directory).resolve()
    index = {}
    unavailable = []
    for working_file in sorted(parts_directory.glob("oomp_project_*/working.yaml")):
        project_directory = working_file.parent
        metadata = yaml.safe_load(working_file.read_text(encoding="utf-8")) or {}
        project_file = project_directory / "data" / "generated_data" / "project.json"
        if not project_file.is_file():
            unavailable.append(project_directory.name)
            continue
        # Parse every project before changing any part; invalid JSON must not
        # silently erase previously known usage.
        project = json.loads(project_file.read_text(encoding="utf-8"))
        if not isinstance(project.get("components"), list):
            raise ValueError(f"Missing component list in {project_file}")
        project_id = project_directory.name
        github_url = metadata.get("project_github_url", "")
        entry = {
            "project_id": project_id,
            "name": metadata.get("name_readable") or project_id,
            "version": metadata.get("project_version", "current"),
            "github_url": github_url,
            "board_url": metadata.get("project_board_url") or github_url,
            "oomp_url": f"{REPOSITORY_PARTS_URL}/{quote(project_id)}",
            "board_explorer_url": f"{PAGES_PARTS_URL}/{quote(project_id)}/board_explorer.html",
        }
        placements = {}
        for collection in ["components", "mounting_hole_items"]:
            for component in project.get(collection, []):
                match = component.get("oomp") or {}
                part_id = match.get("oomp_id")
                if match.get("status") != "matched" or match.get("accepted") is False or not part_id:
                    continue
                pcb = component.get("pcb") or {}
                if pcb.get("exclude_from_bom") or str(pcb.get("value", "")).strip().upper() == "DNF":
                    continue
                # Dedicated holes also appear as raw footprints. Count only
                # their classified MH items, not both representations.
                if collection == "components" and pcb.get("is_mounting_hole"):
                    continue
                reference = str(component.get("reference") or "")
                if not reference:
                    continue
                placement = [str(pcb.get("source_file") or ""), reference]
                if part_id not in placements:
                    placements[part_id] = []
                if placement not in placements[part_id]:
                    placements[part_id].append(placement)
        for part_id in sorted(placements):
            usage = copy.deepcopy(entry)
            usage["quantity"] = len(placements[part_id])
            usage["references"] = sorted([item[1] for item in placements[part_id]], key=reference_sort_key)
            index.setdefault(part_id, []).append(usage)
    return index, unavailable


def usage_for_part(part_id, previous, index, unavailable):
    entries = copy.deepcopy(index.get(part_id, []))
    # A temporarily missing extraction is not evidence that a part is unused.
    for old_entry in previous.get("used_in_projects", []):
        if old_entry.get("project_id") in unavailable:
            entries.append(copy.deepcopy(old_entry))
    return sorted(entries, key=lambda entry: entry["project_id"])


def apply_usage(part, entries):
    """Keep the canonical field and saved Jinja action snapshots in sync."""
    targets = [part]
    for key, mode in part.items():
        if not str(key).startswith("oomlout_") or not isinstance(mode, dict):
            continue
        for action in mode.get("actions", []):
            if action.get("command") == "text_jinja_template" and isinstance(action.get("dict_data"), dict):
                targets.append(action["dict_data"])
    for target in targets:
        if entries:
            target["used_in_projects"] = copy.deepcopy(entries)
        else:
            target.pop("used_in_projects", None)


def refresh_project_usage(parts_directory="parts", render_readmes=True):
    parts_directory = Path(parts_directory).resolve()
    index, unavailable = build_usage_index(parts_directory)
    changed = []
    render_ids = []
    for working_file in sorted(parts_directory.glob("*/working.yaml")):
        part_id = working_file.parent.name
        original_text = working_file.read_text(encoding="utf-8")
        if part_id not in index and "used_in_projects:" not in original_text:
            continue
        part = yaml.safe_load(original_text) or {}
        previous = copy.deepcopy(part)
        entries = usage_for_part(part_id, part, index, unavailable)
        apply_usage(part, entries)
        if part != previous:
            working_file.write_text(yaml.safe_dump(part, sort_keys=True, allow_unicode=True), encoding="utf-8")
            changed.append(part_id)
        if entries or previous.get("used_in_projects") or part != previous:
            render_ids.append(part_id)
    if render_readmes and render_ids:
        from kicad_agents.readme_action import regenerate_readmes
        regenerate_readmes(parts_directory, part_ids=render_ids)
    missing_parts = []
    for part_id in sorted(index):
        if not (parts_directory / part_id / "working.yaml").is_file():
            missing_parts.append(part_id)
    return {
        "used_part_count": len(index),
        "project_usage_count": sum(len(entries) for entries in index.values()),
        "updated_part_ids": changed,
        "unavailable_project_ids": unavailable,
        "missing_part_ids": missing_parts,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parts-dir", default="parts")
    parser.add_argument("--no-readmes", action="store_true")
    parser.add_argument("--kwargs", help="JSON supplied by the Roboclick run_python action")
    arguments = parser.parse_args()
    details = json.loads(arguments.kwargs) if arguments.kwargs else {}
    result = refresh_project_usage(
        details.get("parts_directory", arguments.parts_dir),
        render_readmes=not arguments.no_readmes,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
