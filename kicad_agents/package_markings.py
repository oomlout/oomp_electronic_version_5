"""Explicit package-marking policies; never infer a supplier scheme from value alone."""
from decimal import Decimal
import re

E96 = (100,102,105,107,110,113,115,118,121,124,127,130,133,137,140,143,
       147,150,154,158,162,165,169,174,178,182,187,191,196,200,205,210,
       215,221,226,232,237,243,249,255,261,267,274,280,287,294,301,309,
       316,324,332,340,348,357,365,374,383,392,402,412,422,432,442,453,
       464,475,487,499,511,523,536,549,562,576,590,604,619,634,649,665,
       681,698,715,732,750,768,787,806,825,845,866,887,909,931,953,976)
MULTIPLIERS = {-3:'Z', -2:'Y', -1:'X', 0:'A', 1:'B', 2:'C', 3:'D',
               4:'E', 5:'F', 6:'G', 7:'H'}


def marking_text(marking):
    policy = marking['policy']
    if policy == 'avx_taj_illustrative':
        # TAJ A/B/C/D cases use a three-digit capacitance code and a
        # voltage letter. A lot code and logo are intentionally not invented.
        codes = {'2.5': 'e', '4': 'G', '6.3': 'J', '10': 'A', '16': 'C',
                 '20': 'D', '25': 'E', '35': 'V', '50': 'T'}
        if not marking.get('evidence') or not marking.get('appearance_status'):
            raise ValueError('TAJ illustrative marking needs evidence and an explicit limitation.')
        if marking.get('case') not in ('A', 'B', 'C', 'D'):
            raise ValueError('Unreviewed TAJ case')
        capacitance = marking.get('capacitance_code')
        if not isinstance(capacitance, str) or not re.fullmatch(r'[1-9][0-9][0-9]', capacitance):
            raise ValueError('Expected a three-digit TAJ capacitance code')
        voltage = str(marking.get('rated_voltage_v'))
        if voltage not in codes:
            raise ValueError('Unreviewed TAJ voltage code')
        return f'{capacitance} {codes[voltage]}'
    if policy == 'none':
        return ''
    if policy == 'unmarked_illustration':
        if not marking.get('evidence') or not marking.get('appearance_status'):
            raise ValueError('An illustrative unmarked appearance requires evidence and an explicit limitation.')
        return ''
    if policy == 'verified_literal':
        if not marking.get('evidence'):
            raise ValueError('Literal package text requires evidence, including line order.')
        return marking['text']
    if policy == 'illustrative_literal':
        if not marking.get('evidence') or not marking.get('appearance_status') or not marking.get('text'):
            raise ValueError('Illustrative text requires evidence and an explicit appearance limitation.')
        return marking['text']
    if policy == 'uniroyal_0603_e96':
        if not marking.get('evidence'):
            raise ValueError('Select a verified manufacturer marking policy first.')
        value = Decimal(str(marking['resistance_ohm']))
        for exponent, suffix in MULTIPLIERS.items():
            for index, significant in enumerate(E96, 1):
                if Decimal(significant) * Decimal(10) ** exponent == value:
                    return f'{index:02d}{suffix}'
        raise ValueError('Value is not exactly representable by this E96 policy; do not round it.')
    raise ValueError(f'Unsupported marking policy: {policy}')
