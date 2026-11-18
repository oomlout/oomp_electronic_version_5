# Display-render execution runbook

This is a procedural companion to [DISPLAY_RENDER_AGENT.md](DISPLAY_RENDER_AGENT.md).
It is written to let GPT-6.1 Terra carry out repeated, bounded work without having
to reconstruct decisions from chat history. The guide explains the pipeline;
this file specifies the order of operations and the evidence needed to advance.

## 1. Contract and scope

The deliverable for each selected existing component is an inspected studio PNG,
a compact WebP, a provenance manifest, and a component page displaying the image.
This is display work. It does not change electrical specifications, taxonomy,
procurement identity, footprints, compatibility links, or component population.

The default launch prompt covers at most five additional existing **0603 imperial
(1608 metric) chip resistors** using the current adapter. A user's explicit list
replaces discovery; do not silently substitute other IDs. For discovery, prefer
verified variants of the pilot's UNI-ROYAL series, and process exact IDs in a
stable sorted order. A smaller evidence-backed batch is an acceptable result.
An unsupported family needs a separate adapter task, not an improvised recipe.

Do not change the shared studio or renderer during this routine batch. These are
shared inputs and changing them makes other renders stale. Report an implementation
blocker instead of bypassing a guard. Keep duplicate repair paused. Do not change
the separate project checkout, generate the whole catalogue, commit, or push.

## 2. Read and establish the baseline

Read the files in the launch prompt, then inspect these implementation files:

| File | What you must understand before proceeding |
| --- | --- |
| `kicad_agents/display_render.py` | Model and evidence hashes, colour roles, dimensions, output paths, cache and CLI |
| `kicad_agents/package_markings.py` | Exactly which marking policies exist and what they validate |
| `kicad_agents/publish_display_render.py` | Exact component publication and exact-ID compiler selection |
| `working_oomp_populate_display_render.py` | When valid render metadata is included or rejected |
| `source_file/display_render/recipes.json` | Complete approved recipe schema and pilot evidence |

From the actual checkout root, run:

```powershell
Get-Location
git status --short
git diff --stat
Test-Path tmp/display_render_env/Scripts/python.exe
```

Record the initial dirty-file list before editing. Existing uncommitted work may
belong to the user or a previous task. Do not reset, clean, stash, overwrite or
claim ownership of it. Compare your final scope with this baseline.

The render environment normally already exists. Only recreate it if missing:

```powershell
python -m venv tmp/display_render_env
tmp/display_render_env/Scripts/python.exe -m pip install -r requirements-display-render.txt
```

Use this environment for CAD, textures and rendering. Use the normal repository
`python` for publication and repository tests; the isolated render environment
does not contain all the catalogue framework dependencies. Do not globally install
the render dependencies or upgrade an already working environment casually.

Check the pilot without rewriting its output:

```powershell
tmp/display_render_env/Scripts/python.exe -X utf8 -m kicad_agents.display_render electronic_resistor_0603_10000_ohm --check
```

Expected pilot results: marking `01C`, dimensions approximately `[1.6, 0.8, 0.45]`
mm, and 1,332 triangles with the pinned model. This validates the import and
evidence, not the appearance of a newly rendered image. If it fails, diagnose
before creating new recipes. Do not re-pin a changed file merely to make it pass.

## 3. Select and substantiate each candidate

Use `rg --files parts_source` and focused searches in existing population data to
find records. Read `parts_source/<exact-id>/working.yaml` and the relevant supplier
records. Require both an existing source record and an existing generated part.
Do not infer an exact manufacturer MPN by replacing digits in the pilot's MPN.

For each candidate, fill these fields in the batch note before rendering:

| Required field | Acceptance rule |
| --- | --- |
| Exact catalogue ID | Existing directory; no prefix or wildcard selection |
| Selected manufacturer and MPN | An evidenced supplier option belonging to that component |
| Resistance and tolerance | Match the selected MPN and source data, with explicit units |
| Package and footprint | 0603 imperial / 1608 metric, verified model reference |
| Model file | Actual local file, source URL, license, SHA-256, expected bounds |
| Marking scheme | Manufacturer document applicable to this series, size and tolerance |
| Printed text | Independently checked against the document, including line order |
| Evidence | Local PDF path, title/revision, printed page or PDF page distinction, rule, SHA-256 |
| Limitations | Generic geometry and approximate typography/materials; any unresolved facts |

