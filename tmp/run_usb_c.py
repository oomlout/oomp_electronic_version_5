import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import working_oomp

working_oomp.main(filter="electronic_connector_usb_c_surface_mount_16_pin_shou_han_type_c_16pin_2md_073", regenerate_pngs=False)
print("Done")
