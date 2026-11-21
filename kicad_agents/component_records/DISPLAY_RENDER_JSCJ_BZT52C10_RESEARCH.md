# JSCJ BZT52C10 SOD-123 display evidence

Reviewed 2026-11-21 against the existing local
`parts_source/electronic_diode_zener_sod_123_jiangsu_changjing_electronics_technology_co_ltd_bzt52c10/datasheet.pdf`,
SHA-256 `fd5a910fc58737806f1596a6318cecd1e1264061e3ca7c6c7f13e69667e36ab5`.
Page 1 shows a cathode bar and says the optional solid dot denotes green
moulding; page 2 lists **WF** for BZT52C10; page 4 shows the SOD-123 drawing
with 2.60–2.80 mm body length, 3.55–3.85 mm lead span, 1.50–1.70 mm body
width and 1.05–1.25 mm height. The optional dot is omitted because the source
record does not specify it.

The installed KiCad `D_SOD-123.step` source SHA-256 is
`b3dc4065573abc72e3d5b4cca0e908f72a24205a41b6284b1f75ccacbe99adf8` and
its overall bounds are 3.8 x 1.6 x 1.26 mm; height exceeds the drawing maximum
by about 0.01 mm. A separate light band region is on negative X, matching pad
1 at negative X in the installed KiCad D_SOD-123 footprint and the cathode
bar convention. Actual finish, typography and positioning are illustrative.
The source 1.6 x 1.25 x 1.1 mm values use a different envelope and remain
unchanged. This is a display approximation, not manufacturing CAD or a PCB
footprint.
