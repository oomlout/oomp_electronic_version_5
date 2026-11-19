# onsemi TSSOP-20 display research

Reviewed 2026-11-19; candidates not staged. Individual manufacturer datasheets show the device code split over two lines for the TSSOP variant, plus variable factory/date fields. Preserve the actual line break rather than concatenating it, and review the final image at full size. Generic KiCad TSSOP model is 1.2 mm high and approximates the 4.4 × 6.5 mm case; catalogue height/footprint gaps and manufacturer package assignment must be disclosed.

- `74ACT244MTCX`: [onsemi datasheet](https://www.onsemi.com/pdf/datasheet/74act244-d.pdf) ordering table shows `ACT` / `244`; record dimensions 6.5 × 4.4 × 1.1 mm and TSSOP-20 footprint. Datasheet includes both case 948AQ and wide-body 948E drawings without unambiguous orderable-to-case mapping in the table; verify the exact package case before choosing a model or disclose the remaining uncertainty.
- `74VHCT244AMTCX`: [onsemi datasheet](https://www.onsemi.com/download/data-sheet/pdf/74vhct244a-d.pdf) table gives `VHCT` / `244A`; drawing 948AQ gives nominal body 6.5 × 4.4 mm, max 1.2 mm, 0.65 mm pitch. Catalogue omits height and footprint.
- `74LCX245MTCX`: [onsemi datasheet](https://www.onsemi.com/pdf/datasheet/74lcx245-d.pdf) lists `LCX 245` for TSSOP-20 and drawing 948AQ. Confirm the intended line break using the manufacturer marking diagram before committing a two-line interpretation. Catalogue omits height and footprint.

All markings exclude logo/date/lot and should explicitly disclose illustrative typography and placement. Do not infer markings for `74HCT373MTCX` from related devices; exact onsemi evidence remains to be found.
