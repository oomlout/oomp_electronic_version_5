"""Build a single-file, offline HTML explorer for an extracted KiCad board."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

import yaml


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


def _component_record(component, asset_directory):
    pcb = component.get("pcb") or {}
    oomp = component.get("oomp") or {}
    oomp_id = str(oomp.get("oomp_id") or "")
    properties = pcb.get("properties") or {}
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
        "value": str(pcb.get("value") or properties.get("Value") or ""),
        "footprint": str(pcb.get("library_id") or ""),
        "side": str(pcb.get("side") or ""),
        "position": pcb.get("position") or {},
        "oomp_id": oomp_id,
        "match_status": str(oomp.get("status") or "unmatched"),
        "confidence": oomp.get("confidence", 0),
        "part_url": f"{OOMP_PARTS_URL}/{oomp_id}" if oomp_id else "",
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
  --shadow: 0 18px 50px rgba(20, 20, 20, .14);
  --radius: 18px;
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
.panel { min-height: 0; background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); overflow: hidden; box-shadow: 0 4px 18px rgba(0,0,0,.05); }
.list-panel { display: grid; grid-template-rows: auto 1fr; }
.search-wrap { padding: 14px; border-bottom: 1px solid var(--line); }
input { width: 100%; padding: 10px 12px; border: 1px solid var(--line); border-radius: 10px; font: inherit; }
.part-list { overflow: auto; padding: 7px; }
.part-button { width: 100%; display: grid; grid-template-columns: 50px 1fr; gap: 8px; padding: 9px; border: 0; border-radius: 10px; background: transparent; color: inherit; text-align: left; cursor: pointer; }
.part-button:hover, .part-button.active { background: var(--accent-soft); }
.part-button strong { font-size: 13px; }
.part-button span { overflow: hidden; color: var(--muted); font-size: 11px; text-overflow: ellipsis; white-space: nowrap; }
.board-panel { position: relative; display: grid; place-items: center; overflow: auto; padding: 18px; background: var(--board); }
.board-toolbar { position: absolute; z-index: 10; top: 12px; left: 12px; display: flex; gap: 5px; padding: 5px; border: 1px solid var(--line); border-radius: 12px; background: rgba(255,255,255,.94); box-shadow: 0 4px 14px rgba(0,0,0,.08); }
.side-button { padding: 7px 11px; border: 0; border-radius: 8px; background: transparent; color: var(--muted); font: inherit; font-size: 12px; font-weight: 750; cursor: pointer; }
.side-button:hover, .side-button.active { background: var(--ink); color: white; }
.board-stage { width: min(100%, 1050px); min-width: 560px; }
.board-view { width: 100%; }
.board-view[hidden] { display: none; }
.board-view > svg { display: block; width: 100%; height: auto; filter: drop-shadow(0 9px 13px rgba(0,0,0,.12)); }
.board-stage .board-component { cursor: pointer; outline: none; transition: opacity .13s ease; }
.board-stage .board-component:hover, .board-stage .board-component:focus, .board-stage .board-component.is-active { filter: drop-shadow(0 0 1.5px var(--accent)) drop-shadow(0 0 3px var(--accent)); }
.board-stage.has-selection .board-component:not(.is-active) { opacity: .38; }
.board-stage .indicator { pointer-events: none; }
.detail { overflow: auto; padding: 18px; }
.eyebrow { color: var(--accent); font-size: 11px; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; }
.detail h2 { margin: 5px 0 0; font-size: 30px; letter-spacing: -.04em; }
.value { margin: 4px 0 18px; color: var(--muted); }
.facts { display: grid; grid-template-columns: 92px 1fr; gap: 7px 10px; margin: 0 0 18px; font-size: 13px; }
.facts dt { color: var(--muted); }
.facts dd { margin: 0; overflow-wrap: anywhere; }
.pinout { min-height: 120px; display: grid; place-items: center; margin: 12px 0; padding: 10px; border: 1px solid var(--line); border-radius: 14px; background: white; overflow: hidden; }
.pinout svg { width: 100%; max-height: 300px; }
.pin-table { width: 100%; border-collapse: collapse; font-size: 12px; }
.pin-table th, .pin-table td { padding: 6px; border-bottom: 1px solid #e5e2da; text-align: left; }
.actions { display: flex; flex-wrap: wrap; gap: 8px; margin: 14px 0; }
.actions a { display: inline-block; padding: 9px 12px; border-radius: 10px; background: var(--ink); color: white; text-decoration: none; font-size: 12px; }
.actions a.secondary { background: var(--accent-soft); color: var(--ink); }
.empty { color: var(--muted); line-height: 1.55; }
.hover-card { position: fixed; z-index: 20; display: none; width: 245px; padding: 11px 13px; border: 1px solid var(--line); border-radius: 12px; background: rgba(255,255,255,.97); box-shadow: var(--shadow); pointer-events: none; }
.hover-card.visible { display: block; }
.hover-card strong { display: block; }
.hover-card span { display: block; margin-top: 3px; color: var(--muted); font-size: 12px; }
@media (max-width: 920px) { .layout { grid-template-columns: 190px minmax(0, 1fr); } .detail.panel { grid-column: 1 / -1; min-height: 360px; } }
@media (max-width: 640px) { html, body { height: auto; min-height: 100%; } body { display: block; overflow: auto; } .layout { display: block; height: auto; overflow: visible; } .panel { margin-bottom: 12px; } .list-panel { height: 240px; } .board-panel { height: 62vh; } .board-stage { min-width: 500px; } }
"""


