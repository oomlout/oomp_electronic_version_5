# Espressif ESP8285H16 QFN display research

Reviewed 2026-11-20. The catalogue ID implies Espressif ESP8285H16, but the
source record has no manufacturer or manufacturer orderable field; preserve
that identity as inferred. Its name includes Wi-Fi and Bluetooth, while the
Espressif documentation establishes Wi-Fi; do not imply Bluetooth support from
this source. The record says QFN-33 and 5 x 5 x 1.0 mm; its package_drawing
lists 33 perimeter pins (9 on one side and 8 on each of the other sides) and
a 2.1 x 2.1 mm centre box.

Espressif's [ESP8285 data sheet](https://documentation.espressif.com/0a-esp8285_datasheet_en.html)
identifies H16 and specifies a 5 x 5 mm 32-perimeter-contact QFN. Its
[manufacturer PDF](https://documentation.espressif.com/api/resource/doc/file/8YeJDEz3/FILE/0a-esp8285_datasheet_en.pdf)
package table text gives 0.85 mm nominal height (0.80-0.90), 0.5 mm pitch and
3.7 x 3.7 mm nominal exposed pad; the screenshot attempt returned a resource
error, so drawing view associations have not been visually confirmed. These
conflict with the source 33-perimeter drawing, 2.1 mm centre box and 1.0 mm
height; retain and disclose the source discrepancies rather than altering
source fields. The centre exposed pad is commonly a 33rd electrical connection,
not a 33rd perimeter contact.

A local KiCad candidate `Package_DFN_QFN.3dshapes/QFN-32-1EP_5x5mm_P0.5mm_EP3.7x3.7mm.step`
matches nominal outline, pitch and pad name; inspect geometry, materials,
height and SHA before selection. Physical product marking has not been verified:
if rendered, ESP8285H16 may only be an illustrative identifier and omitted
production codes, typography, placement and orientation must be disclosed.
No model is staged and no manufacturer PDF was downloaded for this review.

Espressif's [2019 change notice](https://documentation.espressif.com/PCN-04-20190625%20ESP8285%20Datasheet%20Change.pdf)
documents a post-change H16 marking: `ESP8285`, a variable week/year line,
`H16` followed by variable characters, and another variable line. A display
may show the fixed `ESP8285` and `H16` portions with omitted variable codes;
layout, font, logo and omissions remain illustrative. The web-extracted
illustration has not been independently visually checked. Prefer this over a
single-line invented `ESP8285H16` production marking.

Inspected local QFN candidate: one valid root; SHA-256
`7e77a52b3e261a45529e0df739376ea7cd79204fb1afad81332a50f4f1607000`;
5.0 x 5.0 x 0.85 mm bounds; distinct body, termination and pin-indicator
colours. It matches the nominal manufacturer table and candidate name, though
pad placement and manufacturing details remain display approximations.
