# Board explorer: pins and routed nets

The existing project action generates a self-contained, offline page at
`parts/<project-id>/board_explorer.html`, alongside `README.md` and `working.yaml`. It embeds the
assembly SVGs, actual PCB copper, part pinouts, metadata, styles and JavaScript.
There are no external fonts, scripts, image requests or services. GitHub and
supplier links are only opened when the reader clicks them.

## Using it

1. The left pane opens with a **project summary card**: display name, owner /
   repository, version, item and net counts, and a link to the project's GitHub
   page. A matching GitHub icon in the header opens the same page in a new tab.
2. The right-hand **Selection status** box opens with an OOMP matching summary:
   how many components are matched in total and, per category, the
   matched/total ratio. The catch-all `other` bucket is excluded — it says
   nothing about matching progress. As soon as anything is selected it shows
   the selection instead; a **Clear** button sits in its header.
3. Find a component in the left list and expand **Pins**. Click a pin to highlight
   that pin in teal and the net's traces and other pads in per-layer colours.
   The sidebar legend identifies front, back and internal copper. Vias and
   through-hole pads spanning layers have their own shared colour.
3a. The detail pane's actions row is **Open OOMP part**, **Open LCSC** (or the
   **LCSC options (n)** popup button when several catalogue numbers are
   declared), **Search LCSC** and **Supplier source**. Every part declares an
   `lcsc_search` value in its `working.yaml` — the string a human would type
   into LCSC (package plus value for passives such as `0402 100nF`,
   manufacturer part number for ICs and connectors) — shown in the facts table
   and used verbatim for the search link. Unmatched components fall back to
   footprint size plus schematic value.
3b. Pads render **above** the component artwork in a dedicated `.copper-pads`
   layer, white-backed with a black outline, so fills and traces never cut
   through them and the pins stay readable on the board. That visible copy is
   pointer-transparent; an invisible copy inside the copper layer keeps the
   original click behaviour, so a part's own artwork still wins clicks over
   its pads, and clicking a pad outside the part body selects its pin.
4. To follow a net by name, type it in the main search box: matching nets lead
   the results and clicking one highlights its copper. Net names in the
   right-hand pin table are clickable too, as are visible PCB traces and pads.
5. Clicking a selected component — in the list, on the board artwork or inside
   its bounding box — deselects it everywhere, keeping any other selections
   intact. The same applies to pressing Enter on a focused part; Ctrl-click
   still adds/removes single members without clearing the rest. Clicking a
   selected pin or net again (pin buttons, net results, trace or net name)
   deselects it the same way; when nothing is selected the detail pane returns
   to its initial prompt.
6. Clicking **anywhere inside a part's bounding box** on the board selects that
   part. The transparent hitboxes sit below the copper, so traces, vias and
   pads inside a part box are still clicked first and select their net.
7. Selecting a pin always populates its owning part in the detail pane.
   Following a trace or net keeps the current part when it sits on that net,
   and otherwise shows one of the parts the copper connects to — preferring a
   part on the visible side. Selecting anything **never flips the board
   view**: only components on the shown side appear in the list and receive
   hitboxes, so the current view layer is always what is selectable. Use the
   Top/Bottom buttons to change sides.
8. The selected-net summary lists connected pins. Click one to open that
   component and its pin.
9. **All copper layers** is the default. **Visible side copper** follows Top/Bottom, or select a
   named internal layer to follow routing through the board. Changing sides or
   layers keeps the net selected. Through-hole pads appear on both sides.
10. **Traces** hides/shows background copper; the selected net stays visible.
   **Fills** adds the saved zone-fill polygons, including selected-net fills.
   Fills start enabled; turn them off when a large plane obscures traces.
11. **+** and **−** zoom in and out. The changing percentage button fits the
   full board, while the fixed **100%** button restores the original view.
   The mouse wheel zooms around the pointer. Click and drag the drawing to pan;
   on a touch screen, drag with two fingers to pan without selecting a part.
   Escape clears the selected pin/net.
12. **Zoom to net** starts off. Enable it to fit each selected net to the window,
   including the pads, traces, vias and any visible fills. It follows changes
   of side/layer; disabling it or pressing Fit restores the full board.
13. The left hierarchy groups components by **category**. Its checkbox selects
   every member on **both sides**, even while searching. Counts show selected /
   total. Categories start collapsed. Expand a category to show its components and pin submenus.
   Individual component checkboxes refine the selection; multiple categories
   can be selected together. Switching sides preserves selections.
   Hold **Ctrl** (or **Cmd** on macOS) and click category titles, components,
   individual pins, or a **Pins** heading to add/remove them without clearing
   other selections. Ctrl-clicking a category toggles all its components on
   both sides; Ctrl-clicking **Pins** toggles that component's whole pin group.
   Multiple selected pins highlight the union of their nets. Normal pin clicks
   return to a single pin/net; Escape clears pin/net highlights.
14. **Highlight all selected nets**, beside **Zoom to net** in the board toolbar,
   starts off. When checked, it highlights the
   union of the selected components' nets, their copper and all connected pins.
   Layer colours, fill visibility and optional zoom apply to this union too.
   Click a pin or named net to follow just that net again. Escape turns
   bulk-net mode off but keeps the component selection. **Clear** removes
   component selections and net highlights.

