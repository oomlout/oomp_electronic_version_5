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
