# TI CC1020RSSR VQFN-32 display research

Reviewed 2026-11-20. Source identifies exact Texas Instruments CC1020RSSR,
QFN-32-EP and no selected KiCad footprint, with placeholder 10 x 5 mm source
dimensions. [TI product information](https://www.ti.com/product/CC1020/part-details/CC1020RSSR)
confirms RSS VQFN-32, and the [TI package table](https://www.ti.com/packaging/tw/docs/searchtipackages.tsp?packageName=QFN)
gives 7 x 7 mm body, 0.65 mm pitch, 0.9 mm nominal height. TI's
[device marking listing](https://www.ti.com/quality-reliability-packaging-download/ko-kr/report?opn=CC1020RSSR)
gives `CC1020`; typography, position, orientation and variable codes remain
illustrative. Source generic dimensions conflict and must be disclosed.

TI's [CC1020 data sheet](https://www.ti.com/lit/ds/symlink/cc1020.pdf?ts=1793998106610)
shows exposed thermal pad 4.28 +/- 0.10 mm square with a chamfered pin-one
corner. Its figure associations are web-extracted and not visually confirmed.
The local 7 x 7 mm QFN-32 0.65 mm KiCad candidate is named with a 5.46 mm
pad, so it is not an exact thermal-pad match. Look for a closer source or
implement a reviewed display-only geometry adapter; disclose any approximation
and do not claim an exact mechanical model or footprint. No PDF downloaded.

Inspection corrected the filename-based estimate: the actual KiCad metal pad
is 4.70 mm square with a chamfer, not 5.46 mm. The inspected STEP has valid
7 x 7 x 0.87 mm overall bounds, SHA-256
`f8cb3647a783167910c468bc09d5de74223779876388b796a66718dc82b11a1a`.
The pad mesh has 13 isolated triangles, bounds -2.35 to +2.35 mm and z 0-0.02
mm, with no vertices shared with other metal. A guarded display-only adapter
can scale just that pad to 4.28 mm, preserving perimeter terminals; its chamfer
and underside need review and the adjustment must be disclosed.
