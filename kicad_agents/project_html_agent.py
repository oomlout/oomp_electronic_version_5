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


def _lcsc_part_number(component, part_metadata):
    """Prefer the matched catalogue number; fall back to explicit BOM fields."""
    match = component.get("oomp") or {}
    if match.get("status") != "matched" or not match.get("oomp_id"):
        return ""
    candidates = [part_metadata.get("part_number_lcsc", "")]
    for distributor in part_metadata.get("distributors") or []:
        if distributor.get("key") == "lcsc":
            candidates.append(distributor.get("part_number", ""))
    property_sets = [(component.get("pcb") or {}).get("properties") or {}]
    for unit in (component.get("schematic") or {}).get("units") or []:
        property_sets.append(unit.get("properties") or {})
    for properties in property_sets:
        for key, value in properties.items():
            field = re.sub(r"[^a-z0-9]", "", str(key).lower())
            if field in ["partnumberlcsc", "lcsc", "lcscpartnumber", "lcscpart"]:
                candidates.append(value)
    for candidate in candidates:
        number = str(candidate or "").strip().upper()
        if number.isascii() and number.isdigit():
            number = "C" + number
        if re.fullmatch(r"C[0-9]+", number):
            return number
    return ""


def _component_record(component, asset_directory, part_metadata=None):
    pcb = component.get("pcb") or {}
    oomp = component.get("oomp") or {}
    oomp_id = str(oomp.get("oomp_id") or "")
    properties = pcb.get("properties") or {}
    lcsc_number = _lcsc_part_number(component, part_metadata or {})
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
        "supplier": str(properties.get("Supplier") or "").strip(),
        "pads": pads,
        "pinout_svg": _part_pinout_svg(asset_directory, oomp_id),
    }


