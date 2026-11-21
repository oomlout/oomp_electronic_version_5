# Littelfuse miniSMDC020F-2 display research

The source record identifies Littelfuse MINISMDC020F-2, 1812, and includes
`datasheet.pdf`. An independent manufacturer [part specification](https://www.littelfuse.com/assetdocs/ptc-minismdc020f-2-product-specification?assetguid=7dcbb1e5-48fd-4f56-9d10-af5eab9deb8a)
was viewed online, not downloaded. Its page 1 gives 4.37–4.73 mm length,
3.07–3.41 mm width and 0.635–0.89 mm thickness and states the terminations
are tin plated. Its drawing shows a notched outline and a manufacturer mark.
The source `dimensions_mm.height` is 2.4 mm, substantially larger than the
manufacturer's 0.89 mm maximum; preserve the source but disclose the conflict.

The manufacturer [miniSMDC family datasheet](https://www.littelfuse.com/assetdocs/littelfuse_ptc_minismdc_datasheet?assetguid=3ed735aa-64ed-43a6-bc20-610590bc99c6),
also viewed online, maps miniSMDC020F to part marking `2`. Use that code only
for this exact identity. The existing local Tyco Electronics family PDF was
also visually reviewed: PDF page 7 figure S2 shows the concave ends, page 9
confirms the size ranges, and page 15 maps the same part to `2`. Its SHA-256 is
`7b7cb3a9edb8103455448bae8a77bc64c72082e6b90006a8698635a2ebeaac2c`.
The detailed manufacturer logo, ink, body colour and
small geometric features require further visual confirmation; if approximated,
state that explicitly. No KiCad 1812 fuse model was identified in the installed
Fuse.3dshapes folder, so an appropriately labelled procedural display model may
be necessary. These drawings are not authorization to use display geometry as
manufacturing CAD or a footprint.
