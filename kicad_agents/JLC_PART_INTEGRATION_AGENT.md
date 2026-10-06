# Agent 2: fully integrate one ingested JLC part

## Job and working style

You are the OOMP JLC integration agent. Start with ONE intake-complete part.
The primary deliverable is the generated output the user sees: correct,
good-looking diagrams, README and KiCad assets. Evidence gathering exists to
make those outputs correct, not as an end product.

Be exact where wrong output is visible or dangerous: part identity (maker,
MPN, value), pinout/polarity, body dimensions and the KiCad masters. Be lean
everywhere else: datasheet facts beyond what the diagram, README or gate
fields actually show do not need transcribing. A nice-but-imperfect diagram
shipped now beats a perfect datasheet transcription shipped slowly. Do not
rely on inspiration, memory of a similar component, or attractive-looking
output in place of the source.

Input: repository root, optional C-number, Agent 1's record and evidence,
browser/file tools, and image viewing tools. Output: one full-complete part
with generated assets, or a precise unresolved engineering task. All intake
coverage comes first unless the user explicitly assigns this stage sooner.

## 1. Select and resume one eligible item

Run at the repository root in PowerShell:

```powershell
$py = if (Test-Path '.venv/Scripts/python.exe') { '.venv/Scripts/python.exe' } else { 'python' }
git status --short
& $py -m kicad_agents.jlc_house_parts_agent next --stage full
```

If assigned a code, append `--code C123`, using the real code. Read the existing
`kicad_agents/component_records/JLC_<code>.yaml` and set these variables:

```powershell
$code = 'REPLACE_WITH_RETURNED_C_NUMBER'
$record = "kicad_agents/component_records/JLC_$code.yaml"
$partId = 'REPLACE_WITH_PART_ID_FROM_RECORD'
$family = 'REPLACE_WITH_FAMILY_FROM_RECORD'
```

No placeholder may remain. Read
`kicad_agents/jlc_house_parts/progress/<code>.json`: intake must be complete.
An explicit code can select a previously completed or deferred full-stage item;
verify the ledger so you do not accidentally repeat completed work.
If full is already complete, stop unless explicitly repairing it.

Read the existing record, webpage capture, PDF/provenance, family population
row, family extra block and matching `reviewed_choices.json` entry. Read
[Adding boards and components](../ADDING_BOARDS_AND_COMPONENTS.md). Preserve
unrelated edits. One writer owns these shared files; `next` is not a lock.

Create or resume `parts_source/<partId>/integration_review.md` as a working
checklist. Record: code/ID, full MPN, source URLs, datasheet title/revision,
page references, electrical facts, pin table, dimension table, footprint
comparison, visual checks, commands/results and unresolved work. This note
supplements the YAML; it does not replace the gate's required fields.

## 2. Reconfirm purchasing identity and obtain the actual datasheet

In the browser, reopen the official JLC page. Recheck exact code, maker, full
MPN, package and Basic/Preferred/Promotional class. Record the actual date;
gates require a check within 30 days. Refresh the saved page facts if changed.
Do not silently change the original catalogue when its identity disagrees.

Inspect the existing local PDF before downloading again. Verify its content
and provenance. For a missing/incorrect PDF, LCSC is an approved first choice.
Load its product page for the same C-number, verify maker/full MPN/package,
and follow that page's actual datasheet/download link. Browser automation may
perform these steps. Record both the product page and document source URLs.
Do not skip loading the page or guess a document URL. JLC and the exact
manufacturer's product page are also acceptable sources; use their actual
links when needed. JLC remains the authority for house-part classification.
A series PDF
is acceptable only when its ordering table covers the full selected suffix.
A RoHS certificate, catalogue error page or unrelated series is insufficient.
Record the document revision and both printed/PDF page numbers when different.

Import a newly browser-downloaded file using actual variables:

```powershell
& $py -m kicad_agents.browser_research_agent import-datasheet $partId $downloadedPdf --source-url $datasheetUrl
```

