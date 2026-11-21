# Diodes AP7361C 3.3 V DFN-8 display research

Reviewed 2026-11-20. The source ID implies Diodes AP7361C at 3.3 V in DFN-8,
but manufacturer and exact orderable fields are missing. Treat the maker and
device identity as inferred, not a confirmed full purchasing number.

The [Diodes AP7361C datasheet](https://www.diodes.com/datasheet/download/AP7361C.pdf)
specifies U-DFN3030-8 type E, body 2.95–3.05 x 2.95–3.05 mm, height
0.57–0.63 mm, 0.65 mm pitch, and a 1.5 x 2.25 mm nominal exposed pad.
It lists fixed marking `SZ` for the 3.3 V DFN variant, followed by variable
year/week/internal codes; font, placement and omitted variable codes must be
identified as illustrative. The inspected KiCad
`DFN-8-1EP_3x3mm_P0.65mm_EP1.5x2.25mm.step` SHA-256
`65626b93d9b55c6bfae7e3fdafcfd9dc36fe0121778aa04d8da3a20c7d1f041e`
has valid 3.0 x 2.98 x 0.6 mm bounds and reviewed body, metal and pin-dot
colours.

The local catalogue lists height 0.8 mm, specifies a 2 x 2 mm / 0.5 mm pitch
footprint, and depicts two contacts on each of four sides. That conflicts with
the datasheet's 3 x 3 mm package and two rows of four contacts. Preserve and
explicitly disclose the discrepancy; the display is not a verified footprint
or a silent correction of source. Verify the pin-one dot and eight edge
contacts in a preview. No new manufacturer PDF has been saved locally.
