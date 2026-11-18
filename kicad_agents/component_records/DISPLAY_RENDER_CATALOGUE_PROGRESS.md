# Display-render catalogue work

User scope: all remaining catalogue parts for which a display model can be
sourced and labelled. Work in the requested order: resistors, then capacitors,
then ICs; assess other eligible parts after those families. Preserve unrelated
work; do not commit, push or change the separate project repository.

This is an ongoing queue, not a statement that the catalogue is complete.
Use `DISPLAY_RENDER_AGENT.md` for the evidence and visual review gates. The
generic KiCad geometry and illustrative materials do not establish the exact
appearance of every supplier option. Unknown marking policy is not proof that
a part is unmarked.

## Current state, 2026-11-17

- The previous resistor, capacitor and IC examples are published locally and
  remain attributable to their archived renderer. Their evidence and visual
  limitations are in `DISPLAY_RENDER_THREE_FAMILIES_20261117.md`.
- Additional finished, inspected and locally published resistor examples:
  `electronic_resistor_0603_1000_ohm` (UNI-ROYAL `01B`) and
  `electronic_resistor_0603_1200_ohm` (UNI-ROYAL underlined `122`),
  `electronic_resistor_0603_100_ohm` (`01A`) and
  `electronic_resistor_0603_150_ohm` (`18A`),
  `electronic_resistor_0603_200_ohm` (`30A`),
  `electronic_resistor_0603_220_ohm` (underlined `221`) and
  `electronic_resistor_0603_2700_ohm` (underlined `272`), plus
  `electronic_resistor_0805_1000_ohm` (`1001`) and
  `electronic_resistor_0402_1000_ohm` (documented unmarked body).
- Registry contains 222 resistor recipes including the pilot and completed
  examples. Remaining recipes need individual previews, final renders, image
  review and selected-part publication. A recipe is not a completed render.
- `display_render_resistor_queue.py` discovers UNI-ROYAL 0603 candidates only
  when the exact existing supplier record, MPN, footprint and manufacturer
  data match the reviewed datasheet. E96 uses its documented code; E24 values
  outside E96 use a continuous underline. Source records with other suppliers,
  special forms or incomplete evidence require independent review.
- The catalogue includes 701 `electronic_resistor_*` source records, including
  125 0603, 111 0402, 93 0201, 120 0805, 125 1206, 93 axial, and resistor
  arrays and other packages. These are inventory counts, not counts of reviewed
  or eligible recipes. Scanning the other families remains to be completed.
- LLVM 18.1.6 was installed under `%LOCALAPPDATA%/Programs/LLVM-OOMP-18.1.6`.
  Prepend its `bin` to the render process `PATH` to enable the tested LLVM CPU
  backend; scalar remains the supported fallback. Installer exit status was 2,
  but the DLL is present and Dr.Jit reports the LLVM backend available. The
  downloaded installer matched the SHA-256 in Microsoft's winget manifest.
  Pilot-quality 1,400 px / 256-sample 0603 renders took about three minutes
  with LLVM here. After the system drive became nearly full, the downloaded
  installer and unused partial LLVM toolchain executables were removed; the
  working `bin/LLVM-C.dll` remains. Check available disk space before batches.
  Do not lower quality to rush the queue.
- A GitHub Desktop pull stashed the work in progress on 2026-11-17. The stash
  applied cleanly over the pulled connector changes and remains as a backup;
  the previously untracked additions were returned to untracked state.
- KiCad 0402, 0805 and 1206 resistor STEP models were inspected with
  `inspect_display_model.py`; source colours and bounds were recorded during
  the session. They need package-specific recipe and marking evidence review
  before being rendered. The 0201 model was also inspected; axial and array
  models still need inspection.
- `display_render_small_resistor_queue.py` and
  `display_render_large_resistor_queue.py` provide guarded discovery for
  documented 0201/0402 unmarked bodies and 0805/1206 four-digit codes. The
  model- and marking-specific recipes have been added; their initial previews
  were reviewed, and the 0805 and 0402 1 kohm full renders have been accepted.
  The latest reports are under `tmp/display_render/`; regenerate them before
  relying on counts. Datasheet range limits are checked; the 0805 10 MΩ
  boundary and incompatible supplier records need independent review.

## Resume and validation

For actual state, inspect the recipes and each component's
`data/display_render/manifest.json`, generated/source metadata, and README; do
not trust this note alone. A current recipe with no manifest is queued. A
manifest with no matching source/generated display metadata is not published.
Inspect the image and the recorded code before publishing. Confirm artifact and
evidence hashes and run the targeted marking, metadata, texture and publication
tests after relevant code changes. Keep historical renderer source archives and
their LF attributes so earlier image provenance remains verifiable.

The initial 0402 1 kohm full render produced 659 non-finite pixels and was stopped
by the quality guard. A diagnostic render with the bump texture disabled had no
non-finite pixels. The 0201/0402 recipes now specify smooth materials; the final
0402 1 kohm render completed with zero repaired pixels and was published locally.
The current package-size batch also contains 0201 0 ohm and 1206 1 kohm; inspect
their actual manifests and pages for the latest state before resuming.

## Recovery and reviewed 0603 batch (2026-11-17)

The GitHub Desktop stash was applied cleanly over the pulled checkout. All 105
stashed paths were accounted for, and the stash was retained as a backup. The
latest reviewed 0603 shared-pass batch contains the 1 M, 100 k, 13 k, 1.5 M,
150 k, 15 k, 1.5 k, 2 M, 200 k, 20 k, 2 k and 49.9 k ohm parts. Their
full-size images and recorded marking codes were inspected as a contact sheet
before their component pages were updated. The 10 M ohm shared-pass pilot was
also reviewed and published locally. These images use the documented
shared-pass approximation; inspect each manifest for provenance. The 0201
0 ohm and 1206 1 k ohm examples were also accepted and published locally.
The focused regression suite passed 67 tests after recovery. Continue with
unrendered evidenced resistors, then capacitors and ICs; recipes without
rendered, reviewed and published artifacts remain queued.

A further 20 evidenced 0603 resistors were visually reviewed in the second
contact sheet and published locally; inspect their manifests for the exact IDs.

## Small-package coverage and 0805 experiment

All 173 existing 0201, 0402 and 0603 recipes now have individually valid
render provenance and published README references. The unmarked 0201/0402
images reuse inspected direct renders only when visual recipes match exactly;
each manifest and page explicitly discloses reuse and retains the individual
part evidence. The current UNI-ROYAL and FOJAN source records were rechecked
against all 91 small-package recipes. The full targeted suite passed 68 tests.
The compositor has been extended to validate 0805/1206 model identities and
marking bounds; do not treat those paths as visually approved for batch use
until shared-pass results have been compared against the existing independent
full-quality pilot for each package. Older compositor source was archived to
preserve the 0603 renders' provenance.

The independent 0805 and 1206 1 kΩ pilots have now been compared to their
shared-pass equivalents at 1,400 px; whole-image mean absolute channel
differences were 0.168 and 0.142 / 255 respectively. Both side-by-side images
were visually inspected. Other markings still require batch review. Both
package-specific masters were built.

## Further resistor discovery

