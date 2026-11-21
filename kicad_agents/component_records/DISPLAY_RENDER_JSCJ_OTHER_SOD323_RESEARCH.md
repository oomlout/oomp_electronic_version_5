# JSCJ SOD-323 family codes and local source limitations

JSCJ's online [MMSZ5221BS–MMSZ5259BS family PDF](https://www.jscj-elec.com/uploads/20221026/b50c9149a4b6bf65fe2ddd42b92d948b.pdf), page 2, lists `MMSZ5248BS` as `J3` and `MMSZ5250BS` as `J5`. The local MMSZ5248BS PDF SHA-256 `a39a67bd216e2bb869ae7fb71ee320adf8a0feec7421d7cb9ff0045c8981ed3a` independently contains the same table but identifies a different manufacturer, JCST. MMSZ5250BS has no local PDF.

JSCJ's online [1SS404 PDF](https://www.jscj-elec.com/gallery/file/1SS404%20SOD-323.pdf) identifies `S51` as the marking. The locally stored 1SS404 PDF SHA-256 `edd90e8b29235843ad0ef3b62ee229106a5090fd516b1e568bdc495e6f8f5ea7` also says `S51`, but identifies JCST rather than JSCJ. No PDF was downloaded during this review.

All three source records select the KiCad `Diode_SMD:D_SOD-323` footprint and have apparent placeholder 10 x 5 mm dimensions. KiCad `D_SOD-323.step` SHA-256 `cd8619b2119cd95683a2c5e660ab4f2d4db674f696cd6f9e9756f221171a214d` has overall bounds 2.50 x 1.25 x 1.11 mm; its cathode stripe is on negative X, corresponding to pin 1 on that footprint. Dimensions have not been independently checked against the respective manufacturer drawings. Typeface, finish and placement are illustrative; no manufacturing use is implied.
