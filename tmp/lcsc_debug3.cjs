const { chromium } = require(process.env.OOMP_PLAYWRIGHT || 'playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await (await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
  })).newPage();
  for (const id of [1158, 1156, 1157]) {
    await page.goto(`https://www.lcsc.com/category/${id}.html?globalKeyword=0402%2010nF`, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(3500);
    const info = await page.evaluate(() => {
      const rows = [];
      for (const tr of document.querySelectorAll('table tr')) {
        const t = (tr.innerText || '').replace(/\s+/g, ' ').trim();
        if (/\bC\d{4,9}\b/.test(t) && tr.querySelector('td')) rows.push(t.slice(0, 120));
      }
      return { title: document.title.slice(0, 60), rows: rows.slice(0, 2), count: rows.length };
    });
    console.log(id, JSON.stringify(info));
  }
  await browser.close();
})();
