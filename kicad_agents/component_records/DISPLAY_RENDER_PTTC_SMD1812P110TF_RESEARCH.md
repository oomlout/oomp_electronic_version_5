# PTTC SMD1812P110TF display research

The exact source record identifies PTTC (Polytronics Tech) SMD1812P110TF.
Its existing manufacturer-family PDF, SHA-256
`a069663b6cacca56713e2c319c9de96d8a5fc1f15f39e7a480fbd2f6d8f875d0`,
was visually reviewed. Page 10 shows a concave-end 1812 package, the logo and
part identification, and gives the exact part's ranges as 4.37–4.73 mm long,
3.07–3.41 mm wide and 0.30–0.71 mm thick. Page 12 gives marking `110` and
matte tin-plated copper terminals. The source's 2.4 mm height conflicts with
the 0.71 mm maximum; leave the original record unchanged and disclose it.

The existing procedural miniSMDC model has the same broad concave-end form,
but its 0.76 mm height exceeds this part's maximum. A separately rendered
display may scale its height to 0.50 mm, within the drawing range; it is not
manufacturer CAD or a footprint. Exact notch details and dark body/ink shades
are illustrative, the manufacturer logo is omitted, and placement/typeface of
the verified `110` code is approximate.
