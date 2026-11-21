# UTC 78L05G-AB3-R SOT-89 display research

Reviewed 2026-11-20. Source identifies UTC(Unisonic Tech) 78L05G-AB3-R,
with 4.5 x 2.5 mm source dimensions and no selected KiCad footprint. UTC's
[78LXX family data sheet](https://datasheet.lcsc.com/datasheet/pdf/24955d8a86386c685cabea257ea319d6.pdf?productCode=C380213)
identifies the AB3-R as SOT-89, and its extracted marking diagram shows
`78LXX` plus a package character, with 05 for 5 V and G denoting halogen-free.
A render may show `78L05G`, omitting variable date/pin code; layout, font and
placement are illustrative because the diagram was not visually reviewed.

UTC's [SOT-89 mechanical drawing](https://www.unisonic.com.tw/uploadfiles/836/package_pdf/SOT-89.pdf)
gives a 4.40-4.60 mm body dimension, 2.30-2.60 mm body dimension,
3.90-4.40 mm lead span, 1.40-1.60 mm height and 1.50 mm typical pitch.
The already inspected KiCad `SOT-89-3.step`, SHA-256
`844c0bb504d0c383535d9845c6376fe7a4053241a2ede8d8ef694df3fcfc37c8`,
measures 4.0 x 4.5 x 1.52 mm overall. It has no STEP face colours; the
existing reviewed Holtek SOT-89 adapter classifies the five source solids as
one moulded body and four metallic leads/tab based on their exact geometry.
For this part, use an explicitly bound per-part adapter and verify metal/tab,
marking and orientation visually. No generic pin-one dot should be invented.
Display only; not a verified footprint or mechanical model. No PDF was
downloaded for this research.
