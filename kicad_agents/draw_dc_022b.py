"""Generate the DC-022B mechanical reference sheet from nominal dimensions."""
import argparse
from math import sqrt
from pathlib import Path

from working_oomp_populate_connector_dc_022b import SHAFT_ACROSS_FLATS_MM, SHAFT_DIAMETER_MM, SOURCE


def shaft_profile(x, y, pixels_per_mm):
    """Draw the M8 shaft envelope clipped by two parallel flats."""
    radius = SHAFT_DIAMETER_MM * pixels_per_mm / 2
    flat = SHAFT_ACROSS_FLATS_MM * pixels_per_mm / 2
    chord = sqrt(radius**2 - flat**2)
    r = f"{radius:g}"
    return (
        f"M{x-chord:.2f} {y-flat:.2f}H{x+chord:.2f}"
        f"A{r} {r} 0 0 1 {x+chord:.2f} {y+flat:.2f}H{x-chord:.2f}"
        f"A{r} {r} 0 0 1 {x-chord:.2f} {y-flat:.2f}Z"
    )


def make_svg():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="806" viewBox="0 0 1120 806">
<defs>
  <marker id="arrow" viewBox="0 0 8 8" markerWidth="7" markerHeight="7" refX="7" refY="4" orient="auto-start-reverse">
    <path d="M0 0L8 4L0 8Z" fill="#256e86"/>
  </marker>
</defs>
<rect width="1120" height="806" fill="#fff"/>
<g font-family="Arial, sans-serif" fill="#172738">
  <text x="43" y="53" font-size="32" font-weight="bold">DC-022B · Panel mount DC power socket</text>
  <text x="44" y="85" font-size="16">Switch Electronics 210011  /  Nominal dimensions in mm  /  30 V DC · 0.5 A</text>
  <path d="M44 106H1076" stroke="#c8d6de"/>
  <g font-size="19" font-weight="bold">
    <text x="65" y="147">Front</text>
    <text x="370" y="147">Side · nut removed</text>
    <text x="878" y="147">Shank profile</text>
    <text x="59" y="460">Fixing nut</text>
    <text x="370" y="460">Panel mounting</text>
    <text x="828" y="460">Contact assignment</text>
  </g>
</g>
<!-- Front and side use a common scale of 18 px/mm -->
<g stroke="#23394a" stroke-width="2" fill="none">
  <circle cx="167" cy="263" r="90" fill="#e9eef1"/>
  <circle cx="167" cy="263" r="80.1" fill="#fff"/>
  <circle cx="167" cy="263" r="50.4" fill="#e9eef1"/>
  <circle cx="167" cy="263" r="18.9" fill="#fff"/>
  <path d="M121 245h12v36h-12z" fill="#fff"/>
  <path d="M400 263h352M73 263h188M167 169v188" stroke="#8498a4" stroke-dasharray="7 5"/>
  <path d="M400 183h10v-10h62v18h99v10.8h45v122.4h-45V335h-99v18h-62v-10h-10Z" fill="#e9eef1"/>
  <path d="M410 173v180M472 191v144M562 191v144M616 201.8v122.4"/>
  <path d="M476 195l10 136m8-136l10 136m8-136l10 136m8-136l10 136m8-136l10 136" stroke="#8294a0"/>
  <path d="M616 208.1h81v14.4h-81m0 81h104.4v14.4H616" fill="#fff"/>
  <path d="M390 263h345M71 263h192M167 166v194" stroke="#8498a4" stroke-dasharray="7 5"/>
  <path d="M100 557l33-57h66l33 57-33 57h-66Z" fill="#e9eef1"/>
  <circle cx="166" cy="557" r="41.5" fill="white"/>
  <rect x="271" y="500" width="21" height="114" fill="#e9eef1"/>
  <path d="{shaft_profile(952, 257, 15)}" fill="#e9eef1"/>
  <path d="M885 257h134M952 191v132" stroke="#8498a4" stroke-dasharray="7 5"/>
  <circle cx="440" cy="555" r="48" fill="#fff"/>
  <path d="{shaft_profile(639, 555, 12)}" fill="#e9eef1"/>
  <path d="M384 555h112M440 499v112M582 555h114M639 499v112" stroke="#8498a4" stroke-dasharray="7 5"/>
  <path d="M828 529h42m0-7v14m0-7h43m-85 55h7l9-12 9 12h60"/>
  <circle cx="916" cy="529" r="3" fill="#fff"/>
  <circle cx="916" cy="584" r="3" fill="#fff"/>
