# ESP32 WROOM module display research

Reviewed 2026-11-20. Two distinct source records identify Espressif
ESP32-WROOM-32E-N8 and ESP32-S3-WROOM-1-N8, each with PCB antenna,
18 x 25.5 x 3.1 mm dimensions and a matching selected KiCad RF_Module
footprint. [Espressif's 32E dimensions](https://documentation.espressif.com/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.html)
and [S3 product information](https://www.espressif.com/en/products/modules/esp32-s3-wroom-1-wroom-1u)
corroborate the outline and PCB antenna. Exact shield production markings,
logos, certifications and serials have not been verified; do not invent them.
An illustrative family label must be documented as such.

Installed KiCad `RF_Module.3dshapes/ESP32-WROOM-32E.step` is valid, bounds
18 x 25.5 x 3.1 mm, SHA-256
`57f41a512434023f19bef010df050e42a80a478b62cf87b8b96868b490791bee`.
Its 171 uncoloured faces span PCB substrate and need an explicitly reviewed
material assignment; 269 gold-coloured faces are contacts, 19 grey faces form
the shield. The S3 model `ESP32-S3-WROOM-1.step` is valid with same bounds,
SHA-256 `3e35bb7ba7d030d88855fcf968398c8670934c7dca08b4e30b2c578bc1e13954`;
481 dark substrate faces, 774 gold contacts and 20 grey shield faces. The
shield top is at z=3.1 mm and the PCB at z=0-0.8 mm. These are assemblies,
not simple all-black IC packages: a reviewed module-specific material/marking
adapter is required to make a dark PCB, metallic contacts and shield, and
shield-only text. Investigate whether actual PCB antenna traces are represented;
do not claim manufacturer-exact antenna, certification, logo or marking layout
without evidence. Preview both and verify source hashes before publication.
The KiCad model files stay outside the catalogue; no large CAD outputs or
manufacturer PDF were downloaded for this research.
