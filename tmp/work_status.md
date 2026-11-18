# Session work status (updated as stages complete)

## Overall user request (2026-09-06)
1. Add LCSC + manufacturer part numbers to all existing components (683 missing; 675 queued in tmp/lcsc_queue.json — breadboards + jumper bundles intentionally skipped, mounting holes are board features).
2. Run unmatched checker, then add unmatched components one by one.
3. Follow report/unmatched_components_plan.md EXCEPT LED filament.
4. Add right-angle 2.54mm headers — BOTH plastic-on-short-pin-side and plastic-on-long-pin-side variants, with a good naming scheme.
5. Add PH 2.00mm: THT straight + THT right angle + SMD straight (exists: B8B-PH-SM4 vertical) + SMD right angle (S8B-PH-SM4-TB).
6. Add XH 2.50mm: THT straight (exists B2B-XH-A) + THT right angle (S2B-XH-A). XH SMD: JST does not make one — verify on LCSC, note in report.

## Done
- tmp/lcsc_queue_builder.py -> tmp/lcsc_queue.json (675 entries; categories: resistor 1199, MLCC 1142, THT resistor 1203, arrays 1200, LED 412, others MPN search).
- tmp/lcsc_harvest.cjs resumable Playwright harvester -> tmp/lcsc_results.jsonl. MPN from a[href*=product-detail] anchor with text != code.
- action_unmatched_component_check.py run -> report/unmatched_components.yaml (1588 instances, 46 projects, plan file predates new projects).
- LCSC backfill of all existing parts turned out needed for ~683 (harvest running).

## Pending pipeline
- After harvest: tmp/lcsc_apply.py (to write) converts results -> populate extra files per family (format: see working_oomp_populate_resistor_extra.py: part["manufacturer"], part_number_manufacturer, part_number_lcsc, product_url, part_numbers_lcsc[3], part_numbers_manufacturer[3], research_notes).
- Then compile stage (working_oomp.main) bakes working.yaml; tests; preview regen not needed (no svg changes).

## Progress update (later 2026-09-06)
- Matcher final: _is_board_feature excludes buzzard/kibuzzard, fiducials, standoffs, test points, logos, SMD jumper traces; e-radionica HEADER_MALE_NX1/HEADER-UPDI and PinHeader_2xNN dual-row headers infer connector_header; KNOWN_PART_ALIASES for pesd0402/ss14/bat54w/1ss400 (no-MPN only, word-bounded). All MatchingAgentTests pass.
- Matching regen ran once mid-edit (results stale); rerunning with final matcher.
- New connector parts CREATED (1163 parts total now):
  * working_oomp_populate_connector_families_data.py (139 rows: JST PH THT vertical B2B-PH-K-S 2-16, PH THT RA S2B-PH-K-S 2-16, PH SMD RA S..B-PH-SM4-TB 2-14, XH THT RA S..B-XH-A 2-16, 2.54 RA headers 1-40 short_pin + long_pin, dual_row_6_pin)
  * naming: right_angle_short_pin = plastic on short-pin side (KiCad Horizontal master); right_angle_long_pin = plastic on long-pin side (body mirrored across pin row)
  * wiring: populate_connector.py options + populate_connector_extra.py extras; populate stage = `python working_oomp_populate.py` (writes parts_source) THEN `working_oomp.main()` (creates parts/) — compile alone does NOT create new parts!
- LCSC queue2 appended to tmp/lcsc_queue.json (total 815): JST series MPN pages (B2B-PH-K-S etc.), header_ra per-count queries, dual-row, XH-SMD existence probe.
- tmp/lcsc_apply.py converts results -> tmp/lcsc_applied.json (kind-specific filters, word-boundary matching). Old-LED results must be re-harvested (queries were wrong).
- Plan populate gaps (18/27pF 0402, 2.4k 0402, 16MHz 3225, 5032 8MHz, 3215 32.768k, 2.2mm holes) ALL already exist.

## Later update 2
- New unmatched parts CREATED and compiled (parts=1205): ATTINY404, TPS613222A, LM393, RT9080, OPA344, SI7211/SI7201, HX711, M4 SMA rectifier, generic schottky 0402, dual-NMOS sot_363, generic NPN sot_23, MMBT4403, inductor 0806 2.2uH, DSHP03TS-S slide switch, MQ sensor family, TCRT5000L, AM312, APDS-9960, TC33X trimmer (new potentiometer family), easyC SM04B-GH-TF, U.FL, SMA edge, KF235 terminal, CR1220 holder, caps 0805 4.7/22uF, 0603 22uF, 0402 33pF, 1206 10uF, resistors 300/20000 all sizes.
- working_oomp_populate_lcsc_research_data.py (521 rows) + working_oomp_populate_lcsc_extra.py registered at END of working_oomp_populate_extra_detail.main().
- Tantalum capacitor proposal rule added (kemet/eia/tantal evidence -> {size}_avx_a_tantalum_{cap}_{10|16}_volt).
- Matcher aliases now cover ~40 exact values/MPNs (see KNOWN_PART_ALIASES).
- Still to do: final harvest wave finishing (LEDs + queue2 + queue3) -> rerun tmp/lcsc_emit.py -> populate+compile -> final regen_matching -> checker -> svg stage for new parts -> tests. Stragglers with rows=0 need query fixes (2n7002, ws2812b, arrays, 0201 8.2M).
