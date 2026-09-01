# Component expansion ledger

This is the linear implementation queue for expanding OOMP's electronic
component coverage.  Work proceeds strictly in sequence: finish, validate, and
record one row before beginning the next row.  Rows are deliberately explicit
so a person can reorder the queue, add a variant, or change a package without
having to understand a generated dependency graph.

## Status values

- `queued`: no implementation work has started.
- `researching`: browser verification is in progress.
- `implemented`: populate and extra definitions exist, but final regeneration
  or project rematching is still outstanding.
- `validated`: the part is generated, tested, and matched into any project that
  requested it.
- `needs_input`: the available project data does not identify an exact part.
- `not_fitted`: retained as research history, but not added as a fitted part.

## Per-component completion checklist

Every exact manufacturer component must complete these steps in order:

1. Confirm the exact MPN, manufacturer, package, and supplier identity using
   the available browser.  Similar suffixes do not count as a match.
2. Open the manufacturer or supplier datasheet in the browser and record the
   source.  Connectors and ICs must also have a browser-downloaded
   `datasheet.pdf` imported through `browser_research_agent.py`.
3. Add the human-editable option to the appropriate
   `working_oomp_populate_<type>.py` array.
4. Add MPN, supplier number, pin names, dimensions, and source notes in the
   corresponding populate-extra file.
5. Add explicit project match overrides for known references.
6. Run `working_oomp_populate.py`, load the generated definitions, generate the
   part assets through the Roboclick action, and rerun the affected project.
7. Run focused tests and the pipeline audit, then set the row to `validated`.

Generic families follow the same sequence but may intentionally omit a
manufacturer and supplier number.  Exact variants are always separate rows.

## Phase 0 — close current project gaps

| ID | Status | Component | Planned OOMP identity | Package / coverage | Required evidence or decision |
| --- | --- | --- | --- | --- | --- |
| E0001 | validated | onsemi `1N4148WT` switching diode | `electronic_diode_switching_sod_523f_onsemi_1n4148wt` | SOD-523F, 2 pins | LCSC `C232841`; pin 1 cathode, pin 2 anode; 1.6 × 0.8 mm nominal drawing; matched to Bus Pirate D401 and D601–D603. Historical project URL was rejected because it resolves to `1N4148WS`. |
| E0002 | queued | `BAS40T-05` dual Schottky diode | exact identity after research | SOT-523, 3 pins | Must not substitute `BAS40W-05`; confirm common-cathode/common-anode topology and exact suffix. |
| E0003 | queued | 1×3 female socket | `electronic_connector_header_2_54_mm_pitch_through_hole_3_pin_socket` | 2.54 mm, vertical, one row | Generic Bus Pirate J201 item; confirm that socket/body height remains intentionally generic. |
| E0004 | queued | Bus Pirate 0805 power inductor | exact identity after research | 0805 / 2012 metric | Historical supplier page, inductance, current rating, DCR, manufacturer, MPN. Do not classify from `1.5A` alone. |
| E0005 | queued | `TFT_20_QT200H1201` display/interface | exact or project-specific identity | Project footprint, 20 pins | Supplier/module drawing, pinout, display dimensions, connector orientation. |
| E0006 | queued | `MMBT7002K` N-MOSFET | exact identity after research | SOT-23, 3 pins | Historical supplier page, exact manufacturer suffix, G/S/D pin order, electrical limits. |
| E0007 | queued | `SI2301` P-MOSFET used by Bus Pirate | exact identity after research | SOT-523, 3 pins | Base number commonly maps to SOT-23; exact small-package suffix and manufacturer are mandatory. |
| E0008 | queued | `BCM857` dual PNP transistor | exact identity after research | SOT-363 / SC-70-6 | Order suffix, dual-transistor topology, six-pin assignment. |
| E0009 | queued | `MMDT3906` dual PNP transistor | exact identity after research | SOT-363 / SC-70-6 | Manufacturer selection, six-pin assignment, matching specification. |
| E0010 | queued | `LMV321` single op-amp | exact identity after research | SOT-23-5 | Manufacturer/suffix, input/output range, five-pin assignment. |
| E0011 | queued | `LMV324` quad op-amp | exact identity after research | TSSOP-14 | Manufacturer/suffix, fourteen-pin assignment, package dimensions. |
| E0012 | queued | `LMV321A` single op-amp | exact identity after research | SOT-23-5 | Establish whether `A` is a materially distinct fitted MPN rather than an alias. |
| E0013 | queued | `LMV331` comparator | exact identity after research | SOT-23-5 | Comparator taxonomy, open-collector output, pin assignment. |
| E0014 | needs_input | PTS810-family tactile switch | exact identity after fitted-BOM input | SMD | Footprint does not determine actuator height, force, or exact suffix. |
| E0015 | needs_input | GT-TC026-family tactile switch | exact identity after fitted-BOM input | SMD, bottom side | Placeholder contains unresolved height and force fields. |

