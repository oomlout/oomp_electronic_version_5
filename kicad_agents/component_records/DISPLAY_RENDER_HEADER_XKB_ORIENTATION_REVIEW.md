# XKB connector orientation review

The 23- through 27-position source records select vertical footprints and
their generated parts folders contain the same Cankemeng family PDF, not
an XKB drawing (SHA-256
`e942aeb6ead33cfe1b159125f66b75ddf7c706f92a218971a789ec760a109b11`).
Do not treat that PDF as manufacturer evidence for these XKB records.

For the exact 23-position MPN X6511WR-23H-C60D30R2, the independent
Adom listing https://wiki.adom.inc/adom/x6511wr-23h-c60d30r2/files/README.md
identifies a horizontal KiCad footprint; this conflicts with this catalogue's
vertical footprint and needs manufacturer confirmation. For the exact 24-pin
X6511WR-24H-C60D30R1, Holtek's reference design
https://www.holtek.com/webapi/5905185/WAS-24B1EN_ReferenceDesign.pdf
associates it with `HDR-TH_24P-P2.54-H-M-W7.7-P`, also suggesting a horizontal
part. These external sources are supporting clues, not manufacturer drawings.
Do not infer orientation for other variants solely from similar part numbers.
Preserve source data and acquire or inspect exact XKB manufacturer evidence
before rendering an asserted exact match. No PDF was downloaded.

## Exact 23-position drawing link located

The Adom source links the exact XKB product's one-page manufacturer PDF at
https://jlcpcb.com/api/file/downloadByFileSystemAccessId/8588892982900895744 .
The read-only web view exposed a one-page PDF but no extractable text or
visible drawing through the available tool, so it has not been visually
reviewed or saved. Do not claim manufacturer confirmation on this basis.
