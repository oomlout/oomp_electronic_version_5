# Display models, package markings and studio renders

For a detailed execution checklist suitable for GPT-6.1 Terra, read
[DISPLAY_RENDER_TERRA_RUNBOOK.md](DISPLAY_RENDER_TERRA_RUNBOOK.md) after this guide.
The [ready-to-paste launch prompt](DISPLAY_RENDER_TERRA_PROMPT.md) requests up to
five existing 0603 resistor variants using the reviewed adapter. Preparing these
instructions does not run that batch or select a model automatically.

Build one explicitly selected component preview at a time. This pipeline creates
display images, not manufacturing geometry. Keep the duplicate-listing repair
task paused. Do not resume it, change the project repository, commit, push, or
launch unreviewed whole-catalogue generation. A user-authorized catalogue-wide
render effort can process reviewed, resumable batches in the requested order.

## Working pilot

`electronic_resistor_0603_10000_ohm` represents the selected UNI-ROYAL
`0603WAF1002T5E`, a 10 kOhm 1% thick-film resistor. The generic catalogue record
has other supplier options, so this is one sourced appearance, not a promise
that every alternative looks identical.

The installed KiCad 0603 STEP has separate face colours for protective coating,
ceramic and terminations. The adapter maps those reviewed colours to separate
materials and keeps the original geometry. It verifies the 1.6 x 0.8 x 0.45 mm
envelope. Read the STEP's copyright/license header and retain it in provenance.

The local UNI-ROYAL datasheet, page 3, section 4(6), gives the 0603 E96 marking
policy. Value 100 is code 01 and multiplier 100 is C, producing **01C** for 10 kOhm.
Page 4 gives dimensions and additional underlined E24 marking rules. Do not
substitute the procurement code `1002`, or a generic `103` marking, for this
specific series. Typeface, ink colour and positioning remain visual approximations.

## Files and responsibilities

| File | Responsibility |
| --- | --- |
| `source_file/display_render/recipes.json` | Exact part selection, external model reference/hash, colour-to-material mapping, marking evidence and layout |
| `source_file/display_render/studio.json` | Shared camera, softboxes, floor, exposure and framing |
| `kicad_agents/display_render.py` | Locate/import KiCad STEP, verify geometry, texture and path-trace one part |
| `kicad_agents/display_render_composite.py` | Optional reviewed 0603 marking composites from shared path-traced material passes |
| `kicad_agents/package_markings.py` | Tested exact marking policies, with no rounding or guessed IC codes |
| `kicad_agents/display_render_resistor_queue.py` | Discover reviewed UNI-ROYAL 0603 E96 and underlined E24 recipes from matching existing supplier records |
| `kicad_agents/display_render_small_resistor_queue.py` | Discover UNI-ROYAL 0201/0402 unmarked parts, including reviewed 0201 5% and exact-MPN variants |
| `kicad_agents/display_render_multi_0201_queue.py` | Validate five exact Walsin, YAGEO and KOA unmarked 0201 selections |
| `kicad_agents/display_render_yageo_small_queue.py` | Discover exact YAGEO RC_L 0201/0402 records using the documented unmarked-body rule |
| `kicad_agents/display_render_fenghua_small_queue.py` | Discover exact Fenghua RC 0201/0402 records using the documented unmarked-body rule |
| `kicad_agents/display_render_fenghua_rs_queue.py` | Discover Fenghua RS 5% 0805/1206 parts while rejecting contradictory tolerance records |
| `kicad_agents/display_render_uniroyal_five_percent_queue.py` | Discover exact UNI-ROYAL 5% 0603/0805/1206 variants and their three-character markings |
| `kicad_agents/display_render_uniroyal_low_value_queue.py` | Discover reviewed UNI-ROYAL low-value decimal, 0603 E96 and zero-ohm markings |
| `kicad_agents/display_render_fenghua_array_queue.py` | Discover evidenced Fenghua RC-MT08W four-resistor arrays |
| `kicad_agents/display_render_uniroyal_array_queue.py` | Discover evidenced UNI-ROYAL 4D02/4D03 four-resistor arrays |
| `kicad_agents/display_render_ralec_array_pilot.py` | Prepare the exact RALEC RTA03-4D303JTP four-resistor array |
| `kicad_agents/display_render_ralec_rtt_queue.py` | Discover exact RALEC RTT05/06 1% and 5% resistors and reviewed marking codes |
| `kicad_agents/display_render_yageo_axial_queue.py` | Discover exact YAGEO MFR-25 1% axial parts and their five colour bands |
| `kicad_agents/display_render_large_resistor_queue.py` | Discover reviewed UNI-ROYAL 0805/1206 records with documented four-digit markings |
| `kicad_agents/display_render_fojan_queue.py` | Discover exact FOJAN FRC records using separately reviewed FOJAN marking evidence |
| `kicad_agents/display_render_fojan_low_queue.py` | Discover FOJAN decimal MPNs with package-specific markings |
| `kicad_agents/display_render_fojan_5pct_queue.py` | Validate FOJAN 5% parts with individually verified supplier identities |
| `kicad_agents/inspect_display_model.py` | Inspect a KiCad STEP model's bounds, face colours and hash before reviewing a recipe |
| `kicad_agents/display_render_inventory.py` | Report valid renders, prepared recipes, legacy images and records requiring research |
| `source_file/display_render/renderer_versions/` | Byte-for-byte historical renderer sources, named by SHA-256, to keep inspected prior renders attributable |
| `kicad_agents/publish_display_render.py` | Refresh only the selected existing component's source metadata, page and web manifest |
| `kicad_agents/display_render_contact_sheet.py` | Assemble an optional labelled review sheet from existing final images |
| `requirements-display-render.txt` | Optional isolated renderer dependencies |
| `parts/<id>/data/display_render/` | Final PNG, compact WebP preview and provenance manifest |

