# TI SOIC-8 timer and supervisor marking evidence

Reviewed 2026-11-19. Each exact source record names Texas Instruments, uses
`Package_SO:SOIC-8_3.9x4.9mm_P1.27mm`, and gives body length 4.9 mm and
width 3.9 mm without a height field. Manufacturer package tables list:

| Catalogue ID | Exact part | TI marking | Manufacturer source |
| --- | --- | --- | --- |
| `electronic_ic_power_management_shunt_regulator_soic_8_texas_instruments_tlv431aidr` | TLV431AIDR | `TY431A` | [TI TLV431 datasheet](https://www.ti.com/lit/ds/symlink/tlv431.pdf), package option addendum page 29 |
| `electronic_ic_power_management_voltage_supervisor_5_volt_soic_8_texas_instruments_tl7705bidr` | TL7705BIDR | `7705BI` | [TI TL7705B datasheet](https://www.ti.com/lit/ds/symlink/tl7705b.pdf), package option addendum page 17 |
| `electronic_ic_timer_555_precision_timer_soic_8_texas_instruments_sa555dr` | SA555DR | `SA555` | [TI SA555 datasheet](https://www.ti.com/lit/ds/symlink/sa555.pdf), package option addendum page 21 |
| `electronic_ic_timer_555_precision_timer_soic_8_texas_instruments_tlc555cdr` | TLC555CDR | `TL555C` | [TI TLC555 datasheet](https://www.ti.com/lit/ds/symlink/tlc555.pdf), package option addendum |
| `electronic_ic_timer_555_precision_timer_soic_8_texas_instruments_tlc555idr` | TLC555IDR | `TL555I` | [TI quality report](https://www.ti.com/quality-reliability-packaging-download/es-mx/report?opn=TLC555IDR) |

These are research candidates, not renders. Check each individual manufacturer
D0008A outline, selected model hash and pin-one before staging. A manufacturer
maximum is not a source height: retain the missing-field disclosure. TI supports
the exact strings but not their typeface, placement, logo or production lot/date
for an individual device; mark appearance as illustrative. No PDF was downloaded.

Individual D0008A outlines checked: [TLV431](https://www.ti.com/lit/ds/symlink/tlv431.pdf)
page 46, [TL7705B](https://www.ti.com/lit/ds/symlink/tl7705b.pdf) page 23,
[SA555](https://www.ti.com/lit/ds/symlink/sa555.pdf) page 30, and
[TLC555](https://www.ti.com/lit/ds/symlink/tlc555.pdf) D0008A package outline.
Each lists 4.81–5.00 mm body length, 3.81–3.98 mm body width, 5.80–6.19 mm
lead span and 1.75 mm maximum seated height. The previously reviewed KiCad
SOIC-8 model has nominal 6.0 x 4.9 x 1.75 mm overall bounds within those limits.
The source records omit height; maximum does not imply a measured source value.
Recheck pin-one and individual text visually before publication.
