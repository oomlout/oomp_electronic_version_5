"""Re-run kicad process_project (matching) for project parts.

Usage: python tmp/regen_matching.py [name-token ...]
No tokens = all projects.
"""
import sys, time, traceback
from pathlib import Path

ROOT = Path(r"C:/gh/oomp_electronic_version_5")
sys.path.insert(0, str(ROOT))
import os
os.chdir(ROOT)

from kicad_agents.kicad_processing_agent import process_project

tokens = sys.argv[1:]
directories = sorted(d for d in (ROOT / "parts").glob("oomp_project_*") if (d / "working.yaml").is_file())
if tokens:
    directories = [d for d in directories if any(t in d.name for t in tokens)]
print(f"{len(directories)} projects")
failed = []
for index, directory in enumerate(directories):
    t0 = time.time()
    try:
        output_directory = directory / "data" / "generated_data"
        project, _ = process_project(directory, ROOT / "parts", output_directory=output_directory)
        unmatched = [c for c in (project or {}).get("components", []) if c.get("oomp", {}).get("status") in ("unmatched", "ambiguous")]
        print(f"[{index+1}/{len(directories)}] {directory.name} {time.time()-t0:.1f}s unmatched={len(unmatched)}", flush=True)
    except Exception as error:
        failed.append(directory.name)
        print(f"FAILED {directory.name}: {error}", flush=True)
        traceback.print_exc()
print("DONE failed:", failed, flush=True)
