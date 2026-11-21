# Analog Devices ADE7953ACPZ LFCSP-28 display research

Reviewed 2026-11-20. Catalogue ID implies Analog Devices ADE7953ACPZ, but
manufacturer and exact orderable source fields are empty, so both are inferred.
Source specifies 5 x 5 x 0.9 mm and selects a KiCad QFN-28 5 x 5 mm footprint
with a 3.35 mm exposed pad; its generic drawing depicts a 2.1 mm centre box
and roughly 0.714 mm terminal pitch.

Analog Devices' [ADE7953 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADE7953.pdf)
identifies ADE7953ACPZ as CP-28-10, 5 x 5 mm body, 0.75 mm nominal height
(0.70-0.80 mm), 0.5 mm pitch and 3.14 mm nominal exposed pad (3.04-3.24 mm).
These conflict with source height, drawing pitch/box and selected 3.35 mm pad.
Do not change source fields; disclose all differences in display documentation.
Manufacturer drawing was read from web extraction, not visually reviewed.
Physical package text was not verified; `ADE7953` is an illustrative family
identifier only, with font, placement, maker logo and production marks omitted.

Local KiCad `QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm.step` is the selected
footprint's model but has an oversized pad relative to the maker range; inspect
geometry, colour and hash, and consider a more accurate model or explicitly
approximate pad. A display is not a verified footprint or mechanical model.
No manufacturer PDF was downloaded in this review.

The selected KiCad model inspection found one valid root, SHA-256
`e9d6d740f505b03e5aa0ac826330f9e269344b84656d051f50eb07ac162749eb`,
5 x 5 x 0.92 mm overall bounds and separate body, metal and pin-indicator
colours. Its height exceeds the 0.80 mm maker maximum; a display-only vertical
scale to 0.75 mm is needed. The 3.35 mm exposed pad is still oversized and
must be corrected or explicitly disclosed; do not stage without evaluating a
closer model or geometry adapter.

Correction after inspecting actual STEP face geometry (session 90630): despite
the KiCad filename/footprint land name `EP3.35x3.35mm`, the exposed metal pad
in the model is approximately 3.15 x 3.15 mm with a chamfer, within ADI's
3.04-3.24 mm package range. The earlier assertion that the model pad itself
was 3.35 mm was based on its filename and is superseded. The selected
footprint's named 3.35 mm land still differs from the manufacturer package
pad, and the generic source drawing's 2.1 mm box remains conflicting. The
inspected source model height 0.92 mm remains above the maker maximum; scale
display geometry vertically to 0.75 mm and disclose the scale. Pin indication
and exact orientation require visual review.