Search existing PDFs and Downloads before downloading anything. The pilot uses
`parts_source/electronic_resistor_0402_0_ohm/datasheet.pdf`: its folder name does not
limit the scope of the shared series document. Read the document to determine
whether it covers your candidate. Do not duplicate a shared PDF into every part.

For new evidence, obey the browser workflow in `ADDING_COMPONENTS.md`. A local
download must exist before importing it. Use the existing research agent's help
and provenance-preserving import command; do not substitute direct HTTP downloads
without user authorization. A browser tab or a URL does not prove capture. A
browser exception recorded for an older connector batch is not blanket permission
to bypass the current workflow. Missing evidence blocks that candidate, not other
independent candidates. Use the PDF skill when inspecting a PDF if available.

For the pilot, UNI-ROYAL page 3 section 4(6) gives significant value 100 as code
`01`, multiplier 100 as `C`: `100 x 100 = 10000 ohms`, so `01C`. Page 4 also has
rules for other values. A supplier ordering suffix `1002` is not proof of a
printed `1002` mark. Generic resistor code `103` is also wrong for this selection.

**Policy limits:** `uniroyal_0603_e96` computes an exact table match. It does not
validate the manufacturer, package or tolerance for you. Its `tolerance_percent`
field is not a substitute for checking the manufacturer's rule. It rejects values
outside its representable table; never round a value or broaden the policy to get
a render. Zero-ohm, underlined E24 and other special cases require separate verified
handling. The renderer now supports `verified_literal` plus `underline: true`
for a reviewed single-line code; arbitrary graphical markings and logos remain
unsupported. `none` means verified absence of a mark, not unknown markings. The renderer
still requires local evidence and its hash for `none`.

## 4. Create one recipe, then validate it

Edit `source_file/display_render/recipes.json` only after the candidate evidence is
complete. Keep existing entries intact. The top level maps exact IDs to recipes;
there is no separate `parts` wrapper. Copy the pilot entry as a structural template,
not as evidence that a different MPN has the same appearance.

For another verified member of the same series and package:

1. Set the new exact ID key, `represented_manufacturer` and `represented_mpn`.
2. Set `marking.resistance_ohm` and `marking.tolerance_percent` from evidence.
3. Retain the policy only if the manufacturer's rule covers this exact variant.
4. Update `marking.evidence.rule` with this value's calculation and printed code.
   Keep the same PDF path/hash only if it is genuinely the same supporting file.
5. Retain the model path, hash, bounds and colour mapping only if the same reviewed
   KiCad model fits. Colour numbers alone are not universal material identities.
6. Keep the pilot's output settings and marking box dimensions for this batch.
7. Keep honest `appearance_status` descriptions. Do not describe generic nominal
   geometry as manufacturer-exact or approximate typography as a photographed lot.

Use a real assigned ID in all commands below. Set it once for the current part:

```powershell
$partId = 'REPLACE_WITH_THE_EXACT_SELECTED_ID'
tmp/display_render_env/Scripts/python.exe -X utf8 -m kicad_agents.display_render $partId --check
```

Read the output. Require the independently expected printed text and dimensions.
On failure, stop this part and fix the evidence or recipe. Do not run subsequent
steps after a nonzero exit code. A PowerShell command sequence does not inherently
stop after a failed external process; inspect each command's result.

Model location is configurable with `--model-root` or
`OOMP_KICAD_3DMODEL_DIR`. `OOMP_KICAD_ROOT` also participates in discovery. Recipe
paths remain relative to the model root. Do not hard-code this computer's KiCad
installation in recipes. Arial Bold (`arialbd.ttf`) is the reviewed marking font;
drawer-label Arial Narrow is a different purpose. `OOMP_MARKING_FONT` can select
an existing font explicitly, but a changed font requires visual review. Never
redistribute proprietary font files in the repository.

## 5. Preview and inspect before spending final-render time

