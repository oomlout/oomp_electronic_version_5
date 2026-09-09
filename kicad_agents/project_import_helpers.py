"""Deterministic helpers for importing queued GitHub PCB repositories.

The helpers deliberately keep repository selection, Git inspection, board
version selection, and YAML writing in Python.  An external lightweight agent
only needs to review candidates explicitly marked as ambiguous.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import json
import re
import shutil
import subprocess
import tempfile
from typing import Iterable
from urllib.parse import quote

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE = REPOSITORY_ROOT / "report" / "adafruit_sparkfun_pcb_projects_last_updated.yaml"
DEFAULT_PROJECT_DATA = REPOSITORY_ROOT / "project_data"
DEFAULT_RUN_DIRECTORY = REPOSITORY_ROOT / "report" / "project_import_runs"
BOARD_SUFFIXES = {".brd": "eagle", ".kicad_pcb": "kicad"}
KICAD_COMPANIONS = [".kicad_pcb", ".kicad_sch", ".kicad_pro"]
AUXILIARY_WORDS = {
    "array", "backup", "copy", "fab", "fabrication", "old", "panel",
    "panelized", "panelised", "paste", "production", "stencil",
}


@dataclass(frozen=True)
class QueueSelection:
    entry: dict
    skipped_existing: tuple[str, ...]


def _load_mapping(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return data


def _normalise_slug(value: str) -> str:
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", str(value))
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value).lower()
    return re.sub(r"_+", "_", value).strip("_")


def _humanise(value: str) -> str:
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", value)
    value = re.sub(r"[_-]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def existing_repositories(project_data_directory: Path = DEFAULT_PROJECT_DATA) -> set[str]:
    """Return lower-case ``owner/repository`` identifiers already declared."""
    existing = set()
    for path in sorted(project_data_directory.glob("*/working.yaml")):
        data = _load_mapping(path)
        owner = str(data.get("github_user", path.parent.name)).strip()
        for project in data.get("projects", []):
            if isinstance(project, dict) and project.get("github_repository"):
                existing.add(f"{owner}/{project['github_repository']}".lower())
    return existing


def select_next_repository(
    queue_path: Path = DEFAULT_QUEUE,
    project_data_directory: Path = DEFAULT_PROJECT_DATA,
) -> QueueSelection:
    """Select the first TODO row, respecting the queue's stored order."""
    queue = _load_mapping(queue_path)
    repositories = queue.get("repositories")
    if not isinstance(repositories, list):
        raise ValueError(f"{queue_path}: repositories must be a list")
    existing = existing_repositories(project_data_directory)
    skipped = []
    for entry in repositories:
        if not isinstance(entry, dict):
            continue
        full_name = str(entry.get("full_name", "")).strip()
        if not full_name:
            continue
        if full_name.lower() in existing:
            if str(entry.get("status", "TODO")).upper() != "ADDED":
                skipped.append(full_name)
            continue
        if str(entry.get("status", "TODO")).upper() == "TODO":
            return QueueSelection(dict(entry), tuple(skipped))
    raise RuntimeError("No unimported TODO repositories remain in the queue")


def find_queue_repository(queue_path: Path, full_name: str) -> dict:
    """Return one named queue record regardless of its current status."""
    queue = _load_mapping(queue_path)
    for entry in queue.get("repositories", []):
        if isinstance(entry, dict) and str(entry.get("full_name", "")).lower() == full_name.lower():
            return dict(entry)
    raise ValueError(f"{full_name} is not present in {queue_path}")


def _run_git(arguments: list[str], cwd: Path | None = None) -> str:
    completed = subprocess.run(
        ["git", *arguments], cwd=cwd, capture_output=True, text=True,
    )
    if completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip()
        raise RuntimeError(f"git {' '.join(arguments)} failed: {message}")
    return completed.stdout


def _run_git_bytes(arguments: list[str], cwd: Path | None = None) -> bytes:
    completed = subprocess.run(["git", *arguments], cwd=cwd, capture_output=True)
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git {' '.join(arguments)} failed: {message}")
    return completed.stdout


def eagle_storage_format(blob: bytes) -> str:
    """Classify Eagle 6+ XML versus the unsupported pre-Eagle-6 binary format."""
    prefix = blob[:8192].lstrip(b"\xef\xbb\xbf\x00\t\r\n ")
    if prefix.startswith(b"<?xml") or prefix.startswith(b"<eagle"):
        return "xml"
    return "legacy_binary"


