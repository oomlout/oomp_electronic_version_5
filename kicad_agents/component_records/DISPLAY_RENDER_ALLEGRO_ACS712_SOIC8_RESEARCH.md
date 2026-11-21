# Allegro ACS712 SOIC-8 display research

Reviewed 2026-11-20. The catalogue ID implies Allegro ACS712 but the source
has no manufacturer or exact orderable and does not identify a current range.
Allegro's [ACS712 datasheet](https://www.allegromicro.com/-/media/files/datasheets/acs712-datasheet.pdf)
describes multiple ±5 A, ±20 A and ±30 A variants, so no specific range or
complete ordering suffix can be inferred. The display may use `ACS712` as an
illustrative family identifier only; maker and family are inferred, and exact
marking, voltage/current variant, font, orientation and production codes are
not verified. Preserve source data and do not suggest a specific sensor range.

The source specifies a 4.9 x 3.9 x 1.75 mm SOIC-8 body, 6 mm lead span and
1.27 mm pitch. The inspected KiCad `SOIC-8_3.9x4.9mm_P1.27mm.step` SHA-256
`07f46cff378d30e6c27dfd5a03092c795323f86d91c71fc7e743f4f418dc553a`
has valid 6.0 x 4.9 x 1.75 mm overall bounds, body, metal and pin-indicator
colours. Allegro's LC package drawing specifies the same nominal body and span
and a 1.75 mm height maximum. Preview marking, pin indicator and leads before
acceptance. This is not a verified footprint or mechanical model. No
manufacturer PDF was downloaded locally.
