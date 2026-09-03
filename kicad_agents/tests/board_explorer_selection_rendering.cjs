// Exercise actual SVG hover/focus: sidebar selection alone does not reproduce
// inherited text strokes caused by styling a hovered component's parent group.
const assert = require('node:assert/strict');

module.exports = async function checkSelectionRendering(page) {
  await page.locator('#clear-selection').click();
  await page.locator('.side-button[data-side="front"]').click();
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
    return part.dataset.reference;
  });
  const part = page.locator(`.board-view[data-side="front"] .board-component[data-reference="${reference}"]`);
  const label = part.locator('text').first();
  async function labelStyles() {
    return part.locator('text').evaluateAll(labels => labels.map(label => {
      const style = getComputedStyle(label);
      return {stroke: style.stroke, fill: style.fill, fontSize: style.fontSize, strokeWidth: style.strokeWidth};
    }));
  }
  await page.mouse.move(0, 0);
  const before = await labelStyles();
  assert(before.length > 1, 'Use a real multi-pin part with inline labels');
  assert(before.every(style => style.stroke === 'none'));
  await label.hover();
  assert(await part.evaluate(element => element.matches(':hover')));
  assert.deepEqual(await labelStyles(), before, 'Hover must not stroke/recolour pin labels');
  await label.click();
  assert(await part.evaluate(element => element.matches(':focus')), 'Native board click focuses the SVG part');
  assert.deepEqual(await labelStyles(), before, 'Click/focus must not stroke/recolour pin labels');
  await page.mouse.move(0, 0);
  await part.press('Enter');
  assert.deepEqual(await labelStyles(), before, 'Keyboard selection keeps labels clean');
  await label.click({modifiers: ['Control']});
  assert.equal(await page.evaluate(ref => selectedReferences.has(ref), reference), false);
  assert.deepEqual(await labelStyles(), before, 'Ctrl-deselection keeps focused labels clean');
  assert.equal(await part.locator('.selection-box, .hover-box').count(), 0, 'No highlight geometry is embedded in component artwork');

  // Check the independent highlight layer, placement and antialiasing on both
  // sides, including bottom views with no components.
  for (const side of ['front', 'back']) {
    await page.locator(`.side-button[data-side="${side}"]`).click();
    const rendering = await page.evaluate(side => {
      const view = document.querySelector(`.board-view[data-side="${side}"]`);
      const parts = [...view.querySelectorAll('.board-component')];
      const layer = view.querySelector('.component-highlights');
      if (!parts.length) return {empty: true, hasLayer: !!layer};
      const part = parts[0];
      selectComponent(part.dataset.reference);
      const box = [...layer.querySelectorAll('.selection-box')].find(box => box.dataset.reference === part.dataset.reference);
      const style = getComputedStyle(box);
      return {
        belowAllParts: parts.every(item => !!(layer.compareDocumentPosition(item) & Node.DOCUMENT_POSITION_FOLLOWING)),
        transform: box.getAttribute('transform'), expectedTransform: part.getAttribute('transform'),
        fill: style.fill, rendering: style.shapeRendering, pointerEvents: style.pointerEvents,
        rounded: Number(box.getAttribute('rx')) > 0,
        embedded: view.querySelectorAll('.board-component .selection-box, .board-component .hover-box').length,
      };
    }, side);
    if (rendering.empty) { assert(rendering.hasLayer); continue; }
    assert(rendering.belowAllParts, 'Every component label is above the selection and hover outlines');
    assert.equal(rendering.transform, rendering.expectedTransform, 'Highlight follows the native placement and rotation');
    assert.equal(rendering.fill, 'none');
    assert.equal(rendering.rendering, 'geometricprecision');
    assert.equal(rendering.pointerEvents, 'none');
    assert(rendering.rounded, 'Selection outline has smooth rounded corners');
    assert.equal(rendering.embedded, 0);
  }
  await page.locator('#clear-selection').click();
  await page.locator('#search').fill('');
  await page.locator('.side-button[data-side="front"]').click();
  await page.locator('#zoom-fit').click();
};
