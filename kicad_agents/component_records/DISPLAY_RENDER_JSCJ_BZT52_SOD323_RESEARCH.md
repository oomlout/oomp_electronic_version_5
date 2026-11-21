# JSCJ BZT52 SOD-323 zener illustrations

JSCJ's online [BZT52C2V4S–BZT52C43S family datasheet](https://www.jscj-elec.com/gallery/file/BZT52C2V4S-BZT52C43SSOD-323.pdf), page 2, identifies `BZT52C18S` as `WL` and `BZT52C5V1S` as `W8`. The catalogue's `BZT52C5V1S W8` includes the same code in its manufacturer-number field; whether that is an orderable suffix is unverified. JSCJ's page 4 includes an SOD-323 outline, but its dimensions were not independently extracted and compared here.

The existing local BZT52C18S PDF, SHA-256 `b2de1300cc5939db2acde3f2de8e768cf7dd853d179d60e14bf4bf44781c7817`, is a separate JCST document. Its page 2 independently lists `WL` and `W8`; it is not a JSCJ datasheet and its three pages contain no dimensioned outline. The second entry has no local PDF. No PDF was downloaded in this review.

KiCad `D_SOD-323.step` SHA-256 `cd8619b2119cd95683a2c5e660ab4f2d4db674f696cd6f9e9756f221171a214d` has overall bounds 2.50 x 1.25 x 1.11 mm. The band region is at negative X, matching pin 1 at negative X in KiCad's selected D_SOD-323 footprint. The catalogue dimensions 10 x 5 mm appear to be placeholders. Model dimensions have not been verified against the manufacturer's dimensioned drawing, so disclose this explicitly. Typeface, finish and placement are illustrative; no manufacturing use is implied.
