# Yageo visual references for unsourced generic 0603 resistors

These generic entries specify nominal resistance and package, but no supplier
or tolerance. Images illustrate named Yageo examples without assigning their
supplier or tolerance to the entries. KiCad geometry, materials, typeface and
placement are illustrative.

Yageo's [marking specification](https://yageogroup.com/content/Resource%20Library/Product%20Guide-Catalog/yageo_PYu-R_Marking_3_19050818_924.pdf)
documents three-digit E24 codes for 5% RC0603 parts at 10 Ω and above, an R
decimal code below 10 Ω, and EIA-96 for 1% E96 parts. Its E96 table maps 71
to 536 and C to ×100, so 71C represents 53.6 kΩ. The document was reviewed
online; no local PDF is claimed.

| Value | Yageo visual reference | Example tolerance | Mark | Identity evidence |
| --- | --- | --- | --- | --- |
| 1.6 kΩ | RC0603JR-071K6L | 5% | 162 | https://www.ti.com.cn/cn/lit/df/tidr898/tidr898.pdf |
| 30 Ω | RC0603JR-0730RL | 5% | 300 | https://jlcpcb.com/partdetail/YAGEO-RC0603JR0730RL/C137636 |
| 53.6 kΩ | RC0603FR-0753K6L | 1% | 71C | https://yageogroup.com/component-documentation/download/specsheet/RC0603FR-0753K6L |
| 5.6 Ω | RC0603JR-075R6L | 5% | 5R6 | https://www.ibselectronics.com/part/yageo/rc0603jr-075r6l/345452/ |
