from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import yaml
from bs4 import BeautifulSoup

from webserver.app import create_app
from webserver.services.electronics import component_details


class ElectronicsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.parts = root / "parts"
        for name, tier in (("basic_part", "basic"), ("extended_part", "extended"), ("preferred_part", "preferred_extended"), ("unknown_part", "")):
            directory = self.parts / name
            (directory / "data").mkdir(parents=True)
            data = {
                "name_proper": name, "taxonomy_1": "electronic", "taxonomy_2": "capacitor",
                "manufacturer": "FH", "part_number_manufacturer": "0402CG120J500NT",
                "part_number_lcsc": "C1547", "part_numbers_lcsc": [{"part_number": "C1547", "product_name": "12pF precision capacitor"}],
                "jlcpcb_selection": {"tier": tier, "stock_observed": 0, "verified_on": "2026-10-01", "ratings": {"Tolerance": "5%"}},
                "electrical": {"polarized": False, "rated_voltage": "50V"},
                "research_notes": ["Verified against manufacturer datasheet."],
                "part_page": {"diagrams": [{"title": "Assembly pinout", "svg": "data/working_svg_assembly_pins.svg"},
                                           {"title": "Missing drawing", "svg": "data/missing.svg"}]},
            }
            (directory / "working.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")
            for filename in ("label_oomp.svg", "working_svg_part_id.svg", "working_svg_assembly_pins.svg", "working_svg_square_pins.svg"):
                (directory / "data" / filename).write_text('<svg xmlns="http://www.w3.org/2000/svg" width="120" height="80"><rect width="100" height="60"/></svg>', encoding="utf-8")
            (directory / "data/datasheet.pdf").write_bytes(b"%PDF-1.4\n")
        self.app = create_app({"TESTING": True, "PARTS_DIR": self.parts, "PARTS_SOURCE_DIR": root / "parts_source"})
        self.client = self.app.test_client()

    def page(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return BeautifulSoup(response.data, "html.parser")

    def test_tiers_defaults_combinations_empty_and_navigation(self):
        for query, expected in (
            ("", 4), ("?tier=basic", 1), ("?tier=extended", 2),
            ("?tier=unknown", 1), ("?tier=basic&tier=extended", 3),
            ("?tier_filter=1", 0), ("?tier=invalid", 0),
        ):
            with self.subTest(query=query):
                page = self.page("/explore" + query)
                self.assertEqual(len(page.select(".part-card")), expected)
        page = self.page("/explore?tier=extended&q=0402&search_fields=component&sort=id&taxonomy_1=electronic")
        self.assertEqual(len(page.select(".part-card")), 2)
        for link in page.select(".taxonomy-option, .taxonomy-panel__selected a"):
            params = parse_qs(urlsplit(link["href"]).query)
            self.assertEqual(params["tier"], ["extended"])
            self.assertEqual(params["q"], ["0402"])
            self.assertEqual(params["sort"], ["id"])

    def test_search_supplier_codes_names_and_ratings(self):
        for query in ("C1547", "0402CG120J500NT", "precision capacitor", "50V"):
            page = self.page("/explore?q=" + query)
            self.assertEqual(len(page.select(".part-card")), 4)

    def test_detail_labels_gallery_metadata_and_viewer_targets(self):
        page = self.page("/parts/basic_part")
        labels = page.select(".file-tree--labels .file-list__primary > a")
        self.assertEqual(len(labels), 2)
        self.assertIn("label_oomp.svg", labels[0]["href"])
        self.assertLess(str(page).index("Label SVGs"), str(page).index("Other files"))
        self.assertEqual(len(page.select(".diagram-card")), 1)
        self.assertNotIn("Missing drawing", page.select_one(".diagram-gallery").get_text())
        self.assertIn("FH", page.get_text())
        self.assertIn("12pF precision capacitor", page.get_text())
        self.assertIn("2026-10-01", page.get_text())
        self.assertIn("No", page.get_text())
        self.assertIn("Stock at verification", page.get_text())
        self.assertTrue(page.select_one('a[href="https://www.lcsc.com/product-detail/C1547.html"]'))
        self.assertTrue(page.select_one('a[href="/parts/basic_part/data/datasheet.pdf"]'))
        image = page.select_one(".detail-preview")
        self.assertIn("working_svg_square_pins.svg", image["src"])
        payload = self.client.get("/parts/basic_part/viewer-data").get_json()
        for link in page.select(".diagram-card a, .file-tree--labels .file-list__primary > a"):
            item = payload["items"][int(link["data-image-index"])]
            self.assertEqual(link["href"], item["originalUrl"])
            response = self.client.get(link["href"])
            self.assertEqual(response.status_code, 200)
            response.close()

    def test_malformed_optional_metadata_and_unsafe_links(self):
        details = component_details({"part_page": None, "jlcpcb_selection": [], "distributors": [None, {"title": "Bad", "url": "javascript:alert(1)"}], "product_url": "file:///private"})
        self.assertEqual(details["links"], [])
        self.assertEqual(details["tier"], "unknown")
        self.assertEqual(component_details({"jlcpcb_selection": {"tier": "preferred_extended"}})["tier_label"], "Preferred Extended")


if __name__ == "__main__":
    unittest.main()
