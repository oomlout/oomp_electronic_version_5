import sys
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import json
from kicad_agents.oomp_matching_agent import match_component, OompPartIndex

# Test SW_Push from Easyduino Nano
component = {
    "reference": "SW1",
    "schematic": {
        "units": [{
            "library_id": "Switch:SW_Push",
            "properties": {
                "Value": "SW_Push",
                "Footprint": "Button_Switch_SMD:SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS"
            }
        }]
    },
    "pcb": {
        "value": "SW_Push",
        "library_id": "Button_Switch_SMD:SW_Tactile_SPST_NO_Straight_CK_PTS636Sx25SMTRLFS"
    }
}

index = OompPartIndex("parts")
result = match_component(index, component)
print(json.dumps(result, indent=2))
