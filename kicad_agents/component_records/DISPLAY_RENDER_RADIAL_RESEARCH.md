# Radial aluminium capacitor display research

Reviewed 2026-11-18. Seven catalogue records share 8 mm diameter × 12 mm
body and 3.5 mm lead spacing; for example C2749 / KM107M050F12RR0VH2FP0
is 100 µF 50 V and uses `Capacitor_THT:CP_Radial_D8.0mm_P3.50mm`.
Its [LCSC listing](https://www.lcsc.com/product-detail/Aluminum-Electrolytic-Capacitors-Leaded_LCSC-100uF-50V_C2749.html)
identifies the exact part. The [manufacturer KM-series document for another
value](https://datasheet.lcsc.com/lcsc/1810271410_CX-Dongguan-Chengxing-Elec-KM226M050D11RR0VH2FP0_C43346.pdf)
describes repeated sleeve value/voltage, negative-polarity stripe and series
marking. Its part-number table identifies sleeve and printing colour codes;
confirm the exact C2749 suffix against the source before choosing colours.
Do not invent a manufacturer logo or date code. No PDF was downloaded.

Installed KiCad `CP_Radial_D8.0mm_P3.50mm.step` has one valid root,
SHA-256 `abedfe603cd28231e16fb158d7b3f8875be74514f602e356364f48f073d0ef8e`,
and overall bounds 8 × 8 × 10 mm. Its sleeve extends approximately z 0–8 mm,
with lead ends at z -2 mm, so it is shorter than the 12 mm body record. Do
not scale the entire model vertically, which would change lead dimensions.
A reviewed per-region body-height adapter or accurate sourced model is needed;
check seams, stripe orientation relative to the negative lead, metal top and
lead geometry. Existing top-projection text is unsuitable for sleeve text:
implement a cylindrical UV/marking mapping and inspect text and stripe from
the selected camera before a final render. Disclose any dimensions or artwork
that remain illustrative. No recipe, image or page has been produced.

`kicad_agents/radial_display_geometry.py` now provides standalone helpers
for lengthening only a reviewed straight sleeve region while preserving
leads/end details, and for seam-aware per-triangle cylindrical UVs. It
rejects triangles crossing deformation boundaries rather than bending them
silently. Four synthetic geometry and UV tests passed. These helpers are not
wired into the renderer and have not been checked against the real STEP
mesh or visually rendered; integration, boundary/normal validation, model
orientation and actual sleeve text review remain necessary.

Real-mesh audit: the initial rounded 2.14 mm lower deformation boundary
was rejected for three material groups because it crosses actual triangles.
OCCT face inspection locates the straight sleeve start at approximately
2.135020857 mm and its upper edge at 7.8 mm. A second check using those
precise boundaries is running in exec session 28842. Do not integrate the
deformation until all material regions pass and boundary normals/seams have
been visually verified.

The real 8 mm radial KiCad mesh accepted the precise 2.135020857–7.8 mm
stretch interval for all four material groups. The transformed sleeve runs
z 0–12 mm while the lead group still reaches z -2 mm. This is a geometry
check only: normals at boundaries, sleeve UV orientation, seam, appearance
and a final pilot render remain unverified before renderer integration.

Real-mesh cylindrical mapping check: after the reviewed sleeve stretch,
288 coating-side triangles and 323 stripe-side triangles mapped without a
seam span over 0.009 in normalized circumference; the mapped vertical range
covered the straight sleeve. This confirms numerical UV continuity for
those selected triangles only. Renderer integration, camera orientation,
normal transitions, stripe markings and visual comparison remain unverified.

The KiCad stripe's straight side is centered at x ≈ 5.64 mm, y ≈ 0,
on the positive-X side of the can centered at x 1.75 mm. The matching
footprint puts pad 1 at x 0 and pad 2 at x 3.5 mm; the reviewed polarized
symbol makes pad 2 negative. The standard camera points toward the part
from positive X / negative Y, making this stripe potentially visible near
the side. Exact stripe artwork and its projection still require a visual
preview; do not infer production printing placement from this geometry.

Boundary-normal handling has been strengthened: the stretch helper selects
the inverse-transpose transform from incident triangles and rejects shared
sloped normals that span the deformation kink. Five synthetic tests pass,
including normal transformation and ambiguity rejection. A renewed real-mesh
check with this implementation is running in exec session 94253; the earlier
real-mesh acceptance used the previous normal implementation and must not be
treated as validation of this change.

The revised boundary-normal implementation accepted all four material groups
of the real KiCad radial mesh. The helper now also selects triangles wholly
on a reviewed cylindrical sleeve; six synthetic tests pass, including
selection, normal and seam cases. The new selection function still needs
real-mesh verification and none of these helpers is wired into the renderer
or visually validated.

The new straight-sleeve selector was verified against the actual STEP mesh:
288 coating and 323 polarity-stripe side triangles were selected, with UV
seam spans below 0.009. The C2749 pilot evidence and draft recipe are staged
in `DISPLAY_RENDER_RADIAL_8MM_100UF_50V_EVIDENCE.md` and
`source_file/display_render/experimental_radial_recipes.json`; the draft is
intentionally outside the live registry until a dedicated radial renderer
is implemented, checked and previewed. The former source files are backed
up under `tmp/display_render/radial_8mm_pilot_previous/`.

An isolated experimental renderer, `kicad_agents/display_render_radial.py`,
now contains the geometry helpers, separates the straight printable sleeve
from the ends, applies cylindrical per-corner UVs and generates an illustrative
three-line ink mask. It reads only `experimental_radial_recipes.json`; nothing
has entered the live registry. Two adapter tests passed for lead preservation,
face selection, UV output and text-mask generation. Real-model `--check` is
running in exec session 20696; no preview has been generated. The renderer,
lighting, seam, orientation, stripe and normal transitions require visual
inspection and its source must be archived before any publication.

The isolated radial renderer's real-model `--check` completed successfully:
source bounds are 8 × 8 × 10 mm including leads, and the stretched display
bounds are 8 × 8 × 14 mm, with a 12 mm body above the board and 2 mm of lead
below. The illustrative marking is `100uF / 50V / KM 105C`. The recipe is
still experimental and no preview or final image has been rendered.

For a future reviewed 8 × 12 mm KM batch, exact supplier listings include
[KM107M063F12RR0VH2FP0 / C2772](https://www.lcsc.com/product-detail/C2772.html),
[KM227M035F12RR0VH2FP0 / C2063](https://www.lcsc.com/product-detail/C2063.html),
[KM337M025F12RR0VH2FP0 / C2051](https://www.lcsc.com/product-detail/C2051.html),
and [KM475M250F12RR0VH2FP0 / C2775](https://item.szlcsc.com/3156.html).
Check each source record and visual marking separately after the pilot. GR
series parts must not inherit KM appearance or markings without evidence.

The staged pilot's 2048 × 1024 ink mask was generated and inspected: it
contains only the illustrative `100uF`, `50V` and `KM 105C` lines, without
a logo or lot code. This checks the source texture, not its projection or
appearance on the curved sleeve. The actual 3D preview is still pending.

The 700 px / 32 sample preview in `tmp/display_render/radial_8mm_pilot_preview`
was inspected: curved value, voltage and illustrative series marking are
legible, and the negative stripe is on the visible sleeve. The main registry
now contains the reviewed pilot recipe; the standard renderer rejects this
family and directs it to the radial renderer. Both current renderer sources
are archived by hash. Seventeen radial geometry, guard and metadata tests
passed. Full-quality pilot is running in session 46146 to a scratch directory;
it must be visually inspected and validated before publication.

The 1400 px / 256 sample pilot completed and was visually inspected, then
published for the exact 100 µF / 50 V part. Hashes, metadata and page were
validated. Its markings, sleeve and colour remain illustrative. The source
renderer hash is archived and prior files are backed up in
`tmp/display_render/radial_8mm_pilot_previous/`. Other KM values still need
individual evidence, recipe checks, image inspection and publication.

The CX KM 220 µF / 35 V C2063 candidate has supplier-checked evidence in
`DISPLAY_RENDER_RADIAL_KM_220UF_35V_EVIDENCE.md`, an identity-guarded recipe
in `display_render_radial_km_220uf_queue.py`, and a visually inspected
700 px / 32 sample preview in `tmp/display_render/radial_220uf_35v_preview`.
Ten queue/geometry tests passed. A 1400 px / 256 sample final is running in
session 74950 to `tmp/display_render/radial_220uf_35v_final`. Inspect it
before copying to the part and publishing; validate hashes, README, polarity
and source metadata. The KM document and catalogue operating-temperature
range differ; the electrical record has not been changed.

The CX KM 4.7 µF / 250 V C2775 candidate has exact supplier evidence in
`DISPLAY_RENDER_RADIAL_KM_4_7UF_250V_EVIDENCE.md` and an identity-guarded
recipe in `display_render_radial_km_4_7uf_queue.py`. It has not yet been
previewed, rendered or published; inspect the decimal marking and polarity
before a full render. The operating-temperature discrepancy is documented.

The 220 µF / 35 V radial final completed and was visually inspected and
published; hashes, metadata, markings and README validated. The 4.7 µF /
250 V candidate has a low-quality preview running in session 38508; inspect
it before starting any final.

The 4.7 µF / 250 V C2775 preview was visually inspected: the decimal,
voltage and negative stripe are visible. The 1400 px / 256 sample final
is running in session 40568 to `tmp/display_render/radial_4_7uf_250v_final`.
Inspect it, preserve prior part files, publish and validate only after it
completes. Artwork and colour remain illustrative.

The 4.7 µF / 250 V final was inspected, published and validated; earlier
in-progress notes for that part are superseded.

Prepared exact KM 100 µF / 63 V C2772 and 330 µF / 25 V C2051 recipes
using `display_render_radial_km_batch02_queue.py`, with supplier/series
evidence in `DISPLAY_RENDER_RADIAL_KM_BATCH02_EVIDENCE.md`. Eleven targeted
queue and radial geometry tests passed. Neither candidate has been previewed,
rendered or published; inspect each marking before full rendering, preserve
prior files and validate pages. Temperature-source discrepancies remain noted.

## KS 4 x 7 mm radial group: research, not yet rendered (2026-11-19)

Three catalogue records select Chengx KS105M050C07RR0VH2FP0 (C2760, 1 uF/50 V), KS225M050C07RR0VH2FP0 (C2065, 2.2 uF/50 V), and KS336M016C07RR0VH2FP0 (C3314, 33 uF/16 V). Their 4 x 7 mm case and 1.5 mm lead spacing are supported by the respective [C2760](https://jlcpcb.com/partdetail/3141-KS105M050C07RR0VH2FP0/C2760), [C2065](https://jlcpcb.com/partdetail/2417-KS225M050C07RR0VH2FP0/C2065), and [C3314](https://www.lcsc.com/product-detail/C3314.html) listings. The [manufacturer's KS336 specification](https://doc.chipmall.com/datasheet/rev_2501081354_cx-dongguan-chengxing-elec-ks336m016c07rr0vh2fp0_c80919328.pdf) identifies black PVC with white print for the 33 uF example; the exact artwork remains to be reviewed. It was viewed online, not downloaded. Of the three source directories, only C2760 currently contains a local datasheet; do not state the other PDFs have been captured.

KiCad 10 has `Capacitor_THT.3dshapes/CP_Radial_D4.0mm_P1.50mm.step`. Inspect its model and actual 7 mm body height, negative lead and sleeve mapping before building a recipe. Inspect each individual marking and use explicit illustrative disclosure when its actual production artwork is not established. This research does not establish that the three cans share identical artwork.

The KS336 manufacturer outline specifies D = 4 mm, L = 7 mm, F = 1.5 mm, 0.45 mm lead diameter, and `Vent > Phi 6.3`. Do not assume that an engraved pressure vent on a generic 4 mm KiCad model represents this part; inspect and disclose or correct the model geometry as appropriate.

The locally installed 4 mm KiCad STEP has SHA-256 `0b3df9c2ac243b2ec8cdfd919c97a826f512783901f259a9918ba28836e91262` and total bounds X -1.25..2.75, Y -2..2, Z -2..4 mm. Thus the model's upper extent is 4 mm above the seating plane; an accurate 7 mm sleeve requires reviewed stretching of the straight body, preserving the lead and end geometry. A face/colour geometry diagnostic is running in session 47435; use its results to establish stretch boundaries and verify whether the top has a vent before authoring a recipe.

The 4 mm KiCad STEP face diagnostic completed: the top metal includes a cross-shaped groove, but the KS336 drawing says the vent is for diameters greater than 6.3 mm. A separate `kicad_agents/display_render_flat_top.py` adapter and targeted test file were prepared to replace the top metal with an unvented disk while retaining leads, with checks for unexpected geometry. It is not integrated into the renderer and has not yet been checked against the real triangulated model or visually reviewed. The known straight sleeve region is approximately Z 2.105..3.8 mm; verify precise boundaries with real geometry before using the existing stretch operation. Wait for existing full renders before modifying the renderer source, since their provenance depends on it.

The KS336 exact-part evidence now has its own pinned-source candidate document, `DISPLAY_RENDER_RADIAL_KS_33UF_16V_EVIDENCE.md`. A real-model test is running in session 3155: it loads KiCad's coloured STEP, applies the experimental flat-top adapter and checks the proposed 3 mm straight-sleeve stretch. Do not integrate or publish until the test passes and a preview is inspected. The existing full render sessions 59863 and 17107 remain live.

The session 3155 real-model test completed: flat-top replacement succeeded on 46,094 source triangles, but sleeve stretching rejected a boundary-crossing triangle with rounded lower Z 2.105. That failure is a useful safety check, not a successful model validation. A precision geometry inspection is running in session 45552 to determine the actual cylindrical-face boundaries before repeating the check. No KS render has been published.

The 4 mm KiCad model's straight cylinder has exact lower boundary Z 2.105151982969 and upper Z 3.8 mm. Session 38487 successfully applied the unvented top and 3 mm straight-sleeve stretch on the real coloured mesh: final bounds Z -2..7 mm and 287 sleeve triangles. This is geometry validation only; integrate with pinned provenance and inspect a preview before publication.

The 8 x 12 mm KM 100 uF / 63 V preview is running in session 49626, output `tmp/display_render/radial_km_100uf_63v_preview`. Inspect the marking, stripe and material before a full render. Keep the radial renderer source unchanged while that session runs so its manifest records the source actually used.

The reviewed 4 mm KS336 recipe is staged by `display_render_radial_ks_pilot_queue.py`; it is not published. The unvented-top helper was integrated directly into `display_render_radial.py` so its source is covered by the renderer hash. Both old and new source versions were archived, and ten targeted flat-top, queue and radial tests passed. Its 700 px / 32 sample preview is running in session 19714 at `tmp/display_render/radial_ks_33uf_16v_preview`: inspect the unvented top, stripe, markings and materials. The 100 uF / 63 V KM preview was inspected and its 1400 px final is running in session 25552 at `tmp/display_render/radial_km_100uf_63v_final`. Do not modify the radial renderer while either process is live. Earlier notes referring to a standalone adapter are superseded.

The KS336 33 uF / 16 V preview was visually inspected: the unvented top, negative stripe and value/voltage are visible. Its full render is live in session 4689 at `tmp/display_render/radial_ks_33uf_16v_final`. Individually guarded 1 uF / 50 V C2760 and 2.2 uF / 50 V C2065 recipes were staged by `display_render_radial_ks_batch01_queue.py`; neither has been previewed, rendered or published. Their evidence explicitly describes the appearance as an inference from a related KS specification. The C2760 source directory has a local PDF; the C2065 source directory does not.

## KM 10 x 17 mm radial candidates: research only (2026-11-19)

Individual supplier pages identify [C3336](https://www.lcsc.com/product-detail/C3336.html), KM107M100G17RR0VH2FP0, as 100 uF / 100 V; [C5300](https://www.lcsc.com/product-detail/C5300.html), KM156M400G17RR0VH2FP0, as 15 uF / 400 V; and [C2064](https://jlcpcb.com/partdetail/2416-KM477M035G17RR0VH2FP0/C2064), KM477M035G17RR0VH2FP0, as 470 uF / 35 V. All three list 10 x 17 mm bodies and 5 mm pin spacing. The manufacturer KM document previously reviewed for the 8 mm family and the C5300/C2064 supplier pages give a -40 to +105 C range, whereas the present source records give -55 to +125 C. Record this discrepancy; do not silently edit electrical data. Artwork and sleeve appearance are unverified. KiCad `CP_Radial_D10.0mm_P5.00mm.step` is the candidate, but its face colours, geometry, polarity and required sleeve extension must be measured before authoring a recipe. No PDF was downloaded and none of these three parts has been rendered or published as a result of this research.

KiCad 10 mm radial model bounding-box and cylindrical-face diagnostic is running in session 17263; inspect its output and use precise face boundaries before stretching a pilot. It is read-only and does not establish material mapping or polarity by itself.

KiCad 10 mm P5 STEP measured SHA-256 `7367f35dd5439e325ba3912de65e9200831fdc6698080ffd056cd268649ba41d`, bounds X -2.5..7.5, Y -5..5, Z -2..10 mm. Its straight upper sleeve is Z 2.13502085691..9.8 mm. C2064 470 uF / 35 V is staged as the 10 x 17 mm pilot with a 7 mm straight-sleeve extension in `display_render_radial_km_10x17_pilot_queue.py`; five targeted queue tests passed. Real mesh and material check runs in session 17471. Check polarity against footprint, inspect preview and full render before publishing. Temperature discrepancy is explicitly documented; no source electrical data changed.

The C3336 100 uF / 100 V and C5300 15 uF / 400 V KM 10 x 17 mm recipes were staged by `display_render_radial_km_10x17_batch01_queue.py`; neither was previewed, rendered or published. Per-part evidence and the temperature discrepancy are in `DISPLAY_RENDER_RADIAL_KM_10X17_BATCH01_EVIDENCE.md`. Do not render before pilot geometry and polarity are verified, then individually inspect both markings.

Staged KM228M016G20RR0VH2FP0 / C3328, 2200 uF / 16 V, as the 10 x 20 mm pilot in `display_render_radial_km_10x20_pilot_queue.py`. Its candidate 10 mm model uses a 10 mm straight-sleeve extension; identity, dimensions and polarity are guarded. The supplier temperature discrepancy is in `DISPLAY_RENDER_RADIAL_KM_2200UF_16V_10X20_EVIDENCE.md`. It has not yet passed real-mesh, polarity or preview checks and is not published. The related GR C3311/C3312 parts require their own series evidence and are not covered by the KM recipe.

The 10 x 17 mm KM pilot real-mesh check passed with bounds 10 x 10 x 19 mm including 2 mm leads and 99,474 triangles. The KiCad D10/P5 footprint has pad 1 at X=0 and pad 2 at X=5 mm; the source stripe section lies on the positive-X side. A 700 px preview is running in session 95571 at `tmp/display_render/radial_km_10x17_470uf_35v_preview`; inspect markings, stripe and material before a full render. Seven 10 x 17 and 10 x 20 queue tests passed.

The KM C2772 and KS C3314 final renders were visually inspected, published and validated; earlier running notes are superseded. The 10 x 17 mm C2064 preview was inspected and its full render is running in session 8417 at `tmp/display_render/radial_km_10x17_470uf_35v_final`. Two GR 10 x 20 mm candidates C3311 and C3312 are staged in `display_render_radial_gr_10x20_batch_queue.py` using their own GR evidence and markings. Three GR/KM queue tests passed. These remain unrendered; verify the 20 mm model and each preview before publication.

## 6.3 x 11 mm radial pair: research only (2026-11-19)

[LCSC C2029](https://www.lcsc.com/product-detail/C2029.html) identifies Chengx KM106M100E11RR0VH2FP0 as 10 uF / 100 V, and [LCSC C2036](https://www.lcsc.com/product-detail/C2036.html) identifies GR227M010E11RR0VH4FP0 as 220 uF / 10 V. Both list 6.3 x 11 mm, 2.5 mm lead spacing and polarization. The KM C2029 supplier reports -40..+105 C, differing from its source record's -55..+125 C; do not silently alter electrical data. The KM and GR series use distinct illustrative markings and need individual preview inspection. A read-only KiCad D6.3/P2.5 bounding and cylinder diagnostic is running in session 37841. The model's geometry, materials, sleeve deformation and stripe-to-pad polarity must be checked before rendering. No PDF was downloaded.

**GR colour correction:** the [exact Chengx GR108M010F12RR0VL4FP0 / C3299 specification](https://xonstorage.z8.web.core.windows.net/pdf/chengxing_1000uf10v_Lcs01_link.pdf) says green body and gold print. Earlier black/white assumptions based on a generic GR series image are insufficient for individual parts, particularly those sharing its VL4 suffix. Unstaged both unrendered GR 10 x 20 candidates C3311/C3312 and added a staging guard pending individual colour review and support for appropriate materials. Do not infer C3311 or C5154 colours solely from the suffix; check exact evidence. Four targeted staging/identity tests passed. No GR render was published from those recipes.

The 6.3 mm KiCad model measured SHA-256 `39dc7bf95fed00917ab20af81ff9e25a70f8d003bc07cffea11840489a11933e`, source bounds 6.3 x 6.3 x 8.3 mm including 2 mm leads, and upper sleeve Z 2.13502085691..6.1 mm. The C2029 KM 10 uF / 100 V 6.3 x 11 mm pilot is staged using a 4.7 mm straight-sleeve extension in `display_render_radial_km_6x11_pilot_queue.py`; it still requires real-mesh, polarity and preview checks. The C3328 10 x 20 mm real-mesh check passed, and its preview is running in session 58742 at `tmp/display_render/radial_km_10x20_2200uf_16v_preview`.

Prepared (not staged) an exact green/gold C3299 GR pilot in `display_render_radial_gr_green_pilot_queue.py` with exact manufacturer evidence in `DISPLAY_RENDER_RADIAL_GR_1000UF_10V_EVIDENCE.md`. A palette prototype and tests are in `display_render_radial_palettes.py` and its test file. Six targeted tests passed, including guards that keep the uncertain C3311/C3312 GR candidates unstaged. Integrate the reviewed palette into the versioned radial renderer only after live radial renders 8417 and 58742 complete; archive both old and new source hashes, update tests and remove the temporary separate helper so provenance includes the palette. Preserve black/white defaults. Then stage C3299, inspect green/gold preview and verify polarity; exact shade and layout remain illustrative. The 6.3 x 11 mm C2029 real-model check is running in session 11706.

The [Chengx part-number key](https://xonstorage.z8.web.core.windows.net/pdf/chengxing_1000uf10v_Lcs01_link.pdf) explicitly defines sleeve background L = green, H = black, and ink 4 = gold. Thus C3311 VL4 and C3312 VH4 now have separately reviewed green/gold and black/gold recipes, respectively; both remain unstaged until versioned renderer palette support is integrated. C2033/C5154 VL4 and C2036 VH4 are similarly researched in `DISPLAY_RENDER_RADIAL_GR_EXTRA_EVIDENCE.md` and prepared (not staged) by `display_render_radial_gr_extra_queue.py`. Four targeted colour/queue tests passed. The C3328 10 x 20 mm preview was visually inspected; its 2200 / 16V marking and negative stripe are visible. Start its full render after integrating palettes, once live radial sessions permit. C2029 6.3 x 11 mm model check passed (13 mm total including leads, 65,673 triangles); the footprint has pad 2 at X=2.5 mm on the stripe side. Its preview runs in session 80895 at `tmp/display_render/radial_km_6x11_10uf_100v_preview`.

The radial renderer now includes the reviewed black/white, green/gold and black/gold palettes; its old and new source hashes are archived, and 11 targeted geometry, palette and queue tests passed. C3299 and the five individually coded GR candidates are staged but not published; inspect each, starting with the green/gold C3299 preview running in session 70807 at `tmp/display_render/radial_gr_green_1000uf_10v_preview`. The C2029 KM 6.3 x 11 mm preview was inspected, and its final render remains to be started. The C2064 final was published and validated; earlier running notes are superseded. The generic 1210 68 uF TDK example has a visually inspected preview and a full render running in session 59184 at `tmp/display_render/tdk_1210_68uf_example_final`. Its page must prominently disclose the existing 10 x 5 mm versus 1210 dimension conflict and avoid asserting the example's voltage as a generic rating; preserve existing source records.

The visually reviewed KM C2029 (10 uF / 100 V, 6.3 x 11 mm) final is running in session 94124 at `tmp/display_render/radial_km_6x11_10uf_100v_final`. The visually reviewed KM C3328 (2200 uF / 16 V, 10 x 20 mm) final is running in session 81662 at `tmp/display_render/radial_km_10x20_2200uf_16v_final`. Inspect both final images, back up page/source files, publish exact parts and validate hashes, metadata, README and disclosed temperature discrepancies before counting.

## Larger KM radial candidates: research only (2026-11-19)

The 16 x 25 mm records select KM228M035K25RR0VH2FP0 / C2763 (2200 uF / 35 V) and [KM476M450K25RR0VH2FP0 / C2746](https://jlcpcb.com/partdetail/3127-KM476M450K25RR0VH2FP0/C2746) (47 uF / 450 V). Verify C2763 ratings from its [exact supplier entry](https://www.lcsc.com/product-detail/C2763.html) before authoring its recipe. The 18 x 30 mm records select [KM107M400L30RR0VH2FP0 / C2767](https://www.lcsc.com/product-detail/C2767.html) (100 uF / 400 V) and [KM688M025L30RR0VH2FP0 / C2754](https://www.lcsc.com/product-detail/C2754.html) (6800 uF / 25 V). Both 18 mm listings and the 16 mm C2746 listing say 7.5 mm pitch and -40..+105 C, while their local records claim -55..+125 C; do not silently change source ratings. The Chengx numbering key says VH2 means black sleeve and white printing, but the exact lettering, stripe and finish are illustrative. KiCad 10 has D16/P7.5 and D18/P7.5 STEP models; inspect each distinct source's bounds, face colours, polarity and deformation boundaries before any recipe or render. No PDF was downloaded.

C2763 was independently confirmed at [LCSC](https://www.lcsc.com/product-detail/C2763.html) as KM228M035K25RR0VH2FP0, 2200 uF / 35 V, 16 x 25 mm, 7.5 mm lead spacing. KiCad D16/P7.5 and D18/P7.5 bounding/face inspection is running in session 78032; inspect both outputs before constructing size-specific model recipes.

The green/gold C3299 preview was inspected: green sleeve, gold text and stripe, and 1000 uF / 10 V are legible. Its full render is running in session 36734 at `tmp/display_render/radial_gr_green_1000uf_10v_final`; inspect and validate before publication. Four large KM recipes were staged by `display_render_radial_km_large_queue.py`, backed by `DISPLAY_RENDER_RADIAL_KM_LARGE_EVIDENCE.md`; the targeted identity/model test passed. The 16 mm C2746 real-mesh check is running in session 38443. Neither size has yet been visually reviewed or published. The 16 mm source STEP hash is `6ff24b1ad7161c52fa605740f3e2cf292a57964021404ee4b828c6577e1ba561`, upper cylinder Z 2.13502085691..15.8 mm. The 18 mm hash is `ae2d8bf5ddd7b73271c87f1ad63a3849077d694adcf3577672131e4ba0364c02`, cylinder Z 2.13502085691..17.8 mm.

The C2746 16 x 25 mm real-mesh check passed with bounds 16 x 16 x 27 mm including 2 mm leads and 116,256 triangles. KiCad's D16/P7.5 footprint has pad 1 at X=0 and pad 2 at X=7.5 mm on the model stripe side. Its 700 px preview is running in session 7369 at `tmp/display_render/radial_km_16x25_47uf_450v_preview`; inspect lettering, stripe and finish before a final render. The separate 18 mm model still needs its own real-mesh and polarity checks.

The C2029 and C3328 final renders were inspected, published and validated; earlier in-progress notes are superseded. The C2746 16 x 25 mm preview was inspected and its full render is live in session 81891 at `tmp/display_render/radial_km_16x25_47uf_450v_final`.

The 18 mm D18/P7.5 footprint places pad 1 at X=0 and negative pad 2 at X=7.5 mm, on the source stripe side. Its C2767 real-mesh check is running in session 87998; verify that result before preview. The GR C2036 black/gold 220 uF / 10 V preview is running in session 79714 at `tmp/display_render/radial_gr_black_6x11_220uf_10v_preview`; inspect actual colours, markings and stripe before full rendering or publication.

The 4 x 7 mm C2065 KS 2.2 uF / 50 V candidate is rendering a 700 px preview in session 13262 at `tmp/display_render/radial_ks_2_2uf_50v_preview`. Inspect the decimal point, negative stripe, unvented top and material before full rendering; artwork remains illustrative.
