# Project definitions

Project population is data-driven. Each GitHub user has exactly one file at
`project_data/<user>/working.yaml`; the loader discovers these files in folder
name order.

The smallest useful definition is:

```yaml
github_user: example_user
projects:
  - github_repository: example_board
    versions:
      - project_file_path: hardware/example_board
```

`github_url` defaults to `https://github.com/<github_user>/<github_repository>`
and `repository_url` defaults to that URL with `.git`. `version` and `git_ref`
default to `current` and `main`. Add `board`, `board_name`, `board_url`,
`sparse_checkout`, and the `project_file_*` fields when the repository needs
them. A repository may have multiple version records; `current` is selected in
preference to historical entries, otherwise the newest numeric version is used.

Keep `match_blocked`, `review_notes`, and production metadata alongside the
version that they describe. Do not add reference-level component matches here:
add a reusable, evidence-based rule in `kicad_agents/oomp_matching_agent.py`.

Set `source_format: eagle` for an Eagle `.brd` file. The refresh action retains
the input as `source_eagle.brd`, converts it with `kicad-cli pcb import --format
eagle`, then continues with the standard PCB pipeline. The KiCad CLI does not
offer an Eagle schematic importer, so this path intentionally has no schematic
data.
