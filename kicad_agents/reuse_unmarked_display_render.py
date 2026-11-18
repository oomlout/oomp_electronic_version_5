"""Reuse an inspected render only for visually identical unmarked chip resistors.

This does not publish pages. Each target retains its own evidence and recipe;
the manifest explicitly records the source image rather than claiming a render.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil

import yaml

from working_oomp_populate_display_render import ROOT, reused_image_valid
from kicad_agents.display_render_resistor_queue import PILOT
from kicad_agents.display_render_small_resistor_queue import reviewed_recipe as uniroyal_recipe
from kicad_agents.display_render_fojan_queue import reviewed_recipe as fojan_recipe
from kicad_agents.display_render_fojan_low_queue import reviewed_decimal_recipe as fojan_low_recipe, EVIDENCE as FOJAN_LOW_EVIDENCE
from kicad_agents.display_render_fojan_5pct_queue import reviewed_recipe as fojan_5pct_recipe, EVIDENCE as FOJAN_5PCT_EVIDENCE
from kicad_agents.display_render_multi_0201_queue import reviewed_recipe as multi_0201_recipe, EVIDENCE as MULTI_0201_EVIDENCE
from kicad_agents.display_render_yageo_small_queue import reviewed_recipe as yageo_recipe
from kicad_agents.display_render_yageo_ac0402_queue import reviewed_recipe as yageo_ac_recipe, EVIDENCE as YAGEO_AC_EVIDENCE
from kicad_agents.display_render_yageo_visual_0201_queue import reviewed_recipe as yageo_visual_recipe, EVIDENCE as YAGEO_VISUAL_EVIDENCE
from kicad_agents.display_render_yageo_selected_0201_queue import reviewed_recipe as yageo_selected_recipe, EVIDENCE as YAGEO_SELECTED_EVIDENCE
from kicad_agents.display_render_yageo_selected_0402_queue import reviewed_recipe as yageo_selected_0402_recipe, EVIDENCE as YAGEO_SELECTED_0402_EVIDENCE
from kicad_agents.display_render_yageo_small_selected_queue import reviewed_recipe as yageo_small_selected_recipe, EVIDENCE as YAGEO_SMALL_SELECTED_EVIDENCE
from kicad_agents.display_render_yageo_generic_0201_queue import reviewed_recipe as yageo_generic_recipe, EVIDENCE as YAGEO_GENERIC_EVIDENCE
from kicad_agents.display_render_yageo_generic_0402_queue import reviewed_recipe as yageo_generic_0402_recipe, EVIDENCE as YAGEO_GENERIC_0402_EVIDENCE
from kicad_agents.display_render_fenghua_small_queue import reviewed_recipe as fenghua_recipe
from kicad_agents.display_render_fenghua_0402_5pct_queue import reviewed_recipe as fenghua_5pct_recipe, EVIDENCE as FENGHUA_5PCT_EVIDENCE
from kicad_agents.display_render_ralec_small_queue import reviewed_recipe as ralec_small_recipe, EVIDENCE as RALEC_SMALL_EVIDENCE
from kicad_agents.display_render_samsung_0603_batch01_queue import reviewed_recipe as samsung_cap_recipe, EVIDENCE as SAMSUNG_CAP_EVIDENCE
from kicad_agents.display_render_samsung_0603_batch02_queue import reviewed_recipe as samsung_cap_02_recipe, EVIDENCE as SAMSUNG_CAP_02_EVIDENCE
from kicad_agents.display_render_samsung_0603_batch03_queue import reviewed_recipe as samsung_cap_03_recipe, EVIDENCE as SAMSUNG_CAP_03_EVIDENCE
from kicad_agents.display_render_samsung_0603_batch04_queue import reviewed_recipe as samsung_cap_04_recipe, EVIDENCE as SAMSUNG_CAP_04_EVIDENCE
from kicad_agents.display_render_fenghua_0603_batch01_queue import reviewed_recipe as fenghua_cap_recipe, EVIDENCE as FENGHUA_CAP_EVIDENCE
from kicad_agents.display_render_fenghua_0603_batch02_queue import reviewed_recipe as fenghua_cap_02_recipe, EVIDENCE as FENGHUA_CAP_02_EVIDENCE
from kicad_agents.display_render_samsung_0603_batch05_queue import reviewed_recipe as samsung_cap_05_recipe, EVIDENCE as SAMSUNG_CAP_05_EVIDENCE
from kicad_agents.display_render_samsung_0805_batch01_queue import reviewed_recipe as samsung_cap_0805_recipe, EVIDENCE as SAMSUNG_CAP_0805_EVIDENCE
from kicad_agents.display_render_samsung_0805_batch02_queue import reviewed_recipe as samsung_cap_0805_02_recipe, EVIDENCE as SAMSUNG_CAP_0805_02_EVIDENCE
from kicad_agents.display_render_samsung_0805_thin_batch01_queue import reviewed_recipe as samsung_cap_0805_thin_recipe, EVIDENCE as SAMSUNG_CAP_0805_THIN_EVIDENCE
from kicad_agents.display_render_samsung_0805_065_batch01_queue import reviewed_recipe as samsung_cap_0805_065_recipe, EVIDENCE as SAMSUNG_CAP_0805_065_EVIDENCE
from kicad_agents.display_render_samsung_0805_065_batch02_queue import reviewed_recipe as samsung_cap_0805_065_02_recipe, EVIDENCE as SAMSUNG_CAP_0805_065_02_EVIDENCE
from kicad_agents.display_render_fenghua_0805_batch01_queue import reviewed_recipe as fenghua_cap_0805_recipe, EVIDENCE as FENGHUA_CAP_0805_EVIDENCE
from kicad_agents.display_render_fenghua_0805_batch02_queue import reviewed_recipe as fenghua_cap_0805_02_recipe, EVIDENCE as FENGHUA_CAP_0805_02_EVIDENCE
from kicad_agents.display_render_fenghua_0805_batch03_queue import reviewed_recipe as fenghua_cap_0805_03_recipe, EVIDENCE as FENGHUA_CAP_0805_03_EVIDENCE
from kicad_agents.display_render_fenghua_0805_batch04_queue import reviewed_recipe as fenghua_cap_0805_04_recipe, EVIDENCE as FENGHUA_CAP_0805_04_EVIDENCE
from kicad_agents.display_render_fenghua_0805_batch05_queue import reviewed_recipe as fenghua_cap_0805_05_recipe, EVIDENCE as FENGHUA_CAP_0805_05_EVIDENCE
from kicad_agents.display_render_fenghua_0805_batch06_queue import reviewed_recipe as fenghua_cap_0805_06_recipe, EVIDENCE as FENGHUA_CAP_0805_06_EVIDENCE
from kicad_agents.display_render_fenghua_1206_batch01_queue import reviewed_recipe as fenghua_cap_1206_recipe, EVIDENCE as FENGHUA_CAP_1206_EVIDENCE
from kicad_agents.display_render_fenghua_1206_batch02_queue import reviewed_recipe as fenghua_cap_1206_02_recipe, EVIDENCE as FENGHUA_CAP_1206_02_EVIDENCE
from kicad_agents.display_render_fenghua_1206_batch03_queue import reviewed_recipe as fenghua_cap_1206_03_recipe, EVIDENCE as FENGHUA_CAP_1206_03_EVIDENCE
from kicad_agents.display_render_fenghua_1206_secondary_full_height_01_queue import reviewed_recipe as fenghua_cap_1206_secondary_full_height_01_recipe, EVIDENCE as FENGHUA_CAP_1206_SECONDARY_FULL_HEIGHT_01_EVIDENCE
from kicad_agents.display_render_fenghua_1206_secondary_20pf_queue import reviewed_recipe as fenghua_cap_1206_secondary_20pf_recipe, EVIDENCE as FENGHUA_CAP_1206_SECONDARY_20PF_EVIDENCE
from kicad_agents.display_render_fenghua_1206_secondary_y5v_full_height_queue import reviewed_recipe as fenghua_cap_1206_secondary_y5v_full_height_recipe, EVIDENCE as FENGHUA_CAP_1206_SECONDARY_Y5V_FULL_HEIGHT_EVIDENCE
from kicad_agents.display_render_fenghua_1206_secondary_full_height_03_queue import reviewed_recipe as fenghua_cap_1206_secondary_full_height_03_recipe, EVIDENCE as FENGHUA_CAP_1206_SECONDARY_FULL_HEIGHT_03_EVIDENCE
from kicad_agents.display_render_fenghua_1206_secondary_low_c0g_queue import reviewed_recipe as fenghua_cap_1206_secondary_low_c0g_recipe, EVIDENCE as FENGHUA_CAP_1206_SECONDARY_LOW_C0G_EVIDENCE
from kicad_agents.display_render_fenghua_1206_secondary_mixed_heights_queue import reviewed_recipe as fenghua_cap_1206_secondary_mixed_heights_recipe, EVIDENCE as FENGHUA_CAP_1206_SECONDARY_MIXED_HEIGHTS_EVIDENCE
from kicad_agents.display_render_fenghua_1206_secondary_full_height_02_queue import reviewed_recipe as fenghua_cap_1206_secondary_full_height_02_recipe, EVIDENCE as FENGHUA_CAP_1206_SECONDARY_FULL_HEIGHT_02_EVIDENCE
from kicad_agents.display_render_samsung_1206_batch01_queue import reviewed_recipe as samsung_cap_1206_recipe, EVIDENCE as SAMSUNG_CAP_1206_EVIDENCE
from kicad_agents.display_render_fenghua_1206_4u7_queue import reviewed_recipe as fenghua_cap_1206_4u7_recipe, EVIDENCE as FENGHUA_CAP_1206_4U7_EVIDENCE
from kicad_agents.display_render_1206_125_batch01_queue import reviewed_recipe as cap_1206_125_recipe, EVIDENCE as CAP_1206_125_EVIDENCE
from kicad_agents.display_render_fenghua_0603_batch03_queue import reviewed_recipe as fenghua_cap_0603_03_recipe, EVIDENCE as FENGHUA_CAP_0603_03_EVIDENCE
from kicad_agents.display_render_fenghua_0603_batch04_queue import reviewed_recipe as fenghua_cap_0603_04_recipe, EVIDENCE as FENGHUA_CAP_0603_04_EVIDENCE
from kicad_agents.display_render_fenghua_0603_batch05_queue import reviewed_recipe as fenghua_cap_0603_05_recipe, EVIDENCE as FENGHUA_CAP_0603_05_EVIDENCE
from kicad_agents.display_render_fenghua_1206_2n2_queue import reviewed_recipe as fenghua_cap_1206_2n2_recipe, EVIDENCE as FENGHUA_CAP_1206_2N2_EVIDENCE
from kicad_agents.display_render_fenghua_0402_batch01_queue import reviewed_recipe as fenghua_cap_0402_recipe, EVIDENCE as FENGHUA_CAP_0402_EVIDENCE
from kicad_agents.display_render_fenghua_0402_batch02_queue import reviewed_recipe as fenghua_cap_0402_02_recipe, EVIDENCE as FENGHUA_CAP_0402_02_EVIDENCE
from kicad_agents.display_render_fenghua_0402_batch03_queue import reviewed_recipe as fenghua_cap_0402_03_recipe, EVIDENCE as FENGHUA_CAP_0402_03_EVIDENCE
from kicad_agents.display_render_fenghua_0402_batch04_queue import reviewed_recipe as fenghua_cap_0402_04_recipe, EVIDENCE as FENGHUA_CAP_0402_04_EVIDENCE
from kicad_agents.display_render_fenghua_0402_batch05_queue import reviewed_recipe as fenghua_cap_0402_05_recipe, EVIDENCE as FENGHUA_CAP_0402_05_EVIDENCE
from kicad_agents.display_render_fenghua_0402_cog_secondary_queue import reviewed_recipe as fenghua_cap_0402_cog_sec_recipe, EVIDENCE as FENGHUA_CAP_0402_COG_SEC_EVIDENCE
from kicad_agents.display_render_fenghua_0402_cog_secondary_batch02_queue import reviewed_recipe as fenghua_cap_0402_cog_sec02_recipe, EVIDENCE as FENGHUA_CAP_0402_COG_SEC02_EVIDENCE
from kicad_agents.display_render_fenghua_0402_cog_secondary_batch03_queue import reviewed_recipe as fenghua_cap_0402_cog_sec03_recipe, EVIDENCE as FENGHUA_CAP_0402_COG_SEC03_EVIDENCE
from kicad_agents.display_render_fenghua_0402_cog_secondary_batch04_queue import reviewed_recipe as fenghua_cap_0402_cog_sec04_recipe, EVIDENCE as FENGHUA_CAP_0402_COG_SEC04_EVIDENCE
from kicad_agents.display_render_fenghua_0402_680pf_queue import reviewed_recipe as fenghua_cap_0402_680_recipe, EVIDENCE as FENGHUA_CAP_680_EVIDENCE
from kicad_agents.display_render_fenghua_0402_4n7_queue import reviewed_recipe as fenghua_cap_0402_4n7_recipe, EVIDENCE as FENGHUA_CAP_0402_4N7_EVIDENCE
from kicad_agents.display_render_fenghua_0402_150_220_queue import reviewed_recipe as fenghua_cap_0402_150_220_recipe, EVIDENCE as FENGHUA_CAP_0402_150_220_EVIDENCE
from kicad_agents.display_render_fenghua_0402_secondary_next_queue import reviewed_recipe as fenghua_cap_0402_sec_recipe, PARTS as FENGHUA_CAP_0402_SEC_PARTS, EVIDENCE as FENGHUA_CAP_SEC_EVIDENCE
from kicad_agents.display_render_fenghua_0603_secondary_next_queue import reviewed_recipe as fenghua_cap_0603_sec_recipe
from kicad_agents.display_render_fenghua_0603_secondary_batch02_queue import reviewed_recipe as fenghua_cap_0603_sec02_recipe, EVIDENCE as FENGHUA_CAP_0603_SEC02_EVIDENCE
from kicad_agents.display_render_fenghua_0603_secondary_batch03_queue import reviewed_recipe as fenghua_cap_0603_sec03_recipe, EVIDENCE as FENGHUA_CAP_0603_SEC03_EVIDENCE
from kicad_agents.display_render_fenghua_0603_secondary_batch04_queue import reviewed_recipe as fenghua_cap_0603_sec04_recipe, EVIDENCE as FENGHUA_CAP_0603_SEC04_EVIDENCE
from kicad_agents.display_render_fenghua_0603_secondary_batch05_queue import reviewed_recipe as fenghua_cap_0603_sec05_recipe, EVIDENCE as FENGHUA_CAP_0603_SEC05_EVIDENCE
from kicad_agents.display_render_fenghua_0603_secondary_batch06_queue import reviewed_recipe as fenghua_cap_0603_sec06_recipe, EVIDENCE as FENGHUA_CAP_0603_SEC06_EVIDENCE
from kicad_agents.display_render_fenghua_0603_secondary_batch07_queue import reviewed_recipe as fenghua_cap_0603_sec07_recipe, EVIDENCE as FENGHUA_CAP_0603_SEC07_EVIDENCE
from kicad_agents.display_render_fenghua_0402_y5v_secondary_queue import reviewed_recipe as fenghua_cap_0402_y5v_recipe, PARTS as FENGHUA_CAP_0402_Y5V_PARTS, EVIDENCE as FENGHUA_CAP_Y5V_EVIDENCE
from kicad_agents.display_render_fenghua_0603_y5v_secondary_queue import reviewed_recipe as fenghua_cap_0603_y5v_recipe
from kicad_agents.display_render_fenghua_0603_y5v_batch02_queue import reviewed_recipe as fenghua_cap_0603_y5v_33_recipe, EVIDENCE as FENGHUA_CAP_0603_Y5V_33_EVIDENCE
from kicad_agents.display_render_fenghua_0603_30pf_queue import reviewed_recipe as fenghua_cap_0603_30pf_recipe, EVIDENCE as FENGHUA_CAP_0603_30PF_EVIDENCE
from kicad_agents.display_render_fenghua_0603_16_36pf_queue import reviewed_recipe as fenghua_cap_0603_16_36pf_recipe, EVIDENCE as FENGHUA_CAP_0603_16_36PF_EVIDENCE
from kicad_agents.display_render_fenghua_0603_12_75pf_queue import reviewed_recipe as fenghua_cap_0603_12_75pf_recipe, EVIDENCE as FENGHUA_CAP_0603_12_75PF_EVIDENCE
from kicad_agents.display_render_fenghua_0603_25_39_560pf_queue import reviewed_recipe as fenghua_cap_0603_25_39_560pf_recipe, EVIDENCE as FENGHUA_CAP_0603_25_39_560PF_EVIDENCE
from kicad_agents.display_render_fenghua_0603_x7r_additional_queue import reviewed_recipe as fenghua_cap_0603_x7r_additional_recipe, EVIDENCE as FENGHUA_CAP_0603_X7R_ADDITIONAL_EVIDENCE
from kicad_agents.display_render_fenghua_0603_last_identified_queue import reviewed_recipe as fenghua_cap_0603_last_identified_recipe, EVIDENCE as FENGHUA_CAP_0603_LAST_IDENTIFIED_EVIDENCE
from kicad_agents.display_render_fenghua_0402_low_c0g_queue import reviewed_recipe as fenghua_cap_0402_low_c0g_recipe, EVIDENCE as FENGHUA_CAP_0402_LOW_C0G_EVIDENCE
from kicad_agents.display_render_yageo_0402_120pf_queue import reviewed_recipe as yageo_cap_0402_120pf_recipe, EVIDENCE as YAGEO_CAP_0402_120PF_EVIDENCE
from kicad_agents.display_render_samsung_0805_c0g_1nf_queue import reviewed_recipe as samsung_cap_0805_c0g_1nf_recipe, EVIDENCE as SAMSUNG_CAP_0805_C0G_1NF_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_x7r_queue import reviewed_recipe as fenghua_cap_0805_assumed_x7r_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_X7R_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_c0g_01_queue import reviewed_recipe as fenghua_cap_0805_assumed_c0g_01_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_C0G_01_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_low_c0g_01_queue import reviewed_recipe as fenghua_cap_0805_assumed_low_c0g_01_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_LOW_C0G_01_EVIDENCE
from kicad_agents.display_render_fenghua_0805_low_c0g_full_height_queue import reviewed_recipe as fenghua_cap_0805_low_c0g_full_height_recipe, EVIDENCE as FENGHUA_CAP_0805_LOW_C0G_FULL_HEIGHT_EVIDENCE
from kicad_agents.display_render_fenghua_0805_c0g_height_review_02_queue import reviewed_recipe as fenghua_cap_0805_c0g_height_review_02_recipe, EVIDENCE as FENGHUA_CAP_0805_C0G_HEIGHT_REVIEW_02_EVIDENCE
from kicad_agents.display_render_fenghua_0805_c0g_height_review_03_queue import reviewed_recipe as fenghua_cap_0805_c0g_height_review_03_recipe, EVIDENCE as FENGHUA_CAP_0805_C0G_HEIGHT_REVIEW_03_EVIDENCE
from kicad_agents.display_render_fenghua_0805_x7r_height_review_02_queue import reviewed_recipe as fenghua_cap_0805_x7r_height_review_02_recipe, EVIDENCE as FENGHUA_CAP_0805_X7R_HEIGHT_REVIEW_02_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_low_c0g_04_queue import reviewed_recipe as fenghua_cap_0805_assumed_low_c0g_04_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_LOW_C0G_04_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_low_c0g_03_queue import reviewed_recipe as fenghua_cap_0805_assumed_low_c0g_03_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_LOW_C0G_03_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_low_c0g_02_queue import reviewed_recipe as fenghua_cap_0805_assumed_low_c0g_02_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_LOW_C0G_02_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_c0g_03_queue import reviewed_recipe as fenghua_cap_0805_assumed_c0g_03_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_C0G_03_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_c0g_02_queue import reviewed_recipe as fenghua_cap_0805_assumed_c0g_02_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_C0G_02_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_y5v_01_queue import reviewed_recipe as fenghua_cap_0805_assumed_y5v_01_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_Y5V_01_EVIDENCE
from kicad_agents.display_render_fenghua_0805_500pf_queue import reviewed_recipe as fenghua_cap_0805_500pf_recipe, EVIDENCE as FENGHUA_CAP_0805_500PF_EVIDENCE
from kicad_agents.display_render_fenghua_0805_x7r_1_25_queue import reviewed_recipe as fenghua_cap_0805_x7r_1_25_recipe, EVIDENCE as FENGHUA_CAP_0805_X7R_1_25_EVIDENCE
from kicad_agents.display_render_fenghua_0805_y5v_full_height_queue import reviewed_recipe as fenghua_cap_0805_y5v_full_height_recipe, EVIDENCE as FENGHUA_CAP_0805_Y5V_FULL_HEIGHT_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_x7r_03_queue import reviewed_recipe as fenghua_cap_0805_assumed_x7r_03_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_X7R_03_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_x7r_05_queue import reviewed_recipe as fenghua_cap_0805_assumed_x7r_05_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_X7R_05_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_x7r_04_queue import reviewed_recipe as fenghua_cap_0805_assumed_x7r_04_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_X7R_04_EVIDENCE
from kicad_agents.display_render_fenghua_0805_assumed_x7r_02_queue import reviewed_recipe as fenghua_cap_0805_assumed_x7r_02_recipe, EVIDENCE as FENGHUA_CAP_0805_ASSUMED_X7R_02_EVIDENCE
from kicad_agents.display_render_samsung_0805_y5v_1uf_queue import reviewed_recipe as samsung_cap_0805_y5v_1uf_recipe, EVIDENCE as SAMSUNG_CAP_0805_Y5V_1UF_EVIDENCE
from kicad_agents.display_render_yageo_0805_100nf_50v_queue import reviewed_recipe as yageo_cap_0805_100nf_50v_recipe, EVIDENCE as YAGEO_CAP_0805_100NF_50V_EVIDENCE, PART as YAGEO_CAP_0805_100NF_50V_PART
from kicad_agents.display_render_fenghua_0402_last_mixed_queue import reviewed_recipe as fenghua_cap_0402_last_mixed_recipe, EVIDENCE as FENGHUA_CAP_0402_LAST_MIXED_EVIDENCE
from kicad_agents.display_render_fenghua_0402_x7r_values_queue import reviewed_recipe as fenghua_cap_0402_x7r_values_recipe, EVIDENCE as FENGHUA_CAP_0402_X7R_VALUES_EVIDENCE
from kicad_agents.display_render_fenghua_0603_fractional_c0g_queue import reviewed_recipe as fenghua_cap_0603_fractional_c0g_recipe, EVIDENCE as FENGHUA_CAP_0603_FRACTIONAL_C0G_EVIDENCE
from kicad_agents.display_render_fenghua_0603_mixed_values_queue import reviewed_recipe as fenghua_cap_0603_mixed_values_recipe, EVIDENCE as FENGHUA_CAP_0603_MIXED_VALUES_EVIDENCE
from kicad_agents.display_render_fenghua_0603_y5v_values_queue import reviewed_recipe as fenghua_cap_0603_y5v_values_recipe, EVIDENCE as FENGHUA_CAP_0603_Y5V_VALUES_EVIDENCE
from kicad_agents.display_render_murata_0805_10uf_50v_queue import reviewed_recipe as murata_cap_0805_10uf_50v_recipe, EVIDENCE as MURATA_CAP_0805_10UF_50V_EVIDENCE
from kicad_agents.display_render_fenghua_0603_25v_queue import reviewed_recipe as fenghua_cap_0603_25v_recipe, EVIDENCE as FENGHUA_CAP_0603_25V_EVIDENCE
from kicad_agents.display_render_fenghua_0603_1p5_4p7_queue import reviewed_recipe as fenghua_cap_0603_1p5_4p7_recipe, EVIDENCE as FENGHUA_CAP_0603_1P5_4P7_EVIDENCE
from kicad_agents.display_render_fenghua_0805_12nf_secondary_queue import reviewed_recipe as fenghua_cap_0805_12nf_sec_recipe, EVIDENCE as FENGHUA_CAP_0805_12NF_SEC_EVIDENCE
from kicad_agents.display_render_fenghua_0805_1n5_secondary_queue import reviewed_recipe as fenghua_cap_0805_1n5_sec_recipe, PART as FENGHUA_CAP_0805_1N5, EVIDENCE as FENGHUA_CAP_0603_0805_NEXT_EVIDENCE
from kicad_agents.display_render_fenghua_0603_3p6_secondary_queue import reviewed_recipe as fenghua_cap_0603_3p6_sec_recipe
from kicad_agents.display_render_fenghua_0603_1p2_secondary_queue import reviewed_recipe as fenghua_cap_0603_1p2_sec_recipe, EVIDENCE as FENGHUA_CAP_0603_1P2_SEC_EVIDENCE
from kicad_agents.display_render_fenghua_0603_8p2_secondary_queue import reviewed_recipe as fenghua_cap_0603_8p2_sec_recipe, EVIDENCE as FENGHUA_CAP_0603_8P2_SEC_EVIDENCE
from kicad_agents.display_render_fenghua_1206_680pf_queue import reviewed_recipe as fenghua_cap_1206_680_recipe, PART as FENGHUA_CAP_1206_680_PART
from kicad_agents.display_render_samsung_0402_batch01_queue import reviewed_recipe as samsung_cap_0402_recipe, EVIDENCE as SAMSUNG_CAP_0402_EVIDENCE
from kicad_agents.display_render_samsung_0402_batch02_queue import reviewed_recipe as samsung_cap_0402_02_recipe, EVIDENCE as SAMSUNG_CAP_0402_02_EVIDENCE
from kicad_agents.display_render_samsung_0402_1n8_queue import reviewed_recipe as samsung_cap_0402_1n8_recipe, PARTS as SAMSUNG_CAP_0402_1N8_PARTS, EVIDENCE as SAMSUNG_CAP_NEXT_EVIDENCE
from kicad_agents.display_render_samsung_0603_batch06_queue import reviewed_recipe as samsung_cap_0603_06_recipe


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(part_id, source_id):
    if not all(re.fullmatch(r'electronic_[a-z0-9_]+', x) for x in (part_id, source_id)):
        raise ValueError('Use exact component IDs')
    recipes = json.loads((ROOT / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    studio = json.loads((ROOT / 'source_file/display_render/studio.json').read_text(encoding='utf-8'))
    recipe = recipes[part_id]
    source_folder = ROOT / 'parts' / source_id / 'data/display_render'
    source_file = source_folder / 'manifest.json'
    source = json.loads(source_file.read_text(encoding='utf-8'))
    evidence = recipe['marking']['evidence']
    path = (ROOT / evidence['file']).resolve()
    if not path.is_relative_to(ROOT.resolve()) or not path.is_file() or digest(path) != evidence['sha256']:
        raise ValueError('Target evidence is missing or has changed')
    record_path = ROOT / 'parts_source' / part_id / 'working.yaml'
    record = yaml.safe_load(record_path.read_text(encoding='utf-8')) or {}
    if evidence.get('file') == MURATA_CAP_0805_10UF_50V_EVIDENCE.as_posix():
        checked_recipe = murata_cap_0805_10uf_50v_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_NEXT_EVIDENCE.as_posix():
        fn = samsung_cap_0402_1n8_recipe if part_id in SAMSUNG_CAP_0402_1N8_PARTS else samsung_cap_0603_06_recipe
        checked_recipe = fn(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_0402_02_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_0402_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_0402_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_0402_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_8P2_SEC_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_8p2_sec_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_1P2_SEC_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_1p2_sec_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_0805_NEXT_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_1n5_sec_recipe(record, recipes, evidence['sha256']) if part_id == FENGHUA_CAP_0805_1N5 else fenghua_cap_0603_3p6_sec_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_12NF_SEC_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_12nf_sec_recipe(record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_1P5_4P7_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_1p5_4p7_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_Y5V_VALUES_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_y5v_values_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_MIXED_VALUES_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_mixed_values_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_FRACTIONAL_C0G_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_fractional_c0g_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_X7R_VALUES_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_x7r_values_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_LAST_MIXED_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_last_mixed_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_CAP_0805_100NF_50V_EVIDENCE.as_posix():
        if part_id != YAGEO_CAP_0805_100NF_50V_PART: raise ValueError('Unexpected part')
        checked_recipe = yageo_cap_0805_100nf_50v_recipe(record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_0805_Y5V_1UF_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_0805_y5v_1uf_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_X7R_02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_x7r_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_X7R_03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_x7r_03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_X7R_05_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_x7r_05_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_X7R_04_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_x7r_04_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_X7R_1_25_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_x7r_1_25_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_Y5V_FULL_HEIGHT_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_y5v_full_height_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_500PF_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_500pf_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_Y5V_01_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_y5v_01_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_C0G_02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_c0g_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_C0G_03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_c0g_03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_LOW_C0G_01_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_low_c0g_01_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_LOW_C0G_FULL_HEIGHT_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_low_c0g_full_height_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_C0G_HEIGHT_REVIEW_02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_c0g_height_review_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_C0G_HEIGHT_REVIEW_03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_c0g_height_review_03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_X7R_HEIGHT_REVIEW_02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_x7r_height_review_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_LOW_C0G_04_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_low_c0g_04_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_LOW_C0G_03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_low_c0g_03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_LOW_C0G_02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_low_c0g_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_C0G_01_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_c0g_01_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_ASSUMED_X7R_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_assumed_x7r_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_0805_C0G_1NF_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_0805_c0g_1nf_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_CAP_0402_120PF_EVIDENCE.as_posix():
        checked_recipe = yageo_cap_0402_120pf_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_LOW_C0G_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_low_c0g_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_LAST_IDENTIFIED_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_last_identified_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_X7R_ADDITIONAL_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_x7r_additional_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_25_39_560PF_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_25_39_560pf_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_12_75PF_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_12_75pf_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_16_36PF_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_16_36pf_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_30PF_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_30pf_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_Y5V_33_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_y5v_33_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_25V_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_25v_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_Y5V_EVIDENCE.as_posix():
        fn = fenghua_cap_0402_y5v_recipe if part_id in FENGHUA_CAP_0402_Y5V_PARTS else fenghua_cap_0603_y5v_recipe
        checked_recipe = fn(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_SEC07_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_sec07_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_SEC06_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_sec06_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_SEC05_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_sec05_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_SEC04_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_sec04_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_SEC03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_sec03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_SEC02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_sec02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_SEC_EVIDENCE.as_posix():
        fn = fenghua_cap_0402_sec_recipe if part_id in FENGHUA_CAP_0402_SEC_PARTS else fenghua_cap_0603_sec_recipe
        checked_recipe = fn(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_150_220_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_150_220_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_4N7_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_4n7_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_680_EVIDENCE.as_posix():
        if part_id == FENGHUA_CAP_1206_680_PART:
            checked_recipe = fenghua_cap_1206_680_recipe(record, recipes, evidence['sha256'])
        else:
            checked_recipe = fenghua_cap_0402_680_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_COG_SEC04_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_cog_sec04_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_COG_SEC03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_cog_sec03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_COG_SEC02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_cog_sec02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_COG_SEC_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_cog_sec_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_05_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_05_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_04_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_04_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0402_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0402_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_05_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_05_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_2N2_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_2n2_recipe(record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_04_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_04_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0603_03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0603_03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == CAP_1206_125_EVIDENCE.as_posix():
        checked_recipe = cap_1206_125_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_4U7_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_4u7_recipe(record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_1206_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_1206_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_SECONDARY_FULL_HEIGHT_01_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_secondary_full_height_01_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_SECONDARY_20PF_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_secondary_20pf_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_SECONDARY_Y5V_FULL_HEIGHT_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_secondary_y5v_full_height_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_SECONDARY_FULL_HEIGHT_03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_secondary_full_height_03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_SECONDARY_LOW_C0G_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_secondary_low_c0g_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_SECONDARY_MIXED_HEIGHTS_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_secondary_mixed_heights_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_SECONDARY_FULL_HEIGHT_02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_secondary_full_height_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_1206_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_1206_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_06_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_06_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_05_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_05_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_04_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_04_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_03_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_0805_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_0805_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_0805_065_02_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_0805_065_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_0805_065_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_0805_065_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_0805_THIN_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_0805_thin_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_0805_02_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_0805_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_0805_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_0805_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_02_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_05_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_05_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_CAP_EVIDENCE.as_posix():
        checked_recipe = fenghua_cap_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_04_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_04_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_03_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_03_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_02_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_02_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == SAMSUNG_CAP_EVIDENCE.as_posix():
        checked_recipe = samsung_cap_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FOJAN_5PCT_EVIDENCE.as_posix():
        ledger = json.loads((ROOT / FOJAN_5PCT_EVIDENCE).read_text(encoding='utf-8'))
        identities = {item['part_id']: item for item in ledger['records']}
        checked_recipe = fojan_5pct_recipe(part_id, record, recipes, evidence['sha256'], identities)
    elif evidence.get('file') == MULTI_0201_EVIDENCE.as_posix():
        checked_recipe = multi_0201_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_GENERIC_0402_EVIDENCE.as_posix():
        checked_recipe = yageo_generic_0402_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_GENERIC_EVIDENCE.as_posix():
        checked_recipe = yageo_generic_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_SMALL_SELECTED_EVIDENCE.as_posix():
        checked_recipe = yageo_small_selected_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_SELECTED_0402_EVIDENCE.as_posix():
        checked_recipe = yageo_selected_0402_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_SELECTED_EVIDENCE.as_posix():
        checked_recipe = yageo_selected_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_VISUAL_EVIDENCE.as_posix():
        checked_recipe = yageo_visual_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == YAGEO_AC_EVIDENCE.as_posix():
        checked_recipe = yageo_ac_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == FENGHUA_5PCT_EVIDENCE.as_posix():
        checked_recipe = fenghua_5pct_recipe(part_id, record, recipes, evidence['sha256'])
    elif evidence.get('file') == RALEC_SMALL_EVIDENCE.as_posix():
        checked_recipe = ralec_small_recipe(part_id, record, recipes, evidence['sha256'])
    elif recipe.get('represented_manufacturer') == 'UNI-ROYAL':
        checked_recipe = uniroyal_recipe(part_id, record, recipes[PILOT])
    elif recipe.get('represented_manufacturer') == 'FOJAN':
        if evidence.get('file') == FOJAN_LOW_EVIDENCE.as_posix():
            checked_recipe = fojan_low_recipe(part_id, record, recipes, evidence['sha256'])
        else:
            checked_recipe = fojan_recipe(part_id, record, recipes[PILOT], evidence['sha256'])
    elif recipe.get('represented_manufacturer') == 'YAGEO':
        checked_recipe = yageo_recipe(part_id, record, recipes[PILOT], evidence['sha256'])
    elif recipe.get('represented_manufacturer') == 'FH':
        checked_recipe = fenghua_recipe(part_id, record, recipes[PILOT], evidence['sha256'])
    else:
        raise ValueError('This supplier needs a reviewed source-record adapter')
    if recipe != checked_recipe:
        raise ValueError('Current part record does not match the reviewed recipe')
    target = copy.deepcopy(source)
    target.update(part_id=part_id, recipe=recipe,
                  recipe_sha256=hashlib.sha256(json.dumps(recipe, sort_keys=True).encode()).hexdigest())
    target['marking']['evidence_sha256'] = evidence['sha256']
    target['reused_image'] = {'source_part': source_id, 'source_manifest_sha256': digest(source_file),
                              'method': 'identical unmarked package, materials, studio and output'}
    target['input_fingerprint'] = hashlib.sha256(json.dumps(
        {'recipe': recipe, 'reuse': target['reused_image']}, sort_keys=True).encode()).hexdigest()
    if not reused_image_valid(target, recipe, studio):
        raise ValueError('Source image is damaged or does not match this visual recipe')
    destination = ROOT / 'parts' / part_id / 'data/display_render'
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise FileExistsError(f'Existing output preserved: {destination}')
    destination.mkdir(parents=True, exist_ok=True)
    for name in ('render.png', 'preview.webp'):
        shutil.copyfile(source_folder / name, destination / name)
    (destination / 'manifest.json').write_text(json.dumps(target, indent=2) + '\n', encoding='utf-8')
    print(f'Reused inspected {source_id} image for {part_id}; review and publish separately.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part_id')
    parser.add_argument('source_id')
    args = parser.parse_args()
    prepare(args.part_id, args.source_id)


if __name__ == '__main__':
    main()