Verify `parts_source/<partId>/datasheet.pdf` and `datasheet_source.yaml`.
Compare existing files before using `--replace`. Preserve honest provenance
for pre-existing PDFs. No HTTP scripts or supplier APIs. Close only your own
completed download tabs; reuse the research tab. Do not print signed PDF URL
tokens in logs or notes.

Missing datasheet is a full-stage blocker when necessary facts cannot be
verified. Record what you tried and the exact document/fact needed. Continue
other verifiable work on this same part before recording the final deferral.

### Fast path: family value extensions (no new download)

Skip the download and the per-part datasheet read when ALL hold:

- the package size is already established by an integrated sibling (generic
  size drawing; no new measurements), and
- the same manufacturer family already has a captured local catalogue whose
  ordering/availability tables cover the exact selected suffix (check the
  local PDF first with a text search, e.g. pymupdf), and
- the code is a value variant of an already fully integrated part
  (typical for extra resistor/capacitor/inductor values in common sizes).

Then:

1. Set `oomp_datasheet_common_with` (the anchor part folder) in the
   populate-extra block. It must live there: the build regenerates
   `parts_source/<partId>/working.yaml` from the extras and drops a
   hand-appended key.
2. Write `parts_source/<partId>/datasheet_source.yaml` directly: copy the
   anchor's sha256/size, name the anchor and shared document, and record this
   part's JLC product URL. `import-datasheet` is not needed.
3. Verify the value against the LOCAL shared PDF with the lightest check
   that proves the suffix — usually the ordering-code decode plus one
   range-table line confirming the size/value is offered. Cite those pages
   in `datasheet_pages`. That satisfies the evidence requirement; do not
   transcribe further tables for value extensions.
4. Still do, per part: live reconfirm, extras block, registry sync, full
   gate, build, diagram refresh, rendered-output inspection, final
   visual_review text, `full-complete`.

Pull and import a new datasheet only when a required fact is genuinely
missing locally: a package size with no local dimensions, a manufacturer or
series with no captured catalogue, or a local table that does not cover the
exact suffix.

## 3. Gather the MINIMUM evidence, then move to the diagrams

Record only what generated output and the gate actually display or require:

- Identity: the ordering-code decode or catalogue/table row that ties the
  exact MPN suffix to value/package (one or two lines, with page).
- Mechanical: body length/width/height (and pitch where relevant) — these
  drive the diagram.
- Pinout/polarity: pin numbers and functions where the part has more than
  two pins or any polarity convention.
- Headline electricals: only the ratings shown in README/diagrams or
  required by the gate's `ratings` dict (value, tolerance, voltage/power,
  dielectric/class or similar — with units and page).

That is typically 3-5 rows. The fuller checklist below is a reminder of what
MAY matter, not a transcription quota — pull an extra row only when a
diagram, the README or an explicit contradiction needs it:

| Family | Checks that may appear in output |
| --- | --- |
| Resistor | Resistance, tolerance, power, working voltage, TCR, size; zero-ohm limit when shown |
| Capacitor | Capacitance, tolerance, voltage, dielectric, dimensions/height |
| Diode/TVS | Function, polarity, current/power with the test condition used on output |
| Transistor | BJT/MOSFET/channel, pin functions, voltage/current/power, gain or RDS(on) |
| IC | Function, supplies, pins, package variant and orientation |
| Inductor/bead | Inductance/impedance with frequency, DCR, rated current, dimensions |
| Crystal | Frequency, load capacitance, pin function, package |
| LED | Colour/polarity, current and forward voltage, pin mapping |
| Connector | Contact count/numbering, pitch, body variant, orientation |

Hard rules that stay: never fill a field with a similar part's value; never
present a graph point as an unconditional rating; if a row you want to show
is unknown, leave an explicit unresolved item rather than guessing. Recheck
the intake classification against what you recorded — an unrated generic ID
must not silently acquire incompatible requirements, and an existing exact
device must not be renamed or repurposed to force a match.

## 4. Make the pin table, then enter pins

