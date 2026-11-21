# Infineon IRFP4468 and IRFP4568 TO-247 display research

The catalogue identifies the distinct Infineon IRFP4468PBF (100 V, 290 A
silicon-limited; the datasheet also states a lower package current limit) and
IRFP4568PBF (150 V, 171 A silicon-limited). Their existing local International
Rectifier PDF hashes are respectively
`f1ec6fda95d9a163f8cbfe12335dbeb0a9586d2825f67e790aa91c0b38c0d0ef` and
`fc390da2bcba48050d046ce430413abb0567e53b28d86ac8959d2b025b639e4c`.
Each PDF's page 1 identifies the device; each page 8 drawing was visually
reviewed. Both specify TO-247AC with 14.20–16.10 mm lead length, body height
19.71–20.70 mm, and width 15.29–15.87 mm. Their example top markings depict an
unrelated IRFPE30, so the exact markings are not established.

The reviewed KiCad-derived TO-247 model has a display-only 15.15 mm lead
adjustment, within each drawing's lead range. Its 20.95 mm body height and
15.9 mm width slightly exceed the stated maxima. The shape, metal finish and
marking are approximations, not a verified manufacturing model or footprint.
`IRFP4468` and `IRFP4568` may be shown as illustrative identifiers only; the
exact top text, logo, typeface and variable lot/date details are unverified.
