# Validation log

24 September 2026:

- Captured and normalized 2,004 unique C-numbers; 1,586 active and 418 retired.
- Verified 351 Basic and 1,235 Preferred/Promotional Extended active candidates.
- Evaluated actual populate functions with their writer intercepted; no generated
  component files were written by catalogue preparation.
- Tested `next --code C25804` and `status` with the original single-pass queue.
- The original six tests passed: capture coverage, malformed/duplicate capture rejection,
  unit conversion, idempotent preference with preserved alternatives and JLC
  link generation, exact-identity protection, and rejection of unverified intake.
- Combined new tests and `test_populate_workflow`: 16 passed, one existing
  environment-dependent failure. `test_missing_source_file_does_not_create_file_copy_action`
  assumes `parts_source/electronic_connector_jst_ph_2_mm_pitch_surface_mount_right_angle_10_pin_jst_s10b_ph_sm4_tb/datasheet.pdf`
  is absent. That 103,369-byte PDF exists, with a 7 September modification date,
  so the unchanged generator correctly schedules its copy. No test/data deletion
  was performed to hide this failure.

24 September 2026, two-stage revision:

- Split the ledger into `intake` and `full`, each with independent pending,
  complete and deferred states. `next --stage full` only chooses intaken codes.
- The intake gate requires official browser evidence, a saved product-page
  capture, and the effective OOMP purchasing identity. Datasheet and generated
  footprints are deliberately optional until the full pass.
- Intake completed for **C6186, C1525, C1532, C1548, C1549, C1555, C1562,
  C1604, C1620 and C25804**. C6186 reuses
  its exact regulator identity and existing tracked manufacturer PDF. The other
  nine promote verified Basic purchase choices for existing generic capacitor
  and resistor IDs, retaining the previous supplier alternatives. Their PDFs
  could not be saved through the browser and remain open for the full pass.
- C1555 exercised the new `promote-intake` command and reviewed-choice registry;
  the effective capacitor population selects its JLC code without another
  hand-written Python block.
- Continued the same one-part intake cycle for **C1634, C1647, C1653 and
  C1663**, each with browser-checked Samsung MPN, Basic class, saved page-text
  evidence, and an explicit reviewed-choice promotion. Their former YAGEO
  purchasing choices remain alternatives; PDFs and detailed package review
  remain for the second pass.
- Status: 14 intake-complete, 1,572 intake-pending, 0 full-complete. Eight
  house-part tests pass, including saved-page and pre-promotion gates.

24 September 2026, continued intake and browser PDF recovery:

- Intake-completed **C1671, C1779, C12530, C13585, C14663 and C15195**.
  C12530 and C14663 already had the exact LCSC primary; the JLC identity is
  now explicit. New choices preserve prior alternatives.
- Clicking JLC's visible datasheet link saved PDFs into the browser Downloads
  folder. Imported all 19 capacitor/resistor intake PDFs with per-file source
  URL, SHA-256 and `interactive_browser` provenance. Earlier unsuccessful
  `downloadMedia` calls had not created local files. C6186 retains its
  pre-existing, separately documented manufacturer PDF; equality with the
  current JLC-linked PDF is not asserted.
- Status: **20 intake-complete, 1,566 intake-pending, 0 full-complete**. Eight
  house-part tests pass. PDF capture does not itself verify ordering-code
  tables, electrical limits, drawings or footprints; these remain full-pass
  work.
- Continued intake for **C15525, C15849 and C15850**, each with its official
  browser page capture, a browser-downloaded PDF, verified provenance, and an
  effective OOMP purchasing identity. Current status: **23 intake-complete,
  1,563 intake-pending, 0 full-complete**.
- C16780 joined the existing 0805 47 uF generic ID. C19666 received a new
  explicit `electronic_capacitor_0603_4_7_micro_farad_16_volt` variant because
  the generic's existing C69335 choice is rated 25 V. The generic preference
  remains C69335; the variant selects Basic C19666 and links back via
  `generic_oomp_id`. A targeted population regression test checks this.
- Current status: **25 intake-complete, 1,561 intake-pending, 0 full-complete**.
  Nine house-part tests pass.

