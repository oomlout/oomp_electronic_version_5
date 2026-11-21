# TO-251 / I-PAK display model investigation

Six remaining catalogue MOSFET records specify `Package_TO_SOT_THT:TO-251-3_Vertical`. Their local family drawings were visually reviewed on page 9:

| Catalogue orderable | Local PDF SHA-256 | Drawing |
| --- | --- | --- |
| Infineon IRFU3910PBF | `2ab4bf8282d54922c1cb81bea73e53183abef4a44a8e305e8c1f291c3c9ee3f7` | International Rectifier IRFR/U3910PbF TO-251AA. |
| Infineon IRFU120NPBF | `83dc4858004a978949d3e5581a73af82953b8b90c6549b72f88c278bbf8506d9` | International Rectifier IRFR/U120NPbF TO-251AA. [Infineon product page](https://www.infineon.com/part/IRFU120N) confirms the exact orderable. |
| Infineon IRFU220NPBF | `7b8b6e32281bb5b9d3dfde103740646d3ca80293b6efbe9e0f637b920e5af154` | International Rectifier IRFR/U220NPbF TO-251AA. [Infineon product page](https://www.infineon.com/part/IRFU220N) confirms the exact orderable. |
| Infineon IRLU024NPBF | `ff52b6382c5eabdd1e267f1d4cbdf0fbbd81d4a4854a20efdd77225fdae3ed4a` | International Rectifier IRLR/U024NPbF TO-251AA. |
| Infineon IRFU5410PBF | `89490495713f68cfef9d64778bfcba51014763eca5762c87f3edca55c5097228` | International Rectifier IRFR/U5410PbF TO-251AA. |
| Vishay IRFU9024PBF | `82e0db9093d479da7bb32be0903e9a4aa356705fbfb07abd1d8b3467fef72bb0` | Vishay TO-251AA high-voltage outline 91362. |

These drawings show **three full through-hole leads**, not the shortened centre lead of the D2PAK surface-mount models. Most International Rectifier marking examples show a different IRFU120 device and therefore do not independently verify each represented part's physical marking. Exact manufacturer codes, typography and production details require review for each record. Do not assert PbF suffix or package identity solely from similar device names.

The local KiCad `Package_TO_SOT_THT.3dshapes/TO-251-3_Vertical.step` has SHA-256 `7bb694d087837f077086c278225d603d812ff6a7a8af1db64601db91de627c55`, is one fused solid and has approximately 6.575 × 2.31 × 16.26 mm overall bounds. Its STEP faces carry 61 metal and 8 coating colour assignments, independently read by the standard material importer. The measured body spans about 6.575 × 2.31 × 6.1 mm, and its approximately 9.56 mm lead projection fits the International Rectifier drawing's 8.89–9.60 mm range. The face-up orientation and final appearance still require preview review. No PDF was downloaded for this investigation.
