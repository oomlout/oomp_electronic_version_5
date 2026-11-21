# Header orientation evidence needing follow-up

The source records for 17 and 18 positions select vertical KiCad footprints.
Do not render them as confirmed exact vertical products until their identities
and orientation are reconciled.

* Ckmtw `B-2100S17P-A110`: the exact JLCPCB listing
  https://jlcpcb.com/partdetail/51950723-B_2100S17PA110/C49423291
  inconsistently says SMD right-angle package while its attributes say
  through-hole and specify 6 mm mating / 3 mm tail. The exact orientation
  cannot be resolved from this conflicting listing alone.
* XFCN `PZ254R-11-18P`: the exact secondary listing
  https://www.ickey.cn/brand/35145/079999/3.html identifies the part but gives
  no geometry. Related XFCN PZ254R-11-02P, -04P, -05P, -06P and -08P
  listings describe right-angle headers, e.g.
  https://jlc.com.vn/linh-kien/pin-headers/ and
  https://jlc.com.vn/linh-kien/pin-headers/?page=3 . This suggests a possible
  orientation conflict, but does not prove the 18-position part's geometry.

Neither source has a local datasheet in parts_source. Preserve records and
seek an exact manufacturer drawing or otherwise reliable evidence. No PDF
was downloaded.

## Follow-up: generated part PDF copies reviewed

The generated `parts/.../data/datasheet.pdf` files for both entries are the
same Cankemeng family PDF, SHA-256
`e942aeb6ead33cfe1b159125f66b75ddf7c706f92a218971a789ec760a109b11`.
Pages 1 and 2 identify Cankemeng B-2100SXXP-A110 and explicitly list
B-2100S17P-A110 among the straight through-hole variants. The drawing
therefore resolves the 17-position orientation despite the inconsistent
JLCPCB package field. The 18-position PDF is the same Cankemeng drawing,
not the XFCN PZ254R-11-18P manufacturer drawing; it cannot resolve the
18-position record. The copies exist in `parts`, not `parts_source`.
