# TAJ tantalum display research (2026-11-18)

Manufacturer reference: https://datasheets.kyocera-avx.com/TAJ.pdf, pages 1–2.
The TAJ drawing shows a positive-anode polarity band and, on A/B/C/D cases,
capacitance code and voltage letter. The catalogue table defines voltage
letters and explicitly allows higher voltage parts in the same case size.
A render of a nominal value must therefore disclose illustrative exact marking;
never fabricate a production/lot code or claim the actual marking is known.
The manufacturer lists nominal A/B/C/D envelopes respectively as
3.20 × 1.60 × 1.60, 3.50 × 2.80 × 1.90, 6.00 × 3.20 × 2.60 and
7.30 × 4.30 × 2.90 mm. Confirm exact part case and electrical values.

Local KiCad model `Capacitor_Tantalum_SMD.3dshapes/CP_EIA-3216-18_Kemet-A.step`
SHA-256 `eb8dd8439d7308bedc45f035fb97ba75c9c8db4ae2913256dfb99050e00be2f0`
has one valid root and measured bounds 3.20 × 1.60 × 1.80 mm. Its three
STEP face colors are `0.824,0.820,0.781` (metal, 25 faces),
`0.832,0.680,0.066` (yellow body, 16) and `0.809,0.426,0.148` (stripe, 5).
Stripe faces lie on top around x = -0.931 to -0.331 mm. It is a Kemet
package representation, not an exact AVX model; scaling to 1.60 mm nominal
height requires z factor 8/9 and disclosure of approximate edges/stripe.
Check polarity orientation and readable top markings in an actual preview.

`package_markings.marking_text` now implements the explicitly illustrative
`avx_taj_illustrative` code for A/B/C/D cases using the documented voltage
table; it requires evidence and an appearance limitation. Before using it,
validate the selected exact source record and MPN against capacitance and
voltage; don't infer them from the filename. The rendering pipeline still
needs a reviewed yellow-body/contrasting ink material, stripe colouring and
layout that avoids the stripe. Build one preview, inspect, then publish the
exact part with provenance. No AVX render is claimed complete. No PDF was
downloaded.

## A-case pilot and batch workflow

The TAJA106K010RNJ pilot is now published after preview and final image
inspection. `display_render.py` supplies the yellow tantalum material and
stripe and supports a bounded horizontal text offset. The selected KiCad
model uses positive-anode stripe and a z scale of 8/9. Source capacitor
polarity notes and populate definitions were corrected to positive; don't
apply this TAJ convention to aluminium electrolytic parts.

For matching, individually researched A-case parts,
`display_render_taj_a_batch01_queue.py` validates exact MPN, source value,
voltage, package, footprint and distributor. It uses supplier evidence and
flags literal marking and finishes as illustrations.
`display_render_taj_composite.py` builds separate path-traced body and ink
passes from the pilot, then projects each part's checked marking. The
composite approximates indirect ink reflections and is disclosed in each
recipe. The compositor's exact source is archived by hash. Wait for the
master process to finish, then inspect a rendered composite against the
pilot before rendering or publishing the remaining reviewed batch. Verify
manifest hashes and provenance before `publish_display_render`. Do not infer
a manufacturer logo, production code or exact substitute marking.

The A-case shared passes and compositor were reviewed against the independently
path-traced pilot, and both five-part batches were published after a ten-image
contact-sheet review. The composite image approximates indirect ink reflections.
Master and compositor hashes are checked by `apply_extras`; retain the master
assets and archived compositor source. For future candidates, check exact MPN,
value, voltage, case and polarity before choosing a marking code; build new
case-size masters rather than stretching the A-case representation.

## B-case pilot and queued parts

The installed KiCad `CP_EIA-3528-21_Kemet-B.step` has SHA-256
`dfe18bc321e2772dd597027a289d8e13b7b6f0320cfdd8f41c4492bdfe9f7f0c`,
measured 3.5 × 2.8 × 2.1 mm, and the same three metal, body and stripe
source colours as A-case. The reviewed TAJ B nominal height is 1.9 mm, so
the B pilot recipe uses z scale 19/21. Its preview passed visual review.
The 1400 px pilot and three five-part B-case batches are published after
visual and provenance checks. `display_render_taj_b_composite.py` is a
separately archived B-case builder. Other case sizes need their own geometry
and stripe checks, not a stretched B or A model.

