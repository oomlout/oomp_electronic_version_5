# Ckmtw B-2100S17P-A110 header display research

The existing generated copy `parts/electronic_connector_header_2_54_mm_pitch_through_hole_17_pin/data/datasheet.pdf`,
SHA-256 `e942aeb6ead33cfe1b159125f66b75ddf7c706f92a218971a789ec760a109b11`,
pages 1–2 was visually reviewed. Cankemeng's family drawing explicitly lists
B-2100S17P-A110 as a 1×17 straight through-hole header: 2.54 mm pitch,
2.5 mm body, 6 mm mating pins, 3 mm tails, and gold-over-nickel brass. The
exact JLCPCB listing https://jlcpcb.com/partdetail/51950723-B_2100S17PA110/C49423291
contains an inconsistent SMD right-angle package label; the manufacturer's
family drawing resolves the illustrated orientation.

KiCad `PinHeader_1x17_P2.54mm_Vertical.step` SHA-256
`e3562046dcf1df6f05b4b7b8f7d54defeab5ce5ba8f47ac199eb1945b1f85df6`
measures 2.54 × 43.18 × 11.54 mm; source width is 2.48 mm. Exact finish
shade is illustrative. The source local PDF is absent but the generated
copy exists; legacy model and render are present. This is display geometry,
not manufacturer CAD or a footprint. No PDF was downloaded.