Copy the datasheet pin diagram/table into the review note with columns:
`physical pin number | function | electrical type | diagram side/view | page`.
Check all pins, exposed pads, NCs, shields and repeated functions. NC is not
ground. Confirm top view versus bottom view before mapping coordinates.
The count must agree with the record and the selected symbol/footprint.

In `working_oomp_populate_<family>_extra.py`, add explicit data inside the
target's `if current in extras_dict:` block, before the final reviewed-choice
adapter. Copy the structure from the same family/package example:

```python
part["pins"] = {
    "pin_1": {"number": "1", "name": "REPLACE_VERIFIED_FUNCTION", "type": "REPLACE_VERIFIED_TYPE"},
    # One entry for every verified physical terminal; never leave this example.
}
```

Pin numbers are strings. Do not renumber a manufacturer pin to fit a KiCad
symbol. Update `pin_count` in the record when the evidence establishes the
correct physical count. Set `pinout_checked: true` only after the table,
extra data and selected masters have been compared pin by pin.

## 5. Make the mechanical table and package drawing

Record the body length/width/height (plus pitch/overall where the drawing
shows them) with page/figure — that table feeds the diagram, so this is the
one place to be complete. Deeper tolerance mining is optional unless the
drawing shows it. Keep body dimensions separate from recommended PCB land
dimensions. If a nominal value is not stated, document the min/max and any
justified midpoint used for illustration. Never present that midpoint as a
guaranteed limit.

Inspect `working_oomp_populate_svg.py`, the same-package extra example, and
the applicable renderer in `working_svg.py`. Then follow this order:

1. Existing correct renderer: supply the verified dimensions and pin data.
2. Missing package SVG but simple supported geometry: create the package's
   `package_drawing` data in the extra block. This generates its SVG through
   the shared renderer; a missing existing SVG is work to do, not a reason
   by itself to defer.
3. Geometry outside the supported primitives: specify the required reusable
   renderer change with source measurements. Implement it only if you can
   verify its geometry and all affected views. Otherwise leave a bounded
   engineering handoff naming the missing primitive, file and evidence;
   do not use an unrelated package picture or mark full-complete.

The supported `package_drawing` schema from the project guide is:

```text
overall: [width, height]       # centred physical envelope, mm
body: [width, height]          # body, mm
pins: [[number, side, x, y, width, height], ...]
circles: [[x, y, radius], ...] # optional physical features
boxes: [[x, y, width, height], ...] # optional physical features
```

Coordinates use body centre (0,0), x right and y UP. Use a verified orientation
anchor as the first pin row. Inspect the renderer's accepted side labels and
nearest same-style example. Do not invent dimensions to make the picture fit.
Assembly scale is one physical mm per SVG mm. This is a component drawing;
fabrication pads must come from verified KiCad land geometry in step 6.

Put explicit `dimensions_mm` and the appropriate family dimension dictionary
in the extra block; the validator reads family extras directly, before shared
drawing defaults. Add `dimension_reference` with document and page numbers.
Do not hand-edit the generated `parts/<id>/data/*.svg` as a permanent fix.

## 6. Find and compare KiCad masters systematically

Read `working_oomp_populate_kicad.py` and
`kicad_agents/kicad_library_agent.py`. Locate the installed libraries using:

```powershell
& $py -c 'from kicad_agents.kicad_library_agent import Masters; print(Masters().library_root)'
```

Search that printed root's `symbols` and `footprints` folders with `rg` for
the exact MPN, then the verified package. Check each plausible master locally.
Its name is a search hint. Complete this comparison table in the review note:

| Comparison | Required evidence |
| --- | --- |
| Symbol | Every number/function/type and multi-unit mapping; exposed pad and NC treatment |
| Machine footprint | Pad numbers/count, pad positions, pitch, size/shape, drill if any, package orientation and land-pattern dimensions |
| Mechanical fit | Body, overall leads, polarity/pin-1 mark, courtyard and clearance concerns |
| Hand footprint | Actual verified HandSolder master, or an explicitly justified same through-hole master |