24 September 2026, further intake:

- Intake-completed **C19702, C23630, C23733, C45783, C52923 and C57112**.
  Each has an official browser page capture, browser-downloaded PDF with source
  URL and SHA-256, and a checked effective purchasing identity.
- C23733 uses explicit
  `electronic_capacitor_0402_4_7_micro_farad_10_volt_20_percent` because the
  generic 0402 4.7 uF part already prefers a tighter +/-10% choice. The
  regression test also asserts this generic preference remains C368809.
- Current status: **31 intake-complete, 1,555 intake-pending, 0 full-complete**.

24 September 2026, two-stage intake continuation:

- Intake-completed **C59461, C96123 and C96446** from their live official JLC
  pages. Each has a saved page-text snapshot and browser-downloaded PDF with
  source provenance. Ordering-code, dimensional and footprint checks remain
  for the later full pass.
- C96446 is an explicit 0603 10 uF, 25 V, +/-20% variant. The generic 0603
  10 uF preference remains C19702 at 10 V, +/-10%; neither rating is hidden
  by replacing the other. The population regression test covers both IDs.
- Current status: **34 intake-complete, 1,552 intake-pending, 0 full-complete**.
- Continued with **C307331, C440198, C9002 and C32346**. The two capacitors
  are explicit 50 V variants preserving existing 16 V and 25 V generic
  preferences. C9002 is an 80 ohm ESR crystal variant because the existing
  generic 12 MHz / 20 pF choice lists 50 ohm ESR. C32346 matches an existing
  exact Seiko Epson purchasing identity. All four have live JLC page captures
  and browser-downloaded PDFs with recorded source and SHA-256.
- Current status: **38 intake-complete, 1,548 intake-pending, 0 full-complete**.
- Intake-completed **C97521**, matching the existing exact Winbond
  W25Q128JVSIQ OOMP entry. The live JLC page confirmed its Basic class,
  SOIC-8-208mil package and C-number. Its JLC-linked browser PDF differs from
  the repository's previous tracked PDF, so the current `datasheet.pdf` was
  replaced with the browser copy and now has recorded URL/hash provenance;
  the old version remains available in Git history for later comparison.
- Current status: **39 intake-complete, 1,547 intake-pending, 0 full-complete**.

24 September 2026, regulator and resistor intake:

- Intake-completed **C6187, C4177, C4184, C4190 and C4216**, each from its
  live Basic JLC listing with saved page text and browser PDF provenance.
- C6187 matched the existing exact 5 V AMS1117 identity; its downloaded PDF
  matched the tracked copy byte-for-byte. C4177 matched the 0603 1.8 kohm
  generic's recorded 100 mW, 75 V, +/-1% and +/-100ppm/C ratings; its prior
  YAGEO purchasing choice remains an alternative. C4184 filled a generic
  20 kohm resistor without a primary purchase number. C4190 and C4216
  confirmed exact existing UNI-ROYAL purchasing identities.
- Current status: **44 intake-complete, 1,542 intake-pending, 0 full-complete**.
- C4275 then confirmed the existing UNI-ROYAL 0603 75 ohm purchasing identity
  as Basic. Its page capture and browser PDF have been saved with provenance.
- Current status: **45 intake-complete, 1,541 intake-pending, 0 full-complete**.

- Intake-completed **C4310, C4328, C4382, C4410 and C7250** from their live
  Basic JLC listings. Each has a browser-observed page-text capture, a
  browser-downloaded PDF, and recorded source/hash provenance. These are
  0805 1.5 kohm, 0805 20 kohm, 0805 5.6 kohm, 1206 1 kohm and 0603 10 Mohm
  resistors respectively. Previous generic purchasing choices remain as
  alternatives where present. The 1206 1 kohm and 0603 10 Mohm house parts
  list +/-1% tolerance versus the former +/-5% choices; full review must
  still check derating and footprint geometry.
- Current status: **50 intake-complete, 1,536 intake-pending, 0 full-complete**.
- The 10 JLC intake tests and 11 populate workflow tests pass. The populate
  test for a missing source now names a deliberately absent fixture path;
  the old example path acquired a real datasheet during this research. Hashes
  for all five newly imported PDFs match their provenance records.
