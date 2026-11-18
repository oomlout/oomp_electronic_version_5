# RALEC RTT chip resistor display evidence

Reviewed online: RALEC RTT thick-film chip resistor specification IE-SP-010,
released 20 February 2011, page 13, section 9.1:
https://www.bdtic.com/datasheet/RALEC/IE-SP-010.pdf
The later 21 June 2024 general specification IE-SP-010 pages 1–3 records
part-number structure, ratings and dimensions:
https://static6.arrow.com/aropdfconversion/ed478173dacd3fc962fa4cb357910dad909d1015/ie-sp-010.pdf

RTT05 and RTT06 1% values at least 100 ohms use four characters: three
significant digits and a decimal exponent. Below 100 ohms, R denotes the
decimal point. The 5% variants at least 10 ohms use three characters: two
significant digits and a decimal exponent; below 10 ohms R is a decimal
point. Verify the exact primary MPN, value, tolerance, footprint and family.

The manufacturer gives 0805 dimensions 2.00 ± 0.10 by 1.25 ± 0.10 mm;
the reviewed generic KiCad model is 2.00 by 1.20 mm. The 1206 manufacturer
body is 3.05 ± 0.10 by 1.55 ± 0.10 mm, whereas the reviewed generic KiCad
model is 3.20 by 1.60 mm: its length exceeds the stated maximum by 0.05 mm.
Both are illustrative display geometry, not dimensional manufacturer models.
Typeface, ink, placement and finish are illustrative. The specifications were
reviewed online only; no local manufacturer PDF has been captured.
