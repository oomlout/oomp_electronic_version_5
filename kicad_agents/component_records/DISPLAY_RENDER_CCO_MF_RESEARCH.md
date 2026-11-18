# CCO MF axial follow-up, 2026-11-17

The manufacturer-authored [MF specification](https://datasheet.lcsc.com/datasheet/pdf/442097c559f2eb401b6de319ad027dae.pdf?productCode=C127223)
was reviewed online. Its marking table specifies five bands for 1% parts,
including a brown tolerance band. Its 1/4 W body dimensions include a nominal
6.5 mm length and 2.3 mm diameter, compatible with the existing nominal KiCad
axial model. The specification states sky blue; the requested beige finish is
illustrative. No local PDF has been
captured. Check the complete specification and source records before adding
recipes; this file does not claim any render has been made.

These supplier listings showed complete MPNs where the source records currently
contain only `T`. Verify each listing again before repair, retain a backup of
the old records, and update both source metadata and the matching research row.

| Resistance | LCSC code | MPN observed | Listing |
| --- | --- | --- | --- |
| 2 kΩ | C119330 | MF1/4W-2KΩ±1% T | [LCSC](https://www.lcsc.com/product-detail/C119330.html) |
| 4.7 kΩ | C119339 | MF1/4W-4.7KΩ±1% T | [LCSC](https://www.lcsc.com/product-detail/C119339.html) |
| 22 kΩ | C119354 | MF1/4W-22KΩ±1% T | [LCSC](https://www.lcsc.com/product-detail/C119354.html) |
| 3.3 kΩ | C119335 | MF1/4W-3.3KΩ±1% T | [LCSC](https://www.lcsc.com/product-detail/C119335.html) |
| 33 kΩ | C119358 | MF1/4W-33KΩ±1% T | [LCSC category listing](https://www.lcsc.com/brand/1203-1280.html) |
| 330 Ω | C119313 | MF1/4W-330Ω±1% T | [LCSC](https://www.lcsc.com/pt/product-detail/C119313.html) |
| 510 Ω | C119318 | MF1/4W-510Ω±1% T | [LCSC](https://www.lcsc.com/product-detail/Metal-Film-Resistor-TH_510R-5100-1_C119318.html) |
| 270 Ω | C119311 | MF1/4W-270Ω±1% T | [LCSC product image page](https://www.lcsc.com/product-image/C119311.html) |
| 180 kΩ | C119372 | MF1/4W-180KΩ±1% T | [LCSC](https://www.lcsc.com/product-detail/through-hole-resistors_cco-chian-chia-elec-mf1-4w-180k-1-t_C119372.html) |
| 390 kΩ | C119379 | MF1/4W-390KΩ±1% T | [LCSC](https://www.lcsc.com/product-detail/C119379.html) |
| 510 kΩ | C119382 | MF1/4W-510KΩ±1% T | [LCSC China](https://item.szlcsc.com/120651.html) |

Other truncated records need independent identity evidence. In particular, do
not substitute the similar 2.4 kΩ listing C119332 for catalogue code C119879.
At research time, all eleven corresponding source records had the matching
LCSC code, the incomplete primary and manufacturer-entry MPN `T`, and the
reviewed DIN0207 7.62 mm footprint. The eleven identities were subsequently
repaired, with their previous versions retained under
`tmp/display_render/cco_mf_01_previous/`; the immutable render evidence is
`DISPLAY_RENDER_CCO_MF_IDENTITIES_01.json`.

## Subsequent research

Three further 1% MF identities (15 Ω, 330 kΩ and 3.9 MΩ) were verified and
repaired; their immutable render evidence is
`DISPLAY_RENDER_CCO_MF_IDENTITIES_02.json` and backups are in
`tmp/display_render/cco_mf_02_previous/`.

Several other supplier codes are not eligible for the 1/4 W MF batch. Their
part types and ratings must be reconciled with the catalogue ID before using
them; do not guess a similar MPN or render them with this model merely because
the resistance matches:

| Catalogue resistance | LCSC code | Supplier listing observed |
| --- | --- | --- |
| 100 Ω | C216402 | [5 W cement resistor](https://www.lcsc.com/pl/product-detail/C216402.html?is_substitute=1&original_product_code=C1364594&original_unit_price=0.1416) |
| 150 kΩ | C121884 | [3 W metal oxide](https://www.lcsc.com/product-detail/C121884.html) |
| 47 Ω | C121800 | [3 W metal oxide](https://www.lcsc.com/product-detail/C121800.html) |
| 27 Ω | C119144 | [1/8 W metal film](https://www.oemstrade.com/search/19144) (supplier aggregator; recheck directly) |
| 2.4 kΩ | C119879 | [1/6 W carbon film](https://www.lcsc.com/product-detail/C119879.html) |
| 560 Ω | C129902 | [1/2 W small-body metal film](https://www.elektromall.com.tr/yurtdisi-urunler/through-hole-resistors-k72?sayfa=27) (secondary supplier; recheck directly) |
| 750 Ω | C129904 | [1/2 W small-body metal film](https://www.lcsc.com/it/product-detail/Through-Hole-Resistors_CCO-Chian-Chia-Elec-MF1-2WS-750-1-T_C129904.html) |
| 680 kΩ | C119242 | [1/8 W metal film](https://www.lcsc.com/product-detail/C119242.html) |
| 820 kΩ | C136537 | [2% glass-glaze part](https://www.lcsc.com/es/product-detail/through-hole-resistors_cco-chian-chia-elec-ri40-1-4w-820k-2-t_C136537.html) |
| 180 Ω | C120037 | [5% carbon film](https://www.lcsc.com/ko/product-detail/Through-Hole-Resistors_CCO-Chian-Chia-Elec-CF1-4W-180%CE%A9-5-T_C120037.html) |
| 750 kΩ | C120124 | [5% carbon film](https://item.szlcsc.com/121393.html) |

The 180 Ω and 750 kΩ parts may be candidates for a separately evidenced 5%
carbon-film rule. Some other identities remain unresolved.

The 180 Ω and 750 kΩ identities were subsequently verified as CCO CF1/4W 5%
carbon film parts and repaired; their evidence is pinned in
`DISPLAY_RENDER_CCO_CF_IDENTITIES_01.json`. The 120 kΩ identity was then
confirmed by the [direct LCSC listing](https://www.lcsc.com/product-detail/C120105.html)
and repaired separately; its evidence is pinned in
`DISPLAY_RENDER_CCO_CF_IDENTITIES_02.json`.
