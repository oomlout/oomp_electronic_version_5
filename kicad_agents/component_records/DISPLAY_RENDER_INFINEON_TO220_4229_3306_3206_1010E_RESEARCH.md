# Infineon TO-220 MOSFET display research, batch 05

The following catalogue records identify Infineon Technologies and the
TO-220-3 vertical footprint. Each existing International Rectifier PDF's page 1
text was checked for device identity and page 8 was visually reviewed.

| Orderable | Local PDF SHA-256 | Marking evidence |
| --- | --- | --- |
| IRFB4229PBF | `897e32ff2ec11adf865d4ac7296f5c78d105aa4cded9004e1864feaf656bbd9e` | example shows another device |
| IRFB3306PBF | `3a42104e8b332cf0efd4c6b9b6d73746ac790dab82b6e4b623e6ca6b7f794a0a` | drawing illustrates IRFB3306 |
| IRFB3206PBF | `01d48711bec8bc03eab9638341c609cf73fb014f6831f67601f54e88740cb484` | drawing illustrates IRFB3206 |
| IRF1010EPBF | `7f0abaa51fc109f421ba747bc91b764da4693995b102df5494b02b9b05e02ab6` | older IRF1010E PDF does not establish PbF suffix; example shows IRF1010 |

For IRFB3306 and IRFB3206 the stated identifiers follow their manufacturer
family marking examples; typeface, logo, placement and lot/date codes remain
approximate. The other identifiers are illustrative, with exact top markings
unverified. The KiCad TO-220-3 model has 10.25 x 4.455 x 28.525 mm overall
bounds and approximately 13.435 mm body-to-tip lead projection. The IRF1010E
drawing specifies 13.47–14.09 mm, so that display model is approximately
0.035 mm shorter than its minimum. Shape and finish are approximate; this is
not verified manufacturing CAD or a footprint.

The separate IRF3205ZPBF record was initially held because its local PDF's
75 A headline and automotive title appeared inconsistent. Page 1 was then
visually inspected: it also shows IRF3205Z in TO-220AB, specifying 110 A
silicon-limited and 75 A package-limited. Infineon's current
[IRF3205Z product listing](https://www.infineon.com/part/IRF3205Z) separately
identifies IRF3205ZPBF as TO-220 and 110 A. These are different limits, not
evidence of a different device. Its exact top marking still needs review.
