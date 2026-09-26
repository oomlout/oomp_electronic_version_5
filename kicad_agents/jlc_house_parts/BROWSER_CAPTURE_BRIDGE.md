# Local browser evidence handoff

This optional form saves facts already read from a live JLC product page. It
does not contact JLC, download a datasheet, choose an OOMP identity, or mark a
part complete. Use one C-number at a time.

1. Start `python -m kicad_agents.jlc_house_parts.browser_capture_bridge` in a
   local terminal. It listens on `127.0.0.1:8765` only.
2. Open the queued official product URL in the browser. Read the visible
   manufacturer, complete MPN, C-number, package, Basic/Preferred label,
   description, specifications, stock and linked datasheet. Click the visible
   datasheet Download link and confirm the PDF exists in Downloads.
3. In another browser tab, open `http://127.0.0.1:8765/`. Submit a JSON object
   with `official_url`, `code`, `manufacturer`, `mpn`, `package`, `tier_label`,
   `description`, `datasheet_url` (without a temporary query string),
   `specifications`, `stock_observed`, `purchase_moq_observed`,
   `full_reel_observed`, `available_order_qty_observed` and `visible_text` from
   the actual rendered page. The form saves
   `browser_staging/C<number>.json`; check that file exists. It rejects a
   different identity or house tier from the queue.
4. Decide the OOMP classification yourself. Add an explicit population row if
   the chosen ID is missing, or verify generic compatibility if reusing one.
   Then create the observation from the saved capture, for example:

   ```powershell
   python -m kicad_agents.jlc_house_parts.intake_from_capture C123 --part-id electronic_capacitor_0805_47_pico_farad --family capacitor --pin-count 2 --compatibility-notes 'Reviewed value, package and purchasing ratings.' --evidence-note 'Live JLC page showed the complete manufacturer MPN and Basic label.'
   ```

5. Run the normal `scaffold-intake`, browser PDF import, `promote-intake`,
   `intake-check` and `intake-complete` commands in `INTAKE_WORKER.md`.

The staged JSON preserves the browser-visible page text, while the generated
`parts_source/<id>/web_page_distributor_jlc.txt` is a concise text snapshot. If
the browser PDF does not save, record that fact and continue intake. Never
describe a saved text snapshot as an offline HTML mirror.
