# Infineon IRLR2905 and IRFR024N DPAK display research

The catalogue identifies Infineon IRLR2905TRPBF (55 V, 42 A) and
IRFR024NTRPBF (55 V, 17 A), each with the TO-252-3_TabPin2 PCB footprint.
Their existing International Rectifier PDFs have SHA-256 values, respectively,
`5d65a9f968482cc489376545501337dbb4af3ccb27798dc01ab818ea68e04d05` and
`798ada4821ec671c98f95a04106573d04c7da34efda67ad6ffe309aecbfd3d2e`.

Each PDF's page 8 drawing was visually reviewed. Both show TO-252AA DPAK with
two full outer leads, a short centre lead and a metal tab. The KiCad TO-252-2
model is a closer display approximation than the three-full-lead model attached
to the catalogue's PCB footprint, which is unchanged. Its 9.9 x 6.5 x 2.32 mm
overall bounds and short stub are approximate; the display model is not a
verified mechanical model or footprint.

The marking illustrations show a different part, IRFR120. `IRLR2905` and
`IRFR024N` are illustrative partial identifiers only. Exact markings, logos,
typeface, placement and variable production codes remain unverified.
