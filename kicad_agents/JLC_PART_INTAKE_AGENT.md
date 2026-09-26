# Agent 1: ingest one JLC house part

## Job and working style

You are the OOMP JLC intake agent. Your job is to make ONE verified purchasing
identity available to the OOMP population, save its product-page evidence, and
save its datasheet when possible. A separate integration agent completes the
technical work later. You are not expected to solve the whole catalogue at once.

Work slowly and literally. Follow the numbered steps in order. Read the output
of every command. Write down facts before editing population files. Reuse an
existing pattern only after checking it describes the same kind of part. Do
not use memory, plausible part-number decoding, or a similar product as proof.
An honest unresolved item is better than an invented value. No speed target.

Input: repository root, optional exact JLC C-number, browser and file tools.
Output: one intake-complete item or one precisely documented deferred item.
This is an instruction agent for an AI; the Python modules below perform the
local mechanical work. They do not perform browser research for you.

## 1. Start in the repository and select one part

Use PowerShell at the repository root. Select the existing Python environment:

```powershell
$py = if (Test-Path '.venv/Scripts/python.exe') { '.venv/Scripts/python.exe' } else { 'python' }
& $py --version
git status --short
& $py -m kicad_agents.jlc_house_parts_agent next --stage intake
```

If assigned a code, append `--code C123` to `next`, replacing C123. Copy the
returned code, full MPN, manufacturer, package, category, official URL and
candidates to your working notes. Then set these variables to ACTUAL values:

```powershell
$code = 'REPLACE_WITH_C_NUMBER'
$record = "kicad_agents/component_records/JLC_$code.yaml"
$observed = "kicad_agents/jlc_house_parts/observations/$code.json"
```

Do not execute later commands while a placeholder remains. Inspect
`kicad_agents/jlc_house_parts/progress/<code>.json` if it exists. If intake is
already complete, report that and stop unless explicitly assigned to repair it.
If an observation, record or capture already exists, inspect and resume it;
do not delete it to make scaffolding succeed. Preserve unrelated working edits.

One writer at a time: `next` does not claim or lock a task. Do not spawn another
writer. The captured queue includes Basic and Preferred/Promotional Extended
parts. Its candidates and `generic_id_hint` are search hints, not matches.

## 2. Read the official product page in the browser

Open exactly the returned `jlcpcb_url`. Check the visible page against the row:

| Field | What to copy/check |
| --- | --- |
| JLCPCB Part # | Exact C-number, including every digit |
| Manufacturer | Complete visible name; `--`, blank and unknown are unresolved |
| MFR.Part # | Full orderable MPN with punctuation and suffixes |
| Package | Exact listing text, not a guessed equivalent |
| House class | Raw Basic, Preferred or Promotional wording |
| Function/value | Description AND visible specifications |
| Purchasing limits | Stock, purchase minimum, full reel, available order quantity; assembly minimum only if shown |
| Datasheet | Actual linked URL, if shown |

Copy actual observations; leave absent optional numbers null. Full reel,
purchase minimum and assembly minimum are different quantities. Zero stock
does not invalidate identity. Do not substitute another stocked part.

If navigation times out, inspect the current URL/page once before navigating
again; the requested page may already be loaded. If the page has not loaded,
retry the same known URL once. Record an access blocker if it still fails.
Do not run guessed URL searches in a loop or bypass browser challenges.

If manufacturer, MPN, package or class differs from the queue, record the
conflict and defer. The current helpers reject mismatches. Do not edit the
original browser catalogue or weaken the gate to conceal the disagreement.
An ordinary Extended listing is outside this house-parts intake.

**Known example:** JLC C7171 and C16133 displayed manufacturer `--` and no
datasheet link. LCSC's C7171 product page independently identified Kyocera AVX;
its old catalogue PDF URL said the document link was invalid. Preserve both
observations for resolution. Do not turn `--` into a manufacturer or silently
rewrite the queue. Missing PDF alone is not a reason to defer a sound identity.

## 3. Save browser evidence and attempt the PDF

Use the available browser for all supplier research and downloads. No shell
HTTP, Python HTTP, supplier API, or background scraper. Local reading/copying
of a browser-downloaded file is allowed.

The optional [local capture form](jlc_house_parts/BROWSER_CAPTURE_BRIDGE.md)
can save the rendered page facts and full visible text to
`kicad_agents/jlc_house_parts/browser_staging/<code>.json`. Follow that guide.
It is only an output sink; it does not verify electrical equivalence. If its
server is already running, reuse it; do not start a duplicate server.

