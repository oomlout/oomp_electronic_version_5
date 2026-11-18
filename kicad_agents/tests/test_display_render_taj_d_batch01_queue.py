import copy
import json

import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_taj_d_batch01_queue import PARTS, reviewed_recipe
from kicad_agents.package_markings import marking_text


@pytest.mark.parametrize("part", list(PARTS))
def test_d_case_exact_ratings_and_fractional_voltage(part):
    recipes = json.loads(RECIPE_FILE.read_text(encoding="utf8"))
    record = yaml.safe_load((ROOT / "parts_source" / part / "working.yaml").read_text(encoding="utf8"))
    recipe = reviewed_recipe(part, record, recipes, "evidence-hash")
    mpn, _, _, volts, code = PARTS[part]
    assert recipe["represented_mpn"] == mpn
    assert marking_text(recipe["marking"]) == f"{code} { {"6.3": "J", "16": "C", "25": "E", "35": "V", "10": "A", "20": "D"}[volts] }"
    for field, value in [("case_size", "CASE-C-6032-28"), ("rated_voltage", "999 V"), ("polarized", False)]:
        changed = copy.deepcopy(record)
        changed["electrical"][field] = value
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, "evidence-hash")
