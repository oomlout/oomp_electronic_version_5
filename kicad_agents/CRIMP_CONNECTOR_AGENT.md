# Add cable crimp contacts and housings

You are adding **one verified connector item at a time** to OOMP Electronics.
Read this whole file before editing. Follow the numbered steps; use the checked
pilot as a pattern, not as evidence for another manufacturer's part.

## Assignment and limits

- Start with **header, 2.54 mm pitch**. Do not add other header pitches.
- Add loose crimp contacts and empty cable housings as separate purchasing items.
- Header housings: **black only**. Later JST housings: **white/natural only**.
  These colour limits apply to plastic housings, not metal contact plating.
- Use [the second header batch](CRIMP_HEADER_BATCH_02.yaml) to find the exact
  parts, source documents and current validation status.
- The tin contact and black 1-, 3-, 4- and 5-position housings were the first
  review set. The user approved continuing with the verified 6-, 8- and
  10-position housings. Reuse the reviewed M20-106 drawing for those exact
  order codes and refresh both contact pages for reciprocal compatibility.
- Never create a Cartesian product of wire gauges, finishes, colours, and positions.
  Each row must represent an available, researched part.
- Preserve unrelated edits. Do not commit, push, rebuild boards, sync the project
  snapshot, or run whole-catalogue generation as part of connector ingestion.

## Architecture: where each fact belongs

Check for duplicate manufacturer/order codes and supplier codes before adding a
row. Compare colour, finish, wire range, package and position count before treating
a match as the same product. A shared KiCad footprint is not identity evidence.
Never reuse rejected rows from `working_oomp_populate_lcsc_research_data.py`.
Read the purchasing identity rules in `ADDING_COMPONENTS.md`. Generic catalogue
overlap belongs in `catalogue_relationships`; `related_parts` means verified
compatibility and must not be used for an unverified substitution candidate.

| Layer | File or location | Responsibility |
| --- | --- | --- |
| Classification | `working_oomp_populate_connector.py` | Enumerate component identities; imports the cable-part table. |
| Cable-part table | `working_oomp_populate_connector_crimp_data.py` | Literal taxonomy, exact identity, details, dimensions, drawings, and relationships. |
| Family enrichment | `working_oomp_populate_connector_extra.py` | Applies cable extras last, after older PCB defaults and supplier choices. |
| Evidence | `kicad_agents/component_records/CRIMP_*.yaml` and `parts_source/<id>/research_evidence.yaml` | What was checked, where, when, and what remains unverified. |
| Source record | `parts_source/<id>/working.yaml` | Derived from population; never the only place a fact is edited. |
| Component compilation | `working_oomp.py` | Canonical IDs/codes, actions, page details, and generated metadata. |
| Drawings | `working_oomp_populate_svg.py`, `working_svg.py` | Standard diagram selection and reusable rendering. Geometry stays in the data table. |
| Pages | `source_file/template_jinja/oomp_category/template_jinja_markdown/working.md.j2` | Render details, compatible-component links, evidence, and applicability. |
| KiCad | `working_oomp_populate_kicad.py`, `kicad_agents/kicad_library_agent.py` | Explicitly distinguish cable items from PCB-mounted parts. |
| Output | `parts/<id>/` | README, YAML/web metadata, drawer labels, diagrams, previews, applicability manifest. |
| Browse/index | `navigation/`, `kicad_libraries/` | Shared category pages and library manifest. |

The separate `oomp_electronic_project_version_5` owns boards and uses a frozen
component snapshot. New electronics parts do not appear there automatically.
Only explicitly sync it when requested for a board task. These loose cable items
must not become automatic substitutes for PCB headers in the project matcher.

Also read [Adding components](../ADDING_COMPONENTS.md),
[component records](component_records/README.md), and
[KiCad integration](KICAD_LIBRARY_GUIDE.md). The JLC house-parts queue is a separate
workflow; do not assign a C-number or house classification without verifying it.

## 1. Use the agreed taxonomy

| Level | Crimp contact | Empty housing |
| --- | --- | --- |
| 1 | `electronic` | `electronic` |
| 2 | `connector` | `connector` |
| 3 | Family: initially `header` | Same family |
| 4 | `2_54_mm_pitch` | `2_54_mm_pitch` |
| 5 | `crimp` | `housing` |
| 6 | `1_pin` for a single loose contact | Position count, e.g. `2_pin` |
| 7 | `socket` for the female pilot | Default colour: `black` |
| 8 | Verified wire range, e.g. `22_to_30_awg` | Empty unless a verified distinction needs it |
| 9 | Mating finish, e.g. `gold` | Empty |
| 10–13 | Empty for the pilot | Empty for the pilot |
| 14 | Normalized manufacturer | Normalized manufacturer |
| 15 | Normalized complete MPN | Normalized complete MPN |

