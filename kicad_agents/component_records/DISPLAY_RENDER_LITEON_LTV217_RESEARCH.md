# Lite-On LTV-217-B-G SOP-4 display research

Reviewed 2026-11-20. The catalogue source identifies Lite-On LTV-217-B-G
and JLC/LCSC C115450, with generic 10 x 5 mm dimensions and no KiCad
footprint selected. These generic dimensions are not the package drawing.

The manufacturer-authored [LTV-217-G series drawing, 2012, page 2](https://file.thegioiic.com/upload/documents/1734592019_LTV-217-B-G_.pdf)
shows L217, an optional rank mark, three-digit date code, halogen-free mark,
and an optional VDE mark only for the V ordering option. The B rank is listed
on page 6, but the rank marking may be omitted. Typeface, date, manufacturing
marks and any placement not verified against the drawing must be described as
illustrative. Pin 1 is the anode.

The web extraction describes a 4.4 +/- 0.2 mm body dimension, 2.6 +/- 0.3 mm
body dimension, 2.0 +/- 0.2 mm height, 1.27 +/- 0.25 mm pitch, and 7.0 mm
span +0.2/-0.7 mm; the extracted views also mention 5.3 +/- 0.3 mm. The PDF
image could not be displayed by the available web screenshot, so these
measurements and their view associations have NOT been independently visually
confirmed. Treat geometry as approximate until that drawing is inspected.
A [KiCad symbol proposal](https://gitlab.com/kicad/libraries/kicad-symbols/-/merge_requests/5464)
references a SOP-4 4.4 x 2.6 mm footprint, which is corroboration of the
nominal body size, not proof of a suitable local 3D model. Find and inspect a
model, its materials and bounds before staging. Preserve any provenance and
explicitly disclose the generic source dimensions and drawing limitation.
No manufacturer PDF was downloaded locally for this research.

A later manufacturer-authored [LTV-2x7 data sheet, page 2](https://s3.amazonaws.com/snapeda/datasheet/LTV-217-A-V-G_Lite-On_Electronics.pdf)
independently corroborates the text-extracted nominal dimensions and `L217`
marking, and identifies the circular marking as the halogen-free option. The
web screenshot attempt timed out, so the two extracted summaries do not replace
an actual visual review. In particular, do not equate the halogen-option dot
with a generic KiCad pin-one dot without explicit disclosure.

The installed KiCad `Package_SO.3dshapes/SOP-4_4.4x2.6mm_P1.27mm.step`
was inspected: valid single root, SHA-256
`cb2b0da8eb9fdb76dbba2de2ff1cc50164623079ee56b75b8eef2c751591bff3`,
7.0 x 2.6 x 2.1 mm overall bounds and separate body, metallic lead and
indicator colours. The nominal body, pitch and span fit the extracted drawing;
its indicator is a generic KiCad feature and not verified as the maker's
halogen-option mark. Review the marked preview and full render before use.