All 289 current resistor recipes have validated provenance and README image
references. A read-only classification found 31 YAGEO 0201 and 20 YAGEO 0402
source records outside the queue. YAGEO's RC_L product specification V.12,
page 3, identifies RC0201 and RC0402 as unmarked; review the exact MPN, value,
tolerance, footprint and model dimensions for each record before adding any.
The manufacturer-authored datasheet was inspected online at
https://robu-prod-media.s3.ap-south-1.amazonaws.com/uploads/2025/08/C137992.pdf
(no local PDF download is claimed). Older manufacturer-authored RC_L V.8 has
the same unmarked rule:
https://robu-prod-media.s3.ap-south-1.amazonaws.com/uploads/2024/07/C141683.pdf
Build a guarded YAGEO MPN parser and evidence note, test it, and extend the
unmarked reuse helper only after this source review. Other missing groups
include through-hole parts, resistor arrays and additional supplier series;
continue researching those rather than treating the current queue as complete.

A guarded RC_L YAGEO adapter now checks the exact part number, value, tolerance,
manufacturer entry, footprint and documented range. It selected 49 records;
AF and AC parts remain excluded for separate research. Online evidence is in
`DISPLAY_RENDER_YAGEO_EVIDENCE.md`. The unmarked reuse helper verifies each
record against that adapter. After adding the adapter, the focused suite passed
75 tests. Check actual manifests and pages for batch completion on resume.

All 49 checked YAGEO RC_L 0201/0402 pages have now been published locally.
The 338 current resistor recipes were checked together: every one has valid
render provenance and a README image reference. This is not complete catalogue
coverage: additional resistor supplier series, through-hole resistors and
arrays need research, followed by capacitors and ICs as requested.

## FOJAN E24, UNI-ROYAL 5% and Fenghua RC (2026-11-17)

Added and published 15 source-verified FOJAN 0603 E24 exceptions with a short
underline beneath the middle character, ten UNI-ROYAL 5% variants with their
three-character marks, and eight unmarked Fenghua RC small-package parts.
Fenghua RC evidence was inspected online and is recorded in
`DISPLAY_RENDER_FENGHUA_EVIDENCE.md`; no local manufacturer PDF is claimed.
The renderer supports a checked character underline. A 700 px / 128-sample
direct FOJAN preview was compared visually with the 1,400 px / 256-sample
shared-pass output; their mean whole-image difference at preview size was
0.36/255. A package alias validation bug was fixed and tested. Historical
renderer and compositor versions remain archived by hash. All 371 current
resistor recipes have valid provenance and README references; the focused suite
passed 85 tests. Additional resistor series, through-hole parts and arrays
still need research, followed by capacitors and ICs.

## Array research for next pass

KiCad contains valid `R_Array_Convex_4x0402.step` and `R_Array_Convex_4x0603.step`
models. Their inspected SHA-256 hashes are respectively
`36ded1f7b7c9e9dcddde3eb3200acdf1c0e0b60046893660e6f043afc2ec7fad` and
`bec072c4d44e4c5ff693e18ede4078c7e66e7a670d53b00a20edd2c0aecdf3c2`; bounds
are 1 × 2 × 0.35 mm and 1.6 × 3.2 × 0.5 mm respectively. They have coating,
ceramic and termination face colours matching the inspected resistor models.
Fenghua's manufacturer-authored RC-M network datasheet was inspected online:
https://szsdmdz.com/wp-content/uploads/2024/12/%E9%A3%8E%E5%8D%8E%E9%AB%98%E7%A7%91-%E5%8E%9A%E8%86%9C%E7%89%87%E5%BC%8F%E7%BD%91%E7%BB%9C%E7%94%B5%E9%98%BB%E5%99%A8-7.0.pdf
It describes RC-MT08W as a four-resistor, eight-terminal convex array, gives
nominal 2 × 1 × 0.45 mm dimensions (the KiCad height is at the tolerance
limit), shows a marked top and gives the value-code/decimal convention. Do not
apply the unmarked rule for standalone 0402 resistors to these arrays. Verify
the top-face layout, text orientation, pin appearance and individual source
records before developing and reviewing an array-specific render adapter. No
local PDF has been captured.

## Reviewed convex resistor arrays (2026-11-17)

Published 21 four-resistor convex array pages: ten 4×0402 and eleven 4×0603
Fenghua, UNI-ROYAL and RALEC examples with source-backed value marks. The local
Fenghua and UNI-ROYAL array drawings were inspected visually; the RALEC local
specification provides its value rules and dimensions. A 0603 source uses the
valid `Device:R_Pack04_Split` symbol, which is accepted alongside `R_Pack04`.
The rotated marking adapter accounts for the model's physical dimensions.
Independent full 1,400 px direct renders and shared-pass results were compared:
whole-image mean channel differences were 0.221/255 for 4×0402 and 0.022/255
for 4×0603. Shared-pass outputs record their approximation. KiCad array STEP
headers identify GPL-3.0-or-later with a source-file exception; the recipes
record that rather than assuming the individual-resistor license. All 392
current resistor recipes have valid provenance and README image references;
the focused suite passed 94 tests. Other array, resistor, capacitor, IC and
non-resistor families still require evidence and model work.

## Axial resistor research

Several remaining quarter-watt records have exact YAGEO MFR-25 manufacturer
parts and use KiCad footprint R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal.
The corresponding installed STEP model is valid, SHA-256
`46710ac36957e4073ef7e80153823ef7db1ea12932074cb71f43bc4b476a74dc`,
with overall bounds 8.22 × 2.50 × 5.50 mm including bent leads. Its body lies
along X from 0.66 to 6.96 mm. The manufacturer-authored YAGEO MFR specification
reviewed online at https://robu-prod-media.s3.ap-south-1.amazonaws.com/uploads/2025/02/2499275.pdf
gives MFR-25 nominal body dimensions 6.3 × 2.4 mm and 1% five-band marking.
No local PDF has been captured. A new axial adapter should project explicit
coloured bands along X around the cylindrical body, distinguish tolerance and
orientation, verify each exact MPN/value, and inspect a direct full-quality
render before batching. Do not reuse flat chip-resistor text as colour bands.

## Axial colour-band pilot (2026-11-17)

The YAGEO MFR-25 axial adapter uses the inspected KiCad DIN0207 bent-lead STEP
model and a cylindrical X-axis band texture. The 1.2 kΩ pilot was rendered at
1,400 px / 256 samples, visually reviewed and published locally with five
manufacturer-supported bands. The blue coating and band shades/spacing are
illustrative. Manufacturer evidence is recorded in
`DISPLAY_RENDER_YAGEO_AXIAL_EVIDENCE.md` (reviewed online, no local PDF).
Sixteen exact 1% YAGEO source records were identified; mixed-tolerance, jumper
and other series remain excluded. The focused suite passed 100 tests. Additional
full-quality previews and synthetic light-pass calibration are in progress;
verify their actual files and manifests before publishing. A grey band in the
first 18 Ω render was too close to the blue body and needs a darker illustrative
shade and a new reviewed render before publication.


## Beige axial finish and tolerance preference (2026-11-17)

