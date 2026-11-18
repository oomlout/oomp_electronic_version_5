# Aluminium electrolytic display research

2026-11-18: The source inventory includes surface-mount Honor RVT aluminium
electrolytics, including 8 × 10.2 mm and 10 × 10.2 mm sizes. Installed KiCad
has `Capacitor_SMD.3dshapes/C_Elec_8x10.2.step`, SHA-256
`8f86de3213fc1a230094af15b95b24ddd629f28ed265f97c9d2b9c391e729b2a`.
It has not yet been geometrically or visually reviewed against the part drawing.

The existing local series PDF attached to
`parts_source/electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_1000_micro_farad_16_volt/datasheet.pdf`
has SHA-256 `285ae57abc097a56fae89388feef643b79f8d7c2901d6457de4bc00a5f91ce1b`.
Page 1 shows illustrative metal cans with black top sectors and markings; page 2
shows case dimensions and identifies positive/negative terminals. It does not
establish the exact printed text, ink layout or polarity sector orientation for
a specific purchased component. Poppler reported missing font substitutions;
the schematic and product illustration were legible but text needs caution.

The 8 × 10.2 mm 100 µF 50 V source record refers to a PDF which is not present
at its stated local path. Do not claim that file exists or silently download it.
Before any render: verify exact part/source and local provenance, inspect the
STEP model's terminal and face orientations, establish the negative sector
from suitable evidence, and implement top-face value/voltage text with clear
approximation disclosures. Do not reuse the positive-anode tantalum policy.
No aluminium render or recipe has been produced from this research.

## KiCad model comparison

The unpolarized `C_Elec_8x10.2.step` is valid and its total footprint envelope
(including contacts and base) is 9.5 × 8.3 × 10.2 mm, with an 8 mm can.
The source footprint is instead `CP_Elec_8x10`, whose valid matching model is
`CP_Elec_8x10.step`, SHA-256
`eac826caddc87349153805510154d3cd62a11307d11e10b3761a8acf8712a37a`.
Its total bounds are 9.5 × 8.3 × 10.0 mm; the dark top sector is on positive
X (top plane spans x 1.2–3.47 mm), same side as footprint pad 2. The source
uses `Device:C_Polarized`; verify symbol pin 2 is negative before relying on
this inference. The KiCad top marking geometry is blank apart from that
sector. The model may need 1.02 vertical scaling for a 10.2 mm-high source;
check base height and exact manufacturer dimensions before committing to it.
No image or recipe is yet prepared.

The installed `Device:C_Polarized` symbol places its positive sign beside
pin 1; pin 2 is therefore negative, matching the polarized model's dark sector
on the positive-X pad-2 side. Exact manufacturer ink placement still needs
separate verification and a render has not yet been attempted.

A manufacturer RVT series specification for another value, viewed online at
https://xonstorage.z8.web.core.windows.net/pdf/honor_rvt1e470m0505_xonjuly20_20_link.pdf
(page 4, marking section), calls for nominal capacitance, rated voltage,
negative polarity and a manufacturer mark. This supports value/voltage text
but does not establish a particular typography or layout for the 8 mm part;
mark the representation as illustrative and do not invent a logo or date.
The manufacturer drawing on page 5 covers the 8–10 mm family and page 6
lists 8 × 10.2 mm dimensions. No file was downloaded.

## 8 mm pilot preparation

Prepared the exact C3352 / RVT1H101M0810 recipe and evidence record
`DISPLAY_RENDER_RVT_8MM_100UF_50V_EVIDENCE.md`. Its existing files and recipes
are backed up under `tmp/display_render/rvt_8mm_pilot_previous/`. The recipe
uses illustrative 100 / 50V lines and the KiCad dark negative sector. It cannot
yet render: implement a reviewed metal top-face material adapter and test it
after the in-progress D-case render finishes, then preview and inspect before
any final output or page update.

