# Infineon SLB9670 family QFN display research

Reviewed 2026-11-20. The catalogue ID implies Infineon SLB9670 but source
manufacturer and orderable fields are absent; family and manufacturer are
inferred, and TPM revision, temperature grade, firmware and exact orderable
are unspecified. Preserve source fields. The source records a 5 x 5 x 0.9 mm
body and 32 perimeter pads; its illustrative package_drawing has 0.625 mm
pitch and 2.1 x 2.1 mm central box, despite its note saying 0.5 mm pitch.

Infineon's [SLB9670 TPM 2.0 data sheet](https://www.infineon.com/assets/row/public/documents/30/49/infineon-slb-9670vq2.0-datasheet-en.pdf?fileId=5546d4626fc1ce0b016fc78270350cd6%2F)
identifies PG-VQFN-32-13 for VQ and XQ grades: 5 x 5 mm, 0.9 mm maximum
height and 0.5 mm terminal pitch; recommended PCB exposed pad is 3.6 x 3.6 mm.
The associated marking section lists SLB9670 plus VQ20 or XQ20 and variable
firmware/lot/date fields. Since this source does not identify a variant, use
only `SLB9670` as an illustrative family marking, omit all variant, firmware,
logo and production codes, and explicitly disclose font, layout and identity
uncertainty. The manufacturer document's drawings have not been visually
confirmed; the table/figure associations are from web extraction.

The previously inspected KiCad QFN-32 5 x 5 mm, 0.5 mm pitch model with
3.7 mm exposed pad is a possible display approximation: valid 5 x 5 x 0.85 mm
bounds, SHA-256 `7e77a52b3e261a45529e0df739376ea7cd79204fb1afad81332a50f4f1607000`,
body/metal/indicator colours. Its 3.7 mm pad differs from the 3.6 mm
recommended PCB land and is not proof of the package pad size. Explicitly
record the 2.1 mm source central box and 0.625 mm drawing pitch conflicts.
Review image and exact model before selection; display only, not a verified
footprint or mechanical model. No manufacturer PDF downloaded here.