def _script():
    return r"""
const components = JSON.parse(document.getElementById('component-data').textContent);
const byReference = new Map(components.map(component => [component.reference, component]));
const list = document.getElementById('part-list');
const detail = document.getElementById('detail');
const search = document.getElementById('search');
const stage = document.getElementById('board-stage');
const hoverCard = document.getElementById('hover-card');
let activeReference = '';
let activeSide = 'front';

function escapeHtml(value) {
  return String(value ?? '').replace(/[&<>'"]/g, character => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[character]));
}

function renderList(filterText = '') {
  const filter = filterText.trim().toLowerCase();
  list.innerHTML = '';
  components.filter(component => {
    const haystack = [component.reference, component.value, component.oomp_id, component.footprint].join(' ').toLowerCase();
    return component.side === activeSide && haystack.includes(filter);
  }).forEach(component => {
    const button = document.createElement('button');
    button.className = 'part-button' + (component.reference === activeReference ? ' active' : '');
    button.dataset.reference = component.reference;
    button.innerHTML = `<strong>${escapeHtml(component.reference)}</strong><span>${escapeHtml(component.value || 'unlabelled')}</span>`;
    button.addEventListener('click', () => selectComponent(component.reference));
    list.appendChild(button);
  });
}

function pinRows(component) {
  if (!component.pads.length) return '<p class="empty">No PCB pads were extracted for this item.</p>';
  return `<table class="pin-table"><thead><tr><th>Pin</th><th>Name</th><th>Net</th></tr></thead><tbody>${component.pads.map(pin => `<tr><td>${escapeHtml(pin.number)}</td><td>${escapeHtml(pin.name || '—')}</td><td>${escapeHtml(pin.net || '—')}</td></tr>`).join('')}</tbody></table>`;
}

function renderDetail(component) {
  const position = component.position || {};
  const match = component.oomp_id ? 'Matched OOMP part' : 'Needs OOMP match';
  const actions = [
    component.part_url ? `<a href="${escapeHtml(component.part_url)}" target="_blank" rel="noopener">Open OOMP part</a>` : '',
    component.supplier ? `<a class="secondary" href="${escapeHtml(component.supplier)}" target="_blank" rel="noopener">Supplier source</a>` : ''
  ].join('');
  detail.innerHTML = `
    <div class="eyebrow">${escapeHtml(match)}</div>
    <h2>${escapeHtml(component.reference)}</h2>
    <div class="value">${escapeHtml(component.value || 'No value')}</div>
    <dl class="facts">
      <dt>OOMP</dt><dd>${escapeHtml(component.oomp_id || 'unmatched')}</dd>
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

function selectComponent(reference) {
  const component = byReference.get(reference);
  if (!component) return;
  if (component.side && component.side !== activeSide) setSide(component.side, false);
  activeReference = reference;
  stage.classList.add('has-selection');
  document.querySelectorAll('.board-component').forEach(element => element.classList.toggle('is-active', element.dataset.reference === reference));
  renderDetail(component);
  renderList(search.value);
}

function setSide(side, selectFirst = true) {
  activeSide = side === 'back' ? 'back' : 'front';
  document.querySelectorAll('.board-view').forEach(view => { view.hidden = view.dataset.side !== activeSide; });
  document.querySelectorAll('.side-button').forEach(button => button.classList.toggle('active', button.dataset.side === activeSide));
  renderList(search.value);
  const selected = byReference.get(activeReference);
  if (selectFirst && (!selected || selected.side !== activeSide)) {
    const first = components.find(component => component.side === activeSide);
    if (first) selectComponent(first.reference);
  }
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
  element.addEventListener('mouseenter', event => showHover(event, reference));
  element.addEventListener('mousemove', moveHover);
  element.addEventListener('mouseleave', () => hoverCard.classList.remove('visible'));
  element.addEventListener('click', () => selectComponent(reference));
  element.addEventListener('keydown', event => { if (event.key === 'Enter' || event.key === ' ') selectComponent(reference); });
});
search.addEventListener('input', () => renderList(search.value));
document.querySelectorAll('.side-button').forEach(button => button.addEventListener('click', () => setSide(button.dataset.side)));
setSide('front', false);
const firstFrontComponent = components.find(component => component.side === 'front');
if (firstFrontComponent) selectComponent(firstFrontComponent.reference);
"""


def generate_board_explorer(project_directory, project_data, summary_data, output_directory=None):
    project_directory = Path(project_directory).resolve()
    if output_directory is None:
        output_directory = project_directory / "generated_data"
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
        component_records.append(_component_record(component, asset_directory))

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
<header><div><h1>{html.escape(title)}</h1><p>Offline OOMP board explorer · hover or click a component</p></div><div class="badge">{len(component_records)} placed items</div></header>
<main class="layout">
  <section class="panel list-panel"><div class="search-wrap"><input id="search" type="search" placeholder="Filter reference, value or part…" aria-label="Filter components"></div><div id="part-list" class="part-list"></div></section>
  <section class="panel board-panel">
    <div class="board-toolbar" aria-label="Board side">
      <button class="side-button active" type="button" data-side="front">Top · {front_count}</button>
      <button class="side-button" type="button" data-side="back">Bottom · {back_count}</button>
    </div>
    <div id="board-stage" class="board-stage">
      <div class="board-view" data-side="front">{board_svg}</div>
      <div class="board-view" data-side="back" hidden>{board_bottom_svg}</div>
    </div>
  </section>
  <aside id="detail" class="panel detail"><p class="empty">Choose a component to inspect its placement, OOMP match and pins.</p></aside>
</main>
<div id="hover-card" class="hover-card" role="status"></div>
<script id="component-data" type="application/json">{data_json}</script>
<script>{_script()}</script>
</body>
</html>
"""
    output_path = output_directory / "board_explorer.html"
    output_path.write_text(document, encoding="utf-8")
    return output_path


if __name__ == "__main__":
    raise SystemExit("Run this generator through project_readme_action.py")
