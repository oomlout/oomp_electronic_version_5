"""Deduplicate identical datasheet PDFs across ``parts_source``.

Many parts in a family (resistor values, capacitor values, JST connector
pin counts, ...) share byte-identical ``datasheet.pdf`` files.  For each
group of identical PDFs the script keeps a single copy in one canonical
folder (the alphabetically first member that has both a ``working.yaml``
and the PDF) and records ``oomp_datasheet_common_with: <canonical folder>``
in every other member's ``working.yaml``.

The ``working.yaml`` edit is done as a text insertion so the rest of the
file's formatting (as written by ``yaml.dump``) is untouched.

``working_oomp_populate`` calls ``collect_common_with_keys`` before
``write_extras`` (which rewrites each ``working.yaml`` from scratch) and
``restore_common_with_keys`` plus ``deduplicate`` after it, so the pointer
is re-derived on every populate run and persists between generations.
Existing keys that no longer match the canonical folder are re-pointed, so
canonical shifts stay consistent too.

Members without a ``working.yaml`` yet (folders created ahead of the next
``run_populate.py``) are left alone because there is nowhere to record the
pointer; the next populate run folds them in.
"""

import argparse
import hashlib
import os


PARTS_SOURCE_DIRECTORY = "parts_source"
DATASHEET_FILENAME = "datasheet.pdf"
COMMON_WITH_KEY = "oomp_datasheet_common_with"