The user requested traditional beige for axial resistors and prefers a gold
tolerance band. The renderer and agent instructions now select a beige axial
coating; 5% parts use gold, but the existing 1% YAGEO parts must keep their
brown tolerance bands. Select a verified 5% part where appropriate; do not
mislabel a 1% part as 5%. The updated coating was reviewed in a 700 px / 128
sample direct preview at `tmp/display_render/beige_preview/render.png`. The
16 reviewed YAGEO 1% recipes have been regenerated in beige and published
locally. Two independent 1,400 px / 256-sample material passes are stored in
`source_file/display_render/masters/105133288f4358f35c80d6d71e6bdf0e9ea6cfb9e72bd3a7fd8ac31bd020c00b`;
each output records the source hashes and the approximation of indirect
reflections. A 700 px direct comparison differed from the shared-pass result
by a mean of 0.37/255 per channel. All 409 published resistor recipes have
valid provenance and README references. The focused suite passed 102 tests.

A suitable gold-band candidate for the next rule is the catalogue's 6.8 kΩ
YAGEO CFR-25JB-52-6K8, specified as 5% in its source record. The
manufacturer-authored CFR specification (reviewed online only) documents
the four-band code and gold 5% tolerance:
https://s3.amazonaws.com/snapeda/datasheet/CFR-12JB-52-1M_Yageo.pdf
Its correct bands are blue / grey / red / gold. A separate four-band recipe,
texture rule and evidence record were added. Its directly rendered 1,400 px /
256-sample image was reviewed and published locally with its README.
The existing five-band compositor must not be used to invent a fifth band.


## RALEC RTT05/06 batch (2026-11-17)

Published 21 reviewed RALEC 0805 and 1206 resistor renders and individual
README updates. Their exact primary part numbers, values, tolerance, decimal
or exponent marking format and footprint are checked by
`display_render_ralec_rtt_queue.py`. The reviewed RALEC 2011 marking table
and 2024 dimensions are linked in `DISPLAY_RENDER_RALEC_RTT_EVIDENCE.md`;
the PDFs were read online and were not downloaded. The shared-pass render
approximation is disclosed in each output. Manufacturer 1206 body length is
3.05 ± 0.10 mm, while the generic KiCad display model is 3.20 mm; the
discrepancy is explicitly stated in those component descriptions. The ID
`electronic_resistor_0805_1_ohm_uni_royal_uniroyal_elec_rtt051r00ftp`
claims UNI-ROYAL in its taxonomy but RALEC in its source; it was not changed
or rendered and needs an identity review. The focused suite passed 29 tests.
All 430 resistor recipes currently pass render provenance checks and have
README image references. Continue researching remaining resistor entries,
then capacitors and ICs in the requested order.


## UNI-ROYAL low-value batch (2026-11-17)

Published 26 reviewed renders and READMEs for the UNI-ROYAL 0603 zero-ohm
jumper, a 0603 E96 49.9-ohm part, and 0805/1206 low-value parts. Their
manufacturer, exact MPN, value, footprint and decimal marking are checked
by `display_render_uniroyal_low_value_queue.py`. The local UNI-ROYAL 2019
manufacturer data sheet, pages 2–4, was inspected visually; 0805/1206 1%
marks use R as the decimal point while 0603 1% E96 uses its separate code.
Three non-E96 0603 values need separate evidence for the underlined low-value
mark; they were not guessed. Shared-pass rendering and its indirect-light
approximation are disclosed in each output. The focused suite passed 27
tests. All 456 resistor recipes currently pass provenance checks and have
README image references. Continue remaining resistor research, followed by
capacitors and ICs; this count is not catalogue completion.


## FOJAN low-value batch (2026-11-17)

Published 18 exact FOJAN FRC 1% parts: five 0201/0402 unmarked packages,
four 0603 packages, and nine 0805/1206 packages. The 2023 FOJAN manufacturer
specification was reviewed online and recorded in
`DISPLAY_RENDER_FOJAN_LOW_EVIDENCE.md`; no local PDF is claimed. The queue
`display_render_fojan_low_queue.py` verifies primary identity, value, tolerance
and footprint, and applies package-specific decimal, E96 and middle-character
underline rules. Reused images and shared-pass approximations are disclosed.

A first scratch preview silently omitted an underline because an old archived
renderer lacked `underline_character` support. It was rejected before
publication and regenerated with the compatible renderer. All 15 earlier
published FOJAN middle-underline manifests use that compatible source; a
previous example was visually inspected. Metadata now rejects any character-
underline recipe whose recorded renderer lacks support. The focused suite
passed 34 tests. All 474 resistor recipes pass provenance checks and contain
README image references. Remaining resistor records still require review,
followed by the requested capacitor and IC work.


## Fenghua RS 5% batch and source conflicts (2026-11-17)

Published seven non-conflicting Fenghua RS-05/06 5% renders and READMEs.
The manufacturer R-6.1 approval sheet is linked in
`DISPLAY_RENDER_FENGHUA_RS_EVIDENCE.md` and was reviewed online.
`display_render_fenghua_rs_queue.py` checks primary identity, exact value,
footprint and both explicit tolerance fields; it refuses conflicting records.
The seven selected parts had a stale generated UNI-ROYAL PDF and inaccurate
source attribution. Their PDF copies and shared references now use the
existing local Fenghua family datasheet from
`parts_source/electronic_resistor_0402_150000_ohm_5_percent/datasheet.pdf`;
source and previous PDF backups are in `tmp/display_render/fenghua_rs_previous_docs`.
Each corrected PDF hash was checked after page generation.

Eleven other catalogue entries have electrical tolerance 1% but a selected
Fenghua J/5% MPN and JLC 5% rating. They were excluded rather than silently
changing part specifications: 0805 110 Ω and 1206 110 Ω, 1.3 kΩ, 160 Ω,
180 kΩ, 27 kΩ, 3.6 kΩ, 560 kΩ, 68 kΩ, 7.5 kΩ and 8.2 kΩ. Reconcile the
selected supplier and intended tolerance before rendering these. The focused
suite passed 24 tests. All 481 resistor recipes currently have valid render
provenance and README references. Remaining resistors, capacitors and ICs
still require review and rendering.


## Additional UNI-ROYAL small packages (2026-11-17)

Published eight manufacturer-documented unmarked packages: six 0201 5% E24
parts and two exact-MPN 0402 1% variants. Their images reuse reviewed 0201
and 0402 KiCad model renders with explicit reuse provenance. Extended
`display_render_small_resistor_queue.py` to validate the 5% MPN format, E24
value, any explicit tolerance and variant suffix before accepting these parts.
The six 0201 records now link the existing local UNI-ROYAL family datasheet;
the generated PDF copies and README links were verified after targeted page
updates. Their earlier source records are backed up under
`tmp/display_render/uniroyal_small_previous_sources`. The focused suite
passed 28 tests. All 489 resistor recipes have valid render provenance and
README references. Remaining resistors and the later capacitor and IC work
still require review.


## Walsin, YAGEO and KOA 0201 parts (2026-11-17)

