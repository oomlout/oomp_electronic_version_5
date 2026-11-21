# ProTek PSM712-LF-T7 SOT-23 display evidence

Reviewed 2026-11-21 against the existing local
`parts_source/electronic_diode_tvs_array_sot_23_protek_psm712_lf_t7/datasheet.pdf`,
SHA-256 `a3a92d04a81e2da531b9b41e0cccef41b9e3797f970d1869f2db96148f4ab233`.
Page 1 identifies the ProTek PSM712 in SOT-23; page 2 gives device marking
**712**. Page 5 gives package length 2.80–3.04 mm, lead span 2.10–2.50 mm
and height 0.89–1.11 mm. Page 6 explicitly lists base PSM712, lead-free `-LF`
and tape suffix `-T7`, and says a variable date code accompanies the fixed
marking. The date code is omitted in this display.

The KiCad SOT-23 model has 2.5 x 3.0 x 1.2 mm overall bounds and is scaled
vertically to 1.1 mm to fit the drawing. The fixed code is documented;
typeface, position, finish and omitted production code are illustrative.
This is a display model, not manufacturing CAD or a footprint.