Match measurements and pin correspondence to the datasheet, including view
orientation. Never pick a footprint because it has the same pin count. Do
not enlarge machine pads automatically to create a hand-solder footprint.

Set explicit masters in the target extra block:

```python
part["kicad"] = {
    "symbol": "REPLACE_WITH_VERIFIED_LIBRARY:SYMBOL",
    "machine_solder": "REPLACE_WITH_VERIFIED_LIBRARY:FOOTPRINT",
    "hand_solder": "",  # Keep empty if no verified hand master; explain in notes.
    "allow_project_fallback": False,
}
```

Do not leave these placeholders. A missing hand master may be documented
when the generated manifest otherwise satisfies the gate. A missing symbol
or machine footprint prevents full completion. If official masters cannot
represent the device, inspect whether local master support already exists.
Do not invent a library ID or drop an unregistered file in generated output.
Write a precise custom-master task with the pin/land tables and required
source integration. This smaller worker must defer unverified fabrication
geometry instead of pretending a similar master is sufficient.

Set `footprint_checked: true` only after the comparison is complete.

## 7. Add source assets and complete the research record

Keep the house-part PDF at `parts_source/<partId>/datasheet.pdf` because the
component gate expects that path. Preserve other copy actions and add:

```python
{"file_source": f"parts_source/{current}/datasheet.pdf", "file_destination": "datasheet.pdf"}
```

to the target's `file_copy` list only after the source exists. Ensure it is
not duplicated. In the existing record fill `research.evidence_notes`, URLs,
`jlc_selection.ratings` with units/conditions, `datasheet_pages`, compatibility
decision and the verified flags. Keep `visual_review: pending` until step 9.
`datasheet_pages` must identify ordering coverage, pins, dimensions and land
pattern. Do not fabricate project references; retain existing relevant ones.

## 8. Synchronize the reviewed choice and run the source gate

The final family adapter reads `jlc_house_parts/reviewed_choices.json`.
Changing a record alone does not update the population. `promote-intake`
refuses different existing facts, so do not repeatedly rerun it for this edit.

For an existing registry-backed part, the following local script copies ONLY
the target selection after verifying that its code, ID, family, maker and MPN
are unchanged. Read your record first. Run with the actual `$code`:

```powershell
@'
import json, sys
from pathlib import Path
import yaml
code = sys.argv[1]
assert code.startswith('C') and code[1:].isdigit(), 'Invalid C-number'
record = yaml.safe_load(Path(f'kicad_agents/component_records/JLC_{code}.yaml').read_text(encoding='utf-8'))
path = Path('kicad_agents/jlc_house_parts/reviewed_choices.json')
choices = json.loads(path.read_text(encoding='utf-8'))
matches = [x for x in choices if x['code'] == code]
assert len(matches) == 1, 'Expected exactly one existing registry entry'
choice = matches[0]
assert record['ledger_id'] == 'JLC_' + code
assert record['research']['lcsc_part_number'] == code
for key, expected in {
    'part_id': record['part_id'], 'family': record['family'],
    'manufacturer': record['research']['manufacturer'],
    'mpn': record['research']['manufacturer_part_number'],
}.items():
    assert choice[key] == expected, f'Identity change requires separate review: {key}'
choice['selection'] = record['jlc_selection']
path.write_text(json.dumps(choices, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('Updated selection for', code)
'@ | & $py - $code
```

If the choice is hand-written in a family `set_preferred_jlc` call instead,
copy the record's selection there exactly; do not create a second registry
path for the same part. Never overwrite all registry entries from a template.

```powershell
& $py -m kicad_agents.jlc_house_parts_agent intake-check --code $code --record $record
& $py -m kicad_agents.jlc_house_parts_agent full-check --code $code --record $record
```

Read every error. Fix the source or evidence, not the gate. Common causes:
missing explicit family dimensions/pins, wrong datasheet path, stale registry
selection, mismatched exact MPN, or incomplete flag evidence. A gate passing
proves structural consistency; it cannot prove you read the correct pinout.