- Intake-completed **C8218, C11702 and C13167**, respectively 0603 200 ohm,
  0402 1 kohm and 0603 2.7 kohm Basic UNI-ROYAL resistors. Live JLC pages
  establish each C-number, MPN, package and class; saved page-text captures
  and browser-downloaded PDFs record source provenance. Existing generic
  purchasing choices remain as alternatives. The C8218 house part matches
  the existing generic's listed 100 mW, 75 V, +/-1% and +/-100ppm/C ratings.
- Current status: **53 intake-complete, 1,533 intake-pending, 0 full-complete**.

- Intake-completed **C17168, C17379 and C17408**. The zero-ohm 0402 C17168
  was already a generic alternative; its live Basic classification is now
  preferred while current rating and maximum resistance remain explicit
  full-pass questions. C17379 and C17408 confirmed existing exact UNI-ROYAL
  generic preferences. All three have live page-text captures and
  browser-downloaded PDF provenance.
- Added `scaffold-intake` so a smaller worker can supply live browser facts
  and an explicit OOMP compatibility decision as JSON. It checks identity and
  class against the queue, writes an editable page/record pair, refuses to
  overwrite prior evidence, and leaves PDF import and promotion as separate
  reviewed steps. C17379 and C17408 exercised the new command.
- Current status: **56 intake-complete, 1,530 intake-pending, 0 full-complete**.
- Verification: 11 JLC intake tests and 11 populate workflow tests pass; the
  three new browser PDF files match their recorded SHA-256 values.
- Intake-completed **C17414, C17415, C17437, C17444, C17470, C17471,
  C17475 and C17477**. Each Basic listing was checked in the live browser,
  its linked PDF downloaded through the browser, and its page/record and
  purchasing choice passed the per-code intake gate. C17414, C17415 and
  C17437 confirmed existing exact UNI-ROYAL preferences. The others replaced
  generic FOJAN preferences while preserving them as alternatives. For the
  0805 zero-ohm C17477, current rating and maximum resistance remain
  full-pass requirements.
- C17444 initially failed because the population emitted the 12 kohm
  resistor ID twice. Removed the repeated E12 12 kohm value from the extra
  list and a repeated 0603 1.6 kohm declaration; a population-wide duplicate
  assertion now protects the house-part matching gate.
- Current status: **64 intake-complete, 1,522 intake-pending, 0 full-complete**.
- The queue was regenerated from the original 2,004-row browser capture after
  the duplicate fix: 1,586 active candidates, 418 retired, and zero duplicate
  populated OOMP IDs. All 12 JLC intake tests and 11 populate workflow tests
  pass. The eight new PDFs have `interactive_browser` provenance with source
  URLs and matching SHA-256 values.
- Intake-completed **C17513, C17514, C17520, C17526, C17530, C17539,
  C17540, C17556, C17557, C17560, C17561, C17593, C17614, C17617,
  C17630, C17633, C17634, C17655, C17673 and C17709**. Every code was
  checked against a live Basic JLC page, and the visible PDF link was clicked
  in the browser before import. Exact existing UNI-ROYAL identities were
  confirmed; other generic entries received the house preference while
  retaining earlier FOJAN choices. C17539 and C17617 filled generics without
  primary purchase numbers. C17634 records the listing's +/-200ppm/C TCR.
- Current status: **84 intake-complete, 1,502 intake-pending, 0 full-complete**.
- Rebuilt the queue from the same 2,004-row capture; it still has 1,586
  active candidates and no duplicate populated IDs. All 20 newly imported
  PDFs have browser provenance, source URLs equal to their research records,
  and matching SHA-256 values. The 12 JLC intake and 11 populate workflow
  tests pass.
- Intake-completed **C17710, C17713, C17714, C17734, C17772, C17798,
  C17801, C17828, C17887, C17888, C17900, C17901, C17902, C17903,
  C17909 and C17927** from their live Basic JLC listings. Their 0805 and
  1206 generic resistor IDs now select the verified house choice, preserving
  previous purchasing alternatives. C17888 is a zero-ohm jumper; maximum
  resistance and current rating remain full-pass questions, while the
  listing's tolerance and TCR are recorded only as listing facts.
