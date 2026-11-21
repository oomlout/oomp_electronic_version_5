# Diodes AP2112K 3.3 V SOT-23-5 family research

The catalogue ID indicates Diodes AP2112K 3.3 V, but manufacturer and exact orderable fields are absent. It selects `Package_TO_SOT_SMD:SOT-23-5` and gives a 2.9 × 1.6 × 1.1 mm body with 0.95 mm pitch. Its separate package drawing says 4.2 × 3.2 mm overall; its `ic_dimensions_mm` instead gives 2.65–2.95 mm overall width.

The [Diodes AP2112 data sheet](https://www.diodes.com/datasheet/download/AP2112.pdf) lists the 3.3 V SOT25 orderable AP2112K-3.3TRG1 and its device marking `G3P`. This is a representative family variant, not proof that the generic catalogue entry specifies that exact orderable. Logo, typeface, placement and variable lot/date information are unverified.

The inspected KiCad `Package_TO_SOT_SMD.3dshapes/SOT-23-5.step` has SHA-256 `720a6eab0024069bbee68e7cb4c3ff1149468a34611225cdc852662c5d0ec2b7`, expected body/termination/pin-one colours, and total bounds 2.8 × 2.9 × 1.55 mm. The manufacturer's data sheet gives SOT25 1.0–1.3 mm overall height, nominal 1.1 mm, and 0.95 mm pitch; the model is too tall and a display may scale it vertically to 1.1 mm. Disclose that approximation, the source drawing discrepancy, inferred manufacturer and representative marking. This is not a verified footprint or mechanical model.
