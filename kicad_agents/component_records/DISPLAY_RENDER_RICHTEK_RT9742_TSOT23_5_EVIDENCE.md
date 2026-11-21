# Richtek RT9742CGJ5 TSOT-23-5 display evidence

Reviewed 2026-11-20. Source record gives exact orderable RT9742CGJ5, dimensions
2.9 x 1.6 mm and no KiCad footprint. Its manufacturer field is empty, so
Richtek is inferred from the part identity, existing local manufacturer sheet
and catalogue ID; do not silently write a manufacturer into source data.

The existing local `parts_source/electronic_ic_power_management_high_side_power_switch_with_flag_tsot_23_5_richtek_rt9742cgj5/datasheet.pdf`
has SHA-256 `8683bdd544157dcf4600c70bef2533c5fe54ee2806af49b99fcad1fe1d9d4f01`.
Page 2 was visually inspected: Richtek maps this exact orderable to TSOT-23-5
and product code `0K=`; the similarly named FC version is a different code.
The [Richtek source document](https://www.richtek.com/assets/product_file/RT9742/DS9742-10.pdf)
also gives package height 0.7–1.0 mm, body width 1.397–1.803 mm, body length
2.692–3.099 mm, overall span 2.591–3.0 mm and lead pitch 0.838–1.041 mm.
Page 1 pinout matches the source record. No download was necessary.

The previously inspected KiCad `TSOT-23-5.step` SHA-256
`5120f0cee43ef7743cc08408d2c12f234fcac7355386e330a3a16f336e23da8d`
has 2.8 x 2.9 x 0.95 mm overall bounds within those ranges. The fixed `0K=`
is manufacturer-listed; typeface, orientation, placement and any variable
production markings are illustrative. The pin indicator is from the KiCad
model and its physical appearance is illustrative. This is a display model,
not a verified footprint or engineering model.
