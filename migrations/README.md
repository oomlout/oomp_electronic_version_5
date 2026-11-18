# IC package-last naming

The 2026-11-15 migration changes all 600 existing IC definitions and component
directories to this order:

| Level | Meaning |
| --- | --- |
| 1 | `electronic` |
| 2 | `ic` |
| 3 | Function, such as `amplifier` |
| 4 | Subtype and functional qualifiers |
| 5 | Physical package, such as `sot_23_5` |
| 6–13 | Empty |
| 14 | Manufacturer |
| 15 | Manufacturer part number |

`ic_package_last_ids.json` records the complete one-to-one rename and old/new
MD5, short codes and three-word BIP39 labels. Its `old` values are intentional
historical identifiers, not active component paths. The current canonical ID
is the input to the normal OOMP hashing convention. `component_identity.py`
discards historical seeds and recomputes the fields from that ID. A rename
therefore changes printed labels and footprint marks; refresh their previews
alongside the data. Canonical IDs, links, source records, KiCad library names,
category navigation and project catalog references all use the new names.

The project repository carries its own package reader and frozen component
records. Its catalog manifest records this migration while retaining the
original snapshot provenance. Neither repository needs to import the other
at runtime. Saved board geometry and fabrication outputs are not regenerated.

Future ingestion must use `component_taxonomy.validate_ic_taxonomy` and
`package_token`. Extend the documented function set when a genuinely new IC
function is needed. Population validates before creating component records,
and computes canonical identity codes before writing records or executing
drawing actions. Keep the map as migration provenance.

Regression checks are in `kicad_agents/tests/test_ic_taxonomy.py`; run them with
`python tools/run_component_tests.py -q kicad_agents/tests/test_ic_taxonomy.py`.
The project repository tests its independent package reader and compiled
matching index in `tests/test_matching_index.py`.

## PH header family migration

`ph_header_ids.json` maps the five formerly generic `connector/ph` IDs to the
exact BOOMELE headers under `connector/jst_ph`, with each MPN and JLCPCB code.
The manufacturer drawings and distributor captures move with the part.
Existing component folders retain a README linking to the new canonical ID.
Use the canonical ID for new references and labels.