def sha256_of_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as file_input:
        for block in iter(lambda: file_input.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def set_common_with_line(text, canonical_folder):
    """Insert, replace, or (with ``None``) remove the common-with key.

    The key is kept at its alphabetical position among the top-level keys
    written by ``yaml.dump``.
    """
    key = COMMON_WITH_KEY
    lines = text.splitlines()
    line_index = None
    insert_at = None
    for index, line in enumerate(lines):
        if not line or line[0].isspace() or line.startswith("#") or ":" not in line:
            continue
        line_key = line.split(":", 1)[0]
        if line_key == key:
            line_index = index
            break
        if insert_at is None and line_key > key:
            insert_at = index
    new_line = None if canonical_folder is None else f"{key}: {canonical_folder}"
    if line_index is not None:
        if new_line is None:
            del lines[line_index]
        else:
            lines[line_index] = new_line
        return "\n".join(lines) + "\n"
    if new_line is None:
        return text
    if insert_at is None:
        lines.append(new_line)
    else:
        lines.insert(insert_at, new_line)
    return "\n".join(lines) + "\n"


def insert_common_with_line(text, canonical_folder):
    return set_common_with_line(text, canonical_folder)


def find_duplicate_groups():
    groups = {}
    for entry in sorted(os.listdir(PARTS_SOURCE_DIRECTORY)):
        part_directory = os.path.join(PARTS_SOURCE_DIRECTORY, entry)
        if not os.path.isdir(part_directory):
            continue
        datasheet_path = os.path.join(part_directory, DATASHEET_FILENAME)
        if not os.path.isfile(datasheet_path):
            continue
        digest = sha256_of_file(datasheet_path)
        groups.setdefault(digest, []).append(entry)
    return {digest: members for digest, members in groups.items() if len(members) > 1}


def read_working_text(part_directory):
    working_path = os.path.join(part_directory, "working.yaml")
    if not os.path.isfile(working_path):
        return None
    with open(working_path, "r", encoding="utf-8") as file_input:
        return file_input.read()


def write_working_text(part_directory, text):
    working_path = os.path.join(part_directory, "working.yaml")
    with open(working_path, "w", encoding="utf-8", newline="") as file_output:
        file_output.write(text)


def collect_common_with_keys():
    """Snapshot every folder's ``oomp_datasheet_common_with`` value."""
    snapshot = {}
    for entry in sorted(os.listdir(PARTS_SOURCE_DIRECTORY)):
        part_directory = os.path.join(PARTS_SOURCE_DIRECTORY, entry)
        if not os.path.isdir(part_directory):
            continue
        text = read_working_text(part_directory)
        if text is None:
            continue
        for line in text.splitlines():
            if line.startswith(f"{COMMON_WITH_KEY}:"):
                snapshot[entry] = line.split(":", 1)[1].strip()
                break
    return snapshot


def restore_common_with_keys(snapshot, verbose=True):
    """Re-insert pointers that ``write_extras`` rewrote away.

    Only folders that lack their own ``datasheet.pdf`` are restored; a
    folder holding its own PDF is reconciled by ``deduplicate`` instead.
    """
    restored = 0
    for folder, canonical in sorted(snapshot.items()):
        part_directory = os.path.join(PARTS_SOURCE_DIRECTORY, folder)
        text = read_working_text(part_directory)
        if text is None or COMMON_WITH_KEY in text:
            continue
        if os.path.isfile(os.path.join(part_directory, DATASHEET_FILENAME)):
            continue
        if not os.path.isfile(os.path.join(PARTS_SOURCE_DIRECTORY, canonical, DATASHEET_FILENAME)):
            if verbose:
                print(f"  {folder}: kept unrestored, canonical {canonical} has no datasheet.pdf")
            continue
        write_working_text(part_directory, set_common_with_line(text, canonical))
        restored += 1
        if verbose:
            print(f"  {folder} -> {canonical} (restored)")
    if verbose:
        print(f"restored {restored} oomp_datasheet_common_with pointers")
    return restored


def deduplicate(dry_run=False, verbose=True):
    duplicate_groups = find_duplicate_groups()
    member_count = sum(len(members) for members in duplicate_groups.values())
    if verbose or dry_run:
        print(
            f"found {len(duplicate_groups)} duplicate groups covering "
            f"{member_count} parts"
        )

    removed = 0
    annotated = 0
    repointed = 0
    bytes_saved = 0
    skipped = []
    for members in duplicate_groups.values():
        has_working = {
            name: read_working_text(os.path.join(PARTS_SOURCE_DIRECTORY, name))
            for name in members
        }
        has_pdf = {
            name: os.path.isfile(os.path.join(PARTS_SOURCE_DIRECTORY, name, DATASHEET_FILENAME))
            for name in members
        }
        canonical = next(
            (name for name in members if has_working[name] is not None and has_pdf[name]),
            None,
        )
        if canonical is None:
            canonical = next((name for name in members if has_pdf[name]), None)
        if canonical is None:
            continue
        canonical_directory = os.path.join(PARTS_SOURCE_DIRECTORY, canonical)
        canonical_text = has_working[canonical]
        if canonical_text is not None and COMMON_WITH_KEY in canonical_text:
            # The keeper cannot point at another folder.
            updated = set_common_with_line(canonical_text, None)
            if not dry_run:
                write_working_text(canonical_directory, updated)
            annotated += 1
        for member in members:
            if member == canonical:
                continue
            member_directory = os.path.join(PARTS_SOURCE_DIRECTORY, member)
            text = has_working[member]
            if text is None:
                skipped.append(member)
                continue
            datasheet_path = os.path.join(member_directory, DATASHEET_FILENAME)
            datasheet_size = os.path.getsize(datasheet_path) if has_pdf[member] else 0
            updated = set_common_with_line(text, canonical)
            if updated != text:
                if not dry_run:
                    write_working_text(member_directory, updated)
                if COMMON_WITH_KEY in text:
                    repointed += 1
                else:
                    annotated += 1
            if has_pdf[member]:
                if not dry_run:
                    os.remove(datasheet_path)
                removed += 1
                bytes_saved += datasheet_size
            if verbose:
                state = "repointed" if COMMON_WITH_KEY in text and updated != text else "annotated"
                print(f"  {member} -> {canonical} ({state}, pdf removed: {has_pdf[member]})")

    if verbose or dry_run:
        print(f"removed {removed} duplicate datasheets ({bytes_saved} bytes)")
        print(f"annotated {annotated} working.yaml files")
        print(f"repointed {repointed} stale pointers")
        if skipped:
            print(f"left {len(skipped)} members untouched (no working.yaml yet)")
            if verbose:
                for member in skipped:
                    print(f"  {member}")
    return 0


def main(**kwargs):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="report what would change without deleting or editing files",
    )
    arguments = parser.parse_args()
    return deduplicate(dry_run=arguments.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
