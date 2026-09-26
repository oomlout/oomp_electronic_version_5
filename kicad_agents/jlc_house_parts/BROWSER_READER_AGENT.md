# Browser reader agent: record live-page facts, decide nothing

One role in the fan-out (see [MULTI_AGENT.md](MULTI_AGENT.md)): drive the
browser, transcribe what the live JLC product page visibly shows into
`browser_staging/C<number>.json`, and stop. The reader never classifies,
never defers, never edits population files and never guesses a fact. Pool
workers then take over with `next --claim --staged-only` and need no browser.

This role must run in the main agent: the ZCode in-app browser is
unavailable to spawned subagents.

## Loop

1. `python -m kicad_agents.jlc_house_parts_agent stage-plan --count 10`
   prints the next pending codes that have no fresh staged capture, with
   their `url`, queued manufacturer, MPN and package.
2. For each code, run the extraction script below in one `js` call with that
   code's `url` and a temp output path (use the gitignored `tmp/` directory).
   It opens its own tab and closes it.
3. Stage the capture:

   ```powershell
   python -m kicad_agents.jlc_house_parts_agent stage-capture --code <C> --file <tmp.json>
   ```

   The command rejects any identity field that differs from the queue, an
   unknown class badge, a missing description or page text, and refuses to
   overwrite an existing capture without `--force`.
4. Delete the temp file, continue with the next code, then repeat from 1.

Report identity drift, unreadable pages or ambiguous class badges instead of
forcing a capture. If the page shows a manufacturer/MPN/package that differs
from the queue, stage nothing for that code and note it for manual review.

## Extraction script (one js call per page)

Replace `<URL>` and `<OUT>`; set `timeout_ms` to at least 60000.

```js
const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;
if (!browserPluginRoot) throw new Error("Browser plugin root is unavailable");
const { join } = await import("node:path");
const { pathToFileURL } = await import("node:url");
const browserClientUrl = pathToFileURL(join(browserPluginRoot, "scripts", "browser-client.mjs")).href;
const { setupBrowserRuntime } = await import(browserClientUrl);
await setupBrowserRuntime({ globals: globalThis });
const url = "<URL>";
const browser = await agent.browsers.getForUrl(url);
const tab = await browser.tabs.new();
await tab.goto(url);
await tab.playwright.waitForLoadState({ state: "domcontentloaded" });
await tab.playwright.waitForTimeout(2500);
const capture = await tab.playwright.evaluate(`(() => {
  const text = (document.body.innerText || "");
  const lines = text.split("\\n").map(s => s.trim());
  const labels = ["Basic", "Preferred", "Promotional", "Extended"];
  let tier = "";
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_ELEMENT);
  let node;
  while ((node = walker.nextNode())) {
    const t = (node.textContent || "").trim();
    if (labels.includes(t) && node.children.length === 0) { tier = t; break; }
  }
  const fields = {};
  const names = ["Manufacturer", "MFR.Part #", "JLCPCB Part #", "Package"];
  for (let i = 0; i < lines.length - 1; i++) {
    if (names.includes(lines[i]) && lines[i + 1] && !names.includes(lines[i + 1])) {
      fields[lines[i]] = lines[i + 1];
    }
  }
  let description = "";
  const di = lines.indexOf("Description");
  if (di >= 0) {
    const parts = [];
    for (let i = di + 1; i < lines.length && lines[i] !== "EasyEDA Libraries"; i++) parts.push(lines[i]);
    description = parts.join(" ");
  }
  const specifications = {};
  for (const line of lines) {
    const m = line.match(/^([^\\t]+)\\t([^\\t]+)$/);
    if (!m) continue;
    const key = m[1].trim(), value = m[2].trim();
    if (/^(Qty|Unit Price|Attributes|Value)$/.test(key) || /^\\d+\\+$/.test(key) || value.startsWith("$")) continue;
    specifications[key] = value;
  }
  const grab = (re) => { const m = text.match(re); return m ? m[1] : ""; };
  return {
    code: fields["JLCPCB Part #"] || "",
    manufacturer: fields["Manufacturer"] || "",
    mpn: fields["MFR.Part #"] || "",
    package: fields["Package"] || "",
    tier_label: tier,
    description,
    specifications,
    stock_observed: grab(/In Stock:\\s*([\\d,]+)/),
    purchase_moq_observed: grab(/Minimum:\\s*([\\d,]+)/),
    full_reel_observed: grab(/Full Reel:\\s*([\\d,]+)/),
    available_order_qty_observed: grab(/Available Order Qty:\\s*([\\d,]+)/),
    datasheet_url: "",
    visible_text: text.slice(0, 4000),
  };
})()`);
await tab.close();
if (capture.code && capture.code !== url.split("/").pop()) {
  throw new Error("Page JLCPCB Part # does not match the requested URL");
}
const fs = await import("node:fs");
fs.writeFileSync("<OUT>", JSON.stringify({ official_url: url, ...capture }, null, 2));
```

`stage-capture` sets `captured_on` to today and `capture_method` to
`zcode_inapp_browser_visible_page`; the reader must not set them by hand.

## Staged capture schema

`official_url`, `code`, `manufacturer`, `mpn`, `package`, `tier_label`
(visible badge: Basic / Preferred / Promotional / Extended), `description`,
`specifications` (object), `stock_observed`, `purchase_moq_observed`,
`full_reel_observed`, `available_order_qty_observed`, `datasheet_url`
(optional, query-free HTTPS), `visible_text` (first ~4000 chars of page
text, must contain the C-number), `captured_on`, `capture_method`.

## How the pool consumes staged captures

- `tier_label` Extended (queue class `preferred_extended`) → worker runs
  `defer --stage intake --code <C> --from-capture`, which composes the
  documented class-conflict reason from the staged facts and refuses a
  house-class capture.
- `tier_label` Basic/Preferred/Promotional matching the queue → worker runs
  the full intake flow via `intake_from_capture.py` under the family lock.
- Workers hand out only fresh captures with
  `next --stage intake --claim --staged-only --worker W1` (freshness window:
  `--staged-hours`, default 24). The `--staged-only` filter also works for a
  solo `next`.
