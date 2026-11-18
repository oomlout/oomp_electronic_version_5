content = open('working_oomp_populate_diode.py').read()

old = '''        {
            "diode_type": "schottky",
            "package": "sod_123",
            "manufacturer": "generic",
            "part_number": "ss14",
            "name_short": "Schottky Diode SOD-123",
        },
        {
            "diode_type": "schottky",
            "package": "sod_323",
            "manufacturer": "generic",
            "part_number": "bat54w",
            "name_short": "Schottky Diode SOD-323",
        },
        {
            "diode_type": "schottky",
            "package": "0402",
            "manufacturer": "generic",
            "part_number": "1ss400",
            "name_short": "Schottky Diode 0402",
        },'''

new = '''        {
            "diode_type": "schottky",
            "package": "sod_123",
            "part_number": "ss14",
            "name_short": "Schottky Diode SOD-123",
        },
        {
            "diode_type": "schottky",
            "package": "sod_323",
            "part_number": "bat54w",
            "name_short": "Schottky Diode SOD-323",
        },
        {
            "diode_type": "schottky",
            "package": "sod_523",
            "part_number": "1ss400",
            "name_short": "Schottky Diode SOD-523",
        },'''

assert old in content, "old not found"
content = content.replace(old, new)
open('working_oomp_populate_diode.py', 'w').write(content)
print("done")
