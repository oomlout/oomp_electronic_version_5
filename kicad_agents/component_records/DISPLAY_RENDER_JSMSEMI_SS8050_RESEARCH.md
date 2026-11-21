# JSMSEMI SS8050 SOT-23 display evidence

Reviewed 2026-11-21 against the existing local
`parts_source/electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050/datasheet.pdf`,
SHA-256 `73ae45af414373d3eee33ebfe40390a183b9c599244be2aaa46e45582dace1cf`.
The JSMICRO/JSMSEMI sheet's first page shows SS8050, 25 V and 1.5 A, and an
illustration labelled **Y1**. Page 4 gives the SOT-23 drawing, with body
length 2.70–3.10 mm, overall width 2.20–2.60 mm and height 0.90–1.10 mm.
The page 1 Y1 graphic supports the device code but does not establish the
complete production marking, typeface or exact placement.

The source record selects SOT-23W, but its KiCad model spans 2.9 mm across the
leads, outside the local drawing's 2.60 mm maximum. The KiCad SOT-23 model
spans 2.5 x 3.0 x 1.2 mm and is vertically scaled to 1.1 mm for display. It
is a closer visual approximation to the reviewed drawing; the original
SOT-23W footprint remains unchanged. Geometry, finish and lettering are
approximate and this is not manufacturing CAD.
