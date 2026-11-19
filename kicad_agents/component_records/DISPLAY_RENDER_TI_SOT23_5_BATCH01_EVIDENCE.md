# TI SOT-23-5 regulator display render follow-on evidence

The exact orderable-part marking tables in Texas Instruments' TPS763 and TPS793 datasheets identify the following four candidates. DBV0005A is the five-lead SOT-23 outline, with a maximum seated height of 1.45 mm. These catalogue source records list 2.9 × 1.6 mm and omit height. The installed generic KiCad SOT-23-5 model is 1.55 mm tall; like the pilot, its display-only geometry needs vertical scaling to 1.45 mm and the correction must be disclosed. No mechanical or PCB accuracy is implied. Typeface, placement, orientation and manufacturing codes are illustrative.

| Exact local part ID | TI orderable | Marking | Evidence |
|---|---|---|---|
| `electronic_ic_power_management_linear_voltage_regulator_1_8_volt_sot_23_5_texas_instruments_tps76318dbvr` | TPS76318DBVR | `PBAI` | [TPS763 datasheet](https://www.ti.com/lit/gpn/tps763) |
| `electronic_ic_power_management_linear_voltage_regulator_1_8_volt_sot_23_5_texas_instruments_tps79318dbvr` | TPS79318DBVR | `PHHI` | [TPS793 datasheet](https://www.ti.com/lit/ds/symlink/tps793.pdf); [TI device report](https://www.ti.com/quality-reliability-packaging-download/ko-kr/report?opn=TPS79318DBVR) |
| `electronic_ic_power_management_linear_voltage_regulator_2_85_volt_sot_23_5_texas_instruments_tps793285dbvr` | TPS793285DBVR | `PHII` | [TPS793 datasheet](https://www.ti.com/lit/ds/symlink/tps793.pdf) |
| `electronic_ic_power_management_linear_voltage_regulator_3_volt_sot_23_5_texas_instruments_tps79330dbvr` | TPS79330DBVR | `PGYI` | [TPS793 datasheet](https://www.ti.com/lit/ds/symlink/tps793.pdf) |

Checked local manufacturer, exact part number, SOT-23-5 footprint and dimensions on 2026-11-19. Candidates are not yet staged or rendered; independent pilot and shared-pass comparison are prerequisites.
