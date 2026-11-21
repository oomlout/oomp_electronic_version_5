# onsemi FQD2N60CTM DPAK display research

The catalogue identifies onsemi FQD2N60CTM and uses the
TO-252-3_TabPin2 PCB footprint. Its existing local Fairchild FQD2N60C/FQU2N60C
PDF SHA-256 is `513a34bb8a5ed7dabf96a39e27a71a194f43c9b910e5cc8a82fbfa6bf49a1028`.
Page 1 identifies the FQD2N60C surface-mount family; the exact TM orderable
suffix is not independently established by this document. Page 7's D-PAK
outline was visually reviewed and shows two full outer leads, a short centre
stub and a metal tab. The marking itself is not specified there.

The KiCad TO-252-2 model approximates that shape more closely than the
three-full-lead model associated with the unchanged PCB footprint. The source
model is 9.9 x 6.5 x 2.32 mm overall; the drawing's 9.50 +/- 0.30 mm overall
length reaches 9.80 mm, so the model exceeds this limit by about 0.1 mm.
Geometry and finish are approximate and the model is not manufacturing CAD.
`FQD2N60C` is an illustrative partial identifier, not a verified marking;
logo, typeface, placement and lot/date details are unknown.
