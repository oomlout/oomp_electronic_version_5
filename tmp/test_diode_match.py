import sys
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import json
from kicad_agents.oomp_matching_agent import match_component, OompPartIndex

# Test Easyduino Uno D_Schottky SOD-123
component = {
    "reference": "D2",
    "schematic": {
        "units": [{
            "library_id": "Device:D_Schottky",
            "properties": {
                "Value": "D_Schottky",
                "Footprint": "Diode_SMD:D_SOD-123"
            }
        }]
    },
    "pcb": {
        "value": "D_Schottky",
        "library_id": "Diode_SMD:D_SOD-123"
    }
}

index = OompPartIndex("parts")
result = match_component(index, component)
print("SOD-123:", json.dumps(result, indent=2))

# Test SparkFun BAT60A SOD-323
component2 = {
    "reference": "D2",
    "schematic": {
        "units": [{
            "library_id": "SparkFun-DiscreteSemi:D_Schottky_3A_10V_0.28V",
            "properties": {
                "Value": "BAT60A",
                "Footprint": "SparkFun-Semiconductor-Standard:SOD-323"
            }
        }]
    },
    "pcb": {
        "value": "BAT60A",
        "library_id": "SparkFun-Semiconductor-Standard:SOD-323"
    }
}
result2 = match_component(index, component2)
print("SOD-323 BAT60A:", json.dumps(result2, indent=2))

# Test Easyduino Nano D_Schottky 0402
component3 = {
    "reference": "D2",
    "schematic": {
        "units": [{
            "library_id": "Device:D_Schottky",
            "properties": {
                "Value": "D_Schottky",
                "Footprint": "Diode_SMD:D_0402_1005Metric"
            }
        }]
    },
    "pcb": {
        "value": "D_Schottky",
        "library_id": "Diode_SMD:D_0402_1005Metric"
    }
}
result3 = match_component(index, component3)
print("0402:", json.dumps(result3, indent=2))
