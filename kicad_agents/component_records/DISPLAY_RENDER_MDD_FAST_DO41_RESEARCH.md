# MDD fast-recovery DO-41 display evidence

The local manufacturer PDFs were visually reviewed on 2026-11-21. Poppler reported missing display fonts, but the package drawings, numeric dimensions and marking tables on the inspected first pages were legible.

* `FR104/datasheet.pdf`, SHA-256 `ee69054205d45685a9b9c0aff48ba221d23499be8c81ff60bc02894907a783c4`, covers FR101–FR107 and lists the MDD logo plus each full identifier. This supports FR104 and FR107; the FR107 entry has no local PDF.
* `HER107/datasheet.pdf`, SHA-256 `a0dbd27d727387ce3b9fed56bef875c70675d97ad63b835aa27103a3c8027b8a`, covers HER101–HER108 and lists the MDD logo plus identifiers, including HER107.
* `SF18/datasheet.pdf`, SHA-256 `837813e9b7d38bfd0343c3f543ab1de74d4499525d588bcfe9e3a5cf610b8991`, covers SF11–SF18 and lists the MDD logo plus identifiers, including SF18.

All three drawings show DO-41 bodies 4.2–5.2 mm long, 2.0–2.7 mm in diameter, with a polarity band and straight leads at least 25.4 mm long. FR and HER list lead diameters 0.70–0.86 mm; SF18 lists 0.53–0.64 mm. The previously inspected KiCad `D_DO-41_SOD81_P10.16mm_Horizontal.step`, SHA-256 `c3e23d4b276811b74eecb329bd4480209ad3dbc8cf6e6e3f2a5b542c5ca343c1`, has a 5.2 x 2.7 mm body, approximately 0.80 mm diameter bent leads and a stripe near pin 1. Thus its leads fit the FR/HER diameter range but exceed the SF18 drawing maximum by 0.16 mm. Its bent-lead geometry and 10.16 mm pitch illustrate a fitted component rather than the straight, long leads in the drawings.

FR104, FR107 and HER107 source records have no selected KiCad footprint and use placeholder 10 x 5 mm dimensions; SF18 selects that DO-41 footprint and records a 5.2 x 2.7 mm body. Any display must disclose the placeholders and missing selected footprints where applicable, the bent-lead difference, the SF18 lead diameter mismatch and omitted MDD logo. Identifiers, typeface, stripe width and finish are partial illustrative representations, not exact production artwork. Do not alter the catalogue's KiCad selection or source dimensions during display generation.
