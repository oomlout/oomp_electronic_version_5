"""Build a single-file, offline HTML explorer for an extracted KiCad board."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

import yaml

from kicad_agents.pcb_copper import add_copper_svg, copper_svg, explorer_copper


OOMP_PARTS_URL = "https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts"


def _read_text(path):
    return Path(path).read_text(encoding="utf-8")


def _svg_without_declaration(svg_text):
    return re.sub(r"^\s*<\?xml[^>]*>\s*", "", svg_text, count=1)


def _part_pinout_svg(asset_directory, oomp_id):
    if oomp_id == "":
        return ""
    candidates = [
        asset_directory / "components" / oomp_id / "working_svg_square_pins.svg",
        asset_directory / "components" / oomp_id / "working_svg_assembly_pins.svg",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return _svg_without_declaration(_read_text(candidate))
    return ""


def _part_symbol_svg(asset_directory, reference):
    """The placed schematic symbol drawing for this reference, if the sheet has one."""
    safe_reference = re.sub(r"[^A-Za-z0-9_.-]", "_", str(reference))
    if safe_reference == "":
        return ""
    candidate = asset_directory / "schematic_parts" / f"{safe_reference}.svg"
    if candidate.is_file():
        return _svg_without_declaration(_read_text(candidate))
    return ""


def _lcsc_options(component, part_metadata):
    """Ordered, de-duplicated LCSC purchase options for the matched part.

    The part's distributors list carries every catalogue option (with product
    names when populated); explicit BOM properties are the last fallback.  An
    unmatched component has no catalogue to point at, matching the old
    single-number behaviour.
    """
    match = component.get("oomp") or {}
    if match.get("status") != "matched" or not match.get("oomp_id"):
        return []
    options = []
    seen = set()

    def add_option(candidate, product_name=""):
        number = str(candidate or "").strip().upper()
        if number.isascii() and number.isdigit():
            number = "C" + number
        if not re.fullmatch(r"C[0-9]+", number) or number in seen:
            return
        seen.add(number)
        options.append({
            "part_number": number,
            "product_name": str(product_name or "").strip(),
            "url": f"https://www.lcsc.com/product-detail/{number}.html",
        })

    for distributor in part_metadata.get("distributors") or []:
        if distributor.get("key") == "lcsc":
            add_option(distributor.get("part_number"), distributor.get("product_name", ""))
    add_option(part_metadata.get("part_number_lcsc", ""))
    property_sets = [(component.get("pcb") or {}).get("properties") or {}]
    for unit in (component.get("schematic") or {}).get("units") or []:
        property_sets.append(unit.get("properties") or {})
    for properties in property_sets:
        for key, value in properties.items():
            field = re.sub(r"[^a-z0-9]", "", str(key).lower())
            if field in ["partnumberlcsc", "lcsc", "lcscpartnumber", "lcscpart"]:
                add_option(value)
    return options


def _lcsc_part_number(component, part_metadata):
    """Prefer the matched catalogue number; fall back to explicit BOM fields."""
    options = _lcsc_options(component, part_metadata)
    return options[0]["part_number"] if options else ""


def _lcsc_value_shorthand(value):
    """Expand KiCad shorthand values ("100n", "10k", "4R7") for LCSC search."""
    if re.fullmatch(r"\d+(?:\.\d+)?[pnu]", value, re.IGNORECASE):
        return f"{value[:-1]}{value[-1].lower()}F"
    if re.fullmatch(r"\d+R\d+", value):
        return f"{value.replace('R', '.')}Ω"
    if re.fullmatch(r"\d+(?:\.\d+)?[kKmM]", value):
        return f"{value}Ω"
    if value == "0":
        return "0Ω"
    return value


def _lcsc_search_value(component, part_metadata):
    """Search string that finds this part's options on LCSC.

    Matched parts declare their value in working.yaml (lcsc_search, built by
    the metadata normaliser); unmatched components fall back to the footprint
    size plus the schematic value, which is how a human would search.
    """
    explicit = str((part_metadata or {}).get("lcsc_search", "") or "").strip()
    if explicit:
        return explicit
    pcb = component.get("pcb") or {}
    value = _lcsc_value_shorthand(str(pcb.get("value") or "").strip())
    footprint = str(pcb.get("library_id") or "")
    if not value:
        return footprint
    sizes = re.search(r"(?:^|[^0-9])(0201|0402|0603|0805|1206|1210|2010|2512)(?:[^0-9]|$)", footprint)
    passive = re.fullmatch(r"\d+(?:\.\d+)?(?:p|n|u|µ)?F|\d+(?:\.\d+)?(?:k|K|M|m)?Ω", value)
    if sizes and passive:
        return f"{sizes.group(1)} {value}"
    return value


def _component_record(component, asset_directory, part_metadata=None):
    pcb = component.get("pcb") or {}
    oomp = component.get("oomp") or {}
    oomp_id = str(oomp.get("oomp_id") or "")
    properties = pcb.get("properties") or {}
    lcsc_options = _lcsc_options(component, part_metadata or {})
    lcsc_number = lcsc_options[0]["part_number"] if lcsc_options else ""
    pads = []
    pad_keys = []
    for pad in pcb.get("pads") or []:
        pin_number = str(pad.get("number") or "")
        pin_name = str(pad.get("pin_function") or pad.get("net") or "")
        net_name = str(pad.get("net") or "")
        if pin_number == "" and pin_name == "" and net_name == "":
            continue
        pad_key = [pin_number, pin_name, net_name]
        if pad_key in pad_keys:
            continue
        pad_keys.append(pad_key)
        pads.append({"number": pin_number, "name": pin_name, "net": net_name, "type": str(pad.get("pin_type") or pad.get("type") or "")})
    return {
        "reference": str(component.get("reference") or ""),
        "category": str(component.get("category") or "other"),
        "category_name": str(component.get("category_name") or "Other"),
        "category_source": str(component.get("category_source") or ""),
        "value": str(pcb.get("value") or properties.get("Value") or ""),
        "footprint": str(pcb.get("library_id") or ""),
        "side": str(pcb.get("side") or ""),
        "position": pcb.get("position") or {},
        "source_file": pcb.get("source_file") or "",
        "oomp_id": oomp_id,
        "match_status": str(oomp.get("status") or "unmatched"),
        "confidence": oomp.get("confidence", 0),
        "part_url": f"{OOMP_PARTS_URL}/{oomp_id}" if oomp_id else "",
        "lcsc_part_number": lcsc_number,
        "lcsc_url": f"https://www.lcsc.com/product-detail/{lcsc_number}.html" if lcsc_number else "",
        "lcsc_options": lcsc_options,
        "lcsc_search": _lcsc_search_value(component, part_metadata or {}),
        "supplier": str(properties.get("Supplier") or "").strip(),
        "pads": pads,
        "pinout_svg": _part_pinout_svg(asset_directory, oomp_id),
        "symbol_svg": _part_symbol_svg(asset_directory, str(component.get("reference") or "")),
    }


def _style():
    # Everything visual lives here.  The variables at the top are the intended
    # quick-adjustment surface for later restyling.  Three embedded themes
    # (light, dark, rainbow) override only the variables plus a handful of
    # gradient rules — the board drawing itself stays black-on-white so the
    # artwork remains readable in every theme.
    return """