Retain `socket`, `_mm_pitch`, and `_pin` conventions used by existing headers.
Single-row counts use `2_pin`, not `1x2`. Keep the real manufacturer spelling and
punctuated MPN in metadata. Do not rename older components during an addition.

For future JST work, reuse the established series tokens `jst_sh`, `jst_ph`,
and `jst_xh` for actual JST items. Existing `ph`/`xh` compatible products are not
proof of JST identity. SH is 1.0 mm, PH is 2.0 mm, and XH is 2.5 mm: do not round
XH to 2.54 mm. Reverify each exact housing/contact pair in JST documentation.

Finish means the **mating-contact finish**. Record termination plating separately.
Use a single consistent token (`gold`, later `tin` when verified); do not mix
`gold_plated`, `gilded`, and `gold` for the same distinction. Do not infer a finish
from colour or from another suffix. Material, plating thickness, and wire range
differences may prevent substitution even within one series.

## 2. Search for duplicates before adding a row

From `C:\gh\oomp_electronic_version_5` (or the actual checkout):

```powershell
rg -n 'M20-1180042|m20_1180042|M20-1060200|m20_1060200' -g 'working_oomp_populate_connector*.py'
```

Replace these MPNs with the assigned item. Search supplier codes and research
records too. Inspect the full row and extras; similar pitch is not equivalent.
Older comments calling through-hole PH/XH headers “housings” are not a template
for an empty cable housing. The old `housing_contact/xh_series` row is also not
the agreed new family/pitch taxonomy. Preserve it unless explicitly migrating it.

## 3. Verify the manufacturer evidence

Read the exact product page and linked drawing. Record source URLs and the actual
check date, full MPN, family, pitch, role, gender, and packaging (loose versus reel).

For a **contact**, verify wire range, mating finish, termination finish, mating
pin size, overall dimensions, compatible housing series, and the specified tool
if making any tooling claim. Do not invent crimp settings.

For a **housing**, verify positions, row arrangement, colour, material, overall
dimensions, compatible contact codes, and whether contacts are supplied separately.
An empty housing has zero conductive pins: its position count is a cavity count.

Capture only facts needed for identity, labels, diagrams, or compatibility. Keep
uncertain fields absent and describe the missing evidence. Do not guess supplier
SKUs, live stock, or JLC assembly availability.

Follow the actual datasheet link rather than constructing one. Use the browser
to download PDFs as required by [Adding components](../ADDING_COMPONENTS.md).
Import a real local download with:

```powershell
python -m kicad_agents.browser_research_agent import-datasheet $partId $downloadedPdf --source-url $datasheetUrl
```

Inspect the saved PDF and its provenance. Only then declare a `file_copy` action.
A linked URL is not a local PDF; never mark a capture or document inspection done
merely because the link resolves. If browser tools fail, record that outcome and
continue source-backed work. A direct-download exception needs the user's instruction.

If the in-app browser automation is unavailable, the user approved the
dedicated Chrome download workflow for this batch. It requires installed Chrome
and Selenium (`python -m pip install selenium` if needed). Use the drawing URL
linked by the exact manufacturer product page and the relevant canonical IDs.
IDs for the same drawing can share a single download command.

```powershell
python -X utf8 -m kicad_agents.browser_research_agent download-datasheet $partId --source-url $datasheetUrl
```

The command opens an isolated Chrome profile, waits for the download, validates
the PDF header and imports it with its source URL and SHA-256. A failure exits
nonzero. If an already imported drawing differs, review the revision before
using the manual import command with `--replace`. Inspect each downloaded
drawing before proceeding. Two Harwin drawings cover the pilot and the batch.

## 4. Preserve exact compatibility links

Use `related_parts` in population data, with `relationship`, `oomp_id`, `name`,
`notes`, and `evidence_url`; use `quantity` where the assembly needs multiple items.
Add the reciprocal relationship to the other existing component's source row.
Both IDs must resolve to real component records and generated README links.

The pilot contact links to its housing. The housing links to the contact with
quantity **2** and says that contacts are not included. This is a documented
manufacturer pairing. A common 2.54 mm pitch and 0.64 mm square post establish
interface dimensions, not proof that an arbitrary “Dupont” housing, contact,
header length, latch, and plating combination will mate correctly.