## Later C- and D-case model checks

The installed KiCad `CP_EIA-6032-28_Kemet-C.step` has one valid root,
measured bounds 6.0 × 3.2 × 2.8 mm, SHA-256
`328acba14273b2549d644fc7a2a742c63370374d878e4f20086d728ef5a87171`,
and three reviewed-by-colour metal/body/stripe groups (25/16/5 faces).
`CP_EIA-7343-31_Kemet-D.step` similarly has one valid root, bounds
7.3 × 4.3 × 3.1 mm, SHA-256
`1d578cc03d3128d635ae0205945d796d728d36c1e32e83d288ba1795bc01429b`,
and 25/16/5 faces in the same source colours. The manufacturer TAJ table
gives nominal heights 2.6 mm and 2.9 mm respectively. Each case needs its
own carefully checked stripe orientation, marking layout and visual pilot;
these model checks do not constitute rendered parts.

The measured C-case top stripe spans x = -2.154 to -1.554 mm, and the
D-case top stripe spans x = -2.780 to -1.580 mm in their KiCad STEP files.
Use these bounds to keep projected text off the stripe, then visually verify
readability and polarity for each new case pilot.

## B-case batch completion (2026-11-18)

The earlier B-case in-progress notes are superseded: the shared master, pilot
comparison, 15 reviewed composites and individual pages are complete and
validated. See `DISPLAY_RENDER_CATALOGUE_PROGRESS.md` for checks and caveats.
C- and D-case recipes are prepared. The C-case preview passed visual review;
its full render and page are published. Shared C-case master generation is
in progress (session 19454). The D-case still needs a preview and final render.

## C-case next candidate research (2026-11-18)

These exact supplier listings support identity, ratings and C case for the seven
remaining source records; source identity and dimensions still need checking
against each record before preparing recipes. All markings and finish remain
illustrative, and manufacturer-approved voltage substitution may alter them.

- TAJC106K025RNJ, 10 µF 25 V: https://www.digikey.in/en/products/detail/avx-corporation/TAJC106K025RNJ/564732
- TAJC106K035RNJ, 10 µF 35 V: https://win-source.net/products/detail/avx-corporation/tajc106k035rnj.html
- TAJC227K006RNJ, 220 µF 6.3 V: https://www.lcsc.com/product-detail/C7216.html
- TAJC226K025RNJ, 22 µF 25 V: https://www.lioncircuits.com/parts/TAJC226K025RNJ
- TAJC336K016RNJ, 33 µF 16 V: https://www.lcsc.com/product-detail/C7217.html
- TAJC476K016RNJ, 47 µF 16 V: https://www.amarradio.com/en/product/tajc476k016rnj
- TAJC686K016RNJ, 68 µF 16 V: https://www.abacuselect.com/products/catalog/kyocera-avx-TAJC686K016RNJ-fixed-capacitors/

Review tolerance, case and polarity from each listing/source; where the listing
is incomplete, corroborate it before publishing. No local PDF was downloaded.

The seven candidates are checked against source fields by
`display_render_taj_c_batch01_queue.py`, with evidence recorded in
`DISPLAY_RENDER_TAJ_C_BATCH01_EVIDENCE.md`. Seven queue tests passed, including
6.3 V marking and changed case/voltage/polarity rejection. The queue has been added to recipes but is not rendered or published. C compositor source is prepared and archived,
but needs shared-pass generation and a visual comparison to the independent
pilot before use.

## D-case next candidates (2026-11-18)

Eight exact supplier listings are recorded in
`DISPLAY_RENDER_TAJ_D_BATCH01_EVIDENCE.md`, and the corresponding source
records are checked by `display_render_taj_d_batch01_queue.py`. Eight tests
passed, including fractional-voltage markings and case, polarity and rating
guards. The queue is not added or published. The D compositor is prepared and
archived, but the D pilot requires preview and final visual review, then a new
shared master and a visual comparison before any batch is published.
