# Infineon SLB9665 family QFN display research

Reviewed 2026-11-20. The source ID implies Infineon SLB9665 QFN, but contains
no manufacturer or exact orderable. Manufacturer and family are inferred; exact
grade, firmware and ordering suffix remain unspecified. Infineon's
[SLB9665 TPM 2.0 data sheet](https://www.infineon.com/assets/row/public/documents/30/49/infineon-data-sheet-slb9665-2.0-rev1.2-datasheet-en.pdf)
identifies VQ/XQ variants in PG-VQFN-32-13, alongside other TSSOP variants;
the catalogue explicitly specifies QFN, not a specific VQ/XQ variant. Its
marking section gives `SLB9665` plus VQ20/XQ20 and variable firmware, lot and
date. Use only the family text as an illustrative marking, omitting variant,
logo and production codes; font, layout and orientation are illustrative.

Manufacturer PG-VQFN-32-13 package data describe 5 x 5 mm body, 0.9 mm
maximum height, 32 contacts and 0.5 mm pitch; the recommended PCB centre land
is 3.6 x 3.6 mm. Source drawing uses 0.625 mm pitch and 2.1 mm centre box,
while its own note says 0.5 mm. Explicitly disclose this discrepancy. The
manufacturer drawing associations are web-extracted and not visually confirmed.

Previously inspected KiCad QFN-32 5 x 5 mm 0.5 mm pitch model with 3.7 mm
exposed pad, SHA-256 `7e77a52b3e261a45529e0df739376ea7cd79204fb1afad81332a50f4f1607000`,
is a possible display approximation, bounds 5 x 5 x 0.85 mm; 3.7 mm model
pad differs from 3.6 mm recommended PCB land, which is not necessarily the
physical pad size. Review preview and final. This is display-only, not a
verified footprint or mechanical model. No PDF downloaded here.
