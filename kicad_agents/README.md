# KiCad processing and OOMP matching agents

These Python agents digest modern KiCad projects (`.kicad_sch` and `.kicad_pcb`) and create a reviewable component dataset. They do not call an AI API. Instead, the matching agent is an explainable command-line tool that an external AI agent can run, inspect, and override.

## Project parts and Roboclick actions

Projects use this taxonomy:

```text
oomp / project / github / user / repository / version
```

`working_oomp_populate_project.py` defines the repository, version, Git ref,
KiCad source folder, file basename, extensions, and project-specific match
overrides. A missing version definition defaults to `current`.

`working_oomp.py` adds two project-only `run_python` action blocks:

1. Clone into the part's ignored `git/` folder, or fetch and `git pull
   --ff-only` when it already exists, using the system Git executable. The
   selected source files are copied to `kicad_file.kicad_pcb`,
   `kicad_file.kicad_sch`, and `kicad_file.kicad_pro`.
2. Parse those canonical files, match components, copy required OOMP component
   sources, draw the board, and rebuild the project part's `README.md`.

Both blocks use an empty `file_test`, so they run every time actions are run.

## Generated structure

```text
generated_data/
  project.json
  project.yaml
  summary.yaml
  generated_manifest.json
  unmatched_parts.json
  unmatched_parts.yaml
  match_overrides.yaml
  src/
    board.svg                   # self-contained board placement drawing
    components/
      <oomp-id>/
        working_svg_outline.svg # local board-use image copy
      manifest.yaml
  project_style.yaml
  project_style_override.yaml   # optional, human-created style overrides
  project_summary_data.json
  project_summary_data.yaml
  components/
    R1/
      component.json
      component.yaml
      schematic/
        working.yaml
        size.yaml
      pcb/
        working.yaml
        size.yaml
      oomp/
        match.yaml
        working.yaml        # exact copy from parts/<matched-id>/working.yaml when matched
```

Every schematic symbol is retained. Power symbols and other non-physical entries receive `not_applicable` match status. Every PCB footprint and every physical schematic component is sent to the matcher. Uncertain physical items are written to both unmatched-parts files.

The project part also has an ignored `project_source/<oomp-id>/` tree. It
contains `working.yaml` and `working_svg_outline.svg` copied from every matched
OOMP part, plus a manifest.

## Deterministic project summary

The project README action calls the processing and summary agents in sequence.
The summary agent can also be rerun independently after `kicad_file.*` exists:

```powershell
python -m kicad_agents.project_summary_agent parts\oomp_project_github_electrolama_pt1_current --parts-dir parts
```

Python compiles the BOM, principal nets, placement statistics, GitHub link,
board dimensions, and `board.svg`. The board drawing reads the KiCad
`Edge.Cuts` geometry and places the matched `working_svg_outline.svg` diagram
for each component at its PCB coordinates and rotation. Component diagrams are
inlined into `board.svg` for reliable rendering, while their local copies stay
in `generated_data/src/components`.

All README prose and facts are compiled by Python; there is no LLM prompt or
LLM-authored sidecar. Optional visual changes belong in
`project_style_override.yaml`; the shared defaults remain in
`styles/style_project_summary.yaml`.

## AI-assisted matching workflow

1. Run the processing agent.
2. Read `generated_data/unmatched_parts.json` or `.yaml`.
3. Ask the matching agent for a fresh ranked result for an individual `component.json`:

   ```powershell
   python -m kicad_agents.oomp_matching_agent `
     parts\oomp_project_github_electrolama_pt1_current\generated_data\components\R1\component.json `
     --parts-dir parts
   ```

4. When the AI can justify a match, add it to `generated_data/match_overrides.yaml`:

   ```yaml
   matches:
     R1: electronic_resistor_0402_5100_ohm
   ```

5. Rerun the processing agent. Overrides are validated against the current `parts` directory and are marked as override-based in `oomp/match.yaml`.

## Measurement policy

- Schematic size includes embedded symbol graphics only. Pin objects, property fields, and graphical text are excluded.
- Footprint output retains separate pad, courtyard, fabrication, silkscreen, and overall non-text bounding boxes.
- Local and placed axis-aligned bounding boxes are expressed in millimetres.
- Schematic connectivity is reconstructed from pin coordinates, wires, junctions, local/global labels, and power symbols.
- PCB connectivity comes directly from footprint pad net assignments.
- A per-component cross-check records named-net agreement or disagreement between schematic pin numbers and PCB pad numbers. It reports source inconsistencies without silently rewriting them.

## Format references

The parser follows KiCad's official modern file-format documentation:

- [S-expression format](https://dev-docs.kicad.org/en/file-formats/sexpr-intro/)
- [Schematic file format](https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/)
- [Board file format](https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/)

KiCad documents these modern formats as UTF-8 S-expressions using millimetre coordinates. The schematic embeds the library symbols it uses, while the board embeds each placed footprint, its graphics, pads, position, and net assignments.
