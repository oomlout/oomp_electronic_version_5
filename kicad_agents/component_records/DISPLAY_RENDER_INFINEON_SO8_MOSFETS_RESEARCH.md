# Infineon SO-8 MOSFET display research

Reviewed online 2026-11-21. None of these four source records has a local
datasheet PDF; no PDFs were downloaded or copied. The four catalogue records
have generic 10 x 5 mm dimensions and no selected KiCad footprint. Those
values remain unchanged and should not be mistaken for the package outline.

| Orderable | Display identifier | Manufacturer evidence |
| --- | --- | --- |
| IRF7413TRPBF | `IRF7413` | [IRF7413 family](https://www.infineon.com/part/IRF7413) identifies 30 V, 13 A and SO-8; [qualification report](https://www.infineon.com/assets/row/public/documents/24/316/infineon-irf7413-productqualificationreport-en.pdf) includes IRF7413TRPBF. |
| IRF7832TRPBF | `IRF7832` | [Infineon IRF7832](https://www.infineon.com/part/IRF7832) lists that exact orderable in SO-8. |
| IRF7404TRPBF | `IRF7404` | [Infineon IRF7404](https://www.infineon.com/part/IRF7404) lists that exact orderable in SO-8. |
| IRF7416TRPBF | `IRF7416` | [Infineon IRF7416](https://www.infineon.com/part/IRF7416) lists that exact orderable in SO-8. |

Infineon's online [IRF7404PbF-1 family sheet](https://www.infineon.com/assets/row/public/documents/non-assigned/49/irf7404pbf-1.pdf)
page 8 contains the SO-8 outline and an example marking for a different
device; the `-1` variant is a family-package example, not a claim that it is
the catalogue orderable. The KiCad SOIC-8 model has overall 6.0 x 4.9 x
1.75 mm bounds with four gullwing leads on each side and is used as a display
approximation. The rendered partial identifiers are **illustrative**, not
verified exact device markings; logos, typeface, placement and variable
production codes are unverified. No manufacturing geometry or PCB footprint
is implied.