The metal top-face adapter now isolates exactly one top plane for black ink,
leaves the negative sector and base dark, and retains metallic sides. The
checked model is 285,870 temporary triangles; no mesh export is retained. A
700 px preview was inspected: the illustrative 100 / 50V marking is legible
and does not overlap the negative sector. Renderer sources before and after
the adapter are archived by hash; 35 marking, metadata and TAJ queue tests
passed. The final 1400 px render is running in exec session 60748; inspect its
image, validate and publish only after completion.

Two further 8 × 10.2 mm Honor parts, RVT1V221M0810 (220 µF 35 V) and
RVT1C471M0810 (470 µF 16 V), are individually researched and their guarded
recipes are added with two passing identity/voltage/polarity tests; neither
is rendered or published. Prior files are in
`tmp/display_render/rvt_8mm_batch01_previous/`. After reviewing the pilot,
render and inspect both individually or use a validated matching shared pass.
Other SMD packages in the source inventory include 4 × 5.4 mm (five),
6.3 × 7.7 mm (five) and 10 × 10.2 mm (four); each needs model, dimension and
marking review, not automatic reuse of the 8 mm geometry.

## 10 mm model preparation

`CP_Elec_10x10.step` is a valid single-root model with total bounds 12.0 ×
10.3 × 10.0 mm and SHA-256
`8af72237638a055d91e7b5db024aa87cce0ae52e62a77308a6489843773d9c38`.
The upper metal face spans x -4.33–1.50 mm; its dark sector occupies positive
X and aligns with the negative pad 2 of `CP_Elec_10x10`. The C3359 1000 µF
16 V pilot recipe and evidence are prepared, with previous files backed up
under `tmp/display_render/rvt_10mm_pilot_previous/`; it still needs a model
check, preview, visual review, final render and page validation.

