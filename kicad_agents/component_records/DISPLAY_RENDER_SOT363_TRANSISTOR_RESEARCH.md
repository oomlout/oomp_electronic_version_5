# SOT-363 transistor display research

Local manufacturer PDFs reviewed 2026-11-21; no external file was added.

* `MMDT3906DW` (CBI): `parts_source/electronic_transistor_sot_363_6_bipolar_pnp_dual_general_purpose_40_volt_200_milliamp_cbi_mmdt3906dw/datasheet.pdf`, SHA-256 `5304f7811d556f0192aaa78ec6d05a6de53b68ca7aab2131d1af46b2cec56693`. Page 1 lists marking **K3N**. Page 3's drawing gives body length 2.00–2.20 mm, overall lead span 2.15–2.45 mm and height 0.90–1.10 mm.
* `BCM857BS-7-F` (Diodes Incorporated): `parts_source/electronic_transistor_sot_363_6_bipolar_pnp_dual_matched_pair_45_volt_100_milliamp_diodes_incorporated_bcm857bs_7_f/datasheet.pdf`, SHA-256 `cb26f2ade2c320dae17ed6ea22b4ca7bee8550c04b490324150289c00c3336ff`. Page 1 lists the exact orderable and **M3W** product code, along with variable date characters. Page 4's drawing gives length 2.00–2.20 mm, lead span 1.80–2.20 mm, and seated height 0.90–1.00 mm.

The KiCad SOT-363/SC-70-6 model is 2.1 x 2.0 x 1.1 mm overall. It is about
0.05 mm narrower across leads than the CBI drawing's minimum; for the Diodes
part the display model is vertically scaled to 1.0 mm to match the drawing.
This does not change source dimensions or footprints. Codes are supported by
the sheets; typeface, placement, finish and omitted variable markings are
illustrative. Display only, not verified manufacturing geometry.