## Phase 1 — foundational discrete semiconductors

| ID | Status | Component | Planned package | Scope and evidence |
| --- | --- | --- | --- | --- |
| E0016 | queued | generic `2N7002` N-MOSFET | SOT-23 | Generic G/S/D definition used for matching projects without an MPN. |
| E0017 | queued | selected exact `2N7002` | SOT-23 | High-stock LCSC manufacturer variant and datasheet. |
| E0018 | queued | generic `BSS138` N-MOSFET | SOT-23 | Generic level-shifting transistor. |
| E0019 | queued | selected exact `BSS138` | SOT-23 | Exact MPN, supplier code, G/S/D assignment. |
| E0020 | queued | `AO3400A` logic-level N-MOSFET | SOT-23 | Exact Alpha & Omega or verified equivalent identity. |
| E0021 | queued | `IRLML6344` logic-level N-MOSFET | SOT-23 | Exact Infineon/IR variant, package and thermal data. |
| E0022 | queued | `AO3401A` P-MOSFET | SOT-23 | Exact variant and G/S/D assignment. |
| E0023 | queued | confirmed `SI2301` P-MOSFET | SOT-23 | Separate from the Bus Pirate SOT-523 item. |
| E0024 | queued | generic `MMBT3904` NPN transistor | SOT-23 | Generic B/E/C definition. |
| E0025 | queued | selected exact `MMBT3904` | SOT-23 | Exact manufacturer and pinout. |
| E0026 | queued | `BC817` NPN transistor | SOT-23 | Gain-bin suffix must be explicit. |
| E0027 | queued | generic `MMBT3906` PNP transistor | SOT-23 | Generic B/E/C definition. |
| E0028 | queued | selected exact `MMBT3906` | SOT-23 | Exact manufacturer and pinout. |
| E0029 | queued | `BC807` PNP transistor | SOT-23 | Gain-bin suffix must be explicit. |
| E0030 | queued | generic `1N4148W` switching diode | SOD-123 | Generic two-pin polarity definition. |
| E0031 | queued | selected exact `1N4148W` | SOD-123 | Exact manufacturer/package variant. |
| E0032 | queued | selected `1N4148WS` | SOD-323 | Keep distinct from `W` and `WT`; exact manufacturer variant. |
| E0033 | queued | generic `BAT54` Schottky diode | SOT-23 | Single-diode three-lead package definition. |
| E0034 | queued | generic `BAT54C` dual Schottky | SOT-23 | Common-cathode topology. |
| E0035 | queued | generic `BAT54S` dual Schottky | SOT-23 | Series topology. |
| E0036 | queued | selected exact BAT54-family variants | SOT-23 | One verified stocked MPN for each topology. |
| E0037 | queued | `SS14` Schottky rectifier | SMA | Exact 1 A / 40 V stocked variant. |
| E0038 | queued | `B5819W` Schottky rectifier | SOD-123 | Exact manufacturer and limits. |
| E0039 | queued | generic `M7` / SMD `1N4007` rectifier | SMA | Generic polarity and package. |
| E0040 | queued | through-hole `1N4007` rectifier | DO-41 | Generic polarity, body and lead spacing. |
| E0041 | queued | 3.3 V Zener diode | SOD-123 | Select a standard exact MPN after generic entry. |
| E0042 | queued | 5.1 V Zener diode | SOD-123 | Select a standard exact MPN after generic entry. |
| E0043 | queued | 12 V Zener diode | SOD-123 | Select a standard exact MPN after generic entry. |
| E0044 | queued | `USBLC6-2SC6` USB ESD array | SOT-23-6 | Exact ST part or an explicitly named equivalent, six-pin route-through pinout. |
| E0045 | queued | single-line 5 V TVS diode | SOD-323 | Choose an exact low-capacitance part. |
| E0046 | queued | `SMAJ5.0A` TVS | SMA | Unidirectional exact part. |
| E0047 | queued | `SMAJ12A` TVS | SMA | Unidirectional exact part. |
| E0048 | queued | 0.5 A resettable fuse | 0603 | Hold/trip current, voltage and exact MPN. |
| E0049 | queued | 1.0 A resettable fuse | 1206 | Hold/trip current, voltage and exact MPN. |
| E0050 | queued | 1.5 A resettable fuse | 1812 | Hold/trip current, voltage and exact MPN. |

