# TI SOIC-8 power IC marking and package evidence

Reviewed 2026-11-19. The exact catalogue records name Texas Instruments, the
KiCad `Package_SO:SOIC-8_3.9x4.9mm_P1.27mm` machine footprint and 4.9 x
3.9 mm body dimensions; all omit a source height.

| Catalogue ID | Exact part | TI marking | Manufacturer source |
| --- | --- | --- | --- |
| `electronic_ic_power_management_shunt_regulator_soic_8_texas_instruments_tl431aidr` | TL431AIDR | `431AI` | [TI TL431 datasheet](https://www.ti.com/lit/ds/symlink/tl431.pdf), package option addendum page 36; D0008A outline page 67 |
| `electronic_ic_power_management_shunt_regulator_soic_8_texas_instruments_tl431cdr` | TL431CDR | `TL431C` | [TI TL431 datasheet](https://www.ti.com/lit/ds/symlink/tl431.pdf), package option addendum; D0008A outline page 67 |
| `electronic_ic_power_management_current_mode_pwm_controller_soic_8_texas_instruments_ucc38c40dr` | UCC38C40DR | `38C40` | [TI UCC38C40 datasheet](https://www.ti.com/lit/ds/symlink/ucc38c40.pdf), package option addendum page 45; D0008A outline page 56 |

Each D0008A outline gives 4.81–5.00 mm body length, 3.81–3.98 mm width,
5.80–6.19 mm lead span and 1.75 mm maximum seated height. The previously
reviewed KiCad SOIC-8 model's 6.0 x 4.9 x 1.75 mm overall bounds fit these
limits; 1.75 mm is a manufacturer maximum, not a supplied source height. Check
source identity, model hash, pin-one and each marking when staging and rendering.
These are candidates only; typography, logo, placement and lot/date data remain
illustrative. No manufacturer PDF was downloaded.

Additional verified candidate:

| Catalogue ID | Exact part | TI marking | Manufacturer source |
| --- | --- | --- | --- |
| `electronic_ic_power_management_current_mode_pwm_controller_soic_8_texas_instruments_ucc2802dtr` | UCC2802DTR | `UCC2802` | [TI UCC2800 datasheet](https://www.ti.com/lit/ds/symlink/ucc2800.pdf), package option addendum page 42; D0008A outline page 51 |

This source record identifies TI, the same SOIC-8 machine footprint, 4.9 x
3.9 mm body dimensions and no height. The manufacturer D0008A outline gives the
same ranges and 1.75 mm maximum described above. Preserve the source-height
omission and do not invent typography, layout or lot/date markings.
