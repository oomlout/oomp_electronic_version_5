# Seaward SE5218 SOT-23-5 display research

Reviewed 2026-11-20. Two catalogue records name SE5218 and SE5218ALG. Both
omit manufacturer and exact orderable fields and use the same SOT-23-5
footprint and nominal 2.9 x 1.6 x 1.1 mm dimensions. Their relationship has
not been resolved here; preserve both records and do not assert they are
distinct exact devices or silently merge them.

The [Seaward-authored preliminary datasheet](https://static.chipdip.ru/lib/161/DOC013161937.pdf)
lists several output voltages. It identifies `SE5218ALG-LF` as 3.3 V and
shows the 3.3 V marking beginning `218A`, followed by production codes and a
lead-free dot. The exact `-LF` suffix is absent from the catalogue's ALG ID,
and the generic SE5218 record does not identify its output variant. Thus the
ALG record can only be represented as an inferred 3.3 V family variant, not a
verified full orderable; the generic entry must not claim a specific voltage
or variant marking. `SE5218` is an illustrative family label for the generic
record. Font, orientation, physical indicator placement and variable codes are
illustrative. A KiCad pin-one dot must not be conflated with the manufacturer's
separate lead-free dot. No datasheet has been downloaded locally.

The Seaward outline lists 2.80–3.05 mm body length, 1.50–1.75 mm body width,
2.60–3.00 mm lead span and 0.90–1.30 mm height. The previously reviewed
KiCad `SOT-23-5.step` SHA-256
`720a6eab0024069bbee68e7cb4c3ff1149468a34611225cdc852662c5d0ec2b7`
has 2.8 x 2.9 x 1.55 mm overall bounds. Scaling its height to 1.1 mm makes
the display fit the manufacturer range and catalogue height; the scaling is
an approximation, not an engineering or footprint verification.
