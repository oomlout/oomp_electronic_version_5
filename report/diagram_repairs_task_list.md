# Diagram repairs task list

Repair the affected OOMP component schematics and shared drawing routines, then regenerate and inspect the results.

- [x] Battery coin cell `electronic_battery_coin_cell_6_8_mm_maxell_ml414h`: replace the resistor-style schematic with a battery symbol/drawing.
- [x] Micro-SD connector: label pins in the square schematic and keep connector pin labels inside the body.
- [x] General connector schematic layout: ensure pin names stay inside the square; correct connector BIP-39-3-word placement when text currently falls below the body.
- [x] Diode arrays: use the official KiCad-library schematic where available instead of a package-only fallback; regenerate affected diagrams.
- [x] LCD parts: locate the appropriate KiCad-library schematic and update LCD drawings.
- [x] Resettable fuses: replace resistor-style schematics with fuse symbols/drawings.
- [x] ESP32-WROOM: research the package/pin arrangement and correct the schematic drawing.
- [x] AD8495: restore missing pin names in the square schematic; audit the shared IC pin-label path for similar failures.
- [x] TQFP family: research and correct body, pin placement, numbering, and labels across TQFP diagrams.
- [x] Inductors: use the correct resistor-package-style drawing for inductor parts that share standard SMD package sizes.
- [x] LEDs: remove the central circle from text-bearing LED diagrams.
- [x] RGB LEDs: verify pad counts and correct all RGB LED drawings.
- [x] Bus Pirate 5 RGB LED: use the datasheet/package geometry for its unusual leg shape.
- [x] Standard SMD resistors/capacitors: add the normal package marking/value text to the main diagram, including resistor three-digit codes.
- [x] Quarter-watt axial resistors: redraw colour bands as clean un-stroked paint bands and overlay the external capsule outline last.
- [x] 2.54 mm pin headers: scale each collar from the 2.50 mm moulding on the 2.54 mm pitch, reduce the excessive chamfers, and use the documented 3 mm/6 mm right-angle tails.
- [x] Regenerate affected parts, inspect representative SVG/PNG outputs, run focused tests, and update this checklist with results.

## Verification notes

- Battery, fuse, micro-SD, PRTR5V0U2X, LCD, ESP32-WROOM-32E, AD8495, TQFP32, RGB LED, capacitor, and inductor PNG/SVG outputs were regenerated and visually inspected.
- Standard SMD markings now fit inside the package body: resistor `10 ohm` renders `100`; capacitor `2200 pF` renders `222`.
- Quarter-watt resistor colour bands are grouped like the physical part, have no individual black borders, and remain cleanly contained by the final black body outline.
- The 2.54 mm header top and side views now preserve the datasheet proportions: square individual collars, 0.64 mm square pins, and clearly different short/long right-angle legs.
- A complete 2.54 mm header output audit removed the remaining fixed-size identity overlays, corrected the straight carrier offset, replaced right-angle dimension cards that still showed a straight pin, centred low-pin-count bent silhouettes, and added regression coverage for all three profiles.
- SK6812MINI-E remains the four-pad PLCC-style layout; SK6812SIDE-A now follows its datasheet's unusual left-to-right side-emitter row: `1 DIN`, `2 VDD`, `3 DOUT`, `4 GND`.
- Populate-time rules were updated in the extra-detail modules so the repairs survive a future fresh generation.
- Validation: Python compilation, `git diff --check`, `MatchingAgentTests` (21 tests), and the README preview test all pass.

## Follow-up package and project repairs

- [x] LSM9DS1TR: replace the placeholder alternating power/ground pin table with the ST LGA-24 pinout and regenerate the package views.
- [x] PCA9554PW: retain the exact project match and correct the TSSOP-16 pins 8--15 in the canonical part and SparkFun U4 copy.
- [x] SK6812MINI-E: redraw the 3.2 x 2.8 mm body and 1.34 x 0.68 mm side contacts from the manufacturer drawing.
- [x] JST GH SM04B-GH-TF: add the 1.25 mm pitch connector dimensions, four pins, and side-entry top/bottom/side drawing path.
- [x] Eagle-import reconstruction: non-applicable artwork, fiducials, and solder-jumper features remain in audit data but no longer get reconstructed component folders.
- [x] Bus Pirate 5 J302: rotate the canonical PCB footprint by 180 degrees; the preserved original remains unchanged for comparison.

## Scope guard

Only modify shared routines when the behavior is demonstrably generic. Keep source definitions and package metadata separate from generated outputs, and preserve unrelated working-tree changes.

## 2.54 mm pin-header audit

- [x] Replaced the generic straight-header strip with the LCSC C49423294 mechanical style: individual chamfered insulator cells, 0.64 mm square pins, and a dedicated PCB-facing row of 1.02 mm drills. This includes the 22-pin bottom diagram.
- [x] Rebuilt the right-angle short- and long-pin elevations from LCSC C3012223 and C2905424 profiles. Both now show the mating leg, carrier, bend, and board leg; the 6 mm / 3 mm legs distinguish the two OOMP variants.
- [x] Attached the validated LCSC PDF to every source and generated data directory: 40 straight headers, 40 short right-angle headers, and 40 long right-angle headers.
- [x] Routed the physical header-cell rendering through assembly, outline, square, coded, and top views so all diagrams use the same mechanical language.

- [x] Rechecked the right-angle carrier placement against the LCSC 2.54PH 1xN 90-degree mechanical drawing. The shared drawing now offsets the plastic carrier 1.5 mm behind the pad row, while retaining the bent side profile and separate short/long board tails.
- [x] Updated the right-angle family dimensions to the LCSC reference values: 2.5 mm carrier height, 2.5 mm carrier width, and 3.0 mm board-side tail.
- [x] Copied the verified LCSC family datasheet into all 80 right-angle header source directories and generated `data` directories, with the URL and family-reference note recorded in each part's metadata.

- [x] Straight 1xN headers: replace the oversized pin-one marker with a small KiCad-style chamfer and use a square pad only for pin 1; remaining through-hole pads are circular.
- [x] Straight header top/bottom/assembly views: keep the 2.54 mm pitch and the pin-one orientation consistent across the generated views.
- [x] Dual-row headers: normalize the 2xN pad grid to the KiCad 2.54 mm footprint arrangement and preserve odd/even numbering.
- [x] Right-angle short- and long-pin headers: use the one-row KiCad horizontal footprint arrangement for the top view and distinct bent-pin side elevations for the two lead-length variants.
- [x] Female socket headers: retain the 8.5 mm insulation height and 3 mm board tail in the side drawing, with the same square pin-one/circular-pad convention.
- [x] Regenerate all 122 generated `electronic_connector_header_2_54_mm_pitch*` parts and refresh their SVG/PNG orientation views.

### Header verification notes

- Geometry was compared against the installed KiCad `Connector_PinHeader_2.54mm` masters, including `PinHeader_1x06_P2.54mm_Vertical`, `PinHeader_1x06_P2.54mm_Horizontal`, and `PinHeader_2x03_P2.54mm_Vertical`, with 2.54 mm pitch and 0.64 mm square contacts.
- The population rule now applies the normalized drawing after the family metadata copy, preventing the legacy right-angle/dual-row drawing from being reintroduced during regeneration.
- Representative straight, dual-row, right-angle short/long, and socket views were visually checked after the full family refresh.
