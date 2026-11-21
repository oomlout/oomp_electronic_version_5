# XFCN two-position header display research

Candidate: `electronic_connector_header_2_54_mm_pitch_through_hole_2_pin`,
whose source record names XFCN PZ254V-11-02P / LCSC C492401. The existing
`model_3d.step` has no STEP colour data and its accompanying provenance calls
it nominal reference geometry; do not silently treat it as manufacturer CAD.

The [XFCN PZ254V-11-XX family drawing](https://www.xfconn.com/uploads/soft/20240711/4-240G111231T93.pdf),
reviewed online on 2026-11-21, specifies a black PA6T insulator, brass
contacts, and matte tin **or** gold over nickel. It lists two positions,
2.54 mm pitch, 5.08 mm body length, 2.50 mm body width and height, and
0.64 mm square pins. Its drawing indicates a 6.1 mm mating length and
3.0 mm tail. The family drawing allows multiple finishes; it does not prove
the finish of the exact catalogue unit. The [JLCPCB listing](https://jlcpcb.com/partdetail/Xfcn-PZ254V_1102P/C492401)
independently identifies this part as black with 6 mm mating and 3 mm tail.
No manufacturer PDF was downloaded or added locally.

KiCad 10 supplies `Connector_PinHeader_2.54mm.3dshapes/PinHeader_1x02_P2.54mm_Vertical.step`,
SHA-256 `ea4d0799007ebdd3945072bf255d673d2fe87eb05fda85fd8d7993ad9397da41`.
Its authored palette contains separate dark and gold-coloured regions. Before
staging a render, inspect the actual shape dimensions, pin exposure and
material roles against the drawing; the existence of a matching footprint name
alone is not proof of exact equivalence. A gold finish can be shown only as an
illustrative allowed family finish, with that limitation in the output. The
part has no evidence of a printed mark; do not invent a logo or part code.
Credit the KiCad model and license, and retain no new STEP or STL export.

On 2026-11-21 OpenCascade read the KiCad STEP as one valid root with overall
bounds 2.54 x 5.08 x 11.54 mm (Z from -3.00 to 8.54 mm). Its 16 dark
faces and 36 gold-coloured faces are separate material regions. The nominal
2.54 mm body width and height differ from the family drawing's 2.50 mm by
0.04 mm; the overall envelope is consistent with a 3 mm tail, 2.54 mm body
and 6 mm mating end. Inspection by source face colour confirms that the dark
body spans Z=0 to 2.54 mm, while the contacts span Z=-3.00 to 8.54 mm: the
model has a 3.00 mm tail and 6.00 mm mating end. The source CAD is generic
KiCad geometry, not XFCN's own model.
