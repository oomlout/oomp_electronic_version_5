# Infineon TO-220AB MOSFET display research

Five catalogue parts identify Infineon Technologies and TO-220-3 vertical.
Their existing local International Rectifier PDFs were reviewed: page 1 text
for device identification and page 8 visually for package drawings and markings.

| Catalogue orderable | Local PDF SHA-256 | Marking evidence |
| --- | --- | --- |
| IRF3710PBF | `e9cabee1fb9fd6c2a644d608110a87f9da85484ae3273ddde924bcbe9ede122c` | example depicts unrelated IRF1010 |
| IRFB4610PBF | `3c56daa544b01b32583558fe60d97bd60512809ad822ca990ce4b790ecdfb11f` | example depicts unrelated IRF1010 |
| IRFB4710PBF | `04f485c77f19e9cd61f58e097928b9590aa85a6c945cfa8a375bdd4a91715b55` | example depicts unrelated IRF1010 |
| IRFB4410PBF | `135db9a33c1a1df1604acc3a34f27809215d24691e09128e6cb3ecae4215d230` | local PDF names IRFB4410 without PbF suffix; example depicts IRF1010 |
| IRFB4410ZPBF | `a9dbc9f677efadc125b70e9116993ecf292751b1142c3ebd8cf5ac7a7ad4a16f` | page 8 illustrates **FB4410Z** for the device family |

The KiCad TO-220-3 model used for display has 10.25 x 4.455 x 28.525 mm
overall bounds, including the leads. Its body-to-tip projection is approximately
13.435 mm. The IRFB4710 drawing specifies 13.47–14.09 mm, so the model is
about 0.035 mm below its lower limit; for the other reviewed drawings, lead
proportions remain approximate. The source catalogue dimensions are generic.
None of these renders is verified mechanical CAD or a PCB footprint.

For IRFB4410Z, `FB4410Z` follows the manufacturer's family marking example;
the font, layout, logo and changing lot/date codes remain approximate. For the
other devices use the device identifier as illustrative: their examples do not
establish the exact top marking. The IRFB4410 PbF orderable suffix is not
independently confirmed by its local PDF and must remain disclosed.