Otherwise copy browser-visible facts into
[observed_template.json](jlc_house_parts/observed_template.json), saving it as
the `$observed` path. Fill identity, dates, raw class, description and observed
specifications. Steps 4–5 supply the classification fields. Save the complete
visible product text separately when practical. Label all text captures as
text snapshots, never as complete offline HTML pages.

For the datasheet, LCSC is an approved first choice; it need not be a fallback.
Open the LCSC product page for the same C-number, compare its full maker/MPN
and package, then follow the actual datasheet/download link on that page.
Browser automation may load the page and operate the download. Do not guess a
PDF URL or use a bulk endpoint instead of loading the product page. Record the
LCSC page URL as well as the actual document source. Continue to use JLC's
official page to verify its house classification and assembly listing.

JLC and the exact manufacturer's product page are also acceptable datasheet
sources. Click their actual datasheet link when using them. A JLC download has
often opened a new tab and saved `C<number>.pdf` in Downloads; verify the save:

1. Check the file exists and is nonempty. Inspect its first page locally.
2. Confirm it is a component datasheet covering this part/series, not HTML,
   a compliance certificate, unrelated part, or download error.
3. Record the actual source URL. Remove temporary signed query parameters
   from stored evidence and reports; keep the stable path and source identity.
4. If the chosen source has no usable link, try another of the same-code
   LCSC page, JLC listing or exact manufacturer's page in the browser. Stop
   this first-pass search after a direct fallback is unavailable; write the
   precise remaining task.
5. If the PDF is unavailable, set an empty datasheet URL when none is known
   and add an evidence note explaining the failed/missing download. Continue
   intake if identity and classification are otherwise supported.

Do not infer success from clicking a button or a download API returning. A
previously tracked PDF keeps its actual provenance. Do not label it a new
browser download. Close only the download tabs you opened after the local file
is confirmed. Reuse one research tab; do not leave hundreds of PDF tabs open.

## 4. Decide the OOMP classification using this decision table

Read the relevant family population and extra files. Search each candidate ID,
MPN and C-number in those files and `jlc_house_parts/reviewed_choices.json`.
Use `rg`; on PowerShell use `-g 'working_oomp_populate_*.py'`, not an unexpanded
wildcard filename. Record your chosen ID and why.

| Situation | Action |
| --- | --- |
| Exact same existing device, maker, full MPN and package | Reuse its ID; verify current supplier assignment before changing it |
| Generic passive with matching value/package and compatible ratings | Reuse generic ID and make the verified house identity preferred; preserve previous alternatives |
| Missing generic value/package | Add one explicit row/pair in the existing family |
| Same value/package but lower voltage/power, broader tolerance, different dielectric/polarity or another material difference | Do not replace the existing choice; add a justified rated variant following existing taxonomy, or defer ambiguity |
| Generic ID already has a reviewed house preference | Keep it; the registry allows one preferred code per ID. Represent another SKU as a justified rated/exact variant, linked by `generic_oomp_id` where applicable |
| Active device, array, connector, switch, crystal or otherwise non-equivalent part | Use exact maker/MPN/package taxonomy in its established family |
| Unknown maker, conflicting exact identity, unclear package or duplicate definitions | Defer with evidence; never guess a match |

For resistors compare resistance, package, tolerance, power and voltage where
available. For capacitors compare capacitance, package, voltage, tolerance,
dielectric and polarity. Retain units. An 0402 imperial package is not an
0402 metric package. A higher voltage rating alone does not prove equivalence
when other requirements differ. Brand similarity never establishes pinout.

Worked patterns already in this repository:

- C28233 supplies generic `electronic_capacitor_0805_100_nano_farad` at 100 V.
  C49678 is kept at `electronic_capacitor_0805_100_nano_farad_50_volt`.
- C15008 uses `electronic_capacitor_1206_100_micro_farad_6_3_volt_20_percent`
  so the low voltage and broader tolerance remain explicit.
- C32677 is `electronic_diode_tvs_array_sot_23_protek_psm712_lf_t7`.
  Its downloaded datasheet identifies an RS-485 asymmetrical TVS array;
  classifying it as an arbitrary three-pin diode would lose its function.

These are examples to inspect, not values to copy to a different part.
Normalize taxonomy tokens only; preserve the real maker and MPN in metadata.
Do not rename existing IDs or add a Cartesian product to obtain one new pair.

## 5. Add the minimal population row and create the record

Read [Adding boards and components](../ADDING_BOARDS_AND_COMPONENTS.md),
especially the component population section. Edit
`working_oomp_populate_<family>.py` only if the selected ID is missing. Set
`$partId` and `$family` to the actual chosen ID and existing module family.

