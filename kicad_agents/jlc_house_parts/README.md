# JLC house-parts expansion plan

Prepared 24 September 2026. Deliverable: a captured candidate catalogue, an
OOMP comparison, and a repeatable **two-stage** one-part worker. Catalogue
entries are not bulk-imported. Only individually researched queue items change
the purchasing choice; use `status` for the current approved count.

## Scope and inventory

“House parts” means JLCPCB **Basic plus Preferred Extended**, now labelled
**Promotional Extended** on the official site. Keep those classifications
separate. JLCPCB describes the feeder-loading exemption as applying to Economic
PCBA; do not generalize it to all assembly services or all assembly charges.

| Snapshot inventory | Count |
| --- | ---: |
| Active house-part candidates (2026-09-26 corrected capture) | 1,574 |
| Basic | 83 |
| Preferred / Promotional Extended | 1,491 |
| Active candidates with an existing OOMP hint | 96 |
| Existing distinct electronic OOMP IDs | 1,362 |
| Existing electronic IDs with at least one LCSC code | 910 |

The 96 are **candidate matches**, not approved substitutions. Other rows may
also match existing OOMP entries after research.

## Where the list comes from

1. [Official JLC category](https://jlcpcb.com/parts/basic_parts) is the authority
   for scope. Its initial rendered page displayed 1,586 parts on 24 September.
2. [JLC assembly FAQ](https://jlcpcb.com/help/article/pcb-assembly-faqs) explains
   Basic and Preferred Extended. The category page uses the newer Promotional
   name. Its live counts, not the FAQ's rounded/historical counts, guide discovery.
3. [lrks catalogue](https://lrks.github.io/jlcpcb-economic-parts/) provides the
   practical bulk discovery list, including retired records and source dates.
   [CSV download](https://lrks.github.io/jlcpcb-economic-parts/economic-parts.csv).
   Its [source project](https://github.com/lrks/jlcpcb-economic-parts) documents
   weekly updates and captures the combined Basic/Preferred category without a
   stock-only filter. Do not use its “Active Economic Parts” small-order view
   for completeness: MOQ and stock filters would remove research candidates.
4. [CDFER database](https://github.com/CDFER/jlcpcb-parts-database) and
   [jlcparts](https://github.com/yaqwsx/jlcparts) are alternative discovery sources.
   CDFER's stock-filtered products are unsuitable as the sole exhaustive list.
5. **2026-09-26 corrected re-crawl (current authority):** the official category
   page was crawled in the browser with the category filter held for all
   64 pages × 25 rows, saved as
   `sources/catalogue-browser-official-basic-category-2026-09-26.json` in the
   16-column DOM contract (raw rows with per-page provenance:
   `...-raw.json`). The same-day `catalogue-browser-official-2026-09-26.json`
   capture is **retired as a bad seed**: its pagination dropped the category
   restriction and swept the wider catalogue, so 1,495 of its 1,574 queued
   rows were not house parts at all. The corrected capture holds 1,600 raw
   rows, removes 20 site-side page-boundary duplicates by first-occurrence
   dedupe (the listing's offset pagination overlaps consecutive pages),
   excludes the six non-standard listings without a readable class badge
   (C3116, C4650, C4662, C4664, C4688, C4689), and yields 1,574 standard
   house parts — 83 Basic and 1,491 Promotional Extended. The site's own
   counter reports 1,586 items; offset pagination cannot display all of them
   distinctly, so the verified unique set is the authority. Category and
   package columns are empty: the official listing rows do not carry them,
   and intake must read them from each detail page. On the official category
   the non-Basic badge reads plainly "Extended" (tooltip: Promotional
   Extended); because queue membership now equals category membership, that
   badge maps to the `preferred_extended` house tier instead of triggering a
   class-conflict deferral.

The saved input is a browser DOM capture of the official category listing:
1,600 raw rows over 64 pages, reduced to 1,574 standard codes after
page-boundary dedupe and exclusion of the six unbadged listings. All rows
carry the crawl date **2026-09-26** as `first_seen`/`last_seen`; the raw
per-page harvest is retained beside it with original cells and links. The
input SHA-256 is recorded in `summary.json`.

Equal counts do not prove identical membership, and the listing's offset
pagination overlaps consecutive pages, so a handful of rows shift between
pages while crawling. Every worker must still recheck its actual official
product page. Stock, prices, MOQ and class may have changed.

For a refresh, acquire a new browser snapshot or browser-downloaded CSV, retain
its original bytes, dates, URLs and hash, and compare code sets. The current
parser accepts the saved 16-column DOM format. A new CSV needs an explicit
column adapter; never relabel it as a browser capture. Update the source/date
constants and snapshot-count test intentionally before running `prepare`.
Keep prior snapshots and progress; audit changed/retired choices rather than
silently deleting or replacing accepted parts. Do not run supplier HTTP/API
fetches inside population or generation code.

## Files and commands

| File | Purpose |
| --- | --- |
| [BACKLOG.md](BACKLOG.md) | Human-readable list of every active candidate and OOMP hints |
| [queue.json](queue.json) | Full part facts, URLs, dates, candidates and stable `JLC_C...` work IDs |
| [catalogue.json](catalogue.json) | Normalized complete snapshot, including retired rows |
| [existing_parts_audit.json](existing_parts_audit.json) | Phase-two JLC-number audit of all existing electronic OOMP IDs |
| [summary.json](summary.json) | Coverage, categories and duplicate source IDs |
| [WORKER.md](WORKER.md) | Two-stage dispatch instructions for a smaller AI |
| [MULTI_AGENT.md](MULTI_AGENT.md) | Fan-out protocol: N parallel workers, per-code claims, family locks, staged browser captures |
| [BROWSER_READER_AGENT.md](BROWSER_READER_AGENT.md) | Reader role: record live-page facts into browser_staging; decides nothing |
| [JLC_PART_INTAKE_AGENT.md](../JLC_PART_INTAKE_AGENT.md) | Detailed smaller-model agent: identity, classification, OOMP source, page capture and attempted PDF |
| [JLC_PART_INTEGRATION_AGENT.md](../JLC_PART_INTEGRATION_AGENT.md) | Detailed smaller-model agent: datasheet evidence, drawings, footprints, generation and visual validation |
| [INTAKE_WORKER.md](INTAKE_WORKER.md) / [FULL_WORKER.md](FULL_WORKER.md) | Compatibility entry points forwarding to the two canonical agents |
| [record_template.yaml](record_template.yaml) | Required evidence record; placeholders are not approved facts |
| [reviewed_choices.json](reviewed_choices.json) | Explicitly promoted browser-reviewed purchasing choices applied by family extras |
| `progress/C<number>.json` | Separate intake and full status, written after gates or explicit deferral |

Run in the repository with its existing Python environment:

```powershell
.venv/Scripts/python.exe -m kicad_agents.jlc_house_parts_agent next --stage intake
.venv/Scripts/python.exe -m kicad_agents.jlc_house_parts_agent next --stage full
.venv/Scripts/python.exe -m kicad_agents.jlc_house_parts_agent next --code C25804 --stage intake
.venv/Scripts/python.exe -m kicad_agents.jlc_house_parts_agent status
```

`prepare` rebuilds the comparison in memory from real populate functions,
without writing generated parts. It does not change progress or purchasing
choices. Run it after source additions to refresh candidate hints.

## Implementation order

Work in two sweeps. **Intake** verifies the official listing, classifies or
adds one OOMP purchasing identity, saves the observed webpage and captures a
datasheet when possible. Its gate checks the effective population and saved
page; it does not claim verified pins, footprint or generated ecosystem files.
After intake coverage, the **full pass** completes electrical and mechanical
evidence, missing datasheets, SVG/footprint matching, targeted generation and
visual review. `next --stage full` only selects completed intake items.

1. **Pilot parts:** existing generic resistor C25804, several capacitors, and
   exact regulator C6186 have completed intake. Exercise a missing resistor
   value, an exact active device, and an ambiguous package before unattended
   batches; verify both successful intake and explicit deferral.
2. **Basic first:** process existing-ID candidates, then missing parts. Start
   each model run with one `next` result and `WORKER.md`; one writer at a time
   (for a parallel pool of writers, see [MULTI_AGENT.md](MULTI_AGENT.md)).
3. **Preferred/Promotional Extended:** same process. Preserve stock-zero and
   high-MOQ items as candidates, with availability flags. Do not treat stock as
   identity or remove a part just because it is temporarily unavailable.
4. **All existing parts:** work through `existing_parts_audit.json`. For each
   existing LCSC code, verify that the *same code and exact device* has a JLC
   listing, then add `part_number_jlcpcb` and its verified URL. Ordinary Extended
   listings still get their JLC number. Missing codes require manufacturer/MPN
   research. LCSC availability alone does not establish assembly availability.
   This phase is an audit list; the house-only completion gate intentionally
   rejects ordinary Extended parts. Use the existing component agent for them.
5. **Integrate and refresh:** regenerate affected project bundles only after
   their component batch passes. Check BOM identities and assembly suitability.
   Repeat the supplier snapshot/choice audit periodically when planning orders;
   no scheduled automation is created by this plan.

## Purchasing preference rules

The project's effective primary fields are `manufacturer`,
`part_number_manufacturer` and `part_number_lcsc`. The JLC C-number is also stored
as `part_number_jlcpcb` **after confirming the JLC listing**. These normally have
the same C-number; do not substitute an internal JLC numeric database ID.

Use `promote-intake` after saving and checking one browser research record.
It writes only that choice to `reviewed_choices.json`. The relevant family
extra applies these explicit choices through
`working_oomp_populate_jlc.apply_reviewed_jlc_choices` after its older supplier
defaults; the helper preserves previous primary numbers as alternatives,
updates primary links, and records `jlcpcb_selection`. Existing hand-written
verified choice blocks remain valid. A JLCPCB distributor link is supported by
the normal metadata generator. The discovery queue never flows into production
automatically.

For generics, preserve the OOMP ID and generic meaning. Verify value, package,
tolerance, power/voltage/temperature ratings, dielectric/polarity and any
applicable mechanical constraints. Record the selected manufacturer's limits
as **purchasing-choice ratings**, not a promise about every generic component.
Where the generic definition is underspecified, document that explicitly;
do not infer a universal replacement for projects with stricter requirements.

Choose a compatible Basic part first, then a compatible Preferred part. Within
a class prefer a practical in-stock choice with reasonable MOQ, then stable
availability and cost. Never let price, stock or fee status override correctness.
Keep an existing verified house choice if equivalent; avoid needless churn.
If multiple house SKUs share a generic value/package but have different ratings,
use distinct rated/exact variants linked with `generic_oomp_id` where necessary.
Do not repeatedly overwrite the same generic preference to tick every SKU off.
Escalate taxonomy or equivalence ambiguity by deferring the item.

For exact OOMP identities, preserve the full manufacturer and orderable suffix.
Different packages, pinouts, voltage grades, reel variants or temperature grades
need explicit evidence. A matching base MPN or matching footprint name is only
a search hint. The helper rejects changing an existing exact part's MPN.

Production already uses `part_number_lcsc`. Project overrides and explicit
schematic supplier fields take precedence over the OOMP fallback; changing a
generic preference will **not** override an explicitly specified board BOM.
That precedence is preserved. Part-number enrichment also does not certify CPL
rotations, design ratings or assembly-service eligibility for a particular board.

## Acceptance

An **intake-complete** item has a source population definition, exact supplier
identity, official-page evidence with date, and a saved page text/HTML capture.
Datasheet capture is attempted but optional. A **full-complete** item adds
ratings, pinout, dimensions, datasheet provenance, verified KiCad assets,
targeted generation, rendered diagram/README review and a recorded result.
The deterministic checks verify structure and consistency; the worker must
still inspect the evidence. Each stage has its own explicit deferral reason.

The intake sweep ends when all 1,574 snapshot codes are either intake-complete
or intake-deferred, followed by review of deferrals. Full ecosystem coverage
requires full completion, the existing-part audit and affected project
validation. Deferred parts are **not** counted as successfully added.