Three other individually listed 10 × 10.2 mm Honor candidates remain to
be checked against their source records: RVT1H221M1010, 220 µF 50 V
(https://jlcpcb.com/partdetail/HonorElec-RVT1H221M1010/C3358);
RVT1E471M1010, 470 µF 25 V
(https://jlcpcb.com/partdetail/HonorElec-RVT1E471M1010/C3351); and
RVT1V471M1010, 470 µF 35 V
(https://jlcpcb.com/partdetail/HonorElec-RVT1V471M1010/C3350). None has a
recipe or render yet. Exact production text, finish and logo are not verified.

The 8 mm 100 µF 50 V pilot final image and page were inspected and validated;
the earlier in-progress note is superseded. Three 10 mm candidate recipes
have been added after source checks and three passing queue tests, with
backups under `tmp/display_render/rvt_10mm_batch01_previous/`; the 10 mm
pilot and candidates remain unrendered. Model checking is running in exec
session 46241.

The 10 mm model check completed successfully: scaled bounds are 12.0 × 10.3
× 10.2 mm including contacts and base, and the marking is `1000 / 16V`. Its
700 px visual preview is running in exec session 82032; inspect before any
full-quality render.

## 4 mm case preparation

KiCad `CP_Elec_4x5.4.step` has valid bounds 5.5 × 4.3 × 5.4 mm including
base and contacts, SHA-256
`6b6de343280a3e1271e2e2c1c93ec52bb333a72ac1f58e85f2a2b2b189e0e73e`.
Its dark top sector is on the pad-2 negative side. C3343 / RVT1E100M0405
(10 µF 25 V) is prepared as a pilot, checked successfully and backed up in
`tmp/display_render/rvt_4mm_pilot_previous/`. It needs a visual preview and
final render. Four further exact supplier-backed recipes were added and four
identity/rating/polarity tests passed; backups are under
`tmp/display_render/rvt_4mm_batch01_previous/`. None is yet rendered or
published. The small text, including `4.7`, requires individual visual review.

The 10 mm 1000 µF 16 V preview passed visual review and its final render
is running in exec session 53159. Earlier notes calling that preview pending
are superseded.

## 6.3 × 7.7 mm case preparation

KiCad `CP_Elec_6.3x7.7.step` is a valid single-root model with total bounds
7.8 × 6.6 × 7.7 mm and SHA-256
`c2a2efc3a0562b25c21f2b732dd2d6f0c3ff67148e12d40edff0e8fbdf71989b`.
The dark top sector lies on positive X, matching negative pad 2; its metal top
face was checked separately. C3338 / RVT1E101M0607 (100 µF 25 V) is prepared
as a pilot, with backups under `tmp/display_render/rvt_6_3mm_pilot_previous/`.
Model checking is running in exec session 36360; it still needs preview and
final inspection. Four other exact supplier-backed recipes are added, with
four passing identity/rating/polarity tests and backups under
`tmp/display_render/rvt_6_3mm_batch01_previous/`. None has been rendered or
published; the illustrative 6.3 V text needs close visual inspection.
The generic 220 µF 10 V record lacks selected manufacturer/electrical data
and was not silently assigned a specific part.

## 5 mm case preparation

`CP_Elec_5x5.4.step` is valid with total bounds 6.5 × 5.3 × 5.4 mm and
SHA-256 `bbccd1f297129a1c86745dc531025be69b049530f562c20fca3b9594156f1105`.
The dark sector is on pad 2, the negative side of the reviewed symbol.
C3347 / RVT1A101M0505 (100 µF 10 V) is prepared as a pilot; C3337 /
RVT1C470M0505 (47 µF 16 V) has a guarded recipe and one passing identity,
rating and polarity test. Backups are under
`tmp/display_render/rvt_5mm_pilot_previous/` and `rvt_5mm_batch01_previous/`.
Neither part has been rendered or published; check and inspect the pilot first.

The 10 mm pilot final image and page were inspected and validated; earlier
in-progress notes are superseded. The 4 mm pilot preview is running in exec
session 64553; inspect its small text and negative sector before proceeding.

The 6.3 × 7.7 mm pilot model check passed, including 7.8 × 6.6 × 7.7 mm
bounds and the illustrative `100 / 25V` marking. Its visual preview and
final render remain pending.

## Shared aluminium material passes

`display_render_rvt_composite.py` is prepared and archived as
`f5857f95a1d27ec12a459e410cfe93dfd23055ac462605ae491b906908c29495.py`.
It requires a recipe with the reviewed model, font, dimensions and offset
for that specific package. Fourteen prepared recipes passed those gate
checks. It has NOT generated any shared passes or been visually compared
with an independent full render; do not publish a composite until a separate
case-size master and matching pilot comparison are inspected. Compositing
approximates indirect ink reflections and must be disclosed in every target
recipe/page. Preserve prior source files, manifests, passes and archived code.

## 6.3 × 5.4 mm case preparation

`CP_Elec_6.3x5.4.step` is valid, with total bounds 7.8 × 6.6 × 5.4 mm and
SHA-256 `46f919e715e7690f361feabe141d4bd6686ba8f411c7ff5092774b828dd02c71`.
The dark top sector aligns with negative pad 2. C3345 / RVT1A221M0605
(220 µF 10 V) is prepared as pilot; C3344 / RVT1V470M0605 (47 µF 35 V)
has a guarded recipe and passed identity, rating and polarity checks. Prior
files are under `tmp/display_render/rvt_6_3x5_4_pilot_previous/` and
`rvt_6_3x5_4_batch_previous/`. Neither is rendered or published; check and
preview the pilot first. The compositor now includes this case and its latest
archived hash is `ff644a11214a085661eebb03303c82941a7365cd6fced89c4426a25075a5c28f`;
no shared aluminium passes have yet been generated or reviewed.

The 4 mm pilot preview passed; its full render is running in exec session
75970. Earlier notes describing that preview as pending are superseded.

The combined aluminium queue, compositor guard, marking and metadata suite
passed 43 tests on 2026-11-18. This validates the checks and metadata logic; it
does not substitute for individual model, composited-image and page review.
The 5 mm pilot model check is running in exec session 60324; the 4 mm full
render remains active in session 75970.

The 4 mm, 6.3 × 7.7 mm and 10 mm queues now explicitly disclose the planned
shared-pass compositing and approximate indirect ink reflections. All eleven
recipes were rechecked against their guarded source records and 12 targeted
tests passed. Previous queue scripts and registry are saved in
`tmp/display_render/rvt_composite_disclosure_previous/`. None of these
composites has yet been rendered or validated against a pilot.

Six additional source-guard tests passed across the prepared package queues,
checking rejection of a changed manufacturer or distributor identifier,
footprint or height. These tests do not replace visual model review.

## C3353 height discrepancy

The source record for C3353 / RVT1E221M0810 is named and dimensioned
8 × 10.5 mm and references `CP_Elec_8x10.5`. [LCSC](https://www.lcsc.com/product-detail/C3353.html)
and [JLCPCB](https://jlcpcb.com/partdetail/HonorElec-RVT1E221M0810/C3353)
list the package as 8 × 10.5 mm but their seated-height field says 10.2 mm.
[Another supplier](https://www.unikeyic.com/products/aluminum-capacitors/rvt1e221m0810/8369829.html)
also reports 10.2 mm. The Honor RVT series drawing lists 8 × 10.2 mm with a
±0.5 mm length tolerance, which may explain but does not prove the mismatch.
Review exact manufacturer documentation and disclose the discrepancy before
selecting geometry; no recipe or source-data correction has been made.

The 5 mm pilot model check passed: its total scaled bounds are 6.5 × 5.3 ×
5.4 mm and the illustrative marking is `100 / 10V`. It still needs visual
preview and final render; prior in-progress check notes are superseded.

The 4 mm pilot's full render and page were inspected and validated; earlier
in-progress notes are superseded. Four 4 mm recipes await a shared master,
comparison to the pilot and individual image/page validation.

## Generic 220 µF / 10 V 6.3 × 7.7 mm illustration

The generic source previously rejected a different-height KNSCHA candidate.
Honor RVT1A221M0607 / C87859 is independently listed at the desired 6.3 ×
7.7 mm, 220 µF and 10 V. A display-only example recipe and evidence are
prepared by `display_render_rvt_6_3mm_generic_220uf_queue.py`; a test passed
for unchanged procurement state and identity rejection. The recipe explicitly
states that no supplier is selected, uses the reviewed 6.3 mm model and
discloses approximate shared compositing. Previous files are in
`tmp/display_render/rvt_6_3mm_generic_220uf_previous/`. The source procurement
record has not been changed; the image and README remain pending pilot, shared
pass comparison and individual inspection.

C3353 has now been prepared as an 8 × 10.5 mm illustrative pilot using
KiCad `CP_Elec_8x10.5.step`, SHA-256
`ae35c4f1043bc64d44be9822563a47867ce2b6bed1663a1144d81c9b58368562`.
The valid single-root model's total bounds are 9.5 × 8.3 × 10.5 mm; its dark
sector aligns with negative pad 2. An exact manufacturer-part table reports
10.5 mm, but the supplier's seated-height field reports 10.2 mm, so the
recipe/evidence expressly disclose uncertainty. Previous files are under
`tmp/display_render/rvt_8x10_5_pilot_previous/`. The model check is running
in exec session 43520; visual preview and final render are still needed.

The C3353 8 × 10.5 mm model check passed with total bounds 9.5 × 8.3 ×
10.5 mm and illustrative `220 / 25V` marking. Its supplier-height discrepancy
remains disclosed, and preview/final visual checks are still required.

The 4 mm RVT shared material master is running in exec session 4737. Once
finished, compare a pilot composite against the independent full render,
then inspect all four candidate images and validate their provenance/pages.

The 4 mm RVT shared body pass completed; the ink pass is active in session
4737. Compare the finished composite with the independent pilot before any
batch publication.

The 10 × 10.2 mm shared RVT master is running in session 29212 using the
current archived standard renderer. After completion, compare the composite
pilot to the independent published pilot before rendering the three prepared
10 mm recipes. Inspect markings and validate each page and manifest.
