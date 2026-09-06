// Offline browser smoke test. Requires Playwright; no network or installs.
// node board_explorer_smoke.cjs path/to/board_explorer.html [screenshot.png]
// Optional OOMP_PLAYWRIGHT and OOMP_CHROMIUM override local runtime paths.
const {chromium} = require(process.env.OOMP_PLAYWRIGHT || 'playwright');
const assert = require('node:assert/strict');
const {pathToFileURL} = require('node:url');
const path = require('node:path');

(async () => {
  const browser = await chromium.launch({headless: true, executablePath: process.env.OOMP_CHROMIUM || undefined});
  try {
    const page = await browser.newPage({viewport: {width: 1440, height: 1000}});
    const errors = [];
    const requests = [];
    page.on('pageerror', error => errors.push(String(error)));
    page.on('request', request => { if (/^https?:/.test(request.url())) requests.push(request.url()); });
    await page.goto(pathToFileURL(path.resolve(process.argv[2])).href);
    // Category headings stay visible while their component rows start collapsed.
    await page.waitForSelector('.category-select');
    await page.waitForSelector('.part-button', {state: 'attached'});
    assert.equal(await page.locator('.category-group[open]').count(), 0, 'All categories start collapsed');
    assert.equal(await page.locator('.part-button:visible').count(), 0, 'Component rows start hidden');
    const firstCategory = page.locator('.category-group').first();
    await firstCategory.locator(':scope > summary span').click();
    assert(await firstCategory.getAttribute('open') !== null, 'Categories can be opened manually');
    assert(await firstCategory.locator('.part-button:visible').count() > 0);
    await firstCategory.locator(':scope > summary span').click();
    assert.equal(await page.locator('.category-group[open]').count(), 0, 'Categories can be collapsed again');
    assert.equal(await page.locator('#copper-layer').inputValue(), 'all');
    assert(await page.locator('#show-fills').isChecked(), 'Fills default on');
    assert(!(await page.locator('#zoom-to-net').isChecked()), 'Automatic zoom defaults off');
    assert(!(await page.locator('#highlight-selected-nets').isChecked()), 'Bulk nets default off');
    assert.equal(await page.locator('.net-picker, #net-search, #net-select, .selection-tools, #selection-count').count(), 0, 'The follow-a-net picker and the sidebar selection tools are gone');
    assert.equal(await page.locator('.selection-status-header #clear-selection').count(), 1, 'Clear lives in the selection status header');
    assert.equal(await page.evaluate(() => selectedReferences.size), 0, 'Nothing is selected on load');
    const summaryHtml = await page.locator('#net-status').innerHTML();
    assert(summaryHtml.includes('OOMP matching') && /\d+\/\d+ matched · \d+%/.test(summaryHtml), 'Idle status shows the OOMP matching total and ratio');
    assert((await page.locator('.match-rows span').count()) > 0, 'Idle status lists per-category matched/total rows');
    const summaryCounts = await page.evaluate(() => {
      const counted = components.filter(c => c.category !== 'other');
      const match = document.getElementById('net-status').textContent.match(/(\d+)\/(\d+) matched/);
      return {expected: counted.length, shown: Number(match[2]),
        hasOthers: components.some(c => c.category === 'other'),
        hasOtherRow: [...document.querySelectorAll('.match-rows span')].some(span => span.textContent.startsWith('Other '))};
    });
    assert.equal(summaryCounts.shown, summaryCounts.expected, 'Matching total counts every category except other');
    assert(!summaryCounts.hasOthers || !summaryCounts.hasOtherRow, 'The other category is left out of the matching rows');
    const projectLink = page.locator('.project-card-link');
    if (await projectLink.count()) {
      assert((await projectLink.getAttribute('href')).startsWith('https://github.com/'), 'Project card links to the repository');
      assert.equal(await projectLink.getAttribute('target'), '_blank');
      assert((await projectLink.getAttribute('rel')).includes('noopener'));
    }
    assert((await page.locator('.project-card-title').textContent()).length > 0, 'Left pane opens with a project summary card');
    const headerLink = page.locator('header .github-link');
    if (await headerLink.count()) {
      assert((await headerLink.getAttribute('href')).startsWith('https://github.com/'), 'Header shows a GitHub link for the project');
      assert.equal(await headerLink.getAttribute('target'), '_blank');
      assert((await headerLink.getAttribute('rel')).includes('noopener'));
    }
    assert.deepEqual(await page.locator('.board-toolbar .net-selection-controls input').evaluateAll(inputs => inputs.map(input => input.id)), ['zoom-to-net', 'highlight-selected-nets'], 'Net controls are grouped together in the board toolbar');
    const initialViewBox = await page.locator('.board-view[data-side="front"] > svg').getAttribute('viewBox');
    const candidate = await page.evaluate(() => {
      for (const component of components) {
        if (component.side !== 'front') continue;
        for (const pin of component.pads) {
          const net = byNet.get(pin.net_id);
          if (net && net.track_count > 0 && net.pins.length >= 2 && net.pins.length < 12) return {reference: component.reference, number: pin.number, netId: net.id, name: net.name};
        }
      }
    });
    assert(candidate, 'Need a multi-pin routed net for the interaction test');
    await page.locator('#search').fill(candidate.reference);
    const row = page.locator('.part-row').filter({has: page.locator(`.part-button[data-reference="${candidate.reference}"]`)});
    await row.locator('summary').click();
    await row.locator(`.pin-button[data-pin="${candidate.number}"]`).first().click();
    assert.equal(await page.evaluate(() => activeNet), candidate.netId);
    assert(await page.locator('.board-view:not([hidden]) .copper-overlay .copper-feature:not(.layer-hidden):not(.fill-hidden)').count() > 0);
    assert(await row.locator('details').getAttribute('open') !== null, 'Pin menu stays expanded after selection');
    assert(await page.locator('.board-view:not([hidden]) .copper-overlay .copper-pad.selected-pin').count() > 0);
    assert.equal(await page.locator('.selected-pin-ring').count(), 0, 'No enlarged halo around exact-sized pads');
    const padRendering = await page.evaluate(() => {
      const view = document.querySelector('.board-view:not([hidden]) > svg');
      const overlay = view.querySelector('.copper-overlay');
      const part = view.querySelector('.board-component');
      const anchor = overlay.querySelector('.copper-pad .pad-anchor');
      return {belowArtwork: !!(overlay.compareDocumentPosition(part) & Node.DOCUMENT_POSITION_FOLLOWING),
        stroke: getComputedStyle(anchor).stroke, rendering: getComputedStyle(anchor).shapeRendering};
    });
    assert(padRendering.belowArtwork, 'Selected pads and tracks sit below component labels');
    assert.equal(padRendering.stroke, 'none', 'No rough screen-pixel pad edging');
    assert.equal(padRendering.rendering, 'geometricprecision');
    // The part artwork's own pads carry class="pad" and stay solid white on
    // the board, with only the designator label rendered above them.
    const artworkPads = await page.evaluate(() =>
      [...document.querySelectorAll('.board-view .board-component .pad')]
        .map(pad => getComputedStyle(pad).fill));
    assert(artworkPads.length > 0, 'Part artwork includes pad primitives');
    assert(artworkPads.every(fill => fill === 'rgb(255, 255, 255)'), 'Part artwork pads stay solid white on the board');
    assert.equal(await page.locator('.board-view[data-side="front"] > svg').getAttribute('viewBox'), initialViewBox, 'Selecting a net does not zoom by default');
    await page.locator('#zoom-to-net').check();
    const netViewBox = await page.locator('.board-view[data-side="front"] > svg').getAttribute('viewBox');
    assert.notEqual(netViewBox, initialViewBox, 'Opt-in zoom fits the chosen net');
    const fits = await page.evaluate(() => {
      const svg = document.querySelector('.board-view:not([hidden]) > svg');
      const viewport = svg.viewBox.baseVal;
      for (const element of svg.querySelectorAll('.copper-overlay .copper-feature:not(.layer-hidden):not(.fill-hidden)')) {
        const b = element.getBBox();
        const matrix = svg.getCTM().inverse().multiply(element.getCTM());
        for (const [x,y] of [[b.x,b.y],[b.x+b.width,b.y+b.height]]) {
          const p = new DOMPoint(x,y).matrixTransform(matrix);
          if (p.x < viewport.x-.001 || p.y < viewport.y-.001 || p.x > viewport.x+viewport.width+.001 || p.y > viewport.y+viewport.height+.001) return false;
        }
      }
      return true;
    });
    assert(fits, 'Selected net stays entirely inside the automatic viewport');
    await page.locator('#copper-layer').selectOption('all');
    const counts = await page.evaluate(() => {
      const net = byNet.get(activeNet);
      const view = document.querySelector('.board-view:not([hidden])');
      return {expected: net.track_count, actual: view.querySelectorAll('.copper-overlay .copper-segment, .copper-overlay .copper-arc').length};
    });
    assert.equal(counts.actual, counts.expected, 'Every segment on the net is highlighted');
    await page.locator('.side-button[data-side="back"]').click();
    assert.equal(await page.evaluate(() => activeNet), candidate.netId, 'Side switching preserves the selected net');
    assert(await page.locator('.board-view[data-side="back"] .copper-overlay .copper-feature').count() > 0);
    await page.locator('.side-button[data-side="front"]').click();
    await page.locator('#zoom-to-net').uncheck();
    assert.equal(await page.locator('.board-view[data-side="front"] > svg').getAttribute('viewBox'), initialViewBox, 'Turning automatic zoom off restores board fit');
    await page.locator('#zoom-in').click();
    assert.equal(await page.locator('#zoom-label').textContent(), '125%');
    await page.locator('#zoom-fit').click();
    assert.equal(await page.locator('#zoom-label').textContent(), '100%');
    if (process.argv[3]) await page.screenshot({path: process.argv[3], fullPage: true});
    const endpoint = await page.evaluate(() => {
      const buttons = [...document.querySelectorAll('#net-status button[data-reference]')];
      const current = selectedPins[selectedPins.length - 1];
      const chosen = buttons.find(button => !(current && button.dataset.reference === current.reference && button.dataset.pin === current.number)) || buttons[0];
      return {reference: chosen.dataset.reference, pin: chosen.dataset.pin};
    });
    const endpointButton = page.locator(`#net-status button[data-reference="${endpoint.reference}"][data-pin="${endpoint.pin}"]`);
    await endpointButton.click();
    assert.equal(await page.locator('#detail h2').textContent(), endpoint.reference, 'Selecting a pin populates its part in the detail pane');
    assert.equal(await page.evaluate(() => activeNet), candidate.netId);
    await endpointButton.click();
    assert.equal(await page.evaluate(() => selectedPins.length), 0, 'Clicking the followed pin again deselects it');
    assert.equal(await page.locator('#detail h2').textContent(), endpoint.reference, 'Its part stays populated after the pin deselects');
    // Deselecting the pin drops the status window back to the component view,
    // so pick the same pad from the detail pane to restore the net view.
    const endpointIndex = await page.evaluate(endpoint => {
      const component = byReference.get(endpoint.reference);
      return component.pads.findIndex(pin => pin.number === endpoint.pin);
    }, endpoint);
    await page.locator(`#detail [data-pin-index="${endpointIndex}"]`).click();
    assert.equal(await page.evaluate(() => activeNet), candidate.netId);
    await page.locator('#show-traces').uncheck();
    assert(await page.locator('#board-stage').evaluate(element => element.classList.contains('hide-traces')));
    assert(await page.locator('.board-view:not([hidden]) .copper-overlay .copper-feature').count() > 0, 'Selected net stays visible with background traces off');
    await page.locator('#search').fill('GND');
    const ground = await page.evaluate(() => copper.nets.find(net => net.name === 'GND'));
    assert(ground);
    assert((await page.locator('.net-results .net-link').count()) > 0, 'Net names are searchable from the main box');
    await page.locator(`.net-results .net-link[data-net-id="${ground.id}"]`).click();
    assert.equal(await page.evaluate(() => activeNet), ground.id, 'Clicking a net result follows that net');
    await page.locator(`.net-results .net-link[data-net-id="${ground.id}"]`).click();
    assert.equal(await page.evaluate(() => activeNet), '', 'Clicking the followed net again deselects it');
    await page.locator(`.net-results .net-link[data-net-id="${ground.id}"]`).click();
    assert.equal(await page.evaluate(() => activeNet), ground.id, 'The net result can be followed again');
    const colors = await page.evaluate(() => {
      const byLayer = {};
      for (const element of document.querySelectorAll('.board-view:not([hidden]) .copper-overlay .copper-segment')) {
        byLayer[element.dataset.layers] = getComputedStyle(element).color;
      }
      return byLayer;
    });
    if (Object.keys(colors).length > 1) assert.equal(new Set(Object.values(colors)).size, Object.keys(colors).length, 'Each copper layer gets a distinct highlight colour');
    await page.locator('#show-fills').check();
    assert(await page.locator('.board-view:not([hidden]) .copper-overlay .copper-zone:not(.fill-hidden)').count() > 0);
    await page.keyboard.press('Escape');
    assert.equal(await page.evaluate(() => activeNet), '');
    assert.equal(await page.locator('.copper-overlay .copper-feature').count(), 0);
    await page.locator('#search').fill('');
    await page.locator('#show-traces').check();
    const dimensions = await page.evaluate(() => {
      const sidebar = document.querySelector('.list-panel');
      return {width: sidebar.getBoundingClientRect().width, scroll: sidebar.scrollWidth, client: sidebar.clientWidth};
    });
    assert(dimensions.width <= 261 && dimensions.scroll <= dimensions.client + 1, 'Sidebar does not expand or overflow');
    // Exercise the unassigned-pad branch when the board has one. It must not
    // highlight all other pads that also have an empty net name.
    const unassigned = await page.evaluate(() => {
      for (const component of components) {
        const pin = component.pads.find(pin => !pin.net_id);
        if (pin) return {reference: component.reference, number: pin.number, side: component.side};
      }
    });
    if (unassigned) {
      await page.locator(`.side-button[data-side="${unassigned.side}"]`).click();
      await page.locator('#search').fill(unassigned.reference);
      const row = page.locator('.part-row').filter({has: page.locator(`.part-button[data-reference="${unassigned.reference}"]`)});
      if (!(await row.locator('details').evaluate(element => element.open))) await row.locator('summary').click();
      await row.locator(`.pin-button[data-pin="${unassigned.number}"]`).first().click();
      assert.equal(await page.evaluate(() => activeNet), '');
      const wrong = await page.locator('.copper-overlay .copper-feature').evaluateAll((elements, pin) => elements.filter(element => element.dataset.reference !== pin.reference || element.dataset.pin !== pin.number).length, unassigned);
      assert.equal(wrong, 0);
    }
    // Clicking a selected component deselects it and refreshes the status box.
    await page.locator('#clear-selection').click();
    await page.locator('#search').fill(candidate.reference);
    const toggleButton = page.locator(`.part-button[data-reference="${candidate.reference}"]`).first();
    await toggleButton.click();
    assert(await page.evaluate(r => selectedReferences.has(r), candidate.reference), 'First click selects the component');
    assert((await page.locator('#net-status').innerHTML()).includes(candidate.reference), 'Selection status updates on a single item click');
    await toggleButton.click();
    assert(!(await page.evaluate(r => selectedReferences.has(r), candidate.reference)), 'Second click on the selected component deselects it');
    assert((await page.locator('#net-status').innerHTML()).includes('OOMP matching'), 'Deselecting returns to the matching summary');
    assert.equal(await page.locator('#detail p.empty').count(), 1, 'Deselecting everything restores the initial detail prompt');
    // Outline-only selection: clicking a part's empty interior must not select
    // it, and no invisible bounding-box layer may exist. Copper under a part
    // stays directly clickable.
    const hitProbe = await page.evaluate(() => {
      const view = document.querySelector('.board-view[data-side="front"]');
      const svg = view.querySelector('svg');
      const partProbe = {found: false}, traceProbe = {found: false};
      if (svg.querySelector('.component-hitbox, .component-hits')) partProbe.hitboxesLeft = true;
      for (const part of view.querySelectorAll('.board-component')) {
        if (partProbe.found) break;
        const b = part.getBBox();
        const point = new DOMPoint(b.x + b.width / 2, b.y + b.height / 2).matrixTransform(part.getScreenCTM());
        const target = document.elementFromPoint(point.x, point.y);
        if (!target || target.closest('.copper-feature') || target.closest('.board-component') === part) continue;
        partProbe.found = true;
        partProbe.reference = part.dataset.reference;
        partProbe.x = point.x; partProbe.y = point.y;
      }
      for (const segment of view.querySelectorAll('.copper-base .copper-segment')) {
        if (traceProbe.found) continue;
        const b = segment.getBBox();
        const point = new DOMPoint(b.x + b.width / 2, b.y + b.height / 2).matrixTransform(segment.getScreenCTM());
        const target = document.elementFromPoint(point.x, point.y);
        if (target !== segment && !(target && target.closest('.copper-feature') === segment)) continue;
        traceProbe.found = true;
        traceProbe.netId = segment.dataset.netId;
        traceProbe.x = point.x; traceProbe.y = point.y;
      }
      return {partProbe, traceProbe};
    });
    assert(!hitProbe.partProbe.hitboxesLeft, 'No bounding-box hitboxes remain on the board');
    if (hitProbe.partProbe.found) {
      await page.mouse.click(hitProbe.partProbe.x, hitProbe.partProbe.y);
      assert(!(await page.evaluate(r => selectedReferences.has(r), hitProbe.partProbe.reference)), 'Clicking a part\'s empty interior no longer selects it');
    }
    if (hitProbe.traceProbe.found) {
      await page.mouse.click(hitProbe.traceProbe.x, hitProbe.traceProbe.y);
      assert.equal(await page.evaluate(() => activeNet), hitProbe.traceProbe.netId, 'Traces stay clickable under and around the parts');
      const tracePart = await page.evaluate(() => byReference.get(activeReference));
      if (tracePart) assert(await page.evaluate(r => selectedReferences.has(r), tracePart.reference), 'Following a trace shows one of the parts it connects');
    }
    // Selecting a part that sits on the hidden side must populate the detail
    // pane without flipping the board view.
    const flipProbe = await page.evaluate(() => {
      const hiddenPart = components.find(component => component.side !== activeSide);
      if (!hiddenPart) return null;
      selectComponent(hiddenPart.reference);
      return {
        reference: hiddenPart.reference,
        side: activeSide,
        backHidden: document.querySelector('.board-view[data-side="back"]').hidden,
        detail: document.querySelector('#detail h2') ? document.querySelector('#detail h2').textContent : '',
        strayHits: [...document.querySelectorAll('.board-view[data-side="front"] .component-hitbox')].filter(box => {
          const component = byReference.get(box.dataset.reference);
          return component && component.side === 'back';
        }).length,
      };
    });
    if (flipProbe) {
      assert.equal(flipProbe.side, 'front', 'Selecting a hidden-side part keeps the shown board side');
      assert.equal(flipProbe.backHidden, true, 'A selection never flips the board to the hidden side');
      assert.equal(flipProbe.detail, flipProbe.reference, 'The hidden-side part still populates the detail pane');
      assert.equal(flipProbe.strayHits, 0, 'The front view only exposes front-side hitboxes');
    }
    await page.locator('#clear-selection').click();
    await page.locator('#search').fill('');
    // Select whole categories across both board sides, then the union of nets.
    await page.locator('.side-button[data-side="front"]').click();
    await page.locator('#clear-selection').click();
    const categoryCheckbox = page.locator('.category-select[data-category="resistor"]');
    await categoryCheckbox.check();
    const categoryState = await page.evaluate(() => ({
      expected: components.filter(c => c.category === 'resistor').map(c => c.reference).sort(),
      actual: [...selectedReferences].sort(),
      marked: [...new Set([...document.querySelectorAll('.board-component.is-active')].map(e => e.dataset.reference))].sort(),
    }));
    assert(categoryState.expected.length > 1);
    assert.deepEqual(categoryState.actual, categoryState.expected);
    assert.deepEqual(categoryState.marked, categoryState.expected);
    await page.locator('#highlight-selected-nets').check();
    const bulk = await page.evaluate(() => {
      const expected = new Set();
      for (const c of components.filter(c => c.category === 'resistor')) {
        for (const pin of c.pads) if (pin.net_id) expected.add(pin.net_id);
      }
      const shown = [...document.querySelectorAll('.board-view:not([hidden]) .copper-overlay .copper-feature')];
      const base = [...document.querySelectorAll('.board-view:not([hidden]) .copper-base .copper-feature')];
      return {expected: [...expected].sort(), actual: [...new Set(shown.map(e => e.dataset.netId))].sort(),
        expectedFeatures: base.filter(e => expected.has(e.dataset.netId)).length, actualFeatures: shown.length};
    });
    assert(bulk.expected.length > 1);
    assert.deepEqual(bulk.actual, bulk.expected);
    assert.equal(bulk.actualFeatures, bulk.expectedFeatures, 'Net union contains each feature exactly once');
    await page.locator('#zoom-to-net').check();
    const bulkViewport = await page.locator('.board-view[data-side="front"] > svg').getAttribute('viewBox');
    assert(bulkViewport.split(/\s+/).every(n => Number.isFinite(Number(n))));
    await page.locator('.side-button[data-side="back"]').click();
    assert.deepEqual(await page.evaluate(() => [...selectedReferences].sort()), categoryState.expected, 'Side switching preserves category selection');
    await page.locator('.side-button[data-side="front"]').click();
    await page.locator('#zoom-to-net').uncheck();
    // Search must not silently narrow the scope of a category checkbox.
    await page.locator('#search').fill('resistor');
    const visibleOne = await page.locator('.part-select:checked').first().getAttribute('data-reference');
    await page.locator(`.part-select[data-reference="${visibleOne}"]`).uncheck();
    assert(await categoryCheckbox.evaluate(e => e.indeterminate), 'Part selection produces mixed category state');
    assert.equal(await page.evaluate(() => selectedReferences.size), categoryState.expected.length - 1);
    await categoryCheckbox.check();
    await page.locator('#search').fill(visibleOne);
    await categoryCheckbox.uncheck();
    assert.equal(await page.evaluate(() => selectedReferences.size), 0, 'Filtered category clears all members on both sides');
    assert.equal(await page.locator('.copper-overlay .copper-feature').count(), 0, 'Empty selection highlights no unassigned pads');
    await page.locator('#search').fill('');
    await categoryCheckbox.check();
    await page.locator('.category-select[data-category="capacitor"]').check();
    assert(await page.evaluate(() => components.filter(c => ['resistor', 'capacitor'].includes(c.category)).every(c => selectedReferences.has(c.reference))));
    await page.locator('#highlight-selected-nets').uncheck();
    assert.equal(await page.locator('.copper-overlay .copper-feature').count(), 0);
    assert(await page.locator('.selection-box').count() > 1, 'Turning bulk nets off retains component selection');
    await page.locator('#highlight-selected-nets').check();
    await page.keyboard.press('Escape');
    assert(!(await page.locator('#highlight-selected-nets').isChecked()));
    assert.equal(await page.locator('.copper-overlay .copper-feature').count(), 0);
    await page.locator('#clear-selection').click();
    const distributorExamples = await page.evaluate(() => ({
      // A single-option part keeps the plain "Open LCSC" link; multi-option
      // parts render the popup button asserted further below.
      linked: components.find(c => (c.lcsc_options || []).length === 1),
      unlinked: components.find(c => !c.lcsc_url),
    }));
    assert(distributorExamples.linked, 'This board has a matched part with an LCSC number');
    await page.evaluate(reference => selectComponent(reference), distributorExamples.linked.reference);
    const lcscLink = page.locator('.actions .lcsc-link');
    assert.equal(await lcscLink.getAttribute('href'), distributorExamples.linked.lcsc_url);
    assert.equal(await lcscLink.getAttribute('target'), '_blank');
    assert((await lcscLink.getAttribute('rel')).includes('noopener'));
    assert.deepEqual(await page.locator('.actions a').allTextContents().then(labels => labels.slice(0, 2)), ['Open OOMP part', 'Open LCSC']);
    if (distributorExamples.unlinked) {
      await page.evaluate(reference => selectComponent(reference), distributorExamples.unlinked.reference);
      assert.equal(await page.locator('.actions .lcsc-link').count(), 0);
    }
    // Every part declares an LCSC search value; the third action searches
    // LCSC for it and the detail facts show the declared string.
    const searchExample = await page.evaluate(() => components.find(item => (item.lcsc_search || '') !== ''));
    assert(searchExample, 'Components declare an LCSC search value');
    await page.evaluate(reference => selectComponent(reference, true), searchExample.reference);
    const searchLink = page.locator('.actions a[href*="lcsc.com/search"]');
    assert.equal(await searchLink.textContent(), 'Search LCSC');
    assert.equal(await searchLink.getAttribute('href'), `https://www.lcsc.com/search?q=${encodeURIComponent(searchExample.lcsc_search)}`);
    assert((await searchLink.getAttribute('rel')).includes('noopener'));
    const factRows = await page.locator('.facts').textContent();
    assert(factRows.includes(searchExample.lcsc_search), 'The declared LCSC search value is shown in the facts');
    // A part with several LCSC options opens the options popup instead of
    // linking straight to one catalogue page.
    const popupState = await page.evaluate(() => {
      const component = components.find(item => (item.lcsc_options || []).length === 1);
      if (!component) return null;
      const saved = component.lcsc_options;
      component.lcsc_options = [
        ...saved,
        {part_number: 'C999999', product_name: 'Smoke test alternate', url: 'https://www.lcsc.com/product-detail/C999999.html'},
      ];
      selectComponent(component.reference);
      return {reference: component.reference, saved};
    });
    if (popupState) {
      const popupButton = page.locator('.actions button.lcsc-link');
      assert.equal(await popupButton.textContent(), `LCSC options (2)`);
      await popupButton.click();
      const rows = page.locator('#lcsc-popup .popup-row');
      assert.equal(await rows.count(), 2, 'The popup lists every LCSC option');
      assert.equal(await rows.nth(1).getAttribute('href'), 'https://www.lcsc.com/product-detail/C999999.html');
      assert((await rows.nth(0).textContent()).includes('C'));
      await page.locator('#lcsc-popup .popup-close').click();
      assert(await page.locator('#lcsc-popup').isHidden(), 'The close button dismisses the popup');
      // Escape closes it too, before touching the pin/net selection.
      await popupButton.click();
      await page.keyboard.press('Escape');
      assert(await page.locator('#lcsc-popup').isHidden(), 'Escape dismisses the popup');
      await page.evaluate(state => {
        const component = byReference.get(state.reference);
        component.lcsc_options = state.saved;
        // Preserve-flag re-renders the detail pane without toggling the
        // still-selected component off.
        selectComponent(component.reference, true);
      }, popupState);
    }
    await require('./board_explorer_multi_select.cjs')(page);
    await require('./board_explorer_selection_rendering.cjs')(page);
    await require('./board_explorer_status_layout.cjs')(page);
    await page.setViewportSize({width: 390, height: 844});
    const mobile = await page.evaluate(() => ({
      listHeight: document.getElementById('part-list').clientHeight,
      width: document.documentElement.clientWidth, scroll: document.documentElement.scrollWidth,
    }));
    assert(mobile.listHeight >= 100, 'Mobile pin list remains scrollable and usable');
    assert(mobile.scroll <= mobile.width + 1, 'Mobile page does not overflow horizontally');
    assert.deepEqual(errors, []);
    assert.deepEqual(requests, [], 'Page must operate fully offline');
    console.log(JSON.stringify({passed: true, candidate, counts, dimensions, pageErrors: errors, externalRequests: requests}, null, 2));
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