For a staged local capture, create the observation using actual values:

```powershell
& $py -m kicad_agents.jlc_house_parts.intake_from_capture $code --part-id $partId --family $family --pin-count 2 --compatibility-notes 'REPLACE with the specific reuse or new-ID decision and rating comparison' --evidence-note 'REPLACE with the exact browser facts and any missing PDF task'
```

The `2` above is valid only for a verified two-terminal part. Replace it for
the assigned device. Establish physical terminal count from evidence; a
package label alone can hide exposed pads or duplicated contacts. If using
the manual observation route, fill `part_id`, `family`, `pin_count`,
`compatibility_notes` and the `evidence_notes` list in `$observed` instead.

```powershell
& $py -m kicad_agents.jlc_house_parts_agent scaffold-intake --code $code --observed $observed
```

Read BOTH generated files: `$record` and
`parts_source/<partId>/web_page_distributor_jlc.txt`. Compare them with the actual
page. Scaffolding refuses to overwrite evidence; when resuming, edit only
the existing target's files after comparing the differences.

If a correct PDF downloaded, set `$downloadedPdf` and `$datasheetUrl` and run:

```powershell
& $py -m kicad_agents.browser_research_agent import-datasheet $partId $downloadedPdf --source-url $datasheetUrl
```

Inspect `parts_source/<partId>/datasheet.pdf` and `datasheet_source.yaml`.
Check source URL, provenance method, size and SHA-256. Use `--replace` only
after comparing an existing file and deciding it should be replaced.

Leave detailed pin mappings, dimensions, drawings and KiCad certification for
Agent 2. Keep `pinout_checked` and `footprint_checked` false and
`visual_review: pending`. `exact_identity: true` means the chosen purchasing
identity is exact even when the OOMP ID is generic.

## 6. Connect the preferred purchasing choice

At the END of `main()` in `working_oomp_populate_<family>_extra.py`, verify
there is one adapter call after the older supplier assignments:

```python
from working_oomp_populate_jlc import apply_reviewed_jlc_choices
apply_reviewed_jlc_choices(extras_dict, family="REPLACE_WITH_ACTUAL_FAMILY")
```

Use the actual family, for example `family="diode"`; the keyword is required.
Keep the call indented inside `main()`. Do not add a duplicate call. The
registry applies only reviewed choices and preserves prior alternatives.

```powershell
& $py -m kicad_agents.jlc_house_parts_agent promote-intake --code $code --record $record
& $py -m kicad_agents.jlc_house_parts_agent intake-check --code $code --record $record
```

Run each command separately; proceed only when it exits successfully and
reports `status: pass`. If the registry already has different facts, compare
them with the record and source. Do not remove that entry to bypass the
guard. A second code on the same ID requires the classification decision in
step 4, not another primary field. Do not hand-edit generated part YAML.

## 7. Complete, or explicitly defer, this one item

Before completion, check every row:

- [ ] Live C-number, maker, full MPN, package and house class verified.
- [ ] Page capture saved, honestly labelled, readable and linked in the record.
- [ ] PDF imported with provenance, or exact absence/failure recorded.
- [ ] One OOMP population row; rating comparison and reuse/add decision recorded.
- [ ] Effective preferred maker/MPN, LCSC C-number and JLC C-number match.
- [ ] Previous purchasing alternatives preserved; no unrelated edits overwritten.
- [ ] `intake-check` reports pass; full-stage flags remain unverified.

```powershell
& $py -m kicad_agents.jlc_house_parts_agent intake-complete --code $code --record $record
& $py -m kicad_agents.jlc_house_parts_agent prepare
& $py -m kicad_agents.jlc_house_parts_agent status
git diff --check
```

Read `progress/<code>.json` and confirm intake is complete. Inspect `prepare`
for duplicate population IDs affecting the target. It refreshes hints, not
generated component assets. An intake addition does not require a full build.

For a blocker, leave evidence and a precise next action, then run:

```powershell
& $py -m kicad_agents.jlc_house_parts_agent defer --stage intake --code $code --reason 'REPLACE: observed problem; URLs/files checked; exact missing fact; next action'
```

Remove only this attempt's unverified purchasing change if it was applied;
preserve prior verified work and captured evidence. Do not call a deferred
part complete. Missing PDF alone can remain an Agent 2 task.

Stop after one code. Report `code | OOMP ID | intake complete/deferred | PDF
saved/missing | remaining task`. If explicitly asked to process a batch,
start step 1 again only after this item has a ledger outcome. Agent 2 receives
the existing record, page capture, PDF/provenance and unresolved notes.