- Current status: **100 intake-complete, 1,486 intake-pending, 0
  full-complete**. The queue still has 1,586 active candidates and no
  duplicate populated OOMP IDs. All 16 newly imported PDFs have
  `interactive_browser` provenance, source URLs matching the observations,
  and matching SHA-256 values; page-text captures identify their C-numbers.
  The 12 JLC intake and 11 populate workflow tests pass.
- Intake-completed **C17936, C17958, C21189, C21190, C22765, C22775,
  C22787, C22790, C22807, C22808, C22809, C22843, C22859, C22935,
  C22940, C22961, C22962, C22966, C22967 and C22978** from their live
  Basic JLC pages. Each has an observed page-text capture, linked PDF
  downloaded through the browser, and effective OOMP purchase identity.
  Exact existing preferences were confirmed; previous FOJAN choices remain
  alternatives where the house number became preferred. C21189's listing
  tolerance is not a meaningful zero-ohm jumper rating; current and maximum
  resistance remain full-pass questions. C22859 lists a ±400ppm/℃ TCR.
- Current status: **120 intake-complete, 1,466 intake-pending, 0
  full-complete**. All 20 new PDFs have matching `interactive_browser`
  provenance/source URL/SHA-256; all page captures name the expected code.
  Queue regeneration finds 1,586 active candidates and no duplicate OOMP
  IDs. The 12 JLC intake and 11 populate workflow tests pass.
- Intake-completed **C23018, C23025, C23137, C23138, C23140, C23151,
  C23153, C23162, C23178 and C23179** from their live Basic JLC pages.
  C23025 filled a generic 0603 300Ω entry without an established preferred
  LCSC/MPN. Existing exact house preferences were confirmed and former FOJAN
  choices retained as alternatives where replaced. All ten linked PDFs were
  downloaded through the browser and their local source URLs, browser
  provenance and SHA-256 values match their records; all page captures name
  the expected C-number.
- Current status: **130 intake-complete, 1,456 intake-pending, 0
  full-complete**. Queue regeneration still finds 1,586 active candidates
  and no duplicate populated OOMP IDs. The 12 JLC intake and 11 populate
  workflow tests pass.
- Intake-completed **C23182, C23186, C23189, C23192, C23193, C23204,
  C23206, C23212, C23228, C23231, C23234, C23242, C23253, C23254 and
  C23345**, completing the next 0603 UNI-ROYAL Basic group. Eight existing
  exact house preferences were confirmed; seven generic preferences changed
  to the verified house number while retaining the former alternatives.
- Intake-completed **C25076, C25077, C25079, C25087, C25091, C25092,
  C25104, C25105, C25117 and C25123**, the first 0402 UNI-ROYAL Basic
  resistor group. Their live listings show 62.5mW and 50V; C25077 shows
  ±200ppm/℃ rather than the others' ±100ppm/℃. Each has a browser-saved
  linked PDF and page-text capture; older purchase choices remain
  alternatives where replaced.
- Current status: **155 intake-complete, 1,431 intake-pending, 0
  full-complete**. All 25 new PDFs have matching browser provenance,
  source URLs and SHA-256 values, and their page captures name the expected
  codes. Queue regeneration finds 1,586 active candidates and no duplicate
  populated OOMP IDs. The 12 JLC intake and 11 populate workflow tests pass.
- Intake-completed **C25741, C25744, C25752, C25756, C25764, C25765,
  C25768, C25779, C25792 and C25803** from their live Basic pages. C25764
  (0402 200kΩ) and C25765 (0402 20kΩ) filled generic IDs without established
  preferred purchase numbers. C25792 and C25803 confirmed exact existing
  house preferences; other previous purchase choices remain alternatives.
- Current status: **165 intake-complete, 1,421 intake-pending, 0
  full-complete**. All ten browser PDFs have source URLs matching their
  observations and SHA-256 values matching their recorded provenance; page
  captures name the expected codes. Queue regeneration finds 1,586 active
  candidates and no duplicate populated OOMP IDs. The 12 JLC intake and
  11 populate workflow tests pass.
