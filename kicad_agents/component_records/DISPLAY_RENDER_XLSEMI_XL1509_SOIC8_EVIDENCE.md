# XLSEMI XL1509-5.0E1 SOP-8 display evidence

Reviewed 2026-11-20. The source identifies XLSEMI XL1509-5.0E1, fixed 5 V,
SOP/SOIC-8, with a KiCad SOIC-8 3.9 x 4.9 mm footprint and no height. The
[XLSEMI datasheet](https://www.xlsemi.com/datasheet/XL1509-EN.pdf) lists this
exact orderable and `XL1509-5.0E1` as its marking ID. The package table gives
body 4.7–5.1 x 3.8–4.0 mm, lead span 5.8–6.2 mm, pitch 1.14–1.40 mm and
overall height 1.35–1.75 mm. Type, layout, font and variable production
markings remain illustrative even when using the listed ID. The manufacturer
datasheet has not been downloaded locally.

The specified KiCad SOIC-8 source needs its rendered orientation checked.
Catalogue 4.9 x 3.9 mm represents
body size rather than lead span. It is a display model, not a verified
mechanical model or footprint.

Inspection confirms `SOIC-8_3.9x4.9mm_P1.27mm.step` SHA-256
`07f46cff378d30e6c27dfd5a03092c795323f86d91c71fc7e743f4f418dc553a`,
valid bounds 6.0 x 4.9 x 1.75 mm and body, termination and pin-indicator
colours. These dimensions agree with the listed package ranges; inspect
marking and orientation in a preview before publishing.