Do not add matcher aliases or confirmed project usage for loose cable items.
Verified mating PCB headers can be linked later after checking their full
mechanical and contact specifications, without pretending the loose contact is
the footprint of that header.

## 5. Handle drawings and KiCad honestly

The pilot uses product-page **overall envelopes only**. `drawing_note` labels
that limitation in generated pages. It is not a detailed contact/cavity drawing.
Do not infer spring profiles, crimp-wing shapes, cavity sizes, or retention lances.
Upgrade drawings only after examining dimensioned manufacturer evidence.

Keep `pcb_mountable: false`, no header-tail dimensions, and no generic PCB matcher.
The housing has `pins: {}`. The contact has one conductive terminal. No invented
PCB pads should appear in any view; schematic variants are omitted for these
separately stocked cable items.

Their `kicad` selection has `applicability: not_applicable`, blank symbol and
footprints, `allow_project_fallback: false`, and an explicit reason. The library
agent emits an applicability manifest without loading KiCad masters. This is an
intentional non-PCB result, not a missing footprint to fix with a PinHeader master.
An assembled cable connector's schematic representation is a separate decision.

## 6. Prepare and build only the selected component

Use the repository's existing Python environment. The following are the actual
pilot records; prepare **both** before building so their reciprocal sources exist:

```powershell
$contactRecord = 'kicad_agents/component_records/CRIMP_PILOT_01.yaml'
$housingRecord = 'kicad_agents/component_records/CRIMP_PILOT_02.yaml'
python -m kicad_agents.component_addition_agent prepare $contactRecord
python -m kicad_agents.component_addition_agent prepare $housingRecord
python -m kicad_agents.component_addition_agent build $contactRecord --skip-populate --skip-shared-refresh
python -m kicad_agents.component_addition_agent build $housingRecord --skip-populate --skip-shared-refresh
```

When changing existing drawing geometry or titles, append `--regenerate-pngs`
to the affected build command. Otherwise existing previews are deliberately
retained. The explicit regeneration flag now also bypasses the outer preview
existence check. Always inspect the resulting image, not just the command's exit
code. Use `python -X utf8` on Windows if console encoding rejects Unicode.

`prepare` enriches and writes only the selected `parts_source` record. The normal
whole-repository population function rewrites many source records, so do not use
it for this pilot. `--skip-shared-refresh` defers shared indexes; it does not mean
they may be forgotten. Read every command's result and stop on an error.

Refresh the affected navigation ancestors after both builds. The filtered
navigation action now computes shared pages from **all component rows**, preserving
sibling categories while writing only the selected ancestors:

```powershell
python action_generate_navigation.py --filter electronic_connector_header_2_54_mm_pitch_crimp_ --filter electronic_connector_header_2_54_mm_pitch_housing_
python -c "from kicad_agents.kicad_library_agent import package_libraries; print(package_libraries('parts', 'kicad_libraries'))"
```

Package the combined library only once after both builds. This packages existing
assets and applicability records; it does not regenerate other components or
boards. Non-PCB entries contain no native library assets.

## 7. Add a 3D model and render

For new display-only rendering, follow [DISPLAY_RENDER_AGENT.md](DISPLAY_RENDER_AGENT.md).
The user now prefers small render images and recipes without persistent CAD/mesh
exports. The workflow below documents existing connector reference assets;
preserve those assets, but do not create additional STEP/STL exports for a
display-only task. The new pilot adapter currently covers chip resistors; other
families need a reviewed adapter before using it.

