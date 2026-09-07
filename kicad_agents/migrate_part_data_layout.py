"""Move generated part artifacts below parts/<id>/data."""

import argparse
import shutil
from pathlib import Path


ROOT_FILES = ["README.md", "working.yaml", "board_explorer.html"]


def _merge_directory(source_directory, destination_directory):
    destination_directory.mkdir(parents=True, exist_ok=True)
    for source_item in sorted(source_directory.iterdir(), key=lambda path: path.name.lower()):
        destination_item = destination_directory / source_item.name
        if source_item.is_dir() and not source_item.is_symlink():
            _merge_directory(source_item, destination_item)
            if not any(source_item.iterdir()):
                source_item.rmdir()
        else:
            destination_item.parent.mkdir(parents=True, exist_ok=True)
            if destination_item.exists():
                if source_item.read_bytes() == destination_item.read_bytes():
                    source_item.unlink()
                else:
                    raise FileExistsError(
                        f"Different files exist at {source_item} and {destination_item}; "
                        "both were preserved for review."
                    )
            else:
                shutil.move(str(source_item), str(destination_item))
    if source_directory.exists() and not any(source_directory.iterdir()):
        source_directory.rmdir()


def migrate_part_directory(part_directory, dry_run=False):
    part_directory = Path(part_directory).resolve()
    data_directory = part_directory / "data"
    move_names = []
    for item in sorted(part_directory.iterdir(), key=lambda path: path.name.lower()):
        if item.name in ROOT_FILES or item.name == "data":
            continue
        move_names.append(item.name)

    if dry_run or move_names == []:
        return move_names

    data_directory.mkdir(parents=True, exist_ok=True)
    for move_name in move_names:
        source_item = part_directory / move_name
        destination_item = data_directory / move_name
        if source_item.is_dir() and destination_item.is_dir():
            _merge_directory(source_item, destination_item)
        elif destination_item.exists():
            if source_item.is_file() and destination_item.is_file() and source_item.read_bytes() == destination_item.read_bytes():
                source_item.unlink()
            else:
                raise FileExistsError(f"Cannot merge {source_item} into existing {destination_item}")
        else:
            shutil.move(str(source_item), str(destination_item))
    return move_names


def migrate_parts(parts_directory="parts", dry_run=False):
    parts_directory = Path(parts_directory).resolve()
    migrated_parts = []
    moved_items = 0
    for part_directory in sorted(parts_directory.iterdir(), key=lambda path: path.name.lower()):
        if not part_directory.is_dir():
            continue
        move_names = migrate_part_directory(part_directory, dry_run=dry_run)
        if move_names != []:
            migrated_parts.append(part_directory.name)
            moved_items += len(move_names)
    return {
        "parts": len(migrated_parts),
        "items": moved_items,
        "part_ids": migrated_parts,
        "dry_run": dry_run,
    }


def main():
    parser = argparse.ArgumentParser(description="Move generated part artifacts into data directories.")
    parser.add_argument("--parts-dir", default="parts")
    parser.add_argument("--dry-run", action="store_true")
    arguments = parser.parse_args()
    result = migrate_parts(arguments.parts_dir, dry_run=arguments.dry_run)
    mode = "would move" if result["dry_run"] else "moved"
    print(f"{mode} {result['items']} root items in {result['parts']} part folders")


if __name__ == "__main__":
    main()
