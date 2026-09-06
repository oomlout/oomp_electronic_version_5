const { chromium } = require(process.env.OOMP_PLAYWRIGHT || 'playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://www.lcsc.com/search?q=WS2812B', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(6000);
  console.log('title:', await page.title());
  const body = await page.evaluate(() => document.body.innerText.slice(0, 1500));
  console.log('BODY:\n' + body);
  const counts = await page.evaluate(() => ({
    tables: document.querySelectorAll('table').length,
    trs: document.querySelectorAll('table tr').length,
    cCodes: (document.body.innerText.match(/\bC\d{4,9}\b/g) || []).slice(0, 5),
  }));
  console.log('COUNTS:', JSON.stringify(counts));
  await browser.close();
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