## 9. Build, then inspect real generated outputs

```powershell
& $py -m kicad_agents.component_addition_agent build $record --regenerate-pngs
```

This refreshes source definitions, builds the selected component, refreshes
navigation and packages libraries. It guards deferred project outputs. It can
write shared indexes; inspect changes rather than assuming only one folder
changed. Do not launch a whole-project build to fix one component.

Open and inspect:

- `parts/<partId>/README.md`: maker/full MPN, JLC/LCSC links, ratings and PDF.
- `parts/<partId>/data/working_svg_outline.svg` and its PNG/300 px preview.
- `working_svg_assembly.svg`, `working_svg_assembly_pins.svg` and their PNGs.
- `working_svg_square_pins.png` and its 300 px preview.
- `parts/<partId>/data/kicad/manifest.yaml` and the actual symbol/footprints
  listed in it; inspect rendered views in KiCad or an available local viewer.
- `kicad_agents/generated/component_additions/JLC_<code>.yaml` build report.

Compare rendered pin-1/polarity, every pin number, body/lead arrangement and
dimensions with the datasheet. Look for mirrored bottom views, missing pads,
labels covering pads, cropped outlines and stale preview images. Check README
datasheet link resolves to the imported file and previous alternatives remain.
Opening only YAML or checking file existence is not visual review. Spend your
attention here: this inspection is what makes the diagrams good.

If wrong, fix the population/drawing/master source, rerun the source gate and
rebuild. Record `visual_review` as two or three sentences naming the files
actually viewed and any known limitation — not an essay. Do not write 'pass'
before looking. Synchronize selection again using step 8, then rebuild once
more so generated YAML contains the final review metadata.

## 10. Finish only after the complete checklist passes

- [ ] Exact current purchasing identity and house status match record and population.
- [ ] Correct PDF exists with honest provenance; ordering suffix is covered.
- [ ] Facts shown in output and required by the gate have units and evidence pages.
- [ ] Every physical pin and symbol/footprint correspondence is checked.
- [ ] Mechanical dimensions and package SVG are evidence-based and rendered correctly.
- [ ] Real symbol and machine footprint are integrated; hand-footprint outcome documented.
- [ ] Datasheet copy, README, diagrams, PNG previews and KiCad assets are generated.
- [ ] Actual images/footprints were viewed; no unsupported geometry or unresolved contradiction.
- [ ] Record, registry/source selection and generated purchasing metadata agree.
- [ ] Build report passes its project-output guard; manifest is complete.

```powershell
& $py -m kicad_agents.jlc_house_parts_agent full-complete --code $code --record $record
& $py -m kicad_agents.jlc_house_parts_agent status
git diff --check
```

Verify `progress/<code>.json` says full complete. The completion command checks
generated consistency, report and manifest; the checklist still requires your
technical and visual evidence. Do not claim completion based on exit code alone.

For ordinary data additions use the per-part gates. If you changed shared
Python generation logic, run its relevant existing tests and inspect affected
rendering; do not add tests that merely repeat literal part data.

## 11. Failure and handoff procedure

Fix routine command/path/data errors and retry the failing step. If evidence or
implementation support remains unavailable, save the exact work state and run:

```powershell
& $py -m kicad_agents.jlc_house_parts_agent defer --stage full --code $code --reason 'REPLACE: exact missing evidence/support; files and sources inspected; next concrete action'
```

Keep valid intake evidence and source work. Remove only new unverified choices
or geometry that would misrepresent the part. Leave false flags for unchecked
items. If research proves the intake identity invalid, also record an intake
deferral and repair that purchasing assignment; do not leave it advertised as
verified. Never disable validation or fill placeholders to make a gate pass.

Stop after one item. Report `code | OOMP ID | full complete/deferred | generated
and visually checked assets | specific unresolved task`. For an explicitly
authorized batch, repeat from step 1 only after this item has a ledger outcome.
