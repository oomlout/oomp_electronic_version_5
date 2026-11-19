# TI SOIC-8 driver and interface marking evidence

Reviewed 2026-11-19. Each current source record names Texas Instruments, uses
`Package_SO:SOIC-8_3.9x4.9mm_P1.27mm` for machine soldering, and gives body
length 4.9 mm and width 3.9 mm. None specifies source height. The links document
exact package markings; they do not prove layout, font, logo or production date.

| Catalogue ID | Exact orderable part | Manufacturer marking | TI source |
| --- | --- | --- | --- |
| `electronic_ic_driver_dual_peripheral_driver_soic_8_texas_instruments_sn75453bdr` | SN75453BDR | `75453B` | [TI quality report](https://www.ti.com/quality-reliability-packaging-download/de-de/report?opn=SN75453BDR) |
| `electronic_ic_driver_peripheral_driver_soic_8_texas_instruments_sn75451bdr` | SN75451BDR | `75451B` | [TI SN75451B datasheet](https://www.ti.com/lit/ds/symlink/sn75451b.pdf), package option addendum |
| `electronic_ic_interface_rs485_rs422_transceiver_soic_8_texas_instruments_sn75176bdr` | SN75176BDR | `75176B` | [TI quality report](https://www.ti.com/quality-reliability-packaging-download/es-mx/report?opn=SN75176BDR) |
| `electronic_ic_interface_rs_485_transceiver_soic_8_texas_instruments_sn65hvd3082edr` | SN65HVD3082EDR | `VP3082` | [TI SN65HVD3082E datasheet](https://www.ti.com/lit/ds/symlink/sn65hvd3082e.pdf), package option addendum |

The sources distinguish the SOIC-8 markings from other package variants; never
infer top text from the orderable part number. These are research candidates,
not generated renders. Check each individual manufacturer D0008A drawing,
model hash, dimensions and pin-one convention before staging. Disclose the
missing source height and approximate appearance. No PDF was downloaded.

Individual D0008A manufacturer outline checks (page numbers are PDF pages):
[SN75453B](https://www.ti.com/lit/ds/symlink/sn75453b.pdf) page 26,
[SN75451B](https://www.ti.com/lit/ds/symlink/sn75451b.pdf) page 28,
[SN75176B](https://www.ti.com/lit/ds/symlink/sn75176b.pdf) page 25 and
[SN65HVD3082E](https://www.ti.com/lit/ds/symlink/sn65hvd3082e.pdf) page 33.
Each specifies 4.81–5.00 mm body length, 3.81–3.98 mm body width, 5.80–6.19 mm
lead span and 1.75 mm maximum seated height. The reviewed KiCad SOIC-8 model's
nominal 6.0 x 4.9 x 1.75 mm overall bounds fit these limits. The model is an
illustration; individual source height is still unspecified and pin-one and
markings must be checked in each result before publication.
