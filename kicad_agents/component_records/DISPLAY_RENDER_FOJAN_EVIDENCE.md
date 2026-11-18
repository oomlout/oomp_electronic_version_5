# FOJAN FRC chip resistor display evidence

Reviewed online 2026-11-17. These are links to the manufacturer's FRC series
documents hosted by LCSC; this record does not claim that either PDF has been
downloaded locally. The browser-control tool timed out during local capture.

- [FOJAN FRC general thick-film product specification, FJ-JS-3001 V2.0, 2025-09-24](https://datasheet.lcsc.com/lcsc/2111020930_FOJAN-FRC0603F3603TS_C2907029.pdf): part-number explanation, case dimensions, body markings, E96 values and multiplier table. The body-marking section says 0201 and 0402 parts have no value code, and 0603 1% E96 parts use the documented three-character code. The standard 1% mark for larger packages uses three significant digits and a multiplier digit. The document also shows decimal-position markings for values below 100 ohms; review those explicitly instead of treating a procurement suffix as printed text.
- [FOJAN FRC catalogue marking table](https://atta.szlcsc.com/upload/public/pdf/source/20220511/8BC075D05D09E77BE20A0D46B10BFB65.pdf), printed pages 59–60: describes 0603 1% E24 values outside E96 with an underline under the **middle character**. Do not use the full-width underline from the UNI-ROYAL example for FOJAN. The web-extracted older table appears to say code 36 corresponds to 223, while the newer specification says 232. This may be an extraction or document error; use the newer source and flag the discrepancy rather than silently treating both as identical.

The generic KiCad package is a nominal display model, not a manufacturer CAD
model. Body colour, ink, typeface and positioning are illustrative. Exact MPN,
size, value, tolerance, manufacturer and marking rule must all be verified for
each candidate. Do not claim that a supplier-specific appearance represents
all alternatives listed under a generic catalogue component.
