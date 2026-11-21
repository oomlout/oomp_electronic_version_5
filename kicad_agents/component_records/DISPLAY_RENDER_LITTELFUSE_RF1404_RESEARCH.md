# Littelfuse RF1404-000 display research

The source record identifies Littelfuse RF1404-000, a 750 mA resettable 1812
part, with no local PDF. Littelfuse's [certificate](https://www.littelfuse.com/assetdocs/cocrohs10rf1404000-minismdc075f2?assetguid=2682334f-288b-4114-bc8f-e4ba38ade371),
viewed online, associates RF1404-000 with MINISMDC075F-2. Its
[miniSMDC series datasheet](https://www.littelfuse.com/assetdocs/littelfuse_ptc_minismdc_datasheet?assetguid=3ed735aa-64ed-43a6-bc20-610590bc99c6)
was also viewed online; no PDF was downloaded.

The already present local Tyco family PDF from
`parts_source/electronic_fuse_1812_resettable_littelfuse_minismdc020f_2/datasheet.pdf`
(SHA-256 `7b7cb3a9edb8103455448bae8a77bc64c72082e6b90006a8698635a2ebeaac2c`)
was visually reviewed: page 7 shows the concave outline, page 9 lists
miniSMDC075F at 4.37–4.73 × 3.07–3.41 × 0.38–0.62 mm, and page 15 lists its
part marking as `7`. The source's 2.4 mm height conflicts with that range and
the distributor field says 5.4 mm length, above the drawing maximum. Preserve
both source fields and disclose the discrepancy.

The existing display-only concave model can be scaled from 0.76 to 0.50 mm
height, within the manufacturer range. The code `7` is supported; the logo is
omitted and its positioning, typography, body shade, exact notch shape and
terminal finish are illustrative. This is not a manufacturer model or footprint.
