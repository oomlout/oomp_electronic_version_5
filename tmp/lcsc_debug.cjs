const { chromium } = require(process.env.OOMP_PLAYWRIGHT || 'playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await (await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
    viewport: { width: 1400, height: 900 },
  })).newPage();
  await page.goto('https://www.lcsc.com/search?q=0402%2010nF', { waitUntil: 'domcontentloaded', timeout: 30000 });
  try {
    await page.waitForFunction(() => /C\d{4,9}/.test(document.body.innerText), { timeout: 12000 });
  } catch (e) { console.log('no codes at all'); }
  await page.waitForTimeout(1500);
  const info = await page.evaluate(() => {
    const text = document.body.innerText;
    const codes = (text.match(/C\d{6,9}/g) || []).slice(0, 5);
    // find first code element and climb
    let chain = null;
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
      if (/^C\d{6,9}$/.test(node.textContent.trim())) {
        let el = node.parentElement;
        const chainParts = [];
        for (let i = 0; i < 8 && el; i++) {
          chainParts.push({ tag: el.tagName, cls: String(el.className).slice(0, 60), textLen: (el.innerText || '').length, hasStock: /In Stock/i.test(el.innerText || '') });
          el = el.parentElement;
        }
        chain = chainParts;
        break;
      }
    }
    return { codes, chain, sample: text.slice(0, 400) };
  });
  console.log(JSON.stringify(info, null, 1));
  await browser.close();
})();
