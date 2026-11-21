# Nexperia BAV70 and BAV99 SOT-23 diode display evidence

Reviewed 2026-11-21. The existing local PDF for `BAV70,215` is
`parts_source/electronic_diode_switching_dual_common_cathode_sot_23_nexperia_bav70_215/datasheet.pdf`,
SHA-256 `8af3a1214cc19d081bd8604ed1cdb98dc83dbb5a91bbdfba3663484a78450108`.
Page 2 identifies SOT-23 and `A4` followed by a variable manufacturing-site
character. [Nexperia's product record](https://www.nexperia.com/chemical-content/BAV70.html)
identifies the exact BAV70,215 orderable as SOT-23.

The existing local PDF for `BAV99,215` is
`parts_source/electronic_diode_switching_dual_series_sot_23_nexperia_bav99_215/datasheet.pdf`,
SHA-256 `826c982f4f2bbefcc047abea7ed2be517c09cf46bf61c10c25e4b7c378369b2f`.
Page 2 identifies SOT-23 and `A7` followed by a variable site character;
[Nexperia's product series](https://www.nexperia.com/products/diodes/switching-diodes/series/BAV99-SERIES.html)
lists the exact BAV99,215 orderable. The variable site characters are omitted.

Both sheets describe a nominal 2.9 x 1.3 x 1.0 mm body; the previously
reviewed Nexperia SOT-23 outline in the local 2N7002 family sheet permits
0.9–1.1 mm height, 2.8–3.0 mm body length and 2.1–2.5 mm lead span. The
KiCad model's 2.5 x 3.0 x 1.2 mm overall bounds are scaled vertically to
1.1 mm for display. Source dimensions and footprints remain unchanged.
Marking codes are documented; typeface, position, finish and omitted site
code are illustrative. Display only, not verified manufacturing geometry.
