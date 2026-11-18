const { chromium } = require(process.env.OOMP_PLAYWRIGHT || 'playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await (await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
  })).newPage();
  await page.goto('https://www.lcsc.com/search?q=0402%2010nF', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);
  const found = await page.evaluate(() => {
    const out = [];
    for (const el of document.querySelectorAll('a, div, span')) {
      const text = (el.innerText || '').replace(/\s+/g, ' ').trim();
      if (/^(Ceramic Capacitors|Chip Resistor - Surface Mount|LED Indication - Discrete)$/.test(text)) {
        const anchor = el.closest('a') || el.querySelector('a') || (el.parentElement && el.parentElement.closest('a'));
        out.push({ tag: el.tagName, text: text.slice(0, 40), href: anchor ? anchor.getAttribute('href') : null });
      }
    }
    return out.slice(0, 8);
  });
  console.log(JSON.stringify(found, null, 1));
  await browser.close();
})();