## Phase 2 — power and analogue

| ID | Status | Component | Package target | Scope and evidence |
| --- | --- | --- | --- | --- |
| E0051 | queued | `MCP1700-3302` 3.3 V LDO | SOT-23 | Exact suffix, pinout, current and capacitor requirements. |
| E0052 | queued | `XC6206P332` 3.3 V LDO | SOT-23 | Exact manufacturer variant; base name has many clones. |
| E0053 | queued | `AMS1117-3.3` LDO | SOT-223 | Exact manufacturer variant plus generic identity. |
| E0054 | queued | `AMS1117-5.0` LDO | SOT-223 | Exact manufacturer variant plus generic identity. |
| E0055 | queued | `7805` regulator | TO-220 | Generic and selected exact through-hole version. |
| E0056 | queued | `MP1584EN` buck regulator | SOIC-8 exposed pad | Exact pinout, thermal pad and package drawing. |
| E0057 | queued | `MP2307DN` buck regulator | SOIC-8 exposed pad | Exact MPS identity and package drawing. |
| E0058 | queued | `TPS62160` buck regulator | WSON-8 | Exact TI orderable MPN and exposed-pad pin. |
| E0059 | queued | `MT3608` boost regulator | SOT-23-6 | Exact manufacturer rather than module-only naming. |
| E0060 | queued | `TPS61023` boost regulator | VQFN-HR | Exact TI MPN and thermal-pad layout. |
| E0061 | queued | `MCP73831` Li-ion charger | SOT-23-5 | Exact charge-status polarity and programming pin. |
| E0062 | queued | `TP4056` Li-ion charger | SOP-8 exposed pad | Exact manufacturer variant and thermal pad. |
| E0063 | queued | `DW01A` protection controller | SOT-23-6 | Exact clone/manufacturer identity and pinout. |
| E0064 | queued | `FS8205A` dual MOSFET | TSSOP-8 | Back-to-back MOSFET topology and exact pinout. |
| E0065 | queued | `MCP6001` op-amp | SOT-23-5 | Exact suffix and rail-to-rail specification. |
| E0066 | queued | `MCP6002` dual op-amp | SOIC-8 | Exact suffix and eight-pin assignment. |
| E0067 | queued | `LM358` dual op-amp | SOIC-8 | Generic identity plus selected exact modern stocked part. |
| E0068 | queued | `TLV9002` dual op-amp | VSSOP-8 | Exact TI suffix and package. |
| E0069 | queued | `LM393` dual comparator | SOIC-8 | Comparator taxonomy and open-collector outputs. |
| E0070 | queued | `TL431` adjustable reference | SOT-23 | Exact reference/anode/cathode pinout. |
| E0071 | queued | `LM4040-2.5` reference | SOT-23 | Exact voltage-grade suffix. |
| E0072 | queued | `LM4040-3.0` reference | SOT-23 | Exact voltage-grade suffix. |
| E0073 | queued | `INA219` power monitor | SOIC-8 | Exact TI suffix, Kelvin inputs and I2C pins. |
| E0074 | queued | `INA226` power monitor | TSSOP-10 | Exact TI suffix and pinout. |
| E0075 | queued | `ADS1115` ADC | VSSOP-10 | Exact TI suffix, address pin and differential inputs. |
| E0076 | queued | `MCP3008` ADC | DIP-16 and SOIC-16 | Add package variants as separate identities. |
| E0077 | queued | `MCP4725` DAC | SOT-23-6 | Exact address variant and pinout. |

## Phase 3 — logic, interfaces, and memory