:root {
  --page: #f3f1e9;
  --panel: #ffffff;
  --ink: #171717;
  --muted: #686868;
  --line: #c9c5ba;
  --accent: #ff5c35;
  --accent-soft: #ffe4db;
  --board: #f8f8f5;
  --copper: #7a8790;
  --net: #d9480f;
  --selected-pin: #007d8a;
  --copper-front: #d9480f;
  --copper-back: #2563eb;
  --copper-inner-1: #9333ea;
  --copper-inner-2: #16803c;
  --copper-multilayer: #674b26;
  --shadow: 0 18px 50px rgba(20, 20, 20, .14);
  --radius: 18px;
  --selection-status-height: 180px;
  --font: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --header-bg: #171717;
  --header-fg: #ffffff;
  --header-muted: #cfcfcf;
  --header-line: #555555;
  --float-bg: rgba(255, 255, 255, .97);
  --toolbar-bg: rgba(255, 255, 255, .94);
  --sch-page: #ffffff;
  --sch-ink: #171717;
  --sch-muted: #686868;
  --sch-note: #8a7f6a;
  --sch-body: #f0ede4;
  --brd-page: var(--board);
  --brd-board-fill: #ffffff;
  --brd-board-outline: #1f1f1f;
  --brd-component-fill: #ffffff;
  --brd-component-outline: #1f1f1f;
  --brd-text: #171717;
  --brd-plate: #ffffff;
  --brd-plate-text: #171717;
  --brd-pad-fill: #ffffff;
  --brd-pad-outline: #1f1f1f;
}
html[data-theme="dark"] {
  --page: #14161a;
  --panel: #1d2127;
  --ink: #e8e6e1;
  --muted: #9aa0a6;
  --line: #33383f;
  --accent: #ff6b47;
  --accent-soft: #3c2a23;
  --board: #0f1114;
  --copper: #93a1ad;
  --net: #ff7a45;
  --selected-pin: #3fb7c9;
  --shadow: 0 18px 50px rgba(0, 0, 0, .55);
  --header-bg: #0b0c0f;
  --header-muted: #8f959d;
  --header-line: #3a3f46;
  --float-bg: rgba(34, 38, 44, .97);
  --toolbar-bg: rgba(23, 26, 30, .94);
  --sch-page: #1d2127;
  --sch-ink: #e8e6e1;
  --sch-muted: #9aa0a6;
  --sch-note: #b3a58f;
  --sch-body: #2c313a;
  --brd-page: var(--board);
  --brd-board-fill: #1d2127;
  --brd-board-outline: #9aa0a6;
  --brd-component-fill: #262b33;
  --brd-component-outline: #b8bdc4;
  --brd-text: #e8e6e1;
  --brd-plate: #2c313a;
  --brd-plate-text: #e8e6e1;
  --brd-pad-fill: #1d2127;
  --brd-pad-outline: #b8bdc4;
}
html[data-theme="rainbow"] {
  --page: #fdf7ee;
  --ink: #2b2118;
  --muted: #857767;
  --line: #ecdcc3;
  --accent: #ff5c35;
  --accent-soft: #ffe8cc;
  --board: #fbf5ea;
  --copper: #9d4edd;
  --net: #d946ef;
  --selected-pin: #06b6d4;
  --copper-front: #ff5c35;
  --copper-back: #00b4d8;
  --copper-inner-1: #70e000;
  --copper-inner-2: #9d4edd;
  --copper-multilayer: #ffb703;
  --sch-page: #fffbf2;
  --sch-ink: #6d28d9;
  --sch-muted: #c2410c;
  --sch-note: #0f766e;
  --sch-body: #ede9fe;
  --brd-page: var(--board);
  --brd-board-fill: #fff8ec;
  --brd-board-outline: #6d28d9;
  --brd-component-fill: #fdf4ff;
  --brd-component-outline: #9333ea;
  --brd-text: #7e22ce;
  --brd-plate: #fce7f3;
  --brd-plate-text: #be185d;
  --brd-pad-fill: #fef08a;
  --brd-pad-outline: #ca8a04;
  --rainbow: linear-gradient(90deg, #ff5c35, #ffb703, #70e000, #00b4d8, #9d4edd);
}
* { box-sizing: border-box; }
html, body { margin: 0; width: 100%; height: 100%; background: var(--page); color: var(--ink); font-family: var(--font); }
body { display: grid; grid-template-rows: auto minmax(0, 1fr); overflow: hidden; }
header { display: flex; align-items: center; gap: 18px; padding: 16px 22px; background: var(--header-bg); color: var(--header-fg); }
header h1 { margin: 0; font-size: clamp(18px, 2.1vw, 30px); letter-spacing: -.03em; }
header p { margin: 2px 0 0; color: var(--header-muted); font-size: 13px; }
.badge { margin-left: auto; border: 1px solid var(--header-line); border-radius: 999px; padding: 7px 11px; font-size: 12px; white-space: nowrap; }
.github-link { display: inline-flex; align-items: center; justify-content: center; width: 34px; height: 34px; border: 1px solid var(--header-line); border-radius: 999px; color: var(--header-fg); flex: none; }
.github-link:hover { border-color: var(--header-fg); background: rgba(255, 255, 255, .12); }
.github-link svg { fill: currentColor; }
.theme-select { display: inline-flex; align-items: center; gap: 7px; margin-left: auto; font-size: 12px; color: var(--header-muted); white-space: nowrap; }
.theme-select select { width: auto; padding: 7px 9px; border: 1px solid var(--header-line); border-radius: 999px; background: transparent; color: var(--header-fg); font: inherit; font-size: 12px; cursor: pointer; }
.theme-select select option { color: var(--ink); background: var(--panel); }
.badge ~ .theme-select { margin-left: 0; }
.project-card { padding: 12px 14px; border-bottom: 1px solid var(--line); font-size: 12px; }
.project-card-title { font-weight: 650; font-size: 13px; letter-spacing: -.01em; }
.project-card-meta { color: var(--muted); margin-top: 3px; overflow-wrap: anywhere; }
.project-card-link { display: inline-block; margin-top: 7px; color: var(--accent); text-decoration: none; font-weight: 600; }
.project-card-link:hover { text-decoration: underline; }
.popup-overlay { position: fixed; inset: 0; z-index: 60; display: grid; place-items: center; padding: 20px; background: rgba(23, 23, 23, .45); }
.popup-overlay[hidden] { display: none; }
.popup-card { width: min(440px, 100%); display: grid; gap: 8px; padding: 16px 18px; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; box-shadow: var(--shadow); }
.popup-head { display: flex; align-items: center; justify-content: space-between; gap: 10px; font-size: 13px; }
.popup-close { width: auto; padding: 0 6px; border: none; background: none; font-size: 20px; line-height: 1; cursor: pointer; color: var(--muted); }
.popup-close:hover { color: var(--ink); }
.popup-row { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; padding: 9px 11px; border: 1px solid var(--line); border-radius: 10px; color: inherit; text-decoration: none; font-size: 12px; }
.popup-row:hover { border-color: var(--accent); background: var(--accent-soft); }
.popup-name { min-width: 0; overflow-wrap: anywhere; font-weight: 600; }
.popup-number { flex: none; font-family: ui-monospace, "Cascadia Mono", Consolas, monospace; color: var(--muted); }
.layout { height: 100%; min-height: 0; display: grid; grid-template-columns: minmax(190px, 260px) minmax(0, 1fr) minmax(260px, 360px); gap: 14px; padding: 14px; overflow: hidden; }
.panel { min-width: 0; min-height: 0; background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); overflow: hidden; box-shadow: 0 4px 18px rgba(0,0,0,.05); }
.list-panel { display: grid; grid-template-rows: auto auto minmax(0, 1fr); min-width: 0; }
.search-wrap { padding: 14px; border-bottom: 1px solid var(--line); }
input { width: 100%; padding: 10px 12px; border: 1px solid var(--line); border-radius: 10px; background: var(--board); color: var(--ink); font: inherit; }
.part-list { min-width: 0; overflow: auto; padding: 7px; }
.part-row { position: relative; min-width: 0; }
.category-group { border-bottom: 1px solid var(--line); padding-bottom: 5px; }
.category-group > summary { display: flex; align-items: center; gap: 7px; padding: 10px 3px; cursor: pointer; font-size: 12px; font-weight: 750; }
.category-group > summary::before { content: '▸'; }
.category-group[open] > summary::before { content: '▾'; }
.category-group > summary span { flex: 1; min-width: 0; overflow-wrap: anywhere; }
.category-group > summary small { color: var(--muted); font-weight: 400; }
.category-select, .part-select { width: 14px; height: 14px; margin: 0; padding: 0; flex: 0 0 auto; cursor: pointer; accent-color: var(--accent); }
.part-select { position: absolute; left: 5px; top: 12px; }
.part-row > .part-button { padding-left: 25px; }
.part-button.selected { background: var(--accent-soft); }
.selection-status-header { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
.selection-status-header button { border: 0; background: transparent; color: var(--ink); text-decoration: underline; cursor: pointer; font: inherit; font-size: 11px; }
.match-rows { display: flex; flex-wrap: wrap; gap: 3px 12px; margin-top: 4px; }
.match-rows span { font-size: 11px; color: var(--muted); }
.match-rows b { color: var(--ink); font-weight: 650; }
.net-results { display: flex; flex-direction: column; gap: 2px; padding: 2px 3px 6px; }
.net-results .net-link { display: flex; justify-content: space-between; gap: 8px; padding: 6px 8px; border: 0; border-radius: 8px; background: transparent; text-align: left; cursor: pointer; font-size: 12px; }
.net-results .net-link:hover { background: var(--accent-soft); }
.net-results .net-link small { color: var(--muted); font-size: 10px; }
.part-button { width: 100%; min-width: 0; display: grid; grid-template-columns: 50px minmax(0, 1fr); gap: 3px 8px; padding: 9px 32px 9px 9px; border: 0; border-radius: 10px; background: transparent; color: inherit; text-align: left; cursor: pointer; }
.part-button:hover, .part-button.active { background: var(--accent-soft); }
.part-button.active:not(.selected) { background: transparent; box-shadow: inset 0 0 0 1px var(--line); }
.part-button strong { font-size: 13px; }
.part-button span { overflow: hidden; color: var(--muted); font-size: 11px; text-overflow: ellipsis; white-space: nowrap; }
.part-button .oomp-id { grid-column: 1 / -1; overflow-wrap: anywhere; text-overflow: clip; white-space: normal; }
.part-link { position: absolute; top: 8px; right: 7px; display: grid; width: 24px; height: 24px; place-items: center; border-radius: 7px; color: var(--ink); text-decoration: none; }
.part-link:hover { background: var(--ink); color: white; }
.board-panel { position: relative; display: grid; place-items: center; overflow: auto; padding: 18px; background: var(--board); }
.board-toolbar { position: absolute; z-index: 10; top: 12px; left: 12px; right: 12px; display: flex; flex-wrap: wrap; align-items: center; gap: 5px; padding: 5px; border: 1px solid var(--line); border-radius: 12px; background: var(--toolbar-bg); color: var(--ink); box-shadow: 0 4px 14px rgba(0,0,0,.08); }
.side-button { padding: 7px 11px; border: 0; border-radius: 8px; background: transparent; color: var(--muted); font: inherit; font-size: 12px; font-weight: 750; cursor: pointer; }
.side-button:hover, .side-button.active { background: var(--ink); color: var(--panel); }
.zoom-divider { width: 1px; margin: 4px 2px; background: var(--line); }
.zoom-button { width: 31px; padding: 7px 0; border: 0; border-radius: 8px; background: transparent; color: var(--ink); font: inherit; font-weight: 850; cursor: pointer; }
.zoom-button:hover { background: var(--accent-soft); }
.zoom-label { min-width: 43px; align-self: center; color: var(--muted); font-size: 11px; text-align: center; }
.zoom-reset { width: auto; min-width: 47px; padding-inline: 7px; font-size: 11px; }
.board-stage { width: 100%; height: 100%; min-width: 0; min-height: 0; display: grid; place-items: center; cursor: grab; touch-action: none; user-select: none; }
.board-stage.is-panning { cursor: grabbing; }
.board-stage.split { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); place-items: stretch; gap: 8px; position: relative; }
.board-stage.split::after { content: ''; position: absolute; left: 50%; top: 6px; bottom: 6px; width: 1px; background: var(--line); transform: translateX(-0.5px); pointer-events: none; }
.board-stage.split .board-view:not([hidden]), .board-stage.split .schematic-view:not([hidden]) { width: auto; }
.board-view { width: 100%; height: 100%; min-width: 0; min-height: 0; }
/* Per-part artwork keeps its print palette as baked presentation attributes
   (#FFFFFF fills, #000000 strokes); the rules below re-ink the strokes, the
   pin-one markers and the pads with the page theme.  White body fills stay
   governed by the transparent-geometry rule further down. */
.board-component [fill="#000000"] { fill: var(--brd-component-outline); }
.board-component [stroke="#000000"] { stroke: var(--brd-component-outline); }
.board-component .pad { fill: var(--brd-pad-fill); stroke: var(--brd-pad-outline); }
.board-view[hidden], .schematic-view[hidden] { display: none; }
.board-view > svg, .schematic-view > svg { display: block; width: 100%; height: 100%; max-width: 100%; max-height: 100%; margin: auto; filter: drop-shadow(0 9px 13px rgba(0,0,0,.12)); }
.schematic-view { width: 100%; height: 100%; min-width: 0; min-height: 0; overflow: hidden; border-radius: 8px; }
/* Schematic symbols reuse the component hover/select machinery.  They stay
   black whether selected or not — selection is shown only by the accent
   rectangle drawn around them, exactly like the board view. */
