# CJ78L05 and UTC 78L05G SOT-89 display research

Reviewed 2026-11-20. Candidates only; neither render has been staged or published.

## Jiangsu Changjing CJ78L05

The catalogue identifies Jiangsu Changjing Electronics Technology Co., Ltd.,
orderable CJ78L05, SOT-89-3, and catalogue dimensions 4.5 x 2.5 mm. The
[manufacturer-authored SOT-89-3L sheet, rev. 2.3](https://pdf.voron.ua/files/pdf/CJ/VoltageRegulators/CJ78L05_SOT89_3L.pdf)
identifies this device and assigns pins 1–3 to output, ground and input. Its
text extraction describes a two-line `CJ` / `78L05` device marking. A dot can
identify green moulding compound and should not automatically be presented as
a pin-one dot. The marking illustration and dimensional drawing have not yet
been visually verified: review them before selecting exact layout, orientation,
dimensions or a representation of the dot. Do not treat the separate SOT-23
sheet as evidence for this package.

The readable dimension table on page 4 gives body length 4.4–4.6 mm, body
width 2.3–2.6 mm, overall span 3.94–4.25 mm, thickness 1.4–1.6 mm and
1.5 mm typical lead pitch. The inspected KiCad source measures 4.5 mm along
the body, 2.5 mm body width, 4.0 mm span and 1.52 mm height, within those
listed ranges. These are table comparisons, not verification of pinout or
mechanical fit; the drawing still needs visual review.

The inspected KiCad SOT-89-3 source used in the Holtek pilot is uncoloured and
requires the hash- and geometry-checked material adapter. The pilot final is
still in progress; first validate that adapter and confirm that package geometry
is suitable for this manufacturer's drawing. Variable lot details, typeface,
placement and any abbreviated one-line display must be disclosed as
illustrative. Do not claim the seller-hosted manufacturer PDF has been saved
locally; this research used browser-readable content only.

## UTC 78L05G-AB3-R

The [UTC 78LXX manufacturer-authored sheet](https://datasheet.lcsc.com/datasheet/pdf/24955d8a86386c685cabea257ea319d6.pdf?productCode=C380213)
maps AB3 to SOT-89 and the unsuffixed pin assignment to output, ground, input;
the separate `-C-` variant has a different pin assignment. Its extracted
marking diagram describes a `78LXX` voltage-code line and variable date and pin
codes. Verify the exact source record and visually inspect the SOT-89 marking
and package drawing before using `78L05` or representing its pin code. Do not
assume UTC and JSCJ markings or lead orientation are interchangeable. This
document was not downloaded into the repository.
