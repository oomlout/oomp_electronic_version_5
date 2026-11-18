# Duplicate listing audit

Audit date 2026-11-16. Corrected purchasing metadata and catalogue relationships on 2026-11-16. The findings below retain the original audit evidence.

Paused at the user's request after saving the repairs. See the [resume checkpoint](duplicate_listing_repair_resume.md) for pending final tests.

## Repair outcome

- Quarantined all 35 rejected research assignments in the authoritative LCSC table with reasons and evidence URLs. Removed their active supplier links from the 31 JST headers, two capacitor sizes and two custom black Qwiic entries.
- Confirmed the KNSCHA dimensions against its [manufacturer specification, page 1](https://xonstorage.z8.web.core.windows.net/pdf/knscha_rvt220uf10v67rv0037_apr22_xonlink.pdf). The two generic capacitor sizes remain distinct and have no unsupported purchasing identity.
- Added verified SparkFun SKU links for both black Qwiic parts and explicit colour-specific display names. Standard JST entries retain their original supplier mappings.
- Restored the two 2 kOhm resistor population rows. The population now contains 3,062 unique IDs, matching the source and generated directory sets.
- Classified the eleven terminal-block pairs as generic versus exact entries and linked them in both directions. Their pages explicitly require dimensional review before substitution. These are catalogue relationships, not verified compatibility links.
- Added supplier identity/category/custom-variant rejection checks, regression tests, and ingestion instructions. Updated only the 59 affected component records and their required outputs.

Remaining evidence gaps are explicit on the affected pages. Exact replacement LCSC listings remain unverified for 31 JST headers and two capacitor sizes. Terminal-block interchangeability remains unverified. No IDs were merged or retired, so existing links and physical identity codes remain valid. Missing local datasheets reported by the existing generation recipes were not represented as captured documents.

## Scope and method

Enumerated 3,060 population IDs without running catalogue generation. All IDs were unique. Compared source and generated directory identities, each containing 3,062 records. Read all 3,012 electronic source YAML records and matched primary and alternative manufacturer part numbers, normalized manufacturer names, punctuation-normalized part numbers, and LCSC/JLCPCB codes. The remaining 50 source records are mechanical mounting holes and were outside the electronic purchasing-identity scan. Generated metadata and render contents were not individually audited.

Found 12 repeated manufacturer/part-number groups and eight repeated distributor-code groups. Reviewed connector taxonomy overlap separately, retaining finish, wire gauge, colour and other regular taxonomy fields. Exact identity matching cannot detect every duplicate when purchasing data is absent or incorrect.

## Findings and proposed corrections

### 1. Incorrect supplier assignment across 31 JST headers

Fifteen PH surface-mount vertical headers, 2–16 positions, and sixteen XH through-hole headers, 2–16 and 20 positions, all carry C2875161. Their stored supplier description is an ESD diode. The [LCSC listing](https://www.lcsc.com/product-detail/C2875161.html) identifies TECH PUBLIC ESD9X5V, a DFN1006-2 protection diode. These are distinct connector designs with a shared incorrect purchasing reference.

The assignment is durable in [LCSC research data](../working_oomp_populate_lcsc_research_data.py). The [merge function](../working_oomp_populate_lcsc_extra.py) preserves an existing manufacturer identity while adding a missing supplier code from the research row, allowing contradictory identities to coexist. Correct or quarantine the bad research rows and their supplier fields, then research exact replacements. Add a merge check that rejects incompatible manufacturer/MPN/category evidence. Retain each connector position count.

### 2. One capacitor purchasing identity assigned to two case sizes

Both records use KNSCHA RVT220UF10V67RV0037 and C2833309 as their primary purchase identity, despite different case-size taxonomy. The [LCSC listing](https://www.lcsc.com/product-detail/C2833309.html) currently reports D6.3xL5.4 mm, which disagrees with both stored taxonomy heights. This establishes a purchasing conflict but does not establish which record should survive. Inspect the exact manufacturer drawing before changing dimensions, replacing a supplier selection, or merging IDs.

- [electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_220_micro_farad_10_volt](../parts_source/electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_220_micro_farad_10_volt/working.yaml)
- [electronic_capacitor_8_mm_diameter_6_5_mm_tall_electrolytic_220_micro_farad_10_volt](../parts_source/electronic_capacitor_8_mm_diameter_6_5_mm_tall_electrolytic_220_micro_farad_10_volt/working.yaml)

### 3. Two black Qwiic entries share purchasing references with standard JST entries

The right-angle pair shares SM04B-SRSS-TB / C160404, and the vertical pair shares BM04B-SRSS-TB / C160390. SparkFun explicitly describes its [PRT-14417 horizontal connector](https://www.sparkfun.com/qwiic-jst-connector-smd-4-pin-horizontal.html) and [PRT-16766 vertical connector](https://www.sparkfun.com/qwiic-jst-connector-smd-4-pin-vertical.html) as custom black versions of these JST designs. Colour variants are intentional. The current evidence does not establish that the shared LCSC codes supply the custom black versions. Anchor black purchasing references to their verified SparkFun SKUs and verify any claimed alternative independently.

- [electronic_connector_jst_sh_1_mm_pitch_surface_mount_right_angle_4_pin_black_jst_sm04b_srss_tb](../parts_source/electronic_connector_jst_sh_1_mm_pitch_surface_mount_right_angle_4_pin_black_jst_sm04b_srss_tb/working.yaml)
- [electronic_connector_jst_sh_1_mm_pitch_surface_mount_right_angle_4_pin_jst_sm04b_srss_tb](../parts_source/electronic_connector_jst_sh_1_mm_pitch_surface_mount_right_angle_4_pin_jst_sm04b_srss_tb/working.yaml)
- [electronic_connector_jst_sh_1_mm_pitch_surface_mount_vertical_4_pin_black_jst_bm04b_srss_tb](../parts_source/electronic_connector_jst_sh_1_mm_pitch_surface_mount_vertical_4_pin_black_jst_bm04b_srss_tb/working.yaml)
- [electronic_connector_jst_sh_1_mm_pitch_surface_mount_vertical_4_pin_jst_bm04b_srss_tb](../parts_source/electronic_connector_jst_sh_1_mm_pitch_surface_mount_vertical_4_pin_jst_bm04b_srss_tb/working.yaml)

### 4. Two retained resistor records are absent from the population

These exist in both source and generated trees but are absent from the current population ID set. They are stale-definition candidates, not confirmed duplicate resistors. Decide whether to restore explicit population rows or retire them after checking references. Editing generated files alone would leave the inconsistency unresolved.

- [electronic_resistor_0201_2000_ohm](../parts_source/electronic_resistor_0201_2000_ohm/working.yaml)
- [electronic_resistor_quarter_watt_through_hole_2000_ohm](../parts_source/electronic_resistor_quarter_watt_through_hole_2000_ohm/working.yaml)

### 5. Eleven generic/exact terminal-block overlaps need explicit relationships

For each 2–12-position green 3.5 mm terminal block, a generic screw-terminal entry and a 4UCON 1443 entry share regular taxonomy and the same KiCad footprint. The generic research notes describe a DORABO/exemplar style while the exact entries identify 4UCON items 19696–19706. Shared drawing defaults and footprint names do not prove identical physical products. Preserve them pending dimension review, then explicitly link generic alternatives or retire genuinely redundant placeholders. The colour-unspecified generic terminal blocks and 5 mm generic/4UCON families also warrant a future modelling review rather than automatic merging.

Population definitions are in [working_oomp_populate_connector.py](../working_oomp_populate_connector.py), with shared drawing and footprint defaults in [working_oomp_populate_connector_extra.py](../working_oomp_populate_connector_extra.py).

- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_2_pin_green_4ucon_technology_19696](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_2_pin_green_4ucon_technology_19696/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_2_pin_green_screw_terminal_1x02_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_2_pin_green_screw_terminal_1x02_p3_5_mm_green/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_3_pin_green_4ucon_technology_19697](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_3_pin_green_4ucon_technology_19697/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_3_pin_green_screw_terminal_1x03_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_3_pin_green_screw_terminal_1x03_p3_5_mm_green/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_4_pin_green_4ucon_technology_19698](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_4_pin_green_4ucon_technology_19698/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_4_pin_green_screw_terminal_1x04_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_4_pin_green_screw_terminal_1x04_p3_5_mm_green/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_5_pin_green_4ucon_technology_19699](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_5_pin_green_4ucon_technology_19699/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_5_pin_green_screw_terminal_1x05_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_5_pin_green_screw_terminal_1x05_p3_5_mm_green/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_6_pin_green_4ucon_technology_19700](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_6_pin_green_4ucon_technology_19700/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_6_pin_green_screw_terminal_1x06_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_6_pin_green_screw_terminal_1x06_p3_5_mm_green/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_7_pin_green_4ucon_technology_19701](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_7_pin_green_4ucon_technology_19701/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_7_pin_green_screw_terminal_1x07_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_7_pin_green_screw_terminal_1x07_p3_5_mm_green/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_8_pin_green_4ucon_technology_19702](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_8_pin_green_4ucon_technology_19702/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_8_pin_green_screw_terminal_1x08_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_8_pin_green_screw_terminal_1x08_p3_5_mm_green/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_9_pin_green_4ucon_technology_19703](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_9_pin_green_4ucon_technology_19703/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_9_pin_green_screw_terminal_1x09_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_9_pin_green_screw_terminal_1x09_p3_5_mm_green/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_10_pin_green_4ucon_technology_19704](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_10_pin_green_4ucon_technology_19704/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_10_pin_green_screw_terminal_1x10_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_10_pin_green_screw_terminal_1x10_p3_5_mm_green/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_11_pin_green_4ucon_technology_19705](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_11_pin_green_4ucon_technology_19705/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_11_pin_green_screw_terminal_1x11_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_11_pin_green_screw_terminal_1x11_p3_5_mm_green/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_12_pin_green_4ucon_technology_19706](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_12_pin_green_4ucon_technology_19706/working.yaml)
- [electronic_connector_terminal_block_3_5_mm_pitch_through_hole_12_pin_green_screw_terminal_1x12_p3_5_mm_green](../parts_source/electronic_connector_terminal_block_3_5_mm_pitch_through_hole_12_pin_green_screw_terminal_1x12_p3_5_mm_green/working.yaml)

## Reviewed matches that do not justify merging

| Match | Interpretation |
| --- | --- |
| C23733, C1591, C96446, C1592 | Four generic capacitor entries include alternatives also represented by more specific records. Primary preferred selections differ. Voltage, tolerance and exact-manufacturer distinctions must survive. |
| FOJAN TS, 36 records | A series-like token is stored as the manufacturer part number across different resistor values and supplier codes. Obtain full order codes. |
| HWA CHN CNTO, 2 records | Incomplete manufacturer identity across distinct resistor records. |
| CCO T, 27 records | A series-like token is insufficient to establish identity. |
| TyoHM T/B, 2 records | Incomplete manufacturer identity across distinct resistor records. |
| Changjing D882(RANGE:160-320), 2 records | SOT-89-3/C9634 and TO-126/C2152 have different packages and recorded pin orders. Keep separate. |
| JST PH versus BOOMELE PH, 5 pairs | Different manufacturers and exact order codes. Family compatibility is not purchasing identity. |
| JST XH versus BOOMELE XH, 3 pairs | Different manufacturers and exact order codes. Correct the JST supplier errors independently. |
| 2 mm 40-pin and 80-pin header pairs | Male versus female products with different MPNs and supplier codes. Taxonomy should make gender clearer. |
| SH housings and crimp variants | Protrusions, gauge ranges and finishes distinguish variants. Similar names alone do not justify merging. |

## Recommended repair order

1. Quarantine or correct the 31 diode-to-header supplier mappings in authoritative research data and affected records.
2. Resolve the capacitor package evidence and assign each retained size the correct purchasing identity.
3. Separate black Qwiic procurement from standard JST procurement.
4. Resolve the two orphan resistor definitions and explicitly link generic/exact terminal-block alternatives.
5. Add identity checks that distinguish primary identities from alternatives and compare package, colour, finish and manufacturer before flagging duplicates. Treat short resistor series tokens as incomplete evidence.

Any eventual ID retirement should update reciprocal compatibility links, saved component records, population data and necessary indexes, preserving an alias or migration mapping where appropriate. Regenerate only affected components after approved data corrections.

## Complete affected JST header list

- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_10_pin_jst_b10b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_10_pin_jst_b10b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_11_pin_jst_b11b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_11_pin_jst_b11b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_12_pin_jst_b12b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_12_pin_jst_b12b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_13_pin_jst_b13b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_13_pin_jst_b13b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_14_pin_jst_b14b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_14_pin_jst_b14b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_15_pin_jst_b15b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_15_pin_jst_b15b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_16_pin_jst_b16b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_16_pin_jst_b16b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_2_pin_jst_b2b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_2_pin_jst_b2b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_3_pin_jst_b3b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_3_pin_jst_b3b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_4_pin_jst_b4b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_4_pin_jst_b4b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_5_pin_jst_b5b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_5_pin_jst_b5b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_6_pin_jst_b6b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_6_pin_jst_b6b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_7_pin_jst_b7b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_7_pin_jst_b7b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_8_pin_jst_b8b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_8_pin_jst_b8b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_9_pin_jst_b9b_ph_sm4_tb](../parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_vertical_9_pin_jst_b9b_ph_sm4_tb/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_10_pin_jst_b10b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_10_pin_jst_b10b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_11_pin_jst_b11b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_11_pin_jst_b11b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_12_pin_jst_b12b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_12_pin_jst_b12b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_13_pin_jst_b13b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_13_pin_jst_b13b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_14_pin_jst_b14b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_14_pin_jst_b14b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_15_pin_jst_b15b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_15_pin_jst_b15b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_16_pin_jst_b16b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_16_pin_jst_b16b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_20_pin_jst_b20b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_20_pin_jst_b20b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_2_pin_jst_b2b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_2_pin_jst_b2b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_3_pin_jst_b3b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_3_pin_jst_b3b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_4_pin_jst_b4b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_4_pin_jst_b4b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_5_pin_jst_b5b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_5_pin_jst_b5b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_6_pin_jst_b6b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_6_pin_jst_b6b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_7_pin_jst_b7b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_7_pin_jst_b7b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_8_pin_jst_b8b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_8_pin_jst_b8b_xh_a/working.yaml)
- [electronic_connector_jst_xh_2_5_mm_pitch_through_hole_9_pin_jst_b9b_xh_a](../parts_source/electronic_connector_jst_xh_2_5_mm_pitch_through_hole_9_pin_jst_b9b_xh_a/working.yaml)

## Machine-readable evidence

All repeated manufacturer/part-number and supplier-code groups, orphan IDs, and terminal-block candidate pairs are listed in [duplicate_listing_audit_2026_11_16.json](duplicate_listing_audit_2026_11_16.json). This is an audit snapshot, not a list of parts approved for merging.
