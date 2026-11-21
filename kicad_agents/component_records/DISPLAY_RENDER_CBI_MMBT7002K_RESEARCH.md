# CBI MMBT7002K SOT-23 display research

The existing local CBI PDF
`parts_source/electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_300_milliamp_cbi_mmbt7002k/datasheet.pdf`,
SHA-256 `fba5368f324b0423d16ee03fbfdebacab2af893e000ce73ec74b5887f396fab8`,
was reviewed 2026-11-21. Page 1 identifies MMBT7002K, 60 V, 300 mA and
SOT-23; page 3 gives overall lead span 2.20–3.00 mm, body length
2.70–3.10 mm and height 0.95–1.40 mm. It does not specify top marking.

The [Diotec MMBT7002K product page](https://diotec.com/en/product/MMBT7002K.html)
lists `K72` for its own part. That is a different manufacturer and does not
establish the CBI part's marking. Here `K72` is an illustrative family
example only; actual CBI code, typeface and production details are unverified.
The KiCad SOT-23 model is 2.5 x 3.0 x 1.2 mm and is scaled to 1.1 mm in the
display scene, within the cited outline ranges. This is a display model, not
manufacturing geometry or a footprint.
