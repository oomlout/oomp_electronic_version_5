// Shared offline interaction checks, called by board_explorer_smoke.cjs.
const assert = require('node:assert/strict');

module.exports = async function checkMultiSelect(page) {
  const ctrl = {modifiers: ['Control']};
  const references = () => page.evaluate(() => [...selectedReferences].sort());
  const selected = () => page.evaluate(() => selectedPins);
  const netIds = () => page.evaluate(() => [...highlightedNetIds()].sort());
  const heading = category => page.locator(`.category-group[data-category="${category}"] > summary span`);
  const partButton = reference => page.locator(`.part-button[data-reference="${reference}"]`);
  async function clickPart(reference, modifiers = ctrl) {
    await page.locator('#search').fill(reference);
    await partButton(reference).click(modifiers);
  }
  async function clickPin(pin, modifiers = ctrl) {
    await page.locator('#search').fill(pin.reference);
    const row = page.locator('.part-row').filter({has: partButton(pin.reference)});
    if (!(await row.locator('.pin-menu').evaluate(element => element.open))) {
      await row.locator('.pin-menu > summary').click();
    }
    await row.locator(`.pin-button[data-pin="${pin.number}"]`).first().click(modifiers);
  }

  await page.locator('#clear-selection').click();
  await page.locator('#search').fill('');
  await page.locator('.side-button[data-side="front"]').click();
  const categoryOpen = await page.locator('.category-group[open]').count();
  const groups = await page.evaluate(() => ({
    resistor: components.filter(c => c.category === 'resistor').map(c => c.reference).sort(),
    capacitor: components.filter(c => c.category === 'capacitor').map(c => c.reference).sort(),
  }));
  await heading('resistor').click(ctrl);
  await heading('capacitor').click(ctrl);
  assert.deepEqual(await references(), [...groups.resistor, ...groups.capacitor].sort());
  assert.equal(await page.locator('.category-group[open]').count(), categoryOpen, 'Ctrl-category does not expand/collapse');
  await heading('resistor').click(ctrl);
  assert.deepEqual(await references(), groups.capacitor, 'Ctrl-category removes only its members');
  await heading('capacitor').click(ctrl);
  assert.deepEqual(await references(), []);

  const examples = await page.evaluate(() => {
    const front = components.filter(c => c.side === 'front');
    const parts = [front.find(c => c.category === 'resistor'), front.find(c => c.category === 'capacitor')];
    const pins = [];
    for (const component of front) {
      for (const pin of component.pads) {
        if (pin.net_id && !pins.some(p => p.net_id === pin.net_id)) {
          pins.push({reference: component.reference, number: pin.number, net_id: pin.net_id});
          break;
        }
      }
      if (pins.length === 2) break;
    }
    return {parts: parts.map(c => c.reference), pins};
  });
  const [first, second] = examples.parts;
  assert.equal(examples.pins.length, 2, 'Two independently routed pins available');
  await clickPart(first, {});
  await clickPart(second);
  assert.deepEqual(await references(), [first, second].sort(), 'Ctrl-component adds to the selection');
  await clickPart(first);
  assert.deepEqual(await references(), [second], 'Ctrl-component deselects without losing the other part');
  assert.equal(await partButton(first).getAttribute('aria-pressed'), 'false');
  await clickPart(second);
  assert.deepEqual(await references(), []);

  await clickPart(first);
  for (const pin of examples.pins) await clickPin(pin);
  assert.deepEqual(await references(), [first], 'Ctrl-pin preserves component selection');
  assert.equal((await selected()).length, 2);
  assert.deepEqual(await netIds(), examples.pins.map(p => p.net_id).sort(), 'Both pin nets are highlighted');
  const highlighted = await page.evaluate(() => {
    const pins = new Set();
    for (const element of document.querySelectorAll('.copper-overlay .copper-pad.selected-pin')) {
      pins.add(`${element.dataset.reference}.${element.dataset.pin}`);
    }
    return [...pins].sort();
  });
  assert.deepEqual(highlighted, examples.pins.map(p => `${p.reference}.${p.number}`).sort());
  await clickPart(first);
  assert.deepEqual(await references(), []);
  assert.equal((await selected()).length, 2, 'Ctrl-component deselection preserves selected pins');
  await page.locator('#search').fill('');
  await heading('resistor').click(ctrl);
  await page.locator('#highlight-selected-nets').check();
  assert.equal((await selected()).length, 2, 'Bulk-net toggle preserves explicitly selected pins');
  await page.locator('#highlight-selected-nets').uncheck();
  await heading('resistor').click(ctrl);
  assert.deepEqual(await netIds(), examples.pins.map(p => p.net_id).sort());
  await page.locator('.side-button[data-side="back"]').click();
  assert.equal((await selected()).length, 2, 'Side changes preserve pin multiselection');
  await page.locator('.side-button[data-side="front"]').click();
  await clickPin(examples.pins[0]);
  assert.deepEqual(await selected(), [examples.pins[1]], 'Ctrl-pin removes just the clicked pin');
  assert.deepEqual(await netIds(), [examples.pins[1].net_id]);
  await clickPin(examples.pins[1]);
  assert.deepEqual(await selected(), []);
  assert.equal(await page.locator('.copper-overlay .copper-feature').count(), 0);

  // Ctrl-clicking the Pins heading toggles the whole pin group without expansion.
  const groupReference = examples.pins[0].reference;
  await page.locator('#search').fill(groupReference);
  const menu = page.locator('.part-row').filter({has: partButton(groupReference)}).locator('.pin-menu');
  const wasOpen = await menu.evaluate(element => element.open);
  await menu.locator('summary').click(ctrl);
  const uniqueCount = await page.evaluate(reference => {
    const ids = new Set();
    for (const pin of byReference.get(reference).pads) ids.add(`${pin.number}/${pin.net_id}`);
    return ids.size;
  }, groupReference);
  assert.equal((await selected()).length, uniqueCount, 'Pin group deduplicates repeated physical pads');
  assert.equal(await menu.evaluate(element => element.open), wasOpen);
  await menu.locator('summary').click(ctrl);
  assert.equal((await selected()).length, 0);

  for (const pin of examples.pins) await clickPin(pin);
  await clickPin(examples.pins[0], {});
  assert.deepEqual(await selected(), [examples.pins[0]], 'Ordinary pin click returns to one pin/net');
  await page.keyboard.press('Escape');
  assert.deepEqual(await selected(), []);
  await page.locator('#clear-selection').click();
  await page.locator('#search').fill('');
};