1. Search the installed KiCad 3D model directories and the upstream
   [KiCad Packages3D library](https://gitlab.com/kicad/libraries/kicad-packages3D).
   Search the exact MPN and the manufacturer's series variants. Open any match
   and verify the role, row count, position count, pitch and drawing dimensions.
   Example: a solder-tail Harwin M20 board socket has different geometry from
   the M20-106 empty cable housing. The KiCad libraries checked for this batch had
   related M20 board connectors and generic pin sockets.
2. If an exact model is available with redistribution rights, retain its source
   path, version, license and checksum in the part's model provenance. Verify
   the same details for CAD linked from the manufacturer page.
3. For the Harwin M20-106 housings and M20-118 loose sockets, use the reviewed
   local drawing and the parametric [crimp 3D generator](crimp_3d.py). These
   crimp models use OOMP reference geometry. The STEP uses millimetres. The
   housing has one cavity per position on 2.54 mm pitch with simplified cavity
   and retention geometry. The contact has a simplified socket and open crimp
   wings. Consult the drawing for mechanical fit, tool setup and tolerance.

Install CadQuery, Mitsuba, Pillow and OpenCV in the Python environment used for
the repo. The model command is separate from the normal catalogue build, which
can copy existing assets without the rendering dependencies.

```powershell
python -m pip install cadquery==2.8.0 mitsuba==3.7.1 Pillow opencv-python-headless
python -X utf8 -m kicad_agents.crimp_3d M20-1180046 M20-1060100 M20-1060300 M20-1060400 M20-1060500
python -X utf8 -m kicad_agents.crimp_3d M20-1060600 M20-1060800 M20-1061000
```

The selected model command writes `model_3d.step`, `model_3d_render.png` and
`model_3d_source.yaml` under `parts_source/<id>/`. It reopens every STEP and
checks that it contains a single valid solid with the expected envelope. The
PNG comes from the reopened solid. The source YAML records the drawing URL and
checksum, verified dimensions and modeling limits.

The [studio renderer](crimp_studio.py) uses three softboxes and a neutral floor
with contact shadows, following the presentation of the
[OOMP screw product renders](https://github.com/oomlout/oomp_hardware_screw_version_5/blob/main/THREE_D_MODELS.md).
The connector previews use the Mitsuba path tracer, satin tin for the plated
contact and satin black plastic for the housings. The render settings and
material are recorded alongside the drawing provenance. To refresh a preview
from the existing STEP, use:

```powershell
python -X utf8 -m kicad_agents.crimp_3d --render-only M20-1180046
```

Prepare and build only the matching component records with `--skip-populate
--skip-shared-refresh` as described above. Check the three resulting
`data/model_3d*` assets, the README preview and STEP link, and the
web inventory. Open each render and count the housing openings. Check that the
contact shows the socket end and the open crimp wings. Refresh shared indexes
when taxonomy or library contents change.

## 8. Test and inspect the result

```powershell
python -X utf8 tools/run_component_tests.py -q --noconftest --rootdir=. kicad_agents/tests/test_crimp_connectors.py kicad_agents/tests/test_kicad_libraries.py
```

- Confirm one population row per ID, exact MPN, and expected taxonomy.
- Check contact/housing cross-links in both generated pages and stored metadata.
- Inspect actual diagram previews and both drawer-label sizes. Confirm the
  housing says **black**, is empty, and needs two separate contacts.
- Check dimension proportions and the envelope-only note. No PCB tails or pads.
- Confirm `data/kicad/manifest.yaml` says `not_applicable` and has no assets.
- Check current hashes/short codes, navigation links, and `web.yaml`.
- Record whether the local PDF exists. Never clear a document requirement merely
  to pass a full-integration gate. The pilot record explicitly describes the
  narrower envelope test and must not be reported as full integration complete.
- Ensure the project checkout and unrelated component outputs were not rebuilt.

## Pilot findings — 16 November 2026

| Item | Exact identity | Findings |
| --- | --- | --- |
| Contact | [Harwin M20-1180042](https://www.harwin.com/products/M20-1180042) | Loose socket contact; 22–30 AWG; gold mating finish, tin-over-nickel termination. |
| Housing | [Harwin M20-1060200](https://www.harwin.com/products/M20-1060200) | Black single-row, two-position cable housing; manufacturer explicitly lists the pilot contact as compatible. |

The data table holds the canonical IDs; the two `CRIMP_PILOT_*.yaml` records hold
current evidence/build status. Check these records rather than assuming that this
dated summary proves a later run succeeded.

The existing header defaults needed guards in both SVG enrichment and KiCad
selection. Empty housings also needed an explicit applicability outcome, visible
compatibility links, and contact-versus-cavity wording. Those rules are now
covered by targeted regression tests.

Pilot validation completed on 16 November 2026:

- **12 targeted tests passed**, including preservation of PCB-header defaults,
  empty-housing semantics, reciprocal links, filtered navigation siblings, and
  explicit preview regeneration.
- Both component builds and generated-artifact validation passed. Local README
  links resolve, current short codes derive from the new IDs, and both label sizes
  were rendered for review using the installed Arial Narrow font.
- Dimension and title previews were visually checked after regeneration. They
  show envelope dimensions without PCB tails or invented housing pins.
- The pilot's short codes are **9SG8K** (contact) and **4PYH4** (housing).
- Shared navigation retains the existing header categories alongside `crimp`
  and `housing`. The library manifest records both pilot parts as
  `not_applicable`, with no invented assets or missing-footprint review entries.
- Only these two component outputs and their necessary shared indexes were
  built. No JST range or project snapshot was added by this task.

Chrome captured both manufacturer drawings using the download command's workflow.
The contact drawing confirms the gold and tin order codes and calls out a
12.04 mm reference span alongside the 11.70 mm catalogue length. The housing
drawing confirms the position count formula, black PPE+PS and the compatible
loose contacts. Generated diagrams use nominal outer dimensions. See the
manufacturer PDFs for cavity, contact and crimp feature dimensions.

## Handoff format

Report: **ID | exact MPN | source-verified facts | generated/tested outputs |
compatibility evidence | PDF and drawing status | remaining task**.
Stop after the assigned batch and report remaining evidence gaps. Do not expand
to unassigned families or infer parts by multiplying taxonomy combinations.

## JST cable assembly batch

The JST batch covers four wire-to-board families already represented in the connector catalogue.
Use the exact order codes in [the JST cable data table](../working_oomp_populate_connector_jst_cable_data.py).

| Series | Pitch | Tin contacts | Natural-white housings | Drawing |
| --- | --- | --- | --- | --- |
| SH | 1 mm | 1 | 30 PBT housings, with and without end protrusions | [SH catalogue](https://www.jst-mfg.com/product/pdf/eng/eSH.pdf), page 2 |
| GH | 1.25 mm | 1 | 14 PBT housings with standard keying, 2–15 positions | [GH catalogue](https://www.jst-mfg.com/product/pdf/eng/eGH.pdf), pages 2–3 |
| PH | 2 mm | 3 | 15 PA housings, 2–16 positions | [PH catalogue](https://www.jst-mfg.com/product/pdf/eng/ePH.pdf), pages 2–3 |
| XH | 2.5 mm | 3 | 17 PA 6 housings plus 2 resin-filled variants | [XH catalogue](https://www.jst-mfg.com/product/pdf/eng/eXH.pdf), pages 3–4 |

Check the local PDF for each family first. `PDF_OWNERS` identifies the source
folder where the browser workflow stores the original `datasheet.pdf` and
`datasheet_source.yaml`. Siblings reference that folder through
`oomp_datasheet_common_with`. The generated part pages each expose the drawing.
Record the drawing page and keep both wire-gauge and insulation ranges for
contacts. SH '-B' identifies the independent protrusion style here. The plugged
XH variants use 5 mm and 10 mm between active cavities, with a 2.5 mm moulding
grid. Count only active cavities when recording the required contact quantities.
The listed contacts are reel orders. Look up a separate official order code
before adding loose packaging, a gold finish, or another part.

Check KiCad and manufacturer sources for an exact cable-side model. The installed
KiCad `Connector_JST.3dshapes` models checked for this batch were PCB headers.
The [JST model generator](jst_crimp_3d.py) builds reference geometry from the
reviewed catalogue spans and renders the verified exported solid in the same
studio scene as Harwin. The provenance records the local drawing hash and page.
The shell and terminal details are simplified, so use manufacturer drawings for
fit, retention and crimp tooling.

```powershell
python -X utf8 -m kicad_agents.jst_crimp_batch prepare
python -X utf8 -m kicad_agents.jst_crimp_3d all --missing-only
python -X utf8 -m kicad_agents.jst_crimp_batch build all
python -X utf8 action_generate_navigation.py --filter electronic_connector_jst_sh --filter electronic_connector_jst_gh --filter electronic_connector_jst_ph --filter electronic_connector_jst_xh
python -X utf8 -m kicad_agents.kicad_library_agent --package-only
```

The model command also accepts a family or exact MPN. Use Mitsuba's LLVM
backend if available. On Windows, Dr.Jit accepts the full path to
`LLVM-C.dll` in `DRJIT_LIBLLVM_PATH`. The renderer falls back to CPU scalar
rendering. For localized changes, pass a family or exact MPN to the build
command and review individual reports in `generated/component_additions/`.
Refresh the KiCad package once after the batch. Verify all local PDF and model
links, both label sizes, and the reciprocal links and quantities. A PH-style
board header with a BOOMELE MPN uses the `jst_ph` family and keeps its BOOMELE
identity. See the [PH ID migration](../migrations/ph_header_ids.json).