The pin list scrolls within the left sidebar. Selection status and selected-net
connections sit below the matched-part details on the right. Both right-hand
sections scroll independently without resizing the panels or board; adjust
`--selection-status-height` in the embedded stylesheet to change the status
box's fixed height. Filtering the list searches categories, references,
values, OOMP IDs, footprint IDs, pin names and net names. Unassigned pads
highlight only the selected pin: they are never grouped into a fictitious
shared net. Duplicate physical pads with the same pin number/net highlight
together.

## Python and Roboclick flow

```text
working_oomp project actions
  -> project_readme_action.py (always-run run_python action)
     -> kicad_processing_agent.py
        -> pcb_copper.extract_copper()
        -> project.json / project.yaml
     -> project_summary_agent.py (existing assembly SVGs and PNG policy)
     -> project_html_agent.py
        -> pcb_copper.explorer_copper() / copper_drawings() / add_copper_svg()
        -> board_explorer.html
```

Run the saved project README action normally; no browser action or AI step is
needed. The full `action_regenerate_all.bat` also includes this action. Normal
runs keep existing PNGs; full regeneration intentionally refreshes them.

The routing data is stored under `pcb_files[].copper` in both structured project
files. It contains `layers`, `tracks` (segments and three-point arcs), `vias`,
`pads`, `zones` (saved filled polygons only), units and extraction warnings.
Coordinates remain in original KiCad board millimetres. Track widths, via sizes,
pad centres and shapes are not scaled to the OOMP assembly artwork.

Pad centres are transformed from footprint-local coordinates; a pad's saved
angle is already absolute and must not be added to the footprint angle again.
Bottom overlays use the same horizontal reflection axis as the assembly view.
Hover, focus and selection outlines have their own layer below all component
artwork and labels. They never recolour or add a stroke to the pin-label text;
native pad/net highlights remain below the artwork as well.
Nets are identified by name and source PCB, not by proximity or visual contact.
The exporter handles both older numeric net codes and newer named-net tokens.

Non-BOM artwork stays excluded from the component diagram/list. Its physical
copper is retained because it can be part of an electrical net; the connected
pin summary labels those endpoints “not in BOM”.

Saved fills are not recalculated. Refill in KiCad first if they are missing or
stale. This viewer is not a DRC tool: highlighting a net does not prove its
routing is complete. Standard round/rectangular/rounded/oval pads and custom
polygon/line/arc/circle/Bezier primitives are supported. Unsupported pad styles
are explicitly reported as size-envelope previews, not silently treated as
verified geometry. Original KiCad files are never modified by this feature.

## Editing and testing

- Categories: the editable arrays in `working_oomp_populate_category.py`;
  override `category` in any component's populate or populate-extra definition.
  Population persists `category` and `category_name` in `working.yaml` and
  extraction copies them into component JSON/YAML. Unmatched parts use a
  labelled KiCad hint; a category is not an accepted OOMP match.
- Layout, colours and copper/selection styling: `_style()` in
  `project_html_agent.py`; the first CSS variables are the quick-edit surface.
  The lifted `.copper-pads` / invisible `.copper-pad-hits` rules live just
  below the overlay styles; `_lcsc_search_value()` builds the per-component
  search string when the matched part does not declare one.
- Pin menus, selection and layer interaction: `_script()` in the same file.
- Copper extraction and geometry: `pcb_copper.py`; `copper_drawings()` splits
  pads from traces and `add_copper_svg()` places the visible pad copy above
  the component artwork but below the designator labels.
- Assembly artwork line weight: `_scale_assembly_strokes()` in `svg_help.py`
  rewrites every assembly drawing to one constant absolute stroke width (the
  IC4 TSOT-23-5 reference on the pt1 board), so large parts no longer draw
  thicker outlines than small ones.
- The project summary card reads `project.github_url` from the persisted
  summary data; the header icon reuses the same URL. The matching summary
  filters out the `other` category in `matchingSummary()`; the bounding-box
  hitboxes are installed by `installComponentHitboxes()` below the copper
  groups, one per shown side.
- Iterating on the page itself: `action_regenerate_board_explorer.py` rebuilds
  `board_explorer.html` directly from the persisted `project.json` and
  `project_summary_data.json` under `data/generated_data/`, skipping the
  populate/Roboclick pipeline. With no arguments it regenerates every project
  part that has extracted data; `--filter <oomp-id>` regenerates one part.
- Format reference: [official KiCad PCB format](https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/).

```console
python -m unittest kicad_agents.tests.test_pcb_copper -v
python -m unittest discover -s kicad_agents/tests -v
python action_regenerate_board_explorer.py --filter <project-id>
node kicad_agents/tests/board_explorer_smoke.cjs path/to/board_explorer.html screenshot.png
```

The optional browser smoke test requires an already installed Playwright and
Chromium. `OOMP_PLAYWRIGHT` can point at the Playwright module and
`OOMP_CHROMIUM` at its browser executable. It tests actual controls, net-wide
trace counts, mirrored-side persistence, zoom, saved fills, sidebar width,
JavaScript errors and zero external requests. Nothing is downloaded by tests.
