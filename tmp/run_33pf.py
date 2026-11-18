import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import working_oomp

working_oomp.main(filter="electronic_capacitor_0603_33_pico_farad", regenerate_pngs=False)
print("Done")