Published five manufacturer-verified unmarked 0201 parts: Walsin
WR02X155JAL, YAGEO AF0201FR-07560KL, KOA RK73B1HTTC275J and
RK73B1HTTC395J, and KOA RK73H1HTTC7501F. Each uses the inspected KiCad 0201
package image with explicit reuse provenance. Manufacturer-authored marking
documents were reviewed online and are linked in
`DISPLAY_RENDER_MULTI_0201_EVIDENCE.md`; no local PDF is claimed. The
`display_render_multi_0201_queue.py` adapter limits reuse to those exact
source identities and footprint. SAE 0201 records need manufacturer-specific
marking evidence; generic information from another manufacturer is not proof.
The focused suite passed 22 tests. All 494 resistor recipes have valid render
provenance and README references. Remaining resistors, capacitors and ICs
still require review.


## FOJAN 5% supplier identity recovery (2026-11-17)

Fifteen historical FOJAN source records contained only `TS` as the primary
manufacturer number. Their complete MPNs were checked individually against
the LCSC listing titles and are recorded with supplier URLs in
`DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES.json`. The matching FOJAN FRC
manufacturer marking specification was reviewed online; no local PDF is
claimed. Both `parts_source` and the corresponding exact rows in
`working_oomp_populate_lcsc_research_data.py` were corrected, with previous
versions backed up under `tmp/display_render/fojan_supplier_identity_previous_sources`.
The repaired identifiers match the generated part records; a test guards
the research rows against reverting to `TS`.

Published 15 5% renders and individual READMEs using validated 0201 unmarked
image reuse or the reviewed shared-pass marking setup. The
`display_render_fojan_5pct_queue.py` adapter validates each ledger identity,
value, E24 code, tolerance, supplier and footprint. The focused suite passed
35 tests. All 509 resistor recipes have valid provenance and README references.
Other `TS` records still lack individually verified supplier identities and
must not be guessed. Remaining resistors, capacitors and ICs need review.


## UNI-ROYAL 0603 low-value underline follow-up (2026-11-17)

Resolved the three previously deferred 1% 0603 E24 values 2.2, 4.7 and
5.1 ohms. A manufacturer-authored 2017 thick-film specification, reviewed
online and linked in `DISPLAY_RENDER_UNIROYAL_0603_LOW_EVIDENCE.md`,
explicitly documents 5% below-10-ohm R notation and the underlined 1% E24
exception. The rendered codes are underlined 2R2, 4R7 and 5R1. The exact
MPNs, selected footprint and 1% source ratings are checked by the updated
`display_render_uniroyal_low_value_queue.py`; unsupported values remain
excluded. All three images were visually inspected and their individual
READMEs refreshed. Their existing generated PDFs match the local UNI-ROYAL
family sheet. The focused suite passed 34 tests. All 512 resistor recipes
currently have valid render provenance and README references. Remaining
resistor research, followed by capacitors and ICs, remains in progress.


## FOJAN 5% identity recovery, second batch (2026-11-17)

Verified six more previously truncated supplier identities and published their
renders and individual READMEs: 0805 2.2 MΩ and 1206 150 kΩ, 220 kΩ,
270 kΩ, 680 kΩ and 680 Ω. Their observed full MPNs and supplier links are
pinned separately in `DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES_02.json`;
the queue accepts this ledger with `--evidence` without changing the earlier
published ledger. Both source records and corresponding LCSC research rows
were repaired; prior versions are preserved under
`tmp/display_render/fojan_supplier_identity_batch02_previous/`.

The FOJAN marking specification was reviewed online; no local PDF is claimed.
All six three-digit markings were visually inspected. The focused suite passed
35 tests, and all 518 resistor recipes have valid render provenance and README
references. Fifteen other previously identified TS-only records still need
independent identity verification. Remaining resistors, capacitors and ICs
remain to be reviewed.

## RALEC RTT03 59 Ω (2026-11-17)

Published a visually inspected 0603 render and README for RALEC RTT0359R0FTP.
The manufacturer EIAJ-96 table documents `75X` for 59 Ω. Its primary datasheet
reference and generated PDF now use the existing RALEC IE-SP-007 family sheet
instead of the UNI-ROYAL sheet; previous files are in
`tmp/display_render/ralec_0603_59_previous/`. Online IE-SP-010 marking evidence
is recorded separately; no online PDF was downloaded. The focused suite passed
32 tests, and all 574 resistor recipes validate and have README references.
The separate 2.7 Ω RTT03 E24 exception still needs specific evidence for its
low-value mark and underline placement. Remaining resistors, capacitors and
ICs require review.

## RALEC small unmarked parts and FOJAN follow-up (2026-11-17)

Published six RALEC RTT01/02 pages with reviewed unmarked 0201/0402 image
reuse and individual provenance. The online RALEC IE-SP-010 specification
explicitly says RTT01/02 have no body marking. Five source records now link to
an existing local RALEC IE-SP-007 family PDF; three previously pointed to the
unrelated UNI-ROYAL family sheet. Previous source records and generated PDFs
are preserved under `tmp/display_render/ralec_small_previous/`, and all six
published PDF hashes match the local RALEC source. Online marking evidence and
the older local PDF edition are identified separately.

Also restored the supplier-verified FOJAN 1206 39 kΩ MPN and published its
`393` render; its independent evidence ledger is
`DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES_05.json`, with prior records backed
up under `tmp/display_render/fojan_5pct_05_previous/`. The focused suite passed
25 tests. All 573 resistor recipes validate and have README references.
Remaining resistors, capacitors and ICs need review.

## CCO CF1/4W 5% axial resistors (2026-11-17)

Restored supplier-verified identities for 180 Ω, 120 kΩ and 750 kΩ in the
source and LCSC research records, with backups in
`tmp/display_render/cco_cf_01_previous/` and `cco_cf_02_previous/`. Published
and inspected direct 1,400 px / 256-sample renders and READMEs with documented
four-band codes and gold tolerance bands. The manufacturer specification and
individual listings are pinned in the two `DISPLAY_RENDER_CCO_CF_IDENTITIES`
ledgers; the PDF was reviewed online only. The focused suite passed 25 tests;
all 566 resistor recipes validate and have README references. Remaining
resistor records and the capacitor and IC families still need review.

## CCO MF second supplier batch (2026-11-17)

Verified and repaired three further identities for 15 Ω, 330 kΩ and 3.9 MΩ,
and published visually inspected five-band renders and READMEs. The second
immutable ledger `DISPLAY_RENDER_CCO_MF_IDENTITIES_02.json` records the
supplier links; earlier ledger hashes are unchanged. Source and LCSC research
backups are in `tmp/display_render/cco_mf_02_previous/`. The CCO specification
states sky-blue coating, while the requested beige is illustrative. The
focused suite passed 31 tests; all 563 resistor recipes validate and have
README references. `DISPLAY_RENDER_CCO_MF_RESEARCH.md` records several
remaining type or power-rating conflicts that need separate review. Further
resistor work, followed by capacitors and ICs, remains unfinished.

## CCO MF1/4W identities and axial renders (2026-11-17)

Repaired 11 supplier-verified CCO MPNs previously truncated to `T`, in both
part sources and their LCSC research rows. Individual evidence is pinned in
`DISPLAY_RENDER_CCO_MF_IDENTITIES_01.json`; original records are preserved in
`tmp/display_render/cco_mf_01_previous/`. Published and visually reviewed all
11 beige renders and READMEs. CCO specifies a sky-blue coating; each page
discloses that beige is illustrative. The 1% five-band markings come from the
manufacturer specification, reviewed online without claiming a local PDF.
The focused suite passed 30 tests, and all 560 resistor recipes validate and
have README references. Remaining resistors, capacitors and ICs need review.

