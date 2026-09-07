"""Generate the taxonomy navigation tree in one dedicated pass."""

import argparse
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

import working_oomp_metadata

REPOSITORY_ROOT = Path(__file__).resolve().parent
NAVIGATION_ROOT = REPOSITORY_ROOT / "navigation"
TEMPLATE_DIR = REPOSITORY_ROOT / "source_file" / "template_jinja" / "navigation"


def _collect_part_rows(parts_directory: Path, filter_text: str = ""):
    parts = []
    for part_directory in sorted(parts_directory.iterdir(), key=lambda path: path.name.lower()):
        if not part_directory.is_dir():
            continue
        if filter_text and filter_text not in part_directory.name:
            continue
        working_file = part_directory / "working.yaml"
        if not working_file.is_file():
            continue
        working = yaml.safe_load(working_file.read_text(encoding="utf-8")) or {}
        if not isinstance(working, dict):
            continue
        if str(working.get("taxonomy_1", "")) == "navigation":
            continue
        taxonomy = []
        for index in range(1, 16):
            value = str(working.get(f"taxonomy_{index}", "")).strip()
            if value:
                taxonomy.append(value)
        if taxonomy == []:
            continue
        parts.append(working)
    return parts


def _render_navigation_page(navigation_data):
    template = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        trim_blocks=True,
        lstrip_blocks=True,
    ).get_template("canonical.md.j2")
    return template.render(p={"navigation": navigation_data})


def generate(filter_text=""):
    parts_directory = REPOSITORY_ROOT / "parts"
    if not parts_directory.exists():
        raise FileNotFoundError(f"Missing parts directory: {parts_directory}")

    source_parts = _collect_part_rows(parts_directory, filter_text=filter_text)
    navigation_parts = working_oomp_metadata.add_navigation_parts(list(source_parts))

    # Only a full (unfiltered) build may sweep existing pages: a filtered run
    # regenerates just its own pages and must leave other categories intact.
    if NAVIGATION_ROOT.exists() and filter_text == "":
        for path in sorted(NAVIGATION_ROOT.rglob("README.md"), key=lambda item: len(item.relative_to(NAVIGATION_ROOT).parts), reverse=True):
            path.unlink()
        for path in sorted(NAVIGATION_ROOT.rglob("*"), key=lambda item: (len(item.relative_to(NAVIGATION_ROOT).parts), str(item)), reverse=True):
            if path.is_dir() and not any(path.iterdir()):
                path.rmdir()
    NAVIGATION_ROOT.mkdir(parents=True, exist_ok=True)

    for part in navigation_parts:
        category_path = part.get("navigation", {}).get("category_path", [])
        relative_path = Path(working_oomp_metadata._navigation_file_path(category_path).replace("navigation/", ""))
        page_path = NAVIGATION_ROOT / relative_path
        page_path.parent.mkdir(parents=True, exist_ok=True)
        page_path.write_text(_render_navigation_page(part["navigation"]), encoding="utf-8")

    return NAVIGATION_ROOT


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", default="", help="Optional part prefix to limit the navigation build")
    arguments = parser.parse_args()
    generate(filter_text=arguments.filter)


if __name__ == "__main__":
    main()