Source geometry is read from installed KiCad. No STL, duplicate STEP, GLB or
`.blend` is exported. Temporary OBJ tessellation and texture masks are removed
after each run. Store geometry once externally and vary text/material recipes.
The normal catalogue workflow must never start an expensive render implicitly.

## Run the pilot

From the repository root in PowerShell, the pilot environment already exists at
`tmp/display_render_env`. To recreate it on another machine

```powershell
python -m venv tmp/display_render_env
tmp/display_render_env/Scripts/python.exe -m pip install -r requirements-display-render.txt
```

The optional PyMuPDF package is only needed to review PDF evidence. It is not a
rendering dependency. Install it into the same environment when needed.

```powershell
tmp/display_render_env/Scripts/python.exe -X utf8 -m kicad_agents.display_render electronic_resistor_0603_10000_ohm --check
tmp/display_render_env/Scripts/python.exe -X utf8 -m kicad_agents.display_render electronic_resistor_0603_10000_ohm --output tmp/display_render/preview --pixels 700 --samples 32
tmp/display_render_env/Scripts/python.exe -X utf8 -m kicad_agents.display_render electronic_resistor_0603_10000_ohm
python -X utf8 -m kicad_agents.publish_display_render electronic_resistor_0603_10000_ohm
```

Open the preview before the final render, and inspect the final image before publishing. The default output is the exact part's
`data/display_render` directory. A rerun replaces only that selected render set.
Use `--output` for experiments so an approved render stays intact.
Intact outputs are reused when recipe, scene, code, dependency versions, font and
artifact hashes match. Use `--force` to render an unchanged recipe deliberately.

To compare finished images without rendering or regenerating catalogue data, use
`python -m kicad_agents.display_render_contact_sheet --part <exact-id> "Short label"`
for each part, followed by `--output tmp/display_render/contact_sheet.png`. The
command requires every final image to exist and fails if a label would be clipped.

Model discovery supports machine-wide and per-user KiCad installations. Set
`OOMP_KICAD_3DMODEL_DIR` or `--model-root` to override the 3dmodels root. The existing
`OOMP_KICAD_ROOT` is also respected by installation discovery. Nothing depends on
the screw checkout being present. Repository-relative recipe paths work if the
`C:\gh` base changes. The reviewed font is local Arial Bold; set `OOMP_MARKING_FONT`
explicitly for another font, then review the result. Do not copy proprietary font
files into the repository. The manifest records the font's hash.

## Adding a resistor variant with a small model

1. Read `ADDING_COMPONENTS.md`, this file and the pilot recipe. Select exactly one
   existing component ID. Check its manufacturer, MPN, value and tolerance in
   population data and the current source record.
2. Find the model referenced by its verified KiCad footprint. Check imperial vs
   metric size, dimensions and orientation. Reuse a package recipe only when the
   package and material regions match. Hash changes require a deliberate review.
3. Read the exact manufacturer's marking table. Check the local datasheet before
   downloading another copy. Use the established browser workflow for new PDFs.
   Record document, page, hash, rule and evidence status. A part number alone does
   not prove the package's printed text.
4. Add one recipe. For a verified UNI-ROYAL 0603 E96 variant, change the exact ID,
   MPN and `resistance_ohm` while retaining the reviewed package/material mapping.
   Confirm the computed code independently. Unsupported values must stop, not
   round to a nearby E96 value. Underlined E24 and zero-ohm rules need explicit
   reviewed policies or verified literal text.
5. Run `--check`, then a small preview. Check the marking reads left-to-right,
   is not mirrored or clipped, stays within the coating, and has no visible decal
   border. Inspect metal ends, the ceramic edge, contact shadow and highlights.
6. Render the selected final image. Validate its manifest hashes and dimensions.
   Inspect at full size and at 512 px. Keep texture subtle: small components must
   not look like concrete, scratched sheet metal or embossed lettering.
7. Refresh only this component's metadata/README/web manifest when publishing it
   into the catalogue. No taxonomy or library change is needed for a display image.
   Leave all model, marking and render limitations visible beside the preview.

## Pipeline expansion requirements

The importer handles reviewed single-root, coloured STEP models with explicit
material-role sets. The current recipes cover one chip resistor, one ceramic
capacitor and one SOIC-8 IC. It rejects unknown colours, missing models, wrong
dimensions and unsupported assemblies. It does not yet support all KiCad
packages, VRML/GLB import, curved markings or automatic model substitution.