def _version_details(stem: str) -> tuple[str, tuple[int, ...], str]:
    """Return family stem, sortable version, and detected version text."""
    patterns = [
        re.compile(r"(?i)(?:[ _.-]+)(rev(?:ision)?[ _.-]*([a-z]|\d+(?:[._-]\d+)*))"),
        re.compile(r"(?i)(?:[ _.-]+)(v(?:er(?:sion)?)?[ _.-]*(\d+(?:[._-]\d+)*))"),
    ]
    matches = []
    for pattern in patterns:
        matches.extend(pattern.finditer(stem))
    if not matches:
        return stem, (0,), ""
    match = matches[-1]
    version_text = match.group(1)
    token = match.group(2) if match.lastindex and match.lastindex >= 2 else match.group(1)
    if len(token) == 1 and token.isalpha():
        version_key = (ord(token.lower()) - 96,)
    else:
        version_key = tuple(int(number) for number in re.findall(r"\d+", token)) or (0,)
    family = (stem[: match.start()] + stem[match.end() :]).strip(" _.-")
    return family or stem, version_key, version_text


def _candidate(relative_path: str, all_paths: dict[str, str]) -> dict:
    source = PurePosixPath(relative_path)
    suffix = source.suffix.lower()
    source_format = BOARD_SUFFIXES[suffix]
    source_stem = source.name[: -len(source.suffix)]
    family_stem, version_key, version_text = _version_details(source_stem)
    lower_lookup = {key.lower(): value for key, value in all_paths.items()}
    base_path = str(source.with_suffix(""))
    companions = []
    if source_format == "kicad":
        for extension in KICAD_COMPANIONS:
            possible = f"{base_path}{extension}"
            if possible.lower() in lower_lookup:
                companions.append(extension)
    else:
        companions.append(".brd")
        if f"{base_path}.sch".lower() in lower_lookup:
            companions.append(".sch")
    words = set(_normalise_slug(str(source)).split("_"))
    auxiliary = sorted(words & AUXILIARY_WORDS)
    family_key = f"{_normalise_slug(str(source.parent))}/{_normalise_slug(family_stem)}"
    return {
        "path": relative_path,
        "source_format": source_format,
        "folder": "" if str(source.parent) == "." else str(source.parent),
        "basename": source_stem,
        "project_file_path": base_path,
        "project_file_extensions": companions,
        "has_schematic": source_format == "kicad" and ".kicad_sch" in companions
        or source_format == "eagle" and ".sch" in companions,
        "family_stem": family_stem,
        "family_key": family_key,
        "version_key": list(version_key),
        "version_text": version_text,
        "auxiliary_words": auxiliary,
    }


def _select_current_candidates(candidates: list[dict]) -> tuple[list[dict], list[dict]]:
    """Keep one current source per version family and reject clear auxiliaries."""
    groups: dict[str, list[dict]] = {}
    for candidate in candidates:
        groups.setdefault(candidate["family_key"], []).append(candidate)
    selected = []
    excluded = []
    for group in groups.values():
        normal = [candidate for candidate in group if not candidate["auxiliary_words"]]
        pool = normal or group
        winner = max(pool, key=lambda item: (tuple(item["version_key"]), item["path"].lower()))
        selected.append(winner)
        for candidate in group:
            if candidate is winner:
                continue
            rejected = dict(candidate)
            rejected["exclude_reason"] = (
                "auxiliary fabrication/panel source" if candidate["auxiliary_words"]
                else f"older version of {winner['path']}"
            )
            excluded.append(rejected)
    return sorted(selected, key=lambda item: item["path"].lower()), sorted(
        excluded, key=lambda item: item["path"].lower()
    )


def _assign_board_names(candidates: list[dict]) -> None:
    used: set[str] = set()
    for candidate in candidates:
        source = PurePosixPath(candidate["path"])
        base = _normalise_slug(candidate["family_stem"] or candidate["basename"])
        slug = base
        parents = [part for part in source.parent.parts if part not in {".", "hardware", "pcb", "pcb_files"}]
        while slug in used and parents:
            slug = f"{_normalise_slug(parents.pop())}_{base}"
        suffix = 2
        unique = slug
        while unique in used:
            unique = f"{slug}_{suffix}"
            suffix += 1
        candidate["board"] = unique
        candidate["board_name"] = _humanise(candidate["family_stem"] or candidate["basename"])
        used.add(unique)


