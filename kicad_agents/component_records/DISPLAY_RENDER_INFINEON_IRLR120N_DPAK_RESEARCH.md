# Infineon IRLR120NTRPBF DPAK display research

Catalogue source identifies IRLR120NTRPBF, Infineon Technologies, a 100 V
10 A MOSFET, with the TO-252-3_TabPin2 PCB footprint. The already-present
International Rectifier IRLR/U120NPbF datasheet was acquired through the
interactive browser according to `datasheet_source.yaml`; its SHA-256 is
`2677b70bc4ac977f2470ab2c036362530ff0051ac5ca631b6dbf2efcaaf3e0ac`.
Page 1 identifies the surface-mount IRLR120N device; page 8 contains the
D-Pak TO-252AA drawing and a marking example for a different IRFR120 part.

The page 8 drawing shows two full outer leads, a short centre lead and a
metal tab. Its D body dimension is 5.97–6.22 mm, E 6.35–6.73 mm, A
2.18–2.38 mm, and overall H 9.40–10.41 mm. The checked KiCad `TO-252-2.step`
model has overall bounds 9.9 x 6.5 x 2.32 mm and the illustrated two full
leads plus centre stub. It is therefore a better display approximation than
the footprint's `TO-252-3_TabPin2.step`, which has three full leads. This
selection does not change the catalogue footprint or pinout. The shorter
centre lead, exact model tolerances, finish and text placement are approximate;
the display model is not a verified manufacturing model or footprint.

`IRLR120N` is an illustrative partial identifier. The datasheet's marking
example is for IRFR120 and does not verify this device's exact top marking,
logo, typeface or variable production codes; these details are not asserted.
