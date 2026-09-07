const { chromium } = require(process.env.OOMP_PLAYWRIGHT || 'playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await (await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
  })).newPage();
  for (const q of ['right angle pin header 2.54mm 3P', 'right angle long pin header 2.54mm 3P', 'XH SMD 2.5mm', 'pin header 2x3 2.54mm']) {
    await page.goto('https://www.lcsc.com/search?q=' + encodeURIComponent(q), { waitUntil: 'domcontentloaded', timeout: 30000 });
    try { await page.waitForFunction(() => /C\d{4,9}/.test(document.body.innerText), { timeout: 10000 }); } catch (e) {}
    await page.waitForTimeout(1200);
    const rows = await page.evaluate(() => {
      const out = [];
      const seen = new Set();
      for (const tr of document.querySelectorAll('table tr')) {
        const t = (tr.innerText || '').replace(/\s+/g, ' ').trim();
        const code = (t.match(/\bC\d{4,9}\b/) || [])[0];
        if (!code || seen.has(code)) continue;
        seen.add(code);
        let mpn = '';
        for (const a of tr.querySelectorAll('a[href*="product-detail"]')) {
          const c = (a.innerText || '').replace(/\s+/g, ' ').trim();
          if (c && c !== code) { mpn = c; break; }
        }
        out.push({ code, mpn, text: t.slice(0, 260) });
      }
      return out.slice(0, 5);
    });
    console.log('=== ' + q);
    for (const r of rows) console.log('  ', r.code, r.mpn, '::', r.text.slice(0, 200));
  }
  await browser.close();
})();