def inspect_repository(entry: dict, temporary_root: Path | None = None) -> dict:
    """Clone one repository into a disposable directory and inspect its Git tree."""
    full_name = str(entry["full_name"])
    branch = str(entry.get("default_branch") or "main")
    url = str(entry.get("url") or f"https://github.com/{full_name}")
    parent = str(temporary_root) if temporary_root else None
    with tempfile.TemporaryDirectory(prefix="oomp_project_import_", dir=parent) as temporary:
        clone = Path(temporary) / "repository"
        _run_git([
            "clone", "--filter=blob:none", "--no-checkout", "--single-branch",
            "--branch", branch, f"{url}.git", str(clone),
        ])
        tree_output = _run_git(["-C", str(clone), "ls-tree", "-r", "--name-only", "HEAD"])
        tree_paths = [line.strip().replace("\\", "/") for line in tree_output.splitlines() if line.strip()]
        lookup = {path.lower(): path for path in tree_paths}
        candidates = [
            _candidate(path, lookup)
            for path in tree_paths
            if PurePosixPath(path).suffix.lower() in BOARD_SUFFIXES
        ]
        legacy_binary_files = []
        for candidate in candidates:
            if candidate["source_format"] != "eagle":
                continue
            board_format = eagle_storage_format(
                _run_git_bytes(["-C", str(clone), "show", f"HEAD:{candidate['path']}"])
            )
            candidate["eagle_board_storage"] = board_format
            if board_format == "legacy_binary":
                legacy_binary_files.append({"path": candidate["path"], "kind": "board"})
            schematic_path = f"{candidate['project_file_path']}.sch"
            actual_schematic = lookup.get(schematic_path.lower())
            if actual_schematic:
                schematic_format = eagle_storage_format(
                    _run_git_bytes(["-C", str(clone), "show", f"HEAD:{actual_schematic}"])
                )
                candidate["eagle_schematic_storage"] = schematic_format
                if schematic_format == "legacy_binary":
                    legacy_binary_files.append({"path": actual_schematic, "kind": "schematic"})
            else:
                candidate["eagle_schematic_storage"] = "missing"
        selected, excluded = _select_current_candidates(candidates)
        _assign_board_names(selected)
        commit = _run_git(["-C", str(clone), "rev-parse", "HEAD"]).strip()
    too_old = bool(legacy_binary_files)
    ambiguous = []
    for candidate in selected:
        if candidate["source_format"] == "eagle" and not candidate["has_schematic"]:
            ambiguous.append({
                "path": candidate["path"],
                "reason": "Eagle board has no same-basename .sch; board-only Eagle import is not enabled",
            })
    return {
        "repository": full_name,
        "url": url,
        "default_branch": branch,
        "commit": commit,
        "temporary_clone_removed": True,
        "board_file_count": len(candidates),
        "selected_boards": selected,
        "excluded_boards": excluded,
        "legacy_binary_files": legacy_binary_files,
        "ingestion_status": "too_old" if too_old else "ready",
        "ingest_note": (
            "too old: repository contains pre-Eagle-6 binary board or schematic files"
            if too_old else ""
        ),
        "ambiguous": ambiguous,
        "review_required": bool(ambiguous) and not too_old,
    }


def build_project_record(entry: dict, candidates: Iterable[dict]) -> dict:
    full_name = str(entry["full_name"])
    owner, repository = full_name.split("/", 1)
    branch = str(entry.get("default_branch") or "main")
    github_url = str(entry.get("url") or f"https://github.com/{full_name}")
    versions = []
    for candidate in candidates:
        version = {
            "board": candidate["board"],
            "board_name": candidate["board_name"],
            "board_url": f"{github_url}/blob/{quote(branch, safe='')}/{quote(candidate['path'], safe='/')}",
            "version": "current",
            "git_ref": branch,
            "sparse_checkout": bool(candidate["folder"]),
            "project_file_path": candidate["project_file_path"],
        }
        if candidate["source_format"] == "eagle":
            version["source_format"] = "eagle"
        else:
            extensions = candidate["project_file_extensions"]
            if extensions != KICAD_COMPANIONS:
                version["project_file_extensions"] = extensions
        versions.append(version)
    if not versions:
        raise ValueError(f"{full_name}: no selected boards")
    return {
        "github_repository": repository,
        "github_url": github_url,
        "repository_url": f"{github_url}.git",
        "versions": versions,
    }