```powershell
tmp/display_render_env/Scripts/python.exe -X utf8 -m kicad_agents.display_render $partId --output "tmp/display_render/$partId/preview" --pixels 700 --samples 32
```

Open the actual resulting `render.png` with the available image-viewing tool.
Compare it with the approved pilot. For every item below, record pass or the
specific defect; do not just write "looks good" without looking at the image.

- Text is the verified code, left-to-right, not mirrored or upside down.
- Characters fit inside the dark coating, with margins and no clipped strokes.
- Ink has no rectangular decal border and does not look thick or embossed.
- Metal covers only the terminations; ceramic and coating remain distinct.
- Both ends are present, the body has plausible proportions, and no face is missing.
- The part sits on the floor with a soft contact shadow; it does not float or sink.
- Broad highlights reveal shape without blown-out metal or crushed-black coating.
- Surface grain is subtle; no concrete texture, deep scratches, or plastic-looking metal.
- Camera framing and background match the pilot; no light panel intrudes into view.

If you cannot view the image, preserve the scratch output and mark the part as
awaiting visual review. Do not publish it. Fix a per-part layout only if supported
by evidence. A change that needs shared renderer/studio code is outside this batch.
Do not overwrite an approved final image with experiments.

## 6. Final render, artifact checks, and publication

After the preview passes:

```powershell
tmp/display_render_env/Scripts/python.exe -X utf8 -m kicad_agents.display_render $partId
```

The recipe defaults are 1,400 square pixels, 256 samples, and a 512-pixel WebP.
The pilot took about 8.6 minutes on scalar CPU; this is a reference, not a deadline.
Run sequentially, keep progress updates going, and wait for the process to finish.
Do not start another render merely because the first is quiet. Do not edit renderer
inputs while a render is running. An LLVM initialization warning followed by scalar
rendering is not itself failure. Confirm the exit code and actual output files.

The final folder is `parts/<exact-id>/data/display_render/`. It should contain only
`render.png`, `preview.webp` and `manifest.json`. Inspect both images. Confirm PNG
dimensions, thumbnail readability, and the same visual criteria as the preview.
Validate the manifest against the selected recipe and actual artifacts. This
read-only command checks image sizes, IDs, hashes and recorded byte lengths:

```powershell
@'
import hashlib, json, sys
from pathlib import Path
from PIL import Image
part_id = sys.argv[1]
recipe = json.loads(Path('source_file/display_render/recipes.json').read_text())[part_id]
folder = Path('parts') / part_id / 'data/display_render'
manifest = json.loads((folder / 'manifest.json').read_text())
assert manifest['part_id'] == part_id
assert manifest['purpose'] == 'display_only'
assert manifest['recipe'] == recipe
assert set(manifest['artifacts']) == {'render.png', 'preview.webp'}
assert {p.name for p in folder.iterdir()} == {'render.png', 'preview.webp', 'manifest.json'}
sizes = {'render.png': recipe['output']['pixels'], 'preview.webp': recipe['output']['thumbnail_pixels']}
for name, expected in manifest['artifacts'].items():
    path = folder / name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected['sha256'], name
    assert path.stat().st_size == expected['bytes'], name
    with Image.open(path) as picture:
        assert picture.size == (sizes[name], sizes[name]), (name, picture.size)
        picture.verify()
    print(name, expected['bytes'], 'bytes; hash and dimensions OK')
print('marking:', manifest['marking']['text'])
print('total bytes:', sum(p.stat().st_size for p in folder.iterdir()))
'@ | tmp/display_render_env/Scripts/python.exe - $partId
```

Read the printed marking and compare it with the independently checked code.
The pilot's three files total about 203 KB. Treat this as a useful comparison,
not a hard size cap; investigate unexpectedly large output or surplus files.

Only after all checks pass, publish with normal repository Python:

```powershell
python -X utf8 -m kicad_agents.publish_display_render $partId
```

This is local catalogue publication, not a GitHub push. It updates the selected
source metadata, generated component data, README and web manifest. The publisher
uses the compiler's exact-ID selection, including when another component ID has
the selected ID as a prefix. Do not replace it with a broad substring command.

