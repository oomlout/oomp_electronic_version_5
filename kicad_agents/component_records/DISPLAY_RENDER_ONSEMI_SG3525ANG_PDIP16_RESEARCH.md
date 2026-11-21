# onsemi SG3525ANG PDIP-16 display research

Reviewed 2026-11-20. The source record explicitly identifies onsemi SG3525ANG
and DIP-16, has no selected KiCad footprint, and gives generic 10 x 5 mm
dimensions without a reference. The [onsemi data sheet](https://www.onsemi.com/download/data-sheet/pdf/sg3525a-d.pdf)
lists this exact orderable in PDIP-16, case 648-08. The data sheet's extracted
marking diagram gives fixed `SG3525AN` and variable assembly, lot, year and
week fields. A display can omit variable codes but must disclose omissions,
typeface, placement and orientation as illustrative. The manufacturer drawing
has not yet been visually checked; the web extraction alone is not proof of
all placement details.

The case 648-08 drawing text gives 18.80-19.55 mm length and 6.35-6.85 mm
width. The generic source 10 x 5 mm dimensions conflict and must be disclosed.
A local KiCad `Package_DIP.3dshapes/DIP-16_W7.62mm.step` candidate exists;
inspect model bounds, material colours, actual body and lead shape against the
manufacturer package before selecting it. Do not use a socket model. This
render is display-only, not a validated footprint or mechanical model.
No PDF has been downloaded during this research.

KiCad source inspection: one valid root, SHA-256
`17a30b1f0ab3fd5384a1231e3c63c394888d5b952c542a8c189e023ed3467464`;
overall 7.874 x 19.177 x 6.98 mm including projecting pins. Its generic body
length falls within the extracted 18.80-19.55 mm maker range; the two colours
are body and metal, and the moulded notch indicates pin-one end. The source
10 x 5 mm dimensions differ. Actual maker drawing dimensions and marking
placement have not been visually checked, so disclose the approximation.