- Intake-completed **C25808, C25810, C25811, C25819, C25867, C25879,
  C25890, C25900, C25905, C25981, C26010, C26083, C27834, C28636,
  C31850 and C149504** from their live Basic listings. They cover 0402,
  0603 and 0805 UNI-ROYAL resistors; C25811 fills a generic 0603 200kΩ
  entry without an established preferred purchase number. Exact house
  preferences were confirmed where present, and prior purchase choices
  remain alternatives where promoted.
- Current status: **181 intake-complete, 1,405 intake-pending, 0
  full-complete**. All sixteen linked PDFs were downloaded through the
  browser and have matching source URLs, browser provenance and SHA-256;
  page captures name the expected codes. Queue regeneration finds 1,586
  active candidates and no duplicate populated OOMP IDs. The 12 JLC
  intake and 11 populate workflow tests pass.
- Intake-completed **C720477**, the exact XUNPU TS-1088-AR02016 tactile
  switch. Its live Basic listing confirms the MPN, SMD,4x3mm package,
  SPST circuit, 12V and 50mA ratings. The switch populate-extra function
  now applies reviewed JLC choices, and the effective population selects
  C720477. The browser-linked one-page PDF differs from the repository's
  earlier two-page PDF; both are preserved, with the browser copy's URL,
  acquisition method and SHA-256 recorded. The mechanical drawing and
  candidate KiCad footprints remain unverified for the full pass.
- Current status: **182 intake-complete, 1,404 intake-pending, 0
  full-complete**. Queue regeneration finds 1,586 active candidates and no
  duplicate populated OOMP IDs. The 12 JLC intake and 11 populate workflow
  tests pass.
- Intake-completed **C7955** as the Basic onsemi LM393DR2G purchase choice
  for the existing generic LM393 SOIC-8 dual-comparator entry. Its live
  listing, page capture and browser-downloaded datasheet establish maker,
  MPN, package, C-number and listed ratings; pin mapping and footprint
  certification remain for the full pass.
- Intake-completed **C6961** as a new exact STMicroelectronics TL072CDT
  dual JFET-input amplifier option. JLC calls its package SO-8; the OOMP
  SOIC-8 family mapping is provisional pending manufacturer drawing and
  KiCad verification. Its live Basic page, linked browser PDF, source URL,
  SHA-256 and effective population identity passed intake.
- Current status: **184 intake-complete, 1,402 intake-pending, 0
  full-complete**. Queue regeneration finds 1,586 active candidates, 1,195
  populated electronic parts, and no duplicate IDs. The 12 JLC intake and
  11 populate workflow tests pass.
- Intake-completed **C7426, C7950, C71035 and C7433**. Each has a live
  JLC Basic listing, captured page text, exact manufacturer/MPN/package
  identity and a checked effective OOMP purchasing choice. C7950 and C71035
  also have browser-downloaded PDFs with recorded source provenance. C7426
  and C7433 opened TI PDF tabs but did not save local files; their records
  retain the verified PDF URLs and the missing-file notes for a later retry.
- Current status: **188 intake-complete, 1,398 intake-pending, 0
  full-complete**. Queue regeneration finds 1,586 active candidates, 1,199
  populated electronic parts and no duplicate IDs. The 12 JLC intake and
  11 populate workflow tests pass.
- Intake-completed **C1523, C1530, C1538, C1546, C1547, C1554, C1567,
  C1588, C1594, C1603, C1613, C1622 and C1623**. These are live-verified
  Basic FH or Samsung MLCCs. Each fills one previously absent 0402 or 0603
  generic value with the specific JLC C-number, manufacturer/MPN, voltage,
  dielectric and tolerance recorded as a purchase choice. Each has a saved
  browser page capture and browser-downloaded PDF with provenance.
- Current status: **201 intake-complete, 1,385 intake-pending, 0
  full-complete**. Queue regeneration finds 1,586 active candidates, 1,212
  populated electronic parts and no duplicate IDs. The 12 JLC intake and
  11 populate workflow tests pass.