</g>
<g fill="none" stroke="#256e86" stroke-width="1.3">
  <path d="M400 348v52m72-43v18m144-44v44m104.4-52v77M410 173h-35m35 180h-35"/>
  <path d="M400 391h320.4M400 369h72M472 369h144M379 173v180" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
  <path d="M114 366l18-66M266 216l-72 45" marker-end="url(#arrow)"/>
  <path d="M100 500H72m28 114H72m9-114v114M271 614v26m21-26v26m-21-7h21" marker-end="url(#arrow)"/>
  <path d="M984 206h55M984 308h55M392 556v75M488 556v75M591 556v75M687 556v75M665 514.2h59M665 595.8h59"/>
  <path d="M1034 206v102M392 624h96M591 624h96M718 514.2v81.6" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
</g>
<g font-family="Arial, sans-serif" font-size="16" fill="#23485b">
  <text x="93" y="385">Ø5.6 opening</text>
  <text x="264" y="212">Centre pin</text>
  <text transform="translate(367 296) rotate(-90)">Ø10.0 flange</text>
  <text x="424" y="365">4.0</text>
  <text x="531" y="365">8.0</text>
  <text x="493" y="417">17.8 nominal overall</text>
  <text x="741" y="218">4 · 4.5 ±0.3</text>
  <text x="741" y="316">5 · 5.8 ±0.3</text>
  <text x="507" y="182">M8 × 1</text>
  <text x="136" y="561">M8 × 1</text>
  <text x="50" y="563">11</text>
  <text x="270" y="655">2.0</text>
  <text x="1044" y="262">{SHAFT_ACROSS_FLATS_MM:g}</text>
  <text x="881" y="351">M8 × 1 · two flats</text>
  <text x="440" y="493" text-anchor="middle">Round</text>
  <text x="639" y="493" text-anchor="middle">Double-D · anti-rotation</text>
  <text x="440" y="648" text-anchor="middle">Ø{SHAFT_DIAMETER_MM:g}</text>
  <text x="639" y="648" text-anchor="middle">Ø{SHAFT_DIAMETER_MM:g} arcs</text>
  <text x="729" y="560">{SHAFT_ACROSS_FLATS_MM:g}</text>
  <text x="370" y="680">4 mm max panel thickness</text>
  <text x="933" y="535">4 · Centre</text>
  <text x="933" y="590">5 · Sleeve</text>
</g>
<path d="M44 704H1076" stroke="#c8d6de"/>
<g font-family="Arial, sans-serif" font-size="15" fill="#425865">
  <text x="44" y="730">The double-D cut-out follows the nominal shaft profile. Check the actual socket and allow clearance before cutting.</text>
  <text x="44" y="754">Source: Switch Electronics drawing 210011, page 1. Round opening and maximum panel thickness are from the listing.</text>
  <text x="44" y="778">Listing envelope 18.2 × Ø10.2. Drawing envelope 17.8 × Ø10.0, excluding nut. Refer to the datasheet for tolerances.</text>
</g>
</svg>
"""


def main():
    import cairosvg

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SOURCE)
    output = parser.parse_args().output
    output.mkdir(parents=True, exist_ok=True)
    svg = make_svg()
    (output / "mechanical_drawing.svg").write_text(svg, encoding="utf-8")
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(output / "mechanical_drawing.png"))


if __name__ == "__main__":
    main()
