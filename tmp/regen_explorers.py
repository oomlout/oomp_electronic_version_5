"""Regenerate only the board explorer HTML, reusing saved project + summary data."""
import sys
import traceback
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from kicad_agents.project_html_agent import generate_board_explorer

tokens = [token.lower() for token in sys.argv[1:]]

directories = []
for part_directory in sorted((ROOT / "parts").iterdir(), key=lambda path: path.name.lower()):
    generated = part_directory / "data" / "generated_data"
    if not (generated / "project.json").is_file():
        continue
    if not (part_directory / "data" / "kicad_file.kicad_pcb").is_file():
        continue
    if tokens and not all(token in part_directory.name.lower() for token in tokens):
        continue
    directories.append(part_directory)

print(f"regenerating {len(directories)} board explorers")
failures = []
for index, part_directory in enumerate(directories, start=1):
    output_directory = part_directory / "data" / "generated_data"
    try:
        project_data = None
        project_json = output_directory / "project.json"
        if project_json.is_file():
            import json
            project_data = json.loads(project_json.read_text(encoding="utf-8"))
        summary_data = None
        summary_yaml = output_directory / "project_summary_data.yaml"
        if summary_yaml.is_file():
            summary_data = yaml.safe_load(summary_yaml.read_text(encoding="utf-8"))
        if project_data is None or summary_data is None:
            print(f"[{index}/{len(directories)}] {part_directory.name} skipped (missing saved data)")
            continue
        generate_board_explorer(part_directory, project_data, summary_data, output_directory=output_directory)
        print(f"[{index}/{len(directories)}] {part_directory.name} ok", flush=True)
    except Exception as error:
        failures.append((part_directory.name, str(error)))
        print(f"[{index}/{len(directories)}] {part_directory.name} FAILED: {error}", flush=True)
        traceback.print_exc()
print("DONE failures:", failures)