def _style():
    # Everything visual lives here.  The variables at the top are the intended
    # quick-adjustment surface for later restyling.
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
}
* { box-sizing: border-box; }
html, body { margin: 0; width: 100%; height: 100%; background: var(--page); color: var(--ink); font-family: var(--font); }
body { display: grid; grid-template-rows: auto minmax(0, 1fr); overflow: hidden; }
header { display: flex; align-items: center; gap: 18px; padding: 16px 22px; background: var(--ink); color: white; }
header h1 { margin: 0; font-size: clamp(18px, 2.1vw, 30px); letter-spacing: -.03em; }
header p { margin: 2px 0 0; color: #cfcfcf; font-size: 13px; }
.badge { margin-left: auto; border: 1px solid #555; border-radius: 999px; padding: 7px 11px; font-size: 12px; white-space: nowrap; }
.layout { height: 100%; min-height: 0; display: grid; grid-template-columns: minmax(190px, 260px) minmax(0, 1fr) minmax(260px, 360px); gap: 14px; padding: 14px; overflow: hidden; }
.panel { min-width: 0; min-height: 0; background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); overflow: hidden; box-shadow: 0 4px 18px rgba(0,0,0,.05); }
.list-panel { display: grid; grid-template-rows: auto auto minmax(0, 1fr); min-width: 0; }
.search-wrap { padding: 14px; border-bottom: 1px solid var(--line); }
input { width: 100%; padding: 10px 12px; border: 1px solid var(--line); border-radius: 10px; font: inherit; }
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
.selection-tools { margin-top: 7px; font-size: 11px; color: var(--muted); }
.selection-tools button { border: 0; background: transparent; color: var(--ink); text-decoration: underline; cursor: pointer; font: inherit; }
.part-button { width: 100%; min-width: 0; display: grid; grid-template-columns: 50px minmax(0, 1fr); gap: 3px 8px; padding: 9px 32px 9px 9px; border: 0; border-radius: 10px; background: transparent; color: inherit; text-align: left; cursor: pointer; }
.part-button:hover, .part-button.active { background: var(--accent-soft); }
.part-button.active:not(.selected) { background: transparent; box-shadow: inset 0 0 0 1px var(--line); }
.part-button strong { font-size: 13px; }
.part-button span { overflow: hidden; color: var(--muted); font-size: 11px; text-overflow: ellipsis; white-space: nowrap; }
.part-button .oomp-id { grid-column: 1 / -1; overflow-wrap: anywhere; text-overflow: clip; white-space: normal; }
.part-link { position: absolute; top: 8px; right: 7px; display: grid; width: 24px; height: 24px; place-items: center; border-radius: 7px; color: var(--ink); text-decoration: none; }
.part-link:hover { background: var(--ink); color: white; }
.board-panel { position: relative; display: grid; place-items: center; overflow: auto; padding: 18px; background: var(--board); }
.board-toolbar { position: absolute; z-index: 10; top: 12px; left: 12px; right: 12px; display: flex; flex-wrap: wrap; align-items: center; gap: 5px; padding: 5px; border: 1px solid var(--line); border-radius: 12px; background: rgba(255,255,255,.94); box-shadow: 0 4px 14px rgba(0,0,0,.08); }
.side-button { padding: 7px 11px; border: 0; border-radius: 8px; background: transparent; color: var(--muted); font: inherit; font-size: 12px; font-weight: 750; cursor: pointer; }
.side-button:hover, .side-button.active { background: var(--ink); color: white; }
.zoom-divider { width: 1px; margin: 4px 2px; background: var(--line); }
.zoom-button { width: 31px; padding: 7px 0; border: 0; border-radius: 8px; background: transparent; color: var(--ink); font: inherit; font-weight: 850; cursor: pointer; }
.zoom-button:hover { background: var(--accent-soft); }
.zoom-label { min-width: 43px; align-self: center; color: var(--muted); font-size: 11px; text-align: center; }
.board-stage { width: 100%; height: 100%; min-width: 0; min-height: 0; display: grid; place-items: center; }
.board-view { width: 100%; height: 100%; min-width: 0; min-height: 0; }
.board-view[hidden] { display: none; }
.board-view > svg { display: block; width: 100%; height: 100%; max-width: 100%; max-height: 100%; margin: auto; filter: drop-shadow(0 9px 13px rgba(0,0,0,.12)); }
.board-stage .board-component { cursor: pointer; outline: none; transition: opacity .13s ease; shape-rendering: geometricPrecision; }
.board-stage .board-component > .component { fill: none; }
/* Only the explorer makes white assembly geometry transparent. Labels and
   black outlines stay above the actual pad/track shapes; source SVGs stay white. */
.board-stage .board-component :is(rect, path, polygon, circle, ellipse):is([fill="#FFFFFF"], [fill="#ffffff"], [fill="#fff"], [fill="white"]) { fill: none; }
/* Never stroke an ancestor of the pin labels: SVG text inherits that stroke,
   which can be several times wider than the letters at physical board scale. */
.board-stage .board-component text { stroke: none; }
.board-stage.has-selection .board-component:not(.is-active) { opacity: .55; }
.component-highlights { pointer-events: none; }
.selection-box, .hover-box { fill: none; stroke: var(--accent); stroke-width: 1.2; stroke-linejoin: round; stroke-linecap: round; shape-rendering: geometricPrecision; vector-effect: non-scaling-stroke; pointer-events: none; }
.hover-box { opacity: .65; }
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
.pinout { min-height: 120px; display: grid; place-items: center; margin: 12px 0; padding: 10px; border: 1px solid var(--line); border-radius: 14px; background: white; overflow: hidden; }
.pinout svg { width: 100%; max-height: 300px; }
.pin-table { width: 100%; border-collapse: collapse; font-size: 12px; }
.pin-table th, .pin-table td { padding: 6px; border-bottom: 1px solid #e5e2da; text-align: left; }
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
.net-picker { padding: 0 14px 12px; border-bottom: 1px solid var(--line); font-size: 12px; max-height: 300px; overflow: auto; }
.net-picker label { display: block; margin-bottom: 6px; }
.net-picker select, .board-toolbar select { width: 100%; min-width: 0; max-width: 100%; padding: 6px; border: 1px solid var(--line); border-radius: 6px; background: white; font: inherit; }
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
.actions a { display: inline-block; padding: 9px 12px; border-radius: 10px; background: var(--ink); color: white; text-decoration: none; font-size: 12px; }
.actions a.secondary { background: var(--accent-soft); color: var(--ink); }
.empty { color: var(--muted); line-height: 1.55; }
.hover-card { position: fixed; z-index: 20; display: none; width: 245px; padding: 11px 13px; border: 1px solid var(--line); border-radius: 12px; background: rgba(255,255,255,.97); box-shadow: var(--shadow); pointer-events: none; }
.hover-card.visible { display: block; }
.hover-card strong { display: block; }
.hover-card span { display: block; margin-top: 3px; color: var(--muted); font-size: 12px; }
@media (max-width: 920px) { html, body { height: auto; min-height: 100%; } body { overflow: auto; } .layout { height: auto; overflow: visible; grid-template-columns: 190px minmax(0, 1fr); grid-template-rows: minmax(560px, 75vh) auto; } .detail.panel { grid-column: 1 / -1; height: min(680px, 80vh); min-height: 360px; } }
@media (max-width: 640px) { body { display: block; } header { flex-wrap: wrap; } .layout { display: block; } .panel { margin-bottom: 12px; } .list-panel { height: 520px; } .board-panel { height: 70vh; min-height: 400px; } }
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
let activeNet = '';
let activePin = null;
const selectedReferences = new Set();
const selectedPins = [];
const collapsedCategories = new Set(components.map(component => component.category));
const highlightSelectedNets = document.getElementById('highlight-selected-nets');
const expandedReferences = new Set();
const netSelect = document.getElementById('net-select');
const netSearch = document.getElementById('net-search');
const layerSelect = document.getElementById('copper-layer');
const baseFeatures = [...document.querySelectorAll('.copper-base .copper-feature')];
const boardViewports = new Map();
document.querySelectorAll('.board-view > svg').forEach(svg => {
  const original = svg.getAttribute('viewBox').split(/\s+/).map(Number);
  boardViewports.set(svg, {original, target: [...original]});
});
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
  document.getElementById('selection-count').textContent = `${selectedReferences.size} components · ${selectedPins.length} pins · both sides`;
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

function selectionChanged(preservePins = false) {
  if (!preservePins) {
    selectedPins.length = 0;
    activeNet = '';
    activePin = null;
  }
  updateSelectionBoxes();
  updateNetHighlight();
  renderList(search.value);
  const component = byReference.get(activeReference);
  if (component) renderDetail(component);
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
  const actions = [
    component.part_url ? `<a href="${escapeHtml(component.part_url)}" target="_blank" rel="noopener">Open OOMP part</a>` : '',
    component.lcsc_url ? `<a class="secondary lcsc-link" href="${escapeHtml(component.lcsc_url)}" target="_blank" rel="noopener noreferrer" title="${escapeHtml(component.lcsc_part_number)}">Open LCSC</a>` : '',
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
      <dt>Side</dt><dd>${escapeHtml(component.side || '—')}</dd>
      <dt>Position</dt><dd>${escapeHtml(position.x ?? '—')}, ${escapeHtml(position.y ?? '—')} mm</dd>
      <dt>Rotation</dt><dd>${escapeHtml(position.rotation_kicad ?? position.rotation ?? '—')}°</dd>
    </dl>
    <div class="actions">${actions}</div>
    <div class="eyebrow">Pinout</div>
    ${component.pinout_svg ? `<div class="pinout">${component.pinout_svg}</div>` : ''}
    ${pinRows(component)}`;
}

function selectComponent(reference, preserveNet = false, expandCategory = true) {
  const component = byReference.get(reference);
  if (!component) return;
  if (component.side && component.side !== activeSide) setSide(component.side, false);
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
  if (!additive) {
    highlightSelectedNets.checked = false;
    selectedPins.length = 0;
  }
  const index = selectedPinIndex(reference, number, netId);
  if (index >= 0) selectedPins.splice(index, 1);
  else selectedPins.push({reference, number, net_id: netId || ''});
  syncActivePin();
  expandedReferences.add(reference);
  if (additive) {
    const component = byReference.get(reference);
    activeReference = reference;
    collapsedCategories.delete(component.category);
    if (component.side !== activeSide) setSide(component.side);
    selectionChanged(true);
  } else selectComponent(reference, true);
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

function selectNet(netId) {
  highlightSelectedNets.checked = false;
  activeNet = byNet.has(netId) ? netId : '';
  activePin = null;
  selectedPins.length = 0;
  updateNetHighlight();
  renderList(search.value);
  const component = byReference.get(activeReference);
  if (component) renderDetail(component);
}

function renderNetOptions() {
  const filter = netSearch.value.trim().toLowerCase();
  netSelect.innerHTML = '<option value="">Choose a net…</option>';
  copper.nets.forEach(net => {
    if (net.id !== activeNet && !net.name.toLowerCase().includes(filter)) return;
    const option = document.createElement('option');
    option.value = net.id;
    option.textContent = `${net.name} · ${net.pins.length} pins`;
    netSelect.appendChild(option);
  });
  netSelect.value = activeNet;
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
  const status = document.getElementById('net-status');
  if (highlightSelectedNets.checked || selectedPins.length > 1) {
    const selectionLabel = highlightSelectedNets.checked ? `${selectedReferences.size} components · ${selectedPins.length} pins` : `${selectedPins.length} selected pins`;
    status.innerHTML = `<strong>${selectionLabel} · ${netIds.size} nets</strong><br><span class="net-note">All connected pins and copper on the shown layers. Click a net below to follow it alone.</span><div>${[...netIds].map(id => `<button class="net-link" data-net-id="${escapeHtml(id)}">${escapeHtml(byNet.get(id).name)}</button>`).join(' ')}</div>`;
  } else if (net) {
    const visiblePins = net.pins.filter(pin => layerSelect.value === 'all' || pin.layers.includes(layerSelect.value === 'side' ? (activeSide === 'back' ? 'B.Cu' : 'F.Cu') : layerSelect.value));
    status.innerHTML = `<strong>${escapeHtml(net.name)}</strong><br>${net.track_count} traces · ${net.via_count} vias · ${net.fill_count} saved fills<br>${visiblePins.length} / ${net.pins.length} pins on shown layers<br><span class="net-note">${escapeHtml(net.layers.join(' · '))}</span><div>${net.pins.map(pin => byReference.has(pin.reference) ? `<button class="net-link" data-reference="${escapeHtml(pin.reference)}" data-pin="${escapeHtml(pin.number)}">${escapeHtml(pin.reference)}.${escapeHtml(pin.number || 'pad')}</button>` : `<span>${escapeHtml(pin.reference)}.${escapeHtml(pin.number)} (not in BOM) </span>`).join('')}</div>`;
  } else {
    status.textContent = activePin ? `${activePin.reference}.${activePin.number}: no assigned net; only this pin is highlighted.` : 'Expand Pins or choose a net. Highlight colours identify copper layers; teal marks the selected pin. Escape clears.';
  }
  renderNetOptions();
  if (document.getElementById('zoom-to-net').checked) fitSelectedNet();
}

function updateSelectionBoxes() {
  document.querySelectorAll('.component-highlights').forEach(layer => layer.replaceChildren());
  stage.classList.toggle('has-selection', selectedReferences.size > 0);
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

function setZoom(nextZoom) {
  zoomScale = Math.max(0.5, Math.min(12, nextZoom));
  // Keep the SVG sized to the panel. Changing its viewBox zooms around the
  // selected region without growing the grid or moving the toolbar away.
  boardViewports.forEach((viewport, svg) => {
    const [x, y, width, height] = viewport.target;
    const w = width / zoomScale;
    const h = height / zoomScale;
    svg.setAttribute('viewBox', [x + (width - w) / 2, y + (height - h) / 2, w, h].join(' '));
  });
  document.getElementById('zoom-label').textContent = `${Math.round(zoomScale * 100)}%`;
}

function fitBoard() {
  boardViewports.forEach(viewport => { viewport.target = [...viewport.original]; });
  setZoom(1);
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
  boardViewports.get(svg).target = [minX - pad, minY - pad, maxX - minX + pad * 2, maxY - minY + pad * 2];
  setZoom(1);
}

function setSide(side) {
  activeSide = side === 'back' ? 'back' : 'front';
  document.querySelectorAll('.board-view').forEach(view => { view.hidden = view.dataset.side !== activeSide; });
  document.querySelectorAll('.side-button[data-side]').forEach(button => button.classList.toggle('active', button.dataset.side === activeSide));
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
  const gap = 15;
  const width = 245;
  let x = event.clientX + gap;
  let y = event.clientY + gap;
  if (x + width > window.innerWidth) x = event.clientX - width - gap;
  if (y + 90 > window.innerHeight) y = event.clientY - 100;
  hoverCard.style.left = `${Math.max(8, x)}px`;
  hoverCard.style.top = `${Math.max(8, y)}px`;
}

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
  } else if (netButton) selectNet(netButton.dataset.netId);
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
  if (netButton) { selectNet(netButton.dataset.netId); return; }
  const button = event.target.closest('button[data-reference]');
  if (button) selectPin(button.dataset.reference, button.dataset.pin, activeNet, additiveClick(event));
});
netSearch.addEventListener('input', renderNetOptions);
netSelect.addEventListener('change', () => selectNet(netSelect.value));
document.getElementById('clear-net').addEventListener('click', () => selectNet(''));
document.getElementById('clear-selection').addEventListener('click', () => {
  selectedReferences.clear();
  activeReference = '';
  detail.innerHTML = '<p class="empty">Choose a component to inspect its placement, OOMP match and pins.</p>';
  selectionChanged();
});
highlightSelectedNets.addEventListener('change', () => selectionChanged(true));
document.addEventListener('keydown', event => { if (event.key === 'Escape') selectNet(''); });
for (const id of ['copper-layer', 'show-traces', 'show-fills']) {
  document.getElementById(id).addEventListener('change', updateNetHighlight);
}
document.getElementById('zoom-to-net').addEventListener('change', event => {
  if (event.target.checked) fitSelectedNet();
  else fitBoard();
});
document.querySelectorAll('.side-button[data-side]').forEach(button => button.addEventListener('click', () => setSide(button.dataset.side)));
document.getElementById('zoom-in').addEventListener('click', () => setZoom(zoomScale + 0.25));
document.getElementById('zoom-out').addEventListener('click', () => setZoom(zoomScale - 0.25));
document.getElementById('zoom-fit').addEventListener('click', fitBoard);
renderLayerLegend();
setZoom(1);
setSide('front', false);
const firstFrontComponent = components.find(component => component.side === 'front');
// Show the initial part details without opening its category in the tree.
if (firstFrontComponent) selectComponent(firstFrontComponent.reference, false, false);
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
</head>
<body>
<header><div><h1>{html.escape(title)}</h1><p>Offline OOMP board explorer · components, pins &amp; routed nets</p></div><div class="badge">{len(component_records)} items · {len(copper['nets'])} nets</div></header>
<main class="layout">
  <section class="panel list-panel">
    <div class="search-wrap"><input id="search" type="search" placeholder="Filter categories, components or pins…" aria-label="Filter components"><div class="selection-tools"><span id="selection-count">0 selected · both sides</span> · <button id="clear-selection" type="button">Clear selection</button><br>Ctrl-click categories, components or pins to toggle multiple selections.</div></div>
    <div class="net-picker">
      <label for="net-search">Follow a net</label>
      <input id="net-search" type="search" placeholder="Find net by name…" aria-label="Filter nets">
      <select id="net-select" aria-label="Select net"></select>
      <button id="clear-net" class="net-link" type="button">Clear highlight</button>
      <div id="layer-legend" class="layer-legend" aria-label="Highlighted copper layer colours"></div>
    </div>
    <div id="part-list" class="part-list"></div>
  </section>
  <section class="panel board-panel">
    <div class="board-toolbar" aria-label="Board side">
      <button class="side-button active" type="button" data-side="front">Top · {front_count}</button>
      <button class="side-button" type="button" data-side="back">Bottom · {back_count}</button>
      <span class="zoom-divider"></span>
      <button id="zoom-out" class="zoom-button" type="button" aria-label="Zoom out">−</button>
      <button id="zoom-fit" class="zoom-label side-button" type="button" aria-label="Fit board"><span id="zoom-label">100%</span></button>
      <button id="zoom-in" class="zoom-button" type="button" aria-label="Zoom in">+</button>
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
    </div>
  </section>
  <aside class="panel detail">
    <div class="part-detail-scroll"><div id="detail"><p class="empty">Choose a component to inspect its placement, OOMP match and pins.</p></div>{warning_html}</div>
    <section class="selection-status" aria-labelledby="selection-status-title">
      <div id="selection-status-title" class="eyebrow">Selection status</div>
      <div id="net-status" class="net-status" role="status" aria-live="polite"></div>
    </section>
  </aside>
</main>
<div id="hover-card" class="hover-card" role="status"></div>
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
