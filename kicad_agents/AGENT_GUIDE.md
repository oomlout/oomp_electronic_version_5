# Component workflow

ICs use `electronic_ic_<function>_<subtype>_<package>_<manufacturer>_<mpn>`:
taxonomy levels 3, 4, 5, 14 and 15 respectively. Package is last among regular
fields; IC levels 6–13 stay empty. The ingestion and integration guides use this
same rule, enforced by `component_taxonomy.validate_ic_taxonomy`.

This repository owns component definitions, diagrams, datasheets and KiCad libraries.
[Project processing](https://github.com/oomlout/oomp_electronic_project_version_5)
is independently maintained. See [Adding components](../ADDING_COMPONENTS.md).

Population data -> parts_source -> working_oomp -> component Roboclick actions
-> diagrams, previews, README, web manifest and navigation.

### JLC research instruction agents

These are explicit, sequential instructions for a smaller AI model. Read the
whole assigned guide before acting; take time to check evidence and commands.

| Agent | Role | Completion boundary |
| --- | --- | --- |
| [JLC part intake](JLC_PART_INTAKE_AGENT.md) | Verify identity, classify/reuse/add the OOMP source, set preferred purchasing numbers, save page evidence and attempt a datasheet download. | Intake gate and ledger; missing PDF may be recorded for later. |
| [JLC part integration](JLC_PART_INTEGRATION_AGENT.md) | Complete datasheet evidence, ratings, pins, dimensions, package drawings, KiCad assets, generation and visual review. | Full gate and ledger; unresolved technical evidence is deferred explicitly. |

Use [the dispatcher](jlc_house_parts/WORKER.md) for copyable prompts. Complete
the intake sweep before the full sweep unless assigned otherwise. Work on one
code at a time with one writer; Python helpers validate and generate locally.


### Component-generation agents

| Agent | Role | Notes |
| --- | --- | --- |
| `working_oomp.py` | Compiles `parts_source` into full OOMP parts and defines Roboclick action groups. | Datasheet copies are declared as Roboclick `file_copy` actions. AI illustration actions are disabled unless `enable_ai_assets=True` is deliberately supplied. |
| `kicad_agents/component_svg_action.py` | Roboclick adapter that builds exactly one component's diagrams. | Checks that the action part ID equals the current part folder. |
| `working_svg.py` | Draws all standard SVG variants and their normal PNG versions. | Writes under `parts/<id>/data/`; uses `working_svg_assembly.svg` and a shared assembly line style for board composition. |
| `source_file/template_jinja/oomp_category/template_jinja_markdown/working.md.j2` | Deterministic part-page template. | Receives facts prepared by `working_oomp.add_part_page_details`. |
| Roboclick `image_resize` actions | Build 300-pixel previews without distorting aspect ratio. | Existing PNGs are retained unless `regenerate_pngs` is true. |


### Verification agent

`pipeline_audit_agent.py` scans the core generation sources and every generated
part action list. It reports direct HTTP/LLM imports, default AI actions, or
missing Roboclick Python stages.

```powershell
python -m kicad_agents.pipeline_audit_agent --fail-on-error
```

Outputs are written to `kicad_agents/generated/PIPELINE_AUDIT.md`, JSON, and
YAML.


## Add or change a component

### Fast one-component workflow

The preferred route is `component_addition_agent.py`. It turns the repeated
local steps into one command and prevents accidental project-page churn while
the missing-component list is in progress.

1. Copy the short example from `component_records/README.md` to
   `component_records/<ledger-id>.yaml` and fill it from browser-verified
   evidence.
2. Add the editable array row and explicit populate-extra block as described
   below.
3. Import the browser-downloaded PDF. Re-importing the identical PDF is
   idempotent and repairs missing provenance:

   ```powershell
   python -m kicad_agents.browser_research_agent import-datasheet `
     <oomp-id> <browser-download.pdf> --source-url <verified-url>
   ```

4. Run the preflight check, then the targeted build:

   ```powershell
   python -m kicad_agents.component_addition_agent check `
     kicad_agents/component_records/E0000.yaml
   python -m kicad_agents.component_addition_agent build `
     kicad_agents/component_records/E0000.yaml --regenerate-pngs
   ```

The build runs population, generates the selected component, refreshes its
navigation ancestors, and repackages the KiCad library. Only the component and
its ancestor READMEs run Roboclick actions; other components and project outputs are not rebuilt. It restores `regenerate_pngs: false`, validates the result and
writes a compact report under
`kicad_agents/generated/component_additions/`. Project outputs live in the separate repository and are outside this build.

Generic device families can define `part_number_generic`, a representative
`datasheet_note`, and a `generic_match` dictionary in populate extra. Its plain
`values`, `symbols`, and `footprints` arrays must all agree before the matcher
accepts a generic family. Explicit manufacturer or MPN fields prevent this
fallback, and the result records `identity_scope: generic_family`.

### Why this route is faster

The E0005–E0007 additions showed that exact browser research, readable
populate arrays, explicit extra-data blocks and the SVG/Roboclick pipeline all
work well. The expensive failures were procedural: supplier base-number
matches sometimes hid a different package, browser download controls did not
always behave as direct downloads, datasheets were occasionally copied by hand
without provenance, several commands were needed to build one part, and every
new component received a bespoke test.

The research record now preserves the accepted and rejected identity decision;
the importer makes provenance reliable; and the one-component agent performs
the reusable structural tests automatically. Add a bespoke unit test only for
a genuinely special rule, such as deliberately rejecting a tempting but
incompatible LCSC package.

1. Put common combinations in a short array in
   `working_oomp_populate_<type>.py`. Use ordinary nested loops so adding a size
   or value is a one-line edit.
2. Put an exact MPN, LCSC ID, pinout, or datasheet-copy rule in
   `working_oomp_populate_<type>_extra.py` using an explicit `if` block or an
   easily edited list of dictionaries.
3. If research is needed, use the browser workflow below. Never guess a suffix,
   package, pinout, or dimension.
4. Regenerate the population and selected part:

   ```powershell
   python working_oomp_populate.py
   python -c "import working_oomp; working_oomp.load_parts(filter='exact_or_family_filter')"
   ```

5. Run the part's Roboclick actions. The first action now builds the diagrams;
   following actions build the 300-pixel previews and README.
6. Check the generated `working.yaml`, diagrams, README, and audit, then run the
   tests.

For direct SVG debugging only, this remains available:

```powershell
python working_svg.py --filter exact_oomp_id
python working_svg.py --filter exact_oomp_id --regenerate-pngs
```

Routine builds should use the Roboclick action so generation order is recorded
inside the OOMP part.


## Browser-only research and datasheet workflow

Project research queues are generated in the project repository:

```powershell
python -m kicad_agents.browser_research_agent queue `
  parts\<project-id>\data\generated_data\project.json
```

For every task:

1. Open the generated LCSC and datasheet search links with the available
   interactive browser.
2. Prefer the manufacturer product page and manufacturer datasheet. LCSC is
   useful for supplier identity, stock code, package cross-checking, and a
   datasheet link, but the exact manufacturer suffix still matters.
3. Verify package, pin count/names, footprint dimensions, electrical role, and
   order suffix. Mark uncertain results unresolved.
4. Download the PDF with the browser. If its PDF toolbar appears to do nothing,
   inspect the current UI before retrying. With an API that supports download
   events, start `waitForEvent("download")` before clicking the observed Download
   control, then await that event. Verify the actual downloaded filename on disk
   (the browser may add a suffix such as `(1)`) before importing it. An unchanged
   PDF view or a successful click alone does not prove that the file was saved.
5. Import the browser download through the validating Python boundary:

   ```powershell
   python -m kicad_agents.browser_research_agent import-datasheet `
     <oomp-id> <browser-downloaded-file.pdf> `
     --source-url <manufacturer-datasheet-url>
   ```

6. Add the confirmed URL, MPN, LCSC number, pins, and dimensions to the relevant
   populate-extra file. The populator's `file_copy` entry copies the validated
   local `parts_source/<id>/datasheet.pdf` into the generated part.

The importer refuses non-PDF files and does not overwrite an existing
datasheet unless `--replace` is explicitly provided. It records provenance in
`datasheet_source.yaml`.

For a verified manufacturer drawing URL, the Chrome download command combines
steps 4 and 5. It requires installed Chrome and Selenium. Pass multiple exact
OOMP IDs only when their manufacturer pages link to the same drawing.

```powershell
python -m kicad_agents.browser_research_agent download-datasheet `
  <oomp-id> --source-url <manufacturer-datasheet-url>
```

The command uses a temporary Chrome profile and download directory, records
the source and file checksum, and exits nonzero on failure. Review the imported
PDF before recording drawing details.


## What an LLM may and may not do

An LLM may help a person interpret an ambiguous datasheet, propose a concise
description, or rank future work. That judgement is never used as the sole
source for generated data. Confirmed facts must be written into Python
population definitions, and every normal artifact must remain reproducible
without the LLM.

Default builds must not contain `ai_query`, `new_chat`, or image-generation
actions. Optional decorative artwork can be requested explicitly with
`enable_ai_assets=True`; it is outside the component and project data pipeline.


## KiCad library evidence

Component builds use local official KiCad masters and captured fallback candidates
in `source_file/kicad_library/project_fallback_candidates.json`. They never scan a
project checkout. Preserve ambiguity and `allow_project_fallback` restrictions.
Edit verified component master selections in population data for future changes.

Run `python -m pytest kicad_agents/tests` and
`python -m kicad_agents.pipeline_audit_agent --fail-on-error` before publishing.
