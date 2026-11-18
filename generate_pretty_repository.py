#!/usr/bin/env python3
"""Build the small, README-first view of the OOMP electronic catalogue.

The source repository remains the source of truth. This script reads the
top-level ``working.yaml`` file in each part directory and produces a single,
canonical, browsable page for every component, mechanical item, and project.
Only documentation, display PNGs, and self-contained board explorers are copied.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import io
import json
import os
import re
import shutil
import sys
import textwrap
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote, unquote, urlparse

try:
    import yaml
except ImportError as exc:  # pragma: no cover - friendly command-line failure
    raise SystemExit("PyYAML is required. Install it with: python -m pip install pyyaml") from exc

try:
    import cairosvg
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:  # pragma: no cover - friendly command-line failure
    raise SystemExit(
        "PNG generation requires Pillow and CairoSVG. Install them with: "
        "python -m pip install pillow cairosvg"
    ) from exc


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
GENERATED_MARKER = ".oomp-pretty-generated.json"
GENERATED_FILES = {
    "README.md",
    "BUILD_INFO.md",
    "rebuild.bat",
    ".nojekyll",
    GENERATED_MARKER,
}
TOP_LEVEL_KEYS = {
    "id",
    "name",
    "name_proper",
    "name_readable",
    "name_short",
    "category",
    "category_name",
    "link_github",
    "link_main",
    "md5_6_alpha",
    "project_board",
    "project_board_name",
    "project_board_url",
    "project_file_basename",
    "project_git_ref",
    "project_git_url",
    "project_github_repository",
    "project_github_url",
    "project_github_user",
    "project_source_format",
    "project_version",
    *(f"taxonomy_{index}" for index in range(1, 16)),
}
SCALAR_LINE = re.compile(r"^([A-Za-z0-9_]+):(?:[ \t]*(.*))?$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
WINDOWS_RESERVED_NAMES = {
    "con",
    "prn",
    "aux",
    "nul",
    *(f"com{number}" for number in range(1, 10)),
    *(f"lpt{number}" for number in range(1, 10)),
}


@dataclass
class Record:
    identifier: str
    title: str
    taxonomy: tuple[str, ...]
    metadata: dict[str, Any]
    source_directory: Path
    source_readme: Path | None
    kind: str
    summary: str
    snapshot: list[tuple[str, str]]
    detail_url: str
    project_url: str | None
    preview_source: Path | None
    preview_remote: str | None
    explorer_source: Path | None
    output_parts: tuple[str, ...] = field(default_factory=tuple)


@dataclass
class Node:
    path: tuple[str, ...]
    children: set[tuple[str, ...]] = field(default_factory=set)
    records: list[Record] = field(default_factory=list)
    descendant_count: int = 0
    descendant_kinds: Counter[str] = field(default_factory=Counter)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a compact, navigable README catalogue from OOMP metadata."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=SCRIPT_DIRECTORY / "pretty_repository_config.json",
        help="JSON configuration file (default: pretty_repository_config.json).",
    )
    parser.add_argument("--source", type=Path, help="Override source_root from the config.")
    parser.add_argument("--output", type=Path, help="Override output_root from the config.")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate an existing generated repository without rebuilding it.",
    )
    return parser.parse_args()


def load_config(path: Path) -> dict[str, Any]:
    config_path = path if path.is_absolute() else (SCRIPT_DIRECTORY / path)
    if not config_path.is_file():
        raise SystemExit(f"Configuration file not found: {config_path}")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    required = {
        "source_root",
        "output_root",
        "source_repository",
        "source_branch",
        "pretty_repository",
        "html_preview_base_url",
    }
    missing = sorted(required - config.keys())
    if missing:
        raise SystemExit(f"Missing configuration keys: {', '.join(missing)}")
    config["_config_path"] = str(config_path.resolve())
    return config


def resolve_path(value: str | Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = SCRIPT_DIRECTORY / path
    return path.resolve()


def scalar_value(raw: str | None) -> Any:
    if raw is None or raw == "":
        return ""
    try:
        value = yaml.safe_load(raw)
    except yaml.YAMLError:
        return raw.strip().strip("'\"")
    return "" if value is None else value


def read_top_level_metadata(path: Path) -> dict[str, Any]:
    """Read only useful top-level scalars, avoiding a costly full YAML load."""
    metadata: dict[str, Any] = {}
    with path.open("r", encoding="utf-8", errors="replace") as stream:
        for line in stream:
            if not line or line[0].isspace() or line.startswith("-"):
                continue
            match = SCALAR_LINE.match(line.rstrip("\r\n"))
            if match and match.group(1) in TOP_LEVEL_KEYS:
                metadata[match.group(1)] = scalar_value(match.group(2))
    return metadata


def safe_segment(value: Any, fallback: str = "unnamed") -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"[^a-z0-9._-]+", "_", text)
    text = re.sub(r"_+", "_", text).strip(" ._-") or fallback
    if text in WINDOWS_RESERVED_NAMES:
        text = f"_{text}"
    if len(text) > 72:
        suffix = hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]
        text = f"{text[:63].rstrip('._-')}-{suffix}"
    return text


def display_name(value: str) -> str:
    replacements = {
        "oomp": "OOMP",
        "github": "GitHub",
        "ic": "IC",
        "led": "LED",
        "pcb": "PCB",
        "usb": "USB",
        "jst": "JST",
    }
    words = value.replace("-", "_").split("_")
    return " ".join(replacements.get(word.lower(), word.capitalize()) for word in words if word)


def kind_count_phrase(kind: str, count: int) -> str:
    labels = {
        "Component": ("component", "components"),
        "Mechanical": ("mechanical item", "mechanical items"),
        "Project": ("project", "projects"),
    }
    singular, plural = labels.get(kind, (kind.lower(), f"{kind.lower()}s"))
    return f"{count:,} {singular if count == 1 else plural}"


def clean_markdown_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "")
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def extract_intro(readme: Path | None) -> str:
    if readme is None:
        return ""
    lines = readme.read_text(encoding="utf-8", errors="replace").splitlines()
    paragraph: list[str] = []
    for line in lines:
        stripped = line.strip()
        if paragraph and not stripped:
            candidate = clean_markdown_text(" ".join(paragraph))
            if len(candidate) >= 45:
                return candidate
            paragraph = []
            continue
        if not stripped:
            continue
        if stripped.startswith(("#", "[", "![", "<", "`", "|", "- ", ">")):
            continue
        paragraph.append(stripped)
    return clean_markdown_text(" ".join(paragraph)) if paragraph else ""


def extract_table(readme: Path | None, headings: Iterable[str]) -> list[tuple[str, str]]:
    if readme is None:
        return []
    lines = readme.read_text(encoding="utf-8", errors="replace").splitlines()
    wanted = {heading.casefold() for heading in headings}
    active = False
    rows: list[tuple[str, str]] = []
    for line in lines:
        if line.startswith("## "):
            active = line[3:].strip().casefold() in wanted
            continue
        if not active or not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0].casefold() in {"detail", "item"}:
            continue
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells[:2]):
            continue
        rows.append((clean_markdown_text(cells[0]), clean_markdown_text(cells[1])))
    return rows[:14]


def find_preview(source_directory: Path, source_readme: Path | None, kind: str) -> tuple[Path | None, str | None]:
    if kind == "Project":
        local_candidates = (
            "data/generated_data/src/board_300.png",
            "data/generated_data/src/board.svg",
            "data/working_svg_square_pins.svg",
        )
    else:
        local_candidates = (
            "data/working_svg_square_pins.svg",
            "data/working_svg_square_pins_300.png",
            "data/working_svg_assembly.svg",
            "data/working_svg_assembly_300.png",
        )
    for relative in local_candidates:
        candidate = source_directory / relative
        if candidate.is_file():
            return candidate, None
    if kind == "Project" and source_readme is not None:
        text = source_readme.read_text(encoding="utf-8", errors="replace")
        for match in MARKDOWN_IMAGE.finditer(text):
            url = match.group(1).strip().split(maxsplit=1)[0]
            if url.startswith("https://raw.githubusercontent.com/"):
                return None, url
    return None, None


def make_record(part_directory: Path, config: dict[str, Any]) -> Record:
    metadata = read_top_level_metadata(part_directory / "working.yaml")
    identifier = str(metadata.get("id") or part_directory.name)
    title = str(
        metadata.get("name_proper")
        or metadata.get("name_readable")
        or metadata.get("name_short")
        or metadata.get("name")
        or display_name(identifier)
    )
    taxonomy_values = [
        str(metadata.get(f"taxonomy_{index}") or "").strip()
        for index in range(1, 16)
    ]
    taxonomy = tuple(safe_segment(value) for value in taxonomy_values if value)
    if not taxonomy:
        taxonomy = ("uncategorised", safe_segment(identifier))
    if identifier.startswith("oomp_project_") or taxonomy[:2] == ("oomp", "project"):
        kind = "Project"
    elif taxonomy[0] == "mechanical":
        kind = "Mechanical"
    else:
        kind = "Component"
    source_readme_path = part_directory / "README.md"
    source_readme = source_readme_path if source_readme_path.is_file() else None
    summary = extract_intro(source_readme)
    if not summary:
        classification = " › ".join(display_name(value) for value in taxonomy[:4])
        noun = "hardware project" if kind == "Project" else "catalogue definition"
        summary = f"A concise OOMP {noun} organised under {classification}."
    snapshot = extract_table(source_readme, ("At a glance", "Project snapshot"))
    source_repository = str(config["source_repository"]).rstrip("/")
    source_branch = str(config["source_branch"])
    detail_url = str(metadata.get("link_github") or metadata.get("link_main") or "")
    if not detail_url:
        detail_url = f"{source_repository}/tree/{source_branch}/parts/{identifier}"
    project_url = str(metadata.get("project_board_url") or metadata.get("project_github_url") or "") or None
    preview_source, preview_remote = find_preview(part_directory, source_readme, kind)
    explorer_path = part_directory / "board_explorer.html"
    explorer_source = explorer_path if kind == "Project" and explorer_path.is_file() else None
    return Record(
        identifier=identifier,
        title=title,
        taxonomy=taxonomy,
        metadata=metadata,
        source_directory=part_directory,
        source_readme=source_readme,
        kind=kind,
        summary=summary,
        snapshot=snapshot,
        detail_url=detail_url,
        project_url=project_url,
        preview_source=preview_source,
        preview_remote=preview_remote,
        explorer_source=explorer_source,
    )


def discover_records(source_root: Path, config: dict[str, Any]) -> list[Record]:
    parts_root = source_root / "parts"
    if not parts_root.is_dir():
        raise SystemExit(f"Source parts directory not found: {parts_root}")
    records = [
        make_record(directory, config)
        for directory in sorted(parts_root.iterdir(), key=lambda item: item.name.casefold())
        if directory.is_dir() and (directory / "working.yaml").is_file()
    ]
    if not records:
        raise SystemExit(f"No part metadata found under: {parts_root}")
    identifiers = Counter(record.identifier for record in records)
    duplicates = [identifier for identifier, count in identifiers.items() if count > 1]
    if duplicates:
        raise SystemExit(f"Duplicate OOMP identifiers found: {', '.join(duplicates[:5])}")
    return records


def build_nodes(records: list[Record]) -> dict[tuple[str, ...], Node]:
    nodes: dict[tuple[str, ...], Node] = {(): Node(())}
    by_taxonomy: dict[tuple[str, ...], list[Record]] = defaultdict(list)
    for record in records:
        by_taxonomy[record.taxonomy].append(record)
        for depth in range(1, len(record.taxonomy) + 1):
            path = record.taxonomy[:depth]
            nodes.setdefault(path, Node(path))
            parent = path[:-1]
            nodes.setdefault(parent, Node(parent)).children.add(path)
    for taxonomy, grouped_records in by_taxonomy.items():
        nodes[taxonomy].records.extend(grouped_records)
        if len(grouped_records) == 1:
            grouped_records[0].output_parts = taxonomy
        else:
            for record in grouped_records:
                digest = hashlib.sha1(record.identifier.encode("utf-8")).hexdigest()[:10]
                record.output_parts = (*taxonomy, "_items", digest)
    for path, node in nodes.items():
        descendants = [record for record in records if record.taxonomy[: len(path)] == path]
        node.descendant_count = len(descendants)
        node.descendant_kinds = Counter(record.kind for record in descendants)
    return nodes


def markdown_escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def relative_link(from_directory: Path, target: Path) -> str:
    return os.path.relpath(target, from_directory).replace(os.sep, "/")


def breadcrumb(output_directory: Path, catalogue_root: Path, path: tuple[str, ...]) -> str:
    if not path:
        return f"[Home]({relative_link(output_directory, catalogue_root.parent / 'README.md')}) / Catalogue"
    crumbs = [("Catalogue", catalogue_root / "README.md")]
    for depth, segment in enumerate(path[:-1], start=1):
        crumbs.append((display_name(segment), catalogue_root.joinpath(*path[:depth], "README.md")))
    links = [f"[{label}]({relative_link(output_directory, target)})" for label, target in crumbs]
    if path:
        links.append(display_name(path[-1]))
    return " / ".join(links)


def navigation_section(node: Node, nodes: dict[tuple[str, ...], Node], output_directory: Path, catalogue_root: Path, threshold: int) -> str:
    entries: list[str] = []
    for child_path in sorted(node.children, key=lambda item: display_name(item[-1]).casefold()):
        child = nodes[child_path]
        target = catalogue_root.joinpath(*child_path, "README.md")
        kinds = " · ".join(
            kind_count_phrase(kind, count)
            for kind, count in sorted(child.descendant_kinds.items())
        )
        entries.append(
            f"- **[{display_name(child_path[-1])}]({relative_link(output_directory, target)})**  "
            f"<br><sub>{kinds}</sub>"
        )
    if len(node.records) > 1:
        for record in sorted(node.records, key=lambda item: item.title.casefold()):
            target = catalogue_root.joinpath(*record.output_parts, "README.md")
            entries.append(
                f"- **[{markdown_escape(record.title)}]({relative_link(output_directory, target)})**  "
                f"<br><sub>{record.kind} · `{record.identifier}`</sub>"
            )
    if not entries:
        return ""
    body = "\n".join(entries)
    heading = "## Explore"
    if len(entries) >= threshold:
        body = (
            f"<details>\n<summary><strong>Browse all {len(entries):,} entries</strong></summary>\n\n"
            f"{body}\n\n</details>"
        )
    return f"{heading}\n\n{body}\n"


def write_banner(path: Path, title: str, tagline: str, accent: str) -> None:
    safe_title = html.escape(title)
    safe_tagline = html.escape(tagline)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" role="img" aria-labelledby="title description">
  <title id="title">{safe_title}</title>
  <desc id="description">{safe_tagline}</desc>
  <defs>
    <linearGradient id="background" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#111827"/><stop offset="1" stop-color="#242056"/>
    </linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="1200" height="320" rx="28" fill="url(#background)"/>
  <g fill="none" stroke="#{accent}" stroke-width="4" opacity=".75">
    <path d="M0 74h145l38 38h92M0 244h112l52-52h100M1200 62h-148l-44 44h-92M1200 252h-126l-48-48h-104"/>
    <path d="M77 0v55m1046-55v55M76 320v-54m1048 54v-54"/>
  </g>
  <g fill="#{accent}" filter="url(#glow)">
    <circle cx="278" cy="112" r="8"/><circle cx="267" cy="192" r="8"/><circle cx="913" cy="106" r="8"/><circle cx="919" cy="204" r="8"/>
  </g>
  <text x="600" y="143" fill="#ffffff" font-family="Segoe UI, Arial, sans-serif" font-size="54" font-weight="700" text-anchor="middle">{safe_title}</text>
  <text x="600" y="198" fill="#d9d8ff" font-family="Segoe UI, Arial, sans-serif" font-size="21" text-anchor="middle">{safe_tagline}</text>
  <g transform="translate(557 226)" fill="none" stroke="#ffffff" stroke-width="3" opacity=".9">
    <rect x="0" y="0" width="86" height="42" rx="8"/><path d="M-18 10H0m-18 11H0m-18 11H0m86-22h18m-18 11h18m-18 11h18"/>
  </g>
</svg>'''
    path.write_text(svg, encoding="utf-8", newline="\n")


def prepare_output(output_root: Path, catalogue_name: str) -> None:
    marker_exists = (output_root / GENERATED_MARKER).exists()
    generated_readme = output_root / "README.md"
    readme_recognised = False
    if generated_readme.is_file():
        first_line = generated_readme.read_text(encoding="utf-8", errors="replace").splitlines()[:1]
        readme_recognised = bool(first_line and "Generated by generate_pretty_repository.py" in first_line[0])
    recognised = marker_exists or readme_recognised
    if output_root.exists() and (output_root / ".git").exists() and not recognised:
        raise SystemExit(f"Refusing to overwrite an unrecognised Git repository: {output_root}")
    if output_root.exists() and any(output_root.iterdir()) and not recognised:
        raise SystemExit(
            f"Refusing to overwrite a non-empty directory without {GENERATED_MARKER}: {output_root}"
        )
    output_root.mkdir(parents=True, exist_ok=True)
    for directory_name in (catalogue_name, "assets"):
        target = output_root / directory_name
        if target.exists():
            shutil.rmtree(target)
    for filename in GENERATED_FILES:
        target = output_root / filename
        if target.exists():
            target.unlink()
    obsolete_workflow = output_root / ".github" / "workflows" / "publish-pages.yml"
    if obsolete_workflow.exists():
        obsolete_workflow.unlink()
    for obsolete_directory in (obsolete_workflow.parent, obsolete_workflow.parent.parent):
        if obsolete_directory.is_dir() and not any(obsolete_directory.iterdir()):
            obsolete_directory.rmdir()
    (output_root / catalogue_name).mkdir()
    (output_root / "assets").mkdir()


def root_readme(config: dict[str, Any], records: list[Record], nodes: dict[tuple[str, ...], Node]) -> str:
    title = str(config["project_title"])
    tagline = str(config["project_tagline"])
    counts = Counter(record.kind for record in records)
    root_children = sorted(nodes[()].children, key=lambda path: display_name(path[-1]).casefold())
    cards = []
    icons = {"electronic": "⚡", "mechanical": "⚙️", "oomp": "🧭"}
    for child_path in root_children:
        node = nodes[child_path]
        kinds = ", ".join(kind_count_phrase(kind, count) for kind, count in sorted(node.descendant_kinds.items()))
        cards.append(
            f"| {icons.get(child_path[-1], '•')} **[{display_name(child_path[-1])}](catalogue/{'/'.join(child_path)}/README.md)** | {kinds} |"
        )
    card_text = "\n".join(cards)
    return f'''<!-- Generated by generate_pretty_repository.py; edit the source metadata or configuration. -->
<div align="center">

![{markdown_escape(title)}](assets/catalogue-banner.svg)

**{markdown_escape(tagline)}**

[Browse the catalogue](catalogue/README.md) · [Open the full source repository]({config['source_repository']})

![Entries](https://img.shields.io/badge/catalogue-{len(records):,}%20entries-{config['accent_colour']}?style=flat-square)
![Components](https://img.shields.io/badge/components-{counts['Component']:,}-2ea44f?style=flat-square)
![Projects](https://img.shields.io/badge/projects-{counts['Project']:,}-0969da?style=flat-square)

</div>

## Find what you need

| Collection | Inside |
| --- | --- |
{card_text}

## Designed for browsing

Start broad and follow the taxonomy until you reach the exact part or board. Every record appears **once** in the tree, every page carries its context as a breadcrumb, and every concise entry links back to the complete source record.

- **Visual:** every part and project has a display-ready, locally stored PNG.
- **Focused:** high-value metadata is surfaced before implementation detail.
- **Traceable:** “Full details” always opens the canonical page in the original repository.
- **Explorable:** every project includes its HTML file in the repository; processed boards retain the full interactive explorer.
- **Reproducible:** run `rebuild.bat` here, or `generate_pretty_repository.bat` in the source checkout.

## What stays in the full repository

KiCad source, footprints, symbols, manufacturing files, large render sets, working YAML, and generation intermediates remain in the [complete OOMP repository]({config['source_repository']}). This repository is its welcoming, README-first front door.

## Opening the explorers

No GitHub Pages setup is required. Each project offers an **Open board explorer** link rendered from its checked-in `board_explorer.html` through Git-Forge HTML Preview, alongside a direct link to the file inside this repository.

---

<sub>Generated from OOMP metadata. See [build information](BUILD_INFO.md).</sub>
'''


def category_readme(node: Node, nodes: dict[tuple[str, ...], Node], output_directory: Path, catalogue_root: Path, threshold: int, source_repository: str) -> str:
    path_label = " / ".join(display_name(value) for value in node.path)
    kinds = " · ".join(
        f"**{kind_count_phrase(kind, count).split(' ', 1)[0]}** {kind_count_phrase(kind, count).split(' ', 1)[1]}"
        for kind, count in sorted(node.descendant_kinds.items())
    )
    navigation = navigation_section(node, nodes, output_directory, catalogue_root, threshold)
    back_label = "Repository home" if not node.path else "Back to the catalogue"
    back_target = catalogue_root.parent / "README.md" if not node.path else catalogue_root / "README.md"
    return f'''<!-- Generated navigation page. -->
<sub>{breadcrumb(output_directory, catalogue_root, node.path)}</sub>

# {path_label or 'Catalogue'}

> Browse this branch of the OOMP taxonomy. Choose a group below to narrow the catalogue.

{kinds}

{navigation}
---

[← {back_label}]({relative_link(output_directory, back_target)}) · [Full source repository]({source_repository})
'''


def item_readme(record: Record, node: Node, nodes: dict[tuple[str, ...], Node], output_directory: Path, catalogue_root: Path, threshold: int, preview_name: str | None, explorer_url: str | None) -> str:
    icon = {"Project": "🧭", "Mechanical": "⚙️", "Component": "⚡"}[record.kind]
    details: list[tuple[str, str]] = []
    seen = set()
    for key, value in record.snapshot:
        normalized = key.casefold()
        if normalized in seen or not value:
            continue
        seen.add(normalized)
        details.append((key, value))
    if not details:
        if record.kind == "Project":
            candidates = (
                ("Owner", record.metadata.get("project_github_user")),
                ("Repository", record.metadata.get("project_github_repository")),
                ("Board", record.metadata.get("project_board_name")),
                ("Source format", record.metadata.get("project_source_format")),
                ("Version", record.metadata.get("project_version")),
                ("Git ref", record.metadata.get("project_git_ref")),
            )
        else:
            candidates = (
                ("Type", display_name(record.taxonomy[1]) if len(record.taxonomy) > 1 else record.kind),
                ("Category", record.metadata.get("category_name") or record.metadata.get("category")),
            )
        details.extend((key, str(value)) for key, value in candidates if value)
    details = [(key, value) for key, value in details if key.casefold() != "oomp id"]
    rows = "\n".join(f"| {markdown_escape(key)} | {markdown_escape(value)} |" for key, value in details)
    if not rows:
        rows = f"| Kind | {record.kind} |"
    preview = ""
    if preview_name:
        preview = f'\n<p align="center"><img src="{preview_name}" alt="{html.escape(record.title)} preview" width="560"></p>\n'
    elif record.preview_remote:
        preview = f'\n<p align="center"><img src="{record.preview_remote}" alt="{html.escape(record.title)} preview" width="560"></p>\n'
    source_links = []
    if explorer_url:
        source_links.append(f"**[Open board explorer ↗]({explorer_url})**")
        source_links.append("[HTML file](board_explorer.html)")
    source_links.append(f"[Full details →]({record.detail_url})")
    if record.project_url and record.project_url != record.detail_url:
        source_links.append(f"[Original project files]({record.project_url})")
    links = " · ".join(source_links)
    navigation = navigation_section(node, nodes, output_directory, catalogue_root, threshold)
    taxonomy_display = " › ".join(display_name(value) for value in record.taxonomy)
    source_note = "A detailed source README is available." if record.source_readme else "This index entry was built directly from its working metadata."
    explorer_note = ""
    if explorer_url and record.explorer_source:
        explorer_note = f" The [interactive board explorer]({explorer_url}) is included as a self-contained HTML page."
    elif explorer_url:
        explorer_note = f" The [board explorer page]({explorer_url}) currently shows the project preview and source links; interactive board geometry will appear after the source project has been processed."
    return f'''<!-- Generated item page. Full data lives in the source repository. -->
<sub>{breadcrumb(output_directory, catalogue_root, record.taxonomy)}</sub>

# {icon} {markdown_escape(record.title)}

> {markdown_escape(record.summary)}
{preview}
<div align="center">

{links}

</div>

## At a glance

| Detail | Value |
| --- | --- |
{rows}
| OOMP ID | `{markdown_escape(record.identifier)}` |

## Catalogue location

`{markdown_escape(taxonomy_display)}`

{navigation}
## About this page

This is the compact catalogue view. {source_note}{explorer_note} Schematics, fabrication data, working metadata, alternate diagrams, availability data, and project analysis stay with the [full original record]({record.detail_url}).

---

[↑ Parent category]({relative_link(output_directory, catalogue_root.joinpath(*record.taxonomy[:-1], 'README.md'))}) · [Catalogue home]({relative_link(output_directory, catalogue_root / 'README.md')})
'''


def svg_dimensions(path: Path) -> tuple[float, float]:
    try:
        root = ET.parse(path).getroot()
        view_box = root.attrib.get("viewBox", "").replace(",", " ").split()
        if len(view_box) == 4:
            width, height = float(view_box[2]), float(view_box[3])
            if width > 0 and height > 0:
                return width, height
    except (ET.ParseError, OSError, ValueError):
        pass
    return 1.0, 1.0


def fitted_size(width: float, height: float, maximum_width: int, maximum_height: int) -> tuple[int, int]:
    scale = min(maximum_width / width, maximum_height / height)
    return max(1, round(width * scale)), max(1, round(height * scale))


def card_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    windows_fonts = Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts"
    candidates = [
        windows_fonts / ("segoeuib.ttf" if bold else "segoeui.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default(size=size)


def write_metadata_card(record: Record, destination: Path, width: int, height: int) -> None:
    gradient = Image.new("RGB", (1, height))
    colours = []
    for y in range(height):
        blend = y / max(1, height - 1)
        colours.append((
            round(17 + 19 * blend),
            round(24 + 10 * blend),
            round(39 + 47 * blend),
        ))
    gradient.putdata(colours)
    image = gradient.resize((width, height))
    draw = ImageDraw.Draw(image)
    accent = "#7667ff"
    muted = "#d9d8ff"
    draw.line((0, 92, 120, 92, 158, 130, 235, 130), fill=accent, width=4)
    draw.line((width, height - 92, width - 120, height - 92, width - 158, height - 130, width - 235, height - 130), fill=accent, width=4)
    for x, y in ((235, 130), (width - 235, height - 130)):
        draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=accent)
    label = "HARDWARE PROJECT" if record.kind == "Project" else record.kind.upper()
    draw.rounded_rectangle((54, 46, 260, 84), radius=18, fill="#29245d")
    draw.text((72, 55), label, font=card_font(17, True), fill=muted)
    title_lines = textwrap.wrap(record.title, width=38) or [record.title]
    title_lines = title_lines[:4]
    if len(" ".join(title_lines)) < len(record.title):
        title_lines[-1] = title_lines[-1].rstrip(" .") + "…"
    title_text = "\n".join(title_lines)
    title_font = card_font(38 if len(title_lines) <= 3 else 32, True)
    draw.multiline_text((54, 150), title_text, font=title_font, fill="white", spacing=10)
    classification = "  ›  ".join(display_name(value) for value in record.taxonomy[:4])
    draw.text((56, height - 77), classification, font=card_font(18), fill=muted)
    draw.text((56, height - 43), record.identifier[:88], font=card_font(13), fill="#9ca3af")
    image.save(destination, format="PNG", optimize=True)


def render_preview_png(record: Record, output_directory: Path, enabled: bool, maximum_width: int, maximum_height: int) -> tuple[str | None, bool]:
    if not enabled:
        return None, False
    destination = output_directory / "preview.png"
    if record.preview_source is not None:
        try:
            if record.preview_source.suffix.casefold() == ".svg":
                source_width, source_height = svg_dimensions(record.preview_source)
                width, height = fitted_size(source_width, source_height, maximum_width, maximum_height)
                svg_text = record.preview_source.read_text(encoding="utf-8", errors="replace")
                # Board drawings use browser-friendly CSS custom properties. CairoSVG
                # does not resolve them, so use each declaration's explicit fallback.
                svg_text = re.sub(
                    r"var\(\s*--[^,()]+,\s*([^)]+)\)",
                    lambda match: match.group(1).strip(),
                    svg_text,
                )
                png_bytes = cairosvg.svg2png(
                    bytestring=svg_text.encode("utf-8"),
                    output_width=width,
                    output_height=height,
                )
                with Image.open(io.BytesIO(png_bytes)) as rendered:
                    flattened = Image.new("RGB", rendered.size, "white")
                    if rendered.mode == "RGBA":
                        flattened.paste(rendered, mask=rendered.getchannel("A"))
                    else:
                        flattened.paste(rendered.convert("RGB"))
                    flattened.save(destination, format="PNG", optimize=True)
            else:
                with Image.open(record.preview_source) as source_image:
                    rendered = source_image.convert("RGB")
                    rendered.thumbnail((maximum_width, maximum_height), Image.Resampling.LANCZOS)
                    rendered.save(destination, format="PNG", optimize=True)
            return destination.name, True
        except Exception as exc:
            print(f"Warning: could not render {record.identifier}: {exc}", file=sys.stderr)
    write_metadata_card(record, destination, maximum_width, maximum_height)
    return destination.name, False


def write_project_explorer(record: Record, output_directory: Path, enabled: bool) -> bool:
    if not enabled or record.kind != "Project":
        return False
    destination = output_directory / "board_explorer.html"
    if record.explorer_source is not None:
        shutil.copy2(record.explorer_source, destination)
        return True
    title = html.escape(record.title)
    summary = html.escape(record.summary)
    detail_url = html.escape(record.detail_url, quote=True)
    project_url = html.escape(record.project_url or record.detail_url, quote=True)
    identifier = html.escape(record.identifier)
    page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>{title} · Board explorer</title>
  <style>
    :root {{ --page:#0d1224; --panel:#171c35; --ink:#fff; --muted:#c8cae8; --accent:#7868ff; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; min-height:100vh; color:var(--ink); background:radial-gradient(circle at top,#272253 0,var(--page) 52%); font:16px/1.6 Inter,ui-sans-serif,system-ui,sans-serif; }}
    main {{ width:min(1040px,calc(100% - 32px)); margin:0 auto; padding:56px 0 72px; }}
    .eyebrow {{ color:#aaa4ff; font-size:.8rem; font-weight:800; letter-spacing:.14em; text-transform:uppercase; }}
    h1 {{ max-width:850px; margin:.3rem 0 1rem; font-size:clamp(2rem,5vw,4.25rem); line-height:1.05; }}
    .lead {{ max-width:780px; color:var(--muted); font-size:1.1rem; }}
    .panel {{ margin-top:34px; padding:24px; border:1px solid #343b69; border-radius:22px; background:rgba(23,28,53,.9); box-shadow:0 24px 70px #05071488; }}
    img {{ display:block; width:min(100%,800px); max-height:600px; object-fit:contain; margin:auto; border-radius:14px; background:#fff; }}
    .notice {{ margin-top:22px; padding:16px 18px; color:var(--muted); border-left:4px solid var(--accent); background:#211e48; }}
    .actions {{ display:flex; flex-wrap:wrap; gap:12px; margin-top:24px; }}
    a {{ color:#dcd9ff; }} .button {{ padding:11px 17px; border-radius:999px; background:var(--accent); color:#fff; font-weight:750; text-decoration:none; }}
    .button.secondary {{ background:#292f54; }} code {{ color:#aaa4ff; overflow-wrap:anywhere; }}
  </style>
</head>
<body><main>
  <div class="eyebrow">OOMP board explorer</div>
  <h1>{title}</h1>
  <p class="lead">{summary}</p>
  <section class="panel">
    <img src="preview.png" alt="{title} preview">
    <div class="notice"><strong>Interactive board geometry is not available yet.</strong><br>This project is indexed and ready to browse; its source board still needs to pass through the OOMP board-processing pipeline.</div>
    <div class="actions"><a class="button" href="{project_url}">Open original project ↗</a><a class="button secondary" href="{detail_url}">Full OOMP record ↗</a></div>
  </section>
  <p><code>{identifier}</code></p>
</main></body>
</html>'''
    destination.write_text(page, encoding="utf-8", newline="\n")
    return False


def write_rebuild_batch(output_root: Path, source_root: Path, config_path: Path) -> None:
    launcher = source_root / "generate_pretty_repository.bat"
    relative_launcher = os.path.relpath(launcher, output_root)
    relative_config = os.path.relpath(config_path, launcher.parent)
    text = (
        "@echo off\r\n"
        "setlocal\r\n"
        "cd /d \"%~dp0\"\r\n"
        f'call "{relative_launcher}" --config "{relative_config}" %*\r\n'
        "exit /b %errorlevel%\r\n"
    )
    (output_root / "rebuild.bat").write_text(text, encoding="utf-8", newline="")


def validate_repository(output_root: Path) -> list[str]:
    errors: list[str] = []
    readmes = list(output_root.rglob("README.md"))
    if not readmes:
        return ["No README.md files were generated."]
    for readme in readmes:
        text = readme.read_text(encoding="utf-8", errors="replace")
        for match in MARKDOWN_LINK.finditer(text):
            raw_target = match.group(1).strip()
            target_text = raw_target.split(maxsplit=1)[0].strip("<>")
            parsed = urlparse(target_text)
            if parsed.scheme or target_text.startswith(("#", "mailto:")):
                continue
            path_text = unquote(target_text.split("#", 1)[0])
            if not path_text:
                continue
            target = (readme.parent / Path(path_text.replace("/", os.sep))).resolve()
            if not target.exists():
                errors.append(f"Broken link in {readme.relative_to(output_root)}: {target_text}")
    marker_path = output_root / GENERATED_MARKER
    if marker_path.is_file():
        try:
            stats = json.loads(marker_path.read_text(encoding="utf-8"))
            preview_files = list(output_root.rglob("preview.png"))
            explorer_files = list(output_root.rglob("board_explorer.html"))
            if len(preview_files) != int(stats.get("records", -1)):
                errors.append(
                    f"Expected {stats.get('records')} PNG previews, found {len(preview_files)}."
                )
            if len(explorer_files) != int(stats.get("projects", -1)):
                errors.append(
                    f"Expected {stats.get('projects')} board explorers, found {len(explorer_files)}."
                )
            for preview in preview_files:
                try:
                    with Image.open(preview) as image:
                        image.verify()
                except Exception as exc:
                    errors.append(f"Invalid PNG {preview.relative_to(output_root)}: {exc}")
                    if len(errors) >= 50:
                        break
        except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
            errors.append(f"Could not validate build marker: {exc}")
    else:
        errors.append(f"Missing build marker: {GENERATED_MARKER}")
    return errors


def generate(config: dict[str, Any], source_root: Path, output_root: Path) -> dict[str, Any]:
    catalogue_name = safe_segment(config.get("catalogue_directory", "catalogue"), "catalogue")
    threshold = max(2, int(config.get("collapsed_navigation_threshold", 24)))
    records = discover_records(source_root, config)
    nodes = build_nodes(records)
    prepare_output(output_root, catalogue_name)
    catalogue_root = output_root / catalogue_name
    accent = re.sub(r"[^0-9a-fA-F]", "", str(config.get("accent_colour", "6d5dfc")))[:6] or "6d5dfc"
    write_banner(
        output_root / "assets" / "catalogue-banner.svg",
        str(config.get("project_title", "OOMP Electronic Catalogue")),
        str(config.get("project_tagline", "A README-first component catalogue.")),
        accent,
    )
    (output_root / "README.md").write_text(root_readme(config, records, nodes), encoding="utf-8", newline="\n")
    maximum_width = max(320, int(config.get("preview_max_width_px", 800)))
    maximum_height = max(240, int(config.get("preview_max_height_px", 600)))
    previews_enabled = bool(config.get("copy_previews", True))
    explorers_enabled = bool(config.get("include_board_explorers", True))
    pretty_repository = str(config.get("pretty_repository", "")).rstrip("/")
    pretty_branch = str(config.get("pretty_repository_branch", "main"))
    html_preview_base = str(config.get("html_preview_base_url", "https://html-preview.github.io/?url="))
    render_counts: Counter[str] = Counter()

    def render_record(record: Record, node: Node, output_directory: Path) -> str:
        preview_name, rendered_from_source = render_preview_png(
            record,
            output_directory,
            previews_enabled,
            maximum_width,
            maximum_height,
        )
        render_counts["source_previews" if rendered_from_source else "metadata_previews"] += 1
        explorer_url = None
        if record.kind == "Project" and explorers_enabled:
            actual_explorer = write_project_explorer(record, output_directory, True)
            render_counts["interactive_explorers" if actual_explorer else "project_landing_pages"] += 1
            encoded_path = "/".join(quote(part) for part in (catalogue_name, *record.output_parts, "board_explorer.html"))
            repository_file_url = f"{pretty_repository}/blob/{quote(pretty_branch)}/{encoded_path}"
            explorer_url = f"{html_preview_base}{repository_file_url}"
        return item_readme(
            record,
            node,
            nodes,
            output_directory,
            catalogue_root,
            threshold,
            preview_name,
            explorer_url,
        )

    for path, node in sorted(nodes.items(), key=lambda item: (len(item[0]), item[0])):
        output_directory = catalogue_root.joinpath(*path)
        output_directory.mkdir(parents=True, exist_ok=True)
        if path and len(node.records) == 1:
            record = node.records[0]
            content = render_record(record, node, output_directory)
        else:
            content = category_readme(
                node,
                nodes,
                output_directory,
                catalogue_root,
                threshold,
                str(config["source_repository"]),
            )
        (output_directory / "README.md").write_text(content, encoding="utf-8", newline="\n")
    for node in nodes.values():
        if len(node.records) <= 1:
            continue
        for record in node.records:
            output_directory = catalogue_root.joinpath(*record.output_parts)
            output_directory.mkdir(parents=True, exist_ok=True)
            content = render_record(record, node, output_directory)
            (output_directory / "README.md").write_text(content, encoding="utf-8", newline="\n")
    config_path = Path(config["_config_path"])
    write_rebuild_batch(output_root, source_root, config_path)
    counts = Counter(record.kind for record in records)
    stats = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_root": str(source_root),
        "source_repository": config["source_repository"],
        "source_branch": config["source_branch"],
        "output_root": str(output_root),
        "records": len(records),
        "components": counts["Component"],
        "mechanical_items": counts["Mechanical"],
        "projects": counts["Project"],
        "navigation_nodes": len(nodes),
        "source_readmes": sum(record.source_readme is not None for record in records),
        "png_previews": render_counts["source_previews"] + render_counts["metadata_previews"],
        "source_artwork_previews": render_counts["source_previews"],
        "metadata_card_previews": render_counts["metadata_previews"],
        "interactive_board_explorers": render_counts["interactive_explorers"],
        "project_landing_pages": render_counts["project_landing_pages"],
    }
    build_info = "# Build information\n\n" + "\n".join(
        f"- **{display_name(key)}:** {value:,}" if isinstance(value, int) else f"- **{display_name(key)}:** `{value}`"
        for key, value in stats.items()
    ) + "\n"
    (output_root / "BUILD_INFO.md").write_text(build_info, encoding="utf-8", newline="\n")
    (output_root / GENERATED_MARKER).write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    return stats


def main() -> int:
    args = parse_args()
    config = load_config(args.config)
    source_root = resolve_path(args.source or config["source_root"])
    output_root = resolve_path(args.output or config["output_root"])
    if source_root == output_root:
        raise SystemExit("Source and output directories must be different.")
    if args.validate_only:
        errors = validate_repository(output_root)
        if errors:
            print("Validation failed:", file=sys.stderr)
            for error in errors[:50]:
                print(f"  - {error}", file=sys.stderr)
            return 1
        print(f"Validation passed: {output_root}")
        return 0
    stats = generate(config, source_root, output_root)
    errors = validate_repository(output_root)
    if errors:
        print("Generation completed, but validation failed:", file=sys.stderr)
        for error in errors[:50]:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(
        f"Generated {stats['records']:,} records across {stats['navigation_nodes']:,} navigation nodes."
    )
    print(f"Output: {output_root}")
    print("Validation: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
