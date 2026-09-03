// Keep status and detail panes stable as real component/net content changes.
const assert = require('node:assert/strict');

module.exports = async function checkStatusLayout(page) {
  assert.equal(await page.locator('.net-picker #net-status').count(), 0);
  assert.equal(await page.locator('.detail .selection-status #net-status').count(), 1);
  const targets = ['.list-panel', '.net-picker', '.part-list', '.board-panel', '.detail.panel', '.part-detail-scroll', '.selection-status', '#net-status'];
  async function sizes() {
    return page.evaluate(selectors => {
      const result = {};
      for (const selector of selectors) {
        const rect = document.querySelector(selector).getBoundingClientRect();
        result[selector] = [rect.width, rect.height];
      }
      return result;
    }, targets);
  }

  const viewports = [{width: 1440, height: 1000}, {width: 800, height: 900}, {width: 390, height: 844}];
  for (const viewport of viewports) {
    await page.setViewportSize(viewport);
    await page.locator('#clear-selection').click();
    const empty = await sizes();
    // Pick the real board's largest pin table and the most-connected net.
    await page.evaluate(() => {
      let largestPart = components[0];
      let largestNet = copper.nets[0];
      for (const component of components) {
        if (component.pads.length > largestPart.pads.length) largestPart = component;
      }
      for (const net of copper.nets) {
        if (net.pins.length > largestNet.pins.length) largestNet = net;
      }
      selectComponent(largestPart.reference);
      selectNet(largestNet.id);
      // Small boards can fit every real connection in a wide tablet pane.
      // Add stress-test rows only in the browser to exercise overflow there.
      const status = document.getElementById('net-status');
      if (status.scrollHeight <= status.clientHeight) {
        for (let index = 0; index < 40; index++) {
          const row = document.createElement('div');
          row.textContent = `Extra connection ${index}: ${largestNet.name}`;
          status.appendChild(row);
        }
      }
    });
    assert.deepEqual(await sizes(), empty, `Content must not resize panes at ${viewport.width}px`);
    const scrolling = await page.evaluate(() => {
      const status = document.getElementById('net-status');
      const part = document.querySelector('.part-detail-scroll');
      return {
        statusOverflow: getComputedStyle(status).overflowY,
        detailOverflow: getComputedStyle(part).overflowY,
        statusScrollable: status.scrollHeight > status.clientHeight,
        detailScrollable: part.scrollHeight > part.clientHeight,
        noHorizontalOverflow: status.scrollWidth <= status.clientWidth + 1 && part.scrollWidth <= part.clientWidth + 1,
        belowPart: status.getBoundingClientRect().top >= part.getBoundingClientRect().bottom,
      };
    });
    assert.equal(scrolling.statusOverflow, 'auto');
    assert.equal(scrolling.detailOverflow, 'auto');
    assert(scrolling.statusScrollable, `Long net connections get an internal scrollbar at ${viewport.width}px`);
    assert(scrolling.detailScrollable, 'Large pin tables get an independent scrollbar');
    assert(scrolling.noHorizontalOverflow, 'Long IDs and net names wrap within their panes');
    assert(scrolling.belowPart, 'Selection status stays below the matched-part details');
    await page.locator('#clear-selection').click();
    assert.deepEqual(await sizes(), empty, 'Clearing the selection does not resize panes');
  }
};
