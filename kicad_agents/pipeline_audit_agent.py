"""Audit the OOMP build pipeline for deterministic, action-driven operation."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

import yaml


FORBIDDEN_NETWORK_IMPORTS = [
    "requests",
    "httpx",
    "aiohttp",
    "urllib.request",
    "openai",
    "anthropic",
]

FORBIDDEN_DEFAULT_ACTIONS = [
    "ai_query",
    "new_chat",
    "image_generate",
]

DETERMINISTIC_SOURCE_FILES = [
    "working_oomp_populate.py",
    "working_oomp.py",
    "working_svg.py",
    "kicad_agents/component_svg_action.py",
    "kicad_agents/component_addition_agent.py",
    "kicad_agents/browser_research_agent.py",
    "kicad_agents/kicad_processing_agent.py",
    "kicad_agents/oomp_matching_agent.py",
    "kicad_agents/project_git_action.py",
    "kicad_agents/project_readme_action.py",
    "kicad_agents/project_review_agent.py",
    "kicad_agents/project_summary_agent.py",
    "kicad_agents/project_html_agent.py",
]


def _import_names(path):
    imported_names = []
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for imported_name in node.names:
                imported_names.append(imported_name.name)
        if isinstance(node, ast.ImportFrom):
            imported_names.append(str(node.module or ""))
    return imported_names


def _action_commands(working):
    commands = []
    action_keys = []
    for key in working:
        if "roboclick" in str(key):
            action_keys.append(key)
    action_keys.sort()
    for action_key in action_keys:
        action_group = working.get(action_key) or {}
        actions = action_group.get("actions") or []
        for action in actions:
            if isinstance(action, dict):
                commands.append(
                    {
                        "group": action_key,
                        "command": str(action.get("command") or ""),
                        "file_python": str(action.get("file_python") or ""),
                    }
                )
    return commands


def run_audit(repository_root):
    repository_root = Path(repository_root).resolve()
    findings = []
    source_checks = []

    for source_relative in DETERMINISTIC_SOURCE_FILES:
        source_path = repository_root / source_relative
        source_check = {
            "file": source_relative,
            "exists": source_path.is_file(),
            "forbidden_imports": [],
        }
        if not source_path.is_file():
            findings.append(
                {
                    "severity": "error",
                    "code": "missing_pipeline_source",
                    "file": source_relative,
                    "message": "Required deterministic pipeline source is missing.",
                }
            )
        else:
            imported_names = _import_names(source_path)
            for forbidden_import in FORBIDDEN_NETWORK_IMPORTS:
                for imported_name in imported_names:
                    if imported_name == forbidden_import or imported_name.startswith(forbidden_import + "."):
                        source_check["forbidden_imports"].append(imported_name)
            if source_check["forbidden_imports"] != []:
                findings.append(
                    {
                        "severity": "error",
                        "code": "direct_network_or_llm_import",
                        "file": source_relative,
                        "message": "Core generation code must use deterministic local data or the browser research handoff.",
                        "imports": source_check["forbidden_imports"],
                    }
                )
        source_checks.append(source_check)

    part_checks = []
    parts_directory = repository_root / "parts"
    if parts_directory.is_dir():
        part_directories = []
        for candidate in parts_directory.iterdir():
            if candidate.is_dir() and (candidate / "working.yaml").is_file():
                part_directories.append(candidate)
        part_directories.sort(key=lambda path: path.name)

        for part_directory in part_directories:
            working = yaml.safe_load((part_directory / "working.yaml").read_text(encoding="utf-8")) or {}
            taxonomy_1 = str(working.get("taxonomy_1") or "")
            taxonomy_2 = str(working.get("taxonomy_2") or "")
            is_project = taxonomy_1 == "oomp" and taxonomy_2 == "project"
            is_component = taxonomy_1 == "electronic" or (
                taxonomy_1 == "mechanical" and taxonomy_2 == "mounting_hole"
            )
            commands = _action_commands(working)
            command_names = []
            python_files = []
            for command in commands:
                command_names.append(command["command"])
                if command["file_python"] != "":
                    python_files.append(command["file_python"].replace("\\", "/"))

            forbidden_actions = []
            for forbidden_action in FORBIDDEN_DEFAULT_ACTIONS:
                if forbidden_action in command_names:
                    forbidden_actions.append(forbidden_action)
            if forbidden_actions != []:
                findings.append(
                    {
                        "severity": "error",
                        "code": "default_llm_action",
                        "part_id": part_directory.name,
                        "message": "Generated working.yaml contains an LLM action in the default pipeline.",
                        "actions": forbidden_actions,
                    }
                )

            required_python_actions = []
            if is_component:
                required_python_actions.append("kicad_agents/component_svg_action.py")
            if is_project:
                required_python_actions.append("kicad_agents/project_git_action.py")
                required_python_actions.append("kicad_agents/project_readme_action.py")
            missing_python_actions = []
            for required_python_action in required_python_actions:
                if required_python_action not in python_files:
                    missing_python_actions.append(required_python_action)
            if missing_python_actions != []:
                findings.append(
                    {
                        "severity": "error",
                        "code": "missing_roboclick_python_action",
                        "part_id": part_directory.name,
                        "message": "Part is missing a required deterministic Roboclick Python action.",
                        "actions": missing_python_actions,
                    }
                )

            part_checks.append(
                {
                    "part_id": part_directory.name,
                    "is_component": is_component,
                    "is_project": is_project,
                    "action_count": len(commands),
                    "forbidden_actions": forbidden_actions,
                    "missing_python_actions": missing_python_actions,
                }
            )

    errors = []
    warnings = []
    for finding in findings:
        if finding["severity"] == "error":
            errors.append(finding)
        if finding["severity"] == "warning":
            warnings.append(finding)
    return {
        "format_version": 1,
        "generated_by": "kicad_agents.pipeline_audit_agent",
        "status": "pass" if errors == [] else "fail",
        "policy": {
            "core_generation": "deterministic Python populated through OOMP and run through Roboclick actions",
            "online_research": "interactive browser only",
            "llm_usage": "optional commentary/research judgement only; never required for generated artifacts",
        },
        "summary": {
            "source_file_count": len(source_checks),
            "part_count": len(part_checks),
            "component_part_count": sum(1 for item in part_checks if item["is_component"]),
            "project_part_count": sum(1 for item in part_checks if item["is_project"]),
            "error_count": len(errors),
            "warning_count": len(warnings),
        },
        "source_checks": source_checks,
        "part_checks": part_checks,
        "findings": findings,
    }


def write_audit(audit, output_directory):
    output_directory = Path(output_directory).resolve()
    output_directory.mkdir(parents=True, exist_ok=True)
    json_path = output_directory / "pipeline_audit.json"
    yaml_path = output_directory / "pipeline_audit.yaml"
    markdown_path = output_directory / "PIPELINE_AUDIT.md"

    with json_path.open("w", encoding="utf-8") as output_file:
        json.dump(audit, output_file, indent=2, ensure_ascii=False)
        output_file.write("\n")
    with yaml_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(audit, output_file, sort_keys=False, allow_unicode=True)

    lines = [
        "# OOMP pipeline audit",
        "",
        f"Status: **{audit['status'].upper()}**",
        "",
        "| Check | Count |",
        "| --- | ---: |",
        f"| Pipeline source files | {audit['summary']['source_file_count']} |",
        f"| Generated parts checked | {audit['summary']['part_count']} |",
        f"| Component parts | {audit['summary']['component_part_count']} |",
        f"| Project parts | {audit['summary']['project_part_count']} |",
        f"| Errors | {audit['summary']['error_count']} |",
        f"| Warnings | {audit['summary']['warning_count']} |",
        "",
        "Core artifacts must be generated with local Python and Roboclick actions. Online identity and datasheet research is handed to the available browser; LLM artwork is optional and disabled by default.",
        "",
        "## Findings",
        "",
    ]
    if audit["findings"] == []:
        lines.append("No policy or wiring errors found.")
    for finding in audit["findings"]:
        location = finding.get("file") or finding.get("part_id") or "pipeline"
        lines.append(f"- **{finding['severity'].upper()}** `{finding['code']}` in `{location}`: {finding['message']}")
    lines.append("")
    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    return markdown_path


def main():
    parser = argparse.ArgumentParser(description="Audit deterministic OOMP/Roboclick pipeline wiring.")
    parser.add_argument("--repository-root", default=".")
    parser.add_argument("--output-dir", default="kicad_agents/generated")
    parser.add_argument("--fail-on-error", action="store_true")
    arguments = parser.parse_args()
    audit = run_audit(arguments.repository_root)
    markdown_path = write_audit(audit, arguments.output_dir)
    print(f"pipeline audit {audit['status']}: {markdown_path}")
    if arguments.fail_on_error and audit["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
