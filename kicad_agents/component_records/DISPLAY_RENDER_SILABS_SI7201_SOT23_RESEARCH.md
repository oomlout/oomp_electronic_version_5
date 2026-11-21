# Silicon Labs Si7201-B-06-IV SOT-23 display research

The catalogue ID names `Si7201-B-06-IV` and Silicon Labs, but the source has no populated manufacturer or manufacturer-part-number field. Identification is inferred from the ID, not a verified orderable. It selects the KiCad SOT-23 footprint and lists 2.9 × 2.6 mm without an explicit measurement reference.

Silicon Labs' [Si720x data sheet](https://www.silabs.com/documents/public/data-sheets/si720x-data-sheet.pdf) lists `Si7201-B-06-IV` in three-pin SOT-23. Its package drawing gives 2.90 mm nominal length, 2.75 mm nominal lead span, 1.60 mm body width, 0.95 mm pitch and 1.25 mm maximum height. The top-mark illustration specifies a manufacturing code, without publishing a fixed device marking for this orderable. `7201` is therefore an illustrative family identifier, not a claim about the actual code or production lot.

The previously inspected KiCad `Package_TO_SOT_SMD.3dshapes/SOT-23.step` has SHA-256 `dd5d1711204e1d8d26cd11490923bd84340820baa69538c385a4300ec2539bc0`, expected materials and 2.5 × 3.0 × 1.2 mm total bounds. Its height is within the manufacturer's limit, but its 2.5 mm lead span differs from the nominal 2.75 mm maker drawing. Disclose the model approximation, catalogue width, inferred identity and illustrative marking. This is not a verified mechanical model or footprint.
