# TO-252 shared family evidence for display renders

Reviewed 2026-11-21. These are display approximations, not manufacturing models.
The exact TO-252 records listed below do not contain their own local PDFs. The
existing PDFs remain in the sibling TO-251 source records; they were neither
copied nor downloaded for these renders.

| Orderable | Existing family PDF under `parts_source` | SHA-256 |
| --- | --- | --- |
| IRFR120NTRPBF | `electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_100_volt_9_4_amp_infineon_technologies_irfu120npbf/datasheet.pdf` | `83dc4858004a978949d3e5581a73af82953b8b90c6549b72f88c278bbf8506d9` |
| IRFR220NTRPBF | `electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_200_volt_5_amp_infineon_technologies_irfu220npbf/datasheet.pdf` | `7b8b6e32281bb5b9d3dfde103740646d3ca80293b6efbe9e0f637b920e5af154` |
| IRLR024NTRPBF | `electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_55_volt_17_amp_infineon_technologies_irlu024npbf/datasheet.pdf` | `ff52b6382c5eabdd1e267f1d4cbdf0fbbd81d4a4854a20efdd77225fdae3ed4a` |
| IRFR5410TRPBF | `electronic_transistor_to_251_mosfet_p_channel_enhancement_mode_100_volt_13_amp_infineon_technologies_irfu5410pbf/datasheet.pdf` | `89490495713f68cfef9d64778bfcba51014763eca5762c87f3edca55c5097228` |
| MJD45H11G | `electronic_transistor_to_251_bipolar_npn_80_volt_8_amp_onsemi_mjd44h11_1g/datasheet.pdf` | `4f95f0add038033491b7bc1c6a5db1e24b409d5572cc6ec42f1b33438a5d6176` |

Each International Rectifier family sheet's page 8 was visually reviewed: its
D-Pak TO-252AA drawing shows two full outer leads, a short centre stub and a
metal tab. Its example marking is generic and does not establish the exact
marking for these devices. The rendered partial part numbers are illustrative;
typeface, placement, logo and production codes are not verified. Infineon product
pages independently describe the respective families:
[IRFR120N](https://www.infineon.com/part/IRFR120N),
[IRFR220N](https://www.infineon.com/part/IRFR220N),
[IRLR024N](https://www.infineon.com/part/IRLR024N),
[IRFR5410](https://www.infineon.com/part/IRFR5410).

The onsemi family PDF page 6 lists MJD45H11G in DPAK case 369C; page 7's
visually reviewed drawing shows two outer leads and a short centre stub. Page 1
specifies the fixed marking `J4` / `5H11G`; variable production/date codes are
omitted and the rendered typography and location are approximate.

The KiCad TO-252-2 display model has 9.9 x 6.5 x 2.32 mm overall bounds and
is an approximation of the reviewed shapes; the catalogue's original
TO-252-3_TabPin2 footprint is unchanged. Finishes and the short stub are
approximate. There is no separate local PDF in any of the five target records.
