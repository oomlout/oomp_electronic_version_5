const {chromium} = require(process.env.OOMP_PLAYWRIGHT);
const {pathToFileURL} = require('node:url');
const path = require('node:path');
(async () => {
  const browser = await chromium.launch({headless: true, executablePath: process.env.OOMP_CHROMIUM});
  try {
    const page = await browser.newPage({viewport: {width: 1440, height: 1000}});
    await page.goto(pathToFileURL(path.resolve(process.argv[2])).href);
    const reference = await page.evaluate(() => {
      let part;
      for (const item of document.querySelectorAll('.board-view[data-side="front"] .board-component')) {
        if (!part || item.querySelectorAll('text').length > part.querySelectorAll('text').length) part = item;
      }
      const svg = part.closest('.board-view').querySelector('svg');
      const b = part.getBBox();
      const matrix = svg.getCTM().inverse().multiply(part.getCTM());
      const points = [[b.x,b.y], [b.x+b.width,b.y], [b.x,b.y+b.height], [b.x+b.width,b.y+b.height]].map(([x,y]) => new DOMPoint(x,y).matrixTransform(matrix));
      const x = Math.min(...points.map(p=>p.x)), y = Math.min(...points.map(p=>p.y));
      const w = Math.max(...points.map(p=>p.x))-x, h = Math.max(...points.map(p=>p.y))-y;
      boardViewports.get(svg).target = [x-2,y-2,w+4,h+4];
      setZoom(1);
      selectComponent(part.dataset.reference);
      return part.dataset.reference;
    });
    const part = page.locator(`.board-view[data-side="front"] .board-component[data-reference="${reference}"]`);
    async function styles() {
      return part.evaluate(el => ({hover: el.matches(':hover'), focus: el.matches(':focus'), labels: [...el.querySelectorAll('text')].slice(0,4).map(text => ({text:text.textContent, stroke:getComputedStyle(text).stroke, strokeWidth:getComputedStyle(text).strokeWidth, fontSize:getComputedStyle(text).fontSize}))}));
    }
    await page.mouse.move(0,0);
    const before = await styles();
    await part.locator('text').first().hover();
    const hover = await styles();
    await part.locator('text').first().click();
    const click = await styles();
    await page.locator('.board-panel').screenshot({path: process.argv[3]});
    console.log(JSON.stringify({reference,before,hover,click},null,2));
  } finally { await browser.close(); }
})().catch(error => {console.error(error);process.exitCode=1;});
