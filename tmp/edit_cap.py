content = open('working_oomp_populate_capacitor.py').read()

old = '''    sizes = ["0603"]
    capacitance_values = [
        "18_pico_farad",
        "22_pico_farad",
        "27_pico_farad",
        "10_nano_farad",
        "100_nano_farad",
        "1_micro_farad",
        "4_7_micro_farad",
        "10_micro_farad",
    ]'''

new = '''    sizes = ["0603"]
    capacitance_values = [
        "18_pico_farad",
        "22_pico_farad",
        "27_pico_farad",
        "33_pico_farad",
        "47_pico_farad",
        "10_nano_farad",
        "100_nano_farad",
        "1_micro_farad",
        "4_7_micro_farad",
        "10_micro_farad",
    ]'''

if old not in content:
    print("OLD NOT FOUND")
    print(repr(old))
    print("---")
    # Show what's actually there
    idx = content.find('sizes = ["0603"]')
    print(content[idx-10:idx+300])
else:
    content = content.replace(old, new)
    open('working_oomp_populate_capacitor.py', 'w').write(content)
    print("done")
