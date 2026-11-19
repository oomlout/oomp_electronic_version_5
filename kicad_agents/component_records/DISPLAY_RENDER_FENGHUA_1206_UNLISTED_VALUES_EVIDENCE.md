# Fenghua 1206 values absent from the series table

Reviewed 2026-11-19. Supplier listings identify [1206CG250J500NT / C1898, 25 pF](https://item.szlcsc.com/2250.html),
[1206CG360J500NT / C1908, 36 pF](https://techtonions.com/product/TO-INT-1908),
[1206B391K500NT / C1866, 390 pF](https://www.lcsc.com/product-detail/C1866.html),
and [1206B501K500NT / C1873, 500 pF](https://www.lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_FH-Guangdong-Fenghua-Advanced-Tech_C1873.html).
They are 1206, 50 V; the first two are C0G ±5%, the latter two X7R ±10%.

The existing local Fenghua general MLCC PDF, SHA-256
`705023d3be0454148a96fc2715d249a32d8ff442e70b64d1116d3490ed1d8136`,
pages 7 and 12, uses nominal 0.8 mm thickness for nearby listed 1206
values, but does **not** list these exact four values. The unmarked KiCad
illustration therefore uses 0.8 mm as a generic example, not an established
exact thickness. Actual height, colour, terminations and finish are unknown.
It is not a dimensional or purchasing specification. No PDF was downloaded.
