# Plan: missing components in the recent Adafruit and SparkFun projects

## Scope and audit result

This plan covers the 19 generated Adafruit and SparkFun project folders currently present under `parts/oomp_project_github_*`.

Status: the identified ADXL343 item has now been added and the affected Adafruit project has been regenerated. The remaining review records are intentional board-feature exclusions pending queue cleanup.

The audit found:

- 1,309 PCB footprint records across the folders.
- 509 matched component records.
- 0 unmatched physical components in the generated project summaries.
- 1 active browser-research task at the time of the audit: Adafruit ADXL345 STEMMA QT, reference `U1`, value `ADXL343`, footprint `LGA14`. This task is now resolved.
- 87 open LCSC-review records, of which most are board-feature records rather than purchased components.

Therefore the first pass should not blindly create 87 new catalogue parts. The one real component identity is resolved; the remaining work is to cleanly classify and remove the expected non-parts from the review queues.

## Priority 1 — resolve the real missing component

### Adafruit ADXL345 STEMMA QT: `U1`, `ADXL343`, `LGA14`

Files to inspect:

- `parts/oomp_project_github_adafruit_adafruit_adxl345_pcb_adxl345_stemma_qt_current/data/generated_data/browser_research_queue.yaml`
- `parts/oomp_project_github_adafruit_adafruit_adxl345_pcb_adxl345_stemma_qt_current/data/generated_data/lcsc_review.yaml`
- The source project schematic and PCB in that project folder.

Work sequence:

1. Confirm whether the fitted device is genuinely ADXL343 or an ADXL345 variant with an imported/mistyped value.
2. Use the manufacturer datasheet to confirm the LGA14 package outline, pad numbering, orientation, exposed pad behaviour, and pin names.
3. Search the existing catalogue for an equivalent ADXL343 part before creating a new part. Reuse the existing LGA14 accelerometer drawing routines only where the pinout and package are identical.
4. If it is a distinct part, add its definition in the `populate` section only, including the manufacturer part number, datasheet evidence, KiCad symbol, KiCad footprint, pin map, and reusable taxonomy.
5. Add a precise matching rule or project override only after the datasheet identity is confirmed.
6. Regenerate U1's schematic, PCB, assembly, and dimensioned drawings, then verify the pin-1 marker and all 14 pads against the datasheet.

Acceptance criteria: U1 has a confirmed OOMP ID, a populated part folder, a real schematic symbol, the correct LGA14 footprint, and no remaining browser-research task.

## Priority 2 — classify expected board features instead of adding parts

The following open review records should normally remain excluded from the purchased-component catalogue:

- `U$` Eagle-import graphics, STEMMAQT artwork, PCB feature marks, logos, and revision graphics.
- Fiducials and `FIDUCIAL-1X2` footprints.
- SparkFun and Adafruit solder-jumper traces: `Jumper_2_*`, `Jumper_3_*`, `SOLDERJUMPER`, and related trace variants.
- Test points at 0.75 mm, 1.0 mm, and 1.25 mm.
- Ordering-instruction artwork and the BMV080 outline-only footprint.
- Power symbols, `#PWR*`, `#GND*`, `kibuzzard` text, and other schematic-only graphics.

The matcher already contains board-feature handling for these categories. The next implementation step should be to make the review-queue generator use the same classifier, so these records are marked `not_applicable` before LCSC research is requested. This avoids adding fake parts merely to make the review count reach zero.

## Project-specific review groups

| Project family | Open review focus | Planned treatment |
|---|---|---|
| Adafruit ADXL345 STEMMA QT | `U1` ADXL343 LGA14 plus imported artwork | Research and add/confirm the real sensor; exclude artwork |
| Adafruit LIS3DH Breakout | `U$` artwork and `SOLDERJUMPER` | Keep as board features; verify the existing LIS3DH and connector matches |
| SparkFun ADXL345 Breakout | Fiducials and SparkFun logos | Keep excluded; no new catalogue part |
| SparkFun Audio Player MY1690X-16S | Jumper traces; generic 2.54 mm connector already has a candidate match | Keep jumpers excluded; only research the connector if its physical height/type is needed |
| SparkFun Capacitive Soil Moisture | Jumper traces and 1.0 mm test points | Keep as board features |
| SparkFun GNSS DAN-F10N | Jumper traces and measurement links | Keep as board features unless a fitted purchased switch is proven |
| SparkFun GNSS Flex | Jumper traces, 1.25 mm test points, and configuration links | Keep as board features; do not create jumper parts |
| SparkFun BMV080 | Configuration jumpers and outline-only artwork | Keep excluded; retain the BMV080 sensor match |
| SparkFun Qwiic ADC ADS1219 | Jumper/configuration pads | Keep as board features |
| SparkFun Qwiic Current INA2XX and ADE7953 | Jumper/configuration pads | Keep as board features; verify the two IC identities remain distinct |
| SparkFun Qwiic Directional Pad | Configuration jumpers | Keep excluded; verify PCA9554PW and the four-way switch |
| SparkFun Qwiic GNSS SAM-M8Q, both versions | Jumper pads and 0.75 mm test points | Keep as board features; compare the two versions for genuine component differences |
| SparkFun Qwiic Navigation Switch | Address and power jumpers | Keep as board features; verify the navigation switch drawing |
| SparkFun Roller Encoder | No open review items | Use as a clean reference project during regression checks |
| SparkFun LIS3DH Qwiic 1x1 and Micro | Address jumpers and test points | Keep as board features; verify the LIS3DH and connector matches |
| SparkFun u-blox NEO-F10N | Configuration jumpers and ordering artwork | Keep as board features; retain the GNSS module match |

## Implementation order

1. Fix the review-queue generator to call the shared board-feature classifier before creating LCSC tasks.
2. Research and resolve the ADXL343/ADXL345 LGA14 identity.
3. Add or update the part through the `populate` section only; do not hand-edit generated part data.
4. Regenerate the affected component diagrams and the ADXL345 project outputs.
5. Regenerate the review queues for all 19 folders and confirm that only genuinely unresolved purchased parts remain.
6. Run the project and catalogue tests, then compare the matched component count and board images before and after.

## Verification checklist

- Every physical PCB component has a matched OOMP ID or an explicitly documented, intentional exception.
- No `U$`, logo, fiducial, test-point, solder-jumper, power-symbol, or outline-only record creates a catalogue part.
- The ADXL343/ADXL345 identity is backed by a manufacturer datasheet and exact package evidence.
- LGA14 pin numbering, orientation, and drawing dimensions agree with the confirmed device.
- Existing Qwiic/JST, 2.54 mm header, sensor, IC, LED, resistor, capacitor, and mounting-hole matches do not regress.
- The 19 project summaries regenerate with zero unmatched physical components and clean review queues.
