# Infineon IRLR3410 and IRFR3410 DPAK display research

The source records identify the following distinct Infineon MOSFETs, both with
the `Package_TO_SOT_SMD:TO-252-3_TabPin2` PCB footprint:

| Catalogue part | Local International Rectifier PDF SHA-256 | Page 1 |
| --- | --- | --- |
| IRLR3410TRPBF, 100 V 17 A | `8b69599e659b38f3005c381517377511de273c0222928bb5ede95a288486ffe5` | IRLR/U3410PbF, 100 V 17 A |
| IRFR3410TRPBF, 100 V 31 A | `7015efbc3d08d5b97943d7f394847205de662585a8201cf59a1764a6d070c155` | IRFR/U3410PbF, 100 V 31 A |

Each local PDF's page 8 drawing was visually reviewed. Both describe D-Pak
TO-252AA with two full outer leads, a short centre lead and a metal tab; the
marking example is for a different device. The KiCad `TO-252-2.step` model is
a closer display approximation of this shape than the three-full-lead model
selected by the PCB footprint. The footprint and pinout must remain unchanged.
The model's 9.9 x 6.5 x 2.32 mm overall dimensions and short stub are an
approximation; it is not a verified mechanical model or footprint.

`IRLR3410` and `IRFR3410`, respectively, may be used as illustrative partial
identifiers. The exact production markings, logo, typeface, placement and
variable date and lot codes have not been verified.
