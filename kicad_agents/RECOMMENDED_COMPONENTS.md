# Recommended components to add

The current population is strong in resistors, LEDs, headers, and a small set
of project-specific ICs, but it has major gaps in transistors, general-purpose
diodes, op-amps, regulators, switches, sensors, and power parts. The priorities
below combine gaps exposed by the two imported projects with patterns visible
in established open-hardware ecosystems.

Research references:

- [Official KiCad symbol library](https://gitlab.com/kicad/libraries/kicad-symbols/-/tree/master) — its first-level libraries show the broad families a useful electronics taxonomy needs, including logic, amplifiers, ADC/DAC, battery management, and processors.
- [Arduino UNO R3 documentation](https://docs.arduino.cc/hardware/uno-rev3) — a representative microcontroller board with USB, power regulation, clocking, reset, headers, and protection/support components.
- [Raspberry Pi hardware design with RP2040](https://pip.raspberrypi.com/documents/RP-008279-DS-hardware-design-with-rp2040.pdf) — an official reference for a modern MCU, external flash, power, clock, USB, and support circuitry.
- [Adafruit Feather RP2040 PCB](https://github.com/adafruit/Adafruit-Feather-RP2040-PCB) — an open-source compact board combining an MCU, USB, battery/power management, flash, connectors, buttons, and indicators.
- [SparkFun Pro Micro RP2040](https://github.com/sparkfun/SparkFun_Pro_Micro-RP2040) — an open hardware RP2040 board with USB, an addressable LED, and Qwiic connectivity.
- [LCSC 2N7002 browser search](https://www.lcsc.com/search?q=2N7002) — a useful warning that a common base number maps to many manufacturers and stock codes; package and exact manufacturer identity must be recorded rather than assuming the first result.

## Priority 0: finish the currently imported projects

These should be researched first because they already appear as unresolved or
review-required parts in the Bus Pirate project.

| Family | Candidate | Package | Why add it | Research caution |
| --- | --- | --- | --- | --- |
| Switching diode | `1N4148WT` | SOD-523 | Four fitted references | Confirm maker and exact `WT` suffix. |
| Dual Schottky diode | `BAS40T-05` | SOT-523 | Five fitted references | Do not substitute the more visible `BAS40W-05`. |
| N-channel MOSFET | `MMBT7002K` | SOT-23 | Fitted level/power switching part | Confirm exact manufacturer and current/voltage ratings. |
| P-channel MOSFET | `SI2301` family | SOT-523 on this board | Ten fitted references | Base name commonly resolves to a different package; identify the exact suffix. |
| Dual PNP transistor | `BCM857` | SOT-363/SC-70-6 | Fitted matched-pair/dual transistor | Confirm package and order suffix. |
| Dual PNP transistor | `MMDT3906` | SOT-363/SC-70-6 | Fitted dual general-purpose transistor | Choose a real manufacturer part, not only the base number. |
| Op-amp | `LMV321`, `LMV321A` | SOT-23-5 | Four fitted single amplifiers | Manufacturer and suffix affect specification. |
| Quad op-amp | `LMV324` | TSSOP-14 | Two fitted quad amplifiers | Confirm common-mode/output characteristics and suffix. |
| Comparator | `LMV331` | SOT-23-5 | One fitted comparator | Do not classify as an op-amp. |
| Tactile switch | PTS810 family | SMD | Reset/user switch footprint | Height and operating-force suffix are part-specific. |
| Tactile switch | GT-TC026 family | SMD | Bottom-side button | Resolve the placeholder height/force string. |
| Inductor | fitted 0805, 1.5 A part | 0805 | Power/current-limit network | Current alone is insufficient; record inductance or impedance and MPN. |
| Display connector/module | `TFT_20_QT200H1201` | project footprint | Fitted display interface | Find exact supplier/module documentation and pinout. |
| Socket header | 1×3, 2.54 mm vertical | through-hole | Fitted generic connector | Decide whether OOMP stays generic or records a chosen height/manufacturer. |

## Priority 1: foundational discrete parts

Add generic taxonomy entries first, then one or more exact manufacturer variants
through populate-extra files.

| Type | Recommended parts | Packages to cover |
| --- | --- | --- |
| Small-signal N-MOSFET | `2N7002`, `BSS138` | SOT-23 |
| Logic-level power MOSFET | `AO3400A`, `IRLML6344` | SOT-23 |
| Small P-MOSFET | `AO3401A`, a confirmed `SI2301` variant | SOT-23 and the exact smaller package used by projects |
| NPN transistor | `MMBT3904`, `BC817` | SOT-23 |
| PNP transistor | `MMBT3906`, `BC807` | SOT-23 |
| Switching diode | `1N4148W`, `1N4148WT` | SOD-123/SOD-323/SOD-523 as exact variants |
| Schottky diode | `BAT54`, `BAT54C`, `BAT54S`, `SS14`, `B5819W` | SOT-23, SMA, SOD-123 |
| Rectifier diode | `M7`/`1N4007` SMD and through-hole `1N4007` | SMA and DO-41 |
| Zener diode | 3.3 V, 5.1 V, 12 V common variants | SOD-123 and SOT-23 |
| ESD/TVS protection | `USBLC6-2SC6`, single-line 5 V TVS, common SMAJ series | SOT-23-6, SOD-323, SMA |
| Resettable fuse | 0.5 A, 1.0 A, 1.5 A polyfuses | 0603, 1206, 1812 |

## Priority 2: power and analogue building blocks

| Type | Recommended parts | Reason |
| --- | --- | --- |
| 3.3 V LDO | `AP2112K-3.3` (already present), `MCP1700-3302`, `XC6206P332`, `AMS1117-3.3` | Covers compact low-current and easy prototype packages. |
| 5 V LDO | `AMS1117-5.0`, `7805` | Common legacy/open-hardware supply choices. |
| Buck regulator | `MP1584EN`, `MP2307DN`, `TPS62160` | Common module and compact-board switching supplies. |
| Boost regulator | `MT3608`, `TPS61023` | Battery and 5 V boost designs. |
| Li-ion charger | `MCP73831`, `TP4056` | Extremely common single-cell open-hardware charging circuits. |
| Battery protection | `DW01A` plus `FS8205A` | Common protected-cell circuit pair. |
| Single/dual op-amp | `MCP6001`, `MCP6002`, `LMV321`, `LM358`, `TLV9002` | General low-voltage analogue coverage. |
| Comparator | `LM393`, `LMV331` | Dual and single comparator coverage. |
| Voltage reference | `TL431`, `LM4040-2.5`, `LM4040-3.0` | Feedback, ADC, and calibration designs. |
| Current/power monitor | `INA219`, `INA226` | Common I²C power-monitoring parts. |
| ADC/DAC | `ADS1115`, `MCP3008`, `MCP4725` | Common expansion and sensor-interface choices. |

## Priority 3: logic, interfaces, and memory

| Group | Recommended parts |
| --- | --- |
| Basic logic | `74HC00`, `74HC04`, `74HC14`, `74HC32`, `74HC125`, `74HC138`, `74HC165`, `74HC595` |
| Small logic | `74LVC1G04`, `74LVC1G08`, `74LVC1G125`, plus the existing `SN74LVC1G57` |
| Level translation | `BSS138` four-channel circuit, `PCA9306`, `TXS0108E`, `74LVC1T45` |
| USB to serial | `CH340C`, `CP2102N`, `FT232RL`, plus the existing `CH343P` |
| RS-485/CAN | `MAX3485`, `SN65HVD230`, `MCP2551`/modern replacement |
| EEPROM | `24LC32`, `24LC64`, `24LC256` |
| SPI NOR flash | `W25Q16JV`, `W25Q32JV`, `W25Q64JV`, plus the existing `W25Q128JV` |
| microSD | Push-push and hinged microSD sockets plus their ESD/protection network |
| RTC | `DS3231M`/`DS3231`, `PCF8523` |

## Priority 4: controllers, sensors, and user interface

| Group | Recommended parts |
| --- | --- |
| Microcontrollers | `ATmega328P`, `ATtiny85`, `ATtiny1616`, `SAMD21G18A`, `STM32F103C8T6`, a small STM32G0, and existing `RP2040` |
| Wireless modules | `ESP32-C3-MINI-1`, `ESP32-S3-WROOM-1`, `ESP8266-12F` |
| Temperature/humidity | `BME280`, `SHT31`, `AHT20`, `DS18B20` |
| Motion | `LIS3DH`, `MPU-6050`, `ICM-42688-P` |
| Light | `BH1750`, `VEML7700`, common LDR footprints |
| Distance | `VL53L0X`, `HC-SR04` module/header definition |
| Audio | Electret microphone capsule, `MAX9814`, small magnetic buzzer, piezo disc |
| Controls | 6×6 mm through-hole tactile switch, common SMD tactile switches, `EC11` rotary encoder, slide switch |

## Priority 5: connector families

The current library has single-row 2.54 mm headers and a few exact connectors.
The next connector work should emphasize families that recur across open-source
boards:

- 2.54 mm dual-row headers from 2×2 through 2×20, named as total pin count plus
  `dual_row`.
- 2.54 mm female sockets, both single and dual row.
- JST-PH 2.0 mm: 2–6 pins, vertical and right-angle.
- JST-XH 2.5 mm: 2–8 pins.
- JST-SH 1.0 mm: especially 4-pin Qwiic/STEMMA QT and the existing 9-pin part.
- JST-GH 1.25 mm: 4–10 pins for compact robotics/autopilot projects.
- USB Micro-B, USB Mini-B, and exact USB-C 6/12/16/24-pin receptacle variants.
- 3.5 mm and 5.08 mm screw terminals, 2–6 positions.
- 2.1 mm DC barrel jack, common battery connectors, and common FFC/FPC pitches.
- 2×3 AVR ISP, 2×5 ARM Cortex debug, and 2×10 IDC/JTAG headers.

## Recommended implementation order

1. Resolve the Priority 0 list with the browser and add exact datasheets/pinouts.
2. Add generic transistor, MOSFET, diode, switch, inductor, and op-amp
   populators; these are currently the largest taxonomy gaps.
3. Add the common power/analogue set and their exact manufacturer variants.
4. Add dual-row and JST connector families with nested pin-count loops.
5. Add logic/memory families, then controllers and sensors as exact parts.
6. Import two or three more modern KiCad open-hardware projects and use their
   unmatched queues to decide the next batch instead of expanding speculatively.

For every exact component, record the manufacturer part number, supplier part
number when confidently matched, pin names/types, package dimensions, source
URL, and a browser-downloaded datasheet. Generic passives and generic connector
families can remain deliberately light-weight.

