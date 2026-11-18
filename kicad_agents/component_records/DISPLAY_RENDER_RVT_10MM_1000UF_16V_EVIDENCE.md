# Honor RVT 10 mm 1000 µF 16 V display pilot

Reviewed 2026-11-18. [LCSC C3359](https://www.lcsc.com/product-detail/Aluminum-Electrolytic-Capacitors-SMD_1000uF-16V_C3359.html)
identifies Honor RVT1C102M1010 as polarized 1000 µF, 16 V, 10 mm diameter
and 10.2 mm seated height. Its existing local RVT series PDF is
`parts_source/electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_1000_micro_farad_16_volt/datasheet.pdf`,
SHA-256 `285ae57abc097a56fae89388feef643b79f8d7c2901d6457de4bc00a5f91ce1b`.
Its first two pages were visually reviewed: they show a metal can with a dark
top sector and dimension/polarity drawings; PDF font substitution occurred.

The [manufacturer RVT series specification for another value](https://xonstorage.z8.web.core.windows.net/pdf/honor_rvt1e470m0505_xonjuly20_20_link.pdf),
pages 4–6, calls for value, voltage and negative polarity marking and lists
the 10 × 10.2 mm case. `1000` and `16V` on two lines are illustrative: the
exact ink, maker logo and date are unverified and must not be invented.

The KiCad `CP_Elec_10x10.step` has a dark top sector on positive X, same
side as pad 2 of its footprint; the KiCad polarized symbol marks pin 1
positive, making pin 2 negative. The model is scaled vertically from 10.0
to 10.2 mm including its base. Actual finish, sector, text layout and
proportions may differ. No manufacturer PDF was downloaded.
