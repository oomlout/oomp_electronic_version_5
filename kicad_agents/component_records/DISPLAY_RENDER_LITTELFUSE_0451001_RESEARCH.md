# Littelfuse 0451001.MRL display research

The source record identifies Littelfuse 0451001.MRL (1 A, 2410). Its
`dimensions_mm` value of 10 × 5 mm conflicts with both the distributor fields
in the record (6.1 × 2.5 mm) and the manufacturer drawing. It has no selected
KiCad footprint. Preserve those source fields; do not treat the illustration as
a footprint or manufacturing model.

The [Littelfuse 451/453 series datasheet](https://www.littelfuse.com/assetdocs/fuse-451-and-453-datasheet?assetguid=533cd5cc-956c-4243-867f-6ab5a62f6ba1),
revision 12/01/25, was viewed online, not downloaded. Page 2 maps the 001
ampere code to 1 A. Page 4 describes a ceramic body, brand and ampere rating
marking, and gold-plated caps for the L suffix. The drawing gives nominal
6.10 × 2.69 × 2.69 mm and 1.45 mm cap length. The family drawing depicts a
7 A example; it does not establish the exact typography, layout, or ink of the
1 A example. The proposed `LF 1A` marking, cap finish, body shade, and small
edge rounding are therefore illustrative, not a verified exact appearance.

No suitable exact 2410 model was identified in the installed KiCad fuse
library. A procedural display-only model may use the manufacturer nominal
dimensions and be rendered without exporting CAD files.