| ID | Status | Component set | Package target | Scope and evidence |
| --- | --- | --- | --- | --- |
| E0078 | queued | `74HC00`, `74HC04`, `74HC14`, `74HC32` | SOIC-14 | Add one exact stocked family at a time in the order shown. |
| E0079 | queued | `74HC125`, `74HC138`, `74HC165`, `74HC595` | SOIC/TSSOP | Do not conflate logic-family voltage thresholds. |
| E0080 | queued | `74LVC1G04`, `74LVC1G08`, `74LVC1G125` | SOT-23-5/6 | Exact pin-compatible package codes. |
| E0081 | queued | `PCA9306` level translator | TSSOP-8 | Exact pinout and enable/reference behavior. |
| E0082 | queued | `TXS0108E` level translator | TSSOP-20 | Exact package suffix and OE pin. |
| E0083 | queued | `CH340C` USB serial | SOP-16 | Exact WCH part and internal-clock distinction. |
| E0084 | queued | `CP2102N` USB serial | QFN-24 | Exact revision/package and exposed-pad pin. |
| E0085 | queued | `FT232RL` USB serial | SSOP-28 | Exact FTDI part and pin names. |
| E0086 | queued | `MAX3485` RS-485 | SOIC-8 | Exact 3.3 V transceiver variant. |
| E0087 | queued | `SN65HVD230` CAN transceiver | SOIC-8 | Exact TI suffix and standby pin. |
| E0088 | queued | modern `MCP2551` replacement | SOIC-8 | Choose active-production 5 V CAN part rather than obsolete-only entry. |
| E0089 | queued | `24LC32`, `24LC64`, `24LC256` EEPROM | SOIC-8 | Add capacities linearly; confirm address-pin behavior. |
| E0090 | queued | `W25Q16JV`, `W25Q32JV`, `W25Q64JV` flash | SOIC-8 | Add capacities linearly with exact Winbond suffixes. |
| E0091 | queued | microSD push-push socket | exact selected footprint | Datasheet, card-detect pin and shield pins. |
| E0092 | queued | microSD hinged socket | exact selected footprint | Datasheet, card-detect pin and shield pins. |
| E0093 | queued | `DS3231M` / `DS3231` RTC | SOIC-16 | Treat MEMS and crystal versions as separate parts. |
| E0094 | queued | `PCF8523` RTC | SOIC-8 | Exact NXP suffix and backup-supply pin. |

## Phase 4 — controllers, sensors, and user interface

| ID | Status | Component | Package target | Scope and evidence |
| --- | --- | --- | --- | --- |
| E0095 | queued | `ATmega328P` | TQFP-32 | Exact active orderable MPN and full pin names. |
| E0096 | queued | `ATtiny85` | SOIC-8 | Exact suffix and programming pins. |
| E0097 | queued | `ATtiny1616` | SOIC-20 | UPDI and alternate-function pin names. |
| E0098 | queued | `SAMD21G18A` | TQFP-48 | Exact suffix, exposed alternatives excluded. |
| E0099 | queued | `STM32F103C8T6` | LQFP-48 | Exact ST part and full pinout. |
| E0100 | queued | selected small STM32G0 | LQFP/QFN | Choose exact part from observed project demand. |
| E0101 | queued | `ESP32-C3-MINI-1` module | module footprint | Antenna keepout, castellated pins and exact module revision. |
| E0102 | queued | `ESP32-S3-WROOM-1` module | module footprint | Antenna/flash/PSRAM suffixes are separate identities. |
| E0103 | queued | `ESP-12F` module | module footprint | Exact Ai-Thinker module dimensions and pins. |
| E0104 | queued | `BME280` environmental sensor | LGA-8 | Exact Bosch part; do not substitute BMP280. |
| E0105 | queued | `SHT31` humidity sensor | DFN-8 | Exact Sensirion accuracy grade. |
| E0106 | queued | `AHT20` humidity sensor | LGA-6 | Exact Aosong identity and pinout. |
| E0107 | queued | `DS18B20` temperature sensor | TO-92 | Genuine/compatible distinction and 1-Wire pinout. |
| E0108 | queued | `LIS3DH` accelerometer | LGA-16 | Exact ST package and interrupt pins. |
| E0109 | queued | `MPU-6050` IMU | QFN-24 | Exact TDK/InvenSense identity; module is separate. |
| E0110 | queued | `ICM-42688-P` IMU | LGA-14 | Exact part and auxiliary interface pins. |
| E0111 | queued | `BH1750` light sensor | WSOF-6 | Exact manufacturer suffix and address pin. |
| E0112 | queued | `VEML7700` light sensor | SMD-4 | Exact Vishay part and optical opening. |
| E0113 | queued | `VL53L0X` ranging sensor | LGA-12 | Exact ST part and optical keepout. |
| E0114 | queued | `HC-SR04` module | 4-pin module | Module dimensions and transducer clearance. |
| E0115 | queued | electret microphone capsule | through-hole | Generic diameter/height variants. |
| E0116 | queued | `MAX9814` microphone amplifier | TDFN-14 | Exact pinout; module is separate. |
| E0117 | queued | magnetic buzzer and piezo disc | common footprints | Separate active, passive, and bare-disc identities. |
| E0118 | queued | 6×6 mm tactile switch | through-hole | Generic height variants. |
| E0119 | queued | `EC11` rotary encoder | through-hole | Exact shaft/switch/mounting variants. |
| E0120 | queued | common slide switch | through-hole and SMD | Select exact SPDT examples rather than one ambiguous generic body. |

