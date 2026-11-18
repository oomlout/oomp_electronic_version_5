# Fenghua RC-MT08W000JT zero-ohm array marking

Fenghua's manufacturer-authored chip network resistor approval sheet N-5.10,
page 7, explicitly says RCMT08 zero-ohm jumpers are marked `0`:
https://robu.in/wp-content/uploads/2025/01/C880286.pdf
This sheet was reviewed online. The selected catalogue part is also listed as
a four-element 0402×4, eight-terminal 0 Ω array at:
https://jlcpcb.com/partdetail/2353-RCMT08W000JT/C2001

The component has a separate existing local distributor PDF at
`parts_source/electronic_resistor_array_4_x_0402_convex_0_ohm_8_pin/datasheet.pdf`;
its first page identifies the relevant chip network family and its hash is
`ed64f3cf8e3ba35d58715fdc05d1c02b529825795e2d2400e6eabc803ba74218`.
The online approval sheet, not that scanned local PDF, supplies the verified
single-zero marking. KiCad geometry, materials, ink and placement are
illustrative; 0402 model height is at the manufacturer tolerance limit.