## VO CR 5% axial resistors (2026-11-17)

Published direct 1,400 px / 256-sample renders and READMEs for 2.7 kΩ and
1.5 MΩ VO CR1/4W parts; both images were inspected. The beige bodies and
gold 5% bands follow the requested presentation. The VO specification calls
for standard codes without confirming each exact band count, so each README
labels the four-band layout as illustrative. No local PDF is claimed. The
focused suite passed 23 tests; all 549 resistor recipes validate and have
README references.

An additional 11 CCO MF source identities have been researched in
`DISPLAY_RENDER_CCO_MF_RESEARCH.md`; no corresponding source repairs or renders
have yet been performed. The CCO specification states sky-blue bodies, so the
requested beige appearance must be described as illustrative. Continue with
the remaining resistor records, then capacitors and ICs.

## YAGEO CFR-25 four-band renders (2026-11-17)

Published and visually inspected direct 1,400 px, 256-sample renders and
READMEs for 22 Ω and 1.8 MΩ YAGEO CFR-25 5% parts. Their documented fourth
band is gold, with beige bodies as requested. The existing online-only YAGEO
manufacturer evidence is reused; no local PDF is claimed. The new guarded
`display_render_yageo_cfr_queue.py` checks the exact MPN, tolerance, value and
footprint before preparing four-band recipes. The focused suite passed 29
tests; all 547 resistor recipes validate and have README image references.

Two further VO CR 5% candidates have been researched and a tested discovery
adapter prepared in `display_render_vo_carbon_queue.py`; they have not been
added or rendered. Its evidence states that the exact VO production band
count is not confirmed. Remaining resistors, capacitors and ICs need review.

## VO MF1/4W 1% axial resistors (2026-11-17)

Published and visually reviewed seven beige-body renders and READMEs: 200 Ω,
10 kΩ, 47 kΩ, 56 kΩ, 100 kΩ, 560 kΩ and 1 MΩ. The VO manufacturer sheet
links the series to standard MIL/EIA colour codes and gives compatible body
dimensions. It does not confirm the exact band count per MPN: the standard
five-band rendering is explicitly marked as illustrative in every page and in
`DISPLAY_RENDER_VO_MF_EVIDENCE.md`. No local PDF is claimed. The focused suite
passed 30 tests, and all 545 resistor recipes have valid provenance and README
references. Remaining resistors, capacitors and ICs need review.

## Huaxing MF1/4W 1% axial resistors (2026-11-17)

Added and visually reviewed five renders and individual READMEs for 33 Ω,
82 Ω, 1 kΩ, 2.2 kΩ and 5.1 kΩ. The manufacturer-authored MF/RJ online
specification documents the five-band 1% code and body dimensions; see
`DISPLAY_RENDER_HUAXING_MF_EVIDENCE.md`. Its body colour is specified as blue;
the beige render is the user's requested illustrative finish. No local PDF is
claimed. The 82 Ω supplier description had captured price tiers; this was
corrected from the LCSC listing in source and research data, with previous
versions retained in `tmp/display_render/huaxing_82_previous/`. The focused
suite passed 29 tests. All 538 resistor recipes have valid provenance and
README references. Remaining resistors, capacitors and ICs need review.

## UNI-ROYAL 510 Ω and FOJAN 470 Ω 1206 (2026-11-17)

Published and visually inspected two 5% renders, with markings `511` and
`471`. Their exact identities were checked against JLCPCB and LCSC product
listings. The UNI-ROYAL source was linked to the existing manufacturer family
sheet and its generated local PDF was verified against that sheet. FOJAN's
manufacturer marking specification was reviewed online, with no local PDF
claimed; its exact supplier evidence is pinned separately in
`DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES_04.json`. The focused suite passed
30 tests, and all 533 resistor recipes have valid provenance and README
references. The pip download cache was cleared to recover disk space; installed
packages were retained. Remaining resistors, capacitors and ICs need review.

## UNI-ROYAL generic and exact variants (2026-11-17)

Published six more reviewed parts: 0805 3.6 kΩ, 1206 12 kΩ, 15 kΩ and
6.8 Ω at 5%, and the exact UNI-ROYAL 1206 270 Ω and 470 Ω 1% variants.
`display_render_uniroyal_named_queue.py` checks the explicit IDs, MPNs,
family datasheet, tolerance, value and footprint before invoking the reviewed
marking adapters. The six markings were visually inspected and their generated
PDFs match the existing shared UNI-ROYAL family sheet. The focused suite passed
35 tests; all 531 resistor recipes validate and have README references.

The C: drive had less than 512 MiB free; 67.6 MiB was recovered by removing
scratch render files only after verifying byte-identical published copies.
Disk space remains tight and must be checked before further batches. Remaining
resistors, capacitors and ICs are unfinished.

## FOJAN 1206 corroborated identities (2026-11-17)

Added visually inspected 3.3 kΩ (`332`) and 5.1 kΩ (`512`) renders and
READMEs. Distributor listings corroborate both exact FOJAN MPNs; the
associations with their LCSC codes come from secondary sources, recorded with
their limitations in `DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES_03.json`.
The manufacturer marking specification was inspected online; no local PDF is
claimed. Source and LCSC research records were repaired and their former
versions saved under `tmp/display_render/fojan_5pct_03_previous/`. The focused
suite passed 35 tests; all 520 resistor recipes validate and have README image
references. Thirteen other TS-only records still require identity research;
remaining resistors, capacitors and ICs are unfinished.

## YAGEO RC_L 0805 and 1206 (2026-11-17)

Published and visually reviewed five 1% parts: 0805 180 kΩ (`1803`) and
39 kΩ (`3902`), and 1206 180 Ω (`1800`), 470 kΩ (`4703`) and 47 kΩ
(`4702`). `display_render_yageo_large_queue.py` checks the exact primary MPN,
value, selected footprint, supplier tolerance and any explicit catalogue
tolerance before creating recipes. `DISPLAY_RENDER_YAGEO_RC_L_LARGE_EVIDENCE.md`
links the manufacturer marking specification reviewed online; no local PDF
is claimed. The contact sheet and shared-pass approximation were inspected.
The focused suite passed 31 tests, and all 525 resistor recipes have valid
provenance and README references. Remaining resistors, capacitors and ICs
remain to be reviewed.
# Fenghua RC-02 5% 0402 (2026-11-17)

Added display images and part pages for 36 Ω RC-02K360JT and 82 kΩ
RC-02K823JT. Both use an inspected, unmarked 0402 KiCad image with separate
manufacturer evidence and provenance. Removed incorrect inherited UNI-ROYAL
datasheet attribution and retained original records under
`tmp/display_render/fenghua_0402_5pct_originals/`; the Fenghua approval sheet
was reviewed online only. The focused suite passed 28 tests. All 576 resistor
recipes validate and their README files contain image references. The 24 kΩ
and 91 kΩ records have conflicting 1% and 5% tolerances; RS-02K154JT is not
listed in the reviewed RC/RS sheet. These require further evidence. Remaining
resistors, capacitors and ICs remain unfinished.

