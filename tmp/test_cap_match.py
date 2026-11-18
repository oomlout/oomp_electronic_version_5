import sys
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

import json
from kicad_agents.oomp_matching_agent import match_component, OompPartIndex

# Test component matching for SparkFun 47pF 0603
component = {
    "reference": "C2",
    "schematic": {
        "units": [{
            "library_id": "SparkFun-Capacitor:47pF_0603_50V_5%",
            "properties": {
                "Value": "47pF",
                "Footprint": "SparkFun-Capacitor:C_0603_1608Metric"
            }
        }]
    },
    "pcb": {
        "value": "47pF",
        "library_id": "SparkFun-Capacitor:C_0603_1608Metric"
    }
}

index = OompPartIndex("parts")
result = match_component(index, component)
print(json.dumps(result, indent=2))

# Test 33pF
component2 = {
    "reference": "C17",
    "schematic": {
        "units": [{
            "library_id": "SparkFun-Capacitor:33pF_0603_50V_5%",
            "properties": {
                "Value": "33pF",
                "Footprint": "SparkFun-Capacitor:C_0603_1608Metric"
            }
        }]
    },
    "pcb": {
        "value": "33pF",
        "library_id": "SparkFun-Capacitor:C_0603_1608Metric"
    }
}
result2 = match_component(index, component2)
print(json.dumps(result2, indent=2))
