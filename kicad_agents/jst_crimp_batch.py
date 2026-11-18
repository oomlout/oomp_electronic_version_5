"""Prepare and build the JST SH, GH, PH and XH cable contacts and housings."""
import argparse

from kicad_agents.component_addition_agent import build_component, prepare_component_source
from working_oomp_populate_connector_jst_cable_data import FAMILIES, PARTS, SOURCE_ROOT, token
from working_oomp_populate_connector_crimp_data import MODEL_ASSETS


def evidence_record(row):
    return {
        "ledger_id": f"JST_CABLE_{token(row['mpn']).upper()}",
        "family": "connector", "package": row["taxonomy"]["taxonomy_3"],
        "part_id": row["id"], "pin_count": len(row["pins"]), "datasheet_required": True,
        "research": {
            "manufacturer": "JST", "manufacturer_part_number": row["mpn"],
            "lcsc_decision": "No distributor or assembly substitute assigned in this batch.",
            "product_url": row["product_url"], "datasheet_url": row["datasheet_url"],
            "browser_sources": [row["product_url"], row["datasheet_url"]],
            "evidence_notes": [
                f"Exact ordering code and nominal dimensions on JST catalogue page {row['pdf_page']}.",
                row["dimension_note"],
            ],
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "build"))
    parser.add_argument("selection", nargs="*", help="Exact MPNs, SH/GH/PH/XH, or all")
    args = parser.parse_args()
    names = {name.upper() for name in args.selection or ["all"]}
    choices = {row["mpn"] for row in PARTS} | {"ALL"} | {family.upper() for family in FAMILIES}
    if names - choices:
        parser.error(f"Unknown JST selection: {', '.join(sorted(names - choices))}")
    selected = [row for row in PARTS if names.intersection({"ALL", row["family"].upper(), row["mpn"]})]
    if args.mode == "prepare":
        # All reciprocal link targets need a source definition before any build.
        families = {row["family"] for row in selected}
        targets = [row for row in PARTS if row["family"] in families]
        for row in targets:
            prepare_component_source(evidence_record(row))
        print(f"Prepared {len(targets)} JST source definitions", flush=True)
        return
    for row in selected:
        if not all((SOURCE_ROOT / row["id"] / asset).is_file() for asset in MODEL_ASSETS):
            raise FileNotFoundError(f"Build the STEP and studio render for {row['mpn']} first")
        record = evidence_record(row)
        prepare_component_source(record)
        report, _ = build_component(record, regenerate_pngs=True, skip_populate=True, skip_shared_refresh=True)
        print(f"{row['mpn']}: {report['status']}", flush=True)


if __name__ == "__main__":
    main()
