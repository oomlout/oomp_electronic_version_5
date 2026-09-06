/* Resumable LCSC harvester: walks tmp/lcsc_queue_fix2.json, saves ranked rows to
   tmp/lcsc_results_fix.jsonl. Usage:
   OOMP_PLAYWRIGHT=<path> node tmp/lcsc_harvest.cjs [limit] [startKey] */
const fs = require('fs');
const path = require('path');
const ROOT = 'C:/gh/oomp_electronic_version_5';
const { chromium } = require(process.env.OOMP_PLAYWRIGHT || 'playwright');

const queue = JSON.parse(fs.readFileSync(path.join(ROOT, 'tmp/lcsc_queue_fix2.json'), 'utf-8'));
const outPath = path.join(ROOT, 'tmp/lcsc_results_fix.jsonl');
const done = new Set();
if (fs.existsSync(outPath)) {
  for (const line of fs.readFileSync(outPath, 'utf-8').split('\n')) {
    if (!line.trim()) continue;
    try { done.add(JSON.parse(line).key); } catch (e) {}
  }
}

const EXTRACT = () => {
  const clean = (t) => String(t || '').replace(/\s+/g, ' ').trim();
  const out = [];
  const seen = new Set();
  const parseBlock = (element, fullText) => {
    const text = clean(fullText);
    const codeMatch = text.match(/\b(C\d{4,9})\b/);
    if (!codeMatch) return;
    const code = codeMatch[1];
    if (seen.has(code)) return;
    const stockMatch = text.match(/([\d,]+)\s*In Stock/i);
    const inStock = !!stockMatch;
    if (!inStock) return;
    const stock = parseInt(stockMatch[1].replace(/,/g, ''), 10);
    let mpn = '';
    for (const anchor of element.querySelectorAll('a[href*="product-detail"]')) {
      const candidate = clean(anchor.innerText);
      if (candidate && candidate !== code && !/^View/.test(candidate)) { mpn = candidate.split(' ').pop(); break; }
    }
    if (!mpn) {
      const mpnMatch = text.match(new RegExp('([A-Za-z0-9][A-Za-z0-9./+\\-]{1,30})\s+' + code));
      if (mpnMatch) mpn = mpnMatch[1];
    }
    let manufacturer = '';
    const brandLink = element.querySelector('a[href*="brand-detail"]');
    if (brandLink) manufacturer = clean(brandLink.innerText);
    if (!manufacturer) {
      const leadMatch = text.match(/([A-Za-z][A-Za-z0-9&'.\-]*(?:\s+[A-Za-z][A-Za-z0-9&'.\-]*)?)\s+[\d,]+\s+In\s+Stock/i);
      if (leadMatch) {
        manufacturer = leadMatch[1].replace(/\s*(Hot Asian Brands|Preferred|Hot)$/, '').trim();
      }
    }
    const cells = Array.from(element.querySelectorAll('td')).map((c) => clean(c.innerText));
    const packaging = /tape|reel|tray|cut tape|^-?$|^\d{4}$/i;
    const candidates = cells.filter((c) => c.length > 12 && !packaging.test(c));
    let description = candidates.length ? candidates.reduce((a, b) => (b.length > a.length ? b : a), '') : text;
    if (description.length > 220) description = description.slice(0, 220);
    const basic = /\bbasic\b/i.test(text) && !/extended/i.test(text.slice(-120));
    const tags = [];
    if (/\bbasic\b/i.test(text)) tags.push('basic');
    if (/extended/i.test(text)) tags.push('extended');
    out.push({ code, mpn, manufacturer, stock, description, tags });
    seen.add(code);
  };
  for (const table of document.querySelectorAll('table')) {
    for (const tr of table.querySelectorAll('tr')) {
      if (!tr.querySelector('td')) continue;
      parseBlock(tr, tr.innerText);
    }
  }
  if (!out.length) {
    // search pages render div cards
    for (const span of document.querySelectorAll('span')) {
      if (!/^C\d{4,9}$/.test(clean(span.innerText))) continue;
      let card = span.parentElement;
      for (let i = 0; i < 8 && card; i++) {
        const t = card.innerText || '';
        if (/In Stock/i.test(t) && t.length < 1500) break;
        card = card.parentElement;
      }
      if (card) parseBlock(card, card.innerText);
    }
  }
  out.sort((a, b) => b.stock - a.stock);
  return out.slice(0, 12);
};

(async () => {
  const limit = parseInt(process.argv[2] || '0', 10);
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
    viewport: { width: 1400, height: 900 },
    locale: 'en-US',
  });
  const page = await context.newPage();
  const pending = queue.filter((e) => !done.has(e.part_id));
  console.log(`pending ${pending.length} of ${queue.length}`);
  let processed = 0;
  for (const entry of pending) {
    if (limit && processed >= limit) break;
    const url = entry.category
      ? `https://www.lcsc.com/category/${entry.category}.html?globalKeyword=${encodeURIComponent(entry.query)}`
      : `https://www.lcsc.com/search?q=${encodeURIComponent(entry.query)}`;
    let rows = [];
    let status = 'ok';
    try {
      let loaded = false;
      for (let attempt = 0; attempt < 5 && !loaded; attempt++) {
        await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
        const head = await page.evaluate(() => (document.body ? document.body.innerText.slice(0, 200) : ''));
        if (/Access Denied/i.test(head)) { await page.waitForTimeout(9000 + attempt * 4000); continue; }
        loaded = true;
        try {
          await page.waitForFunction(() => {
            const text = document.body ? document.body.innerText : '';
            return /C\d{4,9}/.test(text) && /In Stock|No products|results found/i.test(text);
          }, { timeout: 12000 });
        } catch (e) { /* fall through and harvest what is there */ }
      }
      await page.waitForTimeout(700);
      rows = await page.evaluate(EXTRACT);
      const body = await page.evaluate(() => (document.body ? document.body.innerText.slice(0, 300) : ''));
      if (/robot|captcha|verify/i.test(body)) status = 'captcha';
    } catch (error) {
      status = 'error: ' + String(error).slice(0, 120);
    }
    fs.appendFileSync(outPath, JSON.stringify({ key: entry.part_id, kind: entry.kind, query: entry.query, url, status, rows }) + '\n');
    processed += 1;
    if (processed % 10 === 0) console.log(`[${processed}/${pending.length}] last ${entry.part_id} rows=${rows.length} ${status}`);
    await page.waitForTimeout(900);
  }
  await browser.close();
  console.log('harvest done, processed', processed);
})();