.schematic-view .sch-symbol { cursor: pointer; outline: none; transition: opacity .13s ease; }
.schematic-view .sch-wire.on-net { stroke: var(--net); }
.schematic-view .sch-wire-hit.on-net { stroke: var(--net); stroke-opacity: .25; }
.schematic-view .sch-junction.on-net { fill: var(--net); }
.schematic-view.has-net .sch-wire:not(.on-net), .schematic-view.has-net .sch-wire-hit:not(.on-net) { opacity: .18; }
.schematic-view .sch-global.on-net .sch-label-pill { fill: var(--net); }
.schematic-view .sch-global.on-net .sch-label-pill-text { fill: #ffffff; }
.schematic-view .sch-label-tag.on-net .sch-label-pill { fill: var(--net); stroke: var(--net); }
.schematic-view .sch-label-tag.on-net .sch-label-pill-text { fill: #ffffff; }
.schematic-view .sch-label.on-net { fill: var(--net); font-weight: 700; }
.board-stage .board-component { cursor: pointer; outline: none; transition: opacity .13s ease; shape-rendering: geometricPrecision; }
.board-stage .board-component > .component { fill: none; }
/* Only the explorer makes white assembly geometry transparent. Labels and
   black outlines stay above the actual pad/track shapes; source SVGs stay white.
   The part artwork carries class="pad" primitives: they stay solid white
   (with their black outline) so pins remain readable over routed copper;
   every other white-filled artwork shape stays transparent as before. */
.board-stage .board-component :is(rect, path, polygon, circle, ellipse):is([fill="#FFFFFF"], [fill="#ffffff"], [fill="#fff"], [fill="white"]):not(.pad) { fill: none; }
/* Never stroke an ancestor of the pin labels: SVG text inherits that stroke,
   which can be several times wider than the letters at physical board scale. */
.board-stage .board-component text { stroke: none; }
.board-stage.has-selection .board-component:not(.is-active) { opacity: .55; }
.component-highlights { pointer-events: none; }
.selection-box, .hover-box { fill: none; stroke: var(--accent); stroke-width: 1.2; stroke-linejoin: round; stroke-linecap: round; shape-rendering: geometricPrecision; vector-effect: non-scaling-stroke; pointer-events: none; }
.selection-box { stroke-width: 2.8; }
.hover-box { stroke-width: 1.6; opacity: .65; }
.board-stage .indicator { pointer-events: none; }
.detail { display: grid; grid-template-rows: minmax(0, 1fr) var(--selection-status-height); gap: 14px; padding: 18px; }
.part-detail-scroll { min-width: 0; min-height: 0; overflow: auto; overflow-wrap: anywhere; scrollbar-gutter: stable; }
.selection-status { min-width: 0; min-height: 0; display: grid; grid-template-rows: auto minmax(0, 1fr); gap: 8px; padding: 12px; border: 1px solid var(--line); border-radius: 12px; overflow: hidden; }
.eyebrow { color: var(--accent); font-size: 11px; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; }
.detail h2 { margin: 5px 0 0; font-size: 30px; letter-spacing: -.04em; }
.value { margin: 4px 0 18px; color: var(--muted); }
.facts { display: grid; grid-template-columns: 92px minmax(0, 1fr); gap: 7px 10px; margin: 0 0 18px; font-size: 13px; }
.facts dt { color: var(--muted); }
.facts dd { margin: 0; overflow-wrap: anywhere; }
.pinout { height: 240px; display: grid; place-items: center; margin: 12px 0; padding: 10px; border: 1px solid var(--line); border-radius: 14px; background: white; overflow: hidden; touch-action: none; cursor: grab; }
.pinout.is-panning { cursor: grabbing; }
.pinout svg { width: 100%; height: 100%; max-height: none; will-change: transform; transform-origin: 0 0; }
.pinout.sch-preview { background: var(--sch-page); }
.pin-table { width: 100%; border-collapse: collapse; font-size: 12px; }
.pin-table th, .pin-table td { padding: 6px; border-bottom: 1px solid var(--line); text-align: left; }
.pin-table { table-layout: fixed; overflow-wrap: anywhere; }
.pin-table th:first-child { width: 45px; }
.pin-menu { margin: 0 7px 9px; font-size: 12px; }
.pin-menu summary { cursor: pointer; padding: 5px; color: var(--muted); }
.pin-menu-body { max-height: 260px; overflow: auto; }
.pin-button, .net-link { font: inherit; text-align: left; cursor: pointer; border: 0; border-radius: 5px; color: inherit; background: transparent; overflow-wrap: anywhere; }
.pin-button { display: block; width: 100%; padding: 6px; border-left: 3px solid transparent; }
.pin-button small { display: block; color: var(--muted); overflow-wrap: anywhere; }
.pin-button:hover, .net-link:hover { background: var(--accent-soft); }
.pin-button.on-net, .net-link.on-net { background: var(--accent-soft); }
.pin-button.selected-pin { border-left-color: var(--selected-pin); color: var(--selected-pin); font-weight: 750; }
.net-link { color: var(--net); padding: 3px; text-decoration: underline; }
.board-toolbar select { width: 100%; min-width: 0; max-width: 100%; padding: 6px; border: 1px solid var(--line); border-radius: 6px; background: white; font: inherit; }
.net-status { min-width: 0; min-height: 0; overflow: auto; overflow-wrap: anywhere; font-size: 12px; line-height: 1.5; scrollbar-gutter: stable; }
.net-status button { font-size: 11px; }
.board-toolbar select { width: auto; max-width: 155px; font-size: 11px; }
.board-toolbar label { font-size: 11px; white-space: nowrap; }
.board-toolbar input { width: auto; }
.net-selection-controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; max-width: 100%; }
.copper-feature { color: var(--copper); cursor: pointer; shape-rendering: geometricPrecision; }
.copper-segment, .copper-arc, .copper-via { fill: none; stroke: currentColor; stroke-linecap: round; stroke-linejoin: round; }
.copper-pad, .copper-zone { fill: currentColor; stroke: none; }
.copper-base .copper-feature { opacity: .48; }
.copper-base .copper-zone { opacity: .10; pointer-events: none; }
.copper-base .copper-pad { opacity: .28; }
.copper-feature.layer-hidden, .copper-feature.fill-hidden { display: none; }
.board-stage.hide-traces .copper-base { display: none; }
.board-stage.has-net .copper-base .copper-feature { opacity: .10; }
.board-stage.has-net .board-component { opacity: .25; }
.board-stage.has-net .board-component.on-net { opacity: 1; }
.board-stage.has-net .board-component.is-active { opacity: 1; }
.copper-overlay .copper-feature { color: var(--layer-color, var(--net)); opacity: 1; }
.copper-overlay .copper-zone { opacity: .18; pointer-events: none; }
/* Use the exact native circle/rounded-rectangle/custom pad boundary. The old
   pixel-width white border caused jagged seams, especially on custom pads. */
.copper-overlay .copper-pad .pad-anchor { stroke: none; }
.copper-overlay .selected-pin { color: var(--selected-pin); }
.net-note { font-size: 11px; color: var(--muted); }
.layer-legend { display: flex; flex-wrap: wrap; gap: 4px 12px; font-size: 11px; margin-top: 6px; }
.layer-key { display: inline-flex; align-items: center; gap: 4px; }
.layer-swatch { width: 10px; height: 10px; border-radius: 50%; background: var(--layer-color); }
.actions { display: flex; flex-wrap: wrap; gap: 8px; margin: 14px 0; }
.actions a { display: inline-block; padding: 9px 12px; border-radius: 10px; background: var(--ink); color: var(--panel); text-decoration: none; font-size: 12px; }
.actions a.secondary, .actions button.secondary { border: 0; cursor: pointer; font: inherit; background: var(--accent-soft); color: var(--ink); }
.actions a.secondary, .actions button.secondary { padding: 9px 12px; border-radius: 10px; font-size: 12px; }
.empty { color: var(--muted); line-height: 1.55; }
.hover-card { position: fixed; z-index: 20; display: none; width: 245px; padding: 11px 13px; border: 1px solid var(--line); border-radius: 12px; background: var(--float-bg); box-shadow: var(--shadow); pointer-events: none; }
.hover-card.visible { display: block; }
.hover-card strong { display: block; }
.hover-card span { display: block; margin-top: 3px; color: var(--muted); font-size: 12px; }
@media (max-width: 920px) { html, body { height: auto; min-height: 100%; } body { overflow: auto; } .layout { height: auto; overflow: visible; grid-template-columns: 190px minmax(0, 1fr); grid-template-rows: minmax(560px, 75vh) auto; } .detail.panel { grid-column: 1 / -1; height: min(680px, 80vh); min-height: 360px; } }
@media (max-width: 640px) { body { display: block; } header { flex-wrap: wrap; } .layout { display: block; } .panel { margin-bottom: 12px; } .list-panel { height: 520px; } .board-panel { height: 70vh; min-height: 400px; } }
html[data-theme="rainbow"] header { background: var(--rainbow); }
html[data-theme="rainbow"] .panel { border: 1px solid transparent; background: linear-gradient(var(--panel), var(--panel)) padding-box, var(--rainbow) border-box; }
html[data-theme="rainbow"] .actions a { background: linear-gradient(135deg, #ff5c35, #ff8a00); }
html[data-theme="rainbow"] .actions a.secondary, html[data-theme="rainbow"] .actions button.secondary { background: var(--accent-soft); color: var(--ink); }
html[data-theme="rainbow"] .category-group > summary::before { color: #ff5c35; }
html[data-theme="rainbow"] .layer-swatch { box-shadow: 0 0 0 1px rgba(0, 0, 0, .18); }
html[data-theme="rainbow"] .board-view > svg, html[data-theme="rainbow"] .schematic-view > svg { filter: drop-shadow(0 9px 13px rgba(157, 78, 221, .22)); }
html[data-theme="rainbow"] .eyebrow { color: #9d4edd; }
html[data-theme="rainbow"] .side-button:hover, html[data-theme="rainbow"] .side-button.active { background: var(--accent); }
html[data-theme="rainbow"] .zoom-button:hover { color: #9d4edd; }
html[data-theme="rainbow"] .schematic-view .sch-pin { stroke: #9333ea; }
"""


def _script():
    return r"""
const components = JSON.parse(document.getElementById('component-data').textContent);
const copper = JSON.parse(document.getElementById('copper-data').textContent);
const byNet = new Map(copper.nets.map(net => [net.id, net]));
const byReference = new Map(components.map(component => [component.reference, component]));
const list = document.getElementById('part-list');
const detail = document.getElementById('detail');
const search = document.getElementById('search');
const stage = document.getElementById('board-stage');
const hoverCard = document.getElementById('hover-card');
let activeReference = '';
let activeSide = 'front';
let zoomScale = 1;
let mousePan = null;
let touchPan = null;
let suppressBoardClick = false;
const activePointers = new Map();
let activeNet = '';
let activePin = null;
const selectedReferences = new Set();
const selectedPins = [];
const collapsedCategories = new Set(components.map(component => component.category));
const highlightSelectedNets = document.getElementById('highlight-selected-nets');
const expandedReferences = new Set();
const layerSelect = document.getElementById('copper-layer');
const baseFeatures = [...document.querySelectorAll('.copper-base .copper-feature')];
const boardViewports = new Map();
document.querySelectorAll('.board-view > svg').forEach(svg => {
  const originalText = svg.getAttribute('viewBox');
  const original = originalText.split(/\s+/).map(Number);
  boardViewports.set(svg, {original, originalText, target: [...original], box: [...original], scale: 1});
});
const schematicView = document.getElementById('schematic-view');
const schematicSvg = schematicView ? schematicView.querySelector('svg') : null;
if (schematicSvg) {
  const originalText = schematicSvg.getAttribute('viewBox');
  const original = originalText.split(/\s+/).map(Number);
  boardViewports.set(schematicSvg, {original, originalText, target: [...original], box: [...original], scale: 1});
}
// Schematic wires and labels are tagged with plain net names; the copper data
// keys its nets by id, so keep the bridge handy in both directions.
const netIdByName = new Map(copper.nets.map(net => [net.name, net.id]));
// Unlabelled sheet runs only carry a run id; their copper net is recovered
// through any pin sitting on the run (the part's PCB pad knows its net).
const padNetByPin = new Map();
components.forEach(component => {
  for (const pad of component.pads) {
    if (pad.net) padNetByPin.set(`${component.reference}.${pad.number}`, pad.net);
  }
});
const runNetByName = new Map();
if (schematicSvg) {
  schematicSvg.querySelectorAll('.sch-pin-hit[data-run]').forEach(element => {
    const padNet = padNetByPin.get(`${element.dataset.reference}.${element.dataset.pin}`);
    if (padNet && !runNetByName.has(element.dataset.run)) runNetByName.set(element.dataset.run, padNet);
  });
}
const schematicNetElements = schematicSvg ? [...schematicSvg.querySelectorAll('[data-net], [data-run]')] : [];
const schematicSymbols = schematicSvg ? [...schematicSvg.querySelectorAll('.sch-symbol')] : [];
let manualSchematicRun = '';
// Explicit editable colours for the common stack; additional internal layers
// get evenly spaced hues without changing the familiar front/back colours.
const layerColors = {'F.Cu': 'var(--copper-front)', 'B.Cu': 'var(--copper-back)',
  'In1.Cu': 'var(--copper-inner-1)', 'In2.Cu': 'var(--copper-inner-2)'};
copper.layers.forEach((layer, index) => {
  if (!layerColors[layer]) layerColors[layer] = `hsl(${(index * 137.5) % 360} 65% 38%)`;
});

function layerColor(element) {
  const layers = element.dataset.layers.split(' ');
  const requested = layerSelect.value === 'side' ? (activeSide === 'back' ? 'B.Cu' : 'F.Cu') : layerSelect.value;
  if (requested !== 'all' && layers.includes(requested)) return layerColors[requested];
  return layers.length === 1 ? layerColors[layers[0]] : 'var(--copper-multilayer)';
}

function renderLayerLegend() {
  const legend = document.getElementById('layer-legend');
  legend.replaceChildren();
  const items = copper.layers.map(layer => [layer, layerColors[layer]]);
  items.push(['Via / through-hole', 'var(--copper-multilayer)']);
  items.push(['Selected pin', 'var(--selected-pin)']);
  for (const [label, color] of items) {
    const key = document.createElement('span');
    key.className = 'layer-key';
    key.style.setProperty('--layer-color', color);
    const swatch = document.createElement('span');
    swatch.className = 'layer-swatch';
    key.append(swatch, document.createTextNode(label));
    legend.appendChild(key);
  }
}

function escapeHtml(value) {
  return String(value ?? '').replace(/[&<>'"]/g, character => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[character]));
}

function additiveClick(event) {
  return event.ctrlKey || event.metaKey;
}

function selectedPinIndex(reference, number, netId) {
  for (let index = 0; index < selectedPins.length; index++) {
    const pin = selectedPins[index];
    if (pin.reference === reference && pin.number === number && pin.net_id === (netId || '')) return index;
  }
  return -1;
}

function syncActivePin() {
  activePin = selectedPins.length ? selectedPins[selectedPins.length - 1] : null;
  activeNet = selectedPins.length === 1 ? selectedPins[0].net_id : '';
}

function toggleCategory(category) {
  const members = components.filter(component => component.category === category);
  const deselect = members.every(component => selectedReferences.has(component.reference));
  for (const component of members) {
    if (deselect) selectedReferences.delete(component.reference);
    else selectedReferences.add(component.reference);
  }
  selectionChanged(true);
}

function toggleComponent(reference) {
  if (selectedReferences.has(reference)) selectedReferences.delete(reference);
  else selectedReferences.add(reference);
  activeReference = reference;
  selectionChanged(true);
}

function renderList(filterText = '') {
  const filter = filterText.trim().toLowerCase();
  const scrollTop = list.scrollTop;
  list.innerHTML = '';
  // Net names are searchable in the main box; matching nets lead the results
  // so a typed name can be followed straight from the list.
  if (filter) {
    const matchingNets = copper.nets.filter(net => net.name.toLowerCase().includes(filter));
    if (matchingNets.length) {
      const group = document.createElement('details');
      group.className = 'category-group net-group';
      group.open = true;
      const heading = document.createElement('summary');
      const title = document.createElement('span');
      title.textContent = 'Nets';
      const count = document.createElement('small');
      count.textContent = `${matchingNets.length}`;
      heading.append(title, count);
      group.appendChild(heading);
      const body = document.createElement('div');
      body.className = 'net-results';
      for (const net of matchingNets) {
        const netButton = document.createElement('button');
        netButton.type = 'button';
        netButton.className = 'net-link' + (net.id === activeNet ? ' on-net' : '');
        netButton.dataset.netId = net.id;
        netButton.innerHTML = `${escapeHtml(net.name)}<small>${net.pins.length} pins · ${net.track_count} traces</small>`;
        netButton.addEventListener('click', () => toggleNet(net.id));
        body.appendChild(netButton);
      }
      group.appendChild(body);
      list.appendChild(group);
    }
  }
  const groups = new Map();
  const visible = components.filter(component => {
    const haystack = [component.reference, component.value, component.category, component.category_name, component.oomp_id, component.footprint, ...component.pads.map(pin => `${pin.number} ${pin.name} ${pin.net}`)].join(' ').toLowerCase();
    return component.side === activeSide && haystack.includes(filter);
  });
  for (const component of visible) {
    if (!groups.has(component.category)) groups.set(component.category, []);
    groups.get(component.category).push(component);
  }
  for (const [category, members] of [...groups].sort((a, b) => a[0].localeCompare(b[0]))) {
    const allMembers = components.filter(component => component.category === category);
    const selectedCount = allMembers.filter(component => selectedReferences.has(component.reference)).length;
    const group = document.createElement('details');
    group.className = 'category-group';
    group.dataset.category = category;
    group.open = !!filter || !collapsedCategories.has(category);
    const heading = document.createElement('summary');
    heading.title = 'Click to expand; Ctrl-click to select or deselect this category';
    heading.addEventListener('click', event => {
      if (!additiveClick(event)) return;
      event.preventDefault();
      toggleCategory(category);
    });
    const select = document.createElement('input');
    select.type = 'checkbox';
    select.className = 'category-select';
    select.dataset.category = category;
    select.checked = selectedCount === allMembers.length;
    select.indeterminate = selectedCount > 0 && selectedCount < allMembers.length;
    select.setAttribute('aria-label', `Select all ${members[0].category_name} components on both sides`);
    select.addEventListener('click', event => event.stopPropagation());
    select.addEventListener('change', () => {
      for (const component of allMembers) {
        if (select.checked) selectedReferences.add(component.reference);
        else selectedReferences.delete(component.reference);
      }
      selectionChanged(true);
    });
    heading.appendChild(select);
    const title = document.createElement('span');
    title.textContent = members[0].category_name;
    heading.appendChild(title);
    const count = document.createElement('small');
    count.textContent = `${selectedCount}/${allMembers.length}`;
    count.title = `${selectedCount} selected of ${allMembers.length} on both sides; ${members.length} visible`;
    heading.appendChild(count);
    group.appendChild(heading);
    group.addEventListener('toggle', () => {
      if (filter) return;
      if (group.open) collapsedCategories.delete(category);
      else collapsedCategories.add(category);
    });
    for (const component of members) {
    const row = document.createElement('div');
    row.className = 'part-row';
    const selectPart = document.createElement('input');
    selectPart.type = 'checkbox';
    selectPart.className = 'part-select';
    selectPart.dataset.reference = component.reference;
    selectPart.checked = selectedReferences.has(component.reference);
    selectPart.setAttribute('aria-label', `Select ${component.reference}`);
    selectPart.addEventListener('change', () => {
      if (selectPart.checked) selectedReferences.add(component.reference);
      else selectedReferences.delete(component.reference);
      selectionChanged(true);
    });
    row.appendChild(selectPart);
    const button = document.createElement('button');
    button.className = 'part-button' + (component.reference === activeReference ? ' active' : '') + (selectedReferences.has(component.reference) ? ' selected' : '');
    button.dataset.reference = component.reference;
    button.innerHTML = `<strong>${escapeHtml(component.reference)}</strong><span>${escapeHtml(component.value || 'unlabelled')}</span><span class="oomp-id">${escapeHtml(component.oomp_id || 'unmatched')}</span>`;
    button.setAttribute('aria-pressed', selectedReferences.has(component.reference));
    button.addEventListener('click', event => {
      if (additiveClick(event)) toggleComponent(component.reference);
      else selectComponent(component.reference);
    });
    row.appendChild(button);
    if (component.part_url) {
      const link = document.createElement('a');
      link.className = 'part-link';
      link.href = component.part_url;
      link.target = '_blank';
      link.rel = 'noopener';
      link.title = `Open ${component.oomp_id}`;
      link.textContent = '↗';
      row.appendChild(link);
    }
    const menu = document.createElement('details');
    menu.className = 'pin-menu';
    menu.open = expandedReferences.has(component.reference);
    const summary = document.createElement('summary');
    summary.textContent = `Pins · ${component.pads.length}`;
    summary.title = 'Click to expand; Ctrl-click to select or deselect all pins';
    summary.addEventListener('click', event => {
      if (!additiveClick(event)) return;
      event.preventDefault();
      toggleComponentPins(component.reference);
    });
    menu.appendChild(summary);
    const body = document.createElement('div');
    body.className = 'pin-menu-body';
    component.pads.forEach(pin => {
      const pinButton = document.createElement('button');
      pinButton.type = 'button';
      pinButton.className = pinClass(component, pin);
      pinButton.dataset.pin = pin.number;
      pinButton.dataset.reference = component.reference;
      pinButton.innerHTML = `${escapeHtml(pin.number || 'Pad')} · ${escapeHtml(pin.name || 'unnamed')}<small>${escapeHtml(pin.net || 'No assigned net')}</small>`;
      pinButton.setAttribute('aria-pressed', selectedPinIndex(component.reference, pin.number, pin.net_id) >= 0);
      pinButton.addEventListener('click', event => selectPin(component.reference, pin.number, pin.net_id, additiveClick(event)));
      body.appendChild(pinButton);
    });
    menu.appendChild(body);
    menu.addEventListener('toggle', () => {
      if (menu.open) expandedReferences.add(component.reference);
      else expandedReferences.delete(component.reference);
    });
    row.appendChild(menu);
    group.appendChild(row);
    }
    list.appendChild(group);
  }
  list.scrollTop = scrollTop;
}

function highlightedNetIds() {
  const ids = new Set();
  if (highlightSelectedNets.checked) {
    for (const reference of selectedReferences) {
      for (const pin of byReference.get(reference).pads) {
        if (pin.net_id && byNet.has(pin.net_id)) ids.add(pin.net_id);
      }
    }
  } else if (byNet.has(activeNet)) ids.add(activeNet);
  for (const pin of selectedPins) {
    if (byNet.has(pin.net_id)) ids.add(pin.net_id);
  }
  return ids;
}

function renderInitialDetail() {
  detail.innerHTML = '<p class="empty">Choose a component to inspect its placement, OOMP match and pins.</p>';
}

function refreshDetail() {
  const component = byReference.get(activeReference);
  if (component) renderDetail(component);
  else renderInitialDetail();
}

function selectionChanged(preservePins = false) {
  if (!preservePins) {
    selectedPins.length = 0;
    activeNet = '';
    activePin = null;
  }
  updateSelectionBoxes();
  updateNetHighlight();
  renderList(search.value);
  refreshDetail();
}

function pinClass(component, pin) {
  const selected = selectedPinIndex(component.reference, pin.number, pin.net_id) >= 0;
  return 'pin-button' + (highlightedNetIds().has(pin.net_id) ? ' on-net' : '') + (selected ? ' selected-pin' : '');
}

function pinRows(component) {
  if (!component.pads.length) return '<p class="empty">No PCB pads were extracted for this item.</p>';
  return `<table class="pin-table"><thead><tr><th>Pin</th><th>Name</th><th>Net</th></tr></thead><tbody>${component.pads.map((pin, index) => `<tr><td><button class="${pinClass(component, pin)}" data-pin-index="${index}">${escapeHtml(pin.number || 'Pad')}</button></td><td>${escapeHtml(pin.name || '—')}</td><td>${pin.net_id ? `<button class="net-link${activeNet === pin.net_id ? ' on-net' : ''}" data-net-id="${escapeHtml(pin.net_id)}">${escapeHtml(pin.net)}</button>` : 'No net'}</td></tr>`).join('')}</tbody></table>`;
}

function renderDetail(component) {
  const position = component.position || {};
  const match = component.oomp_id ? 'Matched OOMP part' : 'Needs OOMP match';
  const lcscAction = component.lcsc_options && component.lcsc_options.length > 1
    ? `<button class="secondary lcsc-link" type="button" data-reference="${escapeHtml(component.reference)}" title="Choose between ${component.lcsc_options.length} LCSC options">LCSC options (${component.lcsc_options.length})</button>`
    : component.lcsc_url ? `<a class="secondary lcsc-link" href="${escapeHtml(component.lcsc_url)}" target="_blank" rel="noopener noreferrer" title="${escapeHtml(component.lcsc_part_number)}">Open LCSC</a>` : '';
  const lcscSearch = component.lcsc_search || '';
  const searchAction = lcscSearch
    ? `<a class="secondary" href="https://www.lcsc.com/search?q=${encodeURIComponent(lcscSearch)}" target="_blank" rel="noopener noreferrer" title="LCSC search: ${escapeHtml(lcscSearch)}">Search LCSC</a>` : '';
  const actions = [
    component.part_url ? `<a href="${escapeHtml(component.part_url)}" target="_blank" rel="noopener">Open OOMP part</a>` : '',
    lcscAction,
    searchAction,
    component.supplier ? `<a class="secondary" href="${escapeHtml(component.supplier)}" target="_blank" rel="noopener">Supplier source</a>` : ''
  ].join('');
  detail.innerHTML = `
    <div class="eyebrow">${escapeHtml(match)}</div>
    <h2>${escapeHtml(component.reference)}</h2>
    <div class="value">${escapeHtml(component.value || 'No value')}</div>
    <dl class="facts">
      <dt>OOMP</dt><dd>${escapeHtml(component.oomp_id || 'unmatched')}</dd>
      <dt>Category</dt><dd>${escapeHtml(component.category_name)}${component.category_source === 'unmatched_kicad_hint' ? ' (KiCad hint)' : ''}</dd>
      <dt>Footprint</dt><dd>${escapeHtml(component.footprint || '—')}</dd>
      <dt>LCSC search</dt><dd>${escapeHtml(lcscSearch || '—')}</dd>
      <dt>Side</dt><dd>${escapeHtml(component.side || '—')}</dd>
      <dt>Position</dt><dd>${escapeHtml(position.x ?? '—')}, ${escapeHtml(position.y ?? '—')} mm</dd>
      <dt>Rotation</dt><dd>${escapeHtml(position.rotation_kicad ?? position.rotation ?? '—')}°</dd>
    </dl>
    <div class="actions">${actions}</div>
    ${component.symbol_svg ? `<div class="eyebrow">Schematic symbol</div><div class="pinout sch-preview">${component.symbol_svg}</div>` : ''}
    <div class="eyebrow">Pinout</div>
    ${component.pinout_svg ? `<div class="pinout">${component.pinout_svg}</div>` : ''}
    ${pinRows(component)}`;
}

const lcscPopup = document.getElementById('lcsc-popup');

function openLcscPopup(component) {
  const rows = (component.lcsc_options || []).map(option =>
    `<a class="popup-row" href="${escapeHtml(option.url)}" target="_blank" rel="noopener noreferrer">` +
    `<span class="popup-name">${escapeHtml(option.product_name || 'LCSC option')}</span>` +
    `<span class="popup-number">${escapeHtml(option.part_number)}</span></a>`).join('');
  lcscPopup.innerHTML = `<div class="popup-card" role="dialog" aria-label="LCSC options">` +
    `<div class="popup-head"><strong>LCSC options · ${escapeHtml(component.reference)}</strong>` +
    `<button class="popup-close" type="button" aria-label="Close">&times;</button></div>${rows}</div>`;
  lcscPopup.hidden = false;
}

function closeLcscPopup() {
  lcscPopup.hidden = true;
}

lcscPopup.addEventListener('click', event => {
  if (event.target === lcscPopup || event.target.closest('.popup-close')) closeLcscPopup();
});

detail.addEventListener('click', event => {
  const button = event.target.closest('button.lcsc-link');
  if (!button) return;
  const component = byReference.get(button.dataset.reference);
  if (component && (component.lcsc_options || []).length > 1) openLcscPopup(component);
});

function selectComponent(reference, preserveNet = false, expandCategory = true) {
  const component = byReference.get(reference);
  if (!component) return;
  // Selection never flips the board view; components on the hidden side stay
  // reachable through the side buttons instead.
  // Clicking a selected component (list button, board artwork or Enter)
  // deselects it, keeping any other selections intact.
  if (!preserveNet && selectedReferences.has(reference)) {
    selectedReferences.delete(reference);
    if (activeReference === reference) activeReference = [...selectedReferences][0] || '';
    selectionChanged();
    return;
  }
  activeReference = reference;
  if (expandCategory) collapsedCategories.delete(component.category);
  if (!selectedReferences.has(reference)) {
    selectedReferences.clear();
    selectedReferences.add(reference);
  }
  if (!preserveNet) { activeNet = ''; activePin = null; selectedPins.length = 0; }
  updateSelectionBoxes();
  renderDetail(component);
  renderList(search.value);
  updateNetHighlight();
}

function selectPin(reference, number, netId, additive = false) {
  // Clicking a pin that is already selected deselects it again, whichever
  // surface the click came from; its part stays populated in the detail pane.
  const index = selectedPinIndex(reference, number, netId);
  if (index >= 0) {
    selectedPins.splice(index, 1);
    syncActivePin();
    selectionChanged(true);
    return;
  }
  if (!additive) {
    highlightSelectedNets.checked = false;
    selectedPins.length = 0;
  }
  selectedPins.push({reference, number, net_id: netId || ''});
  syncActivePin();
  expandedReferences.add(reference);
  // A pin selection always populates its owning part in the detail pane.
  const component = byReference.get(reference);
  if (component) {
    activeReference = reference;
    collapsedCategories.delete(component.category);
    // Additive clicks only borrow the detail pane; the component selection
    // itself is untouched so grouped selections survive.
    if (!additive && !selectedReferences.has(reference)) {
      selectedReferences.clear();
      selectedReferences.add(reference);
    }
  }
  selectionChanged(true);
}

function toggleComponentPins(reference) {
  const component = byReference.get(reference);
  const deselect = component.pads.every(pin => selectedPinIndex(reference, pin.number, pin.net_id) >= 0);
  for (const pin of component.pads) {
    const index = selectedPinIndex(reference, pin.number, pin.net_id);
    if (deselect && index >= 0) selectedPins.splice(index, 1);
    else if (!deselect && index < 0) selectedPins.push({reference, number: pin.number, net_id: pin.net_id || ''});
  }
  syncActivePin();
  activeReference = reference;
  selectionChanged(true);
}

function toggleNet(netId) {
  selectNet(activeNet === netId ? '' : netId);
}

function selectNet(netId) {
  highlightSelectedNets.checked = false;
  manualSchematicRun = '';
  activeNet = byNet.has(netId) ? netId : '';
  activePin = null;
  selectedPins.length = 0;
  if (activeNet) {
    // Following copper keeps the selected part when it sits on that net and
    // otherwise shows one of the parts the copper connects to.
    const net = byNet.get(activeNet);
    const current = byReference.get(activeReference);
    const connected = current && net.pins.some(pin => pin.reference === current.reference);
    if (!connected) {
      // Prefer a part on the shown side so the detail pane follows copper to a
      // part that is actually visible; the board view itself never flips.
      const pins = net.pins.filter(pin => byReference.has(pin.reference));
      const candidate = pins.find(pin => byReference.get(pin.reference).side === activeSide) || pins[0];
      if (candidate) {
        const component = byReference.get(candidate.reference);
        activeReference = candidate.reference;
        selectedReferences.clear();
        selectedReferences.add(candidate.reference);
        collapsedCategories.delete(component.category);
      }
    }
  }
  updateSelectionBoxes();
  updateNetHighlight();
  renderList(search.value);
  refreshDetail();
}

function matchingSummary() {
  // The catch-all "other" bucket says nothing about matching progress, so the
  // summary counts real component categories only.
  const counted = components.filter(component => component.category !== 'other');
  const categories = new Map();
  for (const component of counted) {
    if (!categories.has(component.category_name)) categories.set(component.category_name, {total: 0, matched: 0});
    const entry = categories.get(component.category_name);
    entry.total += 1;
    if (component.oomp_id) entry.matched += 1;
  }
  const rows = [...categories.entries()].sort((a, b) => b[1].total - a[1].total || a[0].localeCompare(b[0]));
  const total = counted.length;
  const matched = counted.filter(component => component.oomp_id).length;
  const percent = total ? Math.round((matched / total) * 100) : 0;
  return `<strong>OOMP matching</strong> ${matched}/${total} matched · ${percent}%<div class="match-rows">${rows.map(([name, entry]) => `<span>${escapeHtml(name)} <b>${entry.matched}/${entry.total}</b></span>`).join('')}</div><span class="net-note">Filter and click a component to inspect it; search a net name to follow its copper.</span>`;
}

function featureVisible(element) {
  const layer = layerSelect.value;
  const selectedLayer = layer === 'side' ? (activeSide === 'back' ? 'B.Cu' : 'F.Cu') : layer;
  return layer === 'all' || element.dataset.layers.split(' ').includes(selectedLayer);
}

function updateNetHighlight() {
  const net = byNet.get(activeNet);
  const netIds = highlightedNetIds();
  const connectedReferences = new Set();
  for (const id of netIds) {
    for (const pin of byNet.get(id).pins) connectedReferences.add(pin.reference);
  }
  const fills = document.getElementById('show-fills').checked;
  stage.classList.toggle('has-net', netIds.size > 0);
  stage.classList.toggle('hide-traces', !document.getElementById('show-traces').checked);
  baseFeatures.forEach(element => {
    element.classList.toggle('layer-hidden', !featureVisible(element));
    element.classList.toggle('fill-hidden', element.classList.contains('copper-zone') && !fills);
  });
  document.querySelectorAll('.copper-overlay').forEach(overlay => {
    overlay.replaceChildren();
    const base = overlay.closest('svg').querySelector('.copper-base');
    base.querySelectorAll('.copper-feature').forEach(element => {
      const selectedPin = element.classList.contains('copper-pad') && selectedPinIndex(element.dataset.reference, element.dataset.pin, element.dataset.netId) >= 0;
      if (!netIds.has(element.dataset.netId) && !selectedPin) return;
      const clone = element.cloneNode(true);
      clone.style.setProperty('--layer-color', layerColor(element));
      clone.classList.toggle('selected-pin', !!selectedPin);
      overlay.appendChild(clone);
    });
  });
  document.querySelectorAll('.board-component').forEach(element => {
    element.classList.toggle('on-net', connectedReferences.has(element.dataset.reference));
  });
  // The sheet mirrors the copper: same net names light the wires, labels and
  // symbols; unlabelled runs join through the copper net their pins share.
  if (schematicSvg) {
    const netNames = new Set([...netIds].map(id => byNet.get(id).name));
    schematicNetElements.forEach(element => {
      const name = element.dataset.net || runNetByName.get(element.dataset.run) || '';
      element.classList.toggle('on-net', !!name && netNames.has(name));
    });
    if (manualSchematicRun) {
      schematicNetElements.forEach(element => {
        if (element.dataset.run === manualSchematicRun) element.classList.add('on-net');
      });
    }
    schematicSymbols.forEach(element => {
      element.classList.toggle('on-net', connectedReferences.has(element.dataset.reference));
    });
    schematicView.classList.toggle('has-net', netIds.size > 0 || !!manualSchematicRun);
  }
  const status = document.getElementById('net-status');
  if (highlightSelectedNets.checked || selectedPins.length > 1) {
    const selectionLabel = highlightSelectedNets.checked ? `${selectedReferences.size} components · ${selectedPins.length} pins` : `${selectedPins.length} selected pins`;
    status.innerHTML = `<strong>${selectionLabel} · ${netIds.size} nets</strong><br><span class="net-note">All connected pins and copper on the shown layers. Click a net below to follow it alone.</span><div>${[...netIds].map(id => `<button class="net-link" data-net-id="${escapeHtml(id)}">${escapeHtml(byNet.get(id).name)}</button>`).join(' ')}</div>`;
  } else if (net) {
    const visiblePins = net.pins.filter(pin => layerSelect.value === 'all' || pin.layers.includes(layerSelect.value === 'side' ? (activeSide === 'back' ? 'B.Cu' : 'F.Cu') : layerSelect.value));
    status.innerHTML = `<strong>${escapeHtml(net.name)}</strong><br>${net.track_count} traces · ${net.via_count} vias · ${net.fill_count} saved fills<br>${visiblePins.length} / ${net.pins.length} pins on shown layers<br><span class="net-note">${escapeHtml(net.layers.join(' · '))}</span><div>${net.pins.map(pin => byReference.has(pin.reference) ? `<button class="net-link" data-reference="${escapeHtml(pin.reference)}" data-pin="${escapeHtml(pin.number)}">${escapeHtml(pin.reference)}.${escapeHtml(pin.number || 'pad')}</button>` : `<span>${escapeHtml(pin.reference)}.${escapeHtml(pin.number)} (not in BOM) </span>`).join('')}</div>`;
  } else if (activePin) {
    status.textContent = `${activePin.reference}.${activePin.number}: no assigned net; only this pin is highlighted.`;
  } else if (activeReference && byReference.has(activeReference)) {
    const component = byReference.get(activeReference);
    status.innerHTML = `<strong>${escapeHtml(component.reference)}</strong> selected · ${escapeHtml(component.oomp_id || 'no OOMP match yet')}<br><span class="net-note">Expand Pins or click a net name to follow its copper. Click the component again to deselect it.</span>`;
  } else {
    status.innerHTML = matchingSummary();
  }
  if (document.getElementById('zoom-to-net').checked) fitSelectedNet();
}

function updateSelectionBoxes() {
  document.querySelectorAll('.component-highlights').forEach(layer => layer.replaceChildren());
  stage.classList.toggle('has-selection', selectedReferences.size > 0);
  if (schematicSvg) {
    schematicView.classList.toggle('has-selection', selectedReferences.size > 0);
    schematicSymbols.forEach(element => {
      element.classList.toggle('is-active', selectedReferences.has(element.dataset.reference));
    });
  }
  // Symbols get the same accent rectangle treatment as board parts: the sheet
  // drawing itself never changes colour, selected or not.
  if (schematicSvg && !schematicView.hidden) {
    let symbolLayer = schematicSvg.querySelector('.component-highlights');
    if (!symbolLayer) {
      symbolLayer = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      symbolLayer.setAttribute('class', 'component-highlights');
      schematicSvg.appendChild(symbolLayer);
    }
    schematicSymbols.forEach(element => {
      const selected = selectedReferences.has(element.dataset.reference);
      if (!selected && !element.matches(':hover') && !element.matches(':focus')) return;
      // The generator records the tight body rectangle; the group's own bbox
      // would stretch over pin stubs and the label block.
      const boundsData = (element.dataset.bounds || '').split(',').map(Number);
      let bx, by, bw, bh;
      if (boundsData.length === 4 && boundsData.every(value => Number.isFinite(value))) {
        [bx, by, bw, bh] = boundsData;
      } else {
        const bounds = element.getBBox();
        if (!(bounds.width > 0) && !(bounds.height > 0)) return;
        bx = bounds.x; by = bounds.y; bw = bounds.width; bh = bounds.height;
      }
      const box = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      box.setAttribute('class', selected ? 'selection-box' : 'hover-box');
      box.dataset.reference = element.dataset.reference;
      box.setAttribute('x', bx);
      box.setAttribute('y', by);
      box.setAttribute('width', bw);
      box.setAttribute('height', bh);
      box.setAttribute('rx', '0.3');
      symbolLayer.appendChild(box);
    });
  }
  document.querySelectorAll('.board-component').forEach(element => {
    const selected = selectedReferences.has(element.dataset.reference);
    element.classList.toggle('is-active', selected);
    if (!selected && !element.matches(':hover') && !element.matches(':focus')) return;
    const layer = element.closest('.board-view').querySelector('.component-highlights');
    if (!layer) return;
    const bounds = element.getBBox();
    const pad = Math.max(0.7, Math.min(bounds.width, bounds.height) * 0.18);
    const boxWidth = Math.max(bounds.width + pad * 2, 2.4);
    const boxHeight = Math.max(bounds.height + pad * 2, 2.4);
    const box = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    box.setAttribute('class', selected ? 'selection-box' : 'hover-box');
    box.dataset.reference = element.dataset.reference;
    // The generator emits each component and this underlay in board coordinates.
    // Copy its placement, including the bottom-side position and rotation.
    box.setAttribute('transform', element.getAttribute('transform') || '');
    box.setAttribute('x', bounds.x + bounds.width / 2 - boxWidth / 2);
    box.setAttribute('y', bounds.y + bounds.height / 2 - boxHeight / 2);
    box.setAttribute('width', boxWidth);
    box.setAttribute('height', boxHeight);
    box.setAttribute('rx', '0.15');
    layer.appendChild(box);
  });
}

function activeBoardSvg(clientX = null, clientY = null) {
  // In split view the pointer decides which half zooms and pans: wheel or
  // drag over the board moves the board, over the sheet moves the sheet.
  if (clientX !== null && stage.classList.contains('split')) {
    for (const view of document.querySelectorAll('.board-view:not([hidden]), .schematic-view:not([hidden])')) {
      const rect = view.getBoundingClientRect();
      if (clientX >= rect.left && clientX <= rect.right && clientY >= rect.top && clientY <= rect.bottom) {
        return view.querySelector('svg');
      }
    }
  }
  return document.querySelector('.board-view:not([hidden]) > svg, .schematic-view:not([hidden]) > svg');
}

let activeView = 'board';

function setView(view) {
  // The schematic needs no side flipping, so side buttons are board-only:
  // pressing one while the sheet is shown returns to the board drawing.
  activeView = ['board', 'schematic', 'split'].includes(view) && schematicView ? view : 'board';
  stage.classList.toggle('split', activeView === 'split');
  document.querySelectorAll('.board-view').forEach(viewElement => {
    viewElement.hidden = activeView === 'schematic' || (activeView === 'split' && viewElement.dataset.side !== activeSide);
  });
  if (schematicView) schematicView.hidden = activeView === 'board';
  document.querySelectorAll('.view-button').forEach(button => button.classList.toggle('active', button.dataset.view === activeView));
  const viewport = boardViewports.get(activeBoardSvg());
  zoomScale = viewport ? viewport.scale || 1 : 1;
  updateZoomLabel();
}

function applyViewport(svg, viewport) {
  // Restoring the fit view reuses the source viewBox text so regeneration
  // stays byte-identical; Number formatting would drop trailing zeros.
  const isOriginal = viewport.box.every((value, index) => value === viewport.original[index]);
  svg.setAttribute('viewBox', isOriginal ? viewport.originalText : viewport.box.join(' '));
}

function updateZoomLabel() {
  document.getElementById('zoom-label').textContent = `${Math.round(zoomScale * 100)}%`;
}

function clientPointInSvg(svg, clientX, clientY) {
  const matrix = svg.getScreenCTM();
  if (!matrix) return null;
  return new DOMPoint(clientX, clientY).matrixTransform(matrix.inverse());
}

function setZoom(nextZoom, clientX = null, clientY = null) {
  const svg = activeBoardSvg(clientX, clientY);
  if (!svg) return;
  const viewport = boardViewports.get(svg);
  const next = Math.max(0.5, Math.min(12, nextZoom));
  const previous = viewport.scale || 1;
  if (Math.abs(next - previous) < 0.0001) return;
  let anchor = null;
  if (Number.isFinite(clientX) && Number.isFinite(clientY)) {
    anchor = clientPointInSvg(svg, clientX, clientY);
  }
  const [x, y, width, height] = viewport.box;
  if (!anchor) anchor = new DOMPoint(x + width / 2, y + height / 2);
  const ratio = previous / next;
  viewport.box = [
    anchor.x - (anchor.x - x) * ratio,
    anchor.y - (anchor.y - y) * ratio,
    width * ratio,
    height * ratio,
  ];
  viewport.scale = next;
  zoomScale = next;
  applyViewport(svg, viewport);
  updateZoomLabel();
}

function fitBoard() {
  boardViewports.forEach((viewport, svg) => {
    viewport.target = [...viewport.original];
    viewport.box = [...viewport.original];
    viewport.scale = 1;
    applyViewport(svg, viewport);
  });
  zoomScale = 1;
  updateZoomLabel();
}

function panActiveBoard(fromX, fromY, toX, toY) {
  const svg = activeBoardSvg(fromX, fromY);
  if (!svg) return;
  const start = clientPointInSvg(svg, fromX, fromY);
  const end = clientPointInSvg(svg, toX, toY);
  if (!start || !end) return;
  const viewport = boardViewports.get(svg);
  viewport.box[0] -= end.x - start.x;
  viewport.box[1] -= end.y - start.y;
  applyViewport(svg, viewport);
}

function touchCentroid() {
  const points = [...activePointers.values()];
  if (points.length < 2) return null;
  return {
    x: (points[0].x + points[1].x) / 2,
    y: (points[0].y + points[1].y) / 2,
  };
}

function fitSelectedNet() {
  if (!highlightedNetIds().size) { fitBoard(); return; }
  const view = document.querySelector('.board-view:not([hidden])');
  const svg = view.querySelector(':scope > svg');
  const elements = view.querySelectorAll('.copper-overlay .copper-feature:not(.layer-hidden):not(.fill-hidden)');
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  for (const element of elements) {
    const box = element.getBBox();
    // Convert through the SVG matrices so the bottom reflection is included,
    // but current screen size and zoom never contaminate PCB millimetres.
    const matrix = svg.getCTM().inverse().multiply(element.getCTM());
    const corners = [[box.x, box.y], [box.x + box.width, box.y],
      [box.x, box.y + box.height], [box.x + box.width, box.y + box.height]];
    for (const [x, y] of corners) {
      const p = new DOMPoint(x, y).matrixTransform(matrix);
      minX = Math.min(minX, p.x); minY = Math.min(minY, p.y);
      maxX = Math.max(maxX, p.x); maxY = Math.max(maxY, p.y);
    }
  }
  if (!Number.isFinite(minX)) { fitBoard(); return; }
  const pad = Math.max(.8, Math.max(maxX - minX, maxY - minY) * .12);
  const viewport = boardViewports.get(svg);
  viewport.target = [minX - pad, minY - pad, maxX - minX + pad * 2, maxY - minY + pad * 2];
  viewport.box = [...viewport.target];
  viewport.scale = 1;
  zoomScale = 1;
  applyViewport(svg, viewport);
  updateZoomLabel();
}

function setSide(side) {
  // Side flipping only makes sense on the board drawing; leaving the sheet.
  if (activeView === 'schematic') setView('board');
  activeSide = side === 'back' ? 'back' : 'front';
  document.querySelectorAll('.board-view').forEach(view => { view.hidden = view.dataset.side !== activeSide; });
  if (schematicView) schematicView.hidden = activeView !== 'split';
  document.querySelectorAll('.side-button[data-side]').forEach(button => button.classList.toggle('active', button.dataset.side === activeSide));
  const viewport = boardViewports.get(activeBoardSvg());
  zoomScale = viewport ? viewport.scale || 1 : 1;
  updateZoomLabel();
  renderList(search.value);
  updateNetHighlight();
}

function showHover(event, reference) {
  const component = byReference.get(reference);
  if (!component) return;
  hoverCard.innerHTML = `<strong>${escapeHtml(component.reference)} · ${escapeHtml(component.value || 'unlabelled')}</strong><span>${escapeHtml(component.oomp_id || 'Unmatched — click for extracted pins')}</span>`;
  hoverCard.classList.add('visible');
  moveHover(event);
}

function moveHover(event) {
  if (mousePan) return;
  const gap = 15;
  const width = 245;
  let x = event.clientX + gap;
  let y = event.clientY + gap;
  if (x + width > window.innerWidth) x = event.clientX - width - gap;
  if (y + 90 > window.innerHeight) y = event.clientY - 100;
  hoverCard.style.left = `${Math.max(8, x)}px`;
  hoverCard.style.top = `${Math.max(8, y)}px`;
}

stage.addEventListener('wheel', event => {
  event.preventDefault();
  const deltaUnit = event.deltaMode === 1 ? 16 : (event.deltaMode === 2 ? stage.clientHeight : 1);
  const exponent = Math.max(-1, Math.min(1, -event.deltaY * deltaUnit * 0.0015));
  setZoom(zoomScale * Math.exp(exponent), event.clientX, event.clientY);
}, {passive: false});

stage.addEventListener('pointerdown', event => {
  if (event.pointerType === 'touch') {
    activePointers.set(event.pointerId, {x: event.clientX, y: event.clientY});
    if (activePointers.size === 2) {
      touchPan = {last: touchCentroid(), moved: false};
      stage.classList.add('is-panning');
      hoverCard.classList.remove('visible');
      // Capture only once a two-finger pan really starts; capturing every
      // touch would retarget the tap's click to the stage and break selection.
      for (const pointerId of activePointers.keys()) {
        try { stage.setPointerCapture(pointerId); } catch (error) {}
      }
    }
    return;
  }
  if (event.button !== 0) return;
  // Deliberately no pointer capture for the mouse: capturing here retargets
  // the compat mouseup/click to the stage, so component artwork and copper
  // features would never receive clicks. Window listeners track the drag.
  mousePan = {pointerId: event.pointerId, lastX: event.clientX, lastY: event.clientY, distance: 0};
  hoverCard.classList.remove('visible');
});

window.addEventListener('pointermove', event => {
  if (event.pointerType === 'touch') {
    if (!activePointers.has(event.pointerId)) return;
    activePointers.set(event.pointerId, {x: event.clientX, y: event.clientY});
    if (!touchPan || activePointers.size !== 2) return;
    const next = touchCentroid();
    const distance = Math.hypot(next.x - touchPan.last.x, next.y - touchPan.last.y);
    if (distance > 0) {
      panActiveBoard(touchPan.last.x, touchPan.last.y, next.x, next.y);
      touchPan.last = next;
      touchPan.moved = touchPan.moved || distance > 1;
    }
    event.preventDefault();
    return;
  }
  if (!mousePan || mousePan.pointerId !== event.pointerId) return;
  const delta = Math.hypot(event.clientX - mousePan.lastX, event.clientY - mousePan.lastY);
  if (delta > 0) {
    if (mousePan.distance === 0) stage.classList.add('is-panning');
    panActiveBoard(mousePan.lastX, mousePan.lastY, event.clientX, event.clientY);
    mousePan.lastX = event.clientX;
    mousePan.lastY = event.clientY;
    mousePan.distance += delta;
  }
  event.preventDefault();
});

function finishPointerPan(event) {
  if (event.pointerType === 'touch') {
    activePointers.delete(event.pointerId);
    if (touchPan && touchPan.moved) suppressBoardClick = true;
    if (activePointers.size < 2) {
      touchPan = null;
      stage.classList.remove('is-panning');
    }
  } else if (mousePan && mousePan.pointerId === event.pointerId) {
    if (mousePan.distance > 3) suppressBoardClick = true;
    mousePan = null;
    stage.classList.remove('is-panning');
  }
  if (stage.hasPointerCapture(event.pointerId)) stage.releasePointerCapture(event.pointerId);
  if (suppressBoardClick) setTimeout(() => { suppressBoardClick = false; }, 0);
}

window.addEventListener('pointerup', finishPointerPan);
window.addEventListener('pointercancel', finishPointerPan);
stage.addEventListener('click', event => {
  if (!suppressBoardClick) return;
  event.preventDefault();
  event.stopImmediatePropagation();
  suppressBoardClick = false;
}, true);

document.querySelectorAll('.board-component').forEach(element => {
  const reference = element.dataset.reference;
  element.addEventListener('mouseenter', event => { showHover(event, reference); updateSelectionBoxes(); });
  element.addEventListener('mousemove', moveHover);
  element.addEventListener('mouseleave', () => { hoverCard.classList.remove('visible'); updateSelectionBoxes(); });
  element.addEventListener('focus', updateSelectionBoxes);
  element.addEventListener('blur', updateSelectionBoxes);
  element.addEventListener('click', event => {
    if (additiveClick(event)) toggleComponent(reference);
    else selectComponent(reference);
  });
  element.addEventListener('keydown', event => {
    if (event.key !== 'Enter' && event.key !== ' ') return;
    event.preventDefault();
    if (additiveClick(event)) toggleComponent(reference);
    else selectComponent(reference);
  });
});
search.addEventListener('input', () => renderList(search.value));
detail.addEventListener('click', event => {
  const pinButton = event.target.closest('[data-pin-index]');
  const netButton = event.target.closest('.net-link[data-net-id]');
  if (pinButton) {
    const component = byReference.get(activeReference);
    const pin = component.pads[Number(pinButton.dataset.pinIndex)];
    selectPin(component.reference, pin.number, pin.net_id, additiveClick(event));
  } else if (netButton) toggleNet(netButton.dataset.netId);
});
// The detail pane's preview boxes (pinout artwork and schematic symbol) are
// wheel-zoomable and draggable, anchored at the pointer. State lives per
// rendered box and resets naturally when a new part re-renders the pane.
const previewZooms = new WeakMap();

function applyPreviewTransform(container) {
  const svg = container.querySelector('svg');
  const state = previewZooms.get(container);
  if (!svg || !state) return;
  svg.style.transform = `translate(${state.x}px, ${state.y}px) scale(${state.s})`;
}

detail.addEventListener('wheel', event => {
  const container = event.target.closest('.pinout');
  if (!container || !container.querySelector('svg')) return;
  event.preventDefault();
  const state = previewZooms.get(container) || {s: 1, x: 0, y: 0};
  const rect = container.getBoundingClientRect();
  const anchorX = event.clientX - rect.left;
  const anchorY = event.clientY - rect.top;
  const deltaUnit = event.deltaMode === 1 ? 16 : 1;
  const factor = Math.exp(Math.max(-1, Math.min(1, -event.deltaY * deltaUnit * 0.0016)));
  const nextScale = Math.max(1, Math.min(24, state.s * factor));
  const ratio = nextScale / state.s;
  state.x = anchorX - (anchorX - state.x) * ratio;
  state.y = anchorY - (anchorY - state.y) * ratio;
  state.s = nextScale;
  if (state.s <= 1.001) { state.s = 1; state.x = 0; state.y = 0; }
  previewZooms.set(container, state);
  applyPreviewTransform(container);
}, {passive: false});

let previewPan = null;

detail.addEventListener('pointerdown', event => {
  const container = event.target.closest('.pinout');
  if (!container || !container.querySelector('svg')) return;
  const state = previewZooms.get(container) || {s: 1, x: 0, y: 0};
  previewPan = {container, startX: event.clientX - state.x, startY: event.clientY - state.y};
  container.classList.add('is-panning');
});

window.addEventListener('pointermove', event => {
  if (!previewPan) return;
  const state = previewZooms.get(previewPan.container) || {s: 1, x: 0, y: 0};
  state.x = event.clientX - previewPan.startX;
  state.y = event.clientY - previewPan.startY;
  if (state.s <= 1.001) { state.x = 0; state.y = 0; }
  previewZooms.set(previewPan.container, state);
  applyPreviewTransform(previewPan.container);
  event.preventDefault();
});

window.addEventListener('pointerup', () => {
  if (!previewPan) return;
  previewPan.container.classList.remove('is-panning');
  previewPan = null;
});
stage.addEventListener('click', event => {
  const feature = event.target.closest('.copper-feature');
  if (!feature) return;
  if (feature.classList.contains('copper-pad') && byReference.has(feature.dataset.reference)) {
    selectPin(feature.dataset.reference, feature.dataset.pin, feature.dataset.netId, additiveClick(event));
  } else selectNet(feature.dataset.netId);
});
document.getElementById('net-status').addEventListener('click', event => {
  const netButton = event.target.closest('button[data-net-id]');
  if (netButton) { toggleNet(netButton.dataset.netId); return; }
  const button = event.target.closest('button[data-reference]');
  if (!button) return;
  // Resolve the pad's real net instead of assuming the currently shown one.
  const component = byReference.get(button.dataset.reference);
  const pad = component && component.pads.find(pin => String(pin.number) === button.dataset.pin);
  selectPin(button.dataset.reference, button.dataset.pin, pad ? pad.net_id : activeNet, additiveClick(event));
});
document.getElementById('clear-selection').addEventListener('click', () => {
  selectedReferences.clear();
  activeReference = '';
  selectionChanged();
});
highlightSelectedNets.addEventListener('change', () => selectionChanged(true));
document.addEventListener('keydown', event => {
  if (event.key !== 'Escape') return;
  // Escape closes the LCSC options popup first; only then does it clear the
  // pin/net selection.
  if (!lcscPopup.hidden) {
    closeLcscPopup();
    return;
  }
  selectNet('');
});
for (const id of ['copper-layer', 'show-traces', 'show-fills']) {
  document.getElementById(id).addEventListener('change', updateNetHighlight);
}
document.getElementById('zoom-to-net').addEventListener('change', event => {
  if (event.target.checked) fitSelectedNet();
  else fitBoard();
});
document.querySelectorAll('.side-button[data-side]').forEach(button => button.addEventListener('click', () => setSide(button.dataset.side)));
document.querySelectorAll('.view-button').forEach(button => button.addEventListener('click', () => setView(button.dataset.view)));
// Sheet symbols mirror the board artwork: same hover card, same selection
// rules, so either drawing drives the same component state.
schematicSymbols.forEach(element => {
  const reference = element.dataset.reference;
  element.addEventListener('mouseenter', event => showHover(event, reference));
  element.addEventListener('mousemove', moveHover);
  element.addEventListener('mouseleave', () => hoverCard.classList.remove('visible'));
  element.addEventListener('click', event => {
    if (additiveClick(event)) toggleComponent(reference);
    else selectComponent(reference);
  });
  element.addEventListener('keydown', event => {
    if (event.key !== 'Enter' && event.key !== ' ') return;
    event.preventDefault();
    if (additiveClick(event)) toggleComponent(reference);
    else selectComponent(reference);
  });
});
if (schematicSvg) {
  schematicSvg.addEventListener('click', event => {
    const netElement = event.target.closest('[data-net], [data-run]');
    if (!netElement) return;
    // Named runs map straight to their copper net; unlabelled runs borrow the
    // net their pins carry on the PCB.  Runs with neither highlight alone.
    const name = netElement.dataset.net || runNetByName.get(netElement.dataset.run) || '';
    const netId = netIdByName.get(name);
    if (netId) {
      manualSchematicRun = '';
      toggleNet(netId);
    } else if (netElement.dataset.run) {
      manualSchematicRun = manualSchematicRun === netElement.dataset.run ? '' : netElement.dataset.run;
      updateNetHighlight();
    }
  });
  // Clicking a pin selects that pin together with the net the sheet says it
  // belongs to; the click must not also select the owning symbol.
  schematicSvg.querySelectorAll('.sch-pin-hit').forEach(element => {
    element.addEventListener('click', event => {
      event.stopPropagation();
      const pinName = `${element.dataset.reference}.${element.dataset.pin}`;
      const name = padNetByPin.get(pinName) || element.dataset.net || runNetByName.get(element.dataset.run) || '';
      const netId = netIdByName.get(name);
      if (netId) manualSchematicRun = '';
      selectPin(element.dataset.reference, element.dataset.pin, netId || '', additiveClick(event));
    });
  });
}
document.getElementById('zoom-in').addEventListener('click', () => setZoom(zoomScale + 0.25));
document.getElementById('zoom-out').addEventListener('click', () => setZoom(zoomScale - 0.25));
document.getElementById('zoom-fit').addEventListener('click', fitBoard);
document.getElementById('zoom-reset').addEventListener('click', fitBoard);
const themeSelect = document.getElementById('theme-select');
themeSelect.value = document.documentElement.dataset.theme || 'light';
// Rainbow mode gives every schematic net its own vivid hue so the sheet reads
// like wiring loom art; the other themes fall back to the single ink colour.
function schematicNetColor(name) {
  const text = String(name || '');
  let hash = 0;
  for (let index = 0; index < text.length; index++) hash = (hash * 31 + text.charCodeAt(index)) >>> 0;
  return `hsl(${hash % 360} 80% 38%)`;
}
function applyNetColors() {
  if (!schematicSvg) return;
  const rainbow = themeSelect.value === 'rainbow';
  schematicSvg.querySelectorAll('.sch-wire[data-net], .sch-label[data-net]').forEach(element => {
    if (rainbow) element.style.setProperty('--net-color', schematicNetColor(element.dataset.net));
    else element.style.removeProperty('--net-color');
  });
}
themeSelect.addEventListener('change', () => {
  const theme = ['light', 'dark', 'rainbow'].includes(themeSelect.value) ? themeSelect.value : 'light';
  document.documentElement.dataset.theme = theme;
  try { localStorage.setItem('oomp-board-theme', theme); } catch (error) {}
  applyNetColors();
});
applyNetColors();
renderLayerLegend();
setZoom(1);
// Starting unselected also means setSide's first render opens with the OOMP
// matching summary in the status box and the empty prompt in the detail pane.
setSide('front', false);
"""


def generate_board_explorer(project_directory, project_data, summary_data, output_directory=None):
    """Embed generated assets into the project part's root-level explorer."""
    project_directory = Path(project_directory).resolve()
    if output_directory is None:
        output_directory = project_directory / "data" / "generated_data"
    output_directory = Path(output_directory).resolve()
    asset_directory = output_directory / "src"
    board_path = asset_directory / "board_pins.svg"
    if not board_path.is_file():
        board_path = asset_directory / "board.svg"
    board_svg = _svg_without_declaration(_read_text(board_path))
    board_bottom_path = asset_directory / "board_pins_bottom.svg"
    if not board_bottom_path.is_file():
        board_bottom_path = asset_directory / "board_bottom.svg"
    if board_bottom_path.is_file():
        board_bottom_svg = _svg_without_declaration(_read_text(board_bottom_path))
    else:
        board_bottom_svg = board_svg
    schematic_path = asset_directory / "schematic.svg"
    schematic_svg = _svg_without_declaration(_read_text(schematic_path)) if schematic_path.is_file() else ""

    component_records = []
    part_metadata_cache = {}
    for component in project_data.get("components", []):
        pcb = component.get("pcb") or {}
        if pcb == {} or pcb.get("exclude_from_bom", False):
            continue
        if str(pcb.get("value") or "").strip().upper() == "DNF":
            continue
        if component.get("oomp", {}).get("status", "") == "not_applicable" or pcb.get("is_mounting_hole", False):
            continue
        reference = str(component.get("reference") or "")
        reference_upper = reference.upper()
        if reference_upper.startswith("SJ") or reference_upper.startswith("FID") or reference.lower().startswith("logo"):
            continue
        oomp_id = str((component.get("oomp") or {}).get("oomp_id") or "")
        if oomp_id and oomp_id not in part_metadata_cache:
            # The summary action copies canonical OOMP metadata here before
            # generating the explorer. Read once per part, not once per ref.
            metadata_path = project_directory / "data" / "project_source" / oomp_id / "working.yaml"
            part_metadata_cache[oomp_id] = {}
            if metadata_path.is_file():
                part_metadata_cache[oomp_id] = yaml.safe_load(_read_text(metadata_path)) or {}
        component_records.append(_component_record(component, asset_directory, part_metadata_cache.get(oomp_id, {})))

    copper = explorer_copper(project_data)
    for component in component_records:
        for pin in component["pads"]:
            pin["net_id"] = ""
            for net in copper["nets"]:
                if net["name"] == pin["net"] and net["source_file"] == component["source_file"]:
                    pin["net_id"] = net["id"]
                    break
    copper_drawing = copper_svg(copper["features"])
    board_svg = add_copper_svg(board_svg, copper_drawing)
    board_bottom_svg = add_copper_svg(board_bottom_svg, copper_drawing, mirror=True)
    copper_json = json.dumps({key: copper[key] for key in ["nets", "layers", "warnings"]}, ensure_ascii=False).replace("</", "<\\/")
    layer_options = "".join(f'<option value="{html.escape(layer, quote=True)}">{html.escape(layer)}</option>' for layer in copper["layers"])
    warning_html = "".join(f'<p class="net-note">{html.escape(warning)}</p>' for warning in copper["warnings"])
    project = summary_data.get("project") or {}
    title = str(project.get("display_name") or project_directory.name)
    github_url = str(project.get("github_url") or "").strip()
    github_icon = (
        f'<a class="github-link" href="{html.escape(github_url)}" target="_blank" rel="noopener" '
        f'aria-label="Open the project repository on GitHub" title="{html.escape(github_url)}">'
        '<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38'
        ' 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg></a>'
        if github_url else ""
    )
    project_owner = str(project.get("owner") or "").strip()
    project_repository = str(project.get("repository") or "").strip()
    project_version = str(project.get("version") or "").strip()
    project_slug = "/".join(part for part in [project_owner, project_repository] if part)
    project_meta = " · ".join(
        part for part in [project_slug, project_version, f"{len(component_records)} items", f"{len(copper['nets'])} nets"] if part
    )
    project_link = (
        f'<a class="project-card-link" href="{html.escape(github_url)}" target="_blank" rel="noopener">View project on GitHub ↗</a>'
        if github_url else ""
    )
    project_card = (
        f'<div class="project-card"><div class="project-card-title">{html.escape(title)}</div>'
        f'<div class="project-card-meta">{html.escape(project_meta)}</div>{project_link}</div>'
    )
    front_count = 0
    back_count = 0
    for component_record in component_records:
        if component_record["side"] == "back":
            back_count += 1
        else:
            front_count += 1
    data_json = json.dumps(component_records, ensure_ascii=False).replace("</", "<\\/")
    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} board explorer</title>
<style id="oomp-board-style">{_style()}</style>
<script>
// Apply the saved theme before first paint so switching pages never flashes.
(function () {{
  var theme = 'light';
  try {{ theme = localStorage.getItem('oomp-board-theme') || 'light'; }} catch (error) {{}}
  if (['light', 'dark', 'rainbow'].indexOf(theme) < 0) theme = 'light';
  document.documentElement.dataset.theme = theme;
}})();
</script>
</head>
<body>
<header><div><h1>{html.escape(title)}</h1><p>Offline OOMP board explorer · components, pins &amp; routed nets</p></div><div class="badge">{len(component_records)} items · {len(copper['nets'])} nets</div>
  <label class="theme-select">Theme
    <select id="theme-select" aria-label="Colour theme">
      <option value="light">Light</option>
      <option value="dark">Dark</option>
      <option value="rainbow">Rainbow</option>
    </select>
  </label>
  {github_icon}</header>
<main class="layout">
  <section class="panel list-panel">
    {project_card}
    <div class="search-wrap"><input id="search" type="search" placeholder="Filter components, pins or nets…" aria-label="Filter components and nets"><div id="layer-legend" class="layer-legend" aria-label="Highlighted copper layer colours"></div></div>
    <div id="part-list" class="part-list"></div>
  </section>
  <section class="panel board-panel">
    <div class="board-toolbar" aria-label="Board view">
      <button class="side-button view-button active" type="button" data-view="board">Board</button>
      {f'<button class="side-button view-button" type="button" data-view="schematic">Schematic</button>' if schematic_svg else ''}
      {f'<button class="side-button view-button" type="button" data-view="split">Split</button>' if schematic_svg else ''}
      <span class="zoom-divider"></span>
      <button class="side-button active" type="button" data-side="front">Top · {front_count}</button>
      <button class="side-button" type="button" data-side="back">Bottom · {back_count}</button>
      <span class="zoom-divider"></span>
      <button id="zoom-out" class="zoom-button" type="button" aria-label="Zoom out">−</button>
      <button id="zoom-fit" class="zoom-label side-button" type="button" aria-label="Fit board"><span id="zoom-label">100%</span></button>
      <button id="zoom-in" class="zoom-button" type="button" aria-label="Zoom in">+</button>
      <button id="zoom-reset" class="zoom-button zoom-reset" type="button" aria-label="Reset board zoom to 100%">100%</button>
      <span class="zoom-divider"></span>
      <select id="copper-layer" aria-label="Copper layers"><option value="side">Visible side copper</option><option value="all" selected>All copper layers</option>{layer_options}</select>
      <label><input id="show-traces" type="checkbox" checked> Traces</label>
      <label><input id="show-fills" type="checkbox" checked> Fills</label>
      <span class="net-selection-controls">
        <label><input id="zoom-to-net" type="checkbox"> Zoom to net</label>
        <label><input id="highlight-selected-nets" type="checkbox"> Highlight all selected nets</label>
      </span>
    </div>
    <div id="board-stage" class="board-stage">
      <div class="board-view" data-side="front">{board_svg}</div>
      <div class="board-view" data-side="back" hidden>{board_bottom_svg}</div>
      {f'<div id="schematic-view" class="schematic-view" hidden data-side="schematic">{schematic_svg}</div>' if schematic_svg else ''}
    </div>
  </section>
  <aside class="panel detail">
    <div class="part-detail-scroll"><div id="detail"><p class="empty">Choose a component to inspect its placement, OOMP match and pins.</p></div>{warning_html}</div>
    <section class="selection-status" aria-labelledby="selection-status-title">
      <div class="selection-status-header"><div id="selection-status-title" class="eyebrow">Selection status</div><button id="clear-selection" type="button">Clear</button></div>
      <div id="net-status" class="net-status" role="status" aria-live="polite"></div>
    </section>
  </aside>
</main>
<div id="hover-card" class="hover-card" role="status"></div>
<div id="lcsc-popup" class="popup-overlay" hidden></div>
<script id="component-data" type="application/json">{data_json}</script>
<script id="copper-data" type="application/json">{copper_json}</script>
<script>{_script()}</script>
</body>
</html>
"""
    output_path = project_directory / "board_explorer.html"
    output_path.write_text(document, encoding="utf-8")
    # Remove the old generated copy only after its replacement is written.
    legacy_path = output_directory / "board_explorer.html"
    if legacy_path != output_path and legacy_path.is_file():
        legacy_path.unlink()
    return output_path


if __name__ == "__main__":
    raise SystemExit("Run this generator through project_readme_action.py")
