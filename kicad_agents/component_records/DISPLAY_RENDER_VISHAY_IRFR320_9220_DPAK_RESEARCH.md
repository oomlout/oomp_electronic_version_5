# Vishay IRFR320 and IRFR9220 DPAK display research

The catalogue identifies Vishay Intertech IRFR320TRPbF (400 V, 3.1 A) and
IRFR9220TRPBF (200 V, 3.6 A), each with the TO-252-3_TabPin2 PCB footprint.
Existing local Vishay Siliconix datasheets identify the IRFR320 and IRFR9220
surface-mount families; PDF SHA-256 values are respectively
`aefc79753d7e33eb884a72af9553b2bf0f0758db458781081bbc62def6a8348f` and
`25279b90966f742ef742b465351d7b7edb81ffcf1ac553b891644c667dca309e`.

Each PDF's page 8 includes the same Vishay TO-252AA outline document 71197,
visually reviewed; it shows two full outer leads, a short centre stub and a
metal tab. The source PDFs required Poppler's cross-reference reconstruction,
but the package drawings rendered visibly. The KiCad TO-252-2 display model
approximates this shape more closely than the three-full-lead model associated
with the unchanged PCB footprint. Its 9.9 x 6.5 x 2.32 mm envelope and stub
are approximate; it is not verified mechanical CAD or a footprint.

`IRFR320` and `IRFR9220` are illustrative partial identifiers: the photos
and drawings do not establish exact device markings, logos, typeface,
placement or variable manufacturing codes.