| Family | Geometry/material adaptation | Marking policy |
| --- | --- | --- |
| Chip resistors | Shared package mesh, ceramic/core, top coating, metal ends | Manufacturer-specific E96/E24/literal or explicitly unmarked |
| MLCC capacitors | Tan/grey ceramic and plated terminals | Usually unmarked; verify the series rather than painting capacitance on it |
| Electrolytic capacitors | Sleeve, exposed metal, insulating base; cylindrical UV mapping | Verified capacitance/voltage series text and polarity stripe |
| Tantalum/polymer capacitors | Moulded case and metal terminals | Verified value/voltage code and polarity bar, with correct polarity convention |
| ICs | Separate mould compound and leads/pads; planar top marking; pin-one feature | Exact manufacturer top-mark lookup, line order and pin-one orientation |
| Connectors | Separate housing and contacts, multipart assembly transforms | Logos/cavity numbers only where verified |

IC date/lot codes are not derivable from MPNs. Omit them unless an example is
explicitly documented as illustrative. Do not add brand logos from memory.
Unmarked parts are valid completed results. For IC bodies, a laser mark should
change colour/roughness subtly instead of looking like thick white paint.

The checked recipes now also include a Samsung 0603 MLCC and a TI NE555DR
SOIC-8. The colour-region importer supports their explicit reviewed material
role sets, including a separate pin-one indicator. Their source review is in
[the three-family evidence record](component_records/DISPLAY_RENDER_THREE_FAMILIES_20261117.md).
The [final three-family contact sheet](../source_file/display_render/examples/three_families.webp)
compares the current 1,400 px renders.
An unmarked illustration is distinct from a verified unmarked component: the
Samsung specification has not established an absence of markings. The IC's
`NE555` text is documented, while typography and placement are illustrative.
Only reuse these mappings for models with independently verified geometry,
colours, dimensions, orientation and marking evidence.

