"""Human-editable official KiCad master selections. No package geometry guesses.

Exact part overrides can set kicad.symbol, kicad.machine_solder and
kicad.hand_solder in any family's populate-extra file. Empty entries are
reported, not replaced with invented symbols or expanded pads.
"""


def add_kicad_details(part):
    if part.get('taxonomy_1') not in ['electronic', 'mechanical']:
        return
    selections = {'symbol': '', 'machine_solder': '', 'hand_solder': ''}
    kind = part.get('taxonomy_2', '')
    size = part.get('taxonomy_3', '')
    sizes = [
        ['0201', '0603'], ['0402', '1005'], ['0603', '1608'],
        ['0805', '2012'], ['1206', '3216'], ['1210', '3225'], ['2512', '6332'],
    ]
    families = [
        ['resistor', 'Device:R_Small', 'Resistor_SMD', 'R'],
        ['capacitor', 'Device:C_Small', 'Capacitor_SMD', 'C'],
        ['ferrite_bead', 'Device:FerriteBead_Small', 'Inductor_SMD', 'L'],
        ['led', 'Device:LED', 'LED_SMD', 'LED'],
    ]
    for family, symbol, library, prefix in families:
        if kind == family:
            for imperial, metric in sizes:
                if size == imperial:
                    selections['symbol'] = symbol
                    selections['machine_solder'] = f'{library}:{prefix}_{imperial}_{metric}Metric'
    if kind == 'resistor' and size == 'quarter_watt_through_hole':
        selections['symbol'] = 'Device:R_Small'
        selections['machine_solder'] = 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal'
        selections['hand_solder'] = selections['machine_solder']
    if kind == 'led' and part.get('taxonomy_4') != 'rgb':
        for diameter in [3, 5, 10]:
            if size == f'{diameter}_mm':
                selections['symbol'] = 'Device:LED'
                selections['machine_solder'] = f'LED_THT:LED_D{diameter}.0mm'
                selections['hand_solder'] = selections['machine_solder']
    if kind == 'connector' and size == 'header' and part.get('taxonomy_4') == '2_54_mm_pitch':
        count_text = str(part.get('taxonomy_6', '')).replace('_pin', '')
        if count_text.isdigit():
            count = int(count_text)
            socket = part.get('taxonomy_7') == 'socket'
            package = 'PinSocket' if socket else 'PinHeader'
            selections['symbol'] = f'Connector_Generic:Conn_01x{count:02d}'
            selections['machine_solder'] = f'Connector_{package}_2.54mm:{package}_1x{count:02d}_P2.54mm_Vertical'
            selections['hand_solder'] = selections['machine_solder']
    if kind == 'mounting_hole' and part.get('hole_style') == 'round':
        # Only sizes with an exact official nominal diameter are selected.
        sizes = [[2, '2mm'], [2.5, '2.5mm'], [3, '3mm'], [3.2, '3.2mm_M3'], [4, '4mm'], [5, '5mm'], [6, '6mm']]
        for diameter, entry in sizes:
            if part.get('hole_diameter_mm') == diameter and part.get('hole_plating') == 'unplated':
                selections['symbol'] = 'Mechanical:MountingHole'
                selections['machine_solder'] = f'MountingHole:MountingHole_{entry}'
                selections['hand_solder'] = selections['machine_solder']
    # Existing explicit family/populate-extra choices take precedence.
    selections.update(part.get('kicad', {}))
    part['kicad'] = selections