## Phase 5 — connector families

| ID | Status | Family | Variants | Implementation notes |
| --- | --- | --- | --- | --- |
| E0121 | queued | 2.54 mm dual-row male headers | 2×2 through 2×20 | Simple pin-count array and nested loop; OOMP name uses total pins plus `dual_row`. |
| E0122 | queued | 2.54 mm female sockets | 1×1 through 1×40 | Separate socket taxonomy from exposed male headers. |
| E0123 | queued | 2.54 mm dual-row female sockets | 2×2 through 2×20 | Total-pin naming plus `dual_row`. |
| E0124 | queued | JST-PH 2.0 mm | 2–6 pins, vertical and right-angle | Generic family plus selected exact JST MPN per orientation. |
| E0125 | queued | JST-XH 2.5 mm | 2–8 pins | Generic family plus selected exact JST MPN. |
| E0126 | queued | JST-SH 1.0 mm | 2–10 pins, right-angle | Include 4-pin Qwiic/STEMMA QT and retain existing exact 9-pin part. |
| E0127 | queued | JST-GH 1.25 mm | 4–10 pins | Generic family plus selected exact JST MPN. |
| E0128 | queued | USB Micro-B receptacle | common 5-pin SMD | Add exact connector after mechanical drawing review. |
| E0129 | queued | USB Mini-B receptacle | common 5-pin SMD | Add exact connector after mechanical drawing review. |
| E0130 | queued | USB-C receptacles | 6, 12, 16 and 24 contacts | Each mechanical/pad pattern is a separate exact part. |
| E0131 | queued | screw terminals 3.5 mm | 2–6 positions | Nested pitch/pin-count arrays; exact example later. |
| E0132 | queued | screw terminals 5.08 mm | 2–6 positions | Nested pitch/pin-count arrays; exact example later. |
| E0133 | queued | 2.1 mm DC barrel jack | through-hole | Exact switched and unswitched versions. |
| E0134 | queued | FFC/FPC connectors | 0.5 and 1.0 mm common counts | Exact top/bottom-contact orientation must be part of identity. |
| E0135 | queued | AVR ISP header | 2×3, 2.54 mm | Keyed/unkeyed variants and pin names. |
| E0136 | queued | ARM Cortex debug header | 2×5, 1.27 mm | Standard SWD pin names and keyed shroud variant. |
| E0137 | queued | IDC/JTAG header | 2×10, 2.54 mm | Keyed shroud and standard pin naming. |

## Progress log

| Date | ID | Result |
| --- | --- | --- |
| 2026-09-01 | E0001 | Validated. Browser research confirms onsemi `1N4148WT`, `C232841`, SOD-523F, 75 V, 300 mA. Added population/extra data, cathode-band diagrams, eight previews, Jinja README, and four Bus Pirate mappings. The project research queue fell from 15 to 14 items. Historical project link `120141` is rejected because it is onsemi `1N4148WS`, `C118873`, SOD-323. |
