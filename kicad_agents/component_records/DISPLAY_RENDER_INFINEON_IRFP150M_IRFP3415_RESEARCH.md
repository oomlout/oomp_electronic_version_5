# Infineon IRFP150M and IRFP3415 TO-247 display research

Both local International Rectifier PDFs were reviewed at page 8. They describe
different TO-247AC lead lengths, despite the catalogue using the same footprint:

- IRFP150MPBF (100 V, 42 A): PDF SHA-256
  `78fc2de32a1ce05decb1eeb0319634a7ec60113d1b8ddcaa8eecc0880cbd580f`.
  The drawing specifies L = 19.80–20.32 mm, body height 20.80–21.10 mm and
  width 15.75–16.13 mm. The original KiCad TO-247 model's 20.15 mm lead length
  and 20.95 x 15.9 mm body fit these ranges. Do not shorten its leads to the
  15.15 mm used for some other devices.
- IRFP3415PBF (150 V, 43 A): PDF SHA-256
  `0a43a187b417beb46954e1791023c5a0df5160ae7d01d647d050de20098a9829`.
  Its drawing specifies L = 14.20–16.10 mm, and body 19.71–20.70 mm by
  15.29–15.87 mm. The separately reviewed 15.15 mm lead adjustment fits its
  range, although that model's 20.95 x 15.9 mm body slightly exceeds maxima.

The marking examples show a different device, IRFPE30. `IRFP150M` and
`IRFP3415` are illustrative partial identifiers, not verified package-top
markings; exact typeface, layout, logo and variable lot/date codes are unknown.
Neither display model is verified manufacturing CAD or a footprint.