def append_project_record(
    owner: str,
    project: dict,
    project_data_directory: Path = DEFAULT_PROJECT_DATA,
) -> Path:
    """Append exactly one repository block while preserving existing text."""
    destination = project_data_directory / _normalise_slug(owner) / "working.yaml"
    if not destination.is_file():
        raise FileNotFoundError(f"No project definition file for {owner}: {destination}")
    data = _load_mapping(destination)
    if str(data.get("github_user", "")).lower() != owner.lower():
        raise ValueError(f"{destination}: github_user does not match {owner}")
    repository = project["github_repository"]
    existing = {
        str(item.get("github_repository", "")).lower()
        for item in data.get("projects", []) if isinstance(item, dict)
    }
    if repository.lower() in existing:
        raise ValueError(f"{owner}/{repository} is already declared in {destination}")
    fragment = yaml.safe_dump([project], sort_keys=False, allow_unicode=True).rstrip()
    original = destination.read_text(encoding="utf-8").rstrip()
    original = re.sub(r"(?m)^projects:\s*\[\]\s*$", "projects:", original)
    destination.write_text(f"{original}\n{fragment}\n", encoding="utf-8")
    _load_mapping(destination)
    return destination


def _mark_queue_status(queue_path: Path, full_name: str, status: str, note: str = "") -> None:
    """Change only one repository's status and optional note in the queue text."""
    lines = queue_path.read_text(encoding="utf-8").splitlines()
    target = f'    full_name: "{full_name}"'
    found = False
    changed = False
    for index, line in enumerate(lines):
        if line == target:
            found = True
            for status_index in range(index + 1, min(index + 12, len(lines))):
                if lines[status_index].startswith("  - rank:"):
                    break
                if lines[status_index].strip().startswith("status:"):
                    lines[status_index] = f'    status: "{status}"'
                    next_index = status_index + 1
                    if note:
                        note_line = f"    ingest_note: {json.dumps(note, ensure_ascii=False)}"
                        if next_index < len(lines) and lines[next_index].strip().startswith("ingest_note:"):
                            lines[next_index] = note_line
                        else:
                            lines.insert(next_index, note_line)
                    changed = True
                    break
            break
    if not found:
        raise ValueError(f"{full_name} is not present in {queue_path}")
    if not changed:
        raise ValueError(f"Could not update status for {full_name} in {queue_path}")
    queue_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    _load_mapping(queue_path)


def mark_queue_added(queue_path: Path, full_name: str) -> None:
    _mark_queue_status(queue_path, full_name, "ADDED")


def mark_queue_too_old(queue_path: Path, full_name: str, note: str) -> None:
    _mark_queue_status(queue_path, full_name, "INGESTED", note)


def write_yaml(path: Path, data: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )
    return path


def load_decisions(path: Path | None, inspection: dict) -> tuple[list[dict], list[dict]]:
    selected = list(inspection["selected_boards"])
    llm_decisions = []
    if path is None:
        return selected, llm_decisions
    decisions = _load_mapping(path)
    if decisions.get("repository") != inspection["repository"]:
        raise ValueError(f"{path}: repository does not match inspection")
    include = set(decisions.get("include_paths") or [])
    exclude = set(decisions.get("exclude_paths") or [])
    overrides = decisions.get("overrides", {}) or {}
    known = {candidate["path"] for candidate in selected}
    unknown = (include | exclude | set(overrides)) - known
    if unknown:
        raise ValueError(f"{path}: unknown candidate paths: {sorted(unknown)}")
    if include:
        selected = [candidate for candidate in selected if candidate["path"] in include]
        if include != known:
            llm_decisions.append({
                "kind": "include_override",
                "count": len(known - include),
            })
    if exclude:
        selected = [candidate for candidate in selected if candidate["path"] not in exclude]
        llm_decisions.append({"kind": "exclude_paths", "count": len(exclude)})
    for candidate in selected:
        override = overrides.get(candidate["path"], {})
        for field in ["board", "board_name"]:
            if field in override:
                candidate[field] = str(override[field])
                llm_decisions.append({"kind": field, "path": candidate["path"]})
    return selected, llm_decisions


def run_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def write_json(path: Path, data: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def clean_run_directory(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
