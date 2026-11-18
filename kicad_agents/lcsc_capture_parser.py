"""Parse raw LCSC page captures into structured, ranked part options.

The browser saves a page with `document.documentElement.outerHTML` (the "raw
capture").  This module extracts the product table rows -- LCSC code,
manufacturer part number, manufacturer, stock count, description and product
URL -- from either

* a search page  (``https://www.lcsc.com/search?q=...``), or
* a category page (``https://www.lcsc.com/category/<id>.html?globalKeyword=...``)

capture, ranks the rows that are actually in stock, and reports the highest
stock listing per capture.

Command line use::

    python kicad_agents/lcsc_capture_parser.py <capture.html or directory>...
        [--json out.json]   # write the full parsed structure
        [--best]            # print one best (highest-stock) row per capture

The module is reusable: ``parse_capture(text)`` returns the row list for one
capture; ``best_row(rows)`` picks the highest-stock entry.
"""

import argparse
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup


def _clean(text):
    return re.sub(r"\s+", " ", text or "").strip()


def _row_texts(soup):
    """Yield the visible text of every product row in every table."""
    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            yield row


def parse_capture(html_text, source=""):
    """Extract ranked product rows from one raw LCSC page capture."""
    soup = BeautifulSoup(html_text, "lxml")
    rows = []
    seen_codes = set()
    for row in _row_texts(soup):
        text = _clean(row.get_text(" "))
        if not text:
            continue
        code_match = re.search(r"\b(C\d{4,9})\b", text)
        if not code_match:
            continue
        code = code_match.group(1)
        if code in seen_codes:
            continue
        stock_match = re.search(r"([\d,]+)\s*In Stock", text, re.IGNORECASE)
        in_stock = stock_match is not None
        stock = int(stock_match.group(1).replace(",", "")) if in_stock else 0
        if not in_stock and "Other Suppliers" not in text:
            # Rows without an "In Stock" marker on genuine tables are
            # non-stock or marketplace rows; keep them but flag availability.
            lead = re.search(r"([\d,]+)\s*Estimated lead time", text)
            if not lead:
                continue
        # The MPN precedes the LCSC code in the row text.
        mpn = ""
        mpn_match = re.search(r"([A-Za-z0-9][A-Za-z0-9./\-]{2,30})\s*" + re.escape(code), text)
        if mpn_match:
            mpn = mpn_match.group(1)
        manufacturer = ""
        # The manufacturer link follows the code cell; look for a known
        # "brand" link title pattern first, then fall back to a plain scan.
        brand_link = row.select_one('a[href*="brand-detail"]')
        if brand_link:
            manufacturer = _clean(brand_link.get_text(" "))
        if not manufacturer:
            after = text.split(code, 1)[-1]
            words = after.split()
            if words:
                manufacturer = words[0]
        # Description: use the longest cell that is not a packaging /
        # placeholder column ("Tape & Reel (TR)", "Cut Tape (CT)", "-").
        description = ""
        packaging = re.compile(r"tape|reel|tray|cut tape|^-$|^\d{4}$", re.IGNORECASE)
        cells = [_clean(cell.get_text(" ")) for cell in row.find_all("td")]
        candidates = [cell for cell in cells if len(cell) > 12 and not packaging.search(cell)]
        if candidates:
            description = max(candidates, key=len)[:160]
        url = ""
        link = row.select_one(f'a[href*="product-detail/{code}"]')
        if link:
            url = f"https://www.lcsc.com/product-detail/{code}.html"
        rows.append({
            "lcsc_code": code,
            "mpn": mpn,
            "manufacturer": manufacturer,
            "stock": stock,
            "in_stock": in_stock,
            "description": description,
            "url": url,
            "source": source,
        })
        seen_codes.add(code)
    return rows


def best_row(rows):
    """The highest-stock in-stock row, or None when nothing is in stock."""
    in_stock = [row for row in rows if row["in_stock"]]
    if not in_stock:
        return None
    return sorted(in_stock, key=lambda row: row["stock"], reverse=True)[0]


def top_rows(rows, count=3):
    in_stock = [row for row in rows if row["in_stock"]]
    return sorted(in_stock, key=lambda row: row["stock"], reverse=True)[:count]


def option_rows(rows, count=3):
    """Highest-stock rows that identify a real part (MPN + manufacturer).

    Unbranded marketplace listings without a manufacturer part number cannot
    populate `part_numbers_manufacturer`, so they are skipped.
    """
    usable = [row for row in rows if row["in_stock"] and row["mpn"] and row["manufacturer"]]
    return sorted(usable, key=lambda row: row["stock"], reverse=True)[:count]


def parse_paths(paths):
    """Parse every capture file; directories are scanned for *.html."""
    results = []
    for path_text in paths:
        path = Path(path_text)
        files = sorted(path.glob("*.html")) if path.is_dir() else [path]
        for capture in files:
            rows = parse_capture(capture.read_text(encoding="utf-8"), source=capture.stem)
            results.append({"capture": capture.name, "rows": rows})
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="capture files or directories")
    parser.add_argument("--json", dest="json_output", default="", help="write full parse to this file")
    parser.add_argument("--best", action="store_true", help="print the highest-stock row per capture")
    arguments = parser.parse_args()
    results = parse_paths(arguments.paths)
    if arguments.json_output:
        Path(arguments.json_output).write_text(
            json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8"
        )
    for result in results:
        best = best_row(result["rows"])
        summary = f"{result['capture']}: {len(result['rows'])} rows"
        if best:
            summary += f" | best {best['lcsc_code']} {best['mpn']} {best['manufacturer']} stock {best['stock']}"
        print(summary)
        if arguments.best:
            for row in top_rows(result["rows"]):
                print(f"    {row['lcsc_code']:>10}  stock {row['stock']:>12,}  "
                      f"{row['manufacturer']:<24} {row['mpn']:<28} {row['description'][:60]}")


if __name__ == "__main__":
    main()
