"""Generate the standard OOMP documentation bundle for a local KiCad project."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from kicad_agents.browser_research_agent import write_browser_research_queue
from kicad_agents.interactive_html_bom_action import generate_interactive_html_bom
from kicad_agents.kicad_processing_agent import process_project
from kicad_agents.project_html_agent import generate_board_explorer
from kicad_agents.project_review_agent import write_lcsc_review
from kicad_agents.project_summary_agent import _make_board_png, generate_project_summary


OUTPUT_DIRECTORY_NAME = "oomp_documentation"
LOCAL_SUMMARY_TEMPLATE = (
    REPOSITORY_ROOT
    / "source_file"
    / "template_jinja"
    / "project_summary"
    / "standalone.md.j2"
)
IGNORED_DIRECTORY_NAMES = {
    ".git",
    ".venv",
    "__pycache__",
    "archive",
    "backup",
    "backups",
    OUTPUT_DIRECTORY_NAME,
}


def _is_ignored(path: Path, source_directory: Path) -> bool:
    try:
        relative_parts = path.resolve().relative_to(source_directory).parts
    except ValueError:
        return True
    return any(
        part.lower() in IGNORED_DIRECTORY_NAMES
        or part.lower().endswith("-backups")
        for part in relative_parts[:-1]
    )


def _pcb_candidates(source_directory: Path) -> list[Path]:
    return sorted(
        path.resolve()
        for path in source_directory.rglob("*.kicad_pcb")
        if path.is_file() and not _is_ignored(path, source_directory)
    )


def select_pcb(source_directory: Path, project: str = "") -> Path:
    """Select one board, preferring an unambiguous root KiCad project."""
    candidates = _pcb_candidates(source_directory)
    if project:
        requested_path = Path(project)
        if not requested_path.is_absolute():
            requested_path = source_directory / requested_path
        if requested_path.is_file() and requested_path.suffix.lower() == ".kicad_pcb":
            requested_path = requested_path.resolve()
            if requested_path not in candidates:
                raise ValueError(f"The selected PCB is outside the source tree or in an ignored directory: {requested_path}")
            return requested_path

        requested_name = Path(project).stem.lower()
        matches = [path for path in candidates if path.stem.lower() == requested_name]
        if len(matches) == 1:
            return matches[0]
        if not matches:
            raise ValueError(f"No .kicad_pcb file matched --project {project!r}.")
        raise ValueError(_selection_error(matches, f"More than one PCB matched --project {project!r}."))

    if not candidates:
        raise ValueError(f"No .kicad_pcb file was found under {source_directory}.")
    if len(candidates) == 1:
        return candidates[0]

    root_projects = sorted(source_directory.glob("*.kicad_pro"))
    root_project_boards = [project_path.with_suffix(".kicad_pcb").resolve() for project_path in root_projects]
    root_project_boards = [path for path in root_project_boards if path in candidates]
    if len(root_project_boards) == 1:
        return root_project_boards[0]

    top_level_boards = [path for path in candidates if path.parent == source_directory]
    if len(top_level_boards) == 1:
        return top_level_boards[0]

    named_boards = [path for path in candidates if path.stem.lower() == source_directory.name.lower()]
    if len(named_boards) == 1:
        return named_boards[0]

    raise ValueError(_selection_error(candidates, "More than one KiCad PCB was found."))


def _selection_error(candidates: list[Path], heading: str) -> str:
    shown = "\n".join(f"  - {path}" for path in candidates[:20])
    suffix = "\n  - ..." if len(candidates) > 20 else ""
    return f"{heading}\n{shown}{suffix}\nRun again with --project <board-name-or-path>."


def _schematic_children(schematic_path: Path) -> list[Path]:
    """Return existing hierarchical sheet files referenced by a schematic."""
    try:
        text = schematic_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return []
    children = []
    for value in re.findall(r'"([^"\r\n]+\.kicad_sch)"', text, flags=re.IGNORECASE):
        child = (schematic_path.parent / value).resolve()
        if child.is_file() and child != schematic_path.resolve() and child not in children:
            children.append(child)
    return children


def _hierarchical_schematics(root_schematic: Path) -> list[Path]:
    found = []
    queue = [root_schematic.resolve()]
    while queue:
        current = queue.pop(0)
        for child in _schematic_children(current):
            if child not in found and child != root_schematic.resolve():
                found.append(child)
                queue.append(child)
    return found


def stage_project_sources(documentation_directory: Path, pcb_path: Path) -> dict:
    """Copy the chosen KiCad project into the canonical OOMP data layout."""
    data_directory = documentation_directory / "data"
    data_directory.mkdir(parents=True, exist_ok=True)

    for filename in ["kicad_file.kicad_pcb", "kicad_file.kicad_sch", "kicad_file.kicad_pro"]:
        stale_path = data_directory / filename
        if stale_path.is_file():
            stale_path.unlink()
    stale_sheets = data_directory / "kicad_file_sheets"
    if stale_sheets.is_dir():
        shutil.rmtree(stale_sheets)

    copied = {}
    canonical_pcb = data_directory / "kicad_file.kicad_pcb"
    shutil.copy2(pcb_path, canonical_pcb)
    copied["pcb"] = {"source": str(pcb_path), "copy": str(canonical_pcb)}

    schematic_path = pcb_path.with_suffix(".kicad_sch")
    if schematic_path.is_file():
        canonical_schematic = data_directory / "kicad_file.kicad_sch"
        shutil.copy2(schematic_path, canonical_schematic)
        copied["schematic"] = {"source": str(schematic_path), "copy": str(canonical_schematic)}

        sheet_copies = []
        sheets_directory = data_directory / "kicad_file_sheets"
        for index, sheet_path in enumerate(_hierarchical_schematics(schematic_path), start=1):
            try:
                relative_path = sheet_path.relative_to(schematic_path.parent)
            except ValueError:
                relative_path = Path(f"external_{index}_{sheet_path.name}")
            destination = sheets_directory / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(sheet_path, destination)
            sheet_copies.append({"source": str(sheet_path), "copy": str(destination)})
        if sheet_copies:
            copied["schematic_sheets"] = sheet_copies

    project_path = pcb_path.with_suffix(".kicad_pro")
    if project_path.is_file():
        canonical_project = data_directory / "kicad_file.kicad_pro"
        shutil.copy2(project_path, canonical_project)
        copied["project"] = {"source": str(project_path), "copy": str(canonical_project)}

    return copied


def _local_repository_links() -> dict[str, str]:
    generated = "data/generated_data"
    assets = f"{generated}/src"
    return {
        "kicad_original": "data/",
        "generated_source": f"{assets}/",
        "board": f"{assets}/board.svg",
        "board_png": f"{assets}/board.png",
        "board_300_png": f"{assets}/board_300.png",
        "board_300_png_raw": f"{assets}/board_300.png",
        "board_pins": f"{assets}/board_pins.svg",
        "board_pins_png": f"{assets}/board_pins.png",
        "board_pins_300_png": f"{assets}/board_pins_300.png",
        "board_pins_300_png_raw": f"{assets}/board_pins_300.png",
        "board_bottom": f"{assets}/board_bottom.svg",
        "board_bottom_png": f"{assets}/board_bottom.png",
        "board_bottom_300_png": f"{assets}/board_bottom_300.png",
        "board_bottom_300_png_raw": f"{assets}/board_bottom_300.png",
        "board_pins_bottom": f"{assets}/board_pins_bottom.svg",
        "board_pins_bottom_png": f"{assets}/board_pins_bottom.png",
        "board_pins_bottom_300_png": f"{assets}/board_pins_bottom_300.png",
        "board_pins_bottom_300_png_raw": f"{assets}/board_pins_bottom_300.png",
        "board_mechanical": f"{assets}/board_mechanical.svg",
        "board_mechanical_png": f"{assets}/board_mechanical.png",
        "board_mechanical_300_png": f"{assets}/board_mechanical_300.png",
        "board_mechanical_300_png_raw": f"{assets}/board_mechanical_300.png",
        "schematic": f"{assets}/schematic.svg",
        "explorer": "board_explorer.html",
        "interactivehtmlbom": "data/interactivehtmlbom/ibom.html",
        "lcsc_review": f"{generated}/lcsc_review.yaml",
        "browser_research_queue": f"{generated}/browser_research_queue.md",
    }


def _generate_preview_pngs(generated_directory: Path, regenerate_pngs: bool) -> list[str]:
    asset_directory = generated_directory / "src"
    generated = []
    for basename in ["board", "board_pins", "board_bottom", "board_pins_bottom", "board_mechanical"]:
        svg_path = asset_directory / f"{basename}.svg"
        if not svg_path.is_file():
            continue
        png_path = asset_directory / f"{basename}_300.png"
        result = _make_board_png(
            svg_path,
            png_path,
            maximum_dimension=300,
            regenerate_pngs=regenerate_pngs,
        )
        if result.get("available", False):
            generated.append(str(png_path))
    return generated


def generate_documentation(
    source_directory: Path,
    project: str = "",
    regenerate_pngs: bool = False,
    interactive_bom: bool = True,
) -> Path:
    source_directory = source_directory.resolve()
    if not source_directory.is_dir():
        raise ValueError(f"Source directory does not exist: {source_directory}")

    pcb_path = select_pcb(source_directory, project=project)
    documentation_directory = source_directory / OUTPUT_DIRECTORY_NAME
    documentation_directory.mkdir(parents=True, exist_ok=True)
    copied_sources = stage_project_sources(documentation_directory, pcb_path)

    if interactive_bom:
        generate_interactive_html_bom(
            {"directory": str(documentation_directory), "record_run_errors": False}
        )

    generated_directory = documentation_directory / "data" / "generated_data"
    project_data, generated_directory = process_project(
        documentation_directory,
        REPOSITORY_ROOT / "parts",
        output_directory=generated_directory,
        log_missing_schematic=False,
    )
    if project_data is None:
        raise RuntimeError(f"Could not process the selected PCB: {pcb_path}")

    write_lcsc_review(project_data, generated_directory)
    write_browser_research_queue(project_data, generated_directory)
    part_metadata = {
        "name_readable": pcb_path.stem.replace("_", " ").replace("-", " ").strip().title(),
        "project_version": "local",
        "project_git_ref": "",
    }
    summary_data = generate_project_summary(
        documentation_directory,
        parts_directory=REPOSITORY_ROOT / "parts",
        output_directory=generated_directory,
        project_data=project_data,
        part_metadata=part_metadata,
        readme_output=documentation_directory / "README.md",
        regenerate_pngs=regenerate_pngs,
        repository_links_override=_local_repository_links(),
        summary_template=LOCAL_SUMMARY_TEMPLATE,
    )
    preview_pngs = _generate_preview_pngs(generated_directory, regenerate_pngs)
    explorer_path = generate_board_explorer(
        documentation_directory,
        project_data,
        summary_data,
        output_directory=generated_directory,
    )

    manifest = {
        "format_version": 1,
        "generated_by": "kicad_agents.standalone_documentation_action",
        "source_directory": str(source_directory),
        "selected_pcb": str(pcb_path),
        "documentation_directory": str(documentation_directory),
        "copied_sources": copied_sources,
        "outputs": {
            "readme": str(documentation_directory / "README.md"),
            "board_explorer": str(explorer_path),
            "generated_data": str(generated_directory),
            "preview_pngs": preview_pngs,
        },
    }
    (documentation_directory / "generation_manifest.yaml").write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return documentation_directory


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create oomp_documentation for a KiCad project in any directory."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path.cwd(),
        help="Directory to scan; defaults to the current working directory.",
    )
    parser.add_argument(
        "--project",
        default="",
        help="PCB basename or path to use when the source tree contains multiple boards.",
    )
    parser.add_argument(
        "--regenerate-pngs",
        action="store_true",
        help="Replace existing PNG renders instead of preserving them.",
    )
    parser.add_argument(
        "--skip-interactive-bom",
        action="store_true",
        help="Skip the optional KiCad/pcbnew InteractiveHtmlBom step.",
    )
    arguments = parser.parse_args()

    try:
        output = generate_documentation(
            arguments.source,
            project=arguments.project,
            regenerate_pngs=arguments.regenerate_pngs,
            interactive_bom=not arguments.skip_interactive_bom,
        )
    except Exception as error:
        print(f"OOMP documentation generation failed: {error}", file=sys.stderr)
        return 1

    print()
    print(f"OOMP documentation generated: {output}")
    print(f"Open: {output / 'README.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
