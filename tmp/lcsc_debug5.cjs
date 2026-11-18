const { chromium } = require(process.env.OOMP_PLAYWRIGHT || 'playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await (await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
  })).newPage();
  await page.goto('https://www.lcsc.com/category/1142.html?globalKeyword=0402%2010nF', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(4000);
  const info = await page.evaluate(() => {
    for (const tr of document.querySelectorAll('table tr')) {
      const t = (tr.innerText || '');
      if (/\bC\d{6,9}\b/.test(t) && tr.querySelector('td')) {
        const links = Array.from(tr.querySelectorAll('a')).slice(0, 8).map(a => ({ href: (a.getAttribute('href') || '').slice(0, 60), text: (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40) }));
        return { rowText: t.replace(/\s+/g, ' ').slice(0, 400), links };
      }
    }
    return null;
  });
  console.log(JSON.stringify(info, null, 1));
  await browser.close();
})();
