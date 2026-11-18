# 2512 resistor value conflicts and reconciliation

The original supplier selections did not match the catalogue values. Do not
use the former selections for these IDs:

- `electronic_resistor_2512_13_3_ohm` selects Stackpole RMEF2512FT133R,
  which is **133 Ω**, not 13.3 Ω. [Mouser listing](https://br.mouser.com/ProductDetail/SEI-Stackpole/RMEF2512FT133R?qs=IPgv5n7u5QbKZgu9nqSX8Q%3D%3D)
  and the source distributor description agree. Find a verified 13.3 Ω
  selected part rather than silently changing the catalogue value.
- `electronic_resistor_2512_0_2_ohm` selects FH RPL-12L2R00FT, which is
  **2 Ω**, not 0.2 Ω. [LCSC C5119990](https://www.lcsc.com/product-detail/C5119990.html)
  and the source distributor description agree. Find a verified 0.2 Ω part
  or independently reconcile the catalogue value.

Preserve original records and cross-references during reconciliation. Neither item was rendered under the conflicting selection.

## Matching-value candidates for review

- 13.3 Ω: [Yageo RC2512FK-0713R3L](https://www.digikey.ca/en/products/detail/yageo/RC2512FK-0713R3L/5921856), 2512, 1%, 1 W; verify the manufacturer series marking and catalogue sourcing before changing the selected part.
- 0.2 Ω: [Yageo PT2512FK-7W0R2L](https://www.lcsc.com/de/product-detail/C309535.html), 2512, 1%, 2 W; verify its current-sense construction, dimensions, ratings and manufacturer marking before selecting it. A [1 W RL2512FK-070R2L](https://www.lcsc.com/pt/product-detail/C309648.html) also exists, but its lower power and other ratings require separate review.

Candidates match the nominal values, but have not been verified as fully
interchangeable with any original intended parts. The current source records
have not been changed.

## Resolution: 0.2 Ω (2026-11-18)

Selected Yageo PT2512FK-7W0R2L / C309535: manufacturer-verified 0.2 Ω,
1%, 2 W current-sense part. Source and generated records now point to this
part; the original FH 2 Ω record is retained in
`tmp/display_render/2512_0_2_selection_previous/` and in source research notes.
The differing current-sense characteristics require application review.
The 13.3 Ω conflict still requires reconciliation.
