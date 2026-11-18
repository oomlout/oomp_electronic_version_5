# Yageo RL visual references for generic low-ohm resistors

These catalogue entries specify package and nominal resistance, but do not
select a manufacturer, tolerance or power. Images illustrate the named Yageo
1% current-sense examples; they do not assign those ratings to the generic
entries or establish interchangeability. KiCad geometry, materials, ink and
placement are illustrative.

| Generic entry | Example | Documented body mark | Geometry comparison |
| --- | --- | --- | --- |
| 1210, 0.1 Ω | [RL1210FR-070R1L](https://yageogroup.com/component-documentation/download/specsheet/RL1210FR-070R1L), 1%, 0.5 W | R100 | KiCad 3.20 × 2.50 × 0.55 mm; manufacturer 3.10 ±0.10 × 2.60 ±0.15 × 0.55 ±0.10 mm, length at upper limit. |
| 2512, 0.015 Ω | [RL2512FK-070R015L](https://yageogroup.com/component-documentation/download/specsheet/RL2512FK-070R015L), 1%, 1 W | R015 | KiCad 6.30 × 3.20 × 0.60 mm; manufacturer 6.35 ±0.10 × 3.20 ±0.15 × 0.55 ±0.10 mm. |

Yageo's manufacturer [chip-resistor marking specification](https://datasheet.octopart.com/232273091002-Yageo-datasheet-640789.pdf),
page 7, maps RL0805–RL2512 E24 100 mΩ to `R100` and 15 mΩ to `R015`,
for 1% and 5% parts. The document and exact-part specifications were reviewed
online; no local PDFs are claimed. Tolerance, current sensing and power ratings
are attributes of the examples, not the generic source records.