Additional corroboration: a historical [Samsung board specification](https://pdfcoffee.com/samsung-bn4400428bled-power-supply-sch-pdf-free.html)
lists SEMCO `CL10B104KB8NNNC` among its 1608 X7R capacitors and notes that those
capacitors have no markings. This is useful evidence for that application, but
is not a current Samsung Electro-Mechanics marking policy for every production
lot; retain the explicit illustration limitation in the render recipe.

Each reviewed model declares `required_roles`; omitted means the original
resistor roles `coating`, `ceramic`, `termination`. The complete set of
observed roles must match exactly. The IC pin-one colour maps to
`pin_indicator`, not ceramic. For an evidence-limited blank illustration use
`unmarked_illustration` with an evidence record and a clear appearance-status
limitation. Reserve `none` for a verified unmarked package; do not turn lack of
evidence into a factual claim. The renderer still requires a real local evidence
record with a pinned hash. A written review that links a manufacturer source is
not a downloaded datasheet and must say so. Prefer an existing local manufacturer
PDF where one is available. If a text evidence file is hashed, add a specific
`text eol=lf` entry for it to `.gitattributes` and ensure the local file uses LF
before pinning its hash. The hashed renderer and marking-code files have the same
line-ending rule; this keeps provenance valid across Windows and Unix checkouts.

For the next family, implement and test one adapter, then one reviewed recipe.
Only then reuse it across values. New code should retain scale/orientation checks,
material-region accounting and explicit evidence states. A missing KiCad model
may use a separately labelled drawing-based visual proxy; never silently replace
a failed import with a generic box and call it the KiCad model.

## Studio and storage policy

The reference is the [screw product studio](https://github.com/oomlout/oomp_hardware_screw_version_5/blob/main/screw_model_render.py).
It uses Blender/Cycles with AgX, an orthographic camera, three rectangular lights,
a neutral world and a matte seamless floor. This electronics implementation uses
the existing project's Mitsuba approach with the same presentation principles,
an ACES fitted highlight curve and sRGB output. It does not claim to reproduce
Blender's AgX pixel-for-pixel.
The 0201/0402 UNI-ROYAL recipes use smooth materials without the fine bump
texture: that texture produced non-finite path samples at those small package
proportions. The manifest records disabled material roles and any isolated
non-finite pixels repaired from valid neighbours; widespread failures abort.
The final pilot uses 1,400 pixels, 256 samples per pixel and light non-local-means
denoising to remove Monte Carlo noise while retaining the marking edges.

Use satin metal terminations, a dark nonmetallic coating, slightly warm ceramic,
and a matte pale ink mark. Keep reflection highlights broad enough to show edge
shape without turning the metal white. The camera is grounded and consistently
framed from the package envelope. Seeds and renderer parameters are recorded.

Keep the high-resolution PNG and a small WebP preview. The JSON recipe and
manifest should be tiny relative to images. Do not retain temporary meshes,
per-part scene files, redundant render resolutions, CAD exports or duplicated
PDFs. A compact interactive GLB could be considered later if actually requested.

## Checks

```powershell
python -m pytest kicad_agents/tests/test_package_markings.py -q
python -m pytest kicad_agents/tests/test_display_render_metadata.py -q
git diff --check
```

The real pilot render is the integration test for source scale, STEP material
regions and texture orientation. Automated marking tests cover all 96 values
over the supported multipliers, plus the two printed manufacturer examples.
Record tool versions, source hashes, image dimensions, byte sizes and evidence
gaps in the manifest. Retain KiCad attribution and its original license header.

Before changing the renderer, copy its exact bytes to
`source_file/display_render/renderer_versions/<sha256>.py`. The metadata checker
accepts a previous manifest only when its exact renderer hash matches the current
file or an untampered archived source, and its recipe, studio, evidence and output
hashes remain current. Never manufacture an archive for a renderer you cannot
verify. New renders still record the actual current renderer source.

For UNI-ROYAL 0603 1% variants, run `python -m
kicad_agents.display_render_resistor_queue --report tmp/display_render/resistor_discovery.json`
to inspect the candidates, then add confirmed recipes with `--add`. It validates
the existing exact MPN, manufacturer, footprint and shared datasheet reference;
it does not invent suppliers or render or publish images. The E96 table is used
only for exact values. Datasheet page 4 section 4(7) requires E24 values outside
E96 to use a three-digit code with a continuous underline; the recipe records
`underline: true` and the renderer draws that mark. Review the resulting preview
before rendering. Unsupported identities and values are reported for separate
review, not silently omitted as completed.

FOJAN's FRC series has its own [evidence record](component_records/DISPLAY_RENDER_FOJAN_EVIDENCE.md).
Use `python -m kicad_agents.display_render_fojan_queue --report
tmp/display_render/fojan_discovery.json` to inspect its source-backed candidates.
The supported FOJAN cases are unmarked 0201/0402, exact E96 0603, 0603 E24
exceptions with `underline_character: 1`, and four-digit 0805/1206 values.
FOJAN's underline belongs beneath the middle character; do not replace it
with UNI-ROYAL's full-width underline. Inspect a rendered marking against the
manufacturer evidence before processing a new batch.

If LLVM is installed, put its `bin` directory on the process `PATH` before
rendering. Mitsuba then selects its LLVM CPU backend when available, otherwise
the scalar backend. The manifest records which backend was used; a backend
warning alone is not a successful render. Never change quality settings merely
to make a queue finish faster.

### Reusing an unmarked resistor image

For a documented unmarked chip resistor whose complete visual recipe matches an
already inspected, independently rendered image, use
`python -m kicad_agents.reuse_unmarked_display_render TARGET_ID SOURCE_ID`.
The helper checks the model, material roles, studio, output settings, renderer,
source artifact hashes and the target's evidence. It preserves existing outputs
and records the reuse and source-manifest hash; it does not claim a fresh render.
Review the target evidence and image, then publish its exact ID with
`python -m kicad_agents.publish_display_render TARGET_ID`. Never use this to
infer an unmarked body from absent data or to reuse a marked package image.

### Fenghua RS 5% chip resistors

`display_render_fenghua_rs_queue.py` verifies the exact RS-05/06 J-series
manufacturer part, 5% catalogue ratings, value and footprint. It rejects a
record if any explicit tolerance conflicts with 5%. The manufacturer sheet
specifies three-character E24 codes and uses `R` as a decimal point. Confirm
the shared datasheet belongs to the selected manufacturer: historical source
records may incorrectly reference a UNI-ROYAL family sheet.

### FOJAN 5% supplier identity recovery

Some historical FOJAN records contain only the suffix `TS` as their MPN.
Never infer a full MPN from value alone. The exact verified supplier listing,
including LCSC code and URL, is pinned in the separate
`component_records/DISPLAY_RENDER_FOJAN_SUPPLIER_IDENTITIES*.json` ledgers;
the queue validates identity, value, tolerance, footprint and E24 code against
the selected ledger. Use `--evidence` to select a ledger; never edit one
already referenced by published manifests without refreshing them. The third
ledger identifies secondary sources used to associate LCSC codes with MPNs;
keep those limitations explicit. Preserve previous source records before
repairing a truncated MPN.

For YAGEO RC_L 1% 0805 and 1206 resistors,
`display_render_yageo_large_queue.py` checks the MPN, value, footprint and
tolerance before applying the four-digit manufacturer marking documented in
`component_records/DISPLAY_RENDER_YAGEO_RC_L_LARGE_EVIDENCE.md`. Inspect each
new render; the generic package, font and material finish are illustrative.

`display_render_uniroyal_named_queue.py` handles a small reviewed set of
generic 5% IDs and exact 1% variant IDs omitted by earlier naming patterns.
It checks their explicit part identities and catalogue tolerance before using
the existing UNI-ROYAL marking adapters.

`display_render_huaxing_axial_queue.py` validates Huaxing MF1/4W 1% parts
against the online manufacturer specification, using five documented colour
bands. The requested beige finish is illustrative: that specification states
blue. Keep this distinction visible in each recipe and page.

`display_render_cco_axial_queue.py` similarly checks the individually verified
CCO MPNs in the `component_records/DISPLAY_RENDER_CCO_MF_IDENTITIES_*.json`
ledgers and uses the CCO manufacturer's five-band table. Select a later ledger
with `--evidence`. Its specified sky-blue coating
differs from the requested illustrative beige; retain that disclosure. Do not
edit an identity ledger already hashed by published manifests.

`display_render_vo_axial_queue.py` covers VO MF1/4W 1% parts using a
standards-based five-band representation. The VO sheet calls for MIL/EIA colour
codes but does not state each part's band count; preserve that limitation in
the recipe and README and do not claim a production-lot match.
Unverified listings need further research.

### FOJAN low-value chip resistors

FOJAN FRC 0201/0402 devices are documented as unmarked. For 1% 0805/1206
below 100 Ω, the manufacturer gives a four-character R decimal code. The
0603 E96 table is separate; E24 values outside E96 use a short underline
beneath the middle character. `display_render_fojan_low_queue.py` validates
exact values and preserves these differences. A renderer without
`underline_character` support silently drops that line; use a compatible
archived renderer and inspect it visually. Metadata validation rejects
character-underlined recipes if the recorded renderer lacks that support.
The 2023 manufacturer evidence is linked in
`component_records/DISPLAY_RENDER_FOJAN_LOW_EVIDENCE.md`.

### UNI-ROYAL low-value chip resistors

`display_render_uniroyal_low_value_queue.py` verifies the manufacturer,
primary part number, value and KiCad footprint against the local UNI-ROYAL
2019 data sheet. For 0805 and 1206 1% values below 100 Ω it places the
decimal point as `R`, preserving three significant digits: 10 Ω is `10R0`,
2.2 Ω is `2R20`, and 0.1 Ω is `R100`. The 0603 1% E96 policy uses its
separate multiplier table; a 0603 0 Ω jumper normally carries `0`. For 0603
1% E24 values between 1 and 10 Ω that are outside E96, the reviewed 2017
manufacturer specification gives the same three-character decimal code as
5%, with a full underline: for example `2R2`, `4R7` and `5R1`. See
`component_records/DISPLAY_RENDER_UNIROYAL_0603_LOW_EVIDENCE.md`. Review
other exceptions separately.

### RALEC RTT chip resistors

`display_render_ralec_rtt_queue.py` admits exact RALEC RTT05/RTT06
manufacturer records with a matching value, tolerance and footprint. The
manufacturer's reviewed 2011 marking table gives three-character 5% codes
and four-character 1% codes, with `R` as a decimal point below 100 Ω for 1%
or below 10 Ω for 5%. Read the evidence record before extending this rule.
The generic KiCad 1206 model is 0.05 mm longer than the specified maximum,
so its display description states the discrepancy. A conflicting
manufacturer suffix is not automatically corrected or rendered.

### Axial resistor colour bands

`display_render_uniroyal_mfr0w4_queue.py` covers two selected 1% UNI-ROYAL
MFR0W4 axial parts, using documented five-band coding and brown tolerance.
The beige finish is illustrative; see `DISPLAY_RENDER_UNIROYAL_MFR0W4_EVIDENCE.md`.

The individually reviewed `display_render_yageo_mfr50s_queue.py`,
`display_render_uniroyal_mf006_queue.py`, and `display_render_cco_mf1_2ws_queue.py`
cover compact selected parts rated 500 or 600 mW in legacy quarter-watt IDs.
Keep the rating discrepancy explicit in each page and do not infer suitability
from its ID. `display_render_vo_mo_1m2_queue.py` illustrates a selected 5%
metal-oxide part with a gold tolerance band; its standard band layout and beige
coating are illustrative. Each queue checks the exact identity and rating and
links its own evidence record. Inspect the preview and final output, then publish
only that component.

The zero-ohm Yageo axial jumper recipe uses one centered black band and a
beige body as an explicitly illustrative convention. The selected part's
actual marking and coating remain unverified; zero-ohm jumpers have no
resistance-tolerance band. See `DISPLAY_RENDER_YAGEO_AXIAL_JUMPER_EVIDENCE.md`.
The direct renderer accepts a single black band only for this jumper form.

The YAGEO MFR-25 axial recipe uses five documented bands around the KiCad
DIN0207 model. The first three bands are significant digits, the fourth is the
multiplier, and the separated brown fifth band is 1% tolerance. The renderer
maps the stripes along the model's X-axis and keeps them around the cylindrical
body; the traditional beige coating, band colours and spacing are illustrative.
When selecting a representative axial part, prefer an evidenced 5% part with
a gold tolerance band where it fits the catalogue record. The tolerance band
must reflect the documented part: gold for 5%, brown for 1%; never recolour a
1% part gold. The leads are bent to the selected 7.62 mm footprint. The checked manufacturer
specification is linked in `component_records/DISPLAY_RENDER_YAGEO_AXIAL_EVIDENCE.md`;
no local PDF is claimed. Inspect each new colour combination and render at full
quality before publishing. Jumpers, other tolerances and other series need their
own reviewed rules. The separately reviewed 5% YAGEO CFR-25 6.8 kΩ
example uses the four-band sequence blue / grey / red / gold; its source is
`component_records/DISPLAY_RENDER_YAGEO_CFR_EVIDENCE.md`. Its four-band texture
is rendered directly; the five-band compositor cannot be used for it.
`display_render_yageo_cfr_queue.py` validates further CFR-25 5% records before
preparing four-band recipes. `display_render_vo_carbon_queue.py` identifies
reviewed VO CR 5% candidates; the VO specification references standard
colour codes without confirming the exact band count, so its four-band layout
must be described as illustrative on the resulting page. Neither queue renders
or publishes automatically.
`display_render_cco_carbon_queue.py` validates individually evidenced CCO
CF1/4W 5% identities and uses the four-band code in CCO's manufacturer sheet;
the pinned supplier and document links are in the
`component_records/DISPLAY_RENDER_CCO_CF_IDENTITIES_*.json` ledgers. Select a
later ledger with `--evidence` and do not alter a published ledger's contents.

`display_render_ralec_small_queue.py` prepares unmarked RALEC RTT01/RTT02
parts using the manufacturer's documented rule. The reuse adapter validates
the current source identity and identical image-affecting settings before
copying an inspected 0201 or 0402 image. The existing local RALEC family PDF
is an older edition than the online marking evidence; identify them accurately.

`display_render_ralec_0603_queue.py` handles the reviewed 59 Ω RTT03 1%
EIAJ-96 marking `75X`. The 2.7 Ω RTT03 E24 exception remains unrendered until
the exact low-value marking and underline placement are independently verified.

For the reviewed five-band YAGEO MFR-25 setup only,
`kicad_agents.display_render_axial_composite` can reuse its verified beige
black/white material passes at 1,400 px and 256 samples. Run `render` with an
exact reviewed part ID, the master directory and a new scratch output path;
inspect every colour combination and validate its manifest before publishing.
The passes are archived under `source_file/display_render/masters/` with their
reference manifests and source hashes. Band colours are composited in linear
light; indirect reflections and colour interactions are approximate and
recorded in the resulting manifest and page. Do not use the five-band adapter
for four-band parts.

### Shared resistor material passes

For the explicitly reviewed 0603, 0805 and 1206 resistor models and the
4×0402 and 4×0603 convex resistor-array models, the composite
path renders the unmarked body and ink material at 1,400 px / 256 samples once,
then projects each evidenced marking into the same camera and blends in linear
light. It does not recompute how each marking affects indirect reflections. It
records that limitation on each page and in each manifest. Six direct comparisons
including full-width underlines had mean absolute differences of 1.1–1.9/255
within the marking in the pilot comparison. This is not a substitute for a new
package adapter or manufacturer marking evidence.
The 0805 and 1206 1 kΩ examples were each compared visually against an
independent direct render: mean whole-image channel differences were 0.17 and
0.14 out of 255 respectively. Other markings still need individual review.
Build a separate master using an evidenced part from each package size.
The 4×0402 array was compared with an independent 1,400 px direct path trace;
the mean whole-image channel difference was 0.22 / 255. Array models have their
own source-file license notices and their markings run along the long axis. The
4×0603 comparison was also inspected against a direct 1,400 px path trace; its
mean whole-image channel difference was 0.022 / 255.
Keep this separate from the marking rules for individual 0402 resistors.

```powershell
tmp/display_render_env/Scripts/python.exe -X utf8 -m kicad_agents.display_render_composite make-master electronic_resistor_0603_1000_ohm
tmp/display_render_env/Scripts/python.exe -X utf8 -m kicad_agents.display_render_composite render <exact-id> --output tmp/display_render/composite_review/<exact-id>
```

Inspect the scratch output before calling `render <exact-id>` without `--output`
for an unrendered part. The compositor refuses to overwrite an existing output.
Then use the normal exact-ID publisher. The master manifest, both shared images,
model, evidence and both source hashes are validated before metadata advertises
the result. Archive old source files by their exact hash before changing them.
If the machine or dependencies change, a new master may be required. Keep at
least 512 MiB free on the repository drive; the compositor stops below that limit.

## Completed pilot verification

For Fenghua RS-06 5% 1206 parts, use
`python -m kicad_agents.display_render_fenghua_rs_1206_queue` after checking
the source record. The adapter requires agreement between the exact selected
manufacturer part, its value, footprint and both recorded tolerance ratings.
The R-6.1 manufacturer sheet specifies three-digit E24 markings. A generic
catalogue record may contain old UNI-ROYAL fields from a different supplier;
reconcile these against the selected MPN, preserve the prior evidence and do
not present the unrelated PDF as the selected part's datasheet. The archived
1206 shared-pass renderer and its source hashes remain necessary for the
reviewed approximation; inspect every new marking before publication.
After changing a datasheet source, also inspect `parts/<exact-id>/data/datasheet.pdf`
and the regenerated README: an old shared PDF can persist after its source
pointer is removed. Verify its hash and identity, preserve a backup, and remove
it only when it is demonstrably unrelated; then republish the exact page and
confirm that the page links the reviewed source instead.

For Fenghua RC-02 5% 0402 parts, use
`python -m kicad_agents.display_render_fenghua_0402_5pct_queue` to find
exact reviewed candidates. The adapter rejects inconsistent tolerance, value,
footprint or manufacturer records. RS-02 is outside the reviewed document's
listed scope. Do not carry a UNI-ROYAL datasheet attribution over to a selected
Fenghua part; resolve the source record before publishing. Unmarked matching
packages may use `reuse_unmarked_display_render`, which verifies the recipe,
source image and pinned evidence; inspect the image and publish each exact ID.

`display_render_yageo_ac0402_queue.py` covers the specifically reviewed Yageo
AC0402JR-076M8L. Yageo's automotive AC series needs its own evidence; do not
assume that a generic RC-series rule proves its marking. The unmarked reuse
helper rechecks the exact source identity and evidence before reuse.

For the eight explicitly reviewed generic SAE 0201 entries,
`display_render_yageo_visual_0201_queue.py` provides Yageo reference images
with the same package, resistance and tolerance. Each page must state the
represented Yageo MPN and that the selected SAE part's appearance is
unverified. This is a display reference, not an assertion that all electrical
ratings match or a change to the selected supplier. Other references need
their own evidence and source checks before use.

`display_render_yageo_selected_0201_queue.py` prepares four further 0201
visual references for selected HWA CHN and GiantOhm parts. Their selected
markings are unverified, so retain the represented Yageo MPN and explicit
appearance and interchangeability disclosures. It validates the exact selected
identity, supplier listing, nominal value, tolerance and footprint. Discover
with `python -m kicad_agents.display_render_yageo_selected_0201_queue`; add
recipes only when disk space permits immediate rendering, inspection and
publication. Evidence is in `DISPLAY_RENDER_YAGEO_0201_SELECTED_REFERENCES.md`.

`display_render_yageo_selected_0402_queue.py` covers the 2.4 kΩ 0402
entry using the unmarked Yageo RC0402JR-072K4L visual reference. Its recorded
FOJAN supplier identity and appearance are unverified; preserve both
qualifications and the interchangeability disclosure. The selected listing
specifies 5%, while other distributor entries specify 1%; do not imply all
options have the pictured reference's tolerance. Evidence is in
`DISPLAY_RENDER_YAGEO_0402_SELECTED_REFERENCE.md`.

`display_render_yageo_small_selected_queue.py` covers 0201 10 MΩ,
0402 10 MΩ and the separate 5% 0402 150 kΩ record using unmarked Yageo
visual references. Preserve the selected-part appearance and interchangeability
limitations documented in `DISPLAY_RENDER_YAGEO_SMALL_SELECTED_REFERENCES.md`.

`display_render_yageo_generic_0201_queue.py` handles six source entries with no
supplier or tolerance. Their images show documented, nominally matching 1%
Yageo examples and must disclose that the generic entries have no selected
manufacturer or tolerance. The reuse helper verifies that the source remains
unsourced; if a supplier or tolerance is added, review the recipe again.
`display_render_yageo_generic_0402_queue.py` applies the same guarded approach
to three 0402 entries, with separate manufacturer and reference evidence.
`display_render_yageo_selected_0805_queue.py` covers three 5% 0805
entries whose selected FOJAN numbers are truncated to TS. It illustrates
specific, manufacturer-documented Yageo references, preserving the explicit
identity, appearance and interchangeability limitations. Check all value codes
and inspect shared-pass outputs before publication. Evidence is in
`DISPLAY_RENDER_YAGEO_0805_SELECTED_REFERENCES.md`.

`display_render_yageo_selected_1206_queue.py` handles seven analogous 5%
1206 records with truncated FOJAN identities. These show documented Yageo
examples with three-digit markings; retain their identity, appearance and
interchangeability disclosures. Review the evidence in
`DISPLAY_RENDER_YAGEO_1206_SELECTED_REFERENCES.md` and inspect every render.

`display_render_yageo_high_0805_queue.py` handles two additional 5% 0805
high-value entries with incomplete FOJAN identities. Their reference identities
and limitation statements are in `DISPLAY_RENDER_YAGEO_0805_HIGH_VALUE_REFERENCES.md`.

`display_render_yageo_hwa_0805_queue.py` covers two selected HWA CHN
0805 parts using Yageo references with matching value and tolerance. Their
selected HWA body markings remain unverified. Keep that limitation and the
full-interchangeability disclaimer; see `DISPLAY_RENDER_YAGEO_HWA_0805_REFERENCES.md`.

`display_render_ralec_0805_1r00_queue.py` handles RALEC RTT051R00FTP
under a legacy ID that incorrectly includes UNI-ROYAL. Preserve the explicit
manufacturer clarification; the ID requires separate taxonomy review. Its
RALEC family evidence is in `DISPLAY_RENDER_RALEC_0805_1R00_EVIDENCE.md`.

`display_render_ralec_0603_2r7_queue.py` prepares RALEC RTT032R70FTP.
Its underlined `2R7` is inferred by combining two family marking rules; the
reviewed document does not show this exact value. Preserve that disclosure and
`DISPLAY_RENDER_RALEC_0603_2R7_EVIDENCE.md`.

`display_render_fojan_frp1206_15r0_queue.py` prepares the selected FOJAN
FRP1206F15R0TSN 1% high-power part with `15R0`; the manufacturer-specific
evidence is in `DISPLAY_RENDER_FOJAN_FRP1206_15R0_EVIDENCE.md`. Its KiCad
body length is at the manufacturer tolerance limit.

`display_render_yageo_rl_generic_queue.py` prepares the unsourced 1210
0.1 Ω and 2512 0.015 Ω entries using documented Yageo RL current-sense
examples. The entries themselves do not specify manufacturer, tolerance or
power; retain those disclosures. See `DISPLAY_RENDER_YAGEO_RL_GENERIC_REFERENCES.md`.

`display_render_yageo_ac2512_13r3_queue.py` covers the corrected 2512
13.3 Ω Yageo AC selection and `13R3` marking. The former selected Stackpole
part was 133 Ω; replacing it does not establish full interchangeability. See
`DISPLAY_RENDER_YAGEO_AC2512_13R3_EVIDENCE.md`.

`display_render_yageo_pt2512_0r2_queue.py` covers the corrected 2512
0.2 Ω Yageo PT current-sense selection with its `R200` mark. The prior FH
selection was 2 Ω, and its replacement is not proof of full electrical
interchangeability. See `DISPLAY_RENDER_YAGEO_PT2512_0R2_EVIDENCE.md`.

`display_render_yageo_rt1206_133k_queue.py` prepares the selected Yageo
RT1206DRE07133KL thin-film 0.5% part using its RT-series `1333` marking.
The evidence is in `DISPLAY_RENDER_YAGEO_RT1206_133K_EVIDENCE.md`. Check the
2512 selected-value reconciliation history in `DISPLAY_RENDER_2512_VALUE_CONFLICTS.md`
before changing either affected component.

`display_render_fenghua_0603_2r7_queue.py` prepares the selected 5% 2.7 Ω
Fenghua RS-03L2R7JT with its documented `2R7` marking. The local Fenghua
family sheet and provenance are recorded in `DISPLAY_RENDER_FENGHUA_0603_2R7_EVIDENCE.md`.

`display_render_yageo_boundary_0805_queue.py` covers the 5% 110 Ω and
1% 10 MΩ 0805 records using documented Yageo visual references. The 110 Ω
selected Fenghua tolerance was corrected from 1% to 5%; retain the selected
identity and appearance disclosures. Evidence and limitations are in
`DISPLAY_RENDER_YAGEO_0805_BOUNDARY_REFERENCES.md`.

`display_render_yageo_generic_large_queue.py` covers six unsourced 0805 and
1206 entries with documented Yageo 1% reference parts and their four-digit
codes. Preserve the distinction between example and catalogue specification;
inspect each shared-pass output and publish by exact part ID.
`display_render_yageo_generic_0603_queue.py` handles four unsourced 0603
entries with specifically documented Yageo examples. Its evidence distinguishes
5% E24 codes from the 1% EIA-96 marking. Keep the example's tolerance distinct
from the unspecified generic entry, and review every output before publishing.
`display_render_yageo_generic_axial_queue.py` identifies five unsourced axial
entries with documented Yageo examples. Four CFR examples are 5% with gold
tolerance bands; the 53.6 kΩ MFR example is 1% and has a brown band. The
generic entries themselves do not specify tolerance. Use the approved five-band
shared-pass compositor only for the MFR example; render four-band CFR examples
directly and inspect each before publishing.
`display_render_generic_array_0402_queue.py` handles four unsourced 4×0402
array entries with identified UNI-ROYAL visual examples and checked three-digit
marks. `display_render_fenghua_array_jumper_queue.py` covers the selected
Fenghua RC-MT08W000JT jumper, whose manufacturer approval sheet specifies a
single `0` marking. Arrays are not individual 0402 resistors: verify the array
marking and eight-terminal model separately. `display_render_generic_array_0603_queue.py`
handles three unsourced 4×0603 examples after correcting their 10×5 mm placeholder
dimensions to the documented 3.2×1.6 mm package; inspect and refresh affected
dimension diagrams after correcting source data.
`display_render_yageo_yc124_queue.py` covers the selected Yageo
YC124-JR-0710KL 10 kΩ 4×0402 array. Yageo specifies its `103` marking; its
model height is at the manufacturer's tolerance limit. It has no local PDF;
the source record links the manufacturer specification reviewed online.

The [0603 example page](../parts/electronic_resistor_0603_10000_ohm/README.md)
contains the inspected final image. The imported envelope is 1.6 x 0.8 x 0.45 mm,
with 1,332 temporary triangles. The 1,400 px / 256-sample scalar CPU render took
517.3 seconds on the pilot machine. Its PNG, 512 px WebP and manifest total
202,839 bytes. An unchanged rerun reused the verified cache.

Twenty targeted marking, metadata and population-workflow tests passed. Artifact
hashes, README attribution and source/generated/web metadata propagation passed.
Only the selected component was updated, and its only source-data field change
was `display_render`. No mesh/CAD export or separate-project change was made.