# Fenghua RS-06 1206 5% batch (2026-11-17)

Prepared and visually reviewed ten exact E24 markings: 110 Ω, 160 Ω, 1.3 kΩ,
3.6 kΩ, 7.5 kΩ, 8.2 kΩ, 27 kΩ, 68 kΩ, 180 kΩ and 560 kΩ. The selected
Fenghua MPNs and JLCPCB records identify 5% parts; previously copied UNI-ROYAL
source fields incorrectly said 1%. Those fields were reconciled using the
manufacturer sheet reviewed online, with prior source records backed up under
`tmp/display_render/fenghua_rs1206_previous/` and unrelated former datasheet
provenance retained separately in each source folder. No local Fenghua PDF is
claimed. The contact sheet is `tmp/display_render/fenghua_rs1206_contact.png`;
the 23 focused tests passed. All ten pages were published locally. All 586
resistor recipes validate and have README image references. Other resistor
records, capacitors and ICs still need review.

# Fenghua RC-02 tolerance reconciliation (2026-11-17)

Fenghua and JLCPCB listings corroborate RC-02K243JT (24 kΩ) and RC-02K913JT
(91 kΩ) as 5% parts. Corrected their old 1% fields and unrelated UNI-ROYAL
attribution, then prepared and published their unmarked 0402 render images.
Original source records are under `tmp/display_render/fenghua_0402_tolerance_previous/`.
The 24 kΩ distributor PDF remains with its acquisition provenance; the 91 kΩ
part has no local PDF. The existing 150 kΩ RS-02 local Fenghua catalogue has a
general 0402 no-marking rule, but its series table does not establish RS-02 as
a supported combination; exact series evidence remains needed.

Publication retained stale generated UNI-ROYAL PDFs for the earlier 36 Ω and
82 kΩ RC-02 parts, the 91 kΩ part, and the ten RS-06 parts. The files were
hash-checked and removed from those generated pages, then the exact pages were
regenerated. Their shared original remains at
`parts_source/electronic_resistor_0402_0_ohm/datasheet.pdf`; redundant temporary
copies were later removed after verifying their hashes against that original. This is a
separate check from the source-record correction. Verified that all 13 pages
disclose the missing local PDF and no longer link the unrelated one. The 22
focused tests passed; all 588 resistor recipes validate and have README image
references.

# Yageo AC0402 6.8 MΩ (2026-11-17)

Published an inspected unmarked KiCad-based image for Yageo
`AC0402JR-076M8L`, with source evidence in
`DISPLAY_RENDER_YAGEO_AC0402_EVIDENCE.md`. The manufacturer AC-series sheet
and Mouser's exact-part listing were reviewed online; no local PDF is claimed.
`display_render_yageo_ac0402_queue.py` guards the exact part and its tolerance;
the reuse helper verifies its evidence. The FOJAN 0402 2.4 kΩ record remains
queued because an independent exact supplier identity was not located.
SAE 0201 manufacturer marking evidence also remains to be located. Thirteen
focused tests passed; all 589 resistor recipes validate and have README image
references.

# Yageo visual references for generic SAE 0201 entries (2026-11-17)

Prepared eight unmarked Yageo RC0201 visual references for generic values
1.2 MΩ, 1.2 kΩ, 18 Ω, 47 Ω, 560 Ω, 56 Ω, 82 kΩ and 820 Ω. Their selected
SAE identities remain unchanged; the pages disclose the illustrated Yageo
MPN and that SAE appearance is unverified. Same value and tolerance do not
prove the parts are interchangeable across all ratings. Exact reference
evidence is in `DISPLAY_RENDER_YAGEO_0201_VISUAL_REFERENCES.md`; the
manufacturer specification was reviewed online, not downloaded. The guarded
queue and reuse helper reject changed source identities or tolerance conflicts.
All eight pages are published locally and their disclosures were checked.
Thirteen focused tests passed; all 597 resistor recipes validate and have
README image references. Remaining families and records need review.

# Unsourced generic 0201 visual references (2026-11-17)

Prepared six unmarked Yageo 1% visual references for 1.6 kΩ, 200 kΩ, 20 kΩ,
300 Ω, 53.6 kΩ and 8.2 MΩ. These generic entries specify no manufacturer or
tolerance; the images identify the documented example without assigning its
ratings to the entry. Exact part and marking evidence is in
`DISPLAY_RENDER_YAGEO_0201_GENERIC_REFERENCES.md`. The manufacturer sheet was
reviewed online. Thirteen focused tests passed; the source guard rejects
subsequent supplier, tolerance or footprint changes. All six pages were
published locally and their disclosures checked. All 603 resistor recipes
validate and have README image references; remaining records need review.

# Unsourced generic 0402 visual references (2026-11-17)

Added locally published Yageo reference images for 1.6 kΩ, 300 Ω and 53.6 kΩ
generic 0402 entries. They remain unsourced and have no specified tolerance;
each page identifies its illustrated 1% example. The RC_L unmarked policy and
exact examples are linked in `DISPLAY_RENDER_YAGEO_0402_GENERIC_REFERENCES.md`.
Fourteen focused tests passed. Other resistor packages require review.

# Unsourced generic 0805 and 1206 visual references (2026-11-17)

Prepared and inspected six Yageo 1% reference renders: 0805 1.6 kΩ (`1601`)
and 53.6 kΩ (`5362`); 1206 1.6 kΩ (`1601`), 200 kΩ (`2003`), 20 kΩ
(`2002`) and 53.6 kΩ (`5362`). The entries have no selected manufacturer or
tolerance, which each page discloses. Exact identity and marking evidence is
in `DISPLAY_RENDER_YAGEO_LARGE_GENERIC_REFERENCES.md`, reviewed online. The
contact sheet is `tmp/display_render/yageo_generic_large_contact.png`. The
focused suite passed 14 tests. All six pages were published locally, and all
nine new 0402/0805/1206 disclosures were checked. All 612 resistor recipes
validate and have README image references; other records still need review.

# Unsourced generic 0603 visual references (2026-11-17)

Prepared four illustrated Yageo references: 1.6 kΩ (`162`), 30 Ω (`300`),
53.6 kΩ (`71C`, EIA-96) and 5.6 Ω (`5R6`). The entries specify no supplier
or tolerance; the images name the represented example and its tolerance.
Yageo's marking document and exact reference listings were reviewed online,
with evidence in `DISPLAY_RENDER_YAGEO_0603_GENERIC_REFERENCES.md`.
The contact sheet is `tmp/display_render/yageo_generic_0603_contact.png`.
All four pages were published locally and their disclosures checked. The
focused suite passed 23 tests; all 616 resistor recipes validate and have
README image references. Other records still need review.

# Unsourced generic axial references (2026-11-17)

