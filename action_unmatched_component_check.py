#!/usr/bin/env python3
"""Scan all OOMP project parts and collect unmatched components into a flat report."""

import os
from datetime import datetime, timezone
from pathlib import Path

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parent
REPORT_PATH = REPOSITORY_ROOT / "report" / "unmatched_components.yaml"
PARTS_DIR = REPOSITORY_ROOT / "parts"
PROJECT_GLOB = "oomp_project_*"
UNMATCHED_SOURCE = "data/generated_data/unmatched_parts.yaml"


def load_unmatched_flat(parts_dir: Path) -> list[dict]:
    """Yield one flat dict per unmatched component."""
    for project_dir in sorted(parts_dir.glob(PROJECT_GLOB)):
        unmatched_path = project_dir / UNMATCHED_SOURCE
        if not unmatched_path.is_file():
            continue

        data = yaml.safe_load(unmatched_path.read_text(encoding="utf-8"))
        components = data.get("components", []) if isinstance(data, dict) else []

        # Load working.yaml for project metadata
        working_path = project_dir / "working.yaml"
        project_name = project_dir.name
        github_url = ""
        if working_path.is_file():
            try:
                working = yaml.safe_load(working_path.read_text(encoding="utf-8"))
                if isinstance(working, dict):
                    project_name = working.get("name_readable", project_dir.name)
                    github_url = working.get("project_github_url", "")
            except Exception:
                pass

        for comp in components:
            fields = comp.get("fields", {}) or {}
            match = comp.get("match", {}) or {}
            reasons = match.get("reasons", []) if isinstance(match, dict) else []

            yield {
                "project_oomp_id": project_dir.name,
                "project_name": project_name,
                "project_github_url": github_url,
                "reference": fields.get("reference", comp.get("reference", "")),
                "value": fields.get("value", ""),
                "footprint": fields.get("footprint", ""),
                "library_id": fields.get("library_id", ""),
                "reasons": reasons,
            }


def build_report(parts_dir: Path) -> dict:
    """Build the full report dict with a flat component list."""
    entries = list(load_unmatched_flat(parts_dir))
    projects_with_unmatched = len({e["project_oomp_id"] for e in entries})

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "projects_scanned": len(list(parts_dir.glob(PROJECT_GLOB))),
            "projects_with_unmatched": projects_with_unmatched,
            "total_unmatched_components": len(entries),
        },
        "unmatched_components": entries,
    }


def main():
    os.chdir(REPOSITORY_ROOT)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    report = build_report(PARTS_DIR)
    REPORT_PATH.write_text(
        yaml.safe_dump(report, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )

    summary = report["summary"]
    print(
        f"Report written to {REPORT_PATH}\n"
        f"  Projects scanned: {summary['projects_scanned']}\n"
        f"  Projects with unmatched: {summary['projects_with_unmatched']}\n"
        f"  Total unmatched components: {summary['total_unmatched_components']}"
    )


if __name__ == "__main__":
    main()
