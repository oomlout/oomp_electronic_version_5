# Aluminium electrolytic display research

2026-11-18: The source inventory includes surface-mount Honor RVT aluminium
electrolytics, including 8 × 10.2 mm and 10 × 10.2 mm sizes. Installed KiCad
has `Capacitor_SMD.3dshapes/C_Elec_8x10.2.step`, SHA-256
`8f86de3213fc1a230094af15b95b24ddd629f28ed265f97c9d2b9c391e729b2a`.
It has not yet been geometrically or visually reviewed against the part drawing.

The existing local series PDF attached to
`parts_source/electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_1000_micro_farad_16_volt/datasheet.pdf`
has SHA-256 `285ae57abc097a56fae89388feef643b79f8d7c2901d6457de4bc00a5f91ce1b`.
Page 1 shows illustrative metal cans with black top sectors and markings; page 2
shows case dimensions and identifies positive/negative terminals. It does not
establish the exact printed text, ink layout or polarity sector orientation for
a specific purchased component. Poppler reported missing font substitutions;
the schematic and product illustration were legible but text needs caution.

The 8 × 10.2 mm 100 µF 50 V source record refers to a PDF which is not present
at its stated local path. Do not claim that file exists or silently download it.
Before any render: verify exact part/source and local provenance, inspect the
STEP model's terminal and face orientations, establish the negative sector
from suitable evidence, and implement top-face value/voltage text with clear
approximation disclosures. Do not reuse the positive-anode tantalum policy.
No aluminium render or recipe has been produced from this research.
