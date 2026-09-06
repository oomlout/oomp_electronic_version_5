const fs = require('fs');
const { chromium } = require(process.env.OOMP_PLAYWRIGHT || 'playwright');
const EXTRACT = () => {
  const clean = (t) => String(t || '').replace(/\s+/g, ' ').trim();
  const out = [];
  const seen = new Set();
  const blocks = [];
  document.querySelectorAll('table tr').forEach((tr) => blocks.push(tr));
  document.querySelectorAll('div[class*="card"], div[class*="item"], li[class*="item"]').forEach((d) => blocks.push(d));
  for (const element of blocks) {
    const text = clean(element.innerText);
    const codeMatch = text.match(/\b(C\d{4,9})\b/);
    if (!codeMatch) continue;
    const code = codeMatch[1];
    if (seen.has(code)) continue;
    const stockMatch = text.match(/([\d,]+)\s*In Stock/i);
    if (!stockMatch) continue;
    seen.add(code);
    out.push({ code, text: text.slice(0, 200) });
    if (out.length >= 8) break;
  }
  return out;
};
(async () => {
  const queries = [
    ['electronic_led_5050_rgb_ws2812b_worldsemi_ws2812b_b_w', 'https://www.lcsc.com/category/412.html?globalKeyword=WS2812B'],
    ['electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_2n7002', 'https://www.lcsc.com/search?q=2N7002'],
    ['electronic_ic_soic_8_logic_comparator_lm393', 'https://www.lcsc.com/search?q=LM393DR2G'],
  ];
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const out = {};
  for (const [key, url] of queries) {
    let rows = [];
    for (let attempt = 0; attempt < 6 && rows.length === 0; attempt++) {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
      const title = await page.title();
      if (/Access Denied/i.test(title)) { await page.waitForTimeout(12000 + attempt * 5000); continue; }
      try {
        await page.waitForFunction(() => /C\d{4,9}/.test(document.body.innerText) && /In Stock|No products|results/i.test(document.body.innerText), { timeout: 15000 });
      } catch (e) {}
      await page.waitForTimeout(1000);
      rows = await page.evaluate(EXTRACT);
      if (rows.length === 0) await page.waitForTimeout(8000);
    }
    out[key] = rows;
    console.log(key.slice(0, 50), 'rows:', rows.length);
  }
  fs.writeFileSync('C:/gh/oomp_electronic_version_5/tmp/lcsc_retry3.json', JSON.stringify(out, null, 1));
  await browser.close();
})().catch((e) => { console.error('ERR', e.message); process.exit(1); });
