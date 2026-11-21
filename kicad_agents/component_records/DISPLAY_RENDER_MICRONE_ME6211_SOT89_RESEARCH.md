# MicrOne ME6211A33PG-N SOT-89 display research

Reviewed 2026-11-20. The source specifies part number ME6211A33PG-N and
4.5 x 2.5 mm dimensions, but does not provide a manufacturer name; MicrOne
is inferred from the catalogue ID and corroborated by the manufacturer sheets.
No KiCad footprint is selected. The linked local `datasheet.pdf` SHA-256
`a7f450566318afe8ad0a90a04ea17a9e1f866f262ba484f01bbda97f0f66f5b7`
is a 17-page MicrOne ME6118 sheet, NOT the ME6211 data sheet; do not use it
as evidence for this part. Preserve the source record and flag this mismatch.

The manufacturer-authored [ME6211 data sheet](https://www.huazhoucn.com/upFiles/common/2022/12/ME6211%20Series_E30.0.pdf)
lists ME6211A33PG-N as 3.3 V SOT-89-3. A [manufacturer-authored older sheet](https://www.adrirobot.it/wp-content/uploads/2023/10/ME6211-High_Speed_LDO_Regulators.pdf)
indicates `6211A` for P and `6211A1` for P1; this P-orderable implies the
former. The full image, other voltage/manufacturing marks, font and layout
have not been independently visually confirmed, so use `6211A` only as an
illustrative partial marking and disclose all omissions. The maker sheet's
P pin table (1 ground, 2 input, 3 output) matches source. Source dimensions
are consistent with generic SOT-89 but the manufacturer's dimensional drawing
has not yet been visually verified; do not claim exact model equivalence.

The inspected KiCad SOT-89-3 source SHA-256
`844c0bb504d0c383535d9845c6376fe7a4053241a2ede8d8ef694df3fcfc37c8`
has 4.0 x 4.5 x 1.52 mm overall bounds and no face colours. A reviewed
five-solid adapter supplies the body and metal regions. Any candidate needs a
per-part bound adapter, preview and explicit display-only/model limitations.
No manufacturer PDF was downloaded during this research.
