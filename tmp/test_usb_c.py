import sys
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import json
from kicad_agents.oomp_matching_agent import match_component, OompPartIndex

# Test USB-C from Easyduino Nano
component = {
    "reference": "J1",
    "schematic": {
        "units": [{
            "library_id": "Connector:USB_C_Receptacle_USB2.0",
            "properties": {
                "Value": "USB_C_Receptacle_USB2.0",
                "Footprint": "Connector_USB:USB_C_Receptacle_G-Switch_GT-USB-7010ASV"
            }
        }]
    },
    "pcb": {
        "value": "USB_C_Receptacle_USB2.0",
        "library_id": "Connector_USB:USB_C_Receptacle_G-Switch_GT-USB-7010ASV"
    }
}

index = OompPartIndex("parts")
result = match_component(index, component)
print(json.dumps(result, indent=2))
