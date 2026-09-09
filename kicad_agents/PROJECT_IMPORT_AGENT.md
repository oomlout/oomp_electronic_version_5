# Project import agent

Use this procedure exactly. The Python helper owns queue ordering, Git, board
discovery, version selection, names, URLs, YAML formatting, duplicate checks,
and status updates. Do not edit `project_data` manually.

## One-repository loop

1. From the repository root run:

   ```powershell
   python -m kicad_agents.project_import_agent run
   ```

2. If it exits successfully, read the printed `result.yaml`, report the
   repository and board count, then stop. One run imports one repository.

   Python first reads the actual Eagle `.brd` and matching `.sch` blobs. If
   either uses the old binary format, no project definition is added. The queue
   row is marked `INGESTED` with a `too old` note and the run stops successfully.

3. If it exits with code 2, open the printed `inspection.yaml` and adjacent
   `decision.yaml`. Review only entries listed under `ambiguous`.

4. In `decision.yaml`:

   - Keep a path in `include_paths` only when it is a real source board.
   - Put panels, arrays, fabrication copies, backups, and superseded revisions
     in `exclude_paths`.
   - Use `overrides` only to correct `board` or `board_name`.
   - Never invent a path and never change repository metadata.

5. Commit the reviewed packet:

   ```powershell
   python -m kicad_agents.project_import_agent commit --inspection <inspection.yaml> --decisions <decision.yaml>
   ```

6. Run these checks and stop on any failure:

   ```powershell
   python -m pytest kicad_agents/tests/test_project_import_agent.py -q
   python -m pytest kicad_agents/tests/test_agents.py -q -k project_data_declares_one_current_version_per_board
   ```

Never import more than one repository per invocation. Never create historical
version records: every selected board receives exactly one `version: current`
record, and Python chooses the newest revision within a detected board family.