Prepared Yageo visual-reference recipes for 1.6 kΩ, 200 kΩ, 20 kΩ and 300 Ω
5% CFR examples with gold tolerance bands, and a 53.6 kΩ 1% MFR example with
a brown tolerance band. All use illustrative beige bodies, and the generic
entries do not acquire a supplier or tolerance. Exact source and marking
evidence is in `DISPLAY_RENDER_YAGEO_AXIAL_GENERIC_REFERENCES.md`; the focused
suite passed 14 tests. Inspect actual manifests and pages to determine which
full-quality renders are complete before resuming. Four-band CFR parts must
not use the five-band shared-pass compositor. All five renders were inspected
and their pages published locally; the four 5% outputs were directly path
traced at 1,400 px / 256 samples and the 1% output uses reviewed five-band
shared passes. Their contact sheet is
`tmp/display_render/yageo_generic_axial_contact.png`. All 621 resistor recipes
validate and have README image references; further catalogue work remains.

# Four-element 0402 arrays (2026-11-17)

Prepared and inspected four generic 4×0402 array references: 1 MΩ (`105`),
100 kΩ (`104`), 330 Ω (`331`) and 510 Ω (`511`) per element. They illustrate
identified 5% UNI-ROYAL parts; the generic entries remain unsourced and do not
specify tolerance. Evidence is in `DISPLAY_RENDER_GENERIC_ARRAY_0402_REFERENCES.md`.
Also prepared the exact selected Fenghua RC-MT08W000JT zero-ohm array, whose
manufacturer approval sheet specifies the single `0` body marking. Its
separate evidence is in `DISPLAY_RENDER_FENGHUA_ARRAY_JUMPER_EVIDENCE.md`.
The original local Fenghua PDF was preserved. The generic contact sheet is
`tmp/display_render/generic_array_0402_contact.png`. The focused suites passed
23 and 15 tests. All five pages were published locally; all 626 resistor
recipes validate and have README image references. The previously noted 4×0603
placeholder dimensions were subsequently corrected; see the newer entry above.

# Four-element 0603 arrays (2026-11-17)

The unsourced 1 MΩ, 330 Ω and 510 Ω array entries had 10×5 mm placeholder
dimensions. The existing UNI-ROYAL 4D03 array specification gives nominal
3.2×1.6 mm; corrected the source records, preserved previous source files and
diagrams in `tmp/display_render/generic_array_0603_previous/`, and refreshed
only the three components' diagrams. Prepared and visually inspected reference
renders with `105`, `331` and `511` markings, respectively. The generic entries
remain unsourced; each image names its illustrative 5% UNI-ROYAL part. Exact
evidence is in `DISPLAY_RENDER_GENERIC_ARRAY_0603_REFERENCES.md` and the
contact sheet is `tmp/display_render/generic_array_0603_contact.png`.
Fifteen focused tests passed. All three pages were published locally; their
dimensions and updated dimension drawings were checked. All 629 resistor
recipes validate and have README image references. More catalogue work remains.

# Yageo YC124 10 kΩ array (2026-11-17)

Published and visually reviewed the selected YC124-JR-0710KL 4×0402 array,
marked `103` according to Yageo's YC/TC specification. The exact part and
marking evidence is in `DISPLAY_RENDER_YAGEO_YC124_EVIDENCE.md`; the
manufacturer PDF was reviewed online and no local copy is claimed. The
original source record is backed up as `tmp/display_render/yageo_yc124_previous.yaml`.
Fourteen focused tests passed. Temporary render images were removed only when
their bytes matched published copies, recovering 13.8 MiB; the system drive
remains close to the 512 MiB render floor and should be checked before batches.
All 630 resistor recipes validate and have README image references; remaining
resistors, capacitors, ICs and other eligible parts still need review. A later
check found 482 MiB free despite removal of additional byte-identical scratch
files; do not begin a rendering batch below the 512 MiB floor.


# HWA 0201 identity corrections and disk limit (2026-11-17)

Corrected two truncated manufacturer numbers using their LCSC listings: 270 Ω
`HRC0201J271 CNTO` (C55098252) and 390 kΩ `HRC0201J394 CNTO` (C55098269).
Refreshed only those two generated records, READMEs and web manifests, and
verified source and generated manufacturer fields agree. Evidence and the
unresolved manufacturer marking question are in
`DISPLAY_RENDER_HWA_0201_RESEARCH.md`; original files are saved under
`tmp/display_render/hwa_0201_identity_previous/`. Neither part was rendered.
The system drive had approximately 482 MiB free after the refresh, below the
512 MiB renderer floor. Free additional disk space before resuming, then review
marking evidence or a clearly disclosed visual reference and continue the
remaining resistor, capacitor, IC and other eligible queues.

# Four selected 0201 visual references prepared (2026-11-17)

Verified matching 39 Ω, 270 Ω, 390 kΩ and 680 kΩ Yageo RC0201
references, recorded the evidence, and prepared the guarded
`display_render_yageo_selected_0201_queue.py` adapter. The source manufacturer
appearance remains unverified; each proposed recipe explicitly names Yageo
and discloses that limitation and lack of full interchangeability. The reuse
helper recognizes the new evidence. Five focused tests passed. No recipes,
images or pages were published for this batch; the drive remained below the
512 MiB rendering minimum. Once space is available, discover the queue,
recheck evidence, add recipes, generate or reuse inspected renders, inspect
and publish the four pages. Continue the wider outstanding catalogue after it.

# Four selected 0201 references published (2026-11-17)

Disk space was recovered. Added the four prepared Yageo 0201 reference recipes,
reused the inspected direct 0201 render with provenance checks, inspected the
image and published all four exact pages. The selected HWA CHN and GiantOhm
appearance remains unverified; each README names its Yageo reference and
explicitly disclaims full interchangeability. Confirmed valid display metadata,
README disclosures and render links for all four; five focused tests passed.
This raises the resistor recipe count to 634; further resistor records, then
capacitors, ICs and other eligible parts still need review.

# 0402 2.4 kΩ visual reference (2026-11-17)

Published the 2.4 kΩ 0402 page with an inspected, reused unmarked image
of manufacturer-documented Yageo RC0402JR-072K4L (5%). The source-record
FOJAN identity and appearance remain unverified, and other listed options
include 1% parts; the page and evidence retain these limitations. The new
guarded adapter validates the selected record, footprint and representative
listing; five focused tests passed and provenance and README text were
validated. There are now 635 resistor recipes; further records remain.

# Three 0805 5% Yageo visual references (2026-11-17)

Published 330 kΩ (`334`), 510 kΩ (`514`) and 820 Ω (`821`)
using manufacturer-documented Yageo references. Selected FOJAN MPNs are
truncated; pages explicitly disclose the unverified selected identity and
appearance and that matching value and tolerance do not prove interchangeability.
The current 0805 shared master was rebuilt at 1,400 px / 256 samples per pass;
the three outputs were visually reviewed in
`tmp/display_render/yageo_selected_0805_contact.png`. All three metadata and
README disclosures validate; three focused tests passed. There are 638
resistor recipes; remaining parts and later families require review.

# Seven 1206 5% Yageo visual references (2026-11-17)

Published 3.3 MΩ (`335`), 3.9 MΩ (`395`), 3.9 kΩ (`392`), 56 Ω
(`560`), 75 Ω (`750`), 8.2 MΩ (`825`) and 82 Ω (`820`). Their selected
FOJAN MPNs are truncated; each README identifies the illustrated Yageo
reference and discloses the unverified selected identity and appearance and
limited interchangeability evidence. Built a current 1,400 px / 256-sample
1206 shared master, reviewed all seven previews in
`tmp/display_render/yageo_selected_1206_contact.png`, verified metadata and
README links/disclosures, and passed seven focused tests. There are now 645
resistor recipes; remaining records and later families need review.

