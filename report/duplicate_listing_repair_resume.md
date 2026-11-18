# Duplicate listing repair checkpoint

Paused at the user's request on 2026-11-16. Resume from the saved changes. No further generation is currently required.

## Completed

- Quarantined 35 incorrect LCSC research assignments in `working_oomp_populate_lcsc_research_data.py`, preserving rejection reasons and evidence URLs.
- Removed the active invalid purchasing fields from 31 JST headers, two capacitor sizes and two custom black Qwiic parts.
- Added supplier manufacturer/MPN/category/custom-variant rejection checks in `working_oomp_populate_lcsc_extra.py`.
- Added SparkFun SKU purchasing links and explicit black Qwiic display names. Standard JST variants remain separate.
- Restored the two existing 2 kOhm resistor population definitions. Population now has 3,062 unique IDs, matching the source/generated directory counts.
- Added reciprocal generic/exact catalogue relationships to 11 terminal-block pairs. Pages explicitly leave physical substitution unverified.
- Updated ingestion instructions, component README template, web display of purchasing/relationship notes and regression tests.
- Compiled all 59 affected components. Refreshed their READMEs, drawer labels and web manifests, and refreshed shared navigation ancestors once. Subsequently refreshed the two Qwiic display names and their leaf navigation pages, plus 13 outline-export titles. These final updates completed successfully.
- Validated source YAML, generated YAML, web metadata and drawer labels for all 59 parts. Rejected codes are absent from active supplier fields and labels. All 22 terminal relationships are reciprocal. No empty purchasing links or broken reciprocal README links were found.
- Verified the corrected capacitor label visually using Inkscape with Arial Narrow. CairoSVG substituted fonts incorrectly, so its preview was discarded as a rendering check.
- Confirmed no component changes outside the 59 affected IDs. No component IDs were merged or retired. No project-repository changes, commits or pushes were made by this repair task.

## Validation completed and remaining

An earlier run passed all 29 tests across `test_purchasing_identity.py`, `test_populate_workflow.py`, `test_crimp_connectors.py` and `test_jst_crimp_connectors.py`. A subsequent run of the then-eight purchasing tests also passed after adding the explicit black display names.

After that, one additional test and the local web-view integration were added. The final command below was still running when the user requested this pause. It was interrupted deliberately and has no final result. Importing `webserver.app` creates the default app and scans the real catalogue before collection, so this run was unusually slow.

```powershell
python -m pytest kicad_agents/tests/test_purchasing_identity.py webserver/tests/test_electronics.py -q
```

On resume

1. Re-run the pending tests above. If collection is still slow, inspect the import-time `app = create_app()` in `webserver/app.py` and the runtime indexing path before deciding how to isolate the test setup. Do not treat the interrupted run as a failure or a pass.
2. Review the final diff and run both `git diff --check` and `git diff --cached --check`. Changes were staged by the end of this session, so preserve the current index and unrelated edits. An earlier whitespace check passed before the final small edits.
3. Check that the audit report and JSON repair status accurately reflect the final test result, then provide the completion summary. Avoid repeating catalogue generation unless a new correction requires it.

## Remaining evidence gaps, already documented on the parts

- Exact replacement LCSC listings remain unverified for 31 JST headers and two capacitor package sizes. Invalid links have been removed; replacements must be researched rather than guessed.
- Dimensional interchangeability of the 11 generic/exact terminal-block pairs remains unverified. Their links are catalogue relationships, not confirmed compatibility.
- Existing generation recipes reported missing local datasheets for some affected JST headers. No PDF capture was claimed or performed in this repair.

## Useful files

- [Audit and repair outcome](duplicate_listing_audit_2026_11_16.md)
- [Machine-readable original audit and repair summary](duplicate_listing_audit_2026_11_16.json)
- `kicad_agents/tests/test_purchasing_identity.py`
- `tmp/duplicate_audit/repair_ids.json` contains the 59 affected IDs.
- `tmp/duplicate_audit/repair_compile.log`, `repair_render.log` and `finish_repair.log` contain successful generation logs.
- `tmp/duplicate_audit/corrected_capacitor_label_inkscape.png` is the inspected label preview.

Temporary files are local aids. Authoritative fixes live in population code and the tracked records, not in the temporary scripts. Preserve the existing scope constraints against whole-catalogue generation, separate-project changes, commits and pushes.