- Intake-completed **C1631, C1644, C1648, C1658, C1664, C1710, C1729,
  C1739, C1743 and C1744**. These live-verified Basic FH/Samsung MLCCs fill
  missing 0603 and 0805 generic values. Each has the exact C-number,
  maker/MPN and purchasing ratings, a page capture, and a browser-downloaded
  PDF with provenance. The browser's clipboard did not bridge to the local
  workspace, so the observed facts were transcribed and checked per part.
- Current status: **211 intake-complete, 1,375 intake-pending, 0
  full-complete**. Queue regeneration finds 1,586 active candidates, 1,222
  populated electronic parts and no duplicate IDs. The 12 JLC intake and
  11 populate workflow tests pass.
- Intake-completed **C1790, C1798, C1804, C1846, C1848, C5378, C9196,
  C12891 and C13967** with live Basic identity and ratings checks, page
  captures, browser-downloaded PDFs, source hashes and effective purchasing
  choices. C9196 is explicitly rated as a 1206 1 nF 2000 V variant; its
  high-voltage land pattern and clearance need the full pass.
- Current status: **220 intake-complete, 1,366 intake-pending, 0
  full-complete**. Queue regeneration finds 1,586 active candidates, 1,231
  populated electronic parts and no duplicate IDs. The 12 JLC intake and
  11 populate workflow tests pass.

- Intake-completed **C14857, C14858, C15008, C16772, C21117, C21120,
  C21122, C24497, C28233, C28260, C28323, C29823, C32949 and C38523**.
  Each has a live Basic product-page capture, explicit OOMP population and
  preferred JLC identity, a browser-downloaded PDF with provenance, and a
  passing first-stage gate. C15008 retains its 6.3 V, +/-20% variant ID.
- Added the optional local browser capture bridge and observation converter
  to preserve rendered product-page text without an HTTP supplier fetch. The
  worker still explicitly chooses and checks OOMP compatibility. Two bridge
  tests and the existing JLC/populate suites pass: **25 tests total**.
- Current status: **234 intake-complete, 1,352 intake-pending, 0
  full-complete**. Queue regeneration finds 1,586 active candidates, 1,245
  populated electronic parts and no duplicate IDs.
- Intake-completed **C49678** as an explicit 50 V variant of 0805 100 nF,
  retaining the 100 V C28233 generic preference. Current status: **235
  intake-complete, 1,351 intake-pending, 0 full-complete**.

- Intake subsequently completed for **C46653, C50254, C53134, C53987,
  C107145, C377773, C1322360 and C32677**. Current ledger: **243
  intake-complete, 2 intake-deferred, 1,341 intake-pending, 0 full-complete**.
  C7171 and C16133 remain deferred for unresolved manufacturer identity.
- Added canonical `JLC_PART_INTAKE_AGENT.md` and
  `JLC_PART_INTEGRATION_AGENT.md`, with explicit sequential instructions,
  evidence tables, command examples, completion gates and recovery steps for
  smaller models. Earlier worker paths forward to these guides; `next` routes
  each stage to its own guide. LCSC page-based browser downloads are an
  approved first choice for datasheets; JLC verifies house classification.
- Verified both CLI guide routes, local guide links and Python example syntax.
  The JLC, populate workflow and capture bridge suites pass **25 tests**.
  `git diff --check` passes. No part was marked full-complete by this guide work;
  the complete integration workflow still requires a real part's technical
  and visual acceptance.

Automated checks establish consistency, not electrical equivalence. Intake
does not certify ratings or footprint suitability. Full workers must inspect
the datasheet and rendered assets.

Commands:

```powershell
.venv/Scripts/python.exe -m unittest kicad_agents.tests.test_jlc_house_parts -v
.venv/Scripts/python.exe -m unittest kicad_agents.tests.test_populate_workflow -v
.venv/Scripts/python.exe -m kicad_agents.jlc_house_parts_agent next --stage intake
.venv/Scripts/python.exe -m kicad_agents.jlc_house_parts_agent next --stage full
.venv/Scripts/python.exe -m kicad_agents.jlc_house_parts_agent status
```