# Two high-value 0805 references (2026-11-17)

Published 7.5 MΩ (`755`) and 8.2 MΩ (`825`) with documented Yageo
reference identities and selected-FOJAN identity/appearance disclosures.
Inspected both previews and validated render provenance and README text;
two focused tests passed. There are 647 resistor recipes.
Separately, the 5.6 MΩ selected HWA CHN identity was corrected from FNTN to
HRC0805J565 FNTN based on LCSC C54921355. Original files are preserved in
`tmp/display_render/hwa_0805_identity_previous/`. Generated metadata and
README still need refreshing, together with a reviewed display reference.

# Two HWA 0805 records and identity repair (2026-11-17)

Published 5.6 MΩ (`565`) and 133 kΩ (`1333`) with Yageo visual references
and explicit unverified-HWA-appearance and interchangeability limitations.
Corrected the 5.6 MΩ selected MPN from FNTN to HRC0805J565 FNTN using
LCSC C54921355; source and generated identities now agree. Inspected both
previews, verified metadata and README disclosure, and passed two focused
tests. There are now 649 resistor recipes; further records remain.

# Three small Yageo visual references (2026-11-17)

Published 0201 10 MΩ 5%, 0402 10 MΩ 1%, and the separate 0402
150 kΩ 5% entry using inspected, provenance-checked unmarked Yageo visual
references. Pages identify the represented Yageo MPN and disclose unverified
selected appearance and lack of full interchangeability evidence. Corrected
the 150 kΩ record's stale UNI-ROYAL shared-datasheet metadata after inspecting
its actual local Fenghua RS-series PDF; preserved the PDF and prior notes.
The previous metadata is backed up in `tmp/display_render/fh_150k_metadata_previous/`.
Three focused tests passed, all metadata and README disclosures were validated.
There are 652 resistor recipes; remaining resistors and later families need review.

# 0805 110 Ω and 10 MΩ references (2026-11-17)

Published 110 Ω (`111`) and 10 MΩ (`1005`) Yageo reference renders,
with explicit selected-part appearance and interchangeability limitations.
The 110 Ω selected Fenghua RS-05K111JT is 5%, confirmed by JLCPCB and
LCSC; corrected a conflicting 1% electrical field and replaced the unrelated
UNI-ROYAL generated PDF with the existing Fenghua RS-series family PDF.
Prior files are saved in `tmp/display_render/fh_110ohm_previous/`. Corrected
prior 150 kΩ Fenghua thick-film marking page references to pages 11–12.
Both previews were inspected, two focused tests passed, and display metadata,
README disclosures, 110 Ω tolerance and PDF hashes were validated. There are
654 resistor recipes; remaining parts and later families require review.

# Fenghua 0603 2.7 Ω (2026-11-17)

Published the selected FH RS-03L2R7JT 5% part with `2R7` marking backed
by the existing Fenghua RS family specification. Built current 0603 shared
passes at 1,400 px / 256 samples per pass and visually inspected the preview.
Replaced a stale UNI-ROYAL generated PDF with the existing Fenghua family
PDF and corrected datasheet metadata; originals are backed up in
`tmp/display_render/fh_0603_2r7_previous/`. The focused identity and rating
test passed; render provenance, README marking, PDF hash and page references
were checked. There are 655 resistor recipes; further records remain.

# RALEC 0603 2.7 Ω (2026-11-17)

Published the RALEC RTT032R70FTP 1% variant with an underlined `2R7`
mark. The local IE-SP-007 sheet specifies the 1% E24 underline and the
sub-10 Ω decimal rule, but does not show 2.7 Ω explicitly; the inference is
disclosed on the page and evidence record. Inspected the preview, linked the
existing local RALEC family PDF, preserved the original source metadata,
passed a focused guard test and verified provenance, README and PDF hash.
There are 656 resistor recipes; remaining records and later families need review.

# RALEC 0805 1 Ω legacy identity (2026-11-17)

Published RALEC RTT051R00FTP with documented `1R00` marking, using the
existing inspected 0805 shared passes. The legacy ID contains UNI-ROYAL even
though the selected C4321 part is RALEC; the page explicitly explains this
and the ID remains for later taxonomy review. Corrected inherited UNI-ROYAL
datasheet and dimension metadata and linked the existing RALEC family PDF;
originals are backed up in `tmp/display_render/ralec_0805_1r00_previous/`.
Inspected preview, passed a focused guard test, and verified provenance,
manufacturer disclosure and PDF hash. There are 657 resistor recipes; more
records and later families remain.

# Yageo axial zero-ohm jumper (2026-11-17)

Published MFR-25-T-52-0R using a direct 1,400 px / 256-sample KiCad-based
render with a beige body and a centered black jumper band. The band convention
is illustrative; exact Yageo appearance has not been verified. A jumper has
no tolerance band. Extended the renderer only for a single black band and
archived the previous renderer by hash. Inspected preview and final output;
nine focused tests passed and all 658 resistor recipes have valid render
metadata and README references. Further records and families remain.

# Yageo RT 1206 133 kΩ (2026-11-17)

Published the selected RT1206DRE07133KL 0.5% thin-film part with its
manufacturer-documented `1333` marking. Inspected preview and direct 1,400 px /
256-sample render, passed a source guard test, and verified metadata, marking
and README. Online manufacturer evidence is recorded in
`DISPLAY_RENDER_YAGEO_RT1206_133K_EVIDENCE.md`; no local PDF is claimed.
Documented two 2512 source-value conflicts in
`DISPLAY_RENDER_2512_VALUE_CONFLICTS.md`; neither conflicting part was rendered.
There are 659 resistor recipes; further records and families remain.

# FOJAN FRP 1206 15 Ω (2026-11-17)

Published FOJAN FRP1206F15R0TSN, 15 Ω 1% 0.5 W, with manufacturer-
documented `15R0`. Inspected preview and direct 1,400 px / 256-sample render,
passed a focused source guard test, and verified provenance and README body-
length disclosure. Manufacturer FRP evidence was reviewed online only.
Recorded matching-value candidate parts for the two 2512 value conflicts in
`DISPLAY_RENDER_2512_VALUE_CONFLICTS.md`; additional rating and marking
review is needed before changing either selection. There are 660 resistor
recipes; further records and families remain.

# Corrected 2512 0.2 Ω Yageo PT selection (2026-11-18)

Replaced the mismatched FH 2 Ω selected supplier with documented Yageo
PT2512FK-7W0R2L / C309535, 0.2 Ω 1% 2 W current-sense. Preserved the
previous source and generated metadata in `tmp/display_render/2512_0_2_selection_previous/`
and source notes; other current-sense characteristics require design review.
Inspected the KiCad 2512 model, rendered and inspected the documented `R200`
mark at 1,400 px / 256 samples, and published the targeted page. The focused
source guard test passed; source and generated selection, output provenance,
README and zero non-finite pixels were checked. No local PDF is claimed.
There are 661 resistor recipes; the 2512 13.3 Ω conflict and other work remain.
