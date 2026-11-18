const { chromium } = require(process.env.OOMP_PLAYWRIGHT || 'playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await (await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
  })).newPage();
  await page.goto('https://www.lcsc.com/search?q=0402%2010nF', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);
  const links = await page.evaluate(() => {
    const out = [];
    for (const a of document.querySelectorAll('a[href*="/category/"]')) {
      out.push({ href: a.getAttribute('href').split('?')[0], text: (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 50) });
    }
    const seen = new Set();
    return out.filter(l => !seen.has(l.href + l.text) && seen.add(l.href + l.text)).slice(0, 12);
  });
  console.log(JSON.stringify(links, null, 1));
  await browser.close();
})();