Read the resulting README and check that image and provenance links resolve, the
appearance limitations and model credit are present, and `display_render` has
propagated to source/generated `working.yaml` and `web.yaml`. Compare the source
record with its pre-edit version: only display metadata should change semantically.
Do not manually patch generated YAML or README to conceal a publisher failure.
No taxonomy, library index or electrical-image regeneration is needed here.

## 7. Batch validation and recovery

Run once after the completed batch (and after any necessary relevant correction):

```powershell
python -m pytest kicad_agents/tests/test_package_markings.py kicad_agents/tests/test_display_render_metadata.py kicad_agents/tests/test_populate_workflow.py -q
git diff --check
git status --short
git diff --stat
```

The initial pilot had 20 passing targeted tests. Report the actual current test
result, not that historical number. `git diff` omits untracked file contents;
inspect newly added recipes, notes and artifacts too. Separate pre-existing dirty
files from this batch's changes. Do not run the full catalogue as a validation step.

| Symptom | Required response |
| --- | --- |
| Missing model or wrong dimensions | Check installed model root, package convention and footprint reference; no substitute box |
| Model/PDF hash mismatch | Inspect the changed source/revision; never blindly update the pinned hash |
| Unknown colours, assembly or unsupported geometry | Adapter limitation; record and skip, do not classify every face as one material |
| Unsupported value or policy | Verify manufacturer rules; no rounding, generic code, or invented marking |
| Missing font | Locate the installed font or explicitly configure one and review; no silent substitution |
| Preview mirrored/clipped | Do not reverse the intended text to hide a UV defect; record a renderer blocker if needed |
| Cache reused | Valid behavior if current inputs/artifact hashes match; still inspect before first publication |
| Render interrupted | Outputs may be incomplete; do not publish. Resume selected ID and verify the complete set |
| Publisher rejects stale/damaged data | Inspect recipe/studio/code and artifact hashes; do not hand-edit manifest hashes |
| Exact-ID publisher failure | Preserve rendered artifacts and record the error; do not fall back to substring generation |
| New PDFs unavailable | Record the exact tool/error and missing evidence; continue independent verified candidates |

Use `--force` only for a deliberate unchanged-input rerender, not as a cure for
evidence errors. Intact final artifacts can be reused. Temporary meshes and masks
are automatically discarded; do not retain STL, STEP copies, GLB, blend files or
per-part scene exports. Do not delete unrelated temporary work when cleaning up.

## 8. Resumable note and final report

Create `kicad_agents/component_records/DISPLAY_RENDER_BATCH_<YYYYMMDD>_<NN>.md`
with an unused suffix, or update the exact note for a resumed batch. Record facts
as they happen. Suggested template:

```markdown
# Display render batch <date> <number>
Scope: up to five additional existing 0603 resistors; no ingestion or new adapters.
Workspace:
Initial dirty files / baseline reference:
Selected exact IDs:
Shared studio and renderer unchanged: yes/no (explain)

## <exact-id>
State: selected | evidence_verified | recipe_checked | preview_reviewed |
       final_reviewed | published | blocked
Manufacturer / MPN / supporting local record:
Value / tolerance / package:
Model path / SHA-256 / dimensions / license:
Marking document / local path / revision / page / SHA-256:
Independent marking calculation and expected printed text:
Appearance limitations:
Recipe and --check result:
Preview path and visual-check results:
Final paths / visual-check results / dimensions / hashes / total bytes:
Render elapsed time and cache status:
Publisher result and source/generated/web/README checks:
Blocker and exact next step, if any:

## Batch validation
Commands actually run and results:
Files changed by this batch:
Pre-existing unrelated edits preserved:
Remaining work:
```

Advance state only when that stage is observed complete. A recipe is not a render;
a render is not visual review; a reviewed render is not published metadata. On
resume, read the note, verify the stated files still exist and match, then continue
from the first incomplete stage. Do not duplicate completed work automatically.

Finish with exact IDs, manufacturer choices and printed codes, clickable local
preview links (show at least one image when supported), actual checks, file sizes,
limitations, and a link to this batch note. If fewer than five parts completed,
explain the concrete blockers. Do not describe approximate materials or typography
as exact production appearance. Do not claim changes are on GitHub until synced;
this task does not authorize a commit or push.
